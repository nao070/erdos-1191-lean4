#!/usr/bin/env python3
"""Restore verified mathematical research from a private GitHub archive.

Requires Python 3 and an authenticated GitHub CLI (`gh auth login`).
No original Mac paths are overwritten: use an empty destination directory.
"""
import argparse
import base64
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import urllib.request

API = 'https://api.github.com'
ORIGINAL_HOME = Path.home()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', help='List datasets without restoring')
    parser.add_argument('--dataset', action='append', help='Dataset label to restore; repeat to select several')
    parser.add_argument('--destination', default='math-restored', help='Empty restoration destination')
    parser.add_argument('--repo', help='GitHub owner/repository; defaults to the current cloned repository')
    args = parser.parse_args()
    REPO = args.repo or json.loads(subprocess.check_output(
        ['gh', 'repo', 'view', '--json', 'nameWithOwner'], text=True))['nameWithOwner']
    token = subprocess.check_output(['gh', 'auth', 'token'], text=True).strip()

    def fetch(path, binary=False):
        req = urllib.request.Request(API + path, headers={
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/octet-stream' if binary else 'application/vnd.github+json',
            'User-Agent': 'Verified-Math-Restore', 'X-GitHub-Api-Version': '2022-11-28'})
        return urllib.request.urlopen(req, timeout=120)

    def get_json(path):
        with fetch(path) as response:
            return json.load(response)

    def manifest(item):
        asset = item['manifest_asset']
        with fetch(f'/repos/{REPO}/releases/assets/{asset["id"]}', True) as response:
            data = response.read()
        if len(data) != asset['size'] or 'sha256:' + hashlib.sha256(data).hexdigest() != asset['digest']:
            raise RuntimeError('Manifest checksum mismatch')
        return json.loads(data)

    item = get_json(f'/repos/{REPO}/contents/archive-index.json')
    index = json.loads(base64.b64decode(item['content']))
    datasets = [d for d in index['datasets'] if d.get('verified')]
    if args.list:
        for data in datasets:
            print(data['label'], f'{data["logical_bytes"] / 1e9:.3f} GB', 'verified')
            for path in data['sources']:
                print('  ', path)
        return
    wanted_labels = set(args.dataset or [d['label'] for d in datasets])
    known_labels = {d['label'] for d in datasets}
    if wanted_labels - known_labels:
        raise RuntimeError('Unknown dataset: ' + ', '.join(sorted(wanted_labels - known_labels)))
    destination = Path(args.destination).expanduser().resolve()
    if destination.exists() and any(destination.iterdir()):
        raise RuntimeError('Destination must be empty; original paths will not be overwritten')
    destination.mkdir(parents=True, exist_ok=True)
    manifests = {d['dataset_id']: manifest(d) for d in datasets}
    locations = {}
    wanted = {}
    directories, links, file_metadata = [], [], []
    for data in manifests.values():
        locations.update(data['new_objects'])
        if data['label'] not in wanted_labels:
            continue
        for record in data['records']:
            original = Path(record['source'])
            relative_root = original if index.get('schema') == 2 else original.relative_to(ORIGINAL_HOME)
            for name, entry in record['entries'].items():
                relative = relative_root if name == '.' else relative_root / name
                if '..' in relative.parts or relative.is_absolute():
                    raise RuntimeError('Unsafe archived path')
                target = destination / relative
                if entry['type'] == 'directory':
                    directories.append((target, entry))
                elif entry['type'] == 'symlink':
                    links.append((target, entry))
                elif entry['type'] == 'file':
                    wanted.setdefault(entry['sha256'], []).append((target, entry))
                    file_metadata.append((target, entry))
                else:
                    raise RuntimeError('Unsupported manifest entry')
    for target, entry in sorted(directories, key=lambda pair: len(pair[0].parts)):
        target.mkdir(parents=True, exist_ok=True)

    class Parts(io.RawIOBase):
        def __init__(self, parts):
            self.parts = iter(parts)
            self.response = None
            self.asset = None

        def readable(self):
            return True

        def readinto(self, target):
            while True:
                if self.response is None:
                    try:
                        self.asset = next(self.parts)
                    except StopIteration:
                        return 0
                    self.response = fetch(f'/repos/{REPO}/releases/assets/{self.asset["id"]}', True)
                    self.hash = hashlib.sha256()
                    self.size = 0
                block = self.response.read(len(target))
                if block:
                    target[:len(block)] = block
                    self.hash.update(block)
                    self.size += len(block)
                    return len(block)
                self.response.close()
                self.response = None
                if self.size != self.asset['size'] or 'sha256:' + self.hash.hexdigest() != self.asset['digest']:
                    raise RuntimeError('Downloaded archive part checksum mismatch')

        def close(self):
            if self.response:
                self.response.close()
            super().close()

    needed_archives = {locations[digest]['dataset_id'] for digest in wanted}
    restored = set()
    for dataset_id in sorted(needed_archives):
        data = manifests[dataset_id]
        print('Downloading and verifying:', data['label'], flush=True)
        with io.BufferedReader(Parts(data['parts']), buffer_size=1024 * 1024) as stream:
            with tarfile.open(fileobj=stream, mode='r|gz') as tar:
                for member in tar:
                    if not member.isfile() or not member.name.startswith('objects/'):
                        raise RuntimeError('Unexpected archive member')
                    digest = member.name.split('/', 1)[1]
                    content = tar.extractfile(member)
                    targets = wanted.get(digest, [])
                    output = None
                    if targets:
                        primary = targets[0][0]
                        primary.parent.mkdir(parents=True, exist_ok=True)
                        output = open(primary, 'xb')
                    h = hashlib.sha256()
                    try:
                        for block in iter(lambda: content.read(4 * 1024 * 1024), b''):
                            h.update(block)
                            if output:
                                output.write(block)
                    finally:
                        if output:
                            output.close()
                    if h.hexdigest() != digest:
                        raise RuntimeError('Archived file checksum mismatch')
                    if targets:
                        for target, entry in targets[1:]:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copyfile(primary, target)
                        restored.add(digest)
            while stream.read(4 * 1024 * 1024):
                pass
    if restored != set(wanted):
        raise RuntimeError('Some files could not be restored')
    for target, entry in file_metadata:
        os.chmod(target, entry['mode'])
        os.utime(target, ns=(entry['mtime_ns'], entry['mtime_ns']))
    # Create symlinks only after writing regular files, avoiding writes through links.
    for target, entry in links:
        target.parent.mkdir(parents=True, exist_ok=True)
        os.symlink(entry['target'], target)
    for target, entry in sorted(directories, key=lambda pair: len(pair[0].parts), reverse=True):
        os.chmod(target, entry['mode'])
        os.utime(target, ns=(entry['mtime_ns'], entry['mtime_ns']))
    print('Verified restore complete:', destination)
    print('Regular files:', len(file_metadata), 'Symlinks:', len(links))


if __name__ == '__main__':
    main()

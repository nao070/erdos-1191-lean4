"""Package this unresolved research checkpoint, never a Q1 proof release.

Run only after writers have finished. No original evidence, dependency cache,
or user configuration is modified. The ZIP manifest binds its actual members.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent / "ERDOS1191_Q1_UNRESOLVED_CHECKPOINT_2026-09-05.zip"


def main() -> None:
    inputs = [ROOT / "RESEARCH_STATUS.md", ROOT / "OUTCOME.json"]
    inputs.extend(p for p in (ROOT / "research").rglob("*") if p.is_file())
    inputs.extend(p for p in (ROOT / "evidence").glob("*")
                  if p.is_file() and p.name != "checkpoint_zip.json")
    inputs.extend(p for p in (ROOT / "lean").glob("*") if p.is_file())
    for folder in [ROOT / "lean/Q1", ROOT / "lean/evidence"]:
        inputs.extend(p for p in folder.rglob("*") if p.is_file())
    inputs = sorted(set(inputs))
    assert all(p.is_relative_to(ROOT) for p in inputs)
    assert all(".lake" not in p.parts and not p.is_symlink() for p in inputs)
    blobs = {str(p.relative_to(ROOT)): p.read_bytes() for p in inputs}
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in blobs.items()}
    outcome = json.loads(blobs["OUTCOME.json"])
    assert outcome["status"] == "Q1_UNRESOLVED"
    assert outcome["resolution_theorem"] is None
    manifest = {
        "status": "Q1_UNRESOLVED",
        "scope": "Unfinished supporting research and Lean development; not a proof release",
        "files_sha256": hashes,
    }
    pending = OUTPUT.with_suffix(".zip.pending")
    with zipfile.ZipFile(pending, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in blobs.items():
            archive.writestr("Q1_UNRESOLVED_CHECKPOINT/" + name, data)
        archive.writestr("Q1_UNRESOLVED_CHECKPOINT/FILE_HASHES.json",
                         json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    with zipfile.ZipFile(pending) as archive:
        assert archive.testzip() is None
        for name, expected in hashes.items():
            assert hashlib.sha256(archive.read("Q1_UNRESOLVED_CHECKPOINT/" + name)).hexdigest() == expected
        assert len(archive.namelist()) == len(blobs) + 1
    pending.replace(OUTPUT)
    print(json.dumps({"status": "Q1_UNRESOLVED", "zip": str(OUTPUT),
                      "files": len(blobs) + 1, "bytes": OUTPUT.stat().st_size,
                      "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
                      "zip_integrity": "PASS", "member_hashes": "PASS",
                      "clean_release_rebuild": "NOT_RUN"}, ensure_ascii=False))


if __name__ == "__main__":
    main()

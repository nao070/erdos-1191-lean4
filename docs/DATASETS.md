# Dataset guide

Browse source files directly in [`research/mathematics/`](../research/mathematics/). Use the downloader for complete working snapshots and experimental results.

## Available collections

| Dataset label | File entries | Uncompressed content | Contents |
|---|---:|---:|---|
| `research-notes` | 59 | about 1.9 MB | Research notes and small project snapshots |
| `mathematics-workspaces` | 59,593 | about 2.95 GB | Complete mathematics workspace copies, notes, source code, and research guides |
| `lean-proof-samples` | 27 | about 32 KB | Small Lean examples and proof-development samples |
| `mathematics-downloads` | 66,051 | about 2.86 GB | Downloaded project packages and historical working snapshots |
| `additional-c143-experiments-and-references` | 543 | about 321 MB | C140–C143 experiments and supporting reference material |
| `erdos677-experiment-results` | Pending | about 24 GB | Search outputs and a persistent experiment index; transfer and verification are ongoing |

Sizes are decimal, approximate, and describe file contents rather than filesystem allocation. File-entry counts include repeated copies. Identical contents are stored once in a content-addressed archive. The inventory also contains an internal supplementary-object collection; the downloader resolves those objects automatically.

## Select one collection

```sh
python3 restore_math_archive.py --dataset research-notes --destination notes
```

Select several by repeating `--dataset`:

```sh
python3 restore_math_archive.py \
  --dataset research-notes \
  --dataset lean-proof-samples \
  --destination selected-research
```

Restore all currently verified collections:

```sh
python3 restore_math_archive.py --destination all-research
```

An empty destination is required. If a download fails, preserve any useful output, choose a new empty destination, and rerun the command. The script does not overwrite files outside the selected destination.

## Storage format

Release assets contain gzip-compressed tar streams divided into download parts, SHA-256-addressed file objects, and JSON manifests. The downloader validates each manifest, each download part, and each file. It automatically retrieves objects shared with other collections. Individual `.partNNNN` assets are not independent ZIP files.

Archive containers encountered during preparation were expanded. A stored ZIP or tar is therefore restored as a directory named `original-name.contents`. This makes the contained research files directly inspectable. Dependency caches, build outputs, original Git history, and original filesystem metadata are not reconstructed. Some paths use portable placeholders and need adapting before execution.

## Latest availability

Run `python3 restore_math_archive.py --list` or inspect [`archive-index.json`](../archive-index.json). Only datasets marked `verified` are offered for restoration. Existing verified collections remain usable while further data is being transferred.

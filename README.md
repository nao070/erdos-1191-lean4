# Mathematics Research Archive

Research notes, Lean 4 developments, and computational experiments in additive combinatorics, with a focus on Erdős problem #1191 and Sidon sets.

[Browse the research](research/mathematics/) · [Getting started](docs/GETTING_STARTED.md) · [Research status](docs/RESEARCH_STATUS.md) · [Datasets](docs/DATASETS.md)

## Start here

| What you want to do | Where to start |
|---|---|
| Understand the mathematical target and supporting results | [Erdős #1191: formulation and Lean developments](research/mathematics/q1_lean4_execution_2026-09-05/lean/README.md) |
| Explore a smaller finite formalization | [Finite Lean kernel](research/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/lean_kernel/README.md) |
| Read the research workflow and sources | [Source map](research/mathematics/SOURCE_MAP.md) |
| Download notes, experiments, or complete working snapshots | [Dataset guide](docs/DATASETS.md) |

**Research status:** this collection includes work in progress, supporting lemmas, and computational evidence. It does not establish a solution to Erdős problem #1191. See [research status](docs/RESEARCH_STATUS.md) for the scope of each development.

## Download a dataset

Python 3 is sufficient. No GitHub account or third-party Python packages are required.

```sh
git clone https://github.com/nao070/mathematics-research-archive.git
cd mathematics-research-archive
python3 restore_math_archive.py --list
python3 restore_math_archive.py --dataset research-notes --destination research-notes
```

For complete research workspaces:

```sh
python3 restore_math_archive.py --dataset mathematics-workspaces --destination workspaces
```

The downloader verifies SHA-256 checksums for manifests, download parts, and file contents. Use an empty destination directory. Shared archive objects are resolved automatically.

## Collection layout

```text
research/mathematics/      Browseable research notes and source code
docs/                     Entry points, dataset guide, and research status
restore_math_archive.py   Dataset downloader and integrity verifier
archive-index.json        Machine-readable inventory of verified datasets
```

More than 1,400 research source files are available directly in the repository. The dataset inventory currently includes 126,273 file entries, including historical snapshots and duplicate copies. The large Erdős #677 experiment dataset is still being transferred; it becomes available through the downloader after verification. [The inventory](archive-index.json) is the authoritative availability record.

## Reproduce and contribute

Lean projects retain their `lean-toolchain` and dependency manifests. Follow the README in the selected project and use its pinned environment. Generated dependencies and build outputs must be regenerated locally. Archived computations and previously recorded build results have not all been rerun for this publication.

See [getting started](docs/GETTING_STARTED.md) and [contribution guidelines](CONTRIBUTING.md). Licenses included with individual projects and reference materials apply to those materials; this archive does not assign a single license to the entire collection.

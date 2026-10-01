# Erdős #1191: Sidon Sets and Lean 4 Developments

Lean 4 formulations and supporting results for Erdős problem #1191 on Sidon sets, with finite formalizations, research notes, and computational experiments in additive combinatorics.

[Read the #1191 development](research/mathematics/q1_lean4_execution_2026-09-05/lean/README.md) · [Reproduce a Lean project](docs/GETTING_STARTED.md#try-the-finite-lean-kernel) · [Download datasets](docs/DATASETS.md)

**Status:** research in progress. The formal developments cover formulation bridges and supporting lemmas; they do not establish a solution to the full problem. [Scope and research status](docs/RESEARCH_STATUS.md).

## What you can explore

| What you want to do | Where to start |
|---|---|
| Read the precise Q1 statement and supporting declarations | [Q1 formulation and Lean developments](research/mathematics/q1_lean4_execution_2026-09-05/lean/README.md) — equivalent formulations, Sidon constraints, and finite supporting identities |
| Reproduce a smaller formalization | [Finite Lean kernel](research/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/lean_kernel/README.md) — prefix/scale identities, adjacent-epoch ledgers, and ownership accounting |
| Understand the research methods and references | [Source map](research/mathematics/SOURCE_MAP.md) |
| Inspect experiments or complete working snapshots | [Dataset guide](docs/DATASETS.md) and [browsable research sources](research/mathematics/) |

## Get the Lean source

```sh
git clone https://github.com/nao070/erdos-1191-lean4.git
cd erdos-1191-lean4
```

Start with the [Q1 development README](research/mathematics/q1_lean4_execution_2026-09-05/lean/README.md) for the target, supporting statements, and assumptions. For a short reproduction entry point, follow the [finite-kernel instructions](docs/GETTING_STARTED.md#try-the-finite-lean-kernel). Both Lean projects include their toolchain and dependency pins.

## Download a dataset

Python 3 is sufficient. No GitHub account or third-party Python packages are required.

```sh
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

More than 1,400 research source files are available directly in the repository. The dataset inventory currently includes 126,314 file entries, including historical snapshots and duplicate copies. The broader dataset collection also includes material from other research investigations. The Erdős #677 experiment dataset is available through the downloader, including its persistent search index. [The inventory](archive-index.json) is the authoritative availability record.

## Reproduce and contribute

Lean projects retain their `lean-toolchain` and dependency manifests. Follow the README in the selected project and use its pinned environment. Generated dependencies and build outputs must be regenerated locally. Archived computations and previously recorded build results have not all been rerun for this publication.

See [getting started](docs/GETTING_STARTED.md) and [contribution guidelines](CONTRIBUTING.md). Licenses included with individual projects and reference materials apply to those materials; this archive does not assign a single license to the entire collection.

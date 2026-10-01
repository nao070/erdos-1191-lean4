# Getting started with Erdős #1191 and Lean 4

## Read without installing anything

Begin with the [research status](RESEARCH_STATUS.md), then open one of these entry points:

- [Erdős #1191 target and Lean supporting declarations](../research/mathematics/q1_lean4_execution_2026-09-05/lean/README.md).
- [Finite algebra and bookkeeping kernel](../research/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/lean_kernel/README.md).
- [Research workflow source map](../research/mathematics/SOURCE_MAP.md).

Historical copies are retained for traceability. A filename containing “proof” or “verified” is not, by itself, evidence that the full research problem has been proved.

## Get the source code

```sh
git clone https://github.com/nao070/erdos-1191-lean4.git
cd erdos-1191-lean4
```

Alternatively, use GitHub's **Code → Download ZIP** to obtain the browsable source tree. Large experimental datasets are stored separately in release assets and are not included in that ZIP.

## Try the finite Lean kernel

The kernel README records Lean `leanprover/lean4:v4.33.0` and a pinned mathlib revision. With `elan` installed, run the project's documented commands:

```sh
cd research/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/lean_kernel
elan toolchain install leanprover/lean4:v4.33.0
lake update
lake build
lake env lean Erdos1191/AxiomAudit.lean
```

These commands reproduce the finite kernel, not a proof of the full Erdős problem. Inspect any local scripts before running them, and adapt machine-specific paths to your environment.

## Get experimental data

From the repository root, use Python 3:

```sh
python3 restore_math_archive.py --list
python3 restore_math_archive.py --dataset research-notes --destination notes
```

Use the [dataset guide](DATASETS.md) to choose a larger collection. Keep the destination empty, and allow enough disk space for the uncompressed data. No GitHub login is required for this public archive.

## Check a result

Use the exact project, toolchain, mathematical assumptions, and command associated with the result. Distinguish a Lean declaration accepted by its kernel from a numerical observation, a finite exhaustive search, and an informal argument. Record your environment and output when reporting a reproduction result.

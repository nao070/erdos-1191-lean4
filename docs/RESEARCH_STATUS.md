# Research status

## Erdős problem #1191

This archive contains investigations of Sidon sets and the formulations referred to as Q1 and Q2 in the project notes. It does not provide an established solution to the full problem.

The [Q1 Lean development](../research/mathematics/q1_lean4_execution_2026-09-05/lean/README.md) documents formulation bridges, examples establishing admissibility, finite identities, and supporting inequalities under explicit hypotheses. The central Q1 statement is represented as a proposition, not asserted as a proved theorem.

The [finite kernel](../research/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/lean_kernel/README.md) covers finite prefix/scale identities, adjacent-epoch bookkeeping, and ownership accounting. Its README explicitly limits the scope: these modules do not prove Q1 or Q2.

## Computational experiments

The dataset collection contains search outputs, exact checks, intermediate experiments, and historical snapshots. Such evidence must be interpreted with its actual input range, assumptions, and implementation. A finite experiment alone does not settle an asymptotic or universally quantified claim.

The Erdős #677 experiment collection includes a large persistent search index. Its transfer is ongoing. The downloader offers a dataset only after the archive inventory marks it verified.

## What “verified” means in the dataset inventory

`verified: true` in `archive-index.json` records archive integrity: the stored data was read back and checked against its SHA-256 inventory. It is not a claim that every mathematical statement or program in that dataset is correct.

Historical Lean build records belong to their recorded environments. This publication preserves source files and pinned dependencies; it does not report a fresh successful build of every archived project.

## Working with historical material

Prefer project-specific READMEs, explicit theorem statements, audit modules, and evidence logs over broad claims in draft notes. Include the file path and assumptions when citing or reviewing a result. Proposed proofs, rejected approaches, and incomplete arguments are retained as research material.

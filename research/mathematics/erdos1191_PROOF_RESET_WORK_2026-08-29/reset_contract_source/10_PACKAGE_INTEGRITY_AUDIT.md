# Package Integrity Audit

## Audited package

Extracted root used in this audit:

`mathematics/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28`

Actual files found: **415**.

## Sealed checkpoint vs current worktree

The handoff inventory describes a Wave 12 release with 295 inventory files and a 294-entry self-excluding manifest. Its recorded complete runner passed 275 tests and 54 subtests through Wave 12, including an independently extracted ZIP copy.

The current tree has later Wave 13–15 edits. Therefore it is a worktree layered on top of the sealed checkpoint, not the same release.

## Fresh integrity result

Command:

`python3 integrity/verify_package.py`

Result: exit code 1.

Detected classes of failure:

1. forbidden cache files (`__pycache__`, `.pytest_cache`, `.ruff_cache`);
2. 18 unlisted Wave 13–15 files;
3. checksum mismatches in six listed files:
   - `core_workspace/1191_MASTER_STATUS.md`
   - `core_workspace/approach_registry.md`
   - `core_workspace/counterexamples.md`
   - `core_workspace/endpoint_variance/README.md`
   - `core_workspace/proof_obligations.md`
   - `integrity/run_all_checks.sh`

The full log is in `evidence/verify_package_20260829.log`.

## Entrypoint drift

- `00_START_HERE_PROMPT.txt` says Wave 12 is current and P18 is a sufficient next theorem, not claimed equivalent.
- `HANDOFF_MANIFEST.md` names P18 as the primary next direction.
- `1191_MASTER_STATUS.md` and `proof_obligations.md` later say Wave 13 proves universal P17/P18 are Question-1-equivalent.

This is a functional contradiction for the next agent even though the mathematical history can be reconciled chronologically.

## Test discovery and focused tests

Fresh collection:

- **293 tests collected**.

Fresh focused run on Wave 13/14:

- **18 tests passed**;
- **65,331 subtests passed**;
- exit code 0.

Files run:
- `test_wave13_p18_harmonic_obstruction_probe.py`
- `test_wave13_new_birth_barrier_probe.py`
- `test_wave14_future_rank_promotion.py`
- `test_wave14_future_rank_promotion_certificate.py`

Logs:
- `evidence/pytest_collect_20260829.log`
- `evidence/focused_tests_20260829.log`

## What was not verified here

A fresh complete 293-test historical suite plus all certificate regeneration was not completed in this audit. Therefore this pack does not claim that the entire current tree passes.

## Wave 15 evidence gap

Only this Wave 15 artifact was found:

`WAVE15_LOCAL_PROMOTION_ALLOCATION_AND_HORIZON_OBSTRUCTION_2026-08-29.md`

No Wave 15 Python probe, focused test, or JSON certificate was found, despite the note stating that a deterministic probe records the calibration table.

## Correct repair order

1. Copy original tree read-only.
2. Mark latest tree `UNSEALED_WORKTREE`.
3. Remove caches only in the new release candidate, not from the forensic original.
4. Reconcile claim registry and entrypoints.
5. Independently audit/implement Wave 15 evidence or downgrade it.
6. Run fast/focused tests.
7. Build Lean kernel.
8. Only after theorem statements stabilize, regenerate inventory and manifest.
9. Run full release verification once at the milestone.
10. Extract the new ZIP into a clean directory and rerun everything.

A green regenerated manifest alone would prove only that the altered files were hashed, not that their mathematics is correct.

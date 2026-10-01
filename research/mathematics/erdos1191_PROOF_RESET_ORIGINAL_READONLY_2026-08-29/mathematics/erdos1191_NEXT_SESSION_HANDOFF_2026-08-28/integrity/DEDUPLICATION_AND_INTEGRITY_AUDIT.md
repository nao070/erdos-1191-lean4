# Deduplication and Integrity Audit

**Audit date:** 2026-08-28

## Inputs

1. `erdos1191_CONTINUED_ENDPOINT_VARIANCE_2026-08-28.zip`
2. `erdos1191_endpoint_variance_artifacts_2026-08-28.zip`

## ZIP comparison

- First ZIP: 46 regular files, 54 ZIP entries including directories.
- Second ZIP: 28 regular files, 29 ZIP entries including a directory.
- All 28 regular files in the second ZIP had at least one exact SHA-256 match in the first ZIP.
- The matches corresponded to `core_workspace/endpoint_variance/`, including six compiled Python cache files.
- Unique files contributed by the second ZIP: **0**.

The second ZIP was therefore not nested in the new package.

## Cache removal

Excluded from the canonical handoff:

- `__pycache__/`
- `.pytest_cache/`

These are environment-specific and reproducible from the source/tests.

## Original manifest checks

### Top-level continuation manifest

The original `CONTINUATION_SHA256SUMS_2026-08-28` checked all listed files successfully when run from the extracted ZIP root.

### Endpoint manifest

The original endpoint manifest paths are relative to `core_workspace/`, not to `core_workspace/endpoint_variance/`. From the correct directory:

- every payload entry passed;
- the entry for `endpoint_variance/SHA256SUMS` failed;
- the failure is caused by the manifest hashing itself.

The new package retains the original manifest only as an audit artifact and generates `PACKAGE_SHA256SUMS.txt` without a self-entry.

Three original certificate run-log files were byte-identical to their corresponding JSON certificate files. The canonical package keeps the JSON certificates and the clean combined rerun log, while the archived original manifests preserve the removed filenames and hashes.

## New verification design

`integrity/verify_package.py`:

- verifies every regular package file except the manifest itself;
- rejects missing files;
- rejects unlisted extra files;
- rejects duplicate or malformed manifest lines;
- rejects `__pycache__/` and `.pytest_cache/` files in a release package;
- is cross-platform and uses Python’s standard library.

## Mathematical payload rerun

The endpoint tests and all three deterministic certificate programs were run successfully. See `TEST_VERIFICATION_2026-08-28.json` and `REVERIFICATION_2026-08-28.log`.

## Scope

This audit establishes byte-level organization and finite verifier reproducibility for the available files. It does not establish the mathematical novelty of the theorem, the correctness of older missing computations, or a solution of #1191.

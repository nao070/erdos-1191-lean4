# Missing Referenced Artifacts

The uploaded continuation ZIP contains the endpoint-variance work and consolidated ledgers, but it does **not** contain every older path mentioned by those ledgers.

## Legacy paths referred to but absent

Examples include:

- `computation/crossblock.py`
- `computation/check_sidon.py`
- `computation/forbidden_recurrence.py`
- `computation/greedy_growth.py`
- `computation/out/crossblock_scaling.json`
- `computation/out/check_sidon.json`
- `computation/out/forbidden_recurrence.json`
- earlier finite-profile solvers and certificates for `Lambda_n(d)` / `rho_n`
- the complete old `notes/` directory

A search of the currently available conversation uploads and file library did not locate a complete workspace ZIP containing these code/data paths. The package therefore preserves the narrative records but does not claim those legacy experiments are reproducible from the present files.

## Required handling

- Treat the older numerical claims as `[COMPUTATIONAL — REPORTED, ARTIFACTS MISSING]` until the exact code, raw results, and manifests are recovered.
- Do not rerun or repair a file by inventing its prior contents from prose.
- If the missing local workspace is later provided, hash it first, compare it against the legacy ledger, and import only verified unique files.
- The endpoint-variance code, tests, and certificates **are** present and independently rerunnable.

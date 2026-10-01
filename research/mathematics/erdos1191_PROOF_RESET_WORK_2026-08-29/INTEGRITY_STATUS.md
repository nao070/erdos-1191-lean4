# Integrity status

Date: 2026-08-31 (Asia/Tokyo)  
Status: `UNSEALED_RESET_WORKTREE`  
Mathematical status: `UNRESOLVED_AT_HARD_LIMIT`

## Source bundle

Input:

```text
/Users/USER/Downloads/erdos1191_CODEX_COMPLETE_PROOF_BUNDLE_2026-08-29.zip
```

Checks performed now:

- outer SHA-256: `5f00e19e4cdfa4f5a22e3848af5e23c1cbabdf25f27fa69fbea5d86d21d1446b`;
- `unzip -t`: no compressed-data errors;
- all five payload hashes match the supplied `OUTER_SHA256SUMS.txt`:
  - English contract: `e5f912fe59703c49958780015b6a09be13a5d403317d6e95090d59260c7a1ad3`;
  - Japanese contract: `fe1ec50bbca037ec414b612fb4d69fd3d833b24346a8302c4ff387e5da6594fe`;
  - original mathematics ZIP: `14914924a2520e1a65bc688ad5268f5836bcb50fa264b0c99b4c51e02d39fcea`;
  - audit/reset ZIP: `19e2983df3da5f5c41f0356f0e82a89e4d9a22395829b289caeaa8e6a7301ccc`;
  - bundle README: `423cae516d7f871fdf3a91ead076d7f661804e55bf997c2312a83256f4eeef6c`.

## Original tree preservation

The original mathematics ZIP is preserved at:

```text
/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_ORIGINAL_READONLY_2026-08-29/mathematics/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28
```

Direct permission audit found zero owner-writable files and zero owner-writable directories; the root is `dr-xr-xr-x`. It was not cleaned, repaired, rehashed, or used as the write target.

Exact original snapshot:

- 345 regular files;
- 32 forbidden cache files;
- 294 self-excluding manifest entries;
- 18 non-cache unlisted files;
- six checksum mismatches;
- manifest verifier exit 1.

The full contract-script output is preserved in `evidence/forensic_original_audit/audit.log`. Its BSD `find -printf` and missing-bare-`pytest` failures are retained verbatim. Portable reruns established 293 collected tests and a passing Wave13/14 focus of 18 tests plus 65,331 subtests. These reruns did not mutate the read-only tree.

## Later Wave 19 seed

The reset worktree was seeded from the later canonical Wave 19 package rather than mechanically downgrading to the older original ZIP. Its preserved release record is:

```text
integrity/WAVE19_TEST_VERIFICATION_2026-08-29.json
SHA-256 456719215e41c32ed89dfe919ec500ed5a4a27167a03e88afe4d5e42e971e2e8
```

That record states, for the pre-reset package:

- 379 inventory files;
- 378 self-excluding manifest entries;
- 401 tests and 78,844 subtests passed;
- seven Wave 19 certificate families replayed byte-identically;
- closing manifest verification passed.

Those are prior recorded results. They were not rerun as a full release in this reset. The current old manifest itself has SHA-256 `e7c39676a6c612701eda8e6ef5b06ea11dddb2d1a3af36fa5097368e15dd95fa`.

## Current reset worktree

The current directory intentionally adds reset-contract sources, forensic evidence, new status documents, Lean work, and Gmix no-go files outside the old Wave 19 manifest. An initial fresh `python3 integrity/verify_package.py` therefore exited 1 with unlisted files while all 378 listed paths still matched. At the initial stale-directive reconciliation checkpoint, nine listed files were deliberately changed: `00_START_HERE_PROMPT.txt`, `FILE_INVENTORY.txt`, `HANDOFF_MANIFEST.md`, `NEW_SESSION_LAUNCH_MESSAGE.txt`, `NEXT_LEMMA_TARGETS_ANTI_EULERIAN.md`, `README_START_HERE_JA.md`, `core_workspace/1191_MASTER_STATUS.md`, `core_workspace/approach_registry.md`, and `core_workspace/proof_obligations.md`.

`FILE_INVENTORY.txt` was not regenerated: its historical 379-file body was retained and only a prominent reset-warning banner was added. Likewise, the old checksum manifest was not refreshed.

This is the intended state during stabilization:

- the old manifest remains preserved as the pre-reset baseline; the dated nine-path reconciliation above is historical, and the exact current 11-path mismatch set is recorded below;
- new work is visibly unsealed;
- the old manifest has not been regenerated to manufacture a green result.

Historical controlled snapshot (`2026-08-29T15:48:13+0900`, superseded by
the later Route-C continuation): 445 regular files, zero forbidden
cache/bytecode/lock files, 378 old self-excluding manifest entries, 66
verifier-reported unlisted current files, zero listed files missing, and nine
intentional listed-file checksum mismatches.  Because the verifier
intentionally excludes the manifest itself, the physical not-listed count was
67 when that one file was included.  The historical arithmetic was
`378 listed + 1 self-excluded manifest + 66 verifier-unlisted = 445`.  These
figures are retained only as a dated checkpoint and are not a claim about the
current worktree; a fresh integrity delta is recorded after the current
Route-C artifacts stabilize.

The Wave 15 discrepancy is now resolved by provenance rather than by erasure:

- original supplied mathematics tree: prose memo only;
- later Wave 19 seed: memo, probe, test, and dated JSON present;
- fresh later-seed focus: 5 tests and 26 subtests pass;
- fresh generator replay: byte-identical to the dated JSON;
- theorem boundary: finite fixtures are verified, but the general asymptotic prose theorem remains `HUMAN_PROOF_PENDING_AUDIT`.

The Gmix no-go mathematical audit and focused artifact family are now green:

- the first focused run was exit 1, with 9 passed and 3 failed, exposing missing generator functions `dyadic_current_gap_lower` and `weighted_gmix_floor`;
- after repair, the proof memo, generator, and test are present and a fresh focus is exit 0 with 12 passed;
- the dated deterministic JSON is present, has SHA-256 `596c046c515c610fa91f49781bbd3729eaa0e6f4c513b5910623a3a5ccec091f`, and a fresh generator replay compares byte-identically.

The named-method no-go may be used at its audited mathematical scope. This focused closure does not make the whole reset worktree a release and does not prove abstract P28 or Q1.

## Lean kernel integrity

The controlled Lean distribution now contains 17 files (92 KiB by filesystem
allocation).  It pins Lean `v4.33.0` and mathlib commit
`db584cd6d46c92f209a44c0f1c829460d327499d`.  The fresh final verification
recorded:

- MCP `lean_build(clean=true)`: exit 0, 1,054 jobs;
- the following direct `lake build`: exit 0, 1,047 jobs;
- `lake env lean Erdos1191/AxiomAudit.lean`: exit 0;
- empty diagnostics for `PrefixScaleFinite.lean` and
  `OwnershipFinite.lean`;
- no `sorry`, `admit`, or project-defined axiom in project sources; and
- theorem-by-theorem verification output containing only standard
  Lean/mathlib axioms where present.

The generated `lean_kernel/.lake/` dependency/build cache was then moved
recoverably outside the worktree to
`/private/tmp/erdos1191_generated_20260831_liAYKE/lean_kernel_.lake`.
`lake-manifest.json` retains exact dependency revisions.  Independent
readable derivations for every exported formal theorem are in
`LEAN_KERNEL_PROSE_AUDIT.md`.  The certified scope is the listed finite Sidon
facts, generic finite Abel/telescope algebra, exact prefix/scale transport,
and generic finite ownership/change-of-basis identities.  It does not imply
completion of L2, the Wave-specific analytic master, L4, L5, C058, Q1, or Q2.
A literal extracted-copy Lean dependency rebuild was not performed, so that
release-style replay remains pending.

## Required-output and Route C checklist

All contract outputs are present: reset checkpoint, synchronized CSV/JSON registry, quantifier audit, Lean status/project/prose companion, route portfolio, updated entrypoint, integrity status, literature delta, and one-line final status. The additional Route C evidence files `ROUTE_C_MULTI_N_CONVEXITY_NO_GO.md` and `ROUTE_C_CROSS_KERNEL_GATE.md` are present. The literature delta records the Hou--Zhao v2 correction that its joint direct-sum construction escapes naive convex averaging but remains finite and is subject to the cross-correlation sign gate.

The later Route-C evidence now also includes the exact retained-box memo,
generator, JSON, and tests; the centered multiband-history memo, generator,
JSON, and tests; the cross-ratio box-dipole/Gothic memo, generator, JSON, and
tests; and both targeted plugin literature deltas.  All are unlisted by the
preserved old manifest by design.  They close the internal centered carrier
and the common scale-density/Gothic coefficient map, while leaving C058's
legal phase-integrated signed rewrite open.

## Historical C098 Route-C integrity delta

After the C098 continuation stabilized, the then-current focused verification
recorded:

- all **25 Route-C suites / 291 tests passed** with zero failures, errors, or
  skips: 258 tests from complete `test_*.py` discovery plus 33 tests from the
  four non-discovery `*_test.py` files;
- the five C089--C098 certificate generators (universal star, mixed-scale
  energy, physical transfer, parametric physical cover, and cross-scale
  surplus) all exited 0 on exact `--verify --self-check` replay;
- the direct interval/Haar bundle passed 16 tests and rejected 16 mutations;
  payload SHA-256
  `8f067c8e409b93058520b6e669de7eb4370e81c19b1c5abd988e1c0e68fc6ac2`;
- the membership-SDDM bundle passed 12 tests, rejected 12 mutations, and
  replayed literal raw JSON bytes; payload SHA-256
  `d2620c68c366f765a1f5c502be65dfaf258558af93b9df5f4a50464d8fd52f23`;
- the physical Haar-energy bundle passed 16 tests, rejected 16 mutations,
  replayed literal raw JSON bytes, and received a clean independent exact
  audit over its 496-difference/88-cell three-epoch fixture; payload SHA-256
  `3f406a1a6c7dfa19bf5172eadba5c5227ba175f4caf7811df6e53e5c75d3f630`,
  JSON SHA-256
  `dd0ef8cdac0f1b24c1aaca61d63a8ffc28eeb1dbc2f76fd308e4b141cc874478`;
- the C097--C098 cross-scale bundle passed 6 tests, rejected all 12 semantic
  mutations, and replayed payload SHA-256
  `77eaadc8192e84c2f3a83f4a08161697d26e59b71875e696b8246e2caa2ee529`;
- the synchronized claim registries contain 98 sequential entries through
  C098 and retain global status `UNRESOLVED_AT_HARD_LIMIT`;
- the final scan has zero cache, bytecode, or lock files.  Transient
  `route_probes/__pycache__` content and the research-state lock were moved
  recoverably outside the worktree to
  `/tmp/erdos1191-final-artifacts-20260830.FTOBuF`.

A `PYTHONDONTWRITEBYTECODE=1 python3 integrity/verify_package.py` run at that
checkpoint exited 1, as expected for this intentionally unsealed
continuation.  Its dated delta was:

- 557 physical regular files;
- 556 verifier-eligible files after excluding the old manifest itself;
- 378 old manifest entries;
- 178 verifier-unlisted files;
- zero listed files missing;
- 11 listed-file checksum mismatches; and
- zero forbidden cache or lock files.

The historical arithmetic is
`378 listed + 1 self-excluded manifest + 178 unlisted = 557`.
The mismatch set is the six reconciled legacy entrypoints, the three listed
canonical proof/status documents, `core_workspace/literature_ledger.md`, and
`core_workspace/research_log.md`. The old manifest was deliberately not
refreshed, so this remains an auditable worktree delta, not a sealed-release
or prize-proof claim.

## Current C116 verification and integrity delta — 2026-08-31

The complete current Route-C discovery set contains 32 suite files.  A fresh
cache-suppressed replay ran 352 tests in 261.598 seconds and returned `OK`.
The fixed-history full-phase family separately passed 10 tests, the lacunary
dual obstruction passed 4 tests, and the C107 regression family passed 9
tests.  These focused counts are included in, not added to, the 352-test
total.

The synchronized CSV and JSON claim registries contain exactly 116 sequential
entries, C001--C116, and global status `UNRESOLVED_AT_HARD_LIMIT`.  Every JSON
artifact parses.  The final text scan finds no forbidden C0 control character
apart from permitted tab, line feed, and carriage return.

The exact current old-manifest delta, after adding the final verification
record, is:

- 597 physical regular files;
- 596 verifier-eligible files after excluding the old manifest itself;
- 378 old manifest entries;
- 218 verifier-unlisted files;
- zero listed files missing;
- 11 listed-file checksum mismatches; and
- zero forbidden cache, bytecode, generated Lean/Rocq object, or lock files.

The arithmetic is `378 listed + 1 self-excluded manifest + 218 unlisted =
597`.  A fresh old-manifest verifier exits 1 for precisely the intended
unsealed-state reasons.  The mismatch set remains the six reconciled legacy
entrypoints, the three listed canonical proof/status documents,
`core_workspace/literature_ledger.md`, and `core_workspace/research_log.md`.
The preserved old manifest was not regenerated.

Lean MCP clean-built 1,054 jobs; the following direct Lake build completed
1,047 jobs.  All frozen theorem diagnostics and verification checks were
green, with only standard Lean/mathlib axioms reported.  The pinned Rocq MCP
again exposed 13 tools; health, the minimal proof, both canonical source
compiles, and all five named assumption audits returned success with empty
assumptions.  Generated `.lake`, Python cache, and Rocq object/auxiliary files
were removed from the worktree after their evidence was captured.

The canonical concise record is
`evidence/C116_FINAL_VERIFICATION_2026-08-31.md`.  This is an auditable
unsealed handoff checkpoint, not a sealed release and not prize evidence.

## Current C120 verification delta — 2026-08-31

The current Route-C discovery tree contains 34 suite files.  A fresh
cache-suppressed replay ran 366 tests in 342.109 seconds and returned `OK`
with no failures, errors, or skips.  The C120 reverse-profile bundle separately
passed seven focused tests and rejected all thirteen semantic mutations.

The synchronized CSV and JSON claim registries contain exactly 120 sequential
entries, `C001`--`C120`, and retain global status
`UNRESOLVED_AT_HARD_LIMIT`.  All 113 first-party JSON artifacts parse.  The
selected text/control scan is clean.

A fresh Lean build completed 1,067 jobs and the axiom audit again reported
only `propext`, `Classical.choice`, and `Quot.sound`.  A fresh temporary Rocq
9.1.1 compile/check closed all fourteen audited theorem families.  Source-hole
and generated-artifact scans are clean outside the intentionally retained
Lean `.lake` build/dependency cache.  Transient Python bytecode was moved
recoverably to `/tmp/erdos1191-pycache-c120.vX2840` and
`/tmp/erdos1191-pycache-post-c118.VnIPCX`.

The exact C120 certificate and the unregistered C118 primal-window diagnostic
are recorded in `evidence/C120_VERIFICATION_2026-08-31.md`.  This remains an
auditable unsealed research worktree, not a release, complete proof, or prize
claim.  The preserved old manifest was not regenerated.

## Release decision

Do not regenerate `FILE_INVENTORY.txt` or `integrity/PACKAGE_SHA256SUMS.txt` now. A release manifest is justified only after:

1. the claim registry, quantifier audit, entrypoints, and Lean status stabilize;
2. incomplete exploratory artifacts are repaired or explicitly excluded;
3. focused/formal gates pass;
4. a genuine theorem milestone warrants the release tier;
5. the complete runner, every included certificate replay, cache scan, ZIP test, clean extraction, and closing manifest check all pass.

Until then this directory is an auditable worktree, not a release package and not prize evidence.

`UNRESOLVED_AT_HARD_LIMIT`


## Current C121 verification delta — 2026-08-31

The current Route-C discovery tree contains 35 suite files.  A fresh
cache-suppressed replay ran 371 tests in 357.481 seconds and returned `OK`
with no failures, errors, or skips.  The C121 family separately passed five
focused tests, and its CLI self-check rejected all 18 deliberate mutations;
these checks are included in, not added to, the 371-test total.

The synchronized CSV and JSON registries contain exactly 121 sequential
entries, `C001`--`C121`, and retain global status
`UNRESOLVED_AT_HARD_LIMIT`.  All 114 first-party JSON artifacts parse.  The
new exact certificate stores 102 phase pieces, 204 rational duals, 62,832
nonnegative weights, and 408 endpoint positive-definiteness checks.

The pinned Lean project completed 1,068 jobs after adding the three frozen
coefficient-barrier theorems.  Their axiom audit reports only `propext`,
`Classical.choice`, and `Quot.sound`.  The pinned Rocq MCP health/minimal
probes succeeded, and its selective `CoefficientBarrierAudit.v` compile and
both assumption checks closed under the global context.

Transient Python bytecode and Rocq generated products are excluded from the
canonical tree after verification; the Lean `.lake` dependency/build cache
is intentionally retained and excluded from release claims.  The old
manifest remains deliberately unrefreshed.  This is an auditable unsealed
research checkpoint, not a complete proof, sealed release, or prize claim.

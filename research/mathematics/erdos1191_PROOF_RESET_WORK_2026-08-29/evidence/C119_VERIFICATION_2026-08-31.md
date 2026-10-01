# C117--C119 verification checkpoint

Date: 2026-08-31 (Asia/Tokyo)  
Global status: `UNRESOLVED_AT_HARD_LIMIT`

This is a research-state verification checkpoint, not a sealed release,
complete proof, novelty determination, or prize claim.  C058 remains the sole
primary bottleneck.

## Route-C regression

From the canonical worktree root:

`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s route_probes -p '*test*.py' -v`

Fresh result after the strengthened C118 normalized-bound assertions:

- 33 discovered test suites;
- 359 tests;
- `Ran 359 tests in 302.947s`;
- `OK`.

The strengthened C118 focused module separately passed all seven tests in
22.991 seconds.  Its canonical CLI returned:

`VERIFY_OK chambers_replayed=87 epoch_duals_replayed=174 endpoint_ldl_checks=348 exact_log_integral_upper<-1/40 normalized_log_phase_upper<-1/25 mutations_rejected=12`

Current SHA-256 values:

- verifier source:
  `a8ce48b6170000d373bb2f297d85d4474b6c03345054c8892966080a8e4ee790`;
- certificate JSON:
  `331da5cdf1e553c65cace050ffc2ac2ae2dee847f949e2b932aceaa43dafd55f`;
- focused test:
  `91061952d2279898f4e5b647ef8b1874aa33242cf2a46bed137ef8b81851dade`;
- certificate payload:
  `176cc369f21e9002945e4716b66a1a58a1e358e5e92c03572ae00039c2e01b16`.

## Registry and first-party integrity

Fresh read-only validation returned:

- `REGISTRY_OK claims=119 sequential=C001..C119 csv_json_equal=true`;
- registry global status exactly `UNRESOLVED_AT_HARD_LIMIT`;
- 112 first-party JSON files parsed successfully (the generated
  `lean_kernel/.lake` dependency tree was intentionally excluded);
- 606 non-cache first-party text files had no forbidden C0 control bytes;
- no Python cache, Rocq object, or Lean formal object remained outside the
  expected `lean_kernel/.lake` build/dependency cache; and
- Lean/Rocq source scans found no `sorry`, `admit`, `native_decide`, custom
  `axiom`, `Admitted`, `Parameter`, `Conjecture`, or `Abort` declaration.

The full regression's child processes generated four Python bytecode files
despite the outer cache-suppression flag.  They were moved recoverably out of
the canonical tree to `/tmp/erdos1191-pycache-final.7kK1NW`; an earlier set of
12 stale bytecode files was moved to `/tmp/erdos1191-pycache.vxoNoZ`.

The populated `.lake` directory is deliberately retained because it is the
pinned Lean build/dependency cache.  Therefore this checkpoint does not claim
that the old Wave-19 manifest is sealed or that a release archive is clean.

## Lean 4

Pinned project state:

- Lean 4.33.0;
- mathlib commit
  `db584cd6d46c92f209a44c0f1c829460d327499d`;
- fresh `lake build`: `Build completed successfully (1067 jobs)`.

Fresh `AxiomAudit.lean` output lists only Lean/mathlib's standard
`propext`, `Classical.choice`, and `Quot.sound` dependencies.  The frozen
three-coordinate owner-stitch family includes symmetry, zero-row sums,
arbitrary-rational square energies and nonnegativity, fixed local/global
energies, owner shares, and the final obstruction.

Current formal source SHA-256 values:

- `OwnershipFinite.lean`:
  `7a7d691f14b3b65a08dc78a99b7f5482aaa8294a45e52cc2b4cfcca87b0c88ea`;
- `AxiomAudit.lean`:
  `b8a3e4fd041d03066e6ee06219e901de1fd880ee5da6844ae9cc8748efa60600`.

## Rocq/Coq

Rocq 9.1.1 was independently replayed in the temporary directory
`/tmp/erdos1191-rocq-final.qhCgrm` through the pinned `coq-mcp` opam switch.
Compilation exited zero and printed `Closed under the global context` for all
14 audited theorem families; `rocq check -silent` exited zero.  No generated
Rocq object remains in the canonical tree.

Current `OwnershipFiniteAudit.v` SHA-256:
`12f54f6d24972777e1fc7f1d01d633f818e0fb7d0ec5d513171fc87eba863952`.

The live MCP health/minimal probes and toolchain details are recorded in
`evidence/formal_toolchain_refresh_2026-08-31.txt`.

## Mathematical scope at this checkpoint

- C117 formally blocks only automatic stitching of separate local owner maps.
- C118 proves only the finite `k=2`, `C=2`-envelope, current-cone full-phase
  no-go; its raw integral upper is below `-1/40` and its normalized dual upper
  lies in `(-81/2000,-1/25)`.
- C119 proves only bounded Fejer-weighted signed increments for the normalized
  shell-concentration storage coordinate on the finite range
  `0<=k0<=K<=J`.

The exact reverse-concentration row, same-multiset ordered discovery rows, and
the coefficient trial `epsilon=A=1/1000`, `B=1/3` are finite calibration for
the next phase bank.  They are not a local inequality, arbitrary-rank theorem,
compatible infinite history, solution of either Erdős question, or prize
evidence.

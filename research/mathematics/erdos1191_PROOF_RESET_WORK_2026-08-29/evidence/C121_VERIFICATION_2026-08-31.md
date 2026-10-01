# C121 verification record — 2026-08-31

Global status: `UNRESOLVED_AT_HARD_LIMIT`

## Registered claim

C121 records a finite conditional no-go on the fixed C118 fixture and current
independent epoch-block cone.  Four equal reciprocal-coordinate subpieces in
each of chambers `49,64,70,73,74`, together with the 82 retained canonical
chambers, produce 102 phase pieces, 204 rational epoch duals, 62,832
nonnegative weights, and 408 exact endpoint LDL checks.

The exact replay proves a normalized dual upper below `-83/2000`.  The fixed
prototype right side lies strictly above that value with certified gap greater
than `1/2000`.  More generally, for `epsilon,A>=0`, `e_2=0`, compatibility of
the row forces

`B > 287434930599/860203021250 > 1/3`.

Thus the coefficient box `0<=B<=1/3` fails on this finite row.  This does not
refute all scalar `B`, a larger cone, a sufficiently-large-rank inequality,
C058, either Erdős question, novelty, or prize eligibility.

## Exact artifacts

| artifact | SHA-256 |
|---|---|
| `route_probes/ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.py` | `e568d5562dd8c51c82ff603d678cd712f3f3250398d927982fa9c3fcd0469953` |
| `route_probes/ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json` | `1288d87e095a47f9fdf679a40656bafdef4ad4b03150ccb3254b25b043937a0b` |
| certificate payload | `ee4074acc3e57c5f7fe991a74b7f33ad2424631ec75b814ab0c70c80cde11cff` |
| source refinement | `0c975c10fea08aa33d4eed9f120bd5381d2355f7ea82f235216f7e08a06dcf5d` |
| `lean_kernel/Erdos1191/CoefficientBarrier.lean` | `12fd7dc86110684048bd591cbafe678956bb08506fbd8a033449b39ae1a45f98` |
| `rocq_kernel/CoefficientBarrierAudit.v` | `11594493ce15c078bc3d823f50bbb8d010840f00bd68928219b3d274d61d5018` |

The canonical C118 base certificate is pinned by file SHA-256
`331da5cdf1e553c65cace050ffc2ac2ae2dee847f949e2b932aceaa43dafd55f`
and payload SHA-256
`176cc369f21e9002945e4716b66a1a58a1e358e5e92c03572ae00039c2e01b16`.
The verifier accepts only the exact schema, hashes, reciprocal subdivision,
dual lengths, objectives, endpoint matrices, bounds, and scope flags.  Its
self-check rejects all 18 deliberately corrupted variants.

## Formal finite audit

The current Lean MCP/project build completes 1,068 jobs on Lean 4.33.0 with
the pinned mathlib commit.  `CoefficientBarrier.lean` contains three theorems:
the exact ratio identity, the necessary strict coefficient barrier, and the
`B<=1/3` contradiction.  The axiom audit reports only `propext`,
`Classical.choice`, and `Quot.sound` where imported mathlib results require
them; no source hole or custom axiom is used.

The current direct stdio Rocq MCP health check reports server 0.3.1, Rocq
9.1.1, and 13 tools.  A minimal compile and verify probe is closed.  The full
MCP compile of `CoefficientBarrierAudit.v` succeeds and both assumption
queries return closed under the global context.

These proof-assistant checks audit only the frozen rational coefficient
calculation.  Formalization remains subordinate to the C058 search.

## Interpretation and next gate

The old C118 rational primal and pointwise dual were not the same SDP: the
primal held `X` fixed on each chamber, while the dual optimized pointwise.
The previous interval was therefore not evidence of a strong-duality failure.
The reciprocal subdivision supplies the exact separating upper certificate.

The negative-`Delta V` C120 complete-phase diagnostic currently yields only
an approximate upper restriction `B<0.9904`, so it does not conflict with the
C118 lower threshold.  This diagnostic is not registered as a separate claim.

The next gate is an exact outer coefficient bank with both signs of
`Delta V`, ordered profile coordinates, same-multiset permutations, larger
rank, and one global C103 owner/boundary ledger.  No complete proof or prize
claim is made.

## Final tree replay

The cache-suppressed Route-C discovery tree contained 35 suite files.  A fresh
full replay ran 371 tests in 357.481 seconds and returned `OK`, with no
failures, errors, or skips.  The C121-focused family separately passed five
tests, and the certificate CLI rejected all 18 deliberate mutations; those
focused checks are included in, not added to, the 371-test total.

The synchronized claim registries contain 121 sequential entries,
`C001`--`C121`, and retain global status `UNRESOLVED_AT_HARD_LIMIT`.  All 114
first-party JSON artifacts parse.  These finite gates validate only their
stated artifacts and scopes; they do not establish C058 or either Erdős
question.

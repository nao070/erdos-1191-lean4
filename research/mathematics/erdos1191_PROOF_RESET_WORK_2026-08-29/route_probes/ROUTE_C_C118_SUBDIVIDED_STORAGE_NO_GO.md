# Route C: C118 reciprocal-subdivision storage no-go

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite conditional no-go; `C058` remains open

## 1. Exact scope

This result concerns only the displayed C118 16-mark Golomb fixture, the
finite `k=2`, `C=2` envelope rows, `rho=9/16`, the complete phase

`1649/8 <= t <= 1649/4`,

and the current independent epoch-block, zero-row-sum PSD cone with its stated
owner convention.  It does not cover larger cross-epoch cones, arbitrary
rank, an eventual critical infinite history, or every scalar storage
coefficient.

The fixture has

`eta_2=log(1659/1768)<0`,

and

`Delta V=V_3-V_2=3440812085/9234857208>0`.

## 2. Reciprocal-coordinate refinement

The C118 base certificate has 87 event chambers.  The five localized dual-gap
hotspots

`49, 64, 70, 73, 74`

are replaced by four equal subintervals in reciprocal coordinate `u=1/t`.
The other 82 chambers retain their canonical duals.  The resulting hybrid
certificate therefore has

- 102 phase pieces (`82+5*4`);
- 204 epoch duals;
- 62,832 stored nonnegative rational weights (`204*308`); and
- 408 exact endpoint positive-definiteness checks.

Every endpoint check uses exact fraction-free Bareiss/Sylvester arithmetic.
The log-phase integral uses exact rational atanh bounds with an explicit tail.
No floating-point value is used in the accepted inequality.

## 3. Exact separation

The replay proves

`normalized dual upper < -83/2000`.

For the C119 prototype

`epsilon=A=1/1000`, `B=1/3`, `e_2=0`,

the exact right-side lower bound is strictly greater than `-83/2000`, and its
gap above the certified dual upper is greater than `1/2000`.  Thus the fixed
C118 prototype is impossible in this cone.

The certificate gives a stronger coefficient-box statement.  If
`epsilon>=0`, `A>=0`, `e_2=0`, and the same complete-phase row held, then
`eta_2<0` makes `-A eta_2` nonnegative.  Since `Delta V>0`, comparison with the
dual upper forces

`B > (249/2000)/Delta V`

and exact rational reduction gives

`B > 287434930599/860203021250 > 1/3`.

Consequently every coefficient choice with `epsilon,A>=0` and
`0<=B<=1/3` fails on this one fixed row.  The exact coefficient-box separation
from the dual upper is greater than `1/10000`.

## 4. Why this is not a strong-duality failure

The earlier C118 rational primal diagnostic and the earlier pointwise dual did
not optimize the same finite object.  The primal kept a matrix `X` fixed over
an event chamber (with common endpoint-valid factors), whereas the dual
bounded the pointwise optimum before integration.  Their interval was thus a
fixed-`X`/pointwise-dual comparison, not a primal-dual gap for one SDP.

The reciprocal subdivision reduces that representation mismatch enough to
separate the prototype exactly.  It neither diagnoses nor relies on failure of
finite SDP strong duality.

## 5. Independent finite sign audit

After the rational statement was frozen, Lean 4 proves the exact barrier
identity, the implication from a compatible master row to the strict lower
bound on `B`, and incompatibility with `B<=1/3` in
`lean_kernel/Erdos1191/CoefficientBarrier.lean`.

Rocq 9.1.1 independently checks the denominator-cleared ratio identity and
the strict comparison with `1/3` in
`rocq_kernel/CoefficientBarrierAudit.v`.  These proof-assistant files audit
only the frozen rational sign calculation; they do not formalize the SDP
certificate or C058.

## 6. Artifacts and hashes

- verifier:
  `route_probes/ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.py`
  
  SHA-256
  `e568d5562dd8c51c82ff603d678cd712f3f3250398d927982fa9c3fcd0469953`;
- canonical certificate:
  `route_probes/ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json`
  
  SHA-256
  `1288d87e095a47f9fdf679a40656bafdef4ad4b03150ccb3254b25b043937a0b`;
- canonical payload SHA-256
  `ee4074acc3e57c5f7fe991a74b7f33ad2424631ec75b814ab0c70c80cde11cff`;
- Lean source SHA-256
  `12fd7dc86110684048bd591cbafe678956bb08506fbd8a033449b39ae1a45f98`;
- Rocq source SHA-256
  `11594493ce15c078bc3d823f50bbb8d010840f00bd68928219b3d274d61d5018`.

The certificate self-check rejects 18 structural, arithmetic, provenance, and
scope mutations.

## 7. Consequence for the next C058 experiment

The scalar prototype is now refuted on the positive-`Delta V` C118 side, but
this does not refute all scalar `B`: the exact necessary threshold is only a
lower bound on `B`.  The negative-`Delta V` C120 fixture supplies an upper-side
constraint, but the current complete-phase audit there gives only
approximately `B<0.9904`, so the two rows do not yet contradict one another.

The next exact experiment is an outer coefficient bank containing positive-
and negative-`Delta V` complete-phase dual rows, same-multiset ordered
permutations, and bounded ordered profile coordinates.  It must then be tested
at 32 marks or on a scalable critical-compatible family and embedded in one
global C103 owner/boundary ledger.  C058, Q1, Q2, novelty, and prize
eligibility remain unresolved; the global status is
`UNRESOLVED_AT_HARD_LIMIT`.

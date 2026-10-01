# Route C: C128 exact common-phase per-chamber pointwise no-go

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite obstruction for the fixed C125 candidate; `C058` remains open

## 1. Frozen finite question

C128 tests only the C125 coefficient vector

`epsilon=A=1/1000`, `B=1/2`, `C_ordered_suffix=1/10`, `e2=0`,

on the C126 common completed-shell phase `[82,164]`, with `rho=9/16`,
for the fixed C120/C123 16-mark pair in the independent epoch-block,
zero-row-sum PSD cone.  The row target is

`(epsilon-A*eta-B*DeltaV-C_ordered_suffix*DeltaVrt)/3-e2`,

where `eta=log(82/215)`.

The exact question is whether that same target can be paid separately on
every event chamber.  Such a chamberwise requirement is necessary for an
all-phase pointwise lower bound at the same target.  It is stronger than a
single lower bound after integration over the complete phase.

## 2. Exact reconstruction

The verifier pins and replays the C126 C120/C123 full-dual sources.  Each
source is checked at four levels: file SHA-256, canonical sorted indent-2 JSON
rendering, internal payload SHA-256, and source schema.  The C125 verifier and
C126 verifier/certificate are also pinned by SHA-256, including the C126
compact payload hash.

For all 282 chambers the verifier reconstructs both epoch duals from their
nonnegative rational weights.  This gives 564 exact dual reconstructions and
1,128 exact endpoint positive-definiteness checks using fraction-free integer
Bareiss/Sylvester arithmetic.  The combined log-piece interval is computed by
combining coefficients before the rational logarithm enclosure, exactly as in
C126.  The wider sum of the two separately enclosed epoch intervals is checked
only as a containing interval and is not used for the combined classification.

Before division by the positive chamber log-width, the verifier explicitly
checks

`0 < raw_piece_lower <= raw_piece_upper`.

All logarithms use pinned 30-term rational atanh-series enclosures with an
explicit positive tail.  No floating-point arithmetic enters the accepted
classification.

## 3. Exact separation result

| row | phase chambers | chambers separated by the stored exact local dual |
|---|---:|---:|
| C120 | 147 | 0 |
| C123 | 135 | 22 |

For C123 the separated set is exactly

`0,1,...,21`.

It starts with chamber 0, `[82,493/6]`, and ends with chamber 21,
`[359/4,90]`.  On every one of these 22 chambers, the exact upper bound for
the normalized chamber-average value is strictly below the exact lower bound
for the C125 target.  Thus each of these chambers fails the requested separate
per-chamber target in the frozen cone.

The C120 count `0` has a deliberately one-sided meaning: this stored local
dual test does not separate the candidate on any C120 chamber.  It does not
prove C120 chamberwise primal feasibility.

## 4. Strongest chamber

The largest certified deficit is C123 chamber 0, `[82,493/6]`.  Exact outward
bounds give

- target `> 9/250`;
- combined normalized local dual upper `< 39/2000`;
- target minus upper `> 33/2000`;
- weighted epoch-4 local upper `< -13/1000`;
- weighted epoch-8 local upper `< 33/1000`.

The combined failure is dominated numerically by the negative epoch-4 term,
but the target belongs to the weighted sum.  C128 therefore does not attribute
the obstruction to either epoch in isolation.

## 5. Logical consequence

A pointwise lower bound by the fixed target throughout a chamber would imply
the same lower bound for its positive `dt/t` average.  The exact local-dual
separations contradict that implication on C123 chambers 0--21.  Consequently
the fixed C125 target cannot be imposed uniformly on every C123 chamber, and
an all-phase pointwise lower bound at that target is false in this frozen cone.

This does **not** make the physical phase `[82,164]` impossible.  It also does
not refute a complete-phase integrated inequality.  Any surviving use of this
candidate must instead permit genuine phase redistribution, using surplus on
later chambers to pay the early deficits.  That redistribution is now a
load-bearing obligation rather than an optional proof presentation.

## 6. Numerical integrated screen is heuristic only

A separate floating SDP screen, not included in the canonical certificate,
found complete-phase normalized values approximately

- C120: `0.0845837459948265` against target `0.0465448942665218`;
- C123: `0.0397201128486530` against target `0.0360732464210793`.

The C120 epoch solves reported `12 optimal` and `282 optimal_inaccurate`; the
C123 epoch solves reported `6 optimal` and `264 optimal_inaccurate`.  The
screen used a `5e-6` numerical owner floor and PSD eigenvalue clipping.  It has
no pinned rational primal bank, exact owner replay, or exact integrated log
sum.  These numbers are heuristic route-selection evidence only: they are not
promoted to C128's proof claim and do not prove integrated feasibility.

The isolated temporary C120 chamber-0 rational factor was also not promoted,
because C128 needs no additional factor payload and makes no C120 feasibility
claim.

## 7. Canonical artifacts and hashes

- verifier: `ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_certificate.py`,
  SHA-256
  `d6cc32966f58bc6381d8673901f5438e2c2570d20bcd07f8662192a5c3f3dea2`;
- compact certificate:
  `ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_certificate.json`, SHA-256
  `6bf92fd94021878dbac450668fb5ccf8d6391e67d628c1bd1dd6a22f68c794e5`;
- regression and hardening tests:
  `ROUTE_C_C128_COMMON_PHASE_POINTWISE_NO_GO_test.py`, SHA-256
  `52c1bd72aa89ad9d85785ddf0cb5e0f88a34b2285159d6447aeeae89c9ccfd07`.

The initial TDD run failed because the C128 verifier module did not yet exist.
The P1 regression run then exposed an invalid equality between separately
enclosed epoch sums and the tighter combined enclosure.  The corrected
verifier uses the combined interval for classification, checks containment by
the separate intervals, and rejects nonpositive combined numerators before
log division.  The focused suite has six tests, including controlled mutation
tests for noncanonical source rendering and nonpositive raw pieces.

## 8. Scope and status

- fixed C120/C123 16-mark pair and fixed C125 candidate only;
- common completed-shell phase `[82,164]` and `rho=9/16` only;
- independent epoch-block cone only;
- exact local-average obstruction on C123 chambers 0--21;
- no C120 chamberwise feasibility conclusion;
- no integrated primal certificate and no integrated infeasibility claim;
- no local master inequality;
- global C103 phase-rule admissibility and representative independence unproved;
- no arbitrary-rank theorem or global owner ledger;
- `C058`, `Q1`, and `Q2` unresolved;
- no novelty, publication, or prize claim.

The global project status remains `UNRESOLVED_AT_HARD_LIMIT`.

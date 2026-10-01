# Route C: C126 exact common completed-shell phase audit

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite common-phase scalar bank remains nonempty; `C058` remains open

## 1. Frozen finite question

C126 places the fixed C120 and C123 16-mark rows on the same completed-shell
phase rule

`T=H3/8=656/8=82`,

with common factor-two phase

`82 <= t <= 164`

and `rho=9/16`.  The two rows have the same `H2=430`, `H3=656`,
`eta_ratio=82/215`, and the same old-gap and new-gap multisets.  At this
completed shell endpoint the rule uses only the already exposed span
`a_15-a_7`; it is nonanticipating for this finite pair and scales linearly
under dilation.

This audit removes the row-dependent phase intervals used in C120 and C123.
It concerns only these two fixed rows in the current independent epoch-block,
zero-row-sum PSD cone.  It is not an arbitrary-rank statement and does not
establish a globally admissible C103 phase rule.

## 2. Complete common-phase exact replay

The common interval has different event partitions for the two ordered rows:

| row | exact chambers | epoch duals | nonnegative rational weights | endpoint positive-definiteness checks | normalized upper |
|---|---:|---:|---:|---:|---:|
| C120 | 147 | 294 | 90,552 | 588 | `< 89/1000` |
| C123 | 135 | 270 | 83,160 | 540 | `< 87/2000` |

For every chamber and each of the two epoch blocks, the verifier reconstructs
the demand coefficients, dual objective, and slack matrix with
`fractions.Fraction`.  Both rational endpoints of every slack matrix pass an
exact fraction-free Bareiss/Sylvester positive-definiteness check.  The full
`dt/t` integrals use rational atanh-series logarithm enclosures with explicit
positive tails.  File SHA-256 and internal payload SHA-256 values pin both
stored full-dual sources.

The accepted comparisons therefore do not depend on floating-point solver
status.  The stored numerical search is only the source of candidate weights;
the canonical claim comes from exact replay.

## 3. Exact scalar bank remains nonempty

Under the deliberately narrow calibration assumptions

`epsilon=A=e_2=0`

and one common scalar coefficient `B`, the C120 common-phase row gives the
clean necessary fence

`B < 29/25`.

The stronger C123 common-phase row gives

`B < 1133/2000`.

The independently replayed C121 row gives the clean necessary lower fence

`B > 1341/4000`.

Consequently the outward-rounded necessary fences leave the open window

`1341/4000 < B < 1133/2000`,

whose width is

`37/160`.

Nonemptiness is not inferred from those outward roundings.  The verifier also
checks the load-bearing exact inequalities directly: the rational witness
`B=1/2` lies strictly above the exact C121 lower bound and strictly below both
the exact C120 and C123 common-phase upper bounds.  Thus the exact finite
half-line system is noncontradictory.  This does not assert that every point of
the clean outer window is feasible.

Thus fixing the common phase does not refute all scalar storage coefficients.
In particular, the earlier adaptive phase-base difference is not by itself an
explanation for the surviving scalar bank.  C126 proves a finite
noncontradiction, not a master inequality and not a no-go theorem for a larger
storage cone.

## 4. Remaining C103 phase-rule obligation

For this fixed pair, `T=H3/8` is order-independent because both completed
shells have `H3=656`.  That does not prove that the same selection is legal or
useful along an arbitrary critical-compatible history.  A theorem-level use
still requires a global C103 owner/boundary ledger showing that completed-shell
phase choices can be selected and stitched without anticipation, ownership
duplication, or uncovered terminal terms.

Accordingly C126 closes only the finite C120/C123 phase-comparison caveat.  It
does not prove global C103 admissibility, representative independence beyond
this pair, arbitrary-rank control, or global owner stitching.

## 5. Canonical artifacts and hashes

- verifier: `ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.py`,
  SHA-256
  `830c6afa79d49d386e5bc57bdb5578b8074e783486cbaf991164ae25e91a5981`;
- compact certificate:
  `ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate.json`, SHA-256
  `b1a37954b11a807161d85d916a875058d9a4dab51a5dc208468429fe937074cf`;
- C120 full-dual source: `ROUTE_C_C126_COMMON_PHASE_C120_source.json`,
  SHA-256
  `ba68e13b5a70abe50d14784d4e8e6bd7cf70df4dacace162a28b3383b59627f1`,
  internal payload SHA-256
  `feaada44db91313200e0c5f719421d0572af06b44d40bc7c31419fae726da304`;
- C123 full-dual source: `ROUTE_C_C126_COMMON_PHASE_C123_source.json`,
  SHA-256
  `a47eff804bbdf4082ba61d60202855e2a22b86c2c771df44a1e6f5728e952fae`,
  internal payload SHA-256
  `7415bafcae9c37e043d8d6088fa5471f5916f595c367fde8222d4fe194ac52ab`;
- regression test: `ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_test.py`,
  SHA-256
  `6ce6bb99196f8762d0de67f8f08d795842c9964266bdaa5870d6cb8c206a725b`.

Pinned dependencies are the C120 exact model
`ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py`, SHA-256
`6e8d7e3f975e952442672cb1d18e4512d616f343bb4f6379ba0c8701cd996fe9`,
the C121 compact certificate
`ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.json`, SHA-256
`1288d87e095a47f9fdf679a40656bafdef4ad4b03150ccb3254b25b043937a0b`,
and its imported verifier source
`ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate.py`, SHA-256
`e568d5562dd8c51c82ff603d678cd712f3f3250398d927982fa9c3fcd0469953`.

The CLI self-check rejects twelve provenance, arithmetic, structure, conclusion,
and scope mutations.

## 6. Scope and status

- common fixed phase for C120 and C123 only;
- completed-shell rule `T=H3/8` and `rho=9/16` only;
- independent epoch-block cone only;
- scalar interval explicitly nonempty;
- global C103 phase-rule admissibility unproved;
- ordered-vector storage not refuted;
- no arbitrary-rank theorem or global owner ledger;
- `C058`, `Q1`, and `Q2` unresolved;
- no novelty, publication, or prize claim.

The global project status remains `UNRESOLVED_AT_HARD_LIMIT`.

# Route C: C125 exact five-row ordered-suffix outer bank

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite necessary-side bank remains feasible; `C058` remains open

## 1. Frozen scope

This audit combines five fixed 16-mark, `k=2`, `C=2`, `rho=9/16` rows in the
current independent epoch-block zero-row-sum PSD cone:

1. the positive-`Delta V` C118/C121 row;
2. the negative-`Delta V` C120 row;
3. the C123 same-multiset ordered permutation;
4. a second ordered row labelled index 12; and
5. a third ordered row labelled index 3.

Only the C119 scalar concentration column `V` and the C124 chronological
suffix column `V_rt` are used.  Every row is a finite dual-upper test.  The
bank contains no primal phase witness for the displayed coefficient vector
and no arbitrary-rank or global-owner statement.

## 2. Two new exact full-phase rows

The index-12 points are

`(0,22,60,83,102,312,442,513,579,682,791,882,944,1055,1100,1169)`.

Their adaptive phase is `[295/4,295/2]`.  Exact replay gives 149 chambers,
298 epoch duals, 91,784 nonnegative rational weights, and 596 endpoint
positive-definiteness checks.  The normalized dual upper is below

`42845139/1000000000`,

and `Delta V_rt=113/26445`.

The index-3 points are

`(0,22,60,83,102,173,303,513,579,690,759,868,930,1021,1124,1169)`.

The same adaptive phase has 155 chambers, 310 epoch duals, 95,480 stored
weights, and 620 endpoint positive-definiteness checks.  The normalized dual
upper is below

`6627733/100000000`,

and `Delta V_rt=-12913/58179`.

All objectives, demand coefficients, endpoint slack matrices, logarithm
enclosures, and source hashes are reconstructed exactly.  Floating solvers
were used only to discover candidate weight vectors and do not enter the
accepted comparisons.

## 3. Explicit coefficient vector not separated by the bank

The exact rational vector

`epsilon=A=1/1000`, `B=1/2`, `C=1/10`, `e_2=0`

is compared with the certified normalized dual-upper enclosure on every one
of the five rows.  The verifier uses exact rational upper bounds for
`log(1768/1659)` and `log(215/82)`.  On each row, the stored dual upper minus
the candidate target is strictly greater than

`1/10000`.

Thus these five dual tests do not separate the displayed coefficient vector.
Equivalently, the current two-column necessary-side outer bank is feasible.

This statement is deliberately one-sided.  A dual upper lying above the
target does not construct a feasible primal or prove the desired local master
inequality.  It shows only that the present finite no-go bank cannot reject
this rational vector.

## 4. Phase-base caveat remains load-bearing

The five rows do not share one physical phase interval.  C120 uses
`[553/8,553/4]`, C123 uses `[297/4,297/2]`, and the two new rows use
`[295/4,295/2]`, because the exploratory rule is
`T=(a_15-a_8)/8`.

Therefore C125 is not a theorem-level multi-history bank until the intended
nonanticipating phase rule is frozen or the factor-two average is proved
independent of its representative.  A separate fixed-phase audit using the
permutation-invariant completed-shell choice `T=H_3/8` is the next diagnostic.

## 5. Artifacts and hashes

- verifier:
  `ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate.py`, SHA-256
  `1d9f4d8ea7756eb89fa9e8cc5d44e15a6480057df82392afadd30cbcbcb48fe2`;
- compact certificate:
  `ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_certificate.json`, SHA-256
  `61ce287cda746b1a6d9174cee3306165d88542c239bb8f81a2222fec13b7bd56`;
- index-12 source:
  `ROUTE_C_C125_ORDERED_SUFFIX_ROW12_source.json`, SHA-256
  `8c30fc674f40c2376df7ff2f6bec3b318c9a48710f347197109c3863ee84d0ec`;
- index-3 source:
  `ROUTE_C_C125_ORDERED_SUFFIX_ROW3_source.json`, SHA-256
  `2bcad3750da0f885260f03a5e1d5f251a7901e21c16d59fe61d4d1fd75215348`;
- regression test:
  `ROUTE_C_C125_ORDERED_SUFFIX_FIVE_ROW_BANK_test.py`, SHA-256
  `f37fa3a44a483008582b91b8c9d577ff6b68bd63072eaa6c80069298ea938695`.

The focused family passes four tests and its self-check rejects twelve
provenance, arithmetic, candidate, and scope mutations.

## 6. Consequence for C058

One bounded ordered coordinate is not refuted, but this bank also supplies no
positive mechanism.  The next decision is phase-first: replay the C120/C123
same-multiset pair on one common permutation-invariant factor-two phase.  If
the rational candidate still survives, construct exact primals for it or add
the minimal ordered quarter-mass vector before any larger feature expansion.

Every surviving mechanism must then pass 32-mark or scalable
critical-compatible histories and one global C103 owner/boundary ledger.
C058, Q1, Q2, novelty, publication, and prize eligibility remain unresolved;
the global status is `UNRESOLVED_AT_HARD_LIMIT`.

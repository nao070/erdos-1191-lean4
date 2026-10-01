# Route C: C129 exact common-phase integrated primal sub-bank

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite selected-chamber primal sub-bank; `C058` remains open

## 1. Frozen finite question

C129 keeps the C128/C125 data fixed:

- C123 16-mark row
  `(0,22,60,83,154,284,494,513,575,620,711,777,880,989,1100,1169)`;
- common completed-shell phase `[82,164]` and `rho=9/16`;
- `epsilon=A=1/1000`, `B=1/2`,
  `C_ordered_suffix=1/10`, `e2=0`;
- the independent epoch-4 / epoch-8 zero-row-sum PSD block cone.

C128 proved that the fixed target cannot be paid separately on C123 chambers
`0,...,21`.  C129 asks the weaker integrated question: can rational primal
matrices on later chambers compensate the exact integrated deficits of those
22 early chambers?

## 2. Selected banks

The exact-deficit block is `0,...,21`.  The C128 floating screen ranked later
surplus chambers, and C129 exactifies the following nested choices.

| bank | later chambers | total chambers |
|---|---|---:|
| top six | `120,122,126,132,133,134` | 28 |
| sparse seven | `88,120,122,126,132,133,134` | 29 |
| robust ten | `43,88,119,120,122,124,126,132,133,134` | 32 |

“Top six / top seven” is a minimality witness only inside this frozen C128
numerical ordering.  C129 does **not** prove that no other exact six-chamber
choice could compensate the early block.

## 3. Exact primal representation

Each selected chamber has one reduced rational Gram factor for epoch 4 and one
for epoch 8.  All 64 stored factors have denominator `100000000`.  For a
chamber midpoint `m`, the physical matrix is replayed as

`Q = (1/(m*100000000^2)) * sum_j c_j c_j^T`.

The midpoint scaling is part of the exact certificate.  The reduced columns
are embedded into their 20- and 32-channel epoch blocks by appending the
negative coordinate sum, so every embedded column has zero row sum.  Positive
rational scaling of an integer Gram sum proves PSD without a floating
eigenvalue test.

The 64 exact ranks range from 9 to 24 and sum to 1004.  Independence of every
stored column family is witnessed modulo both `1000000007` and `1000000009`;
embedding and positive scaling preserve those ranks.  The sparse-seven bank
uses 58 factors with rank sum 910.

## 4. Strict ownership and endpoint replay

For every nonstructural generic owner row, the verifier checks the exact owner
inequality strictly at both rational chamber endpoints.  It separately
rebuilds every collapsed endpoint partition and checks all nonstructural owner
rows strictly there.  Structural-zero rows are accepted only when their exact
demand is nonpositive.

The robust-ten census is:

- 12,140 generic owner rows;
- 24,280 generic endpoint inequalities;
- 23,745 collapsed-endpoint owner rows.

The sparse-seven sub-bank has 10,987 generic rows, 21,974 generic endpoint
checks, and 21,500 collapsed-endpoint rows.  All are strictly positive.

At each collapsed endpoint the verifier reconstructs epoch-4 and epoch-8
demand and price separately and checks each value against its exact chamber
polynomial before checking the `rho=9/16` combination.  This prevents the two
epoch errors from cancelling in the weighted total.

## 5. Exact log-weighted margins

For each chamber the verifier constructs the exact polynomial
`P(t)=t*Phi(t)`.  It integrates
`P(t) dt/t^2 = Phi(t) dt/t`; a constant target `R` therefore contributes
`R*log(right/left)`.  Logarithms use 30-term rational atanh-series enclosures
with an explicit positive tail.  The C125 target interval is subtracted
outwards, and the selected-chamber totals are divided outwards by the exact
enclosure of `log(2)`.

| bank | exact raw log-weighted margin | exact `log(2)`-normalized margin |
|---|---:|---:|
| top six | approximately `-0.000046016210820238` | approximately `-0.000066387359150858` |
| sparse seven | approximately `+0.000068970153433814` | approximately `+0.000099502898328314` |
| robust ten | approximately `+0.000357552390724944` | approximately `+0.000515839060956870` |

The accepted exact clean fences are:

- top-six raw upper `< 0`;
- sparse-seven raw lower `> 1/15000`;
- sparse-seven normalized lower `> 99/1000000`;
- robust-ten raw lower `> 143/400000`;
- robust-ten normalized lower `> 103/200000`.

The decimal values are display-only.  Classification uses
`fractions.Fraction` throughout.  The summed raw enclosure width is about
`1.43e-27` and is not rounded inward.

For comparison, the discovery screen gave robust-ten raw margin
`0.000357549646069820`.  All 64 discovery solves were reported
`optimal_inaccurate`; none of those statuses or floats is used by the accepted
certificate.  Exact Gram, owner, endpoint-objective, target, and logarithm
replay determine the result.

## 6. What remains

The robust bank covers only 32 of the 135 C123 phase chambers.  The other 103
chambers are not exactified.  Their net contribution was positive in the C128
floating screen, but 15 individual remaining chambers were numerically
negative (`22--27`, `31--35`, `59`, `60`, `77--79`).  Those facts remain
heuristic until a larger rational bank is replayed.

C129 therefore proves only that the exact early deficit block `0--21` can be
paid by the stated selected later chambers inside this fixed finite cone.  It
does not provide:

- a complete C123 phase primal witness;
- a witness for C120 or any other phase;
- global C103 phase-rule admissibility or representative independence;
- a local master inequality, arbitrary-rank theorem, or global owner ledger;
- a resolution of `C058`, `Q1`, or `Q2`;
- a novelty, publication, prize, or correctness claim beyond this finite
  certificate.

The global project status remains `UNRESOLVED_AT_HARD_LIMIT`.

## 7. TDD, hardening, and provenance

The first focused test run was RED because the C129 verifier module did not
exist (`ModuleNotFoundError`).  After implementation, all ten focused tests
passed.  The standalone CLI exact replay also passed with 21/21 mutations
rejected.  Mutations cover schema/status/provenance, candidate and selection,
clean fences, forbidden scope upgrades, a rehashed factor edit, an arithmetic
factor scaling that reaches the owner replay, zero/drop/endpoint/rank damage,
noncanonical JSON rendering, and a controlled epoch-4/epoch-8 error whose
`rho=9/16` weighted sum cancels.  The latter is rejected by the separate epoch
endpoint-objective checks before the combined equality is considered.  A
second controlled mutation gives the two epoch owner-share recoveries errors
`+1` and `-1`; their combined physical-energy identity still holds, but the
epoch-4 recovery check rejects it before the combined check.
The final controlled owner mutation supplies a nonzero owner share together
with nonpositive demand on a row labelled structural-zero; the verifier now
requires the share itself to equal zero and rejects that case.  Exact rank is
required independently modulo each of the two pinned primes, not merely one
of them.

Pinned dependencies include the C125 verifier, C126 verifier/certificate,
C126 C123 source and internal payload, the exact phase model, and the C128
verifier/certificate.  The canonical JSON uses sorted compact rendering plus
a terminal newline.

Artifact identities at completion:

- verifier SHA-256:
  `b211bae87c7a29bd9a4ec32fbe53f104b6366f922c743f6273aa61e7d800ddb6`;
- certificate file SHA-256:
  `bdd23df5520408b09d6a9a3f8126a2ecd6b5ee68c18d3b5f5e7eb9e3c3375cf9`;
- test SHA-256:
  `f994f505f8c1b5c6555a9e1165116911e386b8d73cff3ddea0339d8d6f1ac874`;
- internal certificate payload SHA-256:
  `b1c484ec31d809d3abdca7331e4f9410feb39f007800405745ab3f22ea81241d`;
- factor-bank SHA-256:
  `9f4bf884515930a03502f785e0d6381d81fdd11be7cb01648370f19ce2b58e15`.

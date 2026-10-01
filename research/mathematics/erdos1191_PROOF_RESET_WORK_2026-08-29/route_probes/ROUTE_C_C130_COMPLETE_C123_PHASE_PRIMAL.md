# Route C: C130 complete fixed-C123 common-phase primal

Date: 2026-08-31 (Asia/Tokyo)  
Status: exact finite complete fixed-C123 phase witness; `C058` remains open

## 1. Exact statement

C130 fixes the same finite data as C125--C129:

- the C123 16-mark row
  `(0,22,60,83,154,284,494,513,575,620,711,777,880,989,1100,1169)`;
- common completed-shell phase `[82,164]` and `rho=9/16`;
- `epsilon=A=1/1000`, `B=1/2`,
  `C_ordered_suffix=1/10`, `e2=0`;
- the independent epoch-4 / epoch-8 zero-row-sum PSD block cone.

For this frozen row and candidate, C130 constructs an exact rational primal
factor on **every one of the 135 phase chambers**.  Unlike C129, no chamber is
omitted and no zero extension is used.  The exact log-phase integral over the
complete interval has strictly positive clean margin.

## 2. Exact Gram representation

Each chamber stores one reduced integer Gram factor for epoch 4 and one for
epoch 8, for 270 factors in total.  Every denominator is `100000000`.  At a
chamber midpoint `m`, each physical block is reconstructed as a positive
rational multiple of an integer Gram sum,

`Q = (1/(m*100000000^2)) * sum_j c_j c_j^T`.

The reduced columns are embedded into their 20- and 32-channel epoch blocks by
appending the negative coordinate sum.  Hence every embedded column has zero
sum and every reconstructed matrix is PSD without a floating eigenvalue test.

The 270 exact ranks range from 9 to 25 and sum to 4288.  Each stored column
family has full stated rank independently modulo both `1000000007` and
`1000000009`.

## 3. Ownership, structural zeros, and objective replay

The verifier uses exact `fractions.Fraction` arithmetic throughout.  It checks:

- 51,355 active generic owner rows at both endpoints, giving 102,710 strict
  endpoint inequalities;
- 100,183 active rows on the separately rebuilt collapsed endpoint
  partitions;
- 31,805 generic and 62,713 collapsed structural-zero rows, each requiring
  owned share exactly zero and demand nonpositive;
- the same 51,355 active and 31,805 structural-zero rows at rational chamber
  midpoints;
- 10,395 exact state evaluations, with 20,790 separate epoch-4/epoch-8 owner
  recovery checks;
- 540 separate endpoint epoch-objective identities and 270 weighted endpoint
  identities;
- 270 separate midpoint epoch-objective identities and 135 weighted midpoint
  identities.

The exact minimum active owner slack is

`1137298595103/235750000000000000 > 0`.

An independent scratch audit located it in chamber 78, epoch 8, owner `(8,8)`
at the left endpoint.  The accepted verifier independently freezes the exact
minimum value and rejects any changed census.

Separate epoch identities are checked before the `rho=9/16` combination, so an
epoch-4 error cannot be hidden by an opposite epoch-8 error.  The same rule is
applied to owner recovery and to both endpoint and interior objectives.

## 4. Exact complete-phase integral

For each chamber the verifier reconstructs the exact polynomial
`P(t)=t*Phi(t)` and integrates `P(t) dt/t^2`.  Every logarithm is enclosed by a
30-term rational atanh series with explicit positive tail.  The target is
subtracted outwards, and normalization by `log(2)` is also outward.

The exact accepted clean fences are:

- complete raw lower margin `> 1/400`;
- complete `log(2)`-normalized lower margin `> 91/25000`;
- total raw enclosure width `< 1/10^26`.

Exactly 37 chamber intervals are strictly negative:

`0--26, 31--35, 59, 60, 77--79`.

The other 98 are strictly positive.  Therefore the result is genuinely
phase-integrated: it does not claim a pointwise lower bound on each chamber.

## 5. Discovery data are not proof data

The temporary SDP run was used only to discover integer columns.  The accepted
JSON projects the source onto exact fields only: chamber index, rational
endpoints, denominator, exact rank, and integer columns.  It contains no
solver status, numerical matrix, eigenvalue, clipped value, numerical margin,
or floating-point value.  A recursive verifier gate rejects any float anywhere
in the accepted payload, and exact type gates reject Python equality confusions
such as `135.0 == 135` or `0 == False` after rehashing.

The stripped exact factor bank has SHA-256
`7d16af8eeba989c068e3d08ffaeff394cbf181a95cefa380834471f024d15173`.

## 6. Scope and remaining bottleneck

C130 is a complete common-phase primal witness only for the fixed C123 row in
the frozen independent epoch-block cone.  It does **not** construct or prove:

- a C120 phase primal or a corresponding witness for every row;
- the C103 phase rule or its Abel boundary/terminal ledger;
- global owner stitching, a global owner ledger, or representative
  independence;
- a local master inequality or arbitrary-rank theorem;
- `C058`, `Q1`, or `Q2`;
- novelty, publication acceptance, prize eligibility, or the full Erdős
  Problem #1191 theorem.

Thus C130 removes the remaining 103-chamber exactification gap left by C129,
but the cross-row/global stitching obligation remains the primary bottleneck.
The project status remains exactly `UNRESOLVED_AT_HARD_LIMIT`.

## 7. TDD and integrity

The focused test was RED before the verifier existed.  After implementation,
all nine focused tests passed.  The mutation barrier rejects 28/28 cases,
including schema/status/provenance changes, coefficient and selection changes,
clean-fence and census changes, forbidden C120/C103/global/C058 scope upgrades,
a rehashed factor edit, factor/rank/order/endpoint damage, controlled
cross-epoch cancellation, nonzero structural-zero ownership, a rehashed float,
and an integer substituted for an exact Boolean.  Noncanonical JSON rendering
is rejected.

Pinned identities at the initial canonical GREEN point:

- C129 replay verifier SHA-256:
  `b211bae87c7a29bd9a4ec32fbe53f104b6366f922c743f6273aa61e7d800ddb6`;
- C130 verifier SHA-256:
  `84c540a1c259a265064eb8fb7287c8b4d696ec64719b9d9a50738efa5fb7415b`;
- C130 certificate file SHA-256:
  `16dec361580b0f070c660a12f8f3f60a57baff0bbf10ae9e5c2f8e4ae13fb37d`;
- C130 test SHA-256:
  `0ae8a46e75e390814a69bd300b834fb498fce266030d8dce5afb498bdfd6bffa`;
- internal certificate payload SHA-256:
  `99b4af93ff095b9a8e03208e66860e2b3c15e6789ab54e7aa1943312207b2a14`;
- exact factor-bank SHA-256:
  `7d16af8eeba989c068e3d08ffaeff394cbf181a95cefa380834471f024d15173`;
- temporary discovery source SHA-256:
  `a03646cb510c5117d9975260d9a3af08672752428309fa9155fa31436c3f099f`.

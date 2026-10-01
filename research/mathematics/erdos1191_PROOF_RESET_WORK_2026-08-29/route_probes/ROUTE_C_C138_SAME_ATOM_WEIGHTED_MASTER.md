# C138: same-atom C133 link and weighted fixed-phase graph witness

Date: 2026-08-31 (Asia/Tokyo)  
Status: `EXACT_FIXED_PHASE_SAME_ATOM_WEIGHTED_GRAPH_FEASIBLE_C058_OPEN`

This is the canonical C138 finite route-probe record. The identifier is C138,
not C137; C137 is assigned to a different exact local no-go.

## 1. Result and exact scope

On the explicit C132 32-mark fixture and only at

```text
t = 17745/32,
w8 = 1,
w16 = 9/16,
active multipliers = 1,2,4,8,
```

there is an exact 57-root nonnegative graph-Laplacian capacity on the 100
channels `(rank,multiplier)`, `7 <= rank <= 31`, which satisfies all 1,192
correctly weighted direct owner-cell inequalities. Its unweighted physical
price has a strictly positive exact master margin:

```text
weighted direct demand D = 1305537/16384,
physical graph price P   = 2367807877181/16716398592,
2D-P                     = 296239592131/16716398592 > 0.
```

The same direct-M atoms give a non-free prefix/scale potential for which the
frozen C133 fourteen-row identity is literally the Abel reindexing of `D`.
The two upper terminals vanish exactly on this fixture.

This is a bounded fixed-fixture, fixed-midpoint result. It proves no phase
interval, phase rule, arbitrary history, arbitrary rank, horizon-uniform C103
ledger, C058, Q1, Q2, publication novelty, or prize eligibility.

## 2. The non-tautological same-atom potential

For epoch size `n in {4,8,16}` and scale `s in {0,1,2,3,4}`, let
`m=2^s`, `T_s=m t`, and use the normalized physical Haar state

```text
q_(r,s)(x) = (8/m) * (1_[a_r,a_r+T_s)(x)-1_[a_r+T_s,a_r+2T_s)(x)).
```

For ranks `n-1,...,2n-1`, define

```text
U_(n,s)(x) = q_(n,s)(x)^T M_n q_(n,s)(x),
```

with the same exact direct matrix `M_n` used by the owner demand. Freeze

```text
C8_s  = U_(4,s),
C16_s = U_(4,s)+U_(8,s),
C32_s = U_(4,s)+U_(8,s)+U_(16,s).
```

No `C8_s`, `C16_s`, or `C32_s` is an optimization variable. Pointwise,

```text
C16_s-C8_s   = U_(8,s),
C32_s-C16_s = U_(16,s).
```

Consequently the C133 left side is identically

```text
sum_(s=0)^3 [w8*(2^s/128)*U_(8,s)
             +w16*(2^s/128)*U_(16,s)],
```

which is precisely the weighted direct-demand density. The exact replay
checks this equality and the fourteen-row Abel equality on all 202 cells of
the complete joint direct-M endpoint partition, with 2,020 prefix-increment
checks.

This removes the C136 box-carrier mismatch: the potential is built from the
actual direct-M atoms, not from a separately chosen carrier and not from free
prefix values.

## 3. Why multiplier 16 is not a missing graph channel here

The earlier C136 box carrier had two nonzero scale-4 rows. That carrier was
the wrong potential for the direct demand. For the correct same-M potential,

```text
16t = 17745/2,
H4  = a7-a3   = 430,
H8  = a15-a7  = 656,
H16 = a31-a15 = 5915,
```

and `16t` exceeds all three spans. Exact cell replay gives

```text
U_(4,4)=U_(8,4)=U_(16,4)=0
```

on every one of the 202 ledger cells (606 terminal-state checks). Thus both
C133 upper terminals are literally zero. Adding a multiplier-16 graph bank
would be an unrelated extra capacity source, not payment of a nonzero direct-M
terminal.

This vanishing is essential to the interpretation of `2D-P`: there is no
unpriced multiplier-16 terminal loan left outside the four active-scale
demand. If the same-M terminal rows were nonzero on another fixture or phase,
this finite margin would not by itself close their boundary payment.

## 4. Exact graph LP and owner equations

Let the 100 active channels be the ranks `7..31` at multipliers `1,2,4,8`.
For every unordered channel pair `a<b`, set

```text
G_ab=(e_a-e_b)(e_a-e_b)^T,
G=sum_(a<b) y_ab G_ab,   y_ab>=0.
```

There are 4,950 candidate roots. On each of the 149 physical endpoint cells,
for each epoch `e in {8,16}` and active multiplier `m`, the direct owner group
contains exactly ranks `e,...,2e-1` at multiplier `m`. Its linear projection
is

```text
S_(e,m)(x)=(P_(e,m)q(x))^T G q(x).
```

The frozen inequalities are

```text
S_(e,m)(x) >= 0,
S_(e,m)(x) >= w_e*(m/128)*U_(e,s)(x),  m=2^s.
```

The epoch weights occur only on these right-hand sides and in `D`. The graph
matrix and its physical price are not weight-rescaled:

```text
P = integral q(x)^T G q(x) dx.
```

The full coordinate fibers `rank7`, `ranks8..15`, and `ranks16..31` partition
all 100 coordinates, so their linear owner shares sum cellwise to the single
unweighted physical price. The previously unchecked pre8/rank7 share is also
nonnegative on every cell:

```text
pre8 rows             = 149,
zero / positive       = 145 / 4,
integrated pre8 share = 6489/256.
```

Thus there is no hidden negative past-owner subsidy.

The owner projections are not equated row-by-row with individual signed C133
bands. The exact relation is instead:

1. each owner projection dominates its weighted direct-M prefix increment;
2. the fourteen signed C133 rows sum exactly to those weighted direct-M
   increments; and
3. all owner fibers recover the one physical graph price, which satisfies
   `P<2D`.

This is the correct finite payment relation. A forced local equality between
an arbitrary graph row and each Abel band is stronger and is not assumed.

## 5. Exact certificate

Numerical HiGHS discovery found a 57-root support. No numerical coefficient or
solver status is accepted. Exactification selects 57 tight owner rows whose
integer coefficient matrix has rank 57 modulo `1000003`, then solves the
57-by-57 system using `Fraction`. Every recovered coefficient is positive.

Exact replay gives:

```text
graph roots / rank            = 57 / 51,
owner rows                    = 1192,
tight / strict                = 884 / 308,
zero / positive capacities    = 807 / 385,
minimum positive owner slack  = 5/65536,
pre8 nonnegative cells        = 149/149,
weighted D                    = 1305537/16384,
physical P                    = 2367807877181/16716398592,
positive margin 2D-P          = 296239592131/16716398592.
```

The graph is PSD by its explicit nonnegative rank-one root sum and has exact
zero row sums.

## 6. C133 row census and degeneracy warning

All fourteen formal C133 keys are retained, but only five integrated rows are
nonzero on this fixture:

```text
band:A16:s0 = 252609/16384,
band:A32:s0 = 19452807/1048576,
band:A32:s1 = -12662595/2097152,
band:A32:s2 = 804195/65536,
band:A32:s3 = 82797525/2097152.
```

The four `A8` initial rows, `A16:s1,s2,s3`, and both upper terminals are zero.
Therefore this fixture does **not** stress a nonzero initial-history boundary
or nonzero terminal payment. It is an exact same-atom/link and weighted
capacity success, but still a degenerate boundary instance. A future phase or
history test must include nonzero initial and terminal rows before any global
claim.

## 7. Reproduction

From `route_probes/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate.py --self-check
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_independent_oracle.py
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_test.py
```

The certificate JSON already stores the exact rational support; no numerical
solver is called by these commands. The independent oracle uses only the
Python standard library and does not import C136 or the certificate verifier.

## 8. Remaining bottleneck

The next gate is no longer the finite same-atom charge map at this midpoint.
It is to obtain a nonanticipating construction over a complete factor-two
phase interval and then promote it to arbitrary adjacent dyadic epochs while
retaining nonzero initial/cutoff/terminal history rows in one global C103
ledger. This fixed example gives no uniformity theorem and does not close
C058.

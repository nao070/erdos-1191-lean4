# C136 fresh joint epoch-8/16 master: exact bounded result

Date: 2026-08-31 (Asia/Tokyo)  
Status: `EXACT_SINGLE_PHASE_DIRECT_OWNER_GRAPH_FEASIBLE_C133_FIXTURE_PHASE_BOX_CARRIER_INSTANTIATED_UNLINKED_PAYMENT_UNKNOWN_C058_OPEN`

This is a finite Route-C certificate.  It does not modify any earlier claim.

## 1. Frozen fixture and phase

The explicit forward C132 composite is

```text
(0,22,60,83,102,173,303,513,616,727,772,881,972,1041,1103,1169,
 1239,1349,1539,1654,2009,2659,3709,3804,4114,4339,4794,5124,
 5639,6184,6739,7084).
```

Exact integer replay finds all 496 positive differences distinct, so this is
a 32-mark Golomb/Sidon-valid fixture of span 7084.  The experiment fixes the
one common physical phase

```text
phase interval = [5915/16, 5915/8]
t              = 17745/32  (the exact midpoint only).
```

Nothing here proves feasibility throughout the phase interval.

## 2. Fresh graph-root LP

There are 100 Haar coordinates `(rank,multiplier)`, with ranks 7 through 31
and multipliers `1,2,4,8`.  At the fixed phase, the 150 collapsed endpoints
give 149 open cells.  The exact state on each cell is the midpoint Haar state.

For every unordered pair of coordinates `a<b`, let

```text
G_ab = (e_a-e_b)(e_a-e_b)^T,
Y    = sum_(a<b) y_ab G_ab,       y_ab >= 0.
```

Thus the discovery LP has 4,950 nonnegative variables.  For each of the 149
cells and each direct owner `(epoch,multiplier)`, where epoch is 8 or 16, it
imposes

```text
<P_owner q, Y q> >= (multiplier/128) q_state^T M_epoch q_state.
```

The epoch-8 state is ranks 7..15 and owns 8..15.  The epoch-16 state is ranks
15..31 and owns 16..31.  Hence rank 15 belongs to epoch 8 exactly once.  This
is 149*8 = 1,192 cell-owner inequalities: 596 using full M8 and 596 using full
M16.  The objective minimizes the exact physical graph price

```text
P = sum_cells |cell| q^T Y q.
```

A scratch-only SciPy/HiGHS LP run was used only to discover a 57-root basic
support.  No numerical package is imported by the accepted canonical
artifacts: the graph-root parameterization makes PSD exact by construction,
and the stored coefficients are recovered by an exact rational solve.  The
accepted evidence is the standalone `Fraction` replay, not the numerical
solver status or objective.

The verifier independently selects 57 tight owner rows whose integer
coefficient matrix has rank 57 modulo `1000003` (hence rank 57 over the
rationals), solves that 57-by-57 system with `Fraction` Gauss-Jordan
elimination, and obtains the stored positive support exactly.

## 3. Exact graph result

The 57 coefficients are all strictly positive.  Therefore `Y` is PSD by an
explicit sum of rank-one Gram roots.  Its row sums vanish exactly; its exact
graph rank is 51.  This is one fresh global matrix and is not a pasted C130 or
C131 local factor.

Exact replay gives:

```text
active events / cells                 150 / 149
candidate roots / positive support   4950 / 57
owner-cell rows                       1192
nonnegative owner capacities          1192 = 807 zero + 385 positive
demand sign census                    40 negative + 971 zero + 181 positive
constraint slacks                     884 tight + 308 positive
integrated direct demand D            457/4
physical graph price P                1878008419901/9402974208
2D-P                                  270571186627/9402974208 > 0
owner fiber sizes                     pre8=4, epoch8=32, epoch16=64
```

Accordingly, the fixed-midpoint direct-owner graph-root subcone is **exactly
feasible**.  No LP optimality claim is needed for this feasibility witness.

## 4. Full M16 and the residual-63 gate

Every epoch-16 row uses the natural 17-state `M16`, never a quarter-scaled
two-`M8` replacement.  Exact reconstruction records:

```text
Gamma8 sources / alpha mass          21 / 329/256
Gamma16 sources / alpha mass        105 / 5425/1024
omitted cross-half sources / mass    63 / 4767/1024
R16 nonzero offdiagonals             160 ordered / 80 unordered
R16 samples                           -1/32, 15/2048, 1/1024
```

`R16` has zero diagonal and zero row sums but mixed signs.  The vectors
`e0+e8` and `e1+e8` give exact quadratic values `-1/16` and `15/1024`, so the
C134 signed representation is not treated as PSD capacity.  The fresh LP
instead carries the full M16 demand directly.

## 5. Same-fixture/phase box-carrier C133 instantiation

On the same fixture and same phase, define the one-sided box-pair prefix
carrier pointwise by

```text
C_(P,s)(x) = (a_(P,s)(x)^2-a_(P,s)(x))/(2^s t)^2,
```

where `a_(P,s)(x)` counts intervals `[p,p+2^s t)` from prefix `A_P` that
contain `x`.  Use `w8=1`, `w16=9/16`, and
`c_s=2^s/128` for `s=0,1,2,3`.

All scale-4 terminal endpoints are included.  The 192 endpoints give 191
cells.  Exact replay checks the C133 identity on every cell, as well as 1,910
unique-pair-birth equalities.  Both birth banks are present (92 and 376 pair
atoms).  The 18 raw occurrences stitch to exactly 14 box-carrier keys:

```text
4 A8 initial bands + 4 net A16 shared bands + 4 A32 final bands
+ 2 width-16t upper terminals.
```

All fourteen integrated rows are nonzero and their sum equals
`10229179/1007632080`, independently reproduced by exact pair-overlap
integration.

This carrier is **not** the potential generating the direct M8/M16 demand.
The exact joint endpoint cell

```text
[44701/4, 46081/4), midpoint 45391/4
```

has box-carrier C133 left-hand density `0`, whereas

```text
sum_e w_e sum_m direct_demand(e,m) = 225/32768.
```

Only the unweighted `(epoch16,multiplier8)` direct component is nonzero, with
value `25/2048`.  The carrier rows `band:A32:s3` and `terminal:e16:s4` are
nonzero but cancel on this cell.  This is an exact counterexample to any
identification of the two potentials, not a normalization discrepancy.

For this deliberately separate box carrier, both integrated scale-4 terminal
rows are nonzero (`253807/111959120` and `6604809/1791345920`), while the graph
contains multipliers only `1,2,4,8`.  This is an additional failure of this
carrier-to-graph identification.  It is not a generic terminal obstruction
for a different potential built from the direct `M8/M16` atoms.

## 6. Classification and missing link

These are two exact but currently unlinked facts:

1. `EXACT FEASIBLE`: one fixed-phase direct-owner graph-root capacity satisfies
   all 1,192 M8/M16 cell constraints and `P<2D`.
2. `EXACT INSTANTIATED BUT UNLINKED`: a separate box-pair carrier on the same
   fixture and phase has all fourteen C133 initial/shared/final/terminal rows
   with its carrier-ledger coefficients.

The graph price is an arbitrary cross-rank/cross-width PSD energy.  The exact
countercell proves that the audited box carrier is not its direct-demand
potential.  No proved charge map assigns the graph price to those fourteen
box-carrier rows with all boundary, birth, cutoff and terminal ownership.
Therefore payment of that carrier is **UNKNOWN**, not feasible and not
infeasible.

In particular this result does not establish phase-interval feasibility, a
phase-integrated master, a nonanticipating phase rule, a global C103 owner and
boundary ledger, arbitrary histories, arbitrary ranks, C058, Q1, or Q2.

## 7. Replay

```bash
cd /Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29

PYTHONDONTWRITEBYTECODE=1 python3 -B \
  route_probes/ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate.py --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  route_probes/ROUTE_C_C136_JOINT_GRAPH_MASTER_test.py

PYTHONDONTWRITEBYTECODE=1 python3 -B \
  route_probes/ROUTE_C_C136_JOINT_GRAPH_MASTER_independent_oracle.py
```

The main verifier, tests, and independent oracle require only the Python
standard library and accept the exact rational certificate.

## 8. Post-audit correction: the load-bearing gap is weighted price

After C136 was frozen, an exact audit assembled the cumulative potential from
the same direct matrices instead of the unrelated one-sided box carrier.  If
`U8_s` and `U16_s` are the direct `M8/M16` quadratics, set

```text
C8_s  = B_s,
C16_s = B_s + U8_s,
C32_s = B_s + U8_s + U16_s.
```

Then the two prefix increments are exactly `U8_s` and `U16_s`, so the C133
left side is the weighted direct demand for `w8=1`, `w16=9/16`, and
`c_s=2^s/128`.  On this fixture `16t=17745/2` exceeds the three direct-block
spans `430`, `656`, and `5915`; exact cell enumeration gives zero for all
three scale-4 direct-`M` quadratics.  Thus C133 still retains both formal
terminal rows, but the correct same-atom terminals evaluate to zero here.
The nonzero terminals above belong only to the rejected box carrier.

C136 optimized the unweighted direct sum.  The exact weighted demand is

```text
D_weighted = 1305537/16384,
2*D_weighted - P = -379481718413/9402974208 < 0.
```

Consequently the current 57-root witness does not prove the weighted C133
master.  The next honest computation is a fresh weighted same-atom graph
optimization.  This correction narrows C136; it does not invalidate the
stored unweighted feasibility certificate.

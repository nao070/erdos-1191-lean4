# Future-addition monotonicity candidate: bounded exact check

2026-09-09. Result: no negative deficit increment in 9108 steps of the
two existing certified C=1,m0=2,M=96 histories. This is finite evidence
only; monotonicity for all actual Sidon histories remains UNPROVED.

Fix b,l,n=b-1. The actual old pair-sum bank

    U={a_u+a_v:1<=u<=l<v<=n}

has no repeated value, by repeated-sum Sidon and the disjoint left/right
rank intervals. Its size is exactly l(n-l). After future ranks b+1..k,
let m=k-b, d=min(l,n-l,m), and v_z count the actual tripartite fibers.
Adding a_(k+1) changes v_z to v_z+w_z, where

    w_z=1[z in a_(k+1)+U],  J=sum_z w_z*v_z.

No pair-sum multiplicity is suppressed: its absence was checked directly
for each actual U. Write d'=min(l,n-l,m+1). The tested exact increment
formula is

    delta_after-delta_before
      =(d'-d)|U|m+(d'-1)|U|-2J.                      (1)

It follows by expanding (v+w)(d'-v-w)-v(d-v), using w^2=w,
sum v=|U|m and sum w=|U|. Once d is saturated, (1) becomes
(d-1)|U|-2J. This identity alone does not imply a sign. Monotonicity
would require an additional bound on the ACTUAL collision increment J.

The bounded scan was exactly:

| b | l range | k before addition | Histories | Steps | Negative increments | Minimum on nontrivial l |
|---:|---|---|---:|---:|---:|---:|
| 24 | 1..22 | 25..95 | 2 | 3124 | 0 | 30 |
| 12 | 1..10 | 13..95 | 2 | 1660 | 0 | 12 |
| 48 | 1..46 | 49..95 | 2 | 4324 | 0 | 66 |

b=24 was tested first; only its failure to produce a negative increment
triggered the explicitly permitted b=12 and b=48 checks. T=96 is fixed
throughout. Each step adds the actual next point of the saved history;
neither a point, a gap, a cap nor an onset is refitted. There were 804
zero increments, exactly at l=1 or l=n-1 where every fiber has size at
most one and delta is identically zero. All other 8304 increments were
strictly positive in this bounded sample.

The minimal code maintains the actual integer fiber Counter. J is
computed directly at the new shifted old-pair-sum sites before adding
them. It checks the Sidon fiber capacity after each addition, tests (1)
using exact integer arithmetic, and independently reconstructs
sum_z v_z(d-v_z) from the full final Counter for every fixed b,l.
Existing input hashes are matched to the independent certificates.
No core record generation, new history or large search was performed.

`tripartite_deficit_increment_existing.py` reproduces only this bounded
check. `tripartite_deficit_increment_existing_exact.json` records all
per-(history,b,l) counts and exact smallest increments, endpoint deltas,
scope, source hashes, and `first_negative: null`. There is no negative
witness or invented prefix/pair-bank certificate to report. The actual
input arrays remain in the named canonical M96 files bound by hash.

This result does not prove an all-history sign for (1), an unbounded
deficit lower estimate, or summability of the priced actual BH profile.
If pursued, the next independent mathematical step is an actual bound
on J retaining the pair-sum and future endpoint correlations, or a
targeted actual Sidon construction that breaks it. The frozen theorem
and Q1 remain unresolved; no Lean verification is claimed here.

## Subsequent targeted result

A separately prescribed fixed C=1000000,m0=2,M11 actual Sidon history
now gives delta 24 to22 under one future addition. It independently
refutes the all-cap raw monotonicity candidate; see
`RAW_DEFICIT_MONOTONICITY_SIDON_COUNTEREXAMPLE.md`. This does not change
the exact finite no-negative result of the C=1 scan recorded above,
and does not supply a core/Q1 counterexample (its core is empty).

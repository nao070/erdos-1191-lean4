# Actual Sidon counterexample to raw tripartite deficit monotonicity

2026-09-09. Independent certification PASS. This rejects the specific
future-addition monotonicity candidate for the RAW tripartite capacity
deficit. The unchanged strict core is empty; this is not a core-profile,
uniform-K or Q1 counterexample.

## The one prescribed fixed-cap history

The campaign fixed C=1000000,m0=2,M=T=11 and this exact sequence before
checking it; no search or modification was performed:

    a=(1,18,1000,1011,1024,2000,
       99959,99993,99994,99996,100000).

The existing evaluator verifies all 55 positive differences are unique.
The separate independent checker verifies repeated two-sum uniqueness,
including doubled endpoints, all intermediate-rank caps, every strict
core record and the full exact profile. All checks PASS, with zero
UNKNOWN logarithmic comparisons. The same fixed C and m0 apply before
and after appending the last point.

Take b=6,l=2, so the old rank prefix n=b-1=5 is split into

    L={a_1,a_2}={1,18},
    R={a_3,a_4,a_5}={1000,1011,1024}.

The rank-b point a_6=2000 is not in either old part or the chosen future
set; this is the original cut convention. The actual pair-sum bank is

    U=L+R={1001,1012,1018,1025,1029,1042},

with all six sums distinct. The future before addition consists of
a_7,...,a_10={99959,99993,99994,99996}. We add the actual next point
a_11=100000. The capacity is saturated both times:
d=min(2,3,m)=2, with m=4 then m=5.

## Complete raw fiber change

Before addition, the 6*4=24 triples have 24 distinct sums, all fibers
of size one. Thus C_before=0 and

    delta_before=sum_z v_z(2-v_z)=24.

The six new shifted sites are 100000+U. Four hit an existing size-one
fiber. Their complete equalities are:

| Sum | New triple | Old triple | Output (i,r) | t | BH type |
|---:|---|---|---|---:|---|
| 101001 | 1+1000+100000 | 18+1024+99959 | (7,11) | 41 | plus / 3 |
| 101012 | 1+1011+100000 | 18+1000+99994 | (9,11) | 6 | minus / 2 |
| 101018 | 18+1000+100000 | 1+1024+99993 | (8,11) | 7 | minus / 2 |
| 101025 | 1+1024+100000 | 18+1011+99996 | (10,11) | 4 | minus / 2 |

Every equality has six distinct actual endpoints. The other two new
sites, 101029 and 101042, were absent and create size-one fibers. Thus
after addition there are 22 fibers of size one and four of size two,
containing 22+2*4=30 triples. This is the full fiber enumeration:

    C_after=4,
    delta_after=22*1*(2-1)+4*2*(2-2)=22.

Equivalently J=sum_z w_z*v_z=4 at the new sites, so the exact saturated
increment formula gives

    delta_after-delta_before
       =(d-1)|U|-2J=6-8=-2<0.

Both sides were independently computed from the complete before/after
fiber lists, not only inferred from the increment formula. The matching
correspondence is one plus and three type-2 minus records; the AC-only
type-1 matchings are not extra raw BH collisions.

## Strict core and logical scope

The original strict core has exactly ZERO records in this M=T=11
history, and every original profile coefficient and N is zero. In
particular all four newly displayed raw collisions have latest old
birth c<=5 and output r=11, so they fail r<c log(c). This illustrates
why raw tripartite collisions must not be silently substituted for
strict core records. The evaluator and independent checker separately
certify that no other matching supplies a hidden core record.

The result is an actual integer Sidon counterexample under one fixed
finite cap to the universal raw-deficit monotonicity candidate. It is
stronger in this specific respect than the earlier scalar relaxation,
which was not Sidon. It does not exhibit a large or divergent core
profile, does not negate U4-F or Q1, and does not prove any failure of
a more refined potential containing price, gate or width terms.

The prior 9108-step scan at C=1 found no negative increment; that finite
statement remains correct. This specified C=1000000 example shows why
that scan could not justify an all-history monotonicity premise. It does
not settle the narrower question restricted to C=1.

## Reproduction and saved evidence

- `deficit_monotonicity_M11_exact.py`: checks ONLY this prescribed
  sequence with the existing evaluator and independent checker.
- `C1000000_m02_M11_deficit_target/campaign_fixed_before_check.json`:
  exact fixed inputs, one history and zero search trials.
- That directory's `C1000000_m02_M11_deficit_target.json`,
  `_records.json` and `_independent_check.json`: canonical certification.
- `raw_deficit_monotonicity_counterexample_exact.json`: the full actual
  prefix, duplicate-free pair-sum bank, all before/after fibers and
  collisions, all new sites, direct deficits, and source/checker hashes.

No further finite search was performed. The next mathematical step must
retain the exact increment and handle its possible negative sign, or
replace raw monotonicity by a correctly compensated potential. No Lean
verification or frozen-goal completion is claimed.

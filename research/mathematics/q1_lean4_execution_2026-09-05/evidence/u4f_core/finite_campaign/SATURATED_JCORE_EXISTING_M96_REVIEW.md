# A20 bounded check: saturated new strict-core BH collisions

2026-09-09. Result: NO strict counterexample in the two existing certified
C=1,m0=2,M=T=96 histories. The all-history saturated inequality remains
UNPROVED. No new history or raw tripartite-fiber scan was performed.

## Source binding confirmed before the count

The current A16-A19 section SHA-256 values exactly matched their final
independent review manifest. The whole WORKING_PROOF file at that check
had SHA-256
`171807b9727b1b3cddce87594439a752b7db109856e27fe0a2325b960046ca75`.
The new result JSON retains those four section hashes. This attack uses
the same original strict gates and unpriced BH matching definition.

## Exact candidate and finite domain

At a new upper output rank r, put n=b-1, m_before=r-1-b,
d=min(l,n-l), and S=l(n-l). The saturated stage means m_before>=d;
it is the capacity BEFORE adding the point a_r. The tested claim is

    J_core(b,l,r) <= (d-1)S/2,

where J_core counts only original strict-core type-2 minus and type-3
plus BH matching records satisfying

    c<b<i<r,  q<=l<s,

for their sorted old quadruple (p,q,s,c). The type-1 minus matching is
AC-only and is not counted. All original strict log/physical conditions
were already certified in the input record banks and remain unchanged.

The nontrivial scanned domain is

    5<=b<r-1, r<=96, 2<=l<=b-3, min(l,b-1-l)<=r-1-b.

There are 82,335 such triples (b,l,r) per history, 164,670 total. Cases
b<5 have no old quadruple. At l=1 or l=b-2 the side capacity is one,
the candidate bound is zero, and J_core is zero by the distinct old
endpoint order; the aggregate grids also confirmed these boundary zeros.
Pre-saturation cases are outside this candidate and already have the
separate proved nonnegative-increment argument of A19.

## Result and exact worst cases

For each cell the ratio is 2J_core/((d-1)S). All comparisons and maxima
were computed by exact integer/rational arithmetic.

| Existing history | BH records used | Saturated cells | Cells with J_core>0 | Worst ratio | A worst (b,l,r) | d | S | J_core | Bound |
|---|---:|---:|---:|---|---|---:|---:|---:|---:|
| Greedy | 128446 | 82335 | 68913 | 3/8 | (11,2,14) | 2 | 16 | 3 | 8 |
| Variant 1 | 131890 | 82335 | 68765 | 1/3 | (12,9,17) | 2 | 18 | 3 | 9 |

The greedy maximum is also attained at (11,8,15); the variant maximum
is also attained at (15,12,19), with S=24,J_core=4,bound=12 there.
All tied maxima are saved. At the displayed worst cells the exact
effective-deficit increments are 16-2*3=10 and 18-2*3=12, respectively.

The first greedy worst cell's three records have (d_source,e_source,
c,s,i,r,t) equal to

    (64,30,9,7,13,14,34),
    (65, 6,9,4,12,14,59),
    (79,20,10,6,12,14,59).

They are two type-2 minus records and one plus record. The first variant
worst cell's three records are

    (87,59,11,10,16,17,28),
    (101,22,11,10,15,17,79),
    (104,76,11,10,16,17,28),

one type-2 minus and two plus records. These tuples abbreviate the full
endpoint rows saved in the result JSON; they do not discard endpoint
conditions in the computation. The actual prefixes through these outputs
and each original source endpoint pair are saved there as well.

The complete source record banks were aggregated with a simple exact
rectangle count: a record contributes once on c+1<=b<i and q<=l<s at
its one actual upper output r. No cut endpoint is enlarged and no BH
matching gets a second allowance. This does not re-enumerate raw fibers.
Each reported first worst cell was independently reconstructed by direct
filtering of its original records, with physical differences, six distinct
endpoints and strict gates rechecked by the existing independent checker
routines; UNKNOWN=0. The canonical input hashes match their independent
certificates. Both campaigns keep their original C=1,m0=2 at every rank.

Passing the full strict-core count implies passing for every fixed subset
of these same old quadruples on these finite inputs, including the all-
large-old-gap selection. It does not establish a uniform bound for
different histories or larger M, and a fixed ratio such as 3/8 must not
be promoted to an all-history margin.

## The concrete saturation obstruction left for analysis

At each new shifted pair-sum site z, Sidon capacity AFTER adding the
new point gives v_old(z)+1<=d, so v_old(z)<=d-1. Summing over S new
sites yields only

    J_core<=J<= (d-1)S.

This is TWICE the upper bound needed for a nonnegative saturated
effective-deficit increment. The raw M11 example shows that improving
this to the desired half using raw fiber capacity alone is false. Its
strict gates delete those collisions, but that particular deletion does
not prove a uniform gate saving.

More precisely, if R_new=J-J_core is the actual number of newly created
raw collisions removed by the chosen gates, then

    Delta D_eff=(d-1)S-2J+2R_new.

Whenever raw J exceeds (d-1)S/2, the desired inequality requires the
specific compensation

    R_new >= J-(d-1)S/2.

The existing rank-only capacity bounds and nonnegativity R_new>=0 do
not supply that compensation. Establishing it requires the actual joint
endpoint/gate structure, or the fixed cap plus additional correlations.
This is the concrete missing inequality after saturation, rather than
an unsupported assertion that the sampled ratios persist.

## Evidence and next nonduplicate action

- `saturated_Jcore_existing_M96.py`: narrow exact record aggregation,
  source-review hash checks and independent worst-cell verification.
- `saturated_Jcore_existing_M96_exact.json`: exact worst ratios and ties,
  worst-by-b and worst-by-r cells, domains/counts, full witness rows,
  actual prefixes, input/source hashes and the empty violation lists.
- `saturated_Jcore_existing_M96_manifest.json`: this attempt's exact
  claim, assumptions, scope, proof obstruction and source binding.

The next task is an analytical gate/cap-sensitive estimate or a targeted
actual strict-core construction addressing that missing compensation.
No additional histories, empty-core fixtures or raw-fiber sweeps were
launched. The saturated candidate, weighted BH norm, U4-F constant and
Q1 remain unresolved, and no new Lean verification is claimed.

## Subsequent bounded counterexample

The unchanged finite C=1 scan above remains true. One later explicitly
fixed C=10^14,m0=2,t64,M156 actual history gives J_core71>64 and
D_eff decrement14, refuting the universal saturated candidate even
in the all-large-old-gap remainder. Its same-history full profile
passed the independent checker. See
`COLORED_STAR_STRICT_CORE_MONOTONICITY_COUNTEREXAMPLE.md`; the earlier
not-yet-proved status above is historical, not the current frontier.

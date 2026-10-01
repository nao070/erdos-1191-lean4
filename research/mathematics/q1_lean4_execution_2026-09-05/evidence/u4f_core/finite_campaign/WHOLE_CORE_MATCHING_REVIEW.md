# Exact whole-core regrouping by four old endpoints

2026-09-09. Independent algebraic and bijection review, with coefficientwise
checks on the two existing independently certified M=96 histories. No new
size campaign, evaluator, or Lean run. This represents the entire strict
six-endpoint core, rather than the small same-(c,e,i) paired subclass.

## Three matchings, with their actual birth clocks

For four old endpoint ranks p<q<s<c put

```
A=a_q-a_p, B=a_s-a_q, C=a_c-a_s, H=A+B+C=a_c-a_p.
```

Here H is the width of this quadruple; it need not equal the global H_c.
The three unordered matchings into two positive source labels are:

| Type | Endpoint matching | Positive source labels | Product | Numeric output | Earlier birth |
|---|---|---|---|---|---|
| 1 | (p,q),(s,c) | {A,C} | AC | t_minus=abs(C-A) | q |
| 2 | (p,s),(q,c) | {A+B,B+C} | AC+BH | t_minus=abs(C-A) | s |
| 3 | (q,s),(p,c) | {B,H} | BH | t_plus=A+C | s |

The type-2 identity is
(A+B)(B+C)=AC+B(A+B+C). Its label difference is C-A. Type 3 has
H-B=A+C. Sidon uniqueness prevents A=C: the two old positive differences
A and C have different endpoint pairs. All labels in each matching are
therefore distinct and positive. The later birth is c in every case.

Each output is tested against its unique actual positive-difference
endpoints. Both endpoints must lie strictly after c and at or before T,
and every frozen strict core condition is retained. In particular source
birth remains a rank, not one of A,B,C,H.

## Bijection and exact all-cut profile

Every strict six-distinct positive source record has exactly four distinct
old source endpoints. Sorting them gives a unique p<q<s<c; their original
pairing is one and only one of the three matchings above. Conversely, a
matching whose unique actual output endpoints and strict tests pass gives
exactly one unordered physical source record. Uniqueness of label endpoints
ensures that no record can arise from another quadruple or matching.

Thus this is a bijection, not a multiplicity bound. Each matching keeps
its own product, actual upper-output price u_r^[M], and exact cut interval
c<b<i. In particular alpha_(M+1) is retained in every genuine price.

For a fixed quadruple the two t_minus matchings have the same output
endpoints (i_minus,r_minus), when these exist. Their strict tests differ
only in earlier source birth q versus s. All old and output endpoint
distinctness tests are the same. Since q<s, type 1 in the core implies
type 2 in the core. If type 2 is in the core but type 1 is absent, the
only failure is q<=c/(log c)^2.

Let chi_minus,q, chi_minus,s and chi_plus,s indicate the full strict core
conditions for the corresponding matching. Terms with nonexistent outputs
are zero. The exact contribution of this quadruple is

```
u_rminus^[M] [AC*chi_minus,q + (AC+BH)*chi_minus,s]
   * 1[c<b<i_minus]
 + u_rplus^[M] BH*chi_plus,s * 1[c<b<i_plus].
```

Summing over all old quadruples gives the frozen P_b^core(M,T) exactly.
The minus term may equivalently be written, when chi_minus,s=1, as
u_rminus^[M] [BH+AC(1+1[q>c/(log c)^2])] on its actual cut interval.
The plus and minus indicators, output ranks, and cut intervals remain
distinct; there is no asserted cancellation or common price.

## Both outputs can be strict core for the same actual quadruple

A small example already belongs to the independently certified M=15
greedy prefix with C=1,m0=2. Take

```
(p,q,s,c)=(2,3,6,8),
(a_p,a_q,a_s,a_c)=(2,4,21,45),
A=2, B=17, C=24, H=43.
```

All three matchings are strict core. They give

```
type 1: {2,24},   product 48,
type 2: {19,41},  product 779,
         t_minus=22=a15-a14=204-182,
         (i_minus,r_minus)=(14,15), cuts b=9,...,13;

type 3: {17,43},  product 731,
         t_plus=26=a12-a11=123-97,
         (i_plus,r_plus)=(11,12), cuts b=9,10.
```

At M=T=15 the respective contribution is therefore

```
827*u15^[15]*1[9<=b<=13] + 731*u12^[15]*1[9<=b<=10].
```

The two prices are genuine and different. In particular the larger
numeric output t_plus=26 has the earlier output birth r_plus=12, whereas
t_minus=22 has birth 15. Numeric output order cannot replace rank order.

**Exact candidate rejected:** a larger physical output has a no-larger
genuine component price. Here the opposite strict inequality holds:

```
t_plus=26 > t_minus=22, but
u12^[15] = 250352825618441671/127861007863930889073926400
         > u15^[15] = 1/7753885440,
u12^[15]-u15^[15] = 17379822995881/9502155756831962624400 > 0.
```

This also follows directly by summing the three positive components at
k=12,13,14. All component prices retain alpha_16. The two actual lower
endpoints, cut intervals, and prices cannot be swapped or identified.
`M15_physical_output_price_reversal.json` records the exact rejection.

The existing M96 core lists contain simultaneous plus/minus core outputs
for 5,151 old quadruples in the greedy history and 5,328 in the variant.
This refutes a proposed per-quadruple mutual exclusion. It supplies no
unbounded family or asymptotic frequency statement.

## Exact BH/AC decomposition of the entire profile

For each old quadruple let G_(minus,q), G_(minus,s), G_(plus,s) denote
the corresponding full core indicator times its genuine u_r^[M] and
its actual cut indicator 1[c<b<i]. They include the specified source
birth, actual output endpoints and T horizon, and are zero when the
matching is absent. The exact identity is

```
P_BH = sum_quad BH (G_(minus,s)+G_(plus,s)),
P_AC = sum_quad AC (G_(minus,q)+G_(minus,s)),
P_core = P_BH + P_AC.
```

Type 2 is split algebraically into its AC and BH product portions under
the same single price and cut interval. It is not counted as two copies
of its full source-pair weight. The AC piece is a retained nonnegative
core part; its smaller finite fraction does not prove it summable.

For the M15 witness, the exact BH coefficients are 731 at each of the
two different outputs. Its AC coefficient is 48 at each minus matching:

```
P_BH = 731*u15^[15]*1[9<=b<=13]
      +731*u12^[15]*1[9<=b<=10],
P_AC = 96*u15^[15]*1[9<=b<=13].
```

The following raw product-coefficient totals are exact integers. They
are diagnostic sums before output pricing, not substitutes for the
price-dependent profile; the JSON retains them separately at every r.

| Existing history | BH minus,s | BH plus,s | AC minus,q | AC minus,s |
|---|---:|---:|---:|---:|
| Greedy M96 | 1,366,859,787,417 | 1,075,331,295,633 | 246,852,403,173 | 246,854,730,226 |
| Variant M96 | 1,344,970,036,242 | 1,060,082,038,406 | 244,952,964,762 | 244,955,037,361 |

Each channel's genuine weighted profile was independently re-aggregated
from the already certified records. The BH and AC profiles sum exactly
to every complete-core rational cut coefficient. Their harmonic coverage
fractions are:

| Existing history | BH fraction of sum_b P_b/b | AC fraction |
|---|---:|---:|
| Greedy M96 | 83.893698% | 16.106302% |
| Variant M96 | 82.751787% | 17.248213% |

The corresponding one-copy weighted record-mass fractions for BH are
83.878396% and 82.346843%. These are finite observations; all displayed
percentages come from exact rational fractions. They indicate that the
joint BH term covers most of the observed whole-profile mass, unlike
the earlier same-(c,e,i) paired subclass. They do not bound its growth.

`BH_AC_whole_profile_decomposition_existing_M96.json` contains exact
coefficients by output rank, genuine weighted channel profiles, mass/I
fractions and source hashes. No new search size was generated.

## Exact finite partition and mass proportions

Every record was classified by its actual endpoint matching. Integer
labels, products, numeric outputs and earlier births were checked against
the table. The type profiles were then reconstructed with the saved
genuine component prices and their actual cut intervals. Their sum equals
every saved rational P_b coefficient exactly; their record masses and I_j
likewise sum to the complete core totals.

| Existing history | Type | Records | Fraction of one-copy record mass | Fraction of harmonic coverage I |
|---|---:|---:|---:|---:|
| Greedy M96 | 1 | 66,520 | 8.060405% | 8.052451% |
| Greedy M96 | 2 | 66,889 | 50.258696% | 48.491645% |
| Greedy M96 | 3 | 61,557 | 41.680898% | 43.455904% |
| Variant M96 | 1 | 68,353 | 8.826175% | 8.623395% |
| Variant M96 | 2 | 68,740 | 51.427912% | 49.681678% |
| Variant M96 | 3 | 63,150 | 39.745913% | 41.694927% |

These percentages are decimal presentations of exact stored rational
fractions. No square-root additive decomposition is asserted. Type-2
counts exceed type-1 counts by precisely the old-birth exclusions:

```
greedy: 369 out of 66,889 type-2 records;
variant: 387 out of 68,740 type-2 records.
```

Each exclusion was checked using the independent integer rational log
enclosures: the q comparison fails and the s comparison passes. All other
strict conditions are shared by the two matchings and already certified.

For example, in the greedy history the quadruple (1,2,14,16) has point
values (1,2,182,252), hence A=1,B=180,C=70,H=251. Its t_minus=69
has actual output (i,r)=(22,23). Type 2 uses {181,250} and earlier birth
14, while type 1 uses {1,70} and earlier birth 2. The sole failure of
type 1 is 2<=16/(log16)^2, resolved rigorously by the log intervals.

## Scope and next nonduplicate action

`whole_core_matching_partition_existing_M96.json` contains the exact
three type profiles, mass/I fractions, counts, simultaneous-output
witnesses, old-birth-only witnesses, and original source hashes.

The all-history bijection and matching algebra are exact mathematical
results. Their coefficientwise checks are finite diagnostics, not a
proof of a uniform bound. The regrouping leaves a whole-profile problem
with genuinely different future output clocks and overlapping record
coverage. The fixed-cap uniform core theorem and Q1 remain unresolved.

Next action: seek a cap-sensitive comparison or charging estimate on
the joint BH expression while retaining the separate actual minus/plus
output ranks, their strict eligibility, their true prices and the explicit
physical-output/rank reversal above. The AC core part remains an additional
unproved obligation; a small observed fraction is not a finite-error bound.

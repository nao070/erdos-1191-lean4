# Three birth clocks: localization of Born and retired mixed pairs

2026-09-05. Author: `/root`, GPT-6 Astra Ultra.

Status: absolute summability and exact core reductions for the existing
raw birth-linear coefficients. These are all-history analytic statements,
not Lean-verified declarations or a resolution of Q1. They do not bound
the remaining signed core or the physical margin.

## 1. A mixed source record has three actual clocks

Use the actual increasing integer Sidon history, banks F_b and G_b,
diameters H_b, q_b=binom(b,2), fixed raw coefficients g, and
`w_b=1/(q_b^2 H_b^2)` of the causal note. Consider an unordered
mixed source pair with a used positive output. Orient it by birth:

```
d in G_b,   e in F_(b-1),   c=tau(e)<b,
t=|d-e| in F_infinity,     r=tau(t).
```

The orientation is unique even when d<e numerically. One record has
one output and one actual output birth. It is Born when r<=b and
retired when r>b. The Born sum B_T uses price w_b; R_T uses price
w_r for retired records. In either case its actual price is no
greater than w_b, and

```
w_b |g_d g_e| <= 1/q_b^2.                                (1)
```

Same-birth source pairs are excluded exactly as in the definition
of B_T; their centered diagonal correction is already elsewhere in
the causal identity.

## 2. The star-intersection bound holds on both sides of birth

The endpoint lemma from `near_retirement_incidence.md` in fact
extends to every r>=2, including r<=b. Fix e in F_(b-1), and write
`d=a_b-a_i`, `t=a_r-a_j`. If d>e,

```
a_j-a_i = a_r-a_b+e.
```

This right side can be negative when r<b, but cannot be zero:
zero would give e=a_b-a_r, which for r<b belongs to the disjoint
new class G_b, and for r>=b is nonpositive. Either contradicts the
choice of e. Actual nonzero-difference uniqueness therefore allows
at most one ordered pair (i,j). If d<e, the equation is

```
a_i+a_j=a_b+a_r-e,
```

so repeated-summand Sidonness permits at most two ordered assignments.
Consequently the number I_(b,r) of used mixed source pairs with
these clocks satisfies

```
I_(b,r)<=3q_(b-1)             for EVERY b>=3, r>=2.        (2)
```

The r=b case is included. Different slot assignments may overcount
the same record; this only strengthens the upper bound.

Fix gamma>1. There are at most `2floor[b/(log b)^gamma]+1` integer
ranks with `|r-b|<=b/(log b)^gamma`. Since
`3q_(b-1)/q_b^2<=6/b^2`, (1)--(2) imply the uniform bound

```
sum_(used mixed, |r-b|<=b/(log b)^gamma) w_b |g_dg_e|
 <=12 sum_(b>=3)1/[b(log b)^gamma]+6 sum_(b>=3)1/b^2
 < infinity.                                             (3)
```

This is a source-clock statement on both Born and retired records.
It is stronger than just applying a retirement-clock estimate to
the r>b half. No extra output multiplicity is charged.

## 3. An old source or old output far below b costs finitely much

Fix a>1/2 and set `k_b=floor[b/(log b)^a]`. For b>=3 we have
`k_b<b`. Set `F_0=F_1=empty` and `q_0=q_1=0` for cutoffs below
two. The number of mixed source pairs with c<=k_b is at most
`(b-1)q_(k_b)`, before even asking whether their output is used.
By (1),

```
sum_(used mixed, c<=b/(log b)^a) w_b |g_dg_e|
 <=3 sum_(b>=3)1/[b(log b)^(2a)] < infinity.               (4)
```

Indeed q_(k_b)<=b^2/[2(log b)^(2a)] and the resulting term is
at most `2/[(b-1)(log b)^(2a)]<=3/[b(log b)^(2a)]`.

If instead r<=k_b, the target t lies in F_(k_b). For every d in
G_b and every such t there are at most two partners e=d-t,d+t.
Keeping only positive old partners can only reduce the count.
Thus there are at most `2(b-1)q_(k_b)` records, giving

```
sum_(used mixed, r<=b/(log b)^a) w_b |g_dg_e|
 <=6 sum_(b>=3)1/[b(log b)^(2a)] < infinity.               (5)
```

These records are Born because k_b<b. Equations (4)--(5) do not
assume any independence between clocks or labels. The first bound
also applies to retired records at their smaller price w_r, and to
the source/retirement weight difference on this retired subset.

## 4. Physical and repeated-endpoint deletions for Born records

Fix beta>1. The actual numeric-output argument from the incidence
note applies to all mixed source pairs, not only retirements:
for t<=floor[b^2/(log b)^beta], there are at most
`2(b-1)floor[b^2/(log b)^beta]` records at source birth b.
Therefore

```
sum_(used mixed, t<=b^2/(log b)^beta) w_b |g_dg_e|
 <=12 sum_(b>=3)1/[b(log b)^beta] < infinity.              (6)
```

For a Born record in the source dyad N<=b<2N, all source and output
endpoints belong to P_(2N). A nontrivial equal-triple configuration
with repeated endpoints contributes to the same repeated-configuration
count already proved in `birth_linear_total_causal_sign.md`.
The safe bound is `12(2N)^3` such records. The coincident-triple
automatic records can be counted separately by the old point triples,
at most `(2N)^3`, or retained with their known centered automatic
formula. For an absolute deletion use the combined safe bound
`13(2N)^3`. Its source-clock total is bounded by

```
13 sum_(N=2^j, j>=1) (2N)^3/q_N^2 < infinity.             (7)
```

The constant is deliberately loose. This deletes all Born records
outside the six-distinct nontrivial case in absolute value; it does
not assert that the unweighted total of those records is bounded.

For retirements, the old far-rank tail must first be deleted at w_r;
the saved near-retirement repeated bound then applies. We do not
transfer that far-rank deletion to source price w_b.

## 5. Exact remaining cores

For B_T retain only Born mixed source records through T satisfying

```
c > b/(log b)^a,
b/(log b)^a < r < b-b/(log b)^gamma,
t > b^2/(log b)^beta,
the equal-triple representation has six distinct endpoints.
```

Call the resulting signed sum B_T^core, still at w_b. Equations
(3)--(7), with their absolute summability, give

```
|B_T-B_T^core| <= C_(a,beta,gamma)                         (8)
```

uniformly in the actual history and T. Intersections of omitted
sets need not be disjoint; their separate absolute bounds suffice.

For R_T further impose c>b/(log b)^a on the core already defined
in `near_retirement_incidence.md`, with its fixed alpha>1/4. The
remaining ranks obey

```
c > b/(log b)^a,
b+b/(log b)^gamma < r < b(log b)^alpha,
t > b^2/(log b)^beta,
six distinct endpoints.
```

Write this sum R_T^core, at the original retirement price w_r.
The prior tails and (4) imply

```
|R_T-R_T^core| <= C_(alpha,a,beta,gamma).                  (9)
```

Consequently the existing Abel identity is localized on both sides:

```
2B_T^core+2R_T^core+D_T=A_T+O_(alpha,a,beta,gamma)(1).     (10)
```

Under the fixed-onset cap, these core outputs lie between
`b^2/(log b)^beta` and `C b^2 log(2b)`, and every one of the three
birth clocks lies within a fixed power of log b of the others.
The output clock is separated from the latest source clock by the
explicit additive window in (3). Thus (10) confines any divergent
contribution to actual six-endpoint configurations in these windows.

It supplies no sign for either core. In particular a finite total
of the omitted costs does not prove that the remaining Born core
diverges by itself. Nor does Born divergence by itself pay the
single physical margin. These are the still missing steps toward
original Q1 and its final Lean theorem.

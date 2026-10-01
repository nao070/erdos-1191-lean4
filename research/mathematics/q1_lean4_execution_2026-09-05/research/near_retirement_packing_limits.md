# Short-star packing with both near-retirement cutoffs

Date: 2026-09-05. Owner: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Status: deterministic refinements of the bounds audited in
`near_retirement_incidence_review.md`, and a quantified limit of those
bounds at critical diameter. Every source dyad, including nongood ones,
remains in the global upper bound. No numerical experiment or Lean run
is used. No actual Sidon counterexample or original-Q1 conclusion is
claimed. The parent's separate source-clock localization is not repeated.

## 1. Both cutoffs inside one source birth

Keep the actual infinite Sidon history, permanent coefficients `g`, and
`w_n=1/(q_n^2 H_n^2)`. Fix the audited parameters `alpha>1/4`,
`beta>1`, `gamma>1`, and a source clock `b>=3`. Put

```
D_b = floor[b^2/(log b)^beta],
J_b = {r integer: r-b>b/(log b)^gamma,
                   r<b(log b)^alpha},
W_b = (H_b-D_b)_+,
U_b = |{D_b+1,...,H_b}\F_b|.                              (1)
```

Reversed-endpoint intervals are empty. Define the actual eligible stars
and their packed total by

```
m^*_(b,r) = |G_r intersect {D_b+1,...,H_b}|,
U_b(J_b)  = sum_(r in J_b)m^*_(b,r) <= U_b.                (2)
```

The inequality uses disjoint physical output labels. Each preceding-point
star occupies an integer interval of `W_b` positions. Thus, when `W_b>=1`,

```
binom(m^*_(b,r),2)<=W_b-1,     m^*_(b,r)<=r-1.             (3)
```

When `W_b=0`, all stars are empty. The six-distinct restriction can
delete edges but cannot enlarge a star or a degree.

Let `Z_b=sum_(core at b) w_r |g_dg_e|` be the absolute contribution.
The local maximum-three and `2m^*` degree bounds, followed by Cauchy
in the output clock, give

```
Z_b <= sqrt(6v_bS_(b-1)) sum_(r in J_b)w_r sqrt(m^*_(b,r))
    <= sqrt[6v_bS_(b-1) U_b(J_b) sum_(r in J_b)w_r^2].     (4)
```

This keeps the actual near-rank interval and physical cutoff together.
Replacing `U_b(J_b)` by its explicit allowance `U_b` is permitted but
may discard essential information.

## 2. Union degrees count a source pair only once

Every source pair has only one actual output birth. In the union over
`r in J_b`, a new source therefore has degree at most `p_b`, and an
old source degree at most `z_b`, where

```
p_b = min(q_(b-1),2U_b(J_b)),
z_b = min(b-1,3|J_b|).                                   (5)
```

If `J_b` is nonempty write `r_-=min J_b`. Two further bounds are

```
Z_b <= w_(r_-) sqrt(p_b z_b v_b S_(b-1)),                 (6)

Z_b <= w_(r_-) H_b^2
       min[(b-1)q_(b-1),2(b-1)U_b(J_b),
                               3q_(b-1)|J_b|].          (7)
```

For an empty `J_b` these expressions mean zero. The same union proof
applies to the source-clock absolute contribution with `w_b` replacing
`w_(r_-)`. In contrast, the square sum in (4) uses retirement prices;
its infinite-rank decay estimate below cannot be assigned to `w_b`.

## 3. Explicit scale of the combined Cauchy estimate

A midpoint variance bound gives

```
v_b<= (b-1)H_b^2/4,     S_(b-1)<=q_(b-1)H_b^2/4.         (8)
```

For each birth class, its variance is at most its sum of squared
distances from the interval midpoint; each distance is at most half
the interval diameter. Summing over permanent classes proves (8).

Since `H_r>=H_b` and `q_r>=r^2/4`,

```
sum_(r in J_b)w_r^2
 <= 256/H_b^4 sum_(r>b)r^(-8)
 <= 256/(7H_b^4 b^7).                                   (9)
```

Substitution into (4), using `(b-1)q_(b-1)<=b^3/2`, proves

```
             Z_b<=4 sqrt(3/7) sqrt(U_b(J_b))/b^2.         (10)
```

Alternatively combine (5), (6), (8), and `w_(r_-)<=w_b`:

```
Z_b <= (b-1)q_(b-1)/(4q_b^2)
     = (b-2)/(2b^2).                                    (11)
```

This holds even if all future retirement clocks are included. Its
series over source births is not summable, and it is not a replacement
for the already proved retirement-clock tails. The count bound (7) also
gives

```
Z_b <= 8U_b(J_b)/[b^2(b-1)].                             (12)
```

A new estimate `U_b(J_b)<=epsilon b^2/log(2b)` would therefore put
(12) at `O(epsilon/(b log b))`. Cauchy (10) alone would require the
stronger `U_b(J_b)=O(b^2/(log b)^2)` for that scale. These are sufficient
conditions for these particular upper bounds, not necessary conditions
on the actual signed retirement.

## 4. The surviving logarithmic gap

Consider the regime `H_b asymp b^2 log b`, which the cap permits but
does not require at every rank. Then

```
D_b/H_b = O((log b)^(-beta-1)),
H_b-D_b-q_b <= U_b <= H_b,
U_b/H_b = 1-O(1/log b).                                 (13)
```

Thus the explicit unused-label allowance is still of order
`b^2 log b`. The subquadratic output cutoff removes a small fraction
of that allowance. It does not show that near stars occupy only
`b^2/log b` of those labels.

Using only `U_b(J_b)<=U_b` in (10) gives
`O(sqrt(log b)/b)`. The minimum with (11) is merely `O(1/b)`.
On a source dyad, one obtains

```
sum_(b=N..2N-1)Z_b
 <= (1/2)sum_(b=N..2N-1)1/b
 <= (log 2)/2+1/(2N).                                  (14)
```

The near-rank cutoffs alone do not improve the power in (9). For large
`b`, every integer `r in [2b,3b]` belongs to `J_b`, since
`(log b)^alpha>3` and `(log b)^gamma>1`. Consequently

```
1/(3^8 b^7) <= sum_(r in J_b)r^(-8) <= 1/(7b^7).          (15)
```

This is a statement about the rank-only sum; it does not give a lower
bound for actual `w_r^2` without diameter information. It shows that
the rank exclusions themselves supply no additional logarithmic factor
to that decay estimate.

At a productive critical-order dyad, the guaranteed Abel block
`Lambda_N` from the audited source is of order `1/log N`. Bound (14)
is larger by a factor of order `log N`. Actual variance or star counts
could improve it, but that requires a new upper estimate. The
good-epoch variance lower bound cannot be used as such an upper bound.

The latitude of the displayed scalar bounds makes the same point.
They permit star sizes of order `N` at order `N` output clocks
`r asymp 2N` for source clocks `b asymp N`. The total `N^2` target
labels fits the allowance `U_b asymp N^2 log N`; the star-diameter
and `r-1` bounds permit these sizes. Both degree bounds and the
source-pair union cap permit order `N^2` incidences per `(b,r)` and
order `N^4` on one source dyad. Such rank intervals obey both core
clock cutoffs for large `N`, and the surviving physical band contains
order `N^2` target labels. This is a description of what the scalar
inequalities leave open. It is not an actual Sidon construction,
counterexample, or claim that the six-endpoint equations impose no
additional restriction.

## 5. A single target budget across a whole source dyad

Let `T_N` be the actual physical targets used by core pairs with
`N<=b<2N`. For `t in T_N`, set `r=tau(t)` and

```
B_N(t)={b in [N,2N): r in J_b, D_b<t<=H_b}.               (16)
```

Some candidate births in this set may have no actual source pair.
Each allows at most `2(b-1)` pairs with this target. Therefore

```
sum_(core, N<=b<2N)w_r |g_dg_e|
 <= sum_(t in T_N) [2/(q_(tau(t))^2 H_(tau(t))^2)]
                     sum_(b in B_N(t))(b-1)H_b^2.        (17)
```

The outer sum counts every target once. Its permissible source-birth
multiplicity and actual retirement weight remain on the inner sum.
No coefficient-one target budget has been substituted for this bound.

With `Dmin_N=min_(N<=b<2N)D_b` and the original `L_N`,

```
T_N subset (F_(L_N)\F_N)
                    intersect {Dmin_N+1,...,H_(2N-1)}.   (18)
```

The explicit minimum avoids an unstated monotonicity premise. This
is one dyad-level mask; it does not remove the order-`N^2` multiplicity
that a target is still allowed over source births by the current bounds.

## 6. Every source dyad remains in the global target

Let `M_N` be the sum over all `b in [N,2N)` of the minimum of (4),
(6), and (7), with zero for empty `J_b`. The right side of (17)
is another upper bound on this same dyad and can be included in the
minimum at dyad level. At dyadic terminal horizons,

```
R_T(w)<=sum_(all dyadic N<T)M_N+O_(alpha,beta,gamma)(1).    (19)
```

Only the audited summable tails and finite initial source births enter
the constant. No nongood source dyad was deleted.

Using the audited source's productive ranks and `c_*`, one sufficient
additional theorem would be

```
sum_(all dyadic N<T)M_N
 <= kappa c_* sum_(productive N<T)N^2/H_N+O(1),
                          0<=kappa<1/2.                 (20)
```

The presently justified substitutions give (14), which does not prove
(20). Restricting its left side to productive source dyads would
discard unsigned terms for which no summable bound is available.
Even (20), if proved, would leave the separate physical margin and
source-clock commutator from the causal note.

The concrete refinements are (4), the union degree caps (5)--(7),
and the one-target dyad budget (17). Their precise limit is visible in
(13)--(15): existing packing leaves a full logarithmic gap at critical
physical scale. Further actual six-endpoint structure or signed
cancellation remains necessary for this route.

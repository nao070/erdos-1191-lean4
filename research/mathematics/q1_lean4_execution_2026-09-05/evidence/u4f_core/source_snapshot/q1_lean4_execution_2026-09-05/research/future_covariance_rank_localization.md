# Rank localization of the actual future-covariance profile

2026-09-06 JST. Author: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Status.** The square-root profile from the causal Fourier commutator
admits a uniform finite-error reduction to six-distinct actual records
in explicit logarithmic rank and physical-label windows. This requires
stronger thresholds than several older scalar-cost deletions. A new
incidence estimate at a fixed source birth and LOWER output endpoint
also removes short interval coverage, even with arbitrarily late upper
outputs. The remaining core profile is not bounded here; original Q1
remains unresolved.

These are analytical all-history bounds, with no numerical experiment,
old-check replay, or Lean execution. Only this new note was written.
Inputs read were `causal_fourier_rank_commutator.md`,
`signed_clock_deficit_global.md`, `clock_core_localization.md`,
`near_retirement_incidence.md`, `late_retirement_tail.md`, and the
raw-product repeated-stage bound in `signed_retirement_fibers.md`.

## 1. One physical pair covers one actual rank interval

Use the positive difference bank of one actual increasing integer Sidon
history, including repeated two-sum uniqueness. Keep the original

```
F_n=Delta P_n, Q_n=n(n-1), H_n=a_n-a_1, alpha_n=Q_n^-2,
u_r=sum_(k>=r)(alpha_k-alpha_(k+1))/H_k^2.
```

For an eligible unordered positive source pair h={d,e}, let
c=max(tau(d),tau(e)), a=min(tau(d),tau(e)), and let its unique output be

```
t=|d-e|=a_r-a_i,       c<i<r.
v_h=u_r de>=0.
```

Same-birth positive sources have an old output, so a<c. The letter a
alone here is a rank; a_j denotes a point value. The Fourier profile is
exactly

```
P_b(T)=sum_(h:r<=T) v_h 1[c<b<i],
N_T(P)=sum_(b=2..T-1)sqrt(P_b(T))/b.                 (1)
```

Thus one record has one interval of coverage, c<b<i, and retains the
true upper-output price u_r throughout. That interval cannot be treated
as independent copies of its pair weight.

For a class E of records write P_b^E for its restriction. It is enough
to prove sum_b sqrt(P_b^E)/b<infinity uniformly in T for each omitted
class, because sqrt(x+y)<=sqrt(x)+sqrt(y). Mere finiteness of
sum_(h in E)v_h does not by itself prove this stronger profile statement.

The elementary estimates used below are

```
v_h<=alpha_r<=4/r^4,
v_h<=alpha_b<=4/b^4 whenever c<b<i,
number of pairs with later source birth c
 <=(c-1)binom(c-1,2)<=c^3/2.                         (2)
```

The first two use de<=H_c^2 and monotonicity of the actual diameters.
The count is taken once per source pair over all of its possible future
outputs; actual Sidonness gives it only one used output.
Also P_b(T)<=1/8 uniformly, by the total positive source-pair mass
bound from the commutator note. Thus every finite set of initial cut
ranks below a parameter-dependent threshold has a uniform finite cost.

## 2. Far source-to-output ratios have a summable square-root profile

Fix A>1/2 and omit records with

```
r>=c(log c)^A.
```

At a fixed cut b the weight is at most
4/max(b,c(log c)^A)^4. By (2),

```
P_b^far<=2 sum_(3<=c<b)c^3/max(b,c(log c)^A)^4.
```

For all sufficiently large b set L_b=(log b/2)^A, so
1<=L_b<=sqrt(b). If c<=b/L_b use the denominator b. For larger c,
one has c>sqrt(b) and (log c)^A>=L_b. Summing the two ranges gives

```
P_b^far<=2(2+log L_b)/L_b^4
 <=2^(4A+1)[2+A log log b]/(log b)^(4A).             (3)
```

For the first range use sum_(c<=x)c^3<=x^4; for the second use
sum_(b/L_b<c<b)1/c<=1+log L_b. Therefore

```
sum_b sqrt(P_b^far)/b<infinity       for A>1/2.      (4)
```

No cap was used. The old late-retirement scalar sum only required
A>1/4. Its hypothesis is not enough to deduce (4) by taking square
roots; the direct profile proof establishes the stated stronger range.
The threshold here is sufficient, not asserted sharp for actual histories.

## 3. A fixed source/lower-output incidence and short coverage intervals

Fix c<i and an older positive label e in F_(c-1). Write the new source
d=a_c-a_j, j<c, and let its eligible output be a_r-a_i with r>i.
If d>e, then

```
a_r+a_j=a_c+a_i-e.
```

Sidonness allows one unordered point pair. The strict order
r>i>c>j fixes its orientation, so at most ONE solution remains.
If d<e, then

```
a_r-a_j=a_i-a_c+e>0,
```

and positive-difference uniqueness again gives at most one solution.
Thus, over ALL future r, the actual incidence and its weight satisfy

```
I_(c,i)<=2 binom(c-1,2),
sum_(h: laterbirth=c, loweroutput=i)v_h
 <=2 binom(c-1,2)alpha_c<=1/c^2.                    (5)
```

This differs from the older fixed-(c,r) incidence with factor three.
The bound in (5) uses the future LOWER endpoint and its strict order.

Fix gamma>1 and omit records with i-c<=c/(log c)^gamma. For a cut
b covered by such a record, eventually c>b/2 and both c and i are
within distance

```
L'_b=ceil[2^gamma b/(log b)^gamma]
```

of b. At most (L'_b)^2 pairs of clocks (c,i) occur, each with weight
at most 4/b^2 by (5). Consequently

```
P_b^shortcoverage<=4(L'_b)^2/b^2
                    =O_gamma((log b)^(-2gamma)),
sum_b sqrt(P_b^shortcoverage)/b<infinity
                                      for gamma>1. (6)
```

The upper output r was not restricted in this proof. In particular a
short interval of rank coverage can be removed even when its output
birth is far beyond both its sources and its lower endpoint.

## 4. Short upper-output lags need their own profile threshold

Fix delta>2 and omit outputs with r-i<=r/(log r)^delta. At upper
rank r there are at most r/(log r)^delta such lower endpoints. For
the positive source bank at cut b, the graph of source gaps separated
by a fixed t has degree at most two, hence

```
K_(b-1)^+(t)<=sum_(d in F_(b-1))d^2
              <=b^2H_b^2/2.
```

Using u_r<=4/(r^4H_b^2) for r>b proves, for large b,

```
P_b^shorttop
 <=2b^2 sum_(r>b)1/[r^3(log r)^delta]
 <=1/(log b)^delta,
sum_b sqrt(P_b^shorttop)/b<infinity     for delta>2. (7)
```

The previous output-capacity theorem gives a finite SUM OF PAIR WEIGHTS
for this class at exponent greater than one; its price-commutator
analogue only needs exponent greater than one half. Neither is the
square-root profile in (1). Equation (7) rechecks the true output price
and proves the range delta>2 without making either transfer. It does
not assert failure of profile summability at the lower thresholds.

## 5. Old partner births, short numeric labels, and repeated endpoints

First fix eta>1 and omit pairs with a<=c/(log c)^eta. At source c
there are at most

```
(c-1)binom(floor[c/(log c)^eta],2)
                    <=c^3/[2(log c)^(2eta)]
```

candidate pairs. At cut b, split c at sqrt(b), use the full count in
(2) below that cutoff and log c>log b/2 above it. This yields

```
P_b^oldpartner<=2/b^2+2^(2eta-1)/(log b)^(2eta),
sum_b sqrt(P_b^oldpartner)/b<infinity      for eta>1. (8)
```

Next fix beta>2 and omit t<=c^2/(log c)^beta. For each new source
and each positive integer target t there are at most two partners,
e=d-t or e=d+t. Across all future outputs at birth c this gives at
most 2c^3/(log c)^beta candidates. The same split proves

```
P_b^smalloutput<=2/b^2+2^(beta+1)/(log b)^beta,
sum_b sqrt(P_b^smalloutput)/b<infinity     for beta>2. (9)
```

These arguments re-use the earlier actual endpoint COUNTS. The older
notes used centered birth-linear coefficients and q_c=binom(c,2)
normalization; those weighted values are not bounds on the present raw
positive products de with Q_c=c(c-1). Equations (2),(8),(9) supply the
required normalization and true-price bounds afresh. The older scalar
thresholds eta>1/2 and beta>1 are therefore not imported into (1).

Finally, all repeated-endpoint eligible records have a summable profile
without first imposing a near-clock condition. The previously established
RAW signed-product stage bound is

```
sum_(non-six retired, output r) |de|
                         <=24(r-1)^2H_r^2.
```

Our positive-source records are a subset, and u_r<=alpha_r/H_r^2,
so their total weight at r is at most 24/r^2. Thus

```
P_b^repeated<=sum_(r>b)24/r^2<=24/b,
sum_b sqrt(P_b^repeated)/b
 <=sqrt(24)[zeta(3/2)-1]<infinity.                  (10)
```

This input is the actual raw-product estimate (12)--(13) of
`signed_retirement_fibers.md`, not a centered-coefficient or source-price
claim. Its newest endpoint occurs once in the new triple; automatic
coincident triples cannot retire. Those are exactly the repeated classes
needed in (10). The later exact multiset theorem does not invalidate
this older, still valid absolute upper bound.

## 6. A uniformly equivalent and narrower remaining profile

Fix parameters

```
A>1/2, gamma>1, delta>2, eta>1, beta>2.
```

Retain only records satisfying all of the following:

```
six distinct endpoints,
a>c/(log c)^eta,
i-c>c/(log c)^gamma,
r-i>r/(log r)^delta,
r<c(log c)^A,
t>c^2/(log c)^beta.                                (11)
```

Let P_b^core(T) be their actual profile at cut b, still with the one
weight u_r de and the one interval c<b<i. From (4),(6)--(10),

```
0<=N_T(P)-N_T(P^core)<=C_(A,gamma,delta,eta,beta)      (12)
```

uniformly in the actual history and terminal T. To see this, the omitted
profile is bounded by the sum of its six nonnegative class profiles;
apply sqrt(x+y)-sqrt(x)<=sqrt(y) and sum. Intersections of omitted
classes do not create an extra spending budget: this is a finite-class
analytic upper bound on the same original profile.

On every cut covered by a surviving record one has, in particular,

```
b/(log b)^A<c<b<i<r<b(log b)^A.                     (13)
```

Thus the latest source and both output endpoints lie within a
log^(1/2+epsilon) multiplicative rank window, if desired, while BOTH
the source-to-lower-output gap and the lower-to-upper-output gap remain
explicitly separated from zero. The earlier source birth is also within
the stated logarithmic range, and repeated configurations are absent.

Under one fixed-onset cap H_c<=C c^2 log(2c), the surviving physical
outputs obey

```
c^2/(log c)^beta<t<=H_c<=C c^2 log(2c).
```

Independently, actual Sidon packing of the r-i+1 points between the
output endpoints gives (r-i)(r-i+1)/2<=t. This is a constraint on the
actual TOP gap. It does not imply that the physical gap a_i-a_c is
short, and no such assertion is used in the coverage estimate (6).

For completeness, the exact dyadic bookkeeping retains shared intervals.
For N=2^j define

```
ell_N(c,i)=sum_(N<=b<2N, c<b<i)1/b,
I_N^core(T)=sum_(h in core,r<=T)v_h ell_N(c,i).
```

Then I_N^core=sum_(N<=b<2N)P_b^core/b, and Cauchy gives

```
sum_(N<=b<2N)sqrt(P_b^core)/b
 <=sqrt[(log 2+1/N) I_N^core].                      (14)
```

One record's total coverage satisfies
sum_N ell_N(c,i)<=log(i/c)<=A log log c on the core.
There is one such factor, not a new mass for each dyadic block. Any
further entropy or interval estimate must act on this actual weighted
coverage expression or on a stronger genuinely correlated quantity.

The remaining sum in (12) is not proved finite. If the single fixed cap
holds, the previously established actual eligible demands and the
commutator bound force N_T(P) to diverge; (12) then locates that necessary
divergence inside this narrower actual core. This conditional consequence
is not a contradiction: an upper bound on the core profile is still
missing. No finite family or abstract coverage model is substituted for
one capped infinite history, and original Q1 remains unresolved.

# Eligible far-clock transport: a stronger deficit and a lower-endpoint split

2026-09-05. Author: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Status.** This note does not bound the full far-clock excess by a
constant. It gives a stronger reduction for the records that can actually
pay strictly future blocks. Such a collision has full geometric deficit
at least B/2 and eligible absolute retirement at most B/2. Consequently
only source/output price ratios exceeding 4 can obstruct a comparison
with 2B. An exact global split at the LOWER output endpoint then removes
short upper/lower endpoint rank lags at a summable cost, even when the
source/output clocks are far apart. The full output-clock capacity on
short top-endpoint lags is also summable with threshold gamma>1.
The remaining expression keeps an actual future-suffix kernel and a
deficit at least (3/2)B.

The parent and causal agent are working independently on the physical
baseline and the output-priced carrier. The causal agent independently
obtained the eligible half-B bound by another calculation. The present
note focuses on source-price transport and its extra lower-endpoint clock.
No numerical experiment, test rerun, Lean execution, or new formal
verification was performed. Only this new research note was written.

## 1. Clocks and the eligible part of a full collision

Use one fixed actual increasing integer Sidon history and the permanent
raw signed feature d. Set Fhat_n=Delta P_n union(-Delta P_n),
Q_n=n(n-1), H_n=a_n-a_1, alpha_n=Q_n^-2 and

```
w_n=alpha_n/H_n^2,
kappa_n=alpha_n-alpha_(n+1),
u_n=sum_(k>=n) kappa_k/H_k^2.
```

The compatible u is fixed from the complete history. It is not reselected
at a terminal horizon. The fixed cap, whenever used below, means one
C>0 and one onset n0 with H_n<=C n^2 log(2n) for every n>=n0.

For a source pair of later birth b and output a_r-a_i, retirement means
b<r. To be usable by any strictly future point block against an old bank,
the stronger condition is

```
                              b<i<r.                    (1)
```

Indeed an old rank n must satisfy b<=n<i. Conversely such a rank exists
if (1) holds. This condition is necessary for payment, but does not itself
assign the output to a chosen block.

In an active equal-sum multiset collision with newest endpoint n in
V={x,y,n}, the output opposite an occurrence m in U has source clock
rank(max(U without m,V without n)). Thus (1) holds only when m is the
unique second-largest endpoint ell and ell belongs to U. All four formal
records of that output are then eligible, with the same later source
clock b, lower output clock i=rank(ell), and upper clock r=rank(n).
Every other output from the collision is ineligible.

This observation concerns actual physical pairs, not deletion of entries
from a PSD matrix. Restricting an upper budget for a nonnegative carrier
to potentially usable pairs does not assert that the restricted matrix
is PSD. Nor does removing ineligible signed terms automatically bound
the earlier FULL source-priced retirement excess.

## 2. Geometry improves both the full deficit and eligible subtotal

Write U={u,v,ell}, V={x,y,n}, with n>ell>u,v,x,y, allowing repeated
old endpoints within a multiset. Let A=aut(U)aut(V), and put

```
t=n-ell>0, p=n-u>t, q=n-v>t,
a=n-x>t, bgeo=n-y>t,
P=p+q, S=P+t=a+bgeo, D2=p^2+q^2+t^2.
```

The exact matching formulas give

```
B=4D2/A,
R=[2D2+2S^2-12a bgeo]/A,
G=2B-R=[6sigma_U^2+12a bgeo]/A.                         (2)
```

Here the product a bgeo is the product of the two top distances from
V. Since (a-t)(bgeo-t)>=0, one has a bgeo>=tP. Also P^2<=2(p^2+q^2).
Substitution into R proves

```
R <=[6(p^2+q^2)-8tP+4t^2]/A <=(3/2)B,
                              G>=B/2.                  (3)
```

The near-zero-deficit geometry possible when the two top endpoints
belong to the same triple is therefore absent in an eligible collision.

For the four formal eligible records, define

```
g1=(a-p)(bgeo-q), g2=(a-q)(bgeo-p),
rho= -2(g1+g2)/A,
K=2(|g1|+|g2|)/A.                                     (4)
```

Thus rho is their actual signed subtotal and K their actual absolute
subtotal. The factor 2/A retains the doubled Schur-list cancellation
from the reviewed multiset orbit proof. Both formulas remain exact when
numeric labels or old endpoint slots repeat.

The positive-part estimate in `signed_output_clock_source.md` gives
(g1)_+,(g2)_+<=a bgeo t/S. Meanwhile
g1+g2=2a bgeo-(p^2+q^2)-Pt. Since P>2t and a bgeo>=tP,

```
|g1|+|g2|
 <=p^2+q^2+Pt-2a bgeo(1-2t/S)
 <=p^2+q^2+Pt(3t-P)/(P+t)
 =D2-t(P-t)^2/(P+t).
```

Consequently

```
|rho|<=K<=B/2-2t(P-t)^2/[A(P+t)]<=B/2.               (5)
```

The signed formula also reads
rho=[(u-v)^2+(x-y)^2-(n-ell)^2]/A. It need not be nonpositive.
The half-B bound has also been independently obtained by the causal
agent. The displayed positive t-dependent correction is not needed
for the global reductions below.

## 3. A global price-ratio reduction, with a fixed early-rank cost

Let c be w or u, and let B_T(c) be the full raw Born total through T,
priced at each Born source stage. Define

```
H_T^src(c)=sum_(eligible records, r<=T)c_b |de|,
H_T^out(c)=sum_(eligible records, r<=T)c_r |de|.
```

Every eligible collision contributes c_b K on the left and c_r B
to the Born total; all its Born source clocks equal r. By (5),

```
H_T^out(c)<=B_T(c)/2,
D_T^elig(c):=2B_T(c)-H_T^out(c)>=(3/2)B_T(c).          (6)
```

The remaining Born contributions are nonnegative and are retained in
this deficit. In particular a collision with c_b<=4c_r satisfies
c_b K<=2c_r B. Writing Bad_T for the eligible collisions with c_b>4c_r,
we obtain the rigorous global reduction

```
H_T^src(c)-2B_T(c)
 <=sum_(C in Bad_T)[c_(b(C))K(C)-2c_(r(C))B(C)].       (7)
```

This inequality discards only nonpositive grouped contributions.
It does not discard individual negative records from a collision.

For every fixed b0, all pairs whose source birth is at most b0 have a
finite uniform cost, regardless of when their output is realized:

```
sum_(source birth<=b0)c_b |de|
 <=[M_(b0)(V)-tr(V_(b0))]/2,
V_de=alpha_maxbirth, M_(b0)(V)=4(h_(b0)-h_(b0)^(2)).    (8)
```

This follows from c_b|de|<=alpha_b and sums each source pair once.
Hence the truly unresolved part of (7) has source births tending to
infinity. Finitely many early sources cannot disprove a bounded-error
global estimate.

## 4. A specific eligible obstruction to pointwise source-price transfer

The stronger eligible restriction still does not justify replacing its
source price by the output price. For every integer L>=204, take

```
P_7={0,1,8,10,100,L,L+3},
U={1,10,L}, V={0,8,L+3}.
```

This is actual Sidon. The first five points have the ten distinct gaps
{1,2,7,8,9,10,90,92,99,100}, which exclude 3. The two new families
L-a and L+3-a, for those five old a, exceed 100. They are separately
distinct, and a coincidence between the two families would force an
old gap 3. The remaining new gap is 3 itself. Thus all 21 gaps are
distinct.

The only eligible output of this collision is 3. Its four pairs are
{-2,1}, {-1,2}, {-10,-7}, {7,10}, with products -2,-2,70,70.
They all have later source clock 4, while the lower and upper output
clocks are 6 and 7. Therefore

```
rho=136, K=144,
B=8L^2-40L+248,
w_4 rho=17/1800,
2w_7 B=(16L^2-80L+496)/[1764(L+3)^2].                (9)
```

The difference in (9) is positive: multiplying by the positive common
denominator 1800*1764*(L+3)^2 gives
1188L^2+323928L-622908>0 for L>=204.

Additional spectator points can be placed successively far apart before
L, maintaining Sidonness and excluding gap 3, and L can then be placed
above twice their diameter. This makes the upper output clock arbitrarily
late while the four later-source clocks remain 4. It does not give a capped
infinite counterexample or a failure of (7) after summing all Born groups.
Indeed (8) bounds its entire early-source contribution. Its purpose is
to rule out a pointwise transfer even after the physically relevant
eligible restriction, and to isolate why a global count is essential.

## 5. Exact decomposition at the lower output endpoint

For a finite signed bank define the positive absolute kernel

```
k_n^abs(t)=sum_(d<e in Fhat_n, e-d=t)|de|,  t>0.
```

For eligible records b<i<r, split the actual price difference as
c_b-c_r=(c_b-c_i)+(c_i-c_r). Let

```
J_T^elig,abs(c)=H_T^src(c)-H_T^out(c).
```

The first part has the exact global form

```
Pre_T(c)
 =sum_(n=2..T-1)(c_n-c_(n+1))
       sum_(t in Delta(P_T\P_n)) k_n^abs(t).           (10)
```

Indeed a pair contributes at intermediate n precisely when b<=n<i,
so its coefficient telescopes to c_b-c_i. The second part is

```
Post_T(c)
 =sum_(2<=i<r<=T)(c_i-c_r)k_(i-1)^abs(a_r-a_i),
J_T^elig,abs(c)=Pre_T(c)+Post_T(c).                   (11)
```

Every nonzero contribution to k_(i-1)^abs(a_r-a_i) is eligible:
its source birth is less than i, and that actual output first appears
at r by Sidon uniqueness. The Post sum counts each actual output once;
the two addends in (11) divide each record's one price difference into
disjoint intervals. The repeated suffixes in (10) express a telescoping
price difference; they are not independently spendable physical budgets.

The same identities hold with the signed kernel k_n(t) and the signed
eligible commutator. For example the inner signed sum in (10) is exactly

```
[ ||1_(P_T\P_n)*g_(Fhat_n)||_2^2-(T-n)Z_n ]/2.
```

The absolute version is the analogous ordinary convolution energy for
the even feature |d|, with the same diagonal. These are actual future
suffixes, not hypothetical blocks or copied capacities.

## 6. Short top-endpoint rank lags are summable even with far source clocks

For any fixed t, the graph of pairs of labels separated by t has degree
at most two. Applying 2|de|<=d^2+e^2 and summing gives

```
k_(i-1)^abs(t)<=Z_(i-1)<=Q_(i-1)H_i^2.               (12)
```

Fix gamma>1/2 and L_i=floor[i/(log i)^gamma], i>=3. For c=u and
r=i+h, the previously proved price bound yields

```
H_i^2(u_i-u_(i+h))<=alpha_i-alpha_(i+h)
                 <=4h alpha_i/(i-1).
```

Using (12), summing h<=L_i, and Q_(i-1)<=(i-1)^2 proves

```
sum_(h=1..L_i)(u_i-u_(i+h))k_(i-1)^abs(a_(i+h)-a_i)
 <=2L_i(L_i+1)/[i^2(i-1)]
 <=3/[i(log i)^(2gamma)]+3/[i^2(log i)^gamma].        (13)
```

Both series converge. This is unconditional for u. It concerns the
UPPER/LOWER OUTPUT clocks i,r, rather than the source/output clocks
b,r in the earlier near-commutator theorem. It therefore applies even
when b is much earlier than i and r-b belongs to that theorem's far set.

For c=w, the additional diameter-change cost at i is at most

```
(2/i^2)sum_(h=1..L_i) log(H_(i+h)/H_i).              (14)
```

On a dyadic N<=i<2N, expand each logarithm into actual consecutive
increments of log H. Each increment is crossed by at most
floor[2N/(log N)^gamma]^2 terms. Thus the cost in (14) over this
dyad is at most

```
8 log(H_(4N)/H_N)/(log N)^(2gamma).                  (15)
```

Under the one fixed cap, H_N>=N^2/4 and hence
H_(4N)/H_N<=64C log(8N) beyond the fixed onset. With N=2^j, the
sum of (15) is bounded by

```
8sum_(j>=j0)
 log(max(1,64C(j+3)log 2))/(j log 2)^(2gamma)<infinity.
```

The finitely many initial lower endpoints also have finite cost by
(8) applied to their old source banks. Therefore the near part of
Post_T(c) is bounded uniformly in T for c=u, and for c=w under the cap.
The signed near part is bounded in total variation by the same estimates.

## 7. Short top-endpoint lags have finite full output-clock capacity

The parent proposed the following further consequence of (12), which
this author independently checked. On the actual output a_r-a_i,
all eligible source pairs lie in Fhat_(i-1). Thus the output-priced
carrier Psi_lambda, for 0<=lambda<=1, of `signed_output_clock_source.md` has eligible
weight at this one physical label at most

```
(1+lambda)u_r k_(i-1)^abs(a_r-a_i)
 <=(1+lambda)u_r Z_(i-1)
 <=(1+lambda)/Q_r.
```

The factor in (12) is one: each unordered edge contributes half its
endpoint square sum, and each endpoint has degree at most two.
Since an actual output label has a unique physical endpoint pair,
there are at most floor[r/(log r)^gamma] labels at upper rank r
whose lower rank satisfies 0<r-i<=r/(log r)^gamma. For gamma>1,

```
sum_(eligible outputs, 0<r-i<=r/(log r)^gamma)
    eligible_kernel_(Psi_lambda)(a_r-a_i)
 <=(1+lambda)sum_(r>=3)1/[(r-1)(log r)^gamma]<infinity. (16)
```

No cap or comparison of neighboring diameters is required. This is
the TOTAL nonnegative physical capacity on these labels, rather than
only a price-commutator estimate. A restriction of Psi_lambda to an
old rank less than i, or an actually dominated nonnegative subsource,
is bounded on that label by this same eligible
kernel. The labels are counted once, so a divergent sum of actual
demands paid by Psi_lambda must use the complementary longer top
endpoint lags. The gamma>1 threshold in (16) must not be replaced
by the gamma>1/2 threshold for the DIFFERENCE of prices in (13).

## 8. The remaining actual endpoint mechanism and the unresolved estimate

Let Post_T^far retain r-i>L_i. Combining (6),(10)--(15) gives the exact
remaining target, with an error bounded uniformly in T:

```
H_T^src(c)-2B_T(c)
 =Pre_T(c)+Post_T^far(c)-D_T^elig(c)+O(1),
D_T^elig(c)>=(3/2)B_T(c).                            (17)
```

All deficit terms are retained. This is a stronger absolute comparison
for potentially usable pairs. It does not by itself prove the original
full signed excess J_T-G_T is bounded: ineligible signed terms have not
been assigned a sign. Its relevance to actual payments is that only
eligible pairs of a nonnegative physical source can pay strictly future
blocks.

There is an additional actual location constraint on the far part. If
h=r-i then the h+1 points from rank i to r have h(h+1)/2 distinct
positive differences, all at most a_r-a_i. Therefore

```
h(h+1)/2<=a_r-a_i<=2H_b                         (eligible record),
h(h+1)/2<=a_r-a_i<=H_b                          (positive product).
```

Under the cap this gives h<=2sqrt(C)b sqrt(log(2b)) in the first case
beyond the onset. It restricts upper/lower rank separation through the
ACTUAL source diameter, while permitting the lower endpoint itself to
lie very far after the sources. The exact family in Section 4 exhibits
the latter possibility.

The existing fixed-output estimate (12) is insufficient alone to close
(17). For example there are at most 2H_n possible outputs in the inner
sum of (10), so it only gives that sum <=2H_n Z_n. For u, this leads
to a per-n upper bound

```
2 kappa_n Q_n H_n
 =8H_n/[(n-1)(n+1)^2]
 <=16C log(2n)/n,
```

whose accumulated upper bound is O((log T)^2). The old physical
source estimate supplies a better O(log T) upper bound, but neither
comparison produces the needed constant after the full deficit is
subtracted. These upper estimates do not assert that the true remainder
diverges.

A closing argument would have to bound the actual future-suffix term
together with the remaining top-endpoint far term against this SAME
deficit, or exploit the global distribution of the top-gap labels beyond
the count in (12). A divergent Born saving by itself supplies no such
upper comparison. The stronger output-price statement (16) still leaves
the longer top-endpoint lags. This note establishes the displayed
geometric, price, and accounting reductions and their summable removals,
while leaving the required global estimate and original Q1 unresolved.

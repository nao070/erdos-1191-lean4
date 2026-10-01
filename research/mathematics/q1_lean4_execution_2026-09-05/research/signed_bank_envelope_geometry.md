# Signed-bank kernel geometry and the exact sign-feature comparison

2026-09-05. Author: `/root`, GPT-6 Astra Ultra.

Status: exact finite kernel identities and a comparison with the existing
positive-bank unit source. These are part of investigating the new signed
Born-positivity route, not an original-Q1 proof. They have not been
formalized in Lean. No finite experiment is used.

## 1. Two positive-bank convolutions determine the signed kernel

Let P_N be actual integer Sidon, N>=2, F its positive difference bank,
q=binom(N,2), H=a_N-a_1, and Fhat=F union(-F), Q=2q. Let phi be
odd, with |phi|<=1 on Fhat. Write h(d)=phi(d) for d in F. For u>0
define

```
D(u)=sum_(d,d+u in F)1,
D_h(u)=sum_(d,d+u in F)h(d)h(d+u),
S(u)=sum_(x in F, u-x in F)1,
S_h(u)=sum_(x in F, u-x in F)h(x)h(u-x).
```

The S sums are ordered in the summand x: unequal summands occur twice,
whereas x=u/2 occurs once. This convention exactly counts the two
opposite-sign source pairs when the summands differ and the single
source pair when they coincide.

Splitting signed source pairs by their signs gives

```
K_J,Fhat(u)=2D(u)+S(u),
K_phi,Fhat(u)=2D_h(u)-S_h(u).                            (1)
```

The two same-sign parts have equal products by oddness. Every
opposite-sign pair has product `-h(x)h(y)` and corresponds to one
ordered positive sum. These are identities of unmasked kernels. They
also hold after the common old-label and actual-span masks are applied.
At u>0 the old-label mask excludes precisely F, whether its source
bank is F or Fhat.

## 2. Every linear scalar direction cancels pointwise

For fixed u, the map d -> -d-u is an involution of the signed
correlation index set `{d:d,d+u in Fhat}`. By oddness,

```
phi(-d-u)+phi(-d) = -[phi(d)+phi(d+u)].
```

At its possible fixed point d=-u/2 the summand itself is zero. Hence

```
sum_(d,d+u in Fhat)[phi(d)+phi(d+u)]=0                   (2)
```

at every physical u, before and after either mask. The same mirror map
preserves the output and all three birth ranks, so the linear Born
statistic also vanishes exactly at every stage.

For any actual future block, the full uniform and odd-feature shadows
therefore satisfy `<f_0,f_phi>=0`: their mixed energy expansion has
zero diagonal m*sum(phi) and the zero off-diagonal kernels in (2).
Thus a scalar `(1+t phi)(1+t phi)^T` gives the same physical kernel
as `J+t^2 phi phi^T`. In the scalar-moment cone with its demand (2),
setting t=0 at the same s preserves capacity and weakly increases the
moment demand. The optimal t for this particular odd signed family is
therefore zero. This statement concerns that specified demand, not all
possible higher-moment scalar lower bounds.

## 3. The sign feature at parameter one is the original unit kernel

Take phi(d)=sign(d) and lambda=1 in W=J+lambda phi phi^T. By (1),

```
K_W,Fhat(u)=4D(u),
K_W,Fhat(u)/Q^2=D(u)/q^2.                               (3)
```

This is pointwise equality with the existing positive-bank unit
kernel. It persists under the same old exclusion and actual future
span, for each prefix and hence for the maximum over any common row
family. It is not just equality of total capacities. The same equality
holds for the historical Born mask, because the mirror pair has the
same birth data and the opposite-sign full W entries are zero.

At the level of shadows, W is block diagonal, with value 2 on each
same-sign block. Its energy is `2||f_+||^2+2||f_-||^2`. The two
norms are equal since F and -F have identical autocorrelation kernels.
Thus E_W=4||f_+||^2, and its trace is 4q. Applying the original
positive-bank interval capacity D_pos=L+H-m gives exactly its
existing normalized raw demand

```
delta_pos=m^2/(2D_pos)-m/(2q).                          (4)
```

This equality does not exclude stronger demands from extra information
about those same shadows. It shows why a signed-unit-relative gain
cannot automatically be called an improvement over the best already
available positive-bank unit comparison.

## 4. The specified full-interval sign-moment demand is no stronger

For the sign feature, write A=(sum_(d in F)d)/q. Its signed first
moment is mu=Q A. Using the signed full interval of length
`T=L+2H` and its m holes, the specified lower bound
`LB=12m^2 mu^2/[T(T^2-1)]` gives at lambda=1

```
delta_sign=m^2/[2(T-m)]
            +6m^2 A^2/[T(T^2-1)]-m/(2q).               (5)
```

Assume N>=8, L>=1, m>=1, and D_pos=T-H-m>0. Then

```
                    delta_sign <= delta_pos.            (6)
```

Here is a proof retaining the diameter and interval conventions.
Translate a_1 to zero. The sum of all positive point differences is

```
sum_(i<j)(a_j-a_i)=sum_i(2i-N-1)a_i
                 <=floor(N^2/4)H.
```

The inequality bounds each positive-coefficient point by H and each
negative-coefficient point by zero. Therefore
`A/H<=floor(N^2/4)/q<=N/[2(N-1)]<=4/7` for N>=8. In particular
`12A^2<=4H^2`. Since T=2H+L with integer L>=1,

```
T^2-1-4H(T-H)=L^2-1>=0.
```

Consequently

```
12A^2/[T(T^2-1)] <= H/[T(T-H)]
                   <=H/[(T-m)(T-H-m)]
                   =1/D_pos-1/(T-m).
```

All denominators are positive by the assumptions. Multiplying by
m^2/2 proves (6). This is a comparison for the stated full-interval
LB only. It does not establish dominance for an optimized hole-deleted
variance, higher moments, another odd feature, or another row family.

Thus the sign endpoint of the new positive-Born family reproduces the
positive unit kernel, and its present signed first-moment demand is
weaker for these ranks. It is not a new contradiction route by itself.

## 5. The linear odd feature has a useful geometric sign window

For phi(d)=d/H, let a(u)=K_J,Fhat(u)/Q^2 and
r(u)=K_phi,Fhat(u)/Q^2, including either common mask if desired.
When 0<u<=2H, every correlation pair has d in [-H,H-u]. The convex
quadratic d(d+u) satisfies

```
-u^2/4 <= d(d+u) <= H(H-u).
```

It follows term by term that

```
-(u^2/(4H^2))a(u) <= r(u) <= (1-u/H)a(u).              (7)
```

In particular r(u)<=0 for H<=u<=2H; beyond 2H both kernels vanish.
For u<H the upper bound permits positive residuals. There is no proof
that the physical maximum is supported only in the nonpositive window.
An active row may have a much larger H than the current physical u,
so choosing a row by radius alone is not a valid replacement for the
actual maximum.

The new all-history Born-positivity result for odd monotone features
can remove one historical sign obstruction. Equations (3)--(7) show
the distinct remaining requirements: avoid merely reproducing the old
positive baseline, retain the full signed interval and its diagonal,
and control the actual maximum, span and overlap costs. None is
established here by the geometric window alone. Original Q1 and its
final Lean verification remain unresolved.

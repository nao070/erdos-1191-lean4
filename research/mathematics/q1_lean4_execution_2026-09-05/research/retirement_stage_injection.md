# Same-stage injection and the remaining unpaired birth term

2026-09-05. Author: `/root/causal_telescoping`, GPT-6 Astra Ultra.

**Status.** Exact endpoint and weighted injection identities, two
uniformly summable error terms, and an extension of the late-retirement
tail to its injection images and signed differences. The remaining
joint near-injection and unpaired-birth functional has no proved sign
or required-scale estimate here. Original Q1 remains unresolved.
No Lean declaration, numerical search, or external theorem is used.

This note uses the fixed raw coefficients and actual clocks from
`causal_birth_energy_telescoping.md`, the endpoint involution in
`retirement_shadow_review.md`, and the proved tail in
`late_retirement_tail.md`. All formulas below use the real raw
birth-linear feature, not a separately normalized or recentered copy
at each past birth.

## 1. The injection prices both records at the same actual stage

Let `a_1<...<a_T` be an actual integer Sidon prefix and write

```
m_j = mean(a_1,...,a_(j-1)),
g_(a_j-a_h) = m_j-a_h,
F_n = Delta P_n,    G_n=F_n\F_(n-1),
H_n=a_n-a_1,        q_n=n(n-1)/2,
w_n=1/(q_n^2 H_n^2).
```

For a retiring pair at stage `n`, orient its distinct positive
source labels as `d<e`. Their output is uniquely `e-d=a_n-a_k`
for some `k<n`. Its unique physical overlap position is

```
x=a_n+d=a_k+e.
```

Both sources are old. Write `d=a_i-a_h`, with `h<i<n`. The high
resource `a_n` with label `d` has the low-resource partner `a_i`
with label

```
d' = x-a_i = a_n-a_h.                             (1)
```

Thus `tau(d')=n`. The other label `e=x-a_k` still has birth less
than `n`. Also `k!=i`, since otherwise `e=d'` would be both old
and new. The image pair `{d',e}` has output

```
|d'-e|=|a_k-a_i| in F_(n-1).
```

Consequently it is a mixed-born pair with later source birth
**exactly `n`**, strictly after its output birth. The retiring
record is priced at `w_n` through its output birth; the image is
priced at `w_n` through its later source birth. These prices agree
without introducing the earlier source-time price `w_b`.

The map is injective globally. In its image, the unique new source
label identifies `n`; the unordered pair has a unique physical
overlap position `x`, by difference uniqueness. Recover
`a_i=x-d'`, `a_k=x-e`, and the original old source `d=x-a_n`.
This recovers the source pair and its entire record. Images from
different stages cannot coincide because their later source birth
is fixed by the image itself.

Let `g_e` denote the unchanged coefficient. The exact weighted
difference between image and source is

```
w_n [g_(d')g_e-g_d g_e]
   = w_n (m_n-m_i) g_e.                          (2)
```

The mean difference is strictly positive. The sign of `g_e` is
retained. The scalar nonnegative-carrier injection does not license
deleting that sign in this quadratic identity.

## 2. Pointwise class formulas give an exact stage decomposition

Use the raw convolution notation

```
f_(n-1)=1_(P_(n-1))*(g 1_(F_(n-1))),
h_n=delta_(a_n)*(g 1_(F_(n-1))),
k_n=1_(P_n)*(g 1_(G_n)),
v_n=sum_(d in G_n)g_d^2,
S_(n-1)=sum_(d in F_(n-1))g_d^2,
x_n=<f_(n-1)+h_n,k_n>,
rho_n=<f_(n-1),h_n>.
```

The first inner product is the mixed-born sum at stage `n`; the
second is the retirement sum at stage `n`. There is no factor two
in either unordered pair interpretation.

Difference uniqueness determines `k_n` at every nonzero translated
position. For `d=a_i-a_h in F_(n-1)`, with `h<i<n`, and for `h<n`,

```
k_n(a_n+d) = m_n-a_h,
k_n(a_n-d) = m_n-a_i,
k_n(2a_n-a_h) = m_n-a_h,
k_n(a_n)=0.                                      (3)
```

These three nonzero location classes are disjoint: after subtracting
`a_n` they are `F_(n-1)`, `-F_(n-1)`, and `G_n`. They exhaust
the support of `k_n`, because its defining locations are
`a_n+a_k-a_h`, with `k<=n` and `h<n`. Coincidences when `k=h`
have total coefficient zero by class centering.

In particular

```
<h_n,k_n>
 = sum_(2<=i<n) sum_(h<i) (m_i-a_h)(m_n-a_h)
 = sum_(2<=i<n) [v_i+(m_n-m_i) sum_(h<i)(m_i-a_h)]
 = S_(n-1).                                      (4)
```

This exact positive automatic term uses the special raw linear
coefficients. No positivity assumption on individual coefficients
is involved.

Define three stage functionals:

```
A_n^inj = sum_(d=a_i-a_h in F_(n-1))
                    (m_n-m_i) f_(n-1)(a_n+d),

U_n = sum_(d=a_i-a_h in F_(n-1))
                    (m_n-a_i) f_(n-1)(a_n-d),

F_n^fix = sum_(h<n) (m_n-a_h) f_(n-1)(2a_n-a_h).
```

Here `F_n^fix` is a scalar and is distinct from the label bank `F_n`.
The first functional is exactly the sum of the unweighted differences
in (2), since `f_(n-1)(a_n+d)` sums the unchanged old resource
coefficients over all retirements with high label `d`. An absent
overlap contributes zero.

Combining (3)–(4) with the definitions of `x_n,rho_n` gives

```
x_n-rho_n = S_(n-1)+A_n^inj+U_n+F_n^fix.          (5)
```

The terms have a literal pair partition. The injection images are
the mixed old/new edges at positions `a_n+F_(n-1)` with both
resource points old. The term (4) is the internal high/low orbit
edge at those positions. The positions `2a_n-a_h` add fixed-point
mixed-born edges. Finally `a_n-d<a_n` has a new-class resource whose
source upper endpoint `a_n` is at or beyond the position. These are
the unpaired resources; their mixed-born edges give `U_n`.
All of these are actual mixed-born pairs. No independent pair copy
is allocated by the partition.

## 3. The automatic and fixed-point terms have finite total price

From `S_(n-1)<=q_(n-1)H_n^2`,

```
0 <= w_n S_(n-1)
 <= q_(n-1)/q_n^2
 = 4/n^2-2/[n(n-1)].
```

Therefore, uniformly in every history and terminal horizon,

```
sum_(n=2..T) w_n S_(n-1) <= 4 zeta(2)-6 < 0.58.  (6)
```

At each position, `f_(n-1)` is a sum of at most `n-1` old resource
coefficients, each of absolute value at most `H_n`. There are
`n-1` positions in the fixed-point expression, and its new
coefficients also have absolute value at most `H_n`. Thus

```
|F_n^fix| <= (n-1)^2 H_n^2,
sum_(n=2..T) w_n |F_n^fix|
 <= 4 sum_(n=2..infinity) 1/n^2
 = 4(zeta(2)-1) < 2.58.                          (7)
```

The bounds (6)–(7) use no cap. They control the full signed
fixed-point term in absolute value and keep every diagonal in (4).

The same elementary estimate on the unpaired term gives only

```
w_n |U_n| <= (n-1)q_(n-1)/q_n^2
                  = 2(n-2)/n^2.                 (8)
```

Its sum can grow logarithmically. Equation (8) is an upper bound,
not an example achieving that size and not evidence of a sign. In
particular (7) cannot be applied to the more numerous unpaired
positions in (8).

## 4. Late original retirements also have negligible image and gap

For each original retirement, retain its original later source birth
`b<n=r`. Fix one `alpha>1/4`, and call the original record far when
`r>=b(log b)^alpha`. The injection image is tagged by this original
record; this is not a claim about every born pair of stage `r`.

There are at most `b^3/2` original records at source birth `b`, each
with only one actual retirement. Their images are distinct by §1.
For an image from such a record,

```
|g_(d')| <= H_r,      |g_e| <= H_b,
0 < m_r-m_i <= H_r,   H_b <= H_r.
```

Consequently both the image product and its signed difference have
the same summable price bound as the original retirement:

```
w_r |g_(d')g_e| <= 1/q_r^2 <= 16/r^4,
w_r |(m_r-m_i)g_e| <= 1/q_r^2 <= 16/r^4.           (9)
```

Define

```
C_alpha = 8 sum_(b=3..infinity) 1/[b(log b)^(4alpha)] < infinity.
```

Counting by the original source birth and using (9) proves separately

```
sum_(far original retirements) w_r |g_(d')g_e| <= C_alpha,
sum_(far original retirements) w_r |(m_r-m_i)g_e| <= C_alpha. (10)
```

The two statements concern different sums, each bounded as displayed.
One need not use a triangle inequality with twice the constant for
the second sum, because its mean difference has the direct bound (9).
As in `late_retirement_tail.md`, there is no additional sum over
possible retirement ranks. The original retired products themselves
already have absolute sum at most `C_alpha` on this tail.

Thus the far portion can be removed from both sides of the stage
injection at bounded error. This remains a statement at price `w_r`;
it does not control the source-time price `w_b`, or the lag
commutator with coefficient `w_b-w_r`.

## 5. The remaining joint functional and the Abel energy

Let

```
B_T(w)=sum_(n=2..T) w_n x_n,
R_T(w)=sum_(n=2..T) w_n rho_n,
J_T^near = sum_(near original retirements, r<=T)
                          w_r (m_r-m_i) g_e,
U_T(w)=sum_(n=2..T) w_n U_n,
J_T=J_T^near+U_T(w).
```

Here near means `b<r<b(log b)^alpha`. By (5)–(7) and (10),

```
B_T(w)-R_T(w) = J_T + e_T,                        (11)
|e_T| <= [4 zeta(2)-6]+4[zeta(2)-1]+C_alpha.
```

More exactly, `e_T` is the sum of the nonnegative automatic term,
the signed fixed-point term, and the far injection difference.
The proof preserves each of these separately before giving the
absolute bound.

Recall the causal note's exact Abel identity

```
2B_T(w)+2R_T(w)+D_T(w)=A_T(w),
0<=D_T(w)<=8 zeta(2)-10,
A_T(w)=w_T E_T+sum_(n=2..T-1)(w_n-w_(n+1))E_n.
```

Solving these two exact equations gives

```
B_T(w) = A_T(w)/4 + J_T/2 - D_T(w)/4 + e_T/2,
R_T(w) = A_T(w)/4 - J_T/2 - D_T(w)/4 - e_T/2.     (12)
```

Under the causal note's full fixed-onset cap and good-epoch hypotheses,
`A_T(w)` diverges. Equations (11)–(12) identify the outstanding
same-stage transport functional without swapping source and
retirement clocks. For example, a new estimate

```
J_T >= -(1/2-epsilon) A_T(w)-O(1),
```

with one fixed `epsilon>0`, would prove
`B_T(w)>=epsilon A_T(w)/2-O_alpha(1)`. A bounded negative part for
`J_T` would give the stronger coefficient `1/4` in (12). Neither
estimate is proved here. The shared physical margin in the causal
note would remain even after such a causal improvement.

## 6. What centering and a square completion actually supply

There is an exact short form of (5): put `d_n=k_n-h_n`. Then

```
x_n-rho_n = S_(n-1)+<f_(n-1),d_n>,
||d_n||^2 = (n-1)v_n-S_(n-1).                    (13)
```

The second equality follows from the known norms of `h_n,k_n`
and (4). It is nonnegative because it is a squared norm. Its
weighted sum is finite, bounded by the causal diagonal charge.
Completing the square yields

```
2(x_n-rho_n)
 = ||f_(n-1)+d_n||^2-||f_(n-1)||^2
                         -(n-1)v_n+3S_(n-1).    (14)
```

The first two squares in (14) do not form the actual energy
increment. Indeed `f_(n-1)+d_n=f_n-2h_n`, whereas the history
evolves by `f_n=f_(n-1)+h_n+k_n`. Consequently (14) cannot be
summed as a telescoping nonnegative boundary energy. Nor does the
finite sum of `w_n||d_n||^2` bound the bilinear work in (13), since
the corresponding sum of `w_n||f_(n-1)||^2` has no finite bound
from these calculations. A finite increment norm alone is insufficient
for that Cauchy--Schwarz step.

Class centering has supplied (4), (6), and the exact square (13).
It has not canceled the irregular retirement incidence sums in
`J_T^near`, or the unpaired weights `(m_n-a_i)` in `U_n`.
The global zero and first-moment identities concern full coefficient
banks; the restricted samples at `a_n+d` and `a_n-d` in §2 are
different sets of actual overlap positions. No missing sign theorem
is being inferred from those moments.

The new bounded reduction is the common-stage injection (1)–(2),
the summable complete automatic/fixed errors, the far-image and
far-gap bounds (10), and the explicit remaining joint functional
in (11)–(12). Its required quantitative estimate, and the one
physical budget needed for Q1, remain open.

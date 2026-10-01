# Completed same-sum fibers: a Gram term and two retained corrections

Date: 2026-09-05. Owner: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Status: an exact decomposition of each **complete** distinct-triple fiber
into a nonnegative Gram term, a diagonal error bounded by `28R` for a
fiber of `R` triples, and two explicit signed corrections. The diagonal
errors sum to `O(N^3)` over all sums. The corrections are retained and
have not been proved to have a cubic lower bound. Thus this is not the
requested universal full-total theorem, an actual counterexample family,
or original Q1. No Lean source was changed or Lean verification claimed.

This starts from equation (6) of `birth_linear_total_causal_sign.md`.
It does not retest individual-fiber-pair positivity or free-gap
copositivity. The finite calculations below test specified identities on
two fixed complete fibers. They are not sign searches.

## 1. One complete fiber and its covariance interpretation

Let `P={a_1<...<a_N}` be actual integer Sidon, with repeated two-sums
included; `H=a_N-a_1>0`. Write `m_j=(sum_(i<j)a_i)/(j-1)` for
`j>=2`, and set `m_1=a_1` only for the matrix identities below.
This convention adds no actual label.

Fix a sum `s`. Let `U_1,...,U_R` be **all** distinct-point triples of
sum `s`, ordered by their largest endpoint rank `n_1<...<n_R`.
Sidonness makes their supports disjoint. In particular their endpoint
incidence vectors `nu_r` have disjoint supports, mass 3, and coordinate
sum `s`. Put `c=s/3` and normalize once by the actual terminal `H`:

```
x_i  = (a_i-c)/H,
mu_i = (m_i-c)/H,
b_i  = (a_i-m_i)/H,
t_i  = x_i+mu_i,
Q_ji = mu_j-x_i     if i<j,      Q_ji=0 otherwise.           (1)
```

Then `Q 1=0`, `0<=b_i<=1`, `|Q_ji|<=1`, and `t_i` is strictly
increasing. Both `x_i` and `mu_i` lie in `[-1,1]`; their individual
ranges have length at most 1. Every completed triple has zero `x` sum.

Write `v_r=nu_1+...+nu_r`, `v_0=0`, `lambda_r=2mu_(n_r)`, and

```
A_r = (diag(x)+lambda_r I) Q.
```

The direct complete-fiber formula is exactly

```
F_s := sum_(u<r) Phi(U_u,U_r)
     = sum_(r=1..R) v_(r-1)^T A_r nu_r.                    (2)
```

All `Q` entries refer to the original ambient history. Its prefix mean
is not replaced by a mean over fiber endpoints.

For `r>=2`, the `M=3(r-1)` old completed endpoints have mean `c`,
so their normalized `x` mean is zero. Put `f_r=Q nu_r`. Equation (2)
also reads

```
v_(r-1)^T A_r nu_r
 = M [Cov_old(x,f_r)+lambda_r Mean_old(f_r)].              (3)
```

This is an exact covariance decomposition of the endpoint update.
The first covariance does not automatically have a sign. Indeed

```
f_r(j)
 = sum_(h in U_r,h<j)(mu_j-mu_h)
     - sum_(h in U_r,h<j) b_h.                            (4)
```

The first term is nondecreasing in `j`; the second consists of downward
jumps in `f_r` at the triple endpoints. Thus `Cov_old(x,f_r)` is a
nonnegative monotone covariance minus another nonnegative covariance.
The drift in (3) can also have either sign. Formula (4) explains why
centering the completed endpoints is useful but insufficient by itself.

## 2. An exact Brownian Gram identity for the ambient birth operator

Let `B=diag(b)`. The symmetric matrix

```
G = Q+Q^T-B
```

has entries, including its diagonal,

```
G_ij = mu_i+mu_j-min(t_i,t_j).                            (5)
```

For example, if `i<j`, the right side is `mu_j-x_i=Q_ji`;
on the diagonal it is `mu_i-x_i=-b_i`. If `sum_i u_i=0`, the
two rank-one mean terms in (5) disappear and the usual interval
representation of `min(t_i,t_j)` gives

```
u^T(Q+Q^T)u = sum_i b_i u_i^2 - Gamma(u),

Gamma(u)
 = integral_(t_1..t_N) [sum_i u_i 1[t_i>y]]^2 dy
 = sum_(k=1..N-1) (t_(k+1)-t_k) [sum_(i>k)u_i]^2
 >= 0.                                                  (6)
```

Possible negative values of `t_1` cause no problem: subtracting `t_1`
from every endpoint changes `min(t_i,t_j)` by a constant matrix, which
vanishes on a zero-mass vector. This is a finite step-function square,
not an appeal to a stochastic independence assumption.

The actual prefix means are nondecreasing. Consequently

```
lambda_(r+1)-lambda_r >= 0,
sum_(r<R)(lambda_(r+1)-lambda_r) <= 2.                    (7)
```

This monotonicity is what will give the Gram term its positive sign.

## 3. Centering the sequence of complete triples

For `R>=1`, set

```
e       = v_R/R,
xi_r    = v_r-r e             (0<=r<=R),
d_r     = xi_r-xi_(r-1) = nu_r-e,
S_r     = A_r+A_r^T,
J_r     = A_r-A_r^T,
Delta_r = lambda_(r+1)-lambda_r       (r<R).               (8)
```

Here `xi_0=xi_R=0`; all the `xi_r` and `d_r` have zero mass and
zero `x` moment. Disjoint endpoint membership gives exact norms:

```
||e||_1 = 3,
||xi_r||_2^2 = 3r(1-r/R) <= 3R/4,
||xi_r||_1   = 6r(1-r/R) <= 3R/2,
||d_r||_1    = 6(1-1/R) <= 6.                            (9)
```

All vectors in (8) are literal functions on the original `N` point
indices. Their centering uses this complete fixed fiber. No fiber is
replaced by a clique or an independent physical difference budget.

Define the following four quantities, with empty sums equal to zero:

```
Gram_s = (1/4) sum_(r<R) Delta_r Gamma(xi_r) >= 0;          (10)

Diag_s = -(1/4) sum_(r=1..R) d_r^T S_r d_r
         -(1/4) sum_(r<R) Delta_r sum_i b_i xi_r(i)^2;     (11)

Circ_s = (1/2) sum_(r=1..R) xi_(r-1)^T J_r d_r
           + sum_(r<R) xi_r^T J_(r+1) e;                 (12)

Mean_s = sum_(r=1..R) (r-1)e^T A_r e
           - sum_(r<R) (r-1)Delta_r xi_r^T Q^T e.         (13)
```

The complete-fiber identity is

```
              F_s = Gram_s + Diag_s + Circ_s + Mean_s.    (14)
```

The first term is a literal weighted sum of squares, and the next
section gives a linear-in-`R` bound on the second. The last two terms
are signed and form part of the identity, not an omitted remainder.

### Derivation of (14)

First replace `v_(r-1)=xi_(r-1)+(r-1)e` and `nu_r=d_r+e` in (2).
For the part with two centered vectors, use

```
xi_(r-1)^T A_r d_r
 = (1/4)[xi_r^T S_r xi_r
            -xi_(r-1)^T S_r xi_(r-1)-d_r^T S_r d_r]
       +(1/2)xi_(r-1)^T J_r d_r.                         (15)
```

Summing its symmetric differences by parts, the endpoint terms vanish
because `xi_0=xi_R=0`. Also

```
S_r-S_(r+1) = -Delta_r(Q+Q^T).
```

Inserting (6) gives exactly `Gram_s+Diag_s` and the first sum of
`Circ_s`.

The terms containing one copy of `e` are

```
sum_r xi_(r-1)^T A_r e
  +sum_r(r-1)e^T A_r(xi_r-xi_(r-1)).
```

Another finite summation by parts gives

```
sum_(r<R) xi_r^T J_(r+1)e
  -sum_(r<R)(r-1)Delta_r xi_r^T Q^T e.
```

Finally the two-copy terms are `sum_r(r-1)e^T A_r e`. These are
the remaining parts of (12)--(13). This proves (14) with its factors,
rank offsets, and diagonal costs intact.

## 4. The diagonal error really is summable over all fibers

Since `|x_i+lambda_r|<=3` and `Q` is strictly lower triangular,
every entry of `S_r` has absolute value at most 3. There is only one
nonzero triangular summand at each off-diagonal position. Thus

```
(1/4) sum_r |d_r^T S_r d_r|
 <= (3/4) sum_r ||d_r||_1^2 <= 27R.
```

By (7), (9), and `0<=b_i<=1`, the absolute value of the second
term in (11) is at most `3R/8`. In particular,

```
                         |Diag_s| <= 28R.                 (16)
```

Every distinct-point triple belongs to exactly one sum fiber, so

```
sum_s R_s = binom(N,3),
sum_s |Diag_s| <= 28 binom(N,3).                          (17)
```

Fibers of size one contribute zero to (14) and can be included in
(17) or omitted. This step uses no density assumption or terminal
cap.

For comparison, the same elementary norm estimates give only

```
                    |Circ_s+Mean_s| <= 50 R^2.            (18)
```

For example, the two terms in (12) are each at most `(27/2)R^2`;
the two terms in (13) are at most `(27/2)R^2` and `9R^2`.
Their sum is less than `50R^2`. Since `R_s<=N/3`, summing this
bound gives an order-`N^4` error, not a cubic one. This is the precise
remaining distinction between the proved diagonal estimate and the
unproved signed correction estimate.

## 5. Consequence for the actual full causal total

Use the notation of `birth_linear_total_causal_sign.md`:
`C_h=sum_(j>h)z_jh`, `S=sum z_jh^2<=q`, and `X_z=L(z)+S/2`.
That note proves, with all six-distinct fibers included,

```
X_z = (1/2)sum_h C_h^2-S/2 + sum_s F_s + D_rep,
|D_rep|<=12N^3.
```

Combining this with (14)--(17) gives the exact global reduction

```
X_z = (1/2)sum_h C_h^2 + sum_s Gram_s
         +sum_s(Circ_s+Mean_s) + E_N,

|E_N| <= 12N^3+28 binom(N,3)+q/2 <= 17N^3  (N>=2).       (19)
```

Thus **all** diagonal and repeated-endpoint contributions can be paid
at cubic scale, and the displayed first two terms are nonnegative.
A sufficient remaining estimate is

```
sum_s(Circ_s+Mean_s) >= -C N^3                             (20)
```

for one fixed constant. More generally it would be enough to lose less
than the retained positive quantities in (19), plus a cubic error.
Neither estimate is proved here. The skew operators in (12) and the
fiber-average terms in (13) are functions of the actual point order,
prefix means, and complete sum fibers. Their signs cannot be replaced
by a statement for an unrelated free matrix or free gap vector.

If (20) were established, (19) would give the requested actual lower
bound, and it could be inserted into the same physical historical
comparison with the future-moment demand. Until then, (19) is a
reduction of that obligation. The fixed-onset cap and good-epoch
conditions have not been shown to control (12)--(13), and no separate
fiber capacity is added to the global envelope.

## 6. Fixed exact identity checks and actual execution provenance

The new checker uses standard-library rational arithmetic only:

- `research/evidence/completed_fiber_gram_exact.py`
- `research/evidence/completed_fiber_gram_exact.txt`
- `research/evidence/completed_fiber_gram_exact.stderr.txt`
- `research/evidence/completed_fiber_gram_exact.run.json`

It checks the complete sum-40 fiber of `{0,1,10,13,17,39}` and the
complete sum-1533 fiber of the fixed 32-point ruler already present in
the preceding notes. These fibers were specified before executing the
checker. Their complete lists are respectively

```
sum 40:   (10,13,17), (0,1,39);
sum 1533: (259,420,854), (1,273,1259), (3,12,1518).
```

The script verifies Sidon difference uniqueness, disjointness of each
complete fiber, the centered sequence and its exact norms, (4), (6),
the direct endpoint formula (2), the four-term identity (14), the
nonnegativity of (10), and the diagonal bound (16). Both fixed checks
passed with observed return code **0**, and stderr was empty.

The checker was launched once by an instrumented `exec_command` wrapper
using the actual executable
`/opt/homebrew/opt/python@3.14/bin/python3.14`. Immediately before
and after that subprocess, the wrapper recorded the source SHA-256:

```
4ffa49d47e9f80a5a9a219c316cb5f08deb804b3cd2f1b00b376df86316cd400
```

The hashes matched and the source-unchanged gate passed. The actual
recorded UTC timestamps were

```
start:  2026-09-05T08:00:42.779718+00:00
finish: 2026-09-05T08:00:42.842507+00:00.
```

The JSON contains the argv, cwd, measured duration, both hashes, source
gate result, return code, and the complete stdout and stderr. These
were recorded around this new execution, not reconstructed as unknown
historical pre-run observations. The enclosing tool call returned exit
code 0 with chunk identifier `ed1099`.

For transparency, the two original fiber totals were respectively
`-2096/22815` and `22733071423/155806470456`; each equals the sum
of its four independently computed components in the output. Their
signs are not used as evidence about the asymptotic corrections in
(20). The substantive result is the analytic decomposition (19) with
the explicit remaining signed terms.

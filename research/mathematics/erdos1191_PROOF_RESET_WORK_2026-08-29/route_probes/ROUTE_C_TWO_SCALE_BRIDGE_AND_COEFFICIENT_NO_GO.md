# Route C: two-scale bridge and coefficient-only no-go

Date: 2026-08-29  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Scope: project-internal exact identities, one scoped method no-go, and one
unproved falsifiable bridge obligation  
Claim boundary: **no compatible infinite history theorem, Question 1 result,
Question 2 result, global optimum, or novelty claim is made.**

## 1. Source and notation boundary

[Hou--Zhao v2](https://arxiv.org/html/2607.01169v2), Sections 2 and 3.1,
proves a finite vector-smoothing lemma and its boundary quadratic program for
several kernels at one finite Sidon set. Its Section 5 suggests controlled
cross-kernel terms, subject to nonnegativity of the combined correlation at
every nonzero shift. The positive-definite
cross-matrix master used here is the project-internal extension recorded in
`ROUTE_C_BOUNDARY_NORMALIZED_CROSS_KERNEL.md`; it is not attributed to
Hou--Zhao.

This memo separates three operations which must not be conflated:

1. using two smoothing widths on the **same** finite Sidon set;
2. applying a finite theorem separately to successive prefixes of one
   infinite Sidon sequence; and
3. putting two **different nested prefixes** into one cross-channel energy.

Operation 1 is legal and retains the finite master. Operation 2 is legal
pointwise but creates no cross-scale covariance. Operation 3 has different
correlation and cover identities and is not supplied by the finite lemma.

Throughout, kernels and sets are finitely supported on `Z`, so every sum can
be rearranged without a convergence issue.

## 2. Exact common-grid lift for widths `T` and `2T`

Fix positive integers `m,h` and put

\[
T=mh,\qquad M=2m,\qquad U=Mh=2T.
\]

Let

\[
p=(p_0,\ldots,p_{m-1}),\qquad
r=(r_0,\ldots,r_{m-1})
\]

be nonnegative probability vectors. A left-aligned common-`h`-grid
representation is

\[
P_i^{(1)}=
\begin{cases}p_i,&0\le i<m,\\0,&m\le i<2m,\end{cases}
\tag{2.1}
\]

and

\[
P_{2i}^{(2)}=P_{2i+1}^{(2)}={r_i\over2}
\qquad(0\le i<m).
\tag{2.2}
\]

Both vectors have mass one. Define the actual integer kernels by

\[
K_s(ih+v)={P_i^{(s)}\over h},
\qquad 0\le v<h,\quad 0\le i<M,
\tag{2.3}
\]

and set them to zero elsewhere. Thus `K_1` has width `T`, while `K_2`
is the width-`2T` lift of `r`.

For zero-extended `P^(s)`, define

\[
R_{st}(q)=\sum_iP_i^{(s)}P_{i+q}^{(t)}.
\tag{2.4}
\]

Let `H=(h_st)` be a symmetric positive-definite `2 by 2` matrix and put

\[
C(q)=\sum_{s,t=1}^2h_{st}R_{st}(q).
\tag{2.5}
\]

### Proposition 2.1: exact block interpolation

For `d=qh+v`, `0<=v<h`, the combined integer correlation is

\[
\boxed{
\mathcal C_H(qh+v)
 ={(h-v)C(q)+vC(q+1)\over h^2}.}
\tag{2.6}
\]

#### Proof

At shift `qh+v`, a source `h`-cell overlaps the cell `q` places to its
right in exactly `h-v` lattice points and the cell `q+1` places to its right
in exactly `v` lattice points. On each overlap the product of the two kernel
values is `P_i^(s)P_j^(t)/h^2`. Summing the two overlap classes gives (2.6).
\(\square\)

No common symmetry centre is needed for (2.6). Moreover, for arbitrary real
kernels,

\[
R_{st}(-q)=R_{ts}(q).
\]

Since `H` is symmetric, this implies

\[
C(-q)=C(q),\qquad \mathcal C_H(-d)=\mathcal C_H(d).
\tag{2.7}
\]

### Corollary 2.2: exact every-shift gate

Positive definiteness gives `C(0)>=0`. Equation (2.6) therefore shows

\[
\boxed{
\mathcal C_H(d)\ge0\ \hbox{for every nonzero integer }d
\iff C(q)\ge0\ \hbox{for every positive integer }q.}
\tag{2.8}
\]

Only `1<=q<=M-1` can be nonzero. The reverse implication uses the fact that
the right side of (2.6) is a nonnegative interpolation. The forward
implication follows by taking `v=0`.

### Proposition 2.3: mass, zero lag, and same-prefix upper energy

Because both kernels have mass one,

\[
\sum_{d\in\mathbb Z}\mathcal C_H(d)
 =\mathbf1^TH\mathbf1=:s.
\tag{2.9}
\]

Also

\[
\mathcal C_H(0)={C(0)\over h}={a_H\over U},
\qquad a_H:=M C(0).
\tag{2.10}
\]

Let `A` be one finite Sidon set of cardinality `k`, put

\[
u_s=\mathbf1_A*K_s,
\qquad
E_H(A)=\sum_{s,t}h_{st}\langle u_s,u_t\rangle,
\]

and let `Delta(A)` be its represented positive differences. Direct
expansion gives

\[
E_H(A)=k\mathcal C_H(0)
       +2\sum_{d\in\Delta(A)}\mathcal C_H(d).
\tag{2.11}
\]

Under the gate (2.8), filling unrepresented differences is legal, so

\[
\boxed{
E_H(A)\le s+{a_H(k-1)\over U}.}
\tag{2.12}
\]

The constant `s` is the total correlation mass, not a separately chosen
normalization.

## 3. Exact boundary cover and the centering/parity caveat

For arbitrary probability kernels `K_s`, no block symmetry is needed for
the lower-energy identity. Let `z(x) in R^2` be any vector weight satisfying

\[
\sum_{s=1}^2\sum_yK_s(y)z_s(a+y)\ge1
\tag{3.1}
\]

at every possible mark position `a`. Then

\[
\begin{aligned}
k
&\le\sum_xz(x)^Tu(x),\\
k^2
&\le
\left(\sum_xz(x)^TH^{-1}z(x)\right)E_H(A).
\end{aligned}
\tag{3.2}
\]

The first line follows by interchanging the `x` and mark sums; the second is
Cauchy--Schwarz in the `H` metric.

Suppose now that the two kernels have been placed on a common `M`-cell grid,
put `n=LM`, and use a constant bulk tail `gamma` with

\[
\gamma_s\ge0,\qquad\gamma_1+\gamma_2=1.
\]

The left boundary program has variables `z_j^-`, `0<=j<n`, tail
`z_j^-=gamma` for `j>=n`, and exact constraints

\[
\sum_{s=1}^2\sum_{i=0}^{M-1}P_i^{(s)}z_{t+i,s}^-\ge1,
\qquad0\le t<n.
\tag{3.3}
\]

Let

\[
\Phi_-:=\sum_{j=0}^{n-1}(z_j^-)^TH^{-1}z_j^-.
\tag{3.4}
\]

The right boundary uses the reflected kernels
`P_i^(s),vee=P_(M-1-i)^(s)` and has its own feasible variables and objective
`Phi_+`. Define

\[
\beta=\gamma^TH^{-1}\gamma,
\qquad
b_{\pm}=\beta+{\Phi_-+\Phi_+\over M}-2L\beta.
\tag{3.5}
\]

Assembling the two boundary weights and the bulk tail gives the exact metric
cost

\[
\sum_xz(x)^TH^{-1}z(x)
=\beta N+b_{\pm}U-\beta,
\tag{3.6}
\]

provided `N>=2LU`, so the two boundary regions are disjoint. Combining
(2.12), (3.2), and (3.6) gives

\[
\boxed{
k^2\le(\beta N+b_{\pm}U-\beta)
       \left(s+{a_H(k-1)\over U}\right).}
\tag{3.7}
\]

If the common-grid placement is symmetric, reflection identifies the two
boundary programs, `Phi_-=Phi_+=Phi`, and

\[
b_{\pm}=\beta+2\left({\Phi\over M}-L\beta\right),
\tag{3.8}
\]

which is the previously recorded cross-matrix master.

### Centering and parity warning

The left-aligned embedding (2.1)--(2.2) always exists, but the zero-padded
short kernel need not be palindromic on the `M`-cell common support. To invoke
the symmetric factor `2Phi`, the two kernels must admit integer translations
to one common symmetry centre. Equal centering can be achieved by further
integer-grid refinement when the necessary half-width is an integer number
of refined cells. If the two support parities force one centre to be integral
and the other half-integral, one may not silently introduce a half-lattice:
use the actual unit grid and the separate objectives `Phi_-`, `Phi_+`.

This is a boundary-accounting caveat, not a failure of the correlation
identity. The combined correlation remains even by (2.7).

### Leading normalization

Metric Cauchy--Schwarz gives

\[
\delta:=\beta s
=(\gamma^TH^{-1}\gamma)(\mathbf1^TH\mathbf1)\ge1.
\tag{3.9}
\]

Equality holds exactly when

\[
\gamma={H\mathbf1\over s},
\tag{3.10}
\]

provided this vector is coordinatewise nonnegative. Different block widths
do not themselves change the total-mass or leading-normalization identities.

For finitely many widths, the unit grid always supplies a common grid. For a
countably infinite dyadic family the maximum support is unbounded, so the
finite lemma does not automatically produce one infinite Hilbert object:
one needs a finite-horizon operator, a terminal boundary, and estimates
uniform in that horizon.

## 4. Different nested prefixes: exact decomposition

Now let `A subset B` be two nested prefixes of one increasing Sidon sequence.
Write

\[
O=A,\qquad W=B\setminus A.
\]

Because these are prefixes, every old mark is smaller than every mark in
`W`. Put

\[
u_1=\mathbf1_O*K_1,
\qquad
u_2=\mathbf1_B*K_2.
\]

For positive `d`, let `Delta_OO`, `Delta_OW`, and `Delta_WW` denote the
differences represented by old--old, old--new, and new--new pairs. Sidon
uniqueness makes these three sets pairwise disjoint.

Using the convention

\[
R_{st}(d)=\sum_xK_s(x)K_t(x+d),
\]

define

\[
\begin{aligned}
C_{OO}(d)&:=\sum_{s,t}h_{st}R_{st}(d)=C_H(d),\\
C_{OW}(d)&:=h_{12}R_{21}(d)+h_{22}R_{22}(d),\\
C_{WW}(d)&:=h_{22}R_{22}(d).
\end{aligned}
\tag{4.1}
\]

### Proposition 4.1: old/new energy identity

The exact energy is

\[
\boxed{
\begin{aligned}
E_H(O,B)={}&|O|C_H(0)+|W|h_{22}R_{22}(0)\\
&+2\sum_{d\in\Delta_{OO}}C_{OO}(d)
 +2\sum_{d\in\Delta_{OW}}C_{OW}(d)
 +2\sum_{d\in\Delta_{WW}}C_{WW}(d).
\end{aligned}}
\tag{4.2}
\]

#### Proof

At an old diagonal mark both channels occur, giving `C_H(0)`. At a new
diagonal mark only channel 2 occurs, giving `h_22 R_22(0)`. For an
old--new pair `a<b`, channel 2 is the only channel available at `b`.
The two orientations in the symmetric quadratic form give

\[
2\bigl(h_{12}R_{21}(b-a)+h_{22}R_{22}(b-a)\bigr).
\]

The old--old and new--new formulas follow similarly. Grouping by the unique
positive difference proves (4.2). \(\square\)

Consequently the universal positive-part envelope is

\[
\boxed{
\begin{aligned}
E_H(O,B)\le{}&|O|C_H(0)+|W|h_{22}R_{22}(0)\\
&+2\sum_{d\ge1}
\max\{0,C_{OO}(d),C_{OW}(d),C_{WW}(d)\}.
\end{aligned}}
\tag{4.3}
\]

At a fixed positive shift, Sidon uniqueness permits at most one of the three
pair types, which proves (4.3). A cost-free typewise fill requires

\[
C_{OO}(d),\ C_{OW}(d),\ C_{WW}(d)\ge0
\qquad\hbox{for every }d\ge1.
\tag{4.4}
\]

For nonnegative `K_2` and positive-definite `H`, `C_WW>=0`, but the
old--new condition is additional. The single combined gate `C_H(d)>=0`
controls only the old--old sector. Even when (4.4) holds, three different
correlation sums remain; there is no identity reducing (4.3) to the one
total mass `1^T H 1`.

## 5. Different nested prefixes: exact cover obstruction

For an arbitrary vector weight `z(x)`, direct rearrangement gives

\[
\begin{aligned}
\sum_xz(x)^T(u_1(x),u_2(x))
={}&\sum_{a\in O}\sum_yK_1(y)z_1(a+y)\\
&+\sum_{b\in B}\sum_yK_2(y)z_2(b+y).
\end{aligned}
\tag{5.1}
\]

If `z=gamma` in the bulk and both kernels have mass one, an old mark
contributes

\[
\gamma_1+\gamma_2=1,
\]

whereas a new mark contributes only `gamma_2`. Thus the natural bulk target
is

\[
|O|+\gamma_2|W|
=\gamma_1|O|+\gamma_2|B|,
\tag{5.2}
\]

not `|B|`. To obtain unit cover for every new mark from a constant simplex
tail one must have `gamma_2>=1`; hence `gamma=(0,1)` and the old channel is
deleted from the leading bulk.

One can impose membership-sensitive cover constraints instead,

\[
\begin{aligned}
\sum_yK_1(y)z_1(a+y)+\sum_yK_2(y)z_2(a+y)&\ge1
&& (a\in O),\\
\sum_yK_2(y)z_2(b+y)&\ge1
&& (b\in W),
\end{aligned}
\tag{5.3}
\]

but then the weight is not the constant Hou--Zhao bulk tail unless the first
channel is absent. Its metric cost can change at order `N`, so the leading
normalization must be rederived rather than imported from (3.9).

Equations (4.2) and (5.1) are the precise reasons that assigning different
prefixes to the two channels is not a routine common-grid extension. The
grid still exists; the common difference coefficient and common cover do
not.

## 6. Coefficient-only dyadic summability no-go

This section concerns operation 2: applying a finite bound independently to
every dyadic prefix. It makes no assumption that a critical infinite branch
exists.

Let `A_j` be any finite Sidon set of cardinality

\[
k_j=2^j
\]

contained in an integer interval of length `N_j`. Its positive differences
are distinct integers in `{1,...,N_j-1}`, so

\[
N_j\ge1+{k_j(k_j-1)\over2}.
\tag{6.1}
\]

Fix `j_0>=1`. Let `omega_(j,J)` be triangular weights satisfying the only condition needed
for the upper summability statement,

\[
|\omega_{j,J}|\le W
\tag{6.2}
\]

for one constant `W` independent of `j,J`. The project Fejer weights

\[
\omega_{j,J}=\left({J+1-j\over J+1}\right)^2,
\qquad j\le J,
\tag{6.3}
\]

satisfy (6.2) with `W=1`.

### Theorem 6.1: every fixed power-saving finite remainder is summable

Fix `delta>0`. Suppose a finite Sidon estimate has a uniform remainder

\[
F(N)\le N^{1/2}+R(N),
\qquad |R(N)|\le C_\delta N^{1/2-\delta},
\tag{6.4}
\]

where `C_delta` is independent of the prefix and of `j`. After division by
the leading `N_j^(1/2)`, its entire remainder contributes at most

\[
\boxed{
\sup_{J\ge j_0}
\sum_{j=j_0}^J|\omega_{j,J}|
{ |R(N_j)|\over N_j^{1/2}}
\le
W C_\delta\,2^{2\delta}
{2^{-2\delta j_0}\over1-2^{-2\delta}}.}
\tag{6.5}
\]

In particular the contribution is `O_delta(1)` uniformly in `J`.

#### Proof

For `k_j>=2`, `k_j-1>=k_j/2`. Equation (6.1) gives

\[
N_j\ge{k_j^2\over4},
\qquad
N_j^{-\delta}\le4^\delta k_j^{-2\delta}
=2^{2\delta}2^{-2\delta j}.
\tag{6.6}
\]

Use (6.2), (6.4), and sum the resulting geometric series. \(\square\)

The uniformity of `C_delta` and `W` is essential. This theorem says nothing
if the finite coefficient grows with `j` or if the weights are not uniformly
bounded.

### The `N^(1/4)` coefficient explicitly

For

\[
F(N)\le N^{1/2}+cN^{1/4}+O(1),
\tag{6.7}
\]

one has `delta=1/4`. More explicitly, (6.1) gives

\[
N_j^{-1/4}
\le\left({2\over k_j(k_j-1)}\right)^{1/4}
\le\sqrt2\,2^{-j/2}.
\tag{6.8}
\]

Changing the finite coefficient from `c_0` to any other bounded `c_1`
therefore changes the normalized dyadic sum by at most

\[
|c_0-c_1|\sqrt2
{2^{-j_0/2}\over1-2^{-1/2}}=O(1).
\tag{6.9}
\]

The `O(1)` term in (6.7), after normalization, is also geometrically
summable. Thus even deleting the entire finite `N^(1/4)` term cannot alter a
logarithmic dyadic order. The exact Hou--Zhao cross perturbation improves its
finite coefficient from `0.9434925907135450...` to
`0.9434922260277725...`; (6.9) applies to that improvement and to any other
uniform bounded coefficient improvement.

### Comparison with the existing harmonic floor

For a hypothetical eventually `C`-critical compatible branch, the existing
integer new-birth theorem gives, at `m=2^j`,

\[
Z_{2^j}\ge{1\over1536C\log(4\cdot2^j)}
={1\over1536C(j+2)\log2}.
\tag{6.10}
\]

For the actual weights (6.3), direct expansion gives

\[
\sum_{j=j_0}^J{\omega_{j,J}\over j+2}
=\log J+O_{j_0}(1).
\tag{6.11}
\]

Indeed `omega=1-2j/(J+1)+j^2/(J+1)^2`; after division by `j+2`, the first
sum is harmonic and the other two are bounded. Hence

\[
\sum_{j=j_0}^J\omega_{j,J}Z_{2^j}
\ge{1\over1536C\log2}\log J-O_{C,j_0}(1).
\tag{6.12}
\]

The uniformly bounded contribution in (6.5) or (6.9) cannot change the
coefficient or order of (6.12). Applying a better finite coefficient at each
prefix is therefore a proved no-go for the existing harmonic obstruction.
It remains a finite `F(N)` improvement, not a compatible-history mechanism.

There is an additional scale mismatch: under the critical cap
`N_j=O_C(k_j^2 log k_j)`, the ratio `sqrt(N_j)/k_j` can be as large as
`O_C(sqrt(log k_j))`; the cap gives no matching lower bound on that ratio.
A second-order finite coefficient does not uniformly close the possible
leading slack.

## 7. Exact rank-one covariance identity

The coefficient-only closure does not rule out retaining an actual
cross-scale covariance before filling all unrepresented differences.

Fix `0<lambda<1`, put

\[
D=\begin{pmatrix}\lambda&0\\0&1-\lambda\end{pmatrix},
\qquad
v=\binom{1}{-1},
\tag{7.1}
\]

and, for

\[
0<\theta<\lambda(1-\lambda),
\]

define

\[
H_\theta=D-\theta vv^T
=\begin{pmatrix}
\lambda-\theta&\theta\\
\theta&1-\lambda-\theta
\end{pmatrix}.
\tag{7.2}
\]

Its determinant is

\[
\det H_\theta=\lambda(1-\lambda)-\theta>0,
\]

and its first diagonal entry is positive, so `H_theta` is positive definite.
Moreover

\[
H_\theta\mathbf1=D\mathbf1
=:\gamma=(\lambda,1-\lambda)^T.
\tag{7.3}
\]

Consequently

\[
s=\mathbf1^TH_\theta\mathbf1=1,
\qquad
\beta=\gamma^TH_\theta^{-1}\gamma=1.
\tag{7.4}
\]

Thus this contrast preserves the leading normalization exactly.

For two same-prefix smoothed fields

\[
u=\mathbf1_A*K_T,
\qquad w=\mathbf1_A*K_{2T},
\]

put

\[
V:=\|u-w\|_2^2.
\tag{7.5}
\]

The energy identity is

\[
\boxed{
E_{H_\theta}
=\lambda\|u\|_2^2+(1-\lambda)\|w\|_2^2-\theta V
=E_D-\theta V.}
\tag{7.6}
\]

This is an actual prefix-dependent covariance deficit, not a changed finite
coefficient.

### Exact Sherman--Morrison boundary price

Since

\[
v^TD^{-1}v={1\over\lambda}+{1\over1-\lambda}
={1\over\lambda(1-\lambda)},
\]

Sherman--Morrison gives

\[
\boxed{
H_\theta^{-1}
=D^{-1}+\kappa D^{-1}vv^TD^{-1},
\qquad
\kappa={\theta\over1-\theta/[\lambda(1-\lambda)]}.}
\tag{7.7}
\]

For any fixed feasible boundary weight `z(x)` with bulk tail `gamma`, define

\[
B_D:=\sum_xz(x)^TD^{-1}z(x),
\qquad
Q:=\sum_x\bigl(v^TD^{-1}z(x)\bigr)^2.
\tag{7.8}
\]

Then

\[
\boxed{B_{H_\theta}=B_D+\kappa Q.}
\tag{7.9}
\]

The penalty `Q` is boundary-localized: by (7.3),

\[
v^TD^{-1}\gamma=v^T\mathbf1=0,
\tag{7.10}
\]

so every constant bulk-tail site contributes zero.

The diagonal correlation is nonnegative at every shift. Its legal Sidon
upper bound is

\[
U_D
=1+(k-1)
\left(\lambda R_{TT}(0)+(1-\lambda)R_{2T,2T}(0)\right).
\tag{7.11}
\]

Using the exact subtraction (7.6), rather than filling its cross term, gives

\[
\boxed{
k^2\le(B_D+\kappa Q)(U_D-\theta V).}
\tag{7.12}
\]

The improvement over the corresponding fixed-cover diagonal product is
exactly

\[
\boxed{
G:=B_DU_D-(B_D+\kappa Q)(U_D-\theta V)
=\theta B_DV-\kappa Q U_D+\kappa\theta QV.}
\tag{7.13}
\]

Thus `V` is useful only after paying the exact inverse-metric boundary price.
Positive definiteness alone does not make `G` positive.

If instead one fills the combined cross correlation directly, its exact
form is

\[
C_\theta(d)
=\lambda R_{TT}(d)+(1-\lambda)R_{2T,2T}(d)
-\theta R_{K_T-K_{2T},K_T-K_{2T}}(d).
\tag{7.14}
\]

That route requires

\[
C_\theta(d)\ge0\qquad(d\ne0).
\tag{7.15}
\]

After (7.15), the upper bound is only

\[
E_{H_\theta}\le1+(k-1)C_\theta(0),
\tag{7.16}
\]

which discards the actual `V` and returns to the coefficient-only class
closed in Section 6. The retained-covariance inequality (7.12) needs no
combined sign gate: it uses the legal diagonal upper bound and subtracts the
exact nonnegative square.

## 8. Precise sufficient finite-horizon bridge obligation

For a finite compatible dyadic chain, let `N_j` be the interval length of the
`2^j`-mark prefix. A **nonanticipating parameter rule** `Pi` assigns the two
widths, kernels, `lambda`, `theta`, and a feasible boundary cover at scale `j`
using only the prefix through that scale and fixed data known before the
terminal horizon. Let `G_j(Pi)` be the exact quantity (7.13). Thus the same
rule applies to two chains sharing the same prefix; it may not optimize using
marks that appear only later.

The following is a sufficient finite-horizon obligation for this rank-one
ansatz to interact with the known harmonic floor. It is deliberately stronger
than an estimate asserted only along an extendable eventually critical
history.

> **Two-scale net-deficit obligation (unproved).** For every fixed critical-cap
> constant `C`, there must exist a nonanticipating admissible rule `Pi`,
> explicit constants `eta_C>0` and `K_C<infinity`, and an exact single-owner
> joint-energy ledger such that the favorable term is `G_j(Pi)/N_j`, occurs
> with the sign opposite the existing positive harmonic sector, and, for every
> horizon `J` and every finite compatible chain obeying the required critical
> cap through that horizon,
> \[
> \sum_{j=j_0}^J\omega_{j,J}{G_j(\Pi)\over N_j}
> \ge \eta_C\log J-K_C
> \tag{8.1}
> \]
> for an explicit `eta_C>0`. To absorb the currently certified floor with
> unit coefficient, one needs
> \[
> \eta_C\ge{1\over1536C\log2}.
> \tag{8.2}
> \]
> Any different allocation coefficient must be stated and propagated
> explicitly.

In addition to (8.1), the ledger must prove all of the following:

1. every correlation fill is justified either by its exact gate or by the
   retained-square identity (7.6);
2. the boundary term `Q_j` and terminal boundary at horizon `J` are paid
   once, with Fejer-weight reindexing included;
3. the same compatible prefix history supplies every `V_j`; optimizing a
   different unrelated finite set at each `j` is inadmissible;
4. no difference atom, diagonal energy budget, or boundary cover is used at
   two scales without an explicit capacity split; and
5. if different prefixes are placed in the two channels, the typewise
   identities (4.2)--(5.3), not the same-prefix master, are used.

Once `Pi`, `eta_C`, and `K_C` are fixed explicitly, one finite compatible
chain violating (8.1) refutes that specified candidate. With an unspecified
`O_C(1)` instead of fixed `K_C`, a single finite shortfall would not suffice;
one would need a sequence for which the shortfall tends to infinity. If
one proves instead that

\[
{G_j(\Pi)\over N_j}=O_C(N_j^{-\delta})
\]

uniformly over the chains and horizons in (8.1) for some fixed `delta>0`,
then Theorem 6.1 closes this rank-one
ansatz as coefficient-only. Finite survival of a specified candidate does not
prove the universally quantified theorem.

This obligation is not asserted here. Even (8.1) would be only the required
energy-level carrier until its single-owner signed ledger is proved. No
Question 1 or Question 2 inference follows from the identities alone.

## 9. Registry-ready claims

| ID | Evidence/status | Exact claim | Explicit non-claim |
|---|---|---|---|
| `RC-2S-COMMON-GRID` | `PROJECT_INTERNAL_THEOREM` | Two widths `T,2T` on the same finite Sidon set admit the exact common-grid correlation (2.6), gate (2.8), mass (2.9), generic left/right boundary master (3.7), and leading normalization (3.9). | No infinite-horizon or coefficient optimum. |
| `RC-2S-NESTED-FACTOR-NO-GO` | `PROJECT_INTERNAL_THEOREM`, scoped method closure | For channels using nested prefixes `A subset B`, the exact energy is the three-type identity (4.2), one combined sign gate is insufficient, and a simplex bulk tail covers new marks only with weight `gamma_2`; unit outer-prefix cover deletes the old channel from the constant leading bulk. | Does not rule out boundary-localized or membership-sensitive cross-prefix theorems. |
| `RC-2S-COEFFICIENT-SUMMABILITY` | `HUMAN_PROOF_AUDITED`, `G2` scoped no-go | Under uniformly bounded triangular weights, every uniform finite remainder `O(N^(1/2-delta))`, `delta>0`, contributes `O(1)` after dyadic normalization; in particular any bounded `N^(1/4)` coefficient change cannot alter the certified `Omega(log J)` floor. | Does not rule out retained covariance, entropy, or arithmetic inverse theorems. |
| `RC-2S-RANK-ONE-IDENTITY` | `PROJECT_INTERNAL_THEOREM` identity plus `G0/OPEN` obligation | Equations (7.6)--(7.13) give the exact covariance gain and Sherman--Morrison boundary price; (8.1)--(8.2) is the precise unproved harmonic-scale target. | No positivity of `G`, compatible-chain theorem, Q1/Q2 result, or novelty claim. |

## 10. Final scope boundary

The memo proves that common-grid geometry is not the main obstruction for
two widths on one prefix. The obstructions are instead:

- loss of one scalar difference coefficient and one simplex cover when
  channels use different prefixes;
- geometric summability of every fixed power-saving finite remainder; and
- the need to retain an actual history-dependent covariance after its exact
  boundary price.

Question 1 and Question 2 remain unresolved.

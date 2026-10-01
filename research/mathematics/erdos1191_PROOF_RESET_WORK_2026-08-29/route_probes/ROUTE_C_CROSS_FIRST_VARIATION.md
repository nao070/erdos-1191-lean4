# Route C: first variation of the boundary-normalized cross objective

Date: 2026-08-29  
Status: `PROJECT_INTERNAL_THEOREM`  
Scope: fixed kernels, with either a reoptimized boundary QP or a separately
identified fixed feasible boundary certificate  
Claim boundary: **no global cross optimum, compatible-history theorem,
Question 1 result, or Question 2 result is claimed.**

## 1. Source boundary and related exact certificates

Hou and Zhao's [Section 2 vector smoothing
lemma](https://arxiv.org/html/2607.01169v2#S2) supplies the diagonal weighted
direct sum, joint boundary cover, and finite Sidon energy argument. Their
[Section 3.1](https://arxiv.org/html/2607.01169v2#S3.SS1) supplies the
fixed-kernel boundary quadratic program and its primal--dual formulation.
Their [Section 5](https://arxiv.org/html/2607.01169v2#S5) identifies controlled
cross-kernel terms as a possible future direction and explicitly notes that
positive semidefiniteness alone does not replace nonnegativity of the combined
correlation at every nonzero shift.

Every formula below involving a non-diagonal matrix `H`, its normalized tail,
or its first variation is a **project-internal extension**, not a theorem
attributed to Hou--Zhao.

The exact finite background is recorded in two companion certificate memos:

- `ROUTE_C_BOUNDARY_NORMALIZED_CROSS_KERNEL.md` proves the normalized
  positive-definite extension and records a bounded exact fixed-kernel/QP
  certificate;
- `ROUTE_C_HOU_ZHAO_CROSS_PERTURBATION.md` records exact row-sum-zero
  perturbations of the pinned official eight-kernel boundary certificate.

Those memos prove only their stated finite scopes. This memo supplies the
local analytic criterion connecting the two settings; it does not enlarge
either computational scope.

## 2. Fixed-kernel normalized setup

Fix integers `R,m,L>=1` and put `n=Lm`. For `1<=r<=R`, let

\[
p^{(r)}=(p_0^{(r)},\ldots,p_{m-1}^{(r)})
\]

be a symmetric nonnegative probability vector. Fix an interior direct-sum
weight

\[
\lambda=(\lambda_1,\ldots,\lambda_R),\qquad
\lambda_r>0,\qquad \sum_r\lambda_r=1,
\]

and write

\[
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_R).
\]

Let `J=J^T` be a real symmetric direction and define

\[
H_\varepsilon=\Lambda+\varepsilon J,
\qquad
s_\varepsilon=\mathbf 1^TH_\varepsilon\mathbf 1,
\]

\[
\gamma_\varepsilon
=\frac{H_\varepsilon\mathbf 1}{s_\varepsilon},
\qquad
\beta_\varepsilon
=\gamma_\varepsilon^TH_\varepsilon^{-1}\gamma_\varepsilon.
\tag{2.1}
\]

For sufficiently small `|epsilon|`, positive definiteness and coordinatewise
positivity of `gamma_epsilon` follow from `Lambda>0`. Put

\[
\tau:=\mathbf 1^TJ\mathbf 1.
\]

Then normalization is exact:

\[
H_\varepsilon^{-1}\gamma_\varepsilon
=\frac{\mathbf 1}{s_\varepsilon},
\qquad
\beta_\varepsilon=\frac1{s_\varepsilon},
\qquad
\beta_\varepsilon s_\varepsilon=1.
\tag{2.2}
\]

At `epsilon=0`,

\[
s'_0=\tau,
\qquad
\beta'_0=-\tau,
\qquad
\gamma'_0=J\mathbf 1-\lambda\tau.
\tag{2.3}
\]

The last formula is essential: changing `H` generally changes both the metric
in the boundary objective and the fixed tail in the covering inequalities.
The derivative identities below do not require `b_0>0`; interpreting a
decrease as an improved finite Sidon coefficient additionally requires
`b_0>0`, and then `b(H_epsilon)>0` persists for sufficiently small
`|epsilon|`.

## 3. Boundary QP and the normalized tail derivative

Order the finite boundary variables `q_(j,r)` **j-major**, with
`0<=j<n`. Set `q_j=gamma_epsilon` for `j>=n`. For `0<=t<n`, define

\[
A_{t,(j,r)}=
\begin{cases}
p_{j-t}^{(r)},&0\le j-t<m,\\
0,&\text{otherwise},
\end{cases}
\tag{3.1}
\]

and

\[
B_{tr}:=\sum_{\substack{0\le i<m\\t+i<n}}p_i^{(r)}.
\tag{3.2}
\]

Since each kernel has total mass one and `sum_r gamma_r=1`, the nontrivial
cover constraints are

\[
Aq\ge c(H),
\qquad
c(H)=B\gamma(H).
\tag{3.3}
\]

The constraint at `t=n` is automatic equality. Equation (2.3) gives

\[
c'_0[J]=B(J\mathbf 1-\lambda\tau).
\tag{3.4}
\]

The finite `q_(j,r)` are unconstrained real variables apart from the cover;
no coordinatewise nonnegativity condition is imposed on them.

Let

\[
D(H)=I_n\otimes H^{-1}
\]

and define the reoptimized boundary value

\[
\Phi^*(H):=\min\{q^TD(H)q:Aq\ge c(H)\}.
\tag{3.5}
\]

After redundant zero rows are deleted, the usual strict-feasibility argument
applies near `Lambda`. The primal minimizer `q^0` is unique because `D` is
positive definite. Write its blocks as `q_j^0` and put

\[
w_j:=\Lambda^{-1}q_j^0.
\tag{3.6}
\]

The dual optimal set is

\[
\mathcal Y_0:=\mathop{\rm argmax}_{y\ge0}
\left\{c_0^Ty-\frac14y^TA(I_n\otimes\Lambda)A^Ty\right\}.
\tag{3.7}
\]

### Theorem 3.1 (project-internal envelope formula)

For a one-sided perturbation in direction `J`, the directional derivative of
the optimal value is

\[
\boxed{
(\Phi^*)'_0[J]
=-\sum_{j=0}^{n-1}w_j^TJw_j
+\max_{y\in\mathcal Y_0}
y^TB(J\mathbf 1-\lambda\tau).
}
\tag{3.8}
\]

If the dual optimizer is unique, say `y^0`, then `Phi^*` is differentiable in
this direction and

\[
\boxed{
(\Phi^*)'_0[J]
=-\sum_jw_j^TJw_j
+(B^Ty^0)^TJ\mathbf 1
-((B^Ty^0)^T\lambda)\tau.
}
\tag{3.9}
\]

No derivative of the reoptimized primal vector occurs in (3.8)--(3.9): its
first-order contribution vanishes by stationarity. The second term is the
dual price of changing the tail and hence the right-hand side `c(H)`.

#### Proof

At `H_0=Lambda`,

\[
\left.\frac{d}{d\varepsilon}H_\varepsilon^{-1}\right|_0
=-\Lambda^{-1}J\Lambda^{-1}.
\]

Consequently

\[
(q^0)^TD'_0q^0=-\sum_jw_j^TJw_j.
\]

The Lagrangian, with the sign convention `y>=0` for `Aq-c>=0`, is

\[
q^TDq-y^T(Aq-c).
\]

Its parameter derivative at a saddle point is therefore

\[
(q^0)^TD'_0q^0+y^Tc'_0[J].
\]

Directional Danskin gives the maximum over the dual optimal set. Uniqueness
of the dual removes the maximum and (3.4) gives (3.9). \(\square\)

For later use, let

\[
v:=B^Ty^0,
\]

and, when the dual is unique, define the symmetric matrix

\[
K_\Phi
:=-\sum_jw_jw_j^T
+\operatorname{sym}(v\mathbf 1^T)
-(v^T\lambda)\mathbf 1\mathbf 1^T,
\tag{3.10}
\]

where `sym(M)=(M+M^T)/2`. Then

\[
(\Phi^*)'_0[J]=\langle J,K_\Phi\rangle_F.
\tag{3.11}
\]

## 4. First variation of the cross objective

Let the fixed zero-lag kernel Gram matrix be

\[
P_{rs}:=\langle p^{(r)},p^{(s)}\rangle
\]

and define

\[
a(H):=m\langle H,P\rangle_F,
\tag{4.1}
\]

\[
b(H):=\beta(H)+2\left(\frac{\Phi^*(H)}m-L\beta(H)\right).
\tag{4.2}
\]

At the diagonal point,

\[
a_0=m\sum_r\lambda_r\|p^{(r)}\|_2^2,
\qquad
b_0=1+2\left(\frac{\Phi_0^*}m-L\right).
\tag{4.3}
\]

Equations (2.3), (3.11), and (4.1)--(4.2) give

\[
a'_0[J]=m\langle J,P\rangle_F,
\tag{4.4}
\]

\[
b'_0[J]=(2L-1)\tau+\frac2m\langle J,K_\Phi\rangle_F.
\tag{4.5}
\]

Hence, under unique-dual differentiability,

\[
\boxed{
(ab)'_0[J]=\langle J,\mathcal G\rangle_F,
}
\tag{4.6}
\]

where the exact project-internal gradient is

\[
\boxed{
\mathcal G
=mb_0P
+a_0\left((2L-1)\mathbf 1\mathbf 1^T+\frac2mK_\Phi\right).
}
\tag{4.7}
\]

In the nonunique-dual case, substitute (3.8) into

\[
(ab)'_0[J]
=mb_0\langle J,P\rangle_F
+a_0\left((2L-1)\tau+\frac2m(\Phi^*)'_0[J]\right).
\tag{4.8}
\]

This is a directional, generally nonsymmetric derivative rather than a
single gradient matrix.

## 5. Scale invariance and diagonal stationarity

For every scalar `rho>0`,

\[
\gamma(\rho H)=\gamma(H),\qquad
a(\rho H)=\rho a(H),
\]

\[
\beta(\rho H)=\rho^{-1}\beta(H),\qquad
\Phi^*(\rho H)=\rho^{-1}\Phi^*(H),
\]

so

\[
a(\rho H)b(\rho H)=a(H)b(H).
\tag{5.1}
\]

At a differentiability point, (5.1) implies

\[
\langle\mathcal G,\Lambda\rangle_F=0.
\tag{5.2}
\]

If `lambda` is an interior local optimum when only the diagonal weights are
varied in the simplex, then

\[
\mathcal G_{11}=\cdots=\mathcal G_{RR}.
\]

Combining this equality with (5.2) and `sum lambda_r=1` gives

\[
\boxed{\mathcal G_{rr}=0\quad(1\le r\le R).}
\tag{5.3}
\]

Diagonal local optimality imposes no sign on the off-diagonal entries of
`mathcal G`.

## 6. Positive-definite and correlation tangent cone

For an integer lag `ell`, extend every kernel by zero and put

\[
(R_\ell)_{rs}:=\sum_i p_i^{(r)}p_{i+\ell}^{(s)}.
\tag{6.1}
\]

The combined discrete correlation is

\[
C_\ell(H)=\langle H,R_\ell\rangle_F,
\qquad
C'_\ell[J]=\langle J,R_\ell\rangle_F.
\tag{6.2}
\]

Because `H_0=Lambda` lies in the interior of the positive-definite cone,
**every** symmetric `J` preserves positive definiteness for all sufficiently
small `|epsilon|`. Thus PD imposes no first-order tangent restriction here.

Only the active correlation inequalities restrict a one-sided direction. For
the path `epsilon>=0`, the exact tangent cone is

\[
\boxed{
\mathcal T_{\rm corr}
=\{J=J^T:\langle J,R_\ell\rangle_F\ge0
\text{ whenever }\ell\ne0\text{ and }C_\ell(\Lambda)=0\}.
}
\tag{6.3}
\]

There are only finitely many relevant lags because the kernels have finite
support. Lags with a strictly positive baseline correlation remain positive
for sufficiently small `epsilon`. A two-sided feasible linear path requires
equality in (6.3) at every active lag. Symmetry of `H` gives
`C_(-ell)=C_ell`.

At the actual zero shift, positive definiteness gives

\[
C_0(H)=\sum_i(p_i^{(1)},\ldots,p_i^{(R)})
H(p_i^{(1)},\ldots,p_i^{(R)})^T>0,
\]

so the obstruction below concerns a **nonzero lag whose baseline correlation
is zero**, not the actual shift `ell=0`.

## 7. Normalized negative-pair criterion and zero-correlation-lag obstruction

Fix `r<s` and let

\[
J^-_{rs}:=-(e_re_s^T+e_se_r^T).
\]

Its scale-normalized representative is

\[
\widehat J^{rs}:=J^-_{rs}+2\Lambda.
\tag{7.1}
\]

It satisfies

\[
\mathbf 1^T\widehat J^{rs}\mathbf 1=0
\]

and has a negative `(r,s)` entry. By scale invariance,

\[
\boxed{
(ab)'_0[\widehat J^{rs}]=-2\mathcal G_{rs}.
}
\tag{7.2}
\]

Consequently, at a differentiable diagonal local optimum, this negative pair
strictly improves the reoptimized objective to first order if and only if

\[
\mathcal G_{rs}>0
\tag{7.3}
\]

and `widehat J^(rs)` belongs to the correlation tangent cone (6.3).

There is a sharp obstruction at every active nonzero lag. If
`C_ell(Lambda)=0`, then positivity of the `lambda_r` and nonnegativity of the
kernels imply

\[
(R_\ell)_{tt}=0\quad\text{for every }t.
\]

Therefore

\[
\langle\widehat J^{rs},R_\ell\rangle_F
=-((R_\ell)_{rs}+(R_\ell)_{sr})\le0.
\tag{7.4}
\]

The negative pair passes this active gate exactly when

\[
\boxed{
(R_\ell)_{rs}=(R_\ell)_{sr}=0.
}
\tag{7.5}
\]

Thus a zero baseline autocorrelation lag with positive cross overlap blocks
the pure negative pair immediately, even though positive definiteness is
open. For a general signed direction, the exact finite first-order test is
to minimize \(\langle\mathcal G,J\rangle_F\) over (6.3), together with whatever
off-diagonal sign or sparsity restrictions define the proposed class. A
negative minimum certifies strict first-order improvement. A zero minimum is
only first-order inconclusive and requires a second-variation analysis.

## 8. Fixed-boundary row-sum-zero corollary

The official-certificate perturbation uses a different operation from
Theorem 3.1: its already feasible boundary vectors are held fixed rather than
reoptimized.

### Corollary 8.1 (fixed feasible boundary)

Assume

\[
J\mathbf 1=0,
\qquad
H_\varepsilon=\Lambda+\varepsilon J.
\tag{8.1}
\]

Then, exactly for every admissible `epsilon`,

\[
H_\varepsilon\mathbf 1=\lambda,
\qquad
s_\varepsilon=1,
\qquad
\gamma_\varepsilon=\lambda,
\qquad
\beta_\varepsilon=1.
\tag{8.2}
\]

Let fixed boundary vectors \(\bar w_j\) be given and set

\[
\bar q_j=\lambda\odot\bar w_j\quad(0\le j<n),
\qquad
\bar q_j=\lambda\quad(j\ge n).
\tag{8.3}
\]

If these vectors satisfy the diagonal direct-sum cover, then the cover is
unchanged under (8.1), because neither the kernels, `gamma`, \(\bar q\), nor the
right-hand side `c=B lambda` changes. Define the fixed-certificate cost

\[
\Phi_{\rm fix}(\varepsilon)
:=\sum_{j=0}^{n-1}\bar q_j^TH_\varepsilon^{-1}\bar q_j.
\tag{8.4}
\]

Its ordinary derivative is

\[
\boxed{
\Phi_{\rm fix}'(0)
=-\sum_j\bar w_j^TJ\bar w_j.
}
\tag{8.5}
\]

The associated valid fixed-boundary quantities are

\[
a_{\rm fix}(\varepsilon)=m\langle H_\varepsilon,P\rangle_F,
\]

\[
b_{\rm fix}(\varepsilon)
=1+2\left(\frac{\Phi_{\rm fix}(\varepsilon)}m-L\right).
\tag{8.6}
\]

This construction gives a valid finite coefficient whenever `H_epsilon` is
positive definite, every combined correlation is nonnegative, and
`b_fix(epsilon)>0`.

Equation (8.5) is **not** the reoptimized-QP claim (3.8). It differentiates
the cost of one fixed feasible certificate. In general,

\[
\Phi^*(H_\varepsilon)\le\Phi_{\rm fix}(\varepsilon),
\tag{8.7}
\]

and equality is not asserted. The two derivatives coincide at zero only if
the fixed boundary vector is itself an optimizer of the diagonal QP and the
corresponding sensitivity hypotheses hold. The exact official-cover
perturbation memo deliberately makes no such reoptimization claim.

## 9. Claim boundary

This theorem is local and finite-dimensional. It holds for fixed kernels and
classifies first-order matrix directions after the normalized boundary tail
and, in Theorem 3.1, the boundary QP have been accounted for exactly. It does
not prove that a favorable direction exists for an arbitrary diagonal local
optimum, and it does not turn a bounded numerical search into a global
optimum or novelty theorem.

Even a strict decrease of `a(H)b(H)` improves only the secondary constant in
a finite estimate of the form

\[
F(N)\le N^{1/2}+\sqrt{a(H)b(H)}\,N^{1/4}+O(1).
\]

It supplies no compatible infinite Sidon history and no change of asymptotic
order for Erdős Problem #1191. Questions 1 and 2 remain unresolved.

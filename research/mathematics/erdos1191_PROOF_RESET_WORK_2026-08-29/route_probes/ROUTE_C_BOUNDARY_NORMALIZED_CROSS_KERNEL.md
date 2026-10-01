# Route C: boundary-normalized positive-definite cross kernels

Date: 2026-08-29  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Scope: project-internal extension plus exact bounded finite search  
Claim boundary: **no global optimum, compatible history theorem, Question 1 result, or Question 2 result is claimed.**

## Source boundary

Hou and Zhao's [Section 2 vector smoothing lemma](https://arxiv.org/pdf/2607.01169v2)
uses a weighted Hilbert direct sum, a joint boundary cover, and a quadratic
boundary cost. Their [Section 3.1](https://arxiv.org/pdf/2607.01169v2) gives
the fixed-kernel primal--dual quadratic program. Their Section 5 observes
that a matrix cross extension additionally needs the combined correlation to
be nonnegative at every shift; positive semidefiniteness alone is not enough.

The positive-definite cross-matrix theorem below is a **project-internal
derivation**, not a theorem attributed to Hou--Zhao.

## Exact normalized extension

Let `p^(1),...,p^(R)` be symmetric nonnegative probability vectors of common
joint support length `m`. Let `H` be symmetric positive definite and let
`gamma` lie in the nonnegative simplex. Define

\[
q_{j,r}=\gamma_rw_j^{(r)},\qquad
\beta=\gamma^TH^{-1}\gamma,\qquad
s=\mathbf1^TH\mathbf1,
\]

\[
a=m\sum_{r,t}h_{rt}\langle p^{(r)},p^{(t)}\rangle,
\]

\[
\Phi=\sum_{j=0}^{Lm-1}q_j^TH^{-1}q_j,
\qquad
b_H=\beta+2\left(\frac\Phi m-L\beta\right).
\]

For `j>=Lm`, set `q_j=gamma`. Coordinates with `gamma_r=0` are fixed to
zero and deleted; they are not free optimization variables.

If the combined discrete correlation

\[
C(d)=\sum_{r,t}h_{rt}\sum_i p_i^{(r)}p_{i+d}^{(t)}
\]

is nonnegative at every positive discrete shift, then the piecewise-constant
block lift is also nonnegative. Indeed, for `d=qh+t`, `0<=t<h`,

\[
C_{\rm lift}(d)
=\frac{(h-t)C(q)+tC(q+1)}{h^2}.
\]

Writing `T=mh`, the exact Cauchy--Schwarz argument gives, for `N>=2LT`,

\[
\boxed{
k^2\le
(\beta N+b_HT-\beta)
\left(s+\frac{a(k-1)}T\right).
}
\tag{1}
\]

The optimization requires `b_H>0`.

## Leading normalization and corrected general coefficient

Metric Cauchy--Schwarz gives

\[
\delta:=\beta s
=(\gamma^TH^{-1}\gamma)(\mathbf1^TH\mathbf1)
\ge(\gamma^T\mathbf1)^2=1.
\]

Equality holds exactly when

\[
\gamma=\frac{H\mathbf1}{s},
\]

provided this vector is coordinatewise nonnegative. If `H*1/s` has a
negative coordinate, equality is not attainable in the cover-weight simplex.

Balancing (1) gives

\[
k\le \sqrt\delta\,N^{1/2}
+\boxed{\delta^{1/4}\sqrt{ab_H}}\,N^{1/4}+O(1).
\tag{2}
\]

The general coefficient in (2) is **not** `sqrt(delta*a*b_H)`. At the only
leading-constant-one normalization, `delta=1`, it reduces to `sqrt(a*b_H)`.

## Exact boundary QP

Put `n=Lm` and order the retained `q` variables **j-major**. For `0<=q<n`,

\[
A_{q,(j,r)}=
\begin{cases}
p_{j-q}^{(r)},&0\le j-q<m,\\
0,&\text{otherwise},
\end{cases}
\]

\[
c_q=1-\sum_r\gamma_r
\sum_{\substack{0\le i<m\\q+i\ge n}}p_i^{(r)}.
\]

After deleting zero-`gamma` coordinates, let

\[
D=I_n\otimes(H^{-1})_{\rm retained}.
\]

Then

\[
\Phi^*=\min\{q^TDq:Aq\ge c\},
\]

with exact dual

\[
\Phi^*=\max_{y\ge0}
\left(c^Ty-\frac14y^TAD^{-1}A^Ty\right).
\]

Every accepted certificate verifies

\[
2Dq=A^Ty,\quad Aq\ge c,\quad y\ge0,
\quad y_q((Aq)_q-c_q)=0,
\]

and exact equality of primal and dual values. The canonical default-Python
replay uses a deterministic standard-library floating active-set discovery,
followed by exact rational reconstruction and complete KKT verification. No
NumPy/SciPy runtime is required, and floating point proves nothing.

## Exact same-kernel cross hit

Take

\[
m=3,\quad L=2,
\]

\[
p^{(1)}=(1/4,1/2,1/4),\qquad
p^{(2)}=(3/8,1/4,3/8),
\]

\[
H=\begin{pmatrix}1&-1/5\\-1/5&1\end{pmatrix},
\qquad \gamma=(1/2,1/2).
\]

Here `beta=5/8`, `s=8/5`, and `delta=1`. The exact correlations are

\[
(C(0),C(1),C(2))=(19/32,27/80,53/320),
\]

so the shift gate passes strictly. The exact active-all primal and dual are
stored in the JSON certificate. They give

\[
\Phi=\frac{629198090085}{175479603614},\qquad
a=\frac{57}{32},
\]

\[
b_H=\frac{361764546455}{701918414456},
\]

\[
ab_H=\frac{20620579147935}{22461389262592}
\approx0.9180455807.
\]

For the same kernels with `H_12=0` and the same half cover,

\[
\Phi_0=\frac{82462667}{28528330},\qquad
a_0=\frac{69}{32},
\]

\[
b_0=\frac{36547849}{85584990},
\qquad
a_0b_0=\frac{840600527}{912906560}.
\]

The exact product ratio is

\[
\frac{ab_H}{a_0b_0}
=\frac{1190831349642527325}{1194398763365825948}<1.
\]

Thus the coefficient improves by the square-root factor
`0.9985054901...`, about **0.15%**, for these same kernels.

## Bounded exhaustive grid

The replay loop uses exact rational gates and exact post-discovery KKT:

- all five symmetric denominator-eight `m=3` kernels;
- all fifteen symmetric denominator-eight `m=5` kernels;
- `L=1,2`;
- all 21 reduced negative rationals with denominator at most eight;
- diagonal direct sums with `lambda=1/8,...,7/8`.

Pairs in the `m=5` list which are common-zero paddings of an `m=3` pair are
normalized back to their minimal joint support and not counted twice. The
certificate records raw counts, padding exclusions, gate passes, and exact
KKT counts.

The cross candidate above is the best cross product in this normalized
bounded grid. The exact diagonal/direct-sum winner is

\[
m=5,\quad L=2,\quad\lambda=1/8,
\]

\[
p^{(1)}=(0,1/8,3/4,1/8,0),
\]

\[
p^{(2)}=(1/8,1/4,1/4,1/4,1/8),
\]

with

\[
\Phi=\frac{6624259711621393}{720717809725096},
\quad a=\frac{85}{64},
\]

\[
b=\frac{1218876138683173}{1801794524312740},
\]

\[
ab=\frac{20720894357613941}{23062969911203072}
\approx0.8984486576.
\]

Its coefficient is `0.9478653162...`; it remains about **1.085% better**
than the cross candidate's `0.9581469515...`. Therefore the same-kernel hit
is real but is not a bounded-grid global improvement.

## Claim boundary and replay

This grid is finite and deliberately small. It proves neither global
optimality nor a current-best finite Sidon coefficient. It supplies no
compatible infinite history and changes no asymptotic order in Erdős #1191.
Compatible history, Question 1, and Question 2 remain open.

The certificate is `boundary_normalized_cross_kernel_certificate.json`.
From `route_probes/` run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_boundary_normalized_cross_kernel_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 boundary_normalized_cross_kernel_probe.py \
  --self-check --verify boundary_normalized_cross_kernel_certificate.json
```

The mutation suite rejects sign-gate failure, non-PD `H`, cover failure,
stationarity and complementarity failure, the wrong general coefficient,
zero-`gamma` free coordinates, and false global/current-best/Q1/Q2 claims.

# Route C: exact Hou--Zhao two-cycle cross perturbation

**Status.** This is an exact finite-certificate refinement of one pinned
eight-kernel input.  It is **not** a global optimum, a novelty determination,
a prize claim, or a resolution of either question in Erdős Problem #1191.

## Source and scope

The source input is Hou--Zhao, *Vector-Valued Smoothing for Finite Sidon Sets*,
[arXiv:2607.01169v2](https://arxiv.org/abs/2607.01169v2).  The external code is
[`sidon_certificate_8kernel.py`](https://github.com/HbZhao1/sidon-vector-smoothing/blob/ef044564300e546f8832b31f5fba133fd192cc3a/sidon_certificate_8kernel.py)
at commit `ef044564300e546f8832b31f5fba133fd192cc3a`, tree
`600e317e727e6a8940cc5f13c072aa1c6b766784`, with SHA-256
`957a5afadd849ac4f97c2b71252abb5c796c2db3c91a608ab35097e3c49292a8`.
The raw upstream file is external and is not bundled here; no explicit
repository license was found.  The optional replay requires precisely this Git
provenance and file hash.

Hou--Zhao v2 Section 5 only suggests that controlled cross terms may be
possible.  The matrix below, its search, and its verification are a
project-internal extension, not a construction or theorem attributed to the
authors.

## Exact perturbation

Keep the official `m=32`, `L=4`, eight kernels `p_r`, mixing vector `lambda`,
and boundary vectors `w_r`.  Put

\[
 q_{r,j}=\lambda_r w_{r,j},\qquad
 w_{r,j}=W_{r,j}/10^9+17/250000000000,
\]

and replace the diagonal energy matrix `D=diag(lambda)` by

\[
 H=D+\varepsilon J,\qquad \varepsilon=1/6250.
\]

The nonzero upper-triangular entries of the symmetric, zero-diagonal `J` are

\[
 J_{12}=-1,\ J_{14}=2,\ J_{17}=-1,\ J_{28}=1,\
 J_{45}=-1,\ J_{48}=-1,\ J_{57}=1.
\]

Equivalently, this is the sum of the two oriented alternating cycles
`(-12,+14,+28,-48)` and `(+14,-17,-45,+57)`.  Every row sum of `J` is zero.
Consequently `H 1=lambda`,

\[
 s=\mathbf 1^T H\mathbf 1=1,
 \qquad
 \beta=\lambda^T H^{-1}\lambda=1.
\]

The original covering inequalities depend only on `p` and
`q=lambda*w`, so they are unchanged.  The official minimum remains zero at
shift 128, and the least positive slack remains at shift 127 with exact value

\[
 \frac{4735171805469436153}
 {6250000000000000000000000000000}.
\]

## Positive definiteness and all-shift legality

Strict diagonal dominance gives a short exact PD proof.  The absolute
off-diagonal row sums of `J` are `(4,2,0,4,2,0,2,2)`.  Among affected rows the
smallest Gershgorin margin is

\[
 \lambda_8-2\varepsilon=\frac{6303669}{10^8}>0.
\]

The smallest margin overall is the untouched
`lambda_3=67671/50000000=135342/10^8>0`.  Since `H` is symmetric with positive
diagonal and is strictly diagonally dominant, `H` is positive definite.

For each `0<=d<=31`, the certificate evaluates exactly

\[
 D_d=\sum_{r,s}H_{rs}\sum_{i=0}^{31-d}p_r(i)p_s(i+d).
\]

All 32 values are positive.  The minimum is at `d=31`:

\[
 D_{31}=\frac{1819897465312660450421661319}
 {6250000000000000000000000000000}>0.
\]

This finite check lifts to every integer shift of the step kernels.  If
`d=q h+t`, `0<=t<h`, then

\[
 C_H(d)=\frac{(h-t)D_q+tD_{q+1}}{h^2},\qquad D_{32}=0.
\]

Thus every required combined cross-correlation is nonnegative.

## Boundary objective and coefficient

With the fixed `q` above, exact inversion of `H` gives

\[
 \Phi_H=\sum_j q_j^T H^{-1}q_j
 =\frac{1579624060150375763081182134406091935613108916851453560453448655773351}
 {12822999091195800386592256049305804181893750000000000000000000000000}.
\]

The two normalized factors are

\[
 a_H=\frac{497337598850312567313325417619}
 {390625000000000000000000000000},
\]

and, because `s=beta=1`,

\[
 b_H=1+\frac{\Phi_H-128}{16}
 =\frac{143448161936446119782849456883841867241008916851453560453448655773351}
 {205167985459132806185476096788892866910300000000000000000000000000000}.
\]

Their product is

\[
 a_Hb_H=
 \frac{71342164416962916721779776697373603740587064431196223748760854144493362660496722080976377486071269}
 {80143744319973752416201600308161276136835937500000000000000000000000000000000000000000000000000000}.
\]

Therefore the canonical exact coefficient is `sqrt(a_H*b_H)`, whose decimal
expansion begins

\[
 0.9434922260277724855696550445\ldots.
\]

The verifier also cross-multiplies the clean rational bound

\[
 a_Hb_H < (94349223/100000000)^2.
\]

Within this finite smoothing theorem, the resulting statement is therefore

\[
 F(N)\le \sqrt N+0.94349223\,N^{1/4}+O(1).
\]

This displayed finite bound is obtained by applying the project-internal
generalized master lemma proved in
[`ROUTE_C_BOUNDARY_NORMALIZED_CROSS_KERNEL.md`](ROUTE_C_BOUNDARY_NORMALIZED_CROSS_KERNEL.md),
not by applying Hou--Zhao's diagonal Lemma 2.1 directly.  This attribution is
essential: the signed off-diagonal extension is ours.

This strictly improves the official diagonal coefficient
`0.9434925907135450255...` and also the earlier one-cycle regression value
`0.9434925804448946831...`.  These are exact product comparisons, not a
floating-point decision.

## Search qualification

The candidate is the best bounded two-cycle combination found in this finite
search: all 210 alternating four-cycles in both orientations were enumerated,
then sums and differences among the best 80 downhill cycles were checked and
integer directions were gcd-reduced.  This does not exhaust arbitrary `J`,
arbitrary epsilon, reoptimized boundary vectors, or other kernel families, so
no global-optimality or novelty conclusion follows.

## Reproduction

Offline generation and validation use only the Python standard library and
`fractions.Fraction`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 hou_zhao_cross_perturbation_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 hou_zhao_cross_perturbation_certificate.py --self-check
PYTHONDONTWRITEBYTECODE=1 python3 hou_zhao_cross_perturbation_certificate.py \
  --verify hou_zhao_cross_perturbation_certificate.json
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_hou_zhao_cross_perturbation_certificate.py
```

When the pinned external checkout is available, replay the official verifier
and recompute every raw-data aggregate with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 hou_zhao_cross_perturbation_certificate.py \
  --verify hou_zhao_cross_perturbation_certificate.json \
  --upstream /path/to/sidon-vector-smoothing/sidon_certificate_8kernel.py
```

# Signed off-diagonal Route-C probe: the minimal two-point-mass no-go

Date: 2026-08-29  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Scope: exact finite theorem for one explicitly normalized joint-kernel class. **Questions 1 and 2 remain unresolved.**

## Result

For the two distinct probability kernels

\[
K_1=\delta_0,\qquad K_2=\delta_1
\]

and an arbitrary symmetric rational matrix

\[
H=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\]

positive semidefiniteness is encoded exactly by

\[
a\geq0,\qquad c\geq0,\qquad ac-b^2\geq0.
\]

The combined correlation has no hidden terms:

\[
C_H(0)=a+c,\qquad C_H(1)=C_H(-1)=b,
\qquad C_H(d)=0\quad(|d|\geq2).
\tag{1}
\]

For a Sidon set of cardinality `k`, the Route-C filled-shift expression from
equation (3) of `ROUTE_C_CROSS_KERNEL_GATE.md` is

\[
U_H(k)=\mathbf 1^T H\mathbf 1+(k-1)C_H(0)
      =k(a+c)+2b.
\tag{2}
\]

Holding the two diagonal coefficients fixed, the diagonal baseline is

\[
U_{\rm diag}(k)=k(a+c).
\]

Thus a strict signed gain in (2) requires `b<0`.  But the exact legal-shift
gate in (1) requires `b>=0`.  Therefore:

> **Two-point-mass no-go.** No symmetric rational PSD matrix in this class
> simultaneously passes `C_H(d)>=0` for every nonzero shift and strictly
> improves the filled-shift expression over its same-diagonal baseline.

The argument does not merely cover the enumerated grid: it holds for every
rational `a,b,c` satisfying the displayed PSD constraints.  Notice that PSD
itself plays a different role from shift positivity.  It permits negative
`b` whenever `b^2<=ac`; it does not repair the sign of `C_H(1)`.

## Exact smallest nondegenerate obstruction

To remove irrelevant scaling, the deterministic search sets `a=c=1` and
requires positive definiteness, so `-1<b<1`.  Reduced rationals are ordered by
denominator, then absolute numerator.  The first negative value is

\[
b=-\frac12,\qquad
H=\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix},
\qquad \det H=\frac34>0.
\]

For the two-mark Sidon set `A={0,2}`, the only represented positive difference
is `2`, so the set avoids the negative correlation shift `1`.  Literal
convolution and the correlation expansion independently give

\[
E_H(A)=4.
\]

The illicit PSD-only filled-shift expression gives

\[
U_H(2)=3,
\]

an exact violation of the would-be upper bound `E_H(A)<=U_H(2)`.  The
always-legal positive-part repair is

\[
U_H^+(k)=k(a+c)+2\max(b,0)\geq U_{\rm diag}(k).
\tag{3}
\]

For the fixture, (3) returns `4`: it erases the entire apparent signed gain.

This is minimal under the stated normalization:

- one kernel has no cross coefficient, so two kernels are necessary;
- two distinct integer point masses have support diameter at least one;
- a two-mark set is the smallest nontrivial Sidon set, and `{0,2}` is the
  least-diameter one avoiding shift `1`;
- no negative unit-diagonal positive-definite rational `b` has denominator
  one, while `-1/2` has denominator two.

If positive semidefinite but singular fixtures are admitted, `b=-1` is
arithmetically simpler, but the Gram matrix has rank one.  The certificate
uses the positive-definite fixture so that the obstruction is not a
rank-degeneracy artifact.

## Deterministic enumeration and replay

The exact enumeration checks every reduced `b=p/q` in `(-1,1)` with `q<=12`:

- positive-definite matrices checked: `91`;
- negative cross coefficients checked: `45`;
- matrices passing the nonnegative-shift gate with strict same-diagonal gain:
  `0`;
- first positive-definite obstruction: `b=-1/2`.

The finite enumeration only validates the implementation and the stated
minimal rational fixture.  The universal no-go follows from equations
(1)--(3), not from grid exhaustion.

The replay certificate is
`signed_offdiag_two_kernel_certificate.json`.  Its canonical payload hash is

`4c071ae8c5ec6408da75b71ea0e54c1c2fe7c3402c3241df00594af7c665363c`.

From `route_probes/`, reproduce with:

```bash
python -m unittest -v signed_offdiag_two_kernel_test.py
python signed_offdiag_two_kernel_probe.py --self-check \
  --verify signed_offdiag_two_kernel_certificate.json
```

## Claim boundary and surviving obligation

This is a scoped method closure, not a joint improvement and not a closure of
Route C as a whole.  It rules out using the smallest translated-delta cross
coefficient as a free negative correction to the filled-difference upper
bound.  It does **not** rule out wider kernels whose diagonal autocorrelations
can cover signed cross-correlations, an explicit boundary-cover constraint,
a common-shift covariance theorem, entropy/inverse mechanisms, or a theorem
forcing the actual difference set to pay negative shifts.

No finite-to-infinite inference is made.  P28, publication novelty, prize
claims, Question 1, and Question 2 all remain unresolved.

# Route C: exact feasibility of overlapping signed kernels

Date: 2026-08-29  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Evidence: exact finite pure-energy theorem and deterministic rational search  
Claim boundary: **no Hou--Zhao boundary-cover lower functional is fixed; Questions 1 and 2 remain unresolved.**

## 1. Exact criterion

Let `K_1,K_2` be finitely supported nonnegative probability kernels on the
integers.  Write

\[
R_{rs}(d)=\sum_x K_r(x)K_s(x+d)
\]

and, for positive shifts,

\[
A_d=R_{11}(d)+R_{22}(d),\qquad
B_d=R_{12}(d)+R_{21}(d).
\]

For

\[
H_b=\begin{pmatrix}1&b\\b&1\end{pmatrix},
\]

the combined correlation is exactly

\[
C_b(d)=A_d+bB_d.
\tag{1}
\]

The eigenvalues of `H_b` are `1+b` and `1-b`.  Thus

\[
H_b\succeq0\iff -1\leq b\leq1,
\qquad
H_b\succ0\iff -1<b<1.
\tag{2}
\]

Nonnegativity of the kernels gives `A_d,B_d>=0`.  Suppose first that at least
one positive shift has `B_d>0`, and define

\[
\rho=\min_{d\geq1:B_d>0}\frac{A_d}{B_d}.
\tag{3}
\]

For `b<0`, (1) proves the equivalence

\[
C_b(d)\geq0\text{ for every }d\ne0
\iff b\geq-\rho.
\tag{4}
\]

Together with (2), a negative PSD coefficient exists exactly when
`rho>0`.  There is also an exact endpoint classification.  Probability mass
and symmetry give

\[
 \sum_{d\ge1}(A_d-B_d)
 =-\frac12\|K_1-K_2\|_2^2\le0.
 \tag{5}
\]

Hence, when some positive `B_d` exists, `rho<=1`; equality forces
`K_1=K_2`, and distinct kernels have `rho<1`.  Thus for distinct kernels with
`rho>0`, the most negative feasible positive-definite coefficient is the
attained value `b=-rho`.  At the identical-kernel endpoint `rho=1`, `b=-1`
is feasible and PSD but singular; the PD feasible set has infimum `-1` and
no minimum there.

The case with no positive `B_d` must not be encoded by inventing `rho=0`.
If

\[
B_d=0\quad\text{for every }d\geq1,
\]

then `rho` is undefined and (1) reads `C_b(d)=A_d>=0`; every
`-1<=b<0` passes the shift gate, and every `-1<b<0` is positive definite.

## 2. Every feasible negative coefficient lowers the pure energy

Because both kernels have mass one,

\[
\sum_{d\in\mathbb Z}C_b(d)
=\boldsymbol1^T H_b\boldsymbol1=2+2b.
\tag{6}
\]

When the nonnegative-shift gate holds, the always-legal positive-part upper
expression simplifies to

\[
\begin{aligned}
U_b(k)
&=kC_b(0)+2\sum_{d\geq1}C_b(d)_+\\
&=2+2b+(k-1)C_b(0).
\end{aligned}
\tag{7}
\]

At shift zero put `B_0=2<K_1,K_2>`.  The same-kernel diagonal baseline is

\[
U_0(k)=2+(k-1)A_0.
\]

Since `C_b(0)=A_0+bB_0`, subtraction gives the exact identity

\[
\boxed{U_b(k)-U_0(k)=b\bigl(2+(k-1)B_0\bigr).}
\tag{8}
\]

The parenthesis is positive.  Consequently every feasible `b<0` strictly
lowers this pure upper-energy expression for every `k>=1`, in particular for
every requested `k>=2`.

This proves that overlap can escape the translated-point-mass sign
obstruction: diagonal autocorrelation at a shift can pay a negative cross
correlation at the same shift.

## 3. Minimal half-grid witness

Take

\[
K_1=(1,0)=\delta_0,
\qquad
K_2=(1/2,1/2),
\qquad
b=-1/2.
\]

Here

\[
A_1=1/4,\qquad B_1=1/2,\qquad\rho=1/2,
\]

so `C_b(1)=0`, while

\[
C_b(0)=1,\qquad \boldsymbol1^TH_b\boldsymbol1=1,
\qquad\det H_b=3/4>0.
\]

For every `k>=2`,

\[
U_b(k)=k,\qquad
U_0(k)=\frac{3k+1}{2},
\qquad
\frac{U_b(k)}{U_0(k)}=\frac{2k}{3k+1}.
\tag{9}
\]

At `k=2`, the exact ratio is `4/7`.

The exhaustive half-grid consists of the six probability triples with
coordinates in `(1/2)Z` on `{0,1,2}`.  Among their nine unordered distinct
overlapping pairs, eight admit a positive-definite negative coefficient and
a strict gain.  The best `k=2` ratio is `4/7`.  Denominator-one probability
kernels are point masses, and two distinct point masses do not overlap, so
the displayed witness is minimal by probability-weight denominator within
this grid model.

## 4. First full-support grid

Requiring every coordinate on `{0,1,2}` to be positive, denominator four is
the first grid containing distinct kernels.  A best pair is

\[
K_1=(1/4,1/4,1/2),\qquad
K_2=(1/4,1/2,1/4),\qquad
b=-7/8.
\]

Its exact shift table is

\[
C_b(0)=\frac{13}{64},\qquad
C_b(1)=0,\qquad
C_b(2)=\frac{3}{128}.
\]

The total mass is `1/4`.  For general `k`,

\[
U_b(k)=\frac{13k+3}{64},qquad
U_0(k)=\frac{3k+5}{4}.
\tag{10}
\]

At `k=2`,

\[
\frac{U_b(2)}{U_0(2)}=\frac{29}{176}.
\]

There are exactly three unordered pairs in the full-support denominator-four
grid; all three are feasible strict-gain hits, and `29/176` is the best
ratio, attained by the displayed pair and its reflection.

## 5. Rational family and the degenerating normalization

For any rational `0<t<1/2`, set

\[
K_1=(1/2-t,1/2+t),\qquad
K_2=(1/2,1/2),\qquad
b=-1+2t^2.
\tag{11}
\]

Then

\[
A_1=1/2-t^2,\qquad B_1=1/2,
\]

so `C_b(1)=0`; all larger positive shifts vanish.  Direct calculation gives

\[
C_b(0)=4t^2,qquad
\boldsymbol1^TH_b\boldsymbol1=4t^2,
\qquad
1+b=2t^2.
\tag{12}
\]

Thus `H_b` is positive definite, but its small eigenvalue tends to zero.
Moreover,

\[
U_b(k)=4kt^2,qquad
U_0(k)=k+1+2(k-1)t^2,
\]

and hence

\[
\frac{U_b(k)}{U_0(k)}
=\frac{4kt^2}{k+1+2(k-1)t^2}\longrightarrow0.
\tag{13}
\]

The exact replay point `t=1/6` has

\[
b=-17/18,\quad C_b(0)=1/9,\quad
\boldsymbol1^TH_b\boldsymbol1=1/9,\quad
1+b=1/18,\quad {U_b(2)\over U_0(2)}={4\over55}.
\]

Equation (13) has infimum zero over distinct rational kernels but no
nondegenerate minimizer.  The apparent gain is produced by simultaneous
collapse of total correlation mass, zero-shift mass, and the Gram eigenvalue.

## 6. Boundary-cover warning and claim boundary

This artifact fixes no Hou--Zhao boundary-cover lower functional.  Therefore
it does not compare the quantity which would appear on the lower side of a
joint Cauchy--Schwarz inequality.  The program deliberately rejects a
mutation that labels the pure-energy hit a useful Sidon inequality while the
boundary functional is absent.

A Route-C promotion would have to fix and preserve an exact joint covering or
lower-energy normalization while improving (7).  Unit diagonal alone is not
such a normalization: (12) shows that the relevant eigenvalue can collapse.

No compatible multiscale theorem, useful Sidon inequality, P28 conclusion,
Question 1 result, or Question 2 result follows.  Q1 and Q2 remain unresolved.

## 7. Replay

The exact certificate is `overlapping_kernel_certificate.json`.  Its
canonical payload SHA-256 is

`f3950cbcb199e2c31123fc7c7b5e650c937bd971afc0e156bbd77f5bc7ae7963`.

From `route_probes/` run:

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v test_overlapping_kernel_probe.py
PYTHONDONTWRITEBYTECODE=1 python overlapping_kernel_probe.py \
  --self-check --verify overlapping_kernel_certificate.json
```

The tests use `Fraction` throughout, require byte-exact deterministic JSON
replay, and reject three adversarial mutations: a failed correlation sign
gate, a non-PSD Gram parameter, and an unsupported boundary-benefit claim.

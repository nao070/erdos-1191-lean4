# Route C: exact positive-part completion and zero-mass contrast no-go

Date: 2026-08-29  
Global status: `UNRESOLVED_AT_HARD_LIMIT`  
Claim tier: finite exact theorem / scoped method closure.  Questions 1 and 2,
P28, publication novelty, and every prize claim remain unresolved.

## 1. Setup

Let `A` be a finite Sidon subset of `Z`.  Let
`K_1,...,K_R : Z -> R` be finitely supported, write

\[
 k(x)=(K_1(x),\ldots,K_R(x))^{\mathsf T},
 \qquad m=\sum_x k(x),
\]

and let `H` be a symmetric real `R`-by-`R` matrix.  Put

\[
 u_r=1_A*K_r,
 \qquad
 E_H(A)=\sum_{r,s}h_{rs}\langle u_r,u_s\rangle,
\]

\[
 C_H(d)=\sum_x k(x)^{\mathsf T}Hk(x+d).
\]

Symmetry of `H` gives `C_H(-d)=C_H(d)`.  If `Delta(A)` is the set of
represented positive differences, direct finite expansion gives

\[
 E_H(A)=|A|C_H(0)+2\sum_{d\in\Delta(A)}C_H(d).
 \tag{1}
\]

This is the same exact expansion as in
`ROUTE_C_CROSS_KERNEL_GATE.md`; no asymptotics or density hypothesis is used.

## 2. The exact positive-part completion cost

Write

\[
 P_H=\sum_{d\ge1}C_H(d)_+,
 \qquad
 N_H=\sum_{d\ge1}(-C_H(d))_+.
\]

Then the always-legal coefficientwise completion of (1) is

\[
 \boxed{E_H(A)\le |A|C_H(0)+2P_H.}
 \tag{2}
\]

More precisely, its slack is the exact nonnegative quantity

\[
\begin{aligned}
 |A|C_H(0)+2P_H-E_H(A)
 ={}&2\sum_{\substack{d\ge1\\d\notin\Delta(A)}}C_H(d)_+\\
 &+2\sum_{d\in\Delta(A)}(-C_H(d))_+.
\end{aligned}
\tag{3}
\]

Represented negative shifts increase the second term in (3).  Negative
shifts that may be unrepresented are instead the reason that the global
`2N_H` correction in (5) cannot be omitted without a theorem about the
actual difference set.

The full correlation mass is

\[
 \sum_{d\in\mathbb Z}C_H(d)=m^{\mathsf T}Hm
 =C_H(0)+2(P_H-N_H).
 \tag{4}
\]

Consequently (2) has the equivalent form

\[
 \boxed{E_H(A)\le
 m^{\mathsf T}Hm+(|A|-1)C_H(0)+2N_H.}
 \tag{5}
\]

Equation (5) identifies the exact price omitted by a PSD-only or
fill-all-shifts shortcut: twice the total negative off-shift correlation.
It is the exact **independent-coordinate positive-part completion** obtained
by relaxing each indicator `1_(d in Delta(A))` separately.  It does not even
retain the cardinality constraint `|Delta(A)|=binom(|A|,2)`: sorting the
positive values and keeping only the largest `binom(|A|,2)` already gives a
potentially stronger relaxation.  No global optimality over Sidon difference
sets is claimed.

## 3. The cost-free gate forces zero-mass PSD contrasts to be energy-trivial

Now assume `H` is positive semidefinite.  Choose a real Gram factor
`H=B^T B` and define signed effective kernels

\[
 L_\ell(x)=\sum_r B_{\ell r}K_r(x).
\]

Then

\[
 C_H(d)=\sum_\ell\sum_xL_\ell(x)L_\ell(x+d),
 \qquad
 E_H(A)=\sum_\ell\|1_A*L_\ell\|_2^2.
 \tag{6}
\]

Suppose the original kernels are probability kernels, so `m=1`, and

\[
 H\mathbf1=0.
 \tag{7}
\]

This is the natural matrix encoding of a contrast between scale channels.
Equations (4) and (7) give

\[
 0=\mathbf1^{\mathsf T}H\mathbf1
   =C_H(0)+2\sum_{d\ge1}C_H(d).
 \tag{8}
\]

If the cost-free Route-C gate `C_H(d)>=0` holds at every nonzero shift, then
every summand in (8) is nonnegative.  Hence `C_H(0)=0`; by PSD,

\[
 0=C_H(0)=\sum_x\|B k(x)\|_2^2
\]

forces `Bk(x)=0` for every `x`.  Therefore every effective kernel in (6),
the entire correlation sequence, and `E_H(A)` for every finite `A` are zero.
If the vectors `k(x)` span `R^R`, then `H=0`.

This proves the scoped no-go:

> **Zero-mass contrast no-go.** Any zero-mass PSD contrast of probability
> kernel channels that passes the nonnegative common-shift gate is
> energy-trivial: every effective Gram kernel vanishes.  A contrast with
> `C_H(0)>0` must have a negative off-shift, and hence needs an explicit
> payment in (5) or a theorem about the actual difference set.

Even without the nonnegative-shift gate, (8) gives the quantitative identity

\[
 2N_H=C_H(0)+2P_H\ge C_H(0).
 \tag{9}
\]

Thus the negative-correlation payment is at least the zero-shift energy of a
zero-mass contrast with nonzero effective energy.  Here “nonzero effective
energy” means `C_H(0)>0`, equivalently `Bk(x) != 0` for at least one `x`; it
does not merely mean `H != 0`.  A reverse-martingale or adjacent-scale
squared difference does not evade this algebra merely by being PSD.

The same proof works for arbitrary kernel masses whenever
`m^T H m=0` (equivalently `Hm=0` under PSD); probability normalization is
only the most relevant Route-C form.

## 4. All distinct point-mass channels reduce to the diagonal baseline

Let `K_r=delta_(t_r)` at distinct integer locations.  Then

\[
 C_H(0)=\operatorname{tr}H.
\]

Regardless of collisions among the nonzero differences `t_s-t_r`, (2)
becomes

\[
 E_H(A)\le |A|\operatorname{tr}H+2P_H
 \ge |A|\operatorname{tr}H.
 \tag{10}
\]

For `H` PSD, the same-diagonal matrix `diag(H)` is PSD and its legal Sidon
upper expression is exactly `|A| tr(H)`.  Therefore no off-diagonal coupling
of finitely many distinct point-mass channels improves the coefficientwise
positive-part upper bound over its same-diagonal baseline.  At each lag the
matrix entries are first aggregated into `C_H(d)`; negative aggregate lag
sums are truncated at zero, while positive aggregate lag sums increase the
bound.

The companion exact memo `SIGNED_OFFDIAG_TWO_KERNEL_NO_GO.md` and its JSON
certificate give the minimal nondegenerate fixture:

\[
 K_1=\delta_0,\quad K_2=\delta_1,\quad
 H=\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix},\quad A=\{0,2\}.
\]

Here the actual energy is `4`, the illicit PSD-only expression is `3`, and
the legal positive-part expression returns `4`.

## 5. Exact verification and surviving route

`cross_kernel_positive_part_certificate.py` and
`test_cross_kernel_positive_part_certificate.py` independently check (1)--(5)
on exact rational wider-kernel fixtures, the Gram factorization (6), the
zero-mass identity (9), the all-point-mass corollary (10), degenerate empty-set
and zero-kernel cases, mutation rejection, semantic replay, canonical payload
hashes, and byte-exact rendering.

This closes, at G2, two named finite-dimensional shortcuts:

1. negative common-shift correlation treated as a free improvement; and
2. a PSD zero-mass scale contrast with nonzero effective energy combined with
   cost-free filling of every unrepresented shift.

It does **not** close wider overlapping kernels with nonzero mass, a proof
forcing the actual difference set to pay selected negative shifts, a boundary
cover that carries information outside the aggregate correlation, an entropy
chain-rule deficit, a compatible-chain inverse theorem, or the P3--P5 signed
quartic budget.  No finite-to-infinite inference is made.

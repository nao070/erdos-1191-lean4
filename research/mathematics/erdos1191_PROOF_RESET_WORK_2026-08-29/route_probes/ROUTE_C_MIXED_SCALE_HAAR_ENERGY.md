# Route C: mixed-scale Haar energy and the physical cell-dual floor

**Status:** exact mixed-scale physical formula and arbitrary-finite-scale
cell-length-dual no-go; cross-scale surplus amortization and every paid
continuum-phase ledger remain open.

This note asks whether off-diagonal blocks between distinct Haar widths can
evade the physical lower bound exposed by the direct-`B` same-scale LP.  They
cannot.  Cross-scale blocks may still lower the sum of separately optimized
pointwise-cover prices, but a block that is nonnegative relative to the
signed target on every actual common cell has physical price at least the
integrated signed demand.  This conclusion needs neither coefficient-matrix
positive semidefiniteness nor a root-SDDM restriction.

The result is a sharp route boundary, not a paid Route-C ledger.  It does not
close C058, Question 1, or Question 2.

## 1. Exact oriented mixed-scale inner product

For `T,S>0`, put

\[
 g_T=\mathbf 1_{[0,T)}-\mathbf 1_{[T,2T)},
 \qquad
 \tau_dg_S(x)=g_S(x-d).
\]

The orientation of `d` matters when `T` and `S` differ.  Define the exact
box-overlap length

\[
 H_{T,S}(d)
 :=|[0,T)\cap[d,d+S)|.
\]

With `u_+=max(u,0)`, inclusion-exclusion gives

\[
 \boxed{
 H_{T,S}(d)
 =(T-d)_+-(T-d-S)_+-(-d)_++(-d-S)_+.}
 \tag{1}
\]

Expanding the four signed half-box intersections gives

\[
 \boxed{
 A_{T,S}(d):=\langle g_T,\tau_dg_S\rangle
 =H_{T,S}(d)-H_{T,S}(d+S)
  -H_{T,S}(d-T)+H_{T,S}(d+S-T).}
 \tag{2}
\]

This is an exact continuous piecewise-linear formula for arbitrary real
`T,S>0` and real `d`.  The possible knots, before coincidences are removed,
are

\[
 -2S,-S,0,T-2S,T-S,T,2T-2S,2T-S,2T,
 \tag{3}
\]

and `A_(T,S)(d)=0` outside `[-2S,2T]`.  Direct changes of variables give

\[
 A_{T,S}(d)=A_{S,T}(-d),
 \qquad
 A_{\lambda T,\lambda S}(\lambda d)=\lambda A_{T,S}(d).
 \tag{4}
\]

For equal scales, (2) reduces to the earlier three-piece tent:

\[
 A_{T,T}(d)=
 \begin{cases}
  2T-3|d|,&|d|\le T,\\
  |d|-2T,&T\le |d|\le2T,\\
  0,&|d|\ge2T.
 \end{cases}
 \tag{5}
\]

Half-open endpoints do not alter the integral, but they do determine the
literal state on every atomic cell and therefore matter for the pointwise
cover test below.

## 2. Exact physical energy

For arbitrary scalars `alpha,beta`, expansion of the square yields

\[
 \boxed{
 \int_{\mathbb R}
 (\alpha g_T(x)+\beta g_S(x-d))^2\,dx
 =2T\alpha^2+2S\beta^2+2\alpha\beta A_{T,S}(d).}
 \tag{6}
\]

Thus the normalized channels

\[
 \phi_{T,a}(x)={g_T(x-a)\over\sqrt{2T}}
\]

have mixed Gram entry

\[
 \langle\phi_{T,a},\phi_{S,b}\rangle
 ={A_{T,S}(b-a)\over2\sqrt{TS}},
 \tag{7}
\]

and the normalized mixed root costs

\[
 \boxed{
 \|\phi_{T,a}-\phi_{S,b}\|_2^2
 =2-{A_{T,S}(b-a)\over\sqrt{TS}}.}
 \tag{8}
\]

At `S=T`, (8) is exactly the physical root cost `chi_T(|b-a|)` from the
same-scale certificate.

For dyadic rational widths the raw quantity (2) is rational.  Normalized
mixed entries can lie in a quadratic field when the scale exponents have
opposite parity.  A rational exact implementation can retain the raw `g_T`
coordinates and place the factors `1/(2T)` in the coefficient matrix; it
must not silently replace (7) by a same-scale trace cost.

More generally, for finitely many translated mixed-scale channels

\[
 f_\alpha(x)=g_{T_\alpha}(x-a_\alpha),
\]

and a symmetric coefficient matrix `C`, the exact physical price is

\[
 \boxed{
 \mathcal E(C)
 =\int f(x)^TCf(x)\,dx
 =\sum_{\alpha,\beta}C_{\alpha\beta}
 A_{T_\alpha,T_\beta}(a_\beta-a_\alpha).}
 \tag{9}
\]

Equation (9), not the sum of diagonal traces, is the mixed-scale objective.

## 3. Arbitrary-finite-scale cell-length-dual no-go

Take any finite collection of scales, endpoints, and translated Haar
channels.  The union of all

\[
 a_p,\qquad a_p+T,\qquad a_p+2T
\]

partitions the real line into finitely many positive-length half-open cells,
plus two zero-state exterior cells.  Every channel vector is constant on each
finite cell.

Let `D_c` be any signed target density on cell `c`, including a sum of
same-scale embedded direct-`B` rows.  Let `P_c` be the density produced by an
arbitrary mixed-scale correction, including arbitrary cross blocks.  Assume
only the actual-cell inequalities

\[
 P_c\ge D_c\qquad\hbox{for every positive-length cell }c.
 \tag{10}
\]

Then the exact physical prices satisfy

\[
 \boxed{
 \mathcal E-\mathcal D
 =\sum_c |c|(P_c-D_c)\ge0.}
 \tag{11}
\]

Equality holds exactly when every positive-length cell has zero slack.

This is the mixed-scale extension of the canonical cell-length dual.  The
dual multiplier of cell `c` is its physical length, with whatever fixed
normalizing factors have already been placed in the channel coordinates.
Every within-scale and cross-scale cost column is saturated because its
objective coefficient is defined by integration over the same cells.

### Theorem 3.1

No finite mixed-scale cross block that satisfies the actual-cell cover (10)
can have physical price below the integrated same-scale signed demand.

This remains true if the coefficient matrix is indefinite; coefficient PSD
is unnecessary.  It also remains true for every finite number of scales.
What cross blocks can still do is reduce the positive surplus of separate
pointwise covers:

\[
 \mathcal E_{\rm mixed}^*
 <\sum_r\mathcal E_{r,\rm separate}^*
\]

is compatible with (11), provided

\[
 \mathcal E_{\rm mixed}^*\ge\mathcal D.
\]

Thus the theorem closes only the proposed below-demand escape, not
cross-scale amortization of cover surplus.

## 4. Exact two-scale cross-block fixture

Use

\[
 T=2,\qquad S=4,\qquad d=-1.
\]

The channels are `z=(g_2(x),g_4(x+1))`.  Their complete nonzero cell list is

\[
\begin{array}{c|c|c}
 c&|c|&z_c\\ \hline
[-1,0)&1&(0,1)\\
[0,2)&2&(1,1)\\
[2,3)&1&(-1,1)\\
[3,4)&1&(-1,-1)\\
[4,7)&3&(0,-1).
\end{array}
\tag{12}
\]

Equation (2) gives

\[
 A_{2,4}(-1)=2.
\]

Take the normalized same-scale target matrix

\[
 Q_0=\begin{pmatrix}1/4&0\\0&1/8\end{pmatrix}.
\]

Its physical demand is exactly `2`.  Adding only the tempting negative cross
coefficient `b=-1/16` produces

\[
 Q_{\rm low}=Q_0+
 \begin{pmatrix}0&-1/16\\-1/16&0\end{pmatrix}.
\]

The full matrix `Q_low` is positive definite, and its integrated physical
price is

\[
 2+2(-1/16)A_{2,4}(-1)=\frac74<2.
\]

Nevertheless, on each same-sign cell `[0,2)` and `[3,4)`, its cover slack is

\[
 2b=-\frac18.
\]

Thus coefficient PSD plus a favorable integrated cross correlation does not
authorize the actual-cell cover.

Adding first-scale diagonal `a=1/8` makes the added block

\[
 R=\begin{pmatrix}1/8&-1/16\\-1/16&0\end{pmatrix}
\]

nonnegative on every actual state in (12).  Its only positive slack is
`1/4` on `[2,3)`, so the physical price becomes

\[
 \frac94=2+\frac14.
\]

The exact two-variable geometry is also transparent.  For an arbitrary
added block

\[
 R=\begin{pmatrix}a&b\\b&c\end{pmatrix},
\]

the states (12) impose

\[
 c\ge0,qquad a+c\ge2|b|.
\tag{13}
\]

Its physical excess is

\[
 4a+4b+8c.
\tag{14}
\]

If `b>=0`, (13) makes (14) at least `12b+4c`; if `b<=0`, it is at least
`-4b+4c`.  Hence it is nonnegative, with equality only at `a=b=c=0`.
This is a sharp analytic no-go on the actual cell cone.  The certificate also
exhausts all `729` triples `a,b,c in {-4,...,4}/16`: `129` are cell-feasible,
none has negative excess, the unique zero is the zero added block, and the
least feasible excess with nonzero `b` is `1/4`.

## 5. Consequences for the continuum-phase Route-C target

For `T_r=2^(r+theta)`, the hinge formula (2) remains exact for every real
phase `theta`.  The rational certificate audits dyadic rational widths and
rational shifts; it does not replace the phase continuum by a finite grid.
The phase dependence changes whenever shifted endpoints cross one of the
knots (3), so a legal continuation must use analytic chamber integration or
a measurable adaptive rule.

The terminal-free direct-`B` identity represents `W_n/log(2)`.  Therefore a
ledger using `W_n` with unit coefficient must multiply the phase-integrated
physical price by `log(2)`.  Dropping that factor would create a false
apparent saving.

Theorem 3.1 means that a mixed-scale block cannot finance itself below the
canonical direct-`B`/Gothic demand.  A surviving next theorem must instead
show a uniform upper bound on

\[
 \mathcal E_{\rm mixed}^*-\mathcal D,
\]

or a strict saving relative to the sum of separate cover optima, and then
charge that remaining physical excess once to a named disjoint source.
The identity `2M=lambda` still rewrites the already-owned Gothic rows; it
does not create a second payment source.

Nothing here supplies:

- a continuum-phase upper bound on mixed-cover excess;
- a cross-scale recurrence valid on one compatible history;
- birth, past-scale, active-gate, scale-terminal, final-row, or
  shared-endpoint ownership;
- a singly owned Gothic, centered-carrier, signed-boundary, or external
  payment;
- C058, Question 1, Question 2, publication novelty, or prize eligibility.

## 6. Exact replay

The exact bundle is

- `ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate.py`;
- `ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate.json`;
- `ROUTE_C_MIXED_SCALE_HAAR_ENERGY_test.py`.

Replay with

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate.py \
  --verify ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate.json --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  ROUTE_C_MIXED_SCALE_HAAR_ENERGY_test.py
```

The payload SHA-256 is recorded inside the deterministic JSON.  The verifier
checks semantic equality, literal bytes, and eight formula/dual/scope/hash
mutations.

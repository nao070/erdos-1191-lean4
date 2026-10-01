# Route C: physical-cover transfer and the shared-endpoint membership threshold

**Status:** exact interface-state theorem; exact finite pass at `T=200` and
smallest membership-threshold failure at `T=250`; no common-history payment
theorem.

This note tests a precise version of the consecutive-epoch transfer idea.
The direct matrices are retained, the two epochs share one physical endpoint,
and one predecessor-side root is allowed to carry demand across that
interface.  The calculation has a sharp answer: the transfer is exact when
the successor positive run has length two, but it fails first at length
three.  The existing 16-mark Golomb fixture realizes both rows at two nearby
widths.

The result is deliberately narrow.  It rules out an endpoint-only physical
telescope and the stated fixed one-sided root recurrence.  It does not rule
out membership-adaptive weights, wider root supports, signed cross-scale
blocks, or a different finite-horizon payment master.

## 1. Consecutive blocks and the transfer ansatz

Let the first epoch have size `n>=4`.  In union coordinates its physical
block is

\[
 S_n=\{0,1,\ldots,n\},
\]

and the next epoch has size `2n` and block

\[
 S_{2n}=\{n,n+1,\ldots,3n\}.
\]

The unique shared coordinate is `n`.  Write `M_n=D_n^T B_nD_n` and embed
`M_n` and `M_(2n)` on these two supports.  As in the earlier direct-`B`
bundle,

\[
 B_{ij}=0\quad(|i-j|\le1),\qquad
 B_{ij}=-\frac{(j-i)^2}{8n^2}\quad(|i-j|\ge2).
\tag{1.1}
\]

Consider the following four canonical boundary roots:

\[
\begin{aligned}
 r_{\rm first}&=e_0-e_2,
 &w_{\rm first}&=\frac1{2n^2},\\
 r_-&=e_{n-2}-e_n,
 &w_-&=\frac1{2n^2},\\
 r_+&=e_n-e_{n+2},
 &w_+&=\frac1{8n^2},\\
 r_{\rm last}&=e_{3n-2}-e_{3n},
 &w_{\rm last}&=\frac1{8n^2}.
\end{aligned}
\tag{1.2}
\]

The strict endpoint-only ansatz retains only `r_first,r_last`.  The
one-sided transfer ansatz also retains the predecessor root `r_-`; it omits
the successor root `r_+`.  The standard two-sided comparison retains all
four roots.  Every coefficient in (1.2) is nonnegative, so these corrections
are graph Laplacians and have no hidden signed-root cancellation.

## 2. Exact interface-state theorem

For

\[
 2\le m\le2n-3,
\]

define the global Haar state `v^(m)` by

\[
 v_{n-1}=v_n=-1,
 \qquad
 v_{n+1}=\cdots=v_{n+m}=1,
\tag{2.1}
\]

with every other coordinate zero.  This is a legal Haar pattern: one
negative interval is immediately followed by one positive interval.

### Theorem 2.1

On the state (2.1),

\[
 \boxed{
 (v^{(m)})^TM_nv^{(m)}=0,
 \qquad
 (v^{(m)})^TM_{2n}v^{(m)}=\frac{m^2}{8n^2}.}
\tag{2.2}
\]

The first and last outer roots vanish, while

\[
 w_-(r_-^Tv^{(m)})^2
 =w_+(r_+^Tv^{(m)})^2
 =\frac1{2n^2}.
\tag{2.3}
\]

Consequently the exact one-sided and standard two-sided slacks are

\[
 \boxed{
 \sigma_-(m)=\frac{4-m^2}{8n^2},
 \qquad
 \sigma_{\pm}(m)=\frac{8-m^2}{8n^2}.}
\tag{2.4}
\]

Thus the one-sided predecessor transfer accepts `m=2` exactly and first
fails at `m=3`.  Even the two standard boundary weights fail at `m=3`.

### Proof

On `S_n`, the two negative entries form a signed interval touching the right
endpoint.  Its `M_n` energy is zero by the interval-state identity.

On `S_(2n)`, use local coordinates beginning at the shared endpoint.  The
state is

\[
 (-1,\underbrace{1,\ldots,1}_{m},0,\ldots,0).
\]

Its difference vector has only two nonzero entries:

\[
 Dv=-2e_0+e_m.
\]

Because `m>=2`, (1.1) for the size-`2n` block gives

\[
 B^{(2n)}_{0m}=-\frac{m^2}{8(2n)^2}
              =-\frac{m^2}{32n^2}.
\]

Hence

\[
 (Dv)^TB^{(2n)}Dv
 =2(-2)(1)B^{(2n)}_{0m}
 =\frac{m^2}{8n^2},
\]

proving (2.2).  The four root differences in (1.2), in the same order, have
squares `0,1,4,0`.  Multiplication by their coefficients proves (2.3) and
(2.4).  The certificate checks all 208 rows with `4<=n<=16` and
`2<=m<=2n-3` exactly.

For later use, after the one-sided root the highlighted row alone forces an
additional successor-root coefficient

\[
 w_+^{\rm extra}\ge
 \frac{m^2-4}{32n^2}.
\tag{2.5}
\]

At `n=4,m=3`, this is `5/512`.

## 3. The smallest canonical two-epoch fixture

Use the already audited Golomb ruler

\[
 a_k=k(k+100),\qquad0\le k\le15.
\tag{3.1}
\]

All 120 positive differences are distinct.  The two consecutive Wave blocks
are

\[
 \{a_3,\ldots,a_7\},\qquad
 \{a_7,\ldots,a_{15}\},
\]

so this is the first canonical `n=4,8` tower and their shared mark is
`a_7=749`.  Deduplication gives the 13 points

\[
 (309,416,525,636,749,864,981,1100,1221,
  1344,1469,1596,1725).
\tag{3.2}
\]

The exact enumerator retains all 40 real-line cells, including both zero
exteriors.

## 4. `T=200`: boundary-only failure and exact one-sided pass

At `T=200`, the actual cell

\[
 [981,1036)
\]

has state

\[
 v=(0,0,0,-1,-1,1,1,0,0,0,0,0,0)=v^{(2)}.
\tag{4.1}
\]

The first epoch contributes zero and the second contributes `1/32`.  Both
outer boundary roots vanish on this cell.  Therefore

\[
 \boxed{
 v^TC_{\rm boundary}v-v^T(M_4+M_8)v=-\frac1{32}.}
\tag{4.2}
\]

This already rules out the literal proposal that every internal correction
telescopes away and only first/last root potentials remain.

Adding the predecessor interface root `(2,4)` with weight `1/32` makes (4.1)
tight.  More strongly, exact enumeration gives

\[
 C_{\leftarrow}
 =\frac1{32}r_{02}r_{02}^T
  +\frac1{32}r_{24}r_{24}^T
  +\frac1{128}r_{10,12}r_{10,12}^T
\tag{4.3}
\]

and

\[
 v_c^T\bigl(C_{\leftarrow}-M_4-M_8\bigr)v_c\ge0
\]

on all 40 actual cells.  Its exact physical price is

\[
 \mathcal E_{200}(C_{\leftarrow})=\frac{81}{400}.
\tag{4.4}
\]

This is a genuine finite pass for the one-sided idea, not a theorem over
other widths or histories.

## 5. `T=250`: the first membership-threshold failure

Keep the same fixed Golomb tower and the same root weights, changing only the
width to `T=250`.  The actual cell

\[
 \boxed{[1100,1114)}
\]

has length `14` and state

\[
 v=(0,0,0,-1,-1,1,1,1,0,0,0,0,0)=v^{(3)}.
\tag{5.1}
\]

The exact row is

\[
 v^T(M_4+M_8)v=\frac9{128},
 \qquad
 v^TC_{\leftarrow}v=\frac1{32},
\]

and therefore

\[
 \boxed{\operatorname{slack}=-\frac5{128}.}
\tag{5.2}
\]

Adding the standard successor root `(4,6)` with weight `1/128` raises the
correction only to `1/16`, leaving slack `-1/128`.  The rowwise minimum extra
successor coefficient from (2.5) is `5/512`.  Its displacement is

\[
 a_9-a_7=232,
\]

so

\[
 \chi_{250}(232)=\frac{348}{125}
\]

and the physical price of this rowwise add-on is

\[
 \frac5{512}\frac{348}{125}=\frac{87}{3200}.
\tag{5.3}
\]

Equation (5.3) repairs only the highlighted row.  The complete `T=250`
one-sided correction has six negative actual cells, so no whole-fixture
feasibility claim is inferred from it.

## 6. Why the physical price cannot telescope for free

For every finite atomic cell set, the canonical dual weights are

\[
 \bar y_c=\frac{|c|}{2T}
\tag{6.1}
\]

on finite cells and zero on the two exteriors.  For every root
`r_ij=e_i-e_j`, they satisfy the column identity

\[
 \sum_c\bar y_c(r_{ij}^Tv_c)^2
 =\chi_T(|b_i-b_j|).
\tag{6.2}
\]

Thus a nonnegative root correction has the exact physical price

\[
 \boxed{
 \mathcal E_T\!\left(\sum_{i<j}w_{ij}r_{ij}r_{ij}^T\right)
 =\sum_{i<j}w_{ij}\chi_T(|b_i-b_j|).}
\tag{6.3}
\]

For distinct marks, `chi_T(d)>0`.  Hence nonnegative internal root weights
can be relocated, reduced, or removed, but they cannot cancel from the
physical objective as a signed telescoping potential.  A claimed price with
only first/last boundary terms forces every unpriced internal nonnegative
root weight to vanish.

In the finite pass above, the predecessor interface root has distance `224`,

\[
 \chi_{200}(224)=\frac{72}{25},
 \qquad
 \frac1{32}\chi_{200}(224)=\frac9{100}.
\tag{6.4}
\]

This is a real positive physical charge.  The boundary-only correction at
`T=200` is instructive: its total physical price is `9/80`, already larger
than the canonical signed demand `1429/12800` by `11/12800`, yet (4.2) shows
that it is infeasible.  A favorable scalar total is not a substitute for
the actual-cell inequalities.

The certificate checks (6.2) on all 78 roots at both `T=200` and `T=250`.
At `T=250`, the infeasible one-sided correction costs `753/4000`, again more
than the total signed demand `2347/16000`.  This is a second exact warning
that canonical-dual comparison alone does not create a transfer theorem.

## 7. Ownership and the Gothic ledger

For each epoch, the direct matrix satisfies the literal mixed-difference
identity

\[
 \boxed{2M_{p-n,q-n+1}=\lambda_{p,q}.}
\tag{7.1}
\]

The certificate rechecks all 46 rows for `n=4,8`.  Consecutive direct-pair
supports are disjoint and the matrices have zero diagonal; the two blocks
share only the point `749`.

Equation (7.1) is ownership, not extra capacity.  Every direct-`M` row used
here is the same Gothic row and must replace it one-for-one.  If an ambient
identity displays that cancellation, only a proved cover excess may be sent
to another owner.  Without the displayed cancellation, the entire physical
correction price needs a disjoint owner.  This probe creates neither a
shared-endpoint diagonal budget nor an external payment reserve.

## 8. Precise surviving finite LP

The counterexample leaves a falsifiable scale-adaptive problem.  At each
fixed tower and scale, choose nonnegative interface weights `w_-,w_+` (or
wider-root weights) **once**, before imposing all complete-cell constraints.
The weights may depend on the scale and on the finite tower, but not on the
cell variable `x`.  Every membership count realized by (2.1) then contributes
the necessary LP row

\[
 \boxed{w_-+4w_+\ge\frac{m^2}{8n^2}.}
\tag{8.1}
\]

Its physical objective contains

\[
 w_-\chi_T(a_{2n-1}-a_{2n-3})
 +w_+\chi_T(a_{2n+1}-a_{2n-1}),
\tag{8.2}
\]

with no cancellation between the two nonnegative columns.  A genuine
finite-horizon transfer certificate must then show, on one fixed compatible
tower and over the full phase continuum, that the paid cover excess is an
internal coboundary plus explicitly owned first/last terminals.  Every
birth, past-scale, active-gate, scale-terminal, final, and shared-endpoint row
must remain visible.

This note does not supply that payment identity.  It excludes only:

1. a literal endpoint-only root telescope;
2. the fixed one-sided predecessor weights (1.2) as a scale-adaptive rule;
3. the standard two-sided boundary weights on the `m=3` row.

It does not close C058, Question 1, Question 2, Erdős Problem #1191,
publication novelty, or prize eligibility.

## 9. Exact replay

The bundle is

- `ROUTE_C_PHYSICAL_COVER_TRANSFER_certificate.py`;
- `ROUTE_C_PHYSICAL_COVER_TRANSFER_certificate.json`;
- `ROUTE_C_PHYSICAL_COVER_TRANSFER_test.py`.

It uses rational arithmetic only.  The generator verifies the 208 general
interface rows, 46 ownership rows, 156 canonical root-cost columns, both
complete 40-cell fixtures, exact physical prices, raw canonical JSON bytes,
and twelve semantic/hash mutations.

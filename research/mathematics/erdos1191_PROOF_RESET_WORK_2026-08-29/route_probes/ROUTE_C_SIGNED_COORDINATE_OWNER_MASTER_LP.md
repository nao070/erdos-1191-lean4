# Signed coordinate-owner graph/PSD master on the fixed Golomb tower

Status: exact finite-fixture theorem and exact replay only.  C058, Questions 1
and 2, arbitrary ownership rules, indefinite blocks, and publication or prize
claims remain open.

## 1. Fixed geometry and normalization

Use

\[
 a_k=k(k+100),\qquad 0\le k\le15,
\]

the two direct-M epochs

\[
 A_4=\{a_3,\ldots,a_7\},\qquad
 A_8=\{a_7,\ldots,a_{15}\},
\]

and the complete finite dyadic widths

\[
 \mathcal T=\{100,200,400,800\},\qquad T_{\rm terminal}=1600.
\]

For every `k=3,...,15` and `T` in this set, put

\[
 g_{k,T}=1_{[a_k,a_k+T)}-1_{[a_k+T,a_k+2T)},\qquad
 h_{k,T}=\frac{g_{k,T}}{2T},\qquad q_{k,T}=1600h_{k,T}.
\]

There are exactly 52 physical coordinates.  The endpoints
`a_k`, `a_k+T`, and `a_k+2T` give 77 distinct finite events and 76
positive-length common cells.  Thus eight owner rows, `(n,T)` with
`n=4,8`, give 608 cell inequalities.  There are
`binom(52,2)=1326` physical graph roots.

The shared point `a_7` is a single coordinate at each width.  It belongs to
the earlier `n=4` coordinate group.  The `n=8` coordinate group begins at
`a_8`, although the `n=8` direct-M demand still uses the complete block
`a_7,...,a_15`.  Consequently the eight coordinate groups partition all 52
coordinates exactly once.

Let `M_n=D^T B_n D` be the direct point matrix.  On a cell `c`, the signed
owner demand is

\[
 d_{n,T,c}=2T\,h_{A_n,T}(c)^T M_n h_{A_n,T}(c).
 \tag{1.1}
\]

The eight integrated values are

| owner | integrated demand |
|---|---:|
| `n4,T100` | `-9/160` |
| `n4,T200` | `63/640` |
| `n4,T400` | `9/320` |
| `n4,T800` | `0` |
| `n8,T100` | `-117/3200` |
| `n8,T200` | `169/12800` |
| `n8,T400` | `4331/51200` |
| `n8,T800` | `361/5120` |

Their sum is

\[
 D=\frac{2069}{10240}.
 \tag{1.2}
\]

The negative `T=100` rows are retained; pooling them away would change the
problem.

## 2. Canonical signed coordinate ownership

For a physical root `e_(i,j)=e_i-e_j`, let

\[
 R_{c,ij}=(h_i(c)-h_j(c))^2,
\]

and for owner coordinate group `G_o` let

\[
 A_{o,c,ij}=\sum_{r\in G_o}h_r(c)
 [e_{ij}e_{ij}^{\mathsf T}h(c)]_r.
 \tag{2.1}
\]

These shares may be negative.  Because the groups partition the coordinates,

\[
 \sum_o A_{o,c,ij}=R_{c,ij}
 \tag{2.2}
\]

pointwise.  The replay checks all `1326*76=100776` identities.  A root
coefficient is one cell-independent physical variable; cellwise owner
reassignment is forbidden.

Its exact physical price is

\[
 p_{ij}=\sum_c |c|R_{c,ij}.
 \tag{2.3}
\]

## 3. Exact graph-root LP results

The graph-root master is

\[
 \min_{w\ge0}\sum_{i<j}p_{ij}w_{ij},\qquad
 \sum_{i<j}A_{o,c,ij}w_{ij}\ge d_{o,c}
 \quad(608\text{ rows}).
 \tag{3.1}
\]

An exact feasible solution with 20 positive roots has price

\[
 U_{\rm graph}=\frac{99062067}{179732480}.
 \tag{3.2}
\]

Six positive roots cross the epoch partition.  An exact dual for the
restriction forbidding all epoch-crossing roots gives

\[
 L_{\rm no\ cross}=\frac{611554977}{1024000000},
\]

and therefore

\[
 L_{\rm no\ cross}-U_{\rm graph}
 =\frac{51737891019}{1123328000000}>0.
 \tag{3.3}
\]

Thus every optimum of the full graph-root LP uses a cross-epoch root.  This
is genuine cross-epoch essentiality inside (3.1), but a symmetric root is not
yet a directed current-to-past payment.

A second exact 30-row dual is feasible for every one of the 1326 roots and
gives

\[
 P\ge L_{\rm graph}
 =\frac{55874798199}{102400000000}
 >2D=\frac{2069}{5120}.
 \tag{3.4}
\]

Hence, under the one-for-one pair identity described below,

\[
 \Phi\le 2D-P
 \le-\frac{14494798199}{102400000000}<0.
 \tag{3.5}
\]

The exact graph optimum is not claimed: (3.2) and (3.4) are a feasible upper
bound and a sufficient lower bound.

## 4. A rational cross-epoch PSD witness

The larger fixed cone replaces graph roots by any matrix

\[
 X\succeq0,\qquad X\mathbf1=0,
 \tag{4.1}
\]

on the 52 `q` coordinates.  Its owner row is

\[
 q_{G_o}(c)^T Xq(c)\ge d_{o,c},
 \tag{4.2}
\]

and its physical price is

\[
 P(X)=\sum_c |c|q(c)^TXq(c).
 \tag{4.3}
\]

The certificate stores an exact rational factor `B` with shape `52 x 13`,
common denominator `5200000`, and column sums zero.  For `X=BB^T`, all 608
rows hold exactly and

\[
 P(X)=\frac{19511959}{50000000}
 <2D
\]

by the exact margin

\[
 \frac{5544953}{400000000}.
 \tag{4.4}
\]

All 640 past/current matrix entries are nonzero; for example the
`T100:a3`--`T100:a8` entry is
`-5161063/13520000000000`.  This proves that legal zero-row-sum PSD geometry
can contain a genuine cross-epoch block.  It does not prove that such a block
is essential in the PSD optimum and does not orient the block as a source-to-
sink flow.

## 5. Exact PSD dual and closure of this fixed cone

For each owner row, let `B_(o,c)` be the symmetric matrix satisfying

\[
 \langle B_{o,c},X\rangle=q_{G_o}(c)^TXq(c),
\]

and let

\[
 G=\sum_c |c|q(c)q(c)^T.
\]

For nonnegative dual weights `y`, it is enough that

\[
 E^T\left(G-\sum_{o,c}y_{o,c}B_{o,c}\right)E\succeq0,
 \qquad E=(e_0-e_{51},\ldots,e_{50}-e_{51}),
 \tag{5.1}
\]

because the columns of `E` span `1^perp`.  The stored rational dual has 227
positive rows and objective

\[
 L_{\rm PSD}=\frac{64678786029}{204800000000}.
 \tag{5.2}
\]

Exact rational LDL replay of the `51 x 51` matrix in (5.1) gives 51 strictly
positive pivots.  No floating solver is used by the certificate.

## 6. One-for-one Gothic/Abel owner ledger

The 46 primitive direct-M pair rows for `n=4,8` are retained one-for-one with

\[
 \lambda_{p,q}=2M_{p-n,q-n+1}.
 \tag{6.1}
\]

This rewrites the existing Gothic row; it does not create a second budget.
Each strict positive pair has one birth epoch, its prebirth state is zero,
and the finite scale Abel identity keeps the upper `T=1600` terminal:

\[
 \sum_r a_{\gamma,r}v_{\gamma,r}
 =\sum_r s_{\gamma,r}(v_{\gamma,r}-v_{\gamma,r+1})
  +s_{\gamma,U}v_{\gamma,U+1}.
 \tag{6.2}
\]

For the existing proportional allocation, exact totals are

\[
 G_{\rm off}=\frac{1553495291871}{12502746112000},\qquad
 T_{\rm owned}=\frac{972694327829}{12502746112000},
\]

and `G_off+T_owned=D`.  At the PSD witness price this gives

\[
 \Phi=2G_{\rm off}-P
 =-\frac{2768860635551669}{19535540800000000}<0.
\]

The certificate also optimizes every permitted finite pair allocation under

\[
 0\le a_{\gamma,r}\le\frac{T_r\beta_\gamma}{2},\qquad
 \sum_\gamma a_{\gamma,r}v_{\gamma,r}=T_rQ_n(T_r).
 \tag{6.3}
\]

Each row is an exact bounded fractional-knapsack primal/dual pair.  The
minimum possible terminal and maximum possible off-diagonal mass are

\[
 T_{\min}=\frac{124605023}{1807769600},\qquad
 G_{\rm off}^{\max}=\frac{240656237}{1807769600}.
 \tag{6.4}
\]

Combining (5.2) and (6.4),

\[
 L_{\rm PSD}-2G_{\rm off}^{\max}
 =\frac{89607170277983}{1807769600000000}>0.
 \tag{6.5}
\]

Therefore every zero-row-sum PSD correction in this fixed coordinate-owner
model has `Phi<0`, even after optimizing the complete finite C067 pair
allocation.  A directed source map is not needed for this no-go: any legal
directed construction inside the priced cone would only be a restriction of
it.

## 7. Exact boundary of the result

What is closed is precise: all zero-row-sum PSD corrections satisfying the
608 canonical coordinate-owner rows on this fixed tower, combined with the
finite C067 pair-allocation convention, have negative `Phi`.

What remains open includes:

- arbitrary PSD corrections under a different owner or channel model;
- indefinite cross blocks;
- an injective primitive-row-to-directed-root source map;
- a global birth, shared-endpoint, final, and terminal ledger beyond this
  fixed finite calculation;
- C058, Questions 1 and 2, and any novelty or prize claim.

The executable certificate is
`ROUTE_C_SIGNED_COORDINATE_OWNER_MASTER_LP_certificate.py`; its committed JSON
is a canonical byte replay, and the focused tests include exact arithmetic,
scope, mutation, Boolean-type, non-object JSON, and raw-byte checks.

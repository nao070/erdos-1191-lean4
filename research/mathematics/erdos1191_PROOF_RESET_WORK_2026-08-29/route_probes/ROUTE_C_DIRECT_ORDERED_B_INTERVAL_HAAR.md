# Route C: direct ordered-\(B\) interval/Haar bridge

Date: 2026-08-30  
Status: `EXACT_DIRECT_B_INTERVAL_HAAR_BRIDGE_ONLY_COMMON_LEDGER_OPEN`

This note keeps the indefinite Wave coefficient matrix instead of replacing
it by a positive-semidefinite completion.  In physical point coordinates the
matrix becomes

\[
 M=D^{\mathsf T}BD.
\]

Although `M` is not positive semidefinite, it is nonnegative on every actual
single-box membership state.  Its entries are also exactly one half of the
finite-horizon Gothic mixed-difference coefficients.  This gives a common
coordinate bridge with no artificial coefficient-PSD diagonal price.

The bridge is useful but is **not** a complete common carrier.  Signed Haar
bands have both signs, a scalar interval cover is forced to vanish, a
zero-price root-restricted Schur coupling is forced to vanish, and the sharp
positive block-count baseline costs more than the positive same-epoch Gothic
sector on an exact Golomb family.  A finite multi-epoch signed SDP remains to
be solved.  Accordingly this note does not close C058, Question 1, Question
2, publication novelty, or the prize claim.

## 1. Coordinates and normalization

Fix an epoch `n>=2` and ordered marks

\[
 0=a_0<a_1<\cdots<a_{2n-1}.
\]

The current block has `n+1` physical endpoints

\[
 b_k=a_{n-1+k},\qquad 0\le k\le n.
 \tag{1.1}
\]

For `T>0`, use the half-open normalized box

\[
 K_T(x)=\frac1T{\bf1}_{[0,T)}(x),
 \qquad q_k=\delta_{b_k}*K_T.
 \tag{1.2}
\]

Let `D` be the `n` by `n+1` first-difference matrix

\[
 (Du)_i=u_i-u_{i+1},\qquad 0\le i<n.
 \tag{1.3}
\]

Thus the full-gap dipole channels are

\[
 f_i=q_i-q_{i+1}.
\]

In local gap indices `0<=i,j<n`, define

\[
 B_{ii}=0,
 \qquad B_{i,i+1}=B_{i+1,i}=0,
 \qquad
 B_{ij}=-\frac{(j-i)^2}{8n^2}\quad(|i-j|\ge2).
 \tag{1.4}
\]

The denominator is `8n^2`, not `4n^2`.  The Wave weight on one unordered
edge is

\[
 \alpha_{ij}=\frac{(j-i)^2}{4n^2},
\]

and the symmetric Frobenius contraction counts the two entries `(i,j)` and
`(j,i)`:

\[
 2B_{ij}\langle f_i,f_j\rangle
 =-\alpha_{ij}\langle f_i,f_j\rangle.
 \tag{1.5}
\]

Write

\[
 P_T=(\langle q_k,q_\ell\rangle)_{0\le k,\ell\le n},
 \qquad
 G_T=DP_TD^{\mathsf T},
 \qquad
 M=D^{\mathsf T}BD.
 \tag{1.6}
\]

Then, with the Frobenius inner product,

\[
 \boxed{Q_n(T)=\langle B,G_T\rangle_F
              =\langle M,P_T\rangle_F.}
 \tag{1.7}
\]

Two elementary structural identities will matter repeatedly:

\[
 M\mathbf1=0,
 \qquad M_{kk}=0\quad(0\le k\le n).
 \tag{1.8}
\]

The first follows from `D 1=0`.  For an internal point `k`, the second is

\[
 M_{kk}=B_{k-1,k-1}+B_{kk}-2B_{k-1,k}=0,
\]

because both diagonal and adjacent entries of `B` vanish.  The two endpoint
diagonal identities are immediate.

## 2. Exact interval-state theorem

For local point indices `0<=p<=q<=n`, let

\[
 u_{[p,q]}={\bf1}_{\{p,p+1,\ldots,q\}},
 \qquad m=q-p+1.
\]

### Theorem 2.1

For every `n>=2`,

\[
 \boxed{
 u_{[p,q]}^{\mathsf T}Mu_{[p,q]}
 =
 \begin{cases}
 \dfrac{m^2}{4n^2},&0<p\le q<n\text{ and }m\ge2,\\[4pt]
 0,&\text{otherwise}.
 \end{cases}}
 \tag{2.1}
\]

Consequently every binary interval state satisfies

\[
 \boxed{
 0\le u^{\mathsf T}Mu
 \le \frac{(\mathbf1^{\mathsf T}u)^2}{4n^2}.}
 \tag{2.2}
\]

The constant is sharp for every `n>=3`; the interval `[1,2]` gives equality.
The canonical Wave application has `n>=4`.

### Proof

If the interval touches the left endpoint only, `Du=e_q`; if it touches the
right endpoint only, `Du=-e_{p-1}`; if it is the whole block, `Du=0`.
Equation (1.4) has zero diagonal, so all three cases have value zero.

For an internal interval,

\[
 Du=-e_{p-1}+e_q.
\]

If `m=1`, the two coordinates are adjacent and the value again vanishes.  If
`m>=2`, their separation is `q-(p-1)=m`, and therefore

\[
 u^{\mathsf T}Mu
 =(Du)^{\mathsf T}B(Du)
 =-2B_{p-1,q}
 =\frac{m^2}{4n^2}.
\]

This proves (2.1), (2.2), and sharpness.  The exact certificate exhausts all
216 interval states for `2<=n<=9`.

### Corollary 2.2: actual box-state domination

At a fixed spatial point `x`, the nonzero coordinates of

\[
 Tq(x)=\bigl(TK_T(x-b_k)\bigr)_{k=0}^n
\]

are consecutive: they are precisely the ordered marks in the half-open
window `(x-T,x]`.  Hence `Tq(x)` is either zero or one of the binary interval
states in Theorem 2.1.  Pointwise,

\[
 q(x)^{\mathsf T}Mq(x)
 \le \frac{(\sum_kq_k(x))^2}{4n^2}.
 \tag{2.3}
\]

Integration gives the sharp membership-count baseline

\[
 \boxed{
 Q_n(T)\le
 \frac1{4n^2}
 \left\|\sum_{k=0}^n q_k\right\|_2^2.}
 \tag{2.4}
\]

This is an actual-state theorem.  It is not a claim that `M` is positive
semidefinite or copositive on every nonnegative vector.

## 3. Exact Gothic mixed-difference matrix

Return temporarily to global interval indices.  For

\[
 n\le p\le q\le2n-1,
 \qquad
 D_{p,q}=a_q-a_{p-1},
\]

the two endpoints are the local physical points

\[
 k=p-n,
 \qquad
 \ell=q-n+1.
 \tag{3.1}
\]

Since

\[
 (P_T)_{k\ell}=R_T(D_{p,q}),
 \qquad
 R_T(d)=\frac{(T-d)_+}{T^2},
\]

and `P_T,M` are symmetric with zero diagonal contribution, (1.7) expands as

\[
 Q_n(T)=
 \sum_{n\le p\le q\le2n-1}
 2M_{p-n,q-n+1}R_T(D_{p,q}).
 \tag{3.2}
\]

The finite-horizon Gothic expansion is

\[
 Q_n(T)=\sum_{p,q}\lambda_{p,q}R_T(D_{p,q}),
\]

where

\[
 \lambda_{p,q}
 =\alpha_{p,q}+\alpha_{p-1,q+1}
  -\alpha_{p,q+1}-\alpha_{p-1,q}.
 \tag{3.3}
\]

This identity does not rely on uniqueness of the numerical distances.  Extend
the local `B` and the global `alpha` by zero outside their supported index
ranges.  Direct multiplication in `M=D^TBD`, with
`k=p-n` and `ell=q-n+1`, gives

\[
 M_{k\ell}
 =B_{k\ell}-B_{k,\ell-1}-B_{k-1,\ell}+B_{k-1,\ell-1}
 =\frac12\lambda_{p,q}.
\]

Thus the literal entrywise identity is

\[
 \boxed{2M_{p-n,q-n+1}=\lambda_{p,q}.}
 \tag{3.4}
\]

The factor `2` is essential.  It is the symmetric Frobenius pair, not a
change of the Gothic normalization.  The certificate checks all 164 rows for
`2<=n<=9` and stores the full `n=4` matrix

\[
M=\begin{pmatrix}
0&0&-1/32&-5/128&9/128\\
0&0&1/32&1/128&-5/128\\
-1/32&1/32&0&1/32&-1/32\\
-5/128&1/128&1/32&0&0\\
9/128&-5/128&-1/32&0&0
\end{pmatrix}.
 \tag{3.5}
\]

Thus direct `M`-pairs and the Gothic `lambda` rows are the **same physical
pairs**.  Equation (3.4) is a rewrite of the existing ledger, not a second
copy of its capacity.

### 3.1 Consecutive epoch ownership

The epoch-`n` point block is

\[
 \{a_{n-1},\ldots,a_{2n-1}\},
\]

and the next dyadic epoch's point block is

\[
 \{a_{2n-1},\ldots,a_{4n-1}\}.
\]

They share only `a_(2n-1)`.  Since `diag M=0`, a direct `M` row always owns a
pair of distinct points.  Therefore consecutive direct-pair supports are
disjoint.  The certificate exhausts this statement for `2<=n<=12`.

This does **not** make the positive count baseline free.  A block-count
matrix `J=11^T` includes the diagonal energy of the shared endpoint in both
blocks.  Naively summing two block baselines gives that diagonal multiplicity
two.  Any multi-epoch use of (2.4) must assign the shared diagonal to one
owner.  It must also replace, rather than duplicate, the same-epoch Gothic
rows identified by (3.4).

## 4. Exact dyadic Abel identity and Haar rows

Fix a logarithmic phase `theta` and set

\[
 T_r=2^{r+\theta},\qquad Q_r=Q_n(T_r).
\]

For any finite integers `L<=U`, direct reindexing gives

\[
 \boxed{
 \sum_{r=L}^U T_rQ_r
 =\sum_{r=L}^U2T_r(Q_r-Q_{r+1})
  -T_LQ_L+T_{U+1}Q_{U+1}.}
 \tag{4.1}
\]

The lower endpoint has a minus sign and the upper endpoint has a plus sign.
Indeed,

\[
 \sum_{r=L}^U2T_rQ_{r+1}
 =\sum_{r=L+1}^{U+1}T_rQ_r,
\]

which proves (4.1).  The certificate keeps a nonzero synthetic endpoint
fixture:

\[
 \frac{496}{21}
 =\frac{346}{231}-\frac{10}{3}+\frac{280}{11}.
 \tag{4.2}
\]

Both endpoint rows are therefore audited even when a later active choice
makes them vanish.

For `n>=3`, define

\[
 m_*=\min(h_{n+1},\ldots,h_{2n-2}),
 \qquad H=a_{2n-1}-a_{n-1}.
\]

Every nonadjacent ordered-root overlap vanishes for `T<=m_*`, while all
shifted current gaps lie beyond the block for `T>=H`.  Hence

\[
 Q_n(T)=0\quad(T\le m_*\text{ or }T\ge H).
 \tag{4.3}
\]

The canonical application has `n>=4`.  Choose `L,U` so that

\[
 T_L\le m_*,\qquad T_{U+1}\ge H.
\]

Then both boundary terms in (4.1) are exactly zero.

For the Golomb ruler

\[
 A=(0,1,3,7,12,20),\qquad n=3,
\]

we have `m_*=5`, `H=17`, and the phase-zero widths

\[
 4,8,16,32.
\]

Their exact densities are

\[
 Q_4=0,\qquad Q_8=\frac1{192},\qquad
 Q_{16}=\frac1{2304},\qquad Q_{32}=0.
\]

Thus

\[
 \sum_{T=4,8,16}TQ_T=\frac7{144},
\]

while the three terminal-free Abel rows are

\[
 -\frac1{24},\qquad \frac{11}{144},\qquad \frac1{72},
\]

and sum to the same `7/144`.  The first row is negative.

### 4.1 Why these are actual Haar Gram rows

Put

\[
 h_T=K_T-K_{2T}.
\]

The refinement identity for the normalized half-open boxes gives

\[
 \langle h_T,\tau_dh_T\rangle
 =R_T(d)-R_{2T}(d).
 \tag{4.4}
\]

Therefore

\[
 P_T-P_{2T}
 =\operatorname{Gram}(\delta_{b_k}*h_T)_{k=0}^n
\]

and

\[
 \boxed{
 G_T-G_{2T}
 =\operatorname{Gram}
 \bigl((\delta_{b_i}-\delta_{b_{i+1}})*h_T\bigr)_{i=0}^{n-1}.}
 \tag{4.5}
\]

Combining (4.1) and (4.5) makes the continuum Wave mass an exact average of
signed direct-`B` Haar rows:

\[
 \int_0^1\sum_{r\in\mathbb Z}T_rQ_n(T_r)\,d\theta
 =\frac1{\log2}\int_0^\infty Q_n(T)\,dT
 =\frac{\mathcal W_n}{\log2},
 \tag{4.6}
\]

where the first equality is the change of variables
`T=2^(r+theta)`, so `dT=(log 2)T dtheta`.  Applying the endpoint-free form of
(4.1) now yields

\[
 \frac{\mathcal W_n}{\log2}
 =\int_0^1\sum_r
 2T_r\langle B,G_{T_r}-G_{2T_r}\rangle_F\,d\theta,
 \tag{4.7}
\]

after the active endpoints have been chosen.  A Haar band can be active only
inside `(m_*/2,H)`, because either `Q(T)` or `Q(2T)` must be active.

Equation (4.7) is the desired common Haar coordinate bridge.  Its rows are
signed because `B` is indefinite.

## 5. Both signed-band signs occur exactly

The sign issue is not hypothetical.

### 5.1 Negative band

For

\[
 A=(0,1,3,7,12,20),\quad n=3,\quad T=3,
\]

the local matrix is

\[
 B=\begin{pmatrix}
 0&0&-1/18\\0&0&0\\-1/18&0&0
 \end{pmatrix}.
\]

The exact Gram rows are

\[
G_3=\begin{pmatrix}
2/3&-1/3&0\\
-1/3&2/3&-1/3\\
0&-1/3&2/3
\end{pmatrix},
\]

\[
G_6=\begin{pmatrix}
2/9&-1/12&-1/36\\
-1/12&5/18&-5/36\\
-1/36&-5/36&1/3
\end{pmatrix}.
\]

Hence

\[
 Q_3=0,\qquad Q_6=\frac1{324},
 \boxed{\langle B,G_3-G_6\rangle_F=-\frac1{324}.}
 \tag{5.1}
\]

### 5.2 Positive band

For

\[
 A=(0,101,204,309,416,525,636,749),\quad n=4,\quad T=200,
\]

exact contraction gives

\[
 Q_{200}=\frac9{32000},\qquad
 Q_{400}=\frac9{256000},
\]

so

\[
 \boxed{
 \langle B,G_{200}-G_{400}\rangle_F
 =\frac{63}{256000}.}
 \tag{5.2}
\]

Taking a positive part is of course a legal loose upper bound.  What (5.1)
and (5.2) forbid is treating the Abel row itself as equal to a nonnegative
retained band, or claiming its positive part as a free commonly owned
carrier.  An exact ownership ledger must retain the signs and actual cell
states.

## 6. An actual zero-aggregate Haar cell defeats `kappa J-mu M`

The positive fixture in Section 5.2 contains a sharper local obstruction.
Use

\[
 h_{200}=K_{200}-K_{400},
 \qquad
 v_p=400h_{200}(x-a_p).
\]

The half-open atomic cell

\[
 \boxed{x\in[636,709)}
\]

has length `73`.  On all eight marks the scaled Haar state is

\[
 (0,0,0,-1,-1,1,1,0).
\]

Restricting to the five current block points

\[
 (309,416,525,636,749)
\]

gives

\[
 v=(-1,-1,1,1,0),\qquad
 Dv=(0,-2,0,1),\qquad
 \mathbf1^{\mathsf T}v=0.
\]

Using (3.5),

\[
 v^{\mathsf T}Mv=(Dv)^{\mathsf T}B(Dv)=\frac18.
 \tag{6.1}
\]

In the unscaled Haar normalization this is the pointwise density

\[
 \frac{1/8}{400^2}=\frac1{1280000},
\]

and the cell contributes `73/1280000` to the Haar Gram contraction.

Let `J=11^T`.  Because `1^T v=0`, for every `kappa` and every `mu>0`,

\[
 v^{\mathsf T}(\kappa J-\mu M)v=-\frac\mu8<0.
 \tag{6.2}
\]

Therefore the aggregate block-count channel alone cannot provide a
cell-by-cell positive rewrite of the direct signed `M` row.  This does not
contradict the integrated positive value (5.2): other cells compensate it.

## 7. Two zero-price repair obstructions

### 7.1 Singleton interval cover

Suppose one tries to cover a scalar linear channel `c^T u` by `M` on every
binary interval state:

\[
 (c^{\mathsf T}u)^2\le C\,u^{\mathsf T}Mu.
 \tag{7.1}
\]

Every singleton `u=e_k` is an interval state and has

\[
 e_k^{\mathsf T}Me_k=M_{kk}=0.
\]

Equation (7.1) forces `c_k=0` for every `k`, so `c=0`.  There is no nonzero
rank-one scalar interval cover at zero price.

### 7.2 Root-restricted Schur coupling

The next statement is deliberately root-restricted; it does **not** assume
that the whole coefficient block containing the indefinite `B` is positive
semidefinite.

Let `D_ext` be positive definite and consider the quadratic block

\[
 \begin{pmatrix}B&X\\X^{\mathsf T}&D_{\rm ext}\end{pmatrix}.
\]

Require nonnegativity only on every pair `(t e_i,y)`, where `e_i` is a
singleton ordered root and `t,y` are unrestricted.  Minimizing over `y`
gives the root residual

\[
 t^2e_i^{\mathsf T}
 (B-XD_{\rm ext}^{-1}X^{\mathsf T})e_i
 =-t^2e_i^{\mathsf T}XD_{\rm ext}^{-1}X^{\mathsf T}e_i,
 \tag{7.2}
\]

because `B_ii=0`.  Nonnegativity for every `t` forces

\[
 X^{\mathsf T}e_i=0
\]

for every `i`, hence `X=0`.  The certificate includes the exact one-column
fixture `D_ext=1`, `X=e_0`; the vector `(e_0,-1)` has quadratic value `-1`.

Thus a positive external channel cannot couple to every zero-slack singleton
root for free.  A legal repair must pay positive diagonal energy or exploit a
weaker signed/actual-state structure.

## 8. The sharp count baseline is not paid by the positive Gothic sector

Consider the affine Golomb family

\[
 A_L=(0,2,5,16,L+16,L+17,L+25,3L+25),
 \qquad L\in\mathbb Z,\ L\ge26.
 \tag{8.1}
\]

Every positive integral collision parameter between two affine difference
forms is at most `25`, and same-slope constants are distinct.  Hence (8.1) is
a Golomb ruler for every integer `L>=26`.

The current five-point block is

\[
 S=(16,L+16,L+17,L+25,3L+25).
\]

On `9<T<L`, only the three middle points interact, at distances `1,8,9`.
Therefore

\[
 \left\|\sum_{b\in S}\delta_b*K_T\right\|_2^2
 =\frac5T+\frac2{T^2}\bigl((T-1)+(T-8)+(T-9)\bigr)
 =\frac{11}{T}-\frac{36}{T^2}.
 \tag{8.2}
\]

Since `4n^2=64`, the sharp count baseline from (2.4) is

\[
 B_{\rm count}(T)
 =\frac{11}{64T}-\frac9{16T^2}.
 \tag{8.3}
\]

The three active Wave edges give

\[
 Q_4(T)=\frac9{64T}-\frac{45}{64T^2},
 \tag{8.4}
\]

and hence

\[
 B_{\rm count}(T)-Q_4(T)
 =\frac1{32T}+\frac9{64T^2}>0.
 \tag{8.5}
\]

Integration gives

\[
 \int_9^L B_{\rm count}(T)\,dT
 =\frac{11}{64}\log\frac L9-\frac1{16}+\frac9{16L}.
 \tag{8.6}
\]

Denote the integral in (8.6) by `mathcal B_L`.

The complete positive same-epoch Gothic capacity for this family is

\[
 G_L=\frac1{16}F_H(1)+\frac1{64}F_H(9)+\frac1{16}F_H(8),
 \qquad H=3L+9,
\]

so

\[
 G_L=\frac1{64}
 \left(9\log H-\log9-4\log8-9+\frac{45}{H}\right).
 \tag{8.7}
\]

The log-`L` coefficient of (8.6) is `11/64`; that of (8.7) is `9/64`.
Their gap is `1/32`.

There is also an exact finite witness.  Put

\[
 L=2^{24},\qquad H=3L+9.
\]

Direct subtraction gives

\[
64(\mathcal B_L-G_L)
=11\log L-9\log H-10\log9+4\log8+5+\frac{36}{L}-\frac{45}{H}.
 \tag{8.8}
\]

Since `H<=4L`, `log 2>2/3`, `log 9<3`, and `45/H<1`, while `36/L>0`,

\[
64(\mathcal B_L-G_L)
>42\cdot\frac23-10\cdot3+5-1=2.
\]

Thus

\[
 \boxed{\mathcal B_L-G_L>\frac1{32}}
 \tag{8.9}
\]

at this finite `L`.  The logarithm bounds are certified by the positive
atanh series: the first term gives `log 2>2/3`; for `z=4/5`, the first term
plus a geometric tail gives `log 9<344/135<3`.

Equations (8.6)--(8.9) close only the proposal that the sharp positive count
baseline is free or is paid solely by the positive same-epoch Gothic sector.
They do not rule out a cheaper state-dependent PSD correction, a signed
cross-epoch repair, or a larger common master.

## 9. A finite, falsifiable SDP target

The actual Haar cell obstruction turns the next step into a finite exact
optimization problem rather than a qualitative hope.

### 9.1 One epoch and one scale

Fix the physical block points and `T`.  Sort all distinct endpoints

\[
 b_k,\qquad b_k+T,
 \qquad b_k+2T.
\]

They partition the real line into half-open atomic cells.  For one sample
`x_c` in each cell, define the integer Haar state

\[
 v_c=\bigl(2T h_T(x_c-b_k)\bigr)_{k=0}^n.
\]

Search over

- a symmetric positive-semidefinite matrix `C` on the `n+1` physical point
  coordinates;
- the normalization `C 1=0`;
- `kappa>=0` and `mu>0`.

The actual-state constraints are

\[
 \boxed{
 v_c^{\mathsf T}(\kappa J+C-\mu M)v_c\ge0
 \quad\text{for every atomic cell }c.}
 \tag{9.1}
\]

A stronger ordinary-Cauchy relaxation replaces (9.1) by

\[
 \kappa J+C-\mu M\succeq0.
\]

The normalized diagonal price objective is

\[
 \min\frac{\operatorname{tr}C}{2T}.
 \tag{9.2}
\]

The cell `[636,709)` proves that `C=0` is infeasible for every `mu>0`,
regardless of `kappa`.  Also, positive-semidefinite `C` with `diag C=0`
forces `C=0`; every nontrivial PSD repair therefore has a positive diagonal
price.

### 9.2 Finite multi-epoch extension

For finitely many epochs, first deduplicate the union of their physical point
blocks.  Embed each `M_s` and `J_s` in this common physical coordinate set.
At a common width `T`, partition by every union endpoint

\[
 a_p,\qquad a_p+T,\qquad a_p+2T,
\]

and impose

\[
 v_c^{\mathsf T}
 \left(C+\sum_s\kappa_sJ_s-\sum_s\mu_sM_s\right)v_c\ge0
 \tag{9.3}
\]

on every cell.  For several dyadic widths, concatenate the coordinates
indexed by `(epoch,scale)`, use one block PSD correction `C`, partition by all
`a_p`, `a_p+T_r`, `a_p+2T_r`, and minimize

\[
 \sum_r\frac{\operatorname{tr}C_{rr}}{2T_r}.
 \tag{9.4}
\]

A successful computation must emit an exact rational primal matrix, exact
rational dual cell weights, and zero duality gap.  Shared endpoint diagonals
must have one explicit owner.  Gothic rows must be rewritten through (3.4),
not counted twice.  This is a concrete falsifiable schema; no feasible
multi-epoch certificate is claimed here.

## 10. What is proved and what remains open

This bundle proves and certifies:

1. the exact `B` normalization and `M=D^TBD` physical-point rewrite;
2. the complete binary interval-state formula and sharp count domination;
3. the exact global/local relation `2M=lambda`;
4. the Abel identity with the lower negative and upper positive endpoint
   rows, plus a terminal-free active choice;
5. the exact Haar Gram identity and both signed-band signs;
6. the actual half-open cell `[636,709)` with zero aggregate and
   `v^T M v=1/8`;
7. the singleton scalar-cover and root-restricted zero-slack Schur
   obstructions;
8. disjoint consecutive direct-pair supports together with the still-unowned
   shared count-diagonal;
9. the `A_L` count-baseline/Gothic separation, including the finite
   `L=2^24` witness;
10. an explicit finite rational SDP target for the next computation.

It does **not** prove:

- a sign for every Haar band;
- a free diagonal/Schur repair;
- an owner for the shared multi-epoch endpoint diagonal;
- a feasible finite multi-epoch common signed master;
- that signed, cross-epoch, cross-phase, or state-dependent payment is
  impossible;
- C058, Question 1, Question 2, a complete proof, publication novelty, or
  prize eligibility.

## 11. Machine replay

The companion exact artifacts are:

- `direct_ordered_b_interval_haar_certificate.py`;
- `direct_ordered_b_interval_haar_certificate.json`;
- `test_direct_ordered_b_interval_haar_certificate.py`.

The committed certificate has semantic payload SHA-256

```text
8f067c8e409b93058520b6e669de7eb4370e81c19b1c5abd988e1c0e68fc6ac2
```

Replay with

```bash
PYTHONDONTWRITEBYTECODE=1 python3 direct_ordered_b_interval_haar_certificate.py \
  --verify direct_ordered_b_interval_haar_certificate.json --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -q \
  test_direct_ordered_b_interval_haar_certificate.py
```

The verifier checks semantic equality and the literal canonical JSON bytes.
The focused suite has 16 tests, and the self-check rejects 16 independent
semantic/hash mutations.

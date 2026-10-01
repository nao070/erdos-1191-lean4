# Route C: actual ordered Gram root cone and the rank-one ramp master

Date: 2026-08-30  
Status: `EXACT_FIXED_SCALE_ORDERED_GRAM_RAMP_ONLY_COMMON_PAYMENT_OPEN`

This note gives an exact positivity theorem that is strictly adapted to the
actual one-dimensional ordered box-dipole Gram matrix.  It is weaker than
coefficient positive semidefiniteness and therefore avoids the diagonal SDP
price of C069 at a fixed scale.  It also gives a rank-one ramp channel whose
energy dominates the Wave density, with an exact nonnegative surplus and an
optimal-shift Schur-complement formula.

The fixed-scale theorem is complete.  Its insertion into the signed,
finite-horizon common master is not complete.  In particular, an ungated
ramp energy diverges at small scales, signed band differences leave the root
cone, and zero slack on every nonadjacent Wave root blocks nonconstant Schur
cross-coupling.  No closure of Route C, C058, either question in Erdős
Problem #1191, publication novelty, complete proof, or prize claim is made.

## 1. Full-gap intervals and the exact root cone

Fix

\[
 0=a_0<a_1<\cdots<a_{2n-1},\qquad
 I=\{n,n+1,\ldots,2n-1\},
\]

and a scale `T>0`.  Put

\[
 e_i=\delta_{a_{i-1}}-\delta_{a_i},\qquad
 K_T=T^{-1}{\bf1}_{[0,T)},\qquad
 f_i=e_i*K_T.
 \tag{1.1}
\]

Use the full gap interval and its translate

\[
 V_i=[a_{i-1},a_i),\qquad U_i=V_i+T.
 \tag{1.2}
\]

The elementary interval identity

\[
 {\bf1}_{[a_{i-1},a_{i-1}+T)}
 -{\bf1}_{[a_i,a_i+T)}
 ={\bf1}_{V_i}-{\bf1}_{U_i}
\]

gives

\[
 \boxed{T f_i={\bf1}_{V_i}-{\bf1}_{U_i}.}
 \tag{1.3}
\]

The intervals `V_i` are pairwise disjoint, and so are the intervals `U_i`.
Moreover, `U_i` can meet `V_j` only in the forward order `i<j`, apart from
the same-index overlap whose two signs cancel.  Therefore, for almost every
`x`, the block vector

\[
 z(x)=T(f_i(x))_{i\in I}
\]

is exactly one of

\[
 0,\qquad +e_i,\qquad -e_i,\qquad e_j-e_i\quad(i<j).
 \tag{1.4}
\]

Here and below `e_i` in a matrix expression denotes the coordinate vector;
the context distinguishes it from the endpoint dipole in (1.1).

Define the ordered overlap cells and their masses by

\[
 E_{ij}=U_i\cap V_j,\qquad
 \psi_{ij}(T)={|E_{ij}|\over T^2}\quad(i<j).
 \tag{1.5}
\]

The cells `E_(i,j)` are pairwise disjoint, because at any point there is at
most one active interval from each of the two families.  If `G=G_T` is the
Gram matrix of `(f_i)_(i in I)`, then

\[
 G_{ij}=-\psi_{ij}(T)\quad(i<j),\qquad
 G_{ii}={2\min(h_i,T)\over T^2},
 \tag{1.6}
\]

where `h_i=a_i-a_(i-1)`.  Put

\[
 \rho_i(T)=G_{ii}-\sum_{j\ne i}\psi_{\min(i,j),\max(i,j)}(T).
 \tag{1.7}
\]

The pointwise alternatives in (1.4) show directly that `rho_i` is the
normalized measure of the singleton cells carrying `+/-e_i`.  Hence
`rho_i>=0`, and integration of `z(x)z(x)^T` gives the exact factorization

\[
 \boxed{
 G=\operatorname{diag}(\rho)
   +\sum_{i<j}\psi_{ij}(e_i-e_j)(e_i-e_j)^T.}
 \tag{1.8}
\]

Thus every actual ordered-box Gram matrix is a grounded Laplacian, or SDDM
matrix, with its root cells still labeled.  For every symmetric coefficient
matrix `C`, (1.8) gives the exact dual contraction

\[
 \boxed{
 \langle C,G\rangle
 =\sum_i\rho_i C_{ii}
  +\sum_{i<j}\psi_{ij}
     (C_{ii}+C_{jj}-2C_{ij}).}
 \tag{1.9}
\]

Consequently the conditions

\[
 C_{ii}\ge0,
 \qquad C_{ii}+C_{jj}-2C_{ij}\ge0\quad(i<j)
 \tag{1.10}
\]

are sufficient for nonnegativity on every such ordered Gram matrix.  They
are strictly weaker than `C>=0` as an ordinary coefficient matrix.

For a nonadjacent pair, the overlap length in (1.5) is precisely the tent
numerator from the box-dipole bridge.  If

\[
 M=D_{i+1,j-1},\quad u=h_i,\quad v=h_j,
\]

then

\[
 T^2\psi_{ij}
 =(T-M)_+ +(T-M-u-v)_+
 -(T-M-u)_+-(T-M-v)_+.
 \tag{1.11}
\]

This also locks the sign and the absence of an extra factor `2`.

## 2. The Wave matrix is in the ordered-Gram dual cone

For every nonadjacent Wave pair in the block, let

\[
 \alpha_{ij}={(j-i)^2\over4n^2},
\]

and define the symmetric matrix `B` by

\[
 B_{ii}=0,\qquad
 B_{ij}=B_{ji}=-{\alpha_{ij}\over2}\quad(j\ge i+2),
 \tag{2.1}
\]

with adjacent entries zero.  The off-diagonal factor `1/2` is required
because the Frobenius contraction counts both `(i,j)` and `(j,i)`.  Using
`G_(i,j)=-psi_(i,j)` gives

\[
 \boxed{
 \langle B,G\rangle
 =\sum_{j\ge i+2}\alpha_{ij}\psi_{ij}(T)
 =Q_n(T).}
 \tag{2.2}
\]

On a singleton root, `B` has value zero.  On `e_j-e_i`, its quadratic value
is `alpha_(i,j)` for a nonadjacent pair and zero for an adjacent pair.  Thus
`B` lies in the dual cone (1.10), although it is not coefficient PSD.

The disjoint cell labels make the positivity more explicit:

\[
 \boxed{
 Q_n(T)=
 \sum_{j\ge i+2}\alpha_{ij}
 \left\|T^{-1}{\bf1}_{E_{ij}}\right\|_2^2.}
 \tag{2.3}
\]

Therefore no coefficient-PSD diagonal completion of `B` is needed to prove
fixed-scale nonnegativity or to obtain the cellwise representation (2.3).
This is not yet a statement that a common smoothing master can absorb these
rank channels at zero global cost.

The distinction is material.  Any nonzero symmetric matrix with zero trace
cannot be semidefinite.  Hence `B` is indefinite as soon as a Wave edge is
present.  The actual Gram `G` is positive definite: convolution by `K_T` is
injective on a finite signed measure, and the chain dipoles are linearly
independent.  Sylvester inertia under the congruence
`G^(1/2) B G^(1/2)` therefore does not turn `B` into an ordinary PSD
coefficient master.

The marginal transport theorem is compatible with (2.3).  Its hierarchy

\[
 Q_n(T)\le V_n(T)\le {P_n^{\rm PSD}(T)\over2}
 \tag{2.4}
\]

is the sharp price after forgetting the exact cells and retaining only row
and column strip masses.  The root-cone SOS retains the cells.  There is no
universal ordering asserted here between `V_n(T)` and the ramp energy below.

## 3. Rank-one ramp domination and exact surplus

Fix any real shift `c` and put

\[
 \eta_i={i-c\over2n},\qquad H=\eta\eta^T.
 \tag{3.1}
\]

For every pair,

\[
 (e_j-e_i)^TH(e_j-e_i)
 = (\eta_j-\eta_i)^2
 ={(j-i)^2\over4n^2}.
 \tag{3.2}
\]

Hence the root quadratic of `H-B` is zero on every nonadjacent Wave pair,
while on every adjacent pair it is exactly `1/(4n^2)`.  Its singleton value
is `eta_i^2`.  Applying the ordered-Gram dual formula (1.9) yields

\[
 \boxed{
 \eta^TG\eta-Q_n(T)
 =\sum_i\rho_i\eta_i^2
  +{1\over4n^2}\sum_{i=n}^{2n-2}\psi_{i,i+1}(T)
 \ge0.}
 \tag{3.3}
\]

This is the exact surplus, not merely an inequality proof.  Equivalently,
`H-B` belongs to the ordered-root dual cone even though it need not be an
ordinary PSD coefficient matrix.

The ramp energy is one scalar `L^2` channel.  Writing

\[
 q_a=\delta_a*K_T,
\]

summation by parts gives

\[
 \boxed{
 \sum_{i=n}^{2n-1}\eta_i f_i
 ={1\over2n}\left[
 (n-c)q_{a_{n-1}}
 +\sum_{p=n}^{2n-2}q_{a_p}
 -(2n-1-c)q_{a_{2n-1}}
 \right].}
 \tag{3.4}
\]

The displayed spatial coefficients sum to zero.  The channel is therefore
centered, but it contains both block terminals and every interior mark.
Legal ownership of those diagonal and terminal contributions is still a
separate common-master obligation.

## 4. Optimal shift and its Schur complement

Let

\[
 r=(n,n+1,\ldots,2n-1)^T,\qquad {\bf1}=(1,\ldots,1)^T.
\]

The Laplacian part of (1.8) kills the all-ones vector, so

\[
 G{\bf1}=\rho,\qquad
 r^TG{\bf1}=\sum_i i\rho_i,\qquad
 {\bf1}^TG{\bf1}=\sum_i\rho_i.
 \tag{4.1}
\]

The dipoles telescope:

\[
 \sum_{i=n}^{2n-1}f_i
 =(\delta_{a_{n-1}}-\delta_{a_{2n-1}})*K_T.
\]

If `H_block=D_(n,2n-1)=a_(2n-1)-a_(n-1)`, then

\[
 \boxed{
 {\bf1}^TG{\bf1}
 ={2\min(H_{\rm block},T)\over T^2}>0.}
 \tag{4.2}
\]

It follows that the unique energy-minimizing shift is

\[
 \boxed{
 c_*={r^TG{\bf1}\over{\bf1}^TG{\bf1}}
 ={\sum_i i\rho_i\over\sum_i\rho_i}.}
 \tag{4.3}
\]

Completing the square gives the exact Schur complement

\[
 \boxed{
 \min_c\eta^TG\eta
 ={1\over4n^2}\left(
 r^TGr-{(r^TG{\bf1})^2\over{\bf1}^TG{\bf1}}
 \right).}
 \tag{4.4}
\]

Combining (3.3) and (4.3), the optimal surplus can also be written

\[
 \boxed{
 \min_c\eta^TG\eta-Q_n(T)
 ={1\over4n^2}\left[
 \sum_{i=n}^{2n-2}\psi_{i,i+1}
 +\sum_i\rho_i(i-c_*)^2
 \right].}
 \tag{4.5}
\]

The optimizer `c_*` generally depends on both the prefix and `T`.  Formula
(3.3) remains valid for every fixed `c`; no scale-dependent choice may be
silently promoted to a pre-existing fixed channel without verifying that
the surrounding master permits it.

## 5. Exact `n=4` ramp fixture

Take the Golomb prefix

\[
 A=(0,101,204,309,416,525,636,749),\qquad n=4,\qquad T=221.
 \tag{5.1}
\]

All 28 positive differences are distinct.  On the gap block
`I={4,5,6,7}`, the exact integer-scaled Gram matrix is

\[
 T^2G=
 \begin{pmatrix}
 214&0&-106&-1\\
 0&218&0&-109\\
 -106&0&222&-3\\
 -1&-109&-3&226
 \end{pmatrix}.
 \tag{5.2}
\]

The six ordered overlap numerators are

\[
 T^2(\psi_{45},\psi_{46},\psi_{47},
      \psi_{56},\psi_{57},\psi_{67})
 =(0,106,1,0,109,3),
 \tag{5.3}
\]

and

\[
 T^2(\rho_4,\rho_5,\rho_6,\rho_7)
 =(107,109,113,113).
 \tag{5.4}
\]

The leading principal minors of `T^2G` are

\[
 214,\quad46652,\quad7907296,\quad1355494352,
\]

so the Gram is positive definite.  The Wave density is

\[
 T^2Q_4(T)={869\over64}.
 \tag{5.5}
\]

At the midpoint shift `c=11/2`,

\[
 \eta={1\over16}(-3,-1,1,3),
\]

and the exact ramp ledger is

\[
 T^2\eta^TG\eta={2845\over128},
 \qquad
 T^2(\eta^TG\eta-Q_4)={1107\over128}.
 \tag{5.6}
\]

The two pieces of the surplus are

\[
 T^2\sum_i\rho_i\eta_i^2={1101\over128},
 \qquad
 {T^2\over64}\sum_{i=4}^{6}\psi_{i,i+1}
 ={3\over64}={6\over128}.
 \tag{5.7}
\]

For the optimal shift, the raw integer-scaled Schur data are

\[
 r^T(T^2G)r=14914,\qquad
 r^T(T^2G){\bf1}=2442,\qquad
 {\bf1}^T(T^2G){\bf1}=442.
\]

Thus

\[
 c_*={1221\over221},\qquad
 T^2\min_c\eta^TG\eta={39289\over1768},
\]

and

\[
 T^2(\min_c\eta^TG\eta-Q_4)
 ={122263\over14144}.
 \tag{5.8}
\]

The residual variance before multiplication by `1/(4n^2)=1/64` is
`121600/221`, agreeing exactly with (4.5).

This fixture also separates ordered-root positivity from coefficient PSD.
Here `B` has bipartite block form with invertible cross block,

\[
 \det B={1\over1048576},\qquad
 \det B_{\{4,5\},\{6,7\}}={1\over1024},
\]

and inertia `(2 positive, 2 negative, 0 zero)`.

## 6. Exact `n=5` active triangle

The ordered-root theorem does not rely on a bipartite sign switch.  Consider

\[
 A=(0,6,14,29,53,153,154,257,259,366),
 \qquad n=5,\qquad T=107.
 \tag{6.1}
\]

All 45 positive differences are distinct.  The active nonadjacent Wave graph
contains the triangle on vertices `{5,7,9}`.  Its exact rows are

\[
\begin{array}{c|c|c|c|c}
(i,j)&M_{ij}&D_{ij}&\alpha_{ij}&\psi_{ij}(107)\\ \hline
(5,7)&1&204&1/25&97/11449\\
(7,9)&2&212&1/25&103/11449\\
(5,9)&106&313&4/25&1/11449.
\end{array}
 \tag{6.2}
\]

Every overlap is positive, so the odd cycle is genuine.  It rules out a
universal bipartite sign-switch reduction even for a Golomb/Sidon prefix.
The cellwise SOS (2.3) and ramp theorem (3.3) are unaffected.

## 7. Why an ungated ramp integral is illegal

Let

\[
 c_0={3n-1\over2}.
\]

If

\[
 0<T<\min_{i\in I}h_i,
\]

no nonadjacent overlap is active, and hence `Q_n(T)=0`.  The adjacent roots
remain active: `psi_(i,i+1)=1/T`, equivalently `G` is `1/T` times the
tridiagonal Dirichlet path matrix with diagonal `2` and adjacent entries
`-1`.
The adjacent roots and the two singleton boundary cells therefore give

\[
 \boxed{
 \eta(c_0)^TG_T\eta(c_0)
 ={n^2-1\over8n^2T}.}
 \tag{7.1}
\]

Therefore integrating this ramp energy down to `T=0` creates a logarithmic
divergence that is absent from `Q_n`.  On the `n=4` fixture the coefficient is
exactly `15/128`.  At the certified scale `T=1`, the matrix is explicitly

\[
 T^2G=
 \begin{pmatrix}
 2&-1&0&0\\
 -1&2&-1&0\\
 0&-1&2&-1\\
 0&0&-1&2
 \end{pmatrix}.
 \tag{7.2}
\]

Thus replacing the energy by `2 sum_i eta_i^2/T` would incorrectly discard
the adjacent cross terms.

There is a natural active localization.  For `n>=3`, set

\[
 m_* =\min_{r=n+1}^{2n-2}h_r,
 \qquad H_{\rm block}=D_{n,2n-1}.
 \tag{7.3}
\]

Every nonadjacent tent satisfies

\[
 \psi_{ij}(T)>0
 \quad\Longleftrightarrow\quad
 D_{i+1,j-1}<T<D_{i,j}.
\]

Consequently

\[
 Q_n(T)=0\quad\text{unless}\quad m_*<T<H_{\rm block}.
 \tag{7.4}
\]

For (5.1), this gate is `109<T<440`.  Restricting (3.3) to the active union
removes the small-scale divergence.  It does not by itself prove that the
resulting gated diagonal and terminal ramp energy is already owned by the
current signed multiband ledger.  That ownership/cancellation step remains
the next central obligation.

## 8. Signed-band cone loss

Nonnegative sums or integrals of matrices of the form (1.8) remain in the
ordered root cone.  Signed scale differences need not.  A minimal exact
Golomb fixture is

\[
 A=(0,1,3,7,12,20),\qquad n=3,\qquad T=3.
 \tag{8.1}
\]

Its 15 positive differences are distinct, but

\[
 G_T-G_{2T}=
 \begin{pmatrix}
 4/9&-1/4&1/36\\
 -1/4&7/18&-7/36\\
 1/36&-7/36&1/3
 \end{pmatrix}.
 \tag{8.2}
\]

The positive off-diagonal entry `1/36` violates the SDDM sign condition.
Thus a signed band cone cannot inherit (1.8) merely by linearity.  Cell labels
or an additional factorization must be retained across scales.

Arbitrary coefficient mixing is also unsafe.  For the `n=3` Wave matrix,
the sum-zero vector `(1,-2,1)` has

\[
 (1,-2,1)B(1,-2,1)^T=-{1\over9}.
 \tag{8.3}
\]

The legal object is the actual ordered Gram contraction, or the pointwise
root-cell scalar master; it is not an arbitrary linear recombination of rank
channels.

## 9. Zero-slack Schur cross-coupling obstruction

The nonadjacent roots of `C=H-B` have exactly zero slack.  This sharply
restricts attempts to couple the ramp block to external channels.

Let `D` be a positive-definite external coefficient block and `X` a cross
block.  If the common block

\[
 \mathcal M=
 \begin{pmatrix}
 C&X\\X^T&D
 \end{pmatrix}
 \tag{9.1}
\]

must be nonnegative for every external vector on an allowed root `r`, then
minimizing over the external vector gives the necessary Schur condition

\[
 r^T(C-XD^{-1}X^T)r\ge0.
 \tag{9.2}
\]

For every nonadjacent Wave root `r=e_j-e_i`,

\[
 r^TCr=0.
\]

Since the subtracted term in (9.2) is nonnegative, (9.2) forces

\[
 \boxed{X^T(e_j-e_i)=0}
 \tag{9.3}
\]

on every nonadjacent Wave edge.  For `n>=4`, the graph containing all pairs
with `|i-j|>=2` is connected.  Therefore every row of `X` must be equal.
Such a constant-row coupling can see only the telescoping total channel
`sum_i f_i`; it cannot provide a nonconstant rank-dependent coupling on the
zero-slack Wave cells.

The `n=4` fixture makes the failure explicit.  Taking scalar cross rows
`X=(0,1,2,3)^T` and `D=1`, the zero-slack root `(4,6)` has Schur value `-4`.

To obtain nonconstant cross-coupling one must add positive edge slack, use
extra actual-cell structure, or pass to a larger signed/cross-epoch master.
For singular `D`, the corresponding range and pseudoinverse conditions do
not remove the zero-slack requirement.

## 10. Exact replay and remaining target

The companion artifacts are:

- `ordered_gram_ramp_master_certificate.py`;
- `ordered_gram_ramp_master_certificate.json`;
- `test_ordered_gram_ramp_master_certificate.py`.

They certify with exact integer and rational arithmetic:

1. 2,700 local full-gap overlap rows;
2. the `n=4` Gram, residual, Wave, ramp, Schur, inertia, and zero-slack data;
3. the `n=5` Golomb active triangle;
4. the small-scale divergence coefficient and active gate;
5. the signed-band cone-loss fixture;
6. semantic and byte-exact JSON replay; and
7. twelve rejected semantic/hash mutations.

The payload hash covers all top-level semantic fields except `integrity`.
No source hash is embedded, so there is no source/hash self-reference.

The surviving Route C target is now precise: insert the actual labeled
root-cell Gram restriction into a legal active-scale common master, or build
a signed/cross-epoch/larger master that pays the ramp's diagonal, adjacent,
and two terminal contributions without double ownership.  Until that step is
proved, Route C, C058, and Erdős Problem #1191 remain unresolved.

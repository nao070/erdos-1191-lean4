# Route C: exact diagonal price of the active dipole coefficient matrix

Date: 2026-08-30  
Status: `EXACT_COEFFICIENT_PSD_PRICE_AND_SAME_EPOCH_CAPACITY_COUNTERFIXTURE`

This note computes the least diagonal energy needed to make the Wave-19
rank-dipole coefficient matrix positive semidefinite at each box scale.  It
also gives an eight-mark Golomb prefix on which the already-owned positive
finite-horizon Gothic capacity is smaller than that least price.  The result
rules out only paying a **coefficient-PSD diagonal lift** from that positive
same-epoch capacity alone.  It does not rule out a Gram-restricted argument,
signed cancellation, a cross-epoch payment, a different larger master, or
either question in Erdős Problem #1191.

## 1. Active coefficient matrix and the relevant notion of price

Use the conventions of the cross-ratio box-dipole bridge.  Thus

\[
 f_{i,T}=e_i*K_T,
 \qquad
 g_i(T)=\|f_{i,T}\|_2^2
 ={2\min(h_i,T)\over T^2},
 \tag{1.1}
\]

and, for a Wave edge `i<j`,

\[
 \langle f_{i,T},f_{j,T}\rangle=-\psi_{ij}(T).
 \tag{1.2}
\]

The edge is active precisely when

\[
 E_n(T)\ni(i,j)
 \quad\Longleftrightarrow\quad
 n\le i\le j-2,\quad j\le2n-1,
 \quad M_{ij}<T<D_{ij},
 \tag{1.3}
\]

where `M_(ij)=D_(i+1,j-1)`.  Outside this interval the inner product in
(1.2) is exactly zero.  Put

\[
 \alpha_{ij}={(j-i)^2\over4n^2},
 \qquad
 (B_T)_{ij}=(B_T)_{ji}=-{\alpha_{ij}\over2}
 \quad((i,j)\in E_n(T)),
 \tag{1.4}
\]

with every other entry, including the diagonal, zero.  If `G_T` is the Gram
matrix of the `f_(i,T)`, then

\[
 Q_n(T)=\langle B_T,G_T\rangle.
 \tag{1.5}
\]

There need not be a componentwise least diagonal completion.  The scalar
quantity relevant to the actual energy is instead

\[
 P_n(T):=\min\left\{
   \sum_i g_i(T)d_i:
   \operatorname{diag}(d)+B_T\succeq0
 \right\}.
 \tag{1.6}
\]

This is the least diagonal energy in a coefficient-PSD representation

\[
 Q_n(T)
 =\langle \operatorname{diag}(d)+B_T,G_T\rangle
  -\sum_i d_i g_i(T).
 \tag{1.7}
\]

This notion is deliberately stronger than positivity only after contraction
with the particular `G_T`.  The latter needs no completion because
`Q_n(T)>=0` is already known.  The stronger notion is the one required if the
rank channels are to enter a common coefficient-PSD smoothing master.

## 2. Exact minimum

For every active edge set, not only for a tree or a bipartite graph,

\[
 \boxed{
 P_n(T)=\sum_{(i,j)\in E_n(T)}
          \alpha_{ij}\sqrt{g_i(T)g_j(T)}.}
 \tag{2.1}
\]

Indeed, one feasible optimizer is

\[
 d_i^*(T)={1\over2\sqrt{g_i(T)}}
    \sum_{j:(i,j)\in E_n(T)}\alpha_{ij}\sqrt{g_j(T)}.
 \tag{2.2}
\]

For each edge, its contribution to
`diag(d^*)+B_T` is the positive semidefinite rank-one block

\[
 {\alpha_{ij}\over2}
 \begin{pmatrix}
  \sqrt{g_j/g_i}&-1\\
  -1&\sqrt{g_i/g_j}
 \end{pmatrix}.
 \tag{2.3}
\]

Summing (2.3) proves feasibility, and its weighted diagonal cost is the
right side of (2.1).  Conversely, the SDP dual of (1.6) is

\[
 \max\{-\langle B_T,X\rangle:
       X\succeq0,\ X_{ii}=g_i(T)\}.
 \tag{2.4}
\]

The rank-one matrix `X=vv^T`, `v_i=sqrt(g_i(T))`, is feasible and attains the
same value.  This proves (2.1) exactly.  Strong duality also follows directly
from a sufficiently large strictly positive diagonal.

There is a second possible sign convention.  If the desired statement is
the direct diagonal domination

\[
 \operatorname{diag}(d)-B_T\succeq0,
 \qquad Q_n(T)\le\sum_i d_i g_i(T),
 \tag{2.5}
\]

then its minimum is at most (2.1) and at least `Q_n(T)`.  It equals (2.1)
whenever the active graph is bipartite, by switching the sign of `v_i` on
one bipartition.  In particular, the two sign conventions have exactly the
same minimum for `n=4`, because the complete Wave graph then has only the
edges `(4,6),(4,7),(5,7)` and is bipartite.

## 3. The exact price is at least twice the tent mass

Write `u=h_i`, `v=h_j`, and assume `u<=v`.  If
`s_(ij)(T)=T^2 psi_(ij)(T)`, the exact tent table is

\[
 s_{ij}(T)=y,\ u,\ u+v-y
\]

on its three successive positive pieces, where `y=T-M_(ij)`.  On every
piece,

\[
 s_{ij}(T)
 \le \sqrt{\min(u,T)\min(v,T)}.
 \tag{3.1}
\]

Consequently

\[
 \sqrt{g_i(T)g_j(T)}
 ={2\sqrt{\min(u,T)\min(v,T)}\over T^2}
 \ge2\psi_{ij}(T).
 \tag{3.2}
\]

After summing the positive Wave coefficients,

\[
 \boxed{P_n(T)\ge2Q_n(T).}
 \tag{3.3}
\]

The active localization makes the price integrable.  Define

\[
 \Pi_n:=\int_0^\infty P_n(T)\,dT.
 \tag{3.4}
\]

Then the exact Wave identity gives the universal lower bound

\[
 \boxed{\Pi_n\ge2\mathcal W_n.}
 \tag{3.5}
\]

The integral also has a closed pairwise formula.  Set

\[
 J(M,u,v)=\int_M^{M+u+v}
 {2\sqrt{\min(u,T)\min(v,T)}\over T^2}\,dT.
 \tag{3.6}
\]

With `a=min(u,v)`, `b=max(u,v)`, and `D=M+u+v`, direct integration gives

\[
 J(M,u,v)=
 \begin{cases}
 2\sqrt{uv}(M^{-1}-D^{-1}),&M\ge b,\\[2mm]
 4\sqrt a(M^{-1/2}-b^{-1/2})
 +2\sqrt{ab}(b^{-1}-D^{-1}),&a\le M<b,\\[2mm]
 2\log(a/M)+4(1-\sqrt{a/b})
 +2\sqrt{ab}(b^{-1}-D^{-1}),&M<a.
 \end{cases}
 \tag{3.7}
\]

Thus

\[
 \boxed{
 \Pi_n=\sum_{n\le i\le j-2\atop j\le2n-1}
 \alpha_{ij}J(M_{ij},h_i,h_j).}
 \tag{3.8}
\]

Both sides are dilation invariant.  There is no universal reverse estimate
`J<=K C` with an absolute `K`.  If `M>=max(u,v)`, then

\[
 J={2\sqrt{uv}(u+v)\over MD},
 \qquad
 C=\log\left(1+{uv\over MD}\right)\le {uv\over MD},
 \tag{3.9}
\]

so

\[
 {J\over C}\ge {2(u+v)\over\sqrt{uv}},
 \tag{3.10}
\]

which is unbounded as `u/v` varies.

It is essential to use the active graph.  If every Wave edge in (1.4) is
retained at all `T`, then for `T<min_i h_i` one has `g_i(T)=2/T`, and (2.1)
is a positive constant times `1/T`.  Its integral at zero diverges.  Exact
zeroing of the inactive cross inner products is therefore not cosmetic; it
is necessary for a finite coefficient-PSD price.

## 4. A Golomb prefix whose positive Gothic capacity cannot pay the price

Take `n=4` and the integer prefix

\[
 A=(0,101,204,309,416,525,636,749).
 \tag{4.1}
\]

Its 28 positive differences, in increasing order, are

\[
\begin{split}
&101,103,105,107,109,111,113,204,208,212,216,220,224,\\
&309,315,321,327,333,416,424,432,440,525,535,545,636,648,749.
\end{split}
\tag{4.2}
\]

They are distinct, so (4.1) is a Golomb ruler.  Its current gaps are

\[
 (h_4,h_5,h_6,h_7)=(107,109,111,113),
 \qquad H=D_{4,7}=440.
 \tag{4.3}
\]

The exact Wave mass is

\[
 \mathcal W_4={1\over16}\log{15840\over11881}
 +{1\over16}\log{49280\over36963}
 +{9\over64}\log{108891\over96800}.
 \tag{4.4}
\]

The entire positive strict-interior finite-horizon Gothic capacity from
the box-dipole bridge is

\[
 \begin{aligned}
 \mathcal G_4
 :={}&{1\over16}F_{440}(109)
      +{1\over64}F_{440}(220)
      +{1\over16}F_{440}(111)\\
 ={}&{1\over16}\log{193600\over12099}
     +{1\over64}\log2-{13\over128}.
 \end{aligned}
 \tag{4.5}
\]

The strict inequality `G_4<2 W_4` can be checked without decimal
approximations.  For `x>1`, let `z=(x-1)/(x+1)`.  The positive atanh series
gives

\[
 2z<\log x
 <2\left(z+{z^3\over3(1-z^2)}\right).
 \tag{4.6}
\]

Applying the lower bound to the three logarithms in (4.4), and the upper
bound to `log(440/109)`, `log 2`, and `log(440/111)` after expanding the
three `F`-terms in the first line of (4.5), gives the exact rational bounds

\[
 \mathcal W_4>
 {822003631010073\over15736132943272736},
 \qquad
 \mathcal G_4<
 {81908500355\over936943462656}.
 \tag{4.7}
\]

Their separated margin is

\[
 2\,{822003631010073\over15736132943272736}
 -{81908500355\over936943462656}
 ={413517772924972663409287
   \over24249781066916299488221952}>0.
 \tag{4.8}
\]

Combining (3.5) and (4.8) proves

\[
 \boxed{\mathcal G_4<2\mathcal W_4\le\Pi_4.}
 \tag{4.9}
\]

For reference, the exact diagonal price itself is

\[
 \Pi_4={J(109,107,111)+J(111,109,113)\over16}
       +{9\over64}J(220,107,113),
 \tag{4.10}
\]

where (3.7) applies; numerically it is about `0.236905`, while
`G_4` is about `0.082560`.  The proof of (4.9) uses only the exact rational
separation (4.8), not these decimals.

## 5. Scope of the obstruction

Equation (4.9) proves that the positive `lambda=beta` finite-horizon capacity
in (4.5) of the box-dipole bridge cannot, by itself and at the same epoch,
pay the least diagonal cost of turning the active rank-dipole coefficient
matrix into a PSD coefficient matrix.  This remains true at `n=4` under the
direct-domination sign convention (2.5), because the active graph is
bipartite there.

This is not a contradiction to `Q_n(T)>=0`: that positivity uses the special
ordered box-dipole Gram geometry.  Nor does it prove that Route C fails.  A
surviving proof may still:

- keep the actual Gram restriction instead of demanding coefficient PSD;
- cancel the diagonal term against a separately owned negative term inside
  one signed master;
- use the nonpositive Gothic boundary coefficients rather than dropping
  them;
- transport ownership between epochs or phases with every boundary row kept;
- find a different PSD lift whose channels include more of the existing
  master than the isolated rank-dipole block.

The raw dilation-dependent Gothic value `sum beta log D` is not compared as
if it were a fresh reserve: the finite-horizon `F_H` rewrite is the relevant
dilation-invariant positive sector, and the original Gothic atoms are already
owned elsewhere.  No Question 1, Question 2, complete-proof, novelty,
publication, or prize conclusion follows.

## 6. Exact certificate

The companion files

- `dipole_psd_price_certificate.py`,
- `dipole_psd_price_certificate.json`, and
- `test_dipole_psd_price_certificate.py`

lock the primal/dual factor on a rational weighted graph, reject factor-two
and sign changes through exact edge blocks, verify the pointwise squared
price margins, replay all 28 differences of (4.1), and reproduce the exact
atanh separation in (4.7)--(4.8).  The focused suite passes 10 tests,
deterministic semantic/byte replay, and eight mutation rejections.  Payload
SHA-256:

`76fcc06eb5d1edcda2c1fd51c93122bdb558eb545bd90006627d42dcea107327`.

The universal SDP identity and integral formulas remain human-proof audited;
the certificate does not replace their quantified derivation with finite
sampling.  Its scope flags preserve every Gram-restricted, signed,
cross-epoch, and larger-master escape, and keep C058, both Erdős questions,
and every prize claim false.

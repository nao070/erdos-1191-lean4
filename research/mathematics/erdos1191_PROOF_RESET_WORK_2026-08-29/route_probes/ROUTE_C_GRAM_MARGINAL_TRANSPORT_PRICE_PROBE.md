# Route C: ordered-dipole Gram strips and the marginal transport price

Date: 2026-08-30  
Status: `EXACT_GRAM_STRIP_COUPLING_MARGINAL_ONLY_PAYMENT_COUNTERFIXTURE`

This note retains more of the actual one-dimensional box-dipole Gram
geometry than the coefficient-PSD completion.  The gap dipoles split into
two disjoint interval families, so their negative off-diagonal Gram entries
form a literal bipartite overlap transport.  The sharp upper price obtainable
from only the row and column strip masses is therefore a fractional
vertex-cover LP, not the SDP price.  An exact eight-mark Golomb prefix shows
that even this cheaper marginal-only price is larger than the positive
same-epoch finite-horizon Gothic budget.

The conclusion is deliberately narrow.  It does not rule out using the
exact intersection coupling, the nonpositive Gothic rows, signed or
cross-epoch cancellation, a larger master, C058, either question in Erdős
Problem #1191, publication novelty, or a prize claim.

## 1. Exact ordered-strip decomposition

Fix an ordered mark sequence and a gap

\[
 h_i=a_i-a_{i-1}>0.
\]

For `T>0`, put `m_i=min(h_i,T)` and use half-open intervals

\[
 L_i=[a_{i-1},a_{i-1}+m_i),\qquad
 R_i=[a_i+T-m_i,a_i+T).
 \tag{1.1}
\]

For the oriented gap dipole `e_i=delta_(a_(i-1))-delta_(a_i)` and
`K_T=T^-1 1_[0,T)`, direct cancellation gives

\[
 \boxed{e_i*K_T=T^{-1}(1_{L_i}-1_{R_i}).}
 \tag{1.2}
\]

Every `L_i` lies in its own gap, so the `L` family is pairwise disjoint.
The right endpoints obey

\[
 \inf R_{i+1}=\max(a_{i+1},a_i+T)\ge \sup R_i,
\]

so the `R` family is also pairwise disjoint.  If `i<j`, then
`L_i` lies strictly before `R_j`; hence the only possible cross overlap is
`R_i intersect L_j`.  Consequently

\[
 \boxed{
 \langle e_i*K_T,e_j*K_T\rangle
 =-{|R_i\cap L_j|\over T^2}\le0\quad(i<j),}
 \tag{1.3}
\]

and

\[
 {|R_i|\over T^2}={|L_i|\over T^2}
 ={\min(h_i,T)\over T^2}={g_i(T)\over2}.
 \tag{1.4}
\]

For a Wave edge `(i,j)`, the overlap length in (1.3) is exactly the tent
numerator in the box-dipole bridge.  Thus

\[
 \psi_{ij}(T)={|R_i\cap L_j|\over T^2}.
 \tag{1.5}
\]

This proves more than scalar nonnegativity: at almost every spatial point
there is at most one active right strip and at most one active left strip.

## 2. The sharp price using only strip marginals

Let `E_n(T)` be the active Wave graph and

\[
 \mu_i(T)={g_i(T)\over2},\qquad
 \nu_j(T)={g_j(T)\over2}.
\]

Define the fractional vertex-cover price

\[
 \begin{aligned}
 V_n(T):=\min\{&\sum_i\mu_i(T)p_i+\sum_j\nu_j(T)q_j:\\
 &p_i,q_j\ge0,\quad p_i+q_j\ge\alpha_{ij}
 \text{ for }(i,j)\in E_n(T)\}.
 \end{aligned}
 \tag{2.1}
\]

At a point in `R_i intersect L_j`, the cover constraint gives

\[
 \alpha_{ij}\le p_i+q_j.
\]

The within-family disjointness then yields

\[
 \boxed{Q_n(T)\le V_n(T).}
 \tag{2.2}
\]

This is sharp among all certificates using only the complete row and column
strip masses.  Finite LP duality gives

\[
 \boxed{
 V_n(T)=\max\left\{
 \sum_{(i,j)\in E_n(T)}\alpha_{ij}y_{ij}:
 y_{ij}\ge0,
 \sum_jy_{ij}\le\mu_i(T),
 \sum_iy_{ij}\le\nu_j(T)
 \right\}.}
 \tag{2.3}
\]

The actual overlap masses

\[
 y_{ij}^{\rm actual}={|R_i\cap L_j|\over T^2}
\]

are dual feasible, which is another proof of (2.2).  Equality need not hold:
the marginal LP forgets exactly where the strips lie.

The price is always no larger than half the coefficient-PSD price from C069.
For every active edge, add to the cover potentials

\[
 p_i^{ij}={\alpha_{ij}\over2}\sqrt{g_j/g_i},\qquad
 q_j^{ij}={\alpha_{ij}\over2}\sqrt{g_i/g_j}.
\]

Their sum is at least `alpha_(i,j)` by AM--GM.  After summing over edges,
their marginal cost is

\[
 {1\over2}\sum_{(i,j)\in E_n(T)}
 \alpha_{ij}\sqrt{g_i(T)g_j(T)}={P_n^{\rm PSD}(T)\over2}.
\]

Therefore the exact hierarchy is

\[
 \boxed{Q_n(T)\le V_n(T)\le {P_n^{\rm PSD}(T)\over2}.}
 \tag{2.4}
\]

Unlike coefficient PSD, (2.1) uses the disjoint left/right Gram geometry.
Unlike the exact overlap coupling, it still discards spatial placement.

## 3. Exact marginal price on the eight-mark fixture

Use the same `n=4` Golomb prefix as C070:

\[
 A=(0,101,204,309,416,525,636,749).
 \tag{3.1}
\]

Its current gaps are `(107,109,111,113)`.  The three Wave edges are

\[
 (4,6):\ (M,D,\alpha)=(109,327,1/16),
\]

\[
 (4,7):\ (M,D,\alpha)=(220,440,9/64),
\]

\[
 (5,7):\ (M,D,\alpha)=(111,333,1/16).
 \tag{3.2}
\]

On each open interval between active-edge breakpoints, the following
primal/dual witnesses give the exact value of (2.1):

\[
\begin{array}{c|c|c|c}
T\text{ interval}&\text{active edges}&\text{nonzero cover}&T^2V_4(T)\\ \hline
(109,111)&46&p_4=1/16&107/16\\
(111,220)&46,57&p_4=p_5=1/16&216/16\\
(220,327)&46,47,57&p_4=5/64,\ q_7=1/16&987/64\\
(327,333)&47,57&p_4=5/64,\ q_7=1/16&987/64\\
(333,440)&47&p_4=9/64&963/64.
\end{array}
 \tag{3.3}
\]

For the first two rows, matching transport loads are respectively `y_46=107`
and `(y_46,y_57)=(107,109)`, all divided by `T^2`.  For the middle two rows,
take `(y_47,y_57)=(107,6)/T^2`; for the last, take `y_47=107/T^2`.
They meet every row and column capacity and have the displayed primal value,
so (3.3) is exact by LP duality.

Integrating gives the rational number

\[
 \begin{aligned}
 \mathcal V_4:=\int_0^\infty V_4(T)dT
={}&{107\over16}\left({1\over109}-{1\over111}\right)\\
&+{216\over16}\left({1\over111}-{1\over220}\right)\\
&+{987\over64}\left({1\over220}-{1\over333}\right)\\
&+{963\over64}\left({1\over333}-{1\over440}\right)\\
={}&\boxed{{32755417\over340707840}}.
 \end{aligned}
 \tag{3.4}
\]

## 4. The positive same-epoch sector is still too small

The positive strict-interior finite-horizon Gothic capacity on (3.1) is

\[
 \mathcal G_4={1\over16}F_{440}(109)
 +{1\over64}F_{440}(220)+{1\over16}F_{440}(111).
 \tag{4.1}
\]

The exact atanh upper bound already used in the C070 certificate gives

\[
 \mathcal G_4< {81908500355\over936943462656}.
 \tag{4.2}
\]

Comparison with (3.4) is separated by

\[
 {32755417\over340707840}
 -{81908500355\over936943462656}
 =\boxed{{898545848033\over103063780892160}}>0.
 \tag{4.3}
\]

Hence

\[
 \boxed{\mathcal G_4<\mathcal V_4.}
 \tag{4.4}
\]

This strengthens the payment obstruction: the same positive sector cannot
pay even the least pointwise cover which remembers the disjoint left/right
strip marginals.  The exact Wave mass itself is smaller than
`mathcal G_4`; the loss occurs because (2.1) replaces the actual intersection
pattern by every coupling compatible with the marginals.

## 5. Surviving interface and replay

The surviving actual-Gram route must use more than coefficient PSD and more
than row/column strip masses.  It must retain the exact monotone intersection
coupling `|R_i intersect L_j|`, or combine it with nonpositive Gothic rows,
signed cross-epoch/cross-phase cancellation, or a larger master.  It must
still rewrite rather than duplicate the Gothic `beta` ownership and keep all
finite terminals.

From `route_probes/`, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_gram_marginal_transport_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 gram_marginal_transport_certificate.py \
  --verify gram_marginal_transport_certificate.json --self-check
```

The certificate verifies the strip identity on 2,700 local integer rows,
the five exact primal/dual LP stages, the integrated rational price, byte
replay, and eight adversarial mutations.  It certifies the finite fixture,
not the universal theorem by itself; the universal strip/LP argument above
is a human-readable proof.

# Endpoint-Imbalance Theorem for Offset-Energy Variance

**Status:** exact finite theorem, independently machine-checked.  This is an
endpoint-sensitive extension of the all-offset identity already present in the
workspace.  It does **not** solve Erdős problem #1191; it isolates a quartic
quantity that escapes the previously certified quadratic/difference-spectrum
barrier.

## 1. Definitions

Let \(A\subset\mathbb Z\) be finite and let \(N\ge2\).  Write
\[
P_N(A)=\{(a,b)\in A^2:a<b,\ b-a<N\}.
\]
For an offset \(r\in\mathbb Z/N\mathbb Z\), let \(E_N(r)\) be the number of
pairs in \(P_N(A)\) whose endpoints lie in the same interval of the translated
partition
\[
[r+jN,r+(j+1)N),\qquad j\in\mathbb Z.
\]
Let \(C_N(r)=|P_N(A)|-E_N(r)\).  Equivalently, a pair \(a<b\) contributes to
\(C_N(r)\) exactly when a partition boundary of phase \(r\) lies in
\((a,b]\).  Its bad-offset set is therefore the cyclic integer arc
\[
B_{a,b}=\{a+1,a+2,\ldots,b\}\pmod N,
\]
of cardinality \(b-a\).

Form the directed short-pair residue multigraph \(G_N(A)\) on
\(\mathbb Z/N\mathbb Z\), with one edge
\[
a\pmod N\longrightarrow b\pmod N
\]
for every \((a,b)\in P_N(A)\).  Define its endpoint imbalance
\[
\delta_N(r)=\operatorname{outdeg}_{G_N(A)}(r)-
             \operatorname{indeg}_{G_N(A)}(r).
\]

## 2. Exact identities

### Proposition 2.1 (boundary-arc identity)
For every \(r\),
\[
E_N(r)+C_N(r)=|P_N(A)|,
\]
and
\[
\sum_{r\bmod N} C_N(r)=
\sum_{(a,b)\in P_N(A)}(b-a),
\qquad
\sum_{r\bmod N} E_N(r)=
\sum_{(a,b)\in P_N(A)}(N-b+a).
\]

**Proof.**  The first equality is the dichotomy “same block / cut by a
boundary.”  The pair \((a,b)\) is cut for exactly the \(b-a\) phases in
\(B_{a,b}\), and is uncut for the remaining \(N-(b-a)\) phases.  Summing over
pairs gives both formulas. \(\square\)

### Theorem 2.2 (endpoint-imbalance reconstruction)
The cyclic forward difference of the boundary load is exactly the endpoint
imbalance:
\[
C_N(r+1)-C_N(r)=\delta_N(r).
\]
Consequently, if
\[
S_N(0)=0,\qquad S_N(r)=\sum_{j=0}^{r-1}\delta_N(j)
\quad(1\le r<N),
\]
then \(C_N-S_N\) is constant and
\[
\boxed{\quad
\operatorname{Var}_{r\bmod N}E_N(r)
=
\operatorname{Var}_{r\bmod N}C_N(r)
=
\frac1N\sum_{r=0}^{N-1}(S_N(r)-\overline S_N)^2.
\quad}
\]
Thus the variance is determined by the *placement of pair endpoints* modulo
\(N\), not merely by the multiplicities of their differences.

**Proof.**  The indicator of \(B_{a,b}\) rises by one when \(r\) passes
\(a\pmod N\), falls by one when it passes \(b\pmod N\), and is unchanged at
all other residues.  Summing these derivatives over all short pairs gives
outdegree minus indegree.  Two cyclic functions with the same forward
difference differ by a constant.  Variance is invariant under adding a
constant and under replacing \(C_N\) by \(|P_N(A)|-C_N\). \(\square\)

With the unnormalised Fourier transform
\(\widehat\delta(k)=\sum_r\delta(r)e^{-2\pi i kr/N}\), the same theorem is
\[
\operatorname{Var}E_N
=
\frac1{N^2}\sum_{k=1}^{N-1}
\frac{|\widehat\delta_N(k)|^2}{4\sin^2(\pi k/N)}.
\]
This is the squared cyclic \(H^{-1}\)-norm of the endpoint imbalance.

### Corollary 2.3 (Eulerian zero modes)
The following are equivalent:

1. \(\operatorname{Var}_{r\bmod N}E_N(r)=0\);
2. \(\delta_N(r)=0\) for every residue \(r\);
3. \(G_N(A)\) is balanced at every vertex;
4. all short-pair edges can be decomposed into directed cycles.

Here “Eulerian” means balanced component by component.  Neither connectivity
nor the existence of one global Euler tour is required.

If \(A\) is Sidon, every edge in these cycles has a distinct positive length
below \(N\), and the sum of the edge lengths around each cycle is a positive
multiple of \(N\).

The family \(A=\{0,1,N\}\) is the smallest nontrivial exact zero mode with a
nonempty short-edge graph: the two short edges have lengths \(1\) and \(N-1\)
and form the residue cycle
\(0\to1\to0\).  Hence a positive variance lower bound cannot hold at every
scale without an additional density-sensitive or cross-scale hypothesis.

### Corollary 2.4 (quantitative lower bounds)
Parseval and \(4\sin^2(\pi k/N)\le4\) give
\[
\boxed{\quad
\operatorname{Var}E_N
\ge \frac1{4N}\sum_{r\bmod N}\delta_N(r)^2.
\quad}
\]
Since \(C_N(r)\) is integer-valued, any nonconstant offset vector also obeys
\[
\operatorname{Var}E_N\ge\frac{N-1}{N^2}.
\]
If
\(q\equiv\sum_{(a,b)\in P_N(A)}(b-a)\pmod N\), \(0\le q<N\), then the fixed
mean and integrality alone imply the sharper spectrum-only floor
\[
\operatorname{Var}E_N\ge\frac{q(N-q)}{N^2}.
\]
The endpoint-imbalance formula generally gives much more information than
this final bound.

## 3. Complete-prefix diameter regime

There is a useful quantitative specialization.  Let
\(A=\{a_1<\cdots<a_m\}\) have diameter \(D=a_m-a_1<N\), and put
\(g_k=a_{k+1}-a_k\) for \(1\le k<m\).  The outside cyclic gap has length
\(N-D\).  A boundary in the gap \((a_k,a_{k+1}]\) separates exactly the first
\(k\) points from the final \(m-k\), so
\[
C_N(r)=k(m-k)
\]
for precisely \(g_k\) offsets, and \(C_N(r)=0\) on the remaining \(N-D\)
offsets.  Therefore
\[
\boxed{\quad
\operatorname{Var}E_N
=\frac1N\sum_{k=1}^{m-1}g_k k^2(m-k)^2
-\left(\frac1N\sum_{k=1}^{m-1}g_k k(m-k)\right)^2.
\quad}
\]

In this regime the residue vertices are distinct and every pair is short.  At
the vertex \(a_i\pmod N\),
\[
\delta_N(a_i)=m+1-2i.
\]
Consequently
\[
\sum_{r\bmod N}\delta_N(r)^2
=\sum_{i=1}^m(m+1-2i)^2
=\frac{m(m^2-1)}3,
\]
and Corollary 2.4 yields the universal cubic lower bound
\[
\boxed{\quad
\operatorname{Var}E_N\ge\frac{m(m^2-1)}{12N}.
\quad}
\]
Taking \(N=D+1\) shows that any sequence of prefixes with
\(D_m\ll m^2\log m\) has endpoint variance at least of order
\(m/\log m\), hence diverging.  This is a genuine quantitative gain over the
mere nonzero-variance statement.  It is not yet a proof of #1191 because a
matching Sidon upper budget for a summable multiscale combination of these
quartic prefix variances is still missing.

### Theorem 3.1 (sharp mandatory-level lower bound)

The gap formula contains more information than the generic Poincaré estimate.
Each internal integer gap is nonempty, and the outside gap is nonempty, so the
\(N\)-entry load vector contains the following indexed mandatory multiset
\[
x_k=k(m-k),\qquad 0\le k<m.
\]
The entries indexed by \(k\) are mandatory even when the symmetric values
\(x_k=x_{m-k}\) coincide numerically.
For any real centre \(c\), dropping the other nonnegative squared deviations
gives
\[
N\operatorname{Var}C_N
=\min_c\sum_{r\bmod N}(C_N(r)-c)^2
\ge \min_c\sum_{k=0}^{m-1}(x_k-c)^2.
\]
Now
\[
\sum_{k=0}^{m-1}x_k=\frac{m(m^2-1)}6,
\qquad
\sum_{k=0}^{m-1}x_k^2=\frac{m^5-m}{30},
\]
so the centred sum is
\[
\frac{m(m^2-1)(m^2+11)}{180}.
\]
Hence
\[
\boxed{\quad
\operatorname{Var}E_N
\ge
\frac{m(m^2-1)(m^2+11)}{180N}.
\quad}
\]
Equality holds exactly when every additional load entry equals the mandatory
mean \((m^2-1)/6\).  The bound is sharp over unrestricted finite sets: for
\(A=\{0,1,\ldots,m-1\}\) and \(N=m\), every indexed mandatory entry occurs
exactly once.  This example is non-Sidon for \(m\ge3\), so sharpness within
the Sidon class remains open.  For a hypothetically critical dense prefix with
\(N\asymp m^2\log m\), the new lower bound is of order
\(m^3/\log m\), two powers of \(m\) stronger than the first-difference
Poincaré bound.

The gain does not by itself close #1191: the pointwise range
\(0\le C_N(r)\le m^2/4\) still permits variance of order \(m^4\).  What the
theorem supplies is a large, unavoidable endpoint-sensitive signal that a
future cross-prefix or cross-scale Sidon budget would need to control.

## 4. Certified homometric separation

Consider the two six-mark Sidon rulers
\[
A=\{0,1,4,10,12,17\},\qquad
A'=\{0,1,8,11,13,17\}.
\]
Both have the identical positive-difference spectrum
\[
\{1,2,3,4,5,6,7,8,9,10,11,12,13,16,17\}.
\]
Hence every statistic that is a function only of \(r_A(d)\) gives the same
answer for the two sets.  At \(N=14\), however,
\[
\operatorname{Var}E_{14}(A)=\frac{79}{28},\qquad
\operatorname{Var}E_{14}(A')=\frac{55}{28},
\]
so the gap is exactly \(6/7\).  The imbalance vectors are
\[
\delta_A=(4,2,0,-3,1,0,0,0,0,0,-1,0,-3,0),
\]
\[
\delta_{A'}=(4,2,0,-3,0,0,0,0,1,0,0,-1,0,-3).
\]
They have the same multiset of entries and the same \(\ell^2\)-norm, but their
cyclic placement differs; the \(H^{-1}\)-energy detects that placement.

This is a rigorous separation theorem: fully translation-averaged quadratic
statistics collapse to the difference spectrum, whereas the variance of the
offset-energy vector is quartic and retains endpoint-incidence information.

## 5. Consequence for the #1191 strategy

The previous workspace barrier remains valid for separable nonnegative scale
mixtures of *means*.  The theorem above identifies the first exact quantity in
this line of attack that is not subject to that barrier.  It also exposes the
new obstruction precisely: balanced residue graphs are genuine zero modes.

A useful next lemma must therefore be **multiscale and anti-Eulerian**.  One
concrete target is to prove that a Sidon sequence satisfying a uniform
critical-density lower bound cannot have balanced, or nearly balanced,
short-pair residue graphs at too many nested scales.  In the notation above,
one needs a density-sensitive lower bound for a weighted sum of
\[
\|\delta_N\|_{H^{-1}(\mathbb Z/N\mathbb Z)}^2
=
\operatorname{Var}E_N,
\]
not a separate lower bound at each \(N\).  The two-cycle example rules out the
latter; it does not rule out a cross-scale theorem.

The exact directed-cycle characterization narrows the combinatorial problem:
near-zero variance means that almost all short-pair edges can be arranged into
residue cycles whose distinct lengths sum to multiples of \(N\).  Quantifying
how often such cycle packings can occur for nested moduli is the next
well-posed research subproblem.

# Independent review of the actual shadow threshold graph

Date: 2026-09-05. Reviewer: `/root/c143_mathematics`, GPT-6 Astra Ultra.
Ownership: this review only; the parent's source was read without editing.

**Result:** the complete four-section source `retirement_shadow_threshold.md`,
including its equations (1)--(6), is supported. The later positive-injection
claim sent by the parent is also correct, with the one-sided qualification
proved below. The review gives exact global orbit counts, an orbit-square
identity, and explicit remaining signed terms. No numerical experiment or
Lean verification is asserted. Original Q1 remains unresolved.

## 1. Literal endpoint checks

Use the source notation \(P=\{a_1<\cdots<a_N\}\), \(F=\Delta P\),
\(q=\binom N2\), and \(H=a_N-a_1>0\). For an active resource at
position \(x\), write uniquely
\[
 d_i=x-a_i=a_j-a_h>0,\qquad h<j.
\]
Then \(a_i+a_j=x+a_h\). The following equivalences are useful:
\[
 a_j<x\iff a_h<a_i\iff h<i,
 \qquad a_j\ge x\iff i\le h.                     \tag{R1}
\]
In the first case \(x-a_j=a_i-a_h>0\), with source upper endpoint
\(i\), so the partner is indeed an active resource. Difference
uniqueness makes the partner assignment involutive. Its partner also
satisfies the first case of (R1). A fixed point has \(j=i\) and
\(x=2a_i-a_h\), with \(h<i\).

In the second case, every active resource rank \(k\) satisfies
\(a_k<x\le a_j\), so \(k<j\). The output difference of its pair
with any other active resource has upper rank at most
\(\max(i,k)<j\). Such a pair cannot retire. This proves the full
absence of retirement edges incident to unpaired vertices, rather
than just their absence from one ordered construction.

For any distinct active \(i,k\), the two label values differ by
\(|a_i-a_k|\), whose actual upper endpoint rank is \(\max(i,k)\).
Thus the source's born-edge test (1) is exact, including equality.
On paired resources the two source ranks are \(\sigma(i),\sigma(k)\).
If a two-point orbit \(\{i,j\}\), \(i<j\), is later than an
earlier orbit, every rank in that earlier orbit is below \(j\).
The low resource \(i\) has source rank \(j\), making its edge born;
the high resource \(j\) has source rank \(i\), making its edge retire.
The internal edge has output rank \(j\) and a source of rank \(j\),
so it is born. A fixed point has identical resource and source rank,
and its edges to earlier orbits are born.

Here “a fixed point adds an isolated vertex” means isolated from the
earlier constructed vertices. A later high resource may retire against
that fixed point. The source states this distinction correctly.

At \(x\in P\), sum uniqueness in \(a_i+a_j=x+a_h\) forces
\(a_j=x,a_i=a_h\): the other matching of summands would require
\(j=h\). Hence all active labels belong to the one birth class with
upper endpoint \(x\), and there are no retirements. At \(x>a_N\),
there are no unpaired vertices. These special cases are consistent
with the general argument.

## 2. Weighted equations and the unique physical position

Each retiring label pair has a unique position, not multiple copies.
Indeed, for \(d<e\), write its positive output as
\(e-d=a_k-a_i\), \(i<k\). The only possible overlap position is
\(x=a_k+d=a_i+e\). Difference injectivity gives uniqueness of
\((i,k)\), hence of \(x\). The same uniqueness holds for a born
pair whose difference lies in \(F\).

Consequently, if \(v_i=z_{x-a_i}\) and \(T_{<O}\) includes all
earlier paired orbits and their fixed points, each retirement is
counted once in
\(R_x(z)=\sum_{\{i,j\},i<j}v_jT_{<\{i,j\}}\).
There is no factor two. The symmetric adjacency quadratic form has
twice this value, as the source explicitly says.

For the birth-linear vector, \(z_{a_j-a_h}=(m_j-a_h)/H\),
the means \(m_j\) are strictly increasing for \(j\ge2\), because
\[
 m_{j+1}-m_j=(a_j-m_j)/j>0.
\]
Each two-point orbit has \(h<i<j\), so both means are defined and
\(v_i-v_j=(m_j-m_i)/H=\delta_O>0\). The source's equation (5)
then follows from \(v_j=(w_O-\delta_O)/2\).

Lastly,
\(\sum_Ow_OT_{<O}=(V_x^2-\sum_Ow_O^2)/2\).
Separating the fixed-point terms proves the source's equation (6),
including the minus sign and factor \(1/2\) on both corrections.
No positivity of the signed prefix sums was used.

The source's example \(\{0,10,11,30\}\) at \(x=31\) is also
correct: the common lower endpoint is 10, the earlier means are 5
and 7, and the two weights are \(-3/30,-5/30\). Its difference
list is injective. It establishes coefficient negativity only.

## 3. Exact global counts and the orbit-square budget

The position representation (R1) gives three disjoint bijections:

* Two-point orbits over all positions correspond to triples
  \(h<i<j\), at \(x=a_i+a_j-a_h\). Their number is \(\binom N3\).
* Fixed points correspond to pairs \(h<i\), at \(x=2a_i-a_h\).
  Their number is \(q\), and their squared coefficients sum exactly
  to \(S=\sum_{d\in F}z_d^2\).
* Unpaired resources correspond to triples \(i\le h<j\).
  Their number is \(\sum_{h<j}h=\binom{N+1}3\).

Different triples may have the same position; they still specify
different resource or orbit incidences. Conversely every such incidence
has unique endpoint labels, so no multiplicity is omitted. The total
resource count is accordingly
\(2\binom N3+q+\binom{N+1}3=Nq\), as it must be.

Write \(z_{jh}=z_{a_j-a_h}\). For any real vector \(z\), not only
the linear one, the sum of squared orbit totals has the exact formula
\[
 Q_{\rm orb}:=\sum_x\sum_{O\text{ paired at }x}w_O^2
 =\sum_{h=1}^{N-1}\left[
    (N-h-1)\sum_{j>h}z_{jh}^2
       +\left(\sum_{j>h}z_{jh}\right)^2\right].     \tag{R2}
\]
To check it, each fixed point contributes \(z_{jh}^2\); each
two-point orbit \(h<i<j\) contributes \((z_{ih}+z_{jh})^2\).
A fixed label \((j,h)\) occurs in \(N-h-1\) two-point orbits.
The cross terms at fixed \(h\) equal
\((\sum_{j>h}z_{jh})^2-\sum_{j>h}z_{jh}^2\), cancelling the
fixed-point diagonal. This proves (R2) with every diagonal present.
Columnwise Cauchy--Schwarz gives
\[
 0\le Q_{\rm orb}\le2(N-1)S.                     \tag{R3}
\]

For the linear carrier, \(|z_d|\le1\) and \(S\le q\).
The entire fixed-point correction has the simple valid upper bound
\[
 \left|\sum_{x,O\text{ fixed}}w_OT_{<O}\right|\le Nq,        \tag{R4}
\]
since there are exactly \(q\) fixed incidences and at most \(N\)
earlier resources of absolute weight at most 1. Thus the orbit-square
term and fixed-point correction are both \(O(N^3)\). This is a
concrete simplification at the larger \(q^2/\log N\) scale.

## 4. The unpaired and signed-prefix terms still have to be retained

Let \(U_x\) be the sum on unpaired resources, \(V_x\) the paired
sum, and set
\[
 A_\delta=\sum_{x,O\text{ two-point}}\delta_OT_{<O},\qquad
 F_{\rm fix}=\sum_{x,O\text{ fixed}}w_OT_{<O}.
\]
The exact global consequences of the reviewed formula are
\[
 R_{\rm ret}(z)=\frac{\|V\|_2^2-Q_{\rm orb}}4
                  -\frac{A_\delta+F_{\rm fix}}2,
 \qquad E_P(z)=\|V+U\|_2^2.                       \tag{R5}
\]
Hence the historical improvement for the centered quadratic residual
\(W=J+zz^T/8\), against the same terminal raw future demand of
size \(m\), is exactly
\[
 I_m^{\rm hist}=\frac1{16}\left[
 \frac{E_P(z)}2+\langle V,U\rangle+\frac{\|U\|_2^2}2
 +\frac{Q_{\rm orb}}2+A_\delta+F_{\rm fix}
 -(N+m-1)S\right].                                \tag{R6}
\]
This is obtained by substituting (R5) into
\([E_P(z)-(N+m-1)S-2R_{\rm ret}(z)]/16\).

For reference, Cauchy--Schwarz at each position only gives
\[
 \|U\|_2^2\le N\sum_{h<j}h z_{jh}^2
                 \le N(N-1)S.                    \tag{R7}
\]
This can be order \(N^4\), so it does not justify discarding the
mixed term in (R6). The unpaired sum need not have a pointwise sign:
for the Sidon set \(\{0,1,4,10\}\), at \(x=9\) its sole active
resource is 0 with label \(10-1\), giving
\(U_9=(5/3-1)/10=1/15>0\); at \(x=6\) its sole active resource
is 0 with label \(10-4\), giving \(U_6=(5/3-4)/10=-7/30<0\).
The six positive differences are \(1,3,4,6,9,10\), all distinct.
Neither point is used as a counterexample to a summed estimate.

Equation (R6), together with (R3)--(R4), leaves a specific joint
obligation on \(A_\delta+\langle V,U\rangle+\|U\|_2^2/2\).
No estimate of the needed sign or scale for that joint quantity
under the complete fixed-onset cap is proved here.

## 5. The parent's positive one-sided scalar injection is valid

Fix the terminal normalization \(H\), and put
\(u_t(d)=1+t z_d\) for \(0\le t\le1\). These coefficients are
nonnegative and every actual birth class has its original total mass.
Consider a retirement at position \(x\), from the high resource
\(j\) of the orbit \(\{i,j\}\), \(i<j\), to an earlier resource
\(k\). Map it to the born edge from low resource \(i\) to that
same \(k\). The two relevant source labels are respectively
\(a_i-a_h\) and \(a_j-a_h\), while the other label stays fixed.
Their weight difference is exactly
\[
 [u_t(a_j-a_h)-u_t(a_i-a_h)]u_t(x-a_k)
      =t\delta_O u_t(x-a_k)\ge0.                  \tag{R8}
\]

This map is globally injective. For an image label pair, the larger
source birth is uniquely \(j\), because every source birth in an
earlier orbit is below \(j\). The physical pair has a unique overlap
position \(x\). Its label of birth \(j\) then recovers its resource
index \(i\) from \(a_i=x-d_i\), and its partner resource is the
already recovered \(j\). The unchanged other resource \(k\) is
also recovered. Thus there cannot be two preimages either at one
position or at two different positions.

Let \(L(u_t)\) and \(R(u_t)\) denote the unordered born and retired
weighted pair sums. All born edges outside the injection image also
have nonnegative weight. Summing (R8) therefore proves
\[
 L(u_t)\ge R(u_t),\qquad
 L(u_t)\ge\tfrac12[L(u_t)+R(u_t)].                 \tag{R9}
\]
In particular, at least half the used weighted mask is retained in
the historical born sum for this scalar carrier.

For clarity one can retain the complete slack at each position:
\[
 L_x(u_t)-R_x(u_t)
 =\sum_{O\text{ two-point}}t\delta_O T_{<O}(u_t)
   +\sum_{\{i,j\}\text{ two-point}}u_t(d_i)u_t(d_j)
   +\sum_{O\text{ fixed}}u_t(d_i)T_{<O}(u_t)
   +\sum_{\substack{\{i,k\}\subset I_x\,:
                    \text{at least one unpaired}}}
                        u_t(d_i)u_t(d_k).          \tag{R10}
\]
Every term here is nonnegative. The final sum is over unordered
pairs, counted once even when both resources are unpaired.

For \(u_-=1-z\), the comparison on the injection's own image is
reversed. The born slack outside that image is still nonnegative,
so this alone does **not** imply the global reverse inequality
\(L(u_-)\le R(u_-)\). Nor does (R9) automatically extend to an
average yielding \(J+zz^T/8\).

## 6. The remaining linear term in the scalar historical comparison

The scalar vector \(u_t\) has full and prefix masses equal to their
uniform values, and trace increase \(t^2S\). Define
\[
 B_{\rm lin}=\sum_{\{d,e\}\text{ born}}(z_d+z_e),
 \qquad X_z=L(zz^T)+S/2.
\]
The latter equals the causal cross energy of the centered feature.
Expanding the exact historical capacity and the same terminal raw
demand gives
\[
 \boxed{\quad I_m^{\rm hist}(u_t)
       =t B_{\rm lin}+t^2(X_z-mS/2).
 \quad}                                             \tag{R11}
\]
The notation on the left means improvement relative to the uniform
scalar carrier, not the nonnegativity of its unreferenced gap. Indeed
the capacity improvement is
\(tB_{\rm lin}+t^2[L(zz^T)+S/2]\), whereas the raw-demand loss
is \(mt^2S/2\). This proves (R11) without assuming any sign on
\(B_{\rm lin}\).

The monotone scalar injection is therefore an exact positive result,
with actual endpoint labels and no repeated capacities. It still
requires a quantitative row or historical gain compatible with the
linear term in (R11). The work above neither assumes the new good-
epoch lemmas nor proves their all-history transport consequence.
The parent's threshold identities pass review; the original Q1
obligation and its Lean verification remain open.

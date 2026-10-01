# Fixed terminal weights and the historical birth envelope

Date: 2026-09-05. Owner: `/root/c143_mathematics`, GPT-6 Astra Ultra.
Status: exact finite identities and a limited transfer bound. Original Q1
remains unresolved. This note does not claim a new Lean verification.

## 1. Fix the weights once, and keep the literal restrictions

Let \(a_1<\cdots<a_N\) be an actual integer Sidon sequence. Fix an integer
width \(D\ge1\), and set
\[
 F_n=\Delta P_n\cap[1,D],\qquad F=F_N,
 \qquad F_1=\varnothing.
\]
Let \(W=(W_{de})_{d,e\in F}\) be a **fixed** symmetric matrix with
nonnegative off-diagonal entries. Its restriction to \(F_n\) is denoted
\(W_n\). Nothing is selected anew or recentered at intermediate prefixes.
Define
\[
 Q_n=\mathbf1_{F_n}^TW\mathbf1_{F_n},\quad
 S_n=\sum_{d\in F_n}W_{dd},\quad
 B_n=\sum_{d<e\in F_n}W_{de}=\frac{Q_n-S_n}{2},
\]
\[
 K_n(t)=\sum_{d<e\in F_n,\ e-d=t}W_{de},\quad
 T_n=\sum_{t\in F_n}K_n(t),\quad E_n=B_n-T_n,
\]
\[
 \mathcal C_N(W)=\sum_{t>0}\max_{1\le n\le N}
                           1[t\notin F_n]K_n(t).     \tag{1}
\]
The diagonal is retained through \(Q_n,S_n\), but is not included in a
positive-difference kernel. All kernels vanish for \(t\ge D\). On this
support the mask equals \(1[t\notin\Delta P_n]\).

The historical identities below need neither PSD nor an analytic demand
inequality. If \(W\succeq0\), each restriction is also PSD and gives the
usual actual-block identity and lower bound
\[
 mS_n+2\Psi_{W_n}(B)
 =\operatorname{Tr}(V_BW_nV_B^T)
 \ge\frac{m^2Q_n}{L_B+\operatorname{diam}F_n}.        \tag{2}
\]
Here \(V_B(z,d)=1[z-d\in B]\), \(L_B\) is the integer interval length
of the actual Sidon block \(B\), and the support has at most the displayed
number of positions. The trace inequality follows from PSD and
\(\mathbf1^TV_BW_nV_B^T\mathbf1=m^2Q_n\). An old-label exclusion bound
may also be used when its separate hypotheses and denominator are kept.

## 2. Weighted births and retirements, including the terminal mass

At step \(n\ge2\), write \(F^-=F_{n-1}\) and
\(G=F_n\setminus F^-\). The total newly born off-diagonal weight is
\[
 A_n=\sum_{d\in F^-,g\in G}W_{dg}
           +\sum_{g<h\in G}W_{gh},\qquad
 Q_n-Q_{n-1}=(S_n-S_{n-1})+2A_n.                    \tag{3}
\]
The retirement weight is
\[
 R_n=\sum_{\substack{d<e\in F^-\\e-d\in G}}W_{de}.
\]
Let \(L_n\) be the weight of newly born label pairs whose positive
difference already belongs to \(F_n\), including pairs whose difference
is born at this same step. Directly partitioning pairs gives
\[
 T_n-T_{n-1}=R_n+L_n,\qquad
 E_n-E_{n-1}=A_n-R_n-L_n.                            \tag{4}
\]
Write \(R^{\rm tot}=\sum_{n=2}^N R_n\) and
\(L^{\rm tot}=\sum_{n=2}^N L_n\).

For each physical \(t\), let \(\tau(t)\) be its first bank-appearance
time, or \(\infty\) if it has not appeared by \(N\). Since \(W\) is
fixed and nonnegative, \(K_n(t)\) is nondecreasing before retirement.
Hence the **exact** fibre maximum is
\[
 \max_n1[t\notin F_n]K_n(t)=
 \begin{cases}
 K_{\tau(t)-1}(t),&\tau(t)\le N,\\
 K_N(t),&\tau(t)=\infty.
 \end{cases}                                       \tag{5}
\]
Summing the retired and unretired fibres separately proves
\[
 \boxed{\quad
 \mathcal C_N(W)=E_N+R^{\rm tot}
   =B_N-L^{\rm tot},\qquad T_N=R^{\rm tot}+L^{\rm tot}.
 \quad}                                            \tag{6}
\]
Thus the fixed-weight historical capacity is a linear functional of \(W\)
on the cone of entrywise nonnegative matrices. Its positive edge set is
exactly
\[
 \mathscr H=\{\{d,e\}\subset F:
 e-d\notin F\ \text{or}\ \tau(e-d)>\max(\tau(d),\tau(e))\}.
                                                               \tag{7}
\]
Each such pair is counted once, even though its physical label can share
a fibre with many other pairs. An actual future-span mask or selection
of fewer prefix states only lowers (1); it need not preserve equality.

## 3. The injection changes the weight

Every retiring pair \(\{d,e\}\), \(d<e\), has \(t=e-d\in G\) and
maps injectively to the new pair \(\{t,e\}\), whose difference \(d\)
is old. The image is a pair born with an already used difference. The
map is injective because its larger element is \(e\); it recovers
\(d=e-t\). The case \(d=t\) cannot retire because it would require the
same label to be both old and newly born.

Its **image weight**, generally different from its source weight, is
\[
 \widetilde R_n
   =\sum_{\substack{d<e\in F^-\\e-d\in G}}W_{e-d,e},
 \qquad Z_n=L_n-\widetilde R_n\ge0.                 \tag{8}
\]
The unweighted injection must not be mistaken for
\(\widetilde R_n=R_n\).

The extra birth weight has an explicit nonnegative decomposition for an
actual Sidon history. Distinct \(g,h\in G\) have \(|g-h|\in F^-\),
and \(G\) is sum-free, including repeated summands: otherwise
\((a_n-a_i)+(a_n-a_j)=a_n-a_k\) would contradict Sidon. Define
\[
 Z_n^{00}=\sum_{\substack{g\in G,\ f,h\in F^-\\f+h=g}}W_{f,g},
 \qquad
 Z_n^{11}=\sum_{\substack{f\in F^-,\ g,h\in G\\g+h=f}}W_{g,f}.
\]
The summand pairs \((f,h)\) and \((g,h)\) are ordered. A repeated
summand occurs once. Then
\[
 Z_n=Z_n^{00}
       +\sum_{g<h\in G}(W_{g,h}+W_{h-g,h})
       +Z_n^{11}.                                  \tag{9}
\]
To verify completeness, split new pairs into old/new and new/new.
Among old/new pairs, a new smaller label with old positive difference is
exactly the injection image. A new larger label with old difference gives
\(Z^{00}\). A new larger label with new difference gives
\(W_{h-g,h}\); a new smaller label with new difference gives \(Z^{11}\).
All new/new pairs have old difference and give \(W_{g,h}\). These cases
are disjoint. No matrix-diagonal entry is part of (9); the repeated-sum
cases, such as the pair \(\{g,2g\}\), are nevertheless retained.

With totals denoted by the same letters without a step subscript,
\[
 \boxed{\quad T_N=R+\widetilde R+Z,\qquad
 \mathcal C_N(W)=\frac{Q_N-S_N}{2}-\widetilde R-Z
 =\frac{Q_N-S_N}{2}-\frac{T_N}{2}
                     +\frac{R-\widetilde R}{2}-\frac Z2.\quad}
                                                               \tag{10}
\]
For \(W=J\), (9) becomes \(S^{00}+2\binom{|G|}{2}+S^{11}\), and
(10) is precisely the earlier half-mask identity.

## 4. What entry bounds alone preserve

Assume \(0<a\le W_{de}\le b\) for all off-diagonal entries. Pairwise
comparison on the injection yields \(\widetilde R\ge(a/b)R\).
Since \(L=\widetilde R+Z\), it follows that
\[
 \boxed{\quad L\ge\frac{a}{a+b}T_N,\qquad
 \mathcal C_N(W)\le\frac{Q_N-S_N}{2}
                           -\frac{a}{a+b}T_N.\quad}             \tag{11}
\]
Thus entries in \([1/2,3/2]\) retain at least **one quarter of the
weighted terminal mask**, and entries in \([1-\varepsilon,1+\varepsilon]\)
retain at least \((1-\varepsilon)/2\) of it.

This is not a guarantee of retaining one quarter of an improvement over
\(J\). The baseline has the stronger coefficient \(1/2\), and switching
to \(1/4\) can lose more baseline mask than a new small gain provides.
Subtracting (11) from the old uniform bound does not establish a saving.

## 5. Centered PSD corrections: exact comparison with the row gain

Now let \(W=J+\lambda R\), with \(\lambda>0\), \(R\succeq0\), \(R\mathbf1_F=0\),
and \(W\) entrywise nonnegative. For any signed matrix \(R\), use
\(T_R,R_{\rm ret},L_R\) for its sums over the fixed terminal mask,
retiring-pair set, and pair set born with used differences. These are
linear functionals and can be negative. The pair classifications remain
valid, but nonnegativity is invoked for \(W\), not for \(R\) separately.
With \(q=|F|\), terminal centering gives
\[
 Q_N(W)=q^2,\quad S_N(W)=q+\lambda S_R,\quad
 B_N(R)=-S_R/2,
\]
\[
 \boxed{\quad
 \mathcal C_N(J)-\mathcal C_N(W)
 =\lambda(S_R/2+L_R)
 =\lambda(S_R/2+T_R-R_{\rm ret}).\quad}             \tag{12}
\]

At the terminal prefix, the centered-spectral note compares old masked
capacity minus raw future demand of size \(m\). Its exact row gain is
\[
 I_m=\lambda\{T_R-(m-1)S_R/2\}.
\]
Combining with (12) gives the precise transfer identity
\[
 \boxed{\quad
 \mathcal C_N(J)-\mathcal C_N(W)
 =I_m+\lambda\{mS_R/2-R_{\rm ret}\}.\quad}          \tag{13}
\]
In particular the whole row gain survives if
\(R_{\rm ret}\le mS_R/2\). More generally a fraction \(c\in[0,1]\)
survives if
\[
 R_{\rm ret}\le mS_R/2+(1-c)I_m/\lambda.             \tag{14}
\]
These are exact sufficient conditions, not proved universal estimates.

For the Fourier correction in `centered_spectral_gain.md`, \(\lambda=1/8\),
\(S_R\le q\), and \(|R_{de}|\le4\). The full-bank row theorem gives
\(I_m/q^2\ge c_C/\log(2p)-O(1/p)\) when \(m=O(p)\), with an explicit
positive constant. An upper bound
\((R_{\rm ret})_+=o(q^2/\log p)\) would therefore preserve this order
of gain in (13). The entry estimate \(R_{\rm ret}\le4R_J\), and the
unweighted half-mask inequality \(R_J\le T_J/2\), only give order
\(q^2\); they do not supply the needed bound. Nor does the exact positive
single-row guarantee itself control this signed retirement functional.

### 5.1 Intermediate prefixes lose centering

Write a Gram representation \(R_{de}=\langle z_d,z_e\rangle\) with
\(\sum_{d\in F}z_d=0\). For \(F_n\), put \(\zeta_n=\sum_{d\in F_n}z_d\).
The literal restriction satisfies
\[
 Q_n(W)=q_n^2+\lambda\|\zeta_n\|^2,\qquad
 S_n(W)=q_n+\lambda\sum_{d\in F_n}\|z_d\|^2.        \tag{15}
\]
For raw demand \((m^2Q_n/D_B-mS_n)/2\), with its actual positive
denominator \(D_B\), the exact restricted row comparison is
\[
 I_{n,m}=\frac\lambda2\left[
 2T_n(R)-(m-1)S_n(R)
       -\left(1-\frac{m^2}{D_B}\right)\|\zeta_n\|^2\right].   \tag{16}
\]
In the critical regime \(m^2/D_B\) can be small, so the missing centering
is a substantial negative term. The terminal frequency theorem does not
imply the same bound at every restriction. Formula (16) was independently
sent by /root/lean_target, and follows here simply by subtracting the two
capacity-minus-demand expressions with the actual masses in (15).

## 6. Fourier injection imbalance is a one-label potential transport

Keep a single terminal phase and mean:
\[
 z_s=e^{i\theta s}-\mu,\qquad
 R_{de}=\Re(z_d\overline{z_e}),\qquad
 h(s)=\Re\{(1+\overline\mu)e^{i\theta s}\}.
\]
For a retirement \(t=e-d\), expansion using \(e=d+t\) gives
\[
 \boxed{R_{de}-R_{t,e}=h(t)-h(d).}                  \tag{17}
\]
Indeed the two terms involving \(e\) and the term \(|\mu|^2\) cancel;
the remaining terms are
\(\cos(\theta t)-\cos(\theta d)
 +\Re\{\overline\mu(e^{i\theta t}-e^{i\theta d})\}\).

Define \(r_s\) to be the number of retiring pairs with physical difference
\(s\), and \(c_s\) the number whose smaller source label is \(s\).
The exact imbalance is therefore
\[
 R_{\rm ret}-\widetilde R_R
 =\sum_{s\in F}h(s)(r_s-c_s),\qquad \sum_s r_s=\sum_s c_s.    \tag{18}
\]
The equality of total counts only removes constant shifts of \(h\).
The degree-weighted divergence \(r_s-c_s\) cannot be discarded. The
frequency window in the spectral note is based on a central quantile
width, so \(\theta H\) need not be small; no global monotonicity of
\(h\) is available from that window. Equation (18) isolates a possible
online-potential argument, but does not close it.

## 7. Equal mass and entry bounds do not transfer a positive row saving

Here is an exact counterexample for general nonnegative pair kernels;
it is explicitly **not** a PSD counterexample. Take the actual positive
Sidon prefix
\[
 P=\{1,2,5,7,14\},\qquad
 F=\{1,2,3,4,5,6,7,9,12,13\}.
\]
Its ten displayed differences are all distinct, which verifies Sidon
including repeated sums. The pair of labels \(\{1,3\}\) retires when
label \(2=7-5\) appears: label 1 was born at rank 2 and label 3 at
rank 3, whereas label 2 was born at rank 4. The pair \(\{1,2\}\) is
born with the already used difference 1. The pair \(\{1,9\}\) has
difference 8, absent from the terminal bank, so it remains unretired.

Starting from \(J\), change just the following symmetric off-diagonal
entries:
\[
 W_{1,3}=3/2,\qquad W_{1,9}=3/4,\qquad W_{1,2}=3/4.
\]
All other entries, including the diagonal, are one. The off-diagonal
increments sum to zero, so \(Q=q^2\) and \(S=q\) are unchanged. The
terminal row capacity decreases by \(1/4\), but the historical capacity
**increases** by \(1/2-1/4=1/4\): the boosted retirement was a past peak,
while the decreased weight on a pair born with a used difference never
entered a peak. Thus no positive fraction of arbitrary row savings is
guaranteed by entry bounds, equal mass, and equal diagonal alone.

The principal block on labels 1 and 3 has determinant \(1-(3/2)^2<0\),
so PSD is absent. Its raw-demand formula would be unchanged by equal
mass and trace, but a PSD shadow lower bound is not asserted for this
matrix. It does not refute the selected Fourier construction, the
fixed-onset cap, or Q1.

## 8. Saved finite checks, and what remains unproved

`evidence/weighted_birth_exact_checks.py` performs one exact rational-phase
check on the same 17-point Sidon prefix used by the centered-spectral note.
It keeps the terminal mean fixed at every prefix, checks all repeated
two-sums, all fibre maxima directly for \(W\), the pair classification,
the Fourier potential identity, and every prefix mass in (15). Integer
Gaussian numerators and rational arithmetic are used for all identities
and signs. The rational phase is
\(\theta=2\arctan(1/(2\cdot248))\), and its variance exceeds \(1/24576\).
The exact report and execution log are saved beside the source. The
post-run provenance `evidence/weighted_birth_checks.run.json` records
the two observed exit codes, source/report/log SHA256 hashes, and the
fact that provenance was saved without rerunning either check. Decimal
displays, not proof inputs, are:

| Quantity | Display |
|---|---:|
| Terminal row-gap gain, \(m=p=17\) | 7.1827955592 |
| Terminal row-capacity gain | 26.5267330178 |
| Signed retirement correction \(R_{\rm ret}/8\) | 1.4073206722 |
| Historical capacity gain | 25.1194123456 |

The last two quantities satisfy (12) exactly. This one example retains
the improvement; it is not an argument for uniform retention.

`evidence/weighted_birth_psd_search.py` is a separate bounded exploratory
search on that same history, for general centered rank-one PSD residuals
with positive row gain and negative historical gain. It used 46 scalar
parameters and 260 floating power iterations per parameter. It found no
witness. The source, every observed parameter output, and execution log
are saved. Failure to find a witness proves no inequality. A witness,
had one been found, would have required the included exact integer
quadratic-form checks before being reported as a counterexample.

The exact general result is (10), the uniform entry-range transfer is
(11), and the specific Fourier transfer obligation is (13)--(18).
A nonzero portion of the guaranteed asymptotic row improvement has not
yet been proved to remain in the fixed-terminal historical envelope.
No independent copies across widths have been summed. Neither original
Q1 nor its required Lean proof is complete.

## 9. Sidonness and terminal centering alone cannot make retirement negligible

The following obstruction was supplied by /root/global_route and checked
independently here. It addresses general centered PSD matrices. It does
not address the special selected Fourier phase or an all-prefix cap.

First there are actual finite \(m\)-point Sidon sets \(P\), or their
reflections, with \(R_J(P)\ge c m^4\) for an absolute \(c>0\) along an
unbounded sequence of \(m\). To see this, use the finite Bose construction
in `short_three_sum_flux.md`, giving \(P\subset[1,m^2]\). More generally
suppose \(P\subset[1,C_0m^2]\), with fixed \(C_0\). The
\(L=\binom m3\) sums of distinct triples lie in at most \(3C_0m^2\)
integer positions. Thus the number of unordered pairs of different
triple representations of the same sum is at least
\[
 \frac{L^2}{6C_0m^2}-\frac L2=\Omega_{C_0}(m^4).     \tag{19}
\]
Two such triples have disjoint vertices: cancelling a common point would
otherwise give a forbidden two-sum equality.

Write the side containing the largest point as \(\{M,u,v\}\), \(u<v\),
and the other side as \(\{a,b,c\}\). If two distinct points on the
other side can be chosen with \(a>u\) and \(b<v\), then
\[
 e=a-u>0,\qquad d=v-b>0,\qquad
 t=M-c=e-d>0
\]
give a retiring source pair \(\{d,e\}\): the source-label births precede
the unique latest endpoint \(M\) of physical label \(t\). Such a choice
fails only if all three points on the other side exceed \(v\). Indeed
some exceed \(u\), since otherwise their sum is too small; if at least
one is below \(v\), the two choices can be made distinct, because the
sets of candidates together cover all three points. In the exceptional
case, reflection of the entire ruler reverses the ordering and supplies
the desired choice. Each retiring record, together with the choice of
original or reflected ruler, recovers the collision from its unique
difference endpoints. Consequently
\[
 R_J(P)+R_J(\operatorname{reflect}P)
 \ge\frac{L^2}{6C_0m^2}-\frac L2.                   \tag{20}
\]
Choose the orientation with at least half this value.

Now append \(m\) much larger points, one at a time, each new point more
than three times the previous maximum. Every new target difference is
larger than the previous label span, so it cannot retire any old label
pair. The new cross star is injective and disjoint from all old
differences, so Sidonness is preserved. The terminal retirement graph
therefore consists exactly of the old retirement graph, with all new
labels isolated. This holds inductively at every padding step.

Let \(q_0=\binom m2\) be the old bank size and
\(q_1=\binom{2m}{2}-q_0=(3m^2-m)/2\) the number of new labels. Put
\[
 v_d=\begin{cases}1,&d\text{ old},\\-q_0/q_1,&d\text{ new},\end{cases}
 \qquad R=vv^T.
\]
Then \(R\succeq0\), \(R\mathbf1=0\), and
\[
 S_R=q_0+q_0^2/q_1\le m^2,\qquad
 R_{\rm ret}(R)=R_J(P)=\Omega(m^4).                 \tag{21}
\]
All values of \(v\) lie in \([-1/3,1]\), so \(J+R/8\) is also PSD,
has entries in \([1/2,3/2]\), and has the terminal mass required in §5.
At terminal point count \(p=2m\), the ratio
\(R_{\rm ret}(R)/S_R=\Omega(p^2)\). Thus no estimate
\(R_{\rm ret}(R)\le O(p\log p)S_R\) follows from actual Sidonness
and centered PSD alone.

The exponentially separated padding destroys the fixed critical cap.
This is not a counterexample to a cap-sensitive operator bound or to
Fourier-specific retention. It prevents removing the correction in (13)
by a cap-free estimate. No new search or numerical calculation was used
in this argument.

## 10. Capacity alone and capacity minus demand have different transfer tests

The improvement in (12)--(14) concerns **historical capacity alone**.
For comparison with the same terminal raw demand, its diagonal loss must
also be charged. At the terminal centered bank,
\(d_B(J)-d_B(W)=\lambda mS_R/2\). Therefore
\[
 \begin{split}
 I_m^{\rm hist}
 &:=[\mathcal C_N-d_B](J)-[\mathcal C_N-d_B](W)\\
 &=I_m-\lambda R_{\rm ret}
  =\frac\lambda2\{2L_R-(m-1)S_R\}.                \tag{22}
 \end{split}
\]
In particular the sufficient condition for keeping the whole **gap**
improvement is \(R_{\rm ret}\le0\), not the weaker condition following
(13) for capacity alone. The order-of-magnitude criterion
\((R_{\rm ret})_+=o(q^2/\log p)\) still suffices to preserve a positive
asymptotic fraction of the spectral row rate.

Let \(A_{\rm born}\) be the zero-diagonal adjacency matrix on label pairs
whose difference was already present at their birth. For a symmetric
matrix, \(2L_R=\operatorname{Tr}(A_{\rm born}R)\). A positive centered
PSD gap improvement exists, with a sufficiently small positive scaling
to keep all entries nonnegative, exactly when
\[
 \lambda_{\max}\bigl(\Pi A_{\rm born}\Pi\vert_{\mathbf1^\perp}\bigr)
 >m-1.                                             \tag{23}
\]
This follows by the Rayleigh principle and decomposing centered PSD
matrices into centered rank-one terms. It involves the actual graph of
pairs born with used differences, not the larger terminal old-mask graph.

### 10.1 An exact finite PSD obstruction supplied by the Lean agent

The source and completed log
`evidence/born_dead_spectral_exact_checks.py` and
`evidence/born_dead_spectral_exact_checks.log` were read here without
rerunning them. They belong to /root/lean_target. They verify an actual
16-point prefix and an actual compatible 16-point continuation, with all
32 positive points satisfying \(a_n\le2n^2\). The old bank has \(q=120\).
For an explicit centered integer vector \(z\) stored in that source,
\[
 \|z\|^2=918,\qquad z^TA_{\rm old}z=13894,\qquad
 z^TA_{\rm born}z=12568,\qquad (m-1)\|z\|^2=13770.
\]
All 119 leading principal minors of
\(E^T(15I-A_{\rm born})E\), with columns of \(E\) equal to
\(e_i-e_{120}\), are exactly positive in the saved certificate.
Sylvester's criterion therefore places the entire centered spectrum
strictly below 15, while the displayed old-mask Rayleigh value is above
15. This excludes a positive historical gap improvement for **every**
nonzero centered PSD correction at this finite history with \(m=16\).

For compatibility with the entry and trace bounds of the current task,
rescale the same witness to
\[
 W=J+zz^T/64=J+R'/8,\qquad R'=zz^T/8.
\]
The source has \(-5\le z_d\le4\). Thus \(W\) has entries in
\([11/16,89/64]\subset[1/2,3/2]\), is PSD, and has
\(R'\mathbf1=0\), \(\operatorname{tr}R'=459/4\le120\).
This rescaling requires no new experiment: every relevant quantity is
linear in the correction. Exact consequences are
\[
 \begin{array}{rcl}
 \text{terminal capacity gain}&=&3703/32,\\
 \text{historical capacity gain}&=&6743/64,\\
 \text{raw-demand loss}&=&459/4,\\
 I_{16}&=&31/32>0,\\
 I_{16}^{\rm hist}&=&-601/64<0.
 \end{array}                                       \tag{24}
\]
The compatible corrected raw demand remains positive:
\(424173/1892>0\). Notice that both capacity gains are positive; the
failure is specifically the transfer of the **gap** improvement after
the same diagonal demand loss has been charged.

This closes an unconditional finite-prefix PSD transfer claim, even with
a strong cap throughout the displayed finite history. It does not refute
a theorem that applies only for sufficiently large ranks in one infinite
fixed-onset capped sequence. The vector here is a general centered
rank-one correction; it is not asserted to equal the phase selected in
the Fourier theorem. The required asymptotic estimate remains a new
bound on \(A_{\rm born}\) or on its specific Fourier quadratic form.

## 11. Fixed-terminal nonnegative decompositions do commute with these maxima

Suppose \(W=\sum_\ell c_\ell u^{(\ell)}u^{(\ell)T}\), with
\(c_\ell\ge0\) and every \(u^{(\ell)}\ge0\), fixed on the terminal
bank. Restrict all vectors to the same chosen prefix states. On every
physical-label fibre, the maximizing state is its last selected state
before retirement, or the last selected state if unretired. This time
depends on the history and the chosen state set, not on the nonnegative
weights. Formula (5), or its restriction to selected states, therefore gives
\[
 \mathcal C(W)=\sum_\ell c_\ell
                    \mathcal C(u^{(\ell)}u^{(\ell)T}).         \tag{25}
\]
Raw demands, using the same denominators for all components, also depend
linearly on each literal restricted matrix.
Consequently historical capacity-minus-raw-demand comparisons respect
the same decomposition, for a fixed collection of states and demands.
For the four nonnegative carriers representing the terminal Fourier
matrix, any positive matrix gap improvement would be their exact
average, and at least one fixed scalar carrier would attain it.

This removes the averaging-versus-maximum obstruction for this particular
fixed-terminal restriction method. It does not apply to independently
reselected matrices or scalar carriers at each prefix, nor does it prove
that the average in question is positive. Statements involving positive
parts of several demands require their signs to be checked separately.
No separate budget has been introduced at each width.

## 12. Review and current boundary

The parent independently checked the weighted flux, its ordered repeated-
summand cases, the transfer and missing-centering signs, and the Fourier
potential. /root/global_route independently read and verified §§1--6;
the minor explicit condition \(\lambda>0\) has been included above.
The newly referenced exact PSD obstruction was verified by its owning
agent and read here at source level; it was not silently rerun or described
as a new Lean theorem.

The fixed-weight historical expression is now exact. A quarter of its
weighted terminal mask is guaranteed by entry bounds, and a fixed
nonnegative rank-one decomposition is compatible with the same maxima.
Preservation of the positive asymptotic **gap** gain still requires
cap-sensitive control of the signed retirement correction or of the
actual graph in (23), over an unbounded range of ranks. Finite automatic
transfer and a cap-free centered-operator shortcut are ruled out by the
recorded constructions. Original Q1 remains unresolved.

# The birth-linear Born term: exact decomposition and a terminal-cap obstruction

Date: 2026-09-05. Owner: `/root/c143_mathematics`, GPT-6 Astra Ultra.

**Proved here:** an exact shadow decomposition of the linear Born term,
and an infinite family of finite actual Sidon sets with constant normalized
variance and a fixed terminal critical cap for which every monotone scalar
carrier \(1+t z\), \(0<t\le1\), worsens the historical raw gap relative
to the uniform carrier. This does not satisfy one fixed-onset cap throughout
the family histories, or the good half/quarter diameter condition. It is
not a counterexample to Q1 or to the conjunction of those hypotheses.

The negative-family idea was proposed in parallel by the parent; the
mixed-collision count, normalization errors, and constants below were
independently derived here. The complete sources
`birth_linear_good_epoch.md`, `dyadic_good_epochs.md`, and the preceding
shadow review were read. Nothing in this note is asserted to be Lean
verified. The finite check in §8 is separate from the analytic theorem.

## 1. The exact quantity and the shadow decomposition

Let \(P=\{a_1<\cdots<a_N\}\) be integer Sidon, including repeated
two-sums, \(F=\Delta P\), \(q=\binom N2\), and \(H=a_N-a_1\).
Write \(m_j=(j-1)^{-1}\sum_{i<j}a_i\) and
\[
 z_{a_j-a_i}=(m_j-a_i)/H,
 \quad S=\sum_{d\in F}z_d^2,
 \quad B_{\rm lin}=\sum_{\{d,e\}\text{ born}}(z_d+z_e).
\]
Here “born” means \(|d-e|\in F\) with its birth no later than the
maximum of the two source births. Each class and each prefix sums to
zero, and \(|z_d|\le1\).

Use the actual partial involution at each position \(x\), as proved
in `retirement_shadow_review.md`. Let \(c_O\) be the number of earlier
paired resources before orbit \(O\), \(T_O\) their signed coefficient
sum, \(w_O\) the sum on that orbit, and
\(\delta_O=(m_j-m_i)/H>0\) for a two-point orbit \(\{i,j\}\),
\(i<j\). Let \(r_x\) be the total number of active resources,
\(u_x\) the number unpaired, \(V_x\) the paired coefficient sum,
and \(U_x\) the unpaired coefficient sum.

The exact linear retirement sum at this position is
\[
 R_{x,\rm lin}=\sum_{O\text{ two-point}}
                   \left[\frac{c_O(w_O-\delta_O)}2+T_O\right].
                                                               \tag{1}
\]
Each high resource retires against precisely its earlier resources.
The sum of the two endpoint coefficients over all active unordered
pairs is \((r_x-1)(V_x+U_x)\). Consequently
\[
 B_{\rm lin}=\sum_x\{(r_x-1)(V_x+U_x)-R_{x,\rm lin}\}.       \tag{2}
\]
Every eligible physical pair has exactly one such position, so (2)
introduces no repeated copies of a label pair.

Differentiating the exact positive-injection slack at the uniform
carrier gives the equivalent signed identity
\[
 \begin{split}
 B_{\rm lin}-R_{\rm lin}
 ={}&\sum_{x,O\text{ two-point}}c_O\delta_O
      +\sum_{x,O\text{ two-point}}w_O\\
    &+\sum_{x,O\text{ fixed}}(c_Ow_O+T_O)
      +\sum_x[(r_x-1)U_x+u_xV_x].
 \end{split}                                                    \tag{3}
\]
The final sum is the entire contribution of born pairs incident to
unpaired resources: the cross part is \((r_x-u_x)U_x+u_xV_x\),
and the unpaired/unpaired part is \((u_x-1)U_x\). Both terms are
needed, even if their sum is negative.

The two-point internal-edge term can be evaluated globally:
\[
 \sum_{x,O\text{ two-point}}w_O
 =\sum_{i<j}(N-i-1)z_{a_j-a_i}
 =\frac1H\sum_{j=2}^N\sum_{i<j}i(a_i-m_j)\ge0.               \tag{4}
\]
The last sign is the covariance of the two increasing sequences
\(i\) and \(a_i\) on each old prefix; the constant \(N-1\)
cancels by class centering. This term is \(O(N^3)\). There are
exactly \(q\) fixed-point incidences, so the absolute fixed linear
term in (3) is at most \(2Nq\). These bounds do not control the
unpaired term, which remains at the potentially larger order.

There is also an exact class-degree expression. If \(b_{ji}\) is
the Born degree of label \(a_j-a_i\), then
\[
 B_{\rm lin}=-\frac1H\sum_j\sum_{i<j}(a_i-m_j)b_{ji}.         \tag{5}
\]
Thus an unproved monotonicity of these actual degrees must not be
substituted for a sign theorem. Section 8 already disproves a universal
nonnegative sign on finite capped, good-shape examples.

## 2. Two elementary counting facts used in the limiting construction

First, any integer Sidon set \(U\) of \(n\) points and diameter
\(h_U\) has, with \(q_U=\binom n2\),
\[
 L_U\ge\frac{n^2q_U^2}{8h_U}-\frac{nq_U}{4},                 \tag{6}
\]
where \(L_U\) is its unweighted Born pair count. To see this,
\(1_U*1_{\Delta U}\) has mass \(nq_U\) in at most \(2h_U\)
integer positions. Its energy is \(nq_U+2T_U\), so Cauchy gives
\(T_U\ge n^2q_U^2/(4h_U)-nq_U/2\). The uniform version of the
actual high-resource to low-resource injection proves \(L_U\ge
T_U/2\). This proves (6) without using any claimed Q1 result.

Second, a used label pair gives a three-sum equality by writing its
two source differences and output difference with their actual unique
endpoints. If the two three-point multisets coincide, their three
nonzero oriented edges form a directed three-cycle. Hence the source
labels share either their lower endpoint or their upper endpoint.
These automatic pairs are born. The automatic graph has degree at
most \(2(N-2)\), so for coefficients bounded by one its entire
linear weight has absolute value at most
\[
 2(N-2)q\le N^3.                                             \tag{7}
\]

If the three-point multisets differ, fix that unordered collision.
Match their three slots in any of the six ways. The three resulting
signed differences sum to zero. When all are nonzero, one positive
length is the sum of the other two, and at most two used source pairs
arise. Thus at most 12 used pairs arise from a collision. This argument
allows repeated slots; repetitions can reduce the count, not increase
it. The coarser bound 36 is therefore also safe below.

## 3. The explicit dense ruler and its separated split

Fix \(\varepsilon=2^{-24}\). Let \(N\) be any odd prime with
\(\log N\ge2^{48}\), and form the actual integer Sidon ruler
\[
 Q_N=\{b_i=2Ni+(i^2\bmod N):0\le i<N\},\qquad
 h=\max Q_N<2N^2.                                             \tag{8}
\]
The points increase with \(i\). A two-sum equality first forces
equal index sums because its residue error is strictly less than
\(2N\); reduction modulo \(N\) then gives equal square sums and
products. The unordered quadratic roots coincide over the odd prime
field, including repeated roots. This proves Sidonicity directly.

Let \(\ell=\lfloor\varepsilon N\rfloor\), let \(L\) be the first
\(\ell\) points of \(Q_N\), and let \(U\) be the remaining
\(n=N-\ell\) points. Put
\[
 M=\lceil N^2\log N\rceil,
 \qquad P_N=L\ \cup\ (M+U),                                  \tag{9}
\]
and translate all its points by 1 for positivity. Since \(M>6h\),
an equality of two or three sums must have the same number of shifted
points on both sides: otherwise a nonzero multiple of \(M\) would
have magnitude at most \(3h\). For two-sums the shifts cancel, and
the equality is a two-sum equality in \(Q_N\). Thus \(P_N\) is
actual Sidon. No labels or births are assigned independently.

For later bounds,
\[
 n\ge N/2,\quad \ell/n\le2\varepsilon=2^{-23},\quad
 \ell\ge\varepsilon n/2,\quad \ell\ge2^{16},\quad n\ge256.
                                                               \tag{10}
\]
The deliberately large prime threshold implies all these inequalities.

## 4. The exact limiting feature and the mixed-collision budget

Let \(z^*\) denote the limiting feature with all \(L\) offsets set
to 0, all shifted \(U\) offsets set to 1, and the actual rank order
kept. This is only a coefficient vector on the actual label bank;
the collapsed points are not asserted Sidon. For the \(r\)-th point
of \(U\), its actual preceding class contains \(\ell+r-1\) points.
The values are exactly
\[
 z^*=0\text{ on internal }L\text{ labels},\qquad
 z^*_{U_r-L_i}=\frac{r-1}{\ell+r-1},\qquad
 z^*_{U_r-U_s}=-\frac{\ell}{\ell+r-1}\quad(s<r).              \tag{11}
\]
Each class still sums to zero, and
\[
 \|z^*\|_1=2\ell\sum_{r=1}^n\frac{r-1}{\ell+r-1}
                                      \le2\ell n.             \tag{12}
\]
Every original Born edge of \(U\) remains born: its three relevant
birth ranks are all shifted by \(\ell\). These inherited edges
contribute at most \(-2\ell L_U/(\ell+n)\). There can additionally
be pairs of internal \(U\) source labels whose output is in
\(\Delta L\); those are mixed records included below. Thus no
equality between the whole restricted Born graph and the original
Born graph of \(U\) is being assumed.

For nontrivial three-sum collisions involving both clusters, the only
possible types after the shift counts cancel are
\(LUU=LUU\) and \(LLU=LLU\). For the first type, fix the ordered
pair of \(L\) points and one unordered \(U\) two-sum. Sidon
uniqueness permits at most one opposite \(U\) two-sum. There are
at most \(\ell^2n^2\) choices, with repeated summands included.
For the second type, fix the ordered \(U\) pair and one unordered
\(L\) two-sum; the same bound follows. These are upper bounds on
unordered collisions as well, since allowing their orientations can
only increase the count.

Each collision contributes at most 36 used source records and each
linear record has absolute weight at most 2. Hence their total possible
positive contribution is at most
\[
 144\ell^2n^2.                                               \tag{13}
\]
All-\(L\) nontrivial records have weight zero. All-\(U\) records
are already included in the negative internal Born graph. Everything
else is covered by the automatic bound (7). In particular, (13)
does not drop any unmatched born slack.

Here \(h_U\le h<2N^2\le8n^2\). Formula (6), together with
\(q_U\ge n^2/4\), \(q_U\le n^2/2\), and \(n\ge256\), gives
\[
 L_U\ge q_U^2/64-nq_U/4\ge n^4/2048.                         \tag{14}
\]
Combining all contributions and (10),
\[
 \begin{split}
 B^*&\le-\frac{\ell n^3}{2048}+144\ell^2n^2+N^3\\
    &\le-\frac{\ell n^3}{4096}.
 \end{split}                                                  \tag{15}
\]
Indeed, each positive term in the first line is at most
\(\ell n^3/8192\): for the mixed term use
\(144\cdot2^{-23}<2^{-13}\), and for the automatic term use
\(N^3\le8n^3\), \(\ell\ge2^{16}\).

## 5. Literal finite-height errors and constant variance

The actual terminal diameter is \(H=M+h\), because the first
point of \(L\) is 0 and the largest point of \(U\) is \(h\).
Every actual feature can be written
\(z_d=(Mz_d^*+c_d)/(M+h)\), with \(|c_d|\le h\). Thus
\[
 e:=\max_d|z_d-z_d^*|\le2h/H\le4/\log N.                    \tag{16}
\]
There are at most \(q^2/2\) Born pairs, so
\[
 |B_{\rm lin}-B^*|\le e q^2\le N^4/\log N
                                  \le\ell n^3/16384.          \tag{17}
\]
For the final inequality use \(N\le2n\),
\(\ell\ge n/2^{25}\), and \(\log N\ge2^{48}\).
Equations (15)--(17) prove the actual negative bound
\[
 B_{\rm lin}\le-3\ell n^3/16384.                             \tag{18}
\]
Similarly \(q e\le\ell n\), so (12) implies
\[
 \|z\|_1\le3\ell n.                                         \tag{19}
\]

This is not a vanishing-variance feature. For each of the last half
of the \(U\) stages, the preceding points include \(\ell\) low
points and at least \(n/2\) high points, separated by at least
\(M-h\). The pairwise variance formula gives for that class
\[
 S_r\ge\frac{\ell(r-1)}{\ell+r-1}
                 \left(\frac{M-h}{M+h}\right)^2.
\]
Since \(M\ge4h\), each selected class has variance at least
\(\ell/16\), and there are at least \(n/3\) such stages.
Therefore
\[
 S\ge\ell n/48\ge\varepsilon q/192.                         \tag{20}
\]
The general upper bound \(S\le q\) and all prefix zero sums remain
valid for the actual vector.

The translated positive points also satisfy the fixed terminal cap
\[
 a_N=M+h+1\le2N^2\log(2N).                                   \tag{21}
\]
No limit exchange was used: (18)--(21) hold for every odd prime above
the stated explicit threshold.

## 6. Every bounded monotone-plus parameter worsens the raw historical gap

Let \(A_{\rm cross}\) be the actual mixed-class Born adjacency.
The centered quadratic causal sum is
\(X_z=\tfrac12z^TA_{\rm cross}z\). Consequently
\[
 |X_z|\le\tfrac12\|z\|_1^2
       \le\tfrac92\ell^2n^2\le\ell n^3/16384.                \tag{22}
\]
The final inequality follows from \(\ell/n\le2^{-23}\).
For any \(0<t\le1\), the scalar \(u_t=1+t z\) is nonnegative,
has the uniform mass on every prefix, and is covered by the parent's
positive monotone injection. Nevertheless its exact historical gap
improvement against the same terminal raw future demand is
\[
 \begin{split}
 I_m^{\rm hist}(u_t)
 &=tB_{\rm lin}+t^2(X_z-mS/2)\\
 &\le-t\ell n^3/8192<0\qquad(m\ge1).
 \end{split}                                                  \tag{23}
\]
This uses \(t^2\le t\), (18), and (22), keeping the nonpositive
diagonal term. For an actual future block the usual positive interval
denominator is assumed; it cancels from this comparison because the
masses agree. Here the terminal raw future demand is the **mass-only**
raw demand with the full diagonal cost. Formula (23) does not include,
and does not disprove improvement for, the additional first-moment demand
proved in `future_moment_demand.md`. No claim about clipped demands is
substituted for (23).

There are arbitrarily large odd primes, so this is an infinite family
of actual finite examples, not an extrapolation from §8. It proves
that positive injection, constant variance, and a terminal critical
cap alone do not guarantee historical improvement for any bounded
monotone-plus choice of \(t\).

The same feature still has a strong **quadratic terminal** row bound.
The general first-moment estimate in `birth_linear_good_epoch.md`
uses no good-epoch assumption once \(S\) is known. Combining it
with (20)--(21), for \(m\le R_0N\), gives
\[
 \frac{I_m(J+zz^T/8)}{q^2}
 \ge\frac{3\varepsilon^2}{64\cdot192^2\log(2N)}
                  -\frac{R_0+1}{8(N-1)}.                       \tag{24}
\]
This is eventually positive. Thus the family preserves the strong
terminal quadratic improvement and still defeats every bounded
monotone-plus historical choice in (23). Replacing that quadratic
carrier by the injection-compatible plus direction is not a free
step. The missing good-shape and full-history assumptions remain
exactly as stated next.

## 7. What the construction leaves open

The whole fixed-onset cap is absent. At each fixed rank \(k\ge2\),
eventually \(k\le\ell\), and its low-cluster coordinate is
\(2N(k-1)+(k-1)^2+1\), which grows with the prime. Thus no single
fixed constant and onset bound all these initial ranks throughout the
family. These are separate finite histories, not one infinite capped
Sidon history.

The good half/quarter condition is absent as well. Since
\(\ell<N/4\), both ranks \(\lfloor N/4\rfloor\) and
\(\lfloor N/2\rfloor\) lie in the shifted cluster, with diameters
between \(M\) and \(M+h\). Their ratio is less than 2. Therefore
this example does not refute the combination of the good-epoch
hypotheses and a full fixed-onset cap. It refutes the broader
terminal-cap and variance-only retention assertion.

The exact sign-sensitive expression remains (23) before its bound,
with \(B_{\rm lin}\) given by (2)--(5). Establishing a useful lower
bound for that expression on the actual good epochs of one fixed
capped history still requires a new estimate. The unmatched born
contribution in (3) cannot be omitted or declared \(O(N^3)\).
No such remaining estimate is proved in this note, and original Q1
and its required Lean verification remain unresolved.

## 8. The bounded exact finite sign check and its reproduction record

Before constructing the analytic family, the following exact Fraction
calculation was executed once on six fixed prefixes of an existing
32-point fixture. This was a sign falsification, not a search over
parameters and not evidence for the limiting theorem. The fixture is
the actual one already recorded in `born_dead_spectral_route.md`.

Observed process: `python3` through `exec_command`; exit code **0**.
The exact code and complete observed output are saved below after the
run. They were not rerun for this recording. Decimal fields in the
output are display-only; signs and reported values come from rational
arithmetic. The execution checked positive-difference uniqueness.

```python
from fractions import Fraction
from itertools import combinations
P=[1,3,4,12,25,29,44,71,89,123,167,197,204,259,273,279,362,410,420,483,519,700,705,800,854,887,971,1032,1259,1297,1421,1518]
for N in (4,8,12,16,24,32):
 A=P[:N]; H=A[-1]-A[0]; F={}
 for j in range(1,N):
  mean=Fraction(sum(A[:j]),j)
  for i in range(j):
   d=A[j]-A[i]
   assert d not in F
   F[d]=(j,Fraction(mean-A[i],H))
 B=Fraction(0); R=Fraction(0); T=0
 for d,e in combinations(F,2):
  t=abs(d-e)
  if t in F:
   term=F[d][1]+F[e][1]
   if F[t][0]<=max(F[d][0],F[e][0]): B+=term
   else: R+=term
   T+=1
 print(N,'B=',str(B),'R=',str(R),'T=',T,'B_float=',float(B))
```

```text
4 B= 3/11 R= 0 T= 9 B_float= 0.2727272727272727
8 B= 43/490 R= 97/210 T= 206 B_float= 0.08775510204081632
12 B= -37654541/2716560 R= 58747/49392 T= 1023 B_float= -13.861111479223725
16 B= -252255203/6261255 R= 101329849/100180080 T= 3669 B_float= -40.2882813429576
24 B= -24979666586339/62912189340 R= 210751642081/5470625160 T= 19150 B_float= -397.05606891758185
32 B= -21933035184794221/15714504285480 R= 6894351086015819/51959248040700 T= 58615 B_float= -1395.7191895044416
```

At \(N=16\), the same literal fixture also has
\(H_8=70\ge2H_4=22\) and \(H_{16}=278\le8H_8=560\).
Its first 16 positive coordinates satisfy \(a_k\le2k^2\) by
inspection. Thus a universal finite sign \(B_{\rm lin}\ge0\) is
already false even with those good-shape inequalities and a finite
all-prefix cap. This does not refute a sufficiently-large-rank
estimate with fixed asymptotic hypotheses; §§3--7 state the precise
scope of the separate limiting family.

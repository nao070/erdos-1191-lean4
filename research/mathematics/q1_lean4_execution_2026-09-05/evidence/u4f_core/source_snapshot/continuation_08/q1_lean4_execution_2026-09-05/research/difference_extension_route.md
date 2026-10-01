# Full difference labels in a finite Sidon extension

Date: 2026-09-05. Research continuation for the original Erdős #1191 Q1.
This note proves finite identities and necessary inequalities. It does not prove
Q1, its negation, or a uniform critical-scale extension obstruction. Nothing in
this note has been checked by Lean. The mathematical statements below have
direct finite proofs; no numerical experiment is used as their proof.

## 1. Exact conventions and the extension equivalence

A finite set of integers is **Sidon** if equal sums determine the same unordered
pair, with repeated summands allowed. Equivalently, its positive differences
have unique ordered endpoints. Write

\[
 \Delta S=\{s'-s:s,s'\in S,\ s<s'\}.
\]

The word "unique" is part of the condition: simply taking a set of differences
would otherwise conceal collisions. In particular, a three-term arithmetic
progression is not Sidon.

For arbitrary disjoint finite sets \(P,B\), put

\[
 C_{P,B}=\{|b-p|:(p,b)\in P\times B\}.
\]

Then \(P\cup B\) is Sidon if and only if all of the following hold:

1. The difference maps within \(P\) and within \(B\) are injective.
2. The map \((p,b)\mapsto |b-p|\) on \(P\times B\) is injective.
3. The three sets \(\Delta P,\Delta B,C_{P,B}\) are pairwise disjoint.

Proof: every unordered pair of different points of the union belongs to exactly
one of these three categories. Positive-difference injectivity of the whole
union is exactly injectivity within, and disjointness between, the categories.
This also proves the statement for interleaved sets. For example, if
\(P=\{0,3\}\), \(B=\{1,2\}\), the two internal difference sets are disjoint,
but the absolute cross map is not injective. Thus the next simplification must
not be applied without the prefix ordering.

Suppose now that \(P<B\), meaning every point of \(P\) is smaller than every
point of \(B\). This is the setting of an actual prefix and its future shell.
Set \(C=B-P\), so that every cross difference is positive. Then the cross map
is injective if and only if

\[
 \Delta P\cap\Delta B=\varnothing.                    \tag{1}
\]

Indeed, a nontrivial equality \(b-p=b'-p'\), after exchanging the two pairs if
necessary, gives \(b'-b=p'-p>0\); the converse follows by reversing this step.
Consequently the exact ordered extension criterion is

\[
\begin{split}
 &P,B\text{ are Sidon},\qquad \Delta P\cap\Delta B=\varnothing,\\
 &(B-P)\cap\Delta P=\varnothing,\qquad
   (B-P)\cap\Delta B=\varnothing.                    \tag{2}
\end{split}
\]

The final two conditions have the equivalent forms

\[
 B\cap(P+P-P)=\varnothing,\qquad
 P\cap(B+B-B)=\varnothing.                            \tag{3}
\]

All repetitions in these sumsets are allowed. For example,
\(b=u+v-w\), with \(u,v,w\in P\), says
\(b-u=v-w>0\), a cross/internal collision; the converse follows from the same
identity. For the second condition, \(p=u+v-w\), with \(u,v,w\in B\), gives
\(v-p=w-u>0\). In particular the case \(u=v\), namely \(p+w=2u\), must not
be discarded.

When (2) holds, the exact update of the used difference bank is

\[
 \Delta(P\cup B)=\Delta P\ \dot\cup\ \Delta B\ \dot\cup\ (B-P), \tag{4}
\]

and every label on the right retains its unique physical pair of endpoints.
Equation (4) is a disjoint union of labels, not just a cardinality identity.

## 2. Exact hypergraph, including mixed three-term progressions

Fix a Sidon prefix \(P\) and a finite candidate set \(V>P\). One may encode
the legal future subsets by a hypergraph on \(V\) with the following forbidden
sets; identical sets in different classes are included only once.

* A singleton \(\{v\}\) if \(v\in P+P-P\).
* A pair \(\{u,v\}\), \(u<v\), if \(v-u\in\Delta P\).
* The set \(\{u,v,w\}\) if \(p+w=u+v\) for some \(p\in P\) and
  \(u,v,w\in V\). Here \(w>u,v\), but \(u=v\) is allowed. This class
  therefore has cardinality **two or three**, not always three.
* Each future Sidon violation \(\{x_1,x_2,x_3,x_4\}\), where
  \(x_1<x_2\le x_3<x_4\) and \(x_1+x_4=x_2+x_3\). Its cardinality is
  **three or four**.

By (2)–(3), \(B\subseteq V\) is independent in this hypergraph if and only if
\(P\cup B\) is Sidon. This formulation keeps the unary, mixed, and internal
conditions separate. Omitting the two-vertex case of the third class or the
three-vertex case of the fourth class would change the theorem.

If

\[
 \min V-\max P>\max(\operatorname{diam}P,\operatorname{diam}V), \tag{5}
\]

then all cross labels are larger than either kind of internal label. Thus the
two mixed conditions in (2) are automatic. Only future Sidon violations and
the old-difference forbidden pairs remain. In particular (5) holds for
\(P\subseteq[1,N]\), \(V=[4N+1,5N]\).

This agrees with the extension reduction in Definition 6.4 of
[Kohayakawa–Lee–Moreira–Rödl, *Infinite Sidon Sets Contained in Sparse Random
Sets of Integers* (2018)](https://doi.org/10.1137/17M1114934).
The primary text inspected for this note is the parent-fetched artifact
`../evidence/goal2_random_sidon_source.json`, whose source is
<https://repositorio.usp.br/bitstreams/ba7fd00d-e405-4f8a-99df-a8224edecfce>.
Its §4.1 explicitly permits a Sidon quadruple with three distinct vertices.
The notation for four-edges in §6.4 must therefore not be used to drop those
violations in an independent exact formulation.

That paper's Definition 6.10 also retains counts of additive relations between
three or four old difference labels through its quantities \(X(S),Y(S)\).
Its goodness hypotheses and extension result concern the construction scale
\((N\log N)^{1/3}\), with further parameters in the random setting. They are
not hypotheses known for every critical-density prefix. No assertion here
transfers its construction theorem to the square-root/logarithm scale.

## 3. A selected-label shadow identity

The following necessary inequality retains where **differences between old
difference labels** land among the new physical difference labels. It is more
information than \(|P||B|\) or \(|\Delta P|\), although its crude scalar
relaxation still has a constant barrier, explained in §6.

Let \(F\subseteq\Delta P\) be any nonempty selected set of old labels. Assign
nonnegative real weights \(u_d\) to these labels and extend \(u\) by zero
off \(F\). Assume \(U=\sum_d u_d>0\), and write

\[
 S=\sum_d u_d^2,\qquad H=\max\{d:u_d>0\},\qquad
 K_u(t)=\sum_d u_d u_{d+t}\quad(t>0).                 \tag{6}
\]

Let \(B\) be a Sidon set with \(m\) points, contained in an integer interval
of length \(L\), and assume \(\Delta B\cap\Delta P=\varnothing\). Full
compatibility (2) implies these hypotheses, but this lemma alone does not
encode the two additional mixed conditions. Define the weighted shadow

\[
 r_B(z)=\sum_{b\in B}u_{z-b},\qquad
 \Psi_u(B)=\sum_{t\in\Delta B}K_u(t).                \tag{7}
\]

The following identities are exact:

\[
 \sum_z r_B(z)=mU,\qquad
 \sum_z r_B(z)^2=mS+2\Psi_u(B).                      \tag{8}
\]

To prove the second one, expand the square. Equal choices of \(b\) contribute
\(mS\). Each unordered pair \(b<b'\) contributes twice
\(K_u(b'-b)\). Sidon injectivity within \(B\) lets us index these terms by
their actual distinct labels \(t\in\Delta B\).

Moreover, \(B\) is disjoint from the support of \(r_B\): a point
\(b'=b+d\in B\), with \(d\in F\), would have a difference in
\(\Delta P\). Both sets lie in an integer interval of length at most
\(L+H\). Cauchy–Schwarz therefore gives the selected-label capacity condition

\[
 \boxed{\quad
  m^2U^2\le (L+H-m)\bigl(mS+2\Psi_u(B)\bigr).
 \quad}                                             \tag{9}
\]

The denominator \(L+H-m\) is positive since \(L\ge m\) and \(H\ge1\).
Equivalently,

\[
 \Psi_u(B)\ge
 \frac12\left(\frac{m^2U^2}{L+H-m}-mS\right)_+ .    \tag{10}
\]

Here \(x_+=\max(x,0)\). The underlying integer support can give a stronger
bound if its actual size is used instead of \(L+H-m\). Formula (9) is valid
for every choice of \(F,u\), for the same actual \(P,B\). Choosing \(u\)
after seeing a finite instance does not alter its validity as a necessary
inequality; a proof requiring a nonanticipating selector would have an
additional obligation.

For \(u=1_F\),

\[
 K_u(t)=R_F(t):=\#\{(d,d')\in F^2:d'-d=t\}.
\]

Thus a large legal extension requires many relations

\[
 (p_2-p_1)-(p_4-p_3)=b'-b,                            \tag{11}
\]

with the two old labels belonging to \(F\) and the new label belonging to
\(\Delta B\). These six-point equations need not violate Sidon: Sidon controls
equal sums of two points, not arbitrary equal sums of three points. It would
be an error to declare the right side of (8) diagonal merely because the
union is Sidon.

## 4. An exact common budget for all future shells

Suppose \(P<B_1<\cdots<B_s\) and their entire union is Sidon. Keep the same
selected old labels and the same weights \(u\) for all shells. Their internal
difference label sets are pairwise disjoint, and none meets \(\Delta P\).
Since

\[
 \sum_{t>0}K_u(t)=\frac{U^2-S}{2},
\]

we obtain the common upper budget

\[
 \sum_{j=1}^s\Psi_u(B_j)
 \le \mathcal E_u(P):=
 \frac{U^2-S}{2}-\sum_{t\in\Delta P}K_u(t).          \tag{12}
\]

Combining (10) and (12) yields an unconditional finite necessary inequality:

\[
 \boxed{\quad
 \sum_{j=1}^s
 \left(\frac{|B_j|^2U^2}{L_j+H-|B_j|}-|B_j|S\right)_+
 \le U^2-S-2\sum_{t\in\Delta P}K_u(t).
 \quad}                                             \tag{13}
\]

All quantities in (13) are defined by physical labels and actual intervals.
There is no independence assumption between the shells and no resetting of
the upper budget for each shell. This is a genuine cumulative constraint,
with a proved upper bound, rather than a request to posit such a bound.
It is nevertheless only a necessary condition for (2).

One can keep still more of the compatibility information. Let
\(A=P\cup\bigcup_j B_j\), and let \(Q=\bigcup_j B_j\). Define

\[
\begin{split}
 T_{P,Q}&=\sum_{p\in P,\ b\in Q}K_u(b-p),\\
 T_{i,j}&=\sum_{b\in B_i,\ c\in B_j}K_u(c-b)\quad(i<j),\\
 T_{\mathrm{unused}}&=\sum_{t>0,\ t\notin\Delta A}K_u(t).
\end{split}
\]

Then (4) and full difference injectivity give the exact conservation law

\[
 \boxed{\quad
 \frac{U^2-S}{2}
 =\sum_{t\in\Delta P}K_u(t)+T_{P,Q}
  +\sum_j\Psi_u(B_j)+\sum_{i<j}T_{i,j}
  +T_{\mathrm{unused}}.
 \quad}                                             \tag{14}
\]

Every term is nonnegative. In particular old/new and cross-shell difference
labels spend the very same budget; they must not be regarded as unrelated
sources. Formula (12) merely drops these nonnegative expenditures. The support
of \(K_u\) is contained in \([1,H-1]\), so sufficiently distant cross pairs
make zero contribution. A lower bound on their total expenditure does not
follow from positivity or from the upper cap on point locations alone.

## 5. A forced old expenditure, with exact endpoint accounting

For the full old label set \(F=\Delta P\), nonnegative weights satisfy

\[
 \sum_{t\in\Delta P}K_u(t)
 \ge\sum_{a<b<c\atop a,b,c\in P}
 u_{c-a}\bigl(u_{b-a}+u_{c-b}\bigr).                 \tag{15}
\]

To see this, each old triple contributes the two pairs of old labels
\(\{b-a,c-a\}\) and \(\{c-b,c-a\}\). The differences between these labels
are respectively \(c-b\) and \(b-a\), both in \(\Delta P\). The two pairs
are distinct since \(P\) has no three-term arithmetic progression. No pair
of labels is used by two different triples: unique endpoints of old labels
identify the two physical intervals. These intervals have either their left
endpoint or their right endpoint in common, and uniquely identify the triple;
the same pair of distinct intervals cannot share both endpoints.

For \(p=|P|\), \(q=\binom p2\), and unit weights on all old labels, (15) gives

\[
 \mathcal E_{1_{\Delta P}}(P)
 \le \binom q2-2\binom p3.                          \tag{16}
\]

There may be additional relations between old labels, which further reduce
the actual available budget. Equation (16) is an upper bound, not an equality.
The forced subtraction has size \(O(p^3)\), while \(\binom q2\) has size
\(p^4/8+O(p^3)\); hence this endpoint accounting alone does not give a
vanishing fraction of the budget as \(p\to\infty\).

## 6. What the fixed-onset critical cap makes (13) demand

Use one-based increasing points \(a_1<a_2<\cdots\), and suppose, for this
calculation only, that a single fixed constant \(C>0\) and a single fixed
onset \(n_0\) satisfy

\[
 a_n\le Cn^2\log(2n)\qquad(n\ge n_0).              \tag{17}
\]

Logarithms in this section are natural; choosing another fixed base changes
\(C\) only. Take \(p\ge\max(n_0,2)\), \(P=\{a_1,\ldots,a_p\}\), and all old
labels with unit weights. Then \(U=S=q=\binom p2\) and
\(H\le Cp^2\log(2p)\). For a future rank shell

\[
 m=2^rp,\qquad B_r=\{a_{m+1},\ldots,a_{2m}\},
\]

one may use the actual interval length
\(L_r=a_{2m}-a_{m+1}+1\). Since \(a_{m+1}\ge1\) and \(m\ge p\), (17) gives

\[
 L_r+H-m\le5Cm^2\log(4m).
\]

Therefore (10) implies the explicit selected-relation demand

\[
 \Psi_{1_{\Delta P}}(B_r)
 \ge\left(\frac{q^2}{10C\log(4m)}-\frac{mq}{2}\right)_+ . \tag{18}
\]

In particular, throughout the range

\[
 m\le\frac{q}{10C\log(4m)},
\]

we have

\[
 \Psi_{1_{\Delta P}}(B_r)\ge\frac{q^2}{20C\log(4m)}. \tag{19}
\]

This range extends from \(m=p\) to order \(p^2/\log p\) for fixed \(C\).
It includes
\(R+1\) shells, where

\[
 R=\log_2p-\log_2\log p+O_C(1).
\]

There are thus order \(\log p\) nontrivial demands, each of normalized order
\(1/\log p\). Crucially their harmonic-looking sum stays bounded:

\[
 \sum_{r=0}^{R}\frac1{\log(4p)+r\log2}\longrightarrow1.
                                                               \tag{20}
\]

For completeness, integral comparison gives the limit
\((\log2)^{-1}\log((\log(4p)+R\log2)/\log(4p))\), and the ratio inside
the logarithm tends to \(2\); the comparison error is \(O(1/\log p)\).
On the other hand (16), divided by \(q^2\), tends to \(1/2\).

Consequently the crude use of (13)–(19) forces only a constant-size expenditure
of a constant-size normalized budget. It does not produce a factor tending
to infinity or force \(C\) to be unbounded. The negative diagonal term in
(18) becomes substantial at \(m\asymp p^2/\log p\). Extending the positive
\(1/\log m\) demand to all later shells would ignore this term and would
give a false proof.

These estimates do **not** construct a compatible infinite sequence at (17),
and do not show that the entire family of weighted inequalities (13) is
insufficient. They precisely locate the failure of its unit-weight,
total-budget relaxation. A hypothetical stronger selection of \(F,u\), or
forced cross-shell spending in (14), has not been ruled out by this
calculation.

## 7. Relation to Q1 and the remaining new arithmetic obligation

The extension equivalence is exact, and (13)–(16) supply a common label budget
valid for every finite segment of an actual Sidon history. Thus the old
forbidden labels are retained through an explicit six-point relation kernel;
they are not replaced by their density or by a factorial lower bound. The
fixed-onset cap in §6 is also maintained for every rank at which it is used.

The unresolved step is a further arithmetical restriction on **which** labels
can spend the budget while the old prefix itself grows. Concretely, a proof
using this route would need one of the following, with full quantifiers:

* A selection of old labels/weights for which the demand side of (13) is
  incompatible with the actual remainder in (14), for every fixed \(C,n_0\)
  and all sufficiently long histories satisfying (17).
* An inverse statement saying that histories which meet these many weighted
  demands must develop specified arithmetic concentration, followed by a
  proof that such concentration is incompatible with (17) and continuing
  extensions. No residue deficiency or concentration conclusion has been
  proved here.
* A way to sum expenditures (14) over growing old prefixes while charging
  each physical relation only a bounded total amount, with a lower bound
  that exceeds that charge under (17). Reusing a fresh \(q^2/2\) budget at
  every old-prefix size is not such a proof.

The two mixed obstructions in (3) are additional exact information for nearby
shells. However, they vanish identically in the separated configuration (5),
so they cannot simply be assumed to contribute a fixed positive loss at
every extension. Likewise the six-point relations in (11) are permitted by
Sidon; bounding them by zero would discard legal histories.

No all-history obstruction under (17) has been obtained. The original Q1
remains unresolved by this route. This note establishes the finite extension
conditions, a label-preserving cumulative inequality, its exact shared
budget including cross-shell terms, and the specific constant barrier of one
relaxation. It does not upgrade those statements to the requested theorem.

## 8. Verification and provenance

The arguments above are finite algebra, set partitions, endpoint injectivity,
and Cauchy–Schwarz; (20) is the stated one-variable integral comparison. No
finite enumeration, floating-point sample, or solver was run for this note.
Accordingly there is no numerical verification result or omitted execution
script to report. Input research notes and the primary-source artifact were
read only. This task's only newly written artifact is this file.

Independent review: `/root/global_route` rederived (9), (13), (14), (15), and
the constant-barrier calculation in §6, and reported agreement. The review
requested the explicit condition \(p\ge2\), incorporated above; this ensures
\(q>0\) and a nonempty old label set. The review also observed that summing
(18) directly over the range used in (19) gives the slightly larger normalized
lower bound \(1/(10C)+o(1)\), since the summed diagonal loss is
\(\sum_{r\le R}2^rp/(2q)=O_C(1/\log p)\). This remains a constant, and
does not change the obstruction to this relaxation.

## 9. Compatible finite histories do not automatically force large residue deficit

This section is a consequence of the construction and estimates in the
independently authored [residue route](residue_route.md), §§5.1–5.5. It extends
that note's single-subset counterexample to an actual finite compatible
history of increasing length. The onset of its cap moves with the finite
construction, as specified below.

For arbitrarily large prime powers \(Q\), put \(N=Q^2-1\). The finite-field
construction in that note gives a Sidon set

\[
 S=\{s_1<\cdots<s_M\}\subseteq[1,N],\quad M=Q,
 \qquad n=\lfloor\sqrt{N/\log N}\rfloor.
\]

For all sufficiently large \(N\), and every \(n\le m\le M\),

\[
 s_m\le N\le3m^2\log(2m).                            \tag{21}
\]

Indeed the last expression is increasing in \(m\), and its value at \(m=n\),
divided by \(N\), tends to \(3/2\). Thus the sorted prefixes
\(P_m=\{s_1,\ldots,s_m\}\) form a **single finite compatible history**
satisfying a cap with the same constant \(3\) at all ranks from \(n\) to
\(M\). This includes

\[
 \left\lfloor\log_2(M/n)\right\rfloor
 =\tfrac12\log_2\log N+O(1)
\]

complete dyadic future shells, a number tending to infinity. Every extension
obeys the entire criterion (2), hence all the weighted inequalities above.

Nevertheless these prefixes do not force the large entropy deficit needed by
the residue route's sufficient zero criterion. Define

\[
 \Gamma(P_m,q)=\log q-H(X_m\bmod q),
\]

where \(X_m\) is uniform on \(P_m\) and \(H\) denotes Shannon entropy.
The near-extremal set \(S\) has, uniformly over
\(q\le\sqrt N/\log N\), normalized residue discrepancy

\[
 \chi_q(S)=q\sum_r\left(\frac{|S_r|}{M}-\frac1q\right)^2
 \ll\frac1{\sqrt{\log N}}.                          \tag{22}
\]

This is exactly the quantitative consequence of Kolountzakis's theorem used
in the residue note, not a distribution assumption imposed on \(P_m\).
Set \(\theta=m/M\), so \(\theta\ge n/M\sim1/\sqrt{\log N}\). The entropy
mixture identity in that note gives

\[
 \Gamma(P_m,q)\le\frac{\chi_q(S)}\theta+
 \frac{h(\theta)}\theta
 \le \log(M/m)+O(1)
 \le\tfrac12\log\log N+O(1).                       \tag{23}
\]

The constants are uniform in \(m,q\) in the displayed ranges.
Here \(h(\theta)/\theta\le\log(1/\theta)+1\), and the case \(m=M\) follows
directly from (22). This argument permits choosing the modulus after seeing
the entire finite history.

The ambient endpoint can also be replaced by each actual endpoint
\(H_m=s_m\). Difference injectivity within \(P_m\) gives

\[
 H_m\ge\binom m2+1\ge\frac{N}{3\log N}
\]

for all sufficiently large \(N\). Consequently
\(\log\log H_m=\log\log N+o(1)\), uniformly in \(n\le m\le M\).
Since \(x\mapsto\sqrt x/\log x\) is increasing for \(x>e^2\), the range
\(q\le\sqrt{H_m}/\log H_m\) is contained in the range of (22).
Thus (23) holds with \(\tfrac12\log\log H_m+O(1)\) on the right for all
moduli relevant to the actual endpoint's sufficient criterion.

These are critical or denser prefixes: uniformly in \(n\le m\le M\),
\(m\sqrt{\log H_m/H_m}\ge1-o(1)\), by \(m\ge n\), \(H_m\le N\), and
the preceding logarithm comparison. For a squarefree modulus, the sum of
marginal prime entropy deficits is at most the joint deficit in (23).
Therefore even actual pointwise Sidon, critical cardinality, compatible
future extensions, and a growing finite string of local caps do not by
themselves force a deficit exceeding \(\log\log H_m\).

**Scope:** the onset \(n\) in (21) tends to infinity with \(N\). These sets
were not made nested as \(Q\) varies, and no bound from one fixed onset across
the infinite history was proved. This is not a counterexample to Q1 or to an
inverse theorem using that stronger history hypothesis. It does refute the
proposed inference if "large compatible future extension" means just one
shell, any fixed number of shells, or the particular growing finite horizon
constructed here.

For the independent review underlying this corollary, I read the residue
note's finite-field Sidon proof, exact thinning expectation, entropy mixture,
and collision-entropy strengthening. I also directly inspected
[Kolountzakis, Theorem 2 and its proof, pp. 2 and 4–5](https://arxiv.org/pdf/math/9808061).
The displayed norm is the unnormalized \(\ell^2\) norm; its constant is
absolute. Taking the deficit parameter zero applies to \(M=Q\ge\sqrt N\).
The proof's small parameter is \(q^{1/2}N^{-1/4}\), at most
\(1/\sqrt{\log N}\) in (22), giving the required uniformity. The subsequent
algebra and the adaptive-modulus conclusion in that note are supported by
this independent review. These statements have not been Lean-verified.

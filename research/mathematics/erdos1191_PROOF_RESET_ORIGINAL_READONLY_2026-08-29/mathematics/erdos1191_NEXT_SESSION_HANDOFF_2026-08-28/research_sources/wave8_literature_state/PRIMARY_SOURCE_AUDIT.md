# Wave 8 primary-source audit against P13

Cutoff: **2026-08-28**. This is a targeted delta from the Wave 7 audit. It does
not repeat Wave 7's compactness, O'Bryant gluing, internal-spectrum packing, or
Hall-completion survey except where needed to locate the new obstruction.

## 1. Exact target and bottom line

For reference, write the six requirements in `core_workspace/proof_obligations.md`
as follows.

- **C1 (survival):** charge only prefixes with
  `surv_C(A_(2m))=infinity`.
- **C2 (orientation):** choose the active cheap child half.
- **C3 (birth split):** distinguish genuinely newborn adjacent differences,
  nested old-half overlap, and already-counted boundary atoms.
- **C4 (repayment):** repay accumulated old-cheap overlap debt by unused
  non-adjacent differences or equal integer-capacity slack.
- **C5 (actual covariance):** identify the repayment quantitatively with both
  newborn-shell covariance and the rank-one mixture terms in the actual `Q_m`.
- **C6 (sublog conclusion):** prove
  \[
  \sum_{j\le J}\left\langle H,
  \frac{Q_{m_j}}{N_{2m_j}}\right\rangle=o(\log J).
  \]

**Qualified conclusion.** The checked primary literature supplies rigorous
pieces on (i) greedy construction, (ii) regular conflict hypergraphs, (iii)
flows and Carleson embeddings on trees, and (iv) unsigned ordered-difference
energy. It does **not** supply a theorem meeting C1--C6, nor a theorem that can
be inserted after merely renaming its variables. The central mismatches are
structural:

1. infinite survival can consist of one ray and gives no quantitative branching
   mass;
2. the prefix-conditioned Sidon conflict system has constraints of sizes
   1, 2, 3, and 4 and is highly irregular;
3. known Fourier/energy identities forget the sign, epoch orientation, and birth
   type that define `Q_m`; and
4. raw unused-difference capacity does not imply the existence of even one legal
   new mark.

The last point has a sharp primary-source witness: Ruzsa constructed extremely
small **maximal** Sidon subsets of an interval.

## 2. Prescribed-prefix completion and the capacity-only obstruction

### 2.1 Ruzsa: very small maximal Sidon sets

Ruzsa constructs a maximal Sidon set (A\subset[1,N]) with

\[
|A|\ll (N\log N)^{1/3},
\]

where maximal means that adjoining any other integer of ([1,N]) destroys the
Sidon property. This is the theorem stated in the official chapter abstract.
[Ruzsa, *A Small Maximal Sidon Set* (1998)](https://link.springer.com/chapter/10.1007/978-1-4757-4507-8_6)

The following consequence is a derivation here, not a separately numbered
theorem of Ruzsa. Since (A) is Sidon,

\[
|\Delta^+(A)|=\binom{|A|}{2}
=O\!\left((N\log N)^{2/3}\right)=o(N).
\]

Thus most numerical difference values in ([1,N]) are unused, yet every
candidate (x\in[1,N]\setminus A) is illegal. Equivalently, translated copies
of the comparatively small old-difference set can cover every candidate
obstruction. Therefore C4 cannot follow from a scalar count of “unused
non-adjacent differences” alone; it needs an injection, matching, expansion, or
other certificate tying each debt atom to distinct usable capacity.

This is not a counterexample to P13: maximality here is only inside ([1,N]) and
says nothing by itself about an infinite branch satisfying the eventual critical
coordinate cap. It is a no-go theorem for any proof that drops C1 and replaces
the repayment map by raw cardinality slack inside the available interval.

### 2.2 Greedy Sidon sequences: a genuine tower, but cubic rather than critical

Cilleruelo records the classical greedy (B_h) construction and proves the
standard bound

\[
a_n\le 2n^{2h-1}.
\]

For (h=2), this is (a_n\le2n^3). His modified strong-(B_h[g]) greedy
algorithm starts from (a_1=1) and proves

\[
a_n\le 2g\,n^{h+(h-1)/g}.
\]

[Cilleruelo, Theorem 2.1, *A greedy algorithm for (B_h[g]) sequences*](https://arxiv.org/abs/1601.00928)

Neither theorem is stated for an arbitrary prescribed prefix, but the same
forbidden-value count gives a useful prefix-relative conclusion. Start from any
finite Sidon prefix (P) with maximum (M), and repeatedly choose the least legal
integer above the current maximum. If a candidate (x) is illegal, then, because
(x>\max P), one of its new differences repeats an old difference:

\[
x-a=b-c
\qquad(a,b,c\text{ in the current prefix},\ b>c).
\]

At a stage with (m) marks there are at most
(m\binom m2=O(m^3)) such values. More importantly, every integer skipped by
the greedy process stays illegal as the prefix grows. Thus all integers skipped
between (M) and the eventual (a_n) are already contained in

\[
\{a+b-c:a,b,c\in A_{n-1},\ b>c\},
\]

and consequently

\[
a_n\le M+n+(n-1)\binom{n-1}{2}=M+O(n^3).
\]

This elementary derivation shows that every finite Sidon prefix has an infinite
cubic-scale continuation. It is not a theorem quoted from Cilleruelo, and it
still falls short of the eventual (O(n^2\log n)) cap in P13.

Cilleruelo's separate explicit infinite Sidon construction does give one
compatible chain, but with
(A(x)=x^{\sqrt2-1+o(1)}), hence
(a_m=m^{\sqrt2+1+o(1)}). It is a special global construction, not a
prescribed-prefix completion theorem and not a critical coordinate tower.
[Cilleruelo, *Infinite Sidon sequences*](https://arxiv.org/abs/1209.0326)

### 2.3 Apparent extension counterexamples are not theorem evidence

arXiv:2604.25214 was the only result of exact catalog searches for “Sidon
extension”. Its current abstract reports computational evidence for two size-four
families, explicitly calls the infinite dilation family “apparent”, and says a
complete proof remains open. It concerns extension to a finite cyclic perfect
difference set, not extension to an infinite integer Sidon branch. It is therefore
excluded from every theorem claim in this audit.

## 3. Mixed-difference conflict graphs: exact hypotheses and the mismatch

### 3.1 The natural fixed-prefix conflict system is nonuniform

Let (A) be the old prefix and (X) a candidate interval for new marks. After
discarding trivial identities, a Sidon violation in (A\cup Y), (Y\subset X),
has the following forms:

\[
\begin{array}{c|l}
\text{number of new variables}&\text{representative obstruction}\\ \hline
1&x+a=b+c,\\
2&x+y=a+b\quad\text{or}\quad x-y=b-a,\\
3&x+y=z+a,\\
4&x+y=z+w.
\end{array}
\]

Hence the literal conflict hypergraph on candidate coordinates has singleton,
2-, 3-, and 4-edges. Degrees depend on the complete old difference and sum
profiles. This encoding is a derivation here; it is included to test the
hypotheses of the primary theorems below.

### 3.2 Bennett--Bohman random greedy independent sets

Bennett--Bohman prove the following. Fix (r\ge3) and (\varepsilon>0).
Let (mathcal H) be an (r)-uniform, (D)-regular hypergraph on (N)
vertices, with (D>N^\varepsilon),

\[
\Delta_\ell(\mathcal H)
<D^{(r-\ell)/(r-1)-\varepsilon}
\quad(2\le\ell\le r-1),
\]

and (Gamma(\mathcal H)<D^{1-\varepsilon}), where (Gamma) is their
maximum ((r-1))-codegree of a pair. Then random greedy produces, with
probability (1-\exp\{-N^{\Omega(1)}\}), an independent set of size

\[
\Omega\!\left(N\left(\frac{\log N}{D}\right)^{1/(r-1)}\right).
\]

[Bennett--Bohman, Theorem 1.1](https://arxiv.org/abs/1308.3732)

The theorem does not cover the literal prefix-conditioned system: it requires one
uniform edge size (r\ge3), exact regularity, and strong codegree bounds, while
the system above begins with singleton and 2-edge obstructions and has degrees
set by the arbitrary old prefix. Removing singleton-forbidden candidates does not
remove the 2/3/4 nonuniformity. Padding to force uniformity is not licensed by the
theorem and could destroy the degree conditions.

### 3.3 Conflict-free hypergraph matchings

Glock--Joos--Kim--Kuehn--Lichev allow a nonuniform **conflict collection**, but
the selectable objects must still be edges of a fixed (k)-uniform,
near-(d)-regular base hypergraph (mathcal H). In their main theorem,

\[
|V(\mathcal H)|\le e^{d^{\varepsilon^3}},\qquad
d_{\mathcal H}(v)=(1\pm d^{-\varepsilon})d,qquad
\Delta_2(\mathcal H)\le d^{1-\varepsilon}.
\]

The conflict hypergraph (mathcal C) has vertices (E(\mathcal H)), conflict
sizes (2\le j\le\ell), and must satisfy

\[
\Delta_1(\mathcal C^{(j)})\le\ell d^{j-1},\qquad
\Delta_{j'}(\mathcal C^{(j)})\le d^{j-j'-\varepsilon}
\quad(2\le j'<j\le\ell),
\]

together with two additional (d^{1-\varepsilon}) bounds for local
interactions of size-two conflicts. The conclusion is a conflict-free matching
covering all but (d^{-\varepsilon^3}|V(\mathcal H)|) base vertices.
[Glock et al., main theorem](https://arxiv.org/abs/2205.05564)

This is closer than a uniform independent-set theorem because (mathcal C) may
have several conflict sizes. It still does not choose raw integer coordinates.
One first needs a fixed-(k) incidence encoding in which a legal new mark is an
edge of (mathcal H), disjoint base edges represent compatible choices, and all
old--new/new--new collisions become conflicts satisfying every displayed degree
bound. No checked source constructs or verifies that encoding for a prescribed
Sidon prefix, much less under C1. Thus the theorem supplies a possible proof
architecture, not C3 or C4 themselves.

## 4. Infinite survival, branching flows, and Carleson assumptions

### 4.1 Survival does not imply quantitative branching

For a locally finite rooted tree (T), Lyons defines

\[
\operatorname{br}T
=\sup\left\{\lambda:\exists\text{ nonzero flow }\theta,
\ 0\le\theta(e)\le\lambda^{-|e|}\ \forall e\right\}
\]

and, by max-flow/min-cut, equivalently

\[
\operatorname{br}T
=\sup\left\{\lambda:
\inf_{\Pi}\sum_{e\in\Pi}\lambda^{-|e|}>0\right\},
\]

where (Pi) ranges over root-to-infinity cutsets.
[Lyons, *Random Walks and Percolation on Trees*, Proposition 2.1 and the
branching-number definition](https://rdlyons.pages.iu.edu/pdf/rwpt.pdf)

Apply this to the extension tree below a prefix with `surv_C(P)=infinity`.
König's lemma gives a ray, but the surviving subtree may be exactly that ray. For
a one-ray tree, the level-(n) cutset has weight (lambda^{-n}), so the infimum
is zero for every (lambda>1) and

\[
\operatorname{br}T=1.
\]

This calculation is a direct consequence of Lyons's formula. It proves that C1
alone cannot manufacture an exponentially decaying boundary measure, positive
branching entropy, or a Kraft budget with uniform slack. Any tree-potential proof
must establish an additional arithmetic cutset/flow estimate, or work along a
single distinguished ray without pretending that survival supplies branching.

### 4.2 Tree Carleson embedding assumes the missing budget

Arcozzi--Holmes--Mozolyako--Volberg prove a dyadic-tree embedding theorem. With
a tree measure (Lambda) and nonnegative (alpha_I), if for every node (I)

\[
\frac1{|I|}\sum_{K\subset I}\alpha_K(\Lambda)_K^2
\le(\Lambda)_I,
\]

then

\[
\frac1{|I_0|}\sum_{I\subset I_0}
\alpha_I(\varphi\sqrt\Lambda)_I^2
\le4(\varphi^2)_{I_0}.
\]

[Arcozzi et al., Carleson embedding theorem for a dyadic tree](https://arxiv.org/abs/1809.03397)

The theorem is a valid downstream tool only after the displayed Carleson testing
condition is proved. Infinite extension survival does not imply that condition,
and the paper contains no arithmetic identification of (alpha_I), (Lambda), or
(`varphi`) with P13 overlap debt and `Q_m`. It therefore relocates rather than
solves C4--C5.

## 5. Ordered differences and covariance: what the exact identities retain

### 5.1 Ortega--Prendiville: a useful Fejer identity, but unsigned

For a Sidon set (S\subset[N]), define the normalized Fejer kernel

\[
\mu_H(h)=\frac{(1_{[H]}*1_{-[H]})(h)}{\lfloor H\rfloor^2}.
\]

Lemma 2.2 gives the exact identity and lower bound

\[
\begin{aligned}
\sum_{h\in(S-S)\setminus\{0\}}\mu_H(h)
&=\sum_h(1_S*1_{-S})(h)\mu_H(h)
-\frac{|S|}{\lfloor H\rfloor},\\
\sum_h(1_S*1_{-S})(h)\mu_H(h)
&=\frac1{\lfloor H\rfloor^2}
\sum_h(1_S*1_{[H]})(h)^2
\ge\frac{|S|^2}{N+H}.
\end{aligned}
\]

[Ortega--Prendiville, Lemma 2.2](https://arxiv.org/html/2110.13447)

Their Fourier-uniformity theorem also states

\[
\left\|\widehat{1_S}-\frac{|S|}{N}\widehat{1_{[N]}}\right\|_\infty
\ll N^{1/2}
\left(\left|\frac{|S|}{N^{1/2}}-1\right|+N^{-1/6}\right)^{1/2},
\]

with (-1/6) improvable to (-1/4) in their Theorem 6.3.
[Ortega--Prendiville, Theorem 1.2](https://www.numdam.org/articles/10.5802/jtnb.1239/)

Two precise limitations follow.

1. The convolution square is nonnegative and sums all ordered differences. It
   has no label for cheap versus expensive half, newborn versus old-overlap
   atoms, or the rank-one component of `Q_m`.
2. P13 does not assume finite extremality (|S|=(1+o(1))\sqrt N). At the hard
   cap scale (N\asymp m^2\log m) with (|S|\asymp m), one has
   (|S|/\sqrt N\asymp1/\sqrt{\log m}), so the defect term stays of order one
   and the theorem gives no uniform small Fourier error. This is a scale check,
   not a criticism of the theorem in its intended extremal regime.

The lemma is an exact additive-energy identity adjacent to C5, but it cannot be
identified with the actual signed P13 covariance without a new, label-preserving
decomposition.

### 5.2 Tafula: matched-even block energy reaches the harmonic barrier

Tafula defines (r_{A,\mathbf b}(n)) using pairwise-distinct ordered tuples. For
(mathbf b=(c_1,-c_1,\ldots,c_k,-c_k)), Theorem 1.1 proves:

\[
\frac{A(x)}{(x/\log x)^{1/(2k)}}\to\infty
\Longrightarrow
\frac1x\sum_{|n|\le x}r_{A,\mathbf b}(n)\to\infty,
\]

and (A(x)\gg x^{1/(2k)}) implies the same normalized average is
(gg\log x). For a dyadic block
(B_N=\{a_{N+1},\ldots,a_{2N}\}), Lemma 2.1 gives

\[
S_{A,\mathbf b}(x;N)
\gg_{\mathbf b}
\frac{xN^{2k}}{\max\{x,a_{2N}-a_N\}}.
\]

The proof is a nonnegative Fourier integral with a triangular Fejer weight.
[Tafula, Theorem 1.1 and Lemma 2.1](https://link.springer.com/article/10.1007/s00605-026-02211-4)

For (k=1), (mathbf b=(1,-1)), and a Sidon set, nonzero ordered
differences have multiplicity at most one. If a difficult block has diameter
(a_{2N}-a_N\asymp N^2\log N), the lemma's normalized contribution is only
of order (1/\log N). Along dyadic (N=2^t), these unsigned contributions
sum like

\[
\sum_{t\le T}\frac1t=\Theta(\log T).
\]

This harmonic-scale calculation is a derivation from the lemma, not Tafula's
claim about `Q_m`. It explains why an unsigned positive-energy estimate is not
enough for C6: P13 needs a genuinely signed cancellation or a survival-conditioned
repayment stronger than summing per-scale mass.

Tafula's general zero-sum gap theorem likewise constrains aggregate
representations; it does not orient epochs or track overlap debt.

## 6. Condition-by-condition map

Here `analogue` means a mathematically rigorous neighboring statement, not a
verified implication to P13.

| Primary result | C1 | C2 | C3 | C4 | C5 | C6 | Exact reason it stops |
|---|---|---|---|---|---|---|---|
| Ruzsa small maximal set | no | no | no | obstruction | no | no | Shows scalar unused capacity can coexist with zero legal in-interval children; survival hypothesis absent. |
| Cilleruelo greedy (B_h[g]) | no | no | weak forbidden-type count | no | no | no | Published theorem has fixed initialization; the derived arbitrary-prefix continuation is only cubic and has no debt/covariance bookkeeping. |
| Bennett--Bohman random greedy | no | no | analogue | no | no | no | Requires one (r\ge3) uniform, regular, low-codegree hypergraph. |
| Glock et al. conflict-free matching | no | no | architecture only | conditional architecture | no | no | Needs a fixed-(k) near-regular incidence encoding and verified conflict degrees. |
| Lyons branching-number flow | diagnoses C1 | no | no | analogue only | no | no | Survival may be one ray with branching number 1. |
| Tree Carleson embedding | no | no | no | assumes budget | analogue only | bounded (L^2), not C6 | The needed testing inequality is a hypothesis, not a consequence of survival. |
| Ortega--Prendiville Fejer identity | no | no | loses birth labels | no | unsigned analogue | no | Convolution aggregates all differences and forgets epoch signs/rank-one mixture. |
| Tafula matched-even energy | no | no | removes repeated coordinates only | no | unsigned analogue | harmonic, not sublog | Positive dyadic contributions are naturally (1/\log N) at critical block diameter. |

No checked row satisfies even C1+C2 simultaneously. No checked row contains the
actual `Q_m` decomposition required by C5.

## 7. What this rules out, and what it leaves open

The primary sources rule out the following shortcuts:

1. **Capacity count alone:** Ruzsa's maximal sets show it cannot prove a child
   exists, much less debt repayment.
2. **Survival implies a useful boundary measure:** a one-ray surviving tree has
   branching number 1.
3. **Invoke random greedy/nibble abstractly:** the literal Sidon conflict system
   fails the published uniformity/regularity interface until a new encoding and
   codegree proof are supplied.
4. **Replace `Q_m` by total additive energy:** the exact Fejer identities are
   unsigned and reach the harmonic scale rather than sublogarithmic cancellation.
5. **Use a tree Carleson theorem as the budget proof:** the arithmetic Carleson
   testing condition is precisely what remains to be established.

The literature does leave three concrete proof interfaces worth attacking:

- construct a **label-preserving** decomposition of the ordered-difference
  convolution into newborn, old-overlap, boundary, and rank-one terms;
- build a fixed-uniformity incidence model for batches of new marks and prove the
  Glock/Bennett degree conditions after conditioning on an infinitely surviving
  prefix; or
- prove directly an arithmetic cutset/Carleson inequality on the surviving
  extension subtree. The inequality must be new: mere nonempty boundary is
  insufficient.

These are research directions, not claims that any of the cited theorems already
delivers P13.

## 8. Self-critique and qualified null

This review does **not** prove that a P13 bridge theorem is absent from all
literature. The local state did not meet its mechanical global-saturation gate;
generic tree and Crossref searches continued to find new, mostly irrelevant
records. The qualified null is restricted to the four logged clusters, exact-title
searches, and citation trails in `QUERY_LOG.md`.

Potential sources of residual miss risk include older undigitized terminology,
results phrased as constrained graceful labeling rather than Golomb extension,
and a specialized irregular-hypergraph theorem not indexed under Sidon language.
Against that risk, the review used three bibliographic scripts, Exa, Firecrawl,
SciSpace, the arXiv catalog/LaTeX/citation graph, and official publisher pages.
Consensus was quota-blocked. Retrieval engines were never used as sole theorem
authority.

The strongest defensible conclusion is therefore:

> Within the recorded searches through 2026-08-28, no primary theorem was located
> that supplies the survival-conditioned, orientation-sensitive, label-preserving
> debt repayment and actual-`Q_m` covariance needed for P13. Several exact primary
> results explain why the obvious capacity, branching, nibble, and unsigned-energy
> substitutions are insufficient.

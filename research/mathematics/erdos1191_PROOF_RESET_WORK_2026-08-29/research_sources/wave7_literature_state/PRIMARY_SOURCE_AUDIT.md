# Wave 7 primary-source audit: nested Sidon/Golomb towers and reset-renewal analogues

Cutoff: **2026-08-28**. This is a tightly scoped scoping review, not a novelty search or a proof of absence. “Not located” below always means “not located by the recorded searches and citation trails,” never “does not exist.” Preprints are identified as such.

## Bottom line

The search located several close ingredients, but no checked primary source that does the whole job: construct one integer Sidon sequence whose prescribed finite prefixes remain under a critical $O(m^2\log m)$ coordinate envelope while quantitatively controlling mixed old–new and new–new difference shells across all epochs.

The closest direct ingredients are:

1. a quantitative two-block gluing/deletion lemma for $g$-Golomb rulers, with the published iteration using cubic scale jumps;
2. a compactness/diagonal principle showing that uniform finite prefix feasibility would be enough for an infinite tower;
3. sharp packing results for *separate internal* Golomb-ruler difference spectra, which omit the mixed cross-block differences needed by a nested union;
4. qualitative completion of every finite Sidon set to an infinite perfect difference set, with no useful size control; and
5. exact Kraft/energy amortizations in adjacent combinatorial settings, without a proved encoding of Sidon reset shells into those settings.

These are useful reductions and obstructions, not an asymptotic resolution.

## 1. Global and compatible-prefix Sidon/Golomb sequences

### 1.1 Current global upper obstruction and the nearest quantitative gluing lemma

Kevin O’Bryant’s 2026 preprint proves that every infinite $g$-Golomb ruler $\mathcal A$ satisfies

\[
\liminf_{n\to\infty}\frac{|\mathcal A\cap[0,n)|}{\sqrt{n/\log n}}
\le \frac{2\sqrt g}{\sqrt{\log 2}},
\]

and hence, for $\mathcal A=\{a_1<a_2<\cdots\}$,

\[
\limsup_{m\to\infty}\frac{a_m}{m^2\log m}\ge \frac{\log 2}{2g}.
\]

This is an obstruction on infinitely many scales, not a nonexistence result for a larger all-prefix envelope such as $a_m\le 2Cm^2\log m$. [O’Bryant, Theorem 1 and Corollary 2, arXiv:2606.28651v3 (preprint)](https://arxiv.org/abs/2606.28651)

The same paper’s Lemma 9 is the closest checked theorem to a nested-block extension oracle. If $\mathcal V\subset[0,V_2)$ and $\mathcal W\subset[W_1,W_1+m)$ are $g$-Golomb rulers and

\[
W_1-V_2\ge \max\{V_2,m\},
\]

then some $\mathcal W^*\subseteq\mathcal W$ obeys

\[
|\mathcal W^*|\ge |\mathcal W|-g\binom{|\mathcal V|}{2},
\qquad
\mathcal V\cup\mathcal W^*\text{ is a }g\text{-Golomb ruler}.
\]

The proof explicitly separates $VV$, $VW$, and $WW$ differences, deletes endpoints of $WW$-pairs colliding with $VV$-differences, and then obtains uniqueness of $VW$-differences. Its actual iteration sets $q_{i+1}=q_i^3$. Thus it controls mixed differences rigorously, but does so with a quadratic deletion allowance and very large scale separation, not a critical compatible-prefix bound. [O’Bryant, Lemma 9 and proof of Theorem 3](https://arxiv.org/html/2606.28651v3#S4)

**Citation trail.** O’Bryant describes the construction as following Halberstam–Roth, uses finite $g$-Golomb rulers quoted from Caicedo–Martos–Trujillo, and sharpens the Erdős/Cilleruelo infinite upper-bound line. Those antecedents control density or isolated finite rulers; Lemma 9 is the checked point at which old–old, old–new, and new–new differences are handled together.

### 1.2 Best checked global lower construction remains supercritical for this purpose

Cilleruelo constructs an explicit infinite Sidon sequence with

\[
A(x)=x^{\sqrt2-1+o(1)}.
\]

Equivalently, its $m$-th element has scale $m^{1/(\sqrt2-1)+o(1)}=m^{\sqrt2+1+o(1)}$, so this construction is much sparser than an $m^2\operatorname{polylog}m$ target. It matches the exponent in Ruzsa’s earlier probabilistic construction. [Cilleruelo, Theorem 1.2, arXiv:1209.0326v2 / Advances in Mathematics](https://arxiv.org/abs/1209.0326), [Ruzsa, *An Infinite Sidon Sequence*, JNT 68 (1998)](https://doi.org/10.1006/jnth.1997.2192)

This is already one compatible prefix chain in the formal sense—every prefix of a Sidon sequence is Sidon—but not at the desired critical coordinate scale.

### 1.3 Compactness turns uniform finite feasibility into an infinite tower

Riblet–Schehr prove that the generating functions of Sidon subsets of $\mathbb N$ form a compact subset of $\mathcal O(\mathbb D)$, and more generally that closed subsets of $\mathcal P(\mathbb N)$ are compact in the discrete product topology for their continuous-extremizer theorem. They explicitly note that the $B_h[g]$ constraints are closed because any violation is witnessed by finitely many elements. [Riblet–Schehr, Theorems 1.1 and 6.3, DOI 10.1007/s10474-026-01604-z](https://doi.org/10.1007/s10474-026-01604-z)

An elementary consequence useful here (this sentence is a derivation, not a theorem numbered by the authors) is:

> If fixed integer caps $B_m$ have the property that, for every depth $M$, there exists a length-$M$ Sidon sequence $0=a_1<a_2<\cdots<a_M$ with $a_m\le B_m$ for all $m\le M$, then there is one infinite Sidon sequence satisfying every cap.

Proof: make a rooted tree whose level-$M$ vertices are the feasible prefixes. Each level is nonempty and each vertex has finitely many children because $a_{M+1}\le B_{M+1}$. König’s infinity lemma gives an infinite branch. This identifies a valid local-to-global route, but supplies no finite feasibility theorem at $B_m\asymp m^2\log m$.

### 1.4 A genuine nested construction with relaxed, difference-dependent multiplicity

Gupta–O’Bryant define an LM ruler by

\[
r_{\mathcal L-\mathcal L}(d)\le d-1\quad(d\ge1)
\]

and construct one infinite LM ruler $\mathcal S=\{h_m:m\ge0\}$ whose every prefix $\mathcal S_n$ has diameter at most

\[
\frac74\big((n+1)^{3/2}-(n+1)\big).
\]

This is a real all-prefix tower, but it is explicitly not Sidon: the allowed multiplicity grows with the difference $d$. It is therefore a useful countermodel for which parts of a nested proof use injectivity rather than merely a growing local multiplicity budget. [Gupta–O’Bryant, Definition 2 and Theorem 12, arXiv:2605.14229 (preprint)](https://arxiv.org/abs/2605.14229)

## 2. Difference-spectrum and interval packing

### 2.1 Separate internal spectra: sharp threshold, but no mixed differences

For a $t$-mark Golomb ruler $A$, Ma–Yi define $\Delta^+(A)$ and let $P_t(U)$ maximize the union of pairwise-disjoint internal spectra $\Delta^+(A_i)\subset[1,U]$. Their Theorem 1.1 states

\[
P_t(U)=U-o(U)\quad\Longleftrightarrow\quad 3\le t\le5.
\]

For fixed $t\ge6$, their Fourier obstruction gives

\[
\liminf_{U\to\infty}\left(1-\frac{P_t(U)}U\right)
\ge \frac{(t-1)\gamma_0-2}{2(t-2)},
\quad \gamma_0=0.4344672564\ldots,
\]

so the six-mark leave is at least $2.1542035\%$. [Ma–Yi, Theorems 1.1 and 3.1, arXiv:2608.13739v1 (preprint)](https://arxiv.org/abs/2608.13739)

The limitation is exact and important: the theorem packs the sets of differences *inside separate rulers*. If two rulers are later united as old and new marks, none of the $|A_i||A_j|$ mixed differences is part of $P_t(U)$. Thus this theorem neither constructs nor obstructs a nested Sidon union without an additional mixed-difference argument.

**Citation trail.** The positive side uses perfect-difference-family spectra for $t=3,4$ and Mathon’s recording of Wild’s product construction with five-mark seeds of orders $121$ and $161$. The negative side relates the problem to difference triangle sets and to Lorentzen–Nilsen/Shearer bounds. These are all families of distinct *internal* spectra.

### 2.2 Disjoint rulers versus disjoint difference spectra

Xu–Xiu–Fan–Liang study $(I,J,n)$-DGRs: $I$ pairwise-disjoint $J$-mark Golomb rulers inside $\{1,\dots,n\}$. Their disjointness is of the mark sets. It does not require different rulers’ positive-difference sets to be disjoint, and it does not assert that their union is a Golomb ruler. [Xu–Xiu–Fan–Liang, arXiv:2409.14409 (preprint)](https://arxiv.org/abs/2409.14409)

Gupta’s modular-to-ordinary theorem starts from one modular ruler, folds modulo a divisor, deletes modular collisions, then cuts at a large gap to obtain one ordinary $g$-Golomb ruler with a finite-$n$ diameter bound. The choices are not shown compatible as $n$ varies. [Gupta, Theorem 3, arXiv:2607.07931 (preprint)](https://arxiv.org/abs/2607.07931)

### 2.3 Finite cyclic perfect difference sets do not automatically form a tower

Singer’s construction gives a perfect difference set of size $q+1$ in the cyclic group of order $q^2+q+1$ for each prime power $q$. Modern finite-field descriptions remain at a single group/order and do not provide inclusions compatible across $q$. [Mészáros–Rónyai–Szabó, discussion and Theorem 1.1, arXiv:1908.05591](https://arxiv.org/abs/1908.05591)

Barré–Pichot prove a useful exact modulus fact for any finite integer Sidon sequence $0=a_0<\cdots<a_n$: $2a_n+1$ is the smallest $N_0$ such that the sequence is Sidon modulo every $N\ge N_0$. This lets each fixed prefix be moved safely to sufficiently large moduli, but gives neither one fixed modulus nor compatible perfect difference sets containing all prefixes. [Barré–Pichot, Proposition 7.1, DOI 10.4171/LEM/1097](https://doi.org/10.4171/LEM/1097)

### 2.4 Two-set spectrum disjointness has a genuine lacunarity theorem

Fang–Sándor call $A,B\subset\mathbb N_0$ disjoint when

\[
(A-A)\cap(B-B)=\{0\}.
\]

If $A(x_n)B(x_n)/x_n\to2$ along a sequence with $x_{n+1}\ge2x_n$ eventually, their Theorem 1.2(i) proves that necessarily $x_{n+1}/x_n\to\infty$; conversely, every scale sequence with this latter ratio divergence supports disjoint $A,B$ attaining the ratio $2$. Their Theorem 1.1 also determines the product profile on fixed proportional windows below and above such extremal scales. This is an exact cross-spectrum packing/renewal phenomenon. [Fang–Sándor, Theorems 1.1–1.2, arXiv:2208.11357v1 (preprint)](https://arxiv.org/abs/2208.11357)

It is adjacent rather than a solution here: the condition separates the *two internal difference sets*, but does not require either internal spectrum to be collision-free, and it omits the mixed differences created by $A\cup B$. Thus its forced scale lacunarity cannot be transferred to nested Sidon epochs without a new encoding.

## 3. Perfect difference sets containing prescribed Sidon data

### 3.1 Finite cyclic completion is false in general

Alexeev–Mixon prove:

- $\{1,2,4,8\}$ does not extend to a perfect difference set modulo $p^2+p+1$ for any prime $p$ (Theorem 8);
- $\{1,2,4,8,13\}$ does not extend to a finite perfect difference set modulo any $v>0$ (Theorem 9).

They also verify Hall’s earlier example, a translate of $\{-8,-6,0,1,4\}$. Therefore finite perfect-difference completion cannot be used as a universal prescribed-prefix step. [Alexeev–Mixon, arXiv:2510.19804v2 (preprint)](https://arxiv.org/abs/2510.19804)

**Citation trail.** The source traces the negative result to Marshall Hall, Jr., *Cyclic projective planes*, Duke Math. J. 14 (1947), Theorem 3.1 and related projective-plane arguments, [DOI 10.1215/S0012-7094-47-01482-8](https://doi.org/10.1215/S0012-7094-47-01482-8). Alexeev–Mixon give new small counterexamples and a Lean-checked reconstruction of Hall’s route.

### 3.2 Finite-to-infinite completion is qualitatively positive, without growth control

Alexeev–Mixon’s Claim 10, citing Hall’s Theorem 3.1, states that every finite Sidon set extends to an infinite perfect difference set. The proof is a greedy one: when a difference $d$ is missing, choose $x$ avoiding finitely many obstructions and add $x,x+d$. No quantitative bound on $x$, on the next mark, or on all-prefix density is asserted. The same paper recalls that an arbitrary *infinite* Sidon set need not be contained in an infinite perfect difference set; $\{2b:b\in B\}$ for an infinite perfect difference set $B$ is a counterexample. [Alexeev–Mixon, Claim 10](https://arxiv.org/html/2510.19804v2#S2)

### 3.3 Dense perfect difference constructions perturb/rescale rather than preserve the seed

Cilleruelo–Nathanson’s Theorem 1 says that for every Sidon set $B$ and every $\omega(x)\to\infty$, there is a perfect difference set $A\subset\mathbb N$ with

\[
A(x)\ge B(x/3)-\omega(x).
\]

Their construction begins with a scaled copy $3B$, deletes a sparse exceptional part, and adds a sparse correction sequence. The paper explicitly says this *perturbs* a Sidon set and also gives an infinite Sidon set that cannot be a subset of any perfect difference set. It is not a theorem that $B\subseteq A$. [Cilleruelo–Nathanson, Theorem 1 and §4.2, arXiv:math/0609244 / Combinatorica](https://arxiv.org/abs/math/0609244)

Chen–Fang improve the rescaling coefficient from $1/3$ to $1/2$: their version-of-record theorem constructs a perfect difference set $A$ with

\[
B(x/2)-\omega(x)\le A(x)\le B(x/2)+\omega(x)
\]

for all sufficiently large $x$. This is a stronger density-transfer theorem, still not prescribed-prefix containment. The article was published online in 2026 and is assigned to the January 2027 issue. [Chen–Fang, Theorem 1.1, DOI 10.1016/j.jcta.2026.106239](https://doi.org/10.1016/j.jcta.2026.106239)

## 4. Renewal/Carleson-type budgets

### 4.1 A genuine Sidon block-energy amortization

O’Bryant’s proof of the infinite upper bound uses shifted length-$N$ block counts $F_\ell^{(t)}$. Difference injectivity gives the exact averaged estimate

\[
\sum_{t=0}^{N-1}\sum_{\ell}\binom{F_\ell^{(t)}}2
\le g\sum_{d=1}^{N-1}(N-d)
=\frac{gN(N-1)}2.
\]

Hence some shift $t^*$ has $\sum_\ell\binom{F_\ell}2\le g(N-1)/2$. Weighted Cauchy with $w_\ell=(\ell\log(\ell N))^{-1/2}$ then yields the liminf theorem above. This is an exact arithmetic amortization across spatial blocks at one scale. The author notes possible reverse-martingale or entropy interpretations only as nonrigorous directions; the paper does not give a renewal theorem for nested reset epochs. [O’Bryant, Lemma 6 and equation (6)](https://arxiv.org/html/2606.28651v3#S3)

### 4.2 An exact Carleson/Kraft analogue in a different category

Sudakov–Tomon–Wagner prove for every antichain $\mathcal F\subset2^{\mathbb N}$ that

\[
\sum_{n\ge1}\frac{|\mathcal F\cap2^{[n]}|}{2^n}\le2,
\]

by converting maximal-element layers into a prefix code and applying Kraft’s inequality. [Sudakov–Tomon–Wagner, Proposition 2.1, arXiv:2008.04804 / JCTA](https://arxiv.org/abs/2008.04804)

This is exactly the shape of a discrete Carleson budget, but it is only an analogy here. No checked source supplied an injective/prefix-free coding from nested Sidon difference collisions, newborn shells, or reset profiles to this antichain family. Using the inequality in the Sidon problem therefore requires a new proved encoding, not just a change of terminology.

Conlon–Fox–Sudakov prove another adjacent infinite-prefix sparsity theorem for $K_{s,t}$-free graphs, but their Theorem 4.1 concerns minimum degree of graph prefixes. They introduce Sidon sets as motivation, not as a transfer theorem. [Conlon–Fox–Sudakov, Theorem 4.1, arXiv:1910.08661](https://arxiv.org/abs/1910.08661)

## 5. Qualified null results from this search

The recorded searches did **not locate** a primary theorem with any of the following exact conclusions:

- one Sidon/Golomb sequence satisfying a critical $O(m^2\log m)$ coordinate bound for every prefix index $m$;
- a compatible family of finite Singer/Bose/other algebraic rulers nested under literal inclusion with uniform integer coordinate control;
- a Hall-type completion bound that extends an arbitrary prescribed finite Sidon prefix while bounding the next coordinates by a critical envelope;
- a difference-packing theorem that simultaneously handles internal old–old, internal new–new, and all mixed old–new differences across many nested epochs without the large-gap/deletion loss of O’Bryant’s Lemma 9;
- an arithmetic renewal or Carleson embedding theorem for reset-profile signs/locations or newborn difference shells.

These are qualified nulls only. The queries were deliberately narrow; terminology may differ; older non-digitized sources and papers outside the citation trails may have been missed. In particular, the absence of an exact phrase such as “nested Golomb ruler” is not evidence that the mathematical idea is new.

## 6. What the literature suggests testing next (not a theorem claim)

1. **Use compactness as the logical endgame.** A finite-depth solver that establishes the same coordinate caps at every depth would already imply one infinite branch; it need not output mutually compatible witnesses itself.
2. **Measure the precise loss in O’Bryant gluing.** The $g\binom{|V|}{2}$ deletion term and gap condition isolate the two quantities a critical construction must improve.
3. **Do not substitute internal-spectrum packing for mixed-spectrum control.** Ma–Yi is highly relevant for shell capacity, but the old–new spectrum remains the missing term.
4. **Treat perfect-difference completion as qualitative.** Hall completion can finish a finite seed eventually, while Alexeev–Mixon rules out a universal finite cyclic completion and neither route supplies critical coordinates.
5. **If using a Carleson analogy, first exhibit the code.** A rigorous prefix-free or bounded-overlap encoding of reset events is the missing bridge to the exact Kraft inequality.

## Source-status note

Peer-reviewed/version-of-record sources used above include Ruzsa (1998), Cilleruelo–Nathanson (2008), Cilleruelo (2014), Sudakov–Tomon–Wagner (2021), Barré–Pichot (2026 issue; online 2025), Riblet–Schehr (2026), and Chen–Fang (published online 2026; January 2027 issue). O’Bryant, Gupta, Gupta–O’Bryant, Ma–Yi, Xu–Xiu–Fan–Liang, Alexeev–Mixon, Mészáros–Rónyai–Szabó, and Fang–Sándor were checked at the cited arXiv versions; where a journal version was not located in this bounded pass, their results are treated as preprints.

## Methodology and adversarial self-critique

The scripted discovery pass ran 14 OpenAlex, Crossref, and arXiv query rounds, retained 316 deduplicated records, and reached the tool’s recorded per-source saturation threshold. A malformed arXiv query produced one HTTP 400 and contributed no records. Automatic relevance ranking produced lexical false positives, so primary mathematical screening and theorem-text verification overrode the ranked list. Consensus was quota-blocked; SciSpace supplied one adjacent lead but also duplicated it with malformed metadata; a hosted Firecrawl search returned only generic listing pages. Exact queries, counts, failures, thresholds, identifiers, and replay commands are in [QUERY_LOG.md](QUERY_LOG.md).

The adversarial review checked anchoring, single-source dependence, venue and author concentration, recency, citation bias, logical tensions, review archetype, preprint status, methodology disclosure, search saturation, counterarguments, formula fidelity, and long-horizon risk. Revisions explicitly separate:

- direct Sidon/Golomb theorems from Carleson, graph, and two-set packing analogies;
- qualitative finite-seed completion from quantitatively bounded next-coordinate extension;
- disjoint internal spectra or disjoint mark sets from injectivity of the full union spectrum;
- compactness of feasible prefixes from the missing uniform finite-feasibility result; and
- convergence of the recorded queries from any claim of literature completeness.

The unresolved epistemic risk is terminology drift or an older undigitized result outside these citation trails. That risk is why every negative search statement is qualified and why this report makes no novelty claim.

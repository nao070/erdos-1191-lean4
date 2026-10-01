# Wave 5 literature delta: cross-epoch compatibility and innovation budgets

**Search date:** 2026-08-28  
**Coverage claimed:** a bounded primary-source search through 2026-08-28  
**Status:** `QUALIFIED_NULL_FOR_THE_MISSING_BUDGET`

## 1. Bottom line

Starting from the existing anti-Eulerian report and the Wave 4 global-history
delta, this search found no primary theorem that proves, for one globally
compatible critical Sidon sequence,

\[
 \sum_{j\le J}
 \left\langle H_{j+1},\frac{Q_j}{N_{j+1}}\right\rangle=o(\log J),
 \qquad\text{or equivalently the required }o(\log J)
 \text{ gap-variance budget.}
\]

It also found no theorem constructing one integer Sidon sequence
\(0=a_1<a_2<\cdots\) with the all-prefix bound
\(a_m=O(m^2\operatorname{polylog}m)\), no packing theorem controlling all
cross-epoch mark differences, and no theorem converting the already proved
\(\Omega(1/\log M)\) diameter-profile reset into an upper bound for the actual
signed covariance innovations.

There are, however, two useful exact partial bridges.

1. Riblet--Schehr's compactness theorem gives a rigorous local-to-global
   diagonal step: **uniform finite all-prefix towers at every depth would
   already imply one infinite tower with the same coordinate envelope.** It
   does not construct those towers or control innovations.
2. Infinite-antichain and infinite \(K_{s,t}\)-free-graph theorems give genuine
   unbounded-history Kraft/Hölder budgets. Their hypotheses provide the
   prefix-free or forbidden-subgraph structure that makes the summation work;
   no primary source supplies an encoding of persistent Sidon difference
   births into either structure.

Thus the result is a qualified null, not an absence or novelty claim.

## 2. Exact target used for screening

A source was counted as a possible bridge only if it supplied at least one of
the following with the needed quantifiers.

- **Compatible density:** one infinite integer Sidon set with a bound at every
  sufficiently large prefix, rather than unrelated optimal finite rulers or a
  limsup subsequence.
- **Cross-epoch arithmetic:** a charge involving differences whose endpoints
  lie in different rank blocks/epochs, not only disjoint mark sets or the
  internal difference spectra of separate rulers.
- **Persistence/amortization:** a summable or \(o(\log J)\) budget along an
  unbounded filtration, not a terminal-scale entropy or energy estimate.
- **Innovation linkage:** a proved comparison with
  \(\operatorname{Var}_{\nu_j}(u(1-u))\), the actual PSD update \(Q_j\), or the
  adjoint sum above. A scalar profile discrepancy by itself is insufficient by
  the workspace's exact homometric and four-point counterexamples.

## 3. A genuine conditional local-to-global bridge

### Riblet--Schehr (2026)

**Primary sources:** [arXiv:2505.20851v2](https://arxiv.org/abs/2505.20851),
[Acta Mathematica Hungarica, DOI 10.1007/s10474-026-01604-z](https://doi.org/10.1007/s10474-026-01604-z).

The following statements were checked in the official arXiv HTML and against
the open publisher version.

- **Theorem 1.1.** If \(\mathcal S\) is the class of Sidon subsets of
  \(\mathbb N^*\) and
  \(f_A(z)=\sum_{a\in A}z^a\), then
  \(\mathfrak S=\{f_A:A\in\mathcal S\}\) is compact in
  \(\mathcal O(\mathbb D)\) for uniform convergence on compact subsets. It
  also gives attainment for the stated integrable linear functionals.
- **Theorem 2.1.** If \(S\) maximizes the reciprocal sum over Sidon sets, then
  there is a constant \(C>0.257\) such that
  \[
    |S\cap[1,n]|>C n^{1/4}\quad\text{for every }n\ge1,
  \]
  and
  \[
    \limsup_{n\to\infty}\frac{|S\cap[1,n]|}{n^{1/3}}>0.
  \]
  The paper explicitly says immediately before the theorem that it was unable
  to prove the expected all-\(n\) \(n^{1/3}\) lower bound.
- **Theorem 6.3.** Every continuous real-valued functional on a closed subset
  of \(\mathcal P(\mathbb N)\), with the discrete product topology, attains
  its supremum. The proof is the diagonal compactness of
  \(\{0,1\}^{\mathbb N}\).

Theorem 2.1 implies only \(a_m=O(m^4)\) for every \(m\), with
\(a_m=O(m^3)\) on an infinite subsequence. This is polynomially weaker than
the needed \(O(m^2\operatorname{polylog}m)\) envelope and contains no
cross-epoch profile or innovation statement.

The useful new consequence is the following elementary corollary of their
compactness proof.

> **Finite-tower compactness corollary (derived here, not stated by the
> authors).** Let \((B_m)_{m\ge1}\) be any finite integer bounds. Suppose that
> for every \(M\) there is an \(M\)-mark integer Sidon ruler
> \(0=a_1<\cdots<a_M\) with \(a_m\le B_m\) for all \(m\le M\). Then there is
> one infinite integer Sidon sequence \(0=a_1<a_2<\cdots\) satisfying
> \(a_m\le B_m\) for every \(m\).

**Proof audit.** Translate to subsets of \(\mathbb N^*\) if needed. Every
finite Sidon set has a greedy infinite Sidon completion because it forbids
only finitely many choices at each step. For each \(M\), let \(K_M\) be the
closed cylinder condition \(0\in S\) and
\(|S\cap[0,B_m]|\ge m\) for every \(m\le M\), restricted to the compact
space of Sidon sets. The hypothesis plus greedy completion makes \(K_M\)
nonempty, and \(K_{M+1}\subseteq K_M\). Compactness gives an element of
\(\bigcap_M K_M\); the conditions force it to be infinite and to satisfy all
coordinate bounds.

**Verdict.** This removes compatibility as an extra obstruction *after*
uniform finite towers at every depth have been proved. It does not prove the
finite-tower hypothesis, and moving-scale functionals such as the adjoint
innovation sum are not supplied as continuous functionals by Theorem 6.3.
It therefore cannot by itself prove the unbounded-history innovation budget.

## 4. Exact unbounded-history analogues, and why transfer fails

### Sudakov--Tomon--Wagner (2022): a literal Kraft/Carleson budget

**Primary sources:** [arXiv:2008.04804v2](https://arxiv.org/abs/2008.04804),
[JCTA DOI 10.1016/j.jcta.2021.105558](https://doi.org/10.1016/j.jcta.2021.105558).

- **Proposition 2.1.** For every antichain
  \(\mathcal F\subset2^{\mathbb N}\),
  \[
    \sum_{n=1}^{\infty}
      \frac{|\mathcal F\cap2^{[n]}|}{2^n}\le2.
  \]
  The proof partitions members by their maximum element, encodes those new
  members as a binary prefix code, applies Kraft's inequality
  \(\sum 2^{-|s|}\le1\), and then telescopes exactly.
- **Theorem 1.1.** Consequently
  \[
    \liminf_{n\to\infty}|\mathcal F\cap2^{[n]}|
      \left(\frac{2^n}{n\log n}\right)^{-1}=0.
  \]

This is the closest exact Carleson-type template found: first births are
placed into mutually prefix-free cylinders and receive a globally summable
mass. It was explicitly motivated by Erdős's infinite Sidon problem.

**Transfer obstruction.** A difference born at one Sidon prefix remains in
the spectrum of every later prefix. The Sidon property makes differences
distinct, but it does not make their birth records prefix-free. No checked
source constructs an injective prefix-free code whose Kraft mass is bounded
below by the actual \(Q_j\) or adjoint contribution. Assuming such a code is
exactly assuming the missing cross-epoch persistence theorem.

### Balister--Powierski--Scott--Tan (2022): the Kraft condition is nearly sharp

**Primary sources:** [arXiv:2102.00246v2](https://arxiv.org/abs/2102.00246),
[SIAM J. Discrete Math. DOI 10.1137/21M143025X](https://doi.org/10.1137/21M143025X).

- **Theorem 3.** If \((f_n)_{n\ge n_0}\) is a nondecreasing sequence of
  positive integers with \(f_{n_0}=1\),
  \(\sum_{n\ge n_0}f_n/2^n\le1/4\), and
  \(f_n/2^n\) nonincreasing (equivalently
  \(f_n\le f_{n+1}\le2f_n\)), then there is an infinite antichain
  \(\mathcal F\) satisfying
  \(|\mathcal F\cap2^{[n]}|\ge f_n\) for every \(n\ge n_0\).
- **Corollary 4.** There is an antichain with
  \[
    |\mathcal F\cap2^{[n]}|
      =\frac{2^n}{n\log^{1+o(1)}n}.
  \]

**Verdict.** In the antichain model, the Kraft mass is essentially the right
complete global-history currency. This sharpens the analogy but supplies no
Sidon-to-code map and no signed-innovation comparison.

### Conlon--Fox--Sudakov (2020): block/Hölder amortization in an infinite graph

**Primary sources:** [arXiv:1910.08661v3](https://arxiv.org/abs/1910.08661),
[Random Structures & Algorithms DOI 10.1002/rsa.20953](https://doi.org/10.1002/rsa.20953).

- **Theorem 4.1.** If \(2\le s\le t\) and \(G\) is a
  \(K_{s,t}\)-free graph on \(\mathbb N\), then, for the induced graph
  \(G_n=G[[n]]\),
  \[
    \liminf_{n\to\infty}
    \frac{\delta(G_n)}{n^{1-1/s}/(\log n)^{1/s}}<\infty.
  \]

The proof is a genuine many-block history argument. With \(n\) consecutive
blocks \(I_j\) of length \(n\), and \(E_j\) the edges from \(I_1\) to
\(I_j\), \(K_{s,t}\)-freeness gives
\[
  \sum_{j=1}^n E_j^s\le t s^s n^{2s-1}.
\]
Hölder then gives
\[
  \sum_{j=1}^n\frac{E_j}{j^{(s-1)/s}}
  <2t^{1/s}s n^{2-1/s}(\log n)^{(s-1)/s}.
\]
Summation by parts contradicts the assumption that every cumulative block
has minimum degree at least
\(16t^{1/s}s|J_j|^{1-1/s}/(\log n)^{1/s}\).

**Verdict.** This is the closest positive long-range block-lag amortization
found. But it proves a liminf sparse-prefix result for minimum degree. The
paper calls \(C_4\)-free graphs a natural analogue of Sidon sets; it does not
give an ordered transformation under which graph degrees equal the
diameter-profile reset, \(\operatorname{Var}_{\nu}(u(1-u))\), or \(Q_j\).
The positive edge counts also contain no signed cancellation. Hence Theorem
4.1 does not prove the required innovation budget.

## 5. New 2024--2026 records screened out by exact scope

### Gupta--O'Bryant: high-multiplicity \(g\)-Golomb rulers

**Primary source:** [arXiv:2605.14229v1](https://arxiv.org/abs/2605.14229).

- **Theorem 3.** For an LM ruler, where each positive distance \(d\) may occur
  at most \(d-1\) times, every \(n\)-mark ruler has diameter at least
  \(\sqrt{8/9}(n-1)^{3/2}\); the authors construct one infinite LM ruler with
  its \(n\)-th initial segment bounded by
  \[
    \frac74\big((n+1)^{3/2}-(n+1)\big).
  \]
- **Theorem 4.** If \(g\ge L(b-1)+1\), then
  \(G(g,g+b)=g+2b-2\); in particular the equality holds when
  \(g\ge\frac74(b^{3/2}-b)+1\).

**Verdict.** Theorem 3 really is one nested infinite all-prefix ruler, but it
allows a distance-dependent number of repetitions. For \(d\ge3\) it is not a
Sidon condition, so distinct interval sums, cross-epoch injectivity, and the
workspace's Sidon energy identities fail. It cannot be substituted for the
required \(g=1\) sequence.

### Gupta: modular-to-ordinary finite conversion

**Primary source:** [arXiv:2607.07931v1](https://arxiv.org/abs/2607.07931).

- **Theorem 3.** Given a modular Golomb ruler with \(k\) marks modulo \(N\),
  \(g\mid N\), and
  \(n\le k-\lfloor g/2\rfloor\), write \(n=ag+r\),
  \(0\le r<g\). Then
  \[
  G(g,n)\le \frac Ng-
    \left\lceil
      \frac{N/g+ga(a-1)/2+ra}{n}
    \right\rceil,
  \]
  with the same bound for larger target multiplicity.

**Verdict.** Even at \(g=1\), the theorem cuts and unwraps one finite modular
ruler. It neither chooses cuts compatibly as \(n\) grows nor preserves a
prescribed prefix, and it has no cross-epoch or innovation conclusion.

### Xu--Xiu--Fan--Liang: disjoint Golomb rulers

**Primary source:** [arXiv:2409.14409v1](https://arxiv.org/abs/2409.14409).

An \((I,J,n)\)-DGR is a family of \(I\) pairwise disjoint \(J\)-mark Golomb
rulers contained in \([n]\); only each member is required to be a Golomb
ruler. **Theorem 4** proves, for example,
\[
 H(a+b,J)\le H(a,J)+H(b,J-1)+b\quad(a\ge b),
 \qquad
 H(2a,J)\le2H(a,J-1)+2a.
\]

**Verdict.** Disjointness here is disjointness of mark sets. Internal
difference spectra of different rulers may overlap, and differences between
marks belonging to different rulers are unrestricted. The union is not a
nested Sidon ruler, so this is not cross-epoch difference packing.

### Barré--Pichot: finite modular geometry, not an energy embedding

**Primary sources:** [arXiv:2309.14524v1](https://arxiv.org/abs/2309.14524),
[EMS Press, DOI 10.4171/LEM/1097](https://doi.org/10.4171/LEM/1097).

- **Proposition 7.1.** For a finite Sidon sequence
  \(a_0<\cdots<a_n\), \(2a_n+1\) is the least \(N_0\) such that it is Sidon
  modulo every \(N\ge N_0\).
- **Question 7.2**, not a theorem, asks for the smallest individual admissible
  modulus \(N_{00}(a_0,\ldots,a_n)\).
- The paper's main CAT(0) constructions, including Theorem 4.1, take finite
  modular Sidon data as input and encode alternating triple sums into flat
  geometry.

**Verdict.** The phrase “nonpositive curvature” is a semantic false positive
for the desired convex/Carleson energy. The paper neither bounds the diameter
of compatible prefixes nor relates the CAT(0) complex to the gap variance or
the covariance innovation matrices. Its moduli may change with the
truncation.

## 6. Martingale/Carleson search boundary

Exact arXiv searches through 2026-08-28 for combinations of
“Sidon sequence,” “Golomb ruler,” “distinct interval sums,” “martingale,”
“Carleson,” and “tree energy” produced no additive-integer Sidon theorem with
the required filtration. The only direct `Sidon + martingale` hit was Pisier's
[arXiv:1704.02969](https://arxiv.org/abs/1704.02969), where “Sidon” means a
property of bounded orthonormal systems and the martingale differences form a
counterexample in harmonic analysis. It has no integer-difference or prefix
diameter content. Generic Walsh--Carleson and Carleson-measure hits were
similarly outside scope.

Zero exact-query results are recorded only as search outcomes. They do not
establish that no relevant theorem exists.

## 7. Citation chase and access limitations

- Semantic Scholar's graph for Riblet--Schehr returned 19 references and zero
  indexed forward citations; its backward list contained finite-diameter and
  classical infinite-Sidon sources already covered by the prior reports, but
  no compatible-prefix or innovation theorem.
- The graph for Gupta--O'Bryant returned seven references and zero indexed
  forward citations. The graph for Gupta's July 2026 paper was rate-limited.
  The Xu--Xiu--Fan--Liang record returned zero citations and zero references,
  which is visibly incomplete and was not treated as evidence.
- OpenAlex likewise showed zero forward citations for the newest 2026 arXiv
  records checked. August 2026 papers have severe indexing lag.
- The scholar search script initially generated HTTP 400 responses because
  field prefixes were doubled (`all:all:`). Re-running plain queries worked,
  but broad arXiv ranking admitted many machine-learning, physics, and
  harmonic-analysis semantic false positives; each retained mathematical
  claim above was rechecked in official full text.
- The Springer and EMS articles were open access. Elsevier's rendered Cheng
  page stripped several formulas, so no theorem extraction from that page is
  used here.
- Semantic Scholar rate limits and incomplete newest-record indexing prevent
  an exhaustive forward-citation claim. This report is therefore a bounded,
  source-audited delta, not a certification of literature absence.

## 8. Precise surviving literature-shaped lemma

The sources isolate a plausible but still unproved bridge. One needs to map
large actual innovation births or signed profile resets of one infinite Sidon
history to disjoint code/tree mass, with all three properties proved:

1. a first-birth assignment that remains injective after later prefixes;
2. a Kraft/Carleson or \(K_{s,t}\)-type global capacity bound across different
   epochs; and
3. a lower comparison from each charged birth to
   \(\langle H_{j+1},Q_j/N_{j+1}\rangle\), retaining location and sign.

Riblet--Schehr compactness would then pass a uniform finite-depth version to
one infinite sequence, but none of the checked sources proves items 1--3.
No source found in Wave 5 can presently prove the unbounded-history
innovation budget.

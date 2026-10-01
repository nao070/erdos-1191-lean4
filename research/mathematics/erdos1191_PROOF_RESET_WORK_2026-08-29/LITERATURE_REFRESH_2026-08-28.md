# Literature Refresh — Erdős Problem #1191

**Search date:** 2026-08-28  
**Status:** no verified complete resolution located in the searched public sources  
**Caution:** this is a documented search result, not proof of mathematical nonexistence.

## 1. Exact public problem record

The public Erdős Problems page states the two questions:

\[
\liminf_{x\to\infty}\frac{|A\cap[1,x]|}{x^{1/2}}(\log x)^{1/2}=0?
\]

and whether there is an infinite Sidon set with

\[
\liminf_{x\to\infty}\frac{|A\cap[1,x]|}{x^{1/2}}(\log x)^c>0
\]

for some `c>0`. At the handoff date the page was marked open, reported no claimed proofs, and listed a USD 1,000 prize. The page itself warns that its status may omit literature and instructs readers to perform an independent search.

Primary public page:

- https://www.erdosproblems.com/1191

## 2. O’Bryant 2026 Part I

Primary record:

- Kevin O’Bryant, *On the Thickness of Infinite Generalized Sidon Sets, I*, arXiv:2606.28651, current handoff version v3 dated 2026-07-26.
- https://arxiv.org/abs/2606.28651

For a `g`-Golomb ruler, the paper proves a finite constant for the classical infinite-density liminf. In the Sidon case this gives

\[
\liminf_{n\to\infty}\frac{A(n)}{\sqrt{n/\log n}}
\le\frac{2}{\sqrt{\log2}},
\]

or equivalently

\[
\limsup_{n\to\infty}\frac{a_n}{n^2\log n}\ge\frac{\log2}{2}.
\]

This does not prove that the liminf is zero or that the sequence-form limsup is infinite.

The paper is especially relevant because its discussion points toward:

- averaging over several values of `N`;
- retaining information from all offsets rather than selecting one;
- reverse-martingale structure;
- entropy or information arguments;
- nonsmooth/stability information beyond the optimized one-scale weighted Cauchy argument.

Those suggestions align directly with the endpoint-variance continuation.

## 3. O’Bryant 2026 Part II

Primary record:

- Kevin O’Bryant, *On the Thickness of Infinite Generalized Sidon Sets, II*, arXiv:2607.23795.
- https://arxiv.org/abs/2607.23795

The paper establishes explicit liminf constants for even-order `B_h` sets. For `h=2`, its statement reduces to the Sidon result from Part I. It does not settle #1191.

## 4. Táfula 2026

Primary record:

- Christian Táfula, *Infinite Sidon-type sets for zero-sum linear forms*, arXiv:2607.20753; journal metadata also lists a 2026 Monatshefte für Mathematik publication.
- https://arxiv.org/abs/2607.20753

The paper studies density restrictions for representation functions of zero-sum linear forms. It recovers the classical finite-constant density phenomenon in the `(1,-1)` case and proves related results under gap hypotheses. It does not produce the zero liminf required for #1191.

Potential relevance:

- translation-invariant representation counts;
- gap-growth criteria;
- matched-even forms and average representation budgets.

## 5. Cilleruelo and Ruzsa constructions

Primary/open records:

- Javier Cilleruelo, *Infinite Sidon sequences*, Advances in Mathematics 255 (2014), 474–486, DOI 10.1016/j.aim.2014.01.011; arXiv:1209.0326.
- https://arxiv.org/abs/1209.0326
- Imre Z. Ruzsa, *An Infinite Sidon Sequence*, Journal of Number Theory 68 (1998), 63–71, DOI 10.1006/jnth.1997.2192.

The benchmark density is

\[
A(x)=x^{\sqrt2-1+o(1)},
\]

with Cilleruelo giving an explicit construction. This remains a genuine polynomial exponent away from the `sqrt(x)/polylog(x)` scale of Question 2.

## 6. Finite Sidon Fourier uniformity and local distribution

Primary records:

- Miquel Ortega and Sean Prendiville, *Extremal Sidon Sets are Fourier Uniform, with Applications to Partition Regularity*, Journal de théorie des nombres de Bordeaux 35 (2023), 115–134, DOI 10.5802/jtnb.1239.
- https://www.numdam.org/articles/10.5802/jtnb.1239/
- Yuchen Ding, *Dense finite Sidon sets on arithmetic progressions*, arXiv:2606.15041.
- https://arxiv.org/abs/2606.15041

Ortega–Prendiville prove Fourier pseudorandomness/equidistribution for extremal finite Sidon sets. Ding uses that input to obtain local and residue-class weighted-sum asymptotics for dense finite Sidon sets.

Potential connection to endpoint imbalance:

- endpoint variance is sensitive to residue placement;
- finite Fourier uniformity may control endpoint charges when a prefix/window is sufficiently close to finite extremality;
- a valid application must establish the required cardinality deficit and uniform error at the growing moduli used in #1191.

It is not valid to apply these theorems to an arbitrary critical infinite prefix merely because `A(x)` has the order `sqrt(x/log x)`, which is smaller than finite extremality by a logarithmic factor.

## 7. Other adjacent 2026 work

Firecrawl’s research index returned recent work on zero-sum forms, generalized Sidon sets, and delta-separated finite sumsets, including arXiv:2608.07416. These are useful for vocabulary and finite constructions but no direct implication for #1191 was verified.

## 8. Novelty search for the endpoint theorem

Queries covered combinations of:

- cyclic `H^{-1}` norms;
- graph divergence and inverse Laplacians on cycles;
- arc coverage variance and circular discrepancy;
- Eulerian residue graphs;
- Golomb rulers and homometric sets;
- endpoint incidence versus difference spectra;
- martingale/entropy methods for Sidon density.

No direct prior theorem matching the complete endpoint-imbalance reconstruction plus the #1191 application was located in this search. This is only a preliminary novelty audit. The identity may be a standard form of one-dimensional discrete potential theory or interval-coverage discrepancy under different terminology. A publication claim requires a more systematic search and expert review.

## 9. Database/tool outcomes

### Exa

Useful for locating and fetching the exact problem page, O’Bryant I/II, Táfula, Ding, Ortega–Prendiville, and Cilleruelo. Some parsed metadata/title fields were imperfect, so official arXiv/journal pages were treated as authoritative.

### SciSpace

Located Cilleruelo and older infinite-Sidon papers, but the targeted result set did not surface the newest O’Bryant papers. This may reflect indexing latency. Results were used only for discovery.

### Consensus

The attempted search failed because the account had exhausted its 30 monthly searches. No mathematical evidence was obtained from Consensus in this handoff.

### Firecrawl

- An exact research-category search for `Erdős Problem #1191` returned no results.
- A broader ordinary search found Táfula and Cilleruelo-related material but missed the exact problem page and O’Bryant papers.
- Firecrawl’s research-paper index did return O’Bryant I/II, Cilleruelo, Táfula, Maldonado, and adjacent papers.
- A search for cyclic `H^{-1}` / endpoint-imbalance analogues returned no results.
- Quality feedback was submitted for empty/partial searches.

### Normal web and specialist sites

- arXiv and official/journal pages supplied the load-bearing primary evidence.
- Numdam directly supplied Ortega–Prendiville.
- EuDML and Math-Net.Ru site-restricted searches produced many false positives from harmonic analysis, dynamics, or unrelated uses of “Sidon.”
- Public searches did not reliably expose exact MathSciNet or zbMATH records for the newest 2026 preprints.
- MathOverflow did not surface a direct discussion resolving #1191 in the targeted public search.
- Project Euclid searches were not decisive.

## 10. Literature conclusions for the next session

1. Do not spend the main effort on another constant optimization of O’Bryant’s one-scale mean energy.
2. The most directly motivated universal route is multiscale/all-offset variance, reverse martingales, entropy, or stability incompatibility.
3. Finite Fourier uniformity is a conditional tool: prove near-extremality before using it.
4. Táfula’s gap and zero-sum representation framework is worth checking for a way to upper-bound a multiscale endpoint functional.
5. Re-run a current exact-statement search before any novelty or solution claim.

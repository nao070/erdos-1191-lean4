# Literature Audit and Relevance Corrections

Date searched: 2026-08-29.

## Canonical problem source

- Erdős Problems #1191: https://www.erdosproblems.com/1191
- The live page is the canonical place to recheck statement, status, prize, comments, and claimed proofs before publication. Direct automated access returned 403 in one audit path, so browser verification remains mandatory.

## Directly relevant current primary sources

### Kevin O'Bryant, 2026

- `On the Thickness of Infinite Generalized Sidon Sets, I`, arXiv:2606.28651v3.
- https://arxiv.org/abs/2606.28651
- For a `g`-Golomb ruler, proves the liminf bound with constant `2*sqrt(g)/sqrt(log 2)`; for `g=1` this improves the finite constant but does not prove zero.
- The discussion explicitly points toward averaging over block sizes, reverse-martingale structure, entropy, and irregularity beyond optimized one-scale Cauchy energy.
- This is the most actionable current route-inspiration source.

### Christian Táfula, 2026

- `Infinite Sidon-type sets for zero-sum linear forms`, arXiv:2607.20753.
- https://arxiv.org/abs/2607.20753
- Extends the classical density phenomenon to zero-sum linear forms and recovers the classical `(1,-1)` scale, but does not replace the finite liminf constant by zero.

### Imre Z. Ruzsa, 1998

- `An infinite Sidon sequence`, Journal of Number Theory 68 (1998), 63–71.
- DOI: https://doi.org/10.1006/jnth.1997.2192
- Gives the record exponent `sqrt(2)-1` for dense infinite Sidon sequences.

### Javier Cilleruelo, 2014

- Explicit infinite Sidon construction with the same exponent.
- Preprint: https://arxiv.org/abs/1209.0326
- Useful for Q2 and for adversarial finite truncations; still polynomially below the `sqrt(x)/(log x)^c` target.

### Classical sources

- P. Erdős and P. Turán, `On a problem of Sidon in additive number theory, and on some related problems`, J. London Math. Soc. 16 (1941), 212–215.
- H. Halberstam and K. F. Roth, `Sequences`, Vol. I, 1966, classical infinite-Sidon density theorem.
- K. O'Bryant, annotated bibliography of Sidon sequences: use it for terminology and citation chaining before general keyword search.

## Sources present in the package but not direct #1191 partial results

### Norbert Hegyvári, 1986

- `On consecutive sums in sequences`, Acta Mathematica Hungarica 48, 193–200.
- DOI: https://doi.org/10.1007/BF01949064
- Concerns finite sequences with distinct consecutive sums. It may supply finite Golomb-ruler-like blocks or a gluing ingredient, but it is not a theorem about the zero liminf in #1191.

### Fang–Sándor, 2022

- `On disjoint sets`, arXiv:2208.11357.
- https://arxiv.org/abs/2208.11357
- Studies two sets whose difference sets are disjoint. Adjacent methodology only; not a direct density theorem for one infinite Sidon set.

### Alexeev–Mixon, 2026

- `Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof`, arXiv:2510.19804.
- https://arxiv.org/abs/2510.19804
- Resolves a different `$1000` Erdős problem about extending finite Sidon sets to finite perfect difference sets. It is relevant to AI+Lean workflow and finite designs, not a partial result on #1191.

## AI-mathematics reliability sources

### Aletheia / DeepMind

- `Towards Autonomous Mathematics Research`, arXiv:2602.10177.
- https://arxiv.org/abs/2602.10177
- In the reported Erdős-problem sweep, 63/200 evaluable candidates were technically correct and 13/200 (6.5%) were meaningfully correct for the intended question. This supports strong specification-gaming safeguards, but the percentage is not a calibrated probability for this project.

### OpenAI, 2025

- `Early experiments in accelerating science with GPT-5`.
- https://openai.com/index/accelerating-science-gpt-5/
- States that examples are curated, expert oversight remains essential, citations/mechanisms/proofs can be hallucinated, and the model is not autonomous.

### OpenAI, 2026

- `Ten advances in mathematics and theoretical computer science`.
- https://openai.com/index/ten-advances-in-mathematics/
- Reports roughly `$2000` in solution-finding tokens for the ten listed results in total at Sol API rates, followed by human manuscript preparation and Lean formalization. Do not restate this as one problem costing `$2000` or as total project cost.

## Database-specific observations

- `zbMATH Open`: search exact title/author/MSC and follow review citations. Public-web retrieval did not expose a clean #1191-specific record in this audit; absence is not evidence.
- `MathSciNet`: use exact title/DOI/MR number. Public access is limited; an institutional search is still needed.
- `arXiv Mathematics`: highest-value source for 2026 updates and version dates.
- `MathOverflow`: useful for precise classical formulations and terminology. The thread `Is there a "complete" Sidon sequence?` records the classical `C sqrt(n/log n)` infinitely-often bound, but comments are not final theorem evidence.
- `EuDML`: many `Sidon` results are harmonic-analysis false positives. Add `B_2`, additive, integer sequence, difference uniqueness.
- `Numdam`: same false-positive risk; targeted searches did not surface a direct #1191 advance.
- `Project Euclid`: no direct hit in the targeted public search; search journal archives and references rather than infer absence.
- `Math-Net.Ru`: public search returned spectral/dynamical uses of “Sidon” and generalized finite topics, not a direct #1191 theorem.
- `Google Scholar`: use for forward/backward citation chains; do not rely on snippets for theorem statements.
- `SciSpace`: returned mostly adjacent literature in this run; all candidate theorems require primary-text verification.
- `Exa Complex`: useful for relevance disambiguation and primary-page retrieval.
- `Consensus`: the connected account had exhausted its 30-search quota in this audit, so it supplied no new result; record this as an access limitation, not a null finding.
- `Firecrawl`: research index and web search were used; direct scrape of the official problem page failed once. Useful for discovery, not final theorem authority.

## Better complementary sources

- Crossref: exact DOI metadata.
- OpenAlex and Semantic Scholar: citation graphs and related-work discovery.
- OEIS for finite ruler/consecutive-sum sequences, followed by primary references.
- Publisher pages and author homepages for accepted versions.
- O'Bryant's annotated bibliography as the subject-specific index.
- Direct expert contact after a concise theorem/no-go draft exists.

## Search conclusion

No searched source supplied a known proof or disproof of Question 1 or Question 2. This is a **qualified literature null**, not a novelty certificate. The most useful fresh direction is O'Bryant's explicit diagnosis that the optimized one-scale energy method may need multi-scale averaging, martingale, entropy, or structural irregularity information.

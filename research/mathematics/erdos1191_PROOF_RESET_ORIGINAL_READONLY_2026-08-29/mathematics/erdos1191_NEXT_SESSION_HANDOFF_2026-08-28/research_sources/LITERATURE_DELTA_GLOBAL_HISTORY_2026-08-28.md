# Focused literature delta: global-history and extension mechanisms

**Audit date:** 2026-08-28  
**Scope:** primary sources capable of changing the Wave 4 target: a
quantitative extension theorem, a nested-prefix packing law, or a multiscale
innovation/entropy budget for one globally compatible critical Sidon sequence.

## Bottom line

No source located in the focused primary corpus proves the required uniform
`o(log J)` covariance-innovation budget or constructs a Sidon sequence with an
all-prefix `n^2 polylog(n)` coordinate envelope.  This is a qualified search
result, not an absence theorem.  The most concrete cross-block theorem found
is O'Bryant's two-block deletion lemma, but its full-history quadratic charge
is absorbed only by a cubic jump of the next construction scale.

## 1. O'Bryant's quantitative gluing lemma

In [O'Bryant, arXiv:2606.28651v3, Lemma 9](https://arxiv.org/html/2606.28651v3),
let `V` and `W` be `g`-Golomb rulers in `[0,V_2)` and
`[W_1,W_1+m)`, with

\[
W_1-V_2\ge \max(V_2,m).
\]

There is `W* subset W` such that

\[
|W^*|\ge |W|-g\binom{|V|}{2},
\qquad V\cup W^*\text{ is }g\text{-Golomb}.
\]

The proof explicitly separates old--old, new--new, and old--new differences.
Its iteration uses `q_(i+1)=q_i^3` and loses only `O(q_i^2)` elements from a
new block of `q_i^3` marks.  This proves a limsup construction of density
`sqrt(g/2)` on selected scales.  It does **not** preserve a critical envelope
at every intermediate prefix: the deletion charge is quadratic in the whole
old history and becomes negligible only because the next scale is cubic and
is placed behind a very large gap.  The paper's Section 5 separately asks for
fine bounds on all repeated partial counts of one finite near-extremal ruler.

**Reusable target.**  A critical-scale successor would need to replace the
`O(|V|^2)` full-history deletion charge by a localized, signed, or amortized
charge that is summable along nested prefixes.

## 2. Difference packings do not include cross-block differences

[Ma--Yi, arXiv:2608.13739v1](https://arxiv.org/html/2608.13739v1) define
`P_t(U)` using families of `t`-mark Golomb rulers whose *internal* positive
difference sets are pairwise disjoint subsets of `[1,U]`.  Their Theorem 1.1
is

\[
P_t(U)=U-o(U)\quad\Longleftrightarrow\quad 3\le t\le5.
\]

They prove eventually `P_3(U)>=U-8`, `P_4(U)>=U-5`, and obtain `t=5` from
the multiplicatively independent exact-covering seeds `121` and `161`.  For
fixed `t>=6`, Theorem 3.1 gives the positive leave

\[
\liminf_{U\to\infty}\left(1-\frac{P_t(U)}U\right)
\ge \frac{(t-1)\gamma_0-2}{2(t-2)},
\qquad \gamma_0=0.4344672564\ldots .
\]

This is adjacent but not a nesting theorem.  Translating the separate rulers
into one mark set creates cross-block differences, which are absent from the
definition of `P_t(U)` and are precisely the difficult part of #1191.

The `t=4` existence input comes from
[Liu--Feng--Wang--Zhang, arXiv:2510.20446v1](https://arxiv.org/html/2510.20446v1).
Their PDF/PSDS extension is likewise an extension of a *system of separate
blocks*, not a nested extension of one ruler, so it does not restore the
missing cross-block constraints.

## 3. Qualitative infinite completion is not quantitative continuation

[Alexeev--Mixon, arXiv:2510.19804v2](https://arxiv.org/html/2510.19804v2#S2)
contains three distinct statements that must not be conflated.

1. Main Theorem 9 is finite and cyclic: `{1,2,4,8,13}` does not embed in any
   finite perfect difference set modulo `v`.
2. Section 2, Claim 10 cites Hall and sketches that every **finite** Sidon set
   embeds in *some* infinite perfect difference set over the integers.
3. An arbitrary already-infinite Sidon set need not embed in an infinite
   perfect difference set; the paper gives `2B` when `B` is an infinite
   perfect difference set.

Claim 10 has no displacement, density, prefix-preservation, or amortized-cost
bound.  It therefore does not turn the growing finite Erdős--Turán windows in
this package into one infinite globally critical sequence.

Chen--Fang's 2026 result, DOI
[`10.1016/j.jcta.2026.106239`](https://doi.org/10.1016/j.jcta.2026.106239),
constructs a dense infinite perfect difference set with counting function
close to a rescaled input Sidon set.  The construction modifies the rescaled
input by deletions and insertions; it neither contains the input nor preserves
prescribed prefixes, and it assumes rather than creates any useful all-scale
density of that input.

## 4. Finite smoothing and entropy do not supply a filtration budget

[Hou--Zhao, arXiv:2607.01169v2](https://arxiv.org/html/2607.01169v2) prove

\[
F(N)\le N^{1/2}+0.943492590\ldots N^{1/4}+O(1)
\]

by coupling eight finite smoothing kernels in a Hilbert direct sum and then
certifying the optimized constants exactly.  This is a one-terminal-scale
result.  It offers no compatible-prefix filtration and does not control the
actual `Q_m` birth innovations in this workspace.  It does warn that a
multikernel proof needs the relevant combined correlation kernel to retain
the necessary pointwise sign, not merely a positive-semidefinite coefficient
matrix.

[Goh, arXiv:2406.18798v2](https://arxiv.org/html/2406.18798v2) proves robust
one-scale entropic doubling inequalities on Sidon supports.  Ordinary
one-scale entropy is already nearly saturated for a Sidon set, and the paper
contains no nested Carleson or conditional-innovation summation.  Any entropy
route for #1191 must therefore build an explicit scale filtration and a new
summable conditional budget.  The printed parenthetical following its
Proposition 11 appears algebraically inconsistent with the displayed identity
for the paper's additive-energy functional; do not quote that derived sign
without an erratum.

## 5. Current construction frontier remains polynomially sparse

Recent infinite-basis constructions by
[Niu, arXiv:2607.11351v2](https://arxiv.org/html/2607.11351v2) and
[Pilatte, arXiv:2303.09659v3](https://arxiv.org/html/2303.09659v3) optimize
additive-basis properties, not all-prefix Sidon density.  Niu's construction
has exponent `0.3393`, and explicitly retains Ruzsa's
`x^(sqrt(2)-1+o(1))` as the stronger density benchmark.  Neither approaches
the near-square-root polylogarithmic envelope required by Question 2.

## 6. Search limitations and disposition

- Official arXiv HTML was available for the theorem statements above.
- Direct publisher retrieval for Chen--Fang later returned HTTP 403; the DOI
  and publisher-indexed theorem statement were available, but no independent
  open PDF was located.
- Semantic Scholar and the arXiv export API returned HTTP 429 during parts of
  the forward-citation pass.  Direct arXiv pages remained accessible.
- OpenAlex counts for the newest August 2026 records were mostly zero and are
  subject to indexing lag.
- Generic harmonic-analysis Carleson theorems were rejected because they
  assume a packing inequality of the same type that must be derived here.
- The focused delta supplements, and does not replace, the persisted
  306-record Wave 3 research state and its Exa, Firecrawl, SciSpace, Consensus,
  OpenAlex, Crossref, and Semantic Scholar audit trail.

**Resulting mathematical direction:** retain O'Bryant Lemma 9 as the nearest
known gluing template, but pursue a long-range same-history collision charge.
Finite difference-packings, qualitative completion, one-scale smoothing, and
unconditional entropy cannot provide the missing innovation budget as stated.

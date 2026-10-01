# C058 storage/PSD localization literature delta

Date: 2026-08-31 (Asia/Tokyo)  
Status: `LITERATURE_QUALIFIED_NULL_ONLY_C058_OPEN`

## Question searched

Can an existing theorem supply the missing C058 step: a phase-integrated
local-to-global PSD estimate on a dyadic history with a bounded
storage/dissipation potential, exact boundary terms, and one globally
consistent owner ledger?

The search used Firecrawl's paper index and in-body reader, Exa, SciSpace,
and Consensus.  The first broad Firecrawl query returned no records; a
matrix-Carleson reframing returned the family below.  Consensus had exhausted
its monthly search quota and supplied no result, so no claim below depends on
Consensus.  This is a dated scoped search, not a claim that no other theorem
exists.

## Closest primary sources and exact relevance

1. Bickel and Wick, [A Study of the Matrix Carleson Embedding
   Theorem with Applications to Sparse
   Operators](https://arxiv.org/abs/1503.06493).  Its displayed matrix
   Carleson theorem assumes a sequence of positive-semidefinite matrices and
   a positive dyadic Carleson testing condition, then proves an embedding by
   a maximal-function/stopping-time argument.  It does not manufacture the
   signed physical owner rows or the testing condition needed by C058.

2. Culiuc and Treil, [The Carleson Embedding Theorem with Matrix
   Weights](https://arxiv.org/abs/1508.01716).  This is a strong martingale
   matrix embedding theorem, including weights in domain and target.  Its
   hypotheses are again an embedding/testing framework; they do not identify
   a nonanticipating shell-profile potential or solve overlap ownership.

3. Domelevo, Petermichl, and Skreb, [Failure of the Matrix Weighted Bilinear
   Carleson Embedding Theorem](https://arxiv.org/abs/1906.08715).  The paper
   gives a high-eigenvalue-discrepancy counterexample to natural bilinear
   matrix extensions and shows that a uniform conditioning bound is the
   relevant missing hypothesis in its setting.  This is a warning against
   inferring a signed/bilinear C058 estimate from a one-sided matrix embedding.

4. Grone, Johnson, Sa, and Wolkowicz, [Positive Definite Completions of
   Partial Hermitian Matrices](https://doi.org/10.1016/0024-3795(84)90207-6),
   and the chordal decomposition literature summarized by Sun, Andersen, and
   Vandenberghe, [Decomposition in Conic Optimization with Partially
   Separable Structure](https://arxiv.org/abs/1306.0057).  Chordality lets
   consistent clique data be completed or a sparse PSD matrix be decomposed.
   The consistency of entries on clique overlaps is a hypothesis, not an
   owner-selection theorem.  C117 is precisely a finite warning that two
   locally feasible owner allocations can disagree on a shared coordinate.

5. Arcozzi, Holmes, and Mozolyako, [Bellman Function Sitting on a
   Tree](https://arxiv.org/abs/1809.03397), and the related dyadic-tree
   embedding literature.  A Bellman main inequality is structurally close to
   bounded storage/dissipation, but the searched statements concern Hardy or
   Carleson embeddings.  No checked passage supplies the C058 physical
   signed-demand rows, full log-phase margin, or global owner ledger.

## Consequence for the research route

The checked theorem families are reusable components, not a resolution:

- matrix Carleson/stopping-time methods may organize a future multiscale
  positive testing condition;
- chordal clique trees may organize a global Gram matrix only after overlap
  consistency has been explicitly enforced; and
- Bellman/tree formulas suggest how to search for a bounded vector potential.

None of the checked sources proves the enriched local target

`Phi_bar_k >= (epsilon_C-A_C eta_k-sum_r B_(C,r) Delta V_(k,r))/(k+1)-e_k`

with the C103 boundaries and one-time ownership.  The next executable step
therefore remains the exact full-phase primal/dual fixture bank, followed by a
candidate Bellman main inequality only after its finite statement stabilizes.
C058, Q1, Q2, novelty, and prize eligibility remain open.


## Academic-MCP refresh on 2026-08-31

A second independent pass used the installed academic services directly:

- arXiv searched Sidon/martingale/entropy/multiscale/Carleson and
  matrix-Carleson combinations and exposed the primary preprint records;
- OpenAlex was queried only after checking its current quota and cross-checked
  the O'Bryant 2026 records and the closest matrix/tree/PSD papers;
- Crossref independently verified titles, authors, venues, dates, and the
  DOIs `10.1093/imrn/rnx222`, `10.1016/j.laa.2019.08.011`,
  `10.1093/imrn/rnz224`, and `10.1016/0024-3795(84)90207-6`;
- Unpaywall located the open arXiv/publisher route for the bilinear
  matrix-Carleson failure paper and reported no open version for the 1984
  Grone--Johnson--Sa--Wolkowicz paper;
- Semantic Scholar's server/toolchain was reachable, but its public paper
  endpoint returned HTTP 429 during the relevant searches; and
- CORE was reachable, but broad discovery was noisy and its attempted exact
  DOI discovery route returned HTTP 405, so no theorem statement was adopted
  from it.

The primary mathematical reading still comes from arXiv/source or publisher
text; metadata services are not treated as proof sources.  This cross-check
found no theorem that supplies the signed physical owner rows, complete-phase
storage inequality, or one-time C103 ledger.  Because two discovery lanes were
rate-/endpoint-limited and broad searches are not exhaustive, the outcome
remains only `LITERATURE_QUALIFIED_NULL_ONLY_C058_OPEN`, not a novelty or
nonexistence claim.

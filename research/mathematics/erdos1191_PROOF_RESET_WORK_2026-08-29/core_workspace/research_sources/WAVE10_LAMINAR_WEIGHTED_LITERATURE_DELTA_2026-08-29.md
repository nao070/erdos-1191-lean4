# Wave 10 laminar-weighted literature delta — 2026-08-29

## Qualified conclusion

No primary source checked through 2026-08-29 proves P15 or upgrades the Wave 9
hereditary rank-lag inequality `(W9-RLP)` to the required endpoint-product and
kernel estimate.  P15 and Erdős Problem #1191 remain open.

The most useful new interface is nevertheless concrete.  Tensor-product
Carleson embedding theorems convert a single rectangular box estimate into a
full hereditary embedding on a bi-tree or tri-tree.  After splitting the Wave 9
factor `min(4XY,Z^2)` into its two active regimes, its numerical monomial has at
most three tensor factors.  A product-preserving tree encoding plus an `o(1)`
box constant would therefore close the survival-conditioned epoch-block
estimate.  Neither the encoding nor the box estimate is currently proved.

Full exact queries, quotas, source dispositions, and hashes are in:

- `research_sources/wave10_literature_state/QUERY_LOG.md`;
- `research_sources/wave10_literature_state/PRIMARY_SOURCE_AUDIT.md`;
- `research_sources/wave10_literature_state/research_state.json`;
- `research_sources/wave10_literature_state/HASHES.sha256`.

## Exact positive interface

For a finite product tree `T^d`, define the one-box constant by

\[
 \sum_{\alpha\leq\beta}w(\alpha)(I^*\mu(\alpha))^2
 \leq C_{\rm box}\sum_{\alpha\leq\beta}\mu(\alpha)
 \qquad(\beta\in T^d).
 \tag{W10-box}
\]

If `w` is a tensor-product weight, the cited theorems for `d=2,3` imply

\[
 \sum_{\alpha}w(\alpha)|I^*(\psi\mu)(\alpha)|^2
 \ll C_{\rm box}\sum_\omega|\psi(\omega)|^2\mu(\omega).
 \tag{W10-embed}
\]

Primary sources:

- [bi-tree product weights, Theorem 2.3](https://arxiv.org/html/1906.11150#S2.Thmtheorem3);
- [tri-tree product weights, Theorem 1.3](https://arxiv.org/html/2001.02373#S1.Thmtheorem3).

Wave 9's tile coefficient is proportional to

\[
 \frac{R^2}{L^2}\frac{\min(4XY,Z^2)}{N^2}q(R,X,Y,Z).
\]

On `4XY<=Z^2`, the active monomial is `R^2XY`, with three factors.  On
`Z^2<4XY`, it is `R^2Z^2`, with two.  This puts the *weight* in the dimensional
range of `(W10-embed)`.  It does not yet put the P15 atoms there: squaring
`I^*mu` creates cross terms, and the remaining tile coordinate and survival
condition must be placed in the arbitrary measure without destroying the full
product-tree structure.

## Exact obstruction

The product hypothesis cannot be discarded.  A pruned sub-bi-tree can satisfy
every rectangular box condition but fail the Carleson condition and embedding
([Holmes--Psaromiligkos--Volberg, Theorem 1.11](https://arxiv.org/html/1903.02478)).
Thus naively deleting empty P15 cells by a non-product zero weight is invalid.

The unsplit `(R,X,Y,Z)` ledger is four-parameter.  Existing methods are not a
black box at that dimension: the tri-tree paper stops at `T^3`, and the
four-tree follow-up gives counterexamples to straightforward extensions even
for `p=2`
([arXiv:2108.04789](https://arxiv.org/abs/2108.04789)).  The related surrogate
maximum principle retains a positive interpolation loss and is not known with
an exponent below one on `T^4`
([arXiv:2109.00021v2](https://arxiv.org/abs/2109.00021)).

## New 2026 Sidon checks

[Ding's Theorem 4](https://arxiv.org/html/2606.15041v2#Thmtheorem4) gives exact
rank-and-power weighted sums for finite Sidon sets, but its discrepancy term is
small only near the extremal density `|S|~sqrt(n)`.  A critical P15 prefix may
have `2m/sqrt(N_(2m))~1/sqrt(log m)`, and the theorem controls mark moments, not
`h_i h_j Phi_ij`.

The 2026 asymmetric additive-energy inequality is a mixed Hölder inequality,
not a branch-specific energy gain
([arXiv:2607.25442](https://arxiv.org/html/2607.25442)).  The arbitrary-set
Sidon-subset theorem extracts a Sidon subset but does not exploit a branch that
is already Sidon
([arXiv:2605.03181](https://arxiv.org/html/2605.03181)).

## Plugin accounting and saturation

- Exa: **10 searches, 100 reviewed result slots**, plus five fetch calls over
  16 URL requests (11 unique pages).
- Firecrawl: **five searches, 75 returned slots**; two related-paper calls
  returned 15 slots and one empty 15-slot request; four inspect and four
  in-body read calls.
- Consensus: two searches, both blocked because all 30 monthly searches were
  used; reset reported as 2026-09-01.
- SciSpace: three searches, 30 returned slots; discovery only.

The exact four-tree follow-up converged on the tri-tree theorem and the 2021
obstruction papers, with no later exact resolution found through the cutoff.
This is targeted convergence only.  Overall saturation remains **false**.

## Next theorem

> **Wave 10 tensor-box encoding lemma.**  After splitting the endpoint-limited
> and difference-limited regimes, encode each survival-conditioned epoch block
> on a full bi-tree or tri-tree with tensor-product weight and positive measure,
> dominate the exact P15 core by `(W10-embed)`, and prove from distinct
> contiguous sums plus `(W9-RLP)` that `C_box=o(1)`.

The literature supplies the final box-to-embedding implication.  The project
must supply the arithmetic encoding and the vanishing box estimate.

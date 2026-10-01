# Wave 11 survival--Abel literature delta — 2026-08-29

## Qualified outcome

Wave 11's leading arithmetic advance is internal, not imported from the
literature: a length-`ell` difference is the sum of `ell` pairwise-distinct
positive adjacent gaps, hence

\[
 D_{p,q}\geq L_\ell:=\binom{\ell+1}{2}.
\]

Inserted into the exact Abel coefficients, this raises the lower-shell floor
from `(1/4)log m` to `(1/2)log m` and gives the full all-length floor

\[
 K_J^{\rm len}=2\sum_{m\in E_J}\log m+O(|E_J|).
\]

Thus the Wave 10 leading-quarter deficit is repaid.  The checked primary
literature does **not** repay the remaining secondary endpoint profile.  On one
fixed eventually-`C`-critical Golomb ray, the exact unresolved target remains

\[
 G_J+S_J\geq T_J-K_J^{\rm len}-\epsilon_J,
 \qquad \epsilon_J=o(\log J),
\]

or equivalently `sum_(m in E_J) Y_m=o(log J)`.  No checked theorem supplies
that nested survival coupling.  Nor does a checked theorem supply the separate
Route B alternative, a summably-vanishing product-box estimate.  No
equivalence or necessity between Routes A and B has been proved.  This is a
qualified result for the logged interfaces, not a
literature-wide absence or priority claim.

Full audit and reproduction state:

- `research_sources/wave11_literature_state/PRIMARY_SOURCE_AUDIT.md`;
- `research_sources/wave11_literature_state/QUERY_LOG.md`;
- `research_sources/wave11_literature_state/FALSE_POSITIVES.md`;
- `research_sources/wave11_literature_state/research_state.json`.

## Exact scale-sensitive consequence and its ceiling

[Beck--Bogart--Pham, Equation (1)](https://arxiv.org/html/1110.6154)
provides the standard positive gap-vector formulation of a Golomb ruler.  From
that structure and elementary ordering, if `M_ell` length-`ell` intervals are
selected and sorted increasingly, then

\[
 D_{(r)}\geq L_\ell+r-1,\qquad 1\leq r\leq M_\ell.
\tag{W11-shift}
\]

Consequently, for equal coefficient `beta_ell`, the within-class product obeys

\[
 \prod_{r=1}^{M_\ell}D_{(r)}^{\beta_\ell}
 \geq
 \left({(L_\ell+M_\ell-1)!\over(L_\ell-1)!}\right)^{\beta_\ell}.
\tag{W11-factorial}
\]

This is an internal deduction, not a theorem located in the cited paper.  Its
extra gain over the already-used termwise floor is too small.  In an
upper/interior length class,

\[
 M_\ell=O(m),\qquad L_\ell=\Theta(\ell^2),qquad
 \beta_\ell=O(m^{-2}),
\]

so

\[
 \Delta_\ell\ll {1\over m^2}
 \sum_{r<M_\ell}\log(1+r/L_\ell).
\]

For `ell<=sqrt(m)`, summation gives
`sum Delta_ell=O(m^(-1/2))` by the bound
`Delta_ell=O(m^(-1)log(1+m/ell^2))`.  For `ell>sqrt(m)`,
`log(1+x)<=x` gives `Delta_ell=O(ell^(-2))`, again totaling
`O(m^(-1/2))`.  The lower shell has only one interval of each length and no
within-class shifted-rank gain.  Therefore

\[
 \Delta_m^{\rm factorial}=O(m^{-1/2})=o(1).
\tag{W11-factorial-ceiling}
\]

This can improve finite constants but cannot cancel an `O(log log m)`
secondary level.  Any closing inequality must couple different lengths,
epochs, endpoint profiles, or survival; `(W11-factorial)` alone is not a route
to closure.

The newest global-diameter improvement has the same limitation.
[Carter--Hunter--O'Bryant](https://doi.org/10.1007/s10474-024-01499-8)
prove `diam(S)>=k^2-bk^(3/2)-O(k)` with `b<=1.96365`, improving the classical
Lindström lower-order constant.  After logarithms the lower bound is only
`log diam(S)>=2log k-O(k^(-1/2))`; changing the coefficient therefore changes
only an `O(k^(-1/2))` correction.  Applied to an interval, `k` does encode its
length and improves the triangular full-span logarithm by a constant-order
term.  But it has no endpoint placement, cross-length coupling, or nested
survival state and therefore cannot recover the secondary profile.

## Primary-source map to the P16 historical umbrella and P17

Here `P16` denotes the broader pre-Wave-11 umbrella retained for audit
continuity.  Wave 11 discharged its leading-quarter subproblem; the exact
surviving Route A statement is now `P17`.  Route B remains a separate
sufficient alternative, not a proved equivalent or necessary reformulation.

| Primary source | Exact load-bearing result | Exact P17 / Route B disposition |
|---|---|---|
| [Beck--Bogart--Pham, Eq. (1), Thm. 1](https://doi.org/10.37236/2741) | Positive gap-vector formulation; fixed-mark enumeration/reciprocity. | Justifies the contiguous-sum model, not a log-product estimate. The 2023 corrigendum affects a later orientation claim, not this use. |
| [Hegyvári](https://doi.org/10.1007/BF01949064), cross-checked in [Konieczny §1.5, (10)](https://arxiv.org/html/1504.07156) | Finite `[n]` sequences with every consecutive sum distinct have maximum length between `(1/3+o(1))n` and `(2/3+o(1))n`. | Finite critical blocks, no prescribed-prefix or one-ray survival theorem. |
| [Beker, Thms. 1.2--1.4, 2.1](https://arxiv.org/html/2311.10087) ([DOI](https://doi.org/10.1112/blms.13098)) | Quadratically many distinct consecutive sums in finite constructions; expected partial-sum energy `O(n^2)`. | Existence/many, not all; energy is not simultaneous over nested prefixes. |
| [Ruzsa--Shakan--Solymosi--Szemerédi, Thms. 1.1, 1.2, 2.1; Ex. 2](https://arxiv.org/html/1910.02159) | `|A+B|>>|A||B|^(1/2)` from distinct adjacent gaps; paired sumset-product bound; adjacent distinctness can still have `E_3(A)>>|A|^4`. | The product is of cardinalities, not interval magnitudes. Example 2 blocks an adjacent-only energy-stability inference. |
| [Fabian--Rué--Spiegel, Thms. 1.3, 2.1](https://arxiv.org/html/1911.13275) ([DOI](https://doi.org/10.1016/j.jcta.2021.105460)) | Constructed infinite strong `B_h` sets with polynomial separation and density bounds. | Quantitative holes require an extra strong-Sidon hypothesis; not inherited by an arbitrary critical branch. |
| [O'Bryant, Lemmas 6 and 9](https://arxiv.org/html/2606.28651v3) | Weighted block-count Abel argument; separated finite extension after at most `g binom(|V|,2)` deletions. | Closest method templates, but wrong state for the interval-hole channel and too costly under naive critical iteration. |
| [Ma--Yi, Thm. 4.1](https://arxiv.org/html/2608.13739) | Rank-selected difference sums: triangular distinct-integer lower bound versus gap-multiplicity upper bound. | Exact additive first moment, not logarithmic product or nested survival. |
| [Carter--Hunter--O'Bryant](https://doi.org/10.1007/s10474-024-01499-8) | Best checked 2025 total-diameter correction `k^2-1.96365k^(3/2)-O(k)`. | The correction to the `2log k` main term is only `O(k^(-1/2))`; total diameter has no cross-length/survival state and gives no secondary repayment. |
| [Riblet, Thms. 2.1, 3.1](https://arxiv.org/html/2202.01296) ([DOI](https://doi.org/10.1007/s10474-022-01246-x)) | Sidon subsets in unions of few intervals; small-difference upper bounds. | Requires a few-interval support localization not present in P17. |
| [Cohen--Colonna--Singman, Thm. 6.1](https://math.gmu.edu/~dsingman/VCRadial_4.pdf) ([DOI](https://doi.org/10.1007/s00009-012-0232-2)) | Vanishing shadow-box ratio iff compact Poisson embedding on a radial tree. | Exact positive-measure benchmark, but one tree and qualitative vanishing only. |
| [Ottazzi--Santagati, arXiv Thm. 2.7 / journal Thm. 2.8](https://arxiv.org/html/2405.08358) ([DOI](https://doi.org/10.1007/s12220-024-01823-2)) | Sector box condition iff Poisson/Hardy embedding on any locally finite tree. | One-tree boundedness, no product encoding or vanishing rate. |
| [El-Fallah--Kellay--Mashreghi--Ransford, Thms. 1.1--1.2](https://arxiv.org/html/1902.05932) ([DOI](https://doi.org/10.1090/S0002-9939-2014-12248-9)) | A Dini-integrable one-box profile implies Dirichlet Carleson; the integral threshold is sharp. | Shows that mere pointwise box decay is too weak; Route B would still need a summable arithmetic profile. |
| [Ding, Thm. 4](https://arxiv.org/html/2606.15041v2#Thmtheorem4) | Rank-and-power weighted moments for dense finite Sidon sets. | At P17 density the discrepancy is not perturbative; controls marks rather than interval holes or cross ratios. |

## Exact Route A consequences

The finite-energy literature does not justify a nested-prefix energy bound.
Beker's construction is finite and `n`-specific, while
[RSSS Example 2](https://arxiv.org/html/1910.02159) shows that even distinct
adjacent gaps can coexist with third energy of order `|A|^4`.  Full Golomb
uniqueness is stronger, so the example is a warning about the hypothesis, not
a counterexample to P17.

The only checked infinite extension mechanism close to the requested
quantifiers is O'Bryant's separated deletion lemma.  It neither preserves a
critical envelope under naive iteration nor couples the future tail to the
triangular-gap premium.  Strong infinite Sidon results become relevant only
after proving that one surviving branch satisfies their extra quantitative
separation hypothesis.

Accordingly the sharp Route A target is unchanged:

> **Secondary survival repayment.**  On one fixed infinite eventually
> `C`-critical Golomb ray, prove
> `G_J+S_J >= T_J-K_J^(len)-epsilon_J` with
> `epsilon_J=o(log J)`.

Neither another global diameter estimate nor another within-length sorting can
meet this scale.  A viable proof must use cross-length allocation, the exact
future-tail identity, or a genuinely survival-conditioned state.

## Exact Route B consequences

The one-tree papers sharpen the analytic endpoint of Wave 10 Route B:

1. a positive shadow-box ratio tending to zero gives compactness on a radial
   tree;
2. the sector test gives boundedness without radial geometry;
3. in the Dirichlet model a Dini integral is the sharp upgrade from one-box
   decay to a full embedding.

They do not remove the two project-specific obligations.  One must still
encode the endpoint-limited and difference-limited Route B regimes as a positive
measure on a full bi-/tri-tree, and prove a box profile whose accumulated
embedding contribution is `o(log J)`.  Wave 10's product-weight theorems,
pruned-tree counterexample, and `T^4` obstruction remain the controlling
multi-parameter references; no Wave 11 source supersedes them.

## Tool accounting and saturation

- Scholar script spine: **26 successful requests** -- Crossref 8, arXiv 11,
  OpenAlex 7 -- returning 449 slots and **351 deduplicated papers**.  Four
  malformed arXiv field-query failures and one local round-cap refusal were
  logged.
- Exa: **18 searches / 180 slots**.
- Firecrawl: **8 searches / 120 slots**, **3 related calls / 45 slots**,
  4 inspect, and 6 read calls.
- SciSpace: **4 searches / 40 slots**.
- Consensus: **1 blocked attempt**; monthly quota 30/30, reset 2026-09-01.

Crossref met the configured four-axis saturation rule after the exact 2025
diameter query.  arXiv and OpenAlex did not; overall saturation is **false**.
The product/geometric-mean branch is only qualifiedly converged.  Its checked
hits expose the structural formula and the scale ceiling above, not a black-box
secondary repayment.

## Integration status

The leading-quarter problem has been removed by the internal triangular
interval theorem.  Literature verification also rules out overclaiming the
natural next refinements:

- the shifted-factorial gain is `O(m^(-1/2))` per shell;
- the best checked finite-diameter improvement is also only lower-order after
  logarithms;
- adjacent distinctness does not by itself stabilize additive energy;
- qualitative one-tree vanishing does not supply the required summable
  bi-/tri-tree box profile.

Thus P17 and Erdős Problem #1191 are not resolved by this literature delta.
The next proof attempt should work directly on the secondary survival
repayment or, as a separate sufficient alternative, a positive-measure
tensor-box profile, not on another
uncoupled rank, diameter, or within-length product bound.

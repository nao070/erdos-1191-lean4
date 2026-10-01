# Wave 6 literature delta: arithmetic bands, forbidden shadows, and finite-field routes

**Audit date:** 2026-08-28  
**Scope:** a bounded follow-up to the reset-renewal literature search for
Erdős Problem #1191.  The target is either

1. a compatible all-prefix integer Sidon/Golomb tower with
   near-critical coordinate growth of order n² times a polylogarithm; or
2. a theorem that amortizes cross-epoch difference-band births, forbidden
   extensions, or covariance innovations to o(log J) over J relevant scales.

This note records a search delta, not a proof of novelty and not a resolution
of #1191.

## 1. Provenance of the semantic-search record

The exact raw query strings and returned-record counts were not preserved
through session compaction.  The phrases below are reconstructed, near-exact
topic labels from the retained session notes.  They must not be cited as
verbatim payloads, and the result counts are **unavailable**.  No count has
been inferred or invented.

The three topic families were searched with Firecrawl, Exa, and SciSpace:

| Reconstructed grouped topic wording | Count | Retained outcome |
|---|---:|---|
| “disjoint difference sets / difference triangle sets / nested Golomb rulers / distinct contiguous sums” | unavailable | Ma--Yi and disjoint-ruler adjacency were returned.  The useful candidates pack internal ruler spectra or disjoint mark sets; they do not impose every cross-family difference required by the union of the rulers. |
| “A+A-A / forbidden next points / maximal Sidon sets / one-point extension shadow” | unavailable | Finite Sidon sumset, distribution, maximality, and extension-adjacent records were returned.  No checked candidate supplied a uniform density theorem for the one-point forbidden shadow in the critical all-prefix regime. |
| “nested Singer difference sets / finite-field extensions / compatible Sidon rulers / projective norm graph” | unavailable | Singer, norm-graph, subdifference-set, and nested-design adjacency were returned.  The checked primary records do not construct compatible ordered integer rulers across sizes. |

The tool outputs were used only to discover candidates.  Every theorem-level
statement retained below was checked against an official arXiv page.

Consensus returned no papers because the monthly quota was exhausted:
30/30 searches used, with reset reported for 2026-09-01.  This is an access
failure, not negative evidence.

## 2. Difference packings: the missing mixed differences

[Ma--Yi, arXiv:2608.13739v1](https://arxiv.org/html/2608.13739v1)
define P_t(U) by taking families of t-mark Golomb rulers whose *internal*
positive-difference sets are pairwise disjoint subsets of [1,U].  Their
Theorem 1.1 proves

P_t(U) = U - o(U) if and only if 3 <= t <= 5.

For each fixed t >= 6 they also prove a positive-density leave.  This is a
precise internal-spectrum packing theorem.  It does not include differences
between a mark in one ruler and a mark in another ruler.

Consequently, translating the separate rulers and taking their union creates
new mixed differences that are outside the definition of P_t(U).  Those mixed
differences can collide with each other or with an internal difference.  The
paper therefore does not yield one Golomb ruler, a nested family of prefixes,
or a cross-epoch band-renewal budget.

[Xu--Xiu--Fan--Liang, arXiv:2409.14409v1](https://arxiv.org/abs/2409.14409)
use “disjoint Golomb rulers” to mean rulers with disjoint mark sets inside a
common ambient set.  Each component is a Golomb ruler, but the definition does
not say that the union is a Golomb ruler.  In particular it does not control
all mixed differences.  This is useful terminology adjacency, not the
required all-prefix construction.

## 3. Qualitative completion does not provide a quantitative prefix tower

[Alexeev--Mixon, arXiv:2510.19804v2](https://arxiv.org/html/2510.19804v2)
separate finite cyclic completion from infinite completion.

- Theorem 9 states that the finite Sidon set {1,2,4,8,13} does not extend to
  a finite perfect difference set modulo any positive modulus.
- Claim 10 states that every finite Sidon set extends to some infinite
  perfect difference set over the integers, using a greedy construction and
  the finiteness of the obstructions at each insertion.
- The same section notes that an arbitrary already-infinite Sidon set need
  not extend to an infinite perfect difference set.

Claim 10 contains the prescribed finite set, but gives no quantitative bound
on the new coordinates, density, displacement, or cumulative extension cost.
It also does not furnish a compatible sequence of ordered finite prefixes
that all satisfy one near-critical coordinate envelope.  Thus it cannot be
used to pass from unrelated critical finite rulers to the globally compatible
tower needed here.

The A+A-A / one-point-shadow searches found adjacent finite extension and
sumset material, but no primary theorem was retained that uniformly controls
the density of

F(A) = A + Delta^+(A)

in the extension region x > diam(A), while simultaneously preserving an
all-prefix critical envelope.  This is only a bounded search outcome.  It is
not a claim that such a theorem is absent from the literature.

## 4. Singer, norm-graph, and subdifference-set candidates

[Mészáros--Rónyai--Szabó, arXiv:1908.05591](https://arxiv.org/abs/1908.05591)
give a finite-field norm-one description of planar Singer difference sets and
use difference-set structure in the projective norm graph.  Their abstract
also says that the description and definitions carry to nonplanar and
infinite settings.  The checked paper record does not state an ordered lift
to integer rulers that is compatible as the field size changes, nor a common
coordinate envelope for every integer prefix.

[Momihara--Xiang, arXiv:1706.05460](https://arxiv.org/abs/1706.05460)
construct strongly regular Cayley graphs over additive groups of finite fields
from partitions of subdifference sets of Singer difference sets.  This is a
finite-group lifting and graph construction.  It supplies no checked theorem
turning those partitions into nested integer Sidon prefixes with controlled
mixed differences.

Other “nested design” hits were rejected at candidate-screening stage because
the retained descriptions concerned compatible incidence or finite-design
data, not ordered integer embeddings.  No theorem statement from those hits
is asserted here.  In particular, a sequence of finite Singer or design
objects at increasing parameters is not automatically a nested sequence of
integer rulers: one still needs compatible embeddings and uniqueness of every
old--new and new--new integer difference.

## 5. Qualified null and exact boundary

Within this bounded Wave 6 search delta, no checked source supplies either:

1. a compatible all-prefix O(n² polylog n) integer Sidon tower; or
2. an o(log J) innovation, forbidden-band, or reset-renewal theorem for one
   globally compatible sequence.

This conclusion is deliberately qualified.  Semantic retrieval was
non-exhaustive, exact raw payloads and result counts were unavailable after
compaction, and several results were rejected from abstracts before any
theorem use.  The statement is not an absence theorem, a priority claim, or
evidence that the project-internal route is novel.

The smallest literature target capable of changing the status would be one of
the following:

- a quantitative Sidon extension theorem with explicit coordinate,
  displacement, and cumulative-cost bounds that hold through prescribed
  ordered prefixes;
- a compatible lifting of finite-field difference sets to one nested integer
  ruler with all mixed differences controlled; or
- an arithmetic Carleson/Kraft-type theorem charging repeated reset-epoch
  difference bands by o(log J), rather than packing only the internal spectra
  of separate finite objects.

The Wave 6 project-internal forbidden-shadow construction is therefore a
no-go test for one local proof strategy, not a substitute for any of these
global theorems and not a solution of Erdős Problem #1191.

## Primary pages checked for this delta

1. Chaohang Ma and Xiangjie Yi,
   [An Almost-Covering Threshold for Golomb-Ruler Difference Packings,
   arXiv:2608.13739v1](https://arxiv.org/html/2608.13739v1).
2. Boris Alexeev and Dustin G. Mixon,
   [Forbidden Sidon subsets of perfect difference sets, featuring a
   human-assisted proof, arXiv:2510.19804v2](https://arxiv.org/html/2510.19804v2).
3. Tamás Mészáros, Lajos Rónyai, and Tibor Szabó,
   [Singer difference sets and the projective norm graph,
   arXiv:1908.05591](https://arxiv.org/abs/1908.05591).
4. Koji Momihara and Qing Xiang,
   [Strongly regular Cayley graphs from partitions of subdifference sets of
   the Singer difference sets, arXiv:1706.05460](https://arxiv.org/abs/1706.05460).
5. Xiaodong Xu, Baoxin Xiu, Changjun Fan, and Meilian Liang,
   [Some constructive results on Disjoint Golomb Rulers,
   arXiv:2409.14409v1](https://arxiv.org/abs/2409.14409).

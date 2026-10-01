# Wave 12 primary-source delta: integer renewal packing and critical product geometry

Date: 2026-08-29  
Status: **two serious adjacent results checked; no P17 theorem found; qualified null only**

## 1. Exact question searched

The Route A target was not searched under a loose phrase such as “dense
Sidon sets.”  The required interface was:

> On one fixed infinite normalized integer Golomb ruler satisfying
> `a_n<=C n^2 log(2n)` eventually, control the four nonnegative Wave 12
> renewal sectors strongly enough to prove
> `sum_(m in E_J) Z_m=o(log J)`, and hence P17.

The separate Route B interface was:

> Encode the positive endpoint/difference core as a measure on a full
> product tree and derive a summably vanishing arithmetic box profile from
> contiguous-sum uniqueness and survival.

Searches used Exa, Firecrawl's paper index and publisher scraper, SciSpace,
Consensus, and the arXiv MCP.  The structured call counts and query angles are
preserved in `research_sources/wave12_literature_state/search_log.json`.
Consensus returned no result because its monthly quota remained exhausted;
that failure carries no mathematical inference.

## 2. Martikainen: a genuinely critical two-depth theorem, but only a Route B template

Henri Martikainen's 2026 preprint, [*Critical two-depth Journé packing for
bi-parameter and Zygmund rectangles*](https://arxiv.org/abs/2608.22628), is
the closest new geometric hit.  The author-submitted LaTeX was checked in
Sections 1.1, 1.2, and 6.2.

For a pairwise incomparable family of bi-parameter dyadic rectangles in a
finite-measure set, the paper defines two halo embeddedness depths `e_1,e_2`
and the critical weight

\[
(e_1+1)^{-s}(e_2+1)^{-(1-s)},\qquad0<s<1.
\]

The exponents add to one although neither factor is summable alone.  Theorem
1.1 proves a weighted `L^1` packing bound of order `1/[s(1-s)]` and an
exponential-integrability refinement.  Theorem 1.2 proves the analogous
critical packing for Zygmund-boundary rectangles
`ell(I^3)=ell(I^1)ell(I^2)`.  Section 6.2 constructs pairwise incomparable
sub-Zygmund families whose normalized critical mass grows linearly in the
number of generations, so the boundary restriction is essential.

This is mathematically relevant to Route B because it shows that two
nonsummable depth factors can combine exactly at their critical exponent.
It does **not** supply any of the missing arithmetic input:

- no Sidon or Golomb sequence;
- no fixed compatible prefix ray;
- no encoding of `C_(i,j)`, `Y_m`, or `Z_m` as rectangle mass;
- no one-box profile deduced from integer contiguous-sum uniqueness; and
- no summably vanishing constant.

The unrestricted tri-parameter failure also warns against assigning the four
P17 variables to a free product grid.  The source is therefore retained as a
sharp geometry template, not a Route A theorem or a completed Route B
embedding.

## 3. Chen--Fang: density-preserving completion, not prescribed-prefix survival

Yong-Gao Chen and Jin-Hui Fang's forthcoming JCTA article,
[*Dense perfect difference sets constructed from Sidon
sets*](https://doi.org/10.1016/j.jcta.2026.106239), was checked from the full
publisher text, not only discovery metadata.  Theorem 1.1 states that for
every Sidon set `B` and every positive `omega(x)->infinity`, there is a
perfect difference set `A` such that for every `x>=1`,

\[
B(x/2)-\omega(x)\leq A(x)\leq B(x/2)+\omega(x).
\tag{1}
\]

The proof first dilates `B` to `2B`, then constructs increasing auxiliary
sets `V_k` and deletion sets `C_k subset 2B`, finally taking

\[
A=V\cup((2B)\setminus C).
\tag{2}
\]

Thus (1) is a counting-function shadow, not a prescribed-prefix embedding:
elements of the supplied set are deleted and new elements are inserted.  In
particular, the theorem does not say that an arbitrary finite Golomb prefix
survives inside `A`.  It also preserves the input density exponent rather
than improving it.  Using it for Question 2 would first require a Sidon set
`B` already having the Question 2 density, which is circular.

The result is therefore adjacent to compatible-construction questions but
does not control the fixed ray in P17 and does not close Question 2.

## 4. Search disposition

Across the searched angles, the remaining hits were finite Sidon bounds,
infinite constructions at the known subcritical exponent, perfect-difference
completion variants, or generic product-Carleson results.  None had the
quantifiers and state variables of the displayed Wave 12 renewal lemma.

The literature conclusion is consequently limited to:

> **Qualified null.**  No checked primary source proves the fixed-ray integer
> renewal packing lemma, P17, or the missing arithmetic product-tree box
> profile.  This is neither a proof of absence nor a novelty claim.

Overall saturation is false.  The primary-source check is sufficient to
prevent the two new candidates from being misapplied, but independent expert
review and broader specialist-database coverage remain necessary before any
publication or prize submission.

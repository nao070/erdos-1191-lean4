# Wave 10 primary-source audit: laminar weighted core

**Cutoff:** 2026-08-29  
**Conclusion:** no checked theorem proves P15 or gives a direct product/kernel
upgrade of W9-RLP.  A useful conditional route was isolated: represent each
kernel regime on a full bi- or tri-tree with tensor-product weight, prove a
vanishing one-box estimate, and invoke the known box-to-embedding theorem.  The
representation and the box estimate remain unproved.

## 1. Closest positive theorem: tensor-product tree embedding

Let `T^d` be a finite product of dyadic trees, let `I*` be downward summation,
and let `mu,w` be nonnegative functions.  The one-box constant is the least
`C_box` such that

\[
 \sum_{\alpha\leq\beta}
 w(\alpha)\bigl(I^*\mu(\alpha)\bigr)^2
 \leq C_{\rm box}\sum_{\alpha\leq\beta}\mu(\alpha)
 \quad(\beta\in T^d).
 \tag{TB-box}
\]

The full embedding constant is the least `C_emb` such that

\[
 \sum_{\alpha\in T^d}w(\alpha)
 \left|I^*(\psi\mu)(\alpha)\right|^2
 \leq C_{\rm emb}
 \sum_{\omega\in T^d}|\psi(\omega)|^2\mu(\omega)
 \quad(\psi:T^d\to\mathbb R).
 \tag{TB-emb}
\]

For `d=2`, Theorem 2.3 of
[Arcozzi et al.](https://arxiv.org/html/1906.11150#S2.Thmtheorem3) proves
`C_emb << C_box` whenever

\[
 w(\alpha_x,\alpha_y)=w_x(\alpha_x)w_y(\alpha_y).
\]

For `d=3`, Theorem 1.3 of
[Mozolyako et al.](https://arxiv.org/html/2001.02373#S1.Thmtheorem3) proves the
same conclusion for a three-fold tensor weight.  Both theorems also identify
the box, Carleson, hereditary-Carleson/restricted-energy, and embedding
constants up to absolute factors.

This is a genuine product-weight amplification theorem.  It does not assume
that `mu` has product support, so sparse or triangular atom support may be put
in the arbitrary measure **if** the P15 objective can first be represented by
the Hardy energy without changing the tensor weight.

## 2. Exact interface with the Wave 9 tiles

Wave 9 bounds the contribution of a tile `(R,X,Y,Z)` by a constant times

\[
 \frac{R^2}{L^2}\frac{\min(4XY,Z^2)}{N^2}\,q(R,X,Y,Z).
 \tag{1}
\]

Split the tiles into two regimes:

\[
 \begin{array}{ll}
 \mathsf E:&4XY\leq Z^2,\quad
     \min(4XY,Z^2)=4XY,\\[2mm]
 \mathsf D:&Z^2<4XY,\quad
     \min(4XY,Z^2)=Z^2.
 \end{array}
 \tag{2}
\]

Ignoring the epoch normalizers, the active monomial weight in `E` is
`R^2 X Y` (three factors), while the active monomial weight in `D` is
`R^2 Z^2` (two factors).  Thus the *numerical weight* of each regime lies
within the dimensional range of the cited bi-/tri-tree theorem.  This is the
new literature-guided observation.

It is only conditional.  To use it one must still construct, for every epoch
block, a positive measure `mu_K` and test function `psi_K` on a full `T^2` or
`T^3` such that:

1. the relevant sum in (1) is bounded by the left side of `(TB-emb)`;
2. unsupported `(R,X,Y,Z)` combinations are represented through `mu_K`, not
   by a non-product deletion of the weight;
3. every `(TB-box)` test follows from contiguous-sum uniqueness, W9-RLP, and
   the fixed-branch survival condition;
4. the resulting `C_box(K)` tends to zero.

Then `(TB-emb)` would give the desired vanishing epoch-block mass.  No checked
paper, and no current project lemma, supplies any of these four steps.  In
particular, choosing atomic masses to linearize `q` creates positive cross
terms when `I^*mu` is squared.  W9-RLP controls a linear sum of distinct
difference lengths and has the wrong form and direction to bound those cross
terms.

## 3. Why naive pruning is unsafe

[Holmes--Psaromiligkos--Volberg, Theorem 1.11](https://arxiv.org/html/1903.02478)
constructs a pruned sub-bi-tree on which every rectangular box test holds but
the Carleson test and embedding fail.  In the P15 language, keeping only
occupied rank--magnitude cells by setting an arbitrary cell weight to zero is
therefore not a legitimate use of the product-weight theorem: that operation
generally destroys the tensor hypothesis.

The safe alternatives are:

- keep a full product tree and put sparsity in the arbitrary measure `mu`;
- prove the full hereditary/open-set testing condition directly; or
- prove an extra structural lemma showing that the particular pruning remains
  product-preserving.

None is presently available for the P15 birth ledger.

## 4. The four-parameter boundary is real

The unsplit Wave 9 ledger uses four coordinates `(R,X,Y,Z)`.  The tri-tree
paper explicitly proves its theorem only through `T^3` and explains the
obstruction at dimension four.  The follow-up paper
[*Multi-parameter Carleson embeddings ... on T^4, and why the proofs fail*](https://arxiv.org/abs/2108.04789)
gives counterexamples showing that straightforward `T^2/T^3` methods cannot be
extended to `T^4`, even for `p=2`, without a new idea.

The related potential-theory paper proves only a surrogate maximum principle
with a positive interpolation loss on bi-/tri-trees and states that no exponent
below one is known on a four-tree
([arXiv:2109.00021v2](https://arxiv.org/abs/2109.00021)).  Such a loss cannot by
itself provide the vanishing factor required by P15.

The regime split (2) is therefore not cosmetic: it is the only currently
visible way to keep the tensor-weight part within a proved two- or
three-parameter theorem.  The missing measure encoding may still force the
fourth coordinate back into the weight, in which case the literature provides
no black box.

## 5. New 2026 Sidon results and why they do not close the gap

### Dense rank-weighted sums

For `S={a_1<...<a_t} subset [1,n]`, Theorem 4 of
[Ding, arXiv:2606.15041v2](https://arxiv.org/html/2606.15041v2#Thmtheorem4)
gives, uniformly over integer intervals and residue classes,

\[
 \sum i^s a_i^\ell
 =\frac{t^{s+1}}{n^{s+1}}\sum a^{s+\ell}
 +O\!\left(t^s n^\ell\Phi(S,n)\log(2n)\right),
\]

with

\[
 \Phi(S,n)=n^{1/2}
 \left(\left|1-\frac{|S|}{n^{1/2}}\right|+n^{-1/4}\right)^{1/2}.
\]

This is an exact rank-weighted theorem, but P15 prefixes may have

\[
 \frac{2m}{\sqrt{N_{2m}}}\asymp\frac1{\sqrt{\log m}}\to0.
\]

Consequently `Phi(S,N_(2m))` can be of order `sqrt(N_(2m))`; the error is not
a small perturbation.  Moreover, mark moments `i^s a_i^ell` are linear in the
marks after Abel summation and do not control `h_i h_j Phi_ij`.

### Mixed additive energy

[Mudgal, arXiv:2607.25442, Theorem 1.1](https://arxiv.org/html/2607.25442)
bounds a mixed `2d`-fold additive energy by the geometric mean of its diagonal
energies.  It is a sharp Hölder-type symmetrization, not a Sidon-specific
upper bound.  It contains no laminar, rank-lag, or survival hypothesis, so it
does not improve W9-RLP.

### Hereditary Sidon-subset extraction

[Bailleul--Riblet, arXiv:2605.03181](https://arxiv.org/html/2605.03181) proves
that every `n`-point subset of `R^N` contains a Sidon subset of size at least
`(1/(3 sqrt(3))+o(1))sqrt(n)`.  This extracts a Sidon subset from an arbitrary
ambient set.  P15 starts with prefixes that are already Sidon and needs a
weighted inequality for all their interval differences, so extraction loses
the relevant structure.

## 6. Literature-guided next theorem

The sharpest next target suggested by the checked sources is:

> **Tensor-box encoding lemma.**  After the regime split (2), encode each
> survival-conditioned epoch block on a full `T^2` or `T^3` with a
> tensor-product weight and an arbitrary positive measure so that the exact
> core mass is dominated by `(TB-emb)`, and prove from the one-branch distinct
> contiguous sums that its box constant is `o(1)`.

This would turn the known Carleson theorem into the required product/kernel
upgrade.  A weaker target is to prove the hereditary/open-set testing estimate
directly, bypassing the tensor encoding.  Until one of these is established,
P15 and Erdős Problem #1191 remain open.

## 7. Qualified status

The exact targeted axes converged: the strongest positive sources are the
bi-/tri-tree tensor theorems, and the strongest negative sources are the
pruned-bi-tree and four-tree obstruction papers.  Searches through 2026-08-29
found no later theorem closing the gap.

Overall saturation is **false**.  Consensus was quota blocked and no semantic
index proves absence.  This audit supports a qualified null and a more precise
next lemma, not a claim of exhaustive impossibility.

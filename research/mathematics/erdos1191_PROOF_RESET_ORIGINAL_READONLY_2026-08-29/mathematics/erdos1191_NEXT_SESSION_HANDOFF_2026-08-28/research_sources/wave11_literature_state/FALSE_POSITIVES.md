# Wave 11 false positives and non-transplants

These exclusions are theorem-scope decisions, not judgments about the quality
of the papers.

## Terminological matches

- **Graceful permutations.**  Michal Adamaszek,
  [*Efficient enumeration of graceful permutations*](https://arxiv.org/abs/math/0608513),
  Definition 1, requires the adjacent absolute differences of a permutation to
  be exactly `{1,...,n-1}`.  It does not constrain all contiguous sums of its
  gap sequence.  Theorem 1 is an exponential enumeration lower bound, not a
  weighted product inequality.
- **Gap-sum and gap-product sequences.**  Hits under this wording study sums
  or products of consecutive *missing integers*, not Golomb gap vectors.
- **Physics uses of `critical`, `spectrum`, `energy`, and `box`.**  These
  dominated the citation-weighted automated ranker but have no additive or
  tree-embedding interface to P17 or the separate Route B alternative.
- **Engineering ruler searches and FPGA papers.**  They optimize finite
  rulers computationally and do not prove hereditary inequalities.

## Structurally adjacent but too weak

- **Generalized-Golomb/Ehrhart enumeration.**  These papers accurately encode
  the forbidden hyperplanes or enumerate finite rulers, but no checked theorem
  lower-bounds a weighted log product of actual interval sums.  Beck--Bogart--
  Pham is retained only for Equation (1)'s structural translation.
- **LP lower bounds for ruler length.**  Christophe Meyer and Brigitte
  Jaumard, [*Equivalence of some LP-based lower bounds for the Golomb ruler
  problem*](https://doi.org/10.1016/j.dam.2005.07.006), compare four global
  length relaxations.  The official abstract supports equivalence, but the
  full theorem text was not openly retrieved.  The state therefore marks it
  shallow, and no endpoint/rank logarithmic claim is inferred.
- **Global diameter bounds.**  Lindström and the 2025 Carter--Hunter--O'Bryant
  improvement control only the full ruler span.  Their gain after logarithms
  is `O(k^(-1/2))`, below the remaining `O(log log m)` scale.
- **Few-interval Sidon subsets.**  Riblet needs the ambient support to be a
  union of few intervals.  P17 currently has no such localization.

## Wrong product or wrong energy quantifier

- **Ruzsa--Shakan--Solymosi--Szemerédi Theorem 2.1.**  Its product is
  `|A+B||A'+B'|`, not a product of interval magnitudes.  Example 2 positively
  warns that adjacent distinctness alone does not stabilize third energy.
- **Beker's additive-energy construction.**  It proves finite existence and
  expected `O(n^2)` energy for a particular random partial-sum set.  It is not
  a simultaneous bound on every prefix of one prescribed infinite ray.
- **Strong infinite Sidon constructions.**  Fabian--Rué--Spiegel impose and
  construct a stronger separation property; they do not prove that every
  critical Golomb branch, or every prescribed finite prefix, has an extension
  retaining it.
- **Arbitrary-set Sidon extraction.**  Extracting a Sidon subset discards the
  exact interval and endpoint structure of a prefix that is already Sidon.

## Analytic endpoint without the arithmetic encoding

- **Single-tree Carleson theorems.**  Cohen--Colonna--Singman and
  Ottazzi--Santagati give exact positive-measure one-tree criteria.  They do
  not encode the separate Route B bi-/tri-tree core or provide the required
  summable rate.
- **Dirichlet one-box Dini theorem.**  El-Fallah--Kellay--Mashreghi--Ransford
  supplies the sharp summability warning, but not the arithmetic box estimate.
- **Wave 10 product-tree results.**  The bi-/tri-tree theorems remain usable
  only after a full product-preserving measure encoding.  The pruned-bi-tree
  counterexample and `T^4` papers still rule out the naive shortcuts; no Wave
  11 hit repairs those hypotheses.

## Scale-sensitive factorial refinement: valid but insufficient

For `M_ell` distinct length-`ell` intervals with the common termwise floor
`R_ell=binom(ell+1,2)`, sorting gives

\[
 D_{(r)}\geq R_\ell+r-1.
\]

This is a valid internal deduction, not a located published theorem.  In the
upper/interior class of one Wave 11 shell,
`M_ell=O(m)`, `R_ell=Theta(ell^2)`, and its coefficient is `O(m^-2)`.  The
extra gain beyond the termwise floor is at most

\[
 \Delta_\ell\ll {1\over m^2}
 \sum_{r<M_\ell}\log(1+r/R_\ell).
\]

For `ell<=sqrt(m)`, this is
`O(m^-1 log(1+m/ell^2))`; summed over these lengths it is
`O(m^-1/2)`.  For `ell>sqrt(m)`, `log(1+x)<=x` gives
`Delta_ell=O(ell^-2)`, again totaling `O(m^-1/2)`.  The lower shell has only
one interval of each length and receives no within-class gain.  Hence the
entire refinement is `O(m^-1/2)=o(1)` per shell and cannot cancel an
`O(log log m)` secondary profile without a cross-length or survival coupling.

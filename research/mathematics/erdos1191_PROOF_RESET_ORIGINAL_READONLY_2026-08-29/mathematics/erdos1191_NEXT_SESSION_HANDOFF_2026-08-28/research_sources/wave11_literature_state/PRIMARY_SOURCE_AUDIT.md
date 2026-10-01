# Wave 11 primary-source audit

**Cutoff:** 2026-08-29  
**Question:** exact transplant into `P17`, the secondary survival--Abel
obligation remaining after the triangular interval floor repaid the
leading-quarter subproblem of the historical `P16` umbrella.  Route B is a
separate sufficient alternative; no Route A/B equivalence or necessity is
claimed.

## A. Consecutive sums and Golomb gap vectors

### Beck--Bogart--Pham: the structural translation

Matthias Beck, Tristram Bogart, and Tu Pham,
[*Enumeration of Golomb Rulers and Acyclic Orientations of Mixed Graphs*](https://doi.org/10.37236/2741),
Electronic Journal of Combinatorics 19(3) (2012), P42;
[arXiv:1110.6154](https://arxiv.org/html/1110.6154).

- Equation (1) writes a ruler as a positive gap vector `z` of prescribed total
  length and enforces unequal sums over disjoint proper consecutive subsets.
- Theorem 1 proves quasipolynomial enumeration and reciprocity for fixed mark
  count.
- This is the clean primary source for the exact gap-vector/contiguous-sum
  language.  It does **not** give a product, geometric-mean, or weighted-log
  lower bound.
- A 2023 corrigendum corrects the later mixed-graph orientation bijection.  The
  present use is only Equation (1) and Theorem 1, not the corrected statement.

### Hegyvári and Konieczny: finite all-distinct blocks

Norbert Hegyvári,
[*On consecutive sums in sequences*](https://doi.org/10.1007/BF01949064),
Acta Mathematica Hungarica 48 (1986), 193--200.

The original theorem text was not openly retrievable.  The statement was
cross-checked in a later primary paper: Jakub Konieczny,
[*On consecutive sums in permutations*](https://arxiv.org/html/1504.07156),
Section 1.5, equation (10), reports

\[
 (1/3+o(1))n\leq k_{\max}(n)\leq(2/3+o(1))n,
\]

where `k_max(n)` is the maximum length of an `[n]`-valued sequence whose
consecutive sums are all distinct.  This supplies finite critical-scale blocks,
not compatible extensions of a prescribed prefix or a one-ray theorem.

### Beker: finite quadratic distinctness via additive energy

Adrian Beker,
[*On a problem of Erdős and Graham about consecutive sums in strictly increasing sequences*](https://doi.org/10.1112/blms.13098),
Bulletin of the London Mathematical Society 56 (2024), 2749--2759;
[arXiv:2311.10087](https://arxiv.org/html/2311.10087).

- Theorem 1.2 gives, for every `n`, a strictly increasing sequence in `[n]`
  with at least `c_1 n^2` distinct consecutive sums.
- Theorem 1.3 proves this with positive probability for
  `a_i=3i+epsilon_i`; Theorem 1.4 gives an explicit modular construction.
- Theorem 2.1 proves `E(P(a))=O(n^2)` in expectation for the random
  partial-sum set.
- Proposition 1.5 gives the upper constant
  `(e^2-1)/(2(e^2+1))` for the general strictly-increasing problem.

The exact transplant fails at the quantifiers: the result constructs finite
sequences with many, not all, distinct sums.  It gives neither a prescribed
prefix extension nor energy stability simultaneously along nested prefixes.

### Ruzsa--Shakan--Solymosi--Szemerédi: useful growth and a decisive energy caveat

Imre Ruzsa, George Shakan, József Solymosi, and Endre Szemerédi,
[*On distinct consecutive differences*](https://arxiv.org/html/1910.02159),
arXiv:1910.02159; published in *Combinatorial and Additive Number Theory IV*
(2021), 425--434.

- Theorem 1.1: if `A` has distinct consecutive differences, then
  `|A+B| >> |A||B|^(1/2)`.
- Theorem 1.2 gives the analogous bound, with a `delta`-dependent constant,
  when at least `delta|A|` adjacent differences are distinct.
- Theorem 2.1 gives
  `|A+B||A'+B'| >> (k^3|B||B'|)^(1/2)` when the paired adjacent
  differences of `A,A'` are distinct.
- Example 2 constructs a set with distinct consecutive differences but
  `E_3(A) >= E_3([k]) >> |A|^4`; the convex-set third-energy estimate is
  therefore false under adjacent distinctness alone.

The product in Theorem 2.1 is a product of **sumset cardinalities**, not a
product or geometric mean of the actual contiguous sums.  Example 2 blocks an
adjacent-gap-only energy argument.  It does not refute an argument using the
strictly stronger full Golomb property.

## B. Infinite survival and quantitative separation

### Fabian--Rué--Spiegel: strong infinite Sidon existence

David Fabian, Juanjo Rué, and Christoph Spiegel,
[*On strong infinite Sidon and B_h sets and random sets of integers*](https://doi.org/10.1016/j.jcta.2021.105460),
Journal of Combinatorial Theory, Series A 182 (2021), 105460;
[arXiv:1911.13275](https://arxiv.org/html/1911.13275).

- Equation (1) defines `(alpha,gamma)`-strong `B_h` separation.
- Theorem 2.1 constructs an infinite such set with counting exponent
  `sqrt((h-1+alpha)^2+1)-(h-1+alpha)+o(1)`.
- Theorem 1.3 gives the matching-form universal upper density
  `S(n) <= c n^((1-alpha)/h)` for an `alpha`-strong `B_h` set.

This is genuine quantitative hole repulsion, but only for specially
constructed/deleted sets.  It is not inherited by an arbitrary critical
Golomb ray and is not a theorem extending every prescribed finite prefix.

### O'Bryant: Abel summation and separated extension

Kevin O'Bryant,
[*On the Thickness of Infinite Generalized Sidon Sets, I*](https://arxiv.org/html/2606.28651v3),
arXiv:2606.28651v3 (2026).

- Lemma 6 uses block counts, weights of order
  `(ell log(ell N))^(-1/2)`, Cauchy--Schwarz, and summation by parts to
  extract a logarithmic counting-function obstruction.
- Lemma 9 joins separated finite `g`-Golomb rulers after deleting at most
  `g binom(|V|,2)` elements from the later block.

Lemma 6 is a valuable Abel template, but its state is block occupancy rather
than the interval-hole variable
`log(D_(p,q)/binom(ell+1,2))`.  Lemma 9 is a coarse separated construction;
its naive critical-scale iteration has the already-audited quartic-window
cost and supplies no compatible survival at `O(n^2 log n)`.

## C. Rank-weighted and global-diameter inequalities

### Ma--Yi: exact rank-selected first moment

Chaohang Ma and Xiangjie Yi,
[*An Almost-Covering Threshold for Golomb-Ruler Difference Packings*](https://arxiv.org/html/2608.13739),
arXiv:2608.13739 (2026).

In Theorem 4.1, all distances of ranks through `q` are selected from `b`
fixed-mark rulers.  Their global distinctness gives the lower bound
`bm_q(bm_q+1)/2`, while each adjacent gap's multiplicity gives the upper
bound `bU q(q+1)/2`.  This is the closest published rank-lag first-moment
calculation.  It is additive, finite, and fixed-mark; it has no logarithmic
product and no nested one-ray survival conclusion.

### Carter--Hunter--O'Bryant and Lindström: total diameter only

D. Carter, Z. Hunter, and K. O'Bryant,
[*On the diameter of finite Sidon sets*](https://doi.org/10.1007/s10474-024-01499-8),
Acta Mathematica Hungarica 175 (2025), 108--126.

Their main theorem gives

\[
 \operatorname{diam}(S)\geq k^2-bk^{3/2}-O(k),\qquad b\leq1.96365,
\]

and a hand-checkable proof with `b<=1.99058`.  This improves the classical
lower-order constant associated with Bernt Lindström,
[*An inequality for B2-sequences*](https://doi.org/10.1016/S0021-9800(69)80124-9),
Journal of Combinatorial Theory 6 (1969), 211--212.

For P17 the limitation is quantitative: taking logarithms gives

\[
 \log\operatorname{diam}(S)\geq2\log k-O(k^{-1/2}).
\]

Thus even the 2025 improvement changes the logarithmic lower bound only by a
vanishing lower-order correction to its `2 log k` term.  When applied to a
contained interval, `k` does encode the interval length and yields a
constant-order gain over the triangular full-span floor.  It does not see
endpoint placement, cross-length coupling, or nested survival and cannot
repay an `O(log log m)` secondary profile.  The often-quoted explicit Golomb
bound `G(k)>k^2-2k\sqrt{k}+\sqrt{k}-2` is an inverse-function translation of
the finite-Sidon estimate in later expositions; it should not be quoted as the
literal displayed theorem of Lindström without that caveat.

### Ding: rank-and-power moments at the wrong density

Yuchen Ding,
[*Dense finite Sidon sets on arithmetic progressions*](https://arxiv.org/html/2606.15041v2#Thmtheorem4),
arXiv:2606.15041v2 (2026), Theorem 4, gives exact rank-and-power weighted
sums with error proportional to

\[
 t^s n^\ell\Phi(S,n)\log(2n),\qquad
 \Phi(S,n)=n^{1/2}
 \left(\left|1-|S|n^{-1/2}\right|+n^{-1/4}\right)^{1/2}.
\]

At a critical P17 prefix, `2m/sqrt(N_(2m))` may tend to zero, so this error is
not perturbative.  The theorem controls mark moments, not the interval-hole or
cross-ratio channels.

### Riblet: few-interval support is an extra hypothesis

Robin Riblet,
[*Sidon sets in a union of intervals*](https://arxiv.org/html/2202.01296),
Acta Mathematica Hungarica 167 (2022), 533--547,
[DOI 10.1007/s10474-022-01246-x](https://doi.org/10.1007/s10474-022-01246-x).

- Theorem 2.1 finds a Sidon subset of size at least `0.876 sqrt(n)` in a
  union of two integer intervals of total size `n`.
- Theorem 3.1 gives small-difference upper bounds for a Sidon subset of a
  union of `k` intervals in three regimes of `k`.

P17 currently has no theorem placing its interval differences in a union of
few intervals.  Without that new localization, the result does not interface
with the survival--Abel ledger.

## D. Positive measures and vanishing boxes on trees

### Cohen--Colonna--Singman: exact vanishing criterion on radial trees

Joel M. Cohen, Flavia Colonna, and David Singman,
[*Carleson and Vanishing Carleson Measures on Radial Trees*](https://doi.org/10.1007/s00009-012-0232-2),
Mediterranean Journal of Mathematics 10 (2013);
[author PDF](https://math.gmu.edu/~dsingman/VCRadial_4.pdf).

- Definition 5.1 uses the shadow ratio
  `sigma(S_v)/m(I_v)^s` for the `s`-Carleson norm.
- Definition 6.1 requires this ratio to tend to zero as `|v|` tends to
  infinity.
- Theorem 6.1 equates that vanishing condition, for finite `sigma` and
  `s>=1`, with compact Poisson embeddings
  `L^p(partial T)->L^(sp)(sigma)` for every `1<p<infinity`, as well as kernel
  and weak-convergence formulations.

This is the closest exact positive-measure vanishing-box theorem.  It is one
radial tree and gives a qualitative limit, not a bi-/tri-tree encoding or a
summable rate that yields `o(log J)`.

### Ottazzi--Santagati: arbitrary locally finite one-tree boundedness

Alessandro Ottazzi and Federico Santagati,
[*Carleson Measures on Locally Finite Trees*](https://doi.org/10.1007/s12220-024-01823-2),
Journal of Geometric Analysis 34 (2024), article 368;
[arXiv:2405.08358](https://arxiv.org/html/2405.08358).

Definition 2.5 makes `sigma(T_x)<=C nu(partial T_x)` the sector test.
Theorem 2.7 in arXiv v1 (renumbered Theorem 2.8 in the journal version)
equates it with Poisson `L^p` boundedness for `p>1`, weak type `(1,1)`, and an
`H^p` formulation.  This removes radial geometry but remains a single tree
and a boundedness theorem, not the product-tree arithmetic encoding the
separate Route B alternative needs.

### El-Fallah--Kellay--Mashreghi--Ransford: sharp Dini summability

Omar El-Fallah, Karim Kellay, Javad Mashreghi, and Thomas Ransford,
[*One-box conditions for Carleson measures for the Dirichlet space*](https://doi.org/10.1090/S0002-9939-2014-12248-9),
Proceedings of the American Mathematical Society 143 (2015), 679--684;
[arXiv:1902.05932](https://arxiv.org/html/1902.05932).

- Theorem 1.1: `mu(S(I))=O(phi(|I|))` and
  `integral phi(x)/x dx<infinity` imply a Dirichlet Carleson measure.
- Theorem 1.2 proves sharpness: under the stated monotonicity hypotheses, a
  divergent integral admits a measure satisfying the one-box profile that is
  not Carleson.

This is the precise warning for Route B.  Merely having box constants tend to
zero is not automatically enough; a summability profile is needed.  The paper
does not construct the separate Route B measure or encode its two/three tree
coordinates.

The product-weight bi-/tri-tree amplification theorems, the pruned-bi-tree
counterexample, and the `T^4` obstruction remain exactly as audited in Wave 10;
no Wave 11 source supersedes them.

## E. Bottom line for P17 and the separate Route B alternative

The literature supplies four reusable components:

1. the exact gap-vector interpretation;
2. finite additive-energy constructions and an adjacent-distinctness energy
   counterexample;
3. an Abel-summation template and a coarse separated-extension lemma;
4. qualitative or Dini-quantified one-tree Carleson endpoints.

It does not supply the missing P17 statement: on one fixed infinite
eventually-critical Golomb ray, the triangular-gap premium plus boundary slack
captures all but `o(log J)` of the remaining endpoint profile.  As a separate
sufficient Route B alternative, it also does not construct a positive measure
with a sufficiently summable vanishing product-box constant.  No equivalence
between these routes has been proved.

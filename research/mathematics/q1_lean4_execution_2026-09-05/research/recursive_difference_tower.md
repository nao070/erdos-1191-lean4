# Recursive full difference banks and nested integer rulers

Date: 2026-09-05. Author: `/root/global_route`, GPT-6 Astra Ultra.
Status: exact reduction using an external, unformalized reconstruction
theorem. Original Erdős #1191 Q1 remains unresolved. This note reports no
Lean verification and constructs no tower satisfying the critical cap.

## 1. Source verification and the precise external input

The requested reference is Ahmad Bekir and Solomon W. Golomb,
*There Are No Further Counterexamples to S. Piccard's Theorem*,
IEEE Transactions on Information Theory **53**(8), 2864–2867 (2007),
[DOI 10.1109/TIT.2007.899468](https://doi.org/10.1109/TIT.2007.899468).
Crossref identifies IEEE article **4276910**. The publisher returned a
JavaScript verification page; OpenAlex reports no open-access location.
**The 2007 full text has not been obtained or read in this review.**
Metadata and later citations are not recorded as verification of its proof.

The primary technical paper actually read is J. Ranieri, A. Chebira,
Y. M. Lu, M. Vetterli, *Phase Retrieval for Sparse Signals: Uniqueness
Conditions*, [arXiv:1308.3058v2](https://arxiv.org/pdf/1308.3058v2),
26 September 2013. Section IV-A, printed p. 6, Theorem 1, explicitly
attributes the collision-free point-set reconstruction result to its
reference [13], the Bekir–Golomb paper. Translation and reflection are
included in the equivalence convention on printed p. 2, equation (1).
This is a direct reading of the later technical paper's statement,
not an independent proof audit of the theorem it cites.

Here is the external input in the exact form used below:

> **CFU.** If finite sets `X,Y ⊂ R` have the same cardinality `r ≥ 7`,
> every positive pair distance in either set occurs just once, and their
> sets of positive pair distances are equal, then `Y = c + εX` for
> some real `c` and `ε ∈ {−1,1}`.

The stated exception has six points. Theorem 1 displays the two families

\[
 \{0,u,v-2u,2v-2u,2v,3v-u\},\qquad
 \{0,u,2u+v,u+2v,2v-u,3v-u\}.
\]

Its collision-free hypothesis still applies; degenerate parameters are
not a license to use a set with repeated points or distances. CFU has no
generic-position, asymptotic, probabilistic, or unequal-amplitude
hypothesis. It is a support/point-set theorem, before the paper's later
claims about signal coefficients. This note only needs `r ≥ 7`.

The ordinary-line hypothesis matters: these are distances in `R`, not
differences modulo a period. The zero diagonal is not required to occur
only once as an ordered-pair multiset. The relevant condition is that
the `binom(r,2)` **positive** distances are all different. Thus the
theorem applies to integer Sidon sets in the usual sense including
repeated summands. Distances as sets and as positive multisets then agree.

No further search is needed for the reduction below. The source boundary
will remain explicit if the original 2007 proof is verified later.

## 2. Full tower hypotheses force actual finite rulers

For a finite set `X ⊂ Z`, put

\[
 \Delta X=\{y-x:x,y\in X,\ x<y\}.
\]

Suppose finite positive integer sets `F_n` (`n ≥ 1`) and `G_n`
(`n ≥ 2`) satisfy

\[
 F_1=\varnothing,\qquad |G_n|=n-1,\qquad
 \Delta G_n=F_{n-1},\qquad
 F_n=F_{n-1}\mathbin{\dot\cup}G_n.                 \tag{1}
\]

No separate Sidon assumption on `G_n` is necessary. Induction yields
`|F_n|=binom(n,2)`. The map from the unordered pairs of distinct elements
of `G_n` to their positive distances is surjective onto `F_(n−1)`.
Its domain and image both have cardinality `binom(n−1,2)`, so it is
injective. Consequently `G_n` has distinct positive distances.

Distinct positive distances are equivalent to uniqueness of unordered
two-sums, including repeated summands: a nontrivial two-sum equality
can be rearranged into an equality of two different positive-distance
representations, and conversely. In particular a three-term arithmetic
progression is excluded; repeated summands have not been dropped.

Now define

\[
 Q_n=\{0\}\cup G_n.
\]

It has `n` points. Distances between its nonzero points are the distinct
labels `F_(n−1)`, and distances from zero are exactly the distinct labels
`G_n`. Disjointness in (1) proves

\[
 Q_n\text{ is an integer Sidon ruler},\qquad
 \Delta Q_n=F_n.                                  \tag{2}
\]

This section is elementary and does not use CFU.

## 3. Tail realization theorem, with the six-point issue removed

**Theorem, using CFU.** Every tower (1) admits finite integer Sidon sets
`P_n`, for all `n ≥ 7`, with

\[
 |P_n|=n,\qquad 0\in P_7\subset P_8\subset\cdots,
 \qquad \Delta P_n=F_n.                           \tag{3}
\]

At each step, the new point is strictly to the left or strictly to the
right of every old point. In particular their union is an infinite
integer Sidon set with one common anchor.

**Proof.** Start with `P_7=Q_7={0}∪G_7`. Suppose `P_(n−1)` has been
constructed for some `n ≥ 8`. By (1) and (3), the two sets `G_n` and
`P_(n−1)` have `n−1 ≥ 7` points, distinct positive distances, and

\[
 \Delta G_n=F_{n-1}=\Delta P_{n-1}.
\]

CFU gives an isometry `φ_n(x)=c_n+ε_n x` carrying `G_n` onto
`P_(n−1)`. Its translation `c_n` is an integer: choose any integer
`g∈G_n`, and use `c_n=φ_n(g)−ε_n g`. Define

\[
 P_n=\phi_n(Q_n)=P_{n-1}\cup\{\phi_n(0)\}.        \tag{4}
\]

Since `G_n` consists of positive integers, `0` is strictly to one side
of it. Thus `φ_n(0)` is strictly outside the old interval, so it is a
new point and (4) is a genuine nested extension. Isometries preserve
Sidonness and all distances, giving (3) at rank `n`.

No previously chosen point is moved at this step: the isometry is
applied to the *incoming* ruler and its old subset is identified with
the already fixed `P_(n−1)`. The common anchor therefore stays fixed.
The union is infinite because cardinalities increase, and is Sidon
because every proposed equality among finitely many points lies in
one finite Sidon `P_n`. This completes the proof.

The reason for starting at seven is exact. Constructing `P_7` from an
arbitrarily fixed `P_6` would compare two six-point rulers, where CFU
need not hold. Starting directly from `Q_7` removes this one transition;
every later comparison has at least seven points. We do not assert
that the original first six banks have a nested realization inside
this particular `P_7`. No asymptotic hypothesis is harmed by discarding
those finite initial choices.

## 4. Exact diameter increment and left/right interpretation

Put `H_1=0` and `H_n=max F_n` for `n ≥ 2`. Let `u_n=min G_n`.
For `n ≥ 3`, (1) gives

\[
 \max G_n-\min G_n=\max\Delta G_n=H_{n-1}.
\]

For `n=2`, `G_2` is a singleton and the same identity holds with
`H_1=0`. Since `u_n>0`, the maximum of `G_n` exceeds `H_(n−1)`, so

\[
 \boxed{H_n=H_{n-1}+u_n=\sum_{j=2}^n u_j.}        \tag{5}
\]

For the nested realization, `diam(P_n)=H_n`. More explicitly, write
the old extrema as `l_n,r_n`. If the matching isometry in (4) preserves
orientation, its new point is `l_n−u_n`. If it reverses orientation,
its new point is `r_n+u_n`. Thus its distance from the nearest old
endpoint is always exactly `u_n`, and reflection introduces no loss
in diameter. The two cases follow by mapping the minimum of `G_n`
to the relevant old endpoint.

Equation (5) is an additional exact constraint on a putative capped
tower. It is not a lower bound strong enough to contradict
`H_n=O(n² log n)`; that remains the substantive problem.

## 5. Consequence for the critical-cap construction problem

The elementary recurrence (1), CFU, and the independently verified
folding argument in
[two_sided_sidon_folding.md](two_sided_sidon_folding.md)
give the following conditional reduction:

* If one constructs a single infinite tower (1) with one eventual
  bound `H_n ≤ C n² log(2n)`, it gives a nested integer Sidon history
  with those diameters.
* Its common anchor allows the one-time map
  `f(a)=4a+1` for `a≥0` and `f(a)=−4a+2` for `a<0`.
  The folded increasing sequence satisfies `b_n≤4H_n+2` for all
  `n≥7`, so it satisfies the required fixed-onset critical cap.
* Conversely an increasing infinite positive Sidon sequence gives
  (1) with `G_n={a_n−a_i:i<n}` and `H_n=a_n−a_1`.

Therefore, using CFU, the **existence** of a critical-cap full tower is
equivalent to the existence of the counterexample sought in Q1's
integer formulation. It is not a relaxation whose endpoint incidence
can be deferred indefinitely. No such critical-cap tower is supplied
here.

The coherent independent-label birth field from previous notes does
not satisfy `ΔG_n=F_(n−1)`. Leading density, Schur flux, Fejér bounds,
or even repaired batch cardinalities do not establish this identity.
This reconstruction reduction must not be read as promoting that
abstract field to an actual Sidon set.

## 6. Independent review of the folding companion

The companion `two_sided_sidon_folding.md` was read in full. The
following points were independently checked: the residues of the
three pair types are `2,0,3 mod 4`; a mixed folded-sum equality gives
an original two-sum equality with its wrong matching excluded by
opposite signs; repeated summands remain included; a common anchor
and diameter `H_n` imply `b_n≤4H_n+2`; and its cardinality argument
establishing (2) from (1) is exact. The only external step needed to
make its nested-congruence paragraph unconditional in ordinary
mathematics is CFU. CFU itself is not formalized or reproved here.

Original Q1 remains unresolved, and there is no new Lean completion
claim in this note.

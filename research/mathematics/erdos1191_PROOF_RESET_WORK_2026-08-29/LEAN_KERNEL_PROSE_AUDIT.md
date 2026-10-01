# Lean kernel companion: independent human-readable proofs

Date: 2026-08-30 (Asia/Tokyo)  
Scope: only the theorems exported by the current L1, generic-L3, and finite
prefix/scale transport kernel  
Global status: `UNRESOLVED_AT_HARD_LIMIT`

This document supplies a proof argument readable independently of Lean syntax
for every theorem currently eligible for the `FORMAL_THEOREM` label.  The Lean
files check the same claims at the pinned toolchain; this companion does not
assert L2, the Wave-specific L3 identity, L4, L5, Q1, or Q2.

Throughout, `a : N -> N` is zero-indexed and strictly increasing when that
hypothesis is stated.  Differences are interpreted in `Z`.

## 1. Casting the Sidon sum equation

### `additiveSidonNat_iff_additiveSidon`

For natural numbers, equality is preserved and reflected by the canonical
embedding `N -> Z`.  Hence

`a_i+a_j=a_k+a_l` in `N`

holds exactly when the same equality holds after all four terms are cast to
`Z`.  The unordered-index conclusion is unchanged.  Applying this observation
in both directions proves the equivalence.

### `additiveSidonNatUpTo_iff_additiveSidonUpTo`

The preceding argument is unchanged after adding the four assumptions
`i,j,k,l<=N`; the bounds concern only indices and are carried through
verbatim.

## 2. Unique sums and unique positive differences

### `additiveSidon_iff_positiveDifferenceUnique`

Assume first that unordered two-term sums are unique.  If `i<j`, `k<l`, and

`a_j-a_i=a_l-a_k`,

then `a_j+a_k=a_l+a_i`.  Sum uniqueness says either `(j,k)=(l,i)`, which is
equivalent to `(i,j)=(k,l)`, or `(j,k)=(i,l)`.  The second alternative forces
`j=i`, contradicting `i<j`.  Thus the positive difference representation is
unique.

Conversely, suppose positive differences are unique and
`a_i+a_j=a_k+a_l`.  Compare `i` and `k`.

- If `i=k`, cancellation and injectivity of the strictly increasing sequence
  give `j=l`.
- If `i<k`, then `a_k-a_i=a_j-a_l`.  The left side is positive, so
  `a_l<a_j`; strict monotonicity reflects this as `l<j`.  Uniqueness applied
  to the endpoint pairs `(i,k)` and `(l,j)` gives `i=l` and `k=j`, the crossed
  unordered equality.
- If `k<i`, the symmetric argument gives `k=j` and `i=l`.

These three cases are exactly uniqueness of the unordered sum representation.

### `additiveSidonNat_iff_positiveDifferenceUnique`

Compose the cast equivalence of Section 1 with the sum/difference equivalence
just proved.  No new hypothesis or arithmetic step is introduced.

### `additiveSidonUpTo_iff_positiveDifferenceUniqueUpTo`

Repeat the preceding case proof with all endpoints at most `N`.  In the
sum-to-difference direction, `i<j<=N` and `k<l<=N` also give `i,k<=N`.  In the
difference-to-sum direction, each derived ordered pair uses only the original
four indices, so the prefix bounds remain valid.

## 3. Gaps and contiguous sums

Define `h_r=a_(r+1)-a_r` in `Z`.

### `sum_adjacentGap_Ico`

For `i<=j`, expand

`h_i+h_(i+1)+...+h_(j-1)`.

Every intermediate `+a_r` cancels the following `-a_r`, leaving `a_j-a_i`.
When `i=j`, both the half-open sum and `a_i-a_i` are zero.  This also gives a
formal induction on `j` by adjoining the last gap.

### `positiveDifferenceUniqueUpTo_iff_contiguousGapSumsUniqueUpTo`

Every nonempty interval `i<j<=N` has contiguous gap sum `a_j-a_i` by the
telescope.  Therefore equality of two such sums is precisely equality of two
positive endpoint differences.  Substituting the telescope in either
definition proves both implications without changing endpoints or bounds.

### `additiveSidonUpTo_iff_contiguousGapSumsUniqueUpTo`

Under strict monotonicity, finite additive-Sidon sums are equivalent to unique
positive differences by Section 2, and unique positive differences are
equivalent to unique nonempty contiguous gap sums by the preceding theorem.
Transitivity proves the claim.

### `additiveSidonNatUpTo_iff_contiguousGapSumsUniqueUpTo`

First replace the direct natural-sum definition by its integer-cast equivalent
from Section 1, then apply the preceding finite Sidon/gap equivalence.

### `adjacentGap_pos`

Strict monotonicity gives `a_r<a_(r+1)`.  Casting this strict inequality to
`Z` and subtracting `a_r` gives `0<a_(r+1)-a_r=h_r`.

### `adjacentGap_injectiveUpTo`

Suppose `h_i=h_k`, with `i+1,k+1<=N`.  These are the positive differences
from the one-step endpoint pairs `(i,i+1)` and `(k,k+1)`.  Finite positive-
difference uniqueness therefore gives equality of both endpoint pairs, in
particular `i=k`.

### `adjacentGaps_positive_and_distinct`

Apply `adjacentGap_pos` separately to `i` and `k`, and use
`adjacentGap_injectiveUpTo` for the implication from equality of the two gaps
to equality of their indices.  The theorem merely packages these three facts.

### `emptyInterval_endpointMutation_is_false`

If nonempty hypotheses `i<j` and `k<l` were weakened to `i<=j` and `k<=l`,
take `[i,j)=[0,0)` and `[k,l)=[1,1)` (with `N>=1`).  Both gap sums are empty
and hence zero, but their endpoints are different.  Thus the mutated
uniqueness statement is false.  This is the explicit endpoint red-team case.

## 4. Generic finite telescopes and Abel summation

### `sum_forwardDiff_range`

In any additive commutative group,

`(x_1-x_0)+(x_2-x_1)+...+(x_n-x_(n-1))=x_n-x_0`

by pairwise cancellation.  The empty `n=0` sum equals `x_0-x_0=0`.
Appending the last difference proves the identity inductively for every `n`.

### `finiteAbel_range`

Put `G_i=sum_(j=0)^i g_j`.  For `n>0`, write each `g_i` as the increment of
these partial sums and collect the coefficient of each `G_i`.  Interior
partial sums receive `f_i-f_(i+1)`, while the terminal partial sum receives
`f_(n-1)`.  Hence

`sum_(i=0)^(n-1) f_i g_i`

`= f_(n-1) sum_(i=0)^(n-1) g_i`

`  - sum_(i=0)^(n-2) (f_(i+1)-f_i) sum_(j=0)^i g_j`.

This is exactly the theorem's `Finset.range` formula.  At `n=0`, every sum is
empty and the apparently terminal factor multiplies zero, so both sides are
zero.  The argument uses only distributivity and additive cancellation in a
commutative ring.

### `finiteAbel_rational_fixture`

For `f_i=2^i`, `g_i=2i+3`, and `i=0,1,2,3`, the direct terms are

`3, 10, 28, 72`, whose sum is `113`.

The total partial sum of `g` is `3+5+7+9=24`, so the terminal contribution is
`2^3*24=192`.  The three coefficient differences are `1,2,4`, and the
corresponding partial sums of `g` are `3,8,15`; their repayment contribution
is `1*3+2*8+4*15=79`.  Thus `192-79=113`, verifying all three exact rational
equalities.

## 5. Finite prefix/scale transport identities

### `prefixScaleCurl`

Expand both sides using subtraction as addition of an inverse.  Each side is

`C_(j+1,r)-C_(j,r)-C_(j+1,r+1)+C_(j,r+1)`.

Only associativity and commutativity of the additive group are used.  No sign,
positivity, limiting, or Sidon hypothesis enters.

### `finiteScaleAbel_terminal`

Write `s_k=sum_(t=0)^k c_(L+t)`.  In

`sum_(k=0)^(n-1) s_k(delta_(L+k)-delta_(L+k+1))+s_(n-1)delta_(L+n)`,

the coefficient multiplying a fixed `c_(L+t)` is

`sum_(k=t)^(n-1)(delta_(L+k)-delta_(L+k+1))+delta_(L+n)`.

This telescopes exactly to `delta_(L+t)`, which recovers the direct sum.  For
`n=0`, both finite sums and the terminal partial sum are zero.

### `finiteEpochFlux_range` and `finiteGridDivergence_range`

Expand `sum_(e=0)^m a_e(flux_(e+1)-flux_e)`.  The first and last fluxes have
coefficients `-a_0` and `a_m`; every interior `flux_(e+1)` has coefficient
`a_e-a_(e+1)`.  This is the displayed epoch formula.  The grid theorem merely
commutes the two finite sums and applies that identity independently at every
scale index, so no boundary is discarded.

### `finiteEpochScaleAbel_transport`

Apply `finiteScaleAbel_terminal` separately in each of the `m+1` epoch rows.
The result has a scale-difference part and the displayed scale-terminal part.
Multiply each scale prefix by its epoch weight and substitute the supplied
curl equality, turning the scale difference into
`band_(e+1)-band_e`.  Commute the two finite sums and apply
`finiteEpochFlux_range` at each scale.  Its two endpoint terms are precisely
the initial and final prefix boundaries; its interior coefficient is

`w_e scalePrefix_(e,k)-w_(e+1) scalePrefix_(e+1,k)`.

The untouched part is exactly the sum of the `m+1` scale-terminal rows.  All
operations are finite commutative-ring identities, and `n=0` is included.

### `finiteEpochScaleAbel_transport_fromPotential`

Define the epoch increment as `C_(e+1,r)-C_(e,r)` and the retained scale band
as `C_(e,r)-C_(e,r+1)`.  `prefixScaleCurl` supplies the curl hypothesis of the
preceding theorem verbatim.  Substitution therefore gives the unconditional
potential form without adding an assumption.

### `adjacentEpochTwoEdgeFourScaleLedger`

Apply the preceding finite scale-Abel expansion separately to the edges
`A8 -> A16` and `A16 -> A32`, at the four active widths.  Each edge gives four
lower/upper prefix-band occurrences and one upper scale terminal.  In the sum
of the two edge identities, the only repeated physical prefix keys are the
four `A16` bands.  At scale `s` their two coefficients are

`+w8*S8_s` and `-w16*S16_s`.

Distributivity combines them into the single net row

`(w8*S8_s-w16*S16_s)*O16_s`.

The remaining rows are four `A8` initial bands, four `A32` final bands, and
the two untouched upper terminals.  Thus 18 raw occurrences become exactly
14 unique keys.  Expanding `Finset.range 4` reduces both sides to the same
commutative-ring polynomial; Lean closes that finite normalization with
`ring`.  No row is set to zero and no boundary or terminal is discarded.

The separate physical owner statement is not smuggled into this algebra:
the canonical test partitions ranks `7..31` at four scales into fibers of
sizes `4,32,64`, with rank 15 owned by epoch 8.  The theorem itself neither
selects that owner map nor proves the C058 capacity inequality.

## 6. Finite ownership and change-of-basis identities

### `finiteSignedPrimitiveToNetRow`

Expand the finite primitive sum by distributivity.  Its summand at primitive
`p` and row `r` is

`coefficient_p * incidence_(p,r) * test_r`.

Commuting the two finite sums groups these same terms by row instead of by
primitive.  Factoring out `test_r` gives the displayed net-row coefficient
`sum_p coefficient_p * incidence_(p,r)`.  The coefficients are arbitrary ring
elements, so signed cancellation happens inside this exact equality before any
inequality or absolute value is applied.

### `ownerFiberPartitionSum`

For a function from a finite coordinate type to a finite owner type, the
fibers over distinct owners are disjoint and their union is every coordinate.
Summing first over a fiber and then over owners therefore counts each
coordinate value exactly once.  No injectivity or surjectivity of the owner map
is assumed or needed.

### `ownerQuadraticShares_sum` and `finiteQuadraticEnergy_eq_doubleSum`

The coordinate-row contribution is defined as

`q_i * sum_j X_(i,j) q_j`.

Applying `ownerFiberPartitionSum` to precisely these row contributions proves
that the sum of all owner shares is the row-expanded finite quadratic form
`qᵀ X q`.  A final use of distributivity expands it to the finite double sum
`sum_i sum_j q_i X_(i,j) q_j`.  Thus every coordinate row occurs once; the
theorems do not assert positivity, symmetry, a legal birth owner, or C058.

### `fejerRatio_three` and `fejerRatio_ge_nineSixteenths`

At `m=3`, direct rational normalization gives
`((3-1)/3)^2=(2/3)^2=4/9`.  For `m>=4`, put `x=m`.  Since `x>0`, multiplying
the desired inequality by the positive quantity `16x^2` reduces it to

`0 <= 7x^2-32x+16 = (x-4)(7x-4)`.

Both factors are nonnegative for `x>=4`, proving
`((m-1)/m)^2>=9/16`.  This is an exact finite rational inequality, not a
weighted transport or asymptotic C058 assertion.

## 7. Acceptance boundary

The matching Lean theorem names are listed in `LEAN_KERNEL_STATUS.md`; their
individual axiom reports are in `lean_kernel/evidence/axioms.txt`.  This prose
audit and the Lean code use the same zero-based endpoints and half-open gap
intervals.  No theorem here contains an asymptotic limit, an eventual critical
cap, the Wave-specific `Y/R/Z` arrays, a project-specific C058 ownership
allocation, or an implication resolving Q1/Q2.

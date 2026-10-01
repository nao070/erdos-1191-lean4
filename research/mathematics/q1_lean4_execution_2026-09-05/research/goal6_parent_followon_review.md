# Parent review of the bounded follow-on arguments

2026-09-05. Reviewer: `/root`, GPT-6 Astra Ultra.

The complete current `completed_fiber_skew_reindex.md` and
`near_retirement_packing_limits.md` were read and their mathematical
identities independently checked. Both pass within their stated scope.
Neither supplies an original-Q1 conclusion or a Lean-verified theorem.
No numerical or Lean execution was used for this review.

For the skew reindexing, expanding the bridge vectors gives exactly the
coefficient `[sum_(r=i..R-1)J_(r+1)+(i-1)J_i]/2` against `nu_i,e`.
Finite summation by parts yields `(R-1)J_R` minus the stated weighted
increments. The first part cancels against `sum nu=R e` by skew
symmetry. The remaining increment is precisely equation (1). Expanding
`v_r^T K e` leaves only pairs crossing r and proves (2)--(3), with
`lambda_u<=gamma_(u,v)<=lambda_v`. For ambient i<j the sign is
`sign(rho(i)-rho(j))`: an earlier i selects the negative upper-triangular
entry, while an earlier j selects the positive lower-triangular entry.
Thus (7) has the correct orientation and factor `1/(2H^2)`.
The divergence count and its positive last-endpoint value follow by
counting three endpoints per preceding or following triple. Combining
the drift with the mean term uses `K+2Q^T=Q+Q^T` and proves (10).
No individual endpoint balance or sign for its mixed bilinear term is
implied by the constant-potential cancellation.

For the packing note, each old source has degree at most three per
output star, and each new source at most twice the actual star size.
Cauchy first on the edge set and then on the output-rank sum gives
(4). The union degree limits use the unique actual output of each
source pair, so (5)--(7) retain that constraint correctly. Midpoint
variance bounds the class and old-bank square sums by the respective
cardinalities times `H_b^2/4`. Substituting into (4) and
`sum_(r>b)r^-8<=1/(7b^7)` gives exactly
`4sqrt(3/7)*sqrt(U_b(J_b))/b^2`. The union bound becomes
`(b-2)/(2b^2)`; the count bound becomes
`8U_b(J_b)/(b^2(b-1))`. All three constants agree.

At critical diameter, subtracting at most q_b old labels and D_b small
labels leaves the allowance U_b of order H_b. The near-rank window
still contains [2b,3b] eventually. The rank-only lower bound in (15)
therefore holds, but gives no lower bound for the actual weighted sum;
the note preserves this distinction. Its hypothetical scalar counts
are explicitly not an endpoint-realizable construction. In (17) every
physical target occurs once in the outer sum, with all candidate
source-birth multiplicities and the actual output price retained.
The dyad mask and minimum over D_b avoid an unsupported monotonicity
assumption. The final global upper target keeps every source dyad,
including nongood ones. None of these bounds proves the missing
logarithmic saving or pays the separate physical margin.

The current source hashes are bound by
`evidence/goal6_reviewed_research.json`, which is written after this
review. The mathematical scope here is these two full source notes,
not an assertion that every research note or their asymptotic endgame
has been proved.

## Further parent audit: symmetric three-clock deletion

After the preceding review, the complete `three_clock_separation.md`
was read and independently rederived. It passes. In a Born record
the source maximum is the maximum of all three clocks; in a retired
record the output clock is that maximum. Thus the actual price is
exactly w_m in both cases, even with repeated clocks. For two specified
distinct numeric labels the only Schur completions are their sum or
their positive difference. Each completed Schur triple has at most
two source records, so the factor four is sufficient regardless of
the eventual third birth. The count in (4) and q_n formula then give
exactly the constant 16 in (5). The equal-birth count gives
`8(n-2)/(n^2(n-1))<=8/n^2` at n, proving (7).

The repeated numeric case must be handled separately because choosing
two distinct labels at one clock does not see the two occurrences of
x in x+x=2x. There is one candidate source record per x, and
`sum_(p>=2)4/[p^2(p-1)]=4(2-zeta(2))`, so (8) closes that case.
The new-star difference inclusion precludes x and 2x having the same
birth and also precludes all three distinct labels having one birth.
Same-birth source pairs stay outside B and R; the automatic mixed
records are within the equal-clock deletion. No diagonal accounting
is changed. The disjoint Born/retired partition permits the combined
absolute error in (10), and inserting it into the existing Abel
identity gives (11) with at most twice the error. Intersecting these
cores with earlier ones only adds their established absolute errors.
This strengthens localization, but neither a sign of the retained
core nor a source-time commutator estimate follows from the proof.

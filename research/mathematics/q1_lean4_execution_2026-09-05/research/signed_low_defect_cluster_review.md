# Independent review of the low-relative-defect cluster cutoff

2026-09-05, 13:15:41 UTC. Reviewer: `/root/moment_evidence_audit`, inherited
GPT-6 Astra Ultra. Reviewed the entire analytical source
`research/signed_low_defect_cluster.md` and independently rederived all
fourteen displayed equations. Final reviewed SHA-256:
`440b954c5f16eaa35e482ff0ff3a70c2c636aca797020f327f24f092bb49d5e9`.

**Verdict:** the cluster, injective count, price estimates, and both summability
thresholds are valid. No material mathematical correction is needed. The
author applied the sole requested domain clarification, `r≥2` in the definition
of `Q_r` and `w_r`, before this final binding. This prevents a zero denominator
at the unused initial rank; actual low-defect collisions already require six
points. No formulas changed.

This review used no finite computation, Lean build, axiom audit, kernel replay,
or source edit. The earlier exact eligible-energy formulas and the separation
inequality had already been independently reviewed; their scope here remains
analytical. The source does not claim Q1 completion.

## Small defect and the bootstrap

Both sides of the small-defect condition have the same positive automorphism
factor. Combining `G≥8(1+lambda)S/aut` with
`G≤epsilon(1+lambda)DeltaY` and `DeltaY≤16(H*)²/aut` gives exactly
`S≤2epsilon(H*)²`. Repeated old slots are still permitted at this step.

For `0<epsilon≤1/64`, the implication from `t²≤S` to `t≤H*/4` is valid and
slightly weaker than the immediate square-root estimate. In either location
of the maximum `M`, `s≥H*-2t`. Thus `s≥H*/2`, and the product term `ts`
gives `t≤4epsilon H*≤H*/16`. Both pair sums are at least `H*-2t`; the stated
initial lower bound `3H*/4` is safe. Consequently each pair has maximum at
least `3H*/8`, and its minimum is at most
`(16/3)epsilon H*≤H*/12`.

The sharper step uses `S≥t(s+t)≥t(H*-t)` and `H*-t≥15H*/16`, giving the
coefficient `32/15`. Therefore both pair sums are at least `14H*/15`.
Subtracting the prior minimum bound gives

\[
 \frac{14}{15}-\frac1{12}=\frac{17}{20}.
\]

Dividing the product bound by this maximum yields the coefficient `40/17`.
The final near-endpoint bound has exact coefficient

\[
 \frac{32}{15}+\frac{40}{17}=\frac{1144}{255}<\frac92.
\]

This verifies (3)–(7), including every use of the onset threshold `1/64`.

## Six distinct endpoints and spatial geometry

Each nearer old endpoint is at distance at most `5H*/136` below `ell`,
whereas the farther endpoint of the same pair is at distance at least
`17H*/20` below `ell`. Thus neither pair can repeat a value, and the nearer
endpoint is uniquely identified. Neither can equal its triple's distinguished
top endpoint. The supports of the two distinct equal-sum actual Sidon
multisets are disjoint. It follows that all six endpoints are distinct and
`aut=1`; this is a consequence rather than a silently imposed hypothesis.

The four top points lie in the interval of width `(9/2)epsilon H*`, and each
far point is at least `17H*/20` below `n`. The latter statement is valid because
its distance below `n` is `t` plus its distance below `ell`. These far points
are outside the top interval, since `9/128<17/20`. The optional bottom-cluster
identity also has the correct sign:
`u-x=t+(ell-v)-(ell-y)`. Its absolute value is bounded by `t` plus the larger
near distance, so the two far points are within the same short width of the
smallest endpoint.

## Actual injective counting

Fix newest point `a_r`. The three other top points are a genuine three-element
subset of the `k_r-1` earlier actual points in the top interval. Their largest
is `ell`. Assigning the remaining two points to the nearer `U` and `V`
endpoints requires at most two choices. The chosen assignment fixes the
ordered far difference `u-x=a_r+y-ell-v`.

This difference cannot be zero: that would give an actual Sidon two-sum
equality with the uniquely largest point `a_r` on one side and no equal
largest point on the other. Actual nonzero signed-difference uniqueness then
determines at most one ordered pair `(u,x)`, also when the prescribed difference
is negative. The two top-point assignments are the only possible remaining
choices. Invalid reconstructions contribute nothing, and canonical placement
of the newest point in `V` removes any additional side-swap factor.
Therefore `2 binom(k_r-1,3)` is a valid upper count of collisions, with no
record or automorphism multiplicity left over.

The local points form an actual Sidon set of integers in an interval of real
width `(9/2)epsilon H_r`. Its distinct positive integer differences number
`k_r(k_r-1)/2` and each is at most that width. Hence
`(k_r-1)²≤9epsilon H_r`. Combining this with
`2 binom(k_r-1,3)≤(k_r-1)³/3`, or zero when there are fewer than four points,
gives exactly the constant `9` in (10). Four top points also require six
distinct positive differences, giving `epsilon H_r≥4/3`. No assumed relation
between their ranks and `r` enters this spatial count.

## Prices, constants, and convergence

For `r≥2`, `H_r>0` and `Q_r>0`. Every selected collision has `aut=1` and
`DeltaY≤16H_r²`. Multiplication by a single actual output price
`omega_r≤1/(Q_r²H_r²)` and the count in (10) gives the coefficient `144` in
the energy estimate. Division by eight gives `18(1+lambda)` for the carrier.
The defining upper small-defect condition contributes an additional factor
`epsilon_r(1+lambda)` for the defect itself. These are precisely (11).

Under one fixed eventual cap `H_r≤C r² log(2r)`, raising the bound to the
power `3/2` and using `Q_r²≥r⁴/4` yields the constants `576`,
`72(1+lambda)`, and `576(1+lambda)` in (13). The fixed constant and fixed
onset are retained. The compatible complete-history price is bounded by `w`
using monotonic radii; it is never replaced by a source-clock or fresh terminal
price. Each collision has one newest output stage, so no extra retirement-time
sum is present.

For `epsilon_r=log(2r)^(-gamma)` after a sufficiently large fixed onset, the
energy/carrier bound is proportional to

\[
 \frac1{r\log(2r)^{(3\gamma-3)/2}},
\]

and the defect bound to the same expression with exponent
`(5gamma-3)/2`. The positive integral criterion consequently gives
`gamma>5/3` for energy and carrier summability, and `gamma>1` for defect
summability. Finite initial ranks have finite cost and cause no change to
these conclusions.

The two removals are distinct claims. A separately established divergence
survives subtraction of the corresponding finite nonnegative tail, but the
note does not obtain divergence of the complementary defect merely from its
energy and a coefficient tending to zero. Nor would divergent geometric
defect alone resolve the smaller eligible-capacity-minus-demand margin. The
final distinction between those margins and original Q1 is mathematically
necessary and is correctly retained.

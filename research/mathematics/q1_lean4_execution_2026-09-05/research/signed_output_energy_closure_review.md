# Independent review of the eligible output energy budget

2026-09-05, 12:57:58 UTC. Reviewer: `/root/moment_evidence_audit`, inherited
GPT-6 Astra Ultra. Read the complete ten-section source
`research/signed_output_energy_closure.md`; SHA-256 before and after the
review:
`8a1ac50d3e8744757e93a287d8943cea5aebc4dd542cc0f0b2608134122c9b12`.

**Verdict:** equations (1)–(30) and their stated quantifiers are supported. No
material correction is needed. This is an analytical audit, including actual
Sidon endpoint geometry and exact multiset normalization. No finite test,
Lean build, axiom audit, or kernel replay was run. The unresolved
demand-versus-budget comparison remains unresolved.

## Eligibility, carrier, and the stage constant

For a source pair used by a strictly future block, actual output uniqueness
gives `b≤n<i<r`. Conversely `b<i` makes that pair available at old rank `i-1`
to the two-point block with output endpoints of ranks `i,r`. This converse
asserts availability only; it does not assert positivity of that block's
moment demand. The fixed source, including its component diagonal factor `k`,
is retained. Deleting entries is used only to identify which nonnegative pair
payments can occur, without a PSD claim for the deleted matrix.

For an active collision `U,V` with newest point `n` occurring once in `V`, the
four source slots for output `n-m` are precisely the other slots of `U` and
the two old slots of `V`. Unique signed-difference endpoints show that the
latest of those values is the actual latest source clock. Hence eligibility
is equivalent to `m` being the unique second-largest occurrence, on the side
opposite `n`. If it repeats or lies on the same side, there is no eligible
output. This accounts for ties and repetitions rather than ignoring them.

The four formal records at the eligible output have products `-g1,-g2` and
their reflections. The same automorphism divisor applies to their actual
carrier, their energy, and the ineligible records. Doubled numeric groups
retain the formal-list/stabilizer cancellation of the previously audited
multiset partition. Both factors of each `gi` sum to `t`, so
`(gi)^+≤t²/4`. Direct expansion gives the exact carrier (6), the energy
increment (7), and the defect (8). The retained coefficient
`8(1+3lambda)t²` is positive for the stipulated range. The comparison with
Born in (9) follows from `|A-B|≤s+t` and the same positive-part bound.

The stage decomposition includes the full positive variance contribution of
active collisions without an eligible output and twice the nonnegative
Born-only remainder. Thus `G_(lambda,j)≥0` holds without an error term or a
discarded negative class. The factor `(1+lambda)/8` in (11)–(12) is correct.
The output clock, rather than each retired record's source clock, is what
permits collision factorization. The exact layer/Abel identity (13) retains
the complete-history tail.

## Actual two-moment demand and its losses

For a nonempty actual block after old rank `n≥2`, the interval has
`T=L+2H_n` integer sites and the hole-deleted support has `D=T-m>0`. Actual
Sidon difference uniqueness makes both shadows vanish on all block points.
The even feature has mass `m A_n`, first moment `m A_n mu_B`; the odd feature
has zero mass and first moment `m Z_n`. Since `Z_n>0`, the latter shadow
cannot be supported on a single point, so `V_Omega>0`. Every denominator
appearing in this projection is therefore legitimate.

Projection onto the constant and centered-coordinate vectors gives the even
mass term, the even centered first moment, and the odd first moment in (15).
The weighted sum of projection residual squares is nonnegative for
`lambda≥0`. The exact convolution expansion subtracts the diagonal
`m(1+lambda)Z_n`, and its unordered off-diagonal pair sum has factor two.
Actual internal differences of the Sidon block have unique endpoint pairs;
there is no missing output multiplicity in (16).

No additional factor `k` belongs in this raw pair demand. It is computed from
the unmasked two-feature carrier, whose off-diagonal entries agree with the
actual component on block outputs. The larger component diagonal does not
change those paid pair entries. Equation (17) correctly retains the raw
negative-demand case: if `J<0`, the positive-part loss is the full raw pair
sum, not merely a projection residual with the wrong sign. The old
full-interval odd-moment bound is no stronger than this projection, and the
additional even projection is nonnegative; therefore the previously proved
good-block lower demands remain available.

For a prescribed difference-disjoint block family, `S≤Gamma` follows from
actual source ranks, actual internal endpoints, and the span cutoff.
`Gamma-S` measures actual membership failure; it does not identify every
integer in a span with an internal block difference. Decreasing output prices
give `u_r-u_e≥0`. Splitting each eligible pair first by these gates and then
by the block-end price proves (19) exactly. Adding the exact stage defect
gives (20). The projection loss, unused pairs, and geometric defect are all
retained. The absent future-output boundary is absent because it cannot pay
a block contained in the prefix, not because it was erased from historical
capacity.

## Component allocation and summability

For a fixed prefix `P_k`, the candidate row list and eligible physical pair
list are finite. Any row with `J_I>0` has a positive actual carrier pair by
(16); the constraint for that pair bounds its coefficient by one. After
omitting rows with nonpositive objective, the feasible region is compact and
the maximum is attained. The constraints apply to each fixed physical source
pair, so aggregation of row fractions never restarts or duplicates its unit
component budget.

All rows ending by `k` agree with the component carrier on their own actual
outputs. Pair expansion gives the exact three-term residual (22), whose
terms are nonnegative. This checks both comparisons in (23). Existing rows
remain feasible at a larger prefix: they use no new source labels and no
output difference with newly born endpoints. Hence `Pi_k` is nondecreasing;
the source correctly does not infer monotonicity of the residual differences.

Independent allocation at each component proves (24). For `k≥N`, a demand
restricted to blocks in `P_N` has precisely the same row problem `Pi_N`; new
pair constraints have zero masks on those rows. The component tail is
summable and the finite prefix optimizers exist, justifying the equality of
the optimum and the sum. This is an ex post complete-history assertion,
consistent with the explicit absence of an online selection claim.

The identities (25) follow by substituting the layer sums. Young's inequality
gives `E_N≤N² Z_N`; thus
`Y_N≤N(N-1)Z_N≤Q_N² H_N²`. Together with
`u_N≤Q_N^-2/H_N²`, this proves the uniform terminal bounds (26). All series
terms in (25) are nonnegative. Uniform boundedness of the finite margins is
therefore equivalent to convergence of the displayed series in (27), without
requiring monotonicity of `r_k` or `q_k` themselves.

The arithmetic `kappa_k Q_k²=4k/(k+1)²` verifies (28). The use of one fixed
eventual cap for good-block divergence retains one fixed constant and onset.
That divergence is compatible with the logarithmic upper bound and does not
establish either residual convergence criterion, much less a contradiction.

## Historical ineligibility and the endpoint choice

For (29), the remaining four formal product types occur together with their
reflections. If `x+y=t>0`, both factors cannot be negative. For nonnegative
factors, `f_lambda(xy)≤A f_lambda(y)+B f_lambda(x)` follows from
`x≤A,y≤B`. If one is negative, its product has the factor `1+lambda`, and
the positive factor's upper bound gives the same inequality. Applying this
to the two eligible product types, reflecting, and dividing by the same
automorphism factor proves eligible retirement at most ineligible
retirement. Every term has the same output-clock price.

Writing the historical capacity as `E+I+Boundary`, with `I≥E` and
`Dstar≤E`, yields
`C-Dstar≥I+Boundary≥(C+Boundary)/2`. This supports the impossibility of a
bounded **literal historical** margin for this carrier and this row/component
class under the stated cap-based divergence. It does not exclude replacing
that oversized capacity by the eligible budget, changing features or demands,
or proving Q1 by a different argument.

Finally, a normalized row demand is affine in
`theta=lambda/(1+lambda)` before the positive part. Its positive part is
convex. Every interior feasible packing remains feasible at both endpoints;
at `lambda=1` the zero-weight opposite-sign constraints can only disappear.
The chord bound on `[0,1/2]` consequently has coefficients
`(1-2theta)Pi_k(0)+theta Pi_k(1)`, exactly as in (30). Assigning zero weight to
nonpositive endpoint rows is legitimate. The same common-lambda comparison
passes through the nonnegative component sum. No equality of feasible sets
at the endpoint is required.

The recent actual-Sidon Lean modules support the local endpoint cancellation
and opposite-top-two counts used in §2. They do not formalize the complete
orbit partition, the Gram source, the projection demand, the finite packing
optimization, the global series, or this analytical energy estimate. The
reviewed source keeps those scopes separate and does not claim original Q1
completion.

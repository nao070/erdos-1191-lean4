# Final independent consistency review: A29-A31

2026-09-09. Status: PASS. The final three sections match their prior
independent notes; no substantive correction remains. Only these new
sections, their existing evidence, two new supporting Lean statements,
and the stated reuse of source disjointness were checked. There was
no experiment, build, full-library inventory or global audit rerun.

Final WORKING_PROOF.md whole SHA-256:

    9ba2049fdf0831eeebac4f811a26c966bc70e950c91ab91c7b15d037a439fed7

Section hashes, including the heading and following blank lines through
immediately before the next ## heading:

    A29: b6f4686e043aacf921d1f30440e392f447bc09e805ad393293a4cb60983d2366
    A30: 52a31949beec80f75684786df51391578c94e317fb9b7a531c1e1b6894b7ad3a
    A31: da6172f177998bf5b5a95e4af4156f1145aae419b1768915cd5c8e129b0dd416

A29 matches A29_FORBIDDEN_OUTPUT_FOUR_CELL_REVIEW.md. Its exact
prefix identity, selected-label upper bound, actual forbidden-set
disjointness, genuine component sum, future-point increment and the
four-cell data are consistent. The two positive observed increments
are explicitly not a general monotonicity theorem. For k>=T the
unpriced output deficit is fixed while genuine prices keep receiving
components, as required by the two-horizon convention.

A30 matches A30_FIXED_STRATUM_FORBIDDEN_COMPRESSION_REVIEW.md. The
same fixed a is used in both factors and at all components. D* is
explicitly a comparison set. Its scalar limit now has M=T>=3b, so
the reviewed future-capacity condition holds. The nonrealizable
triangle/span/nesting properties are not promoted to actual Sidon
counterexamples.

A31 matches A31_ACTUAL_SLIDING_WINDOW_HOLE_BOUND_REVIEW.md, including
the adopted ambient-window correction. The kernel saving constant,
all-rank cap use, price-saving denominator2359296*3^9, and retained
tail through3b when2b<=T<3b are correct. The log^(-4) statement is
about the guaranteed lower-bound expression, not an upper bound or
asymptotic equality for the actual saving.

The additional sufficient large-b condition is also valid. Put
u=log b and retain b>=max(8,m0). If

    u>=max(2,3072C,(3072C)^(1/4)),

then log(2b)<=2u, and u^4>=3072C gives

    u^5>=3072Cu>=1536C log(2b).

Also exp(u)>=u^2/2 and u>=3072C give

    b>=u^2/2>=1536Cu>=768C log(2b).

This implication uses only scalar inequalities, not capped-prefix
existence. It supplies both additional conditions in A31.3.

LEAN_VERIFICATION_08.json was checked by saved-file readback. All
eight recorded source/log/toolchain hashes match, and the reported
compile72151 and audit76996 both have exit0. Its26 supporting
statements include these two new generic natural-number facts:

* integer_kernel_prefix_identity: sum_(t in S)(H-t) equals the sum
  of prefix cardinalities through j in range H. Here subtraction is
  natural truncated subtraction, correctly encoding zero above H.
* selected_integer_kernel_bound: S subset U and card S<=h imply the
  bound by the sum of min(h,allowed-prefix-cardinality).

Both new recorded axiom lists contain only propext, Classical.choice
and Quot.sound. Real normalization by H and the full actual core/price
instantiation remain outside these generic verified statements.

The existing internalLabels_disjoint statement in SharedDifferenceBudget.lean
was read: it requires two disjoint finite subsets of one actual Sidon
set, precisely matching old versus future point values. It was not
rebuilt or counted as a new supporting theorem. Its source hash is
included separately as mathematical reuse, not fresh compilation.

The companion A29_A31_final_review_manifest.json binds all final
source, section, evidence and readback hashes. A30 compression and
A31 actual-window/price arguments remain hand mathematics. No full
CoreUniform, literal Q1, or final clean dependency/axiom closure is
claimed. The frozen problem remains unresolved; the next input must
retain the full actual short-difference functional and its accumulated
genuine prices instead of replacing it by the final vanishing saving.

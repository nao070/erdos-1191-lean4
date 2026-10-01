# Final independent consistency review: A26-A28

2026-09-09. Status: PASS, with no substantive correction required.
Only the three new mathematical sections, their existing evidence,
and the two new Lean supporting statements were reviewed. No global
audit, finite experiment, evaluator run or build was repeated.

The final WORKING_PROOF.md whole SHA-256 is

    feb47de100cec436b90a146b4dede3f1ce1f153487a0181cbb664393246e30f4

Section hashes, from each UTF-8 ## heading through before the next ##:

    A26: f3480e722669216c9ac17359cec9fef5c8014c85c95dac5c663ca0dd9f731964
    A27: 80a5f7b40f62229fcd14535459cfe0303fe1f0b6926e990bc47f790d2b30d730
    A28: 8424500559aea434a3c4f1a7f83ab39b318d2be4d029e5a4ebf624d627c4e0e0

A26 agrees with INTEGER_MIDDLE_GAP_SIGNED_MEASURE_REVIEW.md and the
saved exact seven-pair trace. The signed measure, threshold lengths
and tails, first moment424373, genuine coefficient,183/68 record
counts, and same-birth/same-type two-use counterexample are unchanged
and correctly scoped to one component of the existing variant M96
history. The general signed identity assumes no positivity of mu.

A27 agrees with FIXED_MIDDLE_PAIR_OCCUPANCY_PRICE_REVIEW.md. The three
sign equations, two-coordinate injections, zero-difference handling,
2pv improvement, finite terminal subtractions, price bounds and beta
constants are correct. The growing finite sum is explicitly a lower
bound on an upper majorant, not an actual norm lower bound or proof
of arbitrarily long fixed-cap prefixes. No cap is used below m0.

A28 agrees with ONE_SIDED_OUTPUT_KERNEL_REVIEW.md. It counts a larger
source label once per fixed output, uses the strict floor cutoff,
preserves both genuine horizons and the terminal coefficient, and
keeps the scalar majorant nondecay separate from actual Sidon inputs.
The final actual-output deficit E_(b,k)>=0 follows from the same
integer packing bound applied to the actual distinct future outputs.
Its weighted accumulation and any monotonicity remain unproved, as
the text states. The forbidden old-difference labels are correctly
identified as additional discarded information.

LEAN_VERIFICATION_07.json was checked by saved-source/log readback:
all eight listed hashes match, and compile/audit exit codes are0.
The manifest reports24 supporting statements, with exactly these two
new declarations:

* signed_integer_tail_first_moment: finite real signed mu, with
  coefficient i+1 and tail condition s<=i; the shift B=i+1 gives A26.1.
  Its recorded axioms are propext, Classical.choice and Quot.sound.
* sidon_ordered_pair_recovery: the unchanged literal Sidon predicate
  on natural points, ordered pairs, and equality of sums or positive
  differences; the conclusion fixes both coordinates. Its recorded
  axioms are propext and Quot.sound.

The readback did not rerun the reported local compile13075 or
audit94117. These generic statements do not establish the full actual
core cardinality, all-horizon pricing/norm estimates, A28 instantiation,
CoreUniform, literal Q1, or final clean dependency/axiom closure.

The final source, section, review-note and evidence hashes are stored
in A26_A28_final_review_manifest.json. The next estimate must retain
the actual common output bank, forbidden old labels and source/output
correlations when summing prices and cuts. Frozen U4-F and Q1 remain
unresolved; no master-goal completion is claimed.

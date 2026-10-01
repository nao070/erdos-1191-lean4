# A36-A40 final independent consistency review

Date: 2026-09-09. Status: PASS; no substantive correction requested.

Only the five new mathematical sections were compared with the five
existing independent review notes. The new frontier and continuation-10
formal-scope text were checked for consistency; older mathematical
sections were not audited again. No finite case, source-bank enumeration,
new history, build or target change was run for this final readback.

## Final source binding

WORKING_PROOF.md whole SHA-256: 0f008659632f6d7d961ff2ab5ba0fdbbf38a16160fefea298c5a5ea8841b3019.

| Section | Exact section SHA-256 |
|:---|:---|
|A36|db060552df5801460f80a6df2e3ade5b899c2ec87709e7352e99444fdfa70d45|
|A37|55d617e7fceb6dc12fe89f418d3893ac98348264642a21d46f261f2310066965|
|A38|4e3e075a47fb8666d2f1e2c63363babd609a63b2b59325137dc8963fa5a9b294|
|A39|d14ffce168f7578fb6320e273a3a61e3b7cc24f3525bd8e71ef29fd23198a679|
|A40|9b2357c1fda2eded692a8bb2b1927f01aa7fdef551b9f5e19183eec5702e1813|

Each section hash covers its exact UTF-8 bytes from its level-two heading
to immediately before the next level-two heading, including whitespace.

## Mathematics and finite scope

- A36 matches the canonical prebank, actual cut exchange and integer
  payment identity. Its relative-payment theorem is restricted to a
  fixed threshold. For a rising threshold, the saved sufficient condition
  L_b<=v-f+1 yields Z_new>=Z_old, which is enough even at equality.
  All 18 exact finite cells, three counterexamples and genuine prices
  match the independent certificate. No raw/source-weighted monotonicity
  is silently inferred from relative monotonicity.
- A37 preserves both horizons and the terminal alpha in its allowance
  error. The constant 1/[3(log 2)^(3/2)] is correct. Equivalence is asserted
  only between the two allowance norms; the text expressly does not infer
  an allowance bound from a bound on the actual profile.
- A38 correctly restricts L to the nonempty eligible interval p<=b<f,
  and truncates it to max(3,L) for the stated cut sum. Its normalized
  genuine prices, nonnegative interval measure and all-pair linear loss
  identity retain the same component coefficients at every cut. A possible
  initial component k=b+1 has capacity zero and penalty zero, so it causes
  no mismatch with the allowance sum beginning at b+2. The square-root
  norm and baseline-minus-loss estimate remain explicitly unproved.
- A39 uses exactly the prescribed saved strict record, with eight labels
  above H25 and positive genuine de mass. It refutes only output-endpoint
  localization and does not claim that the complete mixed bank has no loss.
- A40 retains full oriented record recovery at fixed smaller source e.
  No extra sign or matching factor is missing. The old gap sum, finite
  M+1 tail, p>2/3 exponent and p=3/4 constant
  8/[sqrt(3)(log 2)^(1/8)] agree with the independent hand proof. The
  remaining growing rank strip is a sufficient reduction, not a solved
  CoreUniform or Q1 statement.

The new frontier correctly retains the original strict conditions, fixed
cap, component prices, near-rank remainder and unresolved global norm.

## Lean-10 type and evidence readback

LEAN_VERIFICATION_10.json SHA-256: 9c922c0c5171ff7c8be9fab52ad3950b1f65e2950164a8aff78728607bef076c.

All eight final file bindings match. The saved final compile33607 and
audit39081 both report exit 0. The metadata lists 29 supporting declarations
and exactly these two new declarations:

1. integer_capacity_deletion_identity: a generic natural-number identity
   for the loss of prefix capacity minima after erasing one member c of
   a finite set. It precedes real normalization and actual Sidon cut laws.
2. mixed_shift_fiber_card_bound: for finite old/future subsets of the
   unchanged literal Sidon set, with every old point below every future
   point, the ordered rectangles x<y, i<r and y+i=x+r+e have cardinality
   at most old.card*future.card. The actual displayed type retains both
   order restrictions. It does not include the second source pair, six
   distinct endpoints, strict gates, de weights or the norm estimate.

The displayed source/type and axiom logs for both new lemmas agree with
those scopes. Each depends only on propext, Classical.choice and Quot.sound.
The full A36 relative cut theorem, A37 allowance norm, A38 genuine interval
measure, A39 original core certificate, and A40 weighted/tail/norm theorem
are not declared fully Lean-verified by the mathematical text.

The separate intermediate 28-supporting binding is preserved as historical
evidence: compile46703/audit8726 precede the mixed-shift addition. Its four
listed source/audit/log hashes also match; they are not substituted for
the final 29-supporting source or final logs.

No rebuild or full dependency audit was performed here. Uniform CoreUniform,
literal Q1 or its negation, and final clean Q1 closure remain absent. All
owned finite scripts had already completed; no process is left running.

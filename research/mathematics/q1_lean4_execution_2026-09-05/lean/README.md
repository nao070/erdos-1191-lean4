# Erdős 1191 Q1: frozen target and verified formulation bridges

**This development does not resolve Q1.** `Erdos1191Q1.Q1` is a transparent proposition,
not a theorem asserted by this project. The verified equivalences introduce no Sidon-specific
assumption and do not assume the desired conclusion.

## Verified supporting declarations

- `Erdos1191Q1.mem_countingSet_real`: the finite set used by the counting function contains
  exactly the natural numbers in A with `1 ≤ a` and real-valued `a ≤ x`.
- `Erdos1191Q1.original_iff_integerSquared`: the original real-cutoff lower limit is zero
  if and only if the squared integer inequality has arbitrarily late witnesses for every
  positive real epsilon. This is proved for every set of natural numbers.
- `Erdos1191Q1.q1_iff_q1Integer`: the universally quantified challenge statements agree.
- `Erdos1191Q1.not_original_iff` and `Erdos1191Q1.not_q1_iff`: negation is exactly the
  required eventual positive lower bound on a positive infinite Sidon set.
- `Erdos1191Q1.admissible_exists`: powers of three form a positive infinite Sidon set,
  verifying that the challenge's input conditions are simultaneously satisfiable.
- `Erdos1191Q1.direct_point_quadratic_moments`: the direct quadratic form at arbitrary
  finite rank is compressed to moments while retaining the endpoint factor `q 0 - q n`.
  The separate `path_correction_not_psd_witness` evaluates the proposed correction to
  `-1/18` on one arbitrary vector; that vector is not asserted to be a Haar state.
- `Erdos1191Q1.threeJumpCore_eq`, `threeJumpCore_lower`, and
  `corrected_threeJumpCore_nonneg`: exact algebra for the three prescribed jumps
  `1, -2, 1` at positions `p, p+a, p+a+b` with positive integer gaps. The corrected
  expression is nonnegative. `opposite_two_jump_nonneg` handles a two-jump expression
  whose amplitudes have nonpositive product. These results do not formalize the
  geometric classification of actual translated Haar states and do not prove Q1.
- `Erdos1191Q1.sidon_iff_positiveDifferenceUnique`: the target's unordered-sum Sidon
  condition, including repeated summands, is equivalent to injectivity of every positive
  natural-number difference on ordered actual endpoint pairs. `prefixDifferenceMap_injective`
  gives the literal map from prefix pairs into `[1,H]`. `selectedLabels_card_le` and
  `weighted_positivePairs_le_labels` give cardinal and nonnegative weighted constraints
  for any selected actual difference-label set. No desired density bound is assumed,
  and these elementary Sidon constraints do not establish Q1.
- `Q1.SharedDifferenceBudget` proves the finite convolution first and second moments,
  `total_labelKernel = (U²-S)/2`, and the one-budget inequality for disjoint blocks in
  one actual Sidon set. `shadow_interval_capacity` and `shared_interval_demand_budget`
  prove the inequalities in the form (9) and (13) of `research/difference_extension_route.md`:
  support exclusion and the factor `L+H-m` are derived from actual labels and intervals,
  and positive denominators are proved. `F` is not assumed Sidon; all repeated differences
  between selected labels remain in the kernel's fiber sums.
  The interval theorem explicitly assumes `F ⊆ [1,H]` and positive interval lengths;
  the cumulative quotient form additionally assumes `H > 0`. Thus `H` bounds all labels
  in the chosen finite representation, including any labels assigned weight zero.
- `Q1.PhysicalLabelEnvelope` proves (25)–(27) of `research/growing_label_budget.md`.
  The selected old vectors may vary with `k`. `maskedEpochKernel` sums the contributions
  of `k ∈ I` with `k ≤ j`, then applies the literal masks `1 ≤ t ≤ L j - 1` and
  `t ∉ internalLabels (P j)`. Both masks are proved exact on actual shell labels.
  `growing_prefix_interval_envelope` proves the full demand ≤ actual expenditure ≤
  envelope chain from one Sidon history, actual old/future disjointness, interval
  containment, and nonnegative weights. `physicalEnvelope` is the finite maximum
  over selected shells, with empty-family value zero; its finite support is proved.
  The kernel sums retain repeated relations at the same numeric label before taking
  this maximum. No desired demand/capacity gap is assumed.
  `actual_blocks_envelope_accounting` additionally gives the exact finite partition
  and slack identity described after (28): selected spending, other used labels
  (including old/cross labels), unused labels, and envelope slack sum to the same
  source. The identity explicitly intersects all label sets with finite support `T`.
  Positive `H k` bounds every label in `F k`, as in the earlier interval theorem.
  Nesting and dyadic sizes of actual prefixes are unnecessary for this finite result;
  all subset, disjointness, and eligibility conditions actually used are explicit.

- `Q1.MomentDemand` proves the strengthening in `research/future_moment_demand.md`,
  §§1–4. A signed label vector of mass zero gives the actual shadow first moment
  `|B| * ∑ d ∈ F, d * z d`. Centered Cauchy on an explicit finite container gives
  `LB = (|B| * ∑ d ∈ F, d * z d)² / ∑ x ∈ T, (x-c)²`. A zero variance adds zero.
  For the single full kernel `J + lam zzᵀ`, `momentRawDemand_sub_mass` proves the exact
  raw improvement `lam * LB / 2`, retaining the same full diagonal cost. The lower
  bound is proved from the actual convolution, never added as a payment assumption.
  `momentDemand_le` pays its positive part using the actual difference labels.
  `interval_momentDemand_le` supplies a concrete full-interval container and center;
  the coordinate variance is a literal finite sum, with no cubic closed form claimed.
  The general container contains `shadowLocations` itself; an optimal variance on the
  smaller set after deleting holes where cancellation occurs is not formalized here.
  `shared_momentDemand_envelope` combines varying old banks and signed vectors across
  pairwise disjoint actual blocks in one Sidon set. It retains the old-label/span masks
  and charges each physical label only once against the maximum full matrix kernel.
  The coefficient `lam` is nonnegative and every full matrix entry is nonnegative;
  the signed residual kernel itself need not be. Arbitrary empty banks and blocks are
  allowed, while interval lengths and label bounds remain positive. The exact raw
  improvement need not remain a full improvement after taking positive parts.
  This does not establish a uniform envelope gap or transport across infinite histories.

The difference-label bounds concern a `Finset` of distinct actual endpoint pairs. An argument
that counts the same pair in several windows must separately control that repeated use before
applying these bounds to its full ledger; replacing such a ledger by a set forgets multiplicity.
The shared-budget theorem fixes one old block `P`, label set `F`, and weight function `u`
for all its future blocks. Applying it again to a larger old prefix creates another valid
finite inequality, but does not prove a bound on repeated charging across old-prefix sizes.
The physical-label envelope theorem does combine growing-prefix contributions into one
finite budget. It does not bound that budget uniformly over histories or prove a positive
asymptotic gap. The two claims must not be conflated.
No all-history contradiction or resolution of Q1 is asserted.

`Original` embeds the real-valued normalization into `EReal` before taking `Filter.liminf`.
This is the ordinary mathematical lower limit including infinite values. Taking the
conditionally complete `ℝ` supremum without boundedness hypotheses could turn an infinite
lower limit into the arbitrary value zero; this development avoids that semantic error.

The bridge first characterizes zero lower limit by arbitrarily late small positive values.
It then squares the normalization only for `x ≥ 2`. For the real-to-integer transition,
`N = floor x` has the same count, `log N ≤ log x`, and `x < 2N`; replacing epsilon by
epsilon/2 gives the required integer witness. Integer witnesses are already real witnesses.

## Pinned environment and verification

- Lean: `leanprover/lean4:v4.33.0`, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`.
- mathlib: `db584cd6d46c92f209a44c0f1c829460d327499d`.
- All dependency revisions are fixed in `lake-manifest.json`.
- Dependency sources were copied from the existing project; compiled dependencies were
  obtained through `lake exe cache get`. No build directories are symlinked.
- `Q1.lean` imports the supporting modules and `Q1.AxiomAudit`; `Q1` is the default build
  target, so an ordinary `lake build` checks them.

From this directory:

```sh
lake exe cache get
lake build
lake env lean Q1/AxiomAudit.lean
lake env leanchecker --fresh Q1
```

The built-in `leanchecker` supersedes `lean4checker` starting in Lean 4.28, as documented in
the [official checker repository](https://github.com/leanprover/lean4checker). It replays
declarations with the Lean kernel; it is not an independently implemented external checker.
No comparator/nanoda external-check result is claimed.

`evidence/build.log` records the successful initial project build and elaborated definitions.
`evidence/build-with-direct-moment.log` records the build after the moment module was added.
`evidence/build-with-haar-shape.log` records the build with the three-jump algebra module.
`evidence/build-with-difference-labels.log` records the actual-difference-label bridge and bounds.
`evidence/build-with-shared-difference-budget.log` records the shared convolution budget and
the interval capacity/demand inequalities. Its axiom audit and module replay have their own
source-hash metadata, with the earlier state preserved in
`evidence/verification-before-shared-difference-budget.json`.
`evidence/build-with-physical-label-envelope.log` records integration of the growing-prefix
envelope. Its explicit axiom audit and `leanchecker Q1.PhysicalLabelEnvelope` replay have
separate source-hash metadata. This replay checks the new module in its imported environment,
and does not repeat or extend the scope of earlier fresh dependency replays.
The previous record is preserved in `evidence/verification-before-physical-label-envelope.json`.
`evidence/build-with-moment-demand.log` and its explicit axiom audit record the actual
first-moment demand and shared masked-envelope integration. All 28 new named declarations,
including definitions, are included in the axiom audit. `leanchecker Q1.MomentDemand`
replays the new module in its imported environment; this is not a fresh replay of all
dependencies. Each command has separate source hashes before and after execution in its
`.run.json` file. The previous record is `evidence/verification-before-moment-demand.json`.
`evidence/axiom-allowlist.json` records the explicit allowlist check against `propext`,
`Classical.choice`, and `Quot.sound`. `evidence/leanchecker-fresh.log` records the fresh replay.
Verification status and source hashes are recorded separately in `evidence/verification.json`.
The original bridge/nonvacuity snapshot and the subsequently added direct-moment module
are replayed separately; `evidence/leanchecker-direct-moment-fresh.log` records the latter.
The subsequent HaarShape module has its own fresh replay log
`evidence/leanchecker-haar-shape-fresh.log`. HaarShape verification commands record source
hashes before and after execution in their corresponding `.run.json` files. The verification
record before this addition remains in `evidence/verification-before-haar-shape.json`.
The record before the difference-label module remains in
`evidence/verification-before-difference-labels.json`. Its build and explicit axiom audit
have separate source-bound `.run.json` metadata and do not replace the older replay scopes.

The original `erdos1191_PROOF_RESET_WORK_2026-08-29/lean_kernel` was not modified.

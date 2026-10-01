# Erdős Problem #1191 Q1 — Lean Claim Ledger (historical 54-name scope)

Checkpoint date: 2026-09-09 (Asia/Tokyo)

## Scope and count reconciliation

This ledger covers exactly the 54 keys in
`q1_lean4_execution_2026-09-05/lean/evidence/axiom-allowlist-with-physical-label-envelope.json`.
They are the selected `#print axioms` targets at the
`PhysicalLabelEnvelope` checkpoint, not all declarations in the source files and
not the current project-wide total.

- The eight defining modules contain 115 lexical declarations; 54 were selected
  for that historical audit.
- `MomentDemand` later raised the base selected scope to 82.
- Seven later separate audit scopes (`16+5+16+2+4+7+6`) raised the research
  inventory to 138 distinct supporting declarations across eight saved scopes.
- There is no one-shot combined-138 fresh replay and no final Q1 theorem.

Source paths in the table are relative to
`q1_lean4_execution_2026-09-05/lean/`.

## Evidence and trust legend

- `B54`: saved `lake build` exit 0, explicit axiom audit exit 0, and 54-name
  allowlist PASS at the PhysicalLabelEnvelope checkpoint.
- `F0`: saved `leanchecker --fresh Q1` exit 0 for the earlier target/equivalence
  snapshot.
- `FD`, `FH`: saved fresh replays of `Q1.DirectMoment` and `Q1.HaarShape`.
- `ID`, `IS`, `IP`: saved imports-based replays of `DifferenceLabels`,
  `SharedDifferenceBudget`, and `PhysicalLabelEnvelope`; these are not fresh
  replays of all imports.
- `R26`: on 2026-09-09, current `lake build` and current
  `lake env lean Q1/AxiomAudit.lean` completed successfully, and
  `lake env leanchecker Q1.PhysicalLabelEnvelope` returned exit 0.
- `Std3`: dependency axioms are exactly `propext`, `Classical.choice`, and
  `Quot.sound`.
- `Std2`: dependency axioms are exactly `propext` and `Quot.sound`.

The eight substantive source hashes still match the saved 54 checkpoint. The
aggregators `Q1.lean` and `Q1/AxiomAudit.lean` changed later to import/audit
MomentDemand; this does not alter the eight defining modules. A current lexical
scan found no `sorry`, `admit`, `sorryAx`, custom `axiom`, `native_decide`,
`Lean.ofReduceBool`, or kernel-skip command in those eight files. No comparator
or nanoda independently implemented checker result exists.

`VERIFIED-SUPPORTING` means the stated Lean declaration elaborated, was covered
by the recorded audit/replay evidence, and has only the listed standard axioms.
It never means that Q1 is proved. For `Original` and `Q1`, the status is instead
`VERIFIED-DEFINITION`: Lean checked the definition, but there is no proof term
inhabiting `Q1`.

## The 54 declarations

| # | Declaration | Source:line | Kind | Direct project-local dependencies | Explicit assumptions | Role toward Q1 | Evidence | Axioms | Needed in final path? | Status |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | `Original` | `Q1/Target.lean:44` | definition | `normalized`, `Filter.liminf`, `atTop`, `EReal` | `A : Set ℕ` | Original liminf conclusion for one set | B54,F0,R26 | Std3 | Required: target contract | VERIFIED-DEFINITION; not a proof |
| 2 | `Q1` | `Q1/Target.lean:53` | definition | `Positive`, `Set.Infinite`, `Sidon`, `Original` | every positive infinite Sidon set | Literal original Q1 | B54,F0,R26 | Std3 | Required: target contract | VERIFIED-DEFINITION; no inhabitant/proof |
| 3 | `mem_countingSet_real` | `Q1/Equivalence.lean:9` | theorem | `countingSet`, natural floor membership | none | Fixes inclusive real-cutoff semantics | B54,F0,R26 | Std3 | If integer bridge used | VERIFIED-SUPPORTING |
| 4 | `original_iff_integerSquared` | `Q1/Equivalence.lean:106` | theorem | `original_iff_realSquared`, `realSquared_iff_integerSquared` | arbitrary `A` | Real liminf iff integer squared condition | B54,F0,R26 | Std3 | If integer route used | VERIFIED-SUPPORTING equivalence |
| 5 | `q1_iff_q1Integer` | `Q1/Equivalence.lean:110` | theorem | `Q1`, `Q1Integer`, `original_iff_integerSquared` | none | Universal integer reformulation | B54,F0,R26 | Std3 | If integer route used | VERIFIED-SUPPORTING equivalence |
| 6 | `not_original_iff` | `Q1/Equivalence.lean:129` | theorem | `original_iff_integerSquared`, `not_integerSquared_iff` | arbitrary `A` | Exact one-set counterexample condition | B54,F0,R26 | Std3 | If negative route used | VERIFIED-SUPPORTING equivalence |
| 7 | `not_q1_iff` | `Q1/Equivalence.lean:133` | theorem | `Q1`, `not_original_iff` | existence of positive infinite Sidon set with eventual lower bound | Exact negation of Q1 | B54,F0,R26 | Std3 | If negative route used | VERIFIED-SUPPORTING equivalence |
| 8 | `admissible_exists` | `Q1/Nonvacuity.lean:43` | theorem | `powers_three_sidon`, powers-of-three injectivity | none | Shows target assumptions are nonvacuous | B54,F0,R26 | Std3 | No; semantic sanity check | VERIFIED-SUPPORTING |
| 9 | `direct_gap_quadratic_moments` | `Q1/DirectMoment.lean:86` | theorem | `directGapCoefficient_eq`, `negative_distance_quadratic_moments` | finite `s`, real weights `w` | Moment identity for direct gap form | B54,FD,R26 | Std3 | Conditional: direct-matrix route | VERIFIED-SUPPORTING algebra |
| 10 | `direct_point_quadratic_moments` | `Q1/DirectMoment.lean:106` | theorem | `scaledDirectForm`, `direct_gap_quadratic_moments`, range telescoping | rank `n`, vector `q` | All-rank identity retaining endpoint term | B54,FD,R26 | Std3 | Conditional | VERIFIED-SUPPORTING algebra |
| 11 | `path_correction_not_psd_witness` | `Q1/DirectMoment.lean:117` | theorem | `scaledDirectForm`, `directGapCoefficient` | fixed rank-3 expression | Refutes naive arbitrary-vector PSD correction | B54,FD,R26 | Std3 | No; rejection diagnostic | VERIFIED-SUPPORTING counterexample |
| 12 | `directGapCoefficient_shift_gap` | `Q1/HaarShape.lean:13` | theorem | `directGapCoefficient_eq` | arbitrary `p,a` | Closed form for shifted coefficient | B54,FH,R26 | Std3 | Conditional: Haar route | VERIFIED-SUPPORTING |
| 13 | `threeJumpCore_eq` | `Q1/HaarShape.lean:28` | theorem | `threeJumpCore`, `directGapCoefficient_shift_gap` | `a>0`, `b>0` | Exact `1,-2,1` three-jump formula | B54,FH,R26 | Std3 | Conditional | VERIFIED-SUPPORTING; geometric classification not included |
| 14 | `threeJumpCore_lower` | `Q1/HaarShape.lean:36` | theorem | `threeJumpCore_eq` | `a>0`, `b>0` | Three-jump lower bound `-4` | B54,FH,R26 | Std3 | Conditional | VERIFIED-SUPPORTING |
| 15 | `corrected_threeJumpCore_nonneg` | `Q1/HaarShape.lean:42` | theorem | `threeJumpCore_lower` | `a>0`, `b>0` | Corrected local three-jump nonnegativity | B54,FH,R26 | Std3 | Conditional | VERIFIED-SUPPORTING |
| 16 | `directGapCoefficient_nonpos` | `Q1/HaarShape.lean:48` | theorem | `directGapCoefficient` | none | Sign of all direct coefficients | B54,FH,R26 | Std3 | Conditional | VERIFIED-SUPPORTING |
| 17 | `opposite_two_jump_nonneg` | `Q1/HaarShape.lean:55` | theorem | `directGapCoefficient_nonpos` | `u*v ≤ 0` | Opposite-sign two-jump nonnegative energy | B54,FH,R26 | Std3 | Conditional | VERIFIED-SUPPORTING |
| 18 | `sidon_iff_positiveDifferenceUnique` | `Q1/DifferenceLabels.lean:26` | theorem | `Sidon`, `PositiveDifferenceUnique` | arbitrary `A` | Sum-Sidon iff positive-difference uniqueness | B54,ID,R26 | Std2 | Conditional: difference-label route | VERIFIED-SUPPORTING |
| 19 | `differenceLabel_injOn` | `Q1/DifferenceLabels.lean:54` | theorem | `sidon_iff_positiveDifferenceUnique`, `differenceLabel` | `Sidon A` | Injectivity on actual positive endpoint pairs | B54,ID,R26 | Std2 | Conditional: current budget route | VERIFIED-SUPPORTING |
| 20 | `positivePairs_card_le_labels` | `Q1/DifferenceLabels.lean:64` | theorem | `differenceLabel_injOn` | Sidon; actual positive pairs; all labels in `L` | Bounds pair count by label count | B54,ID,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite bound |
| 21 | `positivePairs_image_card_eq` | `Q1/DifferenceLabels.lean:73` | theorem | `differenceLabel_injOn` | Sidon; actual positive pairs | Label image loses no pairs | B54,ID,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite identity |
| 22 | `weighted_positivePairs_le_labels` | `Q1/DifferenceLabels.lean:79` | theorem | `differenceLabel_injOn`, `Finset.sum_image` | Sidon; actual pairs; image in `L`; `w≥0` on `L` | Nonnegative weighted label budget | B54,ID,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite budget |
| 23 | `selectedLabels_card_le` | `Q1/DifferenceLabels.lean:96` | theorem | `positivePairs_card_le_labels` | Sidon; actual pairs | Unit capacity for selected labels | B54,ID,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite bound |
| 24 | `differenceLabel_fiber_card_le_one` | `Q1/DifferenceLabels.lean:106` | theorem | `selectedLabels_card_le` | Sidon; actual pairs | At most one actual pair per label | B54,ID,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite uniqueness |
| 25 | `prefixDifferenceMap_injective` | `Q1/DifferenceLabels.lean:144` | theorem | `prefixDifferenceMap`, `differenceLabel_injOn`, prefix-actual lemma | `Sidon A` | Injects prefix pairs into `[1,H]` | B54,ID,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite prefix |
| 26 | `prefix_selectedLabels_card_le` | `Q1/DifferenceLabels.lean:154` | theorem | `selectedLabels_card_le`, prefix-actual lemma | `Sidon A` | Prefix selected-label cardinality bound | B54,ID,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite bound |
| 27 | `prefixPositivePairs_card_le` | `Q1/DifferenceLabels.lean:159` | theorem | `positivePairs_card_le_labels`, actual-pair/range lemmas | `Sidon A` | Elementary prefix pair count `≤H` | B54,ID,R26 | Std3 | No; alone insufficient | VERIFIED-SUPPORTING finite bound |
| 28 | `internalLabels_disjoint` | `Q1/SharedDifferenceBudget.lean:33` | theorem | `differenceLabel_injOn`, `internalPairs_actual` | Sidon; actual `B,C`; `Disjoint B C` | Excludes label reuse between disjoint blocks | B54,IS,R26 | Std3 | Conditional: no-double-charge route | VERIFIED-SUPPORTING finite theorem |
| 29 | `labelKernel_eq_shift_sum` | `Q1/SharedDifferenceBudget.lean:87` | theorem | `labelKernel`, `internalPairs`, `differenceLabel` | `t>0` | Identifies fiber kernel with shift correlation | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite identity |
| 30 | `total_labelKernel` | `Q1/SharedDifferenceBudget.lean:124` | theorem | symmetric-sum/diagonal identity, kernel fibers | none | Total budget `(U²-S)/2` | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite identity |
| 31 | `shared_label_budget` | `Q1/SharedDifferenceBudget.lean:155` | theorem | `internalLabels_disjoint`, kernel partial-sum bound, `total_labelKernel` | Sidon; actual old/future blocks; pairwise and old/future disjointness; `u≥0` | Shared budget for one fixed old bank | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING; growing old-prefix reuse not solved |
| 32 | `sum_labelShadow` | `Q1/SharedDifferenceBudget.lean:256` | theorem | `labelShadow`, `shadowRow_sum` | none | Total convolution-shadow mass | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite identity |
| 33 | `sum_sq_labelShadow` | `Q1/SharedDifferenceBudget.lean:268` | theorem | row inner products, correlation-to-kernel identity, label injection | Sidon; `B` actual | Exact second moment of shadow | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite identity |
| 34 | `shadow_cauchy_capacity` | `Q1/SharedDifferenceBudget.lean:296` | theorem | `sum_labelShadow`, `sum_sq_labelShadow`, finite Cauchy | Sidon; `B` actual | Capacity inequality on shadow support | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite capacity |
| 35 | `shadowLocations_disjoint_of_actual_labels` | `Q1/SharedDifferenceBudget.lean:313` | theorem | `internalLabels_disjoint`, positivity of internal labels | Sidon; actual/disjoint `P,B`; `F⊆internalLabels P` | Separates future block from its shadow | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite support fact |
| 36 | `shadow_interval_capacity` | `Q1/SharedDifferenceBudget.lean:352` | theorem | ambient shadow Cauchy bound, interval cardinality | Sidon; `L>0`; actual/disjoint `P,B`; `F` old and in `[1,H]`; `B` in length-`L` interval | Capacity factor `L+H-|B|` | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite local capacity |
| 37 | `shared_interval_demand_budget` | `Q1/SharedDifferenceBudget.lean:383` | theorem | `shadow_interval_capacity`, `shared_label_budget` | Sidon; positive `H,L_j`; actual/disjoint blocks; `u≥0`; label/span bounds | Several future blocks' demand under one fixed-bank budget | B54,IS,R26 | Std3 | Conditional | VERIFIED-SUPPORTING; not an all-history theorem |
| 38 | `le_physicalEnvelope` | `Q1/PhysicalLabelEnvelope.lean:21` | theorem | `physicalEnvelope`, finite supremum | `j∈J` | A shell row is below the same-label maximum | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 39 | `physicalEnvelope_nonneg` | `Q1/PhysicalLabelEnvelope.lean:26` | theorem | `le_physicalEnvelope` | each selected row nonnegative | Envelope nonnegativity | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 40 | `physicalEnvelope_eq_zero_of_notMem` | `Q1/PhysicalLabelEnvelope.lean:33` | theorem | `physicalEnvelope` | every row zero off `T`; `t∉T` | Finite support of envelope | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite support |
| 41 | `disjoint_label_envelope_budget` | `Q1/PhysicalLabelEnvelope.lean:44` | theorem | `le_physicalEnvelope`, `physicalEnvelope_nonneg` | `D_j` pairwise disjoint; rows nonnegative and finitely supported | One-copy maximum-envelope budget | B54,IP,R26 | Std3 | Conditional: current core route | VERIFIED-SUPPORTING finite theorem |
| 42 | `disjoint_label_demand_envelope` | `Q1/PhysicalLabelEnvelope.lean:77` | theorem | `disjoint_label_envelope_budget` | row 41 assumptions plus each local demand bound | Moves finite local demands into shared envelope | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 43 | `actual_blocks_envelope_budget` | `Q1/PhysicalLabelEnvelope.lean:87` | theorem | `internalLabels_disjoint`, `disjoint_label_envelope_budget` | Sidon; actual pairwise-disjoint blocks; nonnegative finite-support rows; local demand | Applies envelope budget to actual Sidon blocks | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 44 | `intervalCapacity_pos` | `Q1/PhysicalLabelEnvelope.lean:107` | theorem | interval cardinality arithmetic | `L>0`, `H>0`, `B` in length-`L` interval | Proves demand denominator positive | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING technical lemma |
| 45 | `intervalLabelDemand_le` | `Q1/PhysicalLabelEnvelope.lean:117` | theorem | `intervalCapacity_pos`, `shadow_interval_capacity`, kernel nonnegativity | Sidon; positive `L,H`; actual/disjoint `P,B`; `u≥0`; old/span/interval bounds | Pays one local demand by actual internal labels | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite local theorem |
| 46 | `internalLabels_mem_interval` | `Q1/PhysicalLabelEnvelope.lean:135` | theorem | `internalLabels`, internal-pair membership | `L>0`; `B` in length-`L` interval; `t` an internal label | Justifies `1≤t≤L-1` mask | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite span fact |
| 47 | `maskedEpochKernel_nonneg` | `Q1/PhysicalLabelEnvelope.lean:157` | theorem | `maskedEpochKernel`, kernel nonnegativity | eligible `u_k≥0`, `alpha_kj≥0` | Nonnegativity of masked epoch row | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 48 | `maskedEpochKernel_supported` | `Q1/PhysicalLabelEnvelope.lean:170` | theorem | kernel support lemma, `epochLabelSupport` | `t` outside all selected label supports | Finite support of epoch kernel | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite support |
| 49 | `maskedEpochKernel_eq_on_actual_labels` | `Q1/PhysicalLabelEnvelope.lean:185` | theorem | `internalLabels_mem_interval`, `internalLabels_disjoint` | Sidon; positive shell length; actual/disjoint old/future blocks; interval membership; actual future label | Both masks are exact on actual future labels | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 50 | `weighted_interval_demand_le_epoch` | `Q1/PhysicalLabelEnvelope.lean:199` | theorem | `intervalLabelDemand_le`, exact-mask theorem | Sidon; positive sizes; actual/disjoint blocks; nonnegative weights; label/span/interval bounds | Pays all eligible old demands inside one shell | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 51 | `growing_prefix_interval_envelope` | `Q1/PhysicalLabelEnvelope.lean:242` | theorem | weighted epoch bound, disjoint envelope budget, mask nonnegativity/support | Sidon; finite `I,J`; actual old/future blocks; all stated disjointness, positivity, span and interval hypotheses | `demand ≤ actual spending ≤ one-label envelope` | B54,IP,R26 | Std3 | Conditional: key current support | VERIFIED-SUPPORTING; no uniform history gap |
| 52 | `label_envelope_accounting` | `Q1/PhysicalLabelEnvelope.lean:283` | theorem | finite set partitions, disjoint finite sums | pairwise-disjoint `D_j`; `D_j⊆V` | Exact selected/other-used/unused/slack split | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite identity |
| 53 | `physicalEnvelope_slack_nonneg` | `Q1/PhysicalLabelEnvelope.lean:314` | theorem | `le_physicalEnvelope` | none beyond membership encoded in sum | Nonnegativity of envelope slack | B54,IP,R26 | Std3 | Conditional | VERIFIED-SUPPORTING finite theorem |
| 54 | `actual_blocks_envelope_accounting` | `Q1/PhysicalLabelEnvelope.lean:324` | theorem | `label_envelope_accounting`, `internalLabels_disjoint` | Sidon; terminal `W` actual; `B_j⊆W`; blocks pairwise disjoint | Exact same-source accounting on an actual history | B54,IP,R26 | Std3 | Conditional: current accounting route | VERIFIED-SUPPORTING; no all-history uniform bound |

## Source identity for the 54-name scope

| Module | Current SHA-256; matches saved 54 snapshot |
|---|---|
| `Q1/Target.lean` | `04e63cd522197f6f9f756bf277f69d88256ffb7025f8f09c1b4903f7d443b5bb` |
| `Q1/Equivalence.lean` | `8cfc044da45d3a4c831a8a6509e494015478157f510cd0726f69e795c8b641f6` |
| `Q1/Nonvacuity.lean` | `5a887c47892b42be9a4b4867d16a80b805278cbf2a8098b5eb327513262160e1` |
| `Q1/DirectMoment.lean` | `23f66277238eb682eed74e1b01758bdeb343679b2522c90abf8eed48c319f649` |
| `Q1/HaarShape.lean` | `1389d55534c67f6d10305d0defbecd396b9c43934ff4a3ac95fd5ce393976169` |
| `Q1/DifferenceLabels.lean` | `b42c5cc787c29906d1341a68520bab16370b08318fe7741c73e4d025ad7adc1d` |
| `Q1/SharedDifferenceBudget.lean` | `ef08da0b99b7251b26321c6d7ffe36fe10e8d447c662602d1c016e3ad70d5257` |
| `Q1/PhysicalLabelEnvelope.lean` | `f831816b0eb28e9d7270cbce45c6f8c9ef5c1a82f78355600c92d99611fe03cd` |

## Ledger conclusion

All 54 selected names were found in current source and in the saved explicit
axiom audit. The evidence is sufficient to label the 52 theorems
`VERIFIED-SUPPORTING` within their stated finite/equivalence scopes and the two
definitions `VERIFIED-DEFINITION`. It is not sufficient—and the source does not
attempt—to label original Q1 as proved. Most entries are conditional on the
chosen integer/difference-label/Haar route; only the literal target definitions
are unavoidable in every final formal path.

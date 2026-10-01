# Reproduce the new U4-F supporting evidence

Status: Q1 and Q1191-U4F-CORE-UNIFORM-01 remain unresolved. These commands
check only the artifacts named below. They are not a final Q1 release build.

From the existing execution Lean directory, with its unchanged toolchain:

```sh
cd /Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/lean
/Users/USER/.elan/bin/lake env lean -o .lake/build/lib/lean/Q1/Target.olean Q1/Target.lean
/Users/USER/.elan/bin/lake env lean -o .lake/build/lib/lean/Q1/U4FProfile.olean Q1/U4FProfile.lean
/Users/USER/.elan/bin/lake env lean ../evidence/u4f_core/U4FProfileAudit.lean
```

The main source is a new standalone supporting module; no target definition,
default Lake target, toolchain, dependency version, or old library source was
changed. The audit prints all new theorem types and their transitive axioms.
Only propext, Classical.choice, and Quot.sound are used. The strict core's
complete Sidon instantiation and the full mathematical upper bound are not
formalized by this module. It is not imported as a literal proof of Q1.

To repeat exact checks on the already saved useful actual histories:

```sh
cd /Users/USER/Documents/ChatGPT/mathematics
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/independent_checker.py q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/C1_m02_greedy_M25.json
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/independent_checker.py q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/C1_m02_greedy_M96.json q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/C1_m02_dense_variant1_M96.json
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/check_graph_defect.py
```

The campaign README describes the original reference evaluation and fixed
generation rules. No large rerun is needed to inspect a new candidate on
these saved records. JSON rational profile coefficients and I_j are exact;
N and square-root block contributions are displayed numerical approximations.

`SOURCE_MANIFEST.json` binds selected unchanged original contracts and source
notes to actual copies. `LEAN_VERIFICATION_10.json` binds the current 29 supporting theorem types,
Lean source, unchanged Target dependency, fixed toolchain/manifest and
accepted `c10_final` compiler/axiom logs. `LEAN_VERIFICATION_09.json` retains
the historical27-theorem source/audit copied under
`source_snapshot/continuation_10/`. `LEAN_VERIFICATION_08.json` retains
the historical26-theorem source/audit copied under
`source_snapshot/continuation_09/`. `LEAN_VERIFICATION_07.json` retains
the historical24-theorem source/audit copied under
`source_snapshot/continuation_08/`. `LEAN_VERIFICATION_06.json` retains
the historical22-theorem source/audit copied under
`source_snapshot/continuation_07/`. `LEAN_VERIFICATION_04.json` retains
the historical18-theorem binding; its source/audit are copied under
`source_snapshot/continuation_06/`. `LEAN_VERIFICATION_03.json` retains
the historical 15-theorem binding; its source/audit are copied under
`source_snapshot/continuation_04/`.
`LEAN_VERIFICATION_02.json` retains the historical 14-theorem binding; its
source and audit are copied in `source_snapshot/continuation_03/`.
`LEAN_VERIFICATION.json` records the historical 11-theorem version; the
previous source is preserved in `source_snapshot/continuation_02/`. The
failed draft and stale-olean audit logs are retained as failure evidence
and are not accepted verification of the current source. `RUNTIME.json` records the
observed model and goal reads: initially null, then the existing master
goal ACTIVE, including the continuation checkpoint. No goal was created,
cleared or completed by these research turns. Read `../../research/u4f_core/WORKING_PROOF.md`
and `ATTEMPTS.jsonl` for the current mathematical frontier.

A08--A12 and their independent review files document the new mathematical
results. The all-history weighted packing and generic Sidon construction,
whole-core record bijection, and small-old-gap summability remain hand
proofs rather than complete Lean theorems. Existing M96 matching, BH/AC
and small-B classifications reuse saved certified records; A12 required
no additional enumeration. None of these is a final Q1 proof.

Continuation 03 adds the reviewed A13 cap-free multiscale obstruction, A14
fixed-cap AC/BH counterexample, and A15 nonlinear first-moment comparison.
The new campaign parameters were fixed in
`finite_campaign/C1000000_m02_M12_target/campaign_fixed_before_trials.json`.
Its independently checked history, exact profile and block square-root
enclosures are in that same directory. The parent also independently
squared all three interval endpoints after dividing by harmonic length
19/90; the check passed. Only the generic integer-mass first-moment lemma
of A15 was newly Lean-verified. Neither A13 nor the full Sidon/core
instantiation nor the remaining BH series is a final Lean theorem.

Continuation 04 adds A16--A19. The supporting module now imports the
unchanged `Q1.Target` for its literal Sidon predicate. That dependency
was compiled from its unchanged source before the supporting module.
The tripartite membership/cardinality and generic indicator increment
are Lean verified; the full profile/collision correspondence and global
potential are not. Existing M12 kernel and two single M96 components
were used. The one new M11 history only falsifies raw-deficit monotonicity
and has an empty original strict core; its certificate explicitly says so.

Continuation 05 adds A20--A23 without changing the Lean source. The
164,670-cell existing M96 scan did not prove monotonicity. A23 now
refutes even the original strict-core effective monotonicity candidate:
one fixed C=10^14,m0=2,M156 history has J_core=71>64. Its whole profile
contains2,435 records, all in the three-large-gap subset. Recheck only
this saved full profile with the unchanged independent checker:

```sh
cd /Users/USER/Documents/ChatGPT/mathematics
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/independent_checker.py q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/C100000000000000_m02_colored_star/C100000000000000_m02_colored_star_t64_M156.json
```

The same campaign directory preserves the parameters fixed before the
single trial, all156 integers, the signed graph, complete target fibers,
full rational profile, strict-gate decisions and checker bindings. The
root's separate old-quadruple reconstruction is in
`colored_star_root_review.json`. No further history is required to
inspect or reproduce this counterexample. A21's count relaxation is
explicitly non-Sidon; A22's cap-dependent support statement is a reviewed
hand proof. Neither is a final Q1 proof or an additional Lean verification.

Continuation06 adds A24--A25. The exact changed-bank collision/deficit
identities, open-cut record boundary law and old-quadruple product
bound are the four new supporting Lean statements. The complete
Sidon/core instantiation and the all-history price/cap envelope remain
reviewed hand proofs. Existing C1 histories at cut24->25, component48,
l6/12/18 supply the exact counterexamples; no new history was generated.
The A25 plateau profile is only a numerical-envelope no-go, explicitly
not an actual Sidon/core construction. For the concrete evidence read
`finite_campaign/CUT_SHIFT_B24_COMPONENT48_REVIEW.md` and
`finite_campaign/FULL_HORIZON_CUT_FLUX_ENVELOPE_REVIEW.md`.

Continuation07 adds A26--A28. Only the signed integer-tail first moment
and actual Sidon ordered-pair recovery are newly Lean verified. The
full projection bound, genuine fixed-pair norm, oriented output packing
and their limits are independently reviewed hand mathematics. The
A26 seven-pair trace reuses the existing C1,m02 variant M96 bank; it
checks183 records,68 all-large-gap records, and exact harmonic coverage.
Read `finite_campaign/INTEGER_MIDDLE_GAP_SIGNED_MEASURE_REVIEW.md` and
`finite_campaign/FIXED_MIDDLE_PAIR_OCCUPANCY_PRICE_REVIEW.md`.
No new history, toolchain change, target change or full-profile scan
was performed. The A28 scalar majorant is explicitly not an actual
Sidon realization or Q1 counterexample.

Continuation08 adds A29--A31. The two new Lean statements are an exact
integer-kernel prefix identity and a bound for selecting at most h
allowed labels. The actual old/future disjointness source already exists
as internalLabels_disjoint; it was not rebuilt or recounted here.
The forbidden-set compression and actual sliding-window/cap/price
estimates are independently reviewed hand proofs, not full Lean
CoreUniform theorems. Four prescribed cells of the existing C1,m02
variant M96 bank were checked, with certified ell and strict gates,
exact rational chains and two exact increments. No new history or
broad/full-profile scan was used. Read the A29 manifest and the A30/A31
review notes in finite_campaign. The scalar compression diagnostic
is explicitly not an actual Sidon difference-set realization.

Continuation09 adds A32--A35. Reuse the existing C1,m02 variant M96 bank
for the exact A32 eight-cell mixed-forbidden comparison; its manifest is
`finite_campaign/A32_A34_review_manifest.json`. A33 far-component
uniformity, A34 deferred penalties/conditional payment and A35 finite
short-horizon price are hand proofs. The only new Lean statement is
`priced_component_far_bound`, a generic component denominator bound.
The pinned local c09 compiler and type/axiom logs exited0. This is not
a full formalization of those hand proofs or final Q1 verification.

Continuation10 adds A36--A40. The finite work is one mixed pair at
18 cells and one prescribed already certified strict record, on the
existing C1,m02 variant M96. See `finite_campaign/A36_A38_review_manifest.json`
and `finite_campaign/A39_A40_review_manifest.json`; no broad rerun is
needed. Two new supporting Lean statements cover integer capacity
deletion and the actual Sidon mixed-shift rectangle count. Accepted
`c10_final` compiler and type/axiom logs exited0 (29 support statements);
intermediate28-support source/logs are also preserved. Full relative
penalty, allowance error, pair measure, weighted rank-tail norm and
original Q1 remain outside these formal checks.

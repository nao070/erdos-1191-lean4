# Fixed-cap finite U4-F campaign, 2026-09-09

All files in this directory were produced for a bounded finite worker
task. The fixed parameters are C=1,m0=2 throughout; no parameter was
refitted as M increased. The histories are genuine increasing positive
integer Sidon prefixes normalized by a_1=1.

No prior exact U4-F evaluator survived the bounded search of the execution
workspace and /private/tmp. `reference_evaluator.py` is a minimal source-pair
enumerator; it is not a new general harness. `independent_checker.py` is
a separate output-endpoint enumeration with a different arithmetic
implementation of rigorous log intervals and a repeated-two-sum Sidon test.
The two programs share no imported mathematical code.

## Results

| Chain | M=T | Core records | N, approximate | Maximum cap use, approximate |
|---|---:|---:|---:|---:|
| Greedy | 12 | 20 | 0.00120107802821217 | 0.2776353 |
| Greedy | 15 | 87 | 0.00246677851170134 | 0.2776353 |
| Greedy | 24 | 675 | 0.00497841700757168 | 0.3471145 |
| Greedy | 48 | 13,411 | 0.00937497943291026 | 0.4280531 |
| Greedy | 96 | 194,966 | 0.0137535103787608 | 0.5276487 |
| Dense variant 1 | 24 | 746 | 0.00502238337839727 | 0.3292297 |
| Dense variant 1 | 48 | 14,027 | 0.00948795234084940 | 0.4080223 |
| Dense variant 1 | 96 | 200,243 | 0.0139134935336990 | 0.5130943 |

Greedy appends the least admissible next integer. Variant 1 skips the
first admissible choice at append steps 3,6,9 (zero-based current-prefix
length) and thereafter follows the same least-admissible extension.
These are two fixed chains, not separate constants for each horizon.
At M=96 their terminal marks are respectively 24768 and 24862.

The supplied M=12 fixture, 20 records and all four exact rational P_b
coefficients match exactly. The independent checker passes M=12,
the useful M=15 witness, and both M=96 profiles, reconstructing every
record, every strict comparison, each price and all I_j.

A later targeted M=25 check, requested for a concrete compensation
counterexample, also passes both implementations (820 records through
T=25). This is one additional witness check, not a new size campaign.

All profile and I_j values, cap comparisons and coverage identities are
exact rational checks. All strict comparisons resolve (UNKNOWN count
zero). N, actual square-root block sums, displayed Cauchy square-root
bounds and cap usage ratios are 55-digit Decimal approximations; their
printed digits are not certified interval endpoints.

The genuine price is always
u_r^[M]=sum_(k=r..M)(alpha_k-alpha_(k+1))/H_k^2, including alpha_(M+1).
Every record contributes once to each actual cut c+1,...,i-1. For each
dyadic block the profile aggregation is checked against re-expansion of
those same records on the same truncated cut range. No independent
per-block budget is created.

## Mathematical observations and strict scope

1. `FACTOR_TWO_WITNESS.md` supplies an exact M=15 witness showing both
   source orientation cases can occur even at fixed (c,e,i,r). Therefore
   the existing factor two cannot simply be replaced by one.
2. For the M=96 greedy profile, the complete-block masses at j=3,4,5
   are approximately 1.79644e-5, 2.58354e-5, 2.75703e-5. They do not
   decrease over those three observed blocks. The smaller j=6 value is
   a truncated terminal block and is not evidence of asymptotic decay.
3. `OUTPUT_BOUND_REVIEW.md` reviews a valid all-history output-correlation
   and cap-sensitive moment bound proposed by the main researcher. It
   also identifies exactly why its remaining constant upper bound cannot
   sum to a uniform N. The finite corroboration is recorded separately.
4. `SCALAR_CLOCK_RELAXATION_NO_GO.md` gives a separate abstract-record
   no-go with N>=64, exact fixed-(c,s) and other listed scalar counts,
   genuine prices and P>=9/2^27 on a fixed logarithmic interval per
   scale. It explicitly fails actual numeric-label/endpoint realization
   and cannot refute the frozen theorem or Q1.
5. `ORIENTATION_COMPENSATION_TAIL_WITNESS.md` independently verifies the
   main researcher's actual-Sidon counterexample to two-sign compensation.
   At fixed T=24, its exact excess changes from negative at M=24 to
   positive at M=25, while all 675 records through T=24 remain unchanged.
6. `REPEATED_COLLISION_FIBER_REVIEW.md` proves the paired-orientation
   repeated-triple identity, retains actual source-birth multiplicity,
   and verifies the fixed-R count and nonsummable common-tail majorant.
   Existing actual records show nine positive-excess source births for
   one oriented collision; no further finite history was generated.
7. `WEIGHTED_FIBER_AND_COVERAGE_REVIEW.md` supplies the exact weighted
   p-image deficit and cubic bound, tests the square-root candidate on
   existing fibers, and quantifies the paired-core subclass's small
   observed mass and coverage fractions.
8. `CAP_FREE_SQRT_FIBER_COUNTERFAMILY.md` reviews an actual generic rational
   Sidon family refuting cap-independent square-root fiber bounds. It
   explicitly fails to preserve one cap constant and does not refute Q1.
9. `WHOLE_CORE_MATCHING_REVIEW.md` gives a bijection of the entire core
   with three matchings of four old endpoints, verifies the complete
   rational profile partition, and records simultaneous actual minus/plus
   core outputs with different ranks, prices and cut intervals. It also
   records the exact BH/AC decomposition (BH has about 83% of observed
   harmonic coverage) and rejects physical-output price ordering at M15.
10. `SMALL_MIDDLE_GAP_REVIEW.md` proves a uniform finite square-root cost
    for the unchanged-core subclass B<=c^2/(log c)^3 and checks the
    remaining cap-dependent BH comparison. Its logarithmic multiplier
    remains a substantive summability obligation.
11. `SMALL_OLD_GAP_UNION_REVIEW.md` extends that finite-cost result to
    min(A,B,Cgap)<=c^2/(log c)^3, with the exact cutwise bound
    1/(2b^2)+48/(log b)^3. This is an independent hand proof without
    further finite enumeration.
12. `LARGE_GAP_AC_BH_CANDIDATE_REVIEW.md` rejects the constant-one
    aggregate cut comparison on an independently checked existing M12
    prefix. Its dyadic version passes the 900 checked block/horizon
    cases across the two existing chains, but remains unproved.

No finite value or failure to find a value proves or disproves uniform
K(C,m0), arbitrarily long capped prefixes, or Q1. No Lean theorem was
proved in this worker task. The frozen theorem remains NEEDS-PROOF.

Each main profile JSON records source SHA-256 values, evaluator hash,
all-rank rational cap certificates, nonzero rational profile coefficients,
exact I_j, actual block contributions, top twenty birth/output/cut intervals,
birth masses, output masses and full arithmetic scope. Record JSON files
use the explicit column list in their header. Independent-check JSON files
bind their input and checker by SHA-256.

## Reproduction

From the repository root:

```sh
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/reference_evaluator.py --sizes 12,24,48,96
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/reference_evaluator.py --sizes 15
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/reference_evaluator.py --sizes 24,48,96 --variant 1 --campaign C1_m02_dense_variant1
python3 q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/independent_checker.py q1_lean4_execution_2026-09-05/evidence/u4f_core/finite_campaign/C1_m02_greedy_M96.json
```

Next nonduplicate action: pursue a weighted aggregate output-correlation
estimate retaining the actual shared bank and price variation, or test
a concrete further candidate against these existing records. No further
size campaign is active or needed merely to enlarge this table.

## Final bounded AC/BH comparison and independent reviews

- `FIXED_CAP_DYADIC_AC_BH_COUNTEREXAMPLE.md`: C=1000000,m0=2,M=T=12 pre-fixed targeted campaign; first padding succeeds, exactly two strictcore records, independent PASS, both cut and dyadic constant-one AC<=BH false. Exact original prices, strict gap/log checks, channel sqrt enclosures, and one-trial manifest are under `C1000000_m02_M12_target/`; reproduction uses `targeted_fixed_C12.py`.
- `A13_CAP_FREE_BH_DIVERGENCE_REVIEW.md`: independent symbolic review PASS for actual infinite Sidon BH divergence without fixed cap, including the explicit violation of every eventual cap. No new blocks computed.
- `A15_CAP_SENSITIVE_FIRST_MOMENT_REVIEW.md`: independent proof review PASS of 8b^2 Q_AC^2+Q_AC<=H_b Q_BH and its fixed-cap/dyadic consequences; missing BH summability remains explicit. Source sections/hashes in `A13_A15_review_source_manifest.json`.

- `BH_SYMMETRIC_GAP_KERNEL_COUNTEREXAMPLE.md`: on the existing certified A14 M12 only, the exact symmetrized BH adjacency-gap kernel has K11=0, K13=u12/2, K33=u12 and (2e1-e3)^T K (2e1-e3)=-u12<0. Both PSD and diagonal-Schwarz candidates fail; actual positive g still gives exactly Q_BH=134/676350675. Reproduction `kernel_from_A14_exact.py`; exact matrix/certificate hashes under `C1000000_m02_M12_target/BH_symmetric_gap_kernel_exact.json`.

- `BH_DIAGONAL_TRIPARTITE_FIBER_REVIEW.md`: independent hand-proof PASS for exact BH diagonal/tripartite collision correspondence, both genuine horizons, and Q_BH(b)<=((b-1)/b)^3/48<1/48. The nondecaying rank-only majorant does not imply summability. No new finite run. Source binding in `BH_diagonal_tripartite_review_sources.json`.

- `TRIPARTITE_EXACT_DEFICIT_REVIEW.md`: exact capacity/fiber/gate/width identity PASS in four cases (two existing M96 histories, all core/all-large-gap, single b24/k48/T96 component). Minimal reproduction `tripartite_deficit_b24_k48.py`, all rational losses and per-l fibers in `tripartite_deficit_b24_k48_exact.json`. Also reviews scalar triangular non-Sidon lower bound 1/20155392, expressly not an actual core or Q1 counterexample. Scope/source hashes in `tripartite_deficit_review_manifest.json`.

- `TRIPARTITE_DEFICIT_INCREMENT_FINITE_CHECK.md`: future-addition monotonicity candidate tested exactly on the two existing M96 histories at b24, then b12 and b48. 9108 steps, no negative increment (804 trivial zeros, 8304 positive). No all-history monotonicity claim. Reproduction `tripartite_deficit_increment_existing.py`; exact minima/scope/source hashes in `tripartite_deficit_increment_existing_exact.json`.

- `RAW_DEFICIT_MONOTONICITY_SIDON_COUNTEREXAMPLE.md`: independently certified prescribed actual Sidon M11 with fixed C1000000,m02; raw delta drops 24 to22 with J4. Full original core is empty. This rejects only raw future-addition monotonicity; the earlier bounded C1 scan remains a correct finite non-detection. Reproduction `deficit_monotonicity_M11_exact.py`, all actual fibers/collisions and independent PASS under `C1000000_m02_M11_deficit_target/`.

- `A16_A19_FINAL_CONSISTENCY_REVIEW.md`: final saved A16-A19 mathematical/scope review PASS, including exact gate-adjusted increment, pre-saturation monotonicity and M11 D_eff24->30. Saturated J_core inequality remains unproved. Final whole-file/section hashes and pinned18-supporting-declaration Lean readback (9 file hashes, no rebuild) in `A16_A19_review_source_manifest.json`.

- `SATURATED_JCORE_EXISTING_M96_REVIEW.md`: A20 bounded strict-core saturated-stage test on existing M96 record banks only. 164670 nontrivial cells, no counterexample; exact maxima 3/8 (greedy) and1/3 (variant). No raw-fiber scan or new history. Missing analytical factor2/gate-compensation obligation remains explicit. Exact rows/ratios/hashes in `saturated_Jcore_existing_M96_exact.json`; claim/source binding in corresponding `_manifest.json`.

- `COLORED_STAR_STRICT_CORE_MONOTONICITY_COUNTEREXAMPLE.md`: one successful t64/M156 actual fixed C10^14,m02 history, J_core71>64 and D_eff11264->11250; all71 target gaps large. Full unchanged evaluator+independent checker PASS, 2435 core records/alllarge, N~1.033069026e-5. Exact graph/sequence, profile/records/caps/I/coverage and PASS under `C100000000000000_m02_colored_star/`. No t96 or later trial.
- `A20_A23_FINAL_REVIEW.md`: independent final review of historical scan, monotone scalar no-go, explicit fixed-cap short-left support, and new actual strict-core counterexample. Final whole/section hashes, preserved A16-A19 binding and finite certification source hashes in `A20_A23_final_review_manifest.json`. No running process remains.

- `CUT_SHIFT_B24_COMPONENT48_REVIEW.md`: A24 fixed k48,T96 cut24->25, l6/12/18 on both existing C1 M96 histories. Exact zero-one bank/collision and strict-core weighted boundary identities PASS. Retirement>=birth false for counts/weights; variant large-gap l6 has3 births vs5 retirements yet BH rises424373. Full exact banks/rows/deficits in `cut_shift_b24_component48_exact.json`, smaller witnesses in `cut_shift_b24_compact_counterexamples.json`, source scope in `cut_shift_b24_review_manifest.json`. No new histories or broader scan.

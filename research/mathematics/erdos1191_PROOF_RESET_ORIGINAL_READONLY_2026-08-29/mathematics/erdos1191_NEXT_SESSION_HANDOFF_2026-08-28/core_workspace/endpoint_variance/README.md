# Endpoint-variance continuation

This directory contains the proof notes, exact implementations, unit tests,
deterministic certificates, and test-first logs for the endpoint-imbalance and
Wave 1--13 gap-measure/Abel-repayment/cut-renewal continuations developed on
2026-08-28--29.

Run from this directory:

```bash
python -m venv /tmp/erdos1191-pytest-venv
/tmp/erdos1191-pytest-venv/bin/python -m pip install -r requirements-test.txt
/tmp/erdos1191-pytest-venv/bin/python -m pytest -q -p no:cacheprovider
```

The three original deterministic certificates can then be rerun with either
the same interpreter or the project interpreter:

```bash
python certificate.py
python diameter_certificate.py
python required_levels_certificate.py
```

Expected verified baseline:

- 15 unit tests;
- 10,890 endpoint-imbalance checks;
- 15,345 complete-prefix diameter-regime checks;
- 16,380 mandatory-level checks;
- 42,615 exact machine checks in total.

The JSON certificates use exact rational arithmetic for the homometric separation and zero mode. The `TDD_*_RED.log` / `TDD_*_GREEN.log` files preserve the test-first record.

The original endpoint `SHA256SUMS` was moved to `../../integrity/` because it contained a self-referential checksum line. Use the package-level verifier instead:

```bash
python ../../integrity/verify_package.py
```

For the complete current suite, including byte-for-byte regeneration of all
dated certificates, run from the package root:

```bash
ERDOS1191_PYTHON=/tmp/erdos1191-pytest-venv/bin/python ./integrity/run_all_checks.sh
```

These finite checks do not solve Erdős #1191 and do not establish publication novelty. Independently audit the written proof and literature before external use.

## 2026-08-28 Target A extension

`MULTISCALE_ARC_KERNEL_AND_OBSTRUCTIONS_2026-08-28.md` proves the exact
cyclic-arc covariance kernel, its cycle-resistance representation, and the
ordered pair--pair expansion of endpoint variance.  The corresponding exact
implementation and exhaustive small-modulus tests are:

```bash
python -m pytest -q test_multiscale_variance.py
```

The note also records the critical dyadic lower accumulation and the specific
signed upper-budget lemma that remains open, together with zero-mode,
sign-flip, dominant-gap, and sparse-construction obstructions.  None of these
artifacts is a proof of that missing upper budget.

## 2026-08-28 Target D extension

The dated Golomb-ruler optimization extension is documented in
`TARGET_D_GOLOMB_VARIANCE_2026-08-28.md`.  Its verifier and deterministic
certificate are:

```bash
python -m unittest -v test_golomb_variance.py
python golomb_variance_certificate_2026_08_28.py
```

It exhausts normalized rulers for `2 <= m <= 7`, `m-1 <= D <= 25` at
`N=D+1,D+2,D+3`, retains exact `Fraction` minima and reflection classes, and
checks a smaller range with an independent gap-composition/direct-block
oracle.  This is finite structure-discovery evidence, not an asymptotic
resolution.

## 2026-08-28 Wave 3: positive gap kernel, cover identity, shell falsification

The proof notes are:

- `SIDON_BLOCK_VARIANCE_AND_POSITIVE_MULTISCALE_2026-08-28.md`;
- `GAP_MEASURE_DYNAMICS_AND_TWO_STEP_LOWER_BOUND_2026-08-28.md`;
- `ADJOINT_LYAPUNOV_INNOVATION_BUDGET_AND_PSD_NO_GO_2026-08-28.md`;
- `FIXED_DEPTH_ERDOS_TURAN_NO_GO_AND_INTERVAL_PACKING_2026-08-28.md`;
- `Q_COVER_MARTINGALE_AND_BIRTH_OBSTRUCTION_2026-08-28.md`;
- `ORTHOGONAL_EDGE_COORDINATE_NO_GO_2026-08-28.md`;
- `FIXED_MODULUS_PREFIX_MONOTONICITY_COUNTEREXAMPLE_2026-08-28.md`;
- `critical_shell_results_2026-08-28.md`.

Run their exact tests and deterministic certificates with:

```bash
python -m unittest -v test_sidon_block_variance.py test_gap_measure_dynamics.py
python -m unittest -v test_innovation_budget.py test_fixed_depth_no_go.py
python -m unittest -v test_cover_martingale.py
python -m unittest -v test_prefix_monotonicity.py
python -m unittest -v critical_shell_test.py
python sidon_block_variance_certificate_2026_08_28.py
python prefix_monotonicity_certificate_2026_08_28.py
python critical_shell_certificate_2026_08_28.py
python innovation_budget_certificate_2026_08_28.py
python fixed_depth_no_go_certificate_2026_08_28.py
```

The positive-gap v2 certificate performs 3,200 arbitrary-set identity checks,
9,013 exhaustive Golomb identity checks, 5,000 random 16-mark theorem checks,
four structured lift checks, an exact dyadic birth-expansion comparison, and
11,213 exact gap-measure-dynamics checks.  The latter comprise 6,206 matrix
updates and 5,007 two-step witnesses, including six structured 16/32/64-mark
base/lift cases and one deliberately non-Golomb full extension whose first
quarter is Golomb.  This audits the theorem's precise weaker hypothesis.
The innovation certificate checks 512 positive-definite abstract innovations
and 128 exact adjoint horizons.  The fixed-depth certificate audits seven
Erdős--Turán scales through 1,024 marks.  Their explicit scope warnings are
part of the JSON payloads: neither the abstract orbit nor the finite-window
family is an infinite globally critical Sidon counterexample.
The critical-shell certificate refutes candidates H1--H5 and reports H6 only
as a finite surviving pattern.  None of these computations is an asymptotic
inference or a solution of #1191.

## 2026-08-28 Wave 4: growing depth, profile resets, and nested witnesses

The current Wave 4 proof notes are:

- `GROWING_DEPTH_ERDOS_TURAN_NO_GO_2026-08-28.md`;
- `CROSS_BLOCK_DIAMETER_PROFILE_PACKING_2026-08-28.md`;
- `wave4_nested_results_2026-08-28.md`.

Their tests and deterministic certificates are:

```bash
python -m pytest -q -p no:cacheprovider \
  test_growing_depth_no_go.py test_cross_block_profile.py wave4_nested_test.py
python growing_depth_no_go_certificate_2026_08_28.py
python cross_block_profile_certificate_2026_08_28.py
python wave4_nested_certificate.py \
  --sizes 4,8,16,32 --constant 1 --beam-width 256 \
  --candidates-per-state 48 --retain 2 --seeds 1191,9119 \
  --output wave4_nested_certificate_2026-08-28.json
```

The growing-depth theorem is a finite family whose visible window grows like
`log log M`; it is not one infinite globally critical Sidon sequence.  The
cross-block theorem gives a real same-history diameter-profile reset, but no
innovation upper budget.  The 32-mark nested rulers are finite beam witnesses;
only their four-mark root optimization is complete.  These scope warnings are
part of the dated artifacts and must be preserved.

## 2026-08-28 Wave 5: cross-epoch persistence and 64-mark witnesses

The current Wave 5 notes are:

- `CROSS_EPOCH_RESET_AMORTIZATION_2026-08-28.md`;
- `wave5_nested_results_2026-08-28.md`.

Run the focused exact tests and regenerate the nested certificate with:

```bash
python -m pytest -q -p no:cacheprovider \
  test_wave5_cross_epoch.py wave5_nested_test.py
python wave5_nested_certificate.py \
  --wave4-certificate wave4_nested_certificate_2026-08-28.json \
  --beam-width 128 --candidates-per-state 32 --retain 3 \
  --seeds 501191,502191 \
  --output wave5_nested_certificate_2026-08-28.json
```

Historically, the Wave 5 cross-epoch note proves exact chord inheritance, a signed global reset,
an `O(log log m)` endpoint-flat-run bound, and a conditional variation
amortization.  Its infinite sawtooth counterprofile has uniformly positive
innovation but is explicitly non-Sidon, so it rules out only profile/PSD-only
arguments.  The nested certificate contains finite 64-mark beam witnesses;
it does not prove optimality, 128-mark extension, or an asymptotic result.

## 2026-08-28 Wave 6: arithmetic bands, Hall falsification, and 128 marks

The authoritative mathematical summary is
`../CONTINUATION_2026-08-28_WAVE6_ARITHMETIC_BAND_RENEWAL.md`.  The main
supporting notes are:

- `wave6_collision_reset_renewal_2026-08-28.md`;
- `wave6_arithmetic_mining_results_2026-08-28.md`;
- `FORBIDDEN_SHADOW_RESIDUE_NO_GO_2026-08-28.md`;
- `wave6_hall_candidate_probe_results_2026-08-28.md`.

Run the focused exact suite with:

```bash
python -m pytest -q -p no:cacheprovider \
  wave6_arithmetic_mining_test.py \
  test_wave6_collision_bands.py \
  test_wave6_forbidden_shadow.py \
  test_wave6_hall_candidate_probe.py
```

Regenerate the two serialized Wave 6 certificates with:

```bash
python wave6_arithmetic_mining_certificate.py \
  --wave5-certificate wave5_nested_certificate_2026-08-28.json \
  --beam-width 32 --candidates-per-state 16 --seed 601191 --retain 1 \
  --output wave6_arithmetic_mining_certificate_2026-08-28.json
python wave6_hall_candidate_probe_certificate.py \
  --output wave6_hall_candidate_probe_certificate_2026-08-28.json \
  --replay-search
```

The arithmetic certificate contains an exactly audited 128-mark finite
witness found by a non-exhaustive beam.  The Hall certificate contains a
different 64-mark C=1 ruler with three consecutive exact violations of the
refuted empirical decay candidate.  The collision-band theorems give an
exact `O(log)` endpoint ledger, and the residue lift refutes universal local
shadow-density charging.  None of these proves an infinite extension or
resolves Erdős #1191.

## 2026-08-28 Wave 7: complete birth spectrum and survival-conditioned debt

Read first:

- `WAVE7_GLOBAL_BAND_RENEWAL_POTENTIAL_2026-08-28.md`;
- `WAVE7_ADVERSARIAL_AUDIT_2026-08-28.md`;
- `wave7_band_renewal_probe_results_2026-08-28.md`;
- `WAVE7_GLUE_DELETE_NO_GO_2026-08-28.md`.

The complete-birth note partitions every dyadically born pair, proves the
rank-lag wedge ledger, and obtains the all-history bound
`sum_F q_F ell_F/gamma_F^2<=8 sqrt(2)`. Exact and growing E–T witnesses show
that this potential alone cannot affinely dominate recent adjoint innovation.
The hostile audit introduces the critical survival-height label and proves
its equivalence to one infinite extension by König's lemma.

The renewal probe refutes RH and HT, proves EST universally through eight
marks, and records finite survival on the authenticated larger sample. Its
128-mark debt row shows that adjacent cheap halves leave 63 units unpaid.
The gluing note proves that O'Bryant Lemma 9's scalar worst guarantee cannot
be black-box iterated under an all-prefix critical envelope; structured
low-conflict gluing is not ruled out.

Focused exact checks:

```bash
python -m pytest -q -p no:cacheprovider \
  test_complete_birth_ledger.py \
  test_wave7_band_renewal_probe.py \
  wave7_glue_delete_no_go_test.py
python -m ruff check \
  complete_birth_ledger.py test_complete_birth_ledger.py \
  wave7_band_renewal_probe.py wave7_band_renewal_certificate.py \
  test_wave7_band_renewal_probe.py \
  wave7_glue_delete_no_go_test.py
python wave7_band_renewal_certificate.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output /tmp/wave7-band-renewal.json
cmp wave7_band_renewal_certificate_2026-08-28.json \
  /tmp/wave7-band-renewal.json
```

The exact next theorem is an infinite-survival-conditioned repayment of
old-half overlap debt by unused non-adjacent differences or equivalent
capacity, quantitatively linked to the actual `Q_m` innovations. Nothing in
Wave 7 proves an infinite critical sequence, an asymptotic contradiction, or
a prize-ready resolution. Status: `UNRESOLVED_AT_HARD_LIMIT`.

## 2026-08-28 Wave 8: actual atoms and the positive birth budget

Read first:

- `../CONTINUATION_2026-08-28_WAVE8_POSITIVE_BIRTH_BUDGET.md`;
- `WAVE8_PAIR_TELESCOPE_2026-08-28.md`;
- `WAVE8_Q_ATOM_DECOMPOSITION_2026-08-28.md`;
- `WAVE8_ACTUAL_ADJACENT_RENEWAL_2026-08-28.md`;
- `WAVE8_ADVERSARIAL_AUDIT_2026-08-28.md`;
- `WAVE8_SURVIVAL_DEBT_PROBE_RESULTS_2026-08-28.md`;
- `WAVE8_DENSITY_CANDIDATE_2026-08-28.md`;
- `WAVE8_HEGYVARI_BRIDGE_2026-08-28.md`.

Wave 8 proves actual adjacent renewal, the exact common-grid pair/Abel/square
decompositions of `Q_m`, the complete shell boundary-fan sign theorem, and
summability of the adjacent endpoint debt.  The pair telescope proves

```text
B_H(J)/2 <= sum_(j<=J)<H,Q_j/N_(2m_j)> <= B_H(J).
```

Thus negative old-pair terms cannot create an unbounded saving.  The exact
next theorem is the positive arithmetic budget `B_H(J)=o(log J)` on one fixed
infinite eventually critical Golomb branch.

Focused exact checks:

```bash
uv run --no-project --with pytest python -m pytest -q -p no:cacheprovider \
  test_wave8_actual_adjacent_renewal.py \
  test_wave8_q_atom_verifier.py \
  test_wave8_actual_atom_certificate.py \
  test_wave8_survival_debt_probe.py \
  test_wave8_density_candidate_search.py \
  test_wave8_hegyvari_bridge.py \
  test_wave8_pair_telescope.py
```

Regenerate the three serialized Wave 8 certificates with:

```bash
python wave8_actual_atom_certificate.py --output /tmp/wave8-actual.json
python wave8_survival_debt_probe.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output /tmp/wave8-survival.json
python wave8_hegyvari_bridge.py --output /tmp/wave8-hegyvari.json
cmp wave8_actual_atom_certificate_2026-08-28.json /tmp/wave8-actual.json
cmp wave8_survival_debt_certificate_2026-08-28.json /tmp/wave8-survival.json
cmp wave8_hegyvari_bridge_certificate_2026-08-28.json /tmp/wave8-hegyvari.json
```

The local global-density, latest-shell, raw-count repayment, adjacent-only
fan repayment, rank-one-to-shell, and cancellation shortcuts have exact
counterexamples or no-go theorems.  The 682-mark density fixture and every
finite extension count remain finite evidence only.  The Hegyvári finite
blocks do not give a compatible critical tower.  Status remains
`UNRESOLVED_AT_HARD_LIMIT`.

## 2026-08-29 Wave 9: scalar rank variance and survival-conditioned core

Read first:

- `../CONTINUATION_2026-08-29_WAVE9_RANK_VARIANCE_REDUCTION.md`;
- `WAVE9_BIRTH_BUDGET_CARLESON_ANALYSIS_2026-08-29.md`;
- `WAVE9_BIRTH_BUDGET_PROBE_2026-08-29.md`;
- `WAVE9_WEIGHTED_CROSS_RATIO_2026-08-29.md`.

Wave 9 proves the exact global comparison

```text
(4/49) sum_(k=1)^(J+1) Var_(nu_(2^k))(u)
  <= B_H(J)
  <= (36/35) sum_(k=1)^(J+1) Var_(nu_(2^k))(u).
```

It also proves `Var_(nu_n)(u)>=n^2/(512N_n)` from distinct genuine adjacent
gaps.  Thus the desired upper is now a scalar survival-conditioned theorem
which must contradict an explicit harmonic lower barrier by using
non-adjacent contiguous-sum uniqueness.

The Carleson note removes short-rank and small-endpoint atoms at cumulative
cost `O(log log J)`, proves an exact four-parameter tile bound, and uses a
scaled Erdős--Turán family to refute local numerical sparsity.  The exact
probe exhausts 1,672 four-mark and 1,146 bounded eight-mark `C=1` rulers,
refuting pointwise and harmonic decay plus static rank/magnitude cell
injections.  The weighted cross-ratio note supplies a genuine product
majorant, exact Abel coefficients, a primitive factorial bound, and an exact
dyadic state recursion; the recursion still reconstructs a positive state
sum rather than a terminal telescope.

Focused checks:

```bash
python -m pytest -q -p no:cacheprovider \
  test_wave9_rank_variance_reduction.py \
  test_wave9_birth_budget_probe.py \
  test_wave9_cross_ratio_telescope.py
python wave9_birth_budget_probe.py --output /tmp/wave9-birth.json
cmp wave9_birth_budget_certificate_2026-08-29.json /tmp/wave9-birth.json
```

The next theorem is survival-conditioned non-saturation of the exact
long-rank/two-large-endpoint core on one fixed infinite branch.  A laminar
weighted incomplete-DTS LP may use the hereditary Wave 9 rank-lag inequality,
the tile bounds, and the primitive cross-ratio coefficients, but its dual must
be uniform under `surv_C=infinity`.  P15 and #1191 remain open.

## 2026-08-29 Wave 10: global Abel spectrum and frontier localization

Read first:

- `../CONTINUATION_2026-08-29_WAVE10_LAMINAR_LOG_PRODUCT_NO_GO.md`;
- `WAVE10_LAMINAR_WEIGHTED_TRIANGLE_ANALYSIS_2026-08-29.md`;
- `WAVE10_HEREDITARY_LOG_PRODUCT_PACKING_2026-08-29.md`;
- `WAVE10_LAMINAR_LP_PROBE_2026-08-29.md`.

Wave 10 proves the arbitrary-weight hereditary incomplete-DTS inequality,
its factorial/log-product form, and the cut-kernel estimate

```text
sum_(i<j, i<=t<=j) h_i h_j/D_(i,j) <= (log 2+1/e)a_g.
```

Thus every fixed old gap position has an exponentially summable dyadic future
load.  Persistent mass can only migrate to the advancing frontier.

The exact dyadic Abel negative bulk has globally disjoint right-endpoint bands.
After simultaneous sorting over any finite dyadic epoch set,

```text
F_E=(7/4) sum_(m in E) log m+O(|E|).
```

This uses all exposed global integer distinctness but still leaves a leading
quarter deficit and secondary boundary slack.  The missing quarter is localized
to the lower-shell fan ending at `m-1`.

The exact LP probe adds a separate no-go: once the prefix moduli are fixed,
existing W9-RLP rows have zero coefficients on every tile occupancy variable.
The all-subset DP checked 9,845,549 selections through 128 marks, with zero
violations; every tested tile block has exact primal=dual.  This finite result
does not infer infinite survival.

Focused checks from this directory:

```bash
uv run --no-project --with pytest python -m pytest -q -p no:cacheprovider \
  test_wave10_laminar_triangle_check.py \
  test_wave10_log_product_packing.py \
  test_wave10_laminar_lp_probe.py
uvx --from ruff ruff check \
  wave10_laminar_triangle_check.py test_wave10_laminar_triangle_check.py \
  wave10_log_product_packing.py test_wave10_log_product_packing.py \
  wave10_laminar_lp_probe.py test_wave10_laminar_lp_probe.py
```

Regenerate the finite LP certificate with:

```bash
python wave10_laminar_lp_probe.py --output /tmp/wave10-laminar-lp.json
cmp wave10_laminar_lp_certificate_2026-08-29.json \
  /tmp/wave10-laminar-lp.json
```

The exact obligation remains P15.  One sufficient target combines actual bulk
premium and exact positive-boundary slack to leave `o(log J)` in the Abel
repayment; a lower-shell-only version additionally needs a global floor-
allocation lemma.  A separate sufficient target is a full bi-/tri-tree tensor
encoding with summably vanishing box constants.  The targets are not proved
equivalent or necessary.  P15 and #1191 remain open.

## Wave 11 triangular Abel repayment

The Wave 11 continuation is documented in:

- `WAVE11_SURVIVAL_ABEL_REPAYMENT_ANALYSIS_2026-08-29.md`;
- `WAVE11_ABEL_REPAYMENT_PROBE_2026-08-29.md`;
- `wave11_abel_repayment_probe.py`;
- `test_wave11_abel_repayment_probe.py`;
- `wave11_abel_repayment_certificate_2026-08-29.json`.

The universal theorem is

```text
D_(p,q) >= binom(q-p+2,2),
K_m^len = 2 log m + O(1),
T_m-K_m^len = Y_m+G_m^len+S_m,
Y_m,G_m^len,S_m >= 0.
```

Thus the complete leading quarter missed by the Wave 10 `7/4` floor is
repaid.  On an eventual-`C` branch the direct envelope improves to
`O_C(J log J)`, but the required scale is `o(log J)`.  The exact lower
residual is a future cross-ratio tail; same-pair dyadic overlap grows as
`Theta(log(j/i))`, so uniform birth-atom charging is unavailable.

Run the focused tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 uv run --no-project --with pytest \
  python -m pytest -q test_wave11_abel_repayment_probe.py
```

Regenerate the certificate with:

```bash
python wave11_abel_repayment_probe.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output /tmp/wave11-abel-repayment.json
cmp wave11_abel_repayment_certificate_2026-08-29.json \
  /tmp/wave11-abel-repayment.json
```

The remaining P17 target is, on one fixed infinite eventually-critical branch,

```text
G_J^len+S_J >= T_J-K_J^len-epsilon_J,
epsilon_J=o(log J).
```

Equivalently `sum Y_m=o(log J)`.  Finite fixtures and changing Erdős--Turán
windows are falsification tools only.  P15, P17, and #1191 remain open.

## Wave 12 cut renewal and the integer-lattice boundary

Read first:

- `../CONTINUATION_2026-08-29_WAVE12_CUT_RENEWAL_INTEGER_PACKING.md`;
- `WAVE12_SIGNED_OFFDIAGONAL_SURVIVAL_ANALYSIS_2026-08-29.md`;
- `WAVE12_CUT_RENEWAL_PROBE_2026-08-29.md`;
- `../research_sources/WAVE12_SIGNED_OFFDIAGONAL_LITERATURE_DELTA_2026-08-29.md`.

For the Wave 11 future tail `R_m`, Wave 12 proves coefficientwise

```text
Y_m = R_m-R_(2m)+Z_m,
Z_m = Z_m^ob+Z_m^nb+Z_m^of+Z_m^mf >= 0.
```

The four sectors are explicit.  Their dyadic coefficients are uniformly
summable for each fixed pair, so the raw-tail `Theta(log(j/i))` same-pair
overlap is removed.  The new sufficient target is
`sum_(m in E_J) Z_m=o(log J)` on one fixed infinite eventually-critical
integer Golomb branch.  Different-pair arithmetic packing remains open.

Wave 12 also proves that the best floor using numerical ranks, triangular
length floors, and the complete interval-containment poset improves the
Wave 11 length floor by less than `5` per epoch.  Finally,
`a_n=n^2+sqrt(2)n` is a real Golomb ruler with quadratic growth but
`Y_m -> (3/2)(log 2-1/2)>0`; this is not an integer counterexample, but it
proves that the missing argument must expose integer unit spacing rather than
only abstract difference uniqueness.

Run the focused exact suite and reproduce the deterministic certificate with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_wave12_cut_renewal_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 wave12_cut_renewal_probe.py \
  --output /tmp/wave12-cut-renewal.json
cmp wave12_cut_renewal_certificate_2026-08-29.json \
  /tmp/wave12-cut-renewal.json
```

The focused suite has seven tests.  The certificate audits all 1,146 bounded
eight-mark all-prefix-`C=1` rulers, the authenticated 64-mark fixture, an
independent 128-mark ruler, and 32,130 containment atoms through epoch 128.
These are finite algebra and falsification checks only.  P15, P17, the new
integer renewal packing lemma, and Erdős #1191 remain open.

## Wave 13 harmonic obstruction and finite log-D frontier

Read first:

- `WAVE13_P18_HARMONIC_OBSTRUCTION_2026-08-29.md`;
- `WAVE13_FRONTIER_SPECTRUM_AND_SIGNED_REPAYMENT_2026-08-29.md`;
- `WAVE13_LATTICE_CELL_AND_CENTRAL_RANK_NO_GO_2026-08-29.md`.

For

```text
H_m=a_(2m-1)-a_(m-2),
E_m=m(m-2)(m^2+8m+6)/48,
```

Wave 13 proves the exact integer new-birth floor

```text
Z_m^nb >= E_m/(8m^2 H_m) >= m^2/(384H_m).
```

Under the hypothetical eventual-`C` cap this forces a positive harmonic
`Omega_C(log J)` lower bound for both `sum Y_m` and `sum Z_m`.  Consequently
the Wave 12 P18 sublogarithmic estimate cannot be treated as a small packing
property of an existing critical branch.  It is an explicit contradiction
target.  The terminal `R` tail remains indispensable in the signed-renewal
route.

The independent frontier probe expands the full infinite-tail `Z_m` into a
finite rational spectrum of `log D_(p,q)`.  For `m=4,8,16,32,64`, the closed
formula agrees coefficientwise with a separate sector expansion, has zero
total coefficient, and agrees as an exact formal-log expression with the
direct future-tail telescope.  It also independently cross-checks the
layered floor on all 1,468 bounded eight-mark rulers, including the 1,146
all-prefix-`C=1` subset, plus the authenticated Hall 64 and Erdős--Turán 128
fixtures.

Run both focused suites and replay both deterministic certificates with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_wave13_p18_harmonic_obstruction_probe.py \
  test_wave13_new_birth_barrier_probe.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  wave13_p18_harmonic_obstruction_probe.py \
  --output /tmp/wave13-p18-harmonic-obstruction.json
cmp wave13_p18_harmonic_obstruction_certificate_2026-08-29.json \
  /tmp/wave13-p18-harmonic-obstruction.json
PYTHONDONTWRITEBYTECODE=1 python3 wave13_new_birth_barrier_probe.py \
  --source-certificate wave12_cut_renewal_certificate_2026-08-29.json \
  --output /tmp/wave13-frontier-spectrum.json
cmp wave13_new_birth_barrier_certificate_2026-08-29.json \
  /tmp/wave13-frontier-spectrum.json
```

The harmonic certificate and frontier certificate remain finite executable
audits.  They do not construct an infinite eventual-`C` branch, prove the
missing signed upper repayment, resolve either question of Erdős #1191, or
support a prize claim.

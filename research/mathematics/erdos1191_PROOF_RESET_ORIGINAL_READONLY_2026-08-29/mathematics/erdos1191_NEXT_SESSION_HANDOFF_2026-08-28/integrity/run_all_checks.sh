#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
erdos1191_python="${ERDOS1191_PYTHON:-python}"
export PYTHONDONTWRITEBYTECODE=1

"$erdos1191_python" "$ROOT/integrity/verify_package.py"
cd "$ROOT/core_workspace/endpoint_variance"
"$erdos1191_python" -m pytest -q -p no:cacheprovider
"$erdos1191_python" certificate.py
"$erdos1191_python" diameter_certificate.py
"$erdos1191_python" required_levels_certificate.py

erdos1191_golomb_tmp="$(mktemp)"
erdos1191_multiscale_tmp="$(mktemp)"
erdos1191_sidon_block_tmp="$(mktemp)"
erdos1191_prefix_tmp="$(mktemp)"
erdos1191_critical_shell_tmp="$(mktemp)"
erdos1191_innovation_tmp="$(mktemp)"
erdos1191_fixed_depth_tmp="$(mktemp)"
erdos1191_growing_depth_tmp="$(mktemp)"
erdos1191_cross_block_tmp="$(mktemp)"
erdos1191_nested_tmp="$(mktemp)"
erdos1191_wave5_nested_tmp="$(mktemp)"
erdos1191_wave6_arithmetic_tmp="$(mktemp)"
erdos1191_wave6_hall_tmp="$(mktemp)"
erdos1191_wave7_band_tmp="$(mktemp)"
erdos1191_wave8_actual_tmp="$(mktemp)"
erdos1191_wave8_survival_tmp="$(mktemp)"
erdos1191_wave8_hegyvari_tmp="$(mktemp)"
erdos1191_wave9_birth_tmp="$(mktemp)"
erdos1191_wave10_laminar_tmp="$(mktemp)"
erdos1191_wave11_abel_tmp="$(mktemp)"
erdos1191_wave12_cut_tmp="$(mktemp)"
erdos1191_wave13_harmonic_tmp="$(mktemp)"
erdos1191_wave13_frontier_tmp="$(mktemp)"
trap 'rm -f "$erdos1191_golomb_tmp" "$erdos1191_multiscale_tmp" "$erdos1191_sidon_block_tmp" "$erdos1191_prefix_tmp" "$erdos1191_critical_shell_tmp" "$erdos1191_innovation_tmp" "$erdos1191_fixed_depth_tmp" "$erdos1191_growing_depth_tmp" "$erdos1191_cross_block_tmp" "$erdos1191_nested_tmp" "$erdos1191_wave5_nested_tmp" "$erdos1191_wave6_arithmetic_tmp" "$erdos1191_wave6_hall_tmp" "$erdos1191_wave7_band_tmp" "$erdos1191_wave8_actual_tmp" "$erdos1191_wave8_survival_tmp" "$erdos1191_wave8_hegyvari_tmp" "$erdos1191_wave9_birth_tmp" "$erdos1191_wave10_laminar_tmp" "$erdos1191_wave11_abel_tmp" "$erdos1191_wave12_cut_tmp" "$erdos1191_wave13_harmonic_tmp" "$erdos1191_wave13_frontier_tmp"' EXIT

"$erdos1191_python" golomb_variance_certificate_2026_08_28.py --output "$erdos1191_golomb_tmp"
cmp -s golomb_variance_certificate_2026-08-28.json "$erdos1191_golomb_tmp"
"$erdos1191_python" multiscale_variance_certificate_2026_08_28.py --output "$erdos1191_multiscale_tmp"
cmp -s multiscale_variance_certificate_2026-08-28.json "$erdos1191_multiscale_tmp"
"$erdos1191_python" sidon_block_variance_certificate_2026_08_28.py --output "$erdos1191_sidon_block_tmp"
cmp -s sidon_block_variance_certificate_2026-08-28.json "$erdos1191_sidon_block_tmp"
"$erdos1191_python" prefix_monotonicity_certificate_2026_08_28.py --output "$erdos1191_prefix_tmp"
cmp -s prefix_monotonicity_certificate_2026-08-28.json "$erdos1191_prefix_tmp"
"$erdos1191_python" critical_shell_certificate_2026_08_28.py --output "$erdos1191_critical_shell_tmp"
cmp -s critical_shell_certificate_2026-08-28.json "$erdos1191_critical_shell_tmp"
"$erdos1191_python" innovation_budget_certificate_2026_08_28.py --output "$erdos1191_innovation_tmp"
cmp -s innovation_budget_certificate_2026-08-28.json "$erdos1191_innovation_tmp"
"$erdos1191_python" fixed_depth_no_go_certificate_2026_08_28.py --output "$erdos1191_fixed_depth_tmp"
cmp -s fixed_depth_no_go_certificate_2026-08-28.json "$erdos1191_fixed_depth_tmp"
"$erdos1191_python" growing_depth_no_go_certificate_2026_08_28.py --output "$erdos1191_growing_depth_tmp"
cmp -s growing_depth_no_go_certificate_2026-08-28.json "$erdos1191_growing_depth_tmp"
"$erdos1191_python" cross_block_profile_certificate_2026_08_28.py --output "$erdos1191_cross_block_tmp"
cmp -s cross_block_profile_certificate_2026-08-28.json "$erdos1191_cross_block_tmp"
"$erdos1191_python" wave4_nested_certificate.py \
  --sizes 4,8,16,32 \
  --constant 1 \
  --beam-width 256 \
  --candidates-per-state 48 \
  --retain 2 \
  --seeds 1191,9119 \
  --output "$erdos1191_nested_tmp"
cmp -s wave4_nested_certificate_2026-08-28.json "$erdos1191_nested_tmp"
"$erdos1191_python" wave5_nested_certificate.py \
  --wave4-certificate wave4_nested_certificate_2026-08-28.json \
  --beam-width 128 \
  --candidates-per-state 32 \
  --retain 3 \
  --seeds 501191,502191 \
  --output "$erdos1191_wave5_nested_tmp"
cmp -s wave5_nested_certificate_2026-08-28.json "$erdos1191_wave5_nested_tmp"
"$erdos1191_python" wave6_arithmetic_mining_certificate.py \
  --wave5-certificate wave5_nested_certificate_2026-08-28.json \
  --beam-width 32 \
  --candidates-per-state 16 \
  --seed 601191 \
  --retain 1 \
  --output "$erdos1191_wave6_arithmetic_tmp"
cmp -s wave6_arithmetic_mining_certificate_2026-08-28.json "$erdos1191_wave6_arithmetic_tmp"
"$erdos1191_python" wave6_hall_candidate_probe_certificate.py \
  --output "$erdos1191_wave6_hall_tmp" \
  --replay-search
cmp -s wave6_hall_candidate_probe_certificate_2026-08-28.json "$erdos1191_wave6_hall_tmp"
"$erdos1191_python" wave7_band_renewal_certificate.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output "$erdos1191_wave7_band_tmp"
cmp -s wave7_band_renewal_certificate_2026-08-28.json "$erdos1191_wave7_band_tmp"
"$erdos1191_python" wave8_actual_atom_certificate.py \
  --output "$erdos1191_wave8_actual_tmp"
cmp -s wave8_actual_atom_certificate_2026-08-28.json "$erdos1191_wave8_actual_tmp"
"$erdos1191_python" wave8_survival_debt_probe.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output "$erdos1191_wave8_survival_tmp"
cmp -s wave8_survival_debt_certificate_2026-08-28.json "$erdos1191_wave8_survival_tmp"
"$erdos1191_python" wave8_hegyvari_bridge.py \
  --output "$erdos1191_wave8_hegyvari_tmp"
cmp -s wave8_hegyvari_bridge_certificate_2026-08-28.json "$erdos1191_wave8_hegyvari_tmp"
"$erdos1191_python" wave9_birth_budget_probe.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output "$erdos1191_wave9_birth_tmp"
cmp -s wave9_birth_budget_certificate_2026-08-29.json "$erdos1191_wave9_birth_tmp"
"$erdos1191_python" wave10_laminar_lp_probe.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output "$erdos1191_wave10_laminar_tmp"
cmp -s wave10_laminar_lp_certificate_2026-08-29.json "$erdos1191_wave10_laminar_tmp"
"$erdos1191_python" wave11_abel_repayment_probe.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output "$erdos1191_wave11_abel_tmp"
cmp -s wave11_abel_repayment_certificate_2026-08-29.json \
  "$erdos1191_wave11_abel_tmp"
"$erdos1191_python" wave12_cut_renewal_probe.py \
  --source-certificate wave11_abel_repayment_certificate_2026-08-29.json \
  --output "$erdos1191_wave12_cut_tmp"
cmp -s wave12_cut_renewal_certificate_2026-08-29.json \
  "$erdos1191_wave12_cut_tmp"
"$erdos1191_python" wave13_p18_harmonic_obstruction_probe.py \
  --output "$erdos1191_wave13_harmonic_tmp"
cmp -s wave13_p18_harmonic_obstruction_certificate_2026-08-29.json \
  "$erdos1191_wave13_harmonic_tmp"
"$erdos1191_python" wave13_new_birth_barrier_probe.py \
  --source-certificate wave12_cut_renewal_certificate_2026-08-29.json \
  --output "$erdos1191_wave13_frontier_tmp"
cmp -s wave13_new_birth_barrier_certificate_2026-08-29.json \
  "$erdos1191_wave13_frontier_tmp"

# The three legacy generators write their packaged JSON in place.  Recheck the
# release manifest after every generator so any nondeterministic or stale
# output is detected before this runner can report success.
"$erdos1191_python" "$ROOT/integrity/verify_package.py"

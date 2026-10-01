from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from decimal import Decimal
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

import wave19_certified_remainder_certificate as certificate


class Wave19CertifiedRemainderCertificateTests(unittest.TestCase):
    def test_gothic_coefficients_and_closed_masses_are_exact(self) -> None:
        self.assertEqual(certificate.beta_coefficient(4, 4, 4), Fraction(1, 16))
        self.assertEqual(certificate.beta_coefficient(4, 3, 4), Fraction(1, 64))
        self.assertEqual(certificate.beta_coefficient(4, 2, 4), Fraction(1, 32))
        expected = {
            4: ("27/64", "99/256", "21/128"),
            5: ("12/25", "179/400", "1/5"),
            8: ("147/256", "563/1024", "133/512"),
        }
        for epoch in range(4, 65):
            with self.subTest(epoch=epoch):
                row = certificate.coefficient_mass_audit(epoch)
                self.assertTrue(row["all_exact_checks_pass"])
                self.assertEqual(
                    row["Ucoef_minus_Bcoef_minus_ecoef_plus_epscoef"], "0/1"
                )
                if epoch in expected:
                    self.assertEqual(
                        (row["Bcoef"], row["Ucoef"], row["Rcoef"]),
                        expected[epoch],
                    )

    def test_formal_remainder_reductions_match_all_three_forms(self) -> None:
        row = certificate.formal_remainder_algebra_audit()
        self.assertTrue(row["all_exact_checks_pass"])
        self.assertEqual(row["expanded_map"], row["Z_plus_map"])
        self.assertEqual(
            row["expanded_map"],
            {
                "Dpre": -1,
                "F": -1,
                "J": -1,
                "Srank": -1,
                "U": 1,
                "e": -1,
                "eps": 1,
            },
        )
        self.assertTrue(row["Rsharp_equals_Z_plus_three_quarters_Dpre_minus_J"])
        self.assertTrue(row["Rcert_equals_Rsharp_plus_Pair_after_B_split"])

    def test_sharp_coefficients_and_universal_pair_maximum_are_exact(self) -> None:
        for epoch in (4, 5, 8, 16, 32, 64):
            with self.subTest(epoch=epoch):
                row = certificate.sharp_remainder_coefficient_audit(epoch)
                self.assertTrue(row["cross_half_absorption_coefficientwise"])
                self.assertTrue(
                    row["endpoint_three_quarters_absorption_coefficientwise"]
                )
                self.assertTrue(row["all_exact_checks_pass"])
                pair = row["pair_maximum_audit"]
                self.assertTrue(pair["scaled_exponent_map_verified"])
                self.assertTrue(
                    pair["maximum_minus_minimum_product_is_binomial_c_choose_a_cubed"]
                )
                self.assertTrue(pair["dyadic_scalar_sum_identity_verified"])

    def test_p27_five_piece_coefficient_decomposition_is_exact(self) -> None:
        for epoch in (4, 5, 8, 16, 32, 64):
            with self.subTest(epoch=epoch):
                row = certificate.p27_coefficient_audit(epoch)
                self.assertTrue(row["S_coefficient_at_most_Zfin_coefficient"])
                self.assertTrue(row["endpoint_lambda_at_most_three_quarters_prefix"])
                self.assertTrue(row["hstar_below_five_halves_by_log_bound"])
                self.assertTrue(row["future_sector_coefficients_positive"])
                self.assertTrue(row["five_piece_algebra_reduces_to_Rsharp"])
                self.assertTrue(row["four_channel_algebra_reduces_to_Rsharp"])
                self.assertEqual(row["five_piece_reduced_map"]["Dpre"], "3/4")
                self.assertEqual(row["four_channel_reduced_map"]["Dpre"], "3/4")
                self.assertTrue(row["endpoint_slack_mass_at_least_39_over_256"])
                self.assertTrue(row["all_exact_checks_pass"])

    def test_p27_inner_birth_coefficients_and_layer_polynomial_are_exact(self) -> None:
        for epoch in (4, 8, 16, 32, 64):
            with self.subTest(epoch=epoch):
                row = certificate.inner_birth_coefficient_audit(epoch)
                self.assertTrue(row["W_coefficient_equals_Zfin_coefficient"])
                self.assertTrue(row["S_has_zero_coefficient_on_W_support"])
                self.assertTrue(row["layered_sum_matches_closed_polynomial"])
                self.assertTrue(row["coarse_difference_polynomial_identity"])
                self.assertTrue(row["fejer_constant_is_twice_required_threshold"])
                self.assertTrue(row["all_exact_checks_pass"])

    def test_atom_ledger_proves_rank_and_rearrangement_signs(self) -> None:
        points = certificate.erdos_turan_points(67)
        row = certificate.fixture_audit("erdos_turan_p67", points, 4)
        self.assertEqual(row["atom_count"], 12)
        self.assertEqual(row["minimum_xj_minus_j"], 140)
        self.assertEqual(row["weight_counts"], {"1/16": 3, "1/32": 6, "1/64": 3})
        self.assertEqual(
            row["atom_ledger_sha256"],
            "273ccef8c2a827b84d54dcce3cf73fb7115d3e4d3e6dd5bb35a6eac6e8cb5dba",
        )
        self.assertTrue(row["Srank_nonnegative_by_integer_rank"])
        self.assertTrue(row["Pair_nonnegative_by_rearrangement"])
        self.assertTrue(row["Hloc_equals_Srank_plus_Pair_formally"])
        self.assertTrue(row["Pair_maximum_formula_exact"])
        self.assertTrue(row["all_exact_checks_pass"])
        self.assertTrue(row["all_conservative_decimal_checks_pass"])

    def test_spent_row_and_qcert_pass_on_multiple_fixtures_and_epochs(self) -> None:
        fixtures = (
            ("erdos_turan_p67", certificate.erdos_turan_points(67)),
            (
                "binary_superincreasing_64",
                certificate.binary_superincreasing_points(64),
            ),
        )
        for name, points in fixtures:
            for epoch in (4, 8, 16, 32):
                with self.subTest(fixture=name, epoch=epoch):
                    row = certificate.fixture_audit(name, points, epoch)
                    self.assertTrue(row["spent_row_coefficientwise_at_most_Srank"])
                    self.assertTrue(row["jump_factorizations_exact"])
                    self.assertTrue(row["spent_interval_below_Srank_conservatively"])
                    self.assertTrue(
                        row["Theta_upper_below_spent_plus_J_conservatively"]
                    )
                    self.assertTrue(
                        row["Qcert_upper_surrogate_nonnegative_conservatively"]
                    )
                    self.assertTrue(row["Qcert_finite_nonnegative_conservatively"])

    def test_decimal_intervals_cover_identities_and_rcert_forms(self) -> None:
        row = certificate.fixture_audit(
            "erdos_turan_p67", certificate.erdos_turan_points(67), 16
        )
        self.assertTrue(row["Hloc_and_Srank_plus_Pair_intervals_overlap"])
        self.assertTrue(row["Rcert_forms_1_and_2_overlap"])
        self.assertTrue(row["Rcert_forms_2_and_3_overlap"])
        self.assertTrue(row["Rsharp_forms_overlap"])
        self.assertTrue(row["Rcert_equals_Rsharp_plus_Pair_conservatively"])
        self.assertTrue(row["J_below_half_Y_plus_three_quarters_Dpre_conservatively"])
        self.assertTrue(row["Z_below_half_Y_plus_Rsharp_conservatively"])
        self.assertTrue(row["P27_endpoint_slack_nonnegative"])
        self.assertTrue(row["P27_finite_birth_slack_nonnegative"])
        self.assertTrue(row["P27_split_slack_nonnegative"])
        self.assertTrue(row["P27_future_slack_nonnegative"])
        self.assertTrue(row["P27_cap_monotonicity_slack_nonnegative"])
        self.assertTrue(row["P27_direct_split_slack_nonnegative"])
        self.assertTrue(row["P27_direct_split_equals_two_refined_pieces"])
        self.assertTrue(row["P27_five_piece_sum_equals_Rsharp"])
        self.assertTrue(row["P27_four_channel_sum_equals_Rsharp"])
        self.assertTrue(row["row_exact_endpoint_factorizations_exact"])
        self.assertTrue(row["Eend_is_alias_of_Erow"])
        self.assertTrue(row["P27_profile_Delta_nonnegative"])
        self.assertTrue(row["P27_profile_Delta_at_most_S"])
        self.assertTrue(row["P27_Rprof_nonnegative"])
        self.assertTrue(row["P27_Rprof_equals_Z_minus_Delta"])
        self.assertTrue(row["P27_Rprof_three_channel_decomposition"])
        self.assertTrue(row["P27_Z_below_S_plus_Rprof"])
        self.assertTrue(row["P27_S_plus_Rprof_below_half_Y_plus_Rprof"])
        self.assertTrue(row["P27_Rsharp_equals_Rprof_plus_endpoint_slack"])
        self.assertTrue(row["P27_Rsharp_dominates_Rprof"])
        self.assertTrue(row["P27_Zfin_minus_S_dominates_inner_W"])
        self.assertTrue(row["P27_Rprof_dominates_inner_W"])
        inner = row["inner_birth_layer_audit"]
        self.assertTrue(inner["minimum_inner_moment_dominates_Eprime"])
        self.assertTrue(inner["weighted_moment_dominates_half_Hprime_Eprime"])
        self.assertTrue(inner["W_dominates_exact_layer_floor_conservatively"])
        self.assertTrue(inner["W_dominates_coarse_384_when_applicable_conservatively"])
        self.assertTrue(inner["all_exact_checks_pass"])
        self.assertTrue(inner["all_conservative_decimal_checks_pass"])
        qcert = row["intervals"]["Qcert_rank_upper_surrogate"]
        self.assertGreaterEqual(Decimal(qcert["lower"]), Decimal(0))

    def test_integer_dilation_cancellation_is_realized(self) -> None:
        points = certificate.erdos_turan_points(17)
        base = certificate.fixture_audit("base", points, 8, scale=1)
        scaled = certificate.fixture_audit("scaled", points, 8, scale=7)
        self.assertEqual(base["weight_counts"], scaled["weight_counts"])
        base_interval = base["intervals"]["Rcert_form_2"]
        scaled_interval = scaled["intervals"]["Rcert_form_2"]
        self.assertLessEqual(
            max(Decimal(base_interval["lower"]), Decimal(scaled_interval["lower"])),
            min(Decimal(base_interval["upper"]), Decimal(scaled_interval["upper"])),
        )
        base_sharp = base["intervals"]["Rsharp_form_1"]
        scaled_sharp = scaled["intervals"]["Rsharp_form_1"]
        self.assertLessEqual(
            max(Decimal(base_sharp["lower"]), Decimal(scaled_sharp["lower"])),
            min(Decimal(base_sharp["upper"]), Decimal(scaled_sharp["upper"])),
        )
        self.assertTrue(
            certificate.coefficient_mass_audit(8)["dilation_mass_cancellation_verified"]
        )

    def test_scaled_et_local_ghat_no_go_is_exact_and_scoped(self) -> None:
        expected_primes = {4: 11, 8: 17, 16: 37, 32: 67, 64: 131}
        for epoch, prime in expected_primes.items():
            with self.subTest(epoch=epoch):
                row = certificate.local_ghat_no_go_audit(epoch)
                self.assertEqual(row["bertrand_prime"], prime)
                self.assertTrue(row["base_is_golomb"])
                self.assertTrue(row["appended_ruler_is_golomb"])
                self.assertTrue(row["scaled_ruler_is_golomb"])
                self.assertTrue(row["H_plus_one_above_two_n_squared"])
                self.assertTrue(row["X_below_32_n_squared"])
                self.assertTrue(row["X_over_bq_below_four"])
                self.assertTrue(row["local_C32_cap_window_verified"])
                self.assertTrue(row["Ucoef_minus_Rcoef_formula_verified"])
                self.assertTrue(row["Bcoef_minus_Ucoef_formula_verified"])
                self.assertTrue(row["computed_Ghat_dominates_section_6_bound"])
                self.assertTrue(row["P27_endpoint_slack_clears_39_over_256_log2"])
                self.assertTrue(row["all_exact_checks_pass"])
                self.assertTrue(row["all_conservative_decimal_checks_pass"])
                self.assertTrue(row["uses_a_different_finite_ruler_at_each_epoch"])
                self.assertFalse(row["compatible_infinite_branch_inferred"])
                self.assertFalse(row["p24_refuted"])

    def test_certificate_scope_hash_and_deterministic_byte_replay(self) -> None:
        payload = certificate.build_certificate()
        self.assertTrue(payload["all_required_checks_pass"])
        scope = payload["scope_flags"]
        self.assertTrue(scope["finite_fixture_only"])
        self.assertTrue(scope["problem_unresolved"])
        self.assertTrue(scope["Rsharp_nonnegative_decomposition_proved"])
        self.assertTrue(scope["p27_intermediate_closed_by_inner_birth"])
        self.assertTrue(scope["p26_p27_standalone_upper_targets_saturated"])
        for claim in (
            "infinite_branch_constructed",
            "p24_proved",
            "p25_proved",
            "p26_proved",
            "p27_proved",
            "p27_asymptotic_upper_proved",
            "p27_unconditionally_refuted",
            "question_1_resolved",
            "question_2_resolved",
            "erdos_1191_resolved",
            "prize_claim_ready",
        ):
            self.assertFalse(scope[claim])

        without_hash = dict(payload)
        expected_hash = without_hash.pop("certificate_sha256")
        self.assertEqual(
            sha256(
                json.dumps(without_hash, sort_keys=True, separators=(",", ":")).encode(
                    "utf-8"
                )
            ).hexdigest(),
            expected_hash,
        )

        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.json"
            second = Path(directory) / "second.json"
            script = Path(certificate.__file__).resolve()
            subprocess.run(
                [sys.executable, str(script), "--output", str(first)], check=True
            )
            subprocess.run(
                [sys.executable, str(script), "--output", str(second)], check=True
            )
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(first.read_bytes(), certificate.certificate_bytes())


if __name__ == "__main__":
    unittest.main()

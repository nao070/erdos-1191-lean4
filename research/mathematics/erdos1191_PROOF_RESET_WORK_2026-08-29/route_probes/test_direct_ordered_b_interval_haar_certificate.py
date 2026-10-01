from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import unittest


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import direct_ordered_b_interval_haar_certificate as cert  # noqa: E402


class DirectOrderedBIntervalHaarTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_certificate_validates(self) -> None:
        cert.validate_certificate(self.value)

    def test_02_committed_json_semantic_and_byte_replay(self) -> None:
        raw = cert.DEFAULT_CERTIFICATE.read_bytes()
        loaded = json.loads(raw.decode("utf-8"))
        cert.validate_certificate(loaded)
        self.assertEqual(raw, cert.rendered_bytes(loaded))
        self.assertEqual(raw, cert.rendered_bytes(self.value))

    def test_03_B_and_M_normalizations_are_exact(self) -> None:
        self.assertEqual(
            cert.matrix_text(cert.wave_b_matrix(4)),
            [
                ["0/1", "0/1", "-1/32", "-9/128"],
                ["0/1", "0/1", "0/1", "-1/32"],
                ["-1/32", "0/1", "0/1", "0/1"],
                ["-9/128", "-1/32", "0/1", "0/1"],
            ],
        )
        row = self.value["interval_and_lambda_audit"]
        self.assertEqual(row["n4_M"][0], ["0/1", "0/1", "-1/32", "-5/128", "9/128"])
        self.assertEqual(row["n4_M"][4], ["9/128", "-5/128", "-1/32", "0/1", "0/1"])

    def test_04_interval_formula_and_sharp_count_constant(self) -> None:
        row = self.value["interval_and_lambda_audit"]
        self.assertEqual(row["interval_states_checked"], 216)
        self.assertEqual(row["mixed_difference_rows_checked"], 164)
        self.assertEqual(F(row["sharp_witness"]["value"]), F(1, 9))
        self.assertTrue(row["M_has_zero_diagonal"])
        self.assertTrue(row["M_times_one_is_zero"])

    def test_05_global_Gothic_rows_include_Frobenius_factor_two(self) -> None:
        rows = self.value["interval_and_lambda_audit"]["n4_global_lambda_rows"]
        by_interval = {tuple(row["global_interval"]): row for row in rows}
        self.assertEqual(F(by_interval[(4, 5)]["M_entry"]), F(-1, 32))
        self.assertEqual(F(by_interval[(4, 5)]["lambda"]), F(-1, 16))
        self.assertEqual(F(by_interval[(5, 5)]["lambda"]), F(1, 16))
        self.assertEqual(F(by_interval[(4, 7)]["lambda"]), F(9, 64))

    def test_06_general_Abel_endpoint_signs_are_both_present(self) -> None:
        row = self.value["general_Abel_endpoint_audit"]
        self.assertEqual(F(row["left_sum"]), F(496, 21))
        self.assertEqual(F(row["twice_width_band_sum"]), F(346, 231))
        self.assertEqual(F(row["lower_endpoint_row"]), F(-10, 3))
        self.assertEqual(F(row["upper_endpoint_row"]), F(280, 11))
        self.assertEqual(row["endpoint_signs"], {"lower": "negative", "upper": "positive"})

    def test_07_active_choice_removes_both_Abel_terminals(self) -> None:
        row = self.value["terminal_free_active_Abel_audit"]
        self.assertEqual(row["chosen_widths"], [4, 8, 16, 32])
        self.assertEqual(row["Q_rows"], ["0/1", "1/192", "1/2304", "0/1"])
        self.assertEqual(row["twice_width_band_rows"], ["-1/24", "11/144", "1/72"])
        self.assertEqual(F(row["terminal_free_sum"]), F(7, 144))
        self.assertTrue(row["both_endpoint_rows_vanish"])

    def test_08_signed_band_can_be_negative(self) -> None:
        row = self.value["signed_band_fixtures"]["negative"]
        self.assertEqual(row["difference_count"], 15)
        self.assertEqual(F(row["Q_T"]), 0)
        self.assertEqual(F(row["Q_2T"]), F(1, 324))
        self.assertEqual(F(row["signed_band_contraction"]), F(-1, 324))
        self.assertEqual(F(row["G_T_minus_G_2T"][0][2]), F(1, 36))

    def test_09_signed_band_can_be_positive(self) -> None:
        row = self.value["signed_band_fixtures"]["positive"]
        self.assertEqual(row["difference_count"], 28)
        self.assertEqual(F(row["Q_T"]), F(9, 32000))
        self.assertEqual(F(row["Q_2T"]), F(9, 256000))
        self.assertEqual(F(row["signed_band_contraction"]), F(63, 256000))
        self.assertEqual(F(row["twice_T_weighted_Abel_row"]), F(63, 640))

    def test_10_actual_half_open_Haar_cell_is_zero_aggregate_but_M_positive(self) -> None:
        row = self.value["actual_Haar_cell_fixture"]
        self.assertEqual(row["maximal_atomic_cell"], [636, 709])
        self.assertEqual(row["cell_length"], 73)
        self.assertEqual(row["scaled_state_all_eight_marks"], [0, 0, 0, -1, -1, 1, 1, 0])
        self.assertEqual(row["scaled_local_state_v"], [-1, -1, 1, 1, 0])
        self.assertEqual(row["D_v"], [0, -2, 0, 1])
        self.assertEqual(row["one_transpose_v"], 0)
        self.assertEqual(F(row["v_transpose_M_v"]), F(1, 8))
        self.assertEqual(F(row["pointwise_h_transpose_M_h"]), F(1, 1280000))

    def test_11_singleton_cover_and_zero_slack_Schur_obstructions(self) -> None:
        row = self.value["cover_and_Schur_obstructions"]
        self.assertEqual(row["singleton_M_values"], ["0/1"] * 5)
        self.assertFalse(row["nonzero_scalar_interval_cover_exists"])
        self.assertFalse(row["nonzero_zero_price_Schur_cross_coupling_exists"])
        self.assertEqual(F(row["exact_Schur_counterfixture"]["quadratic_value"]), -1)

    def test_12_A_L_count_baseline_price_and_finite_separation(self) -> None:
        row = self.value["A_L_count_baseline_family"]
        self.assertTrue(row["Golomb_for_every_integer_L_at_least_26"])
        self.assertEqual(row["maximum_positive_integral_collision_parameter"], 25)
        self.assertEqual(F(row["count_baseline_log_L_coefficient"]), F(11, 64))
        self.assertEqual(F(row["positive_same_epoch_Gothic_log_L_coefficient"]), F(9, 64))
        self.assertEqual(F(row["baseline_minus_positive_Gothic_log_L_coefficient"]), F(1, 32))
        finite = row["finite_separation_witness"]
        self.assertEqual(finite["L"], 2**24)
        self.assertEqual(F(finite["coarse_strict_lower_for_64_times_gap"]), 2)
        self.assertEqual(F(finite["count_baseline_minus_positive_Gothic_strictly_greater_than"]), F(1, 32))

    def test_13_epoch_pair_support_is_disjoint_but_J_endpoint_needs_owner(self) -> None:
        row = self.value["epoch_pair_ownership_audit"]
        self.assertEqual(row["shared_physical_points"], 1)
        self.assertTrue(row["direct_M_pair_supports_disjoint"])
        self.assertEqual(row["positive_J_baseline_shared_endpoint_diagonal_multiplicity"], 2)
        self.assertTrue(row["positive_block_count_baseline_requires_explicit_endpoint_owner"])

    def test_14_SDP_schema_records_the_actual_infeasibility_and_price(self) -> None:
        row = self.value["falsifiable_SDP_schema"]
        self.assertIn("half-open cell", row["single_epoch_fixed_scale"]["atomic_endpoints"])
        self.assertEqual(row["positive_fixture_gate"]["C_equal_zero_constraint_value"], "-mu/8 on the certified [636,709) state for every kappa")
        self.assertFalse(row["positive_fixture_gate"]["C_equal_zero_feasible_for_mu_positive"])
        self.assertTrue(row["positive_fixture_gate"]["nontrivial_repair_has_positive_diagonal_price"])

    def test_15_scope_keeps_the_common_ledger_and_problem_open(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["direct_B_interval_state_theorem_exact"])
        self.assertFalse(scope["signed_Haar_band_contraction_has_fixed_sign"])
        self.assertFalse(scope["finite_multi_epoch_SDP_solved"])
        self.assertFalse(scope["common_opposite_sign_capacity_ledger_closed"])
        self.assertFalse(scope["C058_closed"])
        self.assertFalse(scope["question_1_resolved"])
        self.assertFalse(scope["question_2_resolved"])
        self.assertFalse(scope["prize_claim_ready"])

    def test_16_payload_hash_and_all_mutations(self) -> None:
        self.assertEqual(self.value["integrity"]["payload_sha256"], cert.payload_hash(self.value))
        self.assertFalse(self.value["integrity"]["source_hash_embedded"])
        changed = copy.deepcopy(self.value)
        changed["integrity"]["source_hash_embedded"] = True
        with self.assertRaises(cert.CertificateError):
            cert.validate_certificate(changed)
        self.assertEqual(cert.self_check(self.value), 16)


if __name__ == "__main__":
    unittest.main()

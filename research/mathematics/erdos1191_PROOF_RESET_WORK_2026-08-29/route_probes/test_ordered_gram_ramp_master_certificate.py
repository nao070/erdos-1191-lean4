from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import sys
import unittest


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ordered_gram_ramp_master_certificate as cert  # noqa: E402


class OrderedGramRampMasterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_certificate_validates(self) -> None:
        cert.validate_certificate(self.value)

    def test_02_committed_certificate_replays_semantically_and_byte_exactly(self) -> None:
        loaded = json.loads(cert.DEFAULT_CERTIFICATE.read_text(encoding="utf-8"))
        cert.validate_certificate(loaded)
        self.assertEqual(cert.rendered_bytes(loaded), cert.rendered_bytes(self.value))

    def test_03_local_root_cone_overlap_exhaustion(self) -> None:
        row = self.value["local_root_cone_audit"]
        self.assertEqual(row["rows_checked"], 2700)
        self.assertEqual(row["positive_overlap_rows"], 1296)
        self.assertTrue(row["same_sign_and_reverse_order_disjoint"])
        self.assertTrue(row["overlap_equals_tent_numerator"])

    def test_04_n4_golomb_and_gram_matrix(self) -> None:
        row = self.value["n4_ramp_fixture"]
        self.assertEqual(row["difference_count"], 28)
        self.assertEqual(
            row["T_squared_G"],
            [[214, 0, -106, -1], [0, 218, 0, -109], [-106, 0, 222, -3], [-1, -109, -3, 226]],
        )
        self.assertEqual(row["T_squared_rho"], {"4": 107, "5": 109, "6": 113, "7": 113})

    def test_05_wave_dual_factor_and_positive_definite_gram(self) -> None:
        row = self.value["n4_ramp_fixture"]
        self.assertEqual(F(row["wave"]["T_squared_Q"]), F(869, 64))
        self.assertTrue(all(F(value) > 0 for value in row["leading_principal_minors_of_T_squared_G"]))
        self.assertEqual(F(row["wave"]["B_determinant"]), F(1, 1048576))
        self.assertEqual(row["wave"]["B_inertia_from_invertible_bipartite_block"], [2, 2, 0])

    def test_06_midpoint_ramp_surplus_is_exact(self) -> None:
        row = self.value["n4_ramp_fixture"]["midpoint_ramp"]
        self.assertEqual(F(row["T_squared_energy"]), F(2845, 128))
        self.assertEqual(F(row["T_squared_surplus"]), F(1107, 128))
        self.assertEqual(
            F(row["T_squared_residual_surplus"]) + F(row["T_squared_adjacent_surplus"]),
            F(row["T_squared_surplus"]),
        )
        self.assertEqual(
            row["root_slacks_of_H_minus_B"],
            {"4,5": "1/64", "4,6": "0/1", "4,7": "0/1", "5,6": "1/64", "5,7": "0/1", "6,7": "1/64"},
        )

    def test_07_optimal_shift_schur_complement_is_exact(self) -> None:
        row = self.value["n4_ramp_fixture"]["optimal_shift"]
        self.assertEqual(F(row["c_star"]), F(1221, 221))
        self.assertEqual(F(row["T_squared_optimal_energy"]), F(39289, 1768))
        self.assertEqual(F(row["T_squared_optimal_surplus"]), F(122263, 14144))
        self.assertEqual(F(row["T_squared_residual_variance_before_1_over_4n_squared"]), F(121600, 221))

    def test_08_zero_slack_schur_cross_coupling_gate(self) -> None:
        row = self.value["n4_ramp_fixture"]["zero_slack_cross_coupling"]
        self.assertTrue(row["nonadjacent_graph_connected"])
        self.assertEqual(F(row["Schur_root_value_with_D_equal_1"]), -4)
        self.assertIn("all rows of X are equal", row["consequence"])

    def test_09_n5_golomb_active_triangle(self) -> None:
        row = self.value["n5_triangle_fixture"]
        self.assertEqual(row["difference_count"], 45)
        self.assertEqual(row["active_triangle_vertices"], [5, 7, 9])
        self.assertEqual([edge["psi"] for edge in row["edges"]], ["97/11449", "103/11449", "1/11449"])
        self.assertEqual([edge["alpha"] for edge in row["edges"]], ["1/25", "1/25", "4/25"])
        self.assertTrue(row["odd_cycle_blocks_universal_bipartite_sign_switch"])

    def test_10_unlocalized_ramp_divergence_and_active_gate(self) -> None:
        row = self.value["small_scale_divergence_fixture"]
        self.assertEqual(F(row["Q"]), 0)
        self.assertEqual(
            row["T_squared_G"],
            [[2, -1, 0, 0], [-1, 2, -1, 0], [0, -1, 2, -1], [0, 0, -1, 2]],
        )
        self.assertEqual(F(row["midpoint_ramp_energy"]), F(15, 128))
        self.assertEqual(row["active_Q_scale_gate_for_n4"], {"strict_lower": 109, "strict_upper": 440})

    def test_11_signed_band_root_cone_loss(self) -> None:
        row = self.value["signed_band_cone_loss_fixture"]
        self.assertEqual(row["difference_count"], 15)
        self.assertFalse(row["SDDM_root_cone_preserved"])
        self.assertEqual(F(row["positive_offdiagonal_witness"]["value"]), F(1, 36))
        self.assertEqual(F(row["sum_zero_coefficient_mixing_witness"]["quadratic_value_for_Wave_B"]), F(-1, 9))

    def test_12_scope_gates_keep_route_and_problem_open(self) -> None:
        gates = self.value["scope_gates"]
        self.assertTrue(gates["fixed_scale_actual_ordered_gram_only"])
        self.assertTrue(gates["active_scale_localization_required_for_integrated_ramp_use"])
        self.assertFalse(gates["common_master_diagonal_and_terminal_payment_closed"])
        self.assertFalse(gates["route_c_closed"])
        self.assertFalse(gates["C058_closed"])
        self.assertFalse(gates["erdos_1191_solved"])

    def test_13_marginal_transport_scope_is_reconciled(self) -> None:
        row = self.value["marginal_transport_reconciliation"]
        self.assertIn("Q<=V<=P_PSD/2", row["statement"])
        self.assertFalse(row["universal_order_between_V_and_ramp_energy_claimed"])

    def test_14_payload_hash_has_no_source_self_reference(self) -> None:
        self.assertEqual(self.value["integrity"]["payload_sha256"], cert.payload_hash(self.value))
        self.assertFalse(self.value["integrity"]["source_hash_embedded"])
        changed = copy.deepcopy(self.value)
        changed["integrity"]["source_hash_embedded"] = True
        with self.assertRaises(cert.CertificateError):
            cert.validate_certificate(changed)

    def test_15_self_check_rejects_all_mutations(self) -> None:
        self.assertEqual(cert.self_check(self.value), 12)


if __name__ == "__main__":
    unittest.main()

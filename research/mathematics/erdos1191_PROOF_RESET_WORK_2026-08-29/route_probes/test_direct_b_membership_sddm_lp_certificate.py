from __future__ import annotations

import copy
from fractions import Fraction as F
import json
import unittest

import direct_b_membership_sddm_lp_certificate as cert


class DirectBMembershipSDDMLPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_certificate_validates(self) -> None:
        cert.validate_certificate(self.value)

    def test_02_committed_certificate_replays_byte_exactly(self) -> None:
        raw = cert.DEFAULT_CERTIFICATE.read_bytes()
        loaded = json.loads(raw.decode("utf-8"))
        cert.validate_certificate(loaded)
        self.assertEqual(raw, cert.rendered_bytes(self.value))

    def test_03_one_epoch_complete_actual_cells(self) -> None:
        row = self.value["one_epoch"]
        self.assertEqual(row["event_count"], 15)
        self.assertEqual(row["complete_real_line_atomic_cell_count"], 16)
        self.assertEqual(row["finite_active_cell_count"], 14)
        self.assertEqual(row["atomic_cells"][0]["state"], [0, 0, 0, 0, 0])
        self.assertEqual(row["atomic_cells"][-1]["state"], [0, 0, 0, 0, 0])
        self.assertEqual(row["atomic_cells"][6]["id"], "[636,709)")
        self.assertEqual(row["atomic_cells"][6]["state"], [-1, -1, 1, 1, 0])

    def test_04_zero_sum_cells_force_positive_LP_A_correction(self) -> None:
        row = self.value["one_epoch"]
        self.assertEqual(
            [(cell["id"], cell["M_rhs"]) for cell in row["zero_sum_positive_M_cells"]],
            [("[636,709)", "1/8"), ("[749,816)", "1/8")],
        )
        self.assertTrue(row["LP_A_zero_sum_cells_force_positive_exact_correction"])
        self.assertEqual(F(row["LP_A_minimum_trace_C"]), F(1, 16))

    def test_05_LP_A_exact_primal_dual_zero_gap(self) -> None:
        row = self.value["one_epoch"]["LP_A"]
        self.assertEqual(row["primal"]["root_weights"], {"1,3": "1/32"})
        self.assertEqual(row["primal"]["kappas"], ["3/32"])
        self.assertEqual(row["dual"]["cell_weights"], {"[749,816)": "1/2"})
        self.assertEqual(F(row["primal"]["objective"]), F(1, 16))
        self.assertEqual(row["primal"]["objective"], row["dual"]["objective"])
        self.assertTrue(row["zero_duality_gap"])

    def test_06_LP_B_exact_primal_dual_zero_gap(self) -> None:
        row = self.value["one_epoch"]["LP_B"]
        self.assertEqual(row["primal"]["root_weights"], {"0,2": "1/40", "2,4": "1/40"})
        self.assertEqual(row["primal"]["kappas"], ["0/1"])
        self.assertEqual(
            row["dual"]["cell_weights"],
            {"[525,616)": "2/5", "[836,925)": "2/5"},
        )
        self.assertEqual(F(row["optimal_value"]), F(1, 10))
        self.assertEqual(row["primal"]["objective"], row["dual"]["objective"])

    def test_07_root_corrections_are_PSD_SDDM_not_claimed_PD(self) -> None:
        for row in (
            self.value["one_epoch"]["LP_A"],
            self.value["one_epoch"]["LP_B"],
            self.value["two_consecutive_epochs"]["LP_B"],
        ):
            self.assertTrue(row["primal"]["C_is_nonnegative_root_sum_hence_PSD_SDDM"])
            self.assertTrue(row["primal"]["C_times_one_is_zero"])
            matrix = [[F(value) for value in line] for line in row["primal"]["C_matrix"]]
            self.assertTrue(all(sum(line, F(0)) == 0 for line in matrix))

    def test_08_two_epoch_fixture_is_golomb_and_both_epochs_active(self) -> None:
        row = self.value["two_consecutive_epochs"]
        self.assertEqual(len(cert.positive_differences(row["full_16_mark_Golomb_fixture"])), 120)
        self.assertEqual(row["complete_real_line_atomic_cell_count"], 40)
        self.assertEqual(
            row["epoch_activity"],
            {
                "n4_nonzero_cell_constraints": 7,
                "n4_positive_cell_constraints": 5,
                "n8_nonzero_cell_constraints": 15,
                "n8_positive_cell_constraints": 5,
                "n4_integrated_signed_Haar_band": "63/256000",
                "n8_integrated_signed_Haar_band": "169/5120000",
                "combined_integrated_signed_Haar_band": "1429/5120000",
                "n4_dual_objective_share": "5/56",
                "n8_dual_objective_share": "13/448",
                "both_epochs_are_substantively_active_at_common_T": True,
            },
        )

    def test_09_two_epoch_exact_primal_dual_zero_gap(self) -> None:
        row = self.value["two_consecutive_epochs"]["LP_B"]
        self.assertEqual(
            row["primal"]["root_weights"],
            {"0,2": "45/1792", "2,4": "11/448", "4,6": "3/1792", "10,12": "1/128"},
        )
        self.assertEqual(row["primal"]["kappas"], ["0/1", "0/1"])
        self.assertEqual(
            row["dual"]["cell_weights"],
            {
                "[1100,1149)": "3/7",
                "[1725,1744)": "1/2",
                "[636,709)": "3/7",
                "[836,864)": "2/7",
            },
        )
        self.assertEqual(F(row["optimal_value"]), F(53, 448))
        self.assertEqual(row["primal"]["objective"], row["dual"]["objective"])

    def test_10_shared_endpoint_has_single_global_accounting_not_budget_owner(self) -> None:
        row = self.value["two_consecutive_epochs"]
        self.assertTrue(row["direct_M_pair_supports_disjoint"])
        self.assertEqual(row["shared_physical_point"], 749)
        owner = row["shared_endpoint_ownership"]
        self.assertTrue(owner["aggregate_kappas_are_zero"])
        self.assertTrue(owner["no_double_owned_J_diagonal_is_used"])
        self.assertFalse(owner["budget_owner_supplied"])
        self.assertEqual(F(owner["C_shared_endpoint_diagonal"]), F(47, 1792))
        self.assertEqual(owner["C_shared_endpoint_diagonal_trace_multiplicity"], 1)

    def test_11_payload_hash_and_scope_gate(self) -> None:
        self.assertEqual(self.value["integrity"]["payload_sha256"], cert.payload_hash(self.value))
        changed = copy.deepcopy(self.value)
        changed["status"] = "PRIZE_READY"
        cert.rehash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.validate_certificate(changed)

    def test_12_self_check_rejects_all_mutations(self) -> None:
        self.assertEqual(cert.self_check(self.value), 12)


if __name__ == "__main__":
    unittest.main()

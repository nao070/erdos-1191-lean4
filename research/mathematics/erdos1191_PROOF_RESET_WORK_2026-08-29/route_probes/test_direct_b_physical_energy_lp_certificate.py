from __future__ import annotations

import copy
from fractions import Fraction as F
import json
import unittest

import direct_b_physical_energy_lp_certificate as cert


class DirectBPhysicalEnergyLPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_certificate_validates(self) -> None:
        cert.validate_certificate(self.value)

    def test_02_committed_certificate_has_literal_raw_byte_replay(self) -> None:
        raw = cert.DEFAULT_CERTIFICATE.read_bytes()
        loaded = json.loads(raw.decode("utf-8"))
        cert.validate_certificate(loaded)
        self.assertEqual(raw, cert.rendered_bytes(self.value))

    def test_03_piecewise_physical_root_cost(self) -> None:
        self.assertEqual(cert.physical_root_cost(0, 200), F(0))
        self.assertEqual(cert.physical_root_cost(100, 200), F(3, 2))
        self.assertEqual(cert.physical_root_cost(200, 200), F(3))
        self.assertEqual(cert.physical_root_cost(300, 200), F(5, 2))
        self.assertEqual(cert.physical_root_cost(400, 200), F(2))
        self.assertEqual(cert.physical_root_cost(500, 200), F(2))
        audit = cert.root_cost_audit()
        self.assertGreater(audit["exact_integer_parameter_rows_checked"], 400)

    def test_04_complete_cells_and_aggregate_costs(self) -> None:
        self.assertEqual(self.value["separate_n4"]["complete_real_line_atomic_cell_count"], 16)
        self.assertEqual(self.value["separate_n8"]["complete_real_line_atomic_cell_count"], 28)
        self.assertEqual(self.value["joint_n4_n8"]["complete_real_line_atomic_cell_count"], 40)
        self.assertEqual(self.value["separate_n4"]["LP"]["costs"]["aggregate_costs"], ["3/1"])
        self.assertEqual(self.value["separate_n8"]["LP"]["costs"]["aggregate_costs"], ["97/25"])
        self.assertEqual(self.value["joint_n4_n8"]["LP"]["costs"]["aggregate_costs"], ["3/1", "97/25"])

    def test_05_separate_n4_exact_primal_dual(self) -> None:
        row = self.value["separate_n4"]["LP"]
        self.assertEqual(row["primal"]["root_weights"], {"0,2": "1/40", "2,4": "1/40"})
        self.assertEqual(row["primal"]["kappas"], ["0/1"])
        self.assertEqual(F(row["optimal_value"]), F(29, 200))
        self.assertEqual(row["primal"]["objective_from_root_and_aggregate_costs"], row["dual"]["objective"])
        self.assertEqual(F(row["weighted_signed_direct_B_demand"]), F(63, 640))
        self.assertEqual(F(row["physical_correction_surplus_over_signed_demand"]), F(149, 3200))
        self.assertEqual(row["dual"]["aggregate_loads"], ["107/150"])

    def test_06_separate_n8_exact_primal_dual(self) -> None:
        row = self.value["separate_n8"]["LP"]
        self.assertEqual(row["primal"]["root_weights"], {"0,2": "1/128", "6,8": "1/128"})
        self.assertEqual(row["primal"]["kappas"], ["0/1"])
        self.assertEqual(F(row["optimal_value"]), F(139, 3200))
        self.assertEqual(row["primal"]["objective_from_complete_cell_sum"], row["dual"]["objective"])
        self.assertEqual(F(row["weighted_signed_direct_B_demand"]), F(169, 12800))
        self.assertEqual(F(row["physical_correction_surplus_over_signed_demand"]), F(387, 12800))
        self.assertEqual(row["dual"]["aggregate_loads"], ["151/200"])

    def test_07_joint_exact_primal_dual(self) -> None:
        row = self.value["joint_n4_n8"]["LP"]
        self.assertEqual(
            row["primal"]["root_weights"],
            {"0,2": "45/1792", "2,4": "11/448", "4,6": "3/1792", "10,12": "1/128"},
        )
        self.assertEqual(row["primal"]["kappas"], ["0/1", "0/1"])
        self.assertEqual(F(row["optimal_value"]), F(3809, 22400))
        self.assertEqual(row["primal"]["objective_from_complete_cell_sum"], row["dual"]["objective"])
        self.assertEqual(F(row["weighted_signed_direct_B_demand"]), F(1429, 12800))
        self.assertEqual(F(row["physical_correction_surplus_over_signed_demand"]), F(5233, 89600))
        self.assertEqual(row["dual"]["aggregate_loads"], ["16221/7700", "15929/16800"])
        self.assertEqual(
            self.value["joint_n4_n8"]["dual_objective_epoch_split"],
            {"n4": "727/5600", "n8": "901/22400", "both_strictly_positive": True},
        )

    def test_08_active_root_dual_loads_equal_physical_costs(self) -> None:
        for fixture in ("separate_n4", "separate_n8", "joint_n4_n8"):
            row = self.value[fixture]["LP"]
            for edge, weight in row["primal"]["root_weights"].items():
                if F(weight):
                    self.assertEqual(row["dual"]["root_loads"][edge], row["costs"]["root_costs"][edge])
            measure = row["canonical_cell_length_dual"]
            self.assertTrue(measure["every_root_and_aggregate_cost_column_is_saturated"])
            self.assertTrue(measure["dual_feasible_lower_bound"])
            self.assertEqual(
                measure["objective_equals_weighted_signed_direct_B_demand"],
                row["weighted_signed_direct_B_demand"],
            )

    def test_09_joint_is_strictly_cheaper_than_separate_sum(self) -> None:
        row = self.value["joint_vs_separate"]
        self.assertTrue(row["embedded_separate_is_jointly_feasible"])
        self.assertEqual(F(row["sum_of_separate_optima"]), F(603, 3200))
        self.assertEqual(F(row["joint_optimum"]), F(3809, 22400))
        self.assertEqual(F(row["exact_joint_saving"]), F(103, 5600))
        self.assertTrue(row["joint_strictly_less_than_sum_of_separate"])

    def test_10_scope_and_budget_owner_gates(self) -> None:
        self.assertFalse(self.value["joint_n4_n8"]["budget_owner_supplied"])
        self.assertTrue(self.value["objective"]["not_the_coefficient_trace_objective"])
        self.assertIn("C058, Q1, Q2, or Erdos Problem 1191", self.value["scope"]["not_proved"])
        changed = copy.deepcopy(self.value)
        changed["status"] = "ERDOS_1191_SOLVED"
        cert.rehash(changed)
        with self.assertRaises(cert.CertificateError):
            cert.validate_certificate(changed)

    def test_11_payload_hash_is_canonical(self) -> None:
        self.assertEqual(self.value["integrity"]["payload_sha256"], cert.payload_hash(self.value))

    def test_12_self_check_rejects_all_mutations(self) -> None:
        self.assertEqual(cert.self_check(self.value), 16)

    def test_13_three_epoch_fixture_and_complete_cells(self) -> None:
        row = self.value["three_epoch_n4_n8_n16"]
        self.assertEqual(row["fixture"]["positive_difference_count"], 496)
        self.assertTrue(row["fixture"]["all_positive_differences_distinct"])
        self.assertEqual(row["joint"]["complete_real_line_atomic_cell_count"], 88)
        self.assertEqual(
            row["joint"]["per_epoch_weighted_signed_demands"],
            {"n4": "783/6400", "n8": "3769/128000", "n16": "3333/512000", "total": "81049/512000"},
        )

    def test_14_three_epoch_separate_optima(self) -> None:
        row = self.value["three_epoch_n4_n8_n16"]["separate"]
        self.assertEqual(F(row["n4"]["LP"]["optimal_value"]), F(299, 2000))
        self.assertEqual(F(row["n8"]["LP"]["optimal_value"]), F(1489, 32000))
        self.assertEqual(F(row["n16"]["LP"]["optimal_value"]), F(1477, 128000))
        self.assertEqual(F(row["sum_of_separate_optima"]), F(26569, 128000))
        self.assertEqual(row["n16"]["LP"]["dual"]["aggregate_loads"], ["301/400"])

    def test_15_three_epoch_joint_exact_primal_dual(self) -> None:
        row = self.value["three_epoch_n4_n8_n16"]["joint"]
        lp = row["LP"]
        self.assertEqual(
            lp["primal"]["root_weights"],
            {
                "0,2": "45/1792",
                "2,4": "11/448",
                "4,6": "3/1792",
                "10,12": "1/128",
                "26,28": "1/512",
            },
        )
        self.assertEqual(lp["primal"]["kappas"], ["0/1", "0/1", "0/1"])
        self.assertEqual(F(lp["optimal_value"]), F(163481, 896000))
        self.assertEqual(lp["costs"]["aggregate_costs"], ["3/1", "386/125", "444/125"])
        self.assertEqual(lp["dual"]["aggregate_loads"], ["162947/84000", "2463/2000", "171011/168000"])
        self.assertEqual(
            row["dual_objective_epoch_split"],
            {"n4": "7477/56000", "n8": "1979/48000", "n16": "20723/2688000", "all_strictly_positive": True},
        )
        self.assertEqual(F(lp["physical_correction_surplus_over_signed_demand"]), F(86581, 3584000))

    def test_16_three_epoch_saving_and_T2500_countercheck(self) -> None:
        row = self.value["three_epoch_n4_n8_n16"]
        comparison = row["joint_vs_separate"]
        self.assertTrue(comparison["embedded_separate_is_jointly_feasible"])
        self.assertEqual(F(comparison["exact_joint_saving"]), F(11251, 448000))
        counter = row["same_sparse_weights_T2500_countercheck"]
        self.assertEqual(counter["cell"], "[6036,6516)")
        self.assertEqual(F(counter["lhs_correction"]), F(1, 8))
        self.assertEqual(F(counter["rhs_direct_M_demand"]), F(9, 32))
        self.assertEqual(F(counter["slack"]), -F(5, 32))
        self.assertFalse(counter["same_T2000_sparse_correction_is_feasible_at_T2500"])


if __name__ == "__main__":
    unittest.main()

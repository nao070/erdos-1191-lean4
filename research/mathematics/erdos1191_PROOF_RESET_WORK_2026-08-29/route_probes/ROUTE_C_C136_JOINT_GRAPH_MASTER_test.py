#!/usr/bin/env python3
"""Focused exact tests for the scratch-only C136 partial certificate."""

from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path
import sys
import unittest


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate as cert  # noqa: E402


class C136JointMasterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()

    def test_01_explicit_fixture_is_exact_32_mark_golomb_ruler(self) -> None:
        audit = cert.fixture_audit()
        self.assertEqual(audit["marks"], 32)
        self.assertEqual(audit["span"], 7084)
        self.assertEqual(audit["positive_differences"], 496)
        self.assertEqual(audit["distinct_positive_differences"], 496)
        self.assertTrue(audit["Golomb_Sidon_valid"])

    def test_02_all_1192_direct_rows_and_positive_capacity_replay(self) -> None:
        graph = self.value["direct_owner_graph_master"]
        self.assertEqual(graph["classification"], "EXACT_FEASIBLE_IN_STATED_GRAPH_ROOT_SUBCONE")
        self.assertEqual(graph["active_events"], 150)
        self.assertEqual(graph["active_cells"], 149)
        self.assertEqual(graph["direct_owner_cell_rows"], 1192)
        self.assertEqual(graph["epoch8_M8_direct_rows"], 596)
        self.assertEqual(graph["epoch16_full_M16_direct_rows"], 596)
        self.assertEqual(graph["nonnegative_owned_capacity_rows"], 1192)
        self.assertEqual(graph["zero_owned_capacity_rows"], 807)
        self.assertEqual(graph["strict_positive_owned_capacity_rows"], 385)
        self.assertEqual(graph["tight_direct_owner_rows"], 884)
        self.assertEqual(graph["strict_direct_owner_rows"], 308)
        self.assertEqual(graph["negative_zero_positive_demand_rows"], [40, 971, 181])

    def test_03_graph_root_matrix_is_exact_psd_zero_sum_and_affordable(self) -> None:
        graph = self.value["direct_owner_graph_master"]
        self.assertEqual(graph["positive_support_roots"], 57)
        self.assertEqual(graph["graph_matrix_rank"], 51)
        self.assertTrue(graph["PSD_by_nonnegative_graph_root_sum"])
        self.assertTrue(graph["zero_row_sums"])
        self.assertTrue(all(F(row["coefficient_y_equals_t_times_w"]) > 0 for row in graph["support"]))
        recovery = graph["exact_support_recovery"]
        self.assertEqual(recovery["tight_rows_used_for_exactification"], 57)
        self.assertEqual(recovery["modular_rank"], 57)
        self.assertEqual(recovery["modular_full_rank_prime"], 1_000_003)
        self.assertTrue(recovery["unique_Fraction_Gauss_solution_matches_stored_support"])
        self.assertEqual(F(graph["integrated_direct_demand_D"]), F(457, 4))
        self.assertEqual(F(graph["physical_price_P"]), F(1878008419901, 9402974208))
        self.assertEqual(F(graph["positive_2D_minus_P_margin"]), F(270571186627, 9402974208))
        self.assertGreater(F(graph["positive_2D_minus_P_margin"]), 0)

    def test_04_full_M8_M16_and_63_source_gate(self) -> None:
        gate = self.value["full_M16_residual_gate"]
        self.assertEqual((gate["M8_primitive_sources"], gate["M8_primitive_alpha_mass"]), (21, "329/256"))
        self.assertEqual((gate["M16_primitive_sources"], gate["M16_primitive_alpha_mass"]), (105, "5425/1024"))
        self.assertEqual((gate["cross_half_source_count"], gate["cross_half_alpha_mass"]), (63, "4767/1024"))
        self.assertEqual(gate["R16_ordered_nonzero_offdiagonal_entries"], 160)
        self.assertEqual(gate["R16_unordered_nonzero_offdiagonal_entries"], 80)
        self.assertEqual(gate["sample_R16_entries"], ["-1/32", "15/2048", "1/1024"])
        self.assertTrue(gate["M16_used_in_every_epoch16_direct_row"])
        self.assertFalse(gate["quarter_scaled_two_M8_replacement_used"])

    def test_05_rank15_and_complete_C133_box_carrier_ledger(self) -> None:
        graph = self.value["direct_owner_graph_master"]
        ledger = self.value["C133_same_fixture_phase_box_carrier_14_row_contract"]
        self.assertEqual(graph["owner_fiber_counts"], {"past_epoch4": 4, "epoch8": 32, "epoch16": 64})
        self.assertEqual(graph["rank15_owner"], "epoch8")
        self.assertEqual(ledger["pointwise_14_row_identities_checked"], 191)
        self.assertEqual(ledger["unique_pair_birth_checks"], 1910)
        self.assertEqual(ledger["raw_separate_occurrences"], 18)
        self.assertEqual(ledger["unique_stitched_keys"], 14)
        self.assertEqual((ledger["initial_rows"], ledger["shared_rows"], ledger["final_rows"], ledger["upper_terminal_rows"]), (4, 4, 4, 2))
        self.assertTrue(ledger["all_14_integrated_rows_nonzero"])
        self.assertEqual(len(ledger["integrated_rows"]), 14)
        self.assertEqual(F(ledger["integrated_lhs_equals_rhs"]), F(10229179, 1007632080))

    def test_06_exact_countercell_separates_carrier_from_direct_demand(self) -> None:
        gate = self.value["direct_demand_vs_box_carrier_unlink_gate"]
        self.assertEqual(gate["joint_endpoint_cell"], ["44701/4", "46081/4"])
        self.assertEqual(gate["midpoint"], "45391/4")
        self.assertEqual(gate["box_carrier_C133_lhs_density"], "0/1")
        self.assertEqual(gate["weighted_direct_M8_M16_demand_density"], "225/32768")
        self.assertEqual(
            gate["only_nonzero_direct_component"],
            {"owner": [16, 8], "unweighted_demand": "25/2048", "weight": "9/16"},
        )
        self.assertEqual(
            set(gate["nonzero_box_carrier_rows_cancel_on_cell"]),
            {"band:A32:s3", "terminal:e16:s4"},
        )
        self.assertEqual(gate["graph_multipliers"], [1, 2, 4, 8])
        self.assertFalse(gate["scale4_multiplier16_terminal_channel_present"])
        self.assertEqual(
            gate["nonzero_integrated_upper_terminal_values"],
            ["253807/111959120", "6604809/1791345920"],
        )
        self.assertFalse(gate["box_carrier_is_direct_demand_potential"])

    def test_07_scope_keeps_full_joint_payment_unknown_and_C058_open(self) -> None:
        scope = self.value["scope"]
        self.assertEqual(
            self.value["overall_full_14_row_joint_classification"],
            "UNKNOWN_UNLINKED_GRAPH_PRICE_TO_C133_PAYMENT",
        )
        for key in (
            "box_carrier_is_direct_M8_M16_demand_potential",
            "scale4_multiplier16_terminal_channel_present",
            "C133_all_14_box_carrier_rows_paid_by_graph_master",
            "graph_price_to_C133_box_carrier_row_charge_identity_proved",
            "phase_interval_feasible",
            "phase_integrated_master_constructed",
            "nonanticipating_phase_rule_proved",
            "global_C103_owner_boundary_ledger_constructed",
            "arbitrary_history_proved",
            "arbitrary_rank_proved",
            "full_joint_problem_infeasible",
            "C058_Q1_Q2_proved",
        ):
            self.assertFalse(scope[key], key)

    def test_08_json_integrity_and_adversarial_mutations(self) -> None:
        on_disk = json.loads(
            (HERE / "ROUTE_C_C136_JOINT_GRAPH_MASTER_certificate.json").read_text(encoding="utf-8")
        )
        self.assertEqual(cert.validate_certificate(on_disk), self.value)
        mutations = cert.mutation_self_check(self.value)
        self.assertEqual(mutations["attempted"], 10)
        self.assertEqual(mutations["rejected"], 10)


if __name__ == "__main__":
    unittest.main(verbosity=2)

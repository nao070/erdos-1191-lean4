#!/usr/bin/env python3
"""Regression tests for the scoped ramp/common-master insertion no-go."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import ramp_common_master_no_go_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("ramp_common_master_no_go_certificate.json")


class RampCommonMasterNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_affine_family_is_golomb_after_25(self) -> None:
        row = probe.affine_golomb_fixture()
        self.assertEqual(row["difference_count"], 28)
        self.assertEqual(F(row["largest_positive_collision_root"]), 25)
        self.assertTrue(row["golomb_for_every_real_L_greater_than_25"])
        self.assertEqual(row["finite_difference_count"], 28)

    def test_02_ramp_is_not_a_fixed_full_prefix_channel_mix(self) -> None:
        row = probe.formal_nonspan_fixture()
        self.assertEqual(sum((F(value) for value in row["point_weights"]), F(0)), 0)
        self.assertGreater(len(set(row["point_weights"])), 1)
        self.assertFalse(row["ramp_is_in_fixed_full_prefix_channel_span"])

    def test_03_zero_mass_extension_has_positive_schur_price(self) -> None:
        row = probe.schur_extension_fixture()
        self.assertEqual(F(row["b_sum"]), 0)
        self.assertEqual(F(row["minimum_fourth_diagonal_for_psd"]), F(1, 25))
        self.assertEqual(F(row["strict_schur_residual"]), F(1, 100))
        self.assertEqual(F(row["inverse_cover_price"]), 1)
        self.assertFalse(row["nonzero_cross_coupling_has_zero_energy_price"])

    def test_04_small_scale_divergence_is_exact(self) -> None:
        row = probe.active_gate_fixture()
        self.assertEqual(F(row["n4_small_T_coefficient_over_T"]), F(15, 128))
        self.assertTrue(row["ungated_integral_diverges_at_zero"])

    def test_05_finite_abel_terminal_is_retained(self) -> None:
        row = probe.active_gate_fixture()
        self.assertEqual(F(row["finite_abel_lhs"]), 58)
        self.assertEqual(F(row["finite_abel_rhs_with_terminal"]), 58)
        self.assertTrue(row["terminal_is_nonzero_for_nonzero_ramp_measure_and_finite_box_width"])

    def test_06_optimal_ramp_has_sharp_logarithmic_gap(self) -> None:
        row = probe.asymptotic_no_go_fixture()
        self.assertEqual(F(row["Q_log_coefficient"]), F(9, 64))
        self.assertEqual(F(row["surplus_log_coefficient"]), F(9, 128))
        self.assertEqual(F(row["ramp_log_coefficient"]), F(27, 128))
        self.assertEqual(F(row["positive_gothic_log_L_coefficient"]), F(9, 64))
        self.assertEqual(F(row["ramp_minus_positive_gothic_log_L_coefficient"]), F(9, 128))

    def test_07_unused_potential_has_no_logarithmic_reserve(self) -> None:
        row = probe.asymptotic_no_go_fixture()
        self.assertEqual(F(row["wave_log_L_coefficient"]), F(9, 64))
        self.assertEqual(F(row["unused_potential_G_minus_W_log_L_coefficient"]), 0)

    def test_08_endpoint_Hilbert_price_is_sharp(self) -> None:
        row = probe.asymptotic_no_go_fixture()
        self.assertEqual(F(row["wave_edge_47_squared_distance"]), F(9, 64))
        self.assertEqual(F(row["sharp_two_endpoint_Hilbert_boundary_coefficient"]), F(9, 128))

    def test_09_finite_L_separation_is_strict(self) -> None:
        row = probe.asymptotic_no_go_fixture()
        self.assertEqual(row["finite_separation_L"], 2**18)
        self.assertEqual(F(row["finite_log_L_lower"]), 12)
        self.assertEqual(F(row["finite_ramp_integral_minus_gothic_lower_bound"]), F(1, 128))
        self.assertTrue(row["active_ramp_baseline_exceeds_positive_gothic_at_finite_L"])

    def test_10_B_is_ordered_dual_but_not_coefficient_psd(self) -> None:
        row = probe.ordered_dual_caveat_fixture()
        self.assertTrue(row["B_is_in_actual_ordered_root_dual"])
        self.assertFalse(row["B_is_coefficient_psd"])
        self.assertFalse(row["minus_B_is_in_actual_ordered_root_dual_when_a_wave_edge_is_active"])
        self.assertFalse(row["negative_common_carrier_follows_from_dual_positivity_alone"])

    def test_11_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_12_mutations_and_scope_guards(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 10)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["question_1_resolved"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)
        scope = self.fixture["scope"]
        self.assertTrue(scope["linear_cellwise_ramp_insertion_into_fixed_three_full_prefix_carrier_closed"])
        self.assertFalse(scope["direct_actual_cell_signed_rewrite_ruled_out"])
        self.assertFalse(scope["membership_sensitive_common_master_ruled_out"])
        self.assertFalse(scope["cross_epoch_or_cross_phase_payment_ruled_out"])
        self.assertFalse(scope["c058_resolved"])
        self.assertFalse(scope["question_1_resolved"])
        self.assertFalse(scope["question_2_resolved"])
        self.assertFalse(scope["prize_claim_ready"])


if __name__ == "__main__":
    unittest.main()

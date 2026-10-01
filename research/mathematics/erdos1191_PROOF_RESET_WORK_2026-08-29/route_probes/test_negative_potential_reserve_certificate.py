#!/usr/bin/env python3
"""Regression tests for the isolated negative-potential reserve no-go."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import negative_potential_reserve_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("negative_potential_reserve_certificate.json")


class NegativePotentialReserveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_golomb_fixture_has_28_differences(self) -> None:
        row = probe.reserve_fixture()
        self.assertEqual(row["difference_count"], 28)
        self.assertEqual(len(set(row["positive_differences"])), 28)
        self.assertEqual(row["current_gaps"], [6, 1, 8, 4])

    def test_02_unused_reserve_exact_rows_and_upper(self) -> None:
        row = probe.reserve_fixture()
        self.assertEqual(F(row["reserve_atanh_upper"]), F(75853397, 2099365632))
        self.assertEqual([item["distance"] for item in row["negative_lambda_rows"]], [7, 15, 12, 13])
        self.assertTrue(row["unused_equals_negative_potential"])

    def test_03_pointwise_zero_reserve_positive_prices(self) -> None:
        row = probe.pointwise_fixture()
        self.assertEqual(F(row["negative_density"]), 0)
        self.assertEqual(F(row["wave_density"]), F(1, 64))
        self.assertEqual(F(row["ordered_marginal_price"]), F(1, 32))
        self.assertEqual(F(row["coefficient_psd_price"]), F(1, 16))
        self.assertEqual(F(row["full_signless_price_attributable_to_scale"]), F(1, 16))

    def test_04_phase_allocation_replays_exactly(self) -> None:
        row = probe.phase_fixture()
        self.assertEqual(row["cumulative_owner_coefficients"], ["193/384", "11/48", "11/192"])
        self.assertEqual(row["scale_rows"][-1]["q_over_positive"], "11/15")
        self.assertEqual(row["scale_rows"][-1]["owner_coefficients_a"], ["11/48", "11/48", "11/192"])

    def test_05_phase_prices_exceed_reserve(self) -> None:
        row = probe.phase_fixture()
        reserve = F(row["phase_unused_reserve"])
        self.assertEqual(reserve, F(3, 160))
        self.assertEqual(F(row["pair_signless_total_price"]) / reserve, F(31, 2))
        self.assertEqual(F(row["terminal_diagonal_price"]) / reserve, F(101, 24))
        self.assertEqual(F(row["terminal_off_diagonal_row"]) / reserve, F(331, 96))

    def test_06_q_is_piecewise_nonincreasing(self) -> None:
        rows = probe.q_piecewise_rows()
        self.assertEqual(len(rows), 7)
        for row in rows:
            self.assertLessEqual(F(row["derivative_numerator"]), 0)

    def test_07_integrated_psd_separation(self) -> None:
        row = probe.integrated_witnesses()
        self.assertEqual(F(row["coefficient_psd_lower"]), F(2, 13))
        self.assertGreater(F(row["coefficient_psd_lower_minus_reserve_upper"]), 0)

    def test_08_integrated_pair_price_separation(self) -> None:
        row = probe.integrated_witnesses()
        self.assertEqual(F(row["pair_signless_lower"]), F(3, 32))
        self.assertGreater(F(row["pair_signless_lower_minus_reserve_upper"]), 0)

    def test_09_integrated_terminal_separation(self) -> None:
        row = probe.integrated_witnesses()
        contributions = sum(
            (F(item["rational_lower_contribution"]) for item in row["terminal_off_diagonal_lower_segments"]),
            F(0),
        )
        self.assertEqual(contributions, F(48804306505243169, 1330823143467417600))
        self.assertEqual(contributions, F(row["terminal_off_diagonal_lower"]))
        self.assertGreater(F(row["terminal_off_diagonal_lower_minus_reserve_upper"]), 0)
        self.assertTrue(row["terminal_diagonal_is_termwise_larger"])

    def test_10_asymptotic_affine_difference_groups(self) -> None:
        row = probe.asymptotic_family()
        self.assertEqual(row["separation_margins_at_L_26"], [10, 1, 26])
        self.assertTrue(row["golomb_for_every_integer_L_at_least_26"])
        points = (0, 2, 5, 16, 42, 43, 51, 103)
        self.assertEqual(len(probe.positive_differences(points)), 28)

    def test_11_asymptotic_constant_fraction_scope(self) -> None:
        row = probe.asymptotic_family()
        self.assertTrue(row["reserve_over_pair_price_tends_to_zero"])
        self.assertTrue(row["reserve_over_marginal_price_tends_to_zero"])
        self.assertTrue(row["reserve_over_coefficient_psd_price_tends_to_zero"])
        self.assertEqual(row["marginal_price_lower"], "(9/64)*log(L/9)")
        self.assertEqual(row["reserve_limit"], "(9/64)*(log(9/2)-1)")

    def test_12_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_13_mutations_and_scope_guards(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 12)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["question_1_resolved"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)
        scope = self.fixture["scope"]
        self.assertFalse(
            scope["isolated_reserve_pays_any_positive_pointwise_share_of_psd_marginal_or_pair_price"]
        )
        self.assertFalse(scope["exact_signed_negative_rows_ruled_out"])
        self.assertFalse(scope["ordered_gram_intersection_route_ruled_out"])
        self.assertFalse(scope["cross_epoch_payment_ruled_out"])
        self.assertFalse(scope["constant_fraction_of_integrated_marginal_price_proved"])
        self.assertFalse(scope["larger_master_ruled_out"])
        self.assertFalse(scope["c058_resolved"])
        self.assertFalse(scope["question_1_resolved"])
        self.assertFalse(scope["question_2_resolved"])
        self.assertFalse(scope["complete_proof"])
        self.assertFalse(scope["prize_claim_ready"])


if __name__ == "__main__":
    unittest.main()

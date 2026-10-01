from __future__ import annotations

import json
import unittest
from fractions import Fraction
from hashlib import sha256

from wave15_local_promotion_allocation_probe import (
    DEFAULT_OUTPUT,
    build_certificate,
    literal_next_bulk_coefficient,
)


class Wave15LocalPromotionAllocationProbeTests(unittest.TestCase):
    def test_literal_next_bulk_coefficient_cases(self) -> None:
        for epoch in (4, 8, 16, 32):
            right = 2 * epoch
            with self.subTest(epoch=epoch, separation=1):
                self.assertEqual(
                    literal_next_bulk_coefficient(epoch, right - 1, right),
                    Fraction(1, 4 * epoch * epoch),
                )
            with self.subTest(epoch=epoch, separation=2):
                self.assertEqual(
                    literal_next_bulk_coefficient(epoch, right - 2, right),
                    Fraction(1, 16 * epoch * epoch),
                )
            with self.subTest(epoch=epoch, separation=3):
                self.assertEqual(
                    literal_next_bulk_coefficient(epoch, right - 3, right),
                    Fraction(1, 8 * epoch * epoch),
                )

    def test_reported_hall_and_erdos_turan_calibrations(self) -> None:
        certificate = build_certificate()
        rows = certificate["fixture_rows"]
        self.assertEqual(
            [row["minimum_future_future_count"] for row in rows],
            [6, 39, 222, 15, 84, 351, 1465],
        )
        self.assertTrue(all(row["reported_calibration_matches"] for row in rows))
        self.assertTrue(all(row["thresholds_strictly_decreasing"] for row in rows))

    def test_exact_layer_cake_and_literal_bulk_capacity(self) -> None:
        for row in build_certificate()["fixture_rows"]:
            with self.subTest(fixture=row["fixture"], epoch=row["epoch"]):
                self.assertTrue(row["all_selected_differences_are_new"])
                self.assertTrue(
                    row["all_selected_differences_are_literal_next_bulk_atoms"]
                )
                self.assertTrue(row["minimum_coefficient_formula_verified"])
                self.assertTrue(row["layer_cake_identity_exact"])
                self.assertEqual(
                    row["delta"]["formal_sha256"],
                    row["layer_cake"]["formal_sha256"],
                )
                self.assertGreater(row["capacity_minus_delta_exact_sign"], 0)
                self.assertTrue(row["delta_at_most_selected_capacity_exact"])
                self.assertEqual(row["layer_atom_projection_deficit_count"], 0)

    def test_raw_log_equal_share_failure_is_kept_separate(self) -> None:
        for row in build_certificate()["fixture_rows"]:
            with self.subTest(fixture=row["fixture"], epoch=row["epoch"]):
                self.assertTrue(row["raw_equal_share_identity_exact"])
                self.assertEqual(
                    row["raw_frontier"]["formal_sha256"],
                    row["raw_equal_share"]["formal_sha256"],
                )
                self.assertLess(row["capacity_minus_raw_exact_sign"], 0)
                self.assertTrue(row["raw_total_exceeds_selected_capacity_exact"])
                self.assertTrue(row["raw_equal_share_failure_forced_exactly"])
                self.assertGreater(row["raw_equal_share_projection_failure_count"], 0)

    def test_certificate_is_deterministic_self_hashed_and_unresolved(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)

        unhashed = dict(first)
        internal_hash = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())

        self.assertEqual(
            first["scope_flags"],
            {
                "finite_fixture_only": True,
                "eventual_cap_inferred": False,
                "infinite_branch": False,
                "all_epoch_signed_allocation": False,
                "problem_unresolved": True,
            },
        )
        self.assertFalse(first["claim_boundary"]["p19_proved"])
        self.assertFalse(first["claim_boundary"]["erdos_1191_resolved"])
        self.assertFalse(first["claim_boundary"]["prize_claim_ready"])

        committed = json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(committed, first)


if __name__ == "__main__":
    unittest.main()

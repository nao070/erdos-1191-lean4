from __future__ import annotations

import json
import unittest
from fractions import Fraction
from hashlib import sha256

from wave17_residual_capacity_certificate import (
    DECIMAL_PRECISION,
    DEFAULT_OUTPUT,
    LARGE_DIFFERENCE_CUTOFF,
    SMALL_DIFFERENCE_COUNT,
    build_certificate,
    coefficient_class_audit,
    cutoff_ratio_audit,
    layer_load_cap,
    literal_coefficient,
    near_difference_count,
    near_difference_diameter_lower,
    small_value_error_log_coefficient,
    threshold_audit,
    threshold_polynomial_twice,
    triangular_floor,
)


class Wave17ResidualCapacityCertificateTests(unittest.TestCase):
    def test_h10_count_and_exact_threshold_polynomial(self) -> None:
        self.assertEqual(near_difference_count(54), 485)
        self.assertEqual(near_difference_count(55), 495)
        self.assertEqual(threshold_polynomial_twice(54), -810)
        self.assertEqual(threshold_polynomial_twice(55), 990)

        below = threshold_audit(54)
        threshold = threshold_audit(55)
        self.assertFalse(below["threshold_claim_applies"])
        self.assertFalse(below["diameter_lower_at_least_three_halves_triangular"])
        self.assertTrue(threshold["threshold_claim_applies"])
        self.assertTrue(threshold["diameter_lower_at_least_three_halves_triangular"])
        self.assertEqual(threshold["diameter_margin"], "9/2")
        self.assertEqual(
            near_difference_diameter_lower(55) - Fraction(3 * 55 * 54, 4),
            Fraction(9, 2),
        )
        for mark_count in (55, 56, 64, 128, 512, 4096):
            with self.subTest(mark_count=mark_count):
                row = threshold_audit(mark_count)
                self.assertTrue(row["near_difference_count_formula_matches"])
                self.assertTrue(row["polynomial_formula_matches_direct_margin"])
                self.assertTrue(row["diameter_lower_at_least_three_halves_triangular"])

    def test_malformed_and_boundary_inputs_are_rejected(self) -> None:
        for bad in (0, -1, True, 1.5):
            with (
                self.subTest(helper="triangular", bad=bad),
                self.assertRaises((TypeError, ValueError)),
            ):
                triangular_floor(bad)  # type: ignore[arg-type]

        for args in ((10, 10), (11, 0), (True, 1), (12, True)):
            with (
                self.subTest(helper="near_count", args=args),
                self.assertRaises((TypeError, ValueError)),
            ):
                near_difference_count(*args)

        with self.assertRaises(ValueError):
            threshold_polynomial_twice(10)
        with self.assertRaises(ValueError):
            literal_coefficient(3, 1)
        with self.assertRaises(ValueError):
            literal_coefficient(4, 0)
        with self.assertRaises(TypeError):
            literal_coefficient(4, True)

    def test_cutoff_and_exact_coefficient_ownership(self) -> None:
        self.assertEqual(LARGE_DIFFERENCE_CUTOFF, 2147)
        self.assertEqual(SMALL_DIFFERENCE_COUNT, 2146)
        self.assertEqual(triangular_floor(53), 1431)
        self.assertTrue(cutoff_ratio_audit(53)["cutoff_ratio_at_least_three_halves"])
        self.assertFalse(cutoff_ratio_audit(54)["cutoff_ratio_at_least_three_halves"])

        for epoch in (4, 8, 32):
            with self.subTest(epoch=epoch, separation=1):
                self.assertEqual(
                    literal_coefficient(epoch, 1), Fraction(1, 4 * epoch * epoch)
                )
            with self.subTest(epoch=epoch, separation=2):
                self.assertEqual(
                    literal_coefficient(epoch, 2), Fraction(1, 16 * epoch * epoch)
                )
            with self.subTest(epoch=epoch, separation=3):
                self.assertEqual(
                    literal_coefficient(epoch, 3), Fraction(1, 8 * epoch * epoch)
                )
            for separation in (1, 2, 3, 54):
                row = coefficient_class_audit(epoch, separation)
                self.assertTrue(row["literal_coefficient_dominates_minimum"])
                self.assertTrue(row["twelve_times_minimum_equals_layer_load_cap"])
            self.assertEqual(
                small_value_error_log_coefficient(epoch),
                Fraction(2146, 16 * epoch * epoch),
            )
            self.assertEqual(
                12 * Fraction(1, 16 * epoch * epoch), layer_load_cap(epoch)
            )

    def test_fixture_atom_ownership_and_exact_load_caps(self) -> None:
        rows = build_certificate()["fixture_rows"]
        self.assertEqual(
            [row["selected_atom_count"] for row in rows],
            [15, 66, 382, 35, 209, 928, 3896],
        )
        self.assertEqual(
            [row["selected_small_atom_count"] for row in rows],
            [15, 66, 146, 27, 56, 117, 236],
        )
        self.assertEqual(
            [row["selected_large_atom_count"] for row in rows],
            [0, 0, 236, 8, 153, 811, 3660],
        )
        self.assertEqual(
            [row["minimum_large_ratio_cleared_margin"] for row in rows],
            [None, None, 4246, 4274, 4306, 4288, 4270],
        )
        self.assertEqual(
            [row["selected_atom_rows_sha256"] for row in rows],
            [
                "4fe185a284cceac82f74fa49c881b82fb7dca0b457cc69c2fc7c8db986ce1fea",
                "baa17fa457adc663ae1afde239415f6cbbbac2cd1cafd084b75db3fabf36cbfe",
                "a985c7ce35c9257da5e735e03c31ad869a056ad8f6494542ece202a3e6494270",
                "fdc8081026e0a8e3f9dae1ef701846b8f4ec12a7c2a5616177042bfac1c941e3",
                "87e06631d549053b9cfd26d4d6df401e294d9a529a41a0767a103848b2caf28b",
                "b8d7b395096a0acd021d680a8e6649103a52118154b19fc1fec07201a6f19d11",
                "e38451e258c9aea8b835eb60b2fedbcfb91a5fc8bf4857f025642bbd25adff8a",
            ],
        )
        for row in rows:
            with self.subTest(fixture=row["fixture"], epoch=row["epoch"]):
                self.assertTrue(row["global_golomb_prefix_verified"])
                self.assertTrue(row["small_atom_count_at_most_global_cutoff_count"])
                self.assertTrue(row["all_load_uppers_below_cap"])
                self.assertTrue(row["all_selected_atoms_are_literal_next_gothic_atoms"])
                self.assertTrue(row["all_selected_atoms_satisfy_triangular_floor"])
                self.assertTrue(row["all_large_atoms_have_three_halves_residual_ratio"])
                self.assertTrue(row["all_coefficients_dominate_conservative_minimum"])
                self.assertLess(
                    Fraction(row["maximum_exact_load_upper"]),
                    Fraction(row["conservative_layer_load_cap"]),
                )

    def test_decimal_values_are_projection_only(self) -> None:
        certificate = build_certificate()
        self.assertEqual(certificate["decimal_display"]["precision"], 80)
        self.assertTrue(certificate["decimal_display"]["projection_only"])
        for row in certificate["fixture_rows"]:
            with self.subTest(fixture=row["fixture"], epoch=row["epoch"]):
                self.assertEqual(row["decimal_projection_precision"], DECIMAL_PRECISION)
                self.assertTrue(row["transcendental_projection_only"])
                self.assertTrue(row["projected_local_inequality_holds"])

    def test_certificate_replays_is_self_hashed_and_keeps_scope(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        self.assertTrue(first["all_exact_checks_pass"])

        unhashed = dict(first)
        internal_hash = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())

        scope = first["scope_flags"]
        self.assertTrue(scope["certificate_finite_and_algebraic_only"])
        self.assertTrue(
            scope["local_p21_inequality_proved_analytically_by_accompanying_derivation"]
        )
        self.assertFalse(scope["finite_fixtures_promoted_to_infinite_branch"])
        self.assertFalse(scope["p19_proved"])
        self.assertFalse(scope["question_1_resolved"])
        self.assertFalse(scope["question_2_resolved"])
        self.assertFalse(scope["erdos_1191_resolved"])
        self.assertFalse(scope["prize_claim_ready"])
        self.assertTrue(scope["problem_unresolved"])

        committed = json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(committed, first)


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import unittest
from fractions import Fraction

from wave6_forbidden_shadow import (
    difference_residues,
    erdos_turan_ruler,
    endpoint_ratio_error,
    extension_is_golomb,
    extension_shadow_criterion,
    finite_audit,
    forbidden_shadow,
    innovation_q00_per_modulus,
    interval_shadow_bound,
    is_golomb,
    positive_differences,
    profile_grid_error,
    residue_lift,
    shadow_residues,
    lifted_endpoint_ratio_bound,
    lifted_profile_grid_bound,
)


class ForbiddenShadowTests(unittest.TestCase):
    def test_residue_lift_is_golomb_with_exact_taxonomy(self) -> None:
        for prime, count in ((5, 4), (7, 6), (11, 9)):
            base = erdos_turan_ruler(prime, count)
            for dilation in (3, 5, 8):
                lifted = residue_lift(base, dilation)
                self.assertTrue(is_golomb(lifted))
                self.assertEqual(
                    len(set(positive_differences(lifted))),
                    len(lifted) * (len(lifted) - 1) // 2,
                )
                self.assertTrue(
                    set(difference_residues(lifted, dilation))
                    <= {0, 1, dilation - 1}
                )

    def test_shadow_residue_confinement_and_interval_bound(self) -> None:
        lifted = residue_lift(erdos_turan_ruler(13, 10), 7)
        expected_residues = {0, 1, 2, 6}
        self.assertTrue(set(shadow_residues(lifted, 7)) <= expected_residues)

        shadow = forbidden_shadow(lifted)
        for lower in range(0, 2 * lifted[-1], 17):
            for length in (1, 7, 19, 51):
                actual = sum(lower <= value < lower + length for value in shadow)
                self.assertLessEqual(actual, interval_shadow_bound(length, 7))

    def test_shadow_criterion_is_exact_for_every_nearby_candidate(self) -> None:
        for prime, count, dilation in ((5, 4, 3), (7, 6, 5), (11, 8, 7)):
            lifted = residue_lift(erdos_turan_ruler(prime, count), dilation)
            diameter = lifted[-1]
            for candidate in range(diameter + 1, 2 * diameter + 1):
                self.assertEqual(
                    extension_is_golomb(lifted, candidate),
                    extension_shadow_criterion(lifted, candidate),
                )

    def test_compatible_prefixes_and_exact_innovations(self) -> None:
        prime = 67
        dilation = 9
        lifted = residue_lift(erdos_turan_ruler(prime, 63), dilation)
        self.assertTrue(is_golomb(lifted))
        values = []
        for old_count in (4, 8, 16, 32):
            prefix = lifted[: 2 * old_count]
            self.assertTrue(is_golomb(prefix))
            self.assertLessEqual(
                profile_grid_error(lifted[:old_count]),
                lifted_profile_grid_bound(old_count, prime, dilation),
            )
            self.assertLessEqual(
                endpoint_ratio_error(lifted, old_count),
                lifted_endpoint_ratio_bound(old_count, prime, dilation),
            )
            value = innovation_q00_per_modulus(lifted, old_count)
            self.assertIsInstance(value, Fraction)
            values.append(value)
        self.assertTrue(all(value > 0 for value in values))

    def test_finite_audit(self) -> None:
        payload = finite_audit()
        self.assertTrue(payload["golomb"])
        self.assertEqual(payload["difference_count"], 16 * 15 // 2)
        self.assertLessEqual(
            payload["next_interval_shadow_count"],
            payload["next_interval_shadow_upper_bound"],
        )


if __name__ == "__main__":
    unittest.main()

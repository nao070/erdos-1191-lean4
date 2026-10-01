from __future__ import annotations

import unittest
from fractions import Fraction

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave13_new_birth_barrier_probe import (
    _barrier_passes,
    build_certificate,
    derived_frontier_spectrum,
    direct_frontier_form,
    exhaustive_eight_mark_audit,
    frontier_formula_spectrum,
    independent_layered_audit,
    spectrum_form,
)


class Wave13NewBirthBarrierProbeTests(unittest.TestCase):
    def test_closed_frontier_formula_matches_independent_expansion(self) -> None:
        expected_term_counts = {4: 22, 8: 92, 16: 376, 32: 1520, 64: 6112}
        for m, term_count in expected_term_counts.items():
            with self.subTest(m=m):
                derived = derived_frontier_spectrum(m)
                self.assertEqual(derived, frontier_formula_spectrum(m))
                self.assertEqual(len(derived), term_count)
                self.assertEqual(sum(derived.values(), Fraction(0)), 0)
                positive_mass = sum(
                    (
                        coefficient
                        for coefficient in derived.values()
                        if coefficient > 0
                    ),
                    Fraction(0),
                )
                self.assertEqual(
                    positive_mass,
                    Fraction(24 * m * m - 52 * m + 31, 16 * m * m),
                )

    def test_frontier_spectrum_has_the_claimed_special_coefficients(self) -> None:
        for m in (4, 8, 16, 32):
            with self.subTest(m=m):
                spectrum = derived_frontier_spectrum(m)
                frontier = 2 * m - 1
                self.assertEqual(
                    spectrum[(1, frontier)],
                    Fraction(-(12 * m * m - 28 * m + 15), 16 * m * m),
                )
                self.assertEqual(
                    spectrum[(2 * m - 2, frontier)], Fraction(11, 16 * m * m)
                )
                self.assertEqual(
                    spectrum[(2 * m - 1, frontier)], Fraction(-1, 4 * m * m)
                )

    def test_spectrum_form_matches_independent_tail_telescope(self) -> None:
        fixtures = (
            (tuple(COUNTEREXAMPLE_64_POINTS), (4, 8, 16, 32)),
            (erdos_turan_ruler(128, 257), (4, 8, 16, 32, 64)),
        )
        for points, epochs in fixtures:
            for m in epochs:
                with self.subTest(point_count=len(points), m=m):
                    spectrum = derived_frontier_spectrum(m)
                    self.assertEqual(
                        spectrum_form(points, spectrum),
                        direct_frontier_form(points, m),
                    )

    def test_layered_oracle_matches_canonical_obstruction(self) -> None:
        fixtures = (
            (tuple(COUNTEREXAMPLE_64_POINTS), (4, 8, 16, 32)),
            (erdos_turan_ruler(128, 257), (4, 8, 16, 32, 64)),
        )
        for points, epochs in fixtures:
            for m in epochs:
                with self.subTest(point_count=len(points), m=m):
                    audit = independent_layered_audit(points, m)
                    self.assertTrue(_barrier_passes(audit))
                    self.assertTrue(audit.canonical_oracle_matches)
                    self.assertEqual(
                        audit.layered_floor,
                        m * (m - 2) * (m * m + 8 * m + 6) // 48,
                    )

    def test_complete_eight_mark_scope(self) -> None:
        result = exhaustive_eight_mark_audit()
        self.assertEqual(result["all_bounded_rulers"]["candidate_count"], 1468)
        self.assertEqual(result["all_bounded_rulers"]["failure_count"], 0)
        self.assertEqual(result["all_prefix_C1_subset"]["candidate_count"], 1146)
        self.assertEqual(result["all_prefix_C1_subset"]["failure_count"], 0)

    def test_certificate_is_deterministic_and_preserves_claim_boundary(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        self.assertTrue(
            first["claim_boundary"]["frontier_spectrum_coefficientwise_exact"]
        )
        self.assertFalse(first["claim_boundary"]["p18_sublog_upper_proved"])
        self.assertFalse(first["claim_boundary"]["erdos_1191_resolved"])
        self.assertFalse(first["claim_boundary"]["prize_claim_ready"])


if __name__ == "__main__":
    unittest.main()

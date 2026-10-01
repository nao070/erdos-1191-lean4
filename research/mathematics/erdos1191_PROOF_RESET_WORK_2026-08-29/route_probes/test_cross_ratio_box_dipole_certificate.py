#!/usr/bin/env python3
"""Regression tests for the exact cross-ratio/box-dipole certificate."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import cross_ratio_box_dipole_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("cross_ratio_box_dipole_certificate.json")


class CrossRatioBoxDipoleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_tent_positivity_support_and_factor(self) -> None:
        for middle in range(1, 20):
            for h in range(1, 8):
                for k in range(1, 8):
                    for width in range(1, middle + h + k + 3):
                        value = probe.psi(width, middle, h, k)
                        self.assertEqual(value, probe.psi_piecewise(width, middle, h, k))
                        self.assertEqual(value, -probe.edge_inner_product(width, middle, h, k))
                        self.assertGreaterEqual(value, 0)

    def test_02_formal_integral_is_cross_ratio_log(self) -> None:
        for row in ((4, 1, 2), (7, 3, 5), (31, 1, 2)):
            middle, h, k = row
            form = probe.integral_psi_form(*row)
            self.assertEqual(form.constant, 0)
            self.assertEqual(dict(form.logs), {middle: F(-1), middle + h: F(1), middle + k: F(1), middle + h + k: F(-1)})

    def test_03_lambda_formula_epochs(self) -> None:
        for epoch in probe.EPOCHS:
            row = probe.lambda_audit(epoch)
            self.assertEqual(F(row["maximum_other_positive"]), F(1, epoch * epoch))
            self.assertEqual(F(row["full_span_coefficient"]), F((epoch - 1) ** 2, 4 * epoch * epoch))

    def test_03b_finite_horizon_potential_decomposition(self) -> None:
        for epoch in probe.EPOCHS:
            lambda_sum, gap_loads = probe.symbolic_lambda_moments(epoch)
            self.assertEqual(lambda_sum, 0)
            self.assertTrue(all(value == 0 for value in gap_loads))
            row = probe.potential_decomposition_audit(epoch)
            self.assertTrue(row["all_symbolic_gap_loads_zero"])
            self.assertTrue(row["other_positive_strict_Gothic_interior"])
            self.assertTrue(row["terminal_nonfull_all_nonpositive"])
            self.assertEqual(row["potential_rational_constant"], "0")
            self.assertEqual(row["potential_log_digest"], row["W_log_digest"])
        self.assertEqual(probe.finite_horizon_potential(17, 17), probe.FormalIntegral(()))
        self.assertEqual(probe.finite_horizon_potential(18, 17), probe.FormalIntegral(()))
        self.assertEqual(
            probe.finite_horizon_potential(5, 17),
            probe.FormalIntegral.from_parts(((17, 1), (5, -1)), F(5, 17) - 1),
        )
        contract = self.fixture["finite_horizon_potential"]
        self.assertIn("p<=q", contract["identity"])
        self.assertIn("D_(p,q)", contract["identity"])
        self.assertIn("a_q-a_(p-1)", contract["moment_cancellation"])

    def test_04_sharpened_pointwise_map_brute_T(self) -> None:
        fixtures = ((probe.MINIMAL_EIGHT, 4), (probe.HALL_64[:16], 8))
        for marks, epoch in fixtures:
            span = marks[-1] - marks[epoch - 1]
            for width in range(1, span + 3):
                row = probe.pointwise_map_check(marks, epoch, width)
                self.assertLessEqual(F(row["Psi"]), F(row["upper"]))

    def test_05_full_span_boundary_cases(self) -> None:
        marks, epoch = probe.MINIMAL_EIGHT, 4
        span = marks[-1] - marks[epoch - 1]
        self.assertEqual(probe.r_box(span, span), 0)
        self.assertEqual(probe.psi_wave(marks, epoch, span), 0)
        self.assertEqual(probe.psi_wave(marks, epoch, span + 1), 0)

    def test_06_scheduled_scale_no_go(self) -> None:
        self.assertEqual(probe.scheduled_width(probe.MINIMAL_EIGHT), 64)
        self.assertEqual(probe.psi_wave(probe.MINIMAL_EIGHT, 4, 64), 0)
        self.assertGreater(probe.centered_suffix_capacity(probe.MINIMAL_EIGHT, 4, 64), 0)

    def test_07_dyadic_lower_and_upper_no_go(self) -> None:
        self.assertEqual(probe.dyadic_sum_atom(4, 1, 2), 0)
        for exponent in range(3, 16):
            width = 1 << exponent
            self.assertEqual(probe.dyadic_sum_atom(width - 1, 1, 2), F(1, width))
            self.assertGreater(F((width - 1) * (width + 2), 2 * width), F(width - 1, 2))

    def test_08_phase_partition_reindex(self) -> None:
        for row in ((4, 1, 2), (7, 3, 5), (31, 1, 2), (20, 9, 4)):
            audit = probe.phase_partition_audit(*row)
            self.assertTrue(audit["partition_contiguous"])
            self.assertEqual(audit["rational_constant"], "0")

    def test_09_hall_negative_X_exact(self) -> None:
        hall8 = probe.hall_no_go(8)
        hall32 = probe.hall_no_go(32)
        self.assertEqual(hall8["X_first_use"]["2"], "-5105/524288")
        self.assertEqual(hall8["W_form_sha256"], "45475c2b57a01fe0f0c8ab7e4a2516a13638f33b988595420095df390e0e78b7")
        self.assertEqual(hall32["X_first_use"]["4"], "-2351661/134217728")
        self.assertEqual(hall32["W_form_sha256"], "87d57cf7f7d4270df3b2880b73aec13a0946c68290670fd67be8391670648240")

    def test_10_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_11_mutations_rejected(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 12)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["prize_claim_ready"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)

    def test_12_open_scope_flags(self) -> None:
        scope = self.fixture["scope"]
        self.assertFalse(scope["common_signed_history_coupling"])
        self.assertFalse(scope["q1_resolved"])
        self.assertFalse(scope["q2_resolved"])
        self.assertFalse(scope["prize_claim_ready"])


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import wave19_p28_full_row_ownership_certificate as certificate


class Wave19P28FullRowOwnershipCertificateTests(unittest.TestCase):
    def test_full_row_formulas_and_u_equals_v_plus_bar_r(self) -> None:
        for epoch in certificate.AUDIT_EPOCHS:
            for source in range(2, 2 * epoch - 1):
                with self.subTest(epoch=epoch, source=source):
                    self.assertEqual(
                        certificate.row_mass(epoch, source),
                        certificate.closed_row_mass(epoch, source),
                    )
                    self.assertEqual(
                        certificate.allocation_alpha(epoch, source, "u"),
                        certificate.closed_u_alpha(epoch, source),
                    )
                    self.assertEqual(
                        certificate.allocation_alpha(epoch, source, "bar"),
                        certificate.closed_bar_alpha(epoch, source),
                    )
                    self.assertEqual(
                        certificate.terminal_coefficient(epoch, source),
                        certificate.cut_coefficient(epoch, source)
                        + certificate.residual_coefficient(epoch, source),
                    )

    def test_beta_rectangles_equal_wave12_finite_coefficients(self) -> None:
        for epoch in certificate.AUDIT_EPOCHS:
            unit = certificate.coefficient_map(epoch, "unit")
            expected_count = (epoch - 1) * (3 * epoch - 4) // 2
            self.assertEqual(len(unit), expected_count)
            for cell, coefficient in unit.items():
                with self.subTest(epoch=epoch, cell=cell):
                    self.assertEqual(
                        coefficient,
                        certificate.closed_zfin_coefficient(epoch, *cell),
                    )

    def test_exact_epoch_enumerations(self) -> None:
        expected = {
            4: (
                "275/2688",
                "7/64",
                "275/294",
                "-19/2688",
                0,
            ),
            5: (
                "2239/25200",
                "9/100",
                "2239/2268",
                "-29/25200",
                0,
            ),
            6: (
                "2771/35640",
                "11/144",
                "5542/5445",
                "97/71280",
                2,
            ),
            8: (
                "43061/698880",
                "15/256",
                "43061/40950",
                "2111/698880",
                4,
            ),
            16: (
                "913969/27617280",
                "31/1024",
                "913969/836070",
                "77899/27617280",
                26,
            ),
            32: (
                "16665449/975937536",
                "63/4096",
                "16665449/15010758",
                "1654691/975937536",
                130,
            ),
            64: (
                "56796101/6554419200",
                "127/16384",
                "56796101/50806350",
                "5989751/6554419200",
                559,
            ),
        }
        for epoch, values in expected.items():
            with self.subTest(epoch=epoch):
                row = certificate.epoch_audit(epoch)
                self.assertEqual(row["global_worst_cell"], [1, epoch + 1])
                self.assertEqual(row["global_worst_u_coefficient"], values[0])
                self.assertEqual(row["global_worst_zfin_coefficient"], values[1])
                self.assertEqual(row["global_worst_ratio"], values[2])
                self.assertEqual(row["global_worst_excess"], values[3])
                self.assertEqual(row["u_allocation_violation_count"], values[4])
                self.assertTrue(row["all_exact_checks_pass"])

    def test_global_worst_formula_and_minimum_failure(self) -> None:
        self.assertLess(certificate.failure_polynomial(4), 0)
        self.assertLess(certificate.failure_polynomial(5), 0)
        for epoch in range(6, 129):
            with self.subTest(epoch=epoch):
                self.assertEqual(
                    certificate.failure_polynomial(epoch),
                    certificate.shifted_failure_polynomial(epoch - 6),
                )
                self.assertGreater(certificate.failure_polynomial(epoch), 0)
                numerator = certificate.worst_ratio_numerator(epoch)
                denominator = 4 * (epoch - 1) * (2 * epoch - 3) * (2 * epoch - 1) ** 2
                self.assertEqual(
                    certificate.worst_ratio_closed(epoch),
                    Fraction(numerator, denominator),
                )
                worst = certificate.worst_ratio_closed(epoch)
                self.assertGreater(worst, Fraction(3, 4))
                self.assertGreater(
                    worst,
                    certificate.first_late_column_increment(epoch),
                )
                self.assertLess(
                    certificate.gap_one_transition_increment(epoch),
                    Fraction(3, 4),
                )
                for short_length in range(3, epoch):
                    self.assertLess(
                        certificate.interior_late_column_increment(short_length),
                        Fraction(3, 4),
                    )
        self.assertLess(Fraction(207, 280), Fraction(3, 4))

    def test_inner_u_allocation_never_exceeds_W(self) -> None:
        expected = {
            4: "11/16",
            5: "11/16",
            6: "25/36",
            8: "37/52",
            16: "85/116",
            32: "181/244",
            64: "373/500",
        }
        for epoch, maximum in expected.items():
            with self.subTest(epoch=epoch):
                row = certificate.epoch_audit(epoch)
                self.assertEqual(row["inner_u_max_ratio"], maximum)
                self.assertEqual(
                    Fraction(maximum), certificate.expected_inner_u_maximum(epoch)
                )
                self.assertTrue(row["inner_u_strictly_below_three_quarters"])

    def test_cut_valid_bar_allocation_bounds_and_remaining_half_W(self) -> None:
        for epoch in certificate.AUDIT_EPOCHS:
            with self.subTest(epoch=epoch):
                row = certificate.epoch_audit(epoch)
                self.assertTrue(row["bar_rows_respect_capacity"])
                self.assertEqual(row["inner_bar_row_minimum"], "3/10")
                self.assertEqual(row["inner_bar_endpoint"], "3/8")
                self.assertEqual(row["inner_bar_min_ratio"], "3/10")
                self.assertEqual(
                    Fraction(row["inner_bar_max_ratio"]),
                    certificate.expected_inner_bar_maximum(epoch),
                )
                self.assertTrue(row["inner_bar_coefficient_at_least_three_tenths"])
                self.assertTrue(row["inner_bar_coefficient_strictly_below_one_half"])
                self.assertTrue(row["at_least_half_of_W_remains"])

    def test_short_row_endpoint_payment_boundary_has_rational_exp_bound(self) -> None:
        upper = certificate.rational_exp_upper(Fraction(5, 2))
        self.assertLess(upper, 13)
        for epoch in range(7, 129):
            with self.subTest(epoch=epoch):
                c_over_endpoint_length_floor = Fraction(
                    (epoch - 1) * (3 * epoch - 4), 6
                )
                self.assertGreater(c_over_endpoint_length_floor, 13)
        audit = certificate.universal_audit()
        self.assertTrue(audit["short_row_tau_can_be_negative_from_n7"])
        self.assertTrue(audit["row_exact_Delta_bound_valid_for_arbitrary_real_tau"])
        self.assertFalse(audit["unshifted_endpoint_payment_extends_to_negative_tau"])
        self.assertFalse(
            audit["old_four_channel_E0_plus_S_minus_J_certified_nonnegative"]
        )
        self.assertTrue(
            audit["new_short_row_shift_payment_required_for_this_extension"]
        )

    def test_certificate_hash_scope_and_two_run_byte_replay(self) -> None:
        payload = certificate.build_certificate()
        self.assertTrue(certificate.verify_certificate_hash(payload))
        self.assertEqual(payload["audit_counts"]["pytest_tests"], 8)
        self.assertEqual(payload["audit_counts"]["total_exact_subtests"], 21009)
        flags = payload["scope_flags"]
        self.assertTrue(flags["full_u_allocation_fails"])
        self.assertFalse(flags["full_u_allocation_respects_row_ownership"])
        self.assertTrue(flags["bar_allocation_preserves_negative_cut_ownership"])
        self.assertFalse(flags["bar_allocation_proves_p28"])
        self.assertFalse(flags["p28_proved"])
        self.assertFalse(flags["p28_refuted"])
        self.assertFalse(flags["question_1_resolved"])
        self.assertTrue(flags["problem_unresolved"])

        script = Path(certificate.__file__).resolve()
        checked = certificate.DEFAULT_OUTPUT.read_bytes()
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.json"
            second = Path(directory) / "second.json"
            for output in (first, second):
                subprocess.run(
                    [sys.executable, str(script), "--output", str(output)],
                    check=True,
                )
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(first.read_bytes(), checked)
            replay_payload = json.loads(first.read_text())
            self.assertTrue(certificate.verify_certificate_hash(replay_payload))


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from decimal import Decimal
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

import wave17_local_rank_surplus_certificate as certificate


class Wave17LocalRankSurplusCertificateTests(unittest.TestCase):
    def test_exact_weight_counts_and_cumulative_ranks(self) -> None:
        expected = {
            3: (2, 1, 3, 5),
            4: (3, 6, 9, 12),
            16: (15, 300, 315, 330),
        }
        for epoch, values in expected.items():
            with self.subTest(epoch=epoch):
                row = certificate.coefficient_audit(epoch)
                self.assertEqual(
                    (
                        row["high_count"],
                        row["middle_count"],
                        row["cumulative_b"],
                        row["cumulative_c"],
                    ),
                    values,
                )
                self.assertTrue(row["all_exact_checks_pass"])

        row = certificate.coefficient_audit(16)
        self.assertEqual(row["high_mass"], "15/256")
        self.assertEqual(row["middle_mass"], "75/128")
        self.assertEqual(row["low_mass"], "15/1024")
        self.assertEqual(row["total_mass"], "675/1024")
        self.assertEqual(
            row["factorial_numerator_exponents"],
            {"a_factorial": 2, "b_factorial": 1, "c_factorial": 1},
        )
        for epoch in range(3, 129):
            with self.subTest(exact_epoch=epoch):
                self.assertTrue(
                    certificate.coefficient_audit(epoch)["all_exact_checks_pass"]
                )

    def test_strong_error_bound_implies_the_weak_bound_exactly(self) -> None:
        self.assertTrue(
            hasattr(certificate, "analytic_bound_implication_audit"),
            "analytic-bound implication audit is not implemented",
        )
        audit = certificate.analytic_bound_implication_audit
        for epoch in (16, 17, 128, 2**20, 2**22):
            with self.subTest(epoch=epoch):
                row = audit(epoch)
                self.assertEqual(
                    Fraction(row["strong_prefactor_squared"]),
                    Fraction(324, epoch * epoch),
                )
                self.assertEqual(
                    Fraction(row["weak_prefactor_squared"]),
                    Fraction(400, epoch),
                )
                self.assertEqual(row["cleared_nonnegative_margin"], 400 * epoch - 324)
                self.assertTrue(row["strong_bound_implies_weak_bound"])

    def test_weak_majorant_is_monotone_from_sixteen(self) -> None:
        self.assertTrue(
            hasattr(certificate, "weak_majorant_monotonicity_audit"),
            "weak-majorant monotonicity audit is not implemented",
        )
        row = certificate.weak_majorant_monotonicity_audit(16)
        self.assertEqual(row["minimum_epoch"], 16)
        self.assertEqual(row["derivative_formula"], "10*(1-log(x))/x^(3/2)")
        self.assertTrue(row["three_is_a_strict_upper_bound_for_e"])
        self.assertTrue(row["minimum_epoch_exceeds_e"])
        self.assertTrue(row["derivative_strictly_negative_on_domain"])
        self.assertTrue(row["weak_majorant_strictly_decreasing"])

    def test_eighty_digit_threshold_projections(self) -> None:
        self.assertTrue(
            hasattr(certificate, "threshold_projection"),
            "threshold projection is not implemented",
        )
        rows = (
            certificate.threshold_projection(2**20, Fraction(81, 128)),
            certificate.threshold_projection(2**22, Fraction(3, 4)),
        )
        self.assertEqual([row["threshold"] for row in rows], ["81/128", "3/4"])
        self.assertTrue(
            rows[0]["weak_lower_bound"].startswith("0.64737298797496301322")
        )
        self.assertTrue(
            rows[1]["weak_lower_bound"].startswith("0.77898089080776589964")
        )
        for row in rows:
            with self.subTest(epoch=row["epoch"]):
                self.assertEqual(row["decimal_precision"], 80)
                self.assertEqual(
                    len(Decimal(row["weak_lower_bound"]).as_tuple().digits), 80
                )
                threshold = Fraction(row["threshold"])
                lower = Decimal(row["weak_lower_bound"])
                threshold_decimal = Decimal(threshold.numerator) / Decimal(
                    threshold.denominator
                )
                self.assertGreater(lower, threshold_decimal)
                self.assertTrue(row["strict_threshold_conclusion"])
                self.assertTrue(row["transcendental_projection_only"])

    def test_malformed_inputs_are_rejected(self) -> None:
        for bad in (True, 3.0, "3", None):
            with (
                self.subTest(helper="coefficient", bad=bad),
                self.assertRaises(TypeError),
            ):
                certificate.coefficient_audit(bad)  # type: ignore[arg-type]
        for bad in (-10, 0, 1, 2):
            with (
                self.subTest(helper="coefficient", bad=bad),
                self.assertRaises(ValueError),
            ):
                certificate.coefficient_audit(bad)

        self.assertTrue(hasattr(certificate, "analytic_bound_implication_audit"))
        self.assertTrue(hasattr(certificate, "weak_majorant_monotonicity_audit"))
        self.assertTrue(hasattr(certificate, "threshold_projection"))
        for helper in (
            certificate.analytic_bound_implication_audit,
            certificate.weak_majorant_monotonicity_audit,
        ):
            for bad in (True, 16.0, "16"):
                with (
                    self.subTest(helper=helper.__name__, bad=bad),
                    self.assertRaises(TypeError),
                ):
                    helper(bad)  # type: ignore[arg-type]
            with (
                self.subTest(helper=helper.__name__, bad=15),
                self.assertRaises(ValueError),
            ):
                helper(15)

        with self.assertRaises(ValueError):
            certificate.threshold_projection(15, Fraction(1, 2))
        for bad_threshold in (True, 0.5, "1/2"):
            with (
                self.subTest(threshold=bad_threshold),
                self.assertRaises(TypeError),
            ):
                certificate.threshold_projection(
                    16,
                    bad_threshold,  # type: ignore[arg-type]
                )
        for bad_threshold in (Fraction(0), Fraction(-1, 2)):
            with (
                self.subTest(threshold=bad_threshold),
                self.assertRaises(ValueError),
            ):
                certificate.threshold_projection(16, bad_threshold)

    def test_certificate_is_self_hashed_and_scope_is_narrow(self) -> None:
        self.assertTrue(
            hasattr(certificate, "build_certificate"),
            "certificate builder is not implemented",
        )
        first = certificate.build_certificate()
        self.assertEqual(first, certificate.build_certificate())
        self.assertTrue(first["all_required_checks_pass"])

        unhashed = dict(first)
        internal_hash = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())

        self.assertEqual(
            first["scope_flags"],
            {
                "finite_algebraic_only": True,
                "analytic_error_proved_in_memo": True,
                "decimal_thresholds_are_projections_not_proofs": True,
                "p19_proved": False,
                "p22_proved": False,
                "question_1_resolved": False,
                "question_2_resolved": False,
                "erdos_1191_resolved": False,
                "prize_claim_ready": False,
                "problem_unresolved": True,
            },
        )
        for row in first["direct_convergence_projections"]:
            self.assertTrue(row["projection_only"])
            self.assertFalse(row["used_as_proof"])

    def test_cli_byte_replay_matches_the_committed_certificate(self) -> None:
        self.assertTrue(hasattr(certificate, "DEFAULT_OUTPUT"))
        script = Path(__file__).with_name("wave17_local_rank_surplus_certificate.py")
        with tempfile.TemporaryDirectory() as temporary_directory:
            outputs = [
                Path(temporary_directory) / name
                for name in ("first.json", "second.json")
            ]
            for output in outputs:
                completed = subprocess.run(
                    [sys.executable, str(script), "--output", str(output)],
                    cwd=script.parent,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(outputs[0].read_bytes(), outputs[1].read_bytes())
            self.assertTrue(
                certificate.DEFAULT_OUTPUT.exists(),
                "committed certificate has not been generated",
            )
            self.assertEqual(
                outputs[0].read_bytes(), certificate.DEFAULT_OUTPUT.read_bytes()
            )


if __name__ == "__main__":
    unittest.main()

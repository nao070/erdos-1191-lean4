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

import wave18_excess_birth_locality_certificate as certificate


class Wave18ExcessBirthLocalityCertificateTests(unittest.TestCase):
    def test_three_beta_classes_and_complete_atom_count(self) -> None:
        self.assertEqual(certificate.beta_coefficient(4, 4, 4), Fraction(1, 16))
        self.assertEqual(certificate.beta_coefficient(4, 3, 4), Fraction(1, 64))
        self.assertEqual(certificate.beta_coefficient(4, 2, 4), Fraction(1, 32))

        self.assertTrue(hasattr(certificate, "coefficient_ledger_audit"))
        row = certificate.coefficient_ledger_audit(4)
        self.assertEqual(row["high_count"], 3)
        self.assertEqual(row["middle_count"], 6)
        self.assertEqual(row["low_count"], 3)
        self.assertEqual(row["atom_count"], 12)
        self.assertEqual(row["closed_atom_count"], 12)
        self.assertEqual(row["total_coefficient_mass"], "27/64")
        self.assertTrue(row["all_exact_checks_pass"])

    def test_source_masses_and_residual_domination(self) -> None:
        self.assertTrue(hasattr(certificate, "source_mass_audit"))
        self.assertTrue(hasattr(certificate, "residual_coefficient"))
        expected = {
            2: ("3/32", Fraction(9, 128)),
            3: ("5/64", Fraction(7, 128)),
            4: ("7/64", Fraction(5, 128)),
        }
        for source, (weight, residual) in expected.items():
            with self.subTest(source=source):
                row = certificate.source_mass_audit(4, source)
                self.assertEqual(row["direct_source_mass"], weight)
                self.assertEqual(row["closed_source_mass"], weight)
                self.assertEqual(certificate.residual_coefficient(4, source), residual)
                self.assertTrue(row["source_mass_formula_verified"])
                self.assertTrue(row["source_mass_dominates_residual"])

        for epoch in range(3, 65):
            for source in range(2, epoch + 1):
                with self.subTest(epoch=epoch, source=source):
                    self.assertTrue(
                        certificate.source_mass_audit(epoch, source)[
                            "all_exact_checks_pass"
                        ]
                    )

    def test_general_cap_residual_mass_is_below_fifteen_sixteenths(self) -> None:
        self.assertTrue(hasattr(certificate, "residual_mass_audit"))
        row = certificate.residual_mass_audit(4, Fraction(5, 2))
        self.assertEqual(row["direct_residual_mass"], "21/128")
        self.assertEqual(row["closed_residual_mass"], "21/128")
        self.assertEqual(row["capped_residual_mass"], "105/256")
        self.assertTrue(row["residual_mass_below_three_eighths"])
        self.assertTrue(row["capped_residual_below_fifteen_sixteenths"])
        for epoch in (3, 4, 8, 16, 64, 1024):
            with self.subTest(epoch=epoch):
                self.assertTrue(
                    certificate.residual_mass_audit(epoch, Fraction(5, 2))[
                        "all_exact_checks_pass"
                    ]
                )

    def test_strong_rank_surplus_projection_clears_cap(self) -> None:
        self.assertTrue(hasattr(certificate, "rank_surplus_threshold_audit"))
        row = certificate.rank_surplus_threshold_audit(2**22, Fraction(15, 16))
        self.assertEqual(row["decimal_precision"], 80)
        self.assertTrue(row["strong_lower_bound"].startswith("0.93759512121707246847"))
        self.assertTrue(
            row["strict_threshold_margin"].startswith("0.00009512121707246847")
        )
        self.assertTrue(row["strong_error_majorant_strictly_decreasing"])
        self.assertTrue(row["strict_threshold_conclusion"])
        self.assertTrue(row["extends_to_all_larger_epochs"])
        self.assertTrue(row["transcendental_projection_only"])
        self.assertEqual(len(Decimal(row["strong_lower_bound"]).as_tuple().digits), 80)

    def test_rank_layer_pre_log_sums_and_dyadic_geometric_factor(self) -> None:
        self.assertTrue(hasattr(certificate, "rank_layer_load_audit"))
        expected = {
            3: ("1/72", "7/216"),
            4: ("293/26880", "37/1920"),
            8: ("369637/92252160", "237371/46126080"),
        }
        for epoch, values in expected.items():
            with self.subTest(epoch=epoch):
                row = certificate.rank_layer_load_audit(epoch, Fraction(5, 2))
                self.assertIn("exact_rational_pre_log_upper_sum", row)
                self.assertEqual(row["exact_rational_pre_log_upper_sum"], values[0])
                self.assertEqual(row["harmonic_proxy_pre_log"], values[1])
                self.assertTrue(row["all_rank_lower_bounds_verified"])
                self.assertTrue(row["exact_sum_below_harmonic_proxy"])
                self.assertTrue(row["projected_source_load_below_claimed_bound"])
                self.assertTrue(row["transcendental_projection_only"])

        self.assertTrue(hasattr(certificate, "dyadic_load_audit"))
        dyadic = certificate.dyadic_load_audit(4, 6, Fraction(5, 2))
        self.assertEqual(dyadic["partial_geometric_pre_log"], "1365/32768")
        self.assertEqual(dyadic["infinite_geometric_pre_log"], "1/24")
        self.assertEqual(dyadic["exact_geometric_tail"], "1/98304")
        self.assertTrue(dyadic["geometric_identity_verified"])
        self.assertTrue(dyadic["partial_sum_below_all_source_bound"])
        self.assertTrue(dyadic["transcendental_projection_only"])

    def test_erdos_turan_rows_are_exact_finite_calibrations(self) -> None:
        self.assertTrue(hasattr(certificate, "erdos_turan_points"))
        self.assertEqual(
            certificate.erdos_turan_points(5),
            (0, 11, 24, 34, 41),
        )
        self.assertTrue(hasattr(certificate, "erdos_turan_local_slack_audit"))
        small = certificate.erdos_turan_local_slack_audit(5)
        self.assertEqual(small["epoch"], 3)
        self.assertEqual(small["atom_count"], 5)
        self.assertEqual(small["exact_scaled_product_bit_length"], 43)
        self.assertEqual(
            small["exact_scaled_product_sha256"],
            "40ae05038d6b7bec51cad050b68d9c4e2241b9790a91f869dd28e7afb95fa1ea",
        )

        for prime in (5, 7, 11, 31, 61, 127, 257):
            with self.subTest(prime=prime):
                row = certificate.erdos_turan_local_slack_audit(prime)
                self.assertTrue(row["ordinary_golomb_uniqueness_verified"])
                self.assertTrue(row["diameter_below_eight_n_squared"])
                self.assertTrue(row["atom_count_formula_verified"])
                self.assertTrue(row["interior_atom_values_distinct"])
                self.assertGreater(Decimal(row["local_slack_H_decimal"]), 0)
                self.assertLess(Decimal(row["local_slack_H_decimal"]), Decimal("1.2"))
                self.assertTrue(row["bounded_local_slack_projection"])
                self.assertTrue(row["finite_calibration_only"])
                self.assertFalse(row["infinite_family_conclusion_inferred"])
                self.assertLess(row["float_decimal_H_absolute_error"], 1e-12)

    def test_malformed_inputs_are_rejected(self) -> None:
        for bad in (True, 4.0, "4", None):
            with (
                self.subTest(helper="beta", bad=bad),
                self.assertRaises(TypeError),
            ):
                certificate.beta_coefficient(bad, 2, 3)  # type: ignore[arg-type]
        for args in ((2, 2, 2), (4, 1, 4), (4, 5, 4), (4, 2, 3), (4, 2, 7)):
            with (
                self.subTest(helper="beta", args=args),
                self.assertRaises(ValueError),
            ):
                certificate.beta_coefficient(*args)

        self.assertTrue(hasattr(certificate, "source_mass_audit"))
        for source in (1, 5):
            with self.assertRaises(ValueError):
                certificate.source_mass_audit(4, source)
        with self.assertRaises(TypeError):
            certificate.source_mass_audit(4, True)

        self.assertTrue(hasattr(certificate, "residual_mass_audit"))
        with self.assertRaises(TypeError):
            certificate.residual_mass_audit(4, 2.5)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            certificate.residual_mass_audit(4, Fraction(0))

        self.assertTrue(hasattr(certificate, "rank_surplus_threshold_audit"))
        with self.assertRaises(ValueError):
            certificate.rank_surplus_threshold_audit(15, Fraction(15, 16))
        with self.assertRaises(TypeError):
            certificate.rank_surplus_threshold_audit(16, 0.5)  # type: ignore[arg-type]

        self.assertTrue(hasattr(certificate, "dyadic_load_audit"))
        for args in ((2, 6), (4, 0), (4, True)):
            with self.assertRaises((TypeError, ValueError)):
                certificate.dyadic_load_audit(*args, cap=Fraction(5, 2))

        self.assertTrue(hasattr(certificate, "erdos_turan_points"))
        for bad in (True, 3.0, "5"):
            with self.assertRaises(TypeError):
                certificate.erdos_turan_points(bad)  # type: ignore[arg-type]
        for bad in (2, 3, 4, 9, 21):
            with self.assertRaises(ValueError):
                certificate.erdos_turan_points(bad)

    def test_certificate_is_self_hashed_and_scope_is_narrow(self) -> None:
        self.assertTrue(hasattr(certificate, "build_certificate"))
        first = certificate.build_certificate()
        self.assertEqual(first, certificate.build_certificate())
        self.assertTrue(first["all_required_checks_pass"])
        self.assertEqual(
            [row["prime"] for row in first["erdos_turan_calibration_rows"]],
            [5, 7, 11, 31, 61, 127, 257],
        )

        unhashed = dict(first)
        internal_hash = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())
        self.assertEqual(
            first["scope_flags"],
            {
                "finite_algebraic_only": True,
                "analytic_rank_surplus_bound_proved_in_memo": True,
                "transcendental_values_projection_only": True,
                "erdos_turan_rows_finite_calibration_only": True,
                "analytic_infinite_family_no_go_proved_in_memo": True,
                "infinite_family_no_go_reproved_here": False,
                "p19_proved": False,
                "p22_proved": False,
                "question_1_resolved": False,
                "question_2_resolved": False,
                "erdos_1191_resolved": False,
                "prize_claim_ready": False,
                "problem_unresolved": True,
            },
        )

    def test_cli_byte_replay_matches_committed_certificate(self) -> None:
        self.assertTrue(hasattr(certificate, "DEFAULT_OUTPUT"))
        script = Path(__file__).with_name("wave18_excess_birth_locality_certificate.py")
        with tempfile.TemporaryDirectory() as temporary_directory:
            outputs = [
                Path(temporary_directory) / name for name in ("one.json", "two.json")
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
                "committed Wave18 certificate has not been generated",
            )
            self.assertEqual(
                outputs[0].read_bytes(), certificate.DEFAULT_OUTPUT.read_bytes()
            )


if __name__ == "__main__":
    unittest.main()

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

import wave19_cross_ratio_half_absorption_certificate as certificate


class Wave19CrossRatioHalfAbsorptionCertificateTests(unittest.TestCase):
    def test_wave18_weights_residuals_and_alphas_are_exact(self) -> None:
        self.assertEqual(certificate.beta_coefficient(4, 4, 4), Fraction(1, 16))
        self.assertEqual(certificate.beta_coefficient(4, 3, 4), Fraction(1, 64))
        self.assertEqual(certificate.beta_coefficient(4, 2, 4), Fraction(1, 32))

        expected = {
            2: (Fraction(3, 32), Fraction(9, 128), Fraction(3, 4)),
            3: (Fraction(5, 64), Fraction(7, 128), Fraction(7, 10)),
            4: (Fraction(7, 64), Fraction(5, 128), Fraction(5, 14)),
        }
        for source, (weight, residual, alpha) in expected.items():
            with self.subTest(source=source):
                self.assertEqual(certificate.source_weight(4, source), weight)
                self.assertEqual(certificate.closed_source_weight(4, source), weight)
                self.assertEqual(certificate.residual_coefficient(4, source), residual)
                self.assertEqual(certificate.alpha_coefficient(4, source), alpha)
                self.assertEqual(certificate.closed_alpha_coefficient(4, source), alpha)

        row = certificate.weight_alpha_audit(4)
        self.assertEqual(row["total_source_weight"], "9/32")
        self.assertEqual(row["closed_total_source_weight"], "9/32")
        self.assertEqual(row["Rcoef"], "21/128")
        self.assertTrue(row["all_exact_checks_pass"])
        for epoch in range(4, 65):
            with self.subTest(epoch=epoch):
                self.assertTrue(
                    certificate.weight_alpha_audit(epoch)["all_exact_checks_pass"]
                )

    def test_direct_coefficients_match_all_four_analytic_cases(self) -> None:
        expected = {
            (3, 5): ("corner_x1_y1", Fraction(5, 224)),
            (3, 6): ("source_edge_x1", Fraction(25, 896)),
            (2, 5): ("target_edge_y1", Fraction(149, 4480)),
            (2, 6): ("interior_xge2_yge2", Fraction(17, 280)),
        }
        for (left_gap, right_gap), (case, value) in expected.items():
            with self.subTest(left_gap=left_gap, right_gap=right_gap):
                row = certificate.coefficient_case_audit(4, left_gap, right_gap)
                self.assertEqual(row["analytic_case"], case)
                self.assertEqual(
                    certificate.direct_cross_ratio_coefficient(4, left_gap, right_gap),
                    value,
                )
                self.assertEqual(
                    certificate.analytic_cross_ratio_coefficient(
                        4, left_gap, right_gap
                    ),
                    value,
                )
                self.assertEqual(row["direct_coefficient"], f"{value}")
                self.assertTrue(row["direct_matches_analytic"])
                self.assertTrue(row["strict_half_absorption"])

        for epoch in range(4, 21):
            for left_gap in range(1, epoch):
                for right_gap in range(epoch + 1, 2 * epoch):
                    with self.subTest(
                        epoch=epoch, left_gap=left_gap, right_gap=right_gap
                    ):
                        row = certificate.coefficient_case_audit(
                            epoch, left_gap, right_gap
                        )
                        self.assertTrue(row["all_exact_checks_pass"])

    def test_coefficient_masses_and_half_y_mass_have_closed_forms(self) -> None:
        expected = {
            4: ("339/560", "39/32", "21/128"),
            5: ("28601/25200", "11/5", "1/5"),
        }
        for epoch, (mass, half_y_mass, residual_mass) in expected.items():
            with self.subTest(epoch=epoch):
                row = certificate.coefficient_mass_audit(epoch)
                self.assertEqual(row["direct_cross_ratio_coefficient_mass"], mass)
                self.assertEqual(row["rearranged_coefficient_mass"], mass)
                self.assertEqual(row["closed_cross_ratio_coefficient_mass"], mass)
                self.assertEqual(row["closed_half_Y_coefficient_mass"], half_y_mass)
                self.assertEqual(row["Rcoef"], residual_mass)
                self.assertTrue(row["all_exact_checks_pass"])

        for epoch in range(4, 33):
            with self.subTest(epoch=epoch):
                self.assertTrue(
                    certificate.coefficient_mass_audit(epoch)["all_exact_checks_pass"]
                )

    def test_max_ratio_is_the_corner_and_increases_to_one(self) -> None:
        row_four = certificate.max_ratio_audit(4)
        self.assertEqual(row_four["maximizer_xy"], [1, 1])
        self.assertEqual(row_four["maximum_ratio"], "5/7")
        self.assertEqual(row_four["maximum_noncorner_ratio"], "7/12")
        self.assertEqual(row_four["maximum_noncorner_xy"], [3, 3])

        for epoch in range(4, 65):
            with self.subTest(epoch=epoch):
                row = certificate.max_ratio_audit(epoch)
                expected = Fraction(2 * epoch - 3, 2 * epoch - 1)
                self.assertEqual(Fraction(row["maximum_ratio"]), expected)
                self.assertEqual(row["maximizer_xy"], [1, 1])
                self.assertTrue(row["unique_maximizer"])
                self.assertEqual(
                    Fraction(row["deficit_from_one"]), Fraction(2, 2 * epoch - 1)
                )
                self.assertEqual(
                    Fraction(row["increase_to_next_epoch"]),
                    Fraction(4, (2 * epoch - 1) * (2 * epoch + 1)),
                )
                self.assertTrue(row["all_exact_checks_pass"])

    def test_universal_four_case_proof_closes_every_edge(self) -> None:
        row = certificate.universal_proof_audit()
        self.assertEqual(row["minimum_epoch"], 4)
        self.assertEqual(
            row["four_analytic_cases"],
            ["x=1,y=1", "x=1,y>=2", "x>=2,y=1", "x>=2,y>=2"],
        )
        self.assertEqual(row["corner_ratio"], "(2n-3)/(2n-1)")
        self.assertEqual(row["corner_deficit_from_one"], "2/(2n-1)")
        self.assertEqual(row["n4_exact_noncorner_max"], "7/12")
        self.assertTrue(row["four_case_partition_complete"])
        self.assertTrue(row["all_four_cases_below_rectangle_majorant"])
        self.assertTrue(row["rectangle_to_half_Y_by_square_identity"])
        self.assertTrue(row["noncorner_three_eighths_bound"])
        self.assertTrue(row["corner_is_global_max"])
        self.assertTrue(row["all_symbolic_checks_pass"])

    def test_endpoint_lambda_has_three_exact_cases(self) -> None:
        self.assertEqual(certificate.bulk_alpha_sum(4), Fraction(3, 4))
        self.assertEqual(certificate.closed_bulk_alpha_sum(4), Fraction(3, 4))
        expected = {
            4: (
                "q_equals_n",
                Fraction(127, 2240),
                Fraction(7, 64),
                Fraction(227, 8960),
            ),
            5: (
                "q_equals_n_plus_one",
                Fraction(57, 1120),
                Fraction(9, 64),
                Fraction(489, 8960),
            ),
            6: (
                "bulk_q_at_least_n_plus_two",
                Fraction(253, 4480),
                Fraction(11, 64),
                Fraction(649, 8960),
            ),
        }
        for target, (case, lam, prefix_coefficient, margin) in expected.items():
            with self.subTest(target=target):
                row = certificate.endpoint_case_audit(4, target)
                self.assertEqual(row["analytic_case"], case)
                self.assertEqual(certificate.endpoint_lambda(4, target), lam)
                self.assertEqual(certificate.closed_endpoint_lambda(4, target), lam)
                self.assertEqual(
                    certificate.endpoint_prefix_coefficient(4, target),
                    prefix_coefficient,
                )
                self.assertEqual(Fraction(row["three_quarters_margin"]), margin)
                self.assertTrue(row["lambda_below_three_quarters_c"])
                self.assertTrue(row["all_exact_checks_pass"])

        for epoch in range(4, 65):
            with self.subTest(epoch=epoch):
                self.assertEqual(
                    certificate.bulk_alpha_sum(epoch),
                    Fraction(3 * (epoch - 3), 4),
                )
                row = certificate.endpoint_boundary_audit(epoch)
                self.assertEqual(
                    Fraction(row["bulk_alpha_sum"]), Fraction(3 * (epoch - 3), 4)
                )
                self.assertTrue(row["all_exact_checks_pass"])

    def test_endpoint_mass_and_universal_boundary_proof(self) -> None:
        row = certificate.endpoint_boundary_audit(4)
        self.assertEqual(row["lambda_mass"], "21/128")
        self.assertEqual(row["Rcoef"], "21/128")
        self.assertEqual(row["Pmass"], "27/64")
        self.assertEqual(row["Fcoef"], "95/256")
        self.assertEqual(row["Pmass_minus_Fcoef"], "13/256")
        self.assertTrue(row["all_three_q_cases_present"])

        proof = certificate.endpoint_universal_proof_audit()
        self.assertEqual(
            proof["three_q_cases"],
            ["q=n", "q=n+1", "q>=n+2"],
        )
        self.assertEqual(proof["bulk_alpha_sum"], "3(n-3)/4")
        self.assertEqual(proof["Pmass"], "3(n-1)^2/(4n^2)")
        self.assertEqual(proof["Pmass_minus_Fcoef"], "(4n-3)/(16n^2)")
        self.assertTrue(proof["all_three_case_margins_positive_for_n_ge_4"])
        self.assertTrue(proof["endpoint_profile_absorption_proved"])
        self.assertTrue(proof["signed_quarter_deficit_identity_verified"])
        self.assertTrue(proof["all_symbolic_checks_pass"])

    def test_numerical_realization_on_deterministic_golomb_fixtures(self) -> None:
        self.assertEqual(certificate.erdos_turan_points(11)[:5], (0, 23, 48, 75, 93))
        self.assertEqual(
            certificate.binary_superincreasing_points(8),
            (0, 1, 3, 7, 15, 31, 63, 127),
        )

        fixtures = (
            ("erdos_turan_p11_n4", certificate.erdos_turan_points(11), 4, "21/128"),
            ("erdos_turan_p17_n8", certificate.erdos_turan_points(17), 8, "133/512"),
            (
                "binary_superincreasing_n4",
                certificate.binary_superincreasing_points(8),
                4,
                "21/128",
            ),
        )
        rows = []
        for name, points, epoch, residual_mass in fixtures:
            with self.subTest(fixture=name):
                row = certificate.numerical_realization_audit(
                    name, points, epoch, Fraction(5, 2)
                )
                rows.append(row)
                self.assertEqual(row["h"], "5/2")
                self.assertEqual(row["Rcoef"], residual_mass)
                self.assertTrue(row["golomb_verified"])
                self.assertTrue(row["c_over_L_strictly_below_three"])
                self.assertTrue(row["exact_double_telescope_verified"])
                self.assertTrue(row["direct_J_below_reduced_J"])
                self.assertTrue(row["reduced_J_below_cross_ratio_plus_terminal"])
                self.assertTrue(row["cross_ratio_load_below_supported_Y_half"])
                self.assertTrue(row["supported_Y_below_full_Y"])
                self.assertTrue(row["claimed_half_absorption_bound_verified"])
                self.assertTrue(row["endpoint_Erow_below_E0"])
                self.assertTrue(
                    row["endpoint_E0_below_three_quarters_boundary_deficit"]
                )
                self.assertTrue(row["prefix_minus_full_span_identity_verified"])
                self.assertTrue(row["signed_endpoint_boundary_cancellation_verified"])
                self.assertGreaterEqual(
                    Decimal(row["claimed_bound_margin_decimal"]), Decimal(0)
                )
                self.assertTrue(row["finite_fixture_only"])

        self.assertEqual(rows[0]["direct_J_h_decimal"], "0")
        self.assertEqual(rows[0]["terminal_excess_decimal"], "0")
        self.assertGreater(Decimal(rows[2]["direct_J_h_decimal"]), Decimal(0))
        self.assertGreater(Decimal(rows[2]["terminal_excess_decimal"]), Decimal(0))
        self.assertEqual(rows[0]["Pmass"], "27/64")
        self.assertEqual(rows[0]["Fcoef"], "95/256")
        self.assertEqual(rows[0]["Pmass_minus_Fcoef"], "13/256")
        self.assertGreater(Decimal(rows[0]["boundary_deficit_decimal"]), Decimal(0))
        self.assertGreater(Decimal(rows[0]["epsilon_decimal"]), Decimal(0))

    def test_malformed_inputs_are_rejected(self) -> None:
        for bad in (True, 4.0, "4", None):
            with self.assertRaises(TypeError):
                certificate.weight_alpha_audit(bad)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            certificate.weight_alpha_audit(3)

        for source in (1, 5):
            with self.assertRaises(ValueError):
                certificate.source_weight(4, source)
        with self.assertRaises(TypeError):
            certificate.source_weight(4, True)

        for pair in ((0, 5), (4, 5), (3, 4), (3, 8)):
            with self.assertRaises(ValueError):
                certificate.direct_cross_ratio_coefficient(4, *pair)
        with self.assertRaises(TypeError):
            certificate.direct_cross_ratio_coefficient(4, True, 5)

        for bad in (True, 11.0, "11"):
            with self.assertRaises(TypeError):
                certificate.erdos_turan_points(bad)  # type: ignore[arg-type]
        for bad in (2, 9, 15):
            with self.assertRaises(ValueError):
                certificate.erdos_turan_points(bad)

        with self.assertRaises(ValueError):
            certificate.numerical_realization_audit(
                "too-short", (0, 1, 3, 7), 4, Fraction(5, 2)
            )
        with self.assertRaises(ValueError):
            certificate.numerical_realization_audit(
                "not-golomb", (0, 1, 2, 4, 8, 16, 32, 64), 4, Fraction(5, 2)
            )
        with self.assertRaises(TypeError):
            certificate.numerical_realization_audit(
                "bad-h", certificate.binary_superincreasing_points(8), 4, 2.5
            )

    def test_certificate_is_self_hashed_and_scope_is_narrow(self) -> None:
        first = certificate.build_certificate()
        self.assertEqual(first, certificate.build_certificate())
        self.assertEqual(
            first["schema"], "erdos1191.wave19.cross-ratio-half-absorption.v1"
        )
        self.assertTrue(first["all_required_checks_pass"])
        self.assertEqual(
            [row["fixture"] for row in first["numerical_fixture_rows"]],
            [
                "erdos_turan_p11_n4",
                "erdos_turan_p17_n8",
                "erdos_turan_p37_n16",
                "binary_superincreasing_n4",
            ],
        )

        unhashed = dict(first)
        internal_hash = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())
        self.assertEqual(
            first["scope_flags"],
            {
                "cross_ratio_coefficient_theorem_proved_for_all_n_ge_4": True,
                "wave18_J_bound_realized_on_finite_fixtures": True,
                "transcendental_values_are_decimal_projections": True,
                "finite_fixtures_promoted_to_infinite_branch": False,
                "p23_proved": False,
                "question_1_resolved": False,
                "question_2_resolved": False,
                "erdos_1191_resolved": False,
                "prize_claim_ready": False,
                "problem_unresolved": True,
            },
        )

    def test_cli_byte_replay_matches_committed_certificate(self) -> None:
        script = Path(__file__).with_name(
            "wave19_cross_ratio_half_absorption_certificate.py"
        )
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
                "committed Wave19 certificate has not been generated",
            )
            self.assertEqual(
                outputs[0].read_bytes(), certificate.DEFAULT_OUTPUT.read_bytes()
            )


if __name__ == "__main__":
    unittest.main()

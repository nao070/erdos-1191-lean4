from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

import wave19_p28_transport_residual_floor_certificate as certificate


class Wave19P28TransportResidualFloorCertificateTests(unittest.TestCase):
    def test_input_domain_is_dyadic_n_at_least_64(self) -> None:
        for invalid in (0, 32, 63, 65, 96):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                certificate.epoch_audit(invalid)
        with self.assertRaises(TypeError):
            certificate.epoch_audit(True)

    def test_beta_cells_and_exceptional_row_are_exact(self) -> None:
        for epoch in certificate.EXACT_EPOCHS:
            with self.subTest(epoch=epoch):
                square = epoch * epoch
                self.assertEqual(
                    certificate.beta_coefficient(epoch, epoch + 1, epoch + 1),
                    Fraction(1, square),
                )
                self.assertEqual(
                    certificate.beta_coefficient(epoch, epoch + 1, epoch + 2),
                    Fraction(1, 4 * square),
                )
                self.assertEqual(
                    certificate.beta_coefficient(epoch, epoch + 1, epoch + 3),
                    Fraction(1, 2 * square),
                )
                last = 2 * epoch - 2
                self.assertEqual(
                    certificate.residual_row_mass(epoch, last),
                    Fraction(3, 8 * square),
                )
                self.assertEqual(
                    certificate.residual_row_upper(epoch, last),
                    Fraction(1, 2 * square),
                )
                row = certificate.row_sum_audit(epoch)
                self.assertEqual(row["row_checks"], epoch - 2)
                self.assertEqual(
                    row["exceptional_upper_minus_demand"], f"1/{8 * square}"
                )
                self.assertTrue(row["all_row_bounds_verified"])

    def test_every_beta_rectangle_is_represented_and_exact(self) -> None:
        expected_counts = {64: 1953, 128: 8001, 256: 32385}
        for epoch, expected_count in expected_counts.items():
            with self.subTest(epoch=epoch):
                row = certificate.rectangle_capacity_audit(epoch)
                self.assertEqual(
                    row["pointwise_inner_pair_checks_represented"], expected_count
                )
                self.assertEqual(
                    row["expected_pointwise_inner_pair_count"], expected_count
                )
                self.assertTrue(row["all_rectangle_capacities_verified"])
                for distance in (2, epoch // 2, epoch - 1):
                    self.assertEqual(
                        certificate.rectangle_beta_capacity_by_distance(
                            epoch, distance
                        ),
                        Fraction(distance * distance, 4 * epoch * epoch),
                    )

    def test_left_greedy_is_an_exact_feasible_transport(self) -> None:
        expected_cells = {64: 1953, 128: 8001, 256: 32385}
        for epoch, cells in expected_cells.items():
            with self.subTest(epoch=epoch):
                row = certificate.feasible_transport_audit(epoch)
                self.assertEqual(row["transport_cells_checked"], cells)
                self.assertEqual(row["row_sums_checked"], epoch - 2)
                self.assertTrue(row["all_cell_capacities_verified"])
                self.assertTrue(row["all_row_sums_verified"])
                self.assertTrue(row["feasible_set_nonempty"])

    def test_good_partner_family_has_the_required_uniform_residual(self) -> None:
        expected_directed = {64: 64, 128: 256, 256: 1024}
        for epoch, directed in expected_directed.items():
            with self.subTest(epoch=epoch):
                row = certificate.good_partner_audit(epoch)
                self.assertEqual(row["vertices_checked"], epoch)
                self.assertEqual(row["partners_per_vertex"], epoch // 64)
                self.assertEqual(row["directed_partner_checks"], directed)
                self.assertGreaterEqual(
                    row["minimum_partner_distance"], 7 * epoch // 64
                )
                self.assertEqual(row["coarse_residual_coefficient"], "1/2048")
                self.assertTrue(row["all_partner_checks_verified"])

                for vertex in range(epoch, 2 * epoch):
                    partners = certificate.good_partners(epoch, vertex)
                    self.assertEqual(len(partners), epoch // 64)
                    for partner in partners:
                        left, right = sorted((vertex, partner))
                        weight = certificate.inner_weight(epoch, left, right)
                        covered = certificate.row_sum_rectangle_upper(
                            epoch, left, right
                        )
                        self.assertGreaterEqual(weight - covered, Fraction(1, 2048))

    def test_distinct_gap_and_symmetrization_constants_are_exact(self) -> None:
        expected_coefficients = {64: "1/8192", 128: "1/2048", 256: "1/512"}
        for epoch, expected in expected_coefficients.items():
            with self.subTest(epoch=epoch):
                row = certificate.symmetrization_audit(epoch)
                count = epoch // 64
                self.assertEqual(
                    row["least_sum_of_distinct_positive_integer_partner_gaps"],
                    count * (count + 1) // 2,
                )
                self.assertEqual(
                    row["symmetrized_product_floor_coefficient_of_Hprime"],
                    expected,
                )
                self.assertEqual(
                    row["residual_energy_floor"],
                    "Eres>=n^2/(2^25*Hprime)",
                )
                self.assertTrue(row["all_symmetrization_checks_verified"])

    def test_corner_has_transport_independent_one_third_coverage(self) -> None:
        for epoch in certificate.EXACT_EPOCHS:
            with self.subTest(epoch=epoch):
                row = certificate.corner_audit(epoch)
                self.assertEqual(row["coverage_ratio"], "1/3")
                self.assertTrue(row["coverage_ratio_is_one_third"])
                self.assertTrue(
                    row["uniform_coefficient_coverage_above_one_third_impossible"]
                )
                transport = certificate.left_greedy_transport(epoch)
                left, right = row["cell"]
                self.assertEqual(
                    certificate.transport_rectangle_coefficient(
                        epoch, left, right, transport
                    ),
                    Fraction(3, 4 * epoch * epoch),
                )

    def test_energy_correlated_left_greedy_nesting_is_exact(self) -> None:
        expected_checks = {64: 1891, 128: 7875, 256: 32131}
        for epoch, checks in expected_checks.items():
            with self.subTest(epoch=epoch):
                row = certificate.payoff_nesting_audit(epoch)
                self.assertEqual(row["adjacent_target_nesting_checks"], checks)
                self.assertTrue(row["payoff_is_nonincreasing_in_q"])
                self.assertTrue(
                    row["left_greedy_maximizes_each_row_for_fixed_nonnegative_C"]
                )
                self.assertFalse(
                    row["energy_correlated_transport_evades_universal_floor"]
                )

    def test_payload_separates_theorem_from_open_signed_cut_obligation(self) -> None:
        payload = certificate.build_certificate()
        self.assertTrue(payload["all_required_checks_pass"])
        self.assertEqual(
            payload["theorem_contract"]["residual_energy_floor"],
            "Eres_n(t)>=n^2/(2^25*Hprime_n)",
        )
        scope = payload["scope_flags"]
        self.assertTrue(scope["arbitrary_feasible_transport_residual_floor_proved"])
        self.assertTrue(scope["energy_correlated_transport_covered"])
        for claim in (
            "negative_whole_cut_payment_proved",
            "terminal_potential_payment_proved",
            "p28_proved",
            "question_1_resolved",
            "question_2_resolved",
            "infinite_branch_constructed",
            "publication_novelty_established",
            "prize_claim_supported",
        ):
            self.assertFalse(scope[claim])
        self.assertFalse(
            payload["cut_ownership_boundary"]["raw_v_fan_may_be_extracted_and_reused"]
        )

        content = dict(payload)
        recorded_hash = content.pop("payload_sha256")
        self.assertEqual(recorded_hash, certificate._canonical_hash(content))

    def test_cli_replay_is_byte_deterministic(self) -> None:
        script = Path(certificate.__file__).resolve()
        with tempfile.TemporaryDirectory() as temporary:
            first = Path(temporary) / "first.json"
            second = Path(temporary) / "second.json"
            for output in (first, second):
                subprocess.run(
                    [sys.executable, str(script), "--output", str(output)],
                    check=True,
                    capture_output=True,
                    text=True,
                )
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(
                sha256(first.read_bytes()).hexdigest(),
                sha256(second.read_bytes()).hexdigest(),
            )
            subprocess.run(
                [sys.executable, str(script), "--output", str(first), "--check"],
                check=True,
                capture_output=True,
                text=True,
            )
            payload = json.loads(first.read_text(encoding="utf-8"))
            self.assertTrue(payload["all_required_checks_pass"])


if __name__ == "__main__":
    unittest.main()

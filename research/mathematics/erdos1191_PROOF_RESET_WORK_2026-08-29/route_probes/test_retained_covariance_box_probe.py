#!/usr/bin/env python3
"""Deterministic exact tests for the finite retained-covariance box probe."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import random
import unittest

import retained_covariance_box_probe as probe


FIXTURE = Path(__file__).resolve().with_name("retained_covariance_box_certificate.json")


class RetainedCovarianceBoxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_kernel_normalization_and_exact_dyadic_split(self) -> None:
        for width in range(1, 8):
            narrow = probe.box_kernel(width)
            wide = probe.box_kernel(2 * width)
            shifted = (F(0),) * width + narrow
            padded = narrow + (F(0),) * width
            self.assertEqual(sum(narrow), 1)
            self.assertEqual(sum(wide), 1)
            self.assertEqual(wide, tuple((x + y) / 2 for x, y in zip(padded, shifted)))
            self.assertEqual(probe.haar_kernel(width), tuple(x - y for x, y in zip(padded, wide)))

    def test_02_exact_haar_correlation_formula(self) -> None:
        for width in range(1, 8):
            haar = probe.haar_kernel(width)
            for shift in range(0, 2 * width + 3):
                self.assertEqual(probe.correlation(haar, shift), probe.haar_correlation_formula(width, shift))

    def test_03_random_and_ruler_dyadic_energy_identity(self) -> None:
        rng = random.Random(1191)
        samples = [(0,), (0, 1, 3, 7), (0, 1, 4, 9, 11)]
        for _ in range(20):
            samples.append(tuple(sorted(rng.sample(range(20), rng.randrange(1, 7)))) )
        for sample in samples:
            for width in (1, 2, 3, 4, 8):
                self.assertEqual(probe.verify_dyadic_box_identity(sample, width), probe.covariance_v_direct(sample, width))

    def test_04_finite_telescoping_and_infinite_tail_bound(self) -> None:
        for ruler in ((0,), (0, 1, 3, 7), (0, 1, 4, 9, 11)):
            profile = probe.telescoping_profile(ruler, 5)
            self.assertEqual(F(profile["partial_plus_tail"]), len(ruler))
            tail_width = profile["tail_width"]
            # ||1_A*K_L||_2^2 <= ||1_A||_1^2 ||K_L||_2^2 = |A|^2/L.
            self.assertLessEqual(F(profile["tail_energy"]), F(len(ruler) ** 2, tail_width))
            self.assertEqual(F(profile["centered_partial_sum"]), F(profile["centered_terminal_identity"]))
            self.assertLessEqual(F(profile["centered_partial_sum"]), 0)

    def test_05_ambient_range_off_by_one(self) -> None:
        ambient_length, width = 5, 3
        cover, site_count = probe.boundary_matrix(ambient_length, width)
        self.assertEqual(site_count, ambient_length + 2 * width - 1)
        self.assertEqual(2 * site_count, len(cover[0]))
        simple = probe.simple_gamma_cover(ambient_length, width)
        self.assertEqual(probe.cover_values(cover, simple), (F(1),) * ambient_length)
        truncated = simple[:-2] + (F(0), F(0))
        values = probe.cover_values(cover, truncated)
        self.assertEqual(values[-1], 1 - F(1, 4 * width))
        self.assertLess(values[-1], 1)

    def test_06_exact_boundary_qp_kkt(self) -> None:
        for theta in (F(0), F(1, 8)):
            result = probe.solve_boundary_qp(5, 2, theta)
            cover, site_count = probe.boundary_matrix(5, 2)
            probe.validate_qp(cover, site_count, probe.covariance_matrix(theta), result)
            self.assertEqual(result["objective"], result["dual_value"])

    def test_07_same_fixed_cover_G_identity(self) -> None:
        cache: dict[tuple[object, ...], dict[str, object]] = {}
        ruler = (0, 1, 3, 7)
        for kind in probe.COVER_KINDS:
            record = probe.evaluate_pattern(ruler, 1, F(1, 8), kind, cache)
            b_d, q_value = F(record["B_D"]), F(record["Q"])
            kappa, upper = F(record["kappa"]), F(record["U_D"])
            covariance, gain = F(record["V"]), F(record["G"])
            b_h = b_d + kappa * q_value
            self.assertEqual(gain, b_d * upper - b_h * (upper - F(1, 8) * covariance))
        simple = probe.evaluate_pattern(ruler, 1, F(1, 8), "simple_gamma", cache)
        self.assertEqual(F(simple["Q"]), 0)
        self.assertGreater(F(simple["G"]), 0)

    def test_08_exhaustive_scope_and_sign_counts(self) -> None:
        enumeration = self.fixture["enumeration"]
        self.assertEqual(enumeration["ruler_counts"], {"2": 1, "3": 44, "4": 112, "5": 18})
        self.assertEqual(enumeration["total_rulers"], 175)
        self.assertEqual(enumeration["records_per_cover"], 2100)
        expected = {
            "simple_gamma": {"positive": 2100, "zero": 0, "negative": 0},
            "D_optimal": {"positive": 1368, "zero": 0, "negative": 732},
            "H_optimal": {"positive": 2086, "zero": 0, "negative": 14},
        }
        self.assertEqual({key: value["sign_counts"] for key, value in self.fixture["cover_summaries"].items()}, expected)
        self.assertTrue(
            all(value["combined_correlation_gate_pass_count"] == 2100 for value in self.fixture["cover_summaries"].values())
        )

    def test_09_concrete_nonanticipating_rule_falsification(self) -> None:
        rules = self.fixture["dyadic_nonanticipating_rules"]
        d_rule = rules["D_optimal"]
        self.assertEqual(d_rule["chain_count"], 112)
        self.assertEqual(d_rule["all_positive_chain_count"], 0)
        failure = d_rule["lexicographically_first_failure"]
        self.assertEqual(failure["ruler"], [0, 1, 3, 7])
        self.assertEqual([row["G"] for row in failure["prefix_records"]], ["-1/8", "-13/98", "280961/277207"])
        self.assertEqual(rules["simple_gamma"]["all_positive_chain_count"], 112)
        self.assertEqual(rules["H_optimal"]["all_positive_chain_count"], 112)

    def test_10_dyadic_energy_distribution_fixture(self) -> None:
        representative = self.fixture["dyadic_energy_distribution"]["representative_chain"]
        self.assertEqual(representative["ruler"], [0, 1, 3, 7])
        self.assertEqual(representative["prefixes"][2]["V"], ["3/2", "3/4", "15/32", "59/128"])
        self.assertEqual(representative["prefixes"][2]["tail_energy"], "105/128")
        self.assertEqual(representative["prefixes"][2]["partial_plus_tail"], "4")

    def test_11_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_12_hash_and_scope_mutations_rejected(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 11)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["q2_resolved"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)
        bad_hash = copy.deepcopy(self.fixture)
        bad_hash["payload_sha256"] = "f" * 64
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(bad_hash)

    def test_13_shift_normalization_and_PD_mutations_rejected(self) -> None:
        with self.assertRaises(probe.CertificateError):
            probe.haar_kernel(4, shift=5)
        with self.assertRaises(probe.CertificateError):
            probe.covariance_matrix(F(1, 4))
        malformed = tuple(2 * value for value in probe.haar_kernel(3))
        self.assertNotEqual(probe.correlation(malformed, 0), probe.haar_correlation_formula(3, 0))

    def test_14_centered_per_lag_telescope(self) -> None:
        for max_power in range(0, 7):
            terminal_width = 1 << (max_power + 1)
            for shift in range(1, 2 * terminal_width + 3):
                expected = -F(max(terminal_width - shift, 0), terminal_width * terminal_width)
                self.assertEqual(probe.lag_wavelet_partial_sum(shift, max_power), expected)
        ruler = (0, 1, 3, 7)
        values = [probe.covariance_v_direct(ruler, 1 << power) for power in range(4)]
        correct = sum((value - F(len(ruler), 2 * (1 << power)) for power, value in enumerate(values)), F(0))
        wrong_normalization = sum((value - F(len(ruler), 1 << power) for power, value in enumerate(values)), F(0))
        self.assertNotEqual(correct, wrong_normalization)

    def test_15_golomb_lower_bound_and_T_equals_k_rule(self) -> None:
        for ruler in probe.normalized_golomb_rulers():
            width = len(ruler)
            value = probe.covariance_v_direct(ruler, width)
            self.assertGreaterEqual(value, probe.golomb_covariance_lower_bound(len(ruler), width))
            if width >= 2:
                self.assertGreaterEqual(probe.negative_haar_budget(width), -F(3, 16))
        rule = self.fixture["dyadic_nonanticipating_rules"]["simple_T_equals_k"]
        self.assertEqual(rule["all_positive_chain_count"], 112)
        self.assertEqual(rule["certified_lower_bounds"], {"V": "1/8", "G_over_N": "1/64"})
        self.assertGreaterEqual(F(rule["minimum_record"]["G_over_N"]), F(1, 64))

    def test_16_prefix_scale_Abel_ownership(self) -> None:
        ownership = probe.prefix_scale_ownership((0, 1, 3, 7), 3)
        self.assertEqual(len(ownership["Omega_V"]), 4)
        self.assertEqual(len(ownership["Omega_O"]), 4)
        self.assertTrue(all(row["unit_owner_total"] == "1" for row in ownership["owner_checks"]))
        fixture = self.fixture["dyadic_energy_distribution"]["representative_chain"]["prefix_scale_ownership"]
        self.assertEqual(ownership, fixture)


if __name__ == "__main__":
    unittest.main()

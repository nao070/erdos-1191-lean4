#!/usr/bin/env python3
"""Exact regression tests for the centered multiband history certificate."""
from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import centered_multiband_history_certificate as probe


FIXTURE = Path(__file__).resolve().with_name("centered_multiband_history_certificate.json")


class CenteredMultibandHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_01_fixed_matrix_pd_rows_and_path_identity(self) -> None:
        self.assertEqual(probe.leading_minors(probe.H), (F(13, 100), F(97, 5000), F(13, 20000)))
        self.assertEqual(probe.matvec(probe.H, (F(1),) * 3), probe.GAMMA)
        self.assertEqual(probe.matvec(probe.D, (F(1),) * 3), probe.GAMMA)
        y = (F(2), F(-1), F(3))
        self.assertEqual(
            probe.quadratic(probe.D, y) - probe.quadratic(probe.H, y),
            probe.THETA * ((y[0] - y[1]) ** 2 + (y[1] - y[2]) ** 2),
        )

    def test_02_exact_schedule_increments(self) -> None:
        for alpha in (F(1, 7), F(1), F(17, 3), F(1191, 100)):
            rows = probe.rational_schedule(alpha, 1, 256)
            self.assertTrue(all(row["increment"] in (1, 2) for row in rows[1:]))
            self.assertTrue(all(row["T"] == row["k"] * row["q"] for row in rows))

    def test_03_spatial_prefix_fixture_enumeration(self) -> None:
        fixtures = probe.spatial_prefix_fixtures()
        self.assertEqual(len(fixtures), 112)
        self.assertTrue(all(tuple(sorted(ruler)) == ruler for ruler in fixtures))
        self.assertTrue(all(probe.is_golomb(ruler) and probe.is_golomb(ruler[:2]) for ruler in fixtures))

    def test_04_centered_lowpass_formula(self) -> None:
        ruler = (0, 1, 3, 7)
        for width in (1, 2, 4, 8, 16):
            c = probe.centered_lowpass(ruler, width)
            self.assertEqual(
                c,
                2 * sum((F(width - d, width * width) for d in probe.positive_differences(ruler) if d < width), F(0)),
            )
            self.assertGreaterEqual(c, 0)
            self.assertLess(c, 1)

    def test_05_adjacent_new_gap_first_use_bound(self) -> None:
        for ruler in probe.spatial_prefix_fixtures():
            record = probe.verify_adjacent_first_use(ruler, 64)
            self.assertGreaterEqual(record["small_gap_count"], record["required_count"])
            self.assertGreaterEqual(F(record["centered_first_use"]), F(record["lower_bound"]))

    def test_06_multiband_path_telescope(self) -> None:
        ruler = (0, 1, 3, 7)
        for prefix in (ruler[:2], ruler):
            for increment in (1, 2):
                self.assertEqual(
                    probe.multiband_path(prefix, 32, increment),
                    probe.centered_lowpass(prefix, 32) - probe.centered_lowpass(prefix, 32 << increment),
                )
        with self.assertRaises(probe.CertificateError):
            probe.multiband_path(ruler, 32, 3)

    def test_07_exact_fejer_ledger_all_fixtures(self) -> None:
        for ruler in probe.spatial_prefix_fixtures():
            ledger = probe.verify_path_ledger(ruler)
            self.assertEqual(F(ledger["ledger_lhs"]), F(ledger["ledger_rhs"]))
            self.assertEqual(ledger["scale_increments"], [1, 2])

    def test_08_exact_boundary_ratio_bound(self) -> None:
        alpha = F(1191, 100)
        for j in range(1, 6):
            k = 1 << j
            q_j_plus_1 = probe.ceil_power_of_two_rational(alpha * (j + 2))
            n = 1 + k * (k - 1) // 2
            record = probe.boundary_record(k, q_j_plus_1, n)
            self.assertEqual(record["T_next"], 2 * k * q_j_plus_1)
            self.assertEqual(record["B"], n + record["T_next"] - 1)
            self.assertLessEqual(F(record["B_over_N_minus_1"]), F(record["exact_upper_bound"]))
        with self.assertRaises(probe.CertificateError):
            probe.boundary_record(16, 24, 121)

    def test_09_coefficient_margin(self) -> None:
        self.assertEqual(F(3, 3200) - F(1, 1536), F(11, 38400))
        self.assertGreater(F(11, 38400), 0)

    def test_10_certificate_semantic_and_byte_replay(self) -> None:
        generated = probe.build_certificate()
        self.assertEqual(generated, self.fixture)
        self.assertEqual(FIXTURE.read_bytes(), probe.rendered_bytes(self.fixture))
        probe.validate_certificate(self.fixture)

    def test_11_hash_and_scope_mutations_rejected(self) -> None:
        self.assertEqual(probe.self_check(self.fixture), 9)
        changed = copy.deepcopy(self.fixture)
        changed["scope"]["prize_claim_ready"] = True
        probe.rehash(changed)
        with self.assertRaises(probe.CertificateError):
            probe.validate_certificate(changed)

    def test_12_spatial_order_indexing_caveat(self) -> None:
        ruler = (0, 1, 4, 6)
        self.assertTrue(probe.is_golomb(ruler))
        spatial_previous = ruler[:2]
        arbitrary_insertion_previous = (0, 4)
        self.assertNotEqual(spatial_previous, arbitrary_insertion_previous)
        spatial_delta = probe.centered_lowpass(ruler, 16) - probe.centered_lowpass(spatial_previous, 16)
        insertion_delta = probe.centered_lowpass(ruler, 16) - probe.centered_lowpass(arbitrary_insertion_previous, 16)
        self.assertNotEqual(spatial_delta, insertion_delta)
        with self.assertRaises(probe.CertificateError):
            probe.verify_adjacent_first_use(ruler, 16, arbitrary_insertion_previous)

    def test_13_open_obligation_is_preserved(self) -> None:
        scope = self.fixture["scope"]
        self.assertFalse(scope["common_signed_capacity_coupling"])
        self.assertFalse(scope["q1_resolved"])
        self.assertFalse(scope["q2_resolved"])
        self.assertFalse(scope["publication_ready"])
        self.assertFalse(scope["prize_claim_ready"])
        self.assertEqual(self.fixture["open_obligation"]["checkpoint"], "C058 remains OPEN")


if __name__ == "__main__":
    unittest.main()

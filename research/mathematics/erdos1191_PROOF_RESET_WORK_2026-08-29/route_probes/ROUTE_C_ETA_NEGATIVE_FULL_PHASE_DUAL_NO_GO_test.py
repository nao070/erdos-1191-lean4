#!/usr/bin/env python3
"""Exact replay tests for the eta-negative full-phase dual no-go."""

from __future__ import annotations

import copy
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


MODULE = "ROUTE_C_ETA_NEGATIVE_FULL_PHASE_DUAL_NO_GO_certificate"


class EtaNegativeFullPhaseDualNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_fixture_is_golomb_and_has_negative_shell_increment(self) -> None:
        fixture = self.value["fixture"]
        self.assertEqual(
            fixture["points"],
            [0, 26, 60, 77, 110, 175, 326, 519, 529, 543, 566, 622,
             724, 933, 1349, 2178],
        )
        self.assertEqual(fixture["positive_difference_count"], 120)
        self.assertEqual((fixture["H2"], fixture["H3"]), (442, 1659))
        self.assertEqual(fixture["eta_ratio"], "1659/1768")
        self.assertLess(self.cert.F(fixture["eta_ratio"]), 1)

    def test_finite_dyadic_envelope_is_labeled_with_its_exact_convention(self) -> None:
        envelope = self.value["fixture"]["finite_dyadic_envelope"]
        self.assertEqual(envelope["canonical_constant"], 2)
        self.assertEqual(envelope["actual_cap_formula"], "N_m <= 2*C*m^2*log(m)")
        self.assertEqual(
            [(row["m"], row["N_m"], row["required_log"]) for row in envelope["rows"]],
            [(4, 78, "39/32"), (8, 520, "65/32"), (16, 2179, "2179/1024")],
        )
        self.assertTrue(envelope["all_rows_certified"])
        self.assertFalse(envelope["eventual_infinite_ray_constructed"])

    def test_exact_phase_partition_has_87_gap_free_chambers(self) -> None:
        phase = self.value["phase"]
        self.assertEqual((phase["lower"], phase["upper"]), ("1649/8", "1649/4"))
        self.assertEqual(phase["event_line_count"], 78)
        self.assertEqual(phase["chamber_count"], 87)
        self.assertEqual(len(phase["breakpoints"]), 88)
        self.assertEqual(len(self.value["dual_certificate"]["chambers"]), 87)
        self.assertEqual(phase["breakpoints"][0], phase["lower"])
        self.assertEqual(phase["breakpoints"][-1], phase["upper"])

    def test_every_chamber_dual_replays_with_exact_endpoint_psd(self) -> None:
        summary = self.cert.replay_exact(self.value)
        self.assertEqual(summary["chambers_replayed"], 87)
        self.assertEqual(summary["epoch_duals_replayed"], 174)
        self.assertEqual(summary["endpoint_ldl_checks"], 348)
        self.assertTrue(summary["all_weights_nonnegative"])
        self.assertTrue(summary["all_endpoint_slacks_positive_definite"])

    def test_normalized_log_phase_margin_has_strict_negative_upper_bound(self) -> None:
        conclusion = self.value["conclusion"]
        self.assertEqual(conclusion["log_integral_upper_less_than"], "-1/40")
        self.assertEqual(conclusion["normalized_log_phase_upper_less_than"], "-1/40")
        self.assertTrue(conclusion["strictly_negative_full_phase_margin"])
        summary = self.cert.replay_exact(self.value)
        self.assertLess(summary["exact_log_integral_upper"], self.cert.F(-1, 40))
        self.assertLess(
            self.cert.F(-13913, 500000),
            summary["exact_log_integral_lower"],
        )
        self.assertLess(
            summary["exact_log_integral_upper"],
            self.cert.F(-139, 5000),
        )
        self.assertLess(
            self.cert.F(-81, 2000),
            summary["normalized_log_phase_lower"],
        )
        self.assertLess(
            summary["normalized_log_phase_upper"],
            self.cert.F(-1, 25),
        )

    def test_scope_does_not_claim_an_asymptotic_or_erdos_counterexample(self) -> None:
        scope = self.value["scope"]
        for key in (
            "large_rank_local_inequality_refuted",
            "eventual_critical_infinite_history_constructed",
            "C058_refuted",
            "Q1_Q2_resolved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertIs(scope[key], False)
        self.assertTrue(scope["finite_geometry_free_bare_eta_bridge_refuted"])

    def test_mutations_and_canonical_cli_are_hardened(self) -> None:
        result = self.cert.self_check(self.value)
        self.assertGreaterEqual(result["mutations_attempted"], 8)
        self.assertEqual(result["mutations_attempted"], result["mutations_rejected"])

        changed = copy.deepcopy(self.value)
        changed["scope"]["C058_refuted"] = True
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

        script = Path(self.cert.__file__).resolve()
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / "certificate.json"
            copied.write_bytes(self.cert.DEFAULT_CERTIFICATE.read_bytes())
            replay = subprocess.run(
                [sys.executable, str(script), "--verify", str(copied), "--self-check"],
                capture_output=True,
                check=False,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(replay.returncode, 0, replay.stderr.decode())
            self.assertIn(b"chambers_replayed=87", replay.stdout)

        raw = self.cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, self.cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)


if __name__ == "__main__":
    unittest.main()

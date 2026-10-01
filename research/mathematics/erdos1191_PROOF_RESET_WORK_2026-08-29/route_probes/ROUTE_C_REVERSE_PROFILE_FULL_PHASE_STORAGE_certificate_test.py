#!/usr/bin/env python3
"""Exact replay tests for the reverse-profile full-phase storage calibration."""

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


MODULE = "route_probes.ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate"


class ReverseProfileFullPhaseStorageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_reverse_fixture_and_finite_envelope(self) -> None:
        fixture = self.value["fixture"]
        self.assertEqual(
            fixture["points"],
            [0, 22, 60, 83, 102, 173, 303, 513, 616, 727, 772, 881,
             972, 1041, 1103, 1169],
        )
        self.assertEqual(fixture["positive_difference_count"], 120)
        self.assertEqual((fixture["H2"], fixture["H3"]), (430, 656))
        self.assertEqual(fixture["eta_ratio"], "82/215")
        self.assertEqual(fixture["V2"], "20177/66402")
        self.assertEqual(fixture["V3"], "2143/29039")
        self.assertEqual(fixture["delta_V"], "-443620417/1928247678")
        rows = fixture["finite_dyadic_envelope"]["rows"]
        self.assertEqual(
            [(row["m"], row["N_m"], row["required_log"]) for row in rows],
            [(4, 84, "21/16"), (8, 514, "257/128"), (16, 1170, "585/512")],
        )

    def test_exact_phase_partition_and_combined_primal_manifest(self) -> None:
        phase = self.value["phase"]
        self.assertEqual((phase["lower"], phase["upper"]), ("553/8", "553/4"))
        self.assertEqual(phase["event_line_count"], 78)
        self.assertEqual(phase["chamber_count"], 161)
        self.assertEqual(len(phase["breakpoints"]), 162)
        self.assertEqual(len(self.value["primal_certificate"]["chambers"]), 161)
        self.assertEqual(phase["breakpoints"][0], phase["lower"])
        self.assertEqual(phase["breakpoints"][-1], phase["upper"])

    def test_all_rational_gram_primals_and_owner_rows_replay(self) -> None:
        summary = self.cert.replay_exact(self.value)
        self.assertEqual(summary["chambers_replayed"], 161)
        self.assertEqual(summary["rational_gram_columns"], 2285)
        self.assertEqual(summary["generic_owner_rows"], 99176)
        self.assertEqual(summary["generic_owner_endpoint_checks"], 198352)
        self.assertEqual(summary["collapsed_endpoint_owner_rows"], 194528)
        self.assertTrue(summary["all_gram_matrices_psd_by_rational_factor"])
        self.assertTrue(summary["all_owner_rows_nonnegative"])

    def test_complete_phase_integral_beats_the_prototype_exactly(self) -> None:
        summary = self.cert.replay_exact(self.value)
        self.assertGreater(summary["raw_integral_lower"], self.cert.F(49, 1000))
        self.assertLess(summary["raw_integral_upper"], self.cert.F(1, 20))
        self.assertGreater(summary["normalized_lower"], self.cert.F(719, 10000))
        self.assertLess(summary["normalized_upper"], self.cert.F(72, 1000))
        self.assertLess(summary["prototype_rhs_upper"], self.cert.F(27, 1000))
        self.assertGreater(
            summary["normalized_lower"] - summary["prototype_rhs_upper"],
            self.cert.F(457, 10000),
        )

    def test_chamber_zero_exactly_refutes_a_pointwise_interpretation(self) -> None:
        summary = self.cert.replay_exact(self.value)
        self.assertEqual(summary["local_dual_pieces"], 8)
        self.assertEqual(summary["local_duals_replayed"], 16)
        self.assertEqual(summary["local_dual_endpoint_ldl_checks"], 32)
        self.assertLess(summary["chamber0_upper"], self.cert.F(2601, 100000))
        self.assertGreater(summary["prototype_rhs_lower"], summary["chamber0_upper"])
        self.assertGreater(
            summary["prototype_rhs_lower"] - summary["chamber0_upper"],
            self.cert.F(207, 1000000),
        )
        scope = self.value["scope"]
        self.assertTrue(scope["complete_phase_integrated_prototype_survival_proved"])
        self.assertFalse(scope["pointwise_or_per_chamber_prototype_survival_proved"])

    def test_scope_remains_finite_and_does_not_claim_C058(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["fixed_reverse_16_mark_k2_C2_fixture_only"])
        for key in (
            "eventual_critical_infinite_history_constructed",
            "global_owner_stitching_proved",
            "C058_resolved",
            "Q1_Q2_resolved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertIs(scope[key], False)

    def test_mutations_canonical_bytes_and_cli_are_hardened(self) -> None:
        mutations = self.cert.self_check(self.value)
        self.assertGreaterEqual(mutations["mutations_attempted"], 10)
        self.assertEqual(mutations["mutations_attempted"], mutations["mutations_rejected"])

        changed = copy.deepcopy(self.value)
        changed["scope"]["C058_resolved"] = True
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
            self.assertIn(b"chambers_replayed=161", replay.stdout)
            self.assertIn(b"local_endpoint_ldl_checks=32", replay.stdout)
            self.assertIn(b"full_phase_prototype_survives_exactly", replay.stdout)
            self.assertIn(b"chamber0_pointwise_prototype_fails_exactly", replay.stdout)

        raw = self.cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, self.cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)


if __name__ == "__main__":
    unittest.main()

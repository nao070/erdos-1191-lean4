#!/usr/bin/env python3
"""Exact replay tests for the ordered-permutation full-phase dual row."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import importlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


MODULE = "ROUTE_C_C123_ORDERED_PERMUTATION_FULL_PHASE_DUAL_certificate"


class C123OrderedPermutationFullPhaseDualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_exact_permutation_row_tightens_the_scalar_bank(self) -> None:
        summary = self.cert.replay_exact(self.value)
        self.assertEqual(summary["phase_chambers"], 140)
        self.assertEqual(summary["epoch_duals_replayed"], 280)
        self.assertEqual(summary["dual_weights_replayed"], 86_240)
        self.assertEqual(summary["endpoint_ldl_checks"], 560)
        self.assertLess(
            summary["normalized_upper"], F(301_218_263_143, 8_263_918_620_000)
        )
        self.assertEqual(summary["clean_necessary_B_lower"], F(1341, 4000))
        self.assertEqual(summary["clean_necessary_B_upper"], F(4753, 10000))
        self.assertEqual(summary["clean_open_interval_width"], F(2801, 20000))
        self.assertFalse(summary["barriers_contradict"])

    def test_same_multisets_but_different_order(self) -> None:
        fixture = self.value["fixture"]
        self.assertTrue(fixture["same_old_gap_multiset_as_C120"])
        self.assertTrue(fixture["same_new_gap_multiset_as_C120"])
        self.assertTrue(fixture["different_order_from_C120"])
        self.assertEqual(fixture["eta_ratio"], "82/215")
        self.assertEqual(fixture["delta_V"], "-443620417/1928247678")

    def test_scope_remains_finite_and_nondecisive(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["fixed_ordered_permutation_16_mark_row_only"])
        for key in (
            "all_scalar_storage_coefficients_refuted",
            "larger_cone_refuted",
            "arbitrary_rank_proved",
            "global_owner_ledger_constructed",
            "C058_resolved",
            "Q1_Q2_resolved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertIs(scope[key], False)

    def test_tampering_and_cli_are_hardened(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["sources"]["permutation_dual_sha256"] = "0" * 64
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

        changed = copy.deepcopy(self.value)
        changed["scope"]["C058_resolved"] = True
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

        mutations = self.cert.self_check(self.value)
        self.assertGreaterEqual(mutations["mutations_attempted"], 9)
        self.assertEqual(mutations["mutations_attempted"], mutations["mutations_rejected"])

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
            self.assertIn(b"phase_chambers=140", replay.stdout)
            self.assertIn(b"clean_B_upper<4753/10000", replay.stdout)
            self.assertIn(b"barriers_contradict=False", replay.stdout)

        raw = self.cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, self.cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)


if __name__ == "__main__":
    unittest.main()

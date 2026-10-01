#!/usr/bin/env python3
"""Exact replay tests for the first two-row scalar storage coefficient bank."""

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


MODULE = "ROUTE_C_C122_TWO_ROW_SCALAR_STORAGE_BANK_certificate"


class C122TwoRowScalarStorageBankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_exact_two_row_bank_is_nonempty(self) -> None:
        summary = self.cert.replay_exact(self.value)
        self.assertEqual(summary["reverse_epoch_duals_replayed"], 322)
        self.assertEqual(summary["reverse_endpoint_ldl_checks"], 644)
        self.assertLess(summary["reverse_normalized_upper"], F(19, 250))
        self.assertEqual(
            summary["necessary_B_lower"],
            F(287_434_930_599, 860_203_021_250),
        )
        self.assertEqual(
            summary["coarse_necessary_B_upper"],
            F(2_892_371_517, 2_918_555_375),
        )
        self.assertLess(
            summary["necessary_B_lower"], summary["coarse_necessary_B_upper"]
        )
        self.assertFalse(summary["barriers_contradict"])

    def test_scope_is_only_the_fixed_two_row_outer_bank(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["fixed_C118_C120_two_row_bank_only"])
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

    def test_source_or_scope_tampering_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["sources"]["C120_full_phase_dual_sha256"] = "0" * 64
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

        changed = copy.deepcopy(self.value)
        changed["scope"]["C058_resolved"] = True
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

    def test_cli_and_canonical_rendering(self) -> None:
        mutations = self.cert.self_check(self.value)
        self.assertGreaterEqual(mutations["mutations_attempted"], 8)
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
            self.assertIn(b"reverse_epoch_duals=322", replay.stdout)
            self.assertIn(b"barriers_contradict=False", replay.stdout)

        raw = self.cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, self.cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)


if __name__ == "__main__":
    unittest.main()

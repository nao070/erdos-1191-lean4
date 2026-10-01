#!/usr/bin/env python3
"""Exact replay tests for the subdivided C118 storage-prototype no-go."""

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


MODULE = "ROUTE_C_C118_SUBDIVIDED_STORAGE_NO_GO_certificate"


class C118SubdividedStorageNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.cert = importlib.import_module(MODULE)
        cls.value = cls.cert.build_certificate()

    def test_hybrid_partition_replaces_exactly_the_five_hotspots(self) -> None:
        refinement = self.value["refinement"]
        self.assertEqual(refinement["selected_chambers"], [49, 64, 70, 73, 74])
        self.assertEqual(refinement["subdivisions_in_reciprocal_coordinate"], 4)
        self.assertEqual(len(refinement["pieces"]), 20)
        self.assertEqual(
            [(piece["chamber"], piece["piece"]) for piece in refinement["pieces"]],
            [(chamber, piece) for chamber in [49, 64, 70, 73, 74] for piece in range(4)],
        )

    def test_exact_replay_closes_the_previous_window_on_the_no_go_side(self) -> None:
        summary = self.cert.replay_exact(self.value)
        self.assertEqual(summary["hybrid_phase_pieces"], 102)
        self.assertEqual(summary["epoch_duals_replayed"], 204)
        self.assertEqual(summary["dual_weights_replayed"], 62_832)
        self.assertEqual(summary["endpoint_ldl_checks"], 408)
        self.assertLess(summary["normalized_upper"], F(-83, 2000))
        self.assertLess(F(-83, 2000), summary["prototype_rhs_lower"])
        self.assertGreater(summary["prototype_rhs_lower"] - summary["normalized_upper"], F(1, 2000))
        self.assertGreater(summary["coefficient_box_rhs_lower"] - F(-83, 2000), F(1, 10_000))
        self.assertEqual(summary["necessary_B_lower_barrier"], F(287_434_930_599, 860_203_021_250))
        self.assertGreater(summary["necessary_B_lower_barrier"], F(1, 3))

    def test_scope_refutes_only_the_fixed_finite_prototype(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["fixed_C118_storage_prototype_refuted"])
        self.assertTrue(scope["nonnegative_epsilon_A_and_B_at_most_one_third_refuted"])
        for key in (
            "all_scalar_storage_coefficients_refuted",
            "large_rank_local_inequality_refuted",
            "eventual_critical_infinite_history_constructed",
            "C058_refuted",
            "Q1_Q2_resolved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertIs(scope[key], False)

    def test_base_or_refinement_tampering_is_rejected(self) -> None:
        changed = copy.deepcopy(self.value)
        changed["base_certificate"]["file_sha256"] = "0" * 64
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

        changed = copy.deepcopy(self.value)
        changed["refinement"]["pieces"][0]["n4"]["weights"][0] += 1
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

        changed = copy.deepcopy(self.value)
        changed["scope"]["C058_refuted"] = True
        changed["integrity"]["payload_sha256"] = self.cert.payload_hash(changed)
        with self.assertRaises(self.cert.CertificateError):
            self.cert.verify_certificate(changed)

    def test_mutation_set_and_canonical_cli_are_hardened(self) -> None:
        mutations = self.cert.self_check(self.value)
        self.assertGreaterEqual(mutations["mutations_attempted"], 10)
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
            self.assertIn(b"hybrid_phase_pieces=102", replay.stdout)
            self.assertIn(b"prototype_refuted_exactly", replay.stdout)

        raw = self.cert.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, self.cert.rendered_bytes(parsed))
        self.assertEqual(parsed, self.value)


if __name__ == "__main__":
    unittest.main()

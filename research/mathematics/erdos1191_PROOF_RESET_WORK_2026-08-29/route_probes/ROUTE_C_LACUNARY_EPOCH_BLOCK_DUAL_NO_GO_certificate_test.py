#!/usr/bin/env python3
"""Behavior tests for the exact lacunary epoch-block dual no-go."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import unittest

import ROUTE_C_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_certificate as cert


HERE = Path(__file__).resolve().parent
JSON_PATH = HERE / "ROUTE_C_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_certificate.json"


class LacunaryEpochBlockDualNoGoTests(unittest.TestCase):
    def test_exact_replay_proves_the_scoped_strict_dual_obstruction(self) -> None:
        payload = cert.build_certificate()
        self.assertTrue(cert.verify_certificate(payload))
        self.assertEqual(payload["fixture"]["points"], [(1 << k) - 1 for k in range(16)])
        self.assertEqual(payload["fixture"]["t"], "6096/1")
        self.assertEqual(payload["epoch4"]["integrated_demand"], "0/1")
        self.assertEqual(payload["epoch8"]["integrated_demand"], "981/16256")
        self.assertEqual(payload["dual"]["objective"], "370911/2560000")
        self.assertEqual(payload["dual"]["objective_minus_twice_demand"], "7865697/325120000")
        self.assertEqual(payload["dual"]["positive_weight_count"], 243)
        self.assertEqual(payload["dual"]["ldl_positive_pivot_count"], 31)
        self.assertEqual(payload["fejer"]["worst_ratio"], "9/16")
        self.assertEqual(payload["fejer"]["certified_phi_upper_bound"], "-70791273/5201920000")
        self.assertEqual(payload["verification"]["mutation_rejection_count"], 12)
        self.assertEqual(cert.run_mutation_suite(), 12)
        self.assertTrue(payload["scope"]["geometry_free_epoch_block_positivity_refuted"])
        self.assertFalse(payload["scope"]["eventual_fixed_C_critical_history"])
        self.assertFalse(payload["scope"]["C058_resolved"])

    def test_canonical_json_is_literal_replay_of_the_builder(self) -> None:
        stored = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, cert.build_certificate())
        self.assertTrue(cert.verify_certificate(stored))

    def test_semantic_mutations_are_rejected(self) -> None:
        payload = cert.build_certificate()
        mutations = []

        changed_point = copy.deepcopy(payload)
        changed_point["fixture"]["points"][15] -= 1
        mutations.append(changed_point)

        changed_t = copy.deepcopy(payload)
        changed_t["fixture"]["t"] = "6095/1"
        mutations.append(changed_t)

        changed_weight = copy.deepcopy(payload)
        changed_weight["dual"]["weight_numerators"][0] += 1
        mutations.append(changed_weight)

        changed_objective = copy.deepcopy(payload)
        changed_objective["dual"]["objective"] = "370912/2560000"
        mutations.append(changed_objective)

        changed_scope = copy.deepcopy(payload)
        changed_scope["scope"]["eventual_fixed_C_critical_history"] = True
        mutations.append(changed_scope)

        for mutation in mutations:
            with self.subTest(mutation=mutation):
                with self.assertRaises(cert.CertificateError):
                    cert.verify_certificate(mutation)

    def test_cli_verifies_the_canonical_certificate(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-B", str(cert.__file__), "--verify-json", str(JSON_PATH)],
            cwd=HERE,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("EXACT_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO", completed.stdout)


if __name__ == "__main__":
    unittest.main()

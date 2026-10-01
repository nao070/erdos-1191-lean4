#!/usr/bin/env python3
"""Positive and adversarial mutation tests for the canonical C139 bundle."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_certificate.json"
REPLAY = HERE / "ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_certificate.py"
ORACLE = HERE / "ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_independent_oracle.py"


def payload_hash(data: dict) -> str:
    payload = {key: value for key, value in data.items() if key != "integrity"}
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


class C139PhaseChamberTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads(CERTIFICATE.read_text())

    def run_program(self, program: Path, certificate: Path = CERTIFICATE):
        return subprocess.run(
            [sys.executable, "-B", str(program), "--certificate", str(certificate)],
            cwd=HERE,
            text=True,
            capture_output=True,
            env={**dict(__import__("os").environ), "PYTHONDONTWRITEBYTECODE": "1"},
        )

    def mutated(self, change, *, rehash=True):
        data = copy.deepcopy(self.base)
        change(data)
        if rehash:
            data["integrity"]["payload_sha256"] = payload_hash(data)
        temporary = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        json.dump(data, temporary, indent=2, sort_keys=True)
        temporary.write("\n")
        temporary.close()
        self.addCleanup(Path(temporary.name).unlink, missing_ok=True)
        return Path(temporary.name)

    def assert_rejected(self, change, *, rehash=True):
        path = self.mutated(change, rehash=rehash)
        result = self.run_program(REPLAY, path)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_01_primary_exact_replay(self):
        result = self.run_program(REPLAY)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("C139_EXACT_PHASE_CHAMBER_OK", result.stdout)

    def test_02_stdlib_independent_oracle(self):
        result = self.run_program(ORACLE)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("INDEPENDENT_C139_OK", result.stdout)

    def test_03_raw_integrity_mutation_rejected(self):
        self.assert_rejected(
            lambda data: data["endpoint_values"]["upper"].__setitem__("margin", "1/1"),
            rehash=False,
        )

    def test_04_phase_endpoint_mutation_rejected_after_rehash(self):
        self.assert_rejected(
            lambda data: data["phase"]["maximal_closed_feasible_interval"].__setitem__(1, "556/1")
        )

    def test_05_support_mutation_rejected_after_rehash(self):
        self.assert_rejected(lambda data: data["support"][0].__setitem__("coefficient", "1/1"))

    def test_06_c138_ancestry_mutation_rejected_after_rehash(self):
        self.assert_rejected(
            lambda data: data["support_ancestry"].__setitem__("canonical_C138_file_sha256", "0" * 64)
        )

    def test_07_affine_D_mutation_rejected_after_rehash(self):
        self.assert_rejected(lambda data: data["global_affine"]["D"].__setitem__("slope", "0/1"))

    def test_08_pre8_owner_audit_mutation_rejected_after_rehash(self):
        self.assert_rejected(
            lambda data: data["owner_audit"]["generic_open_chamber"].__setitem__("pre8_positive", 5)
        )

    def test_09_adjacent_slack_mutation_rejected_after_rehash(self):
        self.assert_rejected(lambda data: data["adjacent_failures"][0].__setitem__("slack", "-1/1"))

    def test_10_ledger_split_mutation_rejected_after_rehash(self):
        self.assert_rejected(lambda data: data["same_atom_ledger"]["phase_splits"].__setitem__(1, "553/1"))

    def test_11_terminal_scope_mutation_rejected_after_rehash(self):
        self.assert_rejected(
            lambda data: data["same_atom_ledger"].__setitem__("terminal_rows_retained", False)
        )

    def test_12_full_M16_mutation_rejected_after_rehash(self):
        self.assert_rejected(
            lambda data: data["full_M16_audit"].__setitem__("quarter_scaled_two_M8_replacement_used", True)
        )

    def test_13_C058_scope_upgrade_rejected_after_rehash(self):
        self.assert_rejected(lambda data: data["scope"].__setitem__("C058", True))


if __name__ == "__main__":
    unittest.main()


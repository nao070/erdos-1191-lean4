#!/usr/bin/env python3
"""Focused exact tests for C137 local charge-map no-go."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import unittest


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_certificate as cert  # noqa: E402


class C137LocalChargeNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = cert.build_certificate()
        cls.payload = cls.value["payload"]

    def test_01_fixture_and_exact_replay(self) -> None:
        fixture = self.payload["fixture"]
        self.assertEqual((fixture["marks"], fixture["channels"], fixture["supported_graph_roots"]), (32, 100, 57))
        self.assertEqual(fixture["phase"], "17745/32")
        stored = cert.load(cert.DEFAULT_CERTIFICATE)
        self.assertEqual(cert.validate_certificate(stored), self.value)

    def test_02_same_full_state_different_total(self) -> None:
        collision = self.payload["same_state_different_C133_total"]
        a, b = collision["cell_a"], collision["cell_b"]
        self.assertEqual(a["state_hash"], b["state_hash"])
        self.assertNotEqual(a["C133_lhs"], b["C133_lhs"])
        self.assertNotEqual(a["row_hash"], b["row_hash"])
        self.assertTrue(a["root_features_all_zero"])
        self.assertTrue(b["root_features_all_zero"])
        self.assertTrue(a["direct_demands_all_zero"])
        self.assertTrue(b["direct_demands_all_zero"])

    def test_03_same_full_state_different_terminals(self) -> None:
        collision = self.payload["same_state_different_terminal_rows"]
        a, b = collision["cell_a"], collision["cell_b"]
        self.assertEqual(a["state_hash"], b["state_hash"])
        self.assertNotEqual(a["terminal_e8"], b["terminal_e8"])
        self.assertNotEqual(a["terminal_e16"], b["terminal_e16"])

    def test_04_both_terminals_have_zero_capacity_witnesses(self) -> None:
        epoch8 = self.payload["same_state_different_C133_total"]["cell_a"]
        epoch16 = self.payload["zero_capacity_epoch16_terminal"]
        self.assertEqual((epoch8["graph_energy"], epoch8["terminal_e8"]), ("0/1", "1/41984670"))
        self.assertEqual((epoch16["graph_energy"], epoch16["terminal_e16"]), ("0/1", "27/358269184"))
        for witness in (epoch8, epoch16):
            self.assertTrue(witness["root_features_all_zero"])
            self.assertTrue(witness["direct_demands_all_zero"])

    def test_05_scalar_countercells_and_integrals(self) -> None:
        graph = self.payload["positive_graph_zero_ledger"]
        direct = self.payload["positive_direct_zero_ledger"]
        self.assertEqual((graph["graph_energy"], graph["C133_lhs"]), ("21/256", "0/1"))
        self.assertEqual((direct["weighted_direct"], direct["C133_lhs"]), ("225/32768", "0/1"))
        totals = self.payload["integrated_values"]
        self.assertEqual(F(totals["graph_price_P"]), F(1878008419901, 9402974208))
        self.assertEqual(F(totals["box_carrier_C133_integral_I"]), F(10229179, 1007632080))

    def test_06_mutations_floats_and_scope_upgrades_rejected(self) -> None:
        self.assertEqual(cert.mutation_self_check(self.value), {"mutations": 8, "rejected": 8})
        floating = copy.deepcopy(self.value)
        floating["payload"]["fixture"]["phase"] = 554.53125
        with self.assertRaises(cert.CertificateError):
            cert.validate_certificate(floating)
        scope = self.payload["scope"]
        self.assertFalse(scope["rules_out_nonlocal_cross_cell_transport"])
        self.assertFalse(scope["rules_out_same_atom_M8_M16_potential"])
        self.assertFalse(scope["C058_resolved"])

    def test_07_independent_oracle(self) -> None:
        oracle = HERE / "ROUTE_C_C137_LOCAL_GRAPH_C133_CHARGE_NO_GO_independent_oracle.py"
        result = subprocess.run(
            [sys.executable, str(oracle)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("C137_INDEPENDENT_ORACLE_OK", result.stdout)

    def test_08_json_has_no_floats(self) -> None:
        raw = cert.DEFAULT_CERTIFICATE.read_text(encoding="utf-8")
        value = json.loads(raw, parse_float=lambda _: self.fail("float in JSON"))
        cert.reject_floats(value)


if __name__ == "__main__":
    unittest.main(verbosity=2)

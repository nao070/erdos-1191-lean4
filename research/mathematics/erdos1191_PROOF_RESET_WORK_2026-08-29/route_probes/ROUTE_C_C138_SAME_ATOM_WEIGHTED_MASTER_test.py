#!/usr/bin/env python3

from __future__ import annotations

from fractions import Fraction as F
import unittest

import ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_certificate as cert
import ROUTE_C_C138_SAME_ATOM_WEIGHTED_MASTER_independent_oracle as oracle


class C138SameAtomWeightedMasterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = cert.load(cert.DEFAULT_CERTIFICATE)

    def test_exact_certificate(self):
        result = cert.validate_certificate(self.data)
        self.assertEqual(result["rank"], 51)
        self.assertEqual(result["owner_rows"], 1192)
        self.assertEqual(result["D"], F(1305537, 16384))
        self.assertEqual(result["P"], F(2367807877181, 16716398592))
        self.assertEqual(result["margin"], F(296239592131, 16716398592))
        self.assertEqual((result["formal_rows"], result["nonzero_rows"]), (14, 5))

    def test_mutation_self_check(self):
        mutations = cert.mutation_self_check(self.data)
        self.assertEqual((mutations["rejected"], mutations["attempted"]), (14, 14))

    def test_independent_oracle(self):
        result = oracle.verify()
        self.assertEqual(result["roots"], 57)
        self.assertEqual(result["rank"], 51)
        self.assertEqual(result["margin"], F(296239592131, 16716398592))
        self.assertEqual(result["formal_rows"], 14)

    def test_no_float_in_certificate(self):
        def walk(value):
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)
        walk(self.data)

    def test_pre8_and_weight_contract(self):
        owner = self.data["owner_audit"]
        self.assertEqual(
            (owner["pre8_rank7_owner_rows"], owner["pre8_rank7_zero_rows"], owner["pre8_rank7_positive_rows"]),
            (149, 145, 4),
        )
        self.assertEqual(F(owner["pre8_rank7_integral"]), F(6489, 256))
        self.assertTrue(owner["weights_apply_only_to_owner_RHS_and_D"])
        self.assertTrue(self.data["objective"]["price_is_single_unweighted_physical_energy"])

    def test_formal_rows_and_zero_terminals(self):
        ledger = self.data["same_atom_C133"]
        rows = {key: F(value) for key, value in ledger["integrated_rows"].items()}
        self.assertEqual(len(rows), 14)
        self.assertEqual(sum(value != 0 for value in rows.values()), 5)
        self.assertEqual(rows["terminal:e8:s4"], 0)
        self.assertEqual(rows["terminal:e16:s4"], 0)
        self.assertLess(rows["band:A32:s1"], 0)


if __name__ == "__main__":
    unittest.main()

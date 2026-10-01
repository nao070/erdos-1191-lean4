#!/usr/bin/env python3
"""Focused exact tests for the canonical C134 residual63 certificate."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP_certificate as audit


HERE = Path(__file__).resolve().parent


class Residual63Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.built = audit.build_certificate()
        cls.stored = json.loads(
            (HERE / "ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP_certificate.json").read_text(encoding="utf-8")
        )

    def test_stored_certificate_exact_replay(self) -> None:
        self.assertEqual(audit.verify_certificate(self.stored), self.built)

    def test_63_sources_and_signed_gram_identity(self) -> None:
        residual = audit.residual16_by_sources()
        self.assertEqual(residual, audit.residual16_by_subtraction())
        plus, minus, rows = audit.signed_gram_banks()
        self.assertEqual(residual, audit.matrix_sub(plus, minus))
        self.assertEqual(len(rows), 63)
        self.assertEqual(audit.trace(plus), F(4767, 1024))
        self.assertEqual(audit.trace(minus), F(4767, 1024))

    def test_full_boundary_owner_and_C103_slots(self) -> None:
        residual = audit.residual16_by_sources()
        past, current = audit.owner_lift(residual)
        self.assertEqual(audit.matrix_add(past, current), residual)
        self.assertEqual(past[0][8], -F(1, 64))
        for local_rank in range(4):
            self.assertEqual(sum(x != 0 for x in residual[local_rank]), 9)
        audit.verify_c103_embedding(residual)
        slots = audit.c103_slot_factors()
        self.assertTrue(all(value != 0 for value in slots.values()))

    def test_positive_Gram_only_separator(self) -> None:
        residual = audit.residual16_by_sources()
        q = tuple(F(1) if i in (0, 8) else F(0) for i in range(17))
        self.assertEqual(audit.quadratic(residual, q), -F(1, 16))
        for i, j in audit.CROSS_SOURCES:
            u, v = audit.d_vector(i), audit.d_vector(j)
            for z in (audit.vector_add(u, v, -1), audit.vector_add(u, v, 1)):
                self.assertGreaterEqual(audit.quadratic(audit.gram_root(z), q), 0)

    def test_mutations_are_rejected(self) -> None:
        mutations = []

        false_scope = copy.deepcopy(self.stored)
        false_scope["scope"]["C058_Q1_Q2_proved"] = True
        false_scope["integrity"]["payload_sha256"] = audit._canonical_hash(
            {k: v for k, v in false_scope.items() if k != "integrity"}
        )
        mutations.append(false_scope)

        dropped_source = copy.deepcopy(self.stored)
        dropped_source["generator_space"]["source_coefficients"].pop()
        dropped_source["integrity"]["payload_sha256"] = audit._canonical_hash(
            {k: v for k, v in dropped_source.items() if k != "integrity"}
        )
        mutations.append(dropped_source)

        dropped_boundary = copy.deepcopy(self.stored)
        dropped_boundary["C103_minimal_embedding"]["row_slot_factors"][
            "initial_epoch_boundary_band_0"
        ] = "0/1"
        dropped_boundary["integrity"]["payload_sha256"] = audit._canonical_hash(
            {k: v for k, v in dropped_boundary.items() if k != "integrity"}
        )
        mutations.append(dropped_boundary)

        omitted_rank = copy.deepcopy(self.stored)
        omitted_rank["natural_epoch16_coordinates"][
            "mandatory_rank_rows_15_through_18"
        ].pop()
        omitted_rank["integrity"]["payload_sha256"] = audit._canonical_hash(
            {k: v for k, v in omitted_rank.items() if k != "integrity"}
        )
        mutations.append(omitted_rank)

        bad_hash = copy.deepcopy(self.stored)
        bad_hash["integrity"]["payload_sha256"] = "0" * 64
        mutations.append(bad_hash)

        for mutation in mutations:
            with self.assertRaises(audit.CertificateError):
                audit.verify_certificate(mutation)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Mutation and replay tests for the exact Hou--Zhao cross certificate."""
from __future__ import annotations

import copy
import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from fractions import Fraction as F

import hou_zhao_cross_perturbation_certificate as cert


def rehash(payload: dict[str, object]) -> None:
    payload.pop("payload_sha256", None)
    payload["payload_sha256"] = hashlib.sha256(cert.canonical_bytes(payload)).hexdigest()


class CertificateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = cert.build_payload()

    def semantic_mutation(self, change) -> None:
        value = copy.deepcopy(self.payload)
        change(value)
        rehash(value)
        with self.assertRaisesRegex(ValueError, "semantic mismatch"):
            cert.validate_payload(value)

    def test_01_exact_certificate_validates(self) -> None:
        cert.validate_payload(self.payload)
        self.assertEqual(self.payload["boundary_objective"]["coefficient_sqrt_product_decimal"][:18],
                         "0.9434922260277724")

    def test_02_byte_exact_replay(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            one, two = Path(directory)/"one.json", Path(directory)/"two.json"
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(cert.main(["--output",str(one)]),0)
                self.assertEqual(cert.main(["--output",str(two)]),0)
            self.assertEqual(one.read_bytes(),two.read_bytes())
            self.assertEqual(one.read_bytes(),cert.render_payload(self.payload))

    def test_03_wrong_source_hash_payload_rejected(self) -> None:
        self.semantic_mutation(lambda p: p["source"].__setitem__("sha256","0"*64))

    def test_04_wrong_source_file_hash_rejected_before_git(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/cert.UPSTREAM_PATH
            path.write_text("# altered source\n",encoding="utf-8")
            with self.assertRaisesRegex(ValueError,"wrong upstream source hash"):
                cert.verify_upstream(path)

    def test_05_broken_row_sum_rejected(self) -> None:
        self.semantic_mutation(lambda p: p["perturbation"]["row_sums"].__setitem__(0,"1"))

    def test_06_wrong_J_sign_rejected(self) -> None:
        self.semantic_mutation(lambda p: p["perturbation"]["J_edges_one_based"][0].__setitem__(2,1))

    def test_07_non_PD_epsilon_rejected(self) -> None:
        self.assertLess(min(cert.core_values(F(1))["margins"]),0)
        self.semantic_mutation(lambda p: p["perturbation"].__setitem__("epsilon","1"))

    def test_08_negative_correlation_rejected(self) -> None:
        self.semantic_mutation(lambda p: p["correlations"]["at_epsilon"].__setitem__(31,"-1"))

    def test_09_changed_cover_rejected(self) -> None:
        self.semantic_mutation(lambda p: p["fixed_input"]["cover"].__setitem__("minimum_slack","1"))

    def test_10_wrong_beta_or_s_rejected(self) -> None:
        for key in ("beta","s"):
            with self.subTest(key=key):
                self.semantic_mutation(lambda p,k=key: p["perturbation"].__setitem__(k,"2"))

    def test_11_wrong_product_or_improvement_sign_rejected(self) -> None:
        changes=(
          lambda p: p["boundary_objective"].__setitem__("product_a_times_b","0"),
          lambda p: p["boundary_objective"].__setitem__("official_product_minus_product","-1"),
          lambda p: p["boundary_objective"].__setitem__("old_single_cycle_product_minus_product","-1"),
        )
        for change in changes:
            with self.subTest(change=change): self.semantic_mutation(change)

    def test_12_false_global_novelty_resolution_or_prize_claim_rejected(self) -> None:
        for key in ("global_optimum","novelty","erdos_1191_resolution","prize_claim"):
            with self.subTest(key=key):
                self.semantic_mutation(lambda p,k=key: p["claim_boundary"].__setitem__(k,True))

    def test_13_hash_mutation_rejected(self) -> None:
        value=copy.deepcopy(self.payload); value["payload_sha256"]="f"*64
        with self.assertRaisesRegex(ValueError,"payload hash mismatch"):
            cert.validate_payload(value)

    def test_14_semantic_mutation_with_valid_hash_rejected(self) -> None:
        self.semantic_mutation(lambda p: p["boundary_objective"].__setitem__("Phi","1"))

    def test_15_clean_decimal_bound_and_block_lift_are_locked(self) -> None:
        bound=F(self.payload["boundary_objective"]["clean_rational_coefficient_upper_bound"])
        product=F(self.payload["boundary_objective"]["product_a_times_b"])
        self.assertLess(product,bound*bound)
        self.semantic_mutation(lambda p: p["correlations"].__setitem__("block_lift","false"))


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Offline replay and mutation tests for the reoptimized boundary certificate."""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from fractions import Fraction as F

import hou_zhao_two_cycle_epsilon_exploration as cert

FIXTURE=Path(__file__).resolve().with_name("hou_zhao_reoptimized_boundary_certificate.json")

def rehash(value):
    value.pop("payload_sha256",None)
    value["payload_sha256"]=hashlib.sha256(cert.canonical_bytes(value)).hexdigest()

class ReoptimizedBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.payload=json.loads(FIXTURE.read_text(encoding="utf-8"))

    def mutate(self,path,replacement):
        value=copy.deepcopy(self.payload); cursor=value
        for key in path[:-1]: cursor=cursor[key]
        cursor[path[-1]]=replacement; rehash(value)
        with self.assertRaises(ValueError): cert.validate_certificate(value)

    def delete(self,path):
        value=copy.deepcopy(self.payload); cursor=value
        for key in path[:-1]: cursor=cursor[key]
        del cursor[path[-1]]; rehash(value)
        with self.assertRaises(ValueError): cert.validate_certificate(value)

    def test_01_certificate_validates(self):
        cert.validate_certificate(self.payload)

    def test_02_byte_exact_replay(self):
        self.assertEqual(FIXTURE.read_bytes(),cert.render(self.payload))
        with tempfile.TemporaryDirectory() as d:
            a=Path(d)/"a.json"; b=Path(d)/"b.json"
            a.write_bytes(cert.render(self.payload)); b.write_bytes(cert.render(self.payload))
            self.assertEqual(a.read_bytes(),b.read_bytes())

    def test_03_offline_interval_and_stationary_root(self):
        summary=cert.offline_summary()
        self.assertEqual(summary["combined_feasible_rational_epsilons"],"epsilon in Q and -rho < epsilon < rho")

    def test_04_source_hash_mutation_rejected(self):
        self.mutate(("source","sha256"),"0"*64)
        self.mutate(("source","repository"),"https://example.invalid")
        self.mutate(("source","path"),"wrong.py")
        self.delete(("source","repository"))

    def test_05_J_sign_mutation_rejected(self):
        self.mutate(("direction","J_edges_one_based",0,2),1)

    def test_06_epsilon_and_normalization_mutations_rejected(self):
        for key in ("epsilon","s","beta"):
            with self.subTest(key=key): self.mutate(("reoptimized_boundary",key),"2")

    def test_07_active_set_mutations_rejected(self):
        self.mutate(("reoptimized_boundary","active_count"),125)
        self.mutate(("reoptimized_boundary","omitted_constraints",0),2)

    def test_08_KKT_mutations_rejected(self):
        for key in self.payload["reoptimized_boundary"]["exact_kkt"]:
            with self.subTest(key=key): self.mutate(("reoptimized_boundary","exact_kkt",key),False)
        self.mutate(("reoptimized_boundary","q_sha256"),"0"*64)
        self.delete(("reoptimized_boundary","exact_kkt","stationarity_zero"))

    def test_09_PD_mutation_rejected(self):
        self.mutate(("reoptimized_boundary","pd","gershgorin_margins",0),"-1")
        self.mutate(("reoptimized_boundary","pd","proof"),"unchecked")

    def test_10_correlation_mutation_rejected(self):
        self.mutate(("reoptimized_boundary","correlations","minimum_value"),"-1")
        self.mutate(("reoptimized_boundary","correlations","block_lift"),"unchecked")

    def test_11_objective_identities(self):
        r=self.payload["reoptimized_boundary"]
        phi,a,b,p=map(F,(r["Phi"],r["a"],r["b"],r["product"]))
        self.assertEqual(b,1+(phi-128)/16); self.assertEqual(p,a*b)

    def test_12_objective_mutations_rejected(self):
        for key in ("Phi","a","b","product"):
            with self.subTest(key=key): self.mutate(("reoptimized_boundary",key),"1")

    def test_13_clean_bound_mutation_rejected(self):
        self.mutate(("reoptimized_boundary","clean_bound_squared_minus_product"),"-1")
        self.mutate(("reoptimized_boundary","fixed_published_q_product"),"1")
        self.mutate(("reoptimized_boundary","fixed_product_minus_reoptimized_product"),"-1")
        self.mutate(("reoptimized_boundary","coefficient_decimal"),"0")
        self.mutate(("regression_epsilon_1_over_500","payload_sha256"),"0"*64)
        self.mutate(("regression_epsilon_1_over_500","product"),"1")

    def test_14_overclaims_rejected(self):
        for key in ("global_optimum","novelty","prize_claim","erdos_1191_resolution",
                    "q1_resolved","q2_resolved","compatible_history","current_best"):
            with self.subTest(key=key): self.mutate(("claim_boundary",key),True)
        self.mutate(("status",),"Q1 solved")
        value=copy.deepcopy(self.payload); value["q1_resolved"]=True; rehash(value)
        with self.assertRaises(ValueError): cert.validate_certificate(value)
        value=copy.deepcopy(self.payload); value["reoptimized_boundary"]["current_best"]=True; rehash(value)
        with self.assertRaises(ValueError): cert.validate_certificate(value)

    def test_15_payload_hash_mutation_rejected(self):
        value=copy.deepcopy(self.payload); value["payload_sha256"]="f"*64
        with self.assertRaisesRegex(ValueError,"payload hash mismatch"): cert.validate_certificate(value)

if __name__=="__main__": unittest.main()

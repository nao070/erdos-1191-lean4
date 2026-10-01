#!/usr/bin/env python3
"""Focused exact and adversarial mutation tests for canonical C135."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import json
from pathlib import Path
import unittest

import ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_certificate as audit


HERE = Path(__file__).resolve().parent


class C135O0N1Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.value = json.loads(audit.DEFAULT_CERTIFICATE.read_text(encoding="utf-8"))
        cls.refined = json.loads(audit.SOURCE.read_text(encoding="utf-8"))
        cls.parent = json.loads(audit.PARENT_SOURCE.read_text(encoding="utf-8"))
        cls.summaries = audit.replay_sources()
        cls.model, cls.breakpoints = audit._fixture_audit(cls.refined)

    def test_stored_certificate_exact_replay(self) -> None:
        self.assertEqual(
            audit.verify_certificate(self.value, summaries=self.summaries),
            self.summaries,
        )

    def test_exact_complete_phase_separator_and_census(self) -> None:
        refined = self.summaries["refined"]
        parent = self.summaries["parent"]
        self.assertEqual(refined["refined_pieces"], 314)
        self.assertEqual(refined["epoch_duals"], 628)
        self.assertEqual(refined["weights"], 193_424)
        self.assertEqual(refined["endpoint_PD_checks"], 1_256)
        self.assertEqual(refined["denominators"], (100_000, 100_000_000))
        self.assertEqual(refined["support_range"], (183, 307))
        self.assertEqual(refined["strict_improvements"], 480)
        self.assertEqual(refined["inherited_epoch_duals"], 148)
        self.assertLess(refined["normalized_interval"][1], refined["target_interval"][0])
        self.assertGreater(refined["margin"], F(83_737_247, 2 * 10**11))
        self.assertEqual(
            parent["classification"],
            "EXACT_STORED_DUAL_NO_SEPARATION_NOT_PRIMAL_FEASIBILITY",
        )
        self.assertGreater(
            parent["normalized_interval"][0] - parent["target_interval"][1],
            F(1887, 10**6),
        )

    def test_scope_is_narrow_and_C058_stays_open(self) -> None:
        scope = self.value["scope"]
        self.assertTrue(scope["frozen_D1_setup_only"])
        self.assertTrue(scope["O0N1_rotation_only"])
        self.assertTrue(scope["complete_phase_integrated_dual_separator_constructed"])
        self.assertTrue(scope["frozen_O0N1_candidate_lower_bound_refuted_by_weak_duality"])
        self.assertTrue(scope["original_universal_D1_same_multiset_rotation_lemma_false"])
        for key in (
            "chamberwise_sign_test_used",
            "O0N1_primal_feasibility_certified",
            "O0N1_physical_primal_infeasibility_claimed",
            "dual_optimality_proved",
            "all_D1_rotations_refuted",
            "Route_C_false",
            "C130_invalid",
            "C131_invalid",
            "arbitrary_representative_independence_globally_false",
            "C103_global_owner_ledger_resolved",
            "common_phase_rule_globally_admissible_proved",
            "cross_row_compatibility_proved",
            "arbitrary_history_proved",
            "arbitrary_rank_proved",
            "C058_false_or_resolved",
            "Erdos_1191_resolved",
            "Q1_Q2_resolved",
            "publication_novelty_or_prize_claimed",
        ):
            self.assertFalse(scope[key], key)

    def test_rehashed_scope_and_claim_upgrades_are_rejected(self) -> None:
        paths = (
            ("scope", "Route_C_false", True),
            ("scope", "C130_invalid", True),
            ("scope", "C131_invalid", True),
            ("scope", "arbitrary_representative_independence_globally_false", True),
            ("scope", "C103_global_owner_ledger_resolved", True),
            ("scope", "common_phase_rule_globally_admissible_proved", True),
            ("scope", "cross_row_compatibility_proved", True),
            ("scope", "arbitrary_history_proved", True),
            ("scope", "arbitrary_rank_proved", True),
            ("scope", "C058_false_or_resolved", True),
            ("scope", "Q1_Q2_resolved", True),
            ("scope", "Erdos_1191_resolved", True),
            ("scope", "dual_optimality_proved", True),
            ("scope", "O0N1_primal_feasibility_certified", True),
            ("scope", "all_D1_rotations_refuted", True),
            ("exact_results", "chamberwise_sign_criterion_used", True),
        )
        for section, key, replacement in paths:
            with self.subTest(key=key):
                changed = copy.deepcopy(self.value)
                changed[section][key] = replacement
                changed["integrity"]["payload_sha256"] = audit.payload_hash(changed)
                with self.assertRaises(audit.CertificateError):
                    audit.verify_certificate(changed, summaries=self.summaries)

    def test_rehashed_fixture_partition_and_numeric_type_mutations_are_rejected(self) -> None:
        mutations = []
        changed = copy.deepcopy(self.value)
        changed["frozen_setup"]["rotation"] = [0, 2]
        mutations.append(changed)
        changed = copy.deepcopy(self.value)
        changed["frozen_setup"]["rho"] = "1/2"
        mutations.append(changed)
        changed = copy.deepcopy(self.value)
        changed["frozen_setup"]["coefficients"]["B"] = "1/3"
        mutations.append(changed)
        changed = copy.deepcopy(self.value)
        changed["partition_construction"]["complete_refined_piece_count"] = 313
        mutations.append(changed)
        changed = copy.deepcopy(self.value)
        changed["partition_construction"]["uniform_exact_subdivision_factor"] = 4.0
        mutations.append(changed)
        changed = copy.deepcopy(self.value)
        changed["frozen_setup"]["positive_difference_count"] = True
        mutations.append(changed)
        for changed in mutations:
            changed["integrity"]["payload_sha256"] = audit.payload_hash(changed)
            with self.assertRaises(audit.CertificateError):
                audit.verify_certificate(changed, summaries=self.summaries)

    def test_direct_partition_mutations_are_semantically_rejected(self) -> None:
        mutations = []
        changed = copy.deepcopy(self.refined)
        changed["uniform_subdivision_factor"] = 3
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["selected_parent_chambers"][1] = changed["selected_parent_chambers"][0]
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["selected_parent_chambers"][0] = True
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["records"][0], changed["records"][1] = changed["records"][1], changed["records"][0]
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["right"] = changed["records"][1]["right"]
        mutations.append(changed)
        for changed in mutations:
            with self.assertRaises(audit.CertificateError):
                audit.replay_refined(
                    changed,
                    self.parent,
                    self.model,
                    self.breakpoints,
                    require_embedded=False,
                )

    def test_direct_dual_mutations_are_semantically_rejected(self) -> None:
        mutations = []
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["n4"]["weights"][0] = -1
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["n4"]["weights"][0] = True
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["n4"]["denominator"] = 100_000_000.0
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["Dc4"] = "0/1"
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["n4"]["objective"] = "0/1"
        mutations.append(changed)
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["n4"]["improvement_over_parent"] = "0/1"
        mutations.append(changed)
        for changed in mutations:
            with self.assertRaises(audit.CertificateError):
                audit.replay_refined(
                    changed,
                    self.parent,
                    self.model,
                    self.breakpoints,
                    require_embedded=False,
                )

    def test_controlled_double_weight_mutation_reaches_and_fails_endpoint_PD(self) -> None:
        changed = copy.deepcopy(self.refined)
        record = changed["records"][0]
        dual = record["n4"]
        weights = tuple(2 * x for x in dual["weights"])
        denominator = dual["denominator"]
        left, right = F(record["left"]), F(record["right"])
        hc, ho, weighted, dc, do, objective = self.model._dual_epoch_reconstruction(
            left, right, 4, denominator, weights
        )
        record["Dc4"] = audit.ftext(dc)
        record["Do4"] = audit.ftext(do)
        dual["weights"] = list(weights)
        dual["objective"] = audit.ftext(objective)
        parent_objective = F(self.parent["records"][0]["n4"]["objective"])
        dual["improvement_over_parent"] = audit.ftext(objective - parent_objective)
        self.assertFalse(
            self.model._bareiss_positive_definite(
                self.model._integer_slack(hc, ho, weighted, denominator, left)
            )
        )
        with self.assertRaisesRegex(audit.CertificateError, "positive definite"):
            audit.replay_refined(
                changed,
                self.parent,
                self.model,
                self.breakpoints,
                require_embedded=False,
            )

    def test_provenance_and_independent_oracle_boundaries(self) -> None:
        changed = copy.deepcopy(self.refined)
        changed["records"][0]["n4"]["weights"][0] += 1
        with self.assertRaisesRegex(audit.CertificateError, "internal sha256"):
            audit._source_internal_hash(changed, audit.SOURCE_INTERNAL_SHA256, "refined")
        oracle_text = (
            HERE / "ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_independent_oracle.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("import ROUTE_C_C135", oracle_text)
        self.assertNotIn("/private/tmp", oracle_text)
        self.assertNotRegex(oracle_text, r"\bassert\b")

    def test_compact_certificate_contains_no_floats(self) -> None:
        def walk(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)
        walk(self.value)


if __name__ == "__main__":
    unittest.main()

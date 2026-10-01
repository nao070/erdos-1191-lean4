from __future__ import annotations

import json
import unittest
from hashlib import sha256

from wave16_terminal_potential_certificate import DEFAULT_OUTPUT, build_certificate


class Wave16TerminalPotentialCertificateTests(unittest.TestCase):
    def test_all_epoch_fraction_identities(self) -> None:
        certificate = build_certificate()
        self.assertTrue(certificate["all_exact_checks_pass"])
        self.assertEqual(
            certificate["epochs"], [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        )
        for row in certificate["epoch_rows"]:
            with self.subTest(epoch=row["epoch"]):
                self.assertTrue(row["terminal_mass_equality"])
                self.assertTrue(row["r_expansion_coefficients_match"])
                self.assertTrue(row["all_q_row_mass_equalities"])
                self.assertTrue(row["next_bulk_minus_u_formula_matches"])
                self.assertTrue(row["delta_below_log_13_certified"])

    def test_fejer_fraction_identity_and_signs(self) -> None:
        for row in build_certificate()["fejer_rows"]:
            with self.subTest(horizon=row["horizon"]):
                self.assertTrue(row["exact_harmonic_expansion"])
                self.assertTrue(row["weights_strictly_decreasing"])
                self.assertTrue(row["renewal_middle_coefficients_nonpositive"])
                self.assertTrue(row["renewal_terminal_coefficient_nonpositive"])

    def test_certificate_is_deterministic_self_hashed_and_unresolved(self) -> None:
        first = build_certificate()
        self.assertEqual(first, build_certificate())

        unhashed = dict(first)
        internal_hash = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())

        self.assertEqual(
            first["scope_flags"],
            {
                "finite_algebra_only": True,
                "infinite_branch_constructed": False,
                "disjoint_floor_premium_proved": False,
                "p17_proved": False,
                "p19_proved": False,
                "p21_proved": False,
                "question_1_resolved": False,
                "question_2_resolved": False,
                "erdos_1191_resolved": False,
                "problem_unresolved": True,
                "prize_claim_ready": False,
            },
        )
        committed = json.loads(DEFAULT_OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(committed, first)


if __name__ == "__main__":
    unittest.main()

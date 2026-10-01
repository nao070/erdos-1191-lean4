#!/usr/bin/env python3
"""Tests for the universal actual-Haar star cover certificate."""

from __future__ import annotations

import copy
from fractions import Fraction as F
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import direct_b_membership_sddm_lp_certificate as membership
import universal_haar_star_cover_certificate as star


class UniversalHaarStarCoverTests(unittest.TestCase):
    def test_star_mass_has_the_sharp_n4_value(self) -> None:
        # Catches the missing factor two between one star edge and total mass.
        weights = star.star_root_weights(4)
        self.assertEqual(set(weights), {(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4)})
        self.assertTrue(all(value == F(3, 128) for value in weights.values()))
        self.assertEqual(sum(weights.values(), F(0)), F(9, 64))

    def test_hand_checked_states_have_the_expected_energies(self) -> None:
        # Catches a reversed Haar sign block or use of the box-state formula.
        signed = star.haar_block_state(5, 1, 3, 4)
        self.assertEqual(signed, (0, -1, -1, 1, 0))
        self.assertEqual(star.direct_energy(4, signed), -F(1, 64))
        self.assertEqual(star.star_energy(4, signed), F(9, 64))

        # The full internal binary interval is the literal sharp witness.
        sharp = star.haar_block_state(5, 1, 1, 4)
        self.assertEqual(sharp, (0, 1, 1, 1, 0))
        self.assertEqual(star.direct_energy(4, sharp), F(9, 64))
        self.assertEqual(star.star_energy(4, sharp), F(9, 64))

    def test_exhaustive_abstract_haar_states_are_covered(self) -> None:
        # Catches any missing endpoint, empty-sign-block, or adjacent case.
        audit = star.exhaustive_state_audit(2, 10)
        self.assertEqual(audit["n_range"], [2, 10])
        self.assertEqual(audit["failures"], 0)
        # n=2 has only a singleton internal interval, whose direct energy is 0.
        self.assertEqual(audit["sharp_witnesses"], 8)
        self.assertGreater(audit["distinct_states_checked"], 1_000)

    def test_exhaustive_audit_cache_cannot_be_poisoned_by_a_caller(self) -> None:
        # Catches returning a cached mutable dict that can corrupt a later
        # semantic replay in the same Python process.
        first = star.exhaustive_state_audit(2, 3)
        original_count = first["per_n"][0]["distinct_states"]
        first["failures"] = 777
        first["per_n"][0]["distinct_states"] = -1

        replay = star.exhaustive_state_audit(2, 3)
        self.assertEqual(replay["failures"], 0)
        self.assertEqual(replay["per_n"][0]["distinct_states"], original_count)

    def test_actual_n4_cells_replay_the_physical_star_price(self) -> None:
        # Catches replacing chi_T(d) by coefficient trace or dropping a cell.
        points = membership.ONE_EPOCH_POINTS
        self.assertEqual(star.physical_star_price(points, 200), F(207, 640))
        audit = star.actual_cell_audit(4, points, 200)
        self.assertEqual(audit["complete_cell_count"], 16)
        self.assertEqual(audit["classification_failures"], 0)
        self.assertEqual(audit["cover_failures"], 0)
        self.assertEqual(audit["cell_sum_star_price"], F(207, 640))
        self.assertEqual(audit["weighted_signed_demand"], F(63, 640))
        self.assertEqual(audit["star_surplus"], F(9, 40))

    def test_ungated_small_scale_price_stays_positive(self) -> None:
        # Catches an invalid claim that the universal star can be summed over
        # every low dyadic scale without an active gate.
        self.assertEqual(
            star.physical_star_price(membership.ONE_EPOCH_POINTS, 1),
            F(9, 32),
        )

    def test_certificate_replays_literal_theorem_and_fixture_values(self) -> None:
        # Catches a self-consistent generator that silently changes the theorem.
        certificate = star.build_certificate()
        star.verify_certificate(certificate)
        self.assertEqual(certificate["schema"], "erdos1191.universal_haar_star_cover.v1")
        self.assertEqual(certificate["abstract_state_audit"]["distinct_states_checked"], 5_820)
        self.assertEqual(
            [row["physical_star_price"] for row in certificate["fixture_audits"]],
            ["207/640", "5173/12800", "2097/6400", "52423/128000", "46431/102400"],
        )
        self.assertEqual(
            certificate["integrity"]["payload_sha256"],
            star.payload_hash(certificate),
        )

        changed = copy.deepcopy(certificate)
        changed["theorem"]["star_weight"] = "(n-1)/(4n^2)"
        with self.assertRaises(star.CertificateError):
            star.verify_certificate(changed)

    def test_self_check_rejects_every_named_mutation(self) -> None:
        # Catches validators that trust embedded outputs instead of recomputing.
        result = star.self_check(star.build_certificate())
        self.assertEqual(result, {"mutations_attempted": 10, "mutations_rejected": 10})

    def test_cli_generates_then_replays_literal_bytes(self) -> None:
        # Catches a CLI that reports success without writing/verifying bytes.
        script = Path(star.__file__).resolve()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "certificate.json"
            generated = subprocess.run(
                [sys.executable, str(script), "--output", str(output)],
                check=False,
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(generated.returncode, 0, generated.stderr)
            self.assertTrue(output.is_file())
            replay = subprocess.run(
                [sys.executable, str(script), "--verify", str(output), "--self-check"],
                check=False,
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            self.assertEqual(replay.returncode, 0, replay.stderr)
            self.assertIn("mutations_rejected=10", replay.stdout)


if __name__ == "__main__":
    unittest.main()

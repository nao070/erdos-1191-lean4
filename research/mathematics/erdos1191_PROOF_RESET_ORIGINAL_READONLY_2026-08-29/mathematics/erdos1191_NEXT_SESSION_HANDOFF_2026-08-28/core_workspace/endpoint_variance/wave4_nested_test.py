from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest

import wave4_nested_search as nested
from gap_measure_dynamics import normalized_gap_function_variance


class NestedSearchTests(unittest.TestCase):
    def test_integer_moment_gap_variance_matches_fraction_oracle(self) -> None:
        # Catches a missing m^4 or N^2 normalization in the fast score used
        # to rank beam states.
        generator = random.Random(1191)
        fixtures = [(0, 1, 4, 6)]
        fixtures.extend(
            tuple(sorted(generator.sample(range(100), count)))
            for count in range(2, 17)
        )
        for points in fixtures:
            self.assertEqual(
                nested.integer_gap_function_variance(points),
                normalized_gap_function_variance(points),
            )
        self.assertEqual(
            nested.integer_partial_gap_function_variance(
                (0, 1, 4, 6), final_rank_count=8
            ),
            Fraction(297, 50176),
        )

    def test_independent_difference_audit_lists_every_difference(self) -> None:
        # Catches accepting a repeated difference or omitting a pair from the
        # final witness certificate.
        audit = nested.independent_difference_audit((0, 1, 4, 6))
        self.assertTrue(audit.is_golomb)
        self.assertEqual(audit.pair_count, 6)
        self.assertEqual(audit.sorted_differences, (1, 2, 3, 4, 5, 6))
        self.assertEqual(audit.collisions, ())

        collision = nested.independent_difference_audit((0, 1, 2))
        self.assertFalse(collision.is_golomb)
        self.assertEqual(collision.collisions, ((1, ((0, 1), (1, 2))),))

    def test_critical_caps_use_a_rigorous_logarithm_decision(self) -> None:
        # Catches a missing factor 2, using log base 2, or rounding the bound
        # upward.  The exact inequalities are N <= 2*m^2*log(m).
        self.assertEqual(nested.critical_modulus_cap(4, Fraction(1)), 44)
        self.assertEqual(nested.critical_modulus_cap(8, Fraction(1)), 266)
        self.assertEqual(nested.critical_modulus_cap(3, Fraction(1)), 19)
        self.assertEqual(nested.critical_modulus_cap(5, Fraction(1)), 80)
        self.assertTrue(nested.modulus_is_within_envelope(266, 8, Fraction(1)))
        self.assertFalse(nested.modulus_is_within_envelope(267, 8, Fraction(1)))

    def test_exact_profile_has_hand_checked_gap_and_innovation_values(self) -> None:
        # Catches confusing Var_nu(f) with N*Var_nu(f), or normalizing Q_00
        # by the old rather than the new diameter modulus.
        rows = nested.dyadic_score_rows((0, 1, 4, 6), sizes=(2, 4))
        self.assertEqual(tuple(row.mark_count for row in rows), (2, 4))
        self.assertEqual(rows[0].gap_variance, Fraction(1, 64))
        self.assertIsNone(rows[0].innovation_q00_per_modulus)
        self.assertEqual(rows[1].gap_variance, Fraction(3, 448))
        self.assertEqual(rows[1].innovation_q00_per_modulus, Fraction(15, 3584))

    def test_exhaustive_four_mark_search_is_complete_at_its_bound(self) -> None:
        # Catches silently fixing the diameter, pruning a reflection, or
        # reporting a heuristic maximum as complete.  There are C(6,3)=20
        # normalized candidates with N <= 7, and only this reflection pair is
        # Golomb.
        result = nested.exhaustive_gap_search(mark_count=4, max_modulus=7)
        self.assertTrue(result.complete)
        self.assertEqual(result.candidate_count, 20)
        self.assertEqual(result.accepted_count, 2)
        self.assertEqual(result.best_score, Fraction(3, 448))
        self.assertEqual(
            result.best_rulers,
            ((0, 1, 4, 6), (0, 2, 5, 6)),
        )

        unrestricted = nested.exhaustive_gap_search(mark_count=3, max_modulus=19)
        common_envelope = nested.exhaustive_gap_search(
            mark_count=3,
            max_modulus=19,
            envelope_constant=Fraction(1),
        )
        self.assertLess(common_envelope.accepted_count, unrestricted.accepted_count)

    def test_seeded_beam_search_returns_reaudited_nested_rulers(self) -> None:
        # Catches using unchecked search-state differences, a non-reproducible
        # RNG, or enforcing the envelope only at the final checkpoint.
        arguments = dict(
            sizes=(4, 8),
            constant=Fraction(1),
            objective="gap",
            beam_width=24,
            candidates_per_state=16,
            seed=1191,
            retain=3,
        )
        first = nested.beam_search_nested(**arguments)
        second = nested.beam_search_nested(**arguments)
        self.assertEqual(first, second)
        self.assertEqual(first.seed, 1191)
        self.assertGreater(len(first.witnesses), 0)
        for witness in first.witnesses:
            self.assertEqual(len(witness.points), 8)
            self.assertTrue(witness.difference_audit.is_golomb)
            self.assertEqual(witness.difference_audit.pair_count, 28)
            self.assertTrue(witness.envelope_compatible)
            self.assertEqual(
                tuple(row.mark_count for row in witness.envelope_rows),
                tuple(range(2, 9)),
            )
            self.assertTrue(all(row.certified for row in witness.envelope_rows))
            self.assertEqual(tuple(row.mark_count for row in witness.rows), (4, 8))
            self.assertTrue(
                all(row.innovation_q00_per_modulus is not None for row in witness.rows)
            )

    def test_certificate_is_deterministic_and_contains_all_differences(self) -> None:
        # Catches non-canonical serialization or replacing the independent
        # all-pairs audit with a bare boolean.
        script = Path(__file__).with_name("wave4_nested_certificate.py")
        with tempfile.TemporaryDirectory() as temporary_directory:
            outputs = [Path(temporary_directory) / name for name in ("a.json", "b.json")]
            common = [
                sys.executable,
                str(script),
                "--sizes",
                "4,8",
                "--constant",
                "1",
                "--beam-width",
                "12",
                "--candidates-per-state",
                "12",
                "--retain",
                "1",
                "--seeds",
                "1191",
            ]
            for output in outputs:
                completed = subprocess.run(
                    [*common, "--output", str(output)],
                    cwd=script.parent,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(outputs[0].read_bytes(), outputs[1].read_bytes())
            payload = json.loads(outputs[0].read_text())
            recorded_hash = payload.pop("certificate_sha256")
            canonical = json.dumps(
                payload,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode()
            self.assertEqual(hashlib.sha256(canonical).hexdigest(), recorded_hash)
            for run in payload["runs"]:
                witness = run["witnesses"][0]
                self.assertEqual(
                    len(witness["all_positive_differences"]),
                    witness["pair_count"],
                )
                self.assertEqual(
                    len(set(witness["all_positive_differences"])),
                    witness["pair_count"],
                )
                self.assertEqual(
                    [row["mark_count"] for row in witness["all_prefix_envelope_rows"]],
                    list(range(2, 9)),
                )
                self.assertTrue(
                    all(row["certified"] for row in witness["all_prefix_envelope_rows"])
                )


if __name__ == "__main__":
    unittest.main()

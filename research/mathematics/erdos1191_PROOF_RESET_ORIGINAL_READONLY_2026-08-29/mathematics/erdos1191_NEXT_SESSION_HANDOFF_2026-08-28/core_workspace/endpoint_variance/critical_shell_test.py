from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

import critical_shell_search as css


class CriticalShellTests(unittest.TestCase):
    def test_rational_log_two_interval_contains_hand_bounds(self) -> None:
        # Catches a wrong sign or missing tail in the rigorous log enclosure.
        lower, upper = css.log_two_interval(8)
        self.assertLess(Fraction(2, 3), lower)
        self.assertLess(lower, upper)
        self.assertLess(upper, Fraction(7, 10))

    def test_envelope_is_checked_at_every_dyadic_prefix(self) -> None:
        # For (0,1,4,6), C=1/2 passes at m=2 and m=4; C=1/3
        # fails at m=2.  These comparisons use rigorous log bounds.
        ruler = (0, 1, 4, 6)
        compatible = css.critical_envelope_audit(
            ruler, j0=1, horizon=2, constant=Fraction(1, 2)
        )
        incompatible = css.critical_envelope_audit(
            ruler, j0=1, horizon=2, constant=Fraction(1, 3)
        )
        self.assertTrue(compatible.compatible)
        self.assertEqual(tuple(row.j for row in compatible.rows), (1, 2))
        self.assertTrue(all(row.certified for row in compatible.rows))
        self.assertFalse(incompatible.compatible)
        self.assertEqual(
            tuple(row.j for row in incompatible.rows if not row.certified),
            (1,),
        )

    def test_shell_partition_has_hand_derived_four_mark_values(self) -> None:
        # Mutation caught: assigning the old edge to shell 2, dropping the
        # persistence term at N=7, or counting unordered interactions.
        result = css.birth_shell_decomposition((0, 1, 4, 6), j0=1, horizon=2)
        self.assertEqual(result.level_energies, (Fraction(1, 32), Fraction(3, 112)))
        self.assertEqual(result.functional, Fraction(13, 224))

        first, second = result.shells
        self.assertEqual(first.shell, 1)
        self.assertEqual(first.net, Fraction(13, 392))
        self.assertEqual(first.diagonal, Fraction(13, 392))
        self.assertEqual(first.off_diagonal, 0)

        self.assertEqual(second.shell, 2)
        self.assertEqual(second.net, Fraction(39, 1568))
        self.assertEqual(second.diagonal, Fraction(25, 1568))
        self.assertEqual(second.off_diagonal, Fraction(1, 112))
        self.assertEqual(sum(shell.net for shell in result.shells), result.functional)

    def test_smallest_fixture_refutes_signed_shell_candidates(self) -> None:
        # This exact ruler simultaneously kills H1--H4.
        audit = css.audit_candidates((0, 1, 4, 6), j0=1, horizon=2)
        self.assertEqual(audit["H1"].first_failure, (2, 2))
        self.assertEqual(audit["H2"].first_failure, (2, 2))
        self.assertEqual(audit["H3"].first_failure, (1, 2))
        self.assertEqual(audit["H4"].first_failure, (2, 2))
        self.assertIsNone(audit["H5"].first_failure)
        self.assertIsNone(audit["H6"].first_failure)

    def test_branch_and_bound_matches_literal_small_denominator(self) -> None:
        # There are C(5,2)=10 normalized four-mark candidates of diameter 6,
        # and exactly the two reflected Golomb rulers below survive.
        result = css.exhaustive_rulers(mark_count=4, diameter=6)
        self.assertEqual(result.candidate_count, 10)
        # Search nodes are the root, 4 viable one-internal-mark prefixes,
        # 8 viable two-internal-mark prefixes, and 2 accepted endpoints.
        self.assertEqual(result.node_count, 15)
        self.assertEqual(
            result.rulers,
            ((0, 1, 4, 6), (0, 2, 5, 6)),
        )

    def test_random_greedy_search_is_seeded_and_every_output_is_golomb(self) -> None:
        first = css.random_greedy_rulers(
            mark_count=8, attempts=20, max_step=12, seed=1191
        )
        second = css.random_greedy_rulers(
            mark_count=8, attempts=20, max_step=12, seed=1191
        )
        self.assertEqual(first, second)
        self.assertEqual(first.seed, 1191)
        self.assertEqual(first.attempts, 20)
        self.assertGreater(len(first.rulers), 0)
        for ruler in first.rulers:
            differences = [
                ruler[right] - ruler[left]
                for left in range(len(ruler))
                for right in range(left + 1, len(ruler))
            ]
            self.assertEqual(len(differences), len(set(differences)))

    def test_literal_arc_oracle_has_independent_hand_values(self) -> None:
        # The oracle must count residue sets, not call the four-endpoint kernel.
        self.assertEqual(
            css.literal_arc_covariance(0, 1, 0, 4, 7),
            Fraction(3, 7),
        )
        self.assertEqual(
            css.literal_arc_covariance(0, 1, 1, 3, 7),
            Fraction(-3, 7),
        )

    def test_literal_oracle_reproduces_the_shell_fixture(self) -> None:
        oracle = css.oracle_birth_shell_decomposition(
            (0, 1, 4, 6), j0=1, horizon=2
        )
        self.assertEqual(oracle.functional, Fraction(13, 224))
        self.assertEqual(
            tuple(shell.net for shell in oracle.shells),
            (Fraction(13, 392), Fraction(39, 1568)),
        )

    def test_dense_random_search_reaches_long_compatible_rulers(self) -> None:
        first = css.random_dense_greedy_rulers(
            mark_count=16,
            attempts=8,
            scan_limit=400,
            choice_window=4,
            seed=1216,
        )
        second = css.random_dense_greedy_rulers(
            mark_count=16,
            attempts=8,
            scan_limit=400,
            choice_window=4,
            seed=1216,
        )
        self.assertEqual(first, second)
        self.assertGreater(len(first.rulers), 0)
        self.assertTrue(
            any(
                css.critical_envelope_audit(
                    ruler, j0=1, horizon=4, constant=Fraction(2)
                ).compatible
                for ruler in first.rulers
            )
        )

    def test_certificate_is_deterministic_hashed_and_oracle_clean(self) -> None:
        script = Path(__file__).with_name(
            "critical_shell_certificate_2026_08_28.py"
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            first = Path(temporary_directory) / "first.json"
            second = Path(temporary_directory) / "second.json"
            common = [
                sys.executable,
                str(script),
                "--four-max-diameter",
                "7",
                "--eight-min-diameter",
                "34",
                "--eight-max-diameter",
                "34",
                "--random16-attempts",
                "2",
                "--random32-attempts",
                "1",
                "--random-retain",
                "1",
            ]
            for output in (first, second):
                completed = subprocess.run(
                    [*common, "--output", str(output)],
                    cwd=script.parent,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            payload = json.loads(first.read_text())
            recorded_hash = payload.pop("certificate_sha256")
            canonical = json.dumps(
                payload,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode()
            self.assertEqual(hashlib.sha256(canonical).hexdigest(), recorded_hash)
            self.assertEqual(payload["oracle"]["mismatch_count"], 0)
            self.assertEqual(
                payload["exhaustive_four"]["first_failures"]["H1"]["ruler"],
                [0, 1, 4, 6],
            )
            self.assertEqual(
                payload["exhaustive_four"]["first_failures"]["H5"]["ruler"],
                [0, 4, 6, 7],
            )
            self.assertEqual(
                payload["exhaustive_eight"]["per_diameter"][0]["candidate_count"],
                1_107_568,
            )


if __name__ == "__main__":
    unittest.main()

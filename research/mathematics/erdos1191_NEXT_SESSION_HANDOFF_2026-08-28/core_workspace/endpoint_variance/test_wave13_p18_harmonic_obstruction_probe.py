from __future__ import annotations

import json
import tempfile
import unittest
from hashlib import sha256
from pathlib import Path

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave13_p18_harmonic_obstruction_probe import (
    build_certificate,
    erdos_turan_rows,
    new_birth_floor_audit,
    suffix_gap_blocks,
)


class Wave13P18HarmonicObstructionTests(unittest.TestCase):
    def test_suffix_block_indices_and_sizes_are_exact(self) -> None:
        for m in (4, 8, 16, 32, 64):
            with self.subTest(m=m):
                blocks = suffix_gap_blocks(m)
                flattened = tuple(index for block in blocks for index in block)
                self.assertEqual(flattened, tuple(range(m - 1, 2 * m)))
                self.assertEqual(
                    tuple(len(block) for block in blocks),
                    (m // 4, m // 4, m // 4, m // 4 + 1),
                )

    def test_rational_floor_chain_on_authenticated_fixture(self) -> None:
        points = tuple(COUNTEREXAMPLE_64_POINTS)
        for m in (4, 8, 16, 32):
            with self.subTest(m=m):
                audit = new_birth_floor_audit(points, m)
                self.assertEqual(audit.suffix_gap_count, m + 1)
                self.assertEqual(
                    audit.suffix_span,
                    points[2 * m - 1] - points[m - 2],
                )
                self.assertTrue(audit.selected_gaps_distinct)
                self.assertTrue(audit.all_pairs_are_new_birth_pairs)
                self.assertGreaterEqual(
                    audit.minimum_pair_distance, audit.quarter_size + 1
                )
                self.assertGreaterEqual(audit.minimum_far_gap_count, m // 2)
                self.assertTrue(audit.pair_floor_dominates_diameter_floor)
                self.assertTrue(audit.diameter_floor_dominates_far_floor)
                self.assertTrue(audit.diameter_floor_dominates_layered_floor)
                self.assertTrue(audit.observed_layered_energy_dominates_floor)
                self.assertEqual(
                    audit.exact_layered_energy_floor,
                    m * (m - 2) * (m * m + 8 * m + 6) // 48,
                )
                self.assertGreaterEqual(48 * audit.exact_layered_energy_floor, m**4)
                self.assertTrue(audit.layered_floor_dominates_theorem_floor)
                self.assertTrue(audit.pair_floor_dominates_block_floor)
                self.assertTrue(audit.block_floor_dominates_quarter_floor)
                self.assertTrue(audit.floating_value_dominates_rational_pair_floor)

    def test_rational_floor_chain_on_independent_erdos_turan_fixture(self) -> None:
        points = erdos_turan_ruler(128, 257)
        for m in (4, 8, 16, 32, 64):
            with self.subTest(m=m):
                audit = new_birth_floor_audit(points, m)
                self.assertTrue(audit.pair_floor_dominates_diameter_floor)
                self.assertTrue(audit.diameter_floor_dominates_layered_floor)
                self.assertTrue(audit.layered_floor_dominates_theorem_floor)
                self.assertTrue(audit.pair_floor_dominates_block_floor)
                self.assertTrue(audit.block_floor_dominates_quarter_floor)

    def test_erdos_turan_product_floor_is_uniformly_positive(self) -> None:
        rows = erdos_turan_rows()
        self.assertTrue(rows)
        for row in rows:
            with self.subTest(m=row["epoch"]):
                self.assertTrue(row["et_floor_dominates_uniform_floor"])
                self.assertTrue(row["new_birth_value_dominates_et_floor"])

    def test_certificate_is_deterministic_and_self_hashed(self) -> None:
        first = build_certificate()
        second = build_certificate()
        self.assertEqual(first, second)
        internal_hash = first.pop("certificate_sha256")
        canonical = json.dumps(first, sort_keys=True, separators=(",", ":"))
        self.assertEqual(internal_hash, sha256(canonical.encode("utf-8")).hexdigest())
        self.assertTrue(
            first["claim_boundary"][
                "an_existing_eventually_critical_branch_would_violate_p18_conclusion"
            ]
        )
        self.assertFalse(first["claim_boundary"]["p18_unconditionally_disproved"])
        self.assertFalse(first["claim_boundary"]["question_1_resolved"])

        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            output.write_text(
                json.dumps(second, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            reloaded = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(
                json.dumps(reloaded, sort_keys=True),
                json.dumps(second, sort_keys=True),
            )


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import unittest

from wave5_cross_epoch import build_sawtooth_gap_profile
import wave6_arithmetic_mining_search as mining


class Wave6ArithmeticMiningTests(unittest.TestCase):
    def test_four_mark_birth_lag_partition_is_exact(self) -> None:
        points = (0, 1, 4, 6)
        families = mining.birth_lag_families(points)
        keyed = {
            (family.epoch, family.category, family.lag): family
            for family in families
        }
        self.assertEqual(sum(family.demand for family in families), 6)
        self.assertEqual(
            {pair for family in families for pair in family.pairs},
            {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)},
        )
        target = keyed[(4, "ON", 2)]
        self.assertEqual(target.pairs, ((0, 2), (1, 3)))
        self.assertEqual(target.differences, (4, 5))
        self.assertEqual(target.demand, 2)
        self.assertEqual(target.distinct_count, 2)
        self.assertEqual(target.collision_deficit, 0)
        self.assertEqual((target.lower, target.upper, target.width), (4, 5, 2))

    def test_golomb_hall_pressure_is_at_most_one(self) -> None:
        families = mining.birth_lag_families((0, 1, 4, 6))
        audit = mining.hall_pressure(
            families,
            min_family_demand=1,
            min_epoch_count=1,
        )
        self.assertIsNotNone(audit)
        assert audit is not None
        self.assertLessEqual(audit.ratio, Fraction(1))
        brute_ratios = []
        for lower in range(min(row.lower for row in families), 7):
            for upper in range(lower, 7):
                demand = sum(
                    row.demand
                    for row in families
                    if lower <= row.lower and row.upper <= upper
                )
                if demand:
                    brute_ratios.append(Fraction(demand, upper - lower + 1))
        self.assertEqual(audit.ratio, max(brute_ratios))

    def test_sawtooth_two_epoch_nn_pressure_is_exactly_46(self) -> None:
        profile = build_sawtooth_gap_profile(6)
        points = profile.points
        self.assertEqual(profile.smallest_repeated_difference, 8)
        four_mark_audit = mining.audit_arithmetic_witness(
            points[:4], require_golomb=False
        )
        self.assertEqual(
            four_mark_audit.difference_collisions,
            ((14, ((1, 2), (2, 3))),),
        )
        audit = mining.hall_pressure(
            mining.birth_lag_families(points),
            categories=("NN",),
            epochs=(32, 64),
            min_family_demand=2,
            min_epoch_count=2,
        )
        self.assertIsNotNone(audit)
        assert audit is not None
        self.assertEqual(
            (audit.lower, audit.upper, audit.demand, audit.width, audit.ratio),
            (64, 64, 46, 1, Fraction(46)),
        )
        self.assertEqual(
            tuple(
                (family.epoch, family.category, family.lag, family.demand)
                for family in audit.families
            ),
            ((32, "NN", 1, 15), (64, "NN", 1, 31)),
        )
        self.assertTrue(
            all(
                set(family.differences) == {64}
                for family in audit.families
            )
        )

    def test_four_mark_transition_splits_on_and_nn_exactly(self) -> None:
        row = mining.transition_packing((0, 1, 4, 6), new_count=4)
        self.assertEqual(row.old_count, 2)
        self.assertEqual(row.new_count, 4)
        self.assertEqual(row.old_new.pair_count, 4)
        self.assertEqual(row.old_new.differences, (3, 4, 5, 6))
        self.assertEqual(row.new_new.pair_count, 1)
        self.assertEqual(row.new_new.differences, (2,))
        self.assertEqual(row.overlap_width, 0)
        self.assertEqual(row.old_new_occupied_in_overlap, ())
        self.assertEqual(row.new_new_occupied_in_overlap, ())
        self.assertEqual(row.cross_collision_values, ())

    def test_sawtooth_transition_records_actual_cross_collisions(self) -> None:
        points = build_sawtooth_gap_profile(6).points
        row = mining.transition_packing(points, new_count=64)
        self.assertEqual(row.old_new.pair_count, 32 * 32)
        self.assertEqual(row.new_new.pair_count, 32 * 31 // 2)
        self.assertIn(64, row.cross_collision_values)
        self.assertEqual(len(row.cross_collision_values), 31)

    def test_arithmetic_witness_audit_recomputes_every_pair(self) -> None:
        audit = mining.audit_arithmetic_witness((0, 1, 4, 6))
        self.assertTrue(audit.is_golomb)
        self.assertEqual(audit.pair_count, 6)
        self.assertEqual(audit.sorted_differences, (1, 2, 3, 4, 5, 6))
        self.assertEqual(audit.difference_collisions, ())
        self.assertEqual(sum(row.demand for row in audit.families), 6)
        self.assertEqual(len(audit.transitions), 1)
        self.assertEqual(audit.adjacent_nn_pressures, ())

    def test_arithmetic_witness_audit_flags_non_golomb_input(self) -> None:
        audit = mining.audit_arithmetic_witness(
            (0, 1, 2, 4), require_golomb=False
        )
        self.assertFalse(audit.is_golomb)
        self.assertEqual(audit.difference_collisions[0][0], 1)
        with self.assertRaisesRegex(ValueError, "not a Golomb ruler"):
            mining.audit_arithmetic_witness((0, 1, 2, 4))

    def test_wave5_certificate_loader_authenticates_six_witnesses(self) -> None:
        import wave6_arithmetic_mining_certificate as certificate

        path = Path(__file__).with_name(
            "wave5_nested_certificate_2026-08-28.json"
        )
        recorded_hash, witnesses = certificate.load_authenticated_wave5(path)
        self.assertEqual(recorded_hash, certificate.EXPECTED_WAVE5_HASH)
        self.assertEqual(len(witnesses), 6)
        self.assertEqual(
            [(row.objective, row.witness_index) for row in witnesses],
            [
                ("persistence", 0),
                ("persistence", 1),
                ("persistence", 2),
                ("innovation", 0),
                ("innovation", 1),
                ("innovation", 2),
            ],
        )
        self.assertTrue(all(len(row.points) == 64 for row in witnesses))

    def test_committed_certificate_replays_every_retained_witness(self) -> None:
        import wave6_arithmetic_mining_certificate as certificate
        from wave4_nested_search import audit_nested_witness

        directory = Path(__file__).parent
        payload = certificate.load_certificate(
            directory / "wave6_arithmetic_mining_certificate_2026-08-28.json"
        )
        def contains_float(value: object) -> bool:
            if isinstance(value, float):
                return True
            if isinstance(value, dict):
                return any(contains_float(item) for item in value.values())
            if isinstance(value, list):
                return any(contains_float(item) for item in value)
            return False

        self.assertFalse(contains_float(payload))
        self.assertEqual(
            payload["reproducibility"]["source_sha256"],
            certificate.source_hashes(),
        )
        wave5_hash, _ = certificate.load_authenticated_wave5(
            directory / payload["wave5_input"]["filename"]
        )
        self.assertEqual(
            wave5_hash,
            payload["wave5_input"]["internal_certificate_sha256"],
        )
        records = payload["sixty_four_mark_witnesses"]
        self.assertEqual(len(records), 6)
        for record in records:
            stored = record["arithmetic_audit"]
            points = tuple(stored["points"])
            arithmetic = mining.audit_arithmetic_witness(points)
            self.assertEqual(
                certificate.arithmetic_audit_payload(arithmetic), stored
            )
            nested = audit_nested_witness(
                points, sizes=(4, 8, 16, 32, 64), constant=Fraction(1)
            )
            self.assertEqual(
                certificate._nested_payload(nested),
                record["nested_prefix_audit"],
            )

        sawtooth = payload["sawtooth_64_control"]
        self.assertTrue(sawtooth["explicitly_non_sidon"])
        self.assertEqual(sawtooth["smallest_repeated_difference"], 8)
        self.assertEqual(
            certificate.arithmetic_audit_payload(
                mining.audit_arithmetic_witness(
                    tuple(sawtooth["arithmetic_audit"]["points"]),
                    require_golomb=False,
                )
            ),
            sawtooth["arithmetic_audit"],
        )

        extension = payload["heuristic_extension_128"]
        stored = extension["arithmetic_audit"]
        points = tuple(stored["points"])
        self.assertEqual(len(points), 128)
        arithmetic = mining.audit_arithmetic_witness(points)
        self.assertEqual(certificate.arithmetic_audit_payload(arithmetic), stored)
        nested = audit_nested_witness(
            points,
            sizes=(4, 8, 16, 32, 64, 128),
            constant=Fraction(1),
        )
        self.assertTrue(nested.envelope_compatible)
        self.assertEqual(nested.difference_audit.pair_count, 8128)
        self.assertEqual(
            certificate._nested_payload(nested),
            extension["nested_prefix_audit"],
        )

    def test_finite_scaled_pressure_candidate_separates_saved_data(self) -> None:
        import wave6_arithmetic_mining_certificate as certificate

        payload = certificate.load_certificate(
            Path(__file__).with_name(
                "wave6_arithmetic_mining_certificate_2026-08-28.json"
            )
        )
        golomb_audits = [
            row["arithmetic_audit"]
            for row in payload["sixty_four_mark_witnesses"]
        ]
        golomb_audits.append(
            payload["heuristic_extension_128"]["arithmetic_audit"]
        )
        for audit in golomb_audits:
            for row in audit["adjacent_nn_hall_pressure"]:
                older_epoch = row["epochs"][0]
                ratio = Fraction(row["pressure"]["ratio"])
                self.assertLessEqual(16 * older_epoch * ratio * ratio, 1)

        sawtooth_rows = payload["sawtooth_64_control"][
            "arithmetic_audit"
        ]["adjacent_nn_hall_pressure"]
        self.assertTrue(
            all(
                16
                * row["epochs"][0]
                * Fraction(row["pressure"]["ratio"]) ** 2
                > 1
                for row in sawtooth_rows
            )
        )


if __name__ == "__main__":
    unittest.main()

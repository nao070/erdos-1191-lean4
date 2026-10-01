from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from itertools import product
from pathlib import Path

import endpoint_variance as ev


def _oracle_gap_compositions(total: int, parts: int):
    for gaps in product(range(1, total + 1), repeat=parts):
        if sum(gaps) == total:
            yield gaps


def _oracle_golomb_rulers(mark_count: int, diameter: int):
    rulers = []
    for gaps in _oracle_gap_compositions(diameter, mark_count - 1):
        contiguous_sums = [
            sum(gaps[i:j])
            for i in range(len(gaps))
            for j in range(i + 1, len(gaps) + 1)
        ]
        if len(contiguous_sums) != len(set(contiguous_sums)):
            continue
        marks = [0]
        for gap in gaps:
            marks.append(marks[-1] + gap)
        rulers.append(tuple(marks))
    return tuple(rulers)


def _oracle_offset_variance(points: tuple[int, ...], modulus: int) -> Fraction:
    crossing_counts = []
    for boundary in range(modulus):
        cut_pairs = 0
        for i, left in enumerate(points):
            for right in points[i + 1 :]:
                if (left - boundary) // modulus != (right - boundary) // modulus:
                    cut_pairs += 1
        crossing_counts.append(cut_pairs)
    mean = Fraction(sum(crossing_counts), modulus)
    return sum((Fraction(value) - mean) ** 2 for value in crossing_counts) / modulus


class GolombVarianceTests(unittest.TestCase):
    def test_gap_vector_to_ruler_accumulates_positive_gaps(self) -> None:
        convert = getattr(ev, "gap_vector_to_ruler", lambda _gaps: None)
        self.assertEqual(convert((1, 3, 2)), (0, 1, 4, 6))

    def test_contiguous_gap_sums_characterize_golomb_rulers(self) -> None:
        is_golomb = getattr(
            ev,
            "has_distinct_contiguous_gap_sums",
            lambda _gaps: False,
        )
        self.assertTrue(is_golomb((1, 3, 2)))
        self.assertFalse(is_golomb((1, 1)))

    def test_gap_vector_rejects_nonpositive_or_noninteger_entries(self) -> None:
        with self.assertRaises(ValueError):
            ev.gap_vector_to_ruler((1, 0, 2))
        with self.assertRaises(TypeError):
            ev.gap_vector_to_ruler((1, 2.5))

    def test_exact_enumerator_covers_all_six_unit_four_mark_rulers(self) -> None:
        enumerate_rulers = getattr(
            ev,
            "iter_normalized_golomb_rulers",
            lambda _mark_count, _diameter: (),
        )
        candidate_count = getattr(
            ev,
            "normalized_ruler_candidate_count",
            lambda _mark_count, _diameter: None,
        )
        self.assertEqual(candidate_count(4, 6), 10)
        self.assertEqual(
            tuple(enumerate_rulers(4, 6)),
            ((0, 1, 4, 6), (0, 2, 5, 6)),
        )

    def test_reflection_canonicalizes_the_only_length_six_class(self) -> None:
        canonicalize = getattr(
            ev,
            "canonical_reflection_ruler",
            lambda ruler: tuple(ruler),
        )
        self.assertEqual(canonicalize((0, 1, 4, 6)), (0, 1, 4, 6))
        self.assertEqual(canonicalize((0, 2, 5, 6)), (0, 1, 4, 6))

    def test_exact_minimum_records_counts_minimizers_and_symmetry(self) -> None:
        minimize = getattr(ev, "golomb_variance_minimum", lambda *_args: None)
        result = minimize(4, 6, 7)
        self.assertIsNotNone(result)
        self.assertEqual(result.candidate_count, 10)
        self.assertEqual(result.golomb_ruler_count, 2)
        self.assertEqual(result.minimum_variance, Fraction(12, 7))
        self.assertEqual(
            result.minimizers,
            ((0, 1, 4, 6), (0, 2, 5, 6)),
        )
        self.assertEqual(result.reflection_classes, ((0, 1, 4, 6),))

    def test_exhaustive_engine_and_gap_formula_match_independent_oracle(self) -> None:
        for mark_count in range(2, 6):
            for diameter in range(mark_count - 1, 13):
                with self.subTest(mark_count=mark_count, diameter=diameter):
                    expected_rulers = _oracle_golomb_rulers(mark_count, diameter)
                    self.assertEqual(
                        tuple(ev.iter_normalized_golomb_rulers(mark_count, diameter)),
                        expected_rulers,
                    )
                    for modulus in (diameter + 1, diameter + 2):
                        result = ev.golomb_variance_minimum(
                            mark_count,
                            diameter,
                            modulus,
                        )
                        oracle_values = [
                            _oracle_offset_variance(ruler, modulus)
                            for ruler in expected_rulers
                        ]
                        expected_minimum = min(oracle_values, default=None)
                        expected_minimizers = tuple(
                            ruler
                            for ruler, value in zip(expected_rulers, oracle_values)
                            if value == expected_minimum
                        )
                        self.assertEqual(result.minimum_variance, expected_minimum)
                        self.assertEqual(result.minimizers, expected_minimizers)

    def test_dated_certificate_is_deterministic_and_self_authenticating(self) -> None:
        script = Path(__file__).with_name(
            "golomb_variance_certificate_2026_08_28.py"
        )
        with tempfile.TemporaryDirectory() as temporary_directory:
            first = Path(temporary_directory) / "first.json"
            second = Path(temporary_directory) / "second.json"
            common = [
                sys.executable,
                str(script),
                "--max-marks",
                "5",
                "--max-diameter",
                "12",
                "--oracle-max-marks",
                "5",
                "--oracle-max-diameter",
                "12",
            ]
            first_run = subprocess.run(
                [*common, "--output", str(first)],
                cwd=script.parent,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(first_run.returncode, 0, first_run.stderr)
            second_run = subprocess.run(
                [*common, "--output", str(second)],
                cwd=script.parent,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(second_run.returncode, 0, second_run.stderr)
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
            mandatory = payload["mandatory_instances"]
            self.assertEqual(mandatory["zero_mode"]["variance"], "0")
            self.assertEqual(mandatory["modular_cycle_union"]["cycle_count"], 2)
            self.assertEqual(
                mandatory["homometric_pair"]["modulus_14_variances"],
                ["79/28", "55/28"],
            )


if __name__ == "__main__":
    unittest.main()

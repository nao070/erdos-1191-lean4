from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
from random import Random
import subprocess
import sys
import tempfile
import unittest

import wave5_nested_search as wave5


class Wave5NestedTests(unittest.TestCase):
    def test_candidate_budget_one_returns_exactly_one_valid_choice(self) -> None:
        # Catches selecting both flanks (and a negative slice of the middle)
        # when the per-state candidate budget is the minimum valid value.
        points = (0, 1, 4, 6)
        state = wave5._ExtensionState(
            marks=points,
            differences=wave5._all_differences(points),
            parent_index=0,
        )
        choices = wave5._extension_choices(
            state,
            maximum=100,
            budget=1,
            generator=Random(501191),
        )
        self.assertEqual(choices, ((13, (13, 12, 9, 7)),))

    def test_reset_profile_records_signed_location_not_only_norm(self) -> None:
        # Catches swapping old/shell signs, dropping the h_0=1 atom, or
        # reporting an epsilon without the location of its signed extremum.
        profile = wave5.reset_profile((0, 1, 4, 6), old_count=2)
        self.assertEqual(profile.signed_cells, (Fraction(1, 10), Fraction(-1, 10)))
        self.assertEqual(profile.cumulative, (Fraction(1, 10), Fraction(0)))
        self.assertEqual(profile.maximum_absolute_cumulative, Fraction(1, 10))
        self.assertEqual(profile.extremum_boundary, Fraction(1, 2))
        self.assertEqual(profile.extremum_sign, 1)
        self.assertEqual(profile.l1_mass, Fraction(1, 5))

    def test_cross_epoch_persistence_coarsens_cells_with_sign(self) -> None:
        # Catches comparing unequal grids cell-by-cell or taking absolute
        # values before distinguishing aligned from opposed discrepancy.
        coarse = (Fraction(1, 10), Fraction(-1, 10))
        aligned_fine = (
            Fraction(1, 20),
            Fraction(1, 20),
            Fraction(-1, 20),
            Fraction(-1, 20),
        )
        aligned = wave5.compare_signed_profiles(coarse, aligned_fine)
        self.assertEqual(aligned.coarsened_fine, coarse)
        self.assertEqual(aligned.aligned_mass, Fraction(1, 5))
        self.assertEqual(aligned.opposed_mass, 0)
        self.assertEqual(aligned.normalized_signed_overlap, 1)

        opposed = wave5.compare_signed_profiles(
            coarse, tuple(-value for value in aligned_fine)
        )
        self.assertEqual(opposed.aligned_mass, 0)
        self.assertEqual(opposed.opposed_mass, Fraction(1, 5))
        self.assertEqual(opposed.normalized_signed_overlap, -1)

    def test_history_preserves_extremum_location_and_coarse_sign_alignment(self) -> None:
        # At 2->4 the largest cumulative discrepancy is positive at 1/2;
        # at 4->8 it is negative at 3/4.  Nevertheless pair-coarsening the
        # second signed profile gives the same coarse sign pattern.
        points = (0, 2, 5, 6, 28, 36, 43, 75)
        history = wave5.dyadic_reset_history(points, sizes=(4, 8))
        self.assertEqual(
            tuple(profile.extremum_boundary for profile in history.profiles),
            (Fraction(1, 2), Fraction(3, 4)),
        )
        self.assertEqual(
            tuple(profile.extremum_sign for profile in history.profiles),
            (1, -1),
        )
        self.assertEqual(
            history.profiles[1].signed_cells,
            (
                Fraction(85, 483),
                Fraction(-82, 483),
                Fraction(-158, 483),
                Fraction(155, 483),
            ),
        )
        self.assertEqual(history.persistence[0].normalized_signed_overlap, 1)

    def test_seeded_extension_keeps_parent_and_reaudits_every_prefix(self) -> None:
        # Catches restarting from zero, accepting a search-state-only Golomb
        # check, or checking the C=1 envelope only at the final size.
        parent = (0, 2, 5, 6, 28, 36, 43, 75)
        arguments = dict(
            parents=(parent,),
            sizes=(4, 8, 16),
            constant=Fraction(1),
            objective="persistence",
            beam_width=16,
            candidates_per_state=12,
            seed=501191,
            retain=2,
        )
        first = wave5.beam_extend_nested(**arguments)
        second = wave5.beam_extend_nested(**arguments)
        self.assertEqual(first, second)
        self.assertEqual(first.retain, 2)
        self.assertGreater(len(first.witnesses), 0)
        for witness in first.witnesses:
            self.assertEqual(witness.points[: len(parent)], parent)
            self.assertEqual(len(witness.points), 16)
            self.assertTrue(witness.nested_audit.difference_audit.is_golomb)
            self.assertTrue(witness.nested_audit.envelope_compatible)
            self.assertEqual(len(witness.nested_audit.envelope_rows), 15)
            self.assertEqual(witness.history.sizes, (4, 8, 16))
            self.assertEqual(
                witness.final_innovation_q00_per_modulus,
                witness.nested_audit.rows[-1].innovation_q00_per_modulus,
            )

    def test_certificate_is_deterministic_and_keeps_full_signed_profiles(self) -> None:
        # Catches serializing only scalar profile norms, omitting pair
        # differences, accepting a stale/corrupt Wave 4 parent certificate,
        # or hiding the generator defaults/runtime behind an ambient process.
        script = Path(__file__).with_name("wave5_nested_certificate.py")
        source = Path(__file__).with_name("wave4_nested_certificate_2026-08-28.json")
        with tempfile.TemporaryDirectory() as temporary_directory:
            outputs = [Path(temporary_directory) / name for name in ("a.json", "b.json")]
            common = [
                sys.executable,
                str(script),
                "--wave4-certificate",
                str(source),
                "--beam-width",
                "4",
                "--candidates-per-state",
                "4",
                "--seeds",
                "501191,502191",
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
            self.assertEqual(payload["schema"], "wave5_nested_extension_certificate_v2")
            self.assertEqual(payload["retain"], 3)
            reproducibility = payload["reproducibility"]
            self.assertEqual(
                reproducibility["canonical_byte_identity_scope"],
                "recorded_python_runtime_only",
            )
            self.assertEqual(
                reproducibility["python_implementation"],
                platform.python_implementation(),
            )
            self.assertEqual(
                reproducibility["python_version"], platform.python_version()
            )
            self.assertEqual(
                reproducibility["source_sha256"],
                {
                    name: hashlib.sha256(script.with_name(name).read_bytes()).hexdigest()
                    for name in (
                        "wave5_nested_search.py",
                        "wave5_nested_certificate.py",
                        "wave4_nested_search.py",
                        "gap_measure_dynamics.py",
                        "sidon_block_variance.py",
                        "endpoint_variance.py",
                    )
                },
            )

            def assert_exact_json(value: object) -> None:
                self.assertNotIsInstance(value, float)
                if isinstance(value, dict):
                    self.assertFalse(
                        any(key.endswith("_decimal") for key in value), value.keys()
                    )
                    for child in value.values():
                        assert_exact_json(child)
                elif isinstance(value, list):
                    for child in value:
                        assert_exact_json(child)

            assert_exact_json(payload)
            for run in payload["runs"]:
                self.assertEqual(run["retain"], 3)
                self.assertEqual(len(run["witnesses"]), 3)
                witness = run["witnesses"][0]
                self.assertEqual(len(witness["all_positive_differences"]), 2016)
                self.assertEqual(
                    len(set(witness["all_positive_differences"])), 2016
                )
                self.assertEqual(len(witness["all_prefix_envelope_rows"]), 63)
                self.assertTrue(
                    all(row["certified"] for row in witness["all_prefix_envelope_rows"])
                )
                self.assertEqual(
                    [profile["new_count"] for profile in witness["reset_profiles"]],
                    [4, 8, 16, 32, 64],
                )
                for profile in witness["reset_profiles"]:
                    self.assertEqual(
                        len(profile["signed_cells"]), profile["old_count"]
                    )
                    self.assertEqual(
                        len(profile["cumulative"]), profile["old_count"]
                    )

    def test_committed_certificate_hash_and_source_metadata_validate(self) -> None:
        # Catches committing a stale JSON artifact after changing either
        # generator source, or updating its payload without its internal hash.
        directory = Path(__file__).parent
        certificate = directory / "wave5_nested_certificate_2026-08-28.json"
        payload = json.loads(certificate.read_text())
        recorded_hash = payload.pop("certificate_sha256")
        canonical = json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        ).encode()
        self.assertEqual(hashlib.sha256(canonical).hexdigest(), recorded_hash)
        self.assertEqual(
            payload["reproducibility"]["source_sha256"],
            {
                name: hashlib.sha256((directory / name).read_bytes()).hexdigest()
                for name in (
                    "wave5_nested_search.py",
                    "wave5_nested_certificate.py",
                    "wave4_nested_search.py",
                    "gap_measure_dynamics.py",
                    "sidon_block_variance.py",
                    "endpoint_variance.py",
                )
            },
        )


if __name__ == "__main__":
    unittest.main()

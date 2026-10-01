from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from hashlib import sha256
from math import comb
from pathlib import Path

import wave19_sparse_spike_certificate as certificate
import wave19_sparse_spike_search as search


class Wave19SparseSpikeCertificateTests(unittest.TestCase):
    def test_literal_32_mark_root_and_scaled_et_block(self) -> None:
        self.assertEqual(len(certificate.A32), 32)
        self.assertEqual(certificate.A32[-1], 7096)
        self.assertEqual(
            certificate.csv_sha256(certificate.A32),
            "453085605c07dea071c2c5e1bb8d9d90e6a3886a0f3ed1665ef0e84f18586e68",
        )
        self.assertEqual(len(certificate.ET95), 95)
        self.assertEqual(certificate.ET95[:4], (0, 2863, 5397, 7602))
        self.assertEqual(certificate.ET95[-1], 228557)
        self.assertEqual(
            certificate.ET95,
            tuple(
                7 * (346 * index + (63 * index * index) % 173) for index in range(95)
            ),
        )
        self.assertEqual(
            certificate.csv_sha256(certificate.ET95),
            "9f2d5b77e2c9335aeba714d701d95ac5c9154797c824a0dfa859555c46a2f90d",
        )

        root_differences = certificate.positive_differences(certificate.A32)
        block_differences = certificate.positive_differences(certificate.ET95)
        self.assertEqual(len(root_differences), comb(32, 2))
        self.assertEqual(len(set(root_differences)), comb(32, 2))
        self.assertEqual(len(block_differences), comb(95, 2))
        self.assertEqual(len(set(block_differences)), comb(95, 2))
        self.assertEqual(
            certificate.csv_sha256(root_differences),
            "882e53653e3733ad3e5fbdf05b61b7177fd0835b1efe433961c0d52a27d30a04",
        )
        self.assertEqual(
            certificate.csv_sha256(block_differences),
            "e803edf53e8f67e50429e82b52b491a3d03228653faa46a0102aab8f8e3e68c3",
        )

    def test_separated_union_partition_is_exact(self) -> None:
        self.assertEqual(certificate.TRANSLATION, 235654)
        self.assertEqual(
            certificate.TRANSLATION,
            certificate.A32[-1] + certificate.ET95[-1] + 1,
        )
        self.assertEqual(len(certificate.SEPARATED_UNION), 127)
        self.assertEqual(certificate.SEPARATED_UNION[-1], 464211)

        audit = certificate.separated_union_audit()
        self.assertEqual(audit["root_internal_count"], 496)
        self.assertEqual(audit["block_internal_count"], 4465)
        self.assertEqual(audit["cross_count"], 3040)
        self.assertEqual(audit["total_difference_count"], 8001)
        self.assertEqual(audit["distinct_difference_count"], 8001)
        self.assertEqual(audit["largest_internal_difference"], 228557)
        self.assertEqual(audit["smallest_cross_difference"], 228558)
        self.assertTrue(audit["all_partition_checks_pass"])
        self.assertEqual(
            audit["difference_sha256"],
            "20c9b39f25e220d35b31c12c40beb96598e5df527e203e780c5683f891d7c7db",
        )

    def test_primary_128_witness_all_differences_cap_and_csv_sha(self) -> None:
        points = certificate.PRIMARY_WITNESS
        self.assertEqual(len(points), 128)
        self.assertEqual(points[-1], 5087721)
        differences = certificate.positive_differences(points)
        self.assertEqual(len(differences), 8128)
        self.assertEqual(len(set(differences)), 8128)
        self.assertEqual(
            certificate.csv_sha256(differences),
            "dfd2b62ff0b1494727177b26f1ffb61108ff077a0ffbeb627dea072a255c4ff3",
        )
        self.assertEqual(
            certificate.csv_sha256(points),
            "ec7965ccb5c05c0cfcf68900153f09f37ca39f94f9601f0b2b67c29cfacaf373",
        )

        cap_rows = certificate.prefix_cap_audit(points)
        self.assertEqual(len(cap_rows), 127)
        self.assertTrue(all(row["passes"] for row in cap_rows))
        self.assertEqual(cap_rows[-1]["mark_count"], 128)
        self.assertEqual(cap_rows[-1]["certified_cap"], 5087722)
        self.assertEqual(cap_rows[-1]["terminal_plus_one"], 5087722)
        self.assertEqual(cap_rows[-1]["integer_slack"], 0)

    def test_cap_floor_uses_a_rational_log_enclosure(self) -> None:
        expected = {
            2: 177,
            33: 243692,
            128: 5087722,
            129: 5175816,
            255: 23060522,
            256: 23258159,
        }
        for mark_count, cap in expected.items():
            with self.subTest(mark_count=mark_count):
                row = certificate.critical_cap_audit(mark_count)
                self.assertEqual(row["certified_cap"], cap)
                self.assertEqual(row["lower_floor"], cap)
                self.assertEqual(row["upper_floor"], cap)
                self.assertTrue(row["floor_uniquely_certified"])
                self.assertEqual(certificate.critical_cap(mark_count), cap)

    def test_descendant_jump_values_match_reported_binary64_values(self) -> None:
        reported_primary = {
            4: 0.002078576661344486,
            8: 0.06999594179639168,
            16: 0.02824820609231238,
            32: 0.0,
            64: 0.31393714841781556,
        }
        for epoch, reported in reported_primary.items():
            with self.subTest(epoch=epoch):
                row = certificate.descendant_jump_audit(
                    certificate.PRIMARY_WITNESS, epoch, reported
                )
                self.assertLess(row["absolute_binary64_error"], 1e-15)
                self.assertTrue(row["reported_value_matches_projection"])
                self.assertTrue(row["transcendental_projection_only"])
        self.assertEqual(
            str(certificate.descendant_jump_value(certificate.PRIMARY_WITNESS, 4))[:20],
            "0.002078576661344487",
        )
        self.assertEqual(
            str(certificate.descendant_jump_value(certificate.PRIMARY_WITNESS, 64))[
                :20
            ],
            "0.313937148417815519",
        )

    def test_reserve_terminal_is_exact_and_has_claimed_next_prefix_slack(self) -> None:
        points = certificate.RESERVE_WITNESS
        self.assertEqual(len(points), 128)
        self.assertEqual(points[-1], 1271930)
        differences = certificate.positive_differences(points)
        self.assertEqual(len(set(differences)), 8128)
        self.assertEqual(
            certificate.csv_sha256(differences),
            "e1b90baa94d7822da894824976c316cebf106fa797bc78e4ad4677d0be7d2f7d",
        )
        self.assertTrue(
            all(row["passes"] for row in certificate.prefix_cap_audit(points))
        )
        self.assertEqual(certificate.critical_cap(129) - (points[-1] + 1), 3903885)
        row = certificate.descendant_jump_audit(points, 64, 0.06891061854425407)
        self.assertLess(row["absolute_binary64_error"], 1e-15)
        self.assertTrue(row["reported_value_matches_projection"])

    def test_exhaustive_one_step_discriminator_counts_complete_domain(self) -> None:
        primary = search.exhaustive_next_mark_scan(certificate.PRIMARY_WITNESS)
        self.assertEqual(primary.minimum_candidate, 5087722)
        self.assertEqual(primary.maximum_candidate, 5175815)
        self.assertEqual(primary.domain_size, 88094)
        self.assertEqual(primary.forbidden_count, 3249)
        self.assertEqual(primary.allowed_count, 84845)
        self.assertEqual(primary.first_allowed, 5087755)
        self.assertTrue(primary.exhaustive_for_fixed_prefix_and_cap)

        reserve = search.exhaustive_next_mark_scan(certificate.RESERVE_WITNESS)
        self.assertEqual(reserve.domain_size, 3903885)
        self.assertEqual(reserve.forbidden_count, 8128)
        self.assertEqual(reserve.allowed_count, 3895757)
        self.assertEqual(reserve.first_allowed, 1271964)
        self.assertTrue(reserve.exhaustive_for_fixed_prefix_and_cap)

    def test_deterministic_greedy_search_constructs_exact_255_and_256_mark_witnesses(
        self,
    ) -> None:
        expected = {
            "primary": {
                "points": certificate.PRIMARY_WITNESS,
                "end_255": 5192189,
                "end_256": 5192370,
                "marks_255_sha": "78e4961fea307dee95bf7d8086f987e9b4ac653970e7006c7a2f0d4ff4213a3a",
                "marks_256_sha": "b250a53ef2532e4e45f0aeed8021b97b7c37c1180b57088da8d557179091adb8",
                "differences_255_sha": "61e19b78536607c0b780cd33044f8281f0707750c767782a57eefd4acc1f47cf",
                "differences_256_sha": "2696e033857455359f03f9b7639ded516695ebe2dff4aa1263a04b90ebe1c0e0",
            },
            "reserve": {
                "points": certificate.RESERVE_WITNESS,
                "end_255": 1376398,
                "end_256": 1376579,
                "marks_255_sha": "5ea6a222e5b2599154f1715db79a43d990feaaa823c13dd9da0a699983bee130",
                "marks_256_sha": "10145a6470d236b806f9a60dae26bc7e1b52277d690bbec4c7097997319f1530",
                "differences_255_sha": "acb8e8fee07ad2f6802e59d3a4965e54c59acf79af2b99cc380544cf4662d5d0",
                "differences_256_sha": "945f61374b962b1903b7f553afd3e236c9fce02d6a80cb194b12499064bfa897",
            },
        }
        for label, values in expected.items():
            with self.subTest(label=label):
                result = search.greedy_extend(values["points"], 256)
                self.assertTrue(result.completed)
                self.assertEqual(result.points[254], values["end_255"])
                self.assertEqual(result.points[255], values["end_256"])
                self.assertEqual(result.total_candidates_tested, 104649)
                self.assertEqual(max(result.stage_candidate_counts), 5241)
                self.assertEqual(result.stage_candidate_counts.index(5241) + 129, 223)
                self.assertEqual(
                    certificate.csv_sha256(result.points[:255]), values["marks_255_sha"]
                )
                self.assertEqual(
                    certificate.csv_sha256(result.points), values["marks_256_sha"]
                )
                differences_255 = certificate.positive_differences(result.points[:255])
                differences_256 = certificate.positive_differences(result.points)
                self.assertEqual(len(set(differences_255)), comb(255, 2))
                self.assertEqual(len(set(differences_256)), comb(256, 2))
                self.assertEqual(
                    certificate.csv_sha256(differences_255),
                    values["differences_255_sha"],
                )
                self.assertEqual(
                    certificate.csv_sha256(differences_256),
                    values["differences_256_sha"],
                )
                self.assertTrue(
                    all(
                        row["passes"]
                        for row in certificate.prefix_cap_audit(result.points)
                    )
                )
                self.assertFalse(result.global_search_exhaustive)
                self.assertTrue(result.each_step_first_legal_is_exhaustive)
                self.assertEqual(result.scope, "finite constructive witness only")

    def test_stage_256_terminal_maximum_is_exhaustively_certified(self) -> None:
        expected = {
            "primary": {
                "base": certificate.PRIMARY_WITNESS,
                "core_terminal": 5192189,
                "domain_size": 18065969,
                "shadow_upper": 10384378,
                "marks_sha": "4254c6af1ddc0d30e472ec42353b1f7cc9a4fe279e9eaf5bdfd1b25e128643c7",
                "differences_sha": "470771223038ada2c60858096d0aa9cab6bc97eee8d49811055540254e0cbe28",
                "J128_prefix": "0.012725168443812638484230961611",
            },
            "reserve": {
                "base": certificate.RESERVE_WITNESS,
                "core_terminal": 1376398,
                "domain_size": 21881760,
                "shadow_upper": 2752796,
                "marks_sha": "c81e6a65e3164d7da3cf6c70b2c587ab8e4c309c0221c94cf9266a0fcceab4c6",
                "differences_sha": "21344b8e7e0f337e31f5407fd6ab7d7e5ed9ed3ab3442473b3400846a55cb52c",
                "J128_prefix": "0.309186077177781620406421383370",
            },
        }
        for label, values in expected.items():
            with self.subTest(label=label):
                greedy = search.greedy_extend(values["base"], 256)
                core = greedy.points[:255]
                result = search.maximize_next_terminal(core)
                self.assertEqual(core[-1], values["core_terminal"])
                self.assertEqual(result.selected_terminal, 23258158)
                self.assertEqual(result.points[-1] + 1, certificate.critical_cap(256))
                self.assertEqual(result.domain_size, values["domain_size"])
                self.assertEqual(
                    result.forbidden_shadow_upper_bound, values["shadow_upper"]
                )
                self.assertGreater(
                    result.selected_terminal, result.forbidden_shadow_upper_bound
                )
                self.assertEqual(result.selected_blocker_count, 0)
                self.assertEqual(result.candidates_examined_descending, 1)
                self.assertTrue(result.selection_exhaustive_for_maximum)
                self.assertFalse(result.full_domain_classified)
                self.assertTrue(result.cap_maximum_selected)
                self.assertEqual(
                    certificate.csv_sha256(result.points), values["marks_sha"]
                )
                differences = certificate.positive_differences(result.points)
                self.assertEqual(len(set(differences)), comb(256, 2))
                self.assertEqual(
                    certificate.csv_sha256(differences), values["differences_sha"]
                )
                self.assertTrue(
                    all(
                        row["passes"]
                        for row in certificate.prefix_cap_audit(result.points)
                    )
                )
                self.assertTrue(
                    str(
                        certificate.descendant_jump_value(result.points, 128)
                    ).startswith(values["J128_prefix"])
                )

    def test_better_256_prefix_cools_to_511_and_has_exact_maximal_512_spike(
        self,
    ) -> None:
        reserve_greedy = search.greedy_extend(certificate.RESERVE_WITNESS, 256)
        optimized_256 = search.maximize_next_terminal(reserve_greedy.points[:255])
        cooldown = search.greedy_extend(optimized_256.points, 511)
        self.assertTrue(cooldown.completed)
        self.assertEqual(cooldown.points[-1], 24032260)
        self.assertEqual(cooldown.total_candidates_tested, 774102)
        self.assertEqual(max(cooldown.stage_candidate_counts), 15707)
        self.assertEqual(
            cooldown.stage_candidate_counts.index(15707) + 257,
            456,
        )
        self.assertEqual(
            certificate.csv_sha256(cooldown.points),
            "7817c391cb7a33540dcba164805e88411132cf5fa0f4ccff8313e0da13a0e36b",
        )
        self.assertEqual(
            certificate.csv_sha256(certificate.positive_differences(cooldown.points)),
            "ff3b462cf0bd4c47faba92562d9b71b26e01b9af0ebe28d2fbd724e8924e8ab3",
        )
        self.assertFalse(cooldown.global_search_exhaustive)
        self.assertTrue(cooldown.each_step_first_legal_is_exhaustive)

        optimized_512 = search.maximize_next_terminal(cooldown.points)
        self.assertEqual(optimized_512.selected_terminal, 104661718)
        self.assertEqual(optimized_512.points[-1] + 1, certificate.critical_cap(512))
        self.assertEqual(optimized_512.domain_size, 80629458)
        self.assertEqual(optimized_512.forbidden_shadow_upper_bound, 48064520)
        self.assertEqual(optimized_512.candidates_examined_descending, 1)
        self.assertTrue(optimized_512.selection_exhaustive_for_maximum)
        self.assertFalse(optimized_512.full_domain_classified)
        self.assertEqual(
            certificate.csv_sha256(optimized_512.points),
            "9721cbfaa645e96e73283b37d7c476d4a9286799ac2197da40ed1cac79b2ae63",
        )
        differences = certificate.positive_differences(optimized_512.points)
        self.assertEqual(len(differences), 130816)
        self.assertEqual(len(set(differences)), 130816)
        self.assertEqual(
            certificate.csv_sha256(differences),
            "cdad53cb4928712573069e30708d7d354f76302cdb355329a9711759ebb6a7f4",
        )
        self.assertTrue(
            all(
                row["passes"]
                for row in certificate.prefix_cap_audit(optimized_512.points)
            )
        )
        self.assertTrue(
            str(
                certificate.descendant_jump_value(optimized_512.points, 256)
            ).startswith("0.005709533721666033398346642563")
        )

    def test_certificate_is_deterministic_self_hashed_and_scoped(self) -> None:
        first = certificate.build_certificate()
        second = certificate.build_certificate()
        self.assertEqual(first, second)
        self.assertTrue(first["all_required_checks_pass"])
        unhashed = dict(first)
        recorded = unhashed.pop("certificate_sha256")
        canonical = json.dumps(unhashed, sort_keys=True, separators=(",", ":"))
        self.assertEqual(recorded, sha256(canonical.encode("utf-8")).hexdigest())
        self.assertEqual(
            first["scope_flags"],
            {
                "finite_witnesses_exactly_verified": True,
                "one_step_scan_exhaustive_for_each_fixed_prefix": True,
                "greedy_extension_global_search_exhaustive": False,
                "greedy_255_and_256_witnesses_exactly_verified": True,
                "stage_256_terminal_maximization_exhaustive": True,
                "cooldown_to_511_global_search_exhaustive": False,
                "stage_512_terminal_maximization_exhaustive": True,
                "optimized_512_witness_exactly_verified": True,
                "optimality_claimed": False,
                "infinite_extension_claimed": False,
                "p23_refuted": False,
                "question_1_resolved": False,
                "question_2_resolved": False,
                "erdos_1191_resolved": False,
            },
        )

    def test_cli_byte_replay_matches_committed_certificate(self) -> None:
        script = Path(__file__).with_name("wave19_sparse_spike_certificate.py")
        with tempfile.TemporaryDirectory() as temporary_directory:
            output = Path(temporary_directory) / "certificate.json"
            completed = subprocess.run(
                [sys.executable, str(script), "--output", str(output)],
                cwd=script.parent,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertTrue(certificate.DEFAULT_OUTPUT.exists())
            self.assertEqual(
                output.read_bytes(), certificate.DEFAULT_OUTPUT.read_bytes()
            )

    def test_invalid_inputs_are_rejected(self) -> None:
        for points in ((0,), (0, 1, 1), (0, 3, 2), (0, 1.5)):
            with (
                self.subTest(points=points),
                self.assertRaises((TypeError, ValueError)),
            ):
                certificate.positive_differences(points)  # type: ignore[arg-type]
        for bad in (True, 1, 3.0, "4"):
            with self.subTest(bad=bad), self.assertRaises((TypeError, ValueError)):
                certificate.critical_cap(bad)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            certificate.descendant_jump_value(certificate.A32, 32)
        with self.assertRaises(ValueError):
            search.greedy_extend(certificate.PRIMARY_WITNESS, 127)


if __name__ == "__main__":
    unittest.main()

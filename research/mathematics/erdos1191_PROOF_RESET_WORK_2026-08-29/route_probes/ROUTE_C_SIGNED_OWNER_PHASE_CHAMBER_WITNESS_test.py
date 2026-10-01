from __future__ import annotations

import importlib
import importlib.util
import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


MODULE = "ROUTE_C_SIGNED_OWNER_PHASE_CHAMBER_WITNESS_certificate"


class SignedOwnerPhaseChamberWitnessTests(unittest.TestCase):
    def test_exact_midpoint_rational_psd_witness(self) -> None:
        spec = importlib.util.find_spec(MODULE)
        self.assertIsNotNone(spec, "the phase-midpoint certificate module must exist")
        certificate = importlib.import_module(MODULE)
        value = certificate.build_certificate()

        self.assertEqual(
            value["schema"],
            "erdos1191.route_c_signed_owner_phase_chamber_witness.v1",
        )
        self.assertEqual(value["fixture"]["base_width"], "4835/48")
        self.assertEqual(
            value["fixture"]["widths"],
            ["4835/48", "4835/24", "4835/12", "4835/6"],
        )
        self.assertEqual(value["fixture"]["upper_terminal_width"], "4835/3")
        self.assertEqual(value["fixture"]["finite_event_count"], 78)
        self.assertEqual(value["fixture"]["positive_length_cell_count"], 77)
        self.assertEqual(value["fixture"].get("zero_exterior_cells_checked"), 2)
        self.assertEqual(value["fixture"]["owner_cell_row_count"], 616)

        witness = value["rational_PSD_witness"]
        self.assertEqual(witness["factor_shape"], [52, 11])
        self.assertEqual(witness["factor_common_denominator"], 2_000_000)
        self.assertIs(witness["zero_row_sum_exact"], True)
        self.assertIs(witness["PSD_by_rational_Gram_factor"], True)
        self.assertIs(witness["all_owner_rows_feasible_exactly"], True)
        self.assertEqual(witness["owner_rows_checked"], 616)
        self.assertEqual(witness["integrated_signed_demand"], "6221/30944")
        self.assertEqual(witness["physical_price"], "951134501701/3000000000000")
        self.assertEqual(
            witness["below_twice_demand_margin"],
            "246690436855133/2901000000000000",
        )
        self.assertGreater(
            certificate.F(witness["below_twice_demand_margin"]),
            0,
        )

        scope = value["scope"]
        self.assertIs(scope["fixed_midpoint_fixture_only"], True)
        self.assertIs(scope["C058_Q1_Q2_proved"], False)
        self.assertIs(scope["continuum_phase_interval_proved"], False)
        self.assertIs(scope["finite_whole_stencil_accounting_legal_proved"], False)
        self.assertIs(scope["publication_novelty_or_prize_claimed"], False)
        certificate.verify_certificate(value)

    def test_boolean_cannot_impersonate_integer_factor_entry(self) -> None:
        certificate = importlib.import_module(MODULE)
        changed = copy.deepcopy(certificate.build_certificate())
        columns = changed["rational_PSD_witness"]["factor_integer_columns"]
        location = next(
            (column_index, row_index)
            for column_index, column in enumerate(columns)
            for row_index, value in enumerate(column)
            if value == 1 and type(value) is int
        )
        columns[location[0]][location[1]] = True
        changed["integrity"]["payload_sha256"] = certificate.payload_hash(changed)
        with self.assertRaisesRegex(
            certificate.CertificateError,
            "must be an integer, not a boolean",
        ):
            certificate.verify_certificate(changed)

    def test_cache_isolation_and_rehashed_mutations(self) -> None:
        certificate = importlib.import_module(MODULE)
        changed = certificate.build_certificate()
        changed["scope"]["C058_Q1_Q2_proved"] = True
        changed["rational_PSD_witness"]["factor_integer_columns"][0][0] = 0

        rebuilt = certificate.build_certificate()
        self.assertIs(rebuilt["scope"]["C058_Q1_Q2_proved"], False)
        self.assertEqual(
            rebuilt["rational_PSD_witness"]["factor_integer_columns"][0][0],
            -1493,
        )
        self.assertEqual(
            certificate.self_check(rebuilt),
            {"mutations_attempted": 12, "mutations_rejected": 12},
        )

    def test_cli_canonical_bytes_and_nonobject_rejection(self) -> None:
        certificate = importlib.import_module(MODULE)
        script = Path(certificate.__file__).resolve()
        environment = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "certificate.json"
            generated = subprocess.run(
                [sys.executable, str(script), "--output", str(output)],
                capture_output=True,
                check=False,
                env=environment,
            )
            self.assertEqual(generated.returncode, 0, generated.stderr.decode())
            raw = output.read_bytes()
            parsed = json.loads(raw.decode("utf-8"))
            self.assertEqual(raw, certificate.rendered_bytes(parsed))

            verified = subprocess.run(
                [
                    sys.executable,
                    str(script),
                    "--verify",
                    str(output),
                    "--self-check",
                ],
                capture_output=True,
                check=False,
                env=environment,
            )
            self.assertEqual(verified.returncode, 0, verified.stderr.decode())
            self.assertIn(b"mutations_rejected=12", verified.stdout)

            nonobject = Path(directory) / "nonobject.json"
            nonobject.write_text("[]\n", encoding="utf-8")
            rejected = subprocess.run(
                [sys.executable, str(script), "--verify", str(nonobject)],
                capture_output=True,
                check=False,
                env=environment,
            )
            self.assertNotEqual(rejected.returncode, 0)
            self.assertIn(b"JSON root must be an object", rejected.stderr)
            self.assertNotIn(b"Traceback", rejected.stderr)

    def test_committed_json_is_exact_replay(self) -> None:
        certificate = importlib.import_module(MODULE)
        self.assertTrue(
            certificate.DEFAULT_CERTIFICATE.is_file(),
            "the canonical midpoint certificate JSON must be committed",
        )
        raw = certificate.DEFAULT_CERTIFICATE.read_bytes()
        parsed = json.loads(raw.decode("utf-8"))
        self.assertEqual(raw, certificate.rendered_bytes(parsed))
        self.assertEqual(parsed, certificate.build_certificate())
        certificate.verify_certificate(parsed)


if __name__ == "__main__":
    unittest.main()

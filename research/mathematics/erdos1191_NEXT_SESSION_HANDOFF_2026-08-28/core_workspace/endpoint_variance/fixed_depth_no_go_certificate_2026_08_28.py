"""Deterministic exact certificate for the fixed-depth Erdős--Turán no-go."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from fixed_depth_no_go import erdos_turan_fixed_depth_witness


OUTPUT = Path(__file__).with_name("fixed_depth_no_go_certificate_2026-08-28.json")


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()

    records = []
    counts = (16, 32, 64, 128, 256, 512, 1024)
    for count in counts:
        witness = erdos_turan_fixed_depth_witness(count)
        require(
            witness.normalized_birth_shell
            == witness.normalized_birth_diagonal
            + witness.normalized_birth_off_diagonal,
            "birth-shell decomposition failed",
        )
        require(
            witness.normalized_matrix_innovation_00 > 0,
            "matrix innovation was not positive",
        )
        require(
            witness.normalized_birth_off_diagonal > 0,
            "signed off-diagonal shell was not positive",
        )
        records.append(
            {
                "mark_count": count,
                "prime": witness.prime,
                "modulus": witness.modulus,
                "full_normalized_variance": fraction_text(
                    witness.full_normalized_variance
                ),
                "matrix_innovation_00_over_final_modulus": fraction_text(
                    witness.normalized_matrix_innovation_00
                ),
                "same_modulus_birth_shell": fraction_text(
                    witness.normalized_birth_shell
                ),
                "born_diagonal": fraction_text(
                    witness.normalized_birth_diagonal
                ),
                "born_off_diagonal": fraction_text(
                    witness.normalized_birth_off_diagonal
                ),
            }
        )

    terminal = erdos_turan_fixed_depth_witness(counts[-1])
    terminal_errors = {
        "full_variance_to_1_over_180": abs(
            terminal.full_normalized_variance - Fraction(1, 180)
        ),
        "innovation_to_1_over_360": abs(
            terminal.normalized_matrix_innovation_00 - Fraction(1, 360)
        ),
        "birth_shell_to_19_over_3840": abs(
            terminal.normalized_birth_shell - Fraction(19, 3840)
        ),
    }
    require(
        terminal_errors["full_variance_to_1_over_180"] < Fraction(1, 4000),
        "full variance convergence audit failed",
    )
    require(
        terminal_errors["innovation_to_1_over_360"] < Fraction(1, 4000),
        "innovation convergence audit failed",
    )
    require(
        terminal_errors["birth_shell_to_19_over_3840"] < Fraction(1, 4000),
        "birth-shell convergence audit failed",
    )

    payload = {
        "schema": "erdos1191.fixed_depth_erdos_turan_no_go_certificate.v1",
        "arithmetic": "fractions.Fraction",
        "structured_case_count": len(records),
        "structured_cases": records,
        "limiting_constants": {
            "full_normalized_variance": "1/180",
            "matrix_innovation_00_over_final_modulus": "1/360",
            "same_modulus_birth_shell": "19/3840",
            "born_diagonal": "O(M^-2)",
        },
        "terminal_absolute_errors": {
            name: fraction_text(value) for name, value in terminal_errors.items()
        },
        "scope_warning": (
            "For each fixed depth these are arbitrarily large compatible finite "
            "windows, not one infinite globally critical Sidon sequence."
        ),
        "all_checks_passed": True,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

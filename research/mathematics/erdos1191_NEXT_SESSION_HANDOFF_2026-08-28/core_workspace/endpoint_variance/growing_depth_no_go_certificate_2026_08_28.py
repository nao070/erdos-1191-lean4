"""Deterministic certificate for the growing-depth Erdős--Turán no-go."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from growing_depth_no_go import (
    growing_depth_erdos_turan_witness,
    logarithmic_window_depth,
    logarithmic_window_sufficient_condition,
)


OUTPUT = Path(__file__).with_name(
    "growing_depth_no_go_certificate_2026-08-28.json"
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()

    depth_check_maximum = 100_000
    depth_condition_checks = 0
    for scale_index in range(8, depth_check_maximum + 1):
        depth = logarithmic_window_depth(scale_index)
        for terminal_offset in range(depth + 1):
            require(
                logarithmic_window_sufficient_condition(
                    scale_index, terminal_offset
                ),
                "logarithmic critical-window condition failed",
            )
            depth_condition_checks += 1

    records = []
    scale_indices = (8, 10, 12, 14, 16)
    maximum_variance_error = Fraction(0)
    maximum_innovation_error = Fraction(0)
    maximum_birth_shell_error = Fraction(0)
    for scale_index in scale_indices:
        witness = growing_depth_erdos_turan_witness(scale_index)
        scale_records = []
        for record in witness.scales:
            require(
                record.kolmogorov_discrepancy
                <= Fraction(4, record.mark_count),
                "Kolmogorov discrepancy bound failed",
            )
            variance_error = abs(
                record.normalized_variance - Fraction(1, 180)
            )
            maximum_variance_error = max(
                maximum_variance_error, variance_error
            )
            scale_records.append(
                {
                    "terminal_offset": record.terminal_offset,
                    "mark_count": record.mark_count,
                    "modulus": record.modulus,
                    "kolmogorov_discrepancy": fraction_text(
                        record.kolmogorov_discrepancy
                    ),
                    "kolmogorov_bound": fraction_text(
                        Fraction(4, record.mark_count)
                    ),
                    "normalized_variance": fraction_text(
                        record.normalized_variance
                    ),
                }
            )

        transition_records = []
        for record in witness.transitions:
            innovation_error = abs(
                record.normalized_innovation_00 - Fraction(1, 360)
            )
            birth_shell_error = abs(
                record.same_modulus_birth_shell - Fraction(19, 3840)
            )
            maximum_innovation_error = max(
                maximum_innovation_error, innovation_error
            )
            maximum_birth_shell_error = max(
                maximum_birth_shell_error, birth_shell_error
            )
            transition_records.append(
                {
                    "old_count": record.old_count,
                    "new_count": record.new_count,
                    "matrix_innovation_00_over_final_modulus": fraction_text(
                        record.normalized_innovation_00
                    ),
                    "same_modulus_birth_shell": fraction_text(
                        record.same_modulus_birth_shell
                    ),
                }
            )

        require(
            witness.variance_sum
            == sum(
                (record.normalized_variance for record in witness.scales),
                Fraction(0),
            ),
            "variance window sum failed",
        )
        require(
            witness.innovation_00_sum
            == sum(
                (
                    record.normalized_innovation_00
                    for record in witness.transitions
                ),
                Fraction(0),
            ),
            "innovation window sum failed",
        )
        records.append(
            {
                "scale_index": scale_index,
                "terminal_mark_count": witness.terminal_count,
                "depth": witness.depth,
                "prefix_count": witness.depth + 1,
                "prime": witness.prime,
                "scales": scale_records,
                "transitions": transition_records,
                "variance_sum": fraction_text(witness.variance_sum),
                "innovation_00_sum": fraction_text(
                    witness.innovation_00_sum
                ),
                "same_modulus_birth_shell_sum": fraction_text(
                    witness.same_modulus_birth_shell_sum
                ),
            }
        )

    require(
        maximum_variance_error < Fraction(1, 5_000),
        "finite variance convergence audit failed",
    )
    require(
        maximum_innovation_error < Fraction(1, 5_000),
        "finite innovation convergence audit failed",
    )
    require(
        maximum_birth_shell_error < Fraction(1, 5_000),
        "finite birth-shell convergence audit failed",
    )

    payload = {
        "schema": "erdos1191.growing_depth_erdos_turan_no_go_certificate.v1",
        "arithmetic": "fractions.Fraction",
        "depth_arithmetic": {
            "scale_index_range_inclusive": [8, depth_check_maximum],
            "condition_checks": depth_condition_checks,
            "depth_formula": "floor(log2(J))-2",
            "prefix_count_formula": "floor(log2(J))-1",
            "exact_sufficient_condition": "3*2^(ell+1) <= 2*(J-ell)",
            "analytic_input": "log(2)>2/3",
        },
        "structured_case_count": len(records),
        "structured_cases": records,
        "maximum_structured_absolute_errors": {
            "variance_to_1_over_180": fraction_text(
                maximum_variance_error
            ),
            "innovation_to_1_over_360": fraction_text(
                maximum_innovation_error
            ),
            "birth_shell_to_19_over_3840": fraction_text(
                maximum_birth_shell_error
            ),
        },
        "limiting_window_sums": {
            "gap_variance": "(log J)/(180*log(2))+O(1)",
            "matrix_innovation_00": "(log J)/(360*log(2))+O(1)",
            "same_modulus_birth_shell": "19*(log J)/(3840*log(2))+O(1)",
        },
        "scope_warning": (
            "The logarithmically growing compatible windows are finite and "
            "depend on J; they are not one infinite globally critical Sidon "
            "sequence.  The certificate audits exact finite algebra, while "
            "the asymptotic no-go is proved in the accompanying note."
        ),
        "all_checks_passed": True,
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

"""Deterministic audit certificate for the positive gap-kernel theorem."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import random
from fractions import Fraction

from endpoint_variance import iter_normalized_golomb_rulers
from gap_measure_dynamics import (
    DyadicGapUpdate,
    TwoStepGapAgingWitness,
    dyadic_gap_matrix_update,
    two_step_distinct_gap_witness,
)
from sidon_block_variance import (
    direct_diameter_variance,
    dyadic_functional_via_birth_kernel,
    dyadic_positive_functional,
    erdos_turan_ruler,
    positive_gap_variance,
    sidon_block_variance_witness,
    three_rank_lift,
)


OUTPUT = Path(__file__).with_name("sidon_block_variance_certificate_2026-08-28.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def fraction_text(value: Fraction | int) -> str:
    """Stable text form for exact certificate arithmetic."""
    return str(Fraction(value))


def matrix_determinant(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def serialized_matrix(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> list[list[str]]:
    return [[fraction_text(entry) for entry in row] for row in matrix]


def greedy_random_ruler(mark_count: int, generator: random.Random) -> tuple[int, ...]:
    marks = [0]
    differences: set[int] = set()
    while len(marks) < mark_count:
        candidate = marks[-1]
        for _ in range(20_000):
            candidate += generator.randint(1, 4 * mark_count)
            new_differences = [candidate - mark for mark in marks]
            if len(new_differences) == len(set(new_differences)) and not (
                set(new_differences) & differences
            ):
                differences.update(new_differences)
                marks.append(candidate)
                break
        else:
            raise RuntimeError("random greedy ruler construction stalled")
    return tuple(marks)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()
    generator = random.Random(1191)
    dynamics_counts = {
        "random_arbitrary_matrix_update_checks": 0,
        "random_golomb_matrix_update_checks": 0,
        "random_golomb_two_step_checks": 0,
        "structured_matrix_update_checks": 0,
        "structured_two_step_checks": 0,
        "old_prefix_only_two_step_checks": 0,
    }
    minimum_slacks: dict[str, Fraction | None] = {
        "matrix_innovation_00": None,
        "matrix_innovation_11": None,
        "matrix_innovation_determinant": None,
        "two_step_old_rank_minus_bound": None,
        "two_step_final_minus_aged": None,
        "two_step_aged_minus_distinct": None,
        "two_step_final_minus_distinct": None,
    }
    minimum_slack_witnesses: dict[str, dict[str, object]] = {}
    minimum_ratios: dict[str, Fraction | None] = {
        "two_step_old_rank_to_bound": None,
        "two_step_final_to_aged": None,
        "two_step_final_to_distinct": None,
    }
    minimum_ratio_witnesses: dict[str, dict[str, object]] = {}

    def observe_minimum(
        table: dict[str, Fraction | None],
        witnesses: dict[str, dict[str, object]],
        name: str,
        value: Fraction,
        source: str,
        points: tuple[int, ...],
    ) -> None:
        require(value >= 0, f"negative exact audit value for {name}")
        if table[name] is None or value < table[name]:
            table[name] = value
            witnesses[name] = {
                "source": source,
                "points": points,
            }

    def audit_matrix_update(
        points: tuple[int, ...], old_count: int, source: str, counter: str
    ) -> DyadicGapUpdate:
        update = dyadic_gap_matrix_update(points, old_count)
        innovation = update.innovation
        observe_minimum(
            minimum_slacks,
            minimum_slack_witnesses,
            "matrix_innovation_00",
            innovation[0][0],
            source,
            points,
        )
        observe_minimum(
            minimum_slacks,
            minimum_slack_witnesses,
            "matrix_innovation_11",
            innovation[1][1],
            source,
            points,
        )
        observe_minimum(
            minimum_slacks,
            minimum_slack_witnesses,
            "matrix_innovation_determinant",
            matrix_determinant(innovation),
            source,
            points,
        )
        dynamics_counts[counter] += 1
        return update

    def audit_two_step(
        points: tuple[int, ...], source: str, counter: str
    ) -> TwoStepGapAgingWitness:
        witness = two_step_distinct_gap_witness(points)
        slacks = {
            "two_step_old_rank_minus_bound": (
                witness.old_rank_variance - witness.old_rank_lower_bound
            ),
            "two_step_final_minus_aged": (
                witness.final_normalized_variance
                - witness.aged_component_lower_bound
            ),
            "two_step_aged_minus_distinct": (
                witness.aged_component_lower_bound
                - witness.distinct_gap_lower_bound
            ),
            "two_step_final_minus_distinct": (
                witness.final_normalized_variance
                - witness.distinct_gap_lower_bound
            ),
        }
        for name, value in slacks.items():
            observe_minimum(
                minimum_slacks,
                minimum_slack_witnesses,
                name,
                value,
                source,
                points,
            )
        ratios = {
            "two_step_old_rank_to_bound": (
                witness.old_rank_variance / witness.old_rank_lower_bound
            ),
            "two_step_final_to_aged": (
                witness.final_normalized_variance
                / witness.aged_component_lower_bound
            ),
            "two_step_final_to_distinct": (
                witness.final_normalized_variance
                / witness.distinct_gap_lower_bound
            ),
        }
        for name, value in ratios.items():
            observe_minimum(
                minimum_ratios,
                minimum_ratio_witnesses,
                name,
                value,
                source,
                points,
            )
        dynamics_counts[counter] += 1
        return witness

    arbitrary_checks = 0
    for mark_count in range(2, 10):
        for _ in range(400):
            points = tuple(sorted(generator.sample(range(0, 200), mark_count)))
            require(
                positive_gap_variance(points) == direct_diameter_variance(points),
                "arbitrary-set positive gap identity failed",
            )
            arbitrary_checks += 1
            if mark_count >= 4 and mark_count % 2 == 0:
                audit_matrix_update(
                    points,
                    mark_count // 2,
                    f"random_arbitrary_m{mark_count}",
                    "random_arbitrary_matrix_update_checks",
                )

    exhaustive_rulers = 0
    for mark_count in range(2, 8):
        for diameter in range(mark_count - 1, 26):
            for ruler in iter_normalized_golomb_rulers(mark_count, diameter):
                require(
                    positive_gap_variance(ruler) == direct_diameter_variance(ruler),
                    "exhaustive Golomb positive gap identity failed",
                )
                exhaustive_rulers += 1

    random_theorem_checks = 0
    minimum_ratio = None
    minimum_ruler = None
    for _ in range(5_000):
        ruler = greedy_random_ruler(16, generator)
        witness = sidon_block_variance_witness(ruler)
        ratio = witness.exact_variance / witness.simplified_lower_bound
        if minimum_ratio is None or ratio < minimum_ratio:
            minimum_ratio = ratio
            minimum_ruler = ruler
        audit_matrix_update(
            ruler,
            8,
            "random_golomb_m16",
            "random_golomb_matrix_update_checks",
        )
        audit_two_step(
            ruler,
            "random_golomb_m16",
            "random_golomb_two_step_checks",
        )
        random_theorem_checks += 1

    structured = []
    for mark_count, prime in ((8, 11), (16, 17), (24, 29), (32, 37)):
        base = erdos_turan_ruler(mark_count, prime)
        lifted = three_rank_lift(base)
        normalized_energy = positive_gap_variance(lifted) / mark_count**4
        require(
            normalized_energy >= Fraction(1, 2304),
            "structured three-rank lift bound failed",
        )
        structured.append(
            {
                "mark_count": mark_count,
                "prime": prime,
                "base_diameter": base[-1] - base[0],
                "lifted_diameter": lifted[-1] - lifted[0],
                "normalized_energy": str(normalized_energy),
            }
        )

    dynamics_structured = []
    for mark_count, prime in ((16, 17), (32, 37), (64, 67)):
        base = erdos_turan_ruler(mark_count, prime)
        lifted = three_rank_lift(base)
        for variant, ruler in (("base", base), ("three_rank_lift", lifted)):
            update = audit_matrix_update(
                ruler,
                mark_count // 2,
                f"structured_{variant}_m{mark_count}_p{prime}",
                "structured_matrix_update_checks",
            )
            witness = audit_two_step(
                ruler,
                f"structured_{variant}_m{mark_count}_p{prime}",
                "structured_two_step_checks",
            )
            dynamics_structured.append(
                {
                    "variant": variant,
                    "mark_count": mark_count,
                    "prime": prime,
                    "old_modulus": update.old_modulus,
                    "new_modulus": update.new_modulus,
                    "matrix_old_term": serialized_matrix(update.old_term),
                    "matrix_innovation": serialized_matrix(update.innovation),
                    "matrix_new": serialized_matrix(update.new_matrix),
                    "matrix_innovation_determinant": fraction_text(
                        matrix_determinant(update.innovation)
                    ),
                    "old_rank_variance": fraction_text(
                        witness.old_rank_variance
                    ),
                    "old_rank_lower_bound": fraction_text(
                        witness.old_rank_lower_bound
                    ),
                    "final_normalized_variance": fraction_text(
                        witness.final_normalized_variance
                    ),
                    "aged_component_lower_bound": fraction_text(
                        witness.aged_component_lower_bound
                    ),
                    "distinct_gap_lower_bound": fraction_text(
                        witness.distinct_gap_lower_bound
                    ),
                }
            )

    old_prefix_only_points = (0, 1, 4, 6, *range(7, 19))
    old_prefix_only_witness = audit_two_step(
        old_prefix_only_points,
        "non_golomb_full_set_with_golomb_old_prefix",
        "old_prefix_only_two_step_checks",
    )

    dyadic = erdos_turan_ruler(32, 37)
    direct_functional = dyadic_positive_functional(dyadic, 2, 5)
    birth_functional = dyadic_functional_via_birth_kernel(dyadic, 2, 5)
    require(
        direct_functional == birth_functional,
        "dyadic birth-kernel expansion failed",
    )

    require(
        all(value is not None for value in minimum_slacks.values()),
        "minimum gap-dynamics slack table was incomplete",
    )
    require(
        all(value is not None for value in minimum_ratios.values()),
        "minimum gap-dynamics ratio table was incomplete",
    )
    matrix_update_checks = (
        dynamics_counts["random_arbitrary_matrix_update_checks"]
        + dynamics_counts["random_golomb_matrix_update_checks"]
        + dynamics_counts["structured_matrix_update_checks"]
    )
    two_step_checks = (
        dynamics_counts["random_golomb_two_step_checks"]
        + dynamics_counts["structured_two_step_checks"]
        + dynamics_counts["old_prefix_only_two_step_checks"]
    )
    payload = {
        "schema": "erdos1191.sidon_block_variance_certificate.v2",
        "seed": 1191,
        "arbitrary_gap_identity_checks": arbitrary_checks,
        "exhaustive_golomb_identity_checks": exhaustive_rulers,
        "random_m16_theorem_checks": random_theorem_checks,
        "minimum_random_exact_to_simplified_ratio": str(minimum_ratio),
        "minimum_random_ruler": minimum_ruler,
        "structured_lift_checks": structured,
        "gap_measure_dynamics": {
            "arithmetic": "fractions.Fraction",
            "matrix_identity": "M_2m = B M_m B^T + innovation",
            "matrix_B": [["1/4", "1/4"], ["0", "1/2"]],
            "two_step_bound": (
                "Var_nu_M(f) >= (9*M^2-256)/(1048576*N_M)"
            ),
            "audit_counts": {
                **dynamics_counts,
                "matrix_update_checks": matrix_update_checks,
                "two_step_checks": two_step_checks,
                "total_gap_dynamics_checks": matrix_update_checks
                + two_step_checks,
            },
            "minimum_slacks": {
                name: fraction_text(value)
                for name, value in minimum_slacks.items()
                if value is not None
            },
            "minimum_slack_witnesses": minimum_slack_witnesses,
            "minimum_ratios": {
                name: fraction_text(value)
                for name, value in minimum_ratios.items()
                if value is not None
            },
            "minimum_ratio_witnesses": minimum_ratio_witnesses,
            "structured_cases": dynamics_structured,
            "old_prefix_only_case": {
                "points": old_prefix_only_points,
                "old_count": old_prefix_only_witness.old_count,
                "final_count": old_prefix_only_witness.final_count,
                "final_normalized_variance": fraction_text(
                    old_prefix_only_witness.final_normalized_variance
                ),
                "distinct_gap_lower_bound": fraction_text(
                    old_prefix_only_witness.distinct_gap_lower_bound
                ),
            },
        },
        "dyadic_functional": str(direct_functional),
        "dyadic_birth_expansion": str(birth_functional),
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

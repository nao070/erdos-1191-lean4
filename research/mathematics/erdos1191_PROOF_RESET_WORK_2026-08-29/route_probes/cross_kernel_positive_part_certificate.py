"""Exact Route-C positive-part and zero-mass certificates.

The proved scope is finite and algebraic.  This module does not prove or
disprove either question in Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Mapping, Sequence

Kernel = Mapping[int, Fraction]
Matrix = tuple[tuple[Fraction, ...], ...]


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def transpose(matrix: Matrix) -> Matrix:
    return tuple(tuple(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0])))


def matrix_product(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    right_t = transpose(right)
    return tuple(
        tuple(sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in right_t)
        for row in left
    )


def gram_matrix(factor: Matrix) -> Matrix:
    """Return factor^T factor, an exact PSD matrix."""

    return matrix_product(transpose(factor), factor)


def validate_model(kernels: Sequence[Kernel], matrix: Matrix) -> None:
    if not kernels:
        raise ValueError("at least one finitely supported kernel is required")
    size = len(kernels)
    if len(matrix) != size or any(len(row) != size for row in matrix):
        raise ValueError("matrix dimension must equal the number of kernels")
    if any(matrix[r][s] != matrix[s][r] for r in range(size) for s in range(size)):
        raise ValueError("matrix must be symmetric")


def combined_correlation(kernels: Sequence[Kernel], matrix: Matrix, shift: int) -> Fraction:
    validate_model(kernels, matrix)
    total = Fraction(0)
    for r, kernel_r in enumerate(kernels):
        for s, kernel_s in enumerate(kernels):
            overlap = sum(
                (weight * kernel_s.get(x + shift, Fraction(0)) for x, weight in kernel_r.items()),
                Fraction(0),
            )
            total += matrix[r][s] * overlap
    return total


def shift_radius(kernels: Sequence[Kernel]) -> int:
    positions = [position for kernel in kernels for position in kernel]
    if not positions:
        return 0
    return max(positions) - min(positions)


def correlation_table(kernels: Sequence[Kernel], matrix: Matrix) -> dict[int, Fraction]:
    radius = shift_radius(kernels)
    return {
        shift: combined_correlation(kernels, matrix, shift)
        for shift in range(-radius, radius + 1)
    }


def kernel_masses(kernels: Sequence[Kernel]) -> tuple[Fraction, ...]:
    return tuple(sum(kernel.values(), Fraction(0)) for kernel in kernels)


def quadratic(vector: Sequence[Fraction], matrix: Matrix) -> Fraction:
    return sum(
        (matrix[r][s] * vector[r] * vector[s] for r in range(len(vector)) for s in range(len(vector))),
        Fraction(0),
    )


def positive_negative_mass(table: Mapping[int, Fraction]) -> tuple[Fraction, Fraction]:
    positive = sum((max(Fraction(0), value) for shift, value in table.items() if shift > 0), Fraction(0))
    negative = sum((max(Fraction(0), -value) for shift, value in table.items() if shift > 0), Fraction(0))
    return positive, negative


def positive_differences(mark_set: Sequence[int]) -> set[int]:
    return {
        mark_set[j] - mark_set[i]
        for i in range(len(mark_set))
        for j in range(i + 1, len(mark_set))
    }


def is_sidon(mark_set: Sequence[int]) -> bool:
    if sorted(set(mark_set)) != list(mark_set):
        return False
    differences = [
        mark_set[j] - mark_set[i]
        for i in range(len(mark_set))
        for j in range(i + 1, len(mark_set))
    ]
    return len(differences) == len(set(differences))


def convolved_value(mark_set: Sequence[int], kernel: Kernel, position: int) -> Fraction:
    return sum((kernel.get(position - mark, Fraction(0)) for mark in mark_set), Fraction(0))


def direct_energy(mark_set: Sequence[int], kernels: Sequence[Kernel], matrix: Matrix) -> Fraction:
    validate_model(kernels, matrix)
    if not mark_set:
        return Fraction(0)
    kernel_positions = [position for kernel in kernels for position in kernel]
    if not kernel_positions:
        return Fraction(0)
    lower = min(mark_set) + min(kernel_positions)
    upper = max(mark_set) + max(kernel_positions)
    vectors = [
        [convolved_value(mark_set, kernel, position) for position in range(lower, upper + 1)]
        for kernel in kernels
    ]
    return sum(
        (
            matrix[r][s]
            * sum((x * y for x, y in zip(vectors[r], vectors[s])), Fraction(0))
            for r in range(len(kernels))
            for s in range(len(kernels))
        ),
        Fraction(0),
    )


def expansion_energy(mark_set: Sequence[int], table: Mapping[int, Fraction]) -> Fraction:
    return len(mark_set) * table[0] + 2 * sum(
        (table.get(difference, Fraction(0)) for difference in positive_differences(mark_set)),
        Fraction(0),
    )


def positive_part_upper(cardinality: int, table: Mapping[int, Fraction]) -> Fraction:
    positive, _ = positive_negative_mass(table)
    return cardinality * table[0] + 2 * positive


def mass_form_upper(
    cardinality: int, kernels: Sequence[Kernel], matrix: Matrix, table: Mapping[int, Fraction]
) -> Fraction:
    _, negative = positive_negative_mass(table)
    mass = quadratic(kernel_masses(kernels), matrix)
    return mass + (cardinality - 1) * table[0] + 2 * negative


def exact_completion_slack(mark_set: Sequence[int], table: Mapping[int, Fraction]) -> Fraction:
    represented = positive_differences(mark_set)
    missing_positive = sum(
        (
            max(Fraction(0), value)
            for shift, value in table.items()
            if shift > 0 and shift not in represented
        ),
        Fraction(0),
    )
    represented_negative = sum(
        (max(Fraction(0), -table.get(shift, Fraction(0))) for shift in represented),
        Fraction(0),
    )
    return 2 * (missing_positive + represented_negative)


def transformed_kernels(kernels: Sequence[Kernel], factor: Matrix) -> tuple[dict[int, Fraction], ...]:
    if any(len(row) != len(kernels) for row in factor):
        raise ValueError("factor width must equal the number of kernels")
    support = sorted({position for kernel in kernels for position in kernel})
    return tuple(
        {
            position: value
            for position in support
            if (value := sum((row[r] * kernels[r].get(position, Fraction(0)) for r in range(len(kernels))), Fraction(0)))
            != 0
        }
        for row in factor
    )


def point_mass(position: int) -> dict[int, Fraction]:
    return {position: Fraction(1)}


def build_payload() -> dict[str, object]:
    # Wider, overlapping probability kernels and a nontrivial exact Gram factor.
    kernels = (
        {0: Fraction(1, 2), 1: Fraction(1, 2)},
        {0: Fraction(1, 3), 2: Fraction(2, 3)},
        {-1: Fraction(1, 4), 0: Fraction(1, 2), 2: Fraction(1, 4)},
    )
    factor: Matrix = (
        (Fraction(1), Fraction(-1, 2), Fraction(2, 3)),
        (Fraction(0), Fraction(3, 4), Fraction(-1, 3)),
    )
    matrix = gram_matrix(factor)
    mark_set = (0, 1, 4, 6)
    assert is_sidon(mark_set)
    table = correlation_table(kernels, matrix)
    direct = direct_energy(mark_set, kernels, matrix)
    expansion = expansion_energy(mark_set, table)
    upper = positive_part_upper(len(mark_set), table)
    mass_upper = mass_form_upper(len(mark_set), kernels, matrix, table)
    slack = exact_completion_slack(mark_set, table)
    positive, negative = positive_negative_mass(table)
    mass = quadratic(kernel_masses(kernels), matrix)
    assert direct == expansion
    assert upper == mass_upper
    assert upper - direct == slack >= 0
    assert mass == table[0] + 2 * (positive - negative)

    # Rank-one zero-mass contrast between probability point masses.
    contrast_kernels = (point_mass(0), point_mass(1))
    contrast_factor: Matrix = ((Fraction(1), Fraction(-1)),)
    contrast_matrix = gram_matrix(contrast_factor)
    contrast_table = correlation_table(contrast_kernels, contrast_matrix)
    contrast_positive, contrast_negative = positive_negative_mass(contrast_table)
    contrast_mass = quadratic(kernel_masses(contrast_kernels), contrast_matrix)
    assert contrast_mass == 0
    assert contrast_table == {-1: Fraction(-1), 0: Fraction(2), 1: Fraction(-1)}
    assert 2 * contrast_negative == contrast_table[0] + 2 * contrast_positive

    # Arbitrarily many distinct point-mass channels: positive-part cost never
    # beats the same-diagonal baseline.
    locations = (0, 1, 4, 6)
    point_kernels = tuple(point_mass(location) for location in locations)
    point_factor: Matrix = (
        (Fraction(1), Fraction(-1, 2), Fraction(1, 3), Fraction(0)),
        (Fraction(0), Fraction(3, 4), Fraction(-2, 3), Fraction(1)),
    )
    point_matrix = gram_matrix(point_factor)
    point_table = correlation_table(point_kernels, point_matrix)
    point_positive, _ = positive_negative_mass(point_table)
    trace = sum((point_matrix[index][index] for index in range(len(point_matrix))), Fraction(0))
    point_upper = positive_part_upper(len(mark_set), point_table)
    point_baseline = len(mark_set) * trace
    assert point_table[0] == trace
    assert point_upper == point_baseline + 2 * point_positive >= point_baseline

    effective = transformed_kernels(kernels, factor)
    effective_energy = sum(
        (
            direct_energy(mark_set, (kernel,), ((Fraction(1),),))
            for kernel in effective
        ),
        Fraction(0),
    )
    assert effective_energy == direct

    return {
        "global_status": "UNRESOLVED_AT_HARD_LIMIT",
        "claim_boundary": (
            "Exact finite correlation identities and scoped Route-C method closures only; "
            "Questions 1 and 2 remain unresolved."
        ),
        "wider_kernel_fixture": {
            "sidon_set": list(mark_set),
            "gram_factor": [[fraction_text(value) for value in row] for row in factor],
            "matrix": [[fraction_text(value) for value in row] for row in matrix],
            "correlation": {str(shift): fraction_text(value) for shift, value in sorted(table.items())},
            "mass_quadratic": fraction_text(mass),
            "positive_shift_mass": fraction_text(positive),
            "negative_shift_mass": fraction_text(negative),
            "direct_energy": fraction_text(direct),
            "correlation_expansion": fraction_text(expansion),
            "positive_part_upper": fraction_text(upper),
            "mass_form_upper": fraction_text(mass_upper),
            "exact_slack": fraction_text(slack),
            "gram_factor_energy": fraction_text(effective_energy),
        },
        "zero_mass_contrast_fixture": {
            "kernels": ["delta_0", "delta_1"],
            "gram_factor": [["1", "-1"]],
            "matrix": [["1", "-1"], ["-1", "1"]],
            "mass_quadratic": fraction_text(contrast_mass),
            "correlation": {
                str(shift): fraction_text(value) for shift, value in sorted(contrast_table.items())
            },
            "positive_shift_mass": fraction_text(contrast_positive),
            "negative_shift_mass": fraction_text(contrast_negative),
            "identity": "2*N=C(0)+2*P",
        },
        "point_mass_family_fixture": {
            "locations": list(locations),
            "trace": fraction_text(trace),
            "positive_shift_mass": fraction_text(point_positive),
            "same_diagonal_baseline": fraction_text(point_baseline),
            "positive_part_upper": fraction_text(point_upper),
            "identity": "U_plus=|A|*trace(H)+2*P>=|A|*trace(H)",
        },
        "non_claims": [
            "No asymptotic compatible-chain estimate is inferred from these finite identities.",
            "Wider nonzero-mass kernels, difference-set payment, entropy, inverse theorems, and P28 remain open.",
            "No proof, disproof, novelty, publication, or prize claim is asserted.",
        ],
    }


def canonical_payload_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def build_certificate() -> dict[str, object]:
    payload = build_payload()
    return {
        "canonical_payload_sha256": hashlib.sha256(canonical_payload_bytes(payload)).hexdigest(),
        "payload": payload,
    }


def render_certificate() -> str:
    return json.dumps(build_certificate(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def verify_certificate(path: Path) -> None:
    observed = json.loads(path.read_text(encoding="utf-8"))
    expected = build_certificate()
    if observed != expected:
        raise AssertionError(f"certificate replay mismatch: {path}")
    digest = hashlib.sha256(canonical_payload_bytes(observed["payload"])).hexdigest()
    if digest != observed["canonical_payload_sha256"]:
        raise AssertionError("certificate payload hash mismatch")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.write is not None:
        args.write.write_text(render_certificate(), encoding="utf-8")
    if args.verify is not None:
        verify_certificate(args.verify)
    if args.self_check:
        build_payload()
        print("self-check: PASS; Questions 1 and 2 remain unresolved")


if __name__ == "__main__":
    main()

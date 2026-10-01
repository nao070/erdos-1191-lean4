"""Exact finite Route-C probe; Questions 1 and 2 remain unresolved.

Scope: two distinct point-mass probability kernels and a symmetric rational
2-by-2 coefficient matrix.  This module proves a no-go only for that class.
It makes no finite-to-infinite inference and is not a proof or disproof of
Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

Kernel = Mapping[int, Fraction]
Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def fraction_text(value: Fraction) -> str:
    """Return a canonical exact-rational string."""

    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def point_mass(position: int) -> dict[int, Fraction]:
    return {position: Fraction(1)}


def gram(a: Fraction, b: Fraction, c: Fraction) -> Matrix2:
    return ((a, b), (b, c))


def psd_2x2(matrix: Matrix2, *, definite: bool = False) -> bool:
    """Check the exact Sylvester conditions for a symmetric 2-by-2 matrix."""

    (a, b), (b_again, c) = matrix
    if b != b_again:
        return False
    determinant = a * c - b * b
    if definite:
        return a > 0 and determinant > 0
    return a >= 0 and c >= 0 and determinant >= 0


def combined_correlation(
    kernels: Sequence[Kernel], matrix: Matrix2, shift: int
) -> Fraction:
    """Compute C_H(shift) directly from its finite exact definition."""

    total = Fraction(0)
    for r, kernel_r in enumerate(kernels):
        for s, kernel_s in enumerate(kernels):
            overlap = sum(
                (weight_r * kernel_s.get(x + shift, Fraction(0))
                 for x, weight_r in kernel_r.items()),
                Fraction(0),
            )
            total += matrix[r][s] * overlap
    return total


def correlation_table(
    kernels: Sequence[Kernel], matrix: Matrix2
) -> dict[int, Fraction]:
    positions = [position for kernel in kernels for position in kernel]
    diameter = max(positions) - min(positions)
    return {
        shift: value
        for shift in range(-diameter, diameter + 1)
        if (value := combined_correlation(kernels, matrix, shift)) != 0
    }


def convolved_value(mark_set: Sequence[int], kernel: Kernel, x: int) -> Fraction:
    return sum((kernel.get(x - mark, Fraction(0)) for mark in mark_set), Fraction(0))


def direct_energy(
    mark_set: Sequence[int], kernels: Sequence[Kernel], matrix: Matrix2
) -> Fraction:
    """Compute sum_(r,s) h_rs <1_A*K_r,1_A*K_s> literally."""

    support_min = min(mark_set) + min(min(kernel) for kernel in kernels)
    support_max = max(mark_set) + max(max(kernel) for kernel in kernels)
    vectors = [
        [convolved_value(mark_set, kernel, x) for x in range(support_min, support_max + 1)]
        for kernel in kernels
    ]
    return sum(
        (
            matrix[r][s]
            * sum((left * right for left, right in zip(vectors[r], vectors[s])), Fraction(0))
            for r in range(2)
            for s in range(2)
        ),
        Fraction(0),
    )


def positive_differences(mark_set: Sequence[int]) -> set[int]:
    return {
        mark_set[j] - mark_set[i]
        for i in range(len(mark_set))
        for j in range(i + 1, len(mark_set))
    }


def energy_from_correlation(
    mark_set: Sequence[int], kernels: Sequence[Kernel], matrix: Matrix2
) -> Fraction:
    table = correlation_table(kernels, matrix)
    return len(mark_set) * table.get(0, Fraction(0)) + 2 * sum(
        (table.get(shift, Fraction(0)) for shift in positive_differences(mark_set)),
        Fraction(0),
    )


def kernel_masses(kernels: Sequence[Kernel]) -> tuple[Fraction, Fraction]:
    return tuple(sum(kernel.values(), Fraction(0)) for kernel in kernels)  # type: ignore[return-value]


def mass_quadratic(kernels: Sequence[Kernel], matrix: Matrix2) -> Fraction:
    masses = kernel_masses(kernels)
    return sum(
        (matrix[r][s] * masses[r] * masses[s] for r in range(2) for s in range(2)),
        Fraction(0),
    )


def filled_shift_value(
    cardinality: int, kernels: Sequence[Kernel], matrix: Matrix2
) -> Fraction:
    """The Route-C equation-(3) expression, whether legal or not."""

    return mass_quadratic(kernels, matrix) + (cardinality - 1) * combined_correlation(
        kernels, matrix, 0
    )


def positive_part_value(
    cardinality: int, kernels: Sequence[Kernel], matrix: Matrix2
) -> Fraction:
    """Always-legal bound using every positive-shift positive part."""

    positions = [position for kernel in kernels for position in kernel]
    diameter = max(positions) - min(positions)
    return cardinality * combined_correlation(kernels, matrix, 0) + 2 * sum(
        (
            max(Fraction(0), combined_correlation(kernels, matrix, shift))
            for shift in range(1, diameter + 1)
        ),
        Fraction(0),
    )


def reduced_unit_diagonal_parameters(max_denominator: int) -> list[Fraction]:
    """Enumerate all reduced b=p/q in (-1,1), denominator-first."""

    values: list[Fraction] = []
    for denominator in range(1, max_denominator + 1):
        for numerator in range(-denominator + 1, denominator):
            if math.gcd(abs(numerator), denominator) != 1:
                continue
            values.append(Fraction(numerator, denominator))
    return values


def search_unit_diagonal(max_denominator: int = 12) -> dict[str, object]:
    """Search the normalized positive-definite rational Gram family.

    The diagonal is fixed to one to remove trivial rescaling.  A strict gain
    in the filled-shift expression relative to b=0 is -2b.  The exact
    nonnegative-shift gate is C_H(1)=b>=0.
    """

    kernels = (point_mass(0), point_mass(1))
    parameters = reduced_unit_diagonal_parameters(max_denominator)
    checked = 0
    negative = 0
    feasible_gain: list[Fraction] = []
    obstructions: list[Fraction] = []
    for b in parameters:
        matrix = gram(Fraction(1), b, Fraction(1))
        if not psd_2x2(matrix, definite=True):
            continue
        checked += 1
        correlation = combined_correlation(kernels, matrix, 1)
        gain = filled_shift_value(2, kernels, gram(Fraction(1), Fraction(0), Fraction(1))) - filled_shift_value(2, kernels, matrix)
        gate = correlation >= 0
        if b < 0:
            negative += 1
        if gate and gain > 0:
            feasible_gain.append(b)
        if (not gate) and gain > 0:
            obstructions.append(b)

    minimal_obstruction = min(
        obstructions,
        key=lambda value: (value.denominator, abs(value.numerator), value.numerator),
    )
    return {
        "max_denominator": max_denominator,
        "positive_definite_candidates_checked": checked,
        "negative_cross_candidates_checked": negative,
        "feasible_strict_gain_count": len(feasible_gain),
        "minimal_obstruction_parameter": fraction_text(minimal_obstruction),
        "ordering": "denominator, absolute numerator, numerator",
    }


def build_payload() -> dict[str, object]:
    kernels = (point_mass(0), point_mass(1))
    b = Fraction(-1, 2)
    matrix = gram(Fraction(1), b, Fraction(1))
    witness = (0, 2)
    diagonal_matrix = gram(Fraction(1), Fraction(0), Fraction(1))
    table = correlation_table(kernels, matrix)
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] ** 2
    actual = direct_energy(witness, kernels, matrix)
    replay = energy_from_correlation(witness, kernels, matrix)
    illicit = filled_shift_value(len(witness), kernels, matrix)
    repaired = positive_part_value(len(witness), kernels, matrix)
    baseline = filled_shift_value(len(witness), kernels, diagonal_matrix)

    assert psd_2x2(matrix, definite=True)
    assert actual == replay == Fraction(4)
    assert illicit == Fraction(3)
    assert repaired == baseline == Fraction(4)
    assert actual - illicit == Fraction(1)

    return {
        "global_status": "UNRESOLVED_AT_HARD_LIMIT",
        "claim_boundary": (
            "Finite exact no-go for the stated two-point-mass joint-kernel class only; "
            "Questions 1 and 2 remain unresolved."
        ),
        "model": {
            "kernels": ["K1=delta_0", "K2=delta_1"],
            "coefficient_matrix": "H(a,b,c)=[[a,b],[b,c]]",
            "exact_psd_constraints": ["a>=0", "c>=0", "a*c-b^2>=0"],
            "positive_definite_search_normalization": ["a=1", "c=1", "-1<b<1"],
            "correlations": ["C_H(0)=a+c", "C_H(1)=C_H(-1)=b", "C_H(d)=0 for |d|>=2"],
            "filled_shift_objective": "U_H(k)=k*(a+c)+2*b",
            "same_diagonal_baseline": "U_diag(k)=k*(a+c)",
            "strict_signed_gain": "U_diag(k)-U_H(k)=-2*b",
            "gate": "C_H(d)>=0 for every d!=0, equivalently b>=0",
        },
        "exact_no_go": {
            "statement": (
                "For every symmetric rational PSD H in this class, the nonnegative-shift "
                "gate and a strict signed improvement over the same-diagonal baseline "
                "cannot both hold."
            ),
            "reason": "the gate requires b>=0 while strict gain requires b<0",
            "positive_part_repair": "U_plus(k)=k*(a+c)+2*max(b,0)>=U_diag(k)",
        },
        "search": search_unit_diagonal(12),
        "minimal_positive_definite_fixture": {
            "minimality_scope": (
                "two distinct point masses at minimum support diameter; unit diagonal; "
                "positive definite; reduced negative b ordered by denominator then numerator height"
            ),
            "H": [["1", "-1/2"], ["-1/2", "1"]],
            "determinant": fraction_text(determinant),
            "C_H": {str(shift): fraction_text(table[shift]) for shift in sorted(table)},
            "Sidon_set": list(witness),
            "represented_positive_differences": sorted(positive_differences(witness)),
            "actual_energy_direct": fraction_text(actual),
            "actual_energy_correlation_replay": fraction_text(replay),
            "illicit_filled_shift_value": fraction_text(illicit),
            "violation": fraction_text(actual - illicit),
            "same_diagonal_baseline": fraction_text(baseline),
            "positive_part_repair": fraction_text(repaired),
        },
        "minimality_notes": [
            "One kernel has no off-diagonal coefficient, so two kernels are minimal.",
            "Two distinct integer point masses have support diameter at least one; delta_0 and delta_1 attain it.",
            "A two-mark set is the smallest nontrivial Sidon set; {0,2} has the least positive difference avoiding shift one.",
            "Under unit diagonal and positive definiteness, no negative rational b has denominator one; b=-1/2 is first.",
            "If singular PSD matrices were allowed in the fixture search, b=-1 would be simpler but rank-degenerate.",
        ],
        "non_claims": [
            "No claim is made about wider kernels, boundary-cover constraints, or joint inverse theorems.",
            "No finite certificate is promoted to an infinite compatible-chain theorem.",
            "This does not resolve Question 1, Question 2, P28, novelty, or any prize claim.",
        ],
    }


def canonical_payload_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def build_certificate() -> dict[str, object]:
    payload = build_payload()
    digest = hashlib.sha256(canonical_payload_bytes(payload)).hexdigest()
    return {"canonical_payload_sha256": digest, "payload": payload}


def render_certificate() -> str:
    return json.dumps(build_certificate(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def verify_certificate(path: Path) -> None:
    observed = json.loads(path.read_text(encoding="utf-8"))
    expected = build_certificate()
    if observed != expected:
        raise AssertionError(f"certificate replay mismatch: {path}")
    payload = observed["payload"]
    digest = hashlib.sha256(canonical_payload_bytes(payload)).hexdigest()
    if digest != observed["canonical_payload_sha256"]:
        raise AssertionError("certificate payload hash mismatch")


def self_check() -> None:
    kernels = (point_mass(0), point_mass(1))
    for a, b, c in [
        (Fraction(1), Fraction(-1, 2), Fraction(1)),
        (Fraction(2), Fraction(1, 3), Fraction(3)),
        (Fraction(0), Fraction(0), Fraction(5)),
    ]:
        matrix = gram(a, b, c)
        assert combined_correlation(kernels, matrix, 0) == a + c
        assert combined_correlation(kernels, matrix, 1) == b
        assert combined_correlation(kernels, matrix, -1) == b
        assert combined_correlation(kernels, matrix, 2) == 0
    build_payload()


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--print-certificate", action="store_true")
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.self_check:
        self_check()
        print("self-check: PASS; Q1/Q2 remain unresolved")
    if args.verify is not None:
        verify_certificate(args.verify)
        print(f"certificate replay: PASS ({args.verify})")
    if args.print_certificate:
        print(render_certificate(), end="")
    if not (args.self_check or args.verify is not None or args.print_certificate):
        result = search_unit_diagonal(12)
        print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

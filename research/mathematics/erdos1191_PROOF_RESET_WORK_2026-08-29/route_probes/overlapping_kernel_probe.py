"""Exact Route-C overlapping-kernel probe; Q1 and Q2 remain unresolved.

This finite calculation concerns only the pure positive-part energy upper
expression.  It fixes no Hou--Zhao boundary-cover lower functional and makes
no claim of a useful Sidon inequality.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

Kernel = tuple[Fraction, ...]


class MissingBoundaryFunctionalError(ValueError):
    """Raised when a pure-energy witness is promoted beyond its evidence."""


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def kernel_text(kernel: Kernel) -> list[str]:
    return [fraction_text(value) for value in kernel]


def validate_probability_kernel(kernel: Kernel) -> None:
    if not kernel:
        raise ValueError("kernel must be nonempty")
    if any(value < 0 for value in kernel):
        raise ValueError("kernel weights must be nonnegative")
    if sum(kernel, Fraction(0)) != 1:
        raise ValueError("kernel weights must sum exactly to one")


def correlation(left: Kernel, right: Kernel, shift: int) -> Fraction:
    """Return R_(left,right)(shift)=sum_x left(x)right(x+shift)."""

    return sum(
        (
            left[x] * right[x + shift]
            for x in range(len(left))
            if 0 <= x + shift < len(right)
        ),
        Fraction(0),
    )


def maximum_shift(first: Kernel, second: Kernel) -> int:
    return max(len(first), len(second)) - 1


def diagonal_and_cross_correlations(
    first: Kernel, second: Kernel, shift: int
) -> tuple[Fraction, Fraction]:
    """Return A_d and B_d for H_b=[[1,b],[b,1]]."""

    a_value = correlation(first, first, shift) + correlation(second, second, shift)
    b_value = correlation(first, second, shift) + correlation(second, first, shift)
    return a_value, b_value


def combined_correlation(
    first: Kernel, second: Kernel, coefficient: Fraction, shift: int
) -> Fraction:
    a_value, b_value = diagonal_and_cross_correlations(first, second, shift)
    return a_value + coefficient * b_value


def is_psd_parameter(coefficient: Fraction) -> bool:
    """The eigenvalues are 1+b and 1-b."""

    return Fraction(-1) <= coefficient <= Fraction(1)


def is_pd_parameter(coefficient: Fraction) -> bool:
    return Fraction(-1) < coefficient < Fraction(1)


def shift_gate_passes(
    first: Kernel, second: Kernel, coefficient: Fraction
) -> bool:
    """Symmetry reduces the all-nonzero-shift gate to positive shifts."""

    return all(
        combined_correlation(first, second, coefficient, shift) >= 0
        for shift in range(1, maximum_shift(first, second) + 1)
    )


def gate_criterion(first: Kernel, second: Kernel) -> dict[str, object]:
    """Compute the exact A_d/B_d criterion for negative b.

    If no positive shift has B_d>0, no ratio exists and every b in [-1,0)
    passes the correlation gate.  This is represented by rho=None rather than
    by an invented zero or infinity.
    """

    validate_probability_kernel(first)
    validate_probability_kernel(second)
    rows: list[dict[str, object]] = []
    relevant_ratios: list[Fraction] = []
    for shift in range(1, maximum_shift(first, second) + 1):
        a_value, b_value = diagonal_and_cross_correlations(first, second, shift)
        ratio = None if b_value == 0 else a_value / b_value
        if ratio is not None:
            relevant_ratios.append(ratio)
        rows.append(
            {
                "shift": shift,
                "A": a_value,
                "B": b_value,
                "A_over_B": ratio,
            }
        )

    rho = min(relevant_ratios) if relevant_ratios else None
    negative_feasible = rho is None or rho > 0
    return {
        "rows": rows,
        "rho": rho,
        "has_positive_cross_shift": bool(relevant_ratios),
        "negative_feasible": negative_feasible,
    }


def canonical_pd_coefficient(first: Kernel, second: Kernel) -> Fraction | None:
    """Choose the energy-minimizing attained PD coefficient when possible.

    For rho in (0,1), b=-rho is the attained optimum.  If no B_d>0, or if
    rho=1, the PD feasible interval has infimum -1 but no minimum; -1/2 is a
    deterministic interior representative.  If rho=0, no negative b works.
    """

    criterion = gate_criterion(first, second)
    rho = criterion["rho"]
    if not criterion["negative_feasible"]:
        return None
    if rho is None or rho == 1:
        return Fraction(-1, 2)
    if rho > 1:
        raise AssertionError("probability-kernel correlations cannot have rho>1")
    coefficient = -rho
    if not is_pd_parameter(coefficient):
        raise AssertionError("criterion produced a non-PD attained coefficient")
    return coefficient


def total_mass(coefficient: Fraction) -> Fraction:
    """For probability kernels, sum_d C_b(d)=1^T H_b 1."""

    return 2 + 2 * coefficient


def positive_part_energy(
    first: Kernel, second: Kernel, coefficient: Fraction, cardinality: int
) -> Fraction:
    if cardinality < 1:
        raise ValueError("cardinality must be positive")
    c_zero = combined_correlation(first, second, coefficient, 0)
    positive_shift_cost = sum(
        (
            max(Fraction(0), combined_correlation(first, second, coefficient, shift))
            for shift in range(1, maximum_shift(first, second) + 1)
        ),
        Fraction(0),
    )
    return cardinality * c_zero + 2 * positive_shift_cost


def gated_energy_formula(
    first: Kernel, second: Kernel, coefficient: Fraction, cardinality: int
) -> Fraction:
    """Use total mass only after checking the nonnegative-shift gate."""

    if not shift_gate_passes(first, second, coefficient):
        raise ValueError("nonnegative-shift gate fails")
    c_zero = combined_correlation(first, second, coefficient, 0)
    return total_mass(coefficient) + (cardinality - 1) * c_zero


def diagonal_baseline(first: Kernel, second: Kernel, cardinality: int) -> Fraction:
    return positive_part_energy(first, second, Fraction(0), cardinality)


def pure_energy_difference_formula(
    first: Kernel, second: Kernel, coefficient: Fraction, cardinality: int
) -> Fraction:
    """Return U_b-U_0 under the gate: b*(2+(k-1)B_0)."""

    if not shift_gate_passes(first, second, coefficient):
        raise ValueError("nonnegative-shift gate fails")
    _, b_zero = diagonal_and_cross_correlations(first, second, 0)
    return coefficient * (2 + (cardinality - 1) * b_zero)


def probability_grid(denominator: int, *, full_support: bool = False) -> list[Kernel]:
    if denominator < 1:
        raise ValueError("denominator must be positive")
    kernels: set[Kernel] = set()
    for first in range(denominator + 1):
        for second in range(denominator - first + 1):
            third = denominator - first - second
            if full_support and min(first, second, third) == 0:
                continue
            kernels.add(
                (
                    Fraction(first, denominator),
                    Fraction(second, denominator),
                    Fraction(third, denominator),
                )
            )
    return sorted(kernels)


def supports_overlap(first: Kernel, second: Kernel) -> bool:
    return any(
        left > 0 and right > 0
        for left, right in itertools.zip_longest(first, second, fillvalue=Fraction(0))
    )


def evaluate_witness(
    first: Kernel, second: Kernel, coefficient: Fraction, cardinality: int = 2
) -> dict[str, object]:
    validate_probability_kernel(first)
    validate_probability_kernel(second)
    c_values = {
        shift: combined_correlation(first, second, coefficient, shift)
        for shift in range(0, maximum_shift(first, second) + 1)
    }
    energy = positive_part_energy(first, second, coefficient, cardinality)
    baseline = diagonal_baseline(first, second, cardinality)
    return {
        "K1": kernel_text(first),
        "K2": kernel_text(second),
        "b": fraction_text(coefficient),
        "psd": is_psd_parameter(coefficient),
        "positive_definite": is_pd_parameter(coefficient),
        "C_H": {str(shift): fraction_text(value) for shift, value in c_values.items()},
        "shift_gate": shift_gate_passes(first, second, coefficient),
        "total_mass": fraction_text(total_mass(coefficient)),
        "C0": fraction_text(c_values[0]),
        "k": cardinality,
        "U": fraction_text(energy),
        "U_diagonal": fraction_text(baseline),
        "ratio": fraction_text(energy / baseline),
    }


def enumerate_grid(
    denominator: int, *, full_support: bool = False, cardinality: int = 2
) -> dict[str, object]:
    kernels = probability_grid(denominator, full_support=full_support)
    overlapping_pairs = 0
    hits: list[tuple[Fraction, Kernel, Kernel, Fraction]] = []
    for first, second in itertools.combinations(kernels, 2):
        if not supports_overlap(first, second):
            continue
        overlapping_pairs += 1
        coefficient = canonical_pd_coefficient(first, second)
        if coefficient is None:
            continue
        if not is_pd_parameter(coefficient) or not shift_gate_passes(first, second, coefficient):
            continue
        energy = positive_part_energy(first, second, coefficient, cardinality)
        baseline = diagonal_baseline(first, second, cardinality)
        if energy < baseline:
            hits.append((energy / baseline, first, second, coefficient))
    hits.sort(key=lambda row: (row[0], row[1], row[2], row[3]))
    return {
        "denominator": denominator,
        "full_support": full_support,
        "kernel_count": len(kernels),
        "distinct_overlapping_pair_count": overlapping_pairs,
        "feasible_strict_gain_count": len(hits),
        "best_ratio": None if not hits else hits[0][0],
    }


def t_family(t_value: Fraction, cardinality: int = 2) -> dict[str, object]:
    if not Fraction(0) < t_value < Fraction(1, 2):
        raise ValueError("the full-overlap family requires 0<t<1/2")
    first = (Fraction(1, 2) - t_value, Fraction(1, 2) + t_value)
    second = (Fraction(1, 2), Fraction(1, 2))
    coefficient = -1 + 2 * t_value * t_value
    record = evaluate_witness(first, second, coefficient, cardinality)
    record["t"] = fraction_text(t_value)
    record["small_eigenvalue"] = fraction_text(1 + coefficient)
    return record


def validate_boundary_claim(payload: Mapping[str, object]) -> None:
    boundary = payload["hou_zhao_boundary_cover"]
    if not isinstance(boundary, Mapping):
        raise MissingBoundaryFunctionalError("boundary metadata missing")
    fixed = boundary.get("lower_functional_fixed")
    claimed = boundary.get("useful_sidon_inequality_claimed")
    if claimed and not fixed:
        raise MissingBoundaryFunctionalError(
            "pure energy gain cannot be promoted without a fixed boundary-cover lower functional"
        )


def serialize_criterion(first: Kernel, second: Kernel) -> dict[str, object]:
    result = gate_criterion(first, second)
    return {
        "rows": [
            {
                "shift": row["shift"],
                "A": fraction_text(row["A"]),
                "B": fraction_text(row["B"]),
                "A_over_B": None
                if row["A_over_B"] is None
                else fraction_text(row["A_over_B"]),
            }
            for row in result["rows"]
        ],
        "rho": None if result["rho"] is None else fraction_text(result["rho"]),
        "has_positive_cross_shift": result["has_positive_cross_shift"],
        "negative_feasible": result["negative_feasible"],
    }


def serialize_grid(result: Mapping[str, object]) -> dict[str, object]:
    return {
        key: fraction_text(value) if isinstance(value, Fraction) else value
        for key, value in result.items()
    }


def build_payload() -> dict[str, object]:
    half_first = (Fraction(1), Fraction(0))
    half_second = (Fraction(1, 2), Fraction(1, 2))
    half_b = Fraction(-1, 2)
    full_first = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
    full_second = (Fraction(1, 4), Fraction(1, 2), Fraction(1, 4))
    full_b = Fraction(-7, 8)

    half = evaluate_witness(half_first, half_second, half_b)
    full = evaluate_witness(full_first, full_second, full_b)
    family = t_family(Fraction(1, 6))
    identical = (Fraction(1, 2), Fraction(1, 2))
    endpoint = evaluate_witness(identical, identical, Fraction(-1))
    family_samples = [
        t_family(value)
        for value in (Fraction(1, 3), Fraction(1, 6), Fraction(1, 12))
    ]

    assert half["ratio"] == "4/7"
    assert full["ratio"] == "29/176"
    assert family["ratio"] == "4/55"
    assert serialize_criterion(identical, identical)["rho"] == "1"
    assert endpoint["U"] == "0"
    assert gated_energy_formula(half_first, half_second, half_b, 2) == Fraction(2)
    assert pure_energy_difference_formula(half_first, half_second, half_b, 2) == Fraction(-3, 2)

    payload: dict[str, object] = {
        "global_status": "UNRESOLVED_AT_HARD_LIMIT",
        "claim_boundary": (
            "Exact finite pure-energy feasibility only; no Hou-Zhao boundary-cover lower "
            "functional is fixed; Questions 1 and 2 remain unresolved."
        ),
        "general_criterion": {
            "definitions": [
                "A_d=R_11(d)+R_22(d)",
                "B_d=R_12(d)+R_21(d)",
                "C_b(d)=A_d+b*B_d",
                "rho=min_(d>=1:B_d>0) A_d/B_d",
            ],
            "psd_range": "-1<=b<=1",
            "positive_definite_range": "-1<b<1",
            "negative_gate_when_ratios_exist": "b>=-rho together with -1<=b<0",
            "negative_gate_when_no_positive_B": (
                "If B_d=0 at every positive shift, rho is undefined and every -1<=b<0 "
                "passes the shift gate because C_b(d)=A_d>=0."
            ),
            "negative_feasibility": (
                "When some B_d>0, a negative feasible b exists exactly when rho>0."
            ),
            "rho_endpoint_classification": (
                "For probability kernels, sum_(d>=1)(A_d-B_d)=-||K1-K2||_2^2/2; "
                "therefore rho<=1, equality forces K1=K2, and distinct kernels have rho<1."
            ),
            "pure_gain_identity": "U_b(k)-U_0(k)=b*(2+(k-1)*B_0)<0 for feasible b<0",
        },
        "identical_kernel_rho_1_endpoint": {
            "criterion": serialize_criterion(identical, identical),
            "b_equals_minus_1": endpoint,
            "pd_endpoint_status": (
                "b=-1 is PSD and gate-feasible but not positive definite; "
                "PD coefficients approach it from above."
            ),
        },
        "half_grid_enumeration": serialize_grid(enumerate_grid(2)),
        "minimal_half_grid_witness": half,
        "minimal_half_grid_criterion": serialize_criterion(half_first, half_second),
        "full_support_denominator_4_enumeration": serialize_grid(
            enumerate_grid(4, full_support=True)
        ),
        "full_support_denominator_4_witness": full,
        "full_support_denominator_4_criterion": serialize_criterion(full_first, full_second),
        "rational_t_family": {
            "kernels": ["K1=(1/2-t,1/2+t)", "K2=(1/2,1/2)"],
            "domain": "rational 0<t<1/2",
            "b": "-1+2*t^2",
            "C_positive_shifts": "C_b(1)=0 and all larger shifts vanish",
            "C0": "4*t^2",
            "total_mass": "4*t^2",
            "small_eigenvalue": "1+b=2*t^2",
            "U": "4*k*t^2",
            "U_diagonal": "k+1+2*(k-1)*t^2",
            "ratio": "4*k*t^2/(k+1+2*(k-1)*t^2) -> 0",
            "exact_t_equals_1_over_6": family,
            "exact_samples": family_samples,
        },
        "hou_zhao_boundary_cover": {
            "lower_functional_fixed": False,
            "useful_sidon_inequality_claimed": False,
            "status": "NOT_SPECIFIED",
            "warning": (
                "The family drives total mass, C0, and the small Gram eigenvalue to zero. "
                "A pure upper-energy ratio is not a boundary-cover-normalized improvement."
            ),
        },
        "non_claims": [
            "No compatible multiscale chain theorem is proved.",
            "No Hou-Zhao boundary-cover feasibility or lower coefficient is evaluated.",
            "No useful Sidon inequality, Question 1 result, or Question 2 result follows.",
        ],
    }
    validate_boundary_claim(payload)
    return payload


def canonical_payload_bytes(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode(
        "utf-8"
    )


def build_certificate() -> dict[str, object]:
    payload = build_payload()
    digest = hashlib.sha256(canonical_payload_bytes(payload)).hexdigest()
    return {"canonical_payload_sha256": digest, "payload": payload}


def render_certificate() -> str:
    return json.dumps(build_certificate(), indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def verify_certificate(path: Path) -> None:
    expected_bytes = render_certificate().encode("utf-8")
    observed_bytes = path.read_bytes()
    if observed_bytes != expected_bytes:
        raise AssertionError(f"byte-exact certificate replay mismatch: {path}")
    observed = json.loads(observed_bytes)
    payload = observed["payload"]
    digest = hashlib.sha256(canonical_payload_bytes(payload)).hexdigest()
    if digest != observed["canonical_payload_sha256"]:
        raise AssertionError("canonical payload hash mismatch")
    validate_boundary_claim(payload)


def mutation_checks() -> None:
    first = (Fraction(1), Fraction(0))
    second = (Fraction(1, 2), Fraction(1, 2))
    if shift_gate_passes(first, second, Fraction(-3, 4)):
        raise AssertionError("sign-gate mutation was accepted")
    if is_psd_parameter(Fraction(-3, 2)):
        raise AssertionError("PSD mutation was accepted")
    mutated = copy.deepcopy(build_payload())
    boundary = mutated["hou_zhao_boundary_cover"]
    assert isinstance(boundary, dict)
    boundary["useful_sidon_inequality_claimed"] = True
    try:
        validate_boundary_claim(mutated)
    except MissingBoundaryFunctionalError:
        pass
    else:
        raise AssertionError("unsupported boundary-benefit mutation was accepted")


def self_check() -> None:
    build_payload()
    mutation_checks()


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--emit", action="store_true", help="print deterministic certificate JSON")
    parser.add_argument("--write", type=Path, help="write deterministic certificate JSON")
    parser.add_argument("--verify", type=Path, help="verify byte-exact JSON replay")
    parser.add_argument("--self-check", action="store_true", help="run exact invariants and mutations")
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.self_check:
        self_check()
        print("self-check and mutations: PASS; Q1/Q2 remain unresolved")
    if args.verify is not None:
        verify_certificate(args.verify)
        print(f"byte-exact certificate replay: PASS ({args.verify})")
    if args.emit:
        print(render_certificate(), end="")
    if args.write is not None:
        args.write.write_text(render_certificate(), encoding="utf-8")
    if not (args.emit or args.write is not None or args.self_check or args.verify is not None):
        payload = build_payload()
        summary = {
            "half_grid_ratio": payload["minimal_half_grid_witness"]["ratio"],
            "full_support_ratio": payload["full_support_denominator_4_witness"]["ratio"],
            "status": payload["global_status"],
        }
        print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

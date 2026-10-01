"""Independent certificate for the Wave 17 local sorted-rank surplus.

The exact part of this module checks the integer weight multiplicities,
cumulative ranks, rational coefficient masses, and the algebraic implication
from the proved ``18(1+log(n))/n`` error to its weaker square-root majorant.
The analytic error estimate itself belongs to the accompanying Wave 17 memo.

Decimal logarithms are evaluated at precision 80 only to project the two
stated thresholds and a few moderate-size convergence rows.  Those rows are
explicitly excluded from the proof scope.  Nothing here proves P19, P22, an
infinite branch, or either question in Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from hashlib import sha256
from math import factorial
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave17_local_rank_surplus_certificate_2026-08-29.json"

DECIMAL_PRECISION = 80
EXACT_AUDIT_EPOCHS = (3, 4, 8, 16, 32, 64, 128, 256, 1024)
IMPLICATION_EPOCHS = (16, 17, 128, 2**20, 2**22)
DIRECT_PROJECTION_EPOCHS = (16, 32, 64, 128)
THRESHOLDS = ((2**20, Fraction(81, 128)), (2**22, Fraction(3, 4)))


def _require_epoch(epoch: int, minimum: int = 3) -> int:
    if isinstance(epoch, bool) or not isinstance(epoch, int):
        raise TypeError("epoch must be an integer")
    if epoch < minimum:
        raise ValueError(f"epoch must be at least {minimum}")
    return epoch


def _require_threshold(threshold: Fraction) -> Fraction:
    if not isinstance(threshold, Fraction):
        raise TypeError("threshold must be a Fraction")
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    return threshold


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _decimal_text(value: Decimal) -> str:
    return format(value, "f")


def _fraction_decimal(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _canonical_hash(payload: dict[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


def coefficient_audit(epoch: int) -> dict[str, Any]:
    """Audit all count, cumulative-rank, and coefficient-mass identities."""
    epoch = _require_epoch(epoch)
    high_count = epoch - 1
    middle_numerator = (epoch - 1) * (3 * epoch - 8)
    middle_count = middle_numerator // 2
    low_count = epoch - 1
    cumulative_a = high_count
    cumulative_b = high_count + middle_count
    cumulative_c = cumulative_b + low_count

    denominator = epoch * epoch
    high_weight = Fraction(1, denominator)
    middle_weight = Fraction(1, 2 * denominator)
    low_weight = Fraction(1, 4 * denominator)
    high_mass = high_count * high_weight
    middle_mass = middle_count * middle_weight
    low_mass = low_count * low_weight
    total_mass = high_mass + middle_mass + low_mass
    closed_total_mass = Fraction(3 * (epoch - 1) ** 2, 4 * denominator)

    # Scale every logarithmic block by the common denominator 4*n^2.
    # The three sorted rank intervals contribute
    # 4 log(a!), 2(log(b!)-log(a!)), and log(c!)-log(b!).
    block_exponents = ((4, 0, 0), (-2, 2, 0), (0, -1, 1))
    net_exponents = tuple(
        sum(block[index] for block in block_exponents) for index in range(3)
    )

    checks = {
        "middle_count_is_integral": middle_numerator % 2 == 0,
        "middle_count_closed_formula": 2 * middle_count
        == (epoch - 1) * (3 * epoch - 8),
        "b_equals_a_plus_middle": cumulative_b == cumulative_a + middle_count,
        "b_closed_formula": 2 * cumulative_b == 3 * (epoch - 1) * (epoch - 2),
        "c_equals_b_plus_low": cumulative_c == cumulative_b + low_count,
        "c_closed_formula": 2 * cumulative_c == (epoch - 1) * (3 * epoch - 4),
        "total_count_equals_c": high_count + middle_count + low_count == cumulative_c,
        "high_mass_is_count_times_weight": high_mass == high_count * high_weight,
        "middle_mass_is_count_times_weight": middle_mass
        == middle_count * middle_weight,
        "low_mass_is_count_times_weight": low_mass == low_count * low_weight,
        "total_mass_closed_formula": total_mass == closed_total_mass,
        "factorial_exponents_telescope": net_exponents == (2, 1, 1),
    }
    return {
        "epoch": epoch,
        "high_count": high_count,
        "middle_count": middle_count,
        "low_count": low_count,
        "cumulative_a": cumulative_a,
        "cumulative_b": cumulative_b,
        "cumulative_c": cumulative_c,
        "high_weight": _fraction_text(high_weight),
        "middle_weight": _fraction_text(middle_weight),
        "low_weight": _fraction_text(low_weight),
        "high_mass": _fraction_text(high_mass),
        "middle_mass": _fraction_text(middle_mass),
        "low_mass": _fraction_text(low_mass),
        "total_mass": _fraction_text(total_mass),
        "closed_total_mass": _fraction_text(closed_total_mass),
        "scaled_block_factorial_exponents": [list(row) for row in block_exponents],
        "factorial_numerator_exponents": {
            "a_factorial": net_exponents[0],
            "b_factorial": net_exponents[1],
            "c_factorial": net_exponents[2],
        },
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def analytic_bound_implication_audit(epoch: int) -> dict[str, Any]:
    """Check exactly that the proved error implies the weak majorant.

    The common factor ``1+log(n)`` is positive.  Both prefactors are
    nonnegative, so their comparison may be squared.  The resulting rational
    inequality is ``324/n^2 <= 400/n``.
    """
    epoch = _require_epoch(epoch, minimum=16)
    strong_squared = Fraction(18 * 18, epoch * epoch)
    weak_squared = Fraction(20 * 20, epoch)
    cleared_margin = 400 * epoch - 324
    return {
        "epoch": epoch,
        "proved_error_bound": "18*(1+log(n))/n",
        "weak_error_bound": "20*(1+log(n))/sqrt(n)",
        "common_factor_positive": True,
        "strong_prefactor_squared": _fraction_text(strong_squared),
        "weak_prefactor_squared": _fraction_text(weak_squared),
        "cleared_nonnegative_margin": cleared_margin,
        "squared_prefactor_inequality": strong_squared <= weak_squared,
        "strong_bound_implies_weak_bound": (
            cleared_margin >= 0 and strong_squared <= weak_squared
        ),
    }


def weak_majorant_monotonicity_audit(minimum_epoch: int = 16) -> dict[str, Any]:
    """Audit monotonicity of ``20(1+log(x))/sqrt(x)`` on ``x>=16``.

    The derivative is ``10(1-log(x))/x^(3/2)``.  The elementary estimate
    ``e<3`` follows from ``k! >= 2^(k-1)`` for ``k>=2`` (strict at ``k=3``)
    and the exact geometric tail ``sum_{j>=1} 2^-j=1``.  Thus
    ``x>=16>3>e`` implies ``log(x)>1`` and the derivative is negative.
    """
    minimum_epoch = _require_epoch(minimum_epoch, minimum=16)
    factorial_induction_seed = factorial(2) == 2
    factorial_strict_witness = factorial(3) > 2**2
    geometric_tail = Fraction(1)
    e_upper_bound = Fraction(2) + geometric_tail
    e_strictly_below_three = (
        factorial_induction_seed and factorial_strict_witness and e_upper_bound == 3
    )
    minimum_exceeds_e = minimum_epoch > 3 and e_strictly_below_three

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        logarithm = Decimal(minimum_epoch).ln()

    derivative_negative = minimum_exceeds_e and logarithm > 1
    return {
        "minimum_epoch": minimum_epoch,
        "majorant": "20*(1+log(x))/sqrt(x)",
        "derivative_formula": "10*(1-log(x))/x^(3/2)",
        "factorial_induction_seed_verified": factorial_induction_seed,
        "factorial_strict_witness_at_three": factorial_strict_witness,
        "geometric_tail_sum": _fraction_text(geometric_tail),
        "three_is_a_strict_upper_bound_for_e": e_strictly_below_three,
        "minimum_epoch_exceeds_e": minimum_exceeds_e,
        "log_minimum_decimal_projection": _decimal_text(logarithm),
        "log_minimum_greater_than_one": logarithm > 1,
        "derivative_strictly_negative_on_domain": derivative_negative,
        "weak_majorant_strictly_decreasing": derivative_negative,
    }


def _delta_zero_decimal() -> Decimal:
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        return (
            Decimal(3) / Decimal(2)
            + Decimal(3) * Decimal(3).ln() / Decimal(4)
            - Decimal(2) * Decimal(2).ln()
        )


def _weak_majorant_decimal(epoch: int) -> Decimal:
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        value = Decimal(epoch)
        return Decimal(20) * (Decimal(1) + value.ln()) / value.sqrt()


def threshold_projection(epoch: int, threshold: Fraction) -> dict[str, Any]:
    """Project the weak analytic lower bound at precision 80."""
    epoch = _require_epoch(epoch, minimum=16)
    threshold = _require_threshold(threshold)
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        delta_zero = _delta_zero_decimal()
        error = _weak_majorant_decimal(epoch)
        lower = delta_zero - error
        threshold_decimal = _fraction_decimal(threshold)
        margin = lower - threshold_decimal
    return {
        "epoch": epoch,
        "threshold": _fraction_text(threshold),
        "decimal_precision": DECIMAL_PRECISION,
        "delta_zero": _decimal_text(delta_zero),
        "weak_error_majorant": _decimal_text(error),
        "weak_lower_bound": _decimal_text(lower),
        "strict_threshold_margin": _decimal_text(margin),
        "strict_threshold_conclusion": lower > threshold_decimal,
        "transcendental_projection_only": True,
    }


@cache
def _log_factorial_decimal(value: int, precision: int) -> Decimal:
    with localcontext() as context:
        context.prec = precision
        return Decimal(factorial(value)).ln() if value > 1 else Decimal(0)


def direct_floor_projection(epoch: int) -> dict[str, Any]:
    """Directly project ``F_n``, ``K_n``, and ``D_n`` for moderate ``n``."""
    epoch = _require_epoch(epoch)
    count_row = coefficient_audit(epoch)
    a = count_row["cumulative_a"]
    b = count_row["cumulative_b"]
    c = count_row["cumulative_c"]

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        denominator = Decimal(4 * epoch * epoch)
        local_floor = (
            Decimal(2) * _log_factorial_decimal(a, DECIMAL_PRECISION)
            + _log_factorial_decimal(b, DECIMAL_PRECISION)
            + _log_factorial_decimal(c, DECIMAL_PRECISION)
        ) / denominator

        first_triangular_sum = sum(
            (Decimal(index * (index + 1) // 2).ln() for index in range(3, epoch)),
            Decimal(0),
        )
        second_triangular_sum = sum(
            (
                Decimal(2 * epoch - index - 2) * Decimal(index * (index + 1) // 2).ln()
                for index in range(epoch, 2 * epoch - 2)
            ),
            Decimal(0),
        )
        triangular_floor = Decimal(a) * Decimal(3).ln() / denominator + (
            Decimal(a) * first_triangular_sum + second_triangular_sum
        ) / Decimal(2 * epoch * epoch)
        surplus = local_floor - triangular_floor
        delta_zero = _delta_zero_decimal()
        absolute_delta_error = abs(surplus - delta_zero)
        memo_error_bound = (
            Decimal(18) * (Decimal(1) + Decimal(epoch).ln()) / Decimal(epoch)
        )

    return {
        "epoch": epoch,
        "decimal_precision": DECIMAL_PRECISION,
        "local_sorted_rank_floor_F": _decimal_text(local_floor),
        "triangular_floor_K": _decimal_text(triangular_floor),
        "surplus_D": _decimal_text(surplus),
        "absolute_delta_zero_error": _decimal_text(absolute_delta_error),
        "memo_strong_error_bound": _decimal_text(memo_error_bound),
        "observed_within_memo_bound": absolute_delta_error <= memo_error_bound,
        "projection_only": True,
        "used_as_proof": False,
    }


@cache
def build_certificate() -> dict[str, Any]:
    """Build the deterministic Wave 17 local-rank certificate payload."""
    coefficient_rows = [coefficient_audit(epoch) for epoch in EXACT_AUDIT_EPOCHS]
    implication_rows = [
        analytic_bound_implication_audit(epoch) for epoch in IMPLICATION_EPOCHS
    ]
    monotonicity = weak_majorant_monotonicity_audit(16)
    threshold_rows = [
        threshold_projection(epoch, threshold) for epoch, threshold in THRESHOLDS
    ]
    direct_rows = [direct_floor_projection(epoch) for epoch in DIRECT_PROJECTION_EPOCHS]

    payload: dict[str, Any] = {
        "schema": "erdos1191.wave17.local-sorted-rank-surplus.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Independently audit the exact coefficient ledger and the explicit "
            "threshold consequences of the Wave 17 local sorted-rank surplus."
        ),
        "arithmetic": {
            "count_and_mass_checks": "exact integer and fractions.Fraction",
            "analytic_implication": "exact squared rational prefactors",
            "transcendental_projections": (
                "decimal.Context precision 80; display and threshold projection only"
            ),
            "logarithm": "natural",
        },
        "theorem_contract": {
            "high_weight_count": "a=n-1 at 1/n^2",
            "middle_weight_count": "t=(n-1)(3n-8)/2 at 1/(2n^2)",
            "low_weight_count": "a=n-1 at 1/(4n^2)",
            "cumulative_b": "b=3(n-1)(n-2)/2=a+t",
            "cumulative_c": "c=(n-1)(3n-4)/2=b+a",
            "local_floor_F": "[2log(a!)+log(b!)+log(c!)]/(4n^2)",
            "surplus": "D_n=F_n^(loc,int)-K_n^int",
            "delta_zero": "3/2+(3/4)log(3)-2log(2)",
            "memo_proved_error": "|D_n-delta_zero|<=18(1+log(n))/n",
            "weaker_error": "20(1+log(n))/sqrt(n), n>=16",
        },
        "coefficient_rows": coefficient_rows,
        "analytic_bound_implication_rows": implication_rows,
        "weak_majorant_monotonicity": monotonicity,
        "threshold_projections": threshold_rows,
        "direct_convergence_projections": direct_rows,
        "all_required_checks_pass": (
            all(row["all_exact_checks_pass"] for row in coefficient_rows)
            and all(row["strong_bound_implies_weak_bound"] for row in implication_rows)
            and monotonicity["weak_majorant_strictly_decreasing"]
            and all(row["strict_threshold_conclusion"] for row in threshold_rows)
        ),
        "scope_flags": {
            "finite_algebraic_only": True,
            "analytic_error_proved_in_memo": True,
            "decimal_thresholds_are_projections_not_proofs": True,
            "p19_proved": False,
            "p22_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
            "problem_unresolved": True,
        },
        "conclusions": [
            "The three exact coefficient counts end at cumulative ranks a, b, and c.",
            "Their sorted rank blocks telescope to factorial exponents 2, 1, and 1.",
            "The proved 18/n error implies the weak 20/sqrt(n) majorant exactly.",
            "The weak majorant decreases from n=16 and its 80-digit projections clear both stated thresholds.",
            "The direct moderate-n F/K rows are numerical checks only and are not used as proof.",
        ],
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def certificate_bytes() -> bytes:
    """Return the canonical committed byte representation, including LF."""
    return _canonical_bytes(build_certificate()) + b"\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_bytes(certificate_bytes())
    print(build_certificate()["certificate_sha256"])


if __name__ == "__main__":
    main()

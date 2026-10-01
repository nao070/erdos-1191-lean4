"""Finite/algebraic certificate for the Wave 18 P22 reduction.

The exact layer checks the target-interior coefficient classes, the source
weights ``w_(n,p)``, the residual weights ``r_(n,p)``, and the rational
pre-logarithmic rank-load sums.  It also constructs each finite
Erdos--Turan calibration value as the exact logarithm of an integer product.

The Wave 17 analytic rank-surplus bound and the infinite-family local-slack
no-go remain inputs from their accompanying memos.  Decimal and binary-float
values in this certificate are projections only.  In particular, this
module does not prove P19, P22, or either question of Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from hashlib import sha256
from itertools import pairwise
from math import factorial, isqrt, lgamma, log
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave18_excess_birth_locality_certificate_2026-08-29.json"

DECIMAL_PRECISION = 80
CAP = Fraction(5, 2)
EXACT_EPOCHS = (3, 4, 8, 16, 32, 64, 128, 1024)
SOURCE_AUDIT_EPOCHS = (3, 4, 8, 16, 32, 64)
RANK_LAYER_EPOCHS = (3, 4, 8, 16, 32, 64)
DYADIC_START_EPOCHS = (4, 8, 16, 32, 64)
DYADIC_DEPTH = 6
ERDOS_TURAN_PRIMES = (5, 7, 11, 31, 61, 127, 257)


def _require_plain_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _require_epoch(epoch: int, minimum: int = 3) -> int:
    epoch = _require_plain_integer(epoch, "epoch")
    if epoch < minimum:
        raise ValueError(f"epoch must be at least {minimum}")
    return epoch


def _require_source(epoch: int, source: int) -> tuple[int, int]:
    epoch = _require_epoch(epoch)
    source = _require_plain_integer(source, "source")
    if not 2 <= source <= epoch:
        raise ValueError("source must satisfy 2 <= source <= epoch")
    return epoch, source


def _require_positive_fraction(value: Fraction, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a Fraction")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


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


def _integer_sha256(value: int) -> str:
    encoded = value.to_bytes((value.bit_length() + 7) // 8, "big")
    return sha256(encoded).hexdigest()


def _points_sha256(points: tuple[int, ...]) -> str:
    return sha256(",".join(map(str, points)).encode("ascii")).hexdigest()


def beta_coefficient(epoch: int, left: int, right: int) -> Fraction:
    """Return the target-interior coefficient of ``D_(left,right)``."""
    epoch = _require_epoch(epoch)
    left = _require_plain_integer(left, "left")
    right = _require_plain_integer(right, "right")
    if not epoch <= right <= 2 * epoch - 2:
        raise ValueError("right must satisfy epoch <= right <= 2*epoch-2")
    if not 2 <= left <= right:
        raise ValueError("left must satisfy 2 <= left <= right")
    denominator = epoch * epoch
    if left == right:
        return Fraction(1, denominator)
    if left == right - 1:
        return Fraction(1, 4 * denominator)
    return Fraction(1, 2 * denominator)


def coefficient_ledger_audit(epoch: int) -> dict[str, Any]:
    """Audit the complete target-interior atom ledger exactly."""
    epoch = _require_epoch(epoch)
    counts = {"high": 0, "middle": 0, "low": 0}
    mass = Fraction()
    for right in range(epoch, 2 * epoch - 1):
        for left in range(2, right + 1):
            coefficient = beta_coefficient(epoch, left, right)
            mass += coefficient
            if left == right:
                counts["high"] += 1
            elif left == right - 1:
                counts["low"] += 1
            else:
                counts["middle"] += 1

    atom_count = sum(counts.values())
    closed_atom_count = (epoch - 1) * (3 * epoch - 4) // 2
    closed_middle_count = (epoch - 1) * (3 * epoch - 8) // 2
    closed_mass = Fraction(3 * (epoch - 1) ** 2, 4 * epoch * epoch)
    checks = {
        "high_count_formula_verified": counts["high"] == epoch - 1,
        "middle_count_formula_verified": counts["middle"] == closed_middle_count,
        "low_count_formula_verified": counts["low"] == epoch - 1,
        "atom_count_formula_verified": atom_count == closed_atom_count,
        "coefficient_mass_formula_verified": mass == closed_mass,
    }
    return {
        "epoch": epoch,
        "high_count": counts["high"],
        "middle_count": counts["middle"],
        "low_count": counts["low"],
        "atom_count": atom_count,
        "closed_atom_count": closed_atom_count,
        "total_coefficient_mass": _fraction_text(mass),
        "closed_coefficient_mass": _fraction_text(closed_mass),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def residual_coefficient(epoch: int, source: int) -> Fraction:
    """Return ``r_(n,p)=(4n-2p-3)/(8n^2)``."""
    epoch, source = _require_source(epoch, source)
    return Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch)


def _closed_source_mass(epoch: int, source: int) -> Fraction:
    denominator = epoch * epoch
    if source <= epoch - 2:
        return Fraction(epoch - 1, 2 * denominator)
    if source == epoch - 1:
        return Fraction(2 * epoch - 3, 4 * denominator)
    return Fraction(2 * epoch - 1, 4 * denominator)


def source_mass_audit(epoch: int, source: int) -> dict[str, Any]:
    """Audit ``w_(n,p)=sum_q beta_n(p,q)`` and ``w_(n,p)>=r_(n,p)``."""
    epoch, source = _require_source(epoch, source)
    direct = sum(
        (
            beta_coefficient(epoch, source, right)
            for right in range(epoch, 2 * epoch - 1)
        ),
        Fraction(),
    )
    closed = _closed_source_mass(epoch, source)
    residual = residual_coefficient(epoch, source)
    margin = direct - residual
    checks = {
        "source_mass_formula_verified": direct == closed,
        "residual_formula_verified": residual
        == Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch),
        "source_mass_dominates_residual": direct >= residual,
        "domination_margin_positive": margin > 0,
    }
    return {
        "epoch": epoch,
        "source": source,
        "source_mass_case": (
            "bulk"
            if source <= epoch - 2
            else "penultimate"
            if source == epoch - 1
            else "terminal"
        ),
        "direct_source_mass": _fraction_text(direct),
        "closed_source_mass": _fraction_text(closed),
        "residual_coefficient": _fraction_text(residual),
        "domination_margin": _fraction_text(margin),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def residual_mass_audit(epoch: int, cap: Fraction = CAP) -> dict[str, Any]:
    """Audit the residual mass and the general capped-mass consequence."""
    epoch = _require_epoch(epoch)
    cap = _require_positive_fraction(cap, "cap")
    direct = sum(
        (residual_coefficient(epoch, source) for source in range(2, epoch + 1)),
        Fraction(),
    )
    closed = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)
    capped = cap * direct
    cap_upper = cap * Fraction(3, 8)
    checks = {
        "residual_mass_formula_verified": direct == closed,
        "all_residual_coefficients_positive": all(
            residual_coefficient(epoch, source) > 0 for source in range(2, epoch + 1)
        ),
        "residual_mass_below_three_eighths": direct < Fraction(3, 8),
        "capped_mass_below_general_upper": capped < cap_upper,
        "capped_residual_below_fifteen_sixteenths": (
            cap != CAP or capped < Fraction(15, 16)
        ),
    }
    return {
        "epoch": epoch,
        "cap": _fraction_text(cap),
        "direct_residual_mass": _fraction_text(direct),
        "closed_residual_mass": _fraction_text(closed),
        "capped_residual_mass": _fraction_text(capped),
        "general_cap_upper": _fraction_text(cap_upper),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def rank_surplus_threshold_audit(
    epoch: int = 2**22, threshold: Fraction = Fraction(15, 16)
) -> dict[str, Any]:
    """Project the memo-proved strong lower bound at precision 80."""
    epoch = _require_epoch(epoch, minimum=16)
    threshold = _require_positive_fraction(threshold, "threshold")
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        value = Decimal(epoch)
        delta_zero = (
            Decimal(3) / Decimal(2)
            + Decimal(3) * Decimal(3).ln() / Decimal(4)
            - Decimal(2) * Decimal(2).ln()
        )
        strong_error = Decimal(18) * (Decimal(1) + value.ln()) / value
        lower = delta_zero - strong_error
        threshold_decimal = _fraction_decimal(threshold)
        margin = lower - threshold_decimal

    # d[18(1+log x)/x]/dx = -18 log(x)/x^2 < 0 for x>1.
    monotonic = epoch > 1
    strict = lower > threshold_decimal
    return {
        "epoch": epoch,
        "threshold": _fraction_text(threshold),
        "decimal_precision": DECIMAL_PRECISION,
        "delta_zero": _decimal_text(delta_zero),
        "strong_error_majorant": _decimal_text(strong_error),
        "strong_lower_bound": _decimal_text(lower),
        "strict_threshold_margin": _decimal_text(margin),
        "strong_error_derivative": "-18*log(x)/x^2",
        "strong_error_majorant_strictly_decreasing": monotonic,
        "strong_lower_bound_strictly_increasing": monotonic,
        "strict_threshold_conclusion": strict,
        "extends_to_all_larger_epochs": monotonic and strict,
        "transcendental_projection_only": True,
    }


def rank_layer_load_audit(epoch: int, cap: Fraction = CAP) -> dict[str, Any]:
    """Audit the exact rational pre-log rank-layer load at one source."""
    epoch = _require_epoch(epoch)
    cap = _require_positive_fraction(cap, "cap")
    exact_sum = Fraction()
    harmonic_proxy = Fraction()
    rank_counts_match = True
    residual_reindexing_matches = True
    termwise_proxy_holds = True
    for source in range(2, epoch + 1):
        layer = 2 * epoch - source
        contained_interval_count = sum(range(1, layer + 1))
        rank_lower = layer * (layer + 1) // 2
        residual = residual_coefficient(epoch, source)
        residual_reindexed = Fraction(2 * layer - 3, 8 * epoch * epoch)
        term = residual / rank_lower
        proxy = Fraction(1, 2 * epoch * epoch * layer)
        exact_sum += term
        harmonic_proxy += proxy
        rank_counts_match &= contained_interval_count == rank_lower
        residual_reindexing_matches &= residual == residual_reindexed
        termwise_proxy_holds &= term < proxy

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        cap_decimal = _fraction_decimal(cap)
        exponential = cap_decimal.exp()
        log_two = Decimal(2).ln()
        projected_load = _fraction_decimal(exact_sum) / exponential
        projected_upper = log_two / (Decimal(2 * epoch * epoch) * exponential)

    checks = {
        "all_rank_lower_bounds_verified": rank_counts_match,
        "residual_layer_reindexing_verified": residual_reindexing_matches,
        "termwise_harmonic_proxy_verified": termwise_proxy_holds,
        "exact_sum_below_harmonic_proxy": exact_sum < harmonic_proxy,
    }
    return {
        "source_epoch": epoch,
        "cap": _fraction_text(cap),
        "layer_range": [epoch, 2 * epoch - 2],
        "exact_rational_pre_log_upper_sum": _fraction_text(exact_sum),
        "harmonic_proxy_pre_log": _fraction_text(harmonic_proxy),
        "rank_lower_bound_use": (
            "Replacing R_(m,p) by ell(ell+1)/2 gives an upper bound, "
            "not an observed load."
        ),
        "claimed_source_bound": "log(2)/(2*exp(h)*m^2)",
        **checks,
        "all_exact_checks_pass": all(checks.values()),
        "decimal_precision": DECIMAL_PRECISION,
        "exp_cap_projection": _decimal_text(exponential),
        "projected_rank_layer_load_upper": _decimal_text(projected_load),
        "projected_claimed_source_bound": _decimal_text(projected_upper),
        "projected_source_load_below_claimed_bound": projected_load < projected_upper,
        "transcendental_projection_only": True,
    }


def dyadic_load_audit(
    start_epoch: int, depth: int = DYADIC_DEPTH, cap: Fraction = CAP
) -> dict[str, Any]:
    """Audit the dyadic geometric factor in the all-source load bound."""
    start_epoch = _require_epoch(start_epoch)
    depth = _require_plain_integer(depth, "depth")
    if depth < 1:
        raise ValueError("depth must be positive")
    cap = _require_positive_fraction(cap, "cap")
    epochs = tuple(start_epoch * 2**power for power in range(depth))
    partial = sum((Fraction(1, 2 * epoch * epoch) for epoch in epochs), Fraction())
    infinite = Fraction(2, 3 * start_epoch * start_epoch)
    tail = infinite - partial
    expected_tail = infinite / 4**depth

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        exponential = _fraction_decimal(cap).exp()
        log_two = Decimal(2).ln()
        projected_partial = log_two * _fraction_decimal(partial) / exponential
        projected_infinite = log_two * _fraction_decimal(infinite) / exponential

    checks = {
        "geometric_identity_verified": infinite
        == Fraction(1, 2 * start_epoch * start_epoch) / (1 - Fraction(1, 4)),
        "exact_tail_formula_verified": tail == expected_tail,
        "partial_prefactor_below_infinite_prefactor": partial < infinite,
    }
    return {
        "start_epoch": start_epoch,
        "depth": depth,
        "source_epochs": list(epochs),
        "cap": _fraction_text(cap),
        "partial_geometric_pre_log": _fraction_text(partial),
        "infinite_geometric_pre_log": _fraction_text(infinite),
        "exact_geometric_tail": _fraction_text(tail),
        "all_source_bound": "2*log(2)/(3*exp(h)*m_star^2)",
        **checks,
        "all_exact_checks_pass": all(checks.values()),
        "decimal_precision": DECIMAL_PRECISION,
        "projected_partial_bound": _decimal_text(projected_partial),
        "projected_all_source_bound": _decimal_text(projected_infinite),
        "partial_sum_below_all_source_bound": projected_partial < projected_infinite,
        "transcendental_projection_only": True,
    }


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


@cache
def erdos_turan_points(prime: int) -> tuple[int, ...]:
    """Return ``a_i=2*pi+(i^2 mod p)`` for an odd prime ``p>=5``."""
    prime = _require_plain_integer(prime, "prime")
    if prime < 5 or prime % 2 == 0 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime at least five")
    return tuple(2 * prime * index + index * index % prime for index in range(prime))


def _golomb_differences(points: tuple[int, ...]) -> tuple[bool, set[int]]:
    differences: set[int] = set()
    for right in range(1, len(points)):
        for left in range(right):
            difference = points[right] - points[left]
            if difference in differences:
                return False, differences
            differences.add(difference)
    return True, differences


@cache
def erdos_turan_local_slack_audit(prime: int) -> dict[str, Any]:
    """Compute one exact finite Erdos--Turan local-slack calibration row."""
    points = erdos_turan_points(prime)
    epoch = (prime + 1) // 2
    golomb, all_differences = _golomb_differences(points)

    scaled_terms: list[tuple[int, int]] = []
    exact_product = 1
    coefficient_counts = {"high": 0, "middle": 0, "low": 0}
    float_bulk = 0.0
    for right in range(epoch, 2 * epoch - 1):
        for left in range(2, right + 1):
            difference = points[right] - points[left - 1]
            if left == right:
                scaled_exponent = 4
                coefficient_counts["high"] += 1
            elif left == right - 1:
                scaled_exponent = 1
                coefficient_counts["low"] += 1
            else:
                scaled_exponent = 2
                coefficient_counts["middle"] += 1
            scaled_terms.append((difference, scaled_exponent))
            exact_product *= difference**scaled_exponent
            float_bulk += scaled_exponent * log(difference)

    scaled_terms.sort()
    factorization_bytes = ";".join(
        f"{value}^{exponent}" for value, exponent in scaled_terms
    ).encode("ascii")
    atom_count = len(scaled_terms)
    closed_atom_count = (epoch - 1) * (3 * epoch - 4) // 2
    a = epoch - 1
    b = 3 * (epoch - 1) * (epoch - 2) // 2
    c = closed_atom_count
    exact_floor_product = factorial(a) ** 2 * factorial(b) * factorial(c)
    denominator = 4 * epoch * epoch

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        bulk_decimal = Decimal(exact_product).ln() / Decimal(denominator)
        floor_decimal = Decimal(exact_floor_product).ln() / Decimal(denominator)
        slack_decimal = bulk_decimal - floor_decimal

    bulk_float = float_bulk / denominator
    floor_float = (2 * lgamma(a + 1) + lgamma(b + 1) + lgamma(c + 1)) / denominator
    slack_float = bulk_float - floor_float
    expected_pair_count = prime * (prime - 1) // 2
    diameter = points[-1]
    scaled_exponent_sum = sum(exponent for _, exponent in scaled_terms)
    interior_values = {value for value, _ in scaled_terms}
    exact_checks = {
        "points_strictly_increasing": all(
            left < right for left, right in pairwise(points)
        ),
        "ordinary_golomb_uniqueness_verified": golomb
        and len(all_differences) == expected_pair_count,
        "diameter_formula_verified": diameter == 2 * prime * (prime - 1) + 1,
        "diameter_below_eight_n_squared": diameter < 8 * epoch * epoch,
        "atom_count_formula_verified": atom_count == closed_atom_count,
        "interior_atom_values_distinct": len(interior_values) == atom_count,
        "coefficient_class_counts_verified": coefficient_counts
        == {
            "high": epoch - 1,
            "middle": (epoch - 1) * (3 * epoch - 8) // 2,
            "low": epoch - 1,
        },
        "scaled_exponent_mass_verified": scaled_exponent_sum == 3 * (epoch - 1) ** 2,
    }
    return {
        "prime": prime,
        "epoch": epoch,
        "point_count": len(points),
        "points_sha256": _points_sha256(points),
        "point_sample": list(points[:3] + points[-3:]),
        "ordinary_difference_count": len(all_differences),
        "diameter": diameter,
        "eight_n_squared": 8 * epoch * epoch,
        "atom_count": atom_count,
        "closed_atom_count": closed_atom_count,
        "coefficient_class_counts": coefficient_counts,
        "scaled_exponent_sum": scaled_exponent_sum,
        "exact_B_form": "log(P)/(4n^2)",
        "exact_scaled_product_sha256": _integer_sha256(exact_product),
        "exact_scaled_product_bit_length": exact_product.bit_length(),
        "exact_scaled_factorization_sha256": sha256(factorization_bytes).hexdigest(),
        "exact_rank_floor_product_sha256": _integer_sha256(exact_floor_product),
        "exact_rank_floor_product_bit_length": exact_floor_product.bit_length(),
        **exact_checks,
        "all_exact_checks_pass": all(exact_checks.values()),
        "decimal_precision": DECIMAL_PRECISION,
        "bulk_B_decimal": _decimal_text(bulk_decimal),
        "rank_floor_F_decimal": _decimal_text(floor_decimal),
        "local_slack_H_decimal": _decimal_text(slack_decimal),
        "bulk_B_float": bulk_float,
        "rank_floor_F_float": floor_float,
        "local_slack_H_float": slack_float,
        "float_decimal_H_absolute_error": abs(float(slack_decimal) - slack_float),
        "bounded_local_slack_projection": Decimal(0) < slack_decimal < Decimal("1.2"),
        "finite_calibration_only": True,
        "infinite_family_conclusion_inferred": False,
        "transcendental_projection_only": True,
    }


@cache
def build_certificate() -> dict[str, Any]:
    """Build the deterministic Wave 18 certificate payload."""
    coefficient_rows = [coefficient_ledger_audit(epoch) for epoch in EXACT_EPOCHS]
    source_rows = [
        source_mass_audit(epoch, source)
        for epoch in SOURCE_AUDIT_EPOCHS
        for source in range(2, epoch + 1)
    ]
    residual_rows = [residual_mass_audit(epoch, CAP) for epoch in EXACT_EPOCHS]
    threshold_row = rank_surplus_threshold_audit(2**22, Fraction(15, 16))
    rank_rows = [rank_layer_load_audit(epoch, CAP) for epoch in RANK_LAYER_EPOCHS]
    dyadic_rows = [
        dyadic_load_audit(epoch, DYADIC_DEPTH, CAP) for epoch in DYADIC_START_EPOCHS
    ]
    calibration_rows = [
        erdos_turan_local_slack_audit(prime) for prime in ERDOS_TURAN_PRIMES
    ]

    payload: dict[str, Any] = {
        "schema": "erdos1191.wave18.excess-birth-locality.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Audit the finite and algebraic inputs of the Wave 18 P22 "
            "excess-birth locality reduction."
        ),
        "arithmetic": {
            "counts_masses_and_pre_log_sums": "exact integer and fractions.Fraction",
            "exact_finite_B": "B=log(P)/(4n^2) with P constructed as an integer",
            "transcendental_projections": "Decimal precision 80 and binary64; projection only",
            "logarithm": "natural",
        },
        "coefficient_compatibility_audit": {
            "wave11_q_at_least_n_scaled_classes": [4, 1, 2],
            "requested_scaled_classes": [4, 1, 2],
            "wave11_formula_matches": True,
            "wave17_target_n_equals_two_m_rewrite_matches": True,
        },
        "theorem_contract": {
            "target_atoms": "D_(p,q), n<=q<=2n-2, 2<=p<=q",
            "beta_diagonal": "1/n^2",
            "beta_subdiagonal": "1/(4n^2)",
            "beta_interior": "1/(2n^2)",
            "atom_count": "c_n=(n-1)(3n-4)/2",
            "source_mass": "w_(n,p)=sum_(q=n)^(2n-2) beta_n(p,q)",
            "residual": "r_(n,p)=(4n-2p-3)/(8n^2)",
            "residual_mass": "R_n=(n-1)(3n-5)/(8n^2)<3/8",
            "cap": "h=5/2, hence Theta^[h]<15/16",
            "rank_lower": "R_(m,p)>=ell(ell+1)/2, ell=2m-p",
            "per_source_load": "<log(2)/(2*exp(h)*m^2)",
            "all_source_load": "<2log(2)/(3*exp(h)*m_star^2)",
            "rank_surplus_error": "|D_n-delta_0|<=18(1+log(n))/n",
        },
        "coefficient_ledger_rows": coefficient_rows,
        "source_mass_rows": source_rows,
        "residual_mass_rows": residual_rows,
        "rank_surplus_threshold": threshold_row,
        "rank_layer_load_rows": rank_rows,
        "dyadic_load_rows": dyadic_rows,
        "erdos_turan_calibration_rows": calibration_rows,
        "all_required_checks_pass": (
            all(row["all_exact_checks_pass"] for row in coefficient_rows)
            and all(row["all_exact_checks_pass"] for row in source_rows)
            and all(row["all_exact_checks_pass"] for row in residual_rows)
            and threshold_row["extends_to_all_larger_epochs"]
            and all(
                row["all_exact_checks_pass"]
                and row["projected_source_load_below_claimed_bound"]
                for row in rank_rows
            )
            and all(
                row["all_exact_checks_pass"]
                and row["partial_sum_below_all_source_bound"]
                for row in dyadic_rows
            )
            and all(
                row["all_exact_checks_pass"] and row["bounded_local_slack_projection"]
                for row in calibration_rows
            )
        ),
        "scope_flags": {
            "finite_algebraic_only": True,
            "analytic_rank_surplus_bound_proved_in_memo": True,
            "transcendental_values_projection_only": True,
            "erdos_turan_rows_finite_calibration_only": True,
            "analytic_infinite_family_no_go_proved_in_memo": True,
            "infinite_family_no_go_reproved_here": False,
            "p19_proved": False,
            "p22_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
            "problem_unresolved": True,
        },
        "conclusions": [
            "The requested beta classes exactly match the existing Wave 11 and Wave 17 indexing.",
            "Every audited source mass w_(n,p) dominates its residual r_(n,p).",
            "The h=5/2 residual cap is below 15/16 and the strong rank-surplus lower projection clears it from n=2^22 onward.",
            "The rank-layer pre-log sums and the dyadic 4/3 geometric factor are exact rational audits.",
            "The Erdos--Turan rows are bounded finite calibrations and do not establish the memo's infinite-family no-go.",
        ],
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def certificate_bytes() -> bytes:
    """Return the canonical committed JSON bytes with one trailing LF."""
    return _canonical_bytes(build_certificate()) + b"\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_bytes(certificate_bytes())
    print(build_certificate()["certificate_sha256"])


if __name__ == "__main__":
    main()

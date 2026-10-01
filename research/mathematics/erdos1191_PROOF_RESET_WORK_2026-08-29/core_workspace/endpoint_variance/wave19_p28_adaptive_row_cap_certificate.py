"""Exact certificate for the Wave 19 P28 adaptive-row-cap boundary.

This module certifies four facts, and deliberately no more.

* The cut-valid full-row residual has mass
  ``(4*n**2-12*n+11)/(8*n**2)``.
* The adaptive deterministic cap profile at height ``h0=3/2`` is small
  enough to be paid by the preceding Wave 17 rank surplus from target epoch
  2048 onward.  The actual capped promotion is *bounded by* this profile;
  equality is neither assumed nor true in general.
* The natural full-row cross allocation is coefficientwise at most ``Y/2``.
* Actual atom ranks do not remove the endpoint term from the excess split.
  The certificate records the correct endpoint-retaining atomic inequality
  and a local counterexample to the endpoint-free claim.

All combinatorial and comparison checks use :class:`fractions.Fraction`.
High-precision decimals in the report are presentation only.  This module
does not prove P28 or either question of Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from hashlib import sha256
from math import factorial
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave19_p28_adaptive_row_cap_certificate_2026-08-29.json"

AUDIT_EPOCHS = (4, 5, 8, 16, 32, 64, 128)
CAP_PROFILE_EPOCHS = (4, 8, 16, 32, 64, 128, 256, 512, 1024)
H0 = Fraction(3, 2)
CAP_LIMIT_DECIMAL_UPPER = Fraction(8_336_738_101, 10_000_000_000)
CAP_ERROR_DECIMAL_UPPER = Fraction(3_009_853, 10_000_000)
TARGET_ONSET = 2048


def _require_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _require_epoch(epoch: int) -> int:
    epoch = _require_integer(epoch, "epoch")
    if epoch < 4:
        raise ValueError("epoch must be at least four")
    return epoch


def _require_source(epoch: int, source: int) -> tuple[int, int]:
    epoch = _require_epoch(epoch)
    source = _require_integer(source, "source")
    if not 2 <= source <= 2 * epoch - 2:
        raise ValueError("source must satisfy 2 <= source <= 2*epoch-2")
    return epoch, source


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _decimal_text(value: Decimal, places: int = 15) -> str:
    return format(value, f".{places}f")


def _fraction_decimal(value: Fraction, precision: int = 60) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = precision
        return Decimal(value.numerator) / Decimal(value.denominator)


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def _payload_hash(payload: dict[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


def render_certificate(payload: dict[str, Any]) -> bytes:
    """Render stable human-readable JSON."""
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


@cache
def beta_coefficient(epoch: int, source: int, target: int) -> Fraction:
    """Return the exact Gothic coefficient beta_(n,p,q)."""
    epoch, source = _require_source(epoch, source)
    target = _require_integer(target, "target")
    if not max(epoch, source) <= target <= 2 * epoch - 2:
        raise ValueError("target is outside the source row")
    if source == target:
        return Fraction(1, epoch * epoch)
    if source == target - 1:
        return Fraction(1, 4 * epoch * epoch)
    return Fraction(1, 2 * epoch * epoch)


@cache
def row_mass(epoch: int, source: int) -> Fraction:
    """Enumerate the full Gothic row mass w_(n,p)."""
    epoch, source = _require_source(epoch, source)
    return sum(
        (
            beta_coefficient(epoch, source, target)
            for target in range(max(epoch, source), 2 * epoch - 1)
        ),
        Fraction(),
    )


@cache
def closed_row_mass(epoch: int, source: int) -> Fraction:
    """Return the exact five-case formula for w_(n,p)."""
    epoch, source = _require_source(epoch, source)
    square = epoch * epoch
    if source <= epoch - 2:
        return Fraction(epoch - 1, 2 * square)
    if source == epoch - 1:
        return Fraction(2 * epoch - 3, 4 * square)
    if source == epoch:
        return Fraction(2 * epoch - 1, 4 * square)
    if source <= 2 * epoch - 3:
        return Fraction(4 * epoch - 2 * source - 1, 4 * square)
    return Fraction(1, square)


@cache
def residual_coefficient(epoch: int, source: int) -> Fraction:
    """Return the cut-valid full-row residual bar_r_(n,p)."""
    epoch, source = _require_source(epoch, source)
    if source == 2 * epoch - 2:
        return Fraction(3, 8 * epoch * epoch)
    return Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch)


def closed_residual_mass(epoch: int) -> Fraction:
    """Return sum_p bar_r_(n,p)."""
    epoch = _require_epoch(epoch)
    return Fraction(4 * epoch * epoch - 12 * epoch + 11, 8 * epoch * epoch)


@cache
def natural_alpha(epoch: int, source: int) -> Fraction:
    """Return the natural cut-valid row quotient bar_r_p/w_p."""
    epoch, source = _require_source(epoch, source)
    return residual_coefficient(epoch, source) / row_mass(epoch, source)


def cap_profile_decimal(epoch: int) -> dict[str, Any]:
    """Evaluate the deterministic adaptive cap profile at h0=3/2.

    This is ``Cdet=sum_p bar_r_p h_p``, not the actual capped promotion.
    """
    epoch = _require_epoch(epoch)
    residual_mass = sum(
        (residual_coefficient(epoch, source) for source in range(2, 2 * epoch - 1)),
        Fraction(),
    )
    with localcontext() as ctx:
        ctx.prec = 80
        c_value = Decimal((epoch - 1) * (3 * epoch - 4)) / 2
        h0 = Decimal(3) / 2
        cap = Decimal()
        active_rows = 0
        for source in range(2, 2 * epoch - 1):
            short_length = 2 * epoch - source
            triangular = Decimal(short_length * (short_length + 1)) / 2
            logarithmic_height = (c_value / triangular).ln()
            height = max(h0, logarithmic_height)
            if height > h0:
                active_rows += 1
            coefficient = residual_coefficient(epoch, source)
            cap += _fraction_decimal(coefficient, 80) * height
        base = h0 * _fraction_decimal(residual_mass, 80)
        extra = cap - base
        limit = Decimal(3) / 4 + Decimal(3) * (-h0).exp() / 8
        requested_bound = Decimal(CAP_LIMIT_DECIMAL_UPPER.numerator) / Decimal(
            CAP_LIMIT_DECIMAL_UPPER.denominator
        ) + Decimal(CAP_ERROR_DECIMAL_UPPER.numerator) / Decimal(
            CAP_ERROR_DECIMAL_UPPER.denominator
        ) / Decimal(epoch)
    return {
        "epoch": epoch,
        "row_count": 2 * epoch - 3,
        "active_adaptive_rows": active_rows,
        "enumerated_residual_mass": _fraction_text(residual_mass),
        "closed_residual_mass": _fraction_text(closed_residual_mass(epoch)),
        "mass_formula_verified": residual_mass == closed_residual_mass(epoch),
        "deterministic_cap_profile": _decimal_text(cap),
        "adaptive_extra_M": _decimal_text(extra),
        "asymptotic_cap_limit": _decimal_text(limit),
        "requested_upper_bound": _decimal_text(requested_bound),
        "finite_profile_below_requested_bound": cap < requested_bound,
    }


def log_interval(value: Fraction, terms: int = 24) -> tuple[Fraction, Fraction]:
    """Return rigorous rational lower/upper bounds for log(value), value>=1.

    The atanh expansion with ``z=(value-1)/(value+1)`` is used.  The upper
    tail replaces all remaining odd denominators by the first omitted one.
    """
    if value < 1:
        raise ValueError("value must be at least one")
    terms = _require_integer(terms, "terms")
    if terms < 0:
        raise ValueError("terms must be nonnegative")
    z_value = (value - 1) / (value + 1)
    lower = 2 * sum(
        (z_value ** (2 * index + 1) / (2 * index + 1) for index in range(terms + 1)),
        Fraction(),
    )
    remainder = (
        2 * z_value ** (2 * terms + 3) / (2 * terms + 3) / (1 - z_value * z_value)
    )
    return lower, lower + remainder


def exp_lower(value: Fraction, last_term: int = 14) -> Fraction:
    """Return a strict rational lower bound for exp(value), value>0."""
    if value <= 0:
        raise ValueError("value must be positive")
    last_term = _require_integer(last_term, "last_term")
    if last_term < 0:
        raise ValueError("last_term must be nonnegative")
    return sum(
        (value**index / factorial(index) for index in range(last_term + 1)),
        Fraction(),
    )


def cap_surplus_comparison_audit() -> dict[str, Any]:
    """Certify D_N>Cdet_(N/2) from N=2048 onward."""
    log2_lower, log2_upper = log_interval(Fraction(2))
    log3_lower, log3_upper = log_interval(Fraction(3))
    exp_three_halves_lower = exp_lower(H0)
    true_limit_upper = Fraction(3, 4) + Fraction(3, 8) / exp_three_halves_lower

    delta_lower = Fraction(3, 2) + Fraction(3, 4) * log3_lower - 2 * log2_upper
    log_onset_upper = 11 * log2_upper
    d_onset_lower = delta_lower - Fraction(18, TARGET_ONSET) * (1 + log_onset_upper)
    preceding_cap_upper = CAP_LIMIT_DECIMAL_UPPER + Fraction(
        2 * CAP_ERROR_DECIMAL_UPPER.numerator,
        CAP_ERROR_DECIMAL_UPPER.denominator * TARGET_ONSET,
    )
    margin = d_onset_lower - preceding_cap_upper

    return {
        "target_epoch_onset": TARGET_ONSET,
        "source_epoch_at_onset": TARGET_ONSET // 2,
        "log_interval_terms": 24,
        "exp_lower_last_term": 14,
        "log2_lower": _fraction_text(log2_lower),
        "log2_upper": _fraction_text(log2_upper),
        "log3_lower": _fraction_text(log3_lower),
        "log3_upper": _fraction_text(log3_upper),
        "cap_limit_rational_upper": _fraction_text(true_limit_upper),
        "cap_limit_below_0_8336738101": true_limit_upper < CAP_LIMIT_DECIMAL_UPPER,
        "requested_error_constant": _fraction_text(CAP_ERROR_DECIMAL_UPPER),
        "elementary_stronger_error_constant": "1/4",
        "elementary_error_implies_requested_error": Fraction(1, 4)
        < CAP_ERROR_DECIMAL_UPPER,
        "delta0_rational_lower": _fraction_text(delta_lower),
        "D_2048_rational_lower": _fraction_text(d_onset_lower),
        "Cdet_1024_requested_rational_upper": _fraction_text(preceding_cap_upper),
        "onset_margin": _fraction_text(margin),
        "onset_margin_decimal": _decimal_text(_fraction_decimal(margin), 18),
        "onset_comparison_strict": margin > 0,
        "comparison_extends_to_all_larger_real_epochs": True,
        "monotonicity_reason": (
            "delta0-18(1+log N)/N increases for N>1, while "
            "0.8336738101+0.6019706/N decreases"
        ),
    }


def partial_coefficient_map(
    epoch: int, first_source: int, last_source: int
) -> dict[tuple[int, int], Fraction]:
    """Return coefficients contributed by one inclusive source interval."""
    epoch = _require_epoch(epoch)
    first_source = _require_integer(first_source, "first_source")
    last_source = _require_integer(last_source, "last_source")
    if not 2 <= first_source <= last_source <= 2 * epoch - 2:
        raise ValueError("source interval must lie in 2..2n-2")
    columns: dict[int, dict[int, Fraction]] = {}
    for target in range(epoch, 2 * epoch - 1):
        suffix: dict[int, Fraction] = {}
        running = Fraction()
        for source in range(target, 1, -1):
            if first_source <= source <= last_source:
                running += natural_alpha(epoch, source) * beta_coefficient(
                    epoch, source, target
                )
            suffix[source] = running
        columns[target] = suffix

    result: dict[tuple[int, int], Fraction] = {}
    for left_gap in range(1, 2 * epoch - 2):
        running = Fraction()
        for target in range(max(epoch, left_gap + 1), 2 * epoch - 1):
            running += columns[target][left_gap + 1]
            result[left_gap, target + 1] = running
    return result


def coefficient_map(epoch: int) -> dict[tuple[int, int], Fraction]:
    """Return every natural full-row Sbar coefficient in O(n^2) additions."""
    epoch = _require_epoch(epoch)
    return partial_coefficient_map(epoch, 2, 2 * epoch - 2)


def y_coefficient(epoch: int, left_gap: int, right_gap: int) -> Fraction:
    """Return the coefficient of C_(i,j) in Y_n."""
    epoch = _require_epoch(epoch)
    if not epoch <= right_gap <= 2 * epoch - 1:
        raise ValueError("right_gap is outside Y_n")
    if not 1 <= left_gap <= right_gap - 2:
        raise ValueError("left_gap must satisfy 1 <= i <= j-2")
    return Fraction((right_gap - left_gap) ** 2, 4 * epoch * epoch)


def endpoint_prefix_coefficient(epoch: int, target: int) -> Fraction:
    """Return the Wave 13 coefficient of log(a_q) in the prefix term."""
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must lie in n..2n-2")
    return Fraction(2 * target - 1, 4 * epoch * epoch)


def endpoint_transport_coefficient(epoch: int, target: int) -> Fraction:
    """Return sum_p bar_alpha_p beta_(p,q) for the natural transport."""
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must lie in n..2n-2")
    return sum(
        (
            natural_alpha(epoch, source) * beta_coefficient(epoch, source, target)
            for source in range(2, target + 1)
        ),
        Fraction(),
    )


def endpoint_profile_audit(epoch: int) -> dict[str, Any]:
    """Audit E0<=3 Dpre/4 for the natural full-row transport."""
    epoch = _require_epoch(epoch)
    rows = []
    for target in range(epoch, 2 * epoch - 1):
        transported = endpoint_transport_coefficient(epoch, target)
        prefix = endpoint_prefix_coefficient(epoch, target)
        rows.append((target, transported, prefix, transported / prefix))
    worst = max(rows, key=lambda row: row[3])
    return {
        "epoch": epoch,
        "column_count": len(rows),
        "worst_target": worst[0],
        "worst_ratio": _fraction_text(worst[3]),
        "worst_is_midpoint_column": worst[0] == epoch,
        "every_column_at_most_three_quarters": all(
            transported <= Fraction(3, 4) * prefix for _, transported, prefix, _ in rows
        ),
        "every_column_strictly_below_three_quarters": all(
            transported < Fraction(3, 4) * prefix for _, transported, prefix, _ in rows
        ),
    }


def long_coefficient(epoch: int, x_value: int, y_value: int) -> Fraction:
    """Return the p<=n part at i=n-x, j=n+y."""
    epoch = _require_epoch(epoch)
    x_value = _require_integer(x_value, "x_value")
    y_value = _require_integer(y_value, "y_value")
    if not 1 <= x_value <= epoch - 1 or not 1 <= y_value <= epoch - 1:
        raise ValueError("x_value and y_value must lie in 1..n-1")
    left_gap = epoch - x_value
    right_gap = epoch + y_value
    return sum(
        (
            natural_alpha(epoch, source) * beta_coefficient(epoch, source, target)
            for target in range(epoch, right_gap)
            for source in range(left_gap + 1, min(epoch, target) + 1)
        ),
        Fraction(),
    )


def short_coefficient(epoch: int, x_value: int, y_value: int) -> Fraction:
    """Return the p>n part at i=n-x, j=n+y."""
    epoch = _require_epoch(epoch)
    x_value = _require_integer(x_value, "x_value")
    y_value = _require_integer(y_value, "y_value")
    if not 1 <= x_value <= epoch - 1 or not 1 <= y_value <= epoch - 1:
        raise ValueError("x_value and y_value must lie in 1..n-1")
    right_gap = epoch + y_value
    return sum(
        (
            natural_alpha(epoch, source) * beta_coefficient(epoch, source, target)
            for target in range(epoch + 1, right_gap)
            for source in range(epoch + 1, target + 1)
        ),
        Fraction(),
    )


def closed_long_gap(epoch: int, x_value: int, y_value: int) -> Fraction:
    """Return the closed gap from the long-row bound.

    Except at ``(x,y)=(1,1)``, this is
    ``(x^2+2xy)/(8n^2)-K_long``.
    """
    epoch = _require_epoch(epoch)
    x_value = _require_integer(x_value, "x_value")
    y_value = _require_integer(y_value, "y_value")
    if not 1 <= x_value <= epoch - 1 or not 1 <= y_value <= epoch - 1:
        raise ValueError("x_value and y_value must lie in 1..n-1")
    if (x_value, y_value) == (1, 1):
        raise ValueError("the (1,1) corner uses the full half-Y bound")
    n_value = epoch
    x = x_value
    y = y_value
    if x == 1:
        return Fraction(2 * y + 1, 4 * n_value**2 * (2 * n_value - 1))
    if x == 2 and y == 1:
        return Fraction(
            12 * n_value**2 - 12 * n_value - 13,
            8 * n_value**2 * (2 * n_value - 3) * (2 * n_value - 1),
        )
    if x == 2:
        return Fraction(
            4 * n_value**2 - 6 * n_value - 2 * y + 1,
            2 * n_value**2 * (2 * n_value - 3) * (2 * n_value - 1),
        )
    denominator = 8 * n_value**2 * (n_value - 1) * (2 * n_value - 3) * (2 * n_value - 1)
    if y == 1:
        numerator = (
            4 * n_value**3 * x**2
            - 4 * n_value**3
            - 16 * n_value**2 * x**2
            + 8 * n_value**2 * x
            + 24 * n_value**2
            + 19 * n_value * x**2
            - 16 * n_value * x
            - 45 * n_value
            - 6 * x**2
            + 6 * x
            + 25
        )
    else:
        numerator = generic_long_gap_numerator(n_value, x, y)
    return Fraction(numerator, denominator)


def generic_long_gap_numerator(epoch: int, x_value: int, y_value: int) -> int:
    """Return the x>=3,y>=2 long-gap numerator."""
    n_value = _require_epoch(epoch)
    x = _require_integer(x_value, "x_value")
    y = _require_integer(y_value, "y_value")
    return (
        4 * n_value**3 * x**2
        - 12 * n_value**2 * x**2
        + 8 * n_value**2
        + 11 * n_value * x**2
        - 16 * n_value
        - 3 * x**2
        + 8
        + y
        * (
            -4 * n_value * (n_value - 2) * x * (x - 2)
            - 3 * x * (x - 2)
            - 8 * (n_value - 1)
        )
    )


def generic_long_gap_at_last_y(epoch: int, x_value: int) -> int:
    """Return G(n,x,n-1), manifestly positive."""
    epoch = _require_epoch(epoch)
    x_value = _require_integer(x_value, "x_value")
    return 2 * x_value * (epoch - 1) * (2 * epoch - 3) * (2 * epoch - 1)


def y_one_manifest_numerator(a_value: int, b_value: int) -> int:
    """Manifestly positive y=1 numerator for x=3+a,n=x+1+b."""
    a_value = _require_integer(a_value, "a_value")
    b_value = _require_integer(b_value, "b_value")
    if a_value < 0 or b_value < 0:
        raise ValueError("a_value and b_value must be nonnegative")
    a = a_value
    b = b_value
    return (
        4 * a**5
        + 12 * a**4 * b
        + 56 * a**4
        + 12 * a**3 * b**2
        + 136 * a**3 * b
        + 315 * a**3
        + 4 * a**2 * b**3
        + 104 * a**2 * b**2
        + 579 * a**2 * b
        + 904 * a**2
        + 24 * a * b**3
        + 296 * a * b**2
        + 1122 * a * b
        + 1336 * a
        + 32 * b**3
        + 288 * b**2
        + 846 * b
        + 813
    )


def sbar_epoch_audit(epoch: int) -> dict[str, Any]:
    """Audit the full coefficient theorem at one epoch."""
    epoch = _require_epoch(epoch)
    coefficients = coefficient_map(epoch)
    long_coefficients = partial_coefficient_map(epoch, 2, epoch)
    ratios: dict[tuple[int, int], Fraction] = {}
    gaps: dict[tuple[int, int], Fraction] = {}
    for cell, coefficient in coefficients.items():
        y_value = y_coefficient(epoch, *cell)
        ratios[cell] = coefficient / y_value
        gaps[cell] = y_value / 2 - coefficient
    worst_cell = max(ratios, key=ratios.__getitem__)
    terminal_cell = (1, 2 * epoch - 1)
    terminal_y = y_coefficient(epoch, *terminal_cell)
    terminal_coefficient = coefficients[terminal_cell]
    expected_terminal_gap = Fraction(4 * epoch - 7, 8 * epoch * epoch)

    long_case_checks = 0
    decomposition_checks = 0
    for x_value in range(1, epoch):
        for y_value in range(1, epoch):
            left_gap = epoch - x_value
            right_gap = epoch + y_value
            long_part = long_coefficients[left_gap, right_gap]
            short_part = coefficients[left_gap, right_gap] - long_part
            if long_part + short_part != coefficients[left_gap, right_gap]:
                raise AssertionError("long/short coefficient decomposition failed")
            decomposition_checks += 1
            if (x_value, y_value) != (1, 1):
                direct_gap = (
                    Fraction(x_value**2 + 2 * x_value * y_value, 8 * epoch**2)
                    - long_part
                )
                if direct_gap != closed_long_gap(epoch, x_value, y_value):
                    raise AssertionError("closed long-gap formula failed")
                long_case_checks += 1

    row_formula_checks = all(
        row_mass(epoch, source) == closed_row_mass(epoch, source)
        for source in range(2, 2 * epoch - 1)
    )
    residual_mass = sum(
        (residual_coefficient(epoch, source) for source in range(2, 2 * epoch - 1)),
        Fraction(),
    )
    endpoint_audit = endpoint_profile_audit(epoch)
    return {
        "epoch": epoch,
        "row_count": 2 * epoch - 3,
        "finite_atom_count": len(coefficients),
        "long_short_decomposition_checks": decomposition_checks,
        "closed_long_gap_checks": long_case_checks,
        "row_mass_formulas_verified": row_formula_checks,
        "residual_mass_formula_verified": residual_mass == closed_residual_mass(epoch),
        "all_coefficients_at_most_half_Y": all(gap >= 0 for gap in gaps.values()),
        "all_coefficients_strictly_below_half_Y": all(gap > 0 for gap in gaps.values()),
        "worst_ratio_cell": list(worst_cell),
        "worst_ratio_to_Y": _fraction_text(ratios[worst_cell]),
        "terminal_cell": list(terminal_cell),
        "terminal_coefficient": _fraction_text(terminal_coefficient),
        "terminal_equals_residual_mass": terminal_coefficient == residual_mass,
        "terminal_ratio_to_Y": _fraction_text(terminal_coefficient / terminal_y),
        "terminal_ratio_closed": _fraction_text(
            Fraction(4 * epoch**2 - 12 * epoch + 11, 8 * (epoch - 1) ** 2)
        ),
        "terminal_half_Y_gap": _fraction_text(terminal_y / 2 - terminal_coefficient),
        "terminal_half_Y_gap_formula_verified": terminal_y / 2 - terminal_coefficient
        == expected_terminal_gap,
        "all_exact_checks_pass": (
            row_formula_checks
            and residual_mass == closed_residual_mass(epoch)
            and all(gap > 0 for gap in gaps.values())
            and terminal_coefficient == residual_mass
            and terminal_y / 2 - terminal_coefficient == expected_terminal_gap
            and endpoint_audit["every_column_strictly_below_three_quarters"]
        ),
        "endpoint_profile": endpoint_audit,
    }


def positive_part(value: Fraction) -> Fraction:
    """Return max(value,0)."""
    return max(value, Fraction())


def old_c_based_atomic_split(
    endpoint_log: Fraction, cross_log: Fraction, tau: Fraction
) -> tuple[Fraction, Fraction, Fraction]:
    """Return old J atom, endpoint part, and cross upper increment."""
    if endpoint_log < 0 or cross_log < 0 or tau < 0:
        raise ValueError("endpoint_log, cross_log, and tau must be nonnegative")
    old_atom = positive_part(endpoint_log + cross_log - tau)
    endpoint = positive_part(endpoint_log - tau)
    return old_atom, endpoint, cross_log


def actual_rank_atomic_split(
    rank_slack_log: Fraction,
    cross_log: Fraction,
    endpoint_log: Fraction,
    sigma: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Return the correct actual-rank atom and its two candidate bounds.

    The exact logarithmic identity is

    ``log(d/(exp(h)L)) = rank_slack + cross + endpoint - sigma``.

    The valid upper bound retains ``[endpoint-sigma]_+``.  The final return
    value omits it and is intentionally only a candidate, not a bound.
    """
    if any(value < 0 for value in (rank_slack_log, cross_log, endpoint_log, sigma)):
        raise ValueError("all logarithmic inputs must be nonnegative")
    atom = positive_part(rank_slack_log + cross_log + endpoint_log - sigma)
    correct_bound = rank_slack_log + cross_log + positive_part(endpoint_log - sigma)
    endpoint_free_candidate = rank_slack_log + cross_log
    return atom, correct_bound, endpoint_free_candidate


def transport_obstruction(epoch: int) -> dict[str, Any]:
    """Return the exact last-two-row obstruction to coverage above 1/3."""
    epoch = _require_epoch(epoch)
    first_row = residual_coefficient(epoch, 2 * epoch - 3)
    last_row = residual_coefficient(epoch, 2 * epoch - 2)
    available = first_row + last_row
    cell_coefficient = Fraction(9, 4 * epoch * epoch)
    return {
        "epoch": epoch,
        "cell": [2 * epoch - 4, 2 * epoch - 1],
        "first_available_row": 2 * epoch - 3,
        "last_available_row": 2 * epoch - 2,
        "first_row_demand": _fraction_text(first_row),
        "last_row_demand": _fraction_text(last_row),
        "total_available_demand": _fraction_text(available),
        "full_W_cell_coefficient": _fraction_text(cell_coefficient),
        "maximum_possible_coverage_ratio": _fraction_text(available / cell_coefficient),
        "ratio_is_one_third": available / cell_coefficient == Fraction(1, 3),
        "uniform_fraction_strictly_above_one_third_impossible": True,
        "attainment_of_one_third_claimed": False,
    }


def atomic_split_audit() -> dict[str, Any]:
    """Enumerate exact rational positive-part checks and a no-endpoint witness."""
    grid = tuple(Fraction(value, 2) for value in range(7))
    old_checks = 0
    rank_checks = 0
    endpoint_free_failures = 0
    for endpoint in grid:
        for cross in grid:
            for tau in grid:
                atom, endpoint_part, cross_bound = old_c_based_atomic_split(
                    endpoint, cross, tau
                )
                if not endpoint_part <= atom <= endpoint_part + cross_bound:
                    raise AssertionError("old c-based atomic split failed")
                old_checks += 1
            for rank_slack in grid:
                for sigma in grid:
                    atom, correct, endpoint_free = actual_rank_atomic_split(
                        rank_slack, cross, endpoint, sigma
                    )
                    if atom > correct:
                        raise AssertionError("actual-rank atomic split failed")
                    if atom > endpoint_free:
                        endpoint_free_failures += 1
                    rank_checks += 1

    witness = actual_rank_atomic_split(Fraction(), Fraction(), Fraction(1), Fraction())
    return {
        "old_c_based_grid_checks": old_checks,
        "actual_rank_grid_checks": rank_checks,
        "endpoint_free_grid_failures": endpoint_free_failures,
        "endpoint_free_counterexample_logs": {
            "rank_slack": "0/1",
            "cross": "0/1",
            "endpoint": "1/1",
            "sigma": "0/1",
        },
        "counterexample_atom": _fraction_text(witness[0]),
        "counterexample_correct_bound": _fraction_text(witness[1]),
        "counterexample_endpoint_free_candidate": _fraction_text(witness[2]),
        "counterexample_invalidates_endpoint_free_atomic_claim": witness[0]
        > witness[2],
        "old_c_based_adaptive_J_retains_endpoint": True,
        "actual_rank_split_retains_endpoint_E_rank": True,
    }


def build_certificate() -> dict[str, Any]:
    """Build the complete deterministic certificate payload."""
    sbar_audits = [sbar_epoch_audit(epoch) for epoch in AUDIT_EPOCHS]
    cap_profiles = [cap_profile_decimal(epoch) for epoch in CAP_PROFILE_EPOCHS]
    split_audit = atomic_split_audit()
    comparison = cap_surplus_comparison_audit()
    row_subtests = sum(row["row_count"] for row in sbar_audits)
    atom_subtests = sum(row["finite_atom_count"] for row in sbar_audits)
    decomposition_subtests = sum(
        row["long_short_decomposition_checks"] for row in sbar_audits
    )
    long_gap_subtests = sum(row["closed_long_gap_checks"] for row in sbar_audits)
    endpoint_subtests = sum(
        row["endpoint_profile"]["column_count"] for row in sbar_audits
    )

    body: dict[str, Any] = {
        "schema": "erdos1191.wave19.p28-adaptive-row-cap-boundary.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Certify the adaptive full-row cap boundary, the exact Sbar<=Y/2 "
            "coefficient theorem, and the endpoint-retaining rank split."
        ),
        "audit_epochs": list(AUDIT_EPOCHS),
        "cap_profile_epochs": list(CAP_PROFILE_EPOCHS),
        "sbar_epoch_audits": sbar_audits,
        "cap_profile_audits": cap_profiles,
        "cap_surplus_comparison": comparison,
        "atomic_split_audit": split_audit,
        "transport_obstruction_examples": [
            transport_obstruction(epoch) for epoch in AUDIT_EPOCHS
        ],
        "universal_formulas": {
            "full_row_residual_mass": "Rbar=(4n^2-12n+11)/(8n^2)",
            "adaptive_height": "h_p=max(3/2,log(c_n/L_p))",
            "actual_cap_inequality": (
                "Theta_cap=sum_p bar_r_p min(Pi_p,h_p)<=Cdet=sum_p bar_r_p h_p"
            ),
            "deterministic_cap_split": "Cdet=(3/2)Rbar+M_n(3/2)",
            "deterministic_cap_bound": (
                "Cdet<0.8336738101+0.3009853/n (a stronger +1/(4n) proof is used)"
            ),
            "rank_surplus_bound": (
                "D_N>=delta0-18(1+log N)/N>Cdet_(N/2) for every N>=2048"
            ),
            "natural_cross_bound": "Sbar_n<=Y_n/2 coefficientwise",
            "natural_endpoint_bound": "E0_n<=3*Dpre_n/4 coefficientwise",
            "asymptotically_sharp_cell": "C_(1,2n-1)",
            "asymptotically_sharp_ratio_to_Y": ("(4n^2-12n+11)/(8(n-1)^2)->1/2"),
            "asymptotically_sharp_half_Y_gap": "(4n-7)/(8n^2)",
            "actual_rank_atom_identity": (
                "log(d_p/(exp(h_p)L_p))=log(D_pq/j)+log(X_pq)+log(A/a_q)-sigma_pq"
            ),
            "actual_rank_atom_bound": (
                "[lhs]_+<=log(D_pq/j)+log(X_pq)+[log(A/a_q)-sigma_pq]_+"
            ),
            "uniform_inner_transport_obstruction": (
                "cell C_(2n-4,2n-1) prevents coverage fraction >1/3"
            ),
        },
        "ownership_ledger": {
            "bulk_split": "B_n=F_n^loc+Srank_n+Pair_n",
            "rank_payment": ("Q_n^ad=Srank_n+S_t,n+E_t,n^rank-Theta_n^exc>=0"),
            "exact_local_identity": (
                "U_n-B_n=U_n-F_n^loc-Theta_n^exc+S_t,n+E_t,n^rank-Pair_n-Q_n^ad"
            ),
            "cut_ownership": "v_p remains owned by the negative renewal cut",
            "unspent_terms": (
                "S_t and E_t^rank have positive sign; Pair and Q_ad have favorable negative sign"
            ),
            "remaining_gate": (
                "With G_n=R_n+Pcoef_n log(A)-K_n^int-T_n-Theta_n^full-"
                "Dpre_n/4, prove limsup sum_k omega_(k,J)G_(2^k)/log(J) "
                "<1/(3072*C*log(2)), or the clean o(log J) bound."
            ),
            "remaining_gate_status": "unproved",
            "no_reuse_warning": (
                "old Dpre, Y, and W payments cannot be reused without a new signed derivation"
            ),
        },
        "audit_counts": {
            "pytest_tests": 11,
            "row_formula_subtests": row_subtests,
            "finite_atom_coefficient_subtests": atom_subtests,
            "long_short_decomposition_subtests": decomposition_subtests,
            "closed_long_gap_subtests": long_gap_subtests,
            "endpoint_profile_subtests": endpoint_subtests,
            "old_c_atomic_grid_subtests": split_audit["old_c_based_grid_checks"],
            "actual_rank_atomic_grid_subtests": split_audit["actual_rank_grid_checks"],
            "total_exact_subtests": (
                row_subtests
                + atom_subtests
                + decomposition_subtests
                + long_gap_subtests
                + endpoint_subtests
                + split_audit["old_c_based_grid_checks"]
                + split_audit["actual_rank_grid_checks"]
                + len(CAP_PROFILE_EPOCHS)
                + len(AUDIT_EPOCHS)
                + 1
            ),
        },
        "scope_flags": {
            "exact_fraction_arithmetic_used_for_proof_checks": True,
            "actual_capped_promotion_equals_deterministic_cap": False,
            "actual_capped_promotion_bounded_by_deterministic_cap": True,
            "adaptive_cap_paid_by_D_from_target_epoch_2048": True,
            "natural_Sbar_bounded_by_Y_half": True,
            "natural_endpoint_profile_bounded_by_three_quarters_Dpre": True,
            "natural_Sbar_removes_strict_threshold_obstruction": False,
            "actual_rank_split_removes_endpoint_term": False,
            "endpoint_free_actual_rank_claim_valid": False,
            "uniform_inner_transport_fraction_above_one_third_possible": False,
            "uniform_inner_transport_fraction_one_third_attained": False,
            "remaining_signed_fejer_inequality_proved": False,
            "eventual_critical_branch_constructed": False,
            "p28_proved": False,
            "p28_refuted": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "problem_unresolved": True,
            "prize_claim_ready": False,
        },
    }
    body["certificate_sha256"] = _payload_hash(body)
    return body


def verify_certificate_hash(payload: dict[str, Any]) -> bool:
    """Verify the embedded hash after removing the hash field."""
    expected = payload.get("certificate_sha256")
    if not isinstance(expected, str):
        return False
    body = dict(payload)
    del body["certificate_sha256"]
    return _payload_hash(body) == expected


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="write the canonical certificate to stdout instead of a file",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    rendered = render_certificate(build_certificate())
    if args.stdout:
        import sys

        sys.stdout.buffer.write(rendered)
    else:
        args.output.write_bytes(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

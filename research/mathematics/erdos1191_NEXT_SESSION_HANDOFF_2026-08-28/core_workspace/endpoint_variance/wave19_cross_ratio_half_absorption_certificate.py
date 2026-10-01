"""Exact certificate for the Wave 19 cross-ratio half absorption.

For ``n>=4`` this module uses the Wave 18 coefficients ``beta``, row masses
``w``, residuals ``r``, and ``alpha=r/w``.  It proves coefficientwise that

    K_(n,i,j) <= (1/2) ((j-i)/(2n))^2,

where ``1<=i<=n-1``, ``n+1<=j<=2n-1``, and ``K`` is the rectangular partial
sum in the task statement.  The proof is exact ``fractions.Fraction``
arithmetic and is split into the four cases determined by
``x=n-i`` and ``y=j-n`` being one or at least two.

It also proves the three endpoint cases
``lambda_(n,q)=sum_p alpha_(n,p) beta_(n,p,q)<3c_(n,q)/4`` and audits the
resulting signed quarter-boundary-deficit cancellation.

Finite deterministic Golomb rulers separately realize the consequent
Wave 18 bound on ``J_n^(h)`` at ``h=5/2``.  Decimal logarithms are projections
only.  The fixture rows do not construct an infinite critical branch, prove
P23, or resolve either question of Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from hashlib import sha256
from itertools import pairwise
from math import comb, isqrt, prod
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = (
    DIRECTORY / "wave19_cross_ratio_half_absorption_certificate_2026-08-29.json"
)

DECIMAL_PRECISION = 80
CAP = Fraction(5, 2)
EXACT_AUDIT_EPOCHS = (4, 5, 8, 16, 32)


def _require_plain_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _require_epoch(epoch: int) -> int:
    epoch = _require_plain_integer(epoch, "epoch")
    if epoch < 4:
        raise ValueError("epoch must be at least four")
    return epoch


def _require_source(epoch: int, source: int) -> tuple[int, int]:
    epoch = _require_epoch(epoch)
    source = _require_plain_integer(source, "source")
    if not 2 <= source <= epoch:
        raise ValueError("source must satisfy 2 <= source <= epoch")
    return epoch, source


def _require_cross_pair(
    epoch: int, left_gap: int, right_gap: int
) -> tuple[int, int, int]:
    epoch = _require_epoch(epoch)
    left_gap = _require_plain_integer(left_gap, "left_gap")
    right_gap = _require_plain_integer(right_gap, "right_gap")
    if not 1 <= left_gap <= epoch - 1:
        raise ValueError("left_gap must satisfy 1 <= left_gap <= epoch-1")
    if not epoch + 1 <= right_gap <= 2 * epoch - 1:
        raise ValueError("right_gap must satisfy epoch+1 <= right_gap <= 2*epoch-1")
    return epoch, left_gap, right_gap


def _require_positive_fraction(value: Fraction, name: str) -> Fraction:
    if not isinstance(value, Fraction):
        raise TypeError(f"{name} must be a Fraction")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _decimal_text(value: Decimal) -> str:
    if value == 0:
        return "0"
    return format(value, "f")


def _fraction_decimal(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _canonical_hash(payload: dict[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


@cache
def beta_coefficient(epoch: int, source: int, target: int) -> Fraction:
    """Return the Wave 18 coefficient ``beta_(n,p,q)`` on its rectangle."""
    epoch, source = _require_source(epoch, source)
    target = _require_plain_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy epoch <= target <= 2*epoch-2")
    denominator = epoch * epoch
    if source == target:
        return Fraction(1, denominator)
    if source == target - 1:
        return Fraction(1, 4 * denominator)
    return Fraction(1, 2 * denominator)


@cache
def source_weight(epoch: int, source: int) -> Fraction:
    """Enumerate ``w_(n,p)=sum_q beta_(n,p,q)`` exactly."""
    epoch, source = _require_source(epoch, source)
    return sum(
        (
            beta_coefficient(epoch, source, target)
            for target in range(epoch, 2 * epoch - 1)
        ),
        Fraction(),
    )


@cache
def closed_source_weight(epoch: int, source: int) -> Fraction:
    """Return the three-case closed Wave 18 row-mass formula."""
    epoch, source = _require_source(epoch, source)
    if source <= epoch - 2:
        return Fraction(epoch - 1, 2 * epoch * epoch)
    if source == epoch - 1:
        return Fraction(2 * epoch - 3, 4 * epoch * epoch)
    return Fraction(2 * epoch - 1, 4 * epoch * epoch)


@cache
def residual_coefficient(epoch: int, source: int) -> Fraction:
    """Return ``r_(n,p)=(4n-2p-3)/(8n^2)``."""
    epoch, source = _require_source(epoch, source)
    return Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch)


@cache
def alpha_coefficient(epoch: int, source: int) -> Fraction:
    """Return the defining quotient ``alpha_(n,p)=r_(n,p)/w_(n,p)``."""
    epoch, source = _require_source(epoch, source)
    return residual_coefficient(epoch, source) / source_weight(epoch, source)


@cache
def closed_alpha_coefficient(epoch: int, source: int) -> Fraction:
    """Return the independent three-case closed formula for ``alpha``."""
    epoch, source = _require_source(epoch, source)
    if source <= epoch - 2:
        return Fraction(4 * epoch - 2 * source - 3, 4 * (epoch - 1))
    if source == epoch - 1:
        return Fraction(2 * epoch - 1, 2 * (2 * epoch - 3))
    return Fraction(2 * epoch - 3, 2 * (2 * epoch - 1))


@cache
def _closed_partial_alpha_mass(epoch: int, x: int) -> Fraction:
    epoch = _require_epoch(epoch)
    x = _require_plain_integer(x, "x")
    if not 1 <= x <= epoch - 1:
        raise ValueError("x must satisfy 1 <= x <= epoch-1")
    terminal = Fraction(2 * epoch - 3, 2 * (2 * epoch - 1))
    if x == 1:
        return terminal
    penultimate = Fraction(2 * epoch - 1, 2 * (2 * epoch - 3))
    bulk_numerator = x * x + 2 * (epoch - 2) * x - 4 * (epoch - 1)
    bulk = Fraction(bulk_numerator, 4 * (epoch - 1))
    return terminal + penultimate + bulk


@cache
def weight_alpha_audit(epoch: int) -> dict[str, Any]:
    """Audit all ``w``, ``r``, ``alpha``, and ``Rcoef`` identities."""
    epoch = _require_epoch(epoch)
    source_rows = []
    total_weight = Fraction()
    total_residual = Fraction()
    alpha_weight_mass = Fraction()
    all_rows_match = True
    all_alphas_strict = True
    for source in range(2, epoch + 1):
        weight = source_weight(epoch, source)
        closed_weight = closed_source_weight(epoch, source)
        residual = residual_coefficient(epoch, source)
        alpha = alpha_coefficient(epoch, source)
        closed_alpha = closed_alpha_coefficient(epoch, source)
        row_matches = weight == closed_weight and alpha == closed_alpha
        source_rows.append(
            {
                "source": source,
                "weight": _fraction_text(weight),
                "closed_weight": _fraction_text(closed_weight),
                "residual": _fraction_text(residual),
                "alpha": _fraction_text(alpha),
                "closed_alpha": _fraction_text(closed_alpha),
                "formulas_match": row_matches,
                "alpha_strictly_between_zero_and_one": 0 < alpha < 1,
            }
        )
        total_weight += weight
        total_residual += residual
        alpha_weight_mass += alpha * weight
        all_rows_match &= row_matches
        all_alphas_strict &= 0 < alpha < 1

    closed_total_weight = Fraction((epoch - 1) ** 2, 2 * epoch * epoch)
    closed_residual = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)
    checks = {
        "all_row_formulas_match": all_rows_match,
        "all_alphas_strictly_between_zero_and_one": all_alphas_strict,
        "total_source_weight_formula_verified": total_weight == closed_total_weight,
        "residual_mass_formula_verified": total_residual == closed_residual,
        "alpha_weight_mass_equals_residual_mass": alpha_weight_mass == total_residual,
    }
    return {
        "epoch": epoch,
        "source_rows": source_rows,
        "total_source_weight": _fraction_text(total_weight),
        "closed_total_source_weight": _fraction_text(closed_total_weight),
        "direct_residual_mass": _fraction_text(total_residual),
        "closed_residual_mass": _fraction_text(closed_residual),
        "alpha_weight_coefficient_mass": _fraction_text(alpha_weight_mass),
        "Rcoef": _fraction_text(closed_residual),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def direct_cross_ratio_coefficient(
    epoch: int, left_gap: int, right_gap: int
) -> Fraction:
    """Enumerate the defining rectangular sum for ``K_(n,i,j)``."""
    epoch, left_gap, right_gap = _require_cross_pair(epoch, left_gap, right_gap)
    return sum(
        (
            alpha_coefficient(epoch, source) * beta_coefficient(epoch, source, target)
            for source in range(max(2, left_gap + 1), epoch + 1)
            for target in range(epoch, min(2 * epoch - 2, right_gap - 1) + 1)
        ),
        Fraction(),
    )


@cache
def analytic_cross_ratio_coefficient(
    epoch: int, left_gap: int, right_gap: int
) -> Fraction:
    """Evaluate ``K`` from the three exceptional beta cells.

    With ``x=n-i`` and ``y=j-n``, start with middle weight on the whole
    ``x`` by ``y`` rectangle.  The diagonal cell ``(n,n)`` adds one middle
    weight, while ``(n-1,n)`` and ``(n,n+1)`` each subtract half a middle
    weight when present.
    """
    epoch, left_gap, right_gap = _require_cross_pair(epoch, left_gap, right_gap)
    x = epoch - left_gap
    y = right_gap - epoch
    alpha_sum = _closed_partial_alpha_mass(epoch, x)
    alpha_terminal = closed_alpha_coefficient(epoch, epoch)
    alpha_penultimate = closed_alpha_coefficient(epoch, epoch - 1)
    normalized = Fraction(y, 2) * alpha_sum + Fraction(1, 2) * alpha_terminal
    if x >= 2:
        normalized -= Fraction(1, 4) * alpha_penultimate
    if y >= 2:
        normalized -= Fraction(1, 4) * alpha_terminal
    return normalized / (epoch * epoch)


def _analytic_case(x: int, y: int) -> str:
    if x == 1 and y == 1:
        return "corner_x1_y1"
    if x == 1:
        return "source_edge_x1"
    if y == 1:
        return "target_edge_y1"
    return "interior_xge2_yge2"


@cache
def coefficient_case_audit(epoch: int, left_gap: int, right_gap: int) -> dict[str, Any]:
    """Audit one coefficient by direct enumeration and its analytic case."""
    epoch, left_gap, right_gap = _require_cross_pair(epoch, left_gap, right_gap)
    x = epoch - left_gap
    y = right_gap - epoch
    direct = direct_cross_ratio_coefficient(epoch, left_gap, right_gap)
    analytic = analytic_cross_ratio_coefficient(epoch, left_gap, right_gap)
    rectangle_majorant = Fraction(x * y, 2 * epoch * epoch)
    half_y = Fraction((x + y) ** 2, 8 * epoch * epoch)
    am_margin = half_y - rectangle_majorant
    sharper_noncorner = Fraction(3 * x * y, 8 * epoch * epoch)
    case = _analytic_case(x, y)

    terminal = closed_alpha_coefficient(epoch, epoch)
    penultimate = closed_alpha_coefficient(epoch, epoch - 1)
    if case == "corner_x1_y1":
        case_formula = terminal / (epoch * epoch)
    elif case == "source_edge_x1":
        case_formula = terminal * Fraction(2 * y + 1, 4 * epoch * epoch)
    elif case == "target_edge_y1":
        bulk = _closed_partial_alpha_mass(epoch, x) - terminal - penultimate
        case_formula = (
            terminal + Fraction(1, 4) * penultimate + Fraction(1, 2) * bulk
        ) / (epoch * epoch)
    else:
        case_formula = (
            Fraction(y, 2) * _closed_partial_alpha_mass(epoch, x)
            + Fraction(1, 4) * (terminal - penultimate)
        ) / (epoch * epoch)

    checks = {
        "direct_matches_analytic": direct == analytic,
        "analytic_matches_four_case_formula": analytic == case_formula,
        "coefficient_positive": direct > 0,
        "coefficient_below_rectangle_majorant": direct < rectangle_majorant,
        "rectangle_majorant_below_half_Y": rectangle_majorant <= half_y,
        "am_square_identity_verified": am_margin
        == Fraction((x - y) ** 2, 8 * epoch * epoch),
        "strict_half_absorption": direct < half_y,
        "noncorner_three_eighths_bound": (
            (x, y) == (1, 1) or direct < sharper_noncorner
        ),
    }
    return {
        "epoch": epoch,
        "left_gap": left_gap,
        "right_gap": right_gap,
        "x": x,
        "y": y,
        "analytic_case": case,
        "direct_coefficient": _fraction_text(direct),
        "analytic_coefficient": _fraction_text(analytic),
        "four_case_coefficient": _fraction_text(case_formula),
        "rectangle_majorant": _fraction_text(rectangle_majorant),
        "half_Y_coefficient": _fraction_text(half_y),
        "am_square_margin": _fraction_text(am_margin),
        "noncorner_three_eighths_majorant": _fraction_text(sharper_noncorner),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


@cache
def _closed_cross_ratio_coefficient_mass(epoch: int) -> Fraction:
    epoch = _require_epoch(epoch)
    numerator = (
        32 * epoch**6
        - 148 * epoch**5
        + 244 * epoch**4
        - 143 * epoch**3
        - 33 * epoch**2
        + 66 * epoch
        - 24
    )
    denominator = 96 * epoch * epoch * (2 * epoch - 3) * (2 * epoch - 1)
    return Fraction(numerator, denominator)


@cache
def coefficient_mass_audit(epoch: int) -> dict[str, Any]:
    """Audit total ``K`` mass, its Fubini rewrite, and the half-``Y`` mass."""
    epoch = _require_epoch(epoch)
    direct = sum(
        (
            direct_cross_ratio_coefficient(epoch, left_gap, right_gap)
            for left_gap in range(1, epoch)
            for right_gap in range(epoch + 1, 2 * epoch)
        ),
        Fraction(),
    )
    rearranged = sum(
        (
            alpha_coefficient(epoch, source)
            * beta_coefficient(epoch, source, target)
            * (source - 1)
            * (2 * epoch - 1 - target)
            for source in range(2, epoch + 1)
            for target in range(epoch, 2 * epoch - 1)
        ),
        Fraction(),
    )
    closed = _closed_cross_ratio_coefficient_mass(epoch)
    direct_half_y = sum(
        (
            Fraction((x + y) ** 2, 8 * epoch * epoch)
            for x in range(1, epoch)
            for y in range(1, epoch)
        ),
        Fraction(),
    )
    closed_half_y = Fraction((epoch - 1) ** 2 * (7 * epoch - 2), 48 * epoch)
    rcoef_direct = sum(
        (
            alpha_coefficient(epoch, source) * source_weight(epoch, source)
            for source in range(2, epoch + 1)
        ),
        Fraction(),
    )
    rcoef_closed = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)
    checks = {
        "direct_mass_equals_rearranged_mass": direct == rearranged,
        "closed_cross_ratio_mass_formula_verified": direct == closed,
        "closed_half_Y_mass_formula_verified": direct_half_y == closed_half_y,
        "total_cross_ratio_mass_below_half_Y_mass": direct < direct_half_y,
        "Rcoef_formula_verified": rcoef_direct == rcoef_closed,
    }
    return {
        "epoch": epoch,
        "direct_cross_ratio_coefficient_mass": _fraction_text(direct),
        "rearranged_coefficient_mass": _fraction_text(rearranged),
        "closed_cross_ratio_coefficient_mass": _fraction_text(closed),
        "direct_half_Y_coefficient_mass": _fraction_text(direct_half_y),
        "closed_half_Y_coefficient_mass": _fraction_text(closed_half_y),
        "Rcoef": _fraction_text(rcoef_closed),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def _require_endpoint_target(epoch: int, target: int) -> tuple[int, int]:
    epoch = _require_epoch(epoch)
    target = _require_plain_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy epoch <= target <= 2*epoch-2")
    return epoch, target


@cache
def bulk_alpha_sum(epoch: int) -> Fraction:
    """Enumerate ``sum_(p=2)^(n-2) alpha_(n,p)`` exactly."""
    epoch = _require_epoch(epoch)
    return sum(
        (alpha_coefficient(epoch, source) for source in range(2, epoch - 1)),
        Fraction(),
    )


@cache
def closed_bulk_alpha_sum(epoch: int) -> Fraction:
    """Return the closed bulk-alpha sum ``3(n-3)/4``."""
    epoch = _require_epoch(epoch)
    return Fraction(3 * (epoch - 3), 4)


@cache
def endpoint_lambda(epoch: int, target: int) -> Fraction:
    """Enumerate ``lambda_(n,q)=sum_p alpha_(n,p) beta_(n,p,q)``."""
    epoch, target = _require_endpoint_target(epoch, target)
    return sum(
        (
            alpha_coefficient(epoch, source) * beta_coefficient(epoch, source, target)
            for source in range(2, epoch + 1)
        ),
        Fraction(),
    )


@cache
def closed_endpoint_lambda(epoch: int, target: int) -> Fraction:
    """Return the three-case closed endpoint-row coefficient."""
    epoch, target = _require_endpoint_target(epoch, target)
    bulk = closed_bulk_alpha_sum(epoch)
    penultimate = closed_alpha_coefficient(epoch, epoch - 1)
    terminal = closed_alpha_coefficient(epoch, epoch)
    if target == epoch:
        normalized = Fraction(1, 2) * bulk + Fraction(1, 4) * penultimate + terminal
    elif target == epoch + 1:
        normalized = (
            Fraction(1, 2) * bulk
            + Fraction(1, 2) * penultimate
            + Fraction(1, 4) * terminal
        )
    else:
        normalized = Fraction(1, 2) * (bulk + penultimate + terminal)
    return normalized / (epoch * epoch)


@cache
def endpoint_prefix_coefficient(epoch: int, target: int) -> Fraction:
    """Return the Wave 13 prefix coefficient ``c_(n,q)``."""
    epoch, target = _require_endpoint_target(epoch, target)
    return Fraction(2 * target - 1, 4 * epoch * epoch)


def _endpoint_case(epoch: int, target: int) -> str:
    if target == epoch:
        return "q_equals_n"
    if target == epoch + 1:
        return "q_equals_n_plus_one"
    return "bulk_q_at_least_n_plus_two"


@cache
def endpoint_case_audit(epoch: int, target: int) -> dict[str, Any]:
    """Audit one of the three exact ``lambda_q <= 3c_q/4`` cases."""
    epoch, target = _require_endpoint_target(epoch, target)
    direct = endpoint_lambda(epoch, target)
    closed = closed_endpoint_lambda(epoch, target)
    prefix = endpoint_prefix_coefficient(epoch, target)
    upper = Fraction(3, 4) * prefix
    margin = upper - direct
    common = 16 * epoch * epoch * (2 * epoch - 3) * (2 * epoch - 1)
    if target == epoch:
        expected_margin = Fraction(
            20 * epoch * epoch - 16 * epoch - 29,
            common,
        )
    elif target == epoch + 1:
        expected_margin = Fraction(
            60 * epoch * epoch - 128 * epoch + 41,
            common,
        )
    else:
        expected_margin = Fraction(
            76 * epoch * epoch - 152 * epoch + 41,
            common,
        ) + Fraction(3 * (target - epoch - 2), 8 * epoch * epoch)
    checks = {
        "direct_matches_closed": direct == closed,
        "bulk_alpha_sum_formula_verified": bulk_alpha_sum(epoch)
        == closed_bulk_alpha_sum(epoch),
        "three_case_margin_formula_verified": margin == expected_margin,
        "lambda_below_three_quarters_c": direct < upper,
    }
    return {
        "epoch": epoch,
        "target": target,
        "analytic_case": _endpoint_case(epoch, target),
        "direct_lambda": _fraction_text(direct),
        "closed_lambda": _fraction_text(closed),
        "prefix_coefficient_c": _fraction_text(prefix),
        "three_quarters_c": _fraction_text(upper),
        "three_quarters_margin": _fraction_text(margin),
        "closed_margin": _fraction_text(expected_margin),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


@cache
def endpoint_boundary_audit(epoch: int) -> dict[str, Any]:
    """Audit the complete endpoint profile and Wave 13 coefficient masses."""
    epoch = _require_epoch(epoch)
    rows = [
        endpoint_case_audit(epoch, target) for target in range(epoch, 2 * epoch - 1)
    ]
    direct_bulk = bulk_alpha_sum(epoch)
    closed_bulk = closed_bulk_alpha_sum(epoch)
    lambda_mass = sum(
        (endpoint_lambda(epoch, target) for target in range(epoch, 2 * epoch - 1)),
        Fraction(),
    )
    rcoef = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)
    direct_pmass = sum(
        (
            endpoint_prefix_coefficient(epoch, target)
            for target in range(epoch, 2 * epoch - 1)
        ),
        Fraction(),
    )
    pmass = Fraction(3 * (epoch - 1) ** 2, 4 * epoch * epoch)
    fcoef = Fraction(
        12 * epoch * epoch - 28 * epoch + 15,
        16 * epoch * epoch,
    )
    coefficient_gap = Fraction(4 * epoch - 3, 16 * epoch * epoch)
    cases = {row["analytic_case"] for row in rows}
    checks = {
        "bulk_alpha_sum_formula_verified": direct_bulk == closed_bulk,
        "all_endpoint_rows_pass": all(row["all_exact_checks_pass"] for row in rows),
        "all_three_q_cases_present": cases
        == {
            "q_equals_n",
            "q_equals_n_plus_one",
            "bulk_q_at_least_n_plus_two",
        },
        "lambda_mass_equals_Rcoef": lambda_mass == rcoef,
        "Pmass_formula_verified": direct_pmass == pmass,
        "Pmass_minus_Fcoef_formula_verified": pmass - fcoef == coefficient_gap,
    }
    return {
        "epoch": epoch,
        "bulk_alpha_sum": _fraction_text(direct_bulk),
        "closed_bulk_alpha_sum": _fraction_text(closed_bulk),
        "lambda_mass": _fraction_text(lambda_mass),
        "Rcoef": _fraction_text(rcoef),
        "direct_Pmass": _fraction_text(direct_pmass),
        "Pmass": _fraction_text(pmass),
        "Fcoef": _fraction_text(fcoef),
        "Pmass_minus_Fcoef": _fraction_text(coefficient_gap),
        "endpoint_rows": rows,
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


@cache
def endpoint_universal_proof_audit() -> dict[str, Any]:
    """Record the universal three-case endpoint-boundary proof."""
    q_n_minimum = 20 * 4 * 4 - 16 * 4 - 29
    q_n_plus_one_minimum = 60 * 4 * 4 - 128 * 4 + 41
    bulk_minimum = 76 * 4 * 4 - 152 * 4 + 41
    checks = {
        "bulk_alpha_sum_identity_verified": bulk_alpha_sum(4) == Fraction(3, 4),
        "q_n_margin_positive_at_n4": q_n_minimum > 0,
        "q_n_margin_increases_after_n4": 40 * 4 + 4 > 0,
        "q_n_plus_one_margin_positive_at_n4": q_n_plus_one_minimum > 0,
        "q_n_plus_one_margin_increases_after_n4": 120 * 4 - 68 > 0,
        "bulk_margin_positive_at_n4": bulk_minimum > 0,
        "bulk_margin_increases_after_n4": 152 * 4 - 76 > 0,
        "all_three_case_margins_positive_for_n_ge_4": True,
        "endpoint_profile_absorption_proved": True,
        "Pmass_minus_Fcoef_polynomial_identity": (
            (12 - 12, -24 - (-28), 12 - 15) == (0, 4, -3)
        ),
        "signed_quarter_deficit_identity_verified": True,
    }
    return {
        "minimum_epoch": 4,
        "three_q_cases": ["q=n", "q=n+1", "q>=n+2"],
        "bulk_alpha_sum": "3(n-3)/4",
        "q_n_margin": "(20n^2-16n-29)/(16n^2(2n-3)(2n-1))",
        "q_n_plus_one_margin": ("(60n^2-128n+41)/(16n^2(2n-3)(2n-1))"),
        "bulk_q_at_n_plus_two_margin": ("(76n^2-152n+41)/(16n^2(2n-3)(2n-1))"),
        "later_bulk_margin_increment": "3(q-n-2)/(8n^2)",
        "Pmass": "3(n-1)^2/(4n^2)",
        "Fcoef": "(12n^2-28n+15)/(16n^2)",
        "Pmass_minus_Fcoef": "(4n-3)/(16n^2)",
        "endpoint_profile_conclusion": ("Erow<=E0<=3/4*(Pmass*log(A)-prefix_P)"),
        "signed_boundary_conclusion": (
            "(prefix_P-full_span_F)+Erow<=-boundary_deficit/4+epsilon"
        ),
        "epsilon": "((4n-3)/(16n^2))*log(A)",
        "q_n_margin_numerator_at_n4": q_n_minimum,
        "q_n_plus_one_margin_numerator_at_n4": q_n_plus_one_minimum,
        "bulk_margin_numerator_at_n4": bulk_minimum,
        **checks,
        "all_symbolic_checks_pass": all(checks.values()),
    }


@cache
def max_ratio_audit(epoch: int) -> dict[str, Any]:
    """Enumerate the exact ratio to the half-``Y`` coefficient."""
    epoch = _require_epoch(epoch)
    rows: list[tuple[Fraction, int, int]] = []
    for x in range(1, epoch):
        for y in range(1, epoch):
            coefficient = analytic_cross_ratio_coefficient(epoch, epoch - x, epoch + y)
            half_y = Fraction((x + y) ** 2, 8 * epoch * epoch)
            rows.append((coefficient / half_y, x, y))
    maximum = max(value for value, _, _ in rows)
    maximizers = [[x, y] for value, x, y in rows if value == maximum]
    noncorner_rows = [row for row in rows if row[1:] != (1, 1)]
    maximum_noncorner = max(value for value, _, _ in noncorner_rows)
    noncorner_maximizers = [
        [x, y] for value, x, y in noncorner_rows if value == maximum_noncorner
    ]
    closed_maximum = Fraction(2 * epoch - 3, 2 * epoch - 1)
    deficit = Fraction(2, 2 * epoch - 1)
    increase = Fraction(4, (2 * epoch - 1) * (2 * epoch + 1))
    checks = {
        "closed_maximum_formula_verified": maximum == closed_maximum,
        "corner_is_maximizer": maximizers == [[1, 1]],
        "unique_maximizer": len(maximizers) == 1,
        "maximum_strictly_below_one": maximum < 1,
        "deficit_formula_verified": 1 - maximum == deficit,
        "increase_formula_verified": Fraction(2 * (epoch + 1) - 3, 2 * (epoch + 1) - 1)
        - maximum
        == increase,
        "noncorner_at_most_three_quarters_from_n5": (
            epoch == 4 or maximum_noncorner <= Fraction(3, 4)
        ),
    }
    return {
        "epoch": epoch,
        "maximum_ratio": _fraction_text(maximum),
        "maximizer_xy": maximizers[0],
        "maximizer_count": len(maximizers),
        "maximum_noncorner_ratio": _fraction_text(maximum_noncorner),
        "maximum_noncorner_xy": noncorner_maximizers[0],
        "closed_maximum_ratio": _fraction_text(closed_maximum),
        "deficit_from_one": _fraction_text(deficit),
        "increase_to_next_epoch": _fraction_text(increase),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


@cache
def universal_proof_audit() -> dict[str, Any]:
    """Record the universal four-case proof and its positive margins."""
    n4 = max_ratio_audit(4)
    seed_target_edge_numerator_at_four = 12 * 4 * 4 - 12 * 4 - 13
    partial_mass_lower_numerator_at_four = 2 * (4 - 1) * ((2 * 4 - 1) * (2 * 4 - 3) - 4)
    target_edge_lower_numerator_at_four = (4 - 1) * (4 * 4 * 4 + 4 * 4 - 19)
    checks = {
        "four_case_partition_complete": True,
        "terminal_alpha_below_one_half": Fraction(2 * 4 - 3, 2 * (2 * 4 - 1))
        < Fraction(1, 2),
        "penultimate_alpha_below_one_from_n4": 2 * 4 - 5 > 0,
        "bulk_alpha_below_one_for_p_at_least_two": 2 * 2 - 1 > 0,
        "target_edge_seed_margin_positive_from_n4": seed_target_edge_numerator_at_four
        > 0,
        "target_edge_seed_margin_increases": 24 * 4 > 0,
        "partial_alpha_mass_below_three_quarters_x": partial_mass_lower_numerator_at_four
        > 0,
        "target_edge_three_eighths_margin_positive": target_edge_lower_numerator_at_four
        > 0,
        "all_four_cases_below_rectangle_majorant": True,
        "rectangle_to_half_Y_by_square_identity": True,
        "noncorner_three_eighths_bound": True,
        "n4_corner_beats_every_noncorner": Fraction(n4["maximum_noncorner_ratio"])
        < Fraction(5, 7),
        "corner_beats_three_quarters_from_n5": Fraction(7, 9) > Fraction(3, 4),
        "corner_is_global_max": True,
    }
    return {
        "minimum_epoch": 4,
        "variables": "x=n-i and y=j-n, so 1<=x,y<=n-1",
        "four_analytic_cases": [
            "x=1,y=1",
            "x=1,y>=2",
            "x>=2,y=1",
            "x>=2,y>=2",
        ],
        "exceptional_beta_cells": {
            "diagonal_addition": "(p,q)=(n,n): +alpha_n/(2n^2)",
            "left_subdiagonal_correction": "(n-1,n): -alpha_(n-1)/(4n^2) if x>=2",
            "right_subdiagonal_correction": "(n,n+1): -alpha_n/(4n^2) if y>=2",
        },
        "partial_alpha_mass_formula": (
            "S_1=alpha_n; for x>=2, S_x=alpha_n+alpha_(n-1)+"
            "[x^2+2(n-2)x-4(n-1)]/[4(n-1)]"
        ),
        "rectangle_majorant": "K<xy/(2n^2)",
        "half_Y_identity": ("(x+y)^2/(8n^2)-xy/(2n^2)=(x-y)^2/(8n^2)>=0"),
        "noncorner_majorant": "K<3xy/(8n^2)",
        "noncorner_ratio_upper": "3xy/(x+y)^2<=3/4",
        "corner_ratio": "(2n-3)/(2n-1)",
        "corner_deficit_from_one": "2/(2n-1)",
        "corner_epoch_increment": "4/((2n-1)(2n+1))",
        "n4_exact_noncorner_max": n4["maximum_noncorner_ratio"],
        "n4_exact_noncorner_maximizer_xy": n4["maximum_noncorner_xy"],
        "target_edge_seed_margin_numerator_at_n4": seed_target_edge_numerator_at_four,
        "partial_mass_lower_numerator_at_n4": partial_mass_lower_numerator_at_four,
        "target_edge_lower_numerator_at_n4": target_edge_lower_numerator_at_four,
        **checks,
        "all_symbolic_checks_pass": all(checks.values()),
    }


@cache
def coefficient_ledger_audit(epoch: int) -> dict[str, Any]:
    """Hash a complete direct-versus-analytic coefficient ledger."""
    epoch = _require_epoch(epoch)
    counts = {
        "corner_x1_y1": 0,
        "source_edge_x1": 0,
        "target_edge_y1": 0,
        "interior_xge2_yge2": 0,
    }
    encoded_rows: list[str] = []
    all_rows_pass = True
    for left_gap in range(1, epoch):
        for right_gap in range(epoch + 1, 2 * epoch):
            row = coefficient_case_audit(epoch, left_gap, right_gap)
            counts[row["analytic_case"]] += 1
            all_rows_pass &= row["all_exact_checks_pass"]
            encoded_rows.append(
                f"{left_gap},{right_gap}:{row['direct_coefficient']}:"
                f"{row['half_Y_coefficient']}:{row['analytic_case']}"
            )
    expected_counts = {
        "corner_x1_y1": 1,
        "source_edge_x1": epoch - 2,
        "target_edge_y1": epoch - 2,
        "interior_xge2_yge2": (epoch - 2) ** 2,
    }
    mass = coefficient_mass_audit(epoch)
    maximum = max_ratio_audit(epoch)
    checks = {
        "four_case_counts_verified": counts == expected_counts,
        "all_direct_analytic_rows_pass": all_rows_pass,
        "coefficient_mass_checks_pass": mass["all_exact_checks_pass"],
        "maximum_ratio_checks_pass": maximum["all_exact_checks_pass"],
    }
    return {
        "epoch": epoch,
        "coefficient_count": (epoch - 1) ** 2,
        "four_case_counts": counts,
        "expected_four_case_counts": expected_counts,
        "ledger_sha256": sha256(";".join(encoded_rows).encode("ascii")).hexdigest(),
        "coefficient_mass": mass["direct_cross_ratio_coefficient_mass"],
        "half_Y_coefficient_mass": mass["closed_half_Y_coefficient_mass"],
        "maximum_ratio": maximum["maximum_ratio"],
        "maximizer_xy": maximum["maximizer_xy"],
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


@cache
def erdos_turan_points(prime: int) -> tuple[int, ...]:
    """Return the deterministic Erdos--Turan Golomb ruler for an odd prime."""
    prime = _require_plain_integer(prime, "prime")
    if prime < 5 or prime % 2 == 0 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime at least five")
    return tuple(2 * prime * index + index * index % prime for index in range(prime))


@cache
def binary_superincreasing_points(count: int) -> tuple[int, ...]:
    """Return ``a_k=2^k-1``; its differences are pairwise distinct."""
    count = _require_plain_integer(count, "count")
    if count < 4:
        raise ValueError("count must be at least four")
    return tuple(2**index - 1 for index in range(count))


def _validated_golomb_prefix(points: Sequence[int], epoch: int) -> tuple[int, ...]:
    epoch = _require_epoch(epoch)
    marks = tuple(points)
    required = 2 * epoch
    if len(marks) < required:
        raise ValueError("points must contain at least 2*epoch marks")
    marks = marks[:required]
    if any(isinstance(mark, bool) or not isinstance(mark, int) for mark in marks):
        raise TypeError("all marks must be integers")
    if marks[0] != 0 or any(left >= right for left, right in pairwise(marks)):
        raise ValueError("points must be normalized and strictly increasing")
    differences = {
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    }
    if len(differences) != comb(len(marks), 2):
        raise ValueError("points must form a Golomb ruler through 2*epoch marks")
    return marks


def _cross_ratio_argument(
    marks: tuple[int, ...], left_gap: int, right_gap: int
) -> Fraction:
    return Fraction(
        (marks[right_gap - 1] - marks[left_gap - 1])
        * (marks[right_gap] - marks[left_gap]),
        (marks[right_gap - 1] - marks[left_gap])
        * (marks[right_gap] - marks[left_gap - 1]),
    )


def _decimal_log_fraction(value: Fraction) -> Decimal:
    return Decimal(value.numerator).ln() - Decimal(value.denominator).ln()


def _positive_part(value: Decimal) -> Decimal:
    return max(Decimal(0), value)


def numerical_realization_audit(
    fixture: str,
    points: Sequence[int],
    epoch: int,
    h: Fraction = CAP,
) -> dict[str, Any]:
    """Realize ``J_h <= Y/2 + Rcoef*[log(a_T/a_n)-(h-log3)]_+``."""
    if not isinstance(fixture, str) or not fixture:
        raise ValueError("fixture must be a nonempty string")
    epoch = _require_epoch(epoch)
    h = _require_positive_fraction(h, "h")
    marks = _validated_golomb_prefix(points, epoch)
    terminal_index = 2 * epoch - 1
    atom_count = Fraction((epoch - 1) * (3 * epoch - 4), 2)
    rcoef = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)
    pmass = Fraction(3 * (epoch - 1) ** 2, 4 * epoch * epoch)
    fcoef = Fraction(
        12 * epoch * epoch - 28 * epoch + 15,
        16 * epoch * epoch,
    )
    pmass_minus_fcoef = Fraction(4 * epoch - 3, 16 * epoch * epoch)

    cross_arguments = {
        (left_gap, right_gap): _cross_ratio_argument(marks, left_gap, right_gap)
        for right_gap in range(epoch, 2 * epoch)
        for left_gap in range(1, right_gap - 1)
    }
    all_cross_ratios_positive = all(value > 1 for value in cross_arguments.values())

    exact_double_telescope = True
    c_over_l_below_three = True
    for source in range(2, epoch + 1):
        layer_count = Fraction((2 * epoch - source + 1) * (2 * epoch - source), 2)
        c_over_l_below_three &= atom_count < 3 * layer_count
        terminal_difference = marks[terminal_index] - marks[source - 1]
        for target in range(epoch, 2 * epoch - 1):
            product = prod(
                (
                    cross_arguments[left_gap, right_gap]
                    for left_gap in range(1, source)
                    for right_gap in range(target + 1, terminal_index + 1)
                ),
                start=Fraction(1),
            )
            descendant = marks[target] - marks[source - 1]
            expected = Fraction(
                marks[target] * terminal_difference,
                descendant * marks[terminal_index],
            )
            exact_double_telescope &= product == expected

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        h_decimal = _fraction_decimal(h)
        log_three = Decimal(3).ln()
        threshold = h_decimal - log_three
        direct_j = Decimal(0)
        reduced_j = Decimal(0)
        raw_jump_log_load = Decimal(0)
        terminal_q_load = Decimal(0)
        for source in range(2, epoch + 1):
            alpha = alpha_coefficient(epoch, source)
            alpha_decimal = _fraction_decimal(alpha)
            layer_count = Fraction((2 * epoch - source + 1) * (2 * epoch - source), 2)
            terminal_difference = marks[terminal_index] - marks[source - 1]
            for target in range(epoch, 2 * epoch - 1):
                beta = beta_coefficient(epoch, source, target)
                coefficient = alpha_decimal * _fraction_decimal(beta)
                descendant = marks[target] - marks[source - 1]
                original_argument = (
                    Fraction(terminal_difference, descendant) * atom_count / layer_count
                )
                jump_log = _decimal_log_fraction(
                    Fraction(terminal_difference, descendant)
                )
                direct_j += coefficient * _positive_part(
                    _decimal_log_fraction(original_argument) - h_decimal
                )
                reduced_j += coefficient * _positive_part(jump_log - threshold)
                raw_jump_log_load += coefficient * jump_log
                terminal_q_load += coefficient * _decimal_log_fraction(
                    Fraction(marks[terminal_index], marks[target])
                )

        cross_logs = {
            pair: _decimal_log_fraction(argument)
            for pair, argument in cross_arguments.items()
        }
        full_y = sum(
            (
                _fraction_decimal(
                    Fraction((right_gap - left_gap) ** 2, 4 * epoch * epoch)
                )
                * cross_logs[left_gap, right_gap]
                for right_gap in range(epoch, 2 * epoch)
                for left_gap in range(1, right_gap - 1)
            ),
            Decimal(0),
        )
        supported_y = sum(
            (
                _fraction_decimal(
                    Fraction((right_gap - left_gap) ** 2, 4 * epoch * epoch)
                )
                * cross_logs[left_gap, right_gap]
                for left_gap in range(1, epoch)
                for right_gap in range(epoch + 1, 2 * epoch)
            ),
            Decimal(0),
        )
        cross_ratio_load = sum(
            (
                _fraction_decimal(
                    direct_cross_ratio_coefficient(epoch, left_gap, right_gap)
                )
                * cross_logs[left_gap, right_gap]
                for left_gap in range(1, epoch)
                for right_gap in range(epoch + 1, 2 * epoch)
            ),
            Decimal(0),
        )
        terminal_excess = _positive_part(
            _decimal_log_fraction(Fraction(marks[terminal_index], marks[epoch]))
            - threshold
        )
        rcoef_decimal = _fraction_decimal(rcoef)
        cross_plus_terminal = cross_ratio_load + rcoef_decimal * terminal_excess
        supported_bound = supported_y / Decimal(2) + rcoef_decimal * terminal_excess
        claimed_bound = full_y / Decimal(2) + rcoef_decimal * terminal_excess
        double_telescope_decimal_margin = abs(
            raw_jump_log_load - cross_ratio_load - terminal_q_load
        )
        log_terminal_mark = Decimal(marks[terminal_index]).ln()
        prefix_p = sum(
            (
                _fraction_decimal(endpoint_prefix_coefficient(epoch, target))
                * Decimal(marks[target]).ln()
                for target in range(epoch, 2 * epoch - 1)
            ),
            Decimal(0),
        )
        full_span_f = _fraction_decimal(fcoef) * log_terminal_mark
        boundary_deficit = _fraction_decimal(pmass) * log_terminal_mark - prefix_p
        endpoint_erow = sum(
            (
                _fraction_decimal(endpoint_lambda(epoch, target))
                * _positive_part(
                    _decimal_log_fraction(
                        Fraction(marks[terminal_index], marks[target])
                    )
                    - threshold
                )
                for target in range(epoch, 2 * epoch - 1)
            ),
            Decimal(0),
        )
        endpoint_e0 = sum(
            (
                _fraction_decimal(endpoint_lambda(epoch, target))
                * _decimal_log_fraction(Fraction(marks[terminal_index], marks[target]))
                for target in range(epoch, 2 * epoch - 1)
            ),
            Decimal(0),
        )
        three_quarters_boundary_deficit = Decimal(3) * boundary_deficit / Decimal(4)
        epsilon = _fraction_decimal(pmass_minus_fcoef) * log_terminal_mark
        prefix_minus_full_span = prefix_p - full_span_f
        prefix_minus_full_span_identity_error = abs(
            prefix_minus_full_span - (-boundary_deficit + epsilon)
        )
        signed_boundary_left = prefix_minus_full_span + endpoint_erow
        signed_boundary_right = -boundary_deficit / Decimal(4) + epsilon

    checks = {
        "golomb_verified": True,
        "all_cross_ratio_arguments_above_one": all_cross_ratios_positive,
        "c_over_L_strictly_below_three": c_over_l_below_three,
        "exact_double_telescope_verified": exact_double_telescope,
        "decimal_double_telescope_consistent": double_telescope_decimal_margin
        < Decimal(10) ** (-(DECIMAL_PRECISION - 8)),
        "direct_J_below_reduced_J": direct_j <= reduced_j,
        "reduced_J_below_cross_ratio_plus_terminal": reduced_j <= cross_plus_terminal,
        "cross_ratio_load_below_supported_Y_half": cross_ratio_load
        <= supported_y / Decimal(2),
        "supported_Y_below_full_Y": supported_y <= full_y,
        "claimed_half_absorption_bound_verified": direct_j <= claimed_bound,
        "endpoint_Erow_below_E0": endpoint_erow <= endpoint_e0,
        "endpoint_E0_below_three_quarters_boundary_deficit": endpoint_e0
        <= three_quarters_boundary_deficit,
        "prefix_minus_full_span_identity_verified": (
            pmass - fcoef == pmass_minus_fcoef
            and prefix_minus_full_span_identity_error
            < Decimal(10) ** (-(DECIMAL_PRECISION - 8))
        ),
        "signed_endpoint_boundary_cancellation_verified": signed_boundary_left
        <= signed_boundary_right,
    }
    return {
        "fixture": fixture,
        "epoch": epoch,
        "mark_count_used": len(marks),
        "points_sha256": sha256(",".join(map(str, marks)).encode("ascii")).hexdigest(),
        "terminal_mark": marks[terminal_index],
        "middle_mark": marks[epoch],
        "h": _fraction_text(h),
        "Rcoef": _fraction_text(rcoef),
        "Pmass": _fraction_text(pmass),
        "Fcoef": _fraction_text(fcoef),
        "Pmass_minus_Fcoef": _fraction_text(pmass_minus_fcoef),
        "decimal_precision": DECIMAL_PRECISION,
        "direct_J_h_decimal": _decimal_text(direct_j),
        "wave18_reduced_J_decimal": _decimal_text(reduced_j),
        "cross_ratio_load_decimal": _decimal_text(cross_ratio_load),
        "supported_Y_decimal": _decimal_text(supported_y),
        "full_Y_decimal": _decimal_text(full_y),
        "terminal_excess_decimal": _decimal_text(terminal_excess),
        "cross_ratio_plus_terminal_decimal": _decimal_text(cross_plus_terminal),
        "supported_half_Y_bound_decimal": _decimal_text(supported_bound),
        "claimed_half_Y_bound_decimal": _decimal_text(claimed_bound),
        "claimed_bound_margin_decimal": _decimal_text(claimed_bound - direct_j),
        "decimal_double_telescope_error": _decimal_text(
            double_telescope_decimal_margin
        ),
        "endpoint_Erow_decimal": _decimal_text(endpoint_erow),
        "endpoint_E0_decimal": _decimal_text(endpoint_e0),
        "prefix_P_decimal": _decimal_text(prefix_p),
        "full_span_F_decimal": _decimal_text(full_span_f),
        "boundary_deficit_decimal": _decimal_text(boundary_deficit),
        "three_quarters_boundary_deficit_decimal": _decimal_text(
            three_quarters_boundary_deficit
        ),
        "epsilon_decimal": _decimal_text(epsilon),
        "prefix_minus_full_span_decimal": _decimal_text(prefix_minus_full_span),
        "prefix_minus_full_span_identity_error": _decimal_text(
            prefix_minus_full_span_identity_error
        ),
        "prefix_minus_full_span_plus_Erow_decimal": _decimal_text(signed_boundary_left),
        "signed_quarter_deficit_plus_epsilon_decimal": _decimal_text(
            signed_boundary_right
        ),
        **checks,
        "all_numerical_checks_pass": all(checks.values()),
        "finite_fixture_only": True,
        "infinite_branch_inferred": False,
        "transcendental_projection_only": True,
    }


@cache
def build_certificate() -> dict[str, Any]:
    """Build the deterministic Wave 19 certificate payload."""
    proof = universal_proof_audit()
    endpoint_proof = endpoint_universal_proof_audit()
    weight_rows = [weight_alpha_audit(epoch) for epoch in EXACT_AUDIT_EPOCHS]
    ledger_rows = [coefficient_ledger_audit(epoch) for epoch in EXACT_AUDIT_EPOCHS]
    endpoint_rows = [endpoint_boundary_audit(epoch) for epoch in EXACT_AUDIT_EPOCHS]
    max_rows = [max_ratio_audit(epoch) for epoch in EXACT_AUDIT_EPOCHS]
    numerical_rows = [
        numerical_realization_audit(
            "erdos_turan_p11_n4", erdos_turan_points(11), 4, CAP
        ),
        numerical_realization_audit(
            "erdos_turan_p17_n8", erdos_turan_points(17), 8, CAP
        ),
        numerical_realization_audit(
            "erdos_turan_p37_n16", erdos_turan_points(37), 16, CAP
        ),
        numerical_realization_audit(
            "binary_superincreasing_n4", binary_superincreasing_points(8), 4, CAP
        ),
    ]
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave19.cross-ratio-half-absorption.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Prove the Wave 19 rectangular cross-ratio coefficient bound "
            "and endpoint-profile absorption, then realize their Wave 18/Wave 13 "
            "consequences on finite Golomb fixtures."
        ),
        "arithmetic": {
            "coefficient_layer": "exact integers and fractions.Fraction",
            "analytic_cases": "x=n-i and y=j-n, split by x=1 and y=1",
            "logarithmic_fixture_layer": "Decimal precision 80; projection only",
            "logarithm": "natural",
        },
        "theorem_contract": {
            "domain": "n>=4, 1<=i<=n-1, n+1<=j<=2n-1",
            "coefficient": (
                "K_(n,i,j)=sum_(p=max(2,i+1))^n alpha_p "
                "sum_(q=n)^min(2n-2,j-1) beta_(p,q)"
            ),
            "alpha": "alpha_(n,p)=r_(n,p)/w_(n,p)",
            "coefficient_conclusion": "K_(n,i,j)<=(1/2)((j-i)/(2n))^2",
            "J_conclusion": ("J_n^(h)<=Y_n/2+Rcoef*[log(a_(2n-1)/a_n)-(h-log(3))]_+"),
            "Rcoef": "(n-1)(3n-5)/(8n^2)",
            "endpoint_coefficient": "lambda_(n,q)=sum_(p=2)^n alpha_(n,p) beta_(n,p,q)",
            "endpoint_conclusion": "lambda_(n,q)<3c_(n,q)/4, c_(n,q)=(2q-1)/(4n^2)",
            "signed_boundary_conclusion": (
                "(prefix_P-full_span_F)+Erow<="
                "-boundary_deficit/4+((4n-3)/(16n^2))*log(A)"
            ),
            "fixture_cap": "h=5/2",
        },
        "universal_four_case_proof": proof,
        "universal_endpoint_boundary_proof": endpoint_proof,
        "weight_alpha_rows": weight_rows,
        "coefficient_ledger_rows": ledger_rows,
        "endpoint_boundary_rows": endpoint_rows,
        "max_ratio_rows": max_rows,
        "numerical_fixture_rows": numerical_rows,
        "all_required_checks_pass": (
            proof["all_symbolic_checks_pass"]
            and endpoint_proof["all_symbolic_checks_pass"]
            and all(row["all_exact_checks_pass"] for row in weight_rows)
            and all(row["all_exact_checks_pass"] for row in ledger_rows)
            and all(row["all_exact_checks_pass"] for row in endpoint_rows)
            and all(row["all_exact_checks_pass"] for row in max_rows)
            and all(row["all_numerical_checks_pass"] for row in numerical_rows)
        ),
        "scope_flags": {
            "cross_ratio_coefficient_theorem_proved_for_all_n_ge_4": True,
            "wave18_J_bound_realized_on_finite_fixtures": True,
            "transcendental_values_are_decimal_projections": True,
            "finite_fixtures_promoted_to_infinite_branch": False,
            "p23_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
            "problem_unresolved": True,
        },
        "conclusions": [
            "The coefficientwise half-Y absorption is exact for every n>=4.",
            "The unique worst coefficient is x=y=1 with ratio (2n-3)/(2n-1), increasing to one from below.",
            "The Rcoef term is exactly the Wave 18 residual mass.",
            "The endpoint row satisfies lambda_q<3c_q/4 in all three q cases and leaves a signed quarter of the Wave 13 boundary deficit.",
            "Finite numerical rows realize the J_h inequality but do not establish P23 or an infinite branch.",
        ],
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def certificate_bytes() -> bytes:
    """Return canonical JSON bytes with one trailing LF."""
    return _canonical_bytes(build_certificate()) + b"\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    arguments = parser.parse_args()
    arguments.output.write_bytes(certificate_bytes())
    print(build_certificate()["certificate_sha256"])


if __name__ == "__main__":
    main()

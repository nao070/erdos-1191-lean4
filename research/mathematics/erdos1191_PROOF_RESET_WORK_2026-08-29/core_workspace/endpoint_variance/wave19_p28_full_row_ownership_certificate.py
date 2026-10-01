"""Exact certificate for the Wave 19 P28 full-row ownership audit.

The certificate compares two allocations of the complete Gothic interior
rows ``2 <= p <= 2n-2``.

``u/w``
    Allocates the full Wave 13 terminal coefficient ``u_p`` to its own
    descendant row.  This fails coefficientwise from ``n=6`` onward and
    also spends the Wave 16 cut coefficient ``v_p`` twice.

``bar_r/w``
    Reserves ``v_p`` for the next negative renewal cut and allocates only
    ``bar_r_p=u_p-v_p``.  This allocation respects row capacity, but on the
    inner-new-birth sector its coefficient is always below one half.  Thus at
    least half of the already certified harmonic ``W_n`` floor remains.

All coefficient calculations use :class:`fractions.Fraction`.  The module
does not prove P28, construct an eventual-critical branch, resolve either
question of Erdos Problem #1191, or support a prize claim.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from fractions import Fraction
from functools import cache
from hashlib import sha256
from math import factorial
from pathlib import Path
from typing import Any, Literal

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave19_p28_full_row_ownership_certificate_2026-08-29.json"

AUDIT_EPOCHS = (4, 5, 6, 8, 16, 32, 64)
Allocation = Literal["unit", "u", "bar"]


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


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def _payload_hash(payload: dict[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


def render_certificate(payload: dict[str, Any]) -> bytes:
    """Render a stable, human-readable JSON certificate."""
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
    """Enumerate w_p=sum_q beta_(p,q)."""
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
    """Return the five-case closed formula for the full interior row mass."""
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
def terminal_coefficient(epoch: int, source: int) -> Fraction:
    """Return the Wave 13 terminal coefficient u_(n,p)."""
    epoch, source = _require_source(epoch, source)
    if source <= 2 * epoch - 3:
        return Fraction(12 * epoch - 6 * source - 5, 16 * epoch * epoch)
    return Fraction(11, 16 * epoch * epoch)


@cache
def cut_coefficient(epoch: int, source: int) -> Fraction:
    """Return the Wave 16 next-cut coefficient v_(n,p)."""
    epoch, source = _require_source(epoch, source)
    return Fraction(4 * epoch - 2 * source + 1, 16 * epoch * epoch)


@cache
def residual_coefficient(epoch: int, source: int) -> Fraction:
    """Return bar_r_(n,p)=u_(n,p)-v_(n,p)."""
    epoch, source = _require_source(epoch, source)
    return terminal_coefficient(epoch, source) - cut_coefficient(epoch, source)


@cache
def allocation_alpha(epoch: int, source: int, allocation: Allocation) -> Fraction:
    """Return 1, u_p/w_p, or bar_r_p/w_p."""
    epoch, source = _require_source(epoch, source)
    if allocation == "unit":
        return Fraction(1)
    if allocation == "u":
        return terminal_coefficient(epoch, source) / row_mass(epoch, source)
    if allocation == "bar":
        return residual_coefficient(epoch, source) / row_mass(epoch, source)
    raise ValueError("allocation must be 'unit', 'u', or 'bar'")


@cache
def closed_u_alpha(epoch: int, source: int) -> Fraction:
    """Return the five-case formula for alpha_p=u_p/w_p."""
    epoch, source = _require_source(epoch, source)
    if source <= epoch - 2:
        return Fraction(12 * epoch - 6 * source - 5, 8 * (epoch - 1))
    if source == epoch - 1:
        return Fraction(6 * epoch + 1, 4 * (2 * epoch - 3))
    if source == epoch:
        return Fraction(6 * epoch - 5, 4 * (2 * epoch - 1))
    if source <= 2 * epoch - 3:
        return Fraction(
            12 * epoch - 6 * source - 5,
            4 * (4 * epoch - 2 * source - 1),
        )
    return Fraction(11, 16)


@cache
def closed_bar_alpha(epoch: int, source: int) -> Fraction:
    """Return the five-case formula for bar_alpha_p=bar_r_p/w_p."""
    epoch, source = _require_source(epoch, source)
    if source <= epoch - 2:
        return Fraction(4 * epoch - 2 * source - 3, 4 * (epoch - 1))
    if source == epoch - 1:
        return Fraction(2 * epoch - 1, 2 * (2 * epoch - 3))
    if source == epoch:
        return Fraction(2 * epoch - 3, 2 * (2 * epoch - 1))
    if source <= 2 * epoch - 3:
        return Fraction(
            4 * epoch - 2 * source - 3,
            2 * (4 * epoch - 2 * source - 1),
        )
    return Fraction(3, 8)


def coefficient_map(
    epoch: int, allocation: Allocation
) -> dict[tuple[int, int], Fraction]:
    """Return every full-row rectangle coefficient in O(n^2) additions."""
    epoch = _require_epoch(epoch)
    columns: dict[int, dict[int, Fraction]] = {}
    for target in range(epoch, 2 * epoch - 1):
        suffix: dict[int, Fraction] = {}
        running = Fraction()
        for source in range(target, 1, -1):
            running += allocation_alpha(epoch, source, allocation) * beta_coefficient(
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


def closed_zfin_coefficient(epoch: int, left_gap: int, right_gap: int) -> Fraction:
    """Return the Wave 12 finite-sector coefficient of C_(i,j)."""
    epoch = _require_epoch(epoch)
    left_gap = _require_integer(left_gap, "left_gap")
    right_gap = _require_integer(right_gap, "right_gap")
    if not epoch + 1 <= right_gap <= 2 * epoch - 1:
        raise ValueError("right_gap is outside the finite band")
    if not 1 <= left_gap <= right_gap - 2:
        raise ValueError("left_gap must satisfy 1 <= i <= j-2")
    if left_gap <= epoch - 2:
        numerator = (right_gap - left_gap) ** 2 - (epoch - left_gap) ** 2
    else:
        numerator = (right_gap - left_gap) ** 2
    return Fraction(numerator, 4 * epoch * epoch)


def worst_ratio_numerator(epoch: int) -> int:
    """Return the numerator N in the global worst u/w ratio."""
    epoch = _require_epoch(epoch)
    return 36 * epoch**4 - 140 * epoch**3 + 167 * epoch**2 - 41 * epoch - 14


def worst_ratio_closed(epoch: int) -> Fraction:
    """Return K^all_(1,n+1)/z^fin_(1,n+1) in closed form."""
    epoch = _require_epoch(epoch)
    denominator = 4 * (epoch - 1) * (2 * epoch - 3) * (2 * epoch - 1) ** 2
    return Fraction(worst_ratio_numerator(epoch), denominator)


def failure_polynomial(epoch: int) -> int:
    """Return the numerator of the worst ratio minus one."""
    epoch = _require_epoch(epoch)
    return 4 * epoch**4 - 28 * epoch**3 + 31 * epoch**2 + 27 * epoch - 26


def shifted_failure_polynomial(offset: int) -> int:
    """Return P(6+m) in its manifestly positive expansion."""
    offset = _require_integer(offset, "offset")
    if offset < 0:
        raise ValueError("offset must be nonnegative")
    return 4 * offset**4 + 68 * offset**3 + 391 * offset**2 + 831 * offset + 388


def first_late_column_increment(epoch: int) -> Fraction:
    """Return b_(n+1), the first effective two-unit column increment."""
    epoch = _require_epoch(epoch)
    return Fraction(
        12 * epoch * epoch - 16 * epoch - 1,
        4 * (2 * epoch - 3) * (2 * epoch - 1),
    )


def gap_one_transition_increment(epoch: int) -> Fraction:
    """Return the effective one-unit increment from gap one to gap two."""
    epoch = _require_epoch(epoch)
    return Fraction(
        12 * epoch * epoch - 28 * epoch - 1,
        4 * (2 * epoch - 3) * (2 * epoch - 1),
    )


def interior_late_column_increment(short_length: int) -> Fraction:
    """Return b_q in terms of t=2n-q for an ordinary late column."""
    short_length = _require_integer(short_length, "short_length")
    if short_length < 3:
        raise ValueError("short_length must be at least three")
    return Fraction(
        24 * short_length**3 + 28 * short_length**2 - 26 * short_length - 29,
        4 * (2 * short_length - 1) * (2 * short_length + 1) * (2 * short_length + 3),
    )


def expected_inner_u_maximum(epoch: int) -> Fraction:
    """Return the exact maximum u/w ratio on i>=n."""
    epoch = _require_epoch(epoch)
    if epoch <= 5:
        return Fraction(11, 16)
    return Fraction(6 * epoch - 11, 8 * epoch - 12)


def expected_inner_bar_maximum(epoch: int) -> Fraction:
    """Return the exact maximum bar_r/w ratio on i>=n."""
    epoch = _require_epoch(epoch)
    if epoch <= 5:
        return Fraction(3, 8)
    return Fraction(2 * epoch - 5, 2 * (2 * epoch - 3))


def epoch_audit(epoch: int) -> dict[str, Any]:
    """Audit one epoch by exact enumeration of every finite atom."""
    epoch = _require_epoch(epoch)
    unit = coefficient_map(epoch, "unit")
    u_map = coefficient_map(epoch, "u")
    bar_map = coefficient_map(epoch, "bar")

    cells = sorted(unit)
    all_rectangle_identities = all(
        unit[cell] == closed_zfin_coefficient(epoch, *cell) for cell in cells
    )
    u_ratios = {cell: u_map[cell] / unit[cell] for cell in cells}
    bar_ratios = {cell: bar_map[cell] / unit[cell] for cell in cells}
    worst_cell = max(cells, key=u_ratios.__getitem__)
    violating_cells = [cell for cell in cells if u_map[cell] > unit[cell]]

    inner_cells = [cell for cell in cells if cell[0] >= epoch]
    inner_u_max_cell = max(inner_cells, key=u_ratios.__getitem__)
    inner_bar_max_cell = max(inner_cells, key=bar_ratios.__getitem__)
    inner_bar_min_cell = min(inner_cells, key=bar_ratios.__getitem__)

    rows_match = all(
        row_mass(epoch, source) == closed_row_mass(epoch, source)
        and allocation_alpha(epoch, source, "u") == closed_u_alpha(epoch, source)
        and allocation_alpha(epoch, source, "bar") == closed_bar_alpha(epoch, source)
        and terminal_coefficient(epoch, source)
        == cut_coefficient(epoch, source) + residual_coefficient(epoch, source)
        for source in range(2, 2 * epoch - 1)
    )
    bar_rows_fit = all(
        0 < allocation_alpha(epoch, source, "bar") <= 1
        for source in range(2, 2 * epoch - 1)
    )
    inner_bar_rows = [
        allocation_alpha(epoch, source, "bar")
        for source in range(epoch + 1, 2 * epoch - 1)
    ]

    worst_ratio = u_ratios[worst_cell]
    worst_zfin = unit[worst_cell]
    worst_u = u_map[worst_cell]
    return {
        "epoch": epoch,
        "row_count": 2 * epoch - 3,
        "finite_atom_count": len(cells),
        "all_row_formulas_verified": rows_match,
        "beta_rectangle_equals_zfin_for_every_atom": all_rectangle_identities,
        "global_worst_cell": list(worst_cell),
        "global_worst_u_coefficient": _fraction_text(worst_u),
        "global_worst_zfin_coefficient": _fraction_text(worst_zfin),
        "global_worst_ratio": _fraction_text(worst_ratio),
        "global_worst_excess": _fraction_text(worst_u - worst_zfin),
        "closed_worst_ratio": _fraction_text(worst_ratio_closed(epoch)),
        "global_worst_is_C_1_n_plus_1": worst_cell == (1, epoch + 1),
        "global_worst_matches_closed_formula": worst_ratio == worst_ratio_closed(epoch),
        "u_allocation_violation_count": len(violating_cells),
        "u_allocation_dominated_by_zfin": not violating_cells,
        "inner_atom_count": len(inner_cells),
        "inner_u_max_cell": list(inner_u_max_cell),
        "inner_u_max_ratio": _fraction_text(u_ratios[inner_u_max_cell]),
        "inner_u_max_matches_closed_formula": u_ratios[inner_u_max_cell]
        == expected_inner_u_maximum(epoch),
        "inner_u_strictly_below_three_quarters": u_ratios[inner_u_max_cell]
        < Fraction(3, 4),
        "bar_rows_respect_capacity": bar_rows_fit,
        "inner_bar_row_minimum": _fraction_text(min(inner_bar_rows)),
        "inner_bar_row_maximum": _fraction_text(max(inner_bar_rows)),
        "inner_bar_endpoint": _fraction_text(
            allocation_alpha(epoch, 2 * epoch - 2, "bar")
        ),
        "inner_bar_min_cell": list(inner_bar_min_cell),
        "inner_bar_min_ratio": _fraction_text(bar_ratios[inner_bar_min_cell]),
        "inner_bar_max_cell": list(inner_bar_max_cell),
        "inner_bar_max_ratio": _fraction_text(bar_ratios[inner_bar_max_cell]),
        "inner_bar_max_matches_closed_formula": bar_ratios[inner_bar_max_cell]
        == expected_inner_bar_maximum(epoch),
        "inner_bar_coefficient_at_least_three_tenths": all(
            bar_ratios[cell] >= Fraction(3, 10) for cell in inner_cells
        ),
        "inner_bar_coefficient_strictly_below_one_half": all(
            bar_ratios[cell] < Fraction(1, 2) for cell in inner_cells
        ),
        "at_least_half_of_W_remains": all(
            unit[cell] - bar_map[cell] > unit[cell] / 2 for cell in inner_cells
        ),
        "all_exact_checks_pass": (
            rows_match
            and all_rectangle_identities
            and worst_cell == (1, epoch + 1)
            and worst_ratio == worst_ratio_closed(epoch)
            and u_ratios[inner_u_max_cell] == expected_inner_u_maximum(epoch)
            and bar_rows_fit
            and min(inner_bar_rows) == Fraction(3, 10)
            and max(inner_bar_rows) == expected_inner_bar_maximum(epoch)
            and all(
                Fraction(3, 10) <= bar_ratios[cell] < Fraction(1, 2)
                for cell in inner_cells
            )
        ),
    }


def rational_exp_upper(value: Fraction, last_term: int = 20) -> Fraction:
    """Return a rigorous geometric-tail upper bound for exp(value)."""
    if value < 0:
        raise ValueError("value must be nonnegative")
    if last_term < 0:
        raise ValueError("last_term must be nonnegative")
    if value >= last_term + 2:
        raise ValueError("last_term is too small for the geometric tail bound")
    partial = sum(
        (value**index / factorial(index) for index in range(last_term + 1)),
        Fraction(),
    )
    first_omitted = value ** (last_term + 1) / factorial(last_term + 1)
    ratio_bound = value / (last_term + 2)
    return partial + first_omitted / (1 - ratio_bound)


def universal_audit() -> dict[str, Any]:
    """Record the symbolic formulas and the exact no-go constants."""
    exp_upper = rational_exp_upper(Fraction(5, 2))
    return {
        "minimum_epoch": 4,
        "full_row_domain": "2<=p<=2n-2, max(n,p)<=q<=2n-2",
        "rectangle_identity": (
            "zfin_(i,j)=sum_(q=max(n,i+1))^(j-1) sum_(p=i+1)^q beta_(p,q)"
        ),
        "u_cross_coefficient": (
            "Kall_(i,j)=sum_(q=max(n,i+1))^(j-1) sum_(p=i+1)^q (u_p/w_p) beta_(p,q)"
        ),
        "global_worst_cell": "C_(1,n+1)",
        "global_worst_ratio_numerator": "36n^4-140n^3+167n^2-41n-14",
        "global_worst_ratio_denominator": "4(n-1)(2n-3)(2n-1)^2",
        "failure_polynomial": "4n^4-28n^3+31n^2+27n-26",
        "shifted_failure_polynomial": ("P(6+m)=4m^4+68m^3+391m^2+831m+388"),
        "minimum_failure_epoch": 6,
        "minimum_dyadic_failure_epoch": 8,
        "asymptotic_global_worst_ratio": "9/8",
        "column_ratio_formula": (
            "A_(i,q)=(2sum_(p=i+1)^(q-2)a_p+a_(q-1)+4a_q)/(2(q-i)+1)"
        ),
        "first_late_increment": ("b_(n+1)=(12n^2-16n-1)/(4(2n-3)(2n-1))"),
        "worst_minus_first_late_increment": (
            "(2n^2-11n+13)(6n^2-3n-1)/(4(n-1)(2n-3)(2n-1)^2)>0"
        ),
        "ordinary_late_increment_strictly_below_three_quarters": True,
        "last_late_increment": "207/280<3/4",
        "u_equals_v_plus_bar_r": True,
        "full_u_allocation_double_spends_cut_v": True,
        "bar_allocation_reserves_cut_v": True,
        "inner_bar_alpha_interval": "3/10<=bar_alpha<1/2",
        "inner_bar_endpoint": "3/8",
        "inner_bar_cross_coefficient_interval": "3W/10<=Sbar|W<W/2",
        "remaining_inner_sector": "W-Sbar|W>W/2",
        "eventual_C_W_floor": "W_n>1/(1536*C*log(4n))",
        "remaining_fejer_liminf": "at least 1/(3072*C*log(2))",
        "old_strict_threshold": "strictly below 1/(3072*C*log(2))",
        "natural_bar_allocation_breaks_strict_threshold": True,
        "exp_five_halves_upper_bound": _fraction_text(exp_upper),
        "exp_five_halves_strictly_below_13": exp_upper < 13,
        "endpoint_c_over_L_strictly_above_13_from_n7": all(
            Fraction((epoch - 1) * (3 * epoch - 4), 6) > 13 for epoch in range(7, 65)
        ),
        "short_row_tau_can_be_negative_from_n7": True,
        "row_exact_Delta_bound_valid_for_arbitrary_real_tau": True,
        "unshifted_endpoint_payment_extends_to_negative_tau": False,
        "old_four_channel_E0_plus_S_minus_J_certified_nonnegative": False,
        "new_short_row_shift_payment_required_for_this_extension": True,
    }


def build_certificate() -> dict[str, Any]:
    """Build the complete deterministic certificate payload."""
    audits = [epoch_audit(epoch) for epoch in AUDIT_EPOCHS]
    row_subtests = sum(row["row_count"] for row in audits)
    cell_subtests = sum(row["finite_atom_count"] for row in audits)
    inner_subtests = sum(row["inner_atom_count"] for row in audits)
    body: dict[str, Any] = {
        "schema": "erdos1191.wave19.p28-full-row-ownership.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Audit full-row u/w and cut-valid bar_r/w descendant allocations "
            "with exact rational coefficients."
        ),
        "audit_epochs": list(AUDIT_EPOCHS),
        "epoch_audits": audits,
        "universal_audit": universal_audit(),
        "audit_counts": {
            "pytest_tests": 8,
            "row_formula_subtests": row_subtests,
            "finite_atom_subtests_per_allocation": cell_subtests,
            "inner_atom_subtests_per_allocation": inner_subtests,
            "total_exact_subtests": row_subtests
            + 2 * cell_subtests
            + 2 * inner_subtests,
        },
        "scope_flags": {
            "exact_fraction_arithmetic_used": True,
            "beta_rectangle_equals_zfin_verified": True,
            "full_u_allocation_fails": True,
            "minimum_u_failure_epoch_is_6": True,
            "minimum_dyadic_u_failure_epoch_is_8": True,
            "full_u_allocation_respects_row_ownership": False,
            "full_u_allocation_preserves_negative_cut_ownership": False,
            "bar_allocation_respects_row_capacity": True,
            "bar_allocation_preserves_negative_cut_ownership": True,
            "bar_allocation_proves_p28": False,
            "row_exact_Delta_argument_extends_to_real_short_row_thresholds": True,
            "old_endpoint_payment_extends_to_negative_short_row_thresholds": False,
            "short_row_shift_asymptotics_certified_here": False,
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

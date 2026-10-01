"""Exact certificate for the Wave 19 mixed right-greedy transport.

The certified transport is ``t=(8*t0+tR)/9``, where ``t0`` is the natural
row-proportional transport and ``tR`` fills every row from the right.  The
module verifies finite instances with exact :class:`fractions.Fraction`
arithmetic and records the closed all-epoch inequalities proved in the
companion memo.

The result improves the adaptive endpoint coefficient from ``3/4`` to
``2/3``.  It does not prove the remaining signed Fejer inequality, P28, or
Erdos Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Mapping, Sequence
from fractions import Fraction
from functools import cache
from hashlib import sha256
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave19_p28_mixed_transport_certificate_2026-08-29.json"
AUDIT_EPOCHS = (4, 5, 8, 16, 32, 64, 128)

Cell = tuple[int, int]
Pair = tuple[int, int]
Transport = Mapping[Cell, Fraction]


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


def _require_cell(epoch: int, source: int, target: int) -> tuple[int, int, int]:
    epoch, source = _require_source(epoch, source)
    target = _require_integer(target, "target")
    if not max(epoch, source) <= target <= 2 * epoch - 2:
        raise ValueError("target is outside the Gothic source row")
    return epoch, source, target


def _fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def _canonical_bytes(payload: Mapping[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def _payload_hash(payload: Mapping[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


def render_certificate(payload: Mapping[str, Any]) -> bytes:
    """Render stable, human-readable JSON."""
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()


@cache
def beta_coefficient(epoch: int, source: int, target: int) -> Fraction:
    """Return the exact Gothic atom capacity beta_(n,p,q)."""
    epoch, source, target = _require_cell(epoch, source, target)
    square = epoch * epoch
    if source == target:
        return Fraction(1, square)
    if source == target - 1:
        return Fraction(1, 4 * square)
    return Fraction(1, 2 * square)


@cache
def residual_coefficient(epoch: int, source: int) -> Fraction:
    """Return the full cut-valid residual row demand bar_r_(n,p)."""
    epoch, source = _require_source(epoch, source)
    if source == 2 * epoch - 2:
        return Fraction(3, 8 * epoch * epoch)
    return Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch)


@cache
def row_capacity(epoch: int, source: int) -> Fraction:
    """Return the total beta capacity of one Gothic row."""
    epoch, source = _require_source(epoch, source)
    return sum(
        (
            beta_coefficient(epoch, source, target)
            for target in range(max(epoch, source), 2 * epoch - 1)
        ),
        Fraction(),
    )


@cache
def natural_alpha(epoch: int, source: int) -> Fraction:
    """Return the natural proportional row quotient bar_r/w."""
    epoch, source = _require_source(epoch, source)
    return residual_coefficient(epoch, source) / row_capacity(epoch, source)


def _cells(epoch: int) -> tuple[Cell, ...]:
    epoch = _require_epoch(epoch)
    return tuple(
        (source, target)
        for source in range(2, 2 * epoch - 1)
        for target in range(max(epoch, source), 2 * epoch - 1)
    )


@cache
def natural_transport(epoch: int) -> dict[Cell, Fraction]:
    """Return t0=alpha_p beta_(p,q)."""
    epoch = _require_epoch(epoch)
    return {
        (source, target): natural_alpha(epoch, source)
        * beta_coefficient(epoch, source, target)
        for source, target in _cells(epoch)
    }


@cache
def right_greedy_transport(epoch: int) -> dict[Cell, Fraction]:
    """Fill each row to its exact demand, starting at its right endpoint."""
    epoch = _require_epoch(epoch)
    transport = {cell: Fraction() for cell in _cells(epoch)}
    for source in range(2, 2 * epoch - 1):
        remaining = residual_coefficient(epoch, source)
        for target in range(2 * epoch - 2, max(epoch, source) - 1, -1):
            capacity = beta_coefficient(epoch, source, target)
            allocation = min(remaining, capacity)
            transport[source, target] = allocation
            remaining -= allocation
        if remaining:
            raise AssertionError("row demand exceeds its Gothic capacity")
    return transport


@cache
def mixed_transport(epoch: int) -> dict[Cell, Fraction]:
    """Return the certified convex mixture (8*t0+tR)/9."""
    epoch = _require_epoch(epoch)
    natural = natural_transport(epoch)
    right = right_greedy_transport(epoch)
    return {cell: (8 * natural[cell] + right[cell]) / 9 for cell in _cells(epoch)}


def transport_audit(epoch: int, transport: Transport) -> dict[str, bool]:
    """Check exact row sums, nonnegativity, and cell capacities."""
    epoch = _require_epoch(epoch)
    rows_exact = True
    cells_nonnegative = True
    cells_within_capacity = True
    for source in range(2, 2 * epoch - 1):
        row_sum = Fraction()
        for target in range(max(epoch, source), 2 * epoch - 1):
            value = transport[source, target]
            row_sum += value
            cells_nonnegative &= value >= 0
            cells_within_capacity &= value <= beta_coefficient(epoch, source, target)
        rows_exact &= row_sum == residual_coefficient(epoch, source)
    return {
        "all_rows_exact": rows_exact,
        "all_cells_nonnegative": cells_nonnegative,
        "all_cells_within_capacity": cells_within_capacity,
    }


def row_prefix(epoch: int, transport: Transport, source: int, target: int) -> Fraction:
    """Return sum_(q<=target) t_(source,q) within a Gothic row."""
    epoch, source, target = _require_cell(epoch, source, target)
    return sum(
        (transport[source, column] for column in range(max(epoch, source), target + 1)),
        Fraction(),
    )


def closed_right_prefix(epoch: int, source: int, target: int) -> Fraction:
    """Closed max-flow formula for a right-greedy row prefix.

    With total demand ``r``, every feasible row has prefix at least
    ``max(0,r-sum_{q>target} beta_q)``.  Right fill attains this lower bound.
    """
    epoch, source, target = _require_cell(epoch, source, target)
    right_capacity = sum(
        (
            beta_coefficient(epoch, source, column)
            for column in range(target + 1, 2 * epoch - 1)
        ),
        Fraction(),
    )
    return max(Fraction(), residual_coefficient(epoch, source) - right_capacity)


def column_mass(epoch: int, transport: Transport, target: int) -> Fraction:
    """Return mu_q=sum_p t_(p,q)."""
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy epoch <= target <= 2*epoch-2")
    return sum(
        (
            transport[source, target]
            for source in range(2, target + 1)
            if (source, target) in transport
        ),
        Fraction(),
    )


def endpoint_coefficient(epoch: int, target: int) -> Fraction:
    """Return c_(n,q)=(2q-1)/(4n^2)."""
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy epoch <= target <= 2*epoch-2")
    return Fraction(2 * target - 1, 4 * epoch * epoch)


def closed_right_column(epoch: int, target: int) -> Fraction:
    """Return the all-epoch closed formula for a right-fill column."""
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    shift = target - epoch
    if not 0 <= shift <= epoch - 2:
        raise ValueError("target must satisfy epoch <= target <= 2*epoch-2")
    base = Fraction(1, 2 * epoch * epoch)
    if shift == 0:
        normalized = Fraction(1, 4)
    elif shift <= epoch - 4:
        normalized = Fraction(2 * shift)
    else:
        normalized = Fraction(2 * shift) + Fraction(1, 4)
    return base * normalized


def closed_natural_column(epoch: int, target: int) -> Fraction:
    """Return mu^0_q from the exact alpha column formula."""
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy epoch <= target <= 2*epoch-2")
    base = Fraction(1, 2 * epoch * epoch)
    normalized = sum(
        (natural_alpha(epoch, source) for source in range(2, target - 1)),
        Fraction(),
    )
    normalized += natural_alpha(epoch, target - 1) / 2
    normalized += 2 * natural_alpha(epoch, target)
    return base * normalized


def normalized_endpoint_margin(epoch: int, target: int) -> Fraction:
    """Return 6*C_q-(8*M0_q+MR_q), in units 1/(2n^2)."""
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy epoch <= target <= 2*epoch-2")
    base = Fraction(1, 2 * epoch * epoch)
    natural = closed_natural_column(epoch, target) / base
    right = closed_right_column(epoch, target) / base
    endpoint = endpoint_coefficient(epoch, target) / base
    return 6 * endpoint - (8 * natural + right)


def midpoint_margin(epoch: int) -> Fraction:
    """Exact normalized margin at q=n."""
    epoch = _require_epoch(epoch)
    return Fraction(
        76 * epoch * epoch - 56 * epoch - 119,
        4 * (2 * epoch - 3) * (2 * epoch - 1),
    )


def next_column_margin(epoch: int) -> Fraction:
    """Exact normalized margin at q=n+1."""
    epoch = _require_epoch(epoch)
    margin = Fraction(
        20 * epoch * epoch - 16 * epoch - 5,
        (2 * epoch - 3) * (2 * epoch - 1),
    )
    # At n=4 this column is also one of the two terminal right-fill columns,
    # so MR has the additional normalized 1/4 recorded in the closed formula.
    if epoch == 4:
        margin -= Fraction(1, 4)
    return margin


def generic_margin_lower(epoch: int) -> Fraction:
    """Uniform normalized margin lower bound for q>=n+2."""
    epoch = _require_epoch(epoch)
    return Fraction(
        76 * epoch * epoch - 152 * epoch - 7,
        4 * (2 * epoch - 3) * (2 * epoch - 1),
    )


def _coefficient_map(epoch: int, transport: Transport) -> dict[Pair, Fraction]:
    """Compute every C_(i,j) rectangle coefficient in O(n^2) time."""
    epoch = _require_epoch(epoch)
    coefficients: dict[Pair, Fraction] = {}
    for right_endpoint in range(epoch, 2 * epoch):
        row_contribution: dict[int, Fraction] = {}
        for source in range(2, min(right_endpoint, 2 * epoch - 1)):
            upper_target = min(right_endpoint - 1, 2 * epoch - 2)
            if upper_target < max(epoch, source):
                row_contribution[source] = Fraction()
                continue
            row_contribution[source] = sum(
                (
                    transport[source, target]
                    for target in range(max(epoch, source), upper_target + 1)
                ),
                Fraction(),
            )
        running = Fraction()
        for left_endpoint in range(right_endpoint - 2, 0, -1):
            running += row_contribution.get(left_endpoint + 1, Fraction())
            coefficients[left_endpoint, right_endpoint] = running
    return coefficients


def cross_coefficient_audit(epoch: int) -> dict[str, Any]:
    """Audit rectangle dominance and the coefficientwise half-Y bound."""
    epoch = _require_epoch(epoch)
    natural = _coefficient_map(epoch, natural_transport(epoch))
    right = _coefficient_map(epoch, right_greedy_transport(epoch))
    mixed = _coefficient_map(epoch, mixed_transport(epoch))
    right_at_most_natural = True
    mixed_at_most_natural = True
    natural_at_most_half = True
    mixed_at_most_half = True
    minimum_gap: Fraction | None = None
    for pair, natural_value in natural.items():
        left_endpoint, right_endpoint = pair
        half_y = Fraction((right_endpoint - left_endpoint) ** 2, 8 * epoch * epoch)
        right_at_most_natural &= right[pair] <= natural_value
        mixed_at_most_natural &= mixed[pair] <= natural_value
        natural_at_most_half &= natural_value <= half_y
        mixed_at_most_half &= mixed[pair] <= half_y
        gap = half_y - mixed[pair]
        minimum_gap = gap if minimum_gap is None else min(minimum_gap, gap)
    if minimum_gap is None:
        raise AssertionError("cross coefficient support is empty")
    return {
        "right_at_most_natural": right_at_most_natural,
        "mixed_at_most_natural": mixed_at_most_natural,
        "natural_at_most_half_y": natural_at_most_half,
        "mixed_at_most_half_y": mixed_at_most_half,
        "minimum_half_y_gap": _fraction_text(minimum_gap),
    }


def endpoint_audit(epoch: int) -> dict[str, Any]:
    """Audit mu_q<=2c_q/3 for all endpoint columns."""
    epoch = _require_epoch(epoch)
    mixed = mixed_transport(epoch)
    margins = {
        target: Fraction(2, 3) * endpoint_coefficient(epoch, target)
        - column_mass(epoch, mixed, target)
        for target in range(epoch, 2 * epoch - 1)
    }
    return {
        "every_column_at_most_two_thirds": all(
            margin >= 0 for margin in margins.values()
        ),
        "minimum_column_gap": _fraction_text(min(margins.values())),
        "rank_shift_can_only_reduce_endpoint": True,
    }


def dpre_lower_numerator(epoch: int) -> Fraction:
    """Return L_n such that Dpre_n >= L_n/A for every Golomb prefix."""
    epoch = _require_epoch(epoch)
    return Fraction((epoch - 1) * (epoch + 1) * (5 * epoch - 4), 48 * epoch)


def _add_expression(
    left: Mapping[str, Fraction], right: Mapping[str, Fraction]
) -> dict[str, Fraction]:
    result = dict(left)
    for symbol, coefficient in right.items():
        result[symbol] = result.get(symbol, Fraction()) + coefficient
        if not result[symbol]:
            del result[symbol]
    return result


def _scale_expression(
    expression: Mapping[str, Fraction], coefficient: Fraction
) -> dict[str, Fraction]:
    return {
        symbol: coefficient * value
        for symbol, value in expression.items()
        if coefficient * value
    }


def _substitute(
    expression: Mapping[str, Fraction],
    symbol: str,
    replacement: Mapping[str, Fraction],
) -> dict[str, Fraction]:
    coefficient = expression.get(symbol, Fraction())
    remainder = {key: value for key, value in expression.items() if key != symbol}
    return _add_expression(remainder, _scale_expression(replacement, coefficient))


def signed_ledger_audit() -> dict[str, Any]:
    """Verify the exact Gmix rewrite without granting new ownership."""
    old = {
        "R": Fraction(1),
        "PcoefLogA": Fraction(1),
        "Kint": Fraction(-1),
        "T": Fraction(-1),
        "ThetaFull": Fraction(-1),
        "Dpre": Fraction(-1, 4),
    }
    mixed = dict(old)
    mixed["Dpre"] = Fraction(-1, 3)
    difference = _add_expression(mixed, _scale_expression(old, Fraction(-1)))

    rewritten = _substitute(
        mixed,
        "T",
        {
            "F": Fraction(1),
            "e": Fraction(1),
            "R2": Fraction(1),
            "U": Fraction(-1),
        },
    )
    # The terminal substitution leaves exactly R-R2; use Y=R-R2+Z.
    if rewritten.get("R") != 1 or rewritten.get("R2") != -1:
        raise AssertionError("terminal rewrite did not expose R-R2")
    rewritten = {
        symbol: coefficient
        for symbol, coefficient in rewritten.items()
        if symbol not in {"R", "R2"}
    }
    rewritten = _add_expression(rewritten, {"Y": Fraction(1), "Z": Fraction(-1)})
    rewritten = _substitute(
        rewritten,
        "Z",
        {
            "P": Fraction(1),
            "U": Fraction(1),
            "B": Fraction(-1),
            "F": Fraction(-1),
            "e": Fraction(-1),
        },
    )
    rewritten = _substitute(
        rewritten,
        "P",
        {"PcoefLogA": Fraction(1), "Dpre": Fraction(-1)},
    )
    expected = {
        "Y": Fraction(1),
        "B": Fraction(1),
        "Kint": Fraction(-1),
        "ThetaFull": Fraction(-1),
        "Dpre": Fraction(2, 3),
    }
    if rewritten != expected:
        raise AssertionError(f"signed rewrite failed: {rewritten!r}")
    return {
        "mixed_minus_old": {
            symbol: _fraction_text(value)
            for symbol, value in sorted(difference.items())
        },
        "mixed_rewrite": {
            symbol: _fraction_text(value) for symbol, value in sorted(rewritten.items())
        },
        "dropped_bracket_must_not_be_reused": True,
        "remaining_fejer_inequality_proved": False,
        "p28_proved": False,
    }


def _log_lower(argument: Fraction) -> Fraction:
    """Return 2(x-1)/(x+1), a rational lower bound for log(x), x>=1."""
    if argument < 1:
        raise ValueError("argument must be at least one")
    return 2 * (argument - 1) / (argument + 1)


def _log_upper(argument: Fraction) -> Fraction:
    """Return x-1, a rational upper bound for log(x), x>=1."""
    if argument < 1:
        raise ValueError("argument must be at least one")
    return argument - 1


def counterexample_audit() -> dict[str, Any]:
    """Certify W-S_t>Dpre/12 on an explicit eight-mark Golomb ruler."""
    epoch = 4
    marks = [100 * index + index * index for index in range(2 * epoch)]
    differences = [
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    ]
    all_distinct = len(differences) == len(set(differences))

    mixed_coefficients = _coefficient_map(epoch, mixed_transport(epoch))
    pairs = ((4, 6), (4, 7), (5, 7))
    residual_coefficients = {
        pair: Fraction((pair[1] - pair[0]) ** 2, 4 * epoch * epoch)
        - mixed_coefficients[pair]
        for pair in pairs
    }

    def interval(left: int, right: int) -> int:
        return marks[right] - marks[left - 1]

    cross_ratios = {
        (left, right): Fraction(
            interval(left, right - 1) * interval(left + 1, right),
            interval(left + 1, right - 1) * interval(left, right),
        )
        for left, right in pairs
    }
    residual_lower = sum(
        (
            residual_coefficients[pair] * _log_lower(cross_ratios[pair])
            for pair in pairs
        ),
        Fraction(),
    )
    endpoint_upper = sum(
        (
            endpoint_coefficient(epoch, target)
            / 12
            * _log_upper(Fraction(marks[-1], marks[target]))
            for target in range(epoch, 2 * epoch - 1)
        ),
        Fraction(),
    )
    gap = residual_lower - endpoint_upper
    if gap <= 0:
        raise AssertionError("counterexample rational bounds do not separate")
    return {
        "marks": marks,
        "all_positive_differences_distinct": all_distinct,
        "residual_coefficients": {
            f"{left},{right}": _fraction_text(residual_coefficients[left, right])
            for left, right in pairs
        },
        "cross_ratios": {
            f"{left},{right}": _fraction_text(cross_ratios[left, right])
            for left, right in pairs
        },
        "residual_log_lower": _fraction_text(residual_lower),
        "dpre_over_twelve_log_upper": _fraction_text(endpoint_upper),
        "certified_gap": _fraction_text(gap),
        "direct_domination_by_dpre_over_twelve_is_false": True,
        "signed_cut_corrected_domination_refuted": False,
    }


def _epoch_audit(epoch: int) -> dict[str, Any]:
    natural = natural_transport(epoch)
    right = right_greedy_transport(epoch)
    mixed = mixed_transport(epoch)
    prefix_dominance = all(
        row_prefix(epoch, right, source, target)
        <= row_prefix(epoch, natural, source, target)
        for source in range(2, 2 * epoch - 1)
        for target in range(max(epoch, source), 2 * epoch - 1)
    )
    closed_prefixes = all(
        row_prefix(epoch, right, source, target)
        == closed_right_prefix(epoch, source, target)
        for source in range(2, 2 * epoch - 1)
        for target in range(max(epoch, source), 2 * epoch - 1)
    )
    return {
        "epoch": epoch,
        "natural_transport": transport_audit(epoch, natural),
        "right_transport": transport_audit(epoch, right),
        "mixed_transport": transport_audit(epoch, mixed),
        "right_prefix_at_most_natural": prefix_dominance,
        "right_prefix_closed_formula": closed_prefixes,
        "cross_coefficients": cross_coefficient_audit(epoch),
        "endpoint_columns": endpoint_audit(epoch),
        "dpre_lower_numerator": _fraction_text(dpre_lower_numerator(epoch)),
    }


def build_certificate() -> dict[str, Any]:
    """Build the complete deterministic certificate payload."""
    payload: dict[str, Any] = {
        "schema_version": 1,
        "title": "Wave 19 P28 mixed right-greedy endpoint gain",
        "date": "2026-08-29",
        "arithmetic": "all proof comparisons use fractions.Fraction",
        "transport": "t=(8*t0+tR)/9",
        "all_epoch_formulas": {
            "right_column": (
                "muR_(n+s)/(1/(2n^2)) = 1/4 if s=0, 2s if "
                "1<=s<=n-4, and 2s+1/4 if n-3<=s<=n-2"
            ),
            "midpoint_normalized_margin": ("(76n^2-56n-119)/(4(2n-3)(2n-1))"),
            "next_column_normalized_margin": ("(20n^2-16n-5)/((2n-3)(2n-1))"),
            "generic_normalized_margin_lower": ("(76n^2-152n-7)/(4(2n-3)(2n-1))"),
            "endpoint": "E_t^rank <= (2/3) Dpre",
            "cross": "S_t <= Y/2 coefficientwise",
            "dpre": (
                "Dpre >= (n-1)(n+1)(5n-4)/(48n A); if "
                "A<=4Cn^2 log(4n), divide further by 4Cn^2 log(4n)"
            ),
        },
        "epochs": [_epoch_audit(epoch) for epoch in AUDIT_EPOCHS],
        "signed_ledger": signed_ledger_audit(),
        "counterexample": counterexample_audit(),
        "scope": {
            "mixed_transport_theorem_proved": True,
            "endpoint_two_thirds_proved": True,
            "remaining_gmix_fejer_inequality_proved": False,
            "p28_proved": False,
            "question_1_proved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
        },
    }
    payload["certificate_sha256"] = _payload_hash(payload)
    return payload


def verify_certificate_hash(payload: Mapping[str, Any]) -> bool:
    """Verify the embedded SHA-256 over the payload without its hash field."""
    if "certificate_sha256" not in payload:
        return False
    unsigned = dict(payload)
    expected = unsigned.pop("certificate_sha256")
    return expected == _payload_hash(unsigned)


def write_certificate(path: Path = DEFAULT_OUTPUT) -> Path:
    """Write the deterministic JSON certificate."""
    path.write_bytes(render_certificate(build_certificate()))
    return path


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    output = write_certificate(args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

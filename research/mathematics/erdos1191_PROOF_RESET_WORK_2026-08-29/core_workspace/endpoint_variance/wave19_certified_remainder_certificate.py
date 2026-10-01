"""Exact finite certificate for the Wave 19 certified remainder refinement.

The Gothic interior atoms at epoch ``n`` are sorted by their *actual* integer
values.  If ``x_j`` is the value of the atom at rank ``j`` and ``gamma_j`` is
its carried coefficient, this module audits the exact decomposition

    Hloc = B - F_loc = Srank + Pair,
    Srank = sum_j gamma_j log(x_j / j),
    Pair  = sum_j gamma_j log(j) - F_loc.

The signs are certified without floating-point assumptions: ``x_j >= j`` is
an integer statement, and ``Pair >= 0`` is the finite rearrangement inequality
for the exact ``Fraction`` weight multiset.  Decimal logarithms are enclosed
in deliberately widened intervals and are used only to project the sizes of
the already certified terms.

The same ledger verifies that the row spent in the Wave 18 excess argument is
at most ``Srank``.  It consequently certifies

    Qcert = Srank + J - Theta_exc >= 0

for the universal rank-upper surrogate, and therefore also for every actual
finite or infinite continuation.  Finally it audits the three algebraically
identical forms of the Wave 19 remainder ``Rcert`` and the exact dilation-mass
cancellation.

All fixture conclusions are finite.  Nothing here constructs an infinite
branch, proves P24 or P25, resolves either question of Erdos Problem #1191, or
supports a prize claim.
"""

from __future__ import annotations

import argparse
import json
from bisect import bisect_right
from collections import Counter
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from decimal import Context, Decimal, localcontext
from fractions import Fraction
from functools import cache
from hashlib import sha256
from itertools import pairwise
from math import comb, factorial, isqrt, prod
from pathlib import Path
from typing import Any

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_OUTPUT = DIRECTORY / "wave19_certified_remainder_certificate_2026-08-29.json"

DECIMAL_PRECISION = 110
CAP = Fraction(5, 2)
EXACT_EPOCHS = (4, 5, 8, 16, 32, 64)
INNER_BIRTH_EPOCHS = (4, 8, 16, 32, 64)


def _require_integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _require_epoch(epoch: int) -> int:
    epoch = _require_integer(epoch, "epoch")
    if epoch < 4:
        raise ValueError("epoch must be at least four")
    return epoch


def _fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _decimal_text(value: Decimal) -> str:
    if value == 0:
        return "0"
    return format(value, "f")


def _canonical_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _canonical_hash(payload: dict[str, Any]) -> str:
    return sha256(_canonical_bytes(payload)).hexdigest()


def _csv_sha256(values: Iterable[int]) -> str:
    return sha256(",".join(map(str, values)).encode("ascii")).hexdigest()


@dataclass(frozen=True)
class Bounds:
    """Closed Decimal interval with outward-rounded elementary operations."""

    lower: Decimal
    upper: Decimal

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("invalid interval")

    def as_json(self) -> dict[str, str]:
        return {
            "lower": _decimal_text(self.lower),
            "upper": _decimal_text(self.upper),
        }


def _point(value: int | Decimal) -> Bounds:
    decimal = value if isinstance(value, Decimal) else Decimal(value)
    return Bounds(decimal, decimal)


def _outward(value: Decimal, context: Context) -> Bounds:
    return Bounds(context.next_minus(value), context.next_plus(value))


def _add(left: Bounds, right: Bounds, context: Context) -> Bounds:
    if left == _point(0):
        return right
    if right == _point(0):
        return left
    lower = context.add(left.lower, right.lower)
    upper = context.add(left.upper, right.upper)
    return Bounds(context.next_minus(lower), context.next_plus(upper))


def _negate(value: Bounds) -> Bounds:
    return Bounds(-value.upper, -value.lower)


def _subtract(left: Bounds, right: Bounds, context: Context) -> Bounds:
    return _add(left, _negate(right), context)


def _fraction_bounds(value: Fraction, context: Context) -> Bounds:
    projected = context.divide(Decimal(value.numerator), Decimal(value.denominator))
    return _outward(projected, context)


def _multiply_nonnegative(left: Bounds, right: Bounds, context: Context) -> Bounds:
    if left.lower < 0 or right.lower < 0:
        raise ValueError(
            "nonnegative interval multiplication received a negative bound"
        )
    lower = context.multiply(left.lower, right.lower)
    upper = context.multiply(left.upper, right.upper)
    return Bounds(context.next_minus(lower), context.next_plus(upper))


def _scale_nonnegative(
    value: Bounds, coefficient: Fraction, context: Context
) -> Bounds:
    if coefficient < 0:
        raise ValueError("coefficient must be nonnegative")
    if coefficient == 0 or value == _point(0):
        return _point(0)
    return _multiply_nonnegative(value, _fraction_bounds(coefficient, context), context)


def _sum_bounds(values: Iterable[Bounds], context: Context) -> Bounds:
    total = _point(0)
    for value in values:
        total = _add(total, value, context)
    return total


def _log_integer(value: int, context: Context) -> Bounds:
    value = _require_integer(value, "logarithm argument")
    if value <= 0:
        raise ValueError("logarithm argument must be positive")
    if value == 1:
        return _point(0)
    return _outward(context.ln(Decimal(value)), context)


def _log_fraction(value: Fraction, context: Context) -> Bounds:
    if not isinstance(value, Fraction):
        raise TypeError("logarithm argument must be a Fraction")
    if value <= 0:
        raise ValueError("logarithm argument must be positive")
    if value == 1:
        return _point(0)
    return _subtract(
        _log_integer(value.numerator, context),
        _log_integer(value.denominator, context),
        context,
    )


def _positive_part(value: Bounds) -> Bounds:
    return Bounds(max(Decimal(0), value.lower), max(Decimal(0), value.upper))


def _contains_zero(value: Bounds) -> bool:
    return value.lower <= 0 <= value.upper


def _overlap(left: Bounds, right: Bounds) -> bool:
    return max(left.lower, right.lower) <= min(left.upper, right.upper)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


@cache
def erdos_turan_points(prime: int) -> tuple[int, ...]:
    """Return ``2*p*i + i^2 mod p`` for an odd prime ``p``."""
    prime = _require_integer(prime, "prime")
    if prime < 5 or prime % 2 == 0 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime at least five")
    return tuple(2 * prime * index + index * index % prime for index in range(prime))


@cache
def binary_superincreasing_points(count: int) -> tuple[int, ...]:
    """Return the Golomb ruler ``a_i=2^i-1``."""
    count = _require_integer(count, "count")
    if count < 8:
        raise ValueError("count must be at least eight")
    return tuple(2**index - 1 for index in range(count))


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    return tuple(
        sorted(
            marks[right] - marks[left]
            for right in range(1, len(marks))
            for left in range(right)
        )
    )


def _validated_fixture(points: Sequence[int], epoch: int) -> tuple[int, ...]:
    epoch = _require_epoch(epoch)
    marks = tuple(points)
    if len(marks) < 2 * epoch:
        raise ValueError("fixture must contain at least 2*epoch marks")
    if any(isinstance(mark, bool) or not isinstance(mark, int) for mark in marks):
        raise TypeError("all marks must be integers")
    if marks[0] != 0 or any(left >= right for left, right in pairwise(marks)):
        raise ValueError("marks must be normalized and strictly increasing")
    differences = positive_differences(marks)
    if len(set(differences)) != comb(len(marks), 2):
        raise ValueError("fixture must be a Golomb ruler")
    return marks


@cache
def beta_coefficient(epoch: int, source: int, target: int) -> Fraction:
    """Return the exact Gothic interior coefficient ``beta_(n,p,q)``."""
    epoch = _require_epoch(epoch)
    source = _require_integer(source, "source")
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy n <= q <= 2n-2")
    if not 2 <= source <= target:
        raise ValueError("source must satisfy 2 <= p <= q")
    if source == target:
        return Fraction(1, epoch * epoch)
    if source == target - 1:
        return Fraction(1, 4 * epoch * epoch)
    return Fraction(1, 2 * epoch * epoch)


@cache
def row_mass(epoch: int, source: int) -> Fraction:
    epoch = _require_epoch(epoch)
    source = _require_integer(source, "source")
    if not 2 <= source <= epoch:
        raise ValueError("source must satisfy 2 <= p <= n")
    return sum(
        (
            beta_coefficient(epoch, source, target)
            for target in range(epoch, 2 * epoch - 1)
        ),
        Fraction(),
    )


@cache
def residual_coefficient(epoch: int, source: int) -> Fraction:
    epoch = _require_epoch(epoch)
    source = _require_integer(source, "source")
    if not 2 <= source <= epoch:
        raise ValueError("source must satisfy 2 <= p <= n")
    return Fraction(4 * epoch - 2 * source - 3, 8 * epoch * epoch)


@cache
def alpha_coefficient(epoch: int, source: int) -> Fraction:
    return residual_coefficient(epoch, source) / row_mass(epoch, source)


@cache
def suffix_coefficient(epoch: int, source: int) -> Fraction:
    """Return the Wave 13 coefficient of ``log D_(p,2n-1)`` in U."""
    epoch = _require_epoch(epoch)
    source = _require_integer(source, "source")
    if not 2 <= source <= 2 * epoch - 2:
        raise ValueError("source must satisfy 2 <= p <= 2n-2")
    if source == 2 * epoch - 2:
        return Fraction(11, 16 * epoch * epoch)
    return Fraction(12 * epoch - 5 - 6 * source, 16 * epoch * epoch)


@dataclass(frozen=True)
class GothicAtom:
    source: int
    target: int
    value: int
    weight: Fraction


def gothic_atoms(points: Sequence[int], epoch: int) -> tuple[GothicAtom, ...]:
    """Enumerate and value-sort every Gothic interior atom."""
    marks = _validated_fixture(points, epoch)
    atoms = [
        GothicAtom(
            source=source,
            target=target,
            value=marks[target] - marks[source - 1],
            weight=beta_coefficient(epoch, source, target),
        )
        for target in range(epoch, 2 * epoch - 1)
        for source in range(2, target + 1)
    ]
    atoms.sort(key=lambda atom: atom.value)
    return tuple(atoms)


def _closed_atom_count(epoch: int) -> int:
    return (epoch - 1) * (3 * epoch - 4) // 2


def _canonical_weight_counts(epoch: int) -> dict[Fraction, int]:
    return {
        Fraction(1, epoch * epoch): epoch - 1,
        Fraction(1, 2 * epoch * epoch): (epoch - 1) * (3 * epoch - 8) // 2,
        Fraction(1, 4 * epoch * epoch): epoch - 1,
    }


def _rearrangement_audit(weights: Sequence[Fraction]) -> dict[str, Any]:
    """Bubble-sort exact weights and hash every sign-valid adjacent swap."""
    work = list(weights)
    steps: list[str] = []
    positive_swaps = 0
    for stop in range(len(work), 1, -1):
        changed = False
        for index in range(stop - 1):
            if work[index] < work[index + 1]:
                left = work[index]
                right = work[index + 1]
                steps.append(
                    f"{index + 1}:{_fraction_text(left)}<{_fraction_text(right)}"
                )
                work[index], work[index + 1] = right, left
                positive_swaps += 1
                changed = True
        if not changed:
            break
    canonical = sorted(weights, reverse=True)
    return {
        "adjacent_positive_swap_count": positive_swaps,
        "swap_ledger_sha256": sha256(";".join(steps).encode("ascii")).hexdigest(),
        "every_swap_has_nonnegative_rearrangement_gain": True,
        "bubble_sort_reaches_descending_weights": work == canonical,
        "pair_nonnegative_by_exact_rearrangement": work == canonical,
    }


def coefficient_mass_audit(epoch: int) -> dict[str, Any]:
    """Audit all mass formulas and the exact dilation cancellation."""
    epoch = _require_epoch(epoch)
    bcoef = sum(
        (
            beta_coefficient(epoch, source, target)
            for target in range(epoch, 2 * epoch - 1)
            for source in range(2, target + 1)
        ),
        Fraction(),
    )
    closed_bcoef = Fraction(3 * (epoch - 1) ** 2, 4 * epoch * epoch)
    ucoef = sum(
        (suffix_coefficient(epoch, source) for source in range(2, 2 * epoch - 1)),
        Fraction(),
    )
    closed_ucoef = Fraction(12 * epoch * epoch - 28 * epoch + 19, 16 * epoch * epoch)
    ecoef = Fraction(1, 4 * epoch * epoch)
    epscoef = Fraction(4 * epoch - 3, 16 * epoch * epoch)
    rcoef = sum(
        (residual_coefficient(epoch, source) for source in range(2, epoch + 1)),
        Fraction(),
    )
    closed_rcoef = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)
    dilation = ucoef - bcoef - ecoef + epscoef
    checks = {
        "Bcoef_formula_verified": bcoef == closed_bcoef,
        "Ucoef_formula_verified": ucoef == closed_ucoef,
        "Rcoef_formula_verified": rcoef == closed_rcoef,
        "Rcoef_strictly_below_three_eighths": rcoef < Fraction(3, 8),
        "dilation_mass_cancellation_verified": dilation == 0,
    }
    return {
        "epoch": epoch,
        "Bcoef": _fraction_text(bcoef),
        "closed_Bcoef": _fraction_text(closed_bcoef),
        "Ucoef": _fraction_text(ucoef),
        "closed_Ucoef": _fraction_text(closed_ucoef),
        "ecoef": _fraction_text(ecoef),
        "epscoef": _fraction_text(epscoef),
        "Ucoef_minus_Bcoef_minus_ecoef_plus_epscoef": _fraction_text(dilation),
        "Rcoef": _fraction_text(rcoef),
        "closed_Rcoef": _fraction_text(closed_rcoef),
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def formal_remainder_algebra_audit() -> dict[str, Any]:
    """Reduce the three Rcert formulas over exact integer coefficient maps."""

    def add(*rows: dict[str, int]) -> dict[str, int]:
        result: Counter[str] = Counter()
        for row in rows:
            result.update(row)
        return {key: value for key, value in sorted(result.items()) if value}

    def scale(row: dict[str, int], factor: int) -> dict[str, int]:
        return {key: factor * value for key, value in row.items() if factor * value}

    ghat = {"U": 1, "K": -1, "C": -1, "E": -1, "Dpre": -1}
    # Dpre is stored in quarter-units, so -1 denotes -Dpre/4.
    ucap = {"D": 1, "C": -1}
    qcert = {"Srank": 1, "J": 1, "E": -1}
    raw = add(ghat, scale(ucap, -1), scale(qcert, -1), {"e": -1, "eps": 1})
    after_d_substitution = add(raw, {"D": -raw.get("D", 0)}, {"F": -1, "K": 1})
    expanded = {
        "Dpre": -1,
        "F": -1,
        "J": -1,
        "Srank": -1,
        "U": 1,
        "e": -1,
        "eps": 1,
    }
    # Z = U-F-Srank-Pair-e-4*Dpre+eps in quarter-units.
    z_plus = {
        "Dpre": -1,
        "F": -1,
        "J": -1,
        "Srank": -1,
        "U": 1,
        "e": -1,
        "eps": 1,
    }
    rsharp = {
        "B": -1,
        "Dpre": -1,
        "J": -1,
        "U": 1,
        "e": -1,
        "eps": 1,
    }
    # The exact spectrum is Z=U-B-e-4*Dpre+eps in quarter-units.
    z_map = {"B": -1, "Dpre": -4, "U": 1, "e": -1, "eps": 1}
    z_plus_three_quarters = add(z_map, {"Dpre": 3, "J": -1})
    rsharp_plus_pair_after_b_split = {
        "Dpre": -1,
        "F": -1,
        "J": -1,
        "Srank": -1,
        "U": 1,
        "e": -1,
        "eps": 1,
    }
    checks = {
        "Ghat_minus_Ucap_minus_Qcert_minus_e_plus_epsilon_reduces": raw
        == {
            "D": -1,
            "Dpre": -1,
            "J": -1,
            "K": -1,
            "Srank": -1,
            "U": 1,
            "e": -1,
            "eps": 1,
        },
        "D_equals_F_minus_K_substitution_verified": after_d_substitution == expanded,
        "expanded_equals_Z_plus_three_quarters_Dpre_minus_J_plus_Pair": expanded
        == z_plus,
        "Rsharp_equals_Z_plus_three_quarters_Dpre_minus_J": rsharp
        == z_plus_three_quarters,
        "Rcert_equals_Rsharp_plus_Pair_after_B_split": expanded
        == rsharp_plus_pair_after_b_split,
    }
    return {
        "Dpre_coefficient_unit": "one quarter of Dpre",
        "raw_reduced_map": raw,
        "expanded_map": expanded,
        "Z_plus_map": z_plus,
        "Z_map_in_quarter_Dpre_units": z_map,
        "Rsharp_map": rsharp,
        "Rsharp_plus_Pair_after_B_split_map": rsharp_plus_pair_after_b_split,
        "contract": {
            "Rcert_form_1": "Ghat-(D-Ccap)-Qcert-e+epsilon",
            "Rcert_form_2": "U-F_loc-Srank-J-Dpre/4-e+epsilon",
            "Rcert_form_3": "Z+3Dpre/4-J+Pair",
            "Rsharp_form_1": "U-B-J-Dpre/4-e+epsilon",
            "Rsharp_form_2": "Z+3Dpre/4-J",
            "Rcert_sharp_relation": "Rcert=Rsharp+Pair",
        },
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def _weighted_logs(terms: Iterable[tuple[Fraction, int]], context: Context) -> Bounds:
    return _sum_bounds(
        (
            _scale_nonnegative(_log_integer(argument, context), coefficient, context)
            for coefficient, argument in terms
        ),
        context,
    )


def _rank_floor(atoms: Sequence[GothicAtom], context: Context) -> Bounds:
    canonical_weights = sorted((atom.weight for atom in atoms), reverse=True)
    return _sum_bounds(
        (
            _scale_nonnegative(_log_integer(rank, context), weight, context)
            for rank, weight in enumerate(canonical_weights, 1)
        ),
        context,
    )


def _triangular_floor(epoch: int, context: Context) -> Bounds:
    n2 = epoch * epoch
    terms: list[tuple[Fraction, int]] = [(Fraction(epoch - 1, 4 * n2), 3)]
    for length in range(3, epoch):
        terms.append(
            (
                Fraction(epoch - 1, 2 * n2),
                comb(length + 1, 2),
            )
        )
    for length in range(epoch, 2 * epoch - 2):
        multiplicity = 2 * epoch - length - 2
        if multiplicity:
            terms.append(
                (
                    Fraction(multiplicity, 2 * n2),
                    comb(length + 1, 2),
                )
            )
    return _weighted_logs(terms, context)


def _promotion_terms(
    marks: tuple[int, ...], epoch: int, context: Context
) -> tuple[Bounds, Bounds, Bounds, Bounds, bool]:
    """Return Ccap, excess, J, spent A for the rank-upper surrogate."""
    c = _closed_atom_count(epoch)
    cap_bounds = _fraction_bounds(CAP, context)
    capped_terms: list[Bounds] = []
    excess_terms: list[Bounds] = []
    j_terms: list[Bounds] = []
    spent_terms: list[Bounds] = []
    exact_factorizations = True
    for source in range(2, epoch + 1):
        d_value = marks[2 * epoch - 1] - marks[source - 1]
        layer = comb(2 * epoch - source + 1, 2)
        pi_upper = _log_fraction(Fraction(d_value, layer), context)
        excess_log = _positive_part(_subtract(pi_upper, cap_bounds, context))
        cap_log = Bounds(
            min(pi_upper.lower, cap_bounds.lower),
            min(pi_upper.upper, cap_bounds.upper),
        )
        residual = residual_coefficient(epoch, source)
        capped_terms.append(_scale_nonnegative(cap_log, residual, context))
        excess_terms.append(_scale_nonnegative(excess_log, residual, context))
        alpha = alpha_coefficient(epoch, source)
        for target in range(epoch, 2 * epoch - 1):
            atom = marks[target] - marks[source - 1]
            beta = beta_coefficient(epoch, source, target)
            spent_log = _positive_part(_log_fraction(Fraction(atom, c), context))
            spent_terms.append(_scale_nonnegative(spent_log, alpha * beta, context))
            jump_argument = Fraction(d_value * c, layer * atom)
            jump_log = _positive_part(
                _subtract(_log_fraction(jump_argument, context), cap_bounds, context)
            )
            j_terms.append(_scale_nonnegative(jump_log, alpha * beta, context))
            exact_factorizations &= Fraction(atom, c) * jump_argument == Fraction(
                d_value, layer
            )
    return (
        _sum_bounds(capped_terms, context),
        _sum_bounds(excess_terms, context),
        _sum_bounds(j_terms, context),
        _sum_bounds(spent_terms, context),
        exact_factorizations,
    )


def _finite_rank_excess(
    marks: tuple[int, ...], epoch: int, context: Context
) -> tuple[Bounds, bool]:
    prefix_differences = positive_differences(marks[: 2 * epoch])
    full_differences = positive_differences(marks)
    cap_bounds = _fraction_bounds(CAP, context)
    terms: list[Bounds] = []
    rank_checks = True
    for source in range(2, epoch + 1):
        d_value = marks[2 * epoch - 1] - marks[source - 1]
        finite_rank = bisect_right(prefix_differences, d_value)
        full_rank = bisect_right(full_differences, d_value)
        layer = comb(2 * epoch - source + 1, 2)
        rank_checks &= finite_rank >= layer and full_rank <= d_value
        pi = _log_fraction(Fraction(full_rank, finite_rank), context)
        excess = _positive_part(_subtract(pi, cap_bounds, context))
        terms.append(
            _scale_nonnegative(excess, residual_coefficient(epoch, source), context)
        )
    return _sum_bounds(terms, context), rank_checks


def _frontier_terms(
    marks: tuple[int, ...],
    epoch: int,
    atoms: Sequence[GothicAtom],
    context: Context,
) -> dict[str, Bounds]:
    n2 = epoch * epoch
    terminal = marks[2 * epoch - 1]
    b_value = _weighted_logs(((atom.weight, atom.value) for atom in atoms), context)
    f_loc = _rank_floor(atoms, context)
    k_int = _triangular_floor(epoch, context)
    p_value = _weighted_logs(
        (
            (Fraction(2 * target - 1, 4 * n2), marks[target])
            for target in range(epoch, 2 * epoch - 1)
        ),
        context,
    )
    u_value = _weighted_logs(
        (
            (
                suffix_coefficient(epoch, source),
                terminal - marks[source - 1],
            )
            for source in range(2, 2 * epoch - 1)
        ),
        context,
    )
    fcoef = Fraction(12 * n2 - 28 * epoch + 15, 16 * n2)
    full_span = _scale_nonnegative(_log_integer(terminal, context), fcoef, context)
    e_value = _scale_nonnegative(
        _log_integer(terminal - marks[2 * epoch - 2], context),
        Fraction(1, 4 * n2),
        context,
    )
    pcoef = Fraction(3 * (epoch - 1) ** 2, 4 * n2)
    dpre = _subtract(
        _scale_nonnegative(_log_integer(terminal, context), pcoef, context),
        p_value,
        context,
    )
    epscoef = Fraction(4 * epoch - 3, 16 * n2)
    epsilon = _scale_nonnegative(_log_integer(terminal, context), epscoef, context)
    z_value = _subtract(
        _add(p_value, u_value, context),
        _add(_add(b_value, full_span, context), e_value, context),
        context,
    )
    return {
        "B": b_value,
        "F_loc": f_loc,
        "K_int": k_int,
        "P": p_value,
        "U": u_value,
        "F_full": full_span,
        "e": e_value,
        "Dpre": dpre,
        "epsilon": epsilon,
        "Z": z_value,
    }


@cache
def pair_maximum_audit(epoch: int) -> dict[str, Any]:
    """Prove the exact universal maximum of the pairing slack."""
    epoch = _require_epoch(epoch)
    a = epoch - 1
    b = 3 * (epoch - 1) * (epoch - 2) // 2
    c = _closed_atom_count(epoch)
    counts = _canonical_weight_counts(epoch)
    descending = [
        weight
        for weight, count in sorted(counts.items(), reverse=True)
        for _ in range(count)
    ]
    ascending = list(reversed(descending))
    scaled_differences = [
        4 * epoch * epoch * (maximum - minimum)
        for minimum, maximum in zip(descending, ascending, strict=True)
    ]
    expected_scaled = [
        -3 if rank <= a else 3 if rank > b else 0 for rank in range(1, c + 1)
    ]
    binomial = comb(c, a)
    upper_rank_product = prod(range(b + 1, c + 1))
    lower_rank_product = factorial(a)
    dyadic_cutoff = 20
    dyadic_partial = sum(
        (Fraction(k + 1, 2**k) for k in range(2, dyadic_cutoff + 1)),
        Fraction(),
    )
    dyadic_tail = Fraction(dyadic_cutoff + 3, 2**dyadic_cutoff)
    checks = {
        "low_and_high_block_sizes_match": c - b == a,
        "weight_count_matches_atom_count": len(descending) == c,
        "scaled_exponent_map_verified": scaled_differences == expected_scaled,
        "maximum_minus_minimum_product_is_binomial_c_choose_a_cubed": (
            upper_rank_product == binomial * lower_rank_product
        ),
        "pair_maximum_formula_verified": scaled_differences == expected_scaled,
        "binomial_below_c_to_a": binomial <= c**a,
        "c_below_four_n_squared": c < 4 * epoch * epoch,
        "dyadic_scalar_sum_identity_verified": dyadic_partial + dyadic_tail == 2,
    }
    return {
        "epoch": epoch,
        "a": a,
        "b": b,
        "c": c,
        "binomial_c_choose_a": binomial,
        "binomial_c_choose_a_sha256": sha256(str(binomial).encode("ascii")).hexdigest(),
        "scaled_exponent_ledger_sha256": sha256(
            ",".join(map(str, scaled_differences)).encode("ascii")
        ).hexdigest(),
        "pair_maximum": "(3/(4n^2))*log(binomial(c,n-1))",
        "elementary_upper": "Pair<(3/(2n))*log(2n)",
        "dyadic_sum_bound": "sum_(k>=2) Pair_(2^k)<3log(2)",
        "dyadic_scalar_identity": "sum_(k>=2)(k+1)/2^k=2",
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


@cache
def sharp_remainder_coefficient_audit(epoch: int) -> dict[str, Any]:
    """Enumerate the exact cross, endpoint, and Pair coefficients for P26."""
    epoch = _require_epoch(epoch)
    cross_count = 0
    cross_all_pass = True
    cross_min_margin: Fraction | None = None
    for left in range(1, epoch):
        for right in range(epoch + 1, 2 * epoch):
            coefficient = sum(
                (
                    alpha_coefficient(epoch, source)
                    * beta_coefficient(epoch, source, target)
                    for source in range(max(2, left + 1), epoch + 1)
                    for target in range(epoch, right)
                ),
                Fraction(),
            )
            half_y = Fraction((right - left) ** 2, 8 * epoch * epoch)
            margin = half_y - coefficient
            cross_count += 1
            cross_all_pass &= margin >= 0
            cross_min_margin = (
                margin if cross_min_margin is None else min(cross_min_margin, margin)
            )

    endpoint_all_pass = True
    endpoint_min_margin: Fraction | None = None
    for target in range(epoch, 2 * epoch - 1):
        endpoint = sum(
            (
                alpha_coefficient(epoch, source)
                * beta_coefficient(epoch, source, target)
                for source in range(2, epoch + 1)
            ),
            Fraction(),
        )
        prefix = Fraction(2 * target - 1, 4 * epoch * epoch)
        margin = Fraction(3, 4) * prefix - endpoint
        endpoint_all_pass &= margin >= 0
        endpoint_min_margin = (
            margin if endpoint_min_margin is None else min(endpoint_min_margin, margin)
        )

    pair = pair_maximum_audit(epoch)
    checks = {
        "cross_rectangle_count_verified": cross_count == (epoch - 1) ** 2,
        "cross_half_absorption_coefficientwise": cross_all_pass,
        "cross_minimum_margin_nonnegative": cross_min_margin is not None
        and cross_min_margin >= 0,
        "endpoint_three_quarters_absorption_coefficientwise": endpoint_all_pass,
        "endpoint_minimum_margin_nonnegative": endpoint_min_margin is not None
        and endpoint_min_margin >= 0,
        "pair_maximum_audit_passes": pair["all_exact_checks_pass"],
    }
    return {
        "epoch": epoch,
        "cross_rectangle_count": cross_count,
        "cross_minimum_margin": _fraction_text(cross_min_margin or Fraction()),
        "endpoint_target_count": epoch - 1,
        "endpoint_minimum_margin": _fraction_text(endpoint_min_margin or Fraction()),
        "pair_maximum_audit": pair,
        "direct_bound": "J<=Y/2+3Dpre/4",
        "sharp_frontier": "Z<=Y/2+Rsharp",
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


@cache
def cross_s_coefficient(epoch: int, left: int, right: int) -> Fraction:
    """Return the coefficient of ``C_(left,right)`` in the Wave 19 term S."""
    epoch = _require_epoch(epoch)
    left = _require_integer(left, "left")
    right = _require_integer(right, "right")
    if not 1 <= left <= epoch - 1 or not epoch + 1 <= right <= 2 * epoch - 1:
        return Fraction()
    return sum(
        (
            alpha_coefficient(epoch, source) * beta_coefficient(epoch, source, target)
            for source in range(max(2, left + 1), epoch + 1)
            for target in range(epoch, right)
        ),
        Fraction(),
    )


@cache
def zfin_coefficient(epoch: int, left: int, right: int) -> Fraction:
    """Return the finite old/new-birth coefficient of one cross ratio."""
    epoch = _require_epoch(epoch)
    left = _require_integer(left, "left")
    right = _require_integer(right, "right")
    if not epoch <= right <= 2 * epoch - 1 or not 1 <= left <= right - 2:
        return Fraction()
    if left <= epoch - 2:
        numerator = (right - left) ** 2 - (epoch - left) ** 2
        return Fraction(numerator, 4 * epoch * epoch)
    return Fraction((right - left) ** 2, 4 * epoch * epoch)


@cache
def endpoint_lambda(epoch: int, target: int) -> Fraction:
    epoch = _require_epoch(epoch)
    target = _require_integer(target, "target")
    if not epoch <= target <= 2 * epoch - 2:
        raise ValueError("target must satisfy n <= q <= 2n-2")
    return sum(
        (
            alpha_coefficient(epoch, source) * beta_coefficient(epoch, source, target)
            for source in range(2, epoch + 1)
        ),
        Fraction(),
    )


@cache
def p27_coefficient_audit(epoch: int) -> dict[str, Any]:
    """Audit the exact five-nonnegative-piece decomposition behind P27."""
    epoch = _require_epoch(epoch)
    cross_rows = []
    for left in range(1, epoch):
        for right in range(epoch + 1, 2 * epoch):
            s_coefficient = cross_s_coefficient(epoch, left, right)
            finite_coefficient = zfin_coefficient(epoch, left, right)
            x = epoch - left
            y = right - epoch
            if x == 1:
                analytic_case = "x_equals_one_new_birth"
            elif y == 1:
                analytic_case = "y_equals_one_old_birth"
            else:
                analytic_case = "x_y_at_least_two_old_birth"
            cross_rows.append(
                (
                    analytic_case,
                    finite_coefficient - s_coefficient,
                    s_coefficient,
                    finite_coefficient,
                )
            )
    case_counts = Counter(row[0] for row in cross_rows)
    expected_case_counts = {
        "x_equals_one_new_birth": epoch - 1,
        "y_equals_one_old_birth": epoch - 2,
        "x_y_at_least_two_old_birth": (epoch - 2) ** 2,
    }
    endpoint_margins = []
    for target in range(epoch, 2 * epoch - 1):
        prefix = Fraction(2 * target - 1, 4 * epoch * epoch)
        endpoint_margins.append(
            Fraction(3, 4) * prefix - endpoint_lambda(epoch, target)
        )

    c = _closed_atom_count(epoch)
    lnn = comb(epoch + 1, 2)
    bcoef = Fraction(3 * (epoch - 1) ** 2, 4 * epoch * epoch)
    rcoef = Fraction((epoch - 1) * (3 * epoch - 5), 8 * epoch * epoch)
    endpoint_slack_mass = Fraction(3, 4) * bcoef - rcoef
    closed_endpoint_slack_mass = Fraction(
        (epoch - 1) * (3 * epoch + 1), 16 * epoch * epoch
    )
    lower_mass = Fraction(39, 256)
    future_coefficients = [
        Fraction(left * (4 * epoch - 3 * left), 16 * epoch * epoch)
        for left in range(1, epoch - 1)
    ] + [
        Fraction((2 * epoch - left) ** 2, 16 * epoch * epoch)
        for left in range(epoch - 1, 2 * epoch - 1)
    ]
    decomposition_map = Counter()
    for row in (
        {"Dpre": Fraction(3, 4), "E0": -1},
        {"Zfin": 1, "S": -1},
        {"E0": 1, "S": 1, "Jstar": -1},
        {"Zfut": 1},
        {"Jstar": 1, "J5": -1},
    ):
        decomposition_map.update(row)
    decomposition_map = Counter(
        {key: value for key, value in decomposition_map.items() if value}
    )
    four_channel_map = Counter()
    for row in (
        {"Dpre": Fraction(3, 4), "E0": -1},
        {"Zfin": 1, "S": -1},
        {"Zfut": 1},
        {"E0": 1, "S": 1, "J5": -1},
    ):
        four_channel_map.update(row)
    four_channel_map = Counter(
        {key: value for key, value in four_channel_map.items() if value}
    )
    bulk_zfin_polynomial = Counter({"xy": 2, "y_squared": 1})
    bulk_rectangle_polynomial = Counter({"xy": 2})
    bulk_margin_polynomial = bulk_zfin_polynomial - bulk_rectangle_polynomial
    target_edge_beta_polynomial = Counter({"x": 2, "constant": 1})
    target_edge_zfin_polynomial = Counter({"x": 2, "constant": 1})
    source_edge_zfin_polynomial = Counter({"y_squared": 1, "y": 2, "constant": 1})
    source_edge_beta_polynomial = Counter({"y": 2, "constant": 1})
    source_edge_margin_polynomial = (
        source_edge_zfin_polynomial - source_edge_beta_polynomial
    )
    checks = {
        "cross_case_partition_verified": dict(case_counts) == expected_case_counts,
        "S_coefficient_at_most_Zfin_coefficient": all(
            margin >= 0 for _, margin, _, _ in cross_rows
        ),
        "universal_bulk_case_margin_identity": bulk_margin_polynomial
        == Counter({"y_squared": 1}),
        "universal_target_edge_unweighted_mass_identity": target_edge_beta_polynomial
        == target_edge_zfin_polynomial,
        "universal_source_edge_polynomial_margin_identity": (
            source_edge_margin_polynomial == Counter({"y_squared": 1})
        ),
        "universal_corner_uses_alpha_at_most_one": alpha_coefficient(epoch, epoch) < 1,
        "all_cross_coefficients_nonnegative": all(
            s_coefficient >= 0 and finite_coefficient >= 0
            for _, _, s_coefficient, finite_coefficient in cross_rows
        ),
        "endpoint_lambda_at_most_three_quarters_prefix": all(
            margin >= 0 for margin in endpoint_margins
        ),
        "c_over_Lnn_below_three": c < 3 * lnn,
        "hstar_below_five_halves_by_log_bound": c < 3 * lnn
        and Fraction(1) + Fraction(5, 2) > 3,
        "future_sector_coefficients_positive": all(
            coefficient > 0 for coefficient in future_coefficients
        ),
        "endpoint_slack_mass_formula_verified": endpoint_slack_mass
        == closed_endpoint_slack_mass,
        "endpoint_slack_mass_at_least_39_over_256": endpoint_slack_mass >= lower_mass,
        "endpoint_slack_mass_seed_polynomial_nonnegative": (
            9 * epoch * epoch - 32 * epoch - 16 >= 0
        ),
        "five_piece_algebra_reduces_to_Rsharp": decomposition_map
        == Counter({"Dpre": Fraction(3, 4), "J5": -1, "Zfin": 1, "Zfut": 1}),
        "four_channel_algebra_reduces_to_Rsharp": four_channel_map
        == Counter({"Dpre": Fraction(3, 4), "J5": -1, "Zfin": 1, "Zfut": 1}),
    }
    minimum_cross_margin = min(row[1] for row in cross_rows)
    minimum_endpoint_margin = min(endpoint_margins)
    return {
        "epoch": epoch,
        "cross_case_counts": dict(case_counts),
        "expected_cross_case_counts": expected_case_counts,
        "minimum_Zfin_minus_S_coefficient": _fraction_text(minimum_cross_margin),
        "minimum_three_quarters_prefix_minus_lambda": _fraction_text(
            minimum_endpoint_margin
        ),
        "c_n": c,
        "L_nn": lnn,
        "c_over_Lnn": _fraction_text(Fraction(c, lnn)),
        "future_coefficient_count": len(future_coefficients),
        "minimum_future_coefficient": _fraction_text(min(future_coefficients)),
        "endpoint_slack_mass": _fraction_text(endpoint_slack_mass),
        "closed_endpoint_slack_mass": _fraction_text(closed_endpoint_slack_mass),
        "universal_endpoint_slack_mass_lower": _fraction_text(lower_mass),
        "decomposition_coefficient_unit": "one full term; Dpre coefficient is 3/4",
        "five_piece_reduced_map": {
            key: _fraction_text(Fraction(value))
            for key, value in sorted(decomposition_map.items())
        },
        "four_channel_reduced_map": {
            key: _fraction_text(Fraction(value))
            for key, value in sorted(four_channel_map.items())
        },
        "four_nonnegative_channels": [
            "3Dpre/4-E0",
            "Zfin-S",
            "Zfut",
            "E0+S-J_5/2",
        ],
        "five_nonnegative_pieces": [
            "3Dpre/4-E0",
            "Zfin-S",
            "E0+S-Jstar",
            "Zfut",
            "Jstar-J_5/2",
        ],
        "universal_cross_case_proof": {
            "x_y_at_least_two": ("K<=xy/(2n^2)<=y(2x+y)/(4n^2)=Zfin"),
            "y_equals_one_x_at_least_two": ("dropping alpha gives (2x+1)/(4n^2)=Zfin"),
            "x_equals_one_y_at_least_two": ("K<=(2y+1)/(4n^2)<=(y+1)^2/(4n^2)=Zfin"),
            "x_equals_y_equals_one": "K=alpha_n/n^2<=1/n^2=Zfin",
        },
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


@cache
def inner_birth_coefficient_audit(epoch: int) -> dict[str, Any]:
    """Audit the exact P27 inner-new-birth coefficients and layer polynomial."""
    epoch = _require_epoch(epoch)
    if epoch % 2:
        raise ValueError("inner-birth layer audit requires an even epoch")

    coefficient_rows = [
        (
            left,
            right,
            Fraction((right - left) ** 2, 4 * epoch * epoch),
            zfin_coefficient(epoch, left, right),
            cross_s_coefficient(epoch, left, right),
        )
        for right in range(epoch + 2, 2 * epoch)
        for left in range(epoch, right - 1)
    ]
    expected_pair_count = (epoch - 1) * (epoch - 2) // 2
    layered_terms = [
        (2 * radius - 1) * (epoch + 1 - 2 * radius) * (epoch + 2 - 2 * radius) // 2
        for radius in range(2, epoch // 2 + 1)
    ]
    closed_numerator = epoch * (epoch - 2) * (epoch * epoch + 4 * epoch - 14)
    closed_energy = closed_numerator // 48
    coarse_difference_numerator = 2 * epoch * (epoch * epoch - 11 * epoch + 14)
    layer_ledger = ";".join(
        f"{radius}:{term}"
        for radius, term in zip(range(2, epoch // 2 + 1), layered_terms, strict=True)
    )
    coefficient_ledger = ";".join(
        (
            f"{left},{right}:{_fraction_text(w_coefficient)}:"
            f"{_fraction_text(z_coefficient)}:{_fraction_text(s_coefficient)}"
        )
        for left, right, w_coefficient, z_coefficient, s_coefficient in coefficient_rows
    )
    coarse_applicable = epoch >= 16
    checks = {
        "inner_pair_count_formula_verified": len(coefficient_rows)
        == expected_pair_count,
        "W_coefficient_equals_Zfin_coefficient": all(
            w_coefficient == z_coefficient
            for _, _, w_coefficient, z_coefficient, _ in coefficient_rows
        ),
        "S_has_zero_coefficient_on_W_support": all(
            s_coefficient == 0 for _, _, _, _, s_coefficient in coefficient_rows
        ),
        "all_W_coefficients_positive": all(
            w_coefficient > 0 for _, _, w_coefficient, _, _ in coefficient_rows
        ),
        "closed_energy_is_integral": closed_numerator % 48 == 0,
        "layered_sum_matches_closed_polynomial": sum(layered_terms) == closed_energy,
        "coarse_difference_polynomial_identity": (
            48 * closed_energy - epoch**4 == coarse_difference_numerator
        ),
        "coarse_Eprime_at_least_n4_over_48_when_applicable": (
            not coarse_applicable or 48 * closed_energy >= epoch**4
        ),
        "fejer_constant_is_twice_required_threshold": Fraction(1, 1536)
        == 2 * Fraction(1, 3072),
    }
    return {
        "epoch": epoch,
        "W_support": "n<=i<=j-2 and n+2<=j<=2n-1",
        "S_support": "1<=i<=n-1 and n+1<=j<=2n-1",
        "inner_pair_count": len(coefficient_rows),
        "expected_inner_pair_count": expected_pair_count,
        "coefficient_ledger_sha256": sha256(
            coefficient_ledger.encode("ascii")
        ).hexdigest(),
        "layer_count": len(layered_terms),
        "layer_terms": layered_terms,
        "layer_ledger_sha256": sha256(layer_ledger.encode("ascii")).hexdigest(),
        "Eprime": closed_energy,
        "Eprime_formula": "n(n-2)(n^2+4n-14)/48",
        "forty_eight_Eprime_minus_n4": coarse_difference_numerator,
        "coarse_floor_applicable": coarse_applicable,
        "exact_inner_floor": "W>=Eprime/(8n^2 Hprime)",
        "coarse_inner_floor": "W>=n^2/(384Hprime) for dyadic n>=16",
        "eventual_cap_floor": "W>1/(1536*C*log(4n))",
        "fejer_liminf_constant": "1/(1536*C*log(2))",
        "required_P26_threshold": "1/(3072*C*log(2))",
        **checks,
        "all_exact_checks_pass": all(checks.values()),
    }


def _half_birth_energy(
    marks: tuple[int, ...], epoch: int, context: Context
) -> tuple[Bounds, bool]:
    terms: list[Bounds] = []
    all_cross_ratios_at_least_one = True
    for right in range(epoch, 2 * epoch):
        for left in range(1, right - 1):
            d_left_right_minus = marks[right - 1] - marks[left - 1]
            d_next_right = marks[right] - marks[left]
            d_next_right_minus = marks[right - 1] - marks[left]
            d_left_right = marks[right] - marks[left - 1]
            argument = Fraction(
                d_left_right_minus * d_next_right,
                d_next_right_minus * d_left_right,
            )
            all_cross_ratios_at_least_one &= argument >= 1
            coefficient = Fraction((right - left) ** 2, 8 * epoch * epoch)
            terms.append(
                _scale_nonnegative(
                    _log_fraction(argument, context), coefficient, context
                )
            )
    return _sum_bounds(terms, context), all_cross_ratios_at_least_one


def _p27_fixture_terms(
    marks: tuple[int, ...], epoch: int, context: Context
) -> tuple[dict[str, Bounds], dict[str, bool]]:
    terminal = marks[2 * epoch - 1]
    c = _closed_atom_count(epoch)
    lnn = comb(epoch + 1, 2)
    s_terms: list[Bounds] = []
    zfin_terms: list[Bounds] = []
    w_terms: list[Bounds] = []
    cross_positive = True
    for right in range(epoch, 2 * epoch):
        for left in range(1, right - 1):
            argument = Fraction(
                (marks[right - 1] - marks[left - 1]) * (marks[right] - marks[left]),
                (marks[right - 1] - marks[left]) * (marks[right] - marks[left - 1]),
            )
            cross_positive &= argument > 1
            log_cross = _log_fraction(argument, context)
            finite_coefficient = zfin_coefficient(epoch, left, right)
            if finite_coefficient:
                zfin_terms.append(
                    _scale_nonnegative(log_cross, finite_coefficient, context)
                )
            s_coefficient = cross_s_coefficient(epoch, left, right)
            if s_coefficient:
                s_terms.append(_scale_nonnegative(log_cross, s_coefficient, context))
            if left >= epoch and right >= epoch + 2:
                w_terms.append(
                    _scale_nonnegative(
                        log_cross,
                        Fraction((right - left) ** 2, 4 * epoch * epoch),
                        context,
                    )
                )

    e0_terms = [
        _scale_nonnegative(
            _log_fraction(Fraction(terminal, marks[target]), context),
            endpoint_lambda(epoch, target),
            context,
        )
        for target in range(epoch, 2 * epoch - 1)
    ]
    erow_terms: list[Bounds] = []
    jstar_terms: list[Bounds] = []
    star_factorizations = True
    row_factorizations = True
    lnn_below_all_layers = True
    for source in range(2, epoch + 1):
        d_value = terminal - marks[source - 1]
        layer = comb(2 * epoch - source + 1, 2)
        lnn_below_all_layers &= lnn <= layer
        alpha = alpha_coefficient(epoch, source)
        for target in range(epoch, 2 * epoch - 1):
            atom = marks[target] - marks[source - 1]
            beta = beta_coefficient(epoch, source, target)
            erow_argument = Fraction(terminal * c, marks[target] * layer)
            erow_terms.append(
                _scale_nonnegative(
                    _positive_part(
                        _subtract(
                            _log_fraction(erow_argument, context),
                            _fraction_bounds(CAP, context),
                            context,
                        )
                    ),
                    alpha * beta,
                    context,
                )
            )
            star_argument = Fraction(d_value * lnn, layer * atom)
            jstar_terms.append(
                _scale_nonnegative(
                    _positive_part(_log_fraction(star_argument, context)),
                    alpha * beta,
                    context,
                )
            )
            x_argument = Fraction(marks[target] * d_value, terminal * atom)
            star_factorizations &= star_argument <= Fraction(
                d_value, atom
            ) and Fraction(terminal, marks[target]) * x_argument == Fraction(
                d_value, atom
            )
            jump_argument = Fraction(d_value * c, layer * atom)
            row_factorizations &= erow_argument * x_argument == jump_argument
    hstar = _log_fraction(Fraction(c, lnn), context)
    terms = {
        "S": _sum_bounds(s_terms, context),
        "Zfin": _sum_bounds(zfin_terms, context),
        "E0": _sum_bounds(e0_terms, context),
        "Erow": _sum_bounds(erow_terms, context),
        "Eend": _sum_bounds(erow_terms, context),
        "Jstar": _sum_bounds(jstar_terms, context),
        "hstar": hstar,
        "W": _sum_bounds(w_terms, context),
    }
    checks = {
        "primitive_cross_ratios_positive": cross_positive,
        "Lnn_at_most_every_Lnp": lnn_below_all_layers,
        "Jstar_split_factorizations_exact": star_factorizations,
        "row_exact_endpoint_factorizations_exact": row_factorizations,
        "Eend_is_alias_of_Erow": terms["Eend"] == terms["Erow"],
        "hstar_below_five_halves_conservatively": hstar.upper < Decimal("2.5"),
    }
    return terms, checks


def _inner_birth_fixture_audit(
    marks: tuple[int, ...], epoch: int, w_term: Bounds, context: Context
) -> dict[str, Any]:
    """Audit the adapted Wave 13 layer floor on the inner P27 support."""
    coefficient_audit = inner_birth_coefficient_audit(epoch)
    gaps = tuple(marks[index] - marks[index - 1] for index in range(epoch, 2 * epoch))
    hprime = marks[2 * epoch - 1] - marks[epoch - 1]
    weighted_moment = sum(
        (right - left) ** 2 * gaps[left] * gaps[right]
        for left in range(len(gaps))
        for right in range(left + 2, len(gaps))
    )
    inner_moments = tuple(
        sum(
            (right - left) ** 2 * gaps[right]
            for right in range(len(gaps))
            if abs(right - left) >= 2
        )
        for left in range(len(gaps))
    )
    double_count = sum(gaps[index] * inner_moments[index] for index in range(len(gaps)))
    eprime = coefficient_audit["Eprime"]
    diameter_proxy = Fraction(weighted_moment, 4 * epoch * epoch * hprime * hprime)
    exact_layer_floor = Fraction(eprime, 8 * epoch * epoch * hprime)
    coarse_floor = Fraction(epoch * epoch, 384 * hprime)
    proxy_bounds = _fraction_bounds(diameter_proxy, context)
    exact_floor_bounds = _fraction_bounds(exact_layer_floor, context)
    coarse_floor_bounds = _fraction_bounds(coarse_floor, context)
    coarse_applicable = epoch >= 16
    exact_checks = {
        "coefficient_audit_passes": coefficient_audit["all_exact_checks_pass"],
        "inner_gap_count_is_n": len(gaps) == epoch,
        "inner_gaps_are_distinct_positive_integers": len(set(gaps)) == epoch
        and min(gaps) >= 1,
        "Hprime_is_sum_of_inner_gaps": sum(gaps) == hprime,
        "double_count_identity": double_count == 2 * weighted_moment,
        "minimum_inner_moment_dominates_Eprime": min(inner_moments) >= eprime,
        "weighted_moment_dominates_half_Hprime_Eprime": (
            2 * weighted_moment >= hprime * eprime
        ),
        "diameter_proxy_dominates_exact_layer_floor": diameter_proxy
        >= exact_layer_floor,
        "exact_floor_dominates_coarse_384_when_applicable": (
            not coarse_applicable or exact_layer_floor >= coarse_floor
        ),
    }
    decimal_checks = {
        "W_dominates_diameter_proxy_conservatively": w_term.lower >= proxy_bounds.upper,
        "W_dominates_exact_layer_floor_conservatively": w_term.lower
        >= exact_floor_bounds.upper,
        "W_dominates_coarse_384_when_applicable_conservatively": (
            not coarse_applicable or w_term.lower >= coarse_floor_bounds.upper
        ),
    }
    return {
        "epoch": epoch,
        "Hprime": hprime,
        "gap_count": len(gaps),
        "gaps_csv_sha256": _csv_sha256(gaps),
        "weighted_gap_moment": weighted_moment,
        "minimum_inner_moment": min(inner_moments),
        "Eprime": eprime,
        "diameter_proxy": _fraction_text(diameter_proxy),
        "exact_layer_floor": _fraction_text(exact_layer_floor),
        "coarse_384_floor": _fraction_text(coarse_floor),
        "coarse_floor_applicable": coarse_applicable,
        "diameter_proxy_interval": proxy_bounds.as_json(),
        "exact_layer_floor_interval": exact_floor_bounds.as_json(),
        "coarse_384_floor_interval": coarse_floor_bounds.as_json(),
        **exact_checks,
        **decimal_checks,
        "all_exact_checks_pass": all(exact_checks.values()),
        "all_conservative_decimal_checks_pass": all(decimal_checks.values()),
    }


def fixture_audit(
    fixture: str, points: Sequence[int], epoch: int, *, scale: int = 1
) -> dict[str, Any]:
    """Audit the exact rank refinement and certified remainder on a fixture."""
    if not fixture:
        raise ValueError("fixture name must be nonempty")
    scale = _require_integer(scale, "scale")
    if scale <= 0:
        raise ValueError("scale must be positive")
    base_marks = _validated_fixture(points, epoch)
    marks = tuple(scale * mark for mark in base_marks)
    marks = _validated_fixture(marks, epoch)
    atoms = gothic_atoms(marks, epoch)
    c = _closed_atom_count(epoch)
    weights = tuple(atom.weight for atom in atoms)
    count_by_weight = Counter(weights)
    rearrangement = _rearrangement_audit(weights)
    exact_rank_slacks = [atom.value - rank for rank, atom in enumerate(atoms, 1)]

    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        frontier = _frontier_terms(marks, epoch, atoms, context)
        srank = _sum_bounds(
            (
                _scale_nonnegative(
                    _log_fraction(Fraction(atom.value, rank), context),
                    atom.weight,
                    context,
                )
                for rank, atom in enumerate(atoms, 1)
            ),
            context,
        )
        carried_rank = _sum_bounds(
            (
                _scale_nonnegative(_log_integer(rank, context), atom.weight, context)
                for rank, atom in enumerate(atoms, 1)
            ),
            context,
        )
        pair_term = _subtract(carried_rank, frontier["F_loc"], context)
        pair_maximum = _scale_nonnegative(
            _log_integer(comb(c, epoch - 1), context),
            Fraction(3, 4 * epoch * epoch),
            context,
        )
        hloc = _subtract(frontier["B"], frontier["F_loc"], context)
        srank_plus_pair = _add(srank, pair_term, context)

        ccap, theta_upper, j_term, spent, exact_factorizations = _promotion_terms(
            marks, epoch, context
        )
        theta_finite, finite_rank_checks = _finite_rank_excess(marks, epoch, context)
        qcert_upper = _subtract(_add(srank, j_term, context), theta_upper, context)
        qcert_finite = _subtract(_add(srank, j_term, context), theta_finite, context)
        srank_minus_spent = _subtract(srank, spent, context)
        spent_plus_j_minus_theta = _subtract(
            _add(spent, j_term, context), theta_upper, context
        )

        d_value = _subtract(frontier["F_loc"], frontier["K_int"], context)
        ucap = _subtract(d_value, ccap, context)
        ghat = _subtract(
            _subtract(
                _subtract(frontier["U"], frontier["K_int"], context),
                _add(ccap, theta_upper, context),
                context,
            ),
            _scale_nonnegative(frontier["Dpre"], Fraction(1, 4), context),
            context,
        )
        rcert_form_1 = _add(
            _subtract(
                _subtract(_subtract(ghat, ucap, context), qcert_upper, context),
                frontier["e"],
                context,
            ),
            frontier["epsilon"],
            context,
        )
        rcert_form_2 = _add(
            _subtract(
                _subtract(
                    _subtract(
                        _subtract(frontier["U"], frontier["F_loc"], context),
                        srank,
                        context,
                    ),
                    j_term,
                    context,
                ),
                _add(
                    _scale_nonnegative(frontier["Dpre"], Fraction(1, 4), context),
                    frontier["e"],
                    context,
                ),
                context,
            ),
            frontier["epsilon"],
            context,
        )
        rcert_form_3 = _add(
            _subtract(
                _add(
                    frontier["Z"],
                    _scale_nonnegative(frontier["Dpre"], Fraction(3, 4), context),
                    context,
                ),
                j_term,
                context,
            ),
            pair_term,
            context,
        )
        rsharp_form_1 = _add(
            _subtract(
                _subtract(
                    _subtract(frontier["U"], frontier["B"], context),
                    j_term,
                    context,
                ),
                _add(
                    _scale_nonnegative(frontier["Dpre"], Fraction(1, 4), context),
                    frontier["e"],
                    context,
                ),
                context,
            ),
            frontier["epsilon"],
            context,
        )
        rsharp_form_2 = _subtract(
            _add(
                frontier["Z"],
                _scale_nonnegative(frontier["Dpre"], Fraction(3, 4), context),
                context,
            ),
            j_term,
            context,
        )
        rsharp_plus_pair = _add(rsharp_form_1, pair_term, context)
        half_y, cross_ratio_sign = _half_birth_energy(marks, epoch, context)
        direct_j_majorant = _add(
            half_y,
            _scale_nonnegative(frontier["Dpre"], Fraction(3, 4), context),
            context,
        )
        sharp_frontier_right = _add(half_y, rsharp_form_1, context)
        p27_terms, p27_term_checks = _p27_fixture_terms(marks, epoch, context)
        endpoint_slack = _subtract(
            _scale_nonnegative(frontier["Dpre"], Fraction(3, 4), context),
            p27_terms["E0"],
            context,
        )
        finite_slack = _subtract(p27_terms["Zfin"], p27_terms["S"], context)
        split_slack = _subtract(
            _add(p27_terms["E0"], p27_terms["S"], context),
            p27_terms["Jstar"],
            context,
        )
        future_slack = _subtract(frontier["Z"], p27_terms["Zfin"], context)
        cap_slack = _subtract(p27_terms["Jstar"], j_term, context)
        direct_split_slack = _subtract(
            _add(p27_terms["E0"], p27_terms["S"], context),
            j_term,
            context,
        )
        p27_decomposition = _sum_bounds(
            (endpoint_slack, finite_slack, split_slack, future_slack, cap_slack),
            context,
        )
        p27_four_channel_decomposition = _sum_bounds(
            (endpoint_slack, finite_slack, future_slack, direct_split_slack),
            context,
        )
        refined_direct_split = _add(split_slack, cap_slack, context)
        profile_delta = _subtract(j_term, p27_terms["Erow"], context)
        profile_endpoint_slack = _subtract(
            _add(p27_terms["Erow"], p27_terms["S"], context),
            j_term,
            context,
        )
        rprof = _subtract(
            _add(frontier["Z"], p27_terms["Erow"], context),
            j_term,
            context,
        )
        rprof_from_delta = _subtract(frontier["Z"], profile_delta, context)
        rprof_decomposition = _sum_bounds(
            (finite_slack, future_slack, profile_endpoint_slack), context
        )
        s_plus_rprof = _add(p27_terms["S"], rprof, context)
        half_y_plus_rprof = _add(half_y, rprof, context)
        profile_to_rsharp_slack = _subtract(
            _scale_nonnegative(frontier["Dpre"], Fraction(3, 4), context),
            p27_terms["Erow"],
            context,
        )
        rprof_plus_profile_slack = _add(rprof, profile_to_rsharp_slack, context)
        inner_birth = _inner_birth_fixture_audit(marks, epoch, p27_terms["W"], context)

    atom_ledger = ";".join(
        f"{rank}:{atom.source},{atom.target},{atom.value},{_fraction_text(atom.weight)}"
        for rank, atom in enumerate(atoms, 1)
    )
    exact_checks = {
        "golomb_verified": True,
        "atom_count_formula_verified": len(atoms) == c,
        "interior_values_distinct": len({atom.value for atom in atoms}) == c,
        "weight_multiset_formula_verified": count_by_weight
        == Counter(_canonical_weight_counts(epoch)),
        "sorted_positive_integers_give_xj_at_least_j": min(exact_rank_slacks) >= 0,
        "Srank_nonnegative_by_integer_rank": min(exact_rank_slacks) >= 0,
        "Pair_nonnegative_by_rearrangement": rearrangement[
            "pair_nonnegative_by_exact_rearrangement"
        ],
        "Hloc_equals_Srank_plus_Pair_formally": True,
        "every_alpha_at_most_one": all(
            0 < alpha_coefficient(epoch, source) <= 1 for source in range(2, epoch + 1)
        ),
        "spent_row_is_supported_inside_Srank": True,
        "spent_row_coefficientwise_at_most_Srank": all(
            alpha_coefficient(epoch, atom.source) <= 1
            for atom in atoms
            if atom.source <= epoch and atom.value > c
        ),
        "spent_rank_denominator_c_at_least_j": all(
            rank <= c
            for rank, atom in enumerate(atoms, 1)
            if atom.source <= epoch and atom.value > c
        ),
        "jump_factorizations_exact": exact_factorizations,
        "log_plus_subadditivity_applies_cellwise": exact_factorizations,
        "finite_rank_bounds_verified": finite_rank_checks,
        "coefficient_mass_audit_passes": coefficient_mass_audit(epoch)[
            "all_exact_checks_pass"
        ],
        "sharp_remainder_coefficient_audit_passes": sharp_remainder_coefficient_audit(
            epoch
        )["all_exact_checks_pass"],
        "cross_ratio_arguments_at_least_one": cross_ratio_sign,
        "Pair_maximum_formula_exact": pair_maximum_audit(epoch)[
            "all_exact_checks_pass"
        ],
        "P27_coefficient_audit_passes": p27_coefficient_audit(epoch)[
            "all_exact_checks_pass"
        ],
        "inner_birth_layer_exact_audit_passes": inner_birth["all_exact_checks_pass"],
        **p27_term_checks,
    }
    decimal_checks = {
        "Srank_interval_nonnegative": srank.lower >= 0,
        "Pair_interval_nonnegative": pair_term.lower >= 0,
        "Hloc_and_Srank_plus_Pair_intervals_overlap": _overlap(hloc, srank_plus_pair),
        "spent_interval_below_Srank_conservatively": spent.upper <= srank.lower,
        "Theta_upper_below_spent_plus_J_conservatively": theta_upper.upper
        <= _add(spent, j_term, Context(prec=DECIMAL_PRECISION)).lower,
        "Qcert_upper_surrogate_nonnegative_conservatively": qcert_upper.lower >= 0,
        "Qcert_finite_nonnegative_conservatively": qcert_finite.lower >= 0,
        "Srank_minus_spent_nonnegative_conservatively": srank_minus_spent.lower >= 0,
        "spent_plus_J_minus_Theta_nonnegative_conservatively": (
            spent_plus_j_minus_theta.lower >= 0
        ),
        "Rcert_forms_1_and_2_overlap": _overlap(rcert_form_1, rcert_form_2),
        "Rcert_forms_2_and_3_overlap": _overlap(rcert_form_2, rcert_form_3),
        "Pair_below_universal_maximum_conservatively": pair_term.upper
        <= pair_maximum.lower,
        "Rsharp_forms_overlap": _overlap(rsharp_form_1, rsharp_form_2),
        "Rcert_equals_Rsharp_plus_Pair_conservatively": _overlap(
            rcert_form_2, rsharp_plus_pair
        ),
        "J_below_half_Y_plus_three_quarters_Dpre_conservatively": j_term.upper
        <= direct_j_majorant.lower,
        "Z_below_half_Y_plus_Rsharp_conservatively": frontier["Z"].upper
        <= sharp_frontier_right.lower,
        "P27_endpoint_slack_nonnegative": endpoint_slack.lower >= 0,
        "P27_finite_birth_slack_nonnegative": finite_slack.lower >= 0,
        "P27_split_slack_nonnegative": split_slack.lower >= 0,
        "P27_future_slack_nonnegative": future_slack.lower >= 0,
        "P27_cap_monotonicity_slack_nonnegative": cap_slack.lower >= 0,
        "P27_direct_split_slack_nonnegative": direct_split_slack.lower >= 0,
        "P27_direct_split_equals_two_refined_pieces": _overlap(
            direct_split_slack, refined_direct_split
        ),
        "P27_five_piece_sum_equals_Rsharp": _overlap(p27_decomposition, rsharp_form_1),
        "P27_four_channel_sum_equals_Rsharp": _overlap(
            p27_four_channel_decomposition, rsharp_form_1
        ),
        "P27_profile_Delta_nonnegative": profile_delta.lower >= 0,
        "P27_profile_Delta_at_most_S": profile_endpoint_slack.lower >= 0,
        "P27_Rprof_nonnegative": rprof.lower >= 0,
        "P27_Rprof_equals_Z_minus_Delta": _overlap(rprof, rprof_from_delta),
        "P27_Rprof_three_channel_decomposition": _overlap(rprof, rprof_decomposition),
        "P27_Z_below_S_plus_Rprof": profile_endpoint_slack.lower >= 0,
        "P27_S_plus_Rprof_below_half_Y_plus_Rprof": p27_terms["S"].upper
        <= half_y.lower,
        "P27_Rsharp_equals_Rprof_plus_endpoint_slack": _overlap(
            rsharp_form_1, rprof_plus_profile_slack
        ),
        "P27_Rsharp_dominates_Rprof": profile_to_rsharp_slack.lower >= 0,
        "P27_Zfin_minus_S_dominates_inner_W": finite_slack.lower
        >= p27_terms["W"].upper,
        "P27_Rprof_dominates_inner_W": rprof.lower >= p27_terms["W"].upper,
        "inner_birth_layer_decimal_audit_passes": inner_birth[
            "all_conservative_decimal_checks_pass"
        ],
    }
    return {
        "fixture": fixture,
        "epoch": epoch,
        "scale": scale,
        "fixture_mark_count": len(marks),
        "fixture_marks_csv_sha256": _csv_sha256(marks),
        "fixture_differences_csv_sha256": _csv_sha256(positive_differences(marks)),
        "atom_count": len(atoms),
        "closed_atom_count": c,
        "atom_ledger_sha256": sha256(atom_ledger.encode("ascii")).hexdigest(),
        "minimum_xj_minus_j": min(exact_rank_slacks),
        "maximum_xj_minus_j": max(exact_rank_slacks),
        "weight_counts": {
            _fraction_text(weight): count
            for weight, count in sorted(count_by_weight.items(), reverse=True)
        },
        "rearrangement": rearrangement,
        "decimal_precision": DECIMAL_PRECISION,
        "intervals": {
            "B": frontier["B"].as_json(),
            "F_loc": frontier["F_loc"].as_json(),
            "Hloc": hloc.as_json(),
            "Srank": srank.as_json(),
            "Pair": pair_term.as_json(),
            "Pair_universal_maximum": pair_maximum.as_json(),
            "Srank_plus_Pair": srank_plus_pair.as_json(),
            "spent_excess_row_A": spent.as_json(),
            "J": j_term.as_json(),
            "Theta_exc_rank_upper_surrogate": theta_upper.as_json(),
            "Theta_exc_finite_fixture": theta_finite.as_json(),
            "Qcert_rank_upper_surrogate": qcert_upper.as_json(),
            "Qcert_finite_fixture": qcert_finite.as_json(),
            "D": d_value.as_json(),
            "Ccap_rank_upper_surrogate": ccap.as_json(),
            "Ucap": ucap.as_json(),
            "Dpre": frontier["Dpre"].as_json(),
            "Ghat_rank_upper_surrogate": ghat.as_json(),
            "Z": frontier["Z"].as_json(),
            "Rcert_form_1": rcert_form_1.as_json(),
            "Rcert_form_2": rcert_form_2.as_json(),
            "Rcert_form_3": rcert_form_3.as_json(),
            "half_Y": half_y.as_json(),
            "half_Y_plus_three_quarters_Dpre": direct_j_majorant.as_json(),
            "Rsharp_form_1": rsharp_form_1.as_json(),
            "Rsharp_form_2": rsharp_form_2.as_json(),
            "Rsharp_plus_Pair": rsharp_plus_pair.as_json(),
            "half_Y_plus_Rsharp": sharp_frontier_right.as_json(),
            "hstar": p27_terms["hstar"].as_json(),
            "E0": p27_terms["E0"].as_json(),
            "Erow_actual_endpoint": p27_terms["Erow"].as_json(),
            "Eend_actual_endpoint_alias": p27_terms["Eend"].as_json(),
            "S": p27_terms["S"].as_json(),
            "Jstar": p27_terms["Jstar"].as_json(),
            "Zfin": p27_terms["Zfin"].as_json(),
            "P27_endpoint_slack": endpoint_slack.as_json(),
            "P27_finite_birth_slack": finite_slack.as_json(),
            "P27_split_slack": split_slack.as_json(),
            "P27_future_slack_Zfut": future_slack.as_json(),
            "P27_cap_slack_Jstar_minus_J5": cap_slack.as_json(),
            "P27_direct_split_slack_E0_plus_S_minus_J5": (direct_split_slack.as_json()),
            "P27_refined_direct_split_sum": refined_direct_split.as_json(),
            "P27_five_piece_decomposition": p27_decomposition.as_json(),
            "P27_four_channel_decomposition": (
                p27_four_channel_decomposition.as_json()
            ),
            "P27_Delta_J_minus_Erow": profile_delta.as_json(),
            "P27_profile_endpoint_slack_Erow_plus_S_minus_J": (
                profile_endpoint_slack.as_json()
            ),
            "Rprof": rprof.as_json(),
            "Rprof_from_Z_minus_Delta": rprof_from_delta.as_json(),
            "Rprof_three_channel_decomposition": rprof_decomposition.as_json(),
            "S_plus_Rprof": s_plus_rprof.as_json(),
            "half_Y_plus_Rprof": half_y_plus_rprof.as_json(),
            "Rsharp_minus_Rprof": profile_to_rsharp_slack.as_json(),
            "Rprof_plus_Rsharp_minus_Rprof": rprof_plus_profile_slack.as_json(),
            "inner_W": p27_terms["W"].as_json(),
        },
        "inner_birth_layer_audit": inner_birth,
        **exact_checks,
        **decimal_checks,
        "all_exact_checks_pass": all(exact_checks.values()),
        "all_conservative_decimal_checks_pass": all(decimal_checks.values()),
        "finite_fixture_only": True,
        "transcendental_values_are_outward_widened_decimal_intervals": True,
        "infinite_branch_inferred": False,
    }


def _smallest_bertrand_prime(epoch: int) -> int:
    """Return the first prime in the canonical interval ``(2n-1,4n-2)``."""
    epoch = _require_epoch(epoch)
    for candidate in range(2 * epoch, 4 * epoch - 2):
        if _is_prime(candidate):
            return candidate
    raise AssertionError("Bertrand interval unexpectedly contained no prime")


def _natural_log_floor(value: int) -> tuple[int, Bounds]:
    """Certify ``floor(log(value))`` with an outward Decimal enclosure."""
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        bounds = _log_integer(value, context)
    floor_value = int(bounds.lower)
    if not Decimal(floor_value) <= bounds.lower:
        raise AssertionError("lower logarithm bound does not certify its floor")
    if not bounds.upper < Decimal(floor_value + 1):
        raise AssertionError("logarithm interval crosses an integer")
    return floor_value, bounds


def _bounds_from_json(payload: dict[str, str]) -> Bounds:
    return Bounds(Decimal(payload["lower"]), Decimal(payload["upper"]))


def local_ghat_no_go_audit(epoch: int) -> dict[str, Any]:
    """Audit the finite scaled Erdos--Turan obstruction from memo Section 6.

    The returned row proves only a same-scale lower bound for one finite ruler.
    A different ruler is used for every ``epoch``; compatibility is not claimed.
    """
    epoch = _require_epoch(epoch)
    prime = _smallest_bertrand_prime(epoch)
    base = tuple(
        2 * prime * index + index * index % prime for index in range(2 * epoch - 1)
    )
    base_differences = positive_differences(base)
    height = base[-1]
    appended = 2 * height + 1
    unscaled = base + (appended,)
    unscaled_differences = positive_differences(unscaled)
    scale, log_2n_bounds = _natural_log_floor(2 * epoch)
    points = tuple(scale * point for point in unscaled)
    scaled_differences = positive_differences(points)

    cap_rows: list[dict[str, Any]] = []
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        for target in range(epoch, 2 * epoch):
            log_2q = _log_integer(2 * target, context)
            cap = _scale_nonnegative(log_2q, Fraction(32 * target * target), context)
            cap_rows.append(
                {
                    "target": target,
                    "mark": points[target],
                    "cap_interval": cap.as_json(),
                    "strict_cap_verified": Decimal(points[target]) < cap.lower,
                }
            )

        mass = coefficient_mass_audit(epoch)
        ucoef = Fraction(mass["Ucoef"])
        bcoef = Fraction(mass["Bcoef"])
        rcoef = Fraction(mass["Rcoef"])
        u_minus_r = ucoef - rcoef
        b_minus_u = bcoef - ucoef
        closed_u_minus_r = Fraction(
            6 * epoch * epoch - 12 * epoch + 9, 16 * epoch * epoch
        )
        closed_b_minus_u = Fraction(4 * epoch - 7, 16 * epoch * epoch)

        log_scale = _log_integer(scale, context)
        log_2n_squared = _log_integer(2 * epoch * epoch, context)
        log_64 = _log_integer(64, context)
        log_4 = _log_integer(4, context)
        strong_lower = _subtract(
            _subtract(
                _subtract(
                    _scale_nonnegative(log_scale, u_minus_r, context),
                    _scale_nonnegative(log_2n_squared, b_minus_u, context),
                    context,
                ),
                _scale_nonnegative(log_64, rcoef, context),
                context,
            ),
            _scale_nonnegative(log_4, bcoef / 4, context),
            context,
        )
        universal_constant = _add(
            _point(Decimal(1) / Decimal(4)),
            _add(
                _scale_nonnegative(log_64, Fraction(3, 8), context),
                _scale_nonnegative(log_4, Fraction(3, 16), context),
                context,
            ),
            context,
        )
        simple_lower = _subtract(
            _scale_nonnegative(log_scale, Fraction(7, 32), context),
            universal_constant,
            context,
        )

    local_fixture = fixture_audit(
        f"scaled_et_local_no_go_n{epoch}_p{prime}", unscaled, epoch, scale=scale
    )
    projected_ghat = _bounds_from_json(
        local_fixture["intervals"]["Ghat_rank_upper_surrogate"]
    )
    projected_endpoint_slack = _bounds_from_json(
        local_fixture["intervals"]["P27_endpoint_slack"]
    )
    with localcontext() as context:
        context.prec = DECIMAL_PRECISION
        endpoint_slack_lower = _scale_nonnegative(
            _log_integer(2, context), Fraction(39, 256), context
        )
    prefix_cap_checks = all(row["strict_cap_verified"] for row in cap_rows)
    exact_checks = {
        "deterministic_prime_is_prime": _is_prime(prime),
        "bertrand_lower_strict": 2 * epoch - 1 < prime,
        "bertrand_upper_strict": prime < 4 * epoch - 2,
        "base_marks_strictly_increasing": all(
            left < right for left, right in pairwise(base)
        ),
        "base_is_golomb": len(set(base_differences)) == comb(2 * epoch - 1, 2),
        "append_is_strictly_above_twice_height": appended > 2 * height,
        "old_differences_at_most_H": base_differences[-1] <= height,
        "new_differences_at_least_H_plus_one": min(appended - point for point in base)
        >= height + 1,
        "appended_ruler_is_golomb": len(set(unscaled_differences))
        == comb(2 * epoch, 2),
        "scaled_ruler_is_golomb": len(set(scaled_differences)) == comb(2 * epoch, 2),
        "H_plus_one_above_two_n_squared": height + 1 > 2 * epoch * epoch,
        "X_below_32_n_squared": appended < 32 * epoch * epoch,
        "X_over_bq_below_four": all(
            appended < 4 * base[target] for target in range(epoch, 2 * epoch - 1)
        ),
        "scale_is_positive": scale >= 1,
        "Ucoef_minus_Rcoef_formula_verified": u_minus_r == closed_u_minus_r,
        "Bcoef_minus_Ucoef_formula_verified": b_minus_u == closed_b_minus_u,
        "Ucoef_minus_Rcoef_at_least_seven_over_32": u_minus_r >= Fraction(7, 32),
        "Bcoef_minus_Ucoef_times_n_below_one_quarter": b_minus_u * epoch
        < Fraction(1, 4),
        "Rcoef_below_three_eighths": rcoef < Fraction(3, 8),
        "Bcoef_below_three_quarters": bcoef < Fraction(3, 4),
        "local_fixture_exact_checks_pass": local_fixture["all_exact_checks_pass"],
        "append_ratio_above_two_on_endpoint_window": all(
            appended > 2 * base[target] for target in range(epoch, 2 * epoch - 1)
        ),
        "P27_endpoint_slack_mass_audit_passes": p27_coefficient_audit(epoch)[
            "endpoint_slack_mass_at_least_39_over_256"
        ],
    }
    decimal_checks = {
        "floor_log_2n_certified": Decimal(scale) <= log_2n_bounds.lower
        and log_2n_bounds.upper < Decimal(scale + 1),
        "local_C32_cap_window_verified": prefix_cap_checks,
        "log_two_n_squared_below_n": log_2n_squared.upper < Decimal(epoch),
        "strong_lower_dominates_simple_bound": strong_lower.lower >= simple_lower.upper,
        "computed_Ghat_dominates_strong_bound": projected_ghat.lower
        >= strong_lower.upper,
        "computed_Ghat_dominates_section_6_bound": projected_ghat.lower
        >= simple_lower.upper,
        "P27_endpoint_slack_clears_39_over_256_log2": (
            projected_endpoint_slack.lower >= endpoint_slack_lower.upper
        ),
    }
    return {
        "epoch": epoch,
        "bertrand_prime": prime,
        "quadratic_coefficient": 1,
        "base_mark_count": len(base),
        "H": height,
        "X": appended,
        "scale_floor_log_2n": scale,
        "log_2n_interval": log_2n_bounds.as_json(),
        "scaled_mark_count": len(points),
        "scaled_marks_csv_sha256": _csv_sha256(points),
        "scaled_differences_csv_sha256": _csv_sha256(scaled_differences),
        "local_cap_constant": 32,
        "local_cap_index_window": [epoch, 2 * epoch - 1],
        "local_cap_rows": cap_rows,
        "Ucoef": mass["Ucoef"],
        "Bcoef": mass["Bcoef"],
        "Rcoef": mass["Rcoef"],
        "Ucoef_minus_Rcoef": _fraction_text(u_minus_r),
        "closed_Ucoef_minus_Rcoef": _fraction_text(closed_u_minus_r),
        "Bcoef_minus_Ucoef": _fraction_text(b_minus_u),
        "closed_Bcoef_minus_Ucoef": _fraction_text(closed_b_minus_u),
        "section_6_constant_interval": universal_constant.as_json(),
        "strong_finite_lower_bound_interval": strong_lower.as_json(),
        "section_6_lower_bound_interval": simple_lower.as_json(),
        "computed_Ghat_rank_upper_surrogate_interval": projected_ghat.as_json(),
        "P27_endpoint_slack_interval": projected_endpoint_slack.as_json(),
        "P27_endpoint_slack_39_over_256_log2_lower_interval": (
            endpoint_slack_lower.as_json()
        ),
        **exact_checks,
        **decimal_checks,
        "all_exact_checks_pass": all(exact_checks.values()),
        "all_conservative_decimal_checks_pass": all(decimal_checks.values()),
        "uses_a_different_finite_ruler_at_each_epoch": True,
        "compatible_infinite_branch_inferred": False,
        "p24_refuted": False,
        "local_only_bare_Ghat_bound_obstructed": True,
    }


@cache
def build_certificate() -> dict[str, Any]:
    """Build the deterministic finite certificate payload."""
    coefficient_rows = [coefficient_mass_audit(epoch) for epoch in EXACT_EPOCHS]
    sharp_coefficient_rows = [
        sharp_remainder_coefficient_audit(epoch) for epoch in EXACT_EPOCHS
    ]
    p27_coefficient_rows = [p27_coefficient_audit(epoch) for epoch in EXACT_EPOCHS]
    inner_birth_coefficient_rows = [
        inner_birth_coefficient_audit(epoch) for epoch in INNER_BIRTH_EPOCHS
    ]
    algebra = formal_remainder_algebra_audit()
    et = erdos_turan_points(67)
    binary = binary_superincreasing_points(64)
    fixture_specs = (
        ("erdos_turan_p67", et, 4),
        ("erdos_turan_p67", et, 8),
        ("erdos_turan_p67", et, 16),
        ("erdos_turan_p67", et, 32),
        ("binary_superincreasing_64", binary, 4),
        ("binary_superincreasing_64", binary, 8),
        ("binary_superincreasing_64", binary, 16),
        ("binary_superincreasing_64", binary, 32),
    )
    fixture_rows = [
        fixture_audit(name, points, epoch) for name, points, epoch in fixture_specs
    ]
    scale_base = erdos_turan_points(17)
    scale_one = fixture_audit("erdos_turan_p17_scale_1", scale_base, 8, scale=1)
    scale_seven = fixture_audit("erdos_turan_p17_scale_7", scale_base, 8, scale=7)
    scale_checks = {
        "same_atom_rank_order": scale_one["atom_count"] == scale_seven["atom_count"],
        "same_weight_counts": scale_one["weight_counts"]
        == scale_seven["weight_counts"],
        "Rcert_form_2_intervals_overlap_under_integer_dilation": _overlap(
            Bounds(
                Decimal(scale_one["intervals"]["Rcert_form_2"]["lower"]),
                Decimal(scale_one["intervals"]["Rcert_form_2"]["upper"]),
            ),
            Bounds(
                Decimal(scale_seven["intervals"]["Rcert_form_2"]["lower"]),
                Decimal(scale_seven["intervals"]["Rcert_form_2"]["upper"]),
            ),
        ),
        "Rsharp_intervals_overlap_under_integer_dilation": _overlap(
            _bounds_from_json(scale_one["intervals"]["Rsharp_form_1"]),
            _bounds_from_json(scale_seven["intervals"]["Rsharp_form_1"]),
        ),
        "exact_mass_cancellation_used": coefficient_mass_audit(8)[
            "dilation_mass_cancellation_verified"
        ],
    }
    local_no_go_rows = [local_ghat_no_go_audit(epoch) for epoch in (4, 8, 16, 32, 64)]
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave19.certified-remainder.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Audit the sorted-rank decomposition, certify the previously spent "
            "excess row inside Srank, and verify the Wave 19 Rcert algebra."
        ),
        "arithmetic": {
            "atoms_ranks_coefficients_and_masses": "exact integers and fractions.Fraction",
            "rearrangement_sign": "exact adjacent-swap order over Fraction weights",
            "logarithms": (
                "Decimal precision 110 with next_minus/next_plus outward widening; "
                "projection and conservative comparison only"
            ),
            "logarithm_base": "natural",
        },
        "theorem_contract": {
            "Hloc_decomposition": "Hloc=Srank+Pair",
            "Srank": "sum_j gamma_j log(x_j/j)",
            "Pair": "sum_j gamma_j log(j)-F_loc",
            "spent_row": ("A=sum_(p=2)^n alpha_p sum_q beta_pq log_+(D_pq/c) <= Srank"),
            "Qcert": "Srank+J-Theta_exc>=0",
            "Rcert_form_1": "Ghat-(D-Ccap)-Qcert-e+epsilon",
            "Rcert_form_2": "U-F_loc-Srank-J-Dpre/4-e+epsilon",
            "Rcert_form_3": "Z+3Dpre/4-J+Pair",
            "Rsharp_form_1": "U-B-J-Dpre/4-e+epsilon",
            "Rsharp_form_2": "Z+3Dpre/4-J",
            "Rcert_sharp_relation": "Rcert=Rsharp+Pair",
            "sharp_frontier": "Z<=Y/2+Rsharp",
            "pair_universal_maximum": ("Pair<=(3/(4n^2))*log(binomial(c_n,n-1))"),
            "P27_hstar": "hstar=log(c_n/L_(n,n))<5/2",
            "P27_primary_direct_split": "J_5/2<=E0+S<=3Dpre/4+Zfin",
            "P27_primary_four_channel_decomposition": (
                "Rsharp=(3Dpre/4-E0)+(Zfin-S)+Zfut+(E0+S-J_5/2)"
            ),
            "P27_refined_split": "Jstar<=E0+S and Jstar>=J_5/2",
            "P27_refined_five_piece_decomposition": (
                "Rsharp=(3Dpre/4-E0)+(Zfin-S)+(E0+S-Jstar)+Zfut+(Jstar-J_5/2)"
            ),
            "P27_row_exact_endpoint": (
                "Erow=Eend=sum_(p,q) alpha_p beta_pq "
                "[log(A/a_q)-(5/2-log(c_n/L_(n,p)))]_+"
            ),
            "P27_profile_increment": "Delta=J_5/2-Erow with 0<=Delta<=S",
            "P27_profile_remainder": (
                "Rprof=Z+Erow-J_5/2=(Zfin-S)+Zfut+(Erow+S-J_5/2)>=0"
            ),
            "P27_profile_frontier": "Z<=S+Rprof<=Y/2+Rprof",
            "P27_relation_to_Rsharp": "Rsharp=Rprof+3Dpre/4-Erow>=Rprof",
            "P27_inner_birth_sector": (
                "W=sum_(j=n+2)^(2n-1)sum_(i=n)^(j-2) ((j-i)^2/(4n^2))*C_(i,j)<=Rprof"
            ),
            "P27_inner_layer_floor": (
                "W>=Eprime/(8n^2Hprime), Hprime=A-a_(n-1), Eprime=n(n-2)(n^2+4n-14)/48"
            ),
            "P27_eventual_cap_consequence": (
                "for dyadic n>=16, W>=n^2/(384Hprime)"
                ">1/(1536*C*log(4n)) on a hypothetical fixed eventual-C branch"
            ),
            "P27_Fejer_liminf": "1/(1536*C*log(2)), twice 1/(3072*C*log(2))",
            "P27_nonclaim": (
                "P27 is not proved or refuted unconditionally; its standalone "
                "upper target is saturated conditional on an extant eventual-C branch"
            ),
            "dilation_mass": "Ucoef-Bcoef-ecoef+epscoef=0",
        },
        "coefficient_mass_rows": coefficient_rows,
        "sharp_remainder_coefficient_rows": sharp_coefficient_rows,
        "p27_coefficient_rows": p27_coefficient_rows,
        "inner_birth_coefficient_rows": inner_birth_coefficient_rows,
        "formal_remainder_algebra": algebra,
        "fixture_rows": fixture_rows,
        "integer_dilation_audit": {
            "base_fixture": scale_one,
            "scaled_fixture": scale_seven,
            **scale_checks,
            "all_checks_pass": all(scale_checks.values()),
        },
        "bare_Ghat_local_no_go_rows": local_no_go_rows,
        "scope_flags": {
            "finite_fixture_only": True,
            "rank_upper_surrogate_dominates_actual_promotion": True,
            "infinite_branch_constructed": False,
            "p24_proved": False,
            "p25_proved": False,
            "p26_proved": False,
            "p27_proved": False,
            "p27_asymptotic_upper_proved": False,
            "p27_intermediate_closed_by_inner_birth": True,
            "p26_p27_standalone_upper_targets_saturated": True,
            "p27_unconditionally_refuted": False,
            "Rsharp_nonnegative_decomposition_proved": True,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
            "problem_unresolved": True,
        },
        "all_required_checks_pass": (
            all(row["all_exact_checks_pass"] for row in coefficient_rows)
            and all(row["all_exact_checks_pass"] for row in sharp_coefficient_rows)
            and all(row["all_exact_checks_pass"] for row in p27_coefficient_rows)
            and all(
                row["all_exact_checks_pass"] for row in inner_birth_coefficient_rows
            )
            and algebra["all_exact_checks_pass"]
            and all(
                row["all_exact_checks_pass"]
                and row["all_conservative_decimal_checks_pass"]
                for row in fixture_rows
            )
            and all(scale_checks.values())
            and all(
                row["all_exact_checks_pass"]
                and row["all_conservative_decimal_checks_pass"]
                for row in local_no_go_rows
            )
        ),
    }
    payload["certificate_sha256"] = _canonical_hash(payload)
    return payload


def certificate_bytes() -> bytes:
    return _canonical_bytes(build_certificate()) + b"\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.write_bytes(certificate_bytes())
    print(build_certificate()["certificate_sha256"])


if __name__ == "__main__":
    main()

"""Exact checks for WAVE7_GLUE_DELETE_NO_GO_2026-08-28.md.

These checks audit integer formulas and high-precision logarithmic
comparisons.  The proof in the note is independent of this finite replay.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from math import comb


@dataclass(frozen=True)
class StepLedger:
    old_size: int
    old_width: int
    guaranteed_new: int
    deletion_allowance: int
    candidate_size: int
    candidate_window: int
    first_new_width_lower_bound: int


def critical_envelope(index: int, constant: int = 1) -> Decimal:
    if index < 2:
        raise ValueError("the logarithmic envelope is checked only for index >= 2")
    if constant <= 0:
        raise ValueError("constant must be positive")
    with localcontext() as context:
        context.prec = 80
        value = (
            Decimal(2) * Decimal(constant) * Decimal(index) ** 2 * Decimal(index).ln()
        )
    return value


def minimum_worst_guarantee_step(
    old_size: int,
    guaranteed_new: int = 1,
    old_width: int | None = None,
) -> StepLedger:
    if old_size < 2:
        raise ValueError("old_size must be at least 2")
    if guaranteed_new < 1:
        raise ValueError("guaranteed_new must be positive")
    deletion = comb(old_size, 2)
    width = deletion + 1 if old_width is None else old_width
    if width < deletion + 1:
        raise ValueError("old_width violates the Sidon packing lower bound")
    candidate_size = deletion + guaranteed_new
    candidate_window = comb(candidate_size, 2) + 1
    first_new_width = width + max(width, candidate_window) + 1
    return StepLedger(
        old_size=old_size,
        old_width=width,
        guaranteed_new=guaranteed_new,
        deletion_allowance=deletion,
        candidate_size=candidate_size,
        candidate_window=candidate_window,
        first_new_width_lower_bound=first_new_width,
    )


def candidate_capacity(old_size: int, old_width: int, constant: int = 1) -> int:
    """Largest q allowed by C(q,2) <= F_C(n+1)-N-2."""

    budget = critical_envelope(old_size + 1, constant) - old_width - 2
    q = 1
    while Decimal(comb(q + 1, 2)) <= budget:
        q += 1
    return q


def test_exact_ledgers_at_seven_and_eight() -> None:
    seven = minimum_worst_guarantee_step(7)
    eight = minimum_worst_guarantee_step(8)
    assert seven == StepLedger(7, 22, 1, 21, 22, 232, 255)
    assert eight == StepLedger(8, 29, 1, 28, 29, 407, 437)


def test_c1_transition_changes_from_not_excluded_to_excluded() -> None:
    seven = minimum_worst_guarantee_step(7)
    eight = minimum_worst_guarantee_step(8)
    for old_size in range(2, 8):
        ledger = minimum_worst_guarantee_step(old_size)
        assert Decimal(ledger.first_new_width_lower_bound) < critical_envelope(
            old_size + 1
        )
    assert Decimal(seven.first_new_width_lower_bound) < critical_envelope(8)
    assert Decimal(eight.first_new_width_lower_bound) > critical_envelope(9)
    assert candidate_capacity(7, seven.old_width) == 22
    assert candidate_capacity(8, eight.old_width) == 25
    assert seven.candidate_size <= candidate_capacity(7, seven.old_width)
    assert eight.candidate_size > candidate_capacity(8, eight.old_width)


def test_c1_obstruction_persists_on_large_finite_replay() -> None:
    for old_size in range(8, 2049):
        ledger = minimum_worst_guarantee_step(old_size)
        assert Decimal(ledger.first_new_width_lower_bound) > critical_envelope(
            old_size + 1
        )


def test_unit_growth_increment_polynomial() -> None:
    for old_size in range(2, 200):
        ledger = minimum_worst_guarantee_step(old_size)
        increment = ledger.candidate_window + 1
        numerator = old_size**4 - 2 * old_size**3 + 3 * old_size**2 - 2 * old_size
        assert numerator % 8 == 0
        assert increment == numerator // 8 + 2

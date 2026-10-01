"""Exact coefficient audit for the Wave 10 laminar shell analysis.

The analytic note uses the birth-shell Abel coefficients from Wave 9 at
``n = 2m``.  This module independently evaluates the four indicator terms,
checks the claimed sign support, and exposes the negative-bulk coefficient
multiset used in the hereditary logarithmic rearrangement inequality.

Floating logarithms are used only to inspect the asymptotic rearrangement
floor.  All coefficient identities and masses are represented by
``fractions.Fraction``.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable
from fractions import Fraction
from math import log


def shell_coefficient(m: int, p: int, q: int) -> Fraction:
    """Return the exact Abel coefficient of ``log D[p,q]`` for ``n=2m``."""
    if m < 4:
        raise ValueError("m must be at least four")
    g = 2 * m - 1
    if not (1 <= p <= q <= g):
        raise ValueError("invalid interval")
    length = q - p + 1

    def weight(rank: int) -> Fraction:
        return Fraction(rank * rank, 4 * m * m)

    value = Fraction(0)
    if length >= 2 and m - 1 <= q <= g - 1:
        value += weight(length)
    if p >= 2 and length >= 2 and m <= q <= g:
        value += weight(length)
    if p >= 2 and m - 1 <= q <= g - 1:
        value -= weight(length + 1)
    if length >= 3 and m <= q <= g:
        value -= weight(length - 1)
    return value


def coefficient_partition(m: int) -> dict[str, dict[tuple[int, int], Fraction]]:
    """Partition nonzero coefficients into left, suffix, full, and bulk."""
    g = 2 * m - 1
    result: dict[str, dict[tuple[int, int], Fraction]] = {
        "left_positive": {},
        "suffix_positive": {},
        "full_negative": {},
        "bulk_negative": {},
    }
    for p in range(1, g + 1):
        for q in range(p, g + 1):
            coefficient = shell_coefficient(m, p, q)
            if coefficient == 0:
                continue
            if p == 1 and m - 1 <= q <= g - 1:
                bucket = "left_positive"
            elif q == g and 2 <= p <= g - 1:
                bucket = "suffix_positive"
            elif (p, q) == (1, g):
                bucket = "full_negative"
            elif p >= 2 and m - 1 <= q <= g - 1:
                bucket = "bulk_negative"
            else:
                raise AssertionError(f"unexpected coefficient support {(p, q)}")
            result[bucket][(p, q)] = coefficient
    return result


def expected_bulk_weights(m: int) -> Counter[Fraction]:
    """Return the closed-form absolute negative-bulk coefficient multiset."""
    weights: list[Fraction] = []
    weights.extend(Fraction(2 * length + 1, 4 * m * m) for length in range(2, m - 1))
    weights.extend([Fraction(1, m * m)] * m)
    weights.extend([Fraction(1, 2 * m * m)] * ((m - 1) * (3 * m - 8) // 2))
    weights.extend([Fraction(1, 4 * m * m)] * (m - 1))
    return Counter(weights)


def bulk_weights(m: int) -> list[Fraction]:
    """Return the directly enumerated absolute negative-bulk weights."""
    partition = coefficient_partition(m)
    return [-value for value in partition["bulk_negative"].values()]


def rearrangement_floor(scales: Iterable[int]) -> float:
    """Return ``sum beta[r] log(r)`` after globally sorting all bulk weights."""
    weights = sorted(
        (weight for m in scales for weight in bulk_weights(m)), reverse=True
    )
    return sum(float(weight) * log(rank) for rank, weight in enumerate(weights, 1))


def entropy_rank_upper(scales: Iterable[int]) -> float:
    """Return the analytic comparison ``sum beta log(4/beta)``."""
    return sum(
        float(weight) * log(4 / float(weight))
        for m in scales
        for weight in bulk_weights(m)
    )


def audit_scale(m: int) -> dict[str, object]:
    """Build a small human-readable audit record for one dyadic scale."""
    partition = coefficient_partition(m)
    theta = Fraction((m - 1) ** 2, m * m)
    return {
        "m": m,
        "positive_mass": str(
            sum(partition["left_positive"].values())
            + sum(partition["suffix_positive"].values())
        ),
        "full_negative_mass": str(-sum(partition["full_negative"].values())),
        "bulk_negative_mass": str(-sum(partition["bulk_negative"].values())),
        "expected_theta": str(theta),
        "bulk_count": len(partition["bulk_negative"]),
        "floor": rearrangement_floor((m,)),
        "entropy_rank_upper": entropy_rank_upper((m,)),
    }

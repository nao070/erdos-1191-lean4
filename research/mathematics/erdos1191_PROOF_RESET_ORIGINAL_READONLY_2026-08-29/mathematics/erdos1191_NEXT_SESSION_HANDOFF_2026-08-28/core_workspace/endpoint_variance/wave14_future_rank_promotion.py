"""Finite combinatorial audits for the Wave 14 future-rank promotion lemma.

The rigorous theorem is first finite and contains no asymptotic inference.
For an integer Golomb ruler, an old difference ``d``, and a future block of
``N`` marks, every pair of future marks in the same spatial bin of width
``d`` is a distinct new difference strictly below ``d``.  Cauchy--Schwarz
then supplies the exact rational lower bound implemented here.

The eventual ``O(n^2 log n)`` consequence and its constants are proved in
``WAVE14_FUTURE_RANK_PROMOTION_2026-08-29.md``.  This module is only a finite
oracle; a finite fixture never certifies an infinite critical branch.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from math import floor, log


def _validated_golomb_prefix(
    points: Sequence[int], required_marks: int
) -> tuple[int, ...]:
    marks = tuple(points)
    if required_marks < 2 or len(marks) < required_marks:
        raise ValueError("the requested prefix must contain at least two marks")
    prefix = marks[:required_marks]
    if (
        prefix[0] != 0
        or prefix != tuple(sorted(set(prefix)))
        or any(not isinstance(mark, int) for mark in prefix)
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    differences = [
        prefix[right] - prefix[left]
        for left in range(required_marks)
        for right in range(left + 1, required_marks)
    ]
    if len(differences) != len(set(differences)):
        raise ValueError("the requested prefix is not a Golomb ruler")
    return prefix


def difference_rank(points: Sequence[int], mark_count: int, threshold: int) -> int:
    """Count positive differences at most ``threshold`` in a prefix."""
    if threshold < 1:
        raise ValueError("threshold must be positive")
    marks = _validated_golomb_prefix(points, mark_count)
    return sum(
        marks[right] - marks[left] <= threshold
        for left in range(mark_count)
        for right in range(left + 1, mark_count)
    )


def logarithmic_block_size(threshold: int) -> int:
    """Return floor(d / log(d)^2), using the natural logarithm."""
    if threshold <= 1:
        raise ValueError("threshold must exceed one")
    return floor(threshold / log(threshold) ** 2)


@dataclass(frozen=True)
class FutureRankPromotionAudit:
    old_mark_count: int
    future_mark_count: int
    threshold: int
    occupied_bin_count: int
    same_bin_pair_count: int
    cauchy_pair_lower: Fraction
    old_rank: int
    extended_rank: int
    observed_promotion: int
    same_bin_differences_are_distinct: bool
    same_bin_differences_are_new: bool
    same_bin_differences_are_strictly_below_threshold: bool
    observed_promotion_dominates_same_bin_pairs: bool
    same_bin_pairs_dominate_cauchy_lower: bool


def future_rank_promotion_audit(
    points: Sequence[int],
    old_mark_count: int,
    threshold: int,
    *,
    future_mark_count: int | None = None,
) -> FutureRankPromotionAudit:
    """Audit the exact finite spatial-bin promotion inequality.

    The old prefix consists of indices ``0,...,L-1`` and the disjoint future
    block consists of ``L,...,L+N-1``.  Bins are the half-open translates
    ``[a_L+qd, a_L+(q+1)d)``.  Hence a same-bin difference is strictly below
    ``d``, including when marks lie on bin boundaries.
    """
    if old_mark_count < 2:
        raise ValueError("old_mark_count must be at least two")
    if threshold <= 1:
        raise ValueError("threshold must exceed one")
    if future_mark_count is None:
        future_mark_count = logarithmic_block_size(threshold)
    if future_mark_count < 2:
        raise ValueError("future_mark_count must be at least two")

    total = old_mark_count + future_mark_count
    marks = _validated_golomb_prefix(points, total)
    old_differences = {
        marks[right] - marks[left]
        for left in range(old_mark_count)
        for right in range(left + 1, old_mark_count)
    }
    if threshold not in old_differences:
        raise ValueError("threshold must already be an old-prefix difference")

    origin = marks[old_mark_count]
    occupancies = Counter(
        (marks[index] - origin) // threshold for index in range(old_mark_count, total)
    )
    occupied_bin_count = len(occupancies)
    same_bin_pair_count = sum(
        occupancy * (occupancy - 1) // 2 for occupancy in occupancies.values()
    )
    cauchy_pair_lower = Fraction(
        future_mark_count * future_mark_count, occupied_bin_count
    )
    cauchy_pair_lower = (cauchy_pair_lower - future_mark_count) / 2

    same_bin_differences: list[int] = []
    for left in range(old_mark_count, total):
        left_bin = (marks[left] - origin) // threshold
        for right in range(left + 1, total):
            if (marks[right] - origin) // threshold == left_bin:
                same_bin_differences.append(marks[right] - marks[left])

    old_rank = sum(value <= threshold for value in old_differences)
    extended_differences = {
        marks[right] - marks[left]
        for left in range(total)
        for right in range(left + 1, total)
    }
    extended_rank = sum(value <= threshold for value in extended_differences)
    observed_promotion = extended_rank - old_rank

    return FutureRankPromotionAudit(
        old_mark_count=old_mark_count,
        future_mark_count=future_mark_count,
        threshold=threshold,
        occupied_bin_count=occupied_bin_count,
        same_bin_pair_count=same_bin_pair_count,
        cauchy_pair_lower=cauchy_pair_lower,
        old_rank=old_rank,
        extended_rank=extended_rank,
        observed_promotion=observed_promotion,
        same_bin_differences_are_distinct=(
            len(same_bin_differences) == len(set(same_bin_differences))
        ),
        same_bin_differences_are_new=old_differences.isdisjoint(same_bin_differences),
        same_bin_differences_are_strictly_below_threshold=all(
            0 < value < threshold for value in same_bin_differences
        ),
        observed_promotion_dominates_same_bin_pairs=(
            observed_promotion >= same_bin_pair_count
        ),
        same_bin_pairs_dominate_cauchy_lower=(same_bin_pair_count >= cauchy_pair_lower),
    )


def macroscopic_suffix_weight(epoch: int) -> Fraction:
    """Sum Wave 13 terminal-suffix weights for 2 <= p <= m."""
    if epoch < 2:
        raise ValueError("epoch must be at least two")
    return Fraction((epoch - 1) * (9 * epoch - 11), 16 * epoch * epoch)

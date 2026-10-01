"""Same-modulus prefix variance and the minimal doubled-prefix obstruction."""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from fractions import Fraction

from endpoint_variance import crossing_loads, variance
from sidon_block_variance import is_golomb_ruler


def _validated_points(points: Iterable[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if len(marks) < 2 or tuple(sorted(marks)) != marks or len(set(marks)) != len(marks):
        raise ValueError("points must be a strictly increasing sequence of length at least two")
    return marks


def same_modulus_prefix_variance(
    points: Iterable[int], prefix_count: int, modulus: int
) -> Fraction:
    """Evaluate a left prefix at one modulus containing the full point set."""
    marks = _validated_points(points)
    if not isinstance(prefix_count, int) or not isinstance(modulus, int):
        raise TypeError("prefix_count and modulus must be integers")
    if prefix_count < 2 or prefix_count > len(marks):
        raise ValueError("prefix_count must lie between two and the full mark count")
    if modulus <= marks[-1] - marks[0]:
        raise ValueError("the modulus must exceed the full diameter")

    total = 0
    square_total = 0
    for index in range(1, prefix_count):
        gap = marks[index] - marks[index - 1]
        level = index * (prefix_count - index)
        total += gap * level
        square_total += gap * level * level
    return Fraction(square_total, modulus) - Fraction(total * total, modulus * modulus)


@dataclass(frozen=True)
class PrefixMonotonicityComparison:
    modulus: int
    prefix_count: int
    prefix_variance: Fraction
    full_variance: Fraction

    @property
    def change(self) -> Fraction:
        return self.full_variance - self.prefix_variance


def doubled_prefix_comparison(
    points: Iterable[int], prefix_count: int, modulus: int
) -> PrefixMonotonicityComparison:
    """Compare ``A_r`` and ``A_{2r}`` at the same containing modulus."""
    marks = _validated_points(points)
    if len(marks) != 2 * prefix_count:
        raise ValueError("the full set must contain exactly twice the prefix count")
    prefix_variance = same_modulus_prefix_variance(marks, prefix_count, modulus)
    full_variance = same_modulus_prefix_variance(marks, 2 * prefix_count, modulus)
    return PrefixMonotonicityComparison(
        modulus=modulus,
        prefix_count=prefix_count,
        prefix_variance=prefix_variance,
        full_variance=full_variance,
    )


def four_mark_full_variance_lower_bound(modulus: int) -> Fraction:
    """Sharp lower bound for any four increasing marks in a containing modulus."""
    if not isinstance(modulus, int) or modulus < 4:
        raise ValueError("modulus must be an integer at least four")
    return Fraction(10 * modulus - 4, modulus * modulus)


def prefix_monotonicity_counterfamily(modulus: int) -> tuple[int, int, int, int]:
    """Return ``{0,ceil(N/2),ceil(N/2)+1,N-1}`` for ``N >= 40``."""
    if not isinstance(modulus, int) or modulus < 40:
        raise ValueError("the certified Sidon counterfamily starts at N=40")
    midpoint = (modulus + 1) // 2
    points = (0, midpoint, midpoint + 1, modulus - 1)
    if not is_golomb_ruler(points):
        raise AssertionError("counterfamily unexpectedly failed the Sidon check")
    comparison = doubled_prefix_comparison(points, 2, modulus)
    if comparison.change >= 0:
        raise AssertionError("counterfamily did not decrease the variance")
    return points


def direct_same_modulus_prefix_variance(
    points: Iterable[int], prefix_count: int, modulus: int
) -> Fraction:
    """Independent literal cyclic-arc oracle."""
    marks = _validated_points(points)
    if modulus <= marks[-1] - marks[0]:
        raise ValueError("the modulus must exceed the full diameter")
    return variance(crossing_loads(marks[:prefix_count], modulus))

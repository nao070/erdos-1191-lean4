"""Exact cover-projection identity for cyclic interval loads.

This module separates a fine ``qN`` interval load into its conditional
expectation modulo ``N`` and a nonnegative fibre innovation.  It also exposes
the obstruction caused by edges born between the two moduli.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from fractions import Fraction

from endpoint_variance import variance


Pair = tuple[int, int]


def _validated_pairs(pairs: Iterable[Pair], upper_distance: int | None = None) -> tuple[Pair, ...]:
    result = tuple(pairs)
    for pair in result:
        if len(pair) != 2 or any(not isinstance(value, int) for value in pair):
            raise TypeError("pairs must be integer (left, right) tuples")
        if pair[1] <= pair[0]:
            raise ValueError("pairs must be positively oriented")
        if upper_distance is not None and pair[1] - pair[0] >= upper_distance:
            raise ValueError("every pair distance must be below q*N")
    return result


def pair_arc_loads(pairs: Iterable[Pair], modulus: int) -> tuple[int, ...]:
    """Cyclic multiplicity load of the walk ``left+1,...,right`` modulo ``M``.

    A walk longer than ``M`` covers a residue more than once.  The cover
    theorems call this function only after enforcing their stated distance
    bounds; the public helper deliberately preserves multiplicity for longer
    walks.
    """
    if not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    edges = _validated_pairs(pairs)
    loads = [0] * modulus
    for left, right in edges:
        for step in range(1, right - left + 1):
            loads[(left + step) % modulus] += 1
    return tuple(loads)


def residual_arc_loads(pairs: Iterable[Pair], modulus: int, cover: int) -> tuple[int, ...]:
    """Residual modulo-``N`` arcs after writing each distance as ``kN+s``."""
    if not isinstance(modulus, int) or not isinstance(cover, int):
        raise TypeError("modulus and cover must be integers")
    if modulus < 2 or cover < 2:
        raise ValueError("modulus and cover must both be at least 2")
    edges = _validated_pairs(pairs, cover * modulus)
    residuals: list[Pair] = []
    for left, right in edges:
        remainder = (right - left) % modulus
        if remainder:
            residuals.append((left, left + remainder))
    return pair_arc_loads(residuals, modulus)


@dataclass(frozen=True)
class CoverVarianceIdentity:
    modulus: int
    cover: int
    fine_variance: Fraction
    residual_variance: Fraction
    innovation: Fraction
    scaled_fine_variance: Fraction


@dataclass(frozen=True)
class EdgeCoordinateBudget:
    edge_count: int
    trace: Fraction
    synthesis_norm_squared: Fraction
    product: Fraction
    universal_lower_bound: Fraction


def cover_variance_identity(
    pairs: Iterable[Pair], modulus: int, cover: int
) -> CoverVarianceIdentity:
    """Evaluate and certify ``q^2 V_{qN} = V_N(R) + I_{N,q}``."""
    if not isinstance(modulus, int) or not isinstance(cover, int):
        raise TypeError("modulus and cover must be integers")
    if modulus < 2 or cover < 2:
        raise ValueError("modulus and cover must both be at least 2")
    edges = _validated_pairs(pairs, cover * modulus)
    fine = pair_arc_loads(edges, cover * modulus)
    residual = residual_arc_loads(edges, modulus, cover)
    fine_variance = variance(fine)
    residual_variance = variance(residual)

    innovation_sum = 0
    for residue in range(modulus):
        fibre_sum = sum(fine[residue + lift * modulus] for lift in range(cover))
        for lift in range(cover):
            innovation_sum += (cover * fine[residue + lift * modulus] - fibre_sum) ** 2
    innovation = Fraction(innovation_sum, cover * modulus)
    scaled_fine_variance = cover**2 * fine_variance
    if innovation < 0 or scaled_fine_variance != residual_variance + innovation:
        raise AssertionError("cover variance identity failed")
    return CoverVarianceIdentity(
        modulus=modulus,
        cover=cover,
        fine_variance=fine_variance,
        residual_variance=residual_variance,
        innovation=innovation,
        scaled_fine_variance=scaled_fine_variance,
    )


def frozen_cover_variance_identity(
    pairs: Iterable[Pair], modulus: int, cover: int
) -> CoverVarianceIdentity:
    """Specialize the identity to a frozen pair multiset with distances below ``N``."""
    edges = _validated_pairs(pairs, modulus)
    result = cover_variance_identity(edges, modulus, cover)
    if result.residual_variance != variance(pair_arc_loads(edges, modulus)):
        raise AssertionError("frozen residual did not equal the coarse load")
    return result


def old_birth_dichotomy(
    old_pairs: Iterable[Pair], birth_pairs: Iterable[Pair], modulus: int, cover: int
) -> tuple[Fraction, Fraction]:
    """Return both sides of ``V(old)/2 <= q^2 V(fine) + V(birth residual)``."""
    old = _validated_pairs(old_pairs, modulus)
    birth = _validated_pairs(birth_pairs, cover * modulus)
    if any(right - left < modulus for left, right in birth):
        raise ValueError("birth-pair distances must lie in [N,qN)")
    old_variance = variance(pair_arc_loads(old, modulus))
    combined = (*old, *birth)
    fine_variance = variance(pair_arc_loads(combined, cover * modulus))
    birth_variance = variance(residual_arc_loads(birth, modulus, cover))
    left_side = old_variance / 2
    right_side = cover**2 * fine_variance + birth_variance
    if left_side > right_side:
        raise AssertionError("old/birth energy dichotomy failed")
    return left_side, right_side


def edge_coordinate_budget(
    differences: Iterable[int], modulus: int, weights: Iterable[Fraction | int] | None = None
) -> EdgeCoordinateBudget:
    """Audit a diagonal Hilbert-coordinate representation of centered arcs.

    For coordinate weight ``w_d``, the trace is
    ``sum w_d*d*(N-d)/N^2`` and the squared synthesis norm is ``sum 1/w_d``.
    Distinct differences force their product to be at least ``P^3/(9N)``.
    """
    if not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    distances = tuple(differences)
    if any(not isinstance(distance, int) for distance in distances):
        raise TypeError("differences must be integers")
    if any(distance <= 0 or distance >= modulus for distance in distances):
        raise ValueError("differences must lie strictly between 0 and N")
    if len(distances) != len(set(distances)):
        raise ValueError("the trace lower bound requires distinct differences")
    if weights is None:
        exact_weights = (Fraction(1),) * len(distances)
    else:
        exact_weights = tuple(Fraction(weight) for weight in weights)
        if len(exact_weights) != len(distances):
            raise ValueError("weights and differences must have the same length")
        if any(weight <= 0 for weight in exact_weights):
            raise ValueError("coordinate weights must be positive")

    variances = tuple(
        Fraction(distance * (modulus - distance), modulus * modulus)
        for distance in distances
    )
    trace = sum((weight * value for weight, value in zip(exact_weights, variances)), Fraction(0))
    synthesis = sum((1 / weight for weight in exact_weights), Fraction(0))
    product = trace * synthesis
    edge_count = len(distances)
    lower_bound = Fraction(edge_count**3, 9 * modulus)
    if product < lower_bound:
        raise AssertionError("universal edge-coordinate trace lower bound failed")
    return EdgeCoordinateBudget(
        edge_count=edge_count,
        trace=trace,
        synthesis_norm_squared=synthesis,
        product=product,
        universal_lower_bound=lower_bound,
    )


def vector_cover_increment_trace(
    differences: Iterable[int], modulus: int, cover: int, level: int = 0,
    weights: Iterable[Fraction | int] | None = None,
) -> Fraction:
    """Exact Hilbert martingale increment trace at cover level ``level``."""
    if not isinstance(cover, int) or not isinstance(level, int):
        raise TypeError("cover and level must be integers")
    if cover < 2 or level < 0:
        raise ValueError("cover must be at least 2 and level nonnegative")
    distances = tuple(differences)
    exact_weights = (
        (Fraction(1),) * len(distances)
        if weights is None
        else tuple(Fraction(weight) for weight in weights)
    )
    edge_coordinate_budget(distances, modulus, exact_weights)
    weighted_length = sum(
        (weight * distance for weight, distance in zip(exact_weights, distances)),
        Fraction(0),
    )
    return Fraction((cover - 1) * cover**level, modulus) * weighted_length


def vector_discounted_cover_trace(
    differences: Iterable[int], modulus: int, cover: int,
    weights: Iterable[Fraction | int] | None = None,
) -> Fraction:
    """Infinite ``q^(-2l)``-discounted vector square-function trace."""
    if not isinstance(cover, int) or cover < 2:
        raise ValueError("cover must be an integer at least 2")
    distances = tuple(differences)
    exact_weights = (
        (Fraction(1),) * len(distances)
        if weights is None
        else tuple(Fraction(weight) for weight in weights)
    )
    edge_coordinate_budget(distances, modulus, exact_weights)
    weighted_length = sum(
        (weight * distance for weight, distance in zip(exact_weights, distances)),
        Fraction(0),
    )
    return Fraction(cover, modulus) * weighted_length

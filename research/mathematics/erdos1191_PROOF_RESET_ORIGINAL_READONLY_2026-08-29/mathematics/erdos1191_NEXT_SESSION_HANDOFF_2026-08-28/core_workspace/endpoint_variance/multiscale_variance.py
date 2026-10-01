"""Exact pair-pair kernels and fixed-modulus prefix identities.

The functions here keep the offset variable.  They expose the quartic
expansion

    N Var(C_N) = sum_{p,q} K_N(p,q)

for the cyclic bad-offset arcs of the short pairs.  They also record a simple
second-difference identity for a chain of prefixes inside one fixed modulus.
All public arithmetic is integral or :class:`fractions.Fraction` based.
"""
from __future__ import annotations

from collections.abc import Iterable
from fractions import Fraction
from itertools import product

from endpoint_variance import crossing_loads, short_pair_edges


def _validated_modulus(modulus: int) -> int:
    if not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    return modulus


def _validated_arc(start: int, length: int, modulus: int) -> tuple[int, int, int]:
    n = _validated_modulus(modulus)
    if not isinstance(start, int) or not isinstance(length, int):
        raise TypeError("arc start and length must be integers")
    if not 1 <= length < n:
        raise ValueError("a short cyclic arc must have length in [1, modulus)")
    return start % n, length, n


def cyclic_arc_overlap(
    left_start: int,
    left_length: int,
    right_start: int,
    right_length: int,
    modulus: int,
) -> int:
    """Cardinality of two oriented integer arcs on ``Z/modulus Z``.

    An arc with start ``a`` and length ``L`` is ``{a+1,...,a+L}`` modulo
    ``N``.  Put ``x=(c-a) mod N`` for the second start.  Cutting the second
    arc at the wrap point gives the exact positive-part formula used below.
    """
    a, left, n = _validated_arc(left_start, left_length, modulus)
    c, right, _ = _validated_arc(right_start, right_length, n)
    x = (c - a) % n
    positive = lambda value: max(value, 0)
    return (
        positive(left - x)
        - positive(left - x - right)
        + positive(x + right - n)
        - positive(x + right - n - left)
    )


def cyclic_arc_covariance(
    left_start: int,
    left_length: int,
    right_start: int,
    right_length: int,
    modulus: int,
) -> Fraction:
    """Unnormalised covariance ``|B cap B'|-|B||B'|/N``."""
    overlap = cyclic_arc_overlap(
        left_start, left_length, right_start, right_length, modulus
    )
    n = _validated_modulus(modulus)
    return Fraction(overlap) - Fraction(left_length * right_length, n)


def cycle_resistance(position: int, modulus: int) -> Fraction:
    """Effective-resistance kernel ``r(N-r)/N`` on the unit cycle."""
    n = _validated_modulus(modulus)
    if not isinstance(position, int):
        raise TypeError("position must be an integer")
    residue = position % n
    return Fraction(residue * (n - residue), n)


def cyclic_arc_covariance_via_resistance(
    left_start: int,
    left_length: int,
    right_start: int,
    right_length: int,
    modulus: int,
) -> Fraction:
    """The same covariance as a four-endpoint resistance polarization."""
    a, left, n = _validated_arc(left_start, left_length, modulus)
    c, right, _ = _validated_arc(right_start, right_length, n)
    b = a + left
    d = c + right
    return Fraction(1, 2) * (
        cycle_resistance(a - d, n)
        + cycle_resistance(b - c, n)
        - cycle_resistance(a - c, n)
        - cycle_resistance(b - d, n)
    )


def pair_pair_covariance_sum(points: Iterable[int], modulus: int) -> Fraction:
    """Exact ordered pair-pair sum equal to ``N * Var(C_N)``."""
    n = _validated_modulus(modulus)
    edges = short_pair_edges(points, n)
    return sum(
        (
            cyclic_arc_covariance(
                left_edge.left,
                left_edge.distance,
                right_edge.left,
                right_edge.distance,
                n,
            )
            for left_edge, right_edge in product(edges, repeat=2)
        ),
        Fraction(0),
    )


def fixed_modulus_prefix_load_second_difference(
    points: Iterable[int], modulus: int, mark_count: int
) -> list[int]:
    """Return ``C_m-2C_{m-1}+C_{m-2}`` for a fixed containing cycle.

    If the full supplied point set has diameter below ``N``, the result is
    exactly ``(m-1)`` times the indicator of the new adjacent gap
    ``(a_{m-1},a_m]``.  Keeping ``N`` fixed is essential; changing the
    modulus between prefixes destroys this identity.
    """
    n = _validated_modulus(modulus)
    pts = tuple(points)
    if any(not isinstance(point, int) for point in pts):
        raise TypeError("points must be integers")
    if tuple(sorted(pts)) != pts or len(set(pts)) != len(pts):
        raise ValueError("points must be strictly increasing")
    if not isinstance(mark_count, int):
        raise TypeError("mark_count must be an integer")
    if not 2 <= mark_count <= len(pts):
        raise ValueError("mark_count must lie between 2 and the point count")
    if pts and pts[-1] - pts[0] >= n:
        raise ValueError("the supplied points must have diameter below the modulus")

    current = crossing_loads(pts[:mark_count], n)
    previous = crossing_loads(pts[: mark_count - 1], n)
    two_back = crossing_loads(pts[: mark_count - 2], n)
    return [
        current[residue] - 2 * previous[residue] + two_back[residue]
        for residue in range(n)
    ]

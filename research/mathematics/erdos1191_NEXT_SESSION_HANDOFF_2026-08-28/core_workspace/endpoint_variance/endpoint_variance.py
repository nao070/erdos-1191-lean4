"""Exact endpoint-sensitive offset-energy identities for finite integer sets.

All arithmetic exposed by the public API is integral or fractions.Fraction based.
The central object is the directed short-pair residue multigraph modulo ``N``.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb


@dataclass(frozen=True, order=True)
class ShortPairEdge:
    left: int
    right: int
    tail: int
    head: int
    distance: int


def _validated_points(points: Iterable[int]) -> tuple[int, ...]:
    result = tuple(points)
    if any(not isinstance(x, int) for x in result):
        raise TypeError("points must be integers")
    if tuple(sorted(result)) != result or len(set(result)) != len(result):
        raise ValueError("points must be strictly increasing")
    return result


def _validated_modulus(modulus: int) -> int:
    if not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus < 2:
        raise ValueError("modulus must be at least 2")
    return modulus


def gap_vector_to_ruler(gaps: Iterable[int]) -> tuple[int, ...]:
    """Convert positive integer gaps to their normalized ruler marks."""
    gap_tuple = tuple(gaps)
    if any(not isinstance(gap, int) for gap in gap_tuple):
        raise TypeError("gaps must be integers")
    if any(gap <= 0 for gap in gap_tuple):
        raise ValueError("gaps must be positive")
    marks = [0]
    for gap in gap_tuple:
        marks.append(marks[-1] + gap)
    return tuple(marks)


def has_distinct_contiguous_gap_sums(gaps: Iterable[int]) -> bool:
    """Whether every nonempty contiguous sum of ``gaps`` is distinct."""
    marks = gap_vector_to_ruler(gaps)
    differences = [
        marks[j] - marks[i]
        for i in range(len(marks))
        for j in range(i + 1, len(marks))
    ]
    return len(differences) == len(set(differences))


def _validated_normalized_ruler_parameters(mark_count: int, diameter: int) -> None:
    if not isinstance(mark_count, int) or not isinstance(diameter, int):
        raise TypeError("mark_count and diameter must be integers")
    if mark_count < 2:
        raise ValueError("mark_count must be at least 2")
    if diameter < 1:
        raise ValueError("diameter must be positive")


def normalized_ruler_candidate_count(mark_count: int, diameter: int) -> int:
    """Number of normalized increasing candidates before the Golomb filter."""
    _validated_normalized_ruler_parameters(mark_count, diameter)
    internal_marks = mark_count - 2
    available_positions = diameter - 1
    if internal_marks > available_positions:
        return 0
    return comb(available_positions, internal_marks)


def iter_normalized_golomb_rulers(
    mark_count: int, diameter: int
) -> Iterator[tuple[int, ...]]:
    """Enumerate every normalized ``mark_count``-mark Golomb ruler of diameter ``D``.

    The enumeration scans all choices of the internal marks in lexicographic
    order, so its completeness denominator is
    :func:`normalized_ruler_candidate_count`.
    """
    _validated_normalized_ruler_parameters(mark_count, diameter)
    for internal_marks in combinations(range(1, diameter), mark_count - 2):
        ruler = (0, *internal_marks, diameter)
        differences = [
            ruler[j] - ruler[i]
            for i in range(mark_count)
            for j in range(i + 1, mark_count)
        ]
        if len(differences) == len(set(differences)):
            yield ruler


def canonical_reflection_ruler(points: Iterable[int]) -> tuple[int, ...]:
    """Canonical representative of a normalized ruler and its reflection."""
    ruler = _validated_points(points)
    if len(ruler) < 2 or ruler[0] != 0:
        raise ValueError("a normalized ruler must start at 0 and have at least 2 marks")
    diameter = ruler[-1]
    reflected = tuple(diameter - mark for mark in reversed(ruler))
    return min(ruler, reflected)


@dataclass(frozen=True)
class GolombVarianceMinimum:
    mark_count: int
    diameter: int
    modulus: int
    candidate_count: int
    golomb_ruler_count: int
    minimum_variance: Fraction | None
    minimizers: tuple[tuple[int, ...], ...]
    reflection_classes: tuple[tuple[int, ...], ...]


def golomb_variance_minimum(
    mark_count: int, diameter: int, modulus: int
) -> GolombVarianceMinimum:
    """Exact diameter-regime variance minimum over all normalized rulers."""
    _validated_normalized_ruler_parameters(mark_count, diameter)
    n = _validated_modulus(modulus)
    if n <= diameter:
        raise ValueError("Golomb variance search requires modulus > diameter")

    minimum: Fraction | None = None
    minimizers: list[tuple[int, ...]] = []
    ruler_count = 0
    for ruler in iter_normalized_golomb_rulers(mark_count, diameter):
        ruler_count += 1
        value = diameter_regime_variance(ruler, n)
        if minimum is None or value < minimum:
            minimum = value
            minimizers = [ruler]
        elif value == minimum:
            minimizers.append(ruler)

    classes = tuple(sorted({canonical_reflection_ruler(ruler) for ruler in minimizers}))
    return GolombVarianceMinimum(
        mark_count=mark_count,
        diameter=diameter,
        modulus=n,
        candidate_count=normalized_ruler_candidate_count(mark_count, diameter),
        golomb_ruler_count=ruler_count,
        minimum_variance=minimum,
        minimizers=tuple(minimizers),
        reflection_classes=classes,
    )


def short_pair_edges(points: Iterable[int], modulus: int) -> tuple[ShortPairEdge, ...]:
    """Return one directed residue edge for every pair at distance below ``modulus``."""
    pts = _validated_points(points)
    n = _validated_modulus(modulus)
    edges: list[ShortPairEdge] = []
    for i, left in enumerate(pts):
        for right in pts[i + 1 :]:
            distance = right - left
            if distance >= n:
                break
            edges.append(
                ShortPairEdge(
                    left=left,
                    right=right,
                    tail=left % n,
                    head=right % n,
                    distance=distance,
                )
            )
    return tuple(edges)


def crossing_loads(points: Iterable[int], modulus: int) -> list[int]:
    """Boundary-arc load C_N(r).

    A short pair ``a < b`` contributes at the integer phases
    ``a+1, ..., b (mod N)``.  Thus it contributes exactly ``b-a`` times.
    """
    n = _validated_modulus(modulus)
    loads = [0] * n
    for edge in short_pair_edges(points, n):
        for step in range(1, edge.distance + 1):
            loads[(edge.left + step) % n] += 1
    return loads


def offset_energies(points: Iterable[int], modulus: int) -> list[int]:
    """Same-block pair counts for each translation of the N-block partition."""
    edges = short_pair_edges(points, modulus)
    loads = crossing_loads(points, modulus)
    return [len(edges) - load for load in loads]


def endpoint_imbalance(points: Iterable[int], modulus: int) -> list[int]:
    """Outdegree minus indegree in the short-pair residue multigraph."""
    n = _validated_modulus(modulus)
    delta = [0] * n
    for edge in short_pair_edges(points, n):
        delta[edge.tail] += 1
        delta[edge.head] -= 1
    return delta


def forward_difference(values: Sequence[int]) -> list[int]:
    """Cyclic forward difference ``values[r+1]-values[r]``."""
    if len(values) < 2:
        raise ValueError("a cyclic vector must have length at least 2")
    return [values[(r + 1) % len(values)] - values[r] for r in range(len(values))]


def variance(values: Sequence[int]) -> Fraction:
    """Population variance, exactly as a Fraction."""
    if not values:
        raise ValueError("variance requires a nonempty vector")
    n = len(values)
    mean = Fraction(sum(values), n)
    return sum((Fraction(value) - mean) ** 2 for value in values) / n


def variance_from_imbalance(delta: Sequence[int]) -> Fraction:
    """Reconstruct offset variance from the endpoint imbalance alone.

    If ``delta[r] = C(r+1)-C(r)``, then a cumulative sum reconstructs C up to
    an additive constant; variance is invariant under that constant.
    """
    if len(delta) < 2:
        raise ValueError("imbalance vector must have length at least 2")
    if sum(delta) != 0:
        raise ValueError("cyclic endpoint imbalance must sum to zero")
    cumulative = [0]
    for entry in delta[:-1]:
        cumulative.append(cumulative[-1] + entry)
    return variance(cumulative)


def poincare_lower_bound(delta: Sequence[int]) -> Fraction:
    """Exact bound V >= ||delta||_2^2/(4N)."""
    if len(delta) < 2 or sum(delta) != 0:
        raise ValueError("delta must be a zero-sum cyclic vector of length at least 2")
    return Fraction(sum(entry * entry for entry in delta), 4 * len(delta))


def distance_spectrum(points: Iterable[int]) -> Counter[int]:
    pts = _validated_points(points)
    return Counter(right - left for i, left in enumerate(pts) for right in pts[i + 1 :])


def homometric_distance_spectrum(left: Iterable[int], right: Iterable[int]) -> bool:
    return distance_spectrum(left) == distance_spectrum(right)


def zero_variance_cycle_decomposition(
    points: Iterable[int], modulus: int
) -> list[list[ShortPairEdge]]:
    """Decompose all short-pair edges into directed cycles when V_N=0.

    Raises ``ValueError`` unless every residue vertex is balanced.  Hierholzer's
    algorithm is applied component by component and preserves parallel edges.
    """
    n = _validated_modulus(modulus)
    edges = list(short_pair_edges(points, n))
    delta = endpoint_imbalance(points, n)
    if any(delta):
        raise ValueError("zero-variance cycle decomposition requires balanced vertices")

    outgoing: dict[int, list[int]] = defaultdict(list)
    for index, edge in enumerate(edges):
        outgoing[edge.tail].append(index)
    for stack in outgoing.values():
        stack.reverse()

    unused = set(range(len(edges)))
    cycles: list[list[ShortPairEdge]] = []
    while unused:
        first = min(unused)
        start = edges[first].tail
        vertex_stack = [start]
        edge_stack: list[int] = []
        circuit_edge_indices: list[int] = []
        while vertex_stack:
            vertex = vertex_stack[-1]
            while outgoing[vertex] and outgoing[vertex][-1] not in unused:
                outgoing[vertex].pop()
            if outgoing[vertex]:
                edge_index = outgoing[vertex].pop()
                unused.remove(edge_index)
                edge_stack.append(edge_index)
                vertex_stack.append(edges[edge_index].head)
            else:
                vertex_stack.pop()
                if edge_stack:
                    circuit_edge_indices.append(edge_stack.pop())
        circuit_edge_indices.reverse()
        if circuit_edge_indices:
            # A balanced component's Euler circuit is itself a directed cycle in
            # the edge-decomposition sense; repeated vertices are allowed.
            cycle = [edges[index] for index in circuit_edge_indices]
            if cycle[-1].head != cycle[0].tail:
                raise AssertionError("balanced component did not close")
            cycles.append(cycle)
    return cycles


@dataclass(frozen=True)
class DiameterRegimeProfile:
    """Gap data when all points fit in one cyclic arc shorter than N."""

    outside_gap: int
    internal_gaps: tuple[int, ...]
    crossing_levels: tuple[int, ...]


def diameter_regime_profile(points: Iterable[int], modulus: int) -> DiameterRegimeProfile:
    """Return the exact boundary-load profile for ``diam(points) < modulus``.

    The load is zero on the outside cyclic gap.  On the integer gap from the
    k-th to the (k+1)-st point it is ``k*(m-k)``.
    """
    pts = _validated_points(points)
    n = _validated_modulus(modulus)
    if not pts:
        return DiameterRegimeProfile(n, (), ())
    diameter = pts[-1] - pts[0]
    if diameter >= n:
        raise ValueError("diameter_regime_profile requires diameter < modulus")
    gaps = tuple(pts[i + 1] - pts[i] for i in range(len(pts) - 1))
    levels = tuple(k * (len(pts) - k) for k in range(1, len(pts)))
    return DiameterRegimeProfile(n - diameter, gaps, levels)


def diameter_regime_variance(points: Iterable[int], modulus: int) -> Fraction:
    """Exact variance from the gap moment formula in the diameter regime."""
    profile = diameter_regime_profile(points, modulus)
    n = _validated_modulus(modulus)
    first = sum(gap * level for gap, level in zip(profile.internal_gaps, profile.crossing_levels))
    second = sum(gap * level * level for gap, level in zip(profile.internal_gaps, profile.crossing_levels))
    mean = Fraction(first, n)
    return Fraction(second, n) - mean * mean


def rank_imbalance_square_sum(size: int) -> int:
    """Sum of squared endpoint imbalances for a complete ordered graph."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be nonnegative")
    return size * (size * size - 1) // 3



def diameter_required_levels_lower_bound(size: int, modulus: int) -> Fraction:
    """Sharp universal variance floor from mandatory split levels.

    In the diameter regime, the N offset loads contain at least one copy of
    each value ``k*(m-k)`` for k=0,...,m-1.  Dropping all additional copies
    and optimising the centre gives

        Var >= m(m^2-1)(m^2+11)/(180N).

    Equality holds for consecutive points with N=m (and trivially for m<=1).
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be nonnegative")
    n = _validated_modulus(modulus)
    return Fraction(size * (size * size - 1) * (size * size + 11), 180 * n)

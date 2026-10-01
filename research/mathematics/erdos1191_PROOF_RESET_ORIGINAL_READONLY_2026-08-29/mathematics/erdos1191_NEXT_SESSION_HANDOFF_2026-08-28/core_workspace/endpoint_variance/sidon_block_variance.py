"""Positive gap-kernel identities for diameter-regime Sidon prefixes.

The functions in this module use exact ``fractions.Fraction`` arithmetic.  A
``m``-mark prefix is always evaluated at the diameter modulus
``N = max(A) - min(A) + 1``.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from fractions import Fraction

from endpoint_variance import crossing_loads, variance


def _validated_points(points: Iterable[int]) -> tuple[int, ...]:
    result = tuple(points)
    if any(not isinstance(point, int) for point in result):
        raise TypeError("points must be integers")
    if len(result) < 2:
        raise ValueError("at least two points are required")
    if tuple(sorted(result)) != result or len(set(result)) != len(result):
        raise ValueError("points must be strictly increasing")
    return result


def is_golomb_ruler(points: Iterable[int]) -> bool:
    """Return whether all positive pair differences are distinct."""
    marks = _validated_points(points)
    differences = [
        marks[right] - marks[left]
        for left in range(len(marks))
        for right in range(left + 1, len(marks))
    ]
    return len(differences) == len(set(differences))


def diameter_gap_profile(
    points: Iterable[int],
) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    """Return ``(N, h, x)`` for the positive diameter gap identity.

    ``h[0] = 1`` is the unique phase outside the diameter interval,
    ``h[k]`` for ``k >= 1`` is the gap between marks ``k-1`` and ``k``,
    and ``x[k] = k(m-k)`` is the crossing-load level on that gap.
    """
    marks = _validated_points(points)
    mark_count = len(marks)
    modulus = marks[-1] - marks[0] + 1
    gaps = (1, *(marks[index] - marks[index - 1] for index in range(1, mark_count)))
    levels = tuple(index * (mark_count - index) for index in range(mark_count))
    return modulus, gaps, levels


def positive_gap_variance(points: Iterable[int]) -> Fraction:
    """Evaluate the exact nonnegative gap-pair formula for ``Var C_N``."""
    modulus, gaps, levels = diameter_gap_profile(points)
    return sum(
        Fraction(
            gaps[left]
            * gaps[right]
            * (levels[left] - levels[right]) ** 2,
            modulus * modulus,
        )
        for left in range(len(gaps))
        for right in range(left + 1, len(gaps))
    )


@dataclass(frozen=True)
class SidonBlockVarianceWitness:
    mark_count: int
    q: int
    diameter: int
    modulus: int
    heavy_block: int
    target_block: int
    heavy_mass: int
    target_mass: int
    minimum_level_separation: int
    exact_variance: Fraction
    block_lower_bound: Fraction
    simplified_lower_bound: Fraction


def _gap_blocks(mark_count: int) -> tuple[tuple[int, ...], ...]:
    if mark_count % 8:
        raise ValueError("mark count must be divisible by 8")
    q = mark_count // 8
    return (
        tuple(range(1, q)),
        *(tuple(range(block * q, (block + 1) * q)) for block in range(1, 8)),
    )


def sidon_block_variance_witness(
    points: Iterable[int],
) -> SidonBlockVarianceWitness:
    """Certify the positive block lower bound for a ``m = 8q >= 16`` ruler."""
    marks = _validated_points(points)
    mark_count = len(marks)
    if mark_count < 16 or mark_count % 8:
        raise ValueError("the theorem requires m = 8q with q >= 2")
    if not is_golomb_ruler(marks):
        raise ValueError("the theorem requires a Sidon/Golomb ruler")

    modulus, gaps, levels = diameter_gap_profile(marks)
    diameter = modulus - 1
    q = mark_count // 8
    blocks = _gap_blocks(mark_count)
    masses = tuple(sum(gaps[index] for index in block) for block in blocks)
    heavy_block = max(range(8), key=masses.__getitem__)
    target_block = 3 if heavy_block in {0, 1, 6, 7} else 0
    minimum_level_separation = min(
        abs(levels[left] - levels[right])
        for left in blocks[heavy_block]
        for right in blocks[target_block]
    )

    exact_variance = positive_gap_variance(marks)
    block_lower_bound = Fraction(9 * diameter * q**5 * (q - 1), 16 * modulus**2)
    simplified_lower_bound = Fraction(9 * mark_count**6, 16_777_216 * modulus)

    if masses[heavy_block] * 8 < diameter:
        raise AssertionError("heavy-block pigeonhole certificate failed")
    if masses[target_block] < q * (q - 1) // 2:
        raise AssertionError("target-block Sidon span certificate failed")
    if minimum_level_separation < 3 * q * q:
        raise AssertionError("load-level separation certificate failed")
    if exact_variance < block_lower_bound or block_lower_bound < simplified_lower_bound:
        raise AssertionError("Sidon block lower-bound chain failed")

    return SidonBlockVarianceWitness(
        mark_count=mark_count,
        q=q,
        diameter=diameter,
        modulus=modulus,
        heavy_block=heavy_block,
        target_block=target_block,
        heavy_mass=masses[heavy_block],
        target_mass=masses[target_block],
        minimum_level_separation=minimum_level_separation,
        exact_variance=exact_variance,
        block_lower_bound=block_lower_bound,
        simplified_lower_bound=simplified_lower_bound,
    )


def dyadic_positive_functional(
    points: Iterable[int], j0: int, final_j: int
) -> Fraction:
    """Compute ``sum_j Var(C_{N_j}) / m_j^4`` for dyadic prefixes."""
    marks = _validated_points(points)
    if not isinstance(j0, int) or not isinstance(final_j, int):
        raise TypeError("j0 and final_j must be integers")
    if j0 < 1 or final_j < j0:
        raise ValueError("require 1 <= j0 <= final_j")
    if 2**final_j > len(marks):
        raise ValueError("the point sequence does not contain the final prefix")
    return sum(
        positive_gap_variance(marks[: 2**j]) / 2 ** (4 * j)
        for j in range(j0, final_j + 1)
    )


def first_dyadic_birth_scale(gap_index: int, j0: int) -> int:
    """First scale ``j >= j0`` for which ``gap_index < 2**j``."""
    if not isinstance(gap_index, int) or not isinstance(j0, int):
        raise TypeError("gap_index and j0 must be integers")
    if gap_index < 1 or j0 < 1:
        raise ValueError("gap_index and j0 must be positive")
    scale = j0
    while gap_index >= 2**scale:
        scale += 1
    return scale


def positive_birth_kernel(
    points: Iterable[int], left: int, right: int, j0: int, final_j: int
) -> Fraction:
    """Compute the exact nonnegative multiscale kernel ``Lambda_J(left,right)``."""
    marks = _validated_points(points)
    if not (0 <= left < right < 2**final_j <= len(marks)):
        raise ValueError("require 0 <= left < right < 2**final_j <= len(points)")
    if j0 < 1 or final_j < j0:
        raise ValueError("require 1 <= j0 <= final_j")
    birth = first_dyadic_birth_scale(right, j0)
    if birth > final_j:
        return Fraction(0)
    total = Fraction(0)
    for scale in range(birth, final_j + 1):
        mark_count = 2**scale
        modulus = marks[mark_count - 1] - marks[0] + 1
        total += Fraction(
            (right - left) ** 2 * (mark_count - left - right) ** 2,
            mark_count**4 * modulus**2,
        )
    return total


def dyadic_functional_via_birth_kernel(
    points: Iterable[int], j0: int, final_j: int
) -> Fraction:
    """Reconstruct the dyadic functional by exchanging its positive sums."""
    marks = _validated_points(points)
    if j0 < 1 or final_j < j0 or 2**final_j > len(marks):
        raise ValueError("require 1 <= j0 <= final_j and a complete final prefix")
    final_count = 2**final_j
    gaps = (1, *(marks[index] - marks[index - 1] for index in range(1, final_count)))
    return sum(
        gaps[left]
        * gaps[right]
        * positive_birth_kernel(marks, left, right, j0, final_j)
        for left in range(final_count)
        for right in range(left + 1, final_count)
    )


def dyadic_shell_upper_bound(
    points: Iterable[int], j0: int, final_j: int
) -> Fraction:
    """Return the exact unconditional upper bound ``(4/3) sum H_s/N_s``."""
    marks = _validated_points(points)
    if j0 < 1 or final_j < j0 or 2**final_j > len(marks):
        raise ValueError("require 1 <= j0 <= final_j and a complete final prefix")
    total = Fraction(0)
    previous_diameter = 0
    for scale in range(j0, final_j + 1):
        mark_count = 2**scale
        diameter = marks[mark_count - 1] - marks[0]
        shell_mass = diameter if scale == j0 else diameter - previous_diameter
        total += Fraction(shell_mass, diameter + 1)
        previous_diameter = diameter
    return Fraction(4, 3) * total


def three_rank_lift(points: Iterable[int]) -> tuple[int, ...]:
    """Apply the three-rank lift that forces one constant-energy birth shell."""
    marks = _validated_points(points)
    mark_count = len(marks)
    if mark_count % 4:
        raise ValueError("the three-rank lift requires a mark count divisible by 4")
    diameter = marks[-1] - marks[0]
    shift = diameter + 1
    first_boundary = mark_count // 4
    second_boundary = mark_count // 2
    lifted = tuple(
        mark
        + shift
        * (0 if index < first_boundary else 1 if index < second_boundary else 2)
        for index, mark in enumerate(marks)
    )
    if not is_golomb_ruler(lifted):
        raise AssertionError("three-rank lift failed to preserve the Sidon property")
    return lifted


def erdos_turan_ruler(mark_count: int, prime: int) -> tuple[int, ...]:
    """Return ``2*p*i + (i^2 mod p)`` for ``0 <= i < mark_count``."""
    if not isinstance(mark_count, int) or not isinstance(prime, int):
        raise TypeError("mark_count and prime must be integers")
    if mark_count < 2 or prime < mark_count:
        raise ValueError("require 2 <= mark_count <= prime")
    ruler = tuple(2 * prime * index + (index * index % prime) for index in range(mark_count))
    if not is_golomb_ruler(ruler):
        raise ValueError("the supplied modulus does not produce a Sidon ruler")
    return ruler


def direct_diameter_variance(points: Iterable[int]) -> Fraction:
    """Independent crossing-load evaluation used by certificates and tests."""
    marks = _validated_points(points)
    modulus = marks[-1] - marks[0] + 1
    return variance(crossing_loads(marks, modulus))

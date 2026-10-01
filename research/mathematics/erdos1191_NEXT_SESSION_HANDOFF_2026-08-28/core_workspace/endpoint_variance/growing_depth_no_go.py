"""Growing-depth Erdős--Turán windows for the global-history no-go.

The analytic construction uses a terminal ruler with ``M = 2**J`` marks and
keeps its final ``floor(log2(J)) - 1`` dyadic prefixes.  The implementation
uses exact integer and ``Fraction`` arithmetic for every reported statistic;
the elementary inequality ``log(2) > 2/3`` is represented by an integer
sufficient condition rather than evaluated numerically.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from endpoint_variance import diameter_regime_variance
from fixed_depth_no_go import is_prime, least_prime_at_least
from sidon_block_variance import diameter_gap_profile


def logarithmic_window_depth(scale_index: int) -> int:
    """Return ``floor(log2(scale_index)) - 2`` for ``scale_index >= 8``."""
    if not isinstance(scale_index, int):
        raise TypeError("scale_index must be an integer")
    if scale_index < 8:
        raise ValueError("the logarithmic-window theorem starts at scale index eight")
    return scale_index.bit_length() - 3


def logarithmic_window_sufficient_condition(
    scale_index: int, terminal_offset: int
) -> bool:
    """Check an exact sufficient condition for the ``C=1`` critical envelope.

    At terminal size ``M=2**J`` and prefix size ``n=M/2**ell``, the
    Erdős--Turán modulus satisfies ``N_n < 4*M*n``.  It is therefore enough
    that ``2**(ell+1) <= log(n)``.  We certify the stronger rational condition

    ``3*2**(ell+1) <= 2*(J-ell)``,

    which implies the desired inequality from ``log(2) > 2/3``.
    """
    if not isinstance(scale_index, int) or not isinstance(terminal_offset, int):
        raise TypeError("scale_index and terminal_offset must be integers")
    if scale_index < 1 or not 0 <= terminal_offset < scale_index:
        raise ValueError("require scale_index >= 1 and 0 <= offset < scale_index")
    return 3 * 2 ** (terminal_offset + 1) <= 2 * (
        scale_index - terminal_offset
    )


def erdos_turan_points_without_quadratic_check(
    mark_count: int, prime: int
) -> tuple[int, ...]:
    """Construct ``2*p*i + i^2 mod p`` without an ``O(mark_count^2)`` scan.

    The accompanying proof establishes the Golomb property for every prime
    ``p >= mark_count``.  Small instances are still compared with the
    independent quadratic difference oracle in the unit tests.
    """
    if not isinstance(mark_count, int) or not isinstance(prime, int):
        raise TypeError("mark_count and prime must be integers")
    if mark_count < 2 or prime < mark_count or not is_prime(prime):
        raise ValueError("require 2 <= mark_count <= prime with prime prime")
    return tuple(
        2 * prime * index + (index * index % prime)
        for index in range(mark_count)
    )


def _quadratic_function_variance(
    points: tuple[int, ...], dilation: int = 1
) -> Fraction:
    """Return ``Var_nu(f(U/dilation))`` by an integer moment formula."""
    if not isinstance(dilation, int) or dilation < 1:
        raise ValueError("dilation must be a positive integer")
    modulus, gaps, _ = diameter_gap_profile(points)
    count = len(points)
    levels = tuple(
        index * (dilation * count - index) for index in range(count)
    )
    first = sum(gap * level for gap, level in zip(gaps, levels))
    second = sum(gap * level * level for gap, level in zip(gaps, levels))
    denominator_scale = dilation**4 * count**4
    return Fraction(
        modulus * second - first * first,
        modulus * modulus * denominator_scale,
    )


def gap_measure_kolmogorov_discrepancy(points: tuple[int, ...]) -> Fraction:
    """Return the exact Kolmogorov distance from the uniform measure."""
    modulus, gaps, _ = diameter_gap_profile(points)
    count = len(points)
    cumulative = 0
    maximum_numerator = 0
    for index, gap in enumerate(gaps):
        maximum_numerator = max(
            maximum_numerator,
            abs(cumulative * count - index * modulus),
        )
        cumulative += gap
        maximum_numerator = max(
            maximum_numerator,
            abs(cumulative * count - index * modulus),
        )
    if cumulative != modulus:
        raise AssertionError("diameter gap weights did not sum to the modulus")
    return Fraction(maximum_numerator, modulus * count)


def normalized_gap_innovation_00(
    points: tuple[int, ...], old_count: int
) -> Fraction:
    """Return ``Q[0,0]/N_new`` for an exact dyadic prefix transition."""
    if not isinstance(old_count, int) or old_count < 2:
        raise ValueError("old_count must be an integer at least two")
    if len(points) != 2 * old_count:
        raise ValueError("points must contain exactly twice old_count marks")
    old = points[:old_count]
    old_modulus = old[-1] - old[0] + 1
    new_modulus = points[-1] - points[0] + 1
    return _quadratic_function_variance(points) - Fraction(
        old_modulus, new_modulus
    ) * _quadratic_function_variance(old, dilation=2)


def normalized_same_modulus_birth_shell(
    points: tuple[int, ...], old_count: int
) -> Fraction:
    """Return the normalized variance increment at the final modulus."""
    if not isinstance(old_count, int) or old_count < 2:
        raise ValueError("old_count must be an integer at least two")
    if len(points) != 2 * old_count:
        raise ValueError("points must contain exactly twice old_count marks")
    new_modulus = points[-1] - points[0] + 1
    return Fraction(
        diameter_regime_variance(points, new_modulus)
        - diameter_regime_variance(points[:old_count], new_modulus),
        len(points) ** 4,
    )


@dataclass(frozen=True)
class GrowingDepthScale:
    terminal_offset: int
    mark_count: int
    modulus: int
    kolmogorov_discrepancy: Fraction
    normalized_variance: Fraction


@dataclass(frozen=True)
class GrowingDepthTransition:
    old_count: int
    new_count: int
    normalized_innovation_00: Fraction
    same_modulus_birth_shell: Fraction


@dataclass(frozen=True)
class GrowingDepthWitness:
    scale_index: int
    terminal_count: int
    depth: int
    prime: int
    scales: tuple[GrowingDepthScale, ...]
    transitions: tuple[GrowingDepthTransition, ...]
    variance_sum: Fraction
    innovation_00_sum: Fraction
    same_modulus_birth_shell_sum: Fraction


def growing_depth_erdos_turan_witness(
    scale_index: int, prime: int | None = None
) -> GrowingDepthWitness:
    """Return exact statistics for the logarithmically growing final window.

    The witness is a finite nonextendability obstruction.  It is not claimed
    to embed into one infinite globally critical Sidon sequence.
    """
    depth = logarithmic_window_depth(scale_index)
    terminal_count = 1 << scale_index
    chosen_prime = (
        least_prime_at_least(terminal_count) if prime is None else prime
    )
    if (
        not is_prime(chosen_prime)
        or chosen_prime < terminal_count
        or chosen_prime >= 2 * terminal_count
    ):
        raise ValueError("prime must lie in [terminal_count, 2*terminal_count)")

    points = erdos_turan_points_without_quadratic_check(
        terminal_count, chosen_prime
    )
    counts = tuple(
        1 << exponent
        for exponent in range(scale_index - depth, scale_index + 1)
    )

    scale_records = []
    for count in counts:
        terminal_offset = scale_index - (count.bit_length() - 1)
        if not logarithmic_window_sufficient_condition(
            scale_index, terminal_offset
        ):
            raise AssertionError("exact critical-envelope condition failed")
        prefix = points[:count]
        modulus = prefix[-1] - prefix[0] + 1
        if not modulus < 4 * terminal_count * count:
            raise AssertionError("Erdős--Turán modulus upper bound failed")
        discrepancy = gap_measure_kolmogorov_discrepancy(prefix)
        if discrepancy > Fraction(4, count):
            raise AssertionError("uniform gap-measure discrepancy bound failed")
        scale_records.append(
            GrowingDepthScale(
                terminal_offset=terminal_offset,
                mark_count=count,
                modulus=modulus,
                kolmogorov_discrepancy=discrepancy,
                normalized_variance=_quadratic_function_variance(prefix),
            )
        )

    transition_records = []
    for old_count, new_count in zip(counts, counts[1:]):
        full = points[:new_count]
        transition_records.append(
            GrowingDepthTransition(
                old_count=old_count,
                new_count=new_count,
                normalized_innovation_00=normalized_gap_innovation_00(
                    full, old_count
                ),
                same_modulus_birth_shell=normalized_same_modulus_birth_shell(
                    full, old_count
                ),
            )
        )

    scales = tuple(scale_records)
    transitions = tuple(transition_records)
    return GrowingDepthWitness(
        scale_index=scale_index,
        terminal_count=terminal_count,
        depth=depth,
        prime=chosen_prime,
        scales=scales,
        transitions=transitions,
        variance_sum=sum(
            (record.normalized_variance for record in scales), Fraction(0)
        ),
        innovation_00_sum=sum(
            (record.normalized_innovation_00 for record in transitions),
            Fraction(0),
        ),
        same_modulus_birth_shell_sum=sum(
            (record.same_modulus_birth_shell for record in transitions),
            Fraction(0),
        ),
    )

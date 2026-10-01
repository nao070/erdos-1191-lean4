"""Exact finite witnesses for the fixed-depth Erdős--Turán no-go."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt

from endpoint_variance import diameter_regime_variance
from gap_measure_dynamics import dyadic_gap_matrix_update
from sidon_block_variance import erdos_turan_ruler, is_golomb_ruler


def is_prime(value: int) -> bool:
    if not isinstance(value, int) or value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def least_prime_at_least(value: int) -> int:
    if not isinstance(value, int) or value < 2:
        raise ValueError("value must be an integer at least two")
    candidate = value
    while not is_prime(candidate):
        candidate += 1
    return candidate


def born_diagonal_energy(
    points: tuple[int, ...], old_count: int, modulus: int
) -> Fraction:
    """Return the diagonal covariance of edges not wholly in the old prefix."""
    if not 1 <= old_count < len(points):
        raise ValueError("old_count must split a nonempty proper prefix")
    if modulus <= points[-1] - points[0]:
        raise ValueError("modulus must exceed the full diameter")
    total = Fraction(0)
    for left in range(len(points)):
        for right in range(left + 1, len(points)):
            if right < old_count:
                continue
            distance = points[right] - points[left]
            total += Fraction(distance * (modulus - distance), modulus**2)
    return total


@dataclass(frozen=True)
class FixedDepthWitness:
    mark_count: int
    prime: int
    modulus: int
    full_normalized_variance: Fraction
    old_same_modulus_normalized_variance: Fraction
    normalized_birth_shell: Fraction
    normalized_birth_diagonal: Fraction
    normalized_birth_off_diagonal: Fraction
    normalized_matrix_innovation_00: Fraction


def erdos_turan_fixed_depth_witness(
    mark_count: int, prime: int | None = None
) -> FixedDepthWitness:
    """Return exact local-shell data for an even Erdős--Turán ruler."""
    if not isinstance(mark_count, int) or mark_count < 4 or mark_count % 2:
        raise ValueError("mark_count must be an even integer at least four")
    chosen_prime = least_prime_at_least(mark_count) if prime is None else prime
    if not is_prime(chosen_prime) or not mark_count <= chosen_prime < 2 * mark_count:
        raise ValueError("prime must lie in [mark_count,2*mark_count)")
    points = erdos_turan_ruler(mark_count, chosen_prime)
    if not is_golomb_ruler(points):
        raise AssertionError("Erdos--Turan construction was not Golomb")
    old_count = mark_count // 2
    old = points[:old_count]
    modulus = points[-1] - points[0] + 1
    full_variance = diameter_regime_variance(points, modulus)
    old_variance = diameter_regime_variance(old, modulus)
    normalization = mark_count**4
    birth_shell = (full_variance - old_variance) / normalization
    birth_diagonal = born_diagonal_energy(points, old_count, modulus) / normalization
    update = dyadic_gap_matrix_update(points, old_count)
    innovation_00 = update.innovation[0][0] / modulus
    return FixedDepthWitness(
        mark_count=mark_count,
        prime=chosen_prime,
        modulus=modulus,
        full_normalized_variance=full_variance / normalization,
        old_same_modulus_normalized_variance=old_variance / normalization,
        normalized_birth_shell=birth_shell,
        normalized_birth_diagonal=birth_diagonal,
        normalized_birth_off_diagonal=birth_shell - birth_diagonal,
        normalized_matrix_innovation_00=innovation_00,
    )

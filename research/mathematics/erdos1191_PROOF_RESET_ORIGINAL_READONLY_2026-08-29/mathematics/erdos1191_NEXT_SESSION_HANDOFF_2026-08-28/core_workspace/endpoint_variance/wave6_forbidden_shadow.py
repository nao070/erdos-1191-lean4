"""Exact finite checks for the Wave 6 forbidden-shadow no-go family.

The construction inserts the mark 1 into a dilated Golomb ruler.  Its
positive differences and its one-point extension shadow then occupy only a
bounded number of residue classes modulo the dilation.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Sequence


PointTuple = tuple[int, ...]
Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def is_prime(value: int) -> bool:
    """Return whether ``value`` is prime, by exact trial division."""
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor <= isqrt(value):
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    """Return all positive differences, retaining multiplicity."""
    return tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )


def is_golomb(points: Sequence[int]) -> bool:
    """Check strict increase and uniqueness of every positive difference."""
    if not points or points[0] != 0:
        return False
    if any(left >= right for left, right in zip(points, points[1:])):
        return False
    differences = positive_differences(points)
    return len(differences) == len(set(differences))


def erdos_turan_ruler(prime: int, count: int) -> PointTuple:
    """Construct the first ``count`` marks of the integer Erdos--Turan ruler."""
    if not is_prime(prime) or prime == 2:
        raise ValueError("prime must be an odd prime")
    if not 2 <= count <= prime:
        raise ValueError("count must lie between 2 and prime")
    points = tuple(2 * prime * index + (index * index) % prime for index in range(count))
    if not is_golomb(points):
        raise AssertionError("Erdos--Turan construction failed its exact audit")
    return points


def residue_lift(base: Sequence[int], dilation: int) -> PointTuple:
    """Return the marks 0, 1, and the dilated positive base marks."""
    if dilation < 3:
        raise ValueError("dilation must be at least 3")
    if not is_golomb(base):
        raise ValueError("base must be a normalized Golomb ruler")
    lifted = (0, 1, *(dilation * point for point in base[1:]))
    if not is_golomb(lifted):
        raise AssertionError("residue lift failed its exact Golomb audit")
    return lifted


def difference_residues(points: Sequence[int], modulus: int) -> tuple[int, ...]:
    """Return the sorted residues occupied by positive differences."""
    return tuple(sorted({difference % modulus for difference in positive_differences(points)}))


def forbidden_shadow(points: Sequence[int]) -> frozenset[int]:
    """Return F(A)=A+Delta^+(A), the exact one-point extension shadow."""
    differences = set(positive_differences(points))
    return frozenset(point + difference for point in points for difference in differences)


def shadow_residues(points: Sequence[int], modulus: int) -> tuple[int, ...]:
    """Return the sorted residues occupied by the forbidden shadow."""
    return tuple(sorted({value % modulus for value in forbidden_shadow(points)}))


def extension_is_golomb(points: Sequence[int], candidate: int) -> bool:
    """Check a one-point extension directly."""
    if candidate <= points[-1]:
        raise ValueError("candidate must lie beyond the old diameter")
    return is_golomb((*points, candidate))


def extension_shadow_criterion(points: Sequence[int], candidate: int) -> bool:
    """Check a one-point extension using candidate not in A+Delta^+(A)."""
    if candidate <= points[-1]:
        raise ValueError("candidate must lie beyond the old diameter")
    return candidate not in forbidden_shadow(points)


def interval_shadow_bound(length: int, dilation: int) -> int:
    """Four-residue-class upper bound for an integer interval of given length."""
    if length < 0:
        raise ValueError("length must be nonnegative")
    if dilation < 1:
        raise ValueError("dilation must be positive")
    if length == 0:
        return 0
    return 4 * ((length + dilation - 1) // dilation)


def profile_grid_error(points: Sequence[int]) -> Fraction:
    """Return max_k |nu([0,k/n])-k/n| for the endpoint-gap measure."""
    size = len(points)
    modulus = points[-1] - points[0] + 1
    gaps = (1, *(points[index] - points[index - 1] for index in range(1, size)))
    cumulative = 0
    error = Fraction(0)
    for index, gap in enumerate(gaps):
        cumulative += gap
        error = max(error, abs(Fraction(cumulative, modulus) - Fraction(index, size)))
    return error


def lifted_profile_grid_bound(size: int, prime: int, dilation: int) -> Fraction:
    """Explicit grid-error bound for a lifted Erdos--Turan prefix."""
    if size < 4:
        raise ValueError("size must be at least 4")
    return Fraction(2, size - 2) + Fraction(1, dilation * prime * (size - 2))


def endpoint_ratio_error(points: Sequence[int], old_count: int) -> Fraction:
    """Return |N_m/N_(2m)-1/2| exactly."""
    if old_count < 2 or 2 * old_count > len(points):
        raise ValueError("need compatible prefixes of sizes m and 2m")
    old_modulus = points[old_count - 1] - points[0] + 1
    new_modulus = points[2 * old_count - 1] - points[0] + 1
    return abs(Fraction(old_modulus, new_modulus) - Fraction(1, 2))


def lifted_endpoint_ratio_bound(old_count: int, prime: int, dilation: int) -> Fraction:
    """Explicit rank-shift bound for a lifted Erdos--Turan transition."""
    if old_count < 3:
        raise ValueError("old_count must be at least 3")
    denominator = 8 * (old_count - 1)
    return Fraction(7, denominator) + Fraction(1, dilation * prime * denominator)


def _covariance_state(points: Sequence[int]) -> tuple[int, Matrix2]:
    """Return N and N*Cov_nu((u(1-u),u)) exactly."""
    size = len(points)
    modulus = points[-1] - points[0] + 1
    gaps = (1, *(points[index] - points[index - 1] for index in range(1, size)))
    if sum(gaps) != modulus:
        raise AssertionError("gap weights do not sum to the endpoint modulus")

    mean_f = Fraction(0)
    mean_u = Fraction(0)
    mean_ff = Fraction(0)
    mean_fu = Fraction(0)
    mean_uu = Fraction(0)
    for index, gap in enumerate(gaps):
        weight = Fraction(gap, modulus)
        u_value = Fraction(index, size)
        f_value = u_value * (1 - u_value)
        mean_f += weight * f_value
        mean_u += weight * u_value
        mean_ff += weight * f_value * f_value
        mean_fu += weight * f_value * u_value
        mean_uu += weight * u_value * u_value

    covariance = (
        (mean_ff - mean_f * mean_f, mean_fu - mean_f * mean_u),
        (mean_fu - mean_f * mean_u, mean_uu - mean_u * mean_u),
    )
    state = tuple(
        tuple(modulus * covariance[row][column] for column in range(2))
        for row in range(2)
    )
    return modulus, state  # type: ignore[return-value]


def innovation_q00_per_modulus(points: Sequence[int], old_count: int) -> Fraction:
    """Return Q_00/N_(2m) for the compatible m-to-2m prefix transition."""
    if old_count < 2 or 2 * old_count > len(points):
        raise ValueError("need compatible prefixes of sizes m and 2m")
    old_modulus, old_state = _covariance_state(points[:old_count])
    new_modulus, new_state = _covariance_state(points[: 2 * old_count])
    del old_modulus
    transported_00 = (
        old_state[0][0] + 2 * old_state[0][1] + old_state[1][1]
    ) / 16
    return (new_state[0][0] - transported_00) / new_modulus


def finite_audit(prime: int = 17, count: int = 15, dilation: int = 7) -> dict[str, object]:
    """Build one exact instance and audit its shadow and dyadic innovations."""
    base = erdos_turan_ruler(prime, count)
    lifted = residue_lift(base, dilation)
    differences = positive_differences(lifted)
    shadow = forbidden_shadow(lifted)
    diameter = lifted[-1]

    for candidate in range(diameter + 1, 2 * diameter + 1):
        if extension_is_golomb(lifted, candidate) != (candidate not in shadow):
            raise AssertionError("direct extension check disagrees with shadow criterion")

    dyadic_rows: list[dict[str, str | int]] = []
    size = 4
    while 2 * size <= len(lifted):
        value = innovation_q00_per_modulus(lifted, size)
        dyadic_rows.append(
            {
                "endpoint_ratio_error": str(endpoint_ratio_error(lifted, size)),
                "endpoint_ratio_upper_bound": str(
                    lifted_endpoint_ratio_bound(size, prime, dilation)
                ),
                "grid_error": str(profile_grid_error(lifted[:size])),
                "grid_error_upper_bound": str(
                    lifted_profile_grid_bound(size, prime, dilation)
                ),
                "old_count": size,
                "new_count": 2 * size,
                "q00_per_modulus": str(value),
            }
        )
        size *= 2

    occupied_next_interval = sum(
        diameter < value <= 2 * diameter for value in shadow
    )
    return {
        "base_count": len(base),
        "diameter": diameter,
        "difference_count": len(differences),
        "difference_residues": difference_residues(lifted, dilation),
        "dilation": dilation,
        "dyadic_rows": dyadic_rows,
        "golomb": is_golomb(lifted),
        "lifted_count": len(lifted),
        "next_interval_length": diameter,
        "next_interval_shadow_count": occupied_next_interval,
        "next_interval_shadow_upper_bound": interval_shadow_bound(diameter, dilation),
        "prime": prime,
        "shadow_residues": shadow_residues(lifted, dilation),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    payload = finite_audit()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if arguments.output is None:
        print(rendered, end="")
    else:
        arguments.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()

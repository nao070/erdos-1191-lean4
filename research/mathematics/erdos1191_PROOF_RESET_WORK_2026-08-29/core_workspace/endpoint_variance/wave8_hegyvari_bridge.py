"""Exact finite bridge tests for Hegyvári's consecutive-sum construction.

Hegyvári's 1986 construction starts from an odd prime ``p`` and the gaps

    a_{i+1} = 2p + [(i+1)^2]_p - [i^2]_p,  0 <= i < p.

Its partial sums are the Golomb ruler ``s_i = 2pi + [i^2]_p``.  This module
keeps the finite theorem separate from the still-missing infinite-prefix
bridge in Erdős Problem #1191.  It also implements exact affine variants and
the necessary-and-sufficient internal-difference condition for safely
splicing two already-Golomb finite blocks after a sufficiently large shift.

All arithmetic is integral and all searches are deterministic.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import asdict, dataclass
from fractions import Fraction
from itertools import pairwise
from math import comb
from pathlib import Path
from typing import Any

Pair = tuple[int, int]


def is_prime(value: int) -> bool:
    """Return whether ``value`` is prime, by exact trial division."""

    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def _validated_ruler(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    if not is_golomb(marks):
        raise ValueError("points must be a Golomb ruler")
    return marks


def positive_difference_map(points: Sequence[int]) -> dict[int, Pair]:
    """Map every positive difference to its first endpoint-index pair."""

    marks = tuple(points)
    rows: dict[int, Pair] = {}
    for left in range(len(marks)):
        for right in range(left + 1, len(marks)):
            difference = marks[right] - marks[left]
            rows.setdefault(difference, (left, right))
    return rows


def positive_differences(points: Sequence[int]) -> frozenset[int]:
    return frozenset(positive_difference_map(points))


def is_golomb(points: Sequence[int]) -> bool:
    marks = tuple(points)
    if (
        len(marks) < 2
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        return False
    expected = comb(len(marks), 2)
    return len(positive_difference_map(marks)) == expected


def hegyvari_marks(
    prime: int,
    *,
    alpha: int = 1,
    beta: int = 0,
    gamma: int = 0,
    rotation: int = 0,
    gap_translation: int = 0,
) -> tuple[int, ...]:
    """Return an affine/cyclic Hegyvári ruler with ``prime + 1`` marks.

    Put ``r_t = [alpha*(rotation+t)^2 + beta*(rotation+t)+gamma]_p`` and

        s_t = (2p + gap_translation)t + r_t-r_0,  0 <= t <= p.

    ``alpha`` must be nonzero modulo the odd prime.  The nonnegative gap
    translation is exactly the operation of adding the same integer to every
    Hegyvári gap.  More generally the proof works down to base ``2p-1``; this
    API deliberately mirrors the paper and only exposes nonnegative adds.
    """

    p = prime
    if p < 3 or p % 2 == 0 or not is_prime(p):
        raise ValueError("prime must be an odd prime")
    if alpha % p == 0:
        raise ValueError("alpha must be nonzero modulo prime")
    if gap_translation < 0:
        raise ValueError("gap_translation must be nonnegative")

    alpha %= p
    beta %= p
    gamma %= p
    rotation %= p
    base = 2 * p + gap_translation

    def residue(index: int) -> int:
        shifted = rotation + index
        return (alpha * shifted * shifted + beta * shifted + gamma) % p

    initial = residue(0)
    marks = tuple(base * index + residue(index) - initial for index in range(p + 1))
    if not is_golomb(marks):
        raise AssertionError("the exact affine Hegyvári proof has been violated")
    return marks


def hegyvari_gaps(*args: Any, **kwargs: Any) -> tuple[int, ...]:
    marks = hegyvari_marks(*args, **kwargs)
    return tuple(right - left for left, right in pairwise(marks))


@dataclass(frozen=True)
class HegvariAudit:
    prime: int
    mark_count: int
    gap_count: int
    endpoint: int
    minimum_gap: int
    maximum_gap: int
    proved_gap_lower_bound: int
    proved_gap_upper_bound: int
    positive_difference_count: int
    expected_positive_difference_count: int


def audit_original_construction(prime: int) -> HegvariAudit:
    """Audit the exact construction printed in Hegyvári (1986), Theorem 1."""

    marks = hegyvari_marks(prime)
    gaps = tuple(right - left for left, right in pairwise(marks))
    return HegvariAudit(
        prime=prime,
        mark_count=len(marks),
        gap_count=len(gaps),
        endpoint=marks[-1],
        minimum_gap=min(gaps),
        maximum_gap=max(gaps),
        proved_gap_lower_bound=prime + 1,
        proved_gap_upper_bound=3 * prime - 1,
        positive_difference_count=len(positive_differences(marks)),
        expected_positive_difference_count=comb(prime + 1, 2),
    )


@dataclass(frozen=True)
class ConsecutiveSumInequality:
    gap_count: int
    maximum_gap: int
    maximum_interval_length: int
    restricted_sum_count: int
    actual_restricted_sum_total: int
    distinct_positive_lower_bound: int
    occurrence_upper_bound: int
    distinct_gap_upper_bound: Fraction
    asymptotic_ratio_bound: Fraction


def hegyvari_upper_inequality(
    gaps: Sequence[int], maximum_interval_length: int
) -> ConsecutiveSumInequality:
    """Verify the exact inequality behind Hegyvári's ``2/3`` upper constant.

    For ``k`` positive gaps at most ``n``, retain all interval sums of lengths
    ``1,...,t``.  There are

        K = tk - t(t-1)/2

    such sums.  If they are distinct, their total is at least ``K(K+1)/2``.
    Each gap is counted at most ``t(t+1)/2`` times, and the length-one sums
    show that the gaps themselves are distinct, so their sum is at most
    ``k(2n-k+1)/2``.  Hence

        K(K+1)/2 <= t(t+1)k(2n-k+1)/4.

    With fixed ``t`` and ``k/n -> c``, the leading terms give
    ``c <= 2(t+1)/(3t+1)``, which tends to ``2/3`` as ``t`` tends to infinity.
    The same audit applies verbatim to every contiguous window of an infinite
    Golomb gap sequence.
    """

    values = tuple(gaps)
    if not values or any(not isinstance(value, int) or value <= 0 for value in values):
        raise ValueError("gaps must be a nonempty sequence of positive integers")
    k = len(values)
    t = maximum_interval_length
    if not 1 <= t <= k:
        raise ValueError("maximum_interval_length must lie in 1..len(gaps)")

    interval_sums = tuple(
        sum(values[left : left + length])
        for length in range(1, t + 1)
        for left in range(k - length + 1)
    )
    if len(interval_sums) != len(set(interval_sums)):
        raise ValueError("the selected consecutive sums are not distinct")

    count = t * k - t * (t - 1) // 2
    actual_total = sum(interval_sums)
    lower_bound = count * (count + 1) // 2
    occurrence_upper = t * (t + 1) // 2 * sum(values)
    n = max(values)
    distinct_gap_upper = Fraction(t * (t + 1) * k * (2 * n - k + 1), 4)
    if not lower_bound <= actual_total <= occurrence_upper <= distinct_gap_upper:
        raise AssertionError("Hegyvári's exact counting chain has been violated")

    return ConsecutiveSumInequality(
        gap_count=k,
        maximum_gap=n,
        maximum_interval_length=t,
        restricted_sum_count=count,
        actual_restricted_sum_total=actual_total,
        distinct_positive_lower_bound=lower_bound,
        occurrence_upper_bound=occurrence_upper,
        distinct_gap_upper_bound=distinct_gap_upper,
        asymptotic_ratio_bound=Fraction(2 * (t + 1), 3 * t + 1),
    )


@dataclass(frozen=True)
class CommonDifferenceWitness:
    difference: int
    first_pair: Pair
    second_pair: Pair


def common_difference_witness(
    first: Sequence[int], second: Sequence[int]
) -> CommonDifferenceWitness | None:
    """Return the least common positive internal difference, if one exists."""

    first_map = positive_difference_map(first)
    second_map = positive_difference_map(second)
    common = sorted(first_map.keys() & second_map.keys())
    if not common:
        return None
    difference = common[0]
    return CommonDifferenceWitness(
        difference=difference,
        first_pair=first_map[difference],
        second_pair=second_map[difference],
    )


def safe_separated_shift(first: Sequence[int], second: Sequence[int]) -> int:
    """A shift making every mixed difference larger than both diameters."""

    first_marks = _validated_ruler(first)
    second_marks = _validated_ruler(second)
    return first_marks[-1] + max(first_marks[-1], second_marks[-1]) + 1


def safely_splice(first: Sequence[int], second: Sequence[int]) -> tuple[int, ...]:
    """Safely shift and union two rulers if their internal differences are disjoint.

    Disjointness is necessary for *every* relative translation: if
    ``b_j-b_i = a_v-a_u``, then the two corresponding mixed differences are
    equal after any shift.  It is sufficient with the explicit large shift
    returned by :func:`safe_separated_shift`, because all mixed differences
    then lie above both internal-difference ranges.
    """

    first_marks = _validated_ruler(first)
    second_marks = _validated_ruler(second)
    witness = common_difference_witness(first_marks, second_marks)
    if witness is not None:
        raise ValueError(f"internal difference sets intersect at {witness.difference}")
    shift = safe_separated_shift(first_marks, second_marks)
    result = first_marks + tuple(shift + mark for mark in second_marks)
    if not is_golomb(result):
        raise AssertionError("the separated-splice criterion has been violated")
    return result


def affine_hegyvari_variants(
    prime: int, *, gap_translation: int = 0
) -> Iterator[tuple[tuple[int, int, int], tuple[int, ...]]]:
    """Yield distinct affine residue variants in deterministic order.

    The constant coefficient matters because standard residues in
    ``{0,...,p-1}`` are used before subtracting the initial residue.  Cyclic
    rotations are already represented by the full ``(beta, gamma)`` sweep.
    Duplicate normalized rulers are removed, retaining their first parameter
    triple.
    """

    if prime < 3 or prime % 2 == 0 or not is_prime(prime):
        raise ValueError("prime must be an odd prime")
    seen: set[tuple[int, ...]] = set()
    for alpha in range(1, prime):
        for beta in range(prime):
            for gamma in range(prime):
                marks = hegyvari_marks(
                    prime,
                    alpha=alpha,
                    beta=beta,
                    gamma=gamma,
                    gap_translation=gap_translation,
                )
                if marks in seen:
                    continue
                seen.add(marks)
                yield (alpha, beta, gamma), marks


def universal_affine_differences(
    prime: int, *, gap_translation: int = 0
) -> frozenset[int]:
    """Intersect the difference sets of every distinct affine variant."""

    rows = tuple(
        positive_differences(marks)
        for _, marks in affine_hegyvari_variants(prime, gap_translation=gap_translation)
    )
    if not rows:
        raise AssertionError("an odd prime must have affine variants")
    intersection = set(rows[0])
    for differences in rows[1:]:
        intersection.intersection_update(differences)
    return frozenset(intersection)


@dataclass(frozen=True)
class CompatibleVariant:
    gap_translation: int
    alpha: int
    beta: int
    gamma: int
    marks: tuple[int, ...]


def find_compatible_hegyvari_variant(
    old: Sequence[int],
    prime: int,
    *,
    maximum_gap_translation: int = 0,
) -> CompatibleVariant | None:
    """Find the first affine block with no internal difference used by ``old``."""

    old_marks = _validated_ruler(old)
    if maximum_gap_translation < 0:
        raise ValueError("maximum_gap_translation must be nonnegative")
    old_differences = positive_differences(old_marks)
    for gap_translation in range(maximum_gap_translation + 1):
        for (alpha, beta, gamma), marks in affine_hegyvari_variants(
            prime, gap_translation=gap_translation
        ):
            if old_differences.isdisjoint(positive_differences(marks)):
                return CompatibleVariant(
                    gap_translation=gap_translation,
                    alpha=alpha,
                    beta=beta,
                    gamma=gamma,
                    marks=marks,
                )
    return None


def embed_prescribed_differences(distances: Iterable[int]) -> tuple[int, ...]:
    """Embed any finite list of prescribed distances in a finite Golomb ruler.

    This gives an explicit obstruction to every *finite* menu of appended
    blocks: embed one internal difference from each menu item in the old
    ruler.  At an induction step with old diameter ``M``, put
    ``x=M+max(M,d)+1`` and realize a missing distance ``d`` by the new pair
    ``x,x+d``.  All new-to-old differences exceed ``max(M,d)``; the two fans
    can overlap only if ``d`` was already an old difference.
    """

    requested = tuple(distances)
    if not requested or any(
        not isinstance(value, int) or value <= 0 for value in requested
    ):
        raise ValueError("distances must be a nonempty iterable of positive integers")

    marks: tuple[int, ...] = (0, requested[0])
    for distance in requested[1:]:
        if distance in positive_differences(marks):
            continue
        diameter = marks[-1]
        new_left = diameter + max(diameter, distance) + 1
        marks = marks + (new_left, new_left + distance)
        if not is_golomb(marks):
            raise AssertionError("prescribed-difference embedding failed")
    return marks


def blocker_for_gap_translations(
    prime: int, maximum_gap_translation: int
) -> tuple[int, ...]:
    """Block every affine/cyclic variant for translations ``0..maximum``.

    Every full ``p``-gap variant has the parameter-independent diameter
    ``p(2p+t)``.  The returned old ruler contains all those diameters as
    internal differences.
    """

    if prime < 3 or prime % 2 == 0 or not is_prime(prime):
        raise ValueError("prime must be an odd prime")
    if maximum_gap_translation < 0:
        raise ValueError("maximum_gap_translation must be nonnegative")
    spans = tuple(
        prime * (2 * prime + translation)
        for translation in range(maximum_gap_translation + 1)
    )
    return embed_prescribed_differences(spans)


def enumerate_golomb_rulers(
    mark_count: int, maximum_endpoint: int
) -> Iterator[tuple[int, ...]]:
    """Exhaustively enumerate normalized rulers with endpoint at most the cap."""

    if mark_count < 2:
        raise ValueError("mark_count must be at least two")
    if maximum_endpoint < mark_count - 1:
        return

    def recurse(
        marks: tuple[int, ...], used: frozenset[int]
    ) -> Iterator[tuple[int, ...]]:
        if len(marks) == mark_count:
            yield marks
            return
        remaining_after_choice = mark_count - len(marks) - 1
        maximum_choice = maximum_endpoint - remaining_after_choice
        for candidate in range(marks[-1] + 1, maximum_choice + 1):
            new_differences = tuple(candidate - old for old in marks)
            if len(new_differences) != len(set(new_differences)):
                continue
            if not used.isdisjoint(new_differences):
                continue
            yield from recurse(marks + (candidate,), used | frozenset(new_differences))

    yield from recurse((0,), frozenset())


@dataclass(frozen=True)
class ExhaustiveSearchAudit:
    mark_count: int
    maximum_endpoint: int
    prime: int
    maximum_gap_translation: int
    ruler_count: int
    compatible_at_zero_count: int
    compatible_within_range_count: int
    incompatible_examples: tuple[tuple[int, ...], ...]
    largest_minimum_translation: int | None
    largest_minimum_translation_example: tuple[int, ...] | None


def exhaustive_compatibility_audit(
    *,
    mark_count: int,
    maximum_endpoint: int,
    prime: int,
    maximum_gap_translation: int,
) -> ExhaustiveSearchAudit:
    """Audit all small old rulers against all exact affine Hegyvári variants."""

    rulers = tuple(enumerate_golomb_rulers(mark_count, maximum_endpoint))
    variant_rows = tuple(
        (
            gap_translation,
            parameters,
            marks,
            positive_differences(marks),
        )
        for gap_translation in range(maximum_gap_translation + 1)
        for parameters, marks in affine_hegyvari_variants(
            prime, gap_translation=gap_translation
        )
    )
    compatible_at_zero = 0
    compatible_within = 0
    incompatible: list[tuple[int, ...]] = []
    largest_minimum: int | None = None
    largest_example: tuple[int, ...] | None = None

    for ruler in rulers:
        old_differences = positive_differences(ruler)
        result = next(
            (
                (gap_translation, parameters)
                for gap_translation, parameters, _, differences in variant_rows
                if old_differences.isdisjoint(differences)
            ),
            None,
        )
        if result is None:
            incompatible.append(ruler)
            continue
        gap_translation, _ = result
        compatible_within += 1
        if gap_translation == 0:
            compatible_at_zero += 1
        if largest_minimum is None or gap_translation > largest_minimum:
            largest_minimum = gap_translation
            largest_example = ruler

    return ExhaustiveSearchAudit(
        mark_count=mark_count,
        maximum_endpoint=maximum_endpoint,
        prime=prime,
        maximum_gap_translation=maximum_gap_translation,
        ruler_count=len(rulers),
        compatible_at_zero_count=compatible_at_zero,
        compatible_within_range_count=compatible_within,
        incompatible_examples=tuple(incompatible[:8]),
        largest_minimum_translation=largest_minimum,
        largest_minimum_translation_example=largest_example,
    )


def two_block_search(
    first_prime: int,
    second_prime: int,
    *,
    maximum_gap_translation: int = 0,
) -> dict[str, Any]:
    """Try to splice the original first block to an affine second block."""

    first = hegyvari_marks(first_prime)
    result = find_compatible_hegyvari_variant(
        first,
        second_prime,
        maximum_gap_translation=maximum_gap_translation,
    )
    if result is None:
        return {
            "first_prime": first_prime,
            "second_prime": second_prime,
            "compatible": False,
        }
    spliced = safely_splice(first, result.marks)
    return {
        "first_prime": first_prime,
        "second_prime": second_prime,
        "compatible": True,
        "gap_translation": result.gap_translation,
        "second_parameters": (
            result.alpha,
            result.beta,
            result.gamma,
        ),
        "shift": safe_separated_shift(first, result.marks),
        "mark_count": len(spliced),
        "endpoint": spliced[-1],
        "spliced": spliced,
    }


def endpoint_joined_two_block_search(
    first_prime: int,
    second_prime: int,
    *,
    maximum_gap_translation: int,
) -> dict[str, Any]:
    """Search exact end-to-start concatenations of two complete blocks."""

    first = hegyvari_marks(first_prime)
    for translation in range(maximum_gap_translation + 1):
        for parameters, second in affine_hegyvari_variants(
            second_prime, gap_translation=translation
        ):
            joined = first + tuple(first[-1] + mark for mark in second[1:])
            if not is_golomb(joined):
                continue
            return {
                "first_prime": first_prime,
                "second_prime": second_prime,
                "compatible": True,
                "gap_translation": translation,
                "second_parameters": parameters,
                "mark_count": len(joined),
                "endpoint": joined[-1],
                "joined": joined,
            }
    return {
        "first_prime": first_prime,
        "second_prime": second_prime,
        "compatible": False,
        "maximum_gap_translation": maximum_gap_translation,
    }


def untranslated_collision_histogram(
    first_prime: int, second_prime: int
) -> dict[int, int]:
    """Count least collision witnesses across all untranslated second variants."""

    first = hegyvari_marks(first_prime)
    histogram: dict[int, int] = {}
    for _, second in affine_hegyvari_variants(second_prime):
        witness = common_difference_witness(first, second)
        if witness is None:
            continue
        histogram[witness.difference] = histogram.get(witness.difference, 0) + 1
    return dict(sorted(histogram.items()))


def _json_ready(value: Any) -> Any:
    """Convert exact rationals and tuples to a stable JSON representation."""

    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, dict):
        return {key: _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    return value


def build_certificate() -> dict[str, Any]:
    """Build the small deterministic certificate used by the companion note."""

    audits = tuple(asdict(audit_original_construction(p)) for p in (3, 5, 7, 11))
    upper_inequalities = tuple(
        asdict(hegyvari_upper_inequality(hegyvari_gaps(11), t))
        for t in (1, 2, 4, 8, 11)
    )
    exhaustive = tuple(
        asdict(
            exhaustive_compatibility_audit(
                mark_count=marks,
                maximum_endpoint=endpoint,
                prime=prime,
                maximum_gap_translation=translation,
            )
        )
        for marks, endpoint, prime, translation in (
            (4, 16, 3, 3),
            (4, 20, 5, 2),
            (5, 25, 5, 3),
        )
    )
    full_coverage_exhaustive = tuple(
        asdict(
            exhaustive_compatibility_audit(
                mark_count=marks,
                maximum_endpoint=endpoint,
                prime=prime,
                maximum_gap_translation=endpoint - prime,
            )
        )
        for marks, endpoint, prime in (
            (4, 16, 3),
            (4, 20, 5),
            (5, 25, 5),
        )
    )
    blocker = blocker_for_gap_translations(5, 3)
    certificate = {
        "schema": "erdos1191.wave8.hegyvari_bridge.v1",
        "source": {
            "author": "N. Hegyvári",
            "title": "On consecutive sums in sequences",
            "journal": "Acta Mathematica Hungarica 48 (1986), 193-200",
            "primary_pdf": "https://real-j.mtak.hu/7472/1/MTA_ActaMathHung_48.pdf",
        },
        "original_construction_audits": audits,
        "upper_inequality_audits_for_p11": upper_inequalities,
        "universal_affine_difference_audits": tuple(
            {
                "prime": prime,
                "gap_translation": translation,
                "differences": sorted(
                    universal_affine_differences(prime, gap_translation=translation)
                ),
            }
            for prime, translation in ((3, 0), (5, 0), (5, 3), (7, 2))
        ),
        "exhaustive_old_prefix_searches": exhaustive,
        "magnitude_guaranteed_full_coverage_searches": full_coverage_exhaustive,
        "untranslated_two_block_searches": tuple(
            two_block_search(first, second)
            for first, second in ((3, 3), (3, 5), (5, 7), (7, 11))
        ),
        "untranslated_collision_histograms": {
            f"{first}_to_{second}": untranslated_collision_histogram(first, second)
            for first, second in ((3, 5), (5, 7), (7, 11))
        },
        "translated_two_block_searches": tuple(
            two_block_search(first, second, maximum_gap_translation=120)
            for first, second in ((3, 5), (5, 7), (7, 11), (11, 13))
        ),
        "endpoint_joined_two_block_searches": tuple(
            endpoint_joined_two_block_search(
                first,
                second,
                maximum_gap_translation=maximum,
            )
            for first, second, maximum in (
                (3, 5, 20),
                (5, 7, 40),
                (7, 11, 80),
                (11, 13, 120),
            )
        ),
        "translation_blocker": {
            "prime": 5,
            "maximum_gap_translation": 3,
            "universal_spans": tuple(5 * (10 + t) for t in range(4)),
            "old_ruler": blocker,
            "old_difference_count": len(positive_differences(blocker)),
            "blocks_every_translation": all(
                find_compatible_hegyvari_variant(blocker, 5, maximum_gap_translation=t)
                is None
                for t in range(4)
            ),
        },
    }
    return _json_ready(certificate)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    certificate = build_certificate()
    rendered = json.dumps(certificate, indent=2, sort_keys=True)
    if arguments.output is None:
        print(rendered)
        return
    arguments.output.write_text(rendered + "\n", encoding="utf-8")
    print(arguments.output)


if __name__ == "__main__":
    main()

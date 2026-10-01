"""Independent exact probe of the adjacent-epoch NN Hall candidate."""
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from random import Random

COUNTEREXAMPLE_POINTS = (
    0,
    1,
    18,
    34,
    79,
    127,
    171,
    218,
    319,
    415,
    509,
    613,
    710,
    808,
    903,
    1002,
)

COUNTEREXAMPLE_32_POINTS = (
    *COUNTEREXAMPLE_POINTS,
    1135,
    1385,
    1636,
    1885,
    2133,
    2380,
    2632,
    2885,
    3139,
    3396,
    3651,
    3909,
    4165,
    4424,
    4669,
    4930,
)

COUNTEREXAMPLE_64_POINTS = (
    *COUNTEREXAMPLE_32_POINTS,
    5080,
    5578,
    6074,
    6564,
    7066,
    7569,
    8079,
    8573,
    9040,
    9513,
    9970,
    10431,
    10852,
    11311,
    11723,
    12133,
    12607,
    13079,
    13488,
    13896,
    14303,
    14708,
    15109,
    15559,
    15961,
    16359,
    16765,
    17164,
    17618,
    18051,
    18451,
    18854,
)


@dataclass(frozen=True)
class NNFamily:
    epoch: int
    lag: int
    demand: int
    lower: int
    upper: int
    differences: tuple[int, ...]


@dataclass(frozen=True)
class NNPressure:
    old_epoch: int
    new_epoch: int
    lower: int
    upper: int
    width: int
    demand: int
    ratio: Fraction
    families: tuple[NNFamily, ...]


@dataclass(frozen=True)
class CandidateWitnessAudit:
    points: tuple[int, ...]
    is_golomb: bool
    pair_count: int
    difference_count: int
    sorted_difference_sha256: str
    prefix_moduli: tuple[int, ...]
    prefix_caps: tuple[int, ...]
    all_prefix_c1: bool
    pressure: NNPressure
    scaled_value: Fraction
    candidate_holds: bool


@dataclass(frozen=True)
class TargetedExtensionResult:
    parent_count: int
    target_count: int
    beam_width: int
    candidates_per_state: int
    seed: int
    target_gap: int
    expanded_state_count: int
    best_points: tuple[int, ...]


def _validated_points(points: Sequence[int], old_epoch: int) -> tuple[int, ...]:
    marks = tuple(points)
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if marks != tuple(sorted(set(marks))) or not marks or marks[0] != 0:
        raise ValueError("points must be normalized strictly increasing marks")
    if (
        not isinstance(old_epoch, int)
        or old_epoch < 4
        or old_epoch & (old_epoch - 1)
        or len(marks) < 2 * old_epoch
    ):
        raise ValueError("old_epoch must be dyadic and covered through 2*old_epoch")
    return marks


def _nn_families(marks: tuple[int, ...], epoch: int) -> tuple[NNFamily, ...]:
    boundary = epoch // 2
    rows: list[NNFamily] = []
    for lag in range(1, boundary):
        pairs = tuple(
            (left, left + lag) for left in range(boundary, epoch - lag)
        )
        if len(pairs) < 2:
            continue
        differences = tuple(marks[right] - marks[left] for left, right in pairs)
        rows.append(
            NNFamily(
                epoch=epoch,
                lag=lag,
                demand=len(pairs),
                lower=min(differences),
                upper=max(differences),
                differences=differences,
            )
        )
    return tuple(rows)


def _pressure_rank(pressure: NNPressure) -> tuple[Fraction, int, int, int, int]:
    return (
        pressure.ratio,
        pressure.demand,
        -pressure.width,
        -pressure.lower,
        -pressure.upper,
    )


def adjacent_nn_pressure(
    points: Sequence[int], *, old_epoch: int
) -> NNPressure:
    """Independently maximize two-epoch NN family demand / integer width."""
    marks = _validated_points(points, old_epoch)
    new_epoch = 2 * old_epoch
    families = _nn_families(marks, old_epoch) + _nn_families(marks, new_epoch)
    endpoints = tuple(
        sorted(
            {family.lower for family in families}
            | {family.upper for family in families}
        )
    )
    best: NNPressure | None = None
    for lower in endpoints:
        for upper in endpoints:
            if upper < lower:
                continue
            contained = tuple(
                family
                for family in families
                if lower <= family.lower and family.upper <= upper
            )
            if {family.epoch for family in contained} != {old_epoch, new_epoch}:
                continue
            demand = sum(family.demand for family in contained)
            width = upper - lower + 1
            candidate = NNPressure(
                old_epoch=old_epoch,
                new_epoch=new_epoch,
                lower=lower,
                upper=upper,
                width=width,
                demand=demand,
                ratio=Fraction(demand, width),
                families=contained,
            )
            if best is None or _pressure_rank(candidate) > _pressure_rank(best):
                best = candidate
    if best is None:
        raise ValueError("no two-epoch NN pressure exists at this level")
    return best


def scaled_candidate_value(pressure: NNPressure, *, old_epoch: int) -> Fraction:
    """Return the exact candidate value ``16*n*Lambda_NN**2``."""
    if pressure.old_epoch != old_epoch:
        raise ValueError("pressure and old_epoch disagree")
    return 16 * old_epoch * pressure.ratio * pressure.ratio


def _log_integer_interval(value: int, terms: int) -> tuple[Fraction, Fraction]:
    z = Fraction(value - 1, value + 1)
    lower = 2 * sum(
        (
            z ** (2 * index + 1) / (2 * index + 1)
            for index in range(terms)
        ),
        Fraction(0),
    )
    tail = 2 * z ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - z * z)
    )
    return lower, lower + tail


def critical_modulus_cap(mark_count: int) -> int:
    """Certify ``floor(2*n^2*log(n))`` by rational enclosures."""
    if not isinstance(mark_count, int) or mark_count < 2:
        raise ValueError("mark_count must be an integer at least two")
    factor = 2 * mark_count * mark_count
    terms = 4
    while True:
        lower, upper = _log_integer_interval(mark_count, terms)
        lower_floor = (factor * lower).numerator // (factor * lower).denominator
        upper_floor = (factor * upper).numerator // (factor * upper).denominator
        if lower_floor == upper_floor:
            return lower_floor
        terms *= 2
        if terms > 16384:
            raise ArithmeticError("log enclosure did not determine the cap")


def audit_candidate_witness(
    points: Sequence[int], *, old_epoch: int
) -> CandidateWitnessAudit:
    """Rebuild every difference, prefix cap, and candidate quantity."""
    marks = _validated_points(points, old_epoch)
    differences = tuple(
        marks[right] - marks[left]
        for left in range(len(marks))
        for right in range(left + 1, len(marks))
    )
    sorted_differences = tuple(sorted(differences))
    difference_count = len(set(differences))
    rendered = "\n".join(str(value) for value in sorted_differences) + "\n"
    prefix_moduli = tuple(marks[count - 1] + 1 for count in range(2, len(marks) + 1))
    prefix_caps = tuple(critical_modulus_cap(count) for count in range(2, len(marks) + 1))
    pressure = adjacent_nn_pressure(marks, old_epoch=old_epoch)
    scaled = scaled_candidate_value(pressure, old_epoch=old_epoch)
    return CandidateWitnessAudit(
        points=marks,
        is_golomb=difference_count == len(differences),
        pair_count=len(differences),
        difference_count=difference_count,
        sorted_difference_sha256=sha256(rendered.encode("ascii")).hexdigest(),
        prefix_moduli=prefix_moduli,
        prefix_caps=prefix_caps,
        all_prefix_c1=all(
            modulus <= cap for modulus, cap in zip(prefix_moduli, prefix_caps)
        ),
        pressure=pressure,
        scaled_value=scaled,
        candidate_holds=scaled <= 1,
    )


def targeted_extension_search(
    parent: Sequence[int],
    *,
    target_count: int,
    beam_width: int,
    candidates_per_state: int,
    seed: int,
    target_gap: int,
) -> TargetedExtensionResult:
    """Seeded beam favoring a narrow adjacent-gap family in the new block."""
    marks = tuple(parent)
    if marks != tuple(sorted(set(marks))) or not marks or marks[0] != 0:
        raise ValueError("parent must be normalized strictly increasing marks")
    if not isinstance(target_count, int) or target_count <= len(marks):
        raise ValueError("target_count must exceed the parent count")
    if any(
        not isinstance(value, int) or value < 1
        for value in (beam_width, candidates_per_state, target_gap)
    ) or not isinstance(seed, int):
        raise ValueError("beam parameters and target_gap must be positive integers")
    old_differences = frozenset(
        marks[right] - marks[left]
        for left in range(len(marks))
        for right in range(left + 1, len(marks))
    )
    if len(old_differences) != len(marks) * (len(marks) - 1) // 2:
        raise ValueError("parent must be a Golomb ruler")

    parent_count = len(marks)
    generator = Random(seed)
    beam: list[tuple[tuple[int, ...], frozenset[int]]] = [
        (marks, old_differences)
    ]
    expanded_state_count = 0
    for count in range(parent_count + 1, target_count + 1):
        maximum = critical_modulus_cap(count) - 1
        expanded: list[tuple[tuple[int, ...], frozenset[int]]] = []
        for state_marks, used in beam:
            lower = state_marks[-1] + 1
            if lower > maximum:
                continue
            proposed: list[int] = []
            for center_gap in (target_gap, 200, 300, 150, 350, 400):
                center = state_marks[-1] + center_gap
                proposed.extend(
                    range(max(lower, center - 12), min(maximum, center + 12) + 1)
                )
            span = maximum - lower + 1
            if span <= candidates_per_state:
                proposed.extend(range(lower, maximum + 1))
            else:
                proposed.extend(
                    generator.sample(
                        range(lower, maximum + 1),
                        min(4 * candidates_per_state, span),
                    )
                )
            seen: set[int] = set()
            for mark in proposed:
                if mark in seen:
                    continue
                seen.add(mark)
                new_differences = tuple(mark - old for old in state_marks)
                if (
                    len(new_differences) != len(set(new_differences))
                    or not used.isdisjoint(new_differences)
                ):
                    continue
                expanded.append(
                    (
                        (*state_marks, mark),
                        used.union(new_differences),
                    )
                )
        expanded_state_count += len(expanded)
        if not expanded:
            raise RuntimeError(f"beam died before reaching {count} marks")

        def partial_rank(
            state: tuple[tuple[int, ...], frozenset[int]],
        ) -> tuple[int, int, int, tuple[int, ...]]:
            state_marks = state[0]
            newborn_gaps = tuple(
                state_marks[index] - state_marks[index - 1]
                for index in range(parent_count + 1, len(state_marks))
            )
            spread = (
                max(newborn_gaps) - min(newborn_gaps)
                if newborn_gaps
                else 10**9
            )
            center_error = sum(abs(gap - target_gap) for gap in newborn_gaps)
            return (-spread, -center_error, -state_marks[-1], state_marks)

        expanded.sort(key=partial_rank, reverse=True)
        beam = expanded[:beam_width]

    best_points = beam[0][0]
    if target_count == 2 * parent_count and not parent_count & (parent_count - 1):
        scored = tuple(
            (
                scaled_candidate_value(
                    adjacent_nn_pressure(state_marks, old_epoch=parent_count),
                    old_epoch=parent_count,
                ),
                state_marks,
            )
            for state_marks, _ in beam
        )
        best_points = max(scored)[1]
    return TargetedExtensionResult(
        parent_count=parent_count,
        target_count=target_count,
        beam_width=beam_width,
        candidates_per_state=candidates_per_state,
        seed=seed,
        target_gap=target_gap,
        expanded_state_count=expanded_state_count,
        best_points=best_points,
    )

"""Exact finite probes for proposed improvements of the Wave 6 band ledger.

This module deliberately separates three things:

* complete scoring of a fixed finite Golomb ruler;
* exhaustive enumeration of the four-mark ``C=1`` search space; and
* incomplete, deterministic generation of adjacent-gap-swap variants.

Nothing here asserts that a retained finite ruler extends to an infinite
critical Sidon sequence.
"""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from wave6_collision_bands import (
    antidiagonal_threshold,
    dyadic_antidiagonal_band,
    dyadic_shell_profile,
)
from wave6_hall_candidate_probe import critical_modulus_cap

WAVE6_ARITHMETIC_CERTIFICATE_FILE_SHA256 = (
    "573098370f4def5593230bdacb8f9488325eaf67b0e7949c8adb606e1e71e15d"
)
WAVE6_ARITHMETIC_CERTIFICATE_INTERNAL_SHA256 = (
    "16a5e07165c767fe714f1044ae4c7c490265428e746653cfe40c385f0e9e671a"
)


def _validated_points(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or any(not isinstance(mark, int) for mark in marks)
        or marks != tuple(sorted(set(marks)))
        or marks[0] != 0
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    return marks


def dyadic_boundaries(point_count: int) -> tuple[int, ...]:
    """Return all ``m`` for which a complete ``m -> 2m`` shell exists."""
    if not isinstance(point_count, int) or point_count < 2:
        raise ValueError("point_count must be an integer at least two")
    rows: list[int] = []
    boundary = 1
    while 2 * boundary <= point_count:
        rows.append(boundary)
        boundary *= 2
    return tuple(rows)


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    marks = _validated_points(points)
    return tuple(
        marks[right] - marks[left]
        for left in range(len(marks))
        for right in range(left + 1, len(marks))
    )


def is_golomb(points: Sequence[int]) -> bool:
    differences = positive_differences(points)
    return len(differences) == len(set(differences))


def all_prefix_c1(points: Sequence[int]) -> bool:
    marks = _validated_points(points)
    return all(
        marks[count - 1] + 1 <= critical_modulus_cap(count)
        for count in range(2, len(marks) + 1)
    )


@dataclass(frozen=True)
class CrossAtom:
    difference: int
    epoch: int
    antidiagonal: int


def cross_antidiagonal_atoms(points: Sequence[int]) -> tuple[CrossAtom, ...]:
    """Return every actual difference counted by Wave 6 Theorem B."""
    marks = _validated_points(points)
    atoms: list[CrossAtom] = []
    for epoch in dyadic_boundaries(len(marks)):
        for antidiagonal in range(1, epoch + 1):
            band = dyadic_antidiagonal_band(
                marks,
                old_count=epoch,
                antidiagonal=antidiagonal,
            )
            atoms.extend(
                CrossAtom(value, epoch, antidiagonal) for value in band.differences
            )
    return tuple(sorted(atoms, key=lambda atom: (atom.difference, atom.epoch)))


@dataclass(frozen=True)
class RenewalHoleWitness:
    lower: int
    upper: int
    width: int
    occupancy: int
    epochs: tuple[int, ...]
    margin: int
    atoms: tuple[CrossAtom, ...]


def renewal_hole_candidate(points: Sequence[int]) -> RenewalHoleWitness:
    """Completely score the local renewal-hole candidate on one ruler.

    Candidate RH asserts for every integer interval ``K`` meeting at least
    two epochs that

    ``occupancy(K) + epoch_count(K) - 1 <= width(K)``.

    It suffices to scan intervals whose endpoints are occupied differences:
    shrinking any other interval to those endpoints keeps its atoms and can
    only reduce its width.
    """
    atoms = cross_antidiagonal_atoms(points)
    if len({atom.epoch for atom in atoms}) < 2:
        raise ValueError("at least two complete dyadic epochs are required")
    best: RenewalHoleWitness | None = None
    for left, first in enumerate(atoms):
        epochs: set[int] = set()
        for right in range(left, len(atoms)):
            last = atoms[right]
            epochs.add(last.epoch)
            if len(epochs) < 2:
                continue
            width = last.difference - first.difference + 1
            occupancy = right - left + 1
            candidate = RenewalHoleWitness(
                lower=first.difference,
                upper=last.difference,
                width=width,
                occupancy=occupancy,
                epochs=tuple(sorted(epochs)),
                margin=width - occupancy - (len(epochs) - 1),
                atoms=atoms[left : right + 1],
            )
            rank = (
                candidate.margin,
                candidate.width,
                -candidate.occupancy,
                candidate.lower,
                candidate.upper,
            )
            if best is None:
                best = candidate
            else:
                best_rank = (
                    best.margin,
                    best.width,
                    -best.occupancy,
                    best.lower,
                    best.upper,
                )
                if rank < best_rank:
                    best = candidate
    if best is None:
        raise AssertionError("two-epoch scan unexpectedly found no interval")
    return best


@dataclass(frozen=True)
class ThresholdActivation:
    threshold: Fraction
    weight: int
    epoch: int
    antidiagonal: int


def threshold_activations(points: Sequence[int]) -> tuple[ThresholdActivation, ...]:
    marks = _validated_points(points)
    rows: list[ThresholdActivation] = []
    for epoch in dyadic_boundaries(len(marks)):
        profile = dyadic_shell_profile(marks, old_count=epoch)
        for antidiagonal in range(1, epoch + 1):
            rows.append(
                ThresholdActivation(
                    threshold=antidiagonal_threshold(profile, antidiagonal),
                    weight=antidiagonal,
                    epoch=epoch,
                    antidiagonal=antidiagonal,
                )
            )
    return tuple(
        sorted(
            rows,
            key=lambda row: (
                row.threshold,
                row.epoch,
                row.antidiagonal,
            ),
        )
    )


def _activation_groups(
    activations: Sequence[ThresholdActivation],
) -> Iterator[tuple[Fraction, tuple[ThresholdActivation, ...]]]:
    index = 0
    while index < len(activations):
        threshold = activations[index].threshold
        end = index + 1
        while end < len(activations) and activations[end].threshold == threshold:
            end += 1
        yield threshold, tuple(activations[index:end])
        index = end


@dataclass(frozen=True)
class EpochSizeTaxRow:
    threshold: Fraction
    floor_threshold: int
    cumulative_weight: int
    active_epochs: tuple[int, ...]
    epoch_size_tax: int
    margin: int


@dataclass(frozen=True)
class AdjacentHalfOverlapDebt:
    threshold: Fraction
    active_epochs: tuple[int, ...]
    forced_old_epochs: tuple[int, ...]
    forced_new_epochs: tuple[int, ...]
    both_cheap_epochs: tuple[int, ...]
    epoch_size_tax: int
    maximum_distinct_adjacent_charge: int
    overlap_debt: int
    selected_boundary_overlap: int
    maximum_new_adjacent_charge: int
    total_charge_debt: int


def adjacent_half_overlap_debt(
    points: Sequence[int], threshold: Fraction | int
) -> AdjacentHalfOverlapDebt:
    """Quantify the exact nesting debt in the local cheap-half argument.

    At an active epoch ``m``, every old internal adjacent difference is at
    most ``mu^-+2D^-`` and every new internal adjacent difference is at most
    ``mu^++2D^+``.  At least one of these two bounds is at most
    ``tau_(m,1)``.  New-half gap-index sets are disjoint across dyadic
    epochs, whereas old-half sets are nested.  The returned maximum is the
    exact best union size obtainable from these certified adjacent sets.
    """
    marks = _validated_points(points)
    cutoff = Fraction(threshold)
    if cutoff < 0:
        raise ValueError("threshold must be nonnegative")
    active: list[int] = []
    forced_old: list[int] = []
    forced_new: list[int] = []
    both: list[int] = []
    for epoch in dyadic_boundaries(len(marks)):
        profile = dyadic_shell_profile(marks, old_count=epoch)
        activation = antidiagonal_threshold(profile, 1)
        if activation > cutoff:
            continue
        active.append(epoch)
        old_cheap = profile.old_mean + 2 * profile.old_discrepancy <= cutoff
        new_cheap = profile.shell_mean + 2 * profile.shell_discrepancy <= cutoff
        if not old_cheap and not new_cheap:
            raise AssertionError("active epoch has no certified cheap half")
        if old_cheap and new_cheap:
            both.append(epoch)
        elif old_cheap:
            forced_old.append(epoch)
        else:
            forced_new.append(epoch)

    tax = sum(epoch - 1 for epoch in active)
    if forced_old:
        last_forced_old = forced_old[-1]
        overlap_debt = sum(epoch - 1 for epoch in active if epoch < last_forced_old)
        selected_boundary_overlap = sum(epoch < last_forced_old for epoch in active)
    else:
        overlap_debt = 0
        selected_boundary_overlap = 0
    distinct_adjacent_charge = tax - overlap_debt
    new_adjacent_charge = distinct_adjacent_charge - selected_boundary_overlap
    return AdjacentHalfOverlapDebt(
        threshold=cutoff,
        active_epochs=tuple(active),
        forced_old_epochs=tuple(forced_old),
        forced_new_epochs=tuple(forced_new),
        both_cheap_epochs=tuple(both),
        epoch_size_tax=tax,
        maximum_distinct_adjacent_charge=distinct_adjacent_charge,
        overlap_debt=overlap_debt,
        selected_boundary_overlap=selected_boundary_overlap,
        maximum_new_adjacent_charge=new_adjacent_charge,
        total_charge_debt=tax - new_adjacent_charge,
    )


def epoch_size_tax_candidate(
    points: Sequence[int], *, minimum_active_epochs: int = 1
) -> EpochSizeTaxRow:
    """Completely score the strongest retained threshold candidate.

    Candidate EST asserts

    ``S(T) + sum_(active m) (m-1) <= floor(T)``.

    Between activation thresholds the left side is constant and the right
    side is nondecreasing, so checking every distinct activation threshold
    is complete for a fixed ruler.
    """
    if not isinstance(minimum_active_epochs, int) or minimum_active_epochs < 1:
        raise ValueError("minimum_active_epochs must be a positive integer")
    activations = threshold_activations(points)
    weight = 0
    active: set[int] = set()
    best: EpochSizeTaxRow | None = None
    for threshold, group in _activation_groups(activations):
        weight += sum(row.weight for row in group)
        active.update(row.epoch for row in group)
        if len(active) < minimum_active_epochs:
            continue
        floor_threshold = threshold.numerator // threshold.denominator
        tax = sum(epoch - 1 for epoch in active)
        candidate = EpochSizeTaxRow(
            threshold=threshold,
            floor_threshold=floor_threshold,
            cumulative_weight=weight,
            active_epochs=tuple(sorted(active)),
            epoch_size_tax=tax,
            margin=floor_threshold - weight - tax,
        )
        rank = (
            candidate.margin,
            candidate.threshold,
            candidate.cumulative_weight,
        )
        if best is None or rank < (
            best.margin,
            best.threshold,
            best.cumulative_weight,
        ):
            best = candidate
    if best is None:
        raise ValueError("the requested number of active epochs never occurs")
    return best


@dataclass(frozen=True)
class HarmonicTaxRow:
    threshold: Fraction
    ceiling_threshold: int
    cumulative_weight: int
    active_epochs: tuple[int, ...]
    harmonic_number: Fraction
    reciprocal_threshold_sum: Fraction
    proposed_tax: Fraction
    margin: Fraction


def harmonic_epoch_tax_candidate(
    points: Sequence[int], *, minimum_active_epochs: int = 2
) -> HarmonicTaxRow:
    """Score a direct harmonic-renewal strengthening of Theorem D.

    With ``W`` activated unit weights, candidate HT asserts

    ``H_W - sum_(tau<=T) k/tau >= (E(T)-1)/ceil(T)``.

    The score is exact: all quantities are ``Fraction`` objects.
    """
    if not isinstance(minimum_active_epochs, int) or minimum_active_epochs < 1:
        raise ValueError("minimum_active_epochs must be a positive integer")
    activations = threshold_activations(points)
    weight = 0
    harmonic = Fraction(0)
    reciprocal_sum = Fraction(0)
    active: set[int] = set()
    best: HarmonicTaxRow | None = None
    for threshold, group in _activation_groups(activations):
        added_weight = sum(row.weight for row in group)
        for rank in range(weight + 1, weight + added_weight + 1):
            harmonic += Fraction(1, rank)
        weight += added_weight
        reciprocal_sum += sum(
            (Fraction(row.weight, 1) / row.threshold for row in group),
            Fraction(0),
        )
        active.update(row.epoch for row in group)
        if len(active) < minimum_active_epochs:
            continue
        ceiling = -(-threshold.numerator // threshold.denominator)
        tax = Fraction(len(active) - 1, ceiling)
        candidate = HarmonicTaxRow(
            threshold=threshold,
            ceiling_threshold=ceiling,
            cumulative_weight=weight,
            active_epochs=tuple(sorted(active)),
            harmonic_number=harmonic,
            reciprocal_threshold_sum=reciprocal_sum,
            proposed_tax=tax,
            margin=harmonic - reciprocal_sum - tax,
        )
        rank = (candidate.margin, candidate.threshold, candidate.cumulative_weight)
        if best is None or rank < (
            best.margin,
            best.threshold,
            best.cumulative_weight,
        ):
            best = candidate
    if best is None:
        raise ValueError("the requested number of active epochs never occurs")
    return best


def enumerate_compatible_four_mark_rulers() -> Iterator[tuple[int, ...]]:
    """Exhaust the normalized four-mark all-prefix ``C=1`` search space."""
    cap2 = critical_modulus_cap(2)
    cap3 = critical_modulus_cap(3)
    cap4 = critical_modulus_cap(4)
    for first in range(1, cap2):
        for second in range(first + 1, cap3):
            for third in range(second + 1, cap4):
                points = (0, first, second, third)
                if is_golomb(points):
                    yield points


def enumerate_bounded_four_mark_golomb(
    *, maximum_last_mark: int
) -> Iterator[tuple[int, ...]]:
    """Exhaust normalized four-mark Golomb rulers with a bounded last mark."""
    if not isinstance(maximum_last_mark, int) or maximum_last_mark < 6:
        raise ValueError("maximum_last_mark must be an integer at least six")
    for first in range(1, maximum_last_mark - 1):
        for second in range(first + 1, maximum_last_mark):
            for third in range(second + 1, maximum_last_mark + 1):
                points = (0, first, second, third)
                if is_golomb(points):
                    yield points


def enumerate_four_mark_est_failure_region() -> Iterator[tuple[int, ...]]:
    """Exhaust the bounded region containing every possible 4-mark EST failure."""
    for first in range(1, 5):
        for second in range(first + 1, first + 5):
            for third in range(second + 1, first + 6):
                points = (0, first, second, third)
                if is_golomb(points):
                    yield points


@dataclass(frozen=True)
class ShortShellEightMarkAudit:
    maximum_shell_span: int
    maximum_parent_last_mark: int
    parent_count: int
    extension_count: int
    search_node_count: int
    minimum_four_times_first_threshold: int
    minimum_threshold_points: tuple[int, ...]


def short_shell_eight_mark_audit(
    *, maximum_shell_span: int = 35, maximum_parent_last_mark: int = 34
) -> ShortShellEightMarkAudit:
    """Exhaust the only 8-mark region where EST can first fail.

    At the first ``m=4`` activation a failure requires ``floor(tau_4,1)``
    at most eight.  Since ``tau_4,1 >= M_4``, this forces both
    ``N_4=a_3+1 <= 35`` and the new-shell span ``G_4=a_7-a_3 <= 35``.
    This routine exhausts that bounded region without assuming any early
    ``C=1`` prefix cap.  It computes ``4*tau_4,1`` entirely with integers.
    """
    if not isinstance(maximum_shell_span, int) or maximum_shell_span < 4:
        raise ValueError("maximum_shell_span must be an integer at least four")
    if not isinstance(maximum_parent_last_mark, int) or maximum_parent_last_mark < 6:
        raise ValueError("maximum_parent_last_mark must be an integer at least six")
    parent_count = 0
    extension_count = 0
    search_node_count = 0
    best: tuple[int, tuple[int, ...]] | None = None

    for parent in enumerate_bounded_four_mark_golomb(
        maximum_last_mark=maximum_parent_last_mark
    ):
        parent_count += 1
        used = frozenset(positive_differences(parent))
        parent_last = parent[-1]
        prefix_moduli = (0, 1, parent[1] + 1, parent[2] + 1, parent[3] + 1)
        old_modulus = prefix_moduli[4]
        four_times_old_discrepancy = max(
            abs(4 * prefix_moduli[rank] - rank * old_modulus) for rank in range(5)
        )

        def extend(
            partial: tuple[int, ...],
            partial_differences: frozenset[int],
        ) -> None:
            nonlocal extension_count, search_node_count, best
            if len(partial) == 8:
                extension_count += 1
                shell_span = partial[7] - parent_last
                four_times_shell_discrepancy = max(
                    abs(4 * (partial[3 + rank] - parent_last) - rank * shell_span)
                    for rank in range(5)
                )
                four_times_threshold = (
                    four_times_old_discrepancy
                    + four_times_shell_discrepancy
                    + max(old_modulus, shell_span)
                )
                candidate = (four_times_threshold, partial)
                if best is None or candidate < best:
                    best = candidate
                return

            remaining = 8 - len(partial)
            maximum_mark = parent_last + maximum_shell_span
            for mark in range(
                partial[-1] + 1,
                maximum_mark - remaining + 2,
            ):
                search_node_count += 1
                new_differences = tuple(mark - old for old in partial)
                if len(new_differences) == len(
                    set(new_differences)
                ) and partial_differences.isdisjoint(new_differences):
                    extend(
                        (*partial, mark),
                        partial_differences.union(new_differences),
                    )

        extend(parent, used)

    if best is None:
        raise AssertionError("short-shell eight-mark audit unexpectedly empty")
    return ShortShellEightMarkAudit(
        maximum_shell_span=maximum_shell_span,
        maximum_parent_last_mark=maximum_parent_last_mark,
        parent_count=parent_count,
        extension_count=extension_count,
        search_node_count=search_node_count,
        minimum_four_times_first_threshold=best[0],
        minimum_threshold_points=best[1],
    )


def points_from_gaps(gaps: Sequence[int]) -> tuple[int, ...]:
    points = [0]
    for gap in gaps:
        if not isinstance(gap, int) or gap < 1:
            raise ValueError("gaps must be positive integers")
        points.append(points[-1] + gap)
    return tuple(points)


@dataclass(frozen=True)
class GapSwapVariant:
    swapped_gap_index: int
    points: tuple[int, ...]


def compatible_adjacent_gap_swaps(points: Sequence[int]) -> tuple[GapSwapVariant, ...]:
    """Deterministically test every single adjacent-gap swap.

    Generation is exhaustive only within this explicitly bounded mutation
    class.  Every returned variant receives a fresh Golomb and prefix-cap
    audit rather than inheriting validity from its parent.
    """
    marks = _validated_points(points)
    gaps = [marks[index] - marks[index - 1] for index in range(1, len(marks))]
    rows: list[GapSwapVariant] = []
    for index in range(len(gaps) - 1):
        mutated = gaps.copy()
        mutated[index], mutated[index + 1] = mutated[index + 1], mutated[index]
        candidate = points_from_gaps(mutated)
        if candidate != marks and is_golomb(candidate) and all_prefix_c1(candidate):
            rows.append(GapSwapVariant(index, candidate))
    return tuple(rows)


@dataclass(frozen=True)
class AuthenticatedFixtures:
    certificate_file_sha256: str
    sixty_four_mark_points: tuple[tuple[int, ...], ...]
    one_hundred_twenty_eight_mark_points: tuple[int, ...]


def load_authenticated_wave6_fixtures(path: str | Path) -> AuthenticatedFixtures:
    certificate_path = Path(path)
    raw = certificate_path.read_bytes()
    file_hash = sha256(raw).hexdigest()
    if file_hash != WAVE6_ARITHMETIC_CERTIFICATE_FILE_SHA256:
        raise ValueError("Wave 6 arithmetic certificate file hash mismatch")
    payload = json.loads(raw)
    if (
        payload.get("certificate_sha256")
        != WAVE6_ARITHMETIC_CERTIFICATE_INTERNAL_SHA256
    ):
        raise ValueError("Wave 6 arithmetic certificate internal hash mismatch")
    sixty_four = tuple(
        tuple(row["arithmetic_audit"]["points"])
        for row in payload["sixty_four_mark_witnesses"]
    )
    one_twenty_eight = tuple(
        payload["heuristic_extension_128"]["arithmetic_audit"]["points"]
    )
    if len(sixty_four) != 6 or any(len(points) != 64 for points in sixty_four):
        raise ValueError("unexpected authenticated 64-mark fixture count")
    if len(one_twenty_eight) != 128:
        raise ValueError("unexpected authenticated 128-mark fixture length")
    return AuthenticatedFixtures(file_hash, sixty_four, one_twenty_eight)

"""Exact adversarial probes for the Wave 8 density--innovation bridge.

The literal local candidate is

    U_global(T) / T >= <H, Q_m / N_(2m)>,

at a Wave 6 activation threshold.  This module keeps three logically
different statements separate:

* an exhaustive four-mark refutation of the literal candidate inside the
  all-prefix ``C=1`` class;
* deterministic finite searches for a possible later (``m >= 4``) repair;
* exact audits of a scale-invariant square-weighted replacement and of a very
  weak conditional critical-cap factor.

All reported witnesses are replayed with integers and ``Fraction``.  Finite
survival depth is recorded only as a finite tree statement.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from random import Random
from typing import Any

from gap_measure_dynamics import dyadic_gap_matrix_update
from innovation_budget import LYAPUNOV_MATRIX, frobenius_inner
from wave6_collision_bands import antidiagonal_threshold, dyadic_shell_profile
from wave6_hall_candidate_probe import critical_modulus_cap
from wave7_band_renewal_probe import (
    all_prefix_c1,
    dyadic_boundaries,
    enumerate_compatible_four_mark_rulers,
    is_golomb,
)
from wave8_survival_debt_probe import critical_survival_audit

Pair = tuple[int, int]
UNIVERSAL_INNOVATION_UPPER_BOUND = Fraction(3, 4)
FOUR_MARK_INITIAL_ERROR = Fraction(137, 10_976)

FOUR_MARK_LOCAL_COUNTEREXAMPLE = (0, 1, 4, 6)
LATEST_SHELL_COUNTEREXAMPLE = (0, 4, 5, 7, 78, 86, 166, 199)
EIGHT_MARK_FINITE_WITNESS = (0, 2, 3, 8, 79, 128, 161, 234)
SIXTEEN_MARK_FINITE_WITNESS = (
    0,
    3,
    18,
    27,
    34,
    84,
    94,
    200,
    261,
    317,
    437,
    473,
    512,
    690,
    743,
    1384,
)
UNRESTRICTED_BASE = (0, 8, 24, 56, 58, 314, 318, 319)
UNRESTRICTED_SCALE = 100


def _validated_points(
    points: Sequence[int], *, require_c1: bool = False
) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 4
        or len(marks) & (len(marks) - 1)
        or marks[0] != 0
        or any(not isinstance(mark, int) for mark in marks)
        or marks != tuple(sorted(set(marks)))
    ):
        raise ValueError(
            "points must be a normalized, power-of-two-length integer ruler"
        )
    if not is_golomb(marks):
        raise ValueError("points must be a Golomb ruler")
    if require_c1 and not all_prefix_c1(marks):
        raise ValueError("points must obey every C=1 prefix cap")
    return marks


def _wave6_pairs(
    points: tuple[int, ...], threshold: Fraction
) -> tuple[tuple[int, ...], frozenset[Pair]]:
    active: list[int] = []
    pairs: set[Pair] = set()
    for epoch in dyadic_boundaries(len(points)):
        profile = dyadic_shell_profile(points, old_count=epoch)
        if antidiagonal_threshold(profile, 1) <= threshold:
            active.append(epoch)
        for antidiagonal in range(1, epoch + 1):
            if antidiagonal_threshold(profile, antidiagonal) > threshold:
                continue
            pairs.update(
                (
                    epoch - 1 - offset,
                    epoch - 1 + antidiagonal - offset,
                )
                for offset in range(antidiagonal)
            )
    return tuple(active), frozenset(pairs)


@dataclass(frozen=True)
class DensityEvent:
    points: tuple[int, ...]
    epoch: int
    antidiagonal: int
    threshold: Fraction
    floor_threshold: int
    active_epochs: tuple[int, ...]
    wave6_pair_count: int
    global_reservoir_count: int
    latest_reservoir_count: int
    normalized_adjoint_innovation: Fraction
    global_density: Fraction
    latest_density: Fraction
    global_margin: Fraction
    latest_margin: Fraction
    global_square_asset: Fraction
    latest_square_asset: Fraction
    global_square_margin: Fraction
    latest_square_margin: Fraction


def density_event(
    points: Sequence[int], *, old_count: int, antidiagonal: int
) -> DensityEvent:
    """Audit one exact activation of the newest complete dyadic epoch."""
    marks = _validated_points(points)
    if (
        not isinstance(old_count, int)
        or old_count < 2
        or old_count & (old_count - 1)
        or len(marks) != 2 * old_count
        or not isinstance(antidiagonal, int)
        or not 1 <= antidiagonal <= old_count
    ):
        raise ValueError("require len(points)=2*old_count and 1 <= k <= old_count")

    profile = dyadic_shell_profile(marks, old_count=old_count)
    threshold = antidiagonal_threshold(profile, antidiagonal)
    cutoff = threshold.numerator // threshold.denominator
    active, wave6_pairs = _wave6_pairs(marks, threshold)
    if not active or max(active) != old_count:
        raise AssertionError("the requested newest epoch did not activate")

    history_pairs = {
        (left, right)
        for right in range(2 * old_count)
        for left in range(right - 1)
        if marks[right] - marks[left] <= cutoff
    }
    latest_pairs = {
        (left, right)
        for right in range(old_count, 2 * old_count)
        for left in range(right - 1)
        if marks[right] - marks[left] <= cutoff
    }
    global_reservoir = history_pairs.difference(wave6_pairs)
    latest_reservoir = latest_pairs.difference(wave6_pairs)

    update = dyadic_gap_matrix_update(marks, old_count)
    innovation = (
        frobenius_inner(LYAPUNOV_MATRIX, update.innovation) / update.new_modulus
    )
    global_density = Fraction(len(global_reservoir), 1) / threshold
    latest_density = Fraction(len(latest_reservoir), 1) / threshold
    global_square = sum(
        (
            Fraction((marks[right] - marks[left]) ** 2, 1) / threshold**2
            for left, right in global_reservoir
        ),
        Fraction(0),
    )
    latest_square = sum(
        (
            Fraction((marks[right] - marks[left]) ** 2, 1) / threshold**2
            for left, right in latest_reservoir
        ),
        Fraction(0),
    )
    return DensityEvent(
        points=marks,
        epoch=old_count,
        antidiagonal=antidiagonal,
        threshold=threshold,
        floor_threshold=cutoff,
        active_epochs=active,
        wave6_pair_count=len(wave6_pairs),
        global_reservoir_count=len(global_reservoir),
        latest_reservoir_count=len(latest_reservoir),
        normalized_adjoint_innovation=innovation,
        global_density=global_density,
        latest_density=latest_density,
        global_margin=global_density - innovation,
        latest_margin=latest_density - innovation,
        global_square_asset=global_square,
        latest_square_asset=latest_square,
        global_square_margin=global_square - innovation,
        latest_square_margin=latest_square - innovation,
    )


def latest_epoch_events(points: Sequence[int]) -> tuple[DensityEvent, ...]:
    """Return every newest-epoch activation, with exact post-audit."""
    marks = _validated_points(points)
    epoch = len(marks) // 2
    return tuple(
        density_event(marks, old_count=epoch, antidiagonal=antidiagonal)
        for antidiagonal in range(1, epoch + 1)
    )


@dataclass(frozen=True)
class FourMarkExhaustiveAudit:
    ruler_count: int
    activation_event_count: int
    negative_global_event_count: int
    negative_square_event_count: int
    minimum_global_event: DensityEvent
    minimum_square_event: DensityEvent


def exhaustive_four_mark_audit() -> FourMarkExhaustiveAudit:
    """Exhaust every four-mark all-prefix-C=1 ruler and both m=2 activations."""
    rulers = tuple(enumerate_compatible_four_mark_rulers())
    events = tuple(event for points in rulers for event in latest_epoch_events(points))
    return FourMarkExhaustiveAudit(
        ruler_count=len(rulers),
        activation_event_count=len(events),
        negative_global_event_count=sum(event.global_margin < 0 for event in events),
        negative_square_event_count=sum(
            event.global_square_margin < 0 for event in events
        ),
        minimum_global_event=min(
            events,
            key=lambda event: (event.global_margin, event.threshold, event.points),
        ),
        minimum_square_event=min(
            events,
            key=lambda event: (
                event.global_square_margin,
                event.threshold,
                event.points,
            ),
        ),
    )


@dataclass(frozen=True)
class CapFactorAudit:
    event: DensityEvent
    terminal_cap: int
    first_threshold_below_modulus: bool
    innovation_below_universal_bound: bool
    reservoir_nonempty: bool
    exact_factor: Fraction
    factored_margin: Fraction | None


def conditional_c1_cap_factor(points: Sequence[int]) -> CapFactorAudit:
    """Verify the weak first-activation factor, conditional on ``U >= 1``.

    If ``K=critical_modulus_cap(2m)``, the exact implication is

        U/T >= (4/(3K)) * <H,Q_m/N_(2m)>

    whenever the ruler is all-prefix C=1 and its global reservoir is nonempty.
    The implication is far too weak for P13 and is not asserted when ``U=0``.
    """
    marks = _validated_points(points, require_c1=True)
    event = density_event(marks, old_count=len(marks) // 2, antidiagonal=1)
    modulus = marks[-1] + 1
    cap = critical_modulus_cap(len(marks))
    factor = Fraction(4, 3 * cap)
    margin = (
        event.global_density - factor * event.normalized_adjoint_innovation
        if event.global_reservoir_count
        else None
    )
    if modulus > cap:
        raise AssertionError("the all-prefix cap audit failed")
    if event.threshold >= modulus:
        raise AssertionError("the first activation threshold must be below N_(2m)")
    if event.normalized_adjoint_innovation > UNIVERSAL_INNOVATION_UPPER_BOUND:
        raise AssertionError("the universal innovation upper bound failed")
    if margin is not None and margin < 0:
        raise AssertionError("the conditional critical-cap factor failed")
    return CapFactorAudit(
        event=event,
        terminal_cap=cap,
        first_threshold_below_modulus=True,
        innovation_below_universal_bound=True,
        reservoir_nonempty=bool(event.global_reservoir_count),
        exact_factor=factor,
        factored_margin=margin,
    )


def renewal_outstanding_transition(
    *, had_older_debt: bool, ancestry_cleared: bool, new_family_paid: bool
) -> bool:
    """Return whether an adjacent family remains unpaid after one epoch.

    In the ``new-pay-only`` case, an older debt is retained: payment of the
    current family is not a certificate for any older actual threshold.
    """
    if not ancestry_cleared and not new_family_paid:
        raise ValueError("the renewal dichotomy requires at least one paid side")
    older_survives = had_older_debt and not ancestry_cleared
    current_is_born_unpaid = not new_family_paid
    if older_survives and current_is_born_unpaid:
        raise AssertionError("the renewal dichotomy created two debts")
    return older_survives or current_is_born_unpaid


def _random_c1_ruler(mark_count: int, rng: Random, mode: int) -> tuple[int, ...] | None:
    points = [0]
    differences: set[int] = set()
    for count in range(2, mark_count + 1):
        cap = critical_modulus_cap(count) - 1
        candidates: list[int] = []
        for mark in range(points[-1] + 1, cap + 1):
            new_differences = tuple(mark - old for old in points)
            if len(new_differences) == len(
                set(new_differences)
            ) and differences.isdisjoint(new_differences):
                candidates.append(mark)
        if not candidates:
            return None
        if mode == 0:
            pool = candidates
        elif mode == 1:
            pool = candidates[: max(1, len(candidates) // 3)]
        elif mode == 2:
            pool = candidates[len(candidates) // 2 :]
        else:
            third = len(candidates) // 3
            pool = candidates[2 * third :] if count % 2 else candidates[: third or 1]
        mark = rng.choice(pool)
        differences.update(mark - old for old in points)
        points.append(mark)
    return tuple(points)


@dataclass(frozen=True)
class DeterministicSearchAudit:
    mark_count: int
    seed: int
    requested_trials: int
    generated_ruler_count: int
    unique_ruler_count: int
    activation_event_count: int
    negative_global_event_count: int
    negative_square_event_count: int
    minimum_global_event: DensityEvent
    minimum_square_event: DensityEvent
    finite_survival_depth: int
    minimum_witness_survival_level_counts: tuple[int, ...]
    infinite_survival_inferred: bool


def deterministic_c1_search(
    *, mark_count: int, trials: int, seed: int, survival_depth: int = 1
) -> DeterministicSearchAudit:
    """Run a reproducible full-cap random search and exact post-audit.

    This is an adversarial finite search, not an exhaustive enumeration of the
    full C=1 space.  One fixed hard witness is inserted before the generated
    rulers so regression tests retain the strongest audited finite example.
    """
    if mark_count not in (8, 16):
        raise ValueError("this search is calibrated for 8 or 16 marks")
    if not isinstance(trials, int) or trials < 0:
        raise ValueError("trials must be a nonnegative integer")
    if not isinstance(seed, int):
        raise TypeError("seed must be an integer")
    if not isinstance(survival_depth, int) or survival_depth < 0:
        raise ValueError("survival_depth must be nonnegative")

    anchor = (
        EIGHT_MARK_FINITE_WITNESS if mark_count == 8 else SIXTEEN_MARK_FINITE_WITNESS
    )
    rng = Random(seed)
    generated: list[tuple[int, ...]] = []
    for trial in range(trials):
        points = _random_c1_ruler(mark_count, rng, trial % 4)
        if points is not None:
            generated.append(points)
    rulers = tuple(dict.fromkeys((anchor, *generated)))
    if any(not all_prefix_c1(points) or not is_golomb(points) for points in rulers):
        raise AssertionError("the deterministic generator emitted an invalid ruler")
    events = tuple(event for points in rulers for event in latest_epoch_events(points))
    minimum_global = min(
        events,
        key=lambda event: (event.global_margin, event.threshold, event.points),
    )
    minimum_square = min(
        events,
        key=lambda event: (
            event.global_square_margin,
            event.threshold,
            event.points,
        ),
    )
    survival = critical_survival_audit(
        minimum_global.points,
        depth=survival_depth,
    )
    return DeterministicSearchAudit(
        mark_count=mark_count,
        seed=seed,
        requested_trials=trials,
        generated_ruler_count=len(generated),
        unique_ruler_count=len(rulers),
        activation_event_count=len(events),
        negative_global_event_count=sum(event.global_margin < 0 for event in events),
        negative_square_event_count=sum(
            event.global_square_margin < 0 for event in events
        ),
        minimum_global_event=minimum_global,
        minimum_square_event=minimum_square,
        finite_survival_depth=survival_depth,
        minimum_witness_survival_level_counts=survival.level_counts,
        infinite_survival_inferred=False,
    )


@dataclass(frozen=True)
class CumulativeFirstCrossAudit:
    points: tuple[int, ...]
    events: tuple[DensityEvent, ...]
    innovation_sum: Fraction
    global_density_sum: Fraction
    square_asset_sum: Fraction
    corrected_global_margin: Fraction
    corrected_square_margin: Fraction


def cumulative_first_cross_audit(points: Sequence[int]) -> CumulativeFirstCrossAudit:
    """Audit a finite initial-error repair along one finite dyadic prefix."""
    marks = _validated_points(points)
    events = tuple(
        density_event(marks[: 2 * epoch], old_count=epoch, antidiagonal=1)
        for epoch in dyadic_boundaries(len(marks))
        if epoch >= 2
    )
    innovations = sum(
        (event.normalized_adjoint_innovation for event in events), Fraction(0)
    )
    densities = sum((event.global_density for event in events), Fraction(0))
    squares = sum((event.global_square_asset for event in events), Fraction(0))
    return CumulativeFirstCrossAudit(
        points=marks,
        events=events,
        innovation_sum=innovations,
        global_density_sum=densities,
        square_asset_sum=squares,
        corrected_global_margin=densities + FOUR_MARK_INITIAL_ERROR - innovations,
        corrected_square_margin=squares + FOUR_MARK_INITIAL_ERROR - innovations,
    )


def unrestricted_scaling_event() -> DensityEvent:
    """Replay the known scaling counterexample to the unconditioned bridge."""
    points = tuple(UNRESTRICTED_SCALE * mark for mark in UNRESTRICTED_BASE)
    return density_event(points, old_count=4, antidiagonal=1)


@lru_cache(maxsize=1)
def mian_chowla_third_at_661_points() -> tuple[int, ...]:
    """Reconstruct the reported 682-mark perturbed Mian--Chowla fixture.

    Starting at ``b_0=0``, take the least admissible next mark except at
    index 661, where the third admissible mark is selected.  Then resume the
    least-admissible rule through index 681.
    """
    points = [0]
    used_differences: set[int] = set()
    for index in range(1, 682):
        requested_rank = 3 if index == 661 else 1
        admissible_seen = 0
        candidate = points[-1] + 1
        while True:
            new_differences: list[int] = []
            for old in reversed(points):
                difference = candidate - old
                if difference in used_differences:
                    break
                new_differences.append(difference)
            else:
                admissible_seen += 1
                if admissible_seen == requested_rank:
                    points.append(candidate)
                    used_differences.update(new_differences)
                    break
            candidate += 1
    expected_difference_count = len(points) * (len(points) - 1) // 2
    if len(used_differences) != expected_difference_count:
        raise AssertionError("the long fixture lost Golomb difference uniqueness")
    return tuple(points)


@dataclass(frozen=True)
class CompactDensityEvent:
    epoch: int
    antidiagonal: int
    threshold: Fraction
    global_reservoir_count: int
    normalized_adjoint_innovation: Fraction
    global_margin: Fraction
    global_square_margin: Fraction


def _fast_latest_epoch_events(
    points: Sequence[int], *, old_count: int
) -> tuple[CompactDensityEvent, ...]:
    """Audit all newest-epoch activations after one shared exact precompute."""
    marks = tuple(points[: 2 * old_count])
    if len(marks) != 2 * old_count:
        raise ValueError("the requested dyadic prefix is unavailable")

    families: list[tuple[Fraction, tuple[Pair, ...]]] = []
    for epoch in dyadic_boundaries(len(marks)):
        profile = dyadic_shell_profile(marks, old_count=epoch)
        for antidiagonal in range(1, epoch + 1):
            threshold = antidiagonal_threshold(profile, antidiagonal)
            pairs = tuple(
                (
                    epoch - 1 - offset,
                    epoch - 1 + antidiagonal - offset,
                )
                for offset in range(antidiagonal)
            )
            families.append((threshold, pairs))
    families.sort(key=lambda row: row[0])

    history = sorted(
        (
            marks[right] - marks[left],
            (left, right),
        )
        for right in range(2 * old_count)
        for left in range(right - 1)
    )
    update = dyadic_gap_matrix_update(marks, old_count)
    innovation = (
        frobenius_inner(LYAPUNOV_MATRIX, update.innovation) / update.new_modulus
    )
    profile = dyadic_shell_profile(marks, old_count=old_count)
    targets = tuple(
        (antidiagonal_threshold(profile, antidiagonal), antidiagonal)
        for antidiagonal in range(1, old_count + 1)
    )

    family_index = 0
    history_index = 0
    history_square = 0
    selected: set[Pair] = set()
    selected_nonadjacent_count = 0
    selected_nonadjacent_square = 0
    events: list[CompactDensityEvent] = []
    for threshold, antidiagonal in targets:
        while family_index < len(families) and families[family_index][0] <= threshold:
            _, pairs = families[family_index]
            for pair in pairs:
                if pair in selected:
                    continue
                selected.add(pair)
                if pair[1] - pair[0] >= 2:
                    difference = marks[pair[1]] - marks[pair[0]]
                    if difference > threshold:
                        raise AssertionError("a Wave 6 pair missed its threshold")
                    selected_nonadjacent_count += 1
                    selected_nonadjacent_square += difference * difference
            family_index += 1
        cutoff = threshold.numerator // threshold.denominator
        while history_index < len(history) and history[history_index][0] <= cutoff:
            difference, _ = history[history_index]
            history_square += difference * difference
            history_index += 1
        reservoir_count = history_index - selected_nonadjacent_count
        reservoir_square = history_square - selected_nonadjacent_square
        if reservoir_count < 0 or reservoir_square < 0:
            raise AssertionError("the incremental reservoir accounting failed")
        density = Fraction(reservoir_count, 1) / threshold
        square_asset = Fraction(reservoir_square, 1) / threshold**2
        events.append(
            CompactDensityEvent(
                epoch=old_count,
                antidiagonal=antidiagonal,
                threshold=threshold,
                global_reservoir_count=reservoir_count,
                normalized_adjoint_innovation=innovation,
                global_margin=density - innovation,
                global_square_margin=square_asset - innovation,
            )
        )
    return tuple(events)


@dataclass(frozen=True)
class LongFixtureAudit:
    provenance: str
    point_count: int
    b_661: int
    b_680: int
    b_681: int
    difference_count: int
    points_sha256: str
    events_sha256: str
    envelope_holds_through_680: bool
    envelope_fails_at_681: bool
    audited_epochs: tuple[int, ...]
    activation_event_count: int
    negative_global_event_count: int
    negative_square_event_count: int
    minimum_global_event: CompactDensityEvent
    minimum_square_event: CompactDensityEvent
    infinite_survival_inferred: bool


@lru_cache(maxsize=1)
def long_secondary_fixture_audit() -> LongFixtureAudit:
    """Audit every dyadic event through m=256 on the reported long fixture."""
    points = mian_chowla_third_at_661_points()
    with localcontext() as context:
        context.prec = 60
        logarithm_two = Decimal(2).ln()

        def envelope(index: int) -> Decimal:
            return Decimal(index * index) * (Decimal(2 * index).ln() / logarithm_two)

        holds = all(
            Decimal(points[index]) <= envelope(index) for index in range(1, 681)
        )
        fails = Decimal(points[681]) > envelope(681)

    epochs = (2, 4, 8, 16, 32, 64, 128, 256)
    events = tuple(
        event
        for epoch in epochs
        for event in _fast_latest_epoch_events(points, old_count=epoch)
    )
    minimum_global = min(
        events,
        key=lambda event: (event.global_margin, event.epoch, event.antidiagonal),
    )
    minimum_square = min(
        events,
        key=lambda event: (
            event.global_square_margin,
            event.epoch,
            event.antidiagonal,
        ),
    )
    encoded_points = ",".join(str(point) for point in points).encode("ascii")
    encoded_events = "\n".join(
        "|".join(
            (
                str(event.epoch),
                str(event.antidiagonal),
                f"{event.threshold.numerator}/{event.threshold.denominator}",
                str(event.global_reservoir_count),
                (
                    f"{event.normalized_adjoint_innovation.numerator}/"
                    f"{event.normalized_adjoint_innovation.denominator}"
                ),
                f"{event.global_margin.numerator}/{event.global_margin.denominator}",
                (
                    f"{event.global_square_margin.numerator}/"
                    f"{event.global_square_margin.denominator}"
                ),
            )
        )
        for event in events
    ).encode("ascii")
    return LongFixtureAudit(
        provenance=(
            "secondary public-working-report algorithm; independently reconstructed, "
            "not an infinite-branch certificate"
        ),
        point_count=len(points),
        b_661=points[661],
        b_680=points[680],
        b_681=points[681],
        difference_count=len(points) * (len(points) - 1) // 2,
        points_sha256=sha256(encoded_points).hexdigest(),
        events_sha256=sha256(encoded_events).hexdigest(),
        envelope_holds_through_680=holds,
        envelope_fails_at_681=fails,
        audited_epochs=epochs,
        activation_event_count=len(events),
        negative_global_event_count=sum(event.global_margin < 0 for event in events),
        negative_square_event_count=sum(
            event.global_square_margin < 0 for event in events
        ),
        minimum_global_event=minimum_global,
        minimum_square_event=minimum_square,
        infinite_survival_inferred=False,
    )


def _encode(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [_encode(item) for item in value]
    if isinstance(value, list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {key: _encode(item) for key, item in value.items()}
    return value


def build_report(*, trials8: int, trials16: int) -> dict[str, Any]:
    """Build the exact deterministic research report used by the CLI."""
    four = exhaustive_four_mark_audit()
    eight = deterministic_c1_search(
        mark_count=8,
        trials=trials8,
        seed=8_119_108,
        survival_depth=2,
    )
    sixteen = deterministic_c1_search(
        mark_count=16,
        trials=trials16,
        seed=16_119_108,
        survival_depth=1,
    )
    latest = density_event(LATEST_SHELL_COUNTEREXAMPLE, old_count=4, antidiagonal=1)
    latest_survival = critical_survival_audit(LATEST_SHELL_COUNTEREXAMPLE, depth=2)
    unrestricted = unrestricted_scaling_event()
    payload = {
        "schema": "wave8_density_candidate_search_v1",
        "four_mark_exhaustive": asdict(four),
        "eight_mark_deterministic": asdict(eight),
        "sixteen_mark_deterministic": asdict(sixteen),
        "latest_shell_counterexample": {
            "event": asdict(latest),
            "finite_survival_level_counts": latest_survival.level_counts,
            "infinite_survival_inferred": False,
        },
        "unrestricted_scaling_counterexample": asdict(unrestricted),
        "long_secondary_fixture": asdict(long_secondary_fixture_audit()),
        "cumulative_finite_examples": {
            "eight": asdict(cumulative_first_cross_audit(EIGHT_MARK_FINITE_WITNESS)),
            "sixteen": asdict(
                cumulative_first_cross_audit(SIXTEEN_MARK_FINITE_WITNESS)
            ),
        },
        "conclusions": {
            "literal_local_factor_one": "REFUTED",
            "latest_shell_factor_one": "REFUTED",
            "m_at_least_four_global_factor_one": "OPEN_FINITE_EVIDENCE_ONLY",
            "cumulative_initial_error_bridge": "OPEN_FINITE_EVIDENCE_ONLY",
            "square_weighted_reservoir_bridge": "OPEN_FINITE_EVIDENCE_ONLY",
            "conditional_c1_cap_factor": "PROVED_WHEN_GLOBAL_RESERVOIR_NONEMPTY",
            "infinite_extension_claimed": False,
            "erdos_1191_resolved": False,
        },
    }
    encoded = _encode(payload)
    canonical = json.dumps(encoded, sort_keys=True, separators=(",", ":"))
    encoded["report_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials8", type=int, default=5_000)
    parser.add_argument("--trials16", type=int, default=1_200)
    arguments = parser.parse_args()
    print(
        json.dumps(
            build_report(trials8=arguments.trials8, trials16=arguments.trials16),
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()

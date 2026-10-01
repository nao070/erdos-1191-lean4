"""Deterministic bounded searches for the Wave 19 sparse-spike prefixes.

The one-step shadow calculation is exhaustive for its fixed input prefix and
the complete next-prefix C=32 domain.  ``greedy_extend`` exhausts candidates
only until the first legal mark at each selected branch node.  It is therefore
constructive, deterministic, and exactly replayable, but not a globally
exhaustive search over all continuation branches.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from functools import cache
from math import comb

from wave19_sparse_spike_certificate import critical_cap, positive_differences


@dataclass(frozen=True)
class ExhaustiveNextMarkScan:
    prefix_point_count: int
    next_mark_count: int
    minimum_candidate: int
    maximum_candidate: int
    domain_size: int
    forbidden_count: int
    allowed_count: int
    first_allowed: int | None
    exhaustive_for_fixed_prefix_and_cap: bool
    characterization: str


@dataclass(frozen=True)
class GreedyExtensionResult:
    points: tuple[int, ...]
    requested_point_count: int
    stage_candidate_counts: tuple[int, ...]
    total_candidates_tested: int
    completed: bool
    failed_mark_count: int | None
    global_search_exhaustive: bool
    each_step_first_legal_is_exhaustive: bool
    scope: str


@dataclass(frozen=True)
class TerminalMaximizationResult:
    core_point_count: int
    selected_point_count: int
    minimum_candidate: int
    maximum_candidate: int
    domain_size: int
    selected_terminal: int
    old_difference_maximum: int
    selected_new_difference_minimum: int
    forbidden_shadow_upper_bound: int
    selected_blocker_count: int
    candidates_examined_descending: int
    forbidden_candidate_count: int | None
    forbidden_shadow_materialized: bool
    cap_maximum_selected: bool
    selection_exhaustive_for_maximum: bool
    full_domain_classified: bool
    method: str
    points: tuple[int, ...]


def _validated_golomb_prefix(points: Sequence[int]) -> tuple[tuple[int, ...], set[int]]:
    marks = tuple(points)
    differences = positive_differences(marks)
    if len(set(differences)) != comb(len(marks), 2):
        raise ValueError("points must be a Golomb ruler")
    return marks, set(differences)


def exhaustive_next_mark_scan(points: Sequence[int]) -> ExhaustiveNextMarkScan:
    """Count every legal next terminal via the exact forbidden shadow A+Delta."""
    marks, differences = _validated_golomb_prefix(points)
    next_mark_count = len(marks) + 1
    minimum = marks[-1] + 1
    maximum = critical_cap(next_mark_count) - 1
    domain_size = max(0, maximum - minimum + 1)
    forbidden = {
        mark + difference
        for mark in marks
        for difference in differences
        if minimum <= mark + difference <= maximum
    }
    allowed_count = domain_size - len(forbidden)
    first_allowed: int | None = None
    if allowed_count:
        for candidate in range(minimum, maximum + 1):
            if candidate not in forbidden:
                first_allowed = candidate
                break
    return ExhaustiveNextMarkScan(
        prefix_point_count=len(marks),
        next_mark_count=next_mark_count,
        minimum_candidate=minimum,
        maximum_candidate=maximum,
        domain_size=domain_size,
        forbidden_count=len(forbidden),
        allowed_count=allowed_count,
        first_allowed=first_allowed,
        exhaustive_for_fixed_prefix_and_cap=True,
        characterization=(
            "x is forbidden iff x-a is an old positive difference for some a; "
            "new differences x-a are automatically pairwise distinct"
        ),
    )


def maximize_next_terminal(points: Sequence[int]) -> TerminalMaximizationResult:
    """Select the largest legal next mark under the exact C=32 prefix cap.

    The fast path proves the cap maximum legal from the exact shadow bound
    ``A + Delta(A) <= max(A) + max(Delta(A))``.  Only when that bound reaches
    the cap maximum is the relevant forbidden shadow explicitly materialized.
    Thus maximality is exhaustive without scanning every legal-domain integer.
    """
    marks, differences = _validated_golomb_prefix(points)
    selected_point_count = len(marks) + 1
    minimum = marks[-1] + 1
    maximum = critical_cap(selected_point_count) - 1
    if maximum < minimum:
        raise LookupError("the next-prefix cap leaves no candidate terminal")
    old_difference_maximum = max(differences)
    shadow_upper = marks[-1] + old_difference_maximum

    if maximum > shadow_upper:
        selected = maximum
        blockers = sum(selected - mark in differences for mark in marks)
        if blockers:
            raise AssertionError("shadow upper bound contradicted direct blockers")
        candidates_examined = 1
        forbidden_count: int | None = None
        shadow_materialized = False
        full_domain_classified = False
        method = (
            "cap maximum exceeds exact forbidden-shadow upper bound "
            "max(A)+max(Delta(A))"
        )
    else:
        forbidden = {
            mark + difference
            for mark in marks
            for difference in differences
            if minimum <= mark + difference <= maximum
        }
        selected = next(
            (
                candidate
                for candidate in range(maximum, minimum - 1, -1)
                if candidate not in forbidden
            ),
            None,
        )
        if selected is None:
            raise LookupError("no legal next terminal exists under the prefix cap")
        blockers = 0
        candidates_examined = maximum - selected + 1
        forbidden_count = len(forbidden)
        shadow_materialized = True
        full_domain_classified = True
        method = "complete forbidden-shadow materialization over the legal domain"

    new_differences = tuple(selected - mark for mark in marks)
    if not differences.isdisjoint(new_differences):
        raise AssertionError("selected terminal collides with an old difference")
    return TerminalMaximizationResult(
        core_point_count=len(marks),
        selected_point_count=selected_point_count,
        minimum_candidate=minimum,
        maximum_candidate=maximum,
        domain_size=maximum - minimum + 1,
        selected_terminal=selected,
        old_difference_maximum=old_difference_maximum,
        selected_new_difference_minimum=selected - marks[-1],
        forbidden_shadow_upper_bound=shadow_upper,
        selected_blocker_count=blockers,
        candidates_examined_descending=candidates_examined,
        forbidden_candidate_count=forbidden_count,
        forbidden_shadow_materialized=shadow_materialized,
        cap_maximum_selected=selected == maximum,
        selection_exhaustive_for_maximum=True,
        full_domain_classified=full_domain_classified,
        method=method,
        points=marks + (selected,),
    )


def greedy_extend(
    points: Sequence[int], requested_point_count: int
) -> GreedyExtensionResult:
    """Append the smallest legal integer at each step under the C=32 cap."""
    marks_tuple, _ = _validated_golomb_prefix(points)
    if isinstance(requested_point_count, bool) or not isinstance(
        requested_point_count, int
    ):
        raise TypeError("requested_point_count must be an integer")
    if requested_point_count <= len(marks_tuple):
        raise ValueError("requested_point_count must exceed the prefix length")
    return _greedy_extend_cached(marks_tuple, requested_point_count)


@cache
def _greedy_extend_cached(
    marks_tuple: tuple[int, ...], requested_point_count: int
) -> GreedyExtensionResult:
    differences = set(positive_differences(marks_tuple))
    marks = list(marks_tuple)
    stage_counts: list[int] = []
    failed_mark_count: int | None = None

    while len(marks) < requested_point_count:
        next_mark_count = len(marks) + 1
        maximum = critical_cap(next_mark_count) - 1
        candidate = marks[-1] + 1
        tested = 0
        accepted = False
        while candidate <= maximum:
            tested += 1
            new_differences = tuple(candidate - mark for mark in marks)
            if len(set(new_differences)) != len(marks):
                raise AssertionError(
                    "strictly increasing marks gave duplicate differences"
                )
            if differences.isdisjoint(new_differences):
                marks.append(candidate)
                differences.update(new_differences)
                stage_counts.append(tested)
                accepted = True
                break
            candidate += 1
        if not accepted:
            failed_mark_count = next_mark_count
            stage_counts.append(tested)
            break

    return GreedyExtensionResult(
        points=tuple(marks),
        requested_point_count=requested_point_count,
        stage_candidate_counts=tuple(stage_counts),
        total_candidates_tested=sum(stage_counts),
        completed=len(marks) == requested_point_count,
        failed_mark_count=failed_mark_count,
        global_search_exhaustive=False,
        each_step_first_legal_is_exhaustive=True,
        scope="finite constructive witness only",
    )

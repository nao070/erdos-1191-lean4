"""Integer-safe searches for nested dyadic Golomb rulers.

This module is deliberately separate from the search state used to construct
rulers: :func:`independent_difference_audit` rebuilds every pair difference
from a completed witness for certificate checking.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import comb
from random import Random

from gap_measure_dynamics import (
    dyadic_gap_matrix_update,
)


@dataclass(frozen=True)
class DifferenceAudit:
    points: tuple[int, ...]
    pair_count: int
    sorted_differences: tuple[int, ...]
    collisions: tuple[tuple[int, tuple[tuple[int, int], ...]], ...]

    @property
    def is_golomb(self) -> bool:
        return not self.collisions


def independent_difference_audit(points: tuple[int, ...] | list[int]) -> DifferenceAudit:
    """Recompute all positive differences and report every collision exactly."""
    marks = tuple(points)
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if len(marks) < 2 or marks != tuple(sorted(marks)) or len(set(marks)) != len(marks):
        raise ValueError("points must be a strictly increasing sequence of length at least two")

    owners: dict[int, list[tuple[int, int]]] = {}
    for left in range(len(marks)):
        for right in range(left + 1, len(marks)):
            difference = marks[right] - marks[left]
            owners.setdefault(difference, []).append((left, right))
    collisions = tuple(
        (difference, tuple(pairs))
        for difference, pairs in sorted(owners.items())
        if len(pairs) > 1
    )
    return DifferenceAudit(
        points=marks,
        pair_count=len(marks) * (len(marks) - 1) // 2,
        sorted_differences=tuple(sorted(owners)),
        collisions=collisions,
    )


def integer_gap_function_variance(
    points: tuple[int, ...] | list[int],
) -> Fraction:
    """Exact ``Var_nu(u(1-u))`` from three integer moments."""
    return integer_partial_gap_function_variance(
        points, final_rank_count=len(tuple(points))
    )


def integer_partial_gap_function_variance(
    points: tuple[int, ...] | list[int], *, final_rank_count: int
) -> Fraction:
    """Score existing gaps at their ranks in a future larger prefix.

    With ``x_k=k(m-k)`` and integer gap weights ``h_k``, the result is
    ``(N sum h_k x_k^2 - (sum h_k x_k)^2)/(N^2 m^4)``.
    """
    marks = tuple(points)
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if len(marks) < 2 or marks != tuple(sorted(marks)) or len(set(marks)) != len(marks):
        raise ValueError("points must be a strictly increasing sequence of length at least two")
    if not isinstance(final_rank_count, int) or final_rank_count < len(marks):
        raise ValueError("final_rank_count must be an integer at least the point count")
    count = final_rank_count
    modulus = marks[-1] - marks[0] + 1
    gaps = (1, *(marks[index] - marks[index - 1] for index in range(1, len(marks))))
    levels = tuple(index * (count - index) for index in range(len(marks)))
    first_moment = sum(gap * level for gap, level in zip(gaps, levels))
    second_moment = sum(gap * level * level for gap, level in zip(gaps, levels))
    return Fraction(
        modulus * second_moment - first_moment * first_moment,
        modulus * modulus * count**4,
    )


def _log_two_interval(terms: int) -> tuple[Fraction, Fraction]:
    """Rigorous positive-term enclosure of log(2)."""
    if not isinstance(terms, int) or terms < 1:
        raise ValueError("terms must be a positive integer")
    z = Fraction(1, 3)
    lower = 2 * sum(
        (z ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        Fraction(0),
    )
    tail = 2 * z ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - z * z)
    )
    return lower, lower + tail


def _dyadic_exponent(mark_count: int) -> int:
    if not isinstance(mark_count, int) or mark_count < 2:
        raise ValueError("mark_count must be a dyadic integer at least two")
    exponent = mark_count.bit_length() - 1
    if 2**exponent != mark_count:
        raise ValueError("mark_count must be a power of two")
    return exponent


def _log_integer_interval(value: int, terms: int) -> tuple[Fraction, Fraction]:
    """Rigorous atanh-series enclosure of ``log(value)`` for integer value."""
    if not isinstance(value, int) or value < 2:
        raise ValueError("value must be an integer at least two")
    if not isinstance(terms, int) or terms < 1:
        raise ValueError("terms must be a positive integer")
    z = Fraction(value - 1, value + 1)
    lower = 2 * sum(
        (z ** (2 * index + 1) / (2 * index + 1) for index in range(terms)),
        Fraction(0),
    )
    tail = 2 * z ** (2 * terms + 1) / (
        (2 * terms + 1) * (1 - z * z)
    )
    return lower, lower + tail


def critical_modulus_cap(mark_count: int, constant: Fraction | int) -> int:
    """Largest integer ``N`` certified by ``N <= 2*C*m^2*log(m)``."""
    if not isinstance(mark_count, int) or mark_count < 2:
        raise ValueError("mark_count must be an integer at least two")
    exact_constant = Fraction(constant)
    if exact_constant <= 0:
        raise ValueError("constant must be positive")
    exponent = mark_count.bit_length() - 1
    is_dyadic = 2**exponent == mark_count
    factor = 2 * exact_constant * mark_count**2
    terms = 4
    while True:
        if is_dyadic:
            log_two_lower, log_two_upper = _log_two_interval(terms)
            lower, upper = exponent * log_two_lower, exponent * log_two_upper
        else:
            lower, upper = _log_integer_interval(mark_count, terms)
        lower_floor = (factor * lower).numerator // (factor * lower).denominator
        upper_floor = (factor * upper).numerator // (factor * upper).denominator
        if lower_floor == upper_floor:
            return lower_floor
        terms *= 2
        if terms > 4096:
            raise ArithmeticError("log enclosure could not determine the integer cap")


def modulus_is_within_envelope(
    modulus: int, mark_count: int, constant: Fraction | int
) -> bool:
    """Integer-safe decision for one dyadic critical-envelope inequality."""
    if not isinstance(modulus, int) or modulus < 1:
        raise ValueError("modulus must be a positive integer")
    return modulus <= critical_modulus_cap(mark_count, constant)


@dataclass(frozen=True)
class DyadicScoreRow:
    mark_count: int
    modulus: int
    gap_variance: Fraction
    innovation_q00_per_modulus: Fraction | None


def dyadic_score_rows(
    points: tuple[int, ...] | list[int], *, sizes: tuple[int, ...]
) -> tuple[DyadicScoreRow, ...]:
    """Evaluate exact gap variances and consecutive dyadic innovations."""
    marks = tuple(points)
    if not sizes:
        raise ValueError("sizes must be nonempty")
    if tuple(sorted(set(sizes))) != sizes:
        raise ValueError("sizes must be strictly increasing")
    for size in sizes:
        _dyadic_exponent(size)
        if size > len(marks):
            raise ValueError("the witness is too short for the requested sizes")
    if any(right != 2 * left for left, right in zip(sizes, sizes[1:])):
        raise ValueError("requested sizes must be consecutive dyadic levels")

    rows: list[DyadicScoreRow] = []
    previous: int | None = None
    for size in sizes:
        prefix = marks[:size]
        modulus = prefix[-1] - prefix[0] + 1
        innovation: Fraction | None = None
        if previous is not None:
            update = dyadic_gap_matrix_update(prefix, previous)
            innovation = update.innovation[0][0] / modulus
        rows.append(
            DyadicScoreRow(
                mark_count=size,
                modulus=modulus,
                gap_variance=integer_gap_function_variance(prefix),
                innovation_q00_per_modulus=innovation,
            )
        )
        previous = size
    return tuple(rows)


@dataclass(frozen=True)
class ExactGapSearchResult:
    mark_count: int
    max_modulus: int
    complete: bool
    candidate_count: int
    accepted_count: int
    node_count: int
    best_score: Fraction
    best_rulers: tuple[tuple[int, ...], ...]


def _new_differences(mark: int, marks: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(mark - old_mark for old_mark in marks)


def exhaustive_gap_search(
    *,
    mark_count: int,
    max_modulus: int,
    envelope_constant: Fraction | int | None = None,
) -> ExactGapSearchResult:
    """Completely maximize ``Var_nu(u(1-u))`` for ``0=a_1<N``.

    Every increasing normalized candidate with final modulus at most
    ``max_modulus`` is represented.  Incremental difference pruning changes
    the work performed, not the declared combinatorial candidate count.
    """
    if not isinstance(mark_count, int) or not isinstance(max_modulus, int):
        raise TypeError("search bounds must be integers")
    if mark_count < 2 or max_modulus < 2:
        raise ValueError("mark_count and max_modulus must be at least two")
    available = max_modulus - 1
    chosen = mark_count - 1
    candidate_count = comb(available, chosen) if chosen <= available else 0
    accepted_count = 0
    node_count = 1
    best_score: Fraction | None = None
    best: list[tuple[int, ...]] = []

    def visit(marks: tuple[int, ...], used: frozenset[int]) -> None:
        nonlocal accepted_count, node_count, best_score
        if len(marks) == mark_count:
            if envelope_constant is not None and any(
                marks[size - 1] - marks[0] + 1
                > critical_modulus_cap(size, Fraction(envelope_constant))
                for size in range(2, mark_count + 1)
            ):
                return
            accepted_count += 1
            score = integer_gap_function_variance(marks)
            if best_score is None or score > best_score:
                best_score = score
                best.clear()
                best.append(marks)
            elif score == best_score:
                best.append(marks)
            return

        remaining_after_choice = mark_count - len(marks) - 1
        maximum = max_modulus - 1 - remaining_after_choice
        for mark in range(marks[-1] + 1, maximum + 1):
            new = _new_differences(mark, marks)
            if len(new) != len(set(new)) or not used.isdisjoint(new):
                continue
            node_count += 1
            visit((*marks, mark), used.union(new))

    if candidate_count:
        visit((0,), frozenset())
    return ExactGapSearchResult(
        mark_count=mark_count,
        max_modulus=max_modulus,
        complete=True,
        candidate_count=candidate_count,
        accepted_count=accepted_count,
        node_count=node_count,
        best_score=Fraction(0) if best_score is None else best_score,
        best_rulers=tuple(sorted(best)),
    )


@dataclass(frozen=True)
class NestedWitnessAudit:
    points: tuple[int, ...]
    rows: tuple[DyadicScoreRow, ...]
    envelope_rows: tuple["EnvelopePrefixRow", ...]
    difference_audit: DifferenceAudit
    envelope_constant: Fraction
    envelope_compatible: bool
    minimum_gap_variance: Fraction
    minimum_innovation_q00_per_modulus: Fraction


@dataclass(frozen=True)
class EnvelopePrefixRow:
    mark_count: int
    modulus: int
    critical_modulus_cap: int
    certified: bool


def audit_nested_witness(
    points: tuple[int, ...] | list[int],
    *,
    sizes: tuple[int, ...],
    constant: Fraction | int,
) -> NestedWitnessAudit:
    """Independently re-audit a completed nested dyadic witness."""
    marks = tuple(points)
    if not sizes or sizes[0] < 4:
        raise ValueError("sizes must begin at a dyadic mark count of at least four")
    if any(right != 2 * left for left, right in zip(sizes, sizes[1:])):
        raise ValueError("sizes must be consecutive dyadic levels")
    if len(marks) != sizes[-1]:
        raise ValueError("the completed witness must end at the last requested size")
    difference_audit = independent_difference_audit(marks)
    if not difference_audit.is_golomb:
        raise ValueError("the completed witness is not a Golomb ruler")
    exact_constant = Fraction(constant)
    all_rows = dyadic_score_rows(marks, sizes=(sizes[0] // 2, *sizes))
    rows = all_rows[1:]
    envelope_rows = tuple(
        EnvelopePrefixRow(
            mark_count=size,
            modulus=marks[size - 1] - marks[0] + 1,
            critical_modulus_cap=critical_modulus_cap(size, exact_constant),
            certified=modulus_is_within_envelope(
                marks[size - 1] - marks[0] + 1,
                size,
                exact_constant,
            ),
        )
        for size in range(2, len(marks) + 1)
    )
    compatible = all(row.certified for row in envelope_rows)
    innovations = tuple(
        row.innovation_q00_per_modulus
        for row in rows
        if row.innovation_q00_per_modulus is not None
    )
    if len(innovations) != len(rows):
        raise AssertionError("a requested dyadic transition lacked an innovation")
    return NestedWitnessAudit(
        points=marks,
        rows=rows,
        envelope_rows=envelope_rows,
        difference_audit=difference_audit,
        envelope_constant=exact_constant,
        envelope_compatible=compatible,
        minimum_gap_variance=min(row.gap_variance for row in rows),
        minimum_innovation_q00_per_modulus=min(innovations),
    )


@dataclass(frozen=True)
class BeamSearchResult:
    sizes: tuple[int, ...]
    envelope_constant: Fraction
    objective: str
    beam_width: int
    candidates_per_state: int
    seed: int
    exact_root_candidate_count: int
    exact_root_accepted_count: int
    expanded_state_count: int
    witnesses: tuple[NestedWitnessAudit, ...]


@dataclass(frozen=True)
class _SearchState:
    marks: tuple[int, ...]
    differences: frozenset[int]


def _enumerate_golomb_states(
    mark_count: int, max_modulus: int
) -> tuple[int, tuple[_SearchState, ...]]:
    available = max_modulus - 1
    chosen = mark_count - 1
    candidate_count = comb(available, chosen) if 0 <= chosen <= available else 0
    states: list[_SearchState] = []

    def visit(marks: tuple[int, ...], used: frozenset[int]) -> None:
        if len(marks) == mark_count:
            states.append(_SearchState(marks, used))
            return
        remaining_after_choice = mark_count - len(marks) - 1
        maximum = max_modulus - 1 - remaining_after_choice
        for mark in range(marks[-1] + 1, maximum + 1):
            new = _new_differences(mark, marks)
            if len(new) == len(set(new)) and used.isdisjoint(new):
                visit((*marks, mark), used.union(new))

    if candidate_count:
        visit((0,), frozenset())
    return candidate_count, tuple(states)


def _valid_extension(state: _SearchState, mark: int) -> tuple[int, ...] | None:
    new = _new_differences(mark, state.marks)
    if len(new) != len(set(new)) or not state.differences.isdisjoint(new):
        return None
    return new


def _extension_candidates(
    state: _SearchState,
    *,
    maximum: int,
    budget: int,
    generator: Random,
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    lower = state.marks[-1] + 1
    if maximum < lower:
        return ()
    span = maximum - lower + 1
    proposed: list[int] = []

    # Deterministic extremes and quantiles guard against a lucky RNG being the
    # only way to discover either dense or large-shell constructions.
    edge_count = max(2, budget // 4)
    proposed.extend(range(lower, min(maximum + 1, lower + 3 * edge_count)))
    proposed.extend(range(max(lower, maximum - 3 * edge_count + 1), maximum + 1))
    quantile_count = max(2, 2 * budget)
    if span == 1:
        proposed.append(lower)
    else:
        proposed.extend(
            lower + (span - 1) * index // (quantile_count - 1)
            for index in range(quantile_count)
        )
    random_draws = min(span, 6 * budget)
    if random_draws == span:
        proposed.extend(range(lower, maximum + 1))
    else:
        proposed.extend(generator.sample(range(lower, maximum + 1), random_draws))

    valid: list[tuple[int, tuple[int, ...]]] = []
    seen: set[int] = set()
    for mark in proposed:
        if mark in seen:
            continue
        seen.add(mark)
        new = _valid_extension(state, mark)
        if new is not None:
            valid.append((mark, new))

    # Preserve both small and large next gaps, then fill by seeded shuffling.
    valid.sort(key=lambda item: item[0])
    if len(valid) <= budget:
        return tuple(valid)
    flank = max(1, budget // 4)
    selected = [*valid[:flank], *valid[-flank:]]
    middle = valid[flank:-flank]
    generator.shuffle(middle)
    selected.extend(middle[: budget - len(selected)])
    return tuple(sorted(selected, key=lambda item: item[0]))


def _state_rows(
    state: _SearchState, checkpoints: tuple[int, ...]
) -> tuple[DyadicScoreRow, ...]:
    completed = tuple(size for size in checkpoints if size <= len(state.marks))
    if not completed:
        return ()
    prefix = state.marks[: completed[-1]]
    return _cached_checkpoint_rows(prefix, completed)


@lru_cache(maxsize=131_072)
def _cached_checkpoint_rows(
    prefix: tuple[int, ...], completed: tuple[int, ...]
) -> tuple[DyadicScoreRow, ...]:
    return dyadic_score_rows(
        prefix,
        sizes=(completed[0] // 2, *completed),
    )[1:]


def _state_rank(
    state: _SearchState,
    *,
    checkpoints: tuple[int, ...],
    objective: str,
) -> tuple[Fraction, ...]:
    rows = _state_rows(state, checkpoints)
    gaps = tuple(row.gap_variance for row in rows)
    innovations = tuple(
        row.innovation_q00_per_modulus
        for row in rows
        if row.innovation_q00_per_modulus is not None
    )
    provisional = integer_gap_function_variance(state.marks)
    target = next(
        (checkpoint for checkpoint in checkpoints if len(state.marks) <= checkpoint),
        len(state.marks),
    )
    target_provisional = integer_partial_gap_function_variance(
        state.marks, final_rank_count=target
    )
    minimum_gap = min(gaps) if gaps else provisional
    gap_sum = sum(gaps, Fraction(0))
    minimum_innovation = min(innovations) if innovations else Fraction(0)
    innovation_sum = sum(innovations, Fraction(0))
    if objective == "gap":
        return (
            minimum_gap,
            gap_sum,
            target_provisional,
            provisional,
            minimum_innovation,
            innovation_sum,
        )
    if objective == "innovation":
        return (
            minimum_innovation,
            innovation_sum,
            minimum_gap,
            gap_sum,
            target_provisional,
            provisional,
        )
    raise ValueError("objective must be 'gap' or 'innovation'")


def beam_search_nested(
    *,
    sizes: tuple[int, ...] = (4, 8, 16, 32),
    constant: Fraction | int = Fraction(1),
    objective: str = "gap",
    beam_width: int = 256,
    candidates_per_state: int = 48,
    seed: int = 1191,
    retain: int = 8,
) -> BeamSearchResult:
    """Seeded integer beam search through consecutive dyadic prefixes.

    The initial checkpoint is enumerated completely.  Every later truncation
    is explicit in the returned beam parameters, so no completeness claim is
    attached to the final witnesses.
    """
    if not sizes or sizes[0] < 4:
        raise ValueError("sizes must begin at a dyadic mark count of at least four")
    for size in sizes:
        _dyadic_exponent(size)
    if any(right != 2 * left for left, right in zip(sizes, sizes[1:])):
        raise ValueError("sizes must be consecutive dyadic levels")
    if objective not in {"gap", "innovation"}:
        raise ValueError("objective must be 'gap' or 'innovation'")
    integer_parameters = (beam_width, candidates_per_state, seed, retain)
    if any(not isinstance(value, int) for value in integer_parameters):
        raise TypeError("beam parameters must be integers")
    if beam_width < 1 or candidates_per_state < 1 or retain < 1:
        raise ValueError("beam width, candidate budget, and retain must be positive")

    exact_constant = Fraction(constant)
    initial_cap = critical_modulus_cap(sizes[0], exact_constant)
    root_candidates, roots = _enumerate_golomb_states(sizes[0], initial_cap)
    roots = tuple(
        state
        for state in roots
        if all(
            modulus_is_within_envelope(
                state.marks[size - 1] - state.marks[0] + 1,
                size,
                exact_constant,
            )
            for size in range(2, sizes[0] + 1)
        )
    )
    if not roots:
        return BeamSearchResult(
            sizes,
            exact_constant,
            objective,
            beam_width,
            candidates_per_state,
            seed,
            root_candidates,
            0,
            0,
            (),
        )
    generator = Random(seed)
    ordered_roots = sorted(
        roots,
        key=lambda state: (_state_rank(state, checkpoints=sizes, objective=objective), state.marks),
        reverse=True,
    )
    beam = ordered_roots[:beam_width]
    expanded_state_count = 0

    for checkpoint in sizes[1:]:
        cap = critical_modulus_cap(checkpoint, exact_constant)
        while len(beam[0].marks) < checkpoint:
            next_mark_count = len(beam[0].marks) + 1
            remaining = checkpoint - next_mark_count
            maximum = min(
                cap - 1 - remaining,
                critical_modulus_cap(next_mark_count, exact_constant) - 1,
            )
            expanded: list[_SearchState] = []
            for state in beam:
                candidates = _extension_candidates(
                    state,
                    maximum=maximum,
                    budget=candidates_per_state,
                    generator=generator,
                )
                for mark, new in candidates:
                    expanded.append(
                        _SearchState((*state.marks, mark), state.differences.union(new))
                    )
            expanded_state_count += len(expanded)
            if not expanded:
                beam = []
                break
            expanded.sort(
                key=lambda state: (
                    _state_rank(state, checkpoints=sizes, objective=objective),
                    state.marks,
                ),
                reverse=True,
            )
            beam = expanded[:beam_width]
        if not beam:
            break

    audits = tuple(
        audit
        for state in beam
        if len(state.marks) == sizes[-1]
        for audit in (
            audit_nested_witness(state.marks, sizes=sizes, constant=exact_constant),
        )
        if audit.envelope_compatible
    )
    audits = tuple(
        sorted(
            audits,
            key=lambda audit: (
                audit.minimum_gap_variance
                if objective == "gap"
                else audit.minimum_innovation_q00_per_modulus,
                sum((row.gap_variance for row in audit.rows), Fraction(0))
                if objective == "gap"
                else sum(
                    (
                        row.innovation_q00_per_modulus
                        for row in audit.rows
                        if row.innovation_q00_per_modulus is not None
                    ),
                    Fraction(0),
                ),
                audit.points,
            ),
            reverse=True,
        )[:retain]
    )
    return BeamSearchResult(
        sizes=sizes,
        envelope_constant=exact_constant,
        objective=objective,
        beam_width=beam_width,
        candidates_per_state=candidates_per_state,
        seed=seed,
        exact_root_candidate_count=root_candidates,
        exact_root_accepted_count=len(roots),
        expanded_state_count=expanded_state_count,
        witnesses=audits,
    )

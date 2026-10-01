"""Wave 5 exact profile diagnostics and nested Golomb extension search."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from random import Random

from wave4_nested_search import (
    NestedWitnessAudit,
    audit_nested_witness,
    critical_modulus_cap,
    integer_partial_gap_function_variance,
)


@dataclass(frozen=True)
class ResetProfile:
    old_count: int
    new_count: int
    old_modulus: int
    new_modulus: int
    shell_growth: int
    signed_cells: tuple[Fraction, ...]
    cumulative: tuple[Fraction, ...]
    maximum_absolute_cumulative: Fraction
    extremum_boundary: Fraction
    extremum_sign: int
    l1_mass: Fraction


@dataclass(frozen=True)
class ProfilePersistence:
    coarse_cell_count: int
    fine_cell_count: int
    coarsening_factor: int
    coarsened_fine: tuple[Fraction, ...]
    aligned_mass: Fraction
    opposed_mass: Fraction
    signed_overlap: Fraction
    normalization_mass: Fraction
    normalized_signed_overlap: Fraction


@dataclass(frozen=True)
class ResetHistory:
    sizes: tuple[int, ...]
    profiles: tuple[ResetProfile, ...]
    persistence: tuple[ProfilePersistence, ...]


@dataclass(frozen=True)
class ExtensionWitness:
    points: tuple[int, ...]
    parent_index: int
    nested_audit: NestedWitnessAudit
    history: ResetHistory
    minimum_gap_variance: Fraction
    minimum_innovation_q00_per_modulus: Fraction
    final_innovation_q00_per_modulus: Fraction
    latest_persistence: ProfilePersistence


@dataclass(frozen=True)
class ExtensionSearchResult:
    sizes: tuple[int, ...]
    envelope_constant: Fraction
    objective: str
    beam_width: int
    candidates_per_state: int
    seed: int
    retain: int
    parent_count: int
    expanded_state_count: int
    witnesses: tuple[ExtensionWitness, ...]


@dataclass(frozen=True)
class _ExtensionState:
    marks: tuple[int, ...]
    differences: frozenset[int]
    parent_index: int


def _validated_points(points: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if any(not isinstance(mark, int) for mark in marks):
        raise TypeError("points must be integers")
    if len(marks) < 2 or marks != tuple(sorted(marks)) or len(set(marks)) != len(marks):
        raise ValueError("points must be a strictly increasing sequence of length at least two")
    return marks


def _gap_weights(points: tuple[int, ...]) -> tuple[int, ...]:
    return (1, *(points[index] - points[index - 1] for index in range(1, len(points))))


def reset_profile(
    points: tuple[int, ...] | list[int], *, old_count: int
) -> ResetProfile:
    """Compare an old gap profile with its newborn shell after rank reset.

    The old gaps and the shell gaps are separately normalized to probability
    vectors on the same ``old_count`` local rank cells.  ``signed_cells`` is
    shell minus old, so its entries sum to zero exactly.
    """
    marks = _validated_points(points)
    if not isinstance(old_count, int) or old_count < 2 or len(marks) != 2 * old_count:
        raise ValueError("points must contain exactly 2*old_count marks")
    old = marks[:old_count]
    old_modulus = old[-1] - old[0] + 1
    new_modulus = marks[-1] - marks[0] + 1
    shell_growth = new_modulus - old_modulus
    if shell_growth <= 0:
        raise AssertionError("the newborn shell has nonpositive diameter growth")
    full_gaps = _gap_weights(marks)
    old_gaps = full_gaps[:old_count]
    shell_gaps = full_gaps[old_count:]
    signed = tuple(
        Fraction(shell_gap, shell_growth) - Fraction(old_gap, old_modulus)
        for old_gap, shell_gap in zip(old_gaps, shell_gaps)
    )
    if sum(signed, Fraction(0)) != 0:
        raise AssertionError("reset discrepancy did not have zero total mass")
    running = Fraction(0)
    cumulative_values: list[Fraction] = []
    for value in signed:
        running += value
        cumulative_values.append(running)
    maximum = max((abs(value) for value in cumulative_values), default=Fraction(0))
    if maximum == 0:
        boundary = Fraction(0)
        sign = 0
    else:
        extremum_index = next(
            index
            for index, value in enumerate(cumulative_values)
            if abs(value) == maximum
        )
        extremum = cumulative_values[extremum_index]
        boundary = Fraction(extremum_index + 1, old_count)
        sign = 1 if extremum > 0 else -1
    return ResetProfile(
        old_count=old_count,
        new_count=2 * old_count,
        old_modulus=old_modulus,
        new_modulus=new_modulus,
        shell_growth=shell_growth,
        signed_cells=signed,
        cumulative=tuple(cumulative_values),
        maximum_absolute_cumulative=maximum,
        extremum_boundary=boundary,
        extremum_sign=sign,
        l1_mass=sum((abs(value) for value in signed), Fraction(0)),
    )


def compare_signed_profiles(
    coarse_cells: tuple[Fraction, ...] | list[Fraction],
    fine_cells: tuple[Fraction, ...] | list[Fraction],
) -> ProfilePersistence:
    """Compare signed reset profiles after exact consecutive-cell coarsening."""
    coarse = tuple(Fraction(value) for value in coarse_cells)
    fine = tuple(Fraction(value) for value in fine_cells)
    if not coarse or len(fine) < len(coarse) or len(fine) % len(coarse):
        raise ValueError("fine profile length must be a positive multiple of coarse length")
    if sum(coarse, Fraction(0)) != 0 or sum(fine, Fraction(0)) != 0:
        raise ValueError("signed reset profiles must have zero total mass")
    factor = len(fine) // len(coarse)
    coarsened = tuple(
        sum(fine[index * factor : (index + 1) * factor], Fraction(0))
        for index in range(len(coarse))
    )
    aligned = Fraction(0)
    opposed = Fraction(0)
    for old_value, new_value in zip(coarse, coarsened):
        common = min(abs(old_value), abs(new_value))
        if old_value * new_value > 0:
            aligned += common
        elif old_value * new_value < 0:
            opposed += common
    signed_overlap = aligned - opposed
    coarse_mass = sum((abs(value) for value in coarse), Fraction(0))
    fine_mass = sum((abs(value) for value in coarsened), Fraction(0))
    normalization = min(coarse_mass, fine_mass)
    normalized = Fraction(0) if normalization == 0 else signed_overlap / normalization
    return ProfilePersistence(
        coarse_cell_count=len(coarse),
        fine_cell_count=len(fine),
        coarsening_factor=factor,
        coarsened_fine=coarsened,
        aligned_mass=aligned,
        opposed_mass=opposed,
        signed_overlap=signed_overlap,
        normalization_mass=normalization,
        normalized_signed_overlap=normalized,
    )


def dyadic_reset_history(
    points: tuple[int, ...] | list[int], *, sizes: tuple[int, ...]
) -> ResetHistory:
    """Return signed reset profiles and consecutive-epoch persistence data."""
    marks = _validated_points(points)
    if not sizes or sizes[0] < 4 or sizes[-1] > len(marks):
        raise ValueError("sizes must be nonempty and covered by the witness")
    if any(size & (size - 1) for size in sizes):
        raise ValueError("sizes must be powers of two")
    if any(right != 2 * left for left, right in zip(sizes, sizes[1:])):
        raise ValueError("sizes must be consecutive dyadic levels")
    profiles = tuple(
        reset_profile(marks[:size], old_count=size // 2) for size in sizes
    )
    persistence = tuple(
        compare_signed_profiles(left.signed_cells, right.signed_cells)
        for left, right in zip(profiles, profiles[1:])
    )
    return ResetHistory(sizes=sizes, profiles=profiles, persistence=persistence)


def _profile_from_signed(
    signed: tuple[Fraction, ...],
    *,
    old_count: int,
    new_modulus: int,
    old_modulus: int,
) -> ResetProfile:
    running = Fraction(0)
    cumulative_values: list[Fraction] = []
    for value in signed:
        running += value
        cumulative_values.append(running)
    maximum = max((abs(value) for value in cumulative_values), default=Fraction(0))
    if maximum == 0:
        boundary = Fraction(0)
        sign = 0
    else:
        extremum_index = next(
            index
            for index, value in enumerate(cumulative_values)
            if abs(value) == maximum
        )
        extremum = cumulative_values[extremum_index]
        boundary = Fraction(extremum_index + 1, old_count)
        sign = 1 if extremum > 0 else -1
    return ResetProfile(
        old_count=old_count,
        new_count=2 * old_count,
        old_modulus=old_modulus,
        new_modulus=new_modulus,
        shell_growth=new_modulus - old_modulus,
        signed_cells=signed,
        cumulative=tuple(cumulative_values),
        maximum_absolute_cumulative=maximum,
        extremum_boundary=boundary,
        extremum_sign=sign,
        l1_mass=sum((abs(value) for value in signed), Fraction(0)),
    )


def _partial_reset_profile(
    points: tuple[int, ...], *, old_count: int
) -> ResetProfile:
    if not old_count < len(points) <= 2 * old_count:
        raise ValueError("partial transition must contain between m+1 and 2m marks")
    old = points[:old_count]
    old_modulus = old[-1] - old[0] + 1
    current_modulus = points[-1] - points[0] + 1
    growth = current_modulus - old_modulus
    if growth <= 0:
        raise AssertionError("partial newborn shell has nonpositive growth")
    gaps = _gap_weights(points)
    old_gaps = gaps[:old_count]
    observed_shell = gaps[old_count:]
    padded_shell = (*observed_shell, *(0 for _ in range(old_count - len(observed_shell))))
    signed = tuple(
        Fraction(shell_gap, growth) - Fraction(old_gap, old_modulus)
        for old_gap, shell_gap in zip(old_gaps, padded_shell)
    )
    if sum(signed, Fraction(0)) != 0:
        raise AssertionError("partial reset discrepancy did not have zero total mass")
    return _profile_from_signed(
        signed,
        old_count=old_count,
        new_modulus=current_modulus,
        old_modulus=old_modulus,
    )


def _all_differences(points: tuple[int, ...]) -> frozenset[int]:
    differences = tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )
    if len(differences) != len(set(differences)):
        raise ValueError("parent is not a Golomb ruler")
    return frozenset(differences)


def _valid_new_differences(
    state: _ExtensionState, mark: int
) -> tuple[int, ...] | None:
    new = tuple(mark - old_mark for old_mark in state.marks)
    if len(new) != len(set(new)) or not state.differences.isdisjoint(new):
        return None
    return new


def _extension_choices(
    state: _ExtensionState,
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
    edge = max(2, budget // 4)
    proposed.extend(range(lower, min(maximum + 1, lower + 4 * edge)))
    proposed.extend(range(max(lower, maximum - 4 * edge + 1), maximum + 1))
    quantiles = max(2, 3 * budget)
    if span == 1:
        proposed.append(lower)
    else:
        proposed.extend(
            lower + (span - 1) * index // (quantiles - 1)
            for index in range(quantiles)
        )
    draws = min(span, 8 * budget)
    if draws == span:
        proposed.extend(range(lower, maximum + 1))
    else:
        proposed.extend(generator.sample(range(lower, maximum + 1), draws))

    valid: list[tuple[int, tuple[int, ...]]] = []
    seen: set[int] = set()
    for mark in proposed:
        if mark in seen:
            continue
        seen.add(mark)
        new = _valid_new_differences(state, mark)
        if new is not None:
            valid.append((mark, new))
    valid.sort(key=lambda item: item[0])
    if len(valid) <= budget:
        return tuple(valid)
    if budget == 1:
        return (valid[0],)
    flank = max(1, budget // 4)
    selected = [*valid[:flank], *valid[-flank:]]
    middle = valid[flank:-flank]
    generator.shuffle(middle)
    selected.extend(middle[: budget - len(selected)])
    return tuple(sorted(selected, key=lambda item: item[0]))


def _partial_rank(
    state: _ExtensionState,
    *,
    target_count: int,
    previous_profile: ResetProfile,
    historical_minimum_innovation: Fraction,
    objective: str,
) -> tuple[Fraction, ...]:
    partial = _partial_reset_profile(state.marks, old_count=target_count // 2)
    persistence = compare_signed_profiles(
        previous_profile.signed_cells, partial.signed_cells
    )
    target_gap = integer_partial_gap_function_variance(
        state.marks, final_rank_count=target_count
    )
    if objective == "persistence":
        return (
            persistence.normalized_signed_overlap,
            persistence.aligned_mass,
            -persistence.opposed_mass,
            historical_minimum_innovation,
            target_gap,
            partial.maximum_absolute_cumulative,
        )
    if objective == "innovation":
        return (
            historical_minimum_innovation,
            target_gap,
            persistence.normalized_signed_overlap,
            persistence.aligned_mass,
            -persistence.opposed_mass,
            partial.maximum_absolute_cumulative,
        )
    raise ValueError("objective must be 'persistence' or 'innovation'")


def _final_witness(
    state: _ExtensionState,
    *,
    sizes: tuple[int, ...],
    constant: Fraction,
) -> ExtensionWitness:
    nested_audit = audit_nested_witness(
        state.marks, sizes=sizes, constant=constant
    )
    history = dyadic_reset_history(state.marks, sizes=sizes)
    innovations = tuple(
        row.innovation_q00_per_modulus
        for row in nested_audit.rows
        if row.innovation_q00_per_modulus is not None
    )
    if len(innovations) != len(nested_audit.rows):
        raise AssertionError("a dyadic checkpoint lacked its innovation")
    final_innovation = innovations[-1]
    return ExtensionWitness(
        points=state.marks,
        parent_index=state.parent_index,
        nested_audit=nested_audit,
        history=history,
        minimum_gap_variance=min(row.gap_variance for row in nested_audit.rows),
        minimum_innovation_q00_per_modulus=min(innovations),
        final_innovation_q00_per_modulus=final_innovation,
        latest_persistence=history.persistence[-1],
    )


def _final_rank(witness: ExtensionWitness, objective: str) -> tuple[Fraction, ...]:
    persistence = witness.latest_persistence
    if objective == "persistence":
        return (
            persistence.normalized_signed_overlap,
            persistence.aligned_mass,
            -persistence.opposed_mass,
            witness.minimum_innovation_q00_per_modulus,
            witness.final_innovation_q00_per_modulus,
            witness.minimum_gap_variance,
        )
    return (
        witness.minimum_innovation_q00_per_modulus,
        witness.final_innovation_q00_per_modulus,
        persistence.normalized_signed_overlap,
        persistence.aligned_mass,
        -persistence.opposed_mass,
        witness.minimum_gap_variance,
    )


def beam_extend_nested(
    *,
    parents: tuple[tuple[int, ...], ...],
    sizes: tuple[int, ...],
    constant: Fraction | int = Fraction(1),
    objective: str = "persistence",
    beam_width: int = 128,
    candidates_per_state: int = 32,
    seed: int = 501191,
    retain: int = 3,
) -> ExtensionSearchResult:
    """Heuristically extend saved nested rulers by one dyadic epoch."""
    if objective not in {"persistence", "innovation"}:
        raise ValueError("objective must be 'persistence' or 'innovation'")
    if not sizes or sizes[0] < 4 or any(
        right != 2 * left for left, right in zip(sizes, sizes[1:])
    ):
        raise ValueError("sizes must be consecutive dyadic levels starting at four")
    target_count = sizes[-1]
    parent_size = target_count // 2
    if not parents or any(len(parent) != parent_size for parent in parents):
        raise ValueError("every parent must have exactly half the target mark count")
    if any(
        not isinstance(value, int)
        for value in (beam_width, candidates_per_state, seed, retain)
    ):
        raise TypeError("beam parameters must be integers")
    if beam_width < 1 or candidates_per_state < 1 or retain < 1:
        raise ValueError("beam width, candidate budget, and retain must be positive")
    exact_constant = Fraction(constant)
    parent_sizes = sizes[:-1]
    states: list[_ExtensionState] = []
    previous_profiles: dict[int, ResetProfile] = {}
    historical_minima: dict[int, Fraction] = {}
    for parent_index, raw_parent in enumerate(parents):
        parent = _validated_points(raw_parent)
        parent_audit = audit_nested_witness(
            parent, sizes=parent_sizes, constant=exact_constant
        )
        if not parent_audit.envelope_compatible:
            raise ValueError("a supplied parent violates the common envelope")
        parent_history = dyadic_reset_history(parent, sizes=parent_sizes)
        previous_profiles[parent_index] = parent_history.profiles[-1]
        parent_innovations = tuple(
            row.innovation_q00_per_modulus
            for row in parent_audit.rows
            if row.innovation_q00_per_modulus is not None
        )
        historical_minima[parent_index] = min(parent_innovations)
        states.append(
            _ExtensionState(parent, _all_differences(parent), parent_index)
        )

    generator = Random(seed)
    beam = states
    expanded_state_count = 0
    while beam and len(beam[0].marks) < target_count:
        next_count = len(beam[0].marks) + 1
        maximum = critical_modulus_cap(next_count, exact_constant) - 1
        expanded: list[_ExtensionState] = []
        for state in beam:
            for mark, new in _extension_choices(
                state,
                maximum=maximum,
                budget=candidates_per_state,
                generator=generator,
            ):
                expanded.append(
                    _ExtensionState(
                        (*state.marks, mark),
                        state.differences.union(new),
                        state.parent_index,
                    )
                )
        expanded_state_count += len(expanded)
        if not expanded:
            beam = []
            break
        expanded.sort(
            key=lambda state: (
                _partial_rank(
                    state,
                    target_count=target_count,
                    previous_profile=previous_profiles[state.parent_index],
                    historical_minimum_innovation=historical_minima[state.parent_index],
                    objective=objective,
                ),
                state.marks,
            ),
            reverse=True,
        )
        beam = expanded[:beam_width]

    witnesses = tuple(
        _final_witness(state, sizes=sizes, constant=exact_constant)
        for state in beam
        if len(state.marks) == target_count
    )
    witnesses = tuple(
        sorted(
            witnesses,
            key=lambda witness: (_final_rank(witness, objective), witness.points),
            reverse=True,
        )[:retain]
    )
    return ExtensionSearchResult(
        sizes=sizes,
        envelope_constant=exact_constant,
        objective=objective,
        beam_width=beam_width,
        candidates_per_state=candidates_per_state,
        seed=seed,
        retain=retain,
        parent_count=len(parents),
        expanded_state_count=expanded_state_count,
        witnesses=witnesses,
    )

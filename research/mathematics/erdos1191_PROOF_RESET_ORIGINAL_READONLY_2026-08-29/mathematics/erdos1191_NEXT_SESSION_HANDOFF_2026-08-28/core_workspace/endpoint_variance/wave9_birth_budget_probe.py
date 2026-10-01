"""Certified finite probe for the Wave 8 positive birth budget.

The primary open target is a sublogarithmic bound for

    B_H = sum_m N_(2m)^(-2)
          sum_(0 <= i < j < 2m, j >= m) h_i h_j Phi_(i,j).

This module computes every displayed positive birth term exactly, groups the
genuine contiguous-difference atoms simultaneously by dyadic rank lag and
dyadic numerical magnitude, and tests several deliberately strong local
surrogates before they can be mistaken for the required infinite-branch
theorem.  All decisions use :class:`fractions.Fraction`.

The finite fixtures and exhaustive searches below do *not* establish
``surv_C=infinity`` and do not resolve Erdős Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from collections.abc import Iterable, Sequence
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import cache, lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any

from complete_birth_ledger import critical_modulus_cap, erdos_turan_ruler
from gap_measure_dynamics import dyadic_gap_matrix_update
from innovation_budget import LYAPUNOV_MATRIX, frobenius_inner
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave7_band_renewal_probe import (
    enumerate_compatible_four_mark_rulers,
    load_authenticated_wave6_fixtures,
)
from wave8_density_candidate_search import mian_chowla_third_at_661_points
from wave8_pair_telescope import pair_kernel
from wave8_survival_debt_probe import bounded_golomb_exhaustion

PERFECT_FOUR = (0, 1, 4, 6)
DEFAULT_SOURCE_CERTIFICATE = (
    Path(__file__).resolve().parent
    / "wave6_arithmetic_mining_certificate_2026-08-28.json"
)


def _fraction_zero() -> Fraction:
    return Fraction(0)


def _floor_power_of_two(value: int) -> int:
    if not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    return 1 << (value.bit_length() - 1)


def _is_power_of_two(value: int) -> bool:
    return value >= 1 and value & (value - 1) == 0


def _normalized_magnitude_depth(span: int, modulus: int) -> int:
    """Return ``s`` with ``N/2^(s+1) < span <= N/2^s``."""
    if not 1 <= span <= modulus:
        raise ValueError("require 1 <= span <= modulus")
    depth = 0
    while span * (1 << (depth + 1)) <= modulus:
        depth += 1
    if not span * (1 << depth) <= modulus < span * (1 << (depth + 1)):
        raise AssertionError("normalized magnitude band is inconsistent")
    return depth


def _validated_golomb(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or marks[0] != 0
        or any(not isinstance(mark, int) for mark in marks)
        or marks != tuple(sorted(set(marks)))
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    differences = {
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    }
    expected = len(marks) * (len(marks) - 1) // 2
    if len(differences) != expected:
        raise ValueError("points must form a Golomb ruler")
    return marks


def _gap_weights(points: tuple[int, ...]) -> tuple[int, ...]:
    return (
        1,
        *(points[index] - points[index - 1] for index in range(1, len(points))),
    )


def _points_sha256(points: Sequence[int]) -> str:
    encoded = ",".join(str(point) for point in points).encode("ascii")
    return sha256(encoded).hexdigest()


@cache
def _cached_critical_modulus_cap(mark_count: int) -> int:
    """Use the exact range-reduced logarithm oracle from the Wave 7 ledger."""
    return critical_modulus_cap(mark_count)


def _all_prefix_c1_fast(points: Sequence[int]) -> bool:
    marks = tuple(points)
    return all(
        marks[count - 1] + 1 <= _cached_critical_modulus_cap(count)
        for count in range(2, len(marks) + 1)
    )


@dataclass(frozen=True)
class BirthAtom:
    epoch: int
    left: int
    right: int
    kind: str
    kernel_rank_gap: int
    arithmetic_rank_lag: int
    rank_band_lower: int
    span: int
    absolute_magnitude_band_lower: int
    normalized_magnitude_depth: int
    gap_product: int
    kernel: Fraction
    charge: Fraction
    envelope_ratio: Fraction


@dataclass(frozen=True)
class NormalizedBandAudit:
    kind: str
    rank_band_lower: int
    normalized_magnitude_depth: int
    atom_count: int
    total_charge: Fraction
    share_of_epoch_increment: Fraction
    maximum_atom_envelope_ratio: Fraction


@dataclass(frozen=True)
class EpochBirthBudgetAudit:
    epoch: int
    epoch_index: int
    terminal_mark_count: int
    modulus: int
    birth_pair_count: int
    genuine_pair_count: int
    boundary_pair_count: int
    increment: Fraction
    genuine_increment: Fraction
    artificial_boundary_increment: Fraction
    signed_q_charge: Fraction
    old_pair_subtraction: Fraction
    macroscopic_long_rank_increment: Fraction
    macroscopic_long_rank_share: Fraction
    epoch_index_times_increment: Fraction
    one_based_epoch_times_increment: Fraction
    dominant_band: NormalizedBandAudit
    normalized_bands: tuple[NormalizedBandAudit, ...]


@dataclass(frozen=True)
class GlobalMagnitudeLagCell:
    rank_band_lower: int
    absolute_magnitude_band_lower: int
    atom_count: int
    integer_capacity: int
    occupancy_to_capacity: Fraction
    occupancy_to_rank_lower: Fraction
    envelope_upper_load_to_capacity: Fraction
    total_charge: Fraction
    first_atom: tuple[int, int, int, int, int]


@dataclass(frozen=True)
class FixtureAudit:
    name: str
    provenance: str
    supplied_mark_count: int
    audited_mark_count: int
    points_sha256: str
    audited_prefix_sha256: str
    all_prefix_c1_to_audited_count: bool
    pair_partition_count: int
    cumulative_birth_budget: Fraction
    largest_increment: Fraction
    largest_increment_epoch: int
    maximum_global_cell_occupancy_to_rank_lower: Fraction
    maximum_global_cell_occupancy_to_capacity: Fraction
    epoch_rows: tuple[EpochBirthBudgetAudit, ...]
    global_cells: tuple[GlobalMagnitudeLagCell, ...]


def _birth_atoms_unchecked(
    points: tuple[int, ...], *, old_count: int
) -> tuple[BirthAtom, ...]:
    if not _is_power_of_two(old_count) or old_count < 1 or len(points) < 2 * old_count:
        raise ValueError("old_count must specify an available dyadic birth epoch")
    terminal = 2 * old_count
    marks = points[:terminal]
    gaps = _gap_weights(marks)
    modulus = marks[-1] + 1
    atoms: list[BirthAtom] = []
    for right in range(old_count, terminal):
        for left in range(right):
            boundary = left == 0
            kernel_rank_gap = right - left
            arithmetic_rank_lag = kernel_rank_gap if boundary else kernel_rank_gap + 1
            span = marks[right] + 1 if boundary else marks[right] - marks[left - 1]
            kernel = _closed_kernel(left, right, terminal)
            charge = Fraction(gaps[left] * gaps[right], modulus * modulus) * kernel
            normalizer = (
                Fraction(arithmetic_rank_lag, terminal) ** 2
                * Fraction(span, modulus) ** 2
            )
            envelope_ratio = 3 * charge / normalizer
            if not 0 < envelope_ratio <= 1:
                raise AssertionError("the exact atom envelope was violated")
            atoms.append(
                BirthAtom(
                    epoch=old_count,
                    left=left,
                    right=right,
                    kind="boundary" if boundary else "genuine",
                    kernel_rank_gap=kernel_rank_gap,
                    arithmetic_rank_lag=arithmetic_rank_lag,
                    rank_band_lower=_floor_power_of_two(arithmetic_rank_lag),
                    span=span,
                    absolute_magnitude_band_lower=_floor_power_of_two(span),
                    normalized_magnitude_depth=_normalized_magnitude_depth(
                        span,
                        modulus,
                    ),
                    gap_product=gaps[left] * gaps[right],
                    kernel=kernel,
                    charge=charge,
                    envelope_ratio=envelope_ratio,
                )
            )
    expected = old_count * (3 * old_count - 1) // 2
    if len(atoms) != expected:
        raise AssertionError("the birth-pair count is inconsistent")
    return tuple(atoms)


def _closed_kernel(left: int, right: int, count: int) -> Fraction:
    """Evaluate the exact Wave 8 kernel with one integer numerator.

    This is equation (9) of ``WAVE8_Q_ATOM_DECOMPOSITION`` after clearing
    denominators.  The slower matrix oracle is sampled independently by the
    epoch scanner.
    """
    difference = right - left
    centered_sum = count - left - right
    numerator = (
        difference
        * difference
        * (
            112 * centered_sum * centered_sum
            + 16 * centered_sum * count
            + 12 * count * count
        )
    )
    return Fraction(numerator, 105 * count**4)


@dataclass(frozen=True)
class _EpochCellSummary:
    rank_band_lower: int
    absolute_magnitude_band_lower: int
    atom_count: int
    charge_numerator: int
    first_atom: tuple[int, int, int, int, int]


@dataclass(frozen=True)
class _EpochScan:
    audit: EpochBirthBudgetAudit
    charge_denominator: int
    genuine_spans: tuple[int, ...]
    genuine_cells: tuple[_EpochCellSummary, ...]


def birth_atoms(points: Sequence[int], *, old_count: int) -> tuple[BirthAtom, ...]:
    """Return every exact positive atom at one dyadic birth epoch."""
    return _birth_atoms_unchecked(_validated_golomb(points), old_count=old_count)


def _scan_epoch(points: tuple[int, ...], old_count: int) -> _EpochScan:
    terminal = 2 * old_count
    marks = points[:terminal]
    gaps = _gap_weights(marks)
    modulus = marks[-1] + 1
    kernel_denominator = 105 * terminal**4
    charge_denominator = kernel_denominator * modulus * modulus
    total_numerator = 0
    boundary_numerator = 0
    atom_count = 0
    boundary_count = 0
    band_accumulators: dict[tuple[str, int, int], list[Any]] = {}
    cell_accumulators: dict[tuple[int, int], list[Any]] = {}
    genuine_spans: list[int] = []

    for right in range(old_count, terminal):
        for left in range(right):
            boundary = left == 0
            kernel_rank_gap = right - left
            arithmetic_rank_lag = kernel_rank_gap if boundary else kernel_rank_gap + 1
            span = marks[right] + 1 if boundary else marks[right] - marks[left - 1]
            centered_sum = terminal - left - right
            kernel_numerator = (
                kernel_rank_gap
                * kernel_rank_gap
                * (
                    112 * centered_sum * centered_sum
                    + 16 * centered_sum * terminal
                    + 12 * terminal * terminal
                )
            )
            gap_product = gaps[left] * gaps[right]
            charge_numerator = gap_product * kernel_numerator
            total_numerator += charge_numerator
            atom_count += 1
            if boundary:
                boundary_numerator += charge_numerator
                boundary_count += 1

            ratio_numerator = gap_product * kernel_numerator
            ratio_denominator = (
                35
                * terminal
                * terminal
                * arithmetic_rank_lag
                * arithmetic_rank_lag
                * span
                * span
            )
            if not 0 < ratio_numerator <= ratio_denominator:
                raise AssertionError("the exact atom envelope was violated")
            rank_lower = _floor_power_of_two(arithmetic_rank_lag)
            depth = _normalized_magnitude_depth(span, modulus)
            band_key = (
                "boundary" if boundary else "genuine",
                rank_lower,
                depth,
            )
            accumulator = band_accumulators.setdefault(
                band_key,
                [0, 0, ratio_numerator, ratio_denominator],
            )
            accumulator[0] += 1
            accumulator[1] += charge_numerator
            if ratio_numerator * accumulator[3] > accumulator[2] * ratio_denominator:
                accumulator[2] = ratio_numerator
                accumulator[3] = ratio_denominator

            if not boundary:
                magnitude_lower = _floor_power_of_two(span)
                cell_key = (rank_lower, magnitude_lower)
                cell = cell_accumulators.setdefault(
                    cell_key,
                    [0, 0, (old_count, left, right, arithmetic_rank_lag, span)],
                )
                cell[0] += 1
                cell[1] += charge_numerator
                genuine_spans.append(span)

    expected = old_count * (3 * old_count - 1) // 2
    if atom_count != expected or boundary_count != old_count:
        raise AssertionError("the birth-pair count is inconsistent")
    increment = Fraction(total_numerator, charge_denominator)
    boundary_increment = Fraction(boundary_numerator, charge_denominator)
    genuine_increment = increment - boundary_increment

    sample_pairs = ((0, old_count), (terminal - 2, terminal - 1))
    for left, right in sample_pairs:
        if _closed_kernel(left, right, terminal) != pair_kernel(
            LYAPUNOV_MATRIX,
            left,
            right,
            count=terminal,
        ):
            raise AssertionError("the closed kernel failed its matrix oracle")
    if old_count == 1:
        signed_q = increment
        independent_positive = increment
    else:
        update = dyadic_gap_matrix_update(marks, old_count)
        direct_q = frobenius_inner(LYAPUNOV_MATRIX, update.innovation) / (
            update.new_modulus
        )
        old_energy_numerator = 0
        for right in range(1, old_count):
            for left in range(right):
                kernel_rank_gap = right - left
                centered_sum = terminal - left - right
                kernel_numerator = (
                    kernel_rank_gap
                    * kernel_rank_gap
                    * (
                        112 * centered_sum * centered_sum
                        + 16 * centered_sum * terminal
                        + 12 * terminal * terminal
                    )
                )
                old_energy_numerator += gaps[left] * gaps[right] * kernel_numerator
        growth = update.new_modulus - update.old_modulus
        old_subtraction = Fraction(
            growth * old_energy_numerator,
            update.old_modulus
            * update.new_modulus
            * update.new_modulus
            * kernel_denominator,
        )
        independent_positive = direct_q + old_subtraction
        signed_q = direct_q
    if increment != independent_positive:
        raise AssertionError("the positive birth sum failed its independent oracle")
    old_pair_subtraction = increment - signed_q
    if old_pair_subtraction < 0:
        raise AssertionError("the signed Q charge exceeded its positive birth term")

    bands = tuple(
        NormalizedBandAudit(
            kind=key[0],
            rank_band_lower=key[1],
            normalized_magnitude_depth=key[2],
            atom_count=values[0],
            total_charge=Fraction(values[1], charge_denominator),
            share_of_epoch_increment=(
                Fraction(values[1], charge_denominator) / increment
            ),
            maximum_atom_envelope_ratio=Fraction(values[2], values[3]),
        )
        for key, values in sorted(band_accumulators.items())
    )
    dominant = max(
        bands,
        key=lambda row: (
            row.total_charge,
            row.kind,
            -row.rank_band_lower,
            -row.normalized_magnitude_depth,
        ),
    )
    macroscopic_long_rank = sum(
        (
            band.total_charge
            for band in bands
            if band.kind == "genuine"
            and band.normalized_magnitude_depth == 0
            and band.rank_band_lower >= max(1, old_count // 2)
        ),
        Fraction(0),
    )
    epoch_index = old_count.bit_length() - 1
    audit = EpochBirthBudgetAudit(
        epoch=old_count,
        epoch_index=epoch_index,
        terminal_mark_count=terminal,
        modulus=modulus,
        birth_pair_count=atom_count,
        genuine_pair_count=atom_count - boundary_count,
        boundary_pair_count=boundary_count,
        increment=increment,
        genuine_increment=genuine_increment,
        artificial_boundary_increment=boundary_increment,
        signed_q_charge=signed_q,
        old_pair_subtraction=old_pair_subtraction,
        macroscopic_long_rank_increment=macroscopic_long_rank,
        macroscopic_long_rank_share=macroscopic_long_rank / increment,
        epoch_index_times_increment=epoch_index * increment,
        one_based_epoch_times_increment=(epoch_index + 1) * increment,
        dominant_band=dominant,
        normalized_bands=bands,
    )
    cells = tuple(
        _EpochCellSummary(
            rank_band_lower=key[0],
            absolute_magnitude_band_lower=key[1],
            atom_count=values[0],
            charge_numerator=values[1],
            first_atom=values[2],
        )
        for key, values in sorted(cell_accumulators.items())
    )
    return _EpochScan(
        audit=audit,
        charge_denominator=charge_denominator,
        genuine_spans=tuple(genuine_spans),
        genuine_cells=cells,
    )


def epoch_birth_budget_audit(
    points: Sequence[int], *, old_count: int
) -> EpochBirthBudgetAudit:
    """Audit the exact positive increment and both independent Q forms."""
    marks = _validated_golomb(points)
    return _scan_epoch(marks, old_count).audit


def _global_cells(atoms: Iterable[BirthAtom]) -> tuple[GlobalMagnitudeLagCell, ...]:
    genuine = tuple(atom for atom in atoms if atom.kind == "genuine")
    spans = tuple(atom.span for atom in genuine)
    if len(spans) != len(set(spans)):
        raise AssertionError("a genuine Golomb difference was charged twice")
    grouped: dict[tuple[int, int], list[BirthAtom]] = defaultdict(list)
    for atom in genuine:
        grouped[(atom.rank_band_lower, atom.absolute_magnitude_band_lower)].append(atom)
    cells: list[GlobalMagnitudeLagCell] = []
    for (rank_lower, magnitude_lower), rows in sorted(grouped.items()):
        capacity = magnitude_lower
        if len(rows) > capacity:
            raise AssertionError("the numerical magnitude capacity was exceeded")
        cells.append(
            GlobalMagnitudeLagCell(
                rank_band_lower=rank_lower,
                absolute_magnitude_band_lower=magnitude_lower,
                atom_count=len(rows),
                integer_capacity=capacity,
                occupancy_to_capacity=Fraction(len(rows), capacity),
                occupancy_to_rank_lower=Fraction(len(rows), rank_lower),
                envelope_upper_load_to_capacity=Fraction(len(rows), capacity),
                total_charge=sum((row.charge for row in rows), Fraction(0)),
                first_atom=(
                    rows[0].epoch,
                    rows[0].left,
                    rows[0].right,
                    rows[0].arithmetic_rank_lag,
                    rows[0].span,
                ),
            )
        )
    return tuple(cells)


def audit_fixture(
    name: str,
    provenance: str,
    points: Sequence[int],
    *,
    audited_mark_count: int | None = None,
) -> FixtureAudit:
    """Audit all complete dyadic births in one authenticated finite fixture."""
    marks = _validated_golomb(points)
    count = len(marks) if audited_mark_count is None else audited_mark_count
    if not _is_power_of_two(count) or count < 2 or count > len(marks):
        raise ValueError("audited_mark_count must be an available power of two")
    audited = marks[:count]
    epochs: list[EpochBirthBudgetAudit] = []
    global_spans: set[int] = set()
    global_accumulators: dict[tuple[int, int], list[Any]] = {}
    epoch = 1
    while 2 * epoch <= count:
        scan = _scan_epoch(audited, epoch)
        epochs.append(scan.audit)
        for span in scan.genuine_spans:
            if span in global_spans:
                raise AssertionError("a genuine Golomb difference was charged twice")
            global_spans.add(span)
        for cell in scan.genuine_cells:
            key = (cell.rank_band_lower, cell.absolute_magnitude_band_lower)
            accumulator = global_accumulators.setdefault(
                key,
                [0, Fraction(0), cell.first_atom],
            )
            accumulator[0] += cell.atom_count
            accumulator[1] += Fraction(
                cell.charge_numerator,
                scan.charge_denominator,
            )
        epoch *= 2
    cells = tuple(
        GlobalMagnitudeLagCell(
            rank_band_lower=key[0],
            absolute_magnitude_band_lower=key[1],
            atom_count=values[0],
            integer_capacity=key[1],
            occupancy_to_capacity=Fraction(values[0], key[1]),
            occupancy_to_rank_lower=Fraction(values[0], key[0]),
            envelope_upper_load_to_capacity=Fraction(values[0], key[1]),
            total_charge=values[1],
            first_atom=values[2],
        )
        for key, values in sorted(global_accumulators.items())
    )
    if any(cell.atom_count > cell.integer_capacity for cell in cells):
        raise AssertionError("the numerical magnitude capacity was exceeded")
    expected_pairs = count * (count - 1) // 2
    pair_count = sum(row.birth_pair_count for row in epochs)
    if pair_count != expected_pairs:
        raise AssertionError("the dyadic births failed to partition every pair")
    largest = max(epochs, key=lambda row: (row.increment, -row.epoch))
    return FixtureAudit(
        name=name,
        provenance=provenance,
        supplied_mark_count=len(marks),
        audited_mark_count=count,
        points_sha256=_points_sha256(marks),
        audited_prefix_sha256=_points_sha256(audited),
        all_prefix_c1_to_audited_count=_all_prefix_c1_fast(audited),
        pair_partition_count=pair_count,
        cumulative_birth_budget=sum(
            (row.increment for row in epochs),
            Fraction(0),
        ),
        largest_increment=largest.increment,
        largest_increment_epoch=largest.epoch,
        maximum_global_cell_occupancy_to_rank_lower=max(
            (cell.occupancy_to_rank_lower for cell in cells),
            default=Fraction(0),
        ),
        maximum_global_cell_occupancy_to_capacity=max(
            (cell.occupancy_to_capacity for cell in cells),
            default=Fraction(0),
        ),
        epoch_rows=tuple(epochs),
        global_cells=cells,
    )


def _candidate_cell_failures(
    points: tuple[int, ...],
) -> tuple[tuple[GlobalMagnitudeLagCell, ...], tuple[GlobalMagnitudeLagCell, ...]]:
    accumulators: dict[tuple[int, int], list[Any]] = {}
    epoch = 1
    while 2 * epoch <= len(points):
        scan = _scan_epoch(points, epoch)
        for cell in scan.genuine_cells:
            key = (cell.rank_band_lower, cell.absolute_magnitude_band_lower)
            accumulator = accumulators.setdefault(
                key,
                [0, Fraction(0), cell.first_atom],
            )
            accumulator[0] += cell.atom_count
            accumulator[1] += Fraction(
                cell.charge_numerator,
                scan.charge_denominator,
            )
        epoch *= 2
    cells = tuple(
        GlobalMagnitudeLagCell(
            rank_band_lower=key[0],
            absolute_magnitude_band_lower=key[1],
            atom_count=values[0],
            integer_capacity=key[1],
            occupancy_to_capacity=Fraction(values[0], key[1]),
            occupancy_to_rank_lower=Fraction(values[0], key[0]),
            envelope_upper_load_to_capacity=Fraction(values[0], key[1]),
            total_charge=values[1],
            first_atom=values[2],
        )
        for key, values in sorted(accumulators.items())
    )
    one_per_cell = tuple(cell for cell in cells if cell.atom_count > 1)
    rank_capacity = tuple(
        cell for cell in cells if cell.atom_count > cell.rank_band_lower
    )
    return one_per_cell, rank_capacity


@lru_cache(maxsize=1)
def exhaustive_four_mark_c1_audit() -> dict[str, Any]:
    """Exhaust all normalized four-mark all-prefix-``C=1`` rulers."""
    rulers = tuple(enumerate_compatible_four_mark_rulers())
    rows: list[
        tuple[tuple[int, ...], EpochBirthBudgetAudit, EpochBirthBudgetAudit]
    ] = []
    cell_one_failures: list[tuple[int, tuple[int, ...], GlobalMagnitudeLagCell]] = []
    cell_rank_failures: list[tuple[int, tuple[int, ...], GlobalMagnitudeLagCell]] = []
    for points in rulers:
        first = epoch_birth_budget_audit(points, old_count=1)
        second = epoch_birth_budget_audit(points, old_count=2)
        rows.append((points, first, second))
        one, rank = _candidate_cell_failures(points)
        if one:
            cell_one_failures.append((points[-1], points, one[0]))
        if rank:
            cell_rank_failures.append((points[-1], points, rank[0]))

    def extremum(index: int, *, maximum: bool) -> tuple[Fraction, tuple[int, ...]]:
        keyed = ((row[index].increment, row[0]) for row in rows)
        return max(keyed) if maximum else min(keyed)

    cumulative = tuple(
        (first.increment + second.increment, points) for points, first, second in rows
    )
    minimal_one = min(cell_one_failures)
    minimal_rank = min(cell_rank_failures)
    return {
        "scope": "all normalized four-mark all-prefix-C=1 Golomb rulers",
        "scope_is_exhaustive": True,
        "ruler_count": len(rulers),
        "epoch_1_minimum": extremum(1, maximum=False),
        "epoch_1_maximum": extremum(1, maximum=True),
        "epoch_2_minimum": extremum(2, maximum=False),
        "epoch_2_maximum": extremum(2, maximum=True),
        "cumulative_minimum": min(cumulative),
        "cumulative_maximum": max(cumulative),
        "strict_epoch_decrease_count": sum(
            second.increment < first.increment for _, first, second in rows
        ),
        "cell_one_failure_count": len(cell_one_failures),
        "cell_one_minimum_diameter_witness": {
            "points": minimal_one[1],
            "cell": minimal_one[2],
        },
        "cell_rank_lower_failure_count": len(cell_rank_failures),
        "cell_rank_lower_minimum_diameter_witness": {
            "points": minimal_rank[1],
            "cell": minimal_rank[2],
        },
    }


@lru_cache(maxsize=1)
def bounded_eight_mark_c1_audit() -> dict[str, Any]:
    """Exhaust the all-prefix-C=1 subscope with terminal mark at most 40."""
    exhaustion = bounded_golomb_exhaustion(
        mark_count=8,
        maximum_last_mark=40,
    )
    rulers = tuple(
        points for points in exhaustion.rulers if _all_prefix_c1_fast(points)
    )
    rows: list[
        tuple[
            tuple[int, ...],
            EpochBirthBudgetAudit,
            EpochBirthBudgetAudit,
            EpochBirthBudgetAudit,
        ]
    ] = []
    for points in rulers:
        rows.append(
            (
                points,
                epoch_birth_budget_audit(points, old_count=1),
                epoch_birth_budget_audit(points, old_count=2),
                epoch_birth_budget_audit(points, old_count=4),
            )
        )
    monotonic_failures = tuple(
        row for row in rows if row[3].increment > row[2].increment
    )
    harmonic_failures = tuple(
        row for row in rows if 2 * row[3].increment > row[2].increment
    )
    minimal_monotonic = min(
        monotonic_failures,
        key=lambda row: (row[0][-1], row[0]),
    )
    minimal_harmonic = min(
        harmonic_failures,
        key=lambda row: (row[0][-1], row[0]),
    )

    def witness(
        row: tuple[
            tuple[int, ...],
            EpochBirthBudgetAudit,
            EpochBirthBudgetAudit,
            EpochBirthBudgetAudit,
        ],
        *,
        harmonic: bool,
    ) -> dict[str, Any]:
        previous = row[2].increment
        newest = row[3].increment
        return {
            "points": row[0],
            "epoch_2_increment": previous,
            "epoch_4_increment": newest,
            "margin": (2 * newest - previous) if harmonic else (newest - previous),
        }

    return {
        "scope": (
            "all normalized eight-mark Golomb rulers with terminal mark at most "
            "40, restricted to rulers obeying every C=1 prefix cap"
        ),
        "scope_is_exhaustive": True,
        "unrestricted_ruler_count": exhaustion.ruler_count,
        "c1_ruler_count": len(rulers),
        "search_node_count": exhaustion.search_node_count,
        "newest_increment_increase_count": len(monotonic_failures),
        "newest_increment_minimum_diameter_witness": witness(
            minimal_monotonic,
            harmonic=False,
        ),
        "harmonic_schedule_failure_count": len(harmonic_failures),
        "harmonic_schedule_minimum_diameter_witness": witness(
            minimal_harmonic,
            harmonic=True,
        ),
    }


@lru_cache(maxsize=2)
def fixture_audits(
    source_certificate: str = str(DEFAULT_SOURCE_CERTIFICATE),
) -> tuple[FixtureAudit, ...]:
    source_path = Path(source_certificate)
    fixtures = load_authenticated_wave6_fixtures(source_path)
    long_points = mian_chowla_third_at_661_points()
    rows: list[FixtureAudit] = [
        audit_fixture(
            "perfect_four",
            "canonical exact four-mark Golomb ruler",
            PERFECT_FOUR,
        ),
        audit_fixture(
            "wave6_hall_counterexample_64",
            "Wave 6 exact Hall-decay counterexample constant",
            COUNTEREXAMPLE_64_POINTS,
        ),
    ]
    rows.extend(
        audit_fixture(
            f"wave6_authenticated_64_{index}",
            "hash-authenticated Wave 6 arithmetic certificate fixture",
            points,
        )
        for index, points in enumerate(fixtures.sixty_four_mark_points)
    )
    rows.extend(
        (
            audit_fixture(
                "wave6_authenticated_128",
                "hash-authenticated Wave 6 arithmetic certificate fixture",
                fixtures.one_hundred_twenty_eight_mark_points,
            ),
            audit_fixture(
                "wave7_erdos_turan_512_p1423",
                (
                    "exact p=1423 Erdős--Turán finite window; not an all-prefix "
                    "critical branch"
                ),
                erdos_turan_ruler(512, 1423),
            ),
            audit_fixture(
                "wave8_modified_greedy_682_prefix_512",
                (
                    "independently reconstructed 682-mark modified greedy ruler; "
                    "birth budget audited only through its complete 512-mark prefix"
                ),
                long_points,
                audited_mark_count=512,
            ),
        )
    )
    return tuple(rows)


def _file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _encode(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if hasattr(value, "__dataclass_fields__"):
        return _encode(asdict(value))
    if isinstance(value, tuple | list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _encode(item) for key, item in value.items()}
    return value


def build_certificate(
    source_certificate: str | Path = DEFAULT_SOURCE_CERTIFICATE,
) -> dict[str, Any]:
    """Build the byte-stable finite Wave 9 certificate."""
    source_path = Path(source_certificate).resolve()
    directory = Path(__file__).resolve().parent
    fixtures = fixture_audits(str(source_path))
    long_fixture = next(
        row for row in fixtures if row.name == "wave8_modified_greedy_682_prefix_512"
    )
    et_fixture = next(
        row for row in fixtures if row.name == "wave7_erdos_turan_512_p1423"
    )
    payload: dict[str, Any] = {
        "schema": "wave9_birth_budget_probe_v1",
        "research_date": "2026-08-29",
        "purpose": (
            "exact per-epoch positive B_H increments, two-parameter band calibration, "
            "and minimal finite counterexamples to overly local surrogates for P15"
        ),
        "source_authentication": {
            "wave6_arithmetic_certificate": source_path.name,
            "wave6_arithmetic_certificate_file_sha256": _file_sha256(source_path),
            "wave9_source_sha256": _file_sha256(Path(__file__).resolve()),
            "dependency_sha256": {
                name: _file_sha256(directory / name)
                for name in (
                    "complete_birth_ledger.py",
                    "wave6_hall_candidate_probe.py",
                    "wave7_band_renewal_probe.py",
                    "wave8_density_candidate_search.py",
                    "wave8_pair_telescope.py",
                )
            },
        },
        "exact_atom_envelope": {
            "statement": (
                "for every birth atom, 3*charge <= (rank_lag/(2m))^2*(span/N_(2m))^2"
            ),
            "genuine_span_meaning": "span=a_j-a_(i-1) for i>=1",
            "boundary_span_meaning": "span=a_j+1 for the artificial i=0 row",
            "global_magnitude_capacity": (
                "genuine spans are globally distinct; a dyadic magnitude interval "
                "[M,2M) contains at most M of them"
            ),
        },
        "exhaustive_four_mark_c1": exhaustive_four_mark_c1_audit(),
        "bounded_eight_mark_c1": bounded_eight_mark_c1_audit(),
        "fixture_audits": fixtures,
        "candidate_verdicts": {
            "CELL_ONE": {
                "candidate": (
                    "at most one genuine atom in each absolute dyadic "
                    "rank-lag/magnitude cell"
                ),
                "verdict": "REFUTED",
                "minimum_witness": PERFECT_FOUR,
            },
            "CELL_RANK": {
                "candidate": (
                    "cell occupancy is at most the lower endpoint of its dyadic "
                    "rank-lag band"
                ),
                "verdict": "REFUTED",
                "minimum_witness": PERFECT_FOUR,
                "finite_required_constant_modified_512": (
                    long_fixture.maximum_global_cell_occupancy_to_rank_lower
                ),
                "finite_required_constant_erdos_turan_512": (
                    et_fixture.maximum_global_cell_occupancy_to_rank_lower
                ),
            },
            "EPOCH_MONOTONE": {
                "candidate": "Delta B_(2m) <= Delta B_m at every finite C=1 step",
                "verdict": "REFUTED_IN_COMPLETE_BOUNDED_EIGHT_MARK_SCOPE",
            },
            "HARMONIC_MONOTONE": {
                "candidate": ("j*Delta B_(2^j) is nonincreasing from j=1 onward"),
                "verdict": "REFUTED_IN_COMPLETE_BOUNDED_EIGHT_MARK_SCOPE",
                "scope_warning": (
                    "this rejects only the literal pointwise schedule, not an "
                    "eventual logarithmic Cesaro statement on an infinite branch"
                ),
            },
            "MACROSCOPIC_LONG_RANK_DECAY": {
                "candidate": (
                    "the share from genuine atoms with span>N/2 and dyadic "
                    "rank-lag band at least m/2 is already small at long finite "
                    "critical scales"
                ),
                "verdict": "REFUTED_AS_A_UNIFORM_FINITE_SCALE_SURROGATE",
                "modified_512_latest_share": (
                    long_fixture.epoch_rows[-1].macroscopic_long_rank_share
                ),
                "erdos_turan_512_latest_share": (
                    et_fixture.epoch_rows[-1].macroscopic_long_rank_share
                ),
                "scope_warning": (
                    "persistent finite macroscopic mass does not prove the same "
                    "behavior on one infinite eventually critical branch"
                ),
            },
            "UNIQUE_MAGNITUDE_CAPACITY": {
                "candidate": (
                    "a genuine absolute magnitude cell [M,2M) has occupancy <= M"
                ),
                "verdict": "VERIFIED_AND_ALGEBRAICALLY_FORCED_BY_GOLOMB_UNIQUENESS",
                "limitation": (
                    "the capacity bound alone has no vanishing factor across epochs"
                ),
            },
        },
        "conclusions": {
            "finite_computation_only": True,
            "infinite_survival_inferred": False,
            "p15_proved": False,
            "erdos_1191_resolved": False,
            "main_observation": (
                "raw birth increments stay around a fixed positive scale on several "
                "long finite fixtures, while literal bounded-overlap cell injections "
                "already fail at four marks; a successful P15 theorem must use a "
                "history-sensitive charge stronger than global difference uniqueness"
            ),
        },
    }
    encoded = _encode(payload)
    canonical = json.dumps(encoded, sort_keys=True, separators=(",", ":"))
    encoded["certificate_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-certificate",
        type=Path,
        default=DEFAULT_SOURCE_CERTIFICATE,
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=(
            Path(__file__).resolve().parent
            / "wave9_birth_budget_certificate_2026-08-29.json"
        ),
    )
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.source_certificate)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(arguments.output)
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()

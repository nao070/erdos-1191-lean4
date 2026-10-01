"""Exact finite probe for the Wave 11 Abel repayment obligation P16.

Every logarithmic quantity is stored as a finite linear form

    sum_d c_d log(d),  c_d in Q,

so all Abel identities and decompositions use only :class:`fractions.Fraction`.
Floating evaluations are explicitly labelled projections.  Small finite
counterexamples are signed by clearing all coefficient denominators and
comparing the resulting integer products exactly.

The probe computes the Wave 10 quantities ``A, Q, T, F, P, S, U`` and the
exact residual ``U-P-S=sum Y_m``.  It also splits ``P`` canonically into a
numerical-hole premium and a coefficient-rearrangement premium, then records
detailed statistics for the lower-shell ramp responsible for the missing
quarter.  All conclusions are finite; no fixture is promoted to
``surv_C=infinity``.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass
from fractions import Fraction
from functools import cache
from hashlib import sha256
from math import fsum, gcd, isqrt, lgamma, log, log1p
from pathlib import Path
from typing import Any

from complete_birth_ledger import critical_modulus_cap, erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave7_band_renewal_probe import load_authenticated_wave6_fixtures
from wave8_density_candidate_search import mian_chowla_third_at_661_points
from wave8_survival_debt_probe import bounded_golomb_exhaustion
from wave10_log_product_packing import closed_birth_shell_coefficients

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_SOURCE_CERTIFICATE = (
    DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
)


def _lcm(left: int, right: int) -> int:
    return left // gcd(left, right) * right


@cache
def _log_integer(value: int) -> float:
    return log(value)


@dataclass(frozen=True)
class ExactLogForm:
    """A canonical exact rational linear combination of integer logarithms."""

    terms: tuple[tuple[int, Fraction], ...]

    @classmethod
    def zero(cls) -> ExactLogForm:
        return cls(())

    @classmethod
    def from_terms(cls, terms: Iterable[tuple[int, Fraction | int]]) -> ExactLogForm:
        combined: defaultdict[int, Fraction] = defaultdict(Fraction)
        for base, coefficient in terms:
            if not isinstance(base, int) or base < 1:
                raise ValueError("logarithm bases must be positive integers")
            combined[base] += Fraction(coefficient)
        return cls(
            tuple(
                (base, coefficient)
                for base, coefficient in sorted(combined.items())
                if base != 1 and coefficient
            )
        )

    @property
    def is_zero(self) -> bool:
        return not self.terms

    def __add__(self, other: ExactLogForm) -> ExactLogForm:
        if not isinstance(other, ExactLogForm):
            return NotImplemented
        merged: list[tuple[int, Fraction]] = []
        left_index = 0
        right_index = 0
        while left_index < len(self.terms) and right_index < len(other.terms):
            left_base, left_coefficient = self.terms[left_index]
            right_base, right_coefficient = other.terms[right_index]
            if left_base < right_base:
                merged.append((left_base, left_coefficient))
                left_index += 1
            elif right_base < left_base:
                merged.append((right_base, right_coefficient))
                right_index += 1
            else:
                coefficient = left_coefficient + right_coefficient
                if coefficient:
                    merged.append((left_base, coefficient))
                left_index += 1
                right_index += 1
        merged.extend(self.terms[left_index:])
        merged.extend(other.terms[right_index:])
        return ExactLogForm(tuple(merged))

    def __neg__(self) -> ExactLogForm:
        return ExactLogForm(
            tuple((base, -coefficient) for base, coefficient in self.terms)
        )

    def __sub__(self, other: ExactLogForm) -> ExactLogForm:
        if not isinstance(other, ExactLogForm):
            return NotImplemented
        return self + (-other)

    def scale(self, factor: Fraction | int) -> ExactLogForm:
        multiplier = Fraction(factor)
        if not multiplier:
            return ExactLogForm.zero()
        return ExactLogForm(
            tuple((base, multiplier * coefficient) for base, coefficient in self.terms)
        )

    def evaluate(self) -> float:
        return fsum(
            float(coefficient) * _log_integer(base) for base, coefficient in self.terms
        )

    def digest(self) -> str:
        canonical = ";".join(
            f"{base}:{coefficient.numerator}/{coefficient.denominator}"
            for base, coefficient in self.terms
        )
        return sha256(canonical.encode("ascii")).hexdigest()

    def cleared_products(
        self, *, maximum_exponent_mass: int = 1_000_000
    ) -> tuple[int, int, int]:
        """Return exact numerator, denominator, and common exponent scale."""
        common_denominator = 1
        for _, coefficient in self.terms:
            common_denominator = _lcm(common_denominator, coefficient.denominator)
        exponents = tuple(
            (
                base,
                coefficient.numerator * (common_denominator // coefficient.denominator),
            )
            for base, coefficient in self.terms
        )
        exponent_mass = sum(abs(exponent) for _, exponent in exponents)
        if exponent_mass > maximum_exponent_mass:
            raise ValueError("cleared exact product exceeds the configured size guard")
        numerator = 1
        denominator = 1
        for base, exponent in exponents:
            if exponent > 0:
                numerator *= base**exponent
            elif exponent < 0:
                denominator *= base ** (-exponent)
        return numerator, denominator, common_denominator

    def exact_sign(self, *, maximum_exponent_mass: int = 1_000_000) -> int:
        numerator, denominator, _ = self.cleared_products(
            maximum_exponent_mass=maximum_exponent_mass
        )
        return (numerator > denominator) - (numerator < denominator)


def _validated_golomb(points: Sequence[int], *, minimum: int = 8) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < minimum
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
    if len(differences) != len(marks) * (len(marks) - 1) // 2:
        raise ValueError("points must form a Golomb ruler")
    return marks


def _interval_difference(points: tuple[int, ...], interval: tuple[int, int]) -> int:
    left, right = interval
    return points[right] - points[left - 1]


def _available_epochs(
    marks: tuple[int, ...], audited_terminal_mark_count: int | None = None
) -> tuple[int, ...]:
    limit = len(marks)
    if audited_terminal_mark_count is not None:
        if audited_terminal_mark_count < 8:
            raise ValueError("audited terminal mark count must be at least eight")
        limit = min(limit, audited_terminal_mark_count)
    epochs: list[int] = []
    m = 4
    while 2 * m <= limit:
        epochs.append(m)
        m *= 2
    if not epochs:
        raise ValueError("no complete Abel birth shell is available")
    return tuple(epochs)


@dataclass(frozen=True)
class BulkAtom:
    epoch: int
    left_gap: int
    right_gap: int
    length: int
    difference: int
    weight: Fraction
    coefficient_class: str
    lower_shell_ramp: bool
    prefix_difference_rank: int
    prefix_numerical_holes: int


@dataclass(frozen=True)
class LowerShellStats:
    ramp_atom_count: int
    ramp_weight_mass: Fraction
    minimum_difference: int
    maximum_difference: int
    minimum_bulk_rank: int
    maximum_bulk_rank: int
    minimum_selected_numerical_holes: int
    maximum_selected_numerical_holes: int
    total_selected_numerical_holes: int
    minimum_prefix_numerical_holes: int
    maximum_prefix_numerical_holes: int
    total_prefix_numerical_holes: int
    minimum_ideal_weight_rank: int
    maximum_ideal_weight_rank: int
    maximum_absolute_rank_displacement: Fraction
    actual_log_mass: ExactLogForm
    hole_premium: ExactLogForm


def _prefix_difference_ranks(points: tuple[int, ...], count: int) -> dict[int, int]:
    values = sorted(
        points[right] - points[left]
        for right in range(1, count)
        for left in range(right)
    )
    return {value: rank for rank, value in enumerate(values, 1)}


def _coefficient_class(m: int, left: int, right: int) -> str:
    length = right - left + 1
    if right == m - 1:
        return "lower_singleton" if length == 1 else "lower_ramp"
    if length == 1:
        return "weight_four"
    if length == 2:
        return "weight_one"
    return "weight_two"


def _direct_birth_shell_form(points: tuple[int, ...], m: int) -> ExactLogForm:
    count = 2 * m
    terms: list[tuple[int, Fraction]] = []
    for left in range(1, count - 2):
        for right in range(max(m, left + 2), count):
            weight = Fraction((right - left) ** 2, count * count)
            terms.extend(
                (
                    (points[right - 1] - points[left - 1], weight),
                    (points[right] - points[left], weight),
                    (points[right - 1] - points[left], -weight),
                    (points[right] - points[left - 1], -weight),
                )
            )
    return ExactLogForm.from_terms(terms)


def _global_floor(atoms: Sequence[BulkAtom]) -> ExactLogForm:
    weights = sorted((atom.weight for atom in atoms), reverse=True)
    return ExactLogForm(
        tuple((rank, weight) for rank, weight in enumerate(weights, 1) if rank != 1)
    )


def _rank_forms(
    atoms: Sequence[BulkAtom], floor: ExactLogForm
) -> tuple[ExactLogForm, ExactLogForm, ExactLogForm, dict[int, int]]:
    ordered = sorted(atoms, key=lambda atom: atom.difference)
    if len({atom.difference for atom in ordered}) != len(ordered):
        raise AssertionError("bulk differences must be globally distinct")
    ranks = {id(atom): rank for rank, atom in enumerate(ordered, 1)}
    rank_form = ExactLogForm(
        tuple((rank, atom.weight) for rank, atom in enumerate(ordered, 1) if rank != 1)
    )
    actual = ExactLogForm.from_terms((atom.difference, atom.weight) for atom in atoms)
    hole = actual - rank_form
    rearrangement = rank_form - floor
    return rank_form, hole, rearrangement, ranks


def _lower_shell_stats(
    atoms: Sequence[BulkAtom], ranks: Mapping[int, int]
) -> LowerShellStats:
    ramp = tuple(atom for atom in atoms if atom.lower_shell_ramp)
    if not ramp:
        raise AssertionError("every audited shell must contain a lower ramp")
    sorted_weights = sorted((atom.weight for atom in atoms), reverse=True)
    weight_ranges: dict[Fraction, tuple[int, int]] = {}
    for rank, weight in enumerate(sorted_weights, 1):
        if weight not in weight_ranges:
            weight_ranges[weight] = (rank, rank)
        else:
            weight_ranges[weight] = (weight_ranges[weight][0], rank)

    selected_holes = tuple(atom.difference - ranks[id(atom)] for atom in ramp)
    prefix_holes = tuple(atom.prefix_numerical_holes for atom in ramp)
    ideal_ranges = tuple(weight_ranges[atom.weight] for atom in ramp)
    displacements = tuple(
        abs(Fraction(ranks[id(atom)]) - Fraction(first + last, 2))
        for atom, (first, last) in zip(ramp, ideal_ranges, strict=True)
    )
    actual_log_mass = ExactLogForm.from_terms(
        (atom.difference, atom.weight) for atom in ramp
    )
    rank_log_mass = ExactLogForm.from_terms(
        (ranks[id(atom)], atom.weight) for atom in ramp
    )
    return LowerShellStats(
        ramp_atom_count=len(ramp),
        ramp_weight_mass=sum((atom.weight for atom in ramp), Fraction(0)),
        minimum_difference=min(atom.difference for atom in ramp),
        maximum_difference=max(atom.difference for atom in ramp),
        minimum_bulk_rank=min(ranks[id(atom)] for atom in ramp),
        maximum_bulk_rank=max(ranks[id(atom)] for atom in ramp),
        minimum_selected_numerical_holes=min(selected_holes),
        maximum_selected_numerical_holes=max(selected_holes),
        total_selected_numerical_holes=sum(selected_holes),
        minimum_prefix_numerical_holes=min(prefix_holes),
        maximum_prefix_numerical_holes=max(prefix_holes),
        total_prefix_numerical_holes=sum(prefix_holes),
        minimum_ideal_weight_rank=min(first for first, _ in ideal_ranges),
        maximum_ideal_weight_rank=max(last for _, last in ideal_ranges),
        maximum_absolute_rank_displacement=max(displacements),
        actual_log_mass=actual_log_mass,
        hole_premium=actual_log_mass - rank_log_mass,
    )


@dataclass(frozen=True)
class EpochAbelAudit:
    epoch: int
    terminal_mark_count: int
    bulk_atoms: tuple[BulkAtom, ...]
    a_bulk: ExactLogForm
    q_positive: ExactLogForm
    t_full_span: ExactLogForm
    f_floor: ExactLogForm
    p_premium: ExactLogForm
    s_boundary_slack: ExactLogForm
    u_certificate: ExactLogForm
    direct_y: ExactLogForm
    residual: ExactLogForm
    h_hole_premium: ExactLogForm
    r_rearrangement_premium: ExactLogForm
    lower_shell: LowerShellStats


def epoch_abel_audit(points: Sequence[int], *, m: int) -> EpochAbelAudit:
    marks = _validated_golomb(points)
    if m < 4 or m & (m - 1) or 2 * m > len(marks):
        raise ValueError("m must be an available dyadic epoch at least four")
    prefix = marks[: 2 * m]
    count = 2 * m
    coefficients = closed_birth_shell_coefficients(count)
    full_span = (1, count - 1)
    theta = Fraction((m - 1) ** 2, m * m)
    prefix_ranks = _prefix_difference_ranks(prefix, m)

    positive_terms: list[tuple[int, Fraction]] = []
    bulk_terms: list[tuple[int, Fraction]] = []
    atoms: list[BulkAtom] = []
    for interval, coefficient in coefficients.items():
        difference = _interval_difference(prefix, interval)
        if coefficient > 0:
            positive_terms.append((difference, Fraction(coefficient, count * count)))
            continue
        if interval == full_span:
            if Fraction(-coefficient, count * count) != theta:
                raise AssertionError("full-span coefficient is inconsistent")
            continue
        weight = Fraction(-coefficient, count * count)
        bulk_terms.append((difference, weight))
        left, right = interval
        rank = prefix_ranks[difference] if right == m - 1 else 0
        atoms.append(
            BulkAtom(
                epoch=m,
                left_gap=left,
                right_gap=right,
                length=right - left + 1,
                difference=difference,
                weight=weight,
                coefficient_class=_coefficient_class(m, left, right),
                lower_shell_ramp=right == m - 1 and left <= m - 2,
                prefix_difference_rank=rank,
                prefix_numerical_holes=(difference - rank) if rank else 0,
            )
        )

    a_bulk = ExactLogForm.from_terms(bulk_terms)
    q_positive = ExactLogForm.from_terms(positive_terms)
    t_full_span = ExactLogForm.from_terms(
        ((_interval_difference(prefix, full_span), theta),)
    )
    f_floor = _global_floor(atoms)
    _, hole, rearrangement, ranks = _rank_forms(atoms, f_floor)
    p_premium = a_bulk - f_floor
    s_boundary_slack = t_full_span.scale(2) - q_positive
    u_certificate = t_full_span - f_floor
    residual = u_certificate - p_premium - s_boundary_slack
    direct = _direct_birth_shell_form(prefix, m)
    if direct != q_positive - t_full_span - a_bulk or direct != residual:
        raise AssertionError("the exact Abel repayment identity failed")
    if p_premium != hole + rearrangement:
        raise AssertionError("the exact premium split failed")
    return EpochAbelAudit(
        epoch=m,
        terminal_mark_count=count,
        bulk_atoms=tuple(atoms),
        a_bulk=a_bulk,
        q_positive=q_positive,
        t_full_span=t_full_span,
        f_floor=f_floor,
        p_premium=p_premium,
        s_boundary_slack=s_boundary_slack,
        u_certificate=u_certificate,
        direct_y=direct,
        residual=residual,
        h_hole_premium=hole,
        r_rearrangement_premium=rearrangement,
        lower_shell=_lower_shell_stats(atoms, ranks),
    )


@dataclass(frozen=True)
class CumulativeAbelAudit:
    epochs: tuple[int, ...]
    bulk_atoms: tuple[BulkAtom, ...]
    a_bulk: ExactLogForm
    q_positive: ExactLogForm
    t_full_span: ExactLogForm
    f_floor: ExactLogForm
    p_premium: ExactLogForm
    s_boundary_slack: ExactLogForm
    u_certificate: ExactLogForm
    direct_y: ExactLogForm
    residual: ExactLogForm
    h_hole_premium: ExactLogForm
    r_rearrangement_premium: ExactLogForm
    lower_shell: LowerShellStats
    sum_log_epochs: ExactLogForm
    maximum_epoch_depth: int


def cumulative_abel_audit(
    points: Sequence[int], *, epochs: Sequence[int] | None = None
) -> CumulativeAbelAudit:
    marks = _validated_golomb(points)
    selected = tuple(epochs) if epochs is not None else _available_epochs(marks)
    if (
        not selected
        or tuple(sorted(set(selected))) != selected
        or any(m < 4 or m & (m - 1) or 2 * m > len(marks) for m in selected)
    ):
        raise ValueError(
            "epochs must be distinct available dyadic values at least four"
        )
    rows = tuple(epoch_abel_audit(marks, m=m) for m in selected)
    return _cumulative_from_epoch_rows(rows)


def _cumulative_from_epoch_rows(
    rows: Sequence[EpochAbelAudit],
) -> CumulativeAbelAudit:
    if not rows:
        raise ValueError("at least one epoch audit is required")
    selected = tuple(row.epoch for row in rows)
    if tuple(sorted(set(selected))) != selected:
        raise ValueError("epoch audit rows must be distinct and increasing")
    atoms = tuple(atom for row in rows for atom in row.bulk_atoms)
    a_bulk = sum((row.a_bulk for row in rows), ExactLogForm.zero())
    q_positive = sum((row.q_positive for row in rows), ExactLogForm.zero())
    t_full_span = sum((row.t_full_span for row in rows), ExactLogForm.zero())
    direct = sum((row.direct_y for row in rows), ExactLogForm.zero())
    f_floor = _global_floor(atoms)
    _, hole, rearrangement, ranks = _rank_forms(atoms, f_floor)
    p_premium = a_bulk - f_floor
    s_boundary_slack = t_full_span.scale(2) - q_positive
    u_certificate = t_full_span - f_floor
    residual = u_certificate - p_premium - s_boundary_slack
    if direct != residual or p_premium != hole + rearrangement:
        raise AssertionError("the cumulative exact repayment identity failed")
    return CumulativeAbelAudit(
        epochs=selected,
        bulk_atoms=atoms,
        a_bulk=a_bulk,
        q_positive=q_positive,
        t_full_span=t_full_span,
        f_floor=f_floor,
        p_premium=p_premium,
        s_boundary_slack=s_boundary_slack,
        u_certificate=u_certificate,
        direct_y=direct,
        residual=residual,
        h_hole_premium=hole,
        r_rearrangement_premium=rearrangement,
        lower_shell=_lower_shell_stats(atoms, ranks),
        sum_log_epochs=ExactLogForm.from_terms((m, 1) for m in selected),
        maximum_epoch_depth=selected[-1].bit_length() - 1,
    )


def _cross_ratio_form(
    points: tuple[int, ...], left_gap: int, right_gap: int
) -> ExactLogForm:
    """Return the primitive positive cross ratio ``C_(left_gap,right_gap)``."""
    if not (1 <= left_gap <= right_gap - 2 < len(points) - 1):
        raise ValueError("a primitive cross ratio needs two nonadjacent gaps")
    return ExactLogForm.from_terms(
        (
            (_interval_difference(points, (left_gap, right_gap - 1)), 1),
            (_interval_difference(points, (left_gap + 1, right_gap)), 1),
            (_interval_difference(points, (left_gap + 1, right_gap - 1)), -1),
            (_interval_difference(points, (left_gap, right_gap)), -1),
        )
    )


@dataclass(frozen=True)
class LowerTailRow:
    left_gap: int
    base_weight: Fraction
    initial_ratio: ExactLogForm
    consumed: ExactLogForm
    terminal_ratio: ExactLogForm
    cross_ratio_count: int
    primitive_cross_ratios_positive_exact: bool


@dataclass(frozen=True)
class LowerTailAudit:
    epoch: int
    terminal_right_gap: int
    initial_repayment: ExactLogForm
    boundary_minus_lower_shell: ExactLogForm
    consumed: ExactLogForm
    terminal_remainder: ExactLogForm
    identity_residual: ExactLogForm
    primitive_cross_ratio_count: int
    primitive_cross_ratios_positive_exact: bool
    rows: tuple[LowerTailRow, ...]

    @property
    def consumed_fraction_projection(self) -> float:
        initial = self.initial_repayment.evaluate()
        if initial <= 0:
            raise AssertionError("the lower-tail initial repayment must be positive")
        return self.consumed.evaluate() / initial


def lower_tail_audit(
    points: Sequence[int],
    *,
    m: int,
    terminal_right_gap: int | None = None,
    _epoch_audit: EpochAbelAudit | None = None,
) -> LowerTailAudit:
    """Audit the exact finite-horizon lower-quarter tail telescope.

    For ``H=terminal_right_gap`` this checks, as formal rational log forms,

    ``R_m = sum_i v_i (sum_(j=m)^H C_ij + log(D_iH/D_(i+1)H))``.

    No numerical logarithm is used for the identity itself.
    """
    marks = _validated_golomb(points)
    if m < 4 or m & (m - 1) or 2 * m > len(marks):
        raise ValueError("m must be an available dyadic epoch at least four")
    terminal = 2 * m - 1 if terminal_right_gap is None else terminal_right_gap
    if terminal < m or terminal >= len(marks):
        raise ValueError("the finite horizon must satisfy m <= H < mark count")

    rows: list[LowerTailRow] = []
    for left in range(1, m - 1):
        weight = Fraction((m - left) ** 2, 4 * m * m)
        initial_ratio = ExactLogForm.from_terms(
            (
                (_interval_difference(marks, (left, m - 1)), 1),
                (_interval_difference(marks, (left + 1, m - 1)), -1),
            )
        )
        cross_ratio_terms: list[tuple[int, Fraction | int]] = []
        primitive_positive = True
        for right in range(m, terminal + 1):
            cross_ratio = _cross_ratio_form(marks, left, right)
            cross_ratio_terms.extend(cross_ratio.terms)
            numerator = _interval_difference(marks, (left, right - 1)) * (
                _interval_difference(marks, (left + 1, right))
            )
            denominator = _interval_difference(marks, (left + 1, right - 1)) * (
                _interval_difference(marks, (left, right))
            )
            primitive_positive &= numerator > denominator
        consumed = ExactLogForm.from_terms(cross_ratio_terms)
        terminal_ratio = ExactLogForm.from_terms(
            (
                (_interval_difference(marks, (left, terminal)), 1),
                (_interval_difference(marks, (left + 1, terminal)), -1),
            )
        )
        if initial_ratio != consumed + terminal_ratio:
            raise AssertionError("one lower-tail row failed to telescope exactly")
        rows.append(
            LowerTailRow(
                left_gap=left,
                base_weight=weight,
                initial_ratio=initial_ratio,
                consumed=consumed,
                terminal_ratio=terminal_ratio,
                cross_ratio_count=terminal - m + 1,
                primitive_cross_ratios_positive_exact=primitive_positive,
            )
        )

    initial_repayment = sum(
        (row.initial_ratio.scale(row.base_weight) for row in rows),
        ExactLogForm.zero(),
    )
    consumed = sum(
        (row.consumed.scale(row.base_weight) for row in rows),
        ExactLogForm.zero(),
    )
    terminal_remainder = sum(
        (row.terminal_ratio.scale(row.base_weight) for row in rows),
        ExactLogForm.zero(),
    )
    epoch = _epoch_audit if _epoch_audit is not None else epoch_abel_audit(marks, m=m)
    if epoch.epoch != m:
        raise ValueError("the supplied cached epoch audit has the wrong epoch")
    lower_boundary = ExactLogForm.from_terms(
        (
            (
                _interval_difference(marks, (1, m - 1)),
                Fraction((m - 1) ** 2, 4 * m * m),
            ),
        )
    )
    full_lower_shell = ExactLogForm.from_terms(
        (atom.difference, atom.weight)
        for atom in epoch.bulk_atoms
        if atom.right_gap == m - 1
    )
    boundary_minus_lower_shell = lower_boundary - full_lower_shell
    identity_residual = initial_repayment - consumed - terminal_remainder
    if not identity_residual.is_zero:
        raise AssertionError("the weighted lower-tail identity failed")
    if boundary_minus_lower_shell != initial_repayment:
        raise AssertionError("the lower-shell Abel boundary identity failed")
    primitive_cross_ratio_count = sum(row.cross_ratio_count for row in rows)
    primitive_positive = all(row.primitive_cross_ratios_positive_exact for row in rows)
    if not primitive_positive:
        raise AssertionError("a primitive lower-tail cross ratio was nonpositive")
    return LowerTailAudit(
        epoch=m,
        terminal_right_gap=terminal,
        initial_repayment=initial_repayment,
        boundary_minus_lower_shell=boundary_minus_lower_shell,
        consumed=consumed,
        terminal_remainder=terminal_remainder,
        identity_residual=identity_residual,
        primitive_cross_ratio_count=primitive_cross_ratio_count,
        primitive_cross_ratios_positive_exact=primitive_positive,
        rows=tuple(rows),
    )


def _triangular_number(length: int) -> int:
    return length * (length + 1) // 2


@dataclass(frozen=True)
class SplitBulkFloorAudit:
    epochs: tuple[int, ...]
    actual_bulk: ExactLogForm
    lower_actual: ExactLogForm
    upper_actual: ExactLogForm
    lower_triangular_floor: ExactLogForm
    upper_global_floor: ExactLogForm
    combined_floor: ExactLogForm
    plain_global_floor: ExactLogForm
    lower_actual_minus_floor: ExactLogForm
    upper_actual_minus_floor: ExactLogForm
    actual_minus_combined_floor: ExactLogForm
    combined_floor_minus_plain_floor: ExactLogForm
    strengthened_envelope: ExactLogForm
    strengthened_residual: ExactLogForm
    lower_floor_termwise_verified: bool
    minimum_lower_integer_surplus: int
    lower_atom_count: int
    upper_atom_count: int


def split_bulk_floor_audit(
    points: Sequence[int],
    *,
    epochs: Sequence[int] | None = None,
    _cumulative_audit: CumulativeAbelAudit | None = None,
) -> SplitBulkFloorAudit:
    """Split the bulk into a triangular lower shell and globally sorted upper bulk."""
    cumulative = (
        _cumulative_audit
        if _cumulative_audit is not None
        else cumulative_abel_audit(points, epochs=epochs)
    )
    if epochs is not None and cumulative.epochs != tuple(epochs):
        raise ValueError("the supplied cached cumulative audit has the wrong epochs")
    lower_atoms = tuple(
        atom for atom in cumulative.bulk_atoms if atom.right_gap == atom.epoch - 1
    )
    upper_atoms = tuple(
        atom for atom in cumulative.bulk_atoms if atom.right_gap >= atom.epoch
    )
    if len(lower_atoms) + len(upper_atoms) != len(cumulative.bulk_atoms):
        raise AssertionError("the lower/upper bulk partition is incomplete")
    lower_actual = ExactLogForm.from_terms(
        (atom.difference, atom.weight) for atom in lower_atoms
    )
    upper_actual = ExactLogForm.from_terms(
        (atom.difference, atom.weight) for atom in upper_atoms
    )
    lower_floor = ExactLogForm.from_terms(
        (_triangular_number(atom.length), atom.weight) for atom in lower_atoms
    )
    upper_floor = _global_floor(upper_atoms)
    combined_floor = lower_floor + upper_floor
    actual_minus_combined_floor = cumulative.a_bulk - combined_floor
    strengthened_envelope = cumulative.t_full_span - combined_floor
    strengthened_residual = (
        strengthened_envelope
        - actual_minus_combined_floor
        - cumulative.s_boundary_slack
    )
    surpluses = tuple(
        atom.difference - _triangular_number(atom.length) for atom in lower_atoms
    )
    if lower_actual + upper_actual != cumulative.a_bulk:
        raise AssertionError("the lower/upper actual bulk split failed")
    if any(surplus < 0 for surplus in surpluses):
        raise AssertionError("a lower-shell interval violated the triangular floor")
    if strengthened_residual != cumulative.direct_y:
        raise AssertionError("the strengthened exact repayment identity failed")
    return SplitBulkFloorAudit(
        epochs=cumulative.epochs,
        actual_bulk=cumulative.a_bulk,
        lower_actual=lower_actual,
        upper_actual=upper_actual,
        lower_triangular_floor=lower_floor,
        upper_global_floor=upper_floor,
        combined_floor=combined_floor,
        plain_global_floor=cumulative.f_floor,
        lower_actual_minus_floor=lower_actual - lower_floor,
        upper_actual_minus_floor=upper_actual - upper_floor,
        actual_minus_combined_floor=actual_minus_combined_floor,
        combined_floor_minus_plain_floor=combined_floor - cumulative.f_floor,
        strengthened_envelope=strengthened_envelope,
        strengthened_residual=strengthened_residual,
        lower_floor_termwise_verified=True,
        minimum_lower_integer_surplus=min(surpluses),
        lower_atom_count=len(lower_atoms),
        upper_atom_count=len(upper_atoms),
    )


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    return all(value % divisor for divisor in range(3, isqrt(value) + 1, 2))


def _least_prime_at_least(value: int) -> int:
    candidate = value if value % 2 else value + 1
    if value <= 2:
        return 2
    while not _is_prime(candidate):
        candidate += 2
    return candidate


def _birth_shell_cross_ratio_float(points: tuple[int, ...], m: int) -> float:
    count = 2 * m
    if len(points) != count:
        raise ValueError("the calibration requires exactly 2m marks")
    terms: list[float] = []
    for right in range(m, count):
        for left in range(1, right - 1):
            d_left_before = points[right - 1] - points[left - 1]
            d_right_after = points[right] - points[left]
            d_inner = points[right - 1] - points[left]
            d_outer = points[right] - points[left - 1]
            numerator = d_left_before * d_right_after
            denominator = d_inner * d_outer
            if numerator <= denominator:
                raise AssertionError("the primitive cross ratio must exceed one")
            terms.append(
                ((right - left) / count) ** 2
                * log1p((numerator - denominator) / denominator)
            )
    return fsum(terms)


def _lower_triangular_floor_float(m: int) -> float:
    return fsum(
        Fraction(2 * length + 1, 4 * m * m) * log(_triangular_number(length))
        for length in range(2, m - 1)
    )


def _upper_single_shell_floor_float(m: int) -> float:
    weight_four_count = m - 1
    weight_two_count = (m - 1) * (3 * m - 8) // 2
    weight_one_count = m - 1
    first = weight_four_count
    second = first + weight_two_count
    total = second + weight_one_count
    scaled_log_floor = (
        4 * lgamma(first + 1)
        + 2 * (lgamma(second + 1) - lgamma(first + 1))
        + lgamma(total + 1)
        - lgamma(second + 1)
    )
    return scaled_log_floor / (4 * m * m)


def changing_erdos_turan_calibration(
    *, maximum_epoch: int = 1024
) -> tuple[dict[str, Any], ...]:
    """Calibrate the strengthened floor on changing finite ET windows.

    These rulers vary with ``m`` and therefore supply no fixed infinite
    branch.  All reported logarithmic evaluations are labelled floats.
    """
    if maximum_epoch < 16 or maximum_epoch & (maximum_epoch - 1):
        raise ValueError("maximum_epoch must be a power of two at least 16")
    rows: list[dict[str, Any]] = []
    m = 16
    while m <= maximum_epoch:
        count = 2 * m
        prime = _least_prime_at_least(count)
        points = erdos_turan_ruler(count, prime)
        y_value = _birth_shell_cross_ratio_float(points, m)
        lower_floor = _lower_triangular_floor_float(m)
        upper_floor = _upper_single_shell_floor_float(m)
        mixed_floor = lower_floor + upper_floor
        theta = Fraction((m - 1) ** 2, m * m)
        terminal = float(theta) * log(points[-1])
        strengthened_envelope = terminal - mixed_floor
        rows.append(
            {
                "epoch": m,
                "mark_count": count,
                "prime": prime,
                "points_sha256": sha256(
                    ",".join(str(point) for point in points).encode("ascii")
                ).hexdigest(),
                "Y_m_float_projection": format(y_value, ".17g"),
                "T_m_float_projection": format(terminal, ".17g"),
                "lower_triangular_floor_float_projection": format(lower_floor, ".17g"),
                "upper_global_floor_float_projection": format(upper_floor, ".17g"),
                "mixed_floor_float_projection": format(mixed_floor, ".17g"),
                "strengthened_envelope_float_projection": format(
                    strengthened_envelope, ".17g"
                ),
                "Y_over_strengthened_envelope_projection": format(
                    y_value / strengthened_envelope, ".17g"
                ),
                "changing_family_only": True,
                "infinite_branch_inferred": False,
            }
        )
        m *= 2
    return tuple(rows)


def candidate_margins(audit: CumulativeAbelAudit) -> dict[str, ExactLogForm]:
    """Return exact forms; a nonnegative sign means the candidate holds."""
    quarter_target = audit.sum_log_epochs.scale(Fraction(1, 4))
    return {
        "BULK_ONLY_FULL": audit.p_premium - audit.u_certificate,
        "BOUNDARY_ONLY_FULL": audit.s_boundary_slack - audit.u_certificate,
        "ALL_HOLE_FULL": audit.h_hole_premium - audit.u_certificate,
        "LOWER_HOLE_QUARTER": audit.lower_shell.hole_premium - quarter_target,
        "NORMALIZED_HARMONIC": audit.u_certificate.scale(
            Fraction(1, audit.maximum_epoch_depth)
        )
        - audit.direct_y,
        "MIXED_ZERO_RESIDUAL": audit.p_premium
        + audit.s_boundary_slack
        - audit.u_certificate,
    }


@cache
def _form_summary(form: ExactLogForm) -> dict[str, Any]:
    denominators = {coefficient.denominator for _, coefficient in form.terms}
    common_denominator = 1
    for denominator in denominators:
        common_denominator = _lcm(common_denominator, denominator)
    l1_numerator = sum(
        abs(coefficient.numerator) * (common_denominator // coefficient.denominator)
        for _, coefficient in form.terms
    )
    return {
        "term_count": len(form.terms),
        "coefficient_l1": str(Fraction(l1_numerator, common_denominator)),
        "formal_sha256": form.digest(),
        "float_projection": format(form.evaluate(), ".17g"),
    }


def _lower_summary(stats: LowerShellStats) -> dict[str, Any]:
    encoded = asdict(stats)
    encoded["ramp_weight_mass"] = str(stats.ramp_weight_mass)
    encoded["maximum_absolute_rank_displacement"] = str(
        stats.maximum_absolute_rank_displacement
    )
    encoded["actual_log_mass"] = _form_summary(stats.actual_log_mass)
    encoded["hole_premium"] = _form_summary(stats.hole_premium)
    return encoded


def _tail_summary(tail: LowerTailAudit) -> dict[str, Any]:
    consumed_fraction = tail.consumed_fraction_projection
    return {
        "epoch": tail.epoch,
        "terminal_right_gap_H": tail.terminal_right_gap,
        "primitive_cross_ratio_count": tail.primitive_cross_ratio_count,
        "primitive_cross_ratios_positive_exact_integer_products": (
            tail.primitive_cross_ratios_positive_exact
        ),
        "exact_identity_R_equals_consumed_plus_terminal_remainder": (
            tail.identity_residual.is_zero
        ),
        "exact_identity_R_equals_lower_boundary_minus_lower_shell": (
            tail.initial_repayment == tail.boundary_minus_lower_shell
        ),
        "R_m": _form_summary(tail.initial_repayment),
        "consumed_j_m_through_H": _form_summary(tail.consumed),
        "terminal_remainder": _form_summary(tail.terminal_remainder),
        "identity_residual": _form_summary(tail.identity_residual),
        "consumed_fraction_float_projection": format(consumed_fraction, ".17g"),
        "terminal_fraction_float_projection": format(
            tail.terminal_remainder.evaluate() / tail.initial_repayment.evaluate(),
            ".17g",
        ),
    }


def _split_summary(split: SplitBulkFloorAudit) -> dict[str, Any]:
    sum_log_epochs = ExactLogForm.from_terms((m, 1) for m in split.epochs)
    scale = sum_log_epochs.evaluate()
    forms = {
        "actual_bulk": split.actual_bulk,
        "lower_actual": split.lower_actual,
        "upper_actual": split.upper_actual,
        "lower_triangular_floor": split.lower_triangular_floor,
        "upper_global_floor": split.upper_global_floor,
        "combined_split_floor": split.combined_floor,
        "plain_global_floor": split.plain_global_floor,
        "lower_actual_minus_floor": split.lower_actual_minus_floor,
        "upper_actual_minus_floor": split.upper_actual_minus_floor,
        "actual_minus_combined_floor": split.actual_minus_combined_floor,
        "combined_floor_minus_plain_floor": (split.combined_floor_minus_plain_floor),
        "strengthened_envelope_T_minus_combined_floor": (split.strengthened_envelope),
        "strengthened_residual_equals_sum_Y": split.strengthened_residual,
    }
    return {
        "epochs": list(split.epochs),
        "lower_atom_count": split.lower_atom_count,
        "upper_atom_count": split.upper_atom_count,
        "lower_floor_termwise_verified": split.lower_floor_termwise_verified,
        "minimum_lower_integer_surplus_over_triangular_floor": (
            split.minimum_lower_integer_surplus
        ),
        "exact_identity_actual_equals_lower_plus_upper": (
            split.actual_bulk == split.lower_actual + split.upper_actual
        ),
        "exact_identity_strengthened_residual_equals_sum_Y": True,
        "exact_forms": {name: _form_summary(form) for name, form in forms.items()},
        "coefficient_calibration_float_projections": {
            "lower_floor_over_sum_log_m": format(
                split.lower_triangular_floor.evaluate() / scale, ".17g"
            ),
            "upper_floor_over_sum_log_m": format(
                split.upper_global_floor.evaluate() / scale, ".17g"
            ),
            "combined_floor_over_sum_log_m": format(
                split.combined_floor.evaluate() / scale, ".17g"
            ),
            "plain_floor_over_sum_log_m": format(
                split.plain_global_floor.evaluate() / scale, ".17g"
            ),
            "sum_Y_over_strengthened_envelope": format(
                split.strengthened_residual.evaluate()
                / split.strengthened_envelope.evaluate(),
                ".17g",
            ),
        },
    }


def _audit_summary(audit: CumulativeAbelAudit | EpochAbelAudit) -> dict[str, Any]:
    names = {
        "A_J": audit.a_bulk,
        "Q_J": audit.q_positive,
        "T_J": audit.t_full_span,
        "F_E": audit.f_floor,
        "P_J": audit.p_premium,
        "S_J": audit.s_boundary_slack,
        "U_E": audit.u_certificate,
        "sum_Y_m": audit.direct_y,
        "residual_U_minus_P_minus_S": audit.residual,
        "H_hole": audit.h_hole_premium,
        "R_rearrangement": audit.r_rearrangement_premium,
    }
    return {
        "epochs": list(audit.epochs)
        if isinstance(audit, CumulativeAbelAudit)
        else [audit.epoch],
        "bulk_atom_count": len(audit.bulk_atoms),
        "exact_forms": {name: _form_summary(form) for name, form in names.items()},
        "exact_identity_U_minus_P_minus_S_equals_sum_Y": (
            audit.residual == audit.direct_y
        ),
        "exact_identity_P_equals_H_plus_R": (
            audit.p_premium == audit.h_hole_premium + audit.r_rearrangement_premium
        ),
        "lower_shell": _lower_summary(audit.lower_shell),
    }


def _all_prefix_c1(points: Sequence[int]) -> bool:
    return all(
        points[count - 1] + 1 <= critical_modulus_cap(count)
        for count in range(2, len(points) + 1)
    )


def exhaustive_eight_mark_c1_audit() -> dict[str, Any]:
    exhaustion = bounded_golomb_exhaustion(mark_count=8, maximum_last_mark=40)
    rulers = tuple(points for points in exhaustion.rulers if _all_prefix_c1(points))
    candidate_names = tuple(candidate_margins(cumulative_abel_audit(rulers[0])).keys())
    failures: dict[str, list[tuple[tuple[int, ...], ExactLogForm, float]]] = {
        name: [] for name in candidate_names
    }
    all_margins: dict[str, list[tuple[tuple[int, ...], ExactLogForm, float]]] = {
        name: [] for name in candidate_names
    }
    calibrations: list[tuple[tuple[int, ...], CumulativeAbelAudit, float, float]] = []
    for points in rulers:
        audit = cumulative_abel_audit(points, epochs=(4,))
        y_value = audit.direct_y.evaluate()
        envelope_value = audit.u_certificate.evaluate()
        if envelope_value <= 0:
            raise AssertionError("the tested Abel envelope must be positive")
        calibrations.append((points, audit, y_value, y_value / envelope_value))
        for name, margin in candidate_margins(audit).items():
            sign = margin.exact_sign()
            all_margins[name].append((points, margin, margin.evaluate()))
            if sign < 0:
                failures[name].append((points, margin, margin.evaluate()))

    candidates: dict[str, Any] = {}
    for name, rows in failures.items():
        if not rows:
            minimum = min(
                all_margins[name], key=lambda row: (row[2], row[0][-1], row[0])
            )
            numerator, denominator, common = minimum[1].cleared_products()
            candidates[name] = {
                "failure_count": 0,
                "verdict": "NO_FAILURE_FOUND",
                "minimum_margin_witness_by_float_projection": minimum[0],
                "minimum_margin_float_projection": format(minimum[2], ".17g"),
                "exact_margin_common_denominator": common,
                "exact_margin_numerator": str(numerator),
                "exact_margin_denominator": str(denominator),
                "exact_margin_sign": minimum[1].exact_sign(),
            }
            continue
        minimum = min(rows, key=lambda row: (row[0][-1], row[0]))
        numerator, denominator, common = minimum[1].cleared_products()
        candidates[name] = {
            "failure_count": len(rows),
            "verdict": "REFUTED_IN_COMPLETE_BOUNDED_C1_SCOPE",
            "minimum_terminal_then_lexicographic_witness": minimum[0],
            "margin_float_projection": format(minimum[2], ".17g"),
            "exact_margin_common_denominator": common,
            "exact_margin_numerator": str(numerator),
            "exact_margin_denominator": str(denominator),
            "exact_margin_sign": -1,
        }
    max_y = max(calibrations, key=lambda row: (row[2], tuple(-x for x in row[0])))
    max_ratio = max(calibrations, key=lambda row: (row[3], tuple(-x for x in row[0])))
    return {
        "scope": (
            "all normalized eight-mark Golomb rulers with terminal mark at most "
            "40, restricted to rulers satisfying every C=1 prefix cap"
        ),
        "scope_is_exhaustive": True,
        "unrestricted_ruler_count": exhaustion.ruler_count,
        "c1_ruler_count": len(rulers),
        "search_node_count": exhaustion.search_node_count,
        "candidates": candidates,
        "constant_factor_calibration_float_projections": {
            "maximum_sum_Y_m": format(max_y[2], ".17g"),
            "maximum_sum_Y_m_witness": max_y[0],
            "maximum_residual_to_U_ratio": format(max_ratio[3], ".17g"),
            "minimum_repaid_fraction_one_minus_residual_to_U": format(
                1 - max_ratio[3], ".17g"
            ),
            "maximum_ratio_witness": max_ratio[0],
            "maximum_ratio_residual_form": _form_summary(max_ratio[1].direct_y),
            "maximum_ratio_U_form": _form_summary(max_ratio[1].u_certificate),
            "selection_warning": (
                "maxima are selected using labelled floating projections; the "
                "underlying numerator forms and all Abel identities are exact"
            ),
        },
    }


def _candidate_summary(audit: CumulativeAbelAudit) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for name, margin in candidate_margins(audit).items():
        value = margin.evaluate()
        rows[name] = {
            "margin": _form_summary(margin),
            "observed_holds": value >= 0,
        }
    return rows


def _fixture_summary(
    name: str,
    provenance: str,
    points: Sequence[int],
    *,
    audited_terminal_mark_count: int | None = None,
) -> dict[str, Any]:
    marks = _validated_golomb(points)
    epochs = _available_epochs(marks, audited_terminal_mark_count)
    rows = tuple(epoch_abel_audit(marks, m=m) for m in epochs)
    tails = tuple(
        lower_tail_audit(
            marks,
            m=m,
            terminal_right_gap=2 * m - 1,
            _epoch_audit=row,
        )
        for m, row in zip(epochs, rows, strict=True)
    )
    cumulative_rows = tuple(
        _cumulative_from_epoch_rows(rows[: index + 1]) for index in range(len(epochs))
    )
    split_rows = tuple(
        split_bulk_floor_audit(
            marks,
            epochs=epochs[: index + 1],
            _cumulative_audit=cumulative,
        )
        for index, cumulative in enumerate(cumulative_rows)
    )
    return {
        "name": name,
        "provenance": provenance,
        "supplied_mark_count": len(marks),
        "audited_terminal_mark_count": 2 * epochs[-1],
        "points_sha256": sha256(
            ",".join(str(point) for point in marks).encode("ascii")
        ).hexdigest(),
        "all_prefix_c1_to_audited_terminal": _all_prefix_c1(marks[: 2 * epochs[-1]]),
        "epoch_rows": [_audit_summary(row) for row in rows],
        "lower_tail_rows": [_tail_summary(row) for row in tails],
        "cumulative_rows": [
            {
                **_audit_summary(row),
                "candidate_margins": _candidate_summary(row),
                "split_bulk_floor": _split_summary(split),
            }
            for row, split in zip(cumulative_rows, split_rows, strict=True)
        ],
    }


def _file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _encode(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple | list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _encode(item) for key, item in value.items()}
    return value


def build_certificate(
    source_certificate: str | Path = DEFAULT_SOURCE_CERTIFICATE,
) -> dict[str, Any]:
    source_path = Path(source_certificate).resolve()
    authenticated = load_authenticated_wave6_fixtures(source_path)
    long_points = mian_chowla_third_at_661_points()
    fixtures: list[tuple[str, str, Sequence[int], int | None]] = [
        (
            "wave6_hall_counterexample_64",
            "Wave 6 exact Hall-decay counterexample constant",
            COUNTEREXAMPLE_64_POINTS,
            None,
        )
    ]
    fixtures.extend(
        (
            f"wave6_authenticated_64_{index}",
            "hash-authenticated Wave 6 arithmetic certificate fixture",
            points,
            None,
        )
        for index, points in enumerate(authenticated.sixty_four_mark_points)
    )
    fixtures.extend(
        (
            (
                "wave6_authenticated_128",
                "hash-authenticated Wave 6 heuristic continuation",
                authenticated.one_hundred_twenty_eight_mark_points,
                None,
            ),
            (
                "wave7_erdos_turan_512_p1423",
                "exact finite scaled Erdos--Turan window",
                erdos_turan_ruler(512, 1423),
                512,
            ),
            (
                "wave8_modified_greedy_682_audited_512",
                "independently reconstructed 682-mark fixture; complete dyadic audit through 512",
                long_points,
                512,
            ),
        )
    )
    payload: dict[str, Any] = {
        "schema": "wave11_abel_repayment_probe_v2",
        "research_date": "2026-08-29",
        "purpose": (
            "exact formal-log audit of A,Q,T,F,P,S,U and adversarial finite "
            "tests of Abel repayment candidates for P16, including the exact "
            "lower-tail telescope and triangular lower-shell floor"
        ),
        "source_authentication": {
            "wave6_arithmetic_certificate": source_path.name,
            "wave6_arithmetic_certificate_file_sha256": _file_sha256(source_path),
            "wave11_source_sha256": _file_sha256(Path(__file__).resolve()),
            "dependency_sha256": {
                name: _file_sha256(DIRECTORY / name)
                for name in (
                    "wave10_log_product_packing.py",
                    "wave8_survival_debt_probe.py",
                    "wave8_density_candidate_search.py",
                )
            },
        },
        "exact_representation": {
            "form": "sum_d c_d log(d) with c_d in Q",
            "identity_arithmetic": "fractions.Fraction only",
            "float_fields": (
                "labelled projections for ranking finite margins; small exhaustive "
                "counterexample signs are exact cleared-integer-product comparisons"
            ),
        },
        "exhaustive_eight_mark_c1": exhaustive_eight_mark_c1_audit(),
        "fixture_audits": [
            _fixture_summary(
                name, provenance, points, audited_terminal_mark_count=limit
            )
            for name, provenance, points, limit in fixtures
        ],
        "changing_erdos_turan_calibration": changing_erdos_turan_calibration(),
        "candidate_contracts": {
            "BULK_ONLY_FULL": "P_J >= U_E",
            "BOUNDARY_ONLY_FULL": "S_J >= U_E",
            "ALL_HOLE_FULL": "H_J >= U_E, where P_J=H_J+R_J",
            "LOWER_HOLE_QUARTER": (
                "lower-shell numerical-hole premium >= (1/4) sum log m"
            ),
            "NORMALIZED_HARMONIC": "sum Y_m <= U_E / floor(log_2 max(E))",
            "MIXED_ZERO_RESIDUAL": "P_J+S_J >= U_E",
        },
        "new_exact_finite_identities": {
            "lower_tail": (
                "R_m=sum_i ((m-i)/(2m))^2[sum_(j=m)^H C_ij+"
                "log(D_iH/D_(i+1)H)] for every finite H>=m"
            ),
            "lower_triangular_floor": (
                "D_(i,m-1)>=ell(ell+1)/2 for every lower-shell length ell, "
                "because its ell adjacent gaps are distinct positive integers"
            ),
            "split_floor": (
                "actual bulk >= lower triangular floor + global rearrangement "
                "floor of the upper bulk after deleting q=m-1"
            ),
        },
        "analytic_order_calibration": {
            "plain_floor": (
                "F_E=(7/4)sum log(m)+O(|E|), so the critical-cap envelope "
                "is O_C(J^2) on E_J"
            ),
            "split_floor": (
                "L_E=(1/2)sum log(m)+O(|E|) and the upper-only global floor "
                "is (3/2)sum log(m)+O(|E|)"
            ),
            "strengthened_envelope": (
                "T_E-[L_E+F_upper,E] <= sum log log(m)+O_C(|E|) = O_C(J log J) on E_J"
            ),
            "limitation": (
                "O_C(J log J) is not o(log J), and changing finite ET windows "
                "do not imply a fixed infinite branch"
            ),
        },
        "conclusions": {
            "finite_computation_only": True,
            "infinite_survival_inferred": False,
            "p16_proved": False,
            "p15_proved": False,
            "erdos_1191_resolved": False,
            "scope_warning": (
                "candidate failures reject only the literal finite inequalities; "
                "they do not reject eventual survival-conditioned repayment with "
                "an o(log J) residual"
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
        "--source-certificate", type=Path, default=DEFAULT_SOURCE_CERTIFICATE
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DIRECTORY / "wave11_abel_repayment_certificate_2026-08-29.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.source_certificate)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(arguments.output)
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()

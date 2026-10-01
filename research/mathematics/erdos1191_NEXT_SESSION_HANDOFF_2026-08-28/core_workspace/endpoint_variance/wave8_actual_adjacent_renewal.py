"""Exact hybrid ledger and shell-covariance identities for Wave 8.

The hybrid ledger augments the Wave 6 cross-antidiagonal families by the
*actual* internal adjacent-gap family born in each dyadic shell.  It uses no
asymptotic assumption: for a finite Golomb ruler, all selected endpoint pairs
are different, hence all their positive differences are different integers.

All computations use :class:`fractions.Fraction` and are independently
auditable.  The module does not claim that a finite ruler has an infinite
critical extension.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, replace
from fractions import Fraction
from math import floor

from wave6_collision_bands import (
    antidiagonal_threshold,
    dyadic_antidiagonal_band,
    dyadic_shell_profile,
)


def _validated_marks(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or any(not isinstance(mark, int) for mark in marks)
        or marks != tuple(sorted(set(marks)))
        or marks[0] != 0
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    return marks


def dyadic_epochs(mark_count: int) -> tuple[int, ...]:
    """Return every ``m`` for which the complete shell ``m -> 2m`` exists."""
    if not isinstance(mark_count, int) or mark_count < 2:
        raise ValueError("mark_count must be an integer at least two")
    epochs: list[int] = []
    epoch = 1
    while 2 * epoch <= mark_count:
        epochs.append(epoch)
        epoch *= 2
    return tuple(epochs)


def _all_positive_differences(marks: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    )


@dataclass(frozen=True)
class HybridFamily:
    """One family activated at a certified or actual upper threshold."""

    epoch: int
    kind: str
    index: int
    threshold: Fraction
    demand: int
    pairs: tuple[tuple[int, int], ...]
    differences: tuple[int, ...]


def hybrid_families(points: Sequence[int]) -> tuple[HybridFamily, ...]:
    """Return cross families plus one internal-adjacent family per shell.

    The cross family at ``(m, k)`` is activated at the Wave 6 threshold
    ``tau_(m,k)`` and has demand ``k``.  For ``m >= 2``, the internal family
    consists of the ``m-1`` consecutive pairs wholly inside ``[m,2m)`` and
    is activated at its largest *actual* difference ``delta_m``.
    """
    marks = _validated_marks(points)
    differences = _all_positive_differences(marks)
    if len(differences) != len(set(differences)):
        raise ValueError("the hybrid ledger requires a Golomb ruler")

    families: list[HybridFamily] = []
    for epoch in dyadic_epochs(len(marks)):
        profile = dyadic_shell_profile(marks, old_count=epoch)
        for antidiagonal in range(1, epoch + 1):
            band = dyadic_antidiagonal_band(
                marks,
                old_count=epoch,
                antidiagonal=antidiagonal,
            )
            threshold = antidiagonal_threshold(profile, antidiagonal)
            if band.upper > threshold or any(
                difference > threshold for difference in band.differences
            ):
                raise AssertionError("a cross difference exceeds its activation")
            pairs = tuple(
                (
                    epoch - 1 - offset,
                    epoch - 1 + antidiagonal - offset,
                )
                for offset in range(antidiagonal)
            )
            families.append(
                HybridFamily(
                    epoch=epoch,
                    kind="cross",
                    index=antidiagonal,
                    threshold=threshold,
                    demand=antidiagonal,
                    pairs=pairs,
                    differences=band.differences,
                )
            )

        if epoch >= 2:
            pairs = tuple((left, left + 1) for left in range(epoch, 2 * epoch - 1))
            internal_differences = tuple(
                marks[right] - marks[left] for left, right in pairs
            )
            families.append(
                HybridFamily(
                    epoch=epoch,
                    kind="internal_adjacent",
                    index=1,
                    threshold=Fraction(max(internal_differences)),
                    demand=epoch - 1,
                    pairs=pairs,
                    differences=internal_differences,
                )
            )

    pairs = tuple(pair for family in families for pair in family.pairs)
    selected_differences = tuple(
        difference for family in families for difference in family.differences
    )
    if any(family.demand != len(family.pairs) for family in families):
        raise AssertionError("a hybrid family has the wrong pair demand")
    if any(family.demand != len(family.differences) for family in families):
        raise AssertionError("a hybrid family has the wrong difference demand")
    if len(pairs) != len(set(pairs)):
        raise AssertionError("hybrid families reuse an endpoint pair")
    if len(selected_differences) != len(set(selected_differences)):
        raise AssertionError("hybrid families reuse a positive difference")
    return tuple(families)


@dataclass(frozen=True)
class HybridThresholdRow:
    threshold: Fraction
    floor_threshold: int
    cumulative_demand: int
    margin: int
    activated_cross_demand: int
    activated_internal_demand: int


def hybrid_threshold_rows(points: Sequence[int]) -> tuple[HybridThresholdRow, ...]:
    """Audit the cumulative integer-capacity inequality at every jump."""
    families = sorted(
        hybrid_families(points),
        key=lambda family: (family.threshold, family.kind, family.epoch, family.index),
    )
    rows: list[HybridThresholdRow] = []
    cumulative = 0
    cross = 0
    internal = 0
    cursor = 0
    while cursor < len(families):
        threshold = families[cursor].threshold
        end = cursor
        while end < len(families) and families[end].threshold == threshold:
            family = families[end]
            if any(difference > threshold for difference in family.differences):
                raise AssertionError("an activated difference exceeds the threshold")
            cumulative += family.demand
            if family.kind == "cross":
                cross += family.demand
            else:
                internal += family.demand
            end += 1
        cutoff = floor(threshold)
        row = HybridThresholdRow(
            threshold=threshold,
            floor_threshold=cutoff,
            cumulative_demand=cumulative,
            margin=cutoff - cumulative,
            activated_cross_demand=cross,
            activated_internal_demand=internal,
        )
        if row.margin < 0:
            raise AssertionError("hybrid threshold ledger exceeds integer capacity")
        rows.append(row)
        cursor = end
    return tuple(rows)


def harmonic_number(count: int) -> Fraction:
    """Return ``H_count`` exactly."""
    if not isinstance(count, int) or count < 0:
        raise ValueError("count must be a nonnegative integer")
    return sum((Fraction(1, rank) for rank in range(1, count + 1)), Fraction(0))


@dataclass(frozen=True)
class HybridLedgerAudit:
    mark_count: int
    family_count: int
    pair_count: int
    cross_demand: int
    internal_adjacent_demand: int
    threshold_count: int
    minimum_capacity_margin: int
    reciprocal_activation_sum: Fraction
    harmonic_upper_bound: Fraction


def audit_hybrid_ledger(points: Sequence[int]) -> HybridLedgerAudit:
    """Return the exact finite certificate for the hybrid layer cake."""
    marks = _validated_marks(points)
    families = hybrid_families(marks)
    rows = hybrid_threshold_rows(marks)
    reciprocal_sum = sum(
        (Fraction(family.demand, 1) / family.threshold for family in families),
        Fraction(0),
    )
    pair_count = sum(family.demand for family in families)
    harmonic_bound = harmonic_number(pair_count)
    if reciprocal_sum > harmonic_bound:
        raise AssertionError("hybrid reciprocal sum exceeds its harmonic bound")
    return HybridLedgerAudit(
        mark_count=len(marks),
        family_count=len(families),
        pair_count=pair_count,
        cross_demand=sum(
            family.demand for family in families if family.kind == "cross"
        ),
        internal_adjacent_demand=sum(
            family.demand for family in families if family.kind == "internal_adjacent"
        ),
        threshold_count=len(rows),
        minimum_capacity_margin=min(row.margin for row in rows),
        reciprocal_activation_sum=reciprocal_sum,
        harmonic_upper_bound=harmonic_bound,
    )


@dataclass(frozen=True)
class RenewalDichotomy:
    epoch: int
    first_cross_threshold: Fraction
    old_certified_bound: Fraction
    new_certified_bound: Fraction
    old_internal_maximum: int
    new_internal_maximum: int
    old_certified_cheap: bool
    new_certified_cheap: bool
    ancestry_cleared: bool
    new_family_paid: bool
    earlier_internal_maxima: tuple[tuple[int, int], ...]
    earlier_boundary_gaps: tuple[tuple[int, int], ...]


def renewal_dichotomy(points: Sequence[int], *, old_count: int) -> RenewalDichotomy:
    """Certify the exact old-clear/new-pay alternative at one epoch.

    If ``tau=tau_(m,1)``, every old internal adjacent gap is at most
    ``mu^-+2D^-`` and every newborn internal adjacent gap is at most
    ``mu^++2D^+``.  At least one of these two certified bounds is at most
    ``tau``.  Consequently either all earlier adjacent families and dyadic
    boundary gaps are cleared at ``tau``, or the current newborn internal
    family is paid at ``tau`` (possibly both).
    """
    marks = _validated_marks(points)
    if (
        not isinstance(old_count, int)
        or old_count < 2
        or 2 * old_count > len(marks)
        or old_count & (old_count - 1)
    ):
        raise ValueError(
            "old_count must be a dyadic integer at least two with a full shell"
        )
    epoch = old_count
    profile = dyadic_shell_profile(marks, old_count=epoch)
    threshold = antidiagonal_threshold(profile, 1)
    old_bound = profile.old_mean + 2 * profile.old_discrepancy
    new_bound = profile.shell_mean + 2 * profile.shell_discrepancy
    old_gaps = tuple(marks[index] - marks[index - 1] for index in range(1, epoch))
    new_internal_gaps = tuple(
        marks[index] - marks[index - 1] for index in range(epoch + 1, 2 * epoch)
    )
    old_maximum = max(old_gaps)
    new_maximum = max(new_internal_gaps)
    if old_maximum > old_bound or new_maximum > new_bound:
        raise AssertionError("an adjacent gap exceeds its discrepancy bound")
    old_cheap = old_bound <= threshold
    new_cheap = new_bound <= threshold
    if not old_cheap and not new_cheap:
        raise AssertionError("the algebraic cheap-half dichotomy failed")

    earlier_epochs = tuple(epoch_ for epoch_ in dyadic_epochs(epoch) if epoch_ >= 2)
    earlier_internal = tuple(
        (
            earlier,
            max(
                marks[index] - marks[index - 1]
                for index in range(earlier + 1, 2 * earlier)
            ),
        )
        for earlier in earlier_epochs
    )
    earlier_boundaries = tuple(
        (earlier, marks[earlier] - marks[earlier - 1])
        for earlier in dyadic_epochs(epoch)
    )
    ancestry_cleared = old_maximum <= threshold
    new_paid = new_maximum <= threshold
    if not ancestry_cleared and not new_paid:
        raise AssertionError("neither side of the renewal dichotomy was paid")
    if ancestry_cleared and (
        any(value > threshold for _, value in earlier_internal)
        or any(value > threshold for _, value in earlier_boundaries)
    ):
        raise AssertionError("an ancestral adjacent debt survived old-half clearing")

    return RenewalDichotomy(
        epoch=epoch,
        first_cross_threshold=threshold,
        old_certified_bound=old_bound,
        new_certified_bound=new_bound,
        old_internal_maximum=old_maximum,
        new_internal_maximum=new_maximum,
        old_certified_cheap=old_cheap,
        new_certified_cheap=new_cheap,
        ancestry_cleared=ancestry_cleared,
        new_family_paid=new_paid,
        earlier_internal_maxima=earlier_internal,
        earlier_boundary_gaps=earlier_boundaries,
    )


@dataclass(frozen=True)
class InternalFamilyPayment:
    birth_epoch: int
    demand: int
    actual_threshold: int
    birth_cross_threshold: Fraction
    payment_epoch: int | None
    certifying_threshold: Fraction | None
    payment_kind: str


@dataclass(frozen=True)
class RenewalHistoryAudit:
    events: tuple[RenewalDichotomy, ...]
    payments: tuple[InternalFamilyPayment, ...]
    maximum_outstanding_families: int
    unresolved_epochs: tuple[int, ...]


def renewal_history(points: Sequence[int]) -> RenewalHistoryAudit:
    """Match every internal adjacent family to birth or later renewal.

    Process dyadic epochs in increasing order.  If the current newborn family
    is paid, match it to its own first-cross threshold.  Otherwise the renewal
    dichotomy clears every older debt before the current family becomes the
    sole outstanding debt.  Hence at most one family is outstanding at every
    finite time, and along an infinite history at most one family can remain
    unpaid forever.
    """
    marks = _validated_marks(points)
    events = tuple(
        renewal_dichotomy(marks, old_count=epoch)
        for epoch in dyadic_epochs(len(marks))
        if epoch >= 2
    )
    payments: list[InternalFamilyPayment] = []
    outstanding: int | None = None
    maximum_outstanding = 0

    for event in events:
        if event.ancestry_cleared and outstanding is not None:
            debt = payments[outstanding]
            if debt.actual_threshold > event.first_cross_threshold:
                raise AssertionError("a renewal threshold failed to clear its debt")
            payments[outstanding] = replace(
                debt,
                payment_epoch=event.epoch,
                certifying_threshold=event.first_cross_threshold,
                payment_kind="later_ancestry_clear",
            )
            outstanding = None

        current = InternalFamilyPayment(
            birth_epoch=event.epoch,
            demand=event.epoch - 1,
            actual_threshold=event.new_internal_maximum,
            birth_cross_threshold=event.first_cross_threshold,
            payment_epoch=event.epoch if event.new_family_paid else None,
            certifying_threshold=(
                event.first_cross_threshold if event.new_family_paid else None
            ),
            payment_kind="birth" if event.new_family_paid else "unresolved",
        )
        payments.append(current)
        if not event.new_family_paid:
            if not event.ancestry_cleared or outstanding is not None:
                raise AssertionError("renewal created a second outstanding family")
            outstanding = len(payments) - 1
        maximum_outstanding = max(
            maximum_outstanding,
            int(outstanding is not None),
        )

    unresolved = tuple(
        payment.birth_epoch for payment in payments if payment.payment_epoch is None
    )
    if len(unresolved) > 1:
        raise AssertionError("more than one internal family remained unresolved")
    return RenewalHistoryAudit(
        events=events,
        payments=tuple(payments),
        maximum_outstanding_families=maximum_outstanding,
        unresolved_epochs=unresolved,
    )


H_MATRIX = (
    (Fraction(16, 15), Fraction(8, 105)),
    (Fraction(8, 105), Fraction(4, 35)),
)
H_SECANT_MINIMUM = Fraction(16, 147)
H_SECANT_SUPREMUM = Fraction(36, 35)


def rank_embedding(position: Fraction | int) -> tuple[Fraction, Fraction]:
    """Return ``z(u)=(u(1-u),u)`` exactly."""
    u = Fraction(position)
    return (u * (1 - u), u)


def h_quadratic_difference(first: Fraction | int, second: Fraction | int) -> Fraction:
    """Return ``(z(u)-z(v))^T H (z(u)-z(v))`` exactly."""
    first_vector = rank_embedding(first)
    second_vector = rank_embedding(second)
    delta = (
        first_vector[0] - second_vector[0],
        first_vector[1] - second_vector[1],
    )
    return (
        H_MATRIX[0][0] * delta[0] ** 2
        + 2 * H_MATRIX[0][1] * delta[0] * delta[1]
        + H_MATRIX[1][1] * delta[1] ** 2
    )


def h_secant_coefficient(first: Fraction | int, second: Fraction | int) -> Fraction:
    """Return the coefficient of ``(u-v)^2`` in the shell H-distance."""
    u = Fraction(first)
    v = Fraction(second)
    x = 1 - u - v
    return Fraction(16, 15) * x * x + Fraction(16, 105) * x + Fraction(4, 35)


@dataclass(frozen=True)
class ShellCovarianceComparison:
    rank_variance: Fraction
    h_covariance: Fraction
    lower_bound: Fraction
    upper_bound: Fraction


def shell_covariance_comparison(
    positions: Sequence[Fraction | int],
    weights: Sequence[Fraction | int],
) -> ShellCovarianceComparison:
    """Compare ``<H,Cov(z)>`` with ``Var(U)`` on ``1/2 <= U <= 1``.

    The signed off-diagonal entry of ``H`` is retained.  The comparison is
    exact and follows from the pairwise identity

    ``(z(u)-z(v))^T H (z(u)-z(v)) = (u-v)^2 q(1-u-v)``,

    where ``16/147 <= q(x) <= 36/35`` for ``-1 <= x <= 0``.
    """
    locations = tuple(Fraction(position) for position in positions)
    masses = tuple(Fraction(weight) for weight in weights)
    if len(locations) < 2 or len(locations) != len(masses):
        raise ValueError("positions and weights must have the same length at least two")
    if any(position < Fraction(1, 2) or position > 1 for position in locations):
        raise ValueError("all shell positions must lie in [1/2,1]")
    if any(weight < 0 for weight in masses) or sum(masses) <= 0:
        raise ValueError("weights must be nonnegative with positive total mass")
    total = sum(masses)
    mean = (
        sum(
            (weight * position for weight, position in zip(masses, locations)),
            Fraction(0),
        )
        / total
    )
    rank_variance = (
        sum(
            (
                weight * (position - mean) ** 2
                for weight, position in zip(masses, locations)
            ),
            Fraction(0),
        )
        / total
    )
    h_covariance = sum(
        (
            masses[left]
            * masses[right]
            * h_quadratic_difference(locations[left], locations[right])
            for left in range(len(locations))
            for right in range(len(locations))
        ),
        Fraction(0),
    ) / (2 * total * total)
    lower = H_SECANT_MINIMUM * rank_variance
    upper = H_SECANT_SUPREMUM * rank_variance
    if not lower <= h_covariance <= upper:
        raise AssertionError("the shell H-covariance comparison failed")
    return ShellCovarianceComparison(
        rank_variance=rank_variance,
        h_covariance=h_covariance,
        lower_bound=lower,
        upper_bound=upper,
    )

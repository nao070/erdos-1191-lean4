from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import pytest

from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave7_band_renewal_probe import load_authenticated_wave6_fixtures
from wave8_actual_adjacent_renewal import (
    H_SECANT_MINIMUM,
    H_SECANT_SUPREMUM,
    audit_hybrid_ledger,
    h_quadratic_difference,
    h_secant_coefficient,
    hybrid_families,
    hybrid_threshold_rows,
    renewal_dichotomy,
    renewal_history,
    shell_covariance_comparison,
)

DIRECTORY = Path(__file__).resolve().parent
SOURCE_CERTIFICATE = DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
PERFECT_FOUR = (0, 1, 4, 6)
OLD_CLEAR_ONLY_EIGHT = (0, 76, 413, 471, 595, 1283, 1424, 1624)
NEW_PAY_ONLY_EIGHT = (0, 768, 1064, 1216, 1303, 1423, 1676, 1922)
DEBT_REPAID_SIXTEEN = (
    0,
    76,
    413,
    471,
    595,
    1283,
    1424,
    1624,
    1694,
    1925,
    2015,
    2016,
    2059,
    2188,
    2261,
    2333,
)


def test_perfect_four_hybrid_families_are_five_distinct_integer_atoms() -> None:
    families = hybrid_families(PERFECT_FOUR)
    assert tuple(
        (
            family.epoch,
            family.kind,
            family.index,
            family.threshold,
            family.demand,
            family.pairs,
            family.differences,
        )
        for family in families
    ) == (
        (1, "cross", 1, Fraction(1), 1, ((0, 1),), (1,)),
        (2, "cross", 1, Fraction(3), 1, ((1, 2),), (3,)),
        (2, "cross", 2, Fraction(11, 2), 2, ((1, 3), (0, 2)), (5, 4)),
        (2, "internal_adjacent", 1, Fraction(2), 1, ((2, 3),), (2,)),
    )

    rows = hybrid_threshold_rows(PERFECT_FOUR)
    assert tuple(
        (row.threshold, row.cumulative_demand, row.margin) for row in rows
    ) == (
        (Fraction(1), 1, 0),
        (Fraction(2), 2, 0),
        (Fraction(3), 3, 0),
        (Fraction(11, 2), 5, 0),
    )
    audit = audit_hybrid_ledger(PERFECT_FOUR)
    assert audit.pair_count == 5
    assert audit.cross_demand == 4
    assert audit.internal_adjacent_demand == 1
    assert audit.reciprocal_activation_sum == Fraction(145, 66)
    assert audit.harmonic_upper_bound == Fraction(137, 60)


def test_hybrid_ledger_is_exact_on_independent_sixty_four_mark_fixture() -> None:
    audit = audit_hybrid_ledger(COUNTEREXAMPLE_64_POINTS)
    assert audit.mark_count == 64
    assert audit.cross_demand == sum(
        epoch * (epoch + 1) // 2 for epoch in (1, 2, 4, 8, 16, 32)
    )
    assert audit.internal_adjacent_demand == sum(
        epoch - 1 for epoch in (2, 4, 8, 16, 32)
    )
    assert audit.pair_count == audit.cross_demand + audit.internal_adjacent_demand
    assert audit.minimum_capacity_margin >= 0
    assert audit.reciprocal_activation_sum <= audit.harmonic_upper_bound


def test_renewal_dichotomy_certifies_ancestry_when_new_bound_is_not_cheap() -> None:
    fixtures = load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)
    points = fixtures.one_hundred_twenty_eight_mark_points
    row = renewal_dichotomy(points, old_count=64)
    assert row.old_certified_cheap
    assert not row.new_certified_cheap
    assert row.ancestry_cleared
    # The actual 128-mark fixture happens to pay both sides even though the
    # discrepancy certificate guarantees only the old side.
    assert row.new_family_paid
    assert all(
        value <= row.first_cross_threshold
        for _, value in (*row.earlier_internal_maxima, *row.earlier_boundary_gaps)
    )


def test_renewal_alternative_is_not_secretly_always_new_family_payment() -> None:
    row = renewal_dichotomy(OLD_CLEAR_ONLY_EIGHT, old_count=4)
    assert row.first_cross_threshold == Fraction(2731, 4)
    assert row.old_internal_maximum == 337
    assert row.new_internal_maximum == 688
    assert row.ancestry_cleared
    assert not row.new_family_paid
    assert row.earlier_internal_maxima == ((2, 58),)
    assert row.earlier_boundary_gaps == ((1, 76), (2, 337))


def test_renewal_alternative_is_not_secretly_always_ancestry_clearing() -> None:
    row = renewal_dichotomy(NEW_PAY_ONLY_EIGHT, old_count=4)
    assert row.first_cross_threshold == Fraction(1507, 2)
    assert row.old_internal_maximum == 768
    assert row.new_internal_maximum == 253
    assert not row.ancestry_cleared
    assert row.new_family_paid


def test_history_keeps_at_most_one_debt_and_later_clears_it() -> None:
    terminal_debt = renewal_history(OLD_CLEAR_ONLY_EIGHT)
    assert terminal_debt.maximum_outstanding_families == 1
    assert terminal_debt.unresolved_epochs == (4,)

    repaid = renewal_history(DEBT_REPAID_SIXTEEN)
    assert repaid.maximum_outstanding_families == 1
    assert repaid.unresolved_epochs == ()
    payment = next(row for row in repaid.payments if row.birth_epoch == 4)
    assert payment.actual_threshold == 688
    assert payment.payment_epoch == 8
    assert payment.certifying_threshold == Fraction(5983, 8)
    assert payment.payment_kind == "later_ancestry_clear"


def test_every_complete_nontrivial_epoch_satisfies_renewal_alternative() -> None:
    fixtures = load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)
    points = fixtures.one_hundred_twenty_eight_mark_points
    rows = tuple(
        renewal_dichotomy(points, old_count=epoch) for epoch in (2, 4, 8, 16, 32, 64)
    )
    assert all(row.ancestry_cleared or row.new_family_paid for row in rows)
    assert all(row.old_certified_cheap or row.new_certified_cheap for row in rows)


def test_shell_h_secant_identity_and_sharp_lower_constant_are_exact() -> None:
    samples = (
        (Fraction(1, 2), Fraction(4, 7)),
        (Fraction(1, 2), Fraction(3, 4)),
        (Fraction(5, 8), Fraction(7, 8)),
        (Fraction(9, 10), Fraction(1)),
    )
    for first, second in samples:
        coefficient = h_secant_coefficient(first, second)
        assert h_quadratic_difference(first, second) == (
            (first - second) ** 2 * coefficient
        )
        assert H_SECANT_MINIMUM <= coefficient <= H_SECANT_SUPREMUM

    assert h_secant_coefficient(Fraction(1, 2), Fraction(4, 7)) == (H_SECANT_MINIMUM)


def test_shell_covariance_retains_signed_off_diagonal_without_cancellation() -> None:
    comparison = shell_covariance_comparison(
        (Fraction(1, 2), Fraction(4, 7)),
        (3, 11),
    )
    assert comparison.rank_variance > 0
    assert comparison.h_covariance == comparison.lower_bound
    assert comparison.upper_bound == H_SECANT_SUPREMUM * comparison.rank_variance

    mixed = shell_covariance_comparison(
        (Fraction(1, 2), Fraction(5, 8), Fraction(3, 4), Fraction(1)),
        (1, 3, 5, 7),
    )
    assert mixed.lower_bound <= mixed.h_covariance <= mixed.upper_bound


def test_invalid_rulers_and_shell_measures_are_rejected() -> None:
    with pytest.raises(ValueError, match="Golomb"):
        hybrid_families((0, 1, 2, 3))
    with pytest.raises(ValueError, match="dyadic"):
        renewal_dichotomy(PERFECT_FOUR, old_count=3)
    with pytest.raises(ValueError, match=r"\[1/2,1\]"):
        shell_covariance_comparison((Fraction(1, 3), Fraction(2, 3)), (1, 1))
    with pytest.raises(ValueError, match="nonnegative"):
        shell_covariance_comparison((Fraction(1, 2), Fraction(3, 4)), (1, -1))

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import pytest
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave7_band_renewal_probe import load_authenticated_wave6_fixtures
from wave9_rank_variance_reduction import (
    Q_MAX,
    Q_MIN,
    audit_rank_variance_reduction,
    distinct_gap_rank_variance_lower_bound,
    scalar_birth_step,
    weighted_rank_variance,
)

DIRECTORY = Path(__file__).resolve().parent
SOURCE_CERTIFICATE = DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
PERFECT_FOUR = (0, 1, 4, 6)


def test_weighted_rank_variance_is_exact_on_perfect_four_prefixes() -> None:
    assert weighted_rank_variance(PERFECT_FOUR, count=1) == 0
    assert weighted_rank_variance(PERFECT_FOUR, count=2) == Fraction(1, 16)
    assert weighted_rank_variance(PERFECT_FOUR, count=4) == Fraction(3, 49)


def test_one_step_scalar_birth_is_exactly_a_rank_variance_increment() -> None:
    first = scalar_birth_step(PERFECT_FOUR, old_count=1)
    second = scalar_birth_step(PERFECT_FOUR, old_count=2)
    assert first.direct_scalar_birth == Fraction(1, 16)
    assert second.direct_scalar_birth == Fraction(47, 784)
    assert second.telescoped_scalar_birth == second.direct_scalar_birth
    assert second.modulus_ratio == Fraction(2, 7)
    assert Q_MIN <= first.q_ratio <= Q_MAX
    assert Q_MIN <= second.q_ratio <= Q_MAX


def test_global_reduction_has_exact_perfect_four_values() -> None:
    audit = audit_rank_variance_reduction(PERFECT_FOUR)
    assert audit.state_counts == (1, 2, 4)
    assert audit.update_count == 2
    assert audit.variance_sum == Fraction(97, 784)
    assert audit.scalar_birth_sum == Fraction(6, 49)
    assert audit.fixed_h_birth_sum == Fraction(1199, 27440)
    assert Fraction(3, 4) * audit.variance_sum <= audit.scalar_birth_sum
    assert audit.scalar_birth_sum <= audit.variance_sum
    assert audit.universal_h_lower_bound <= audit.fixed_h_birth_sum
    assert audit.fixed_h_birth_sum <= audit.universal_h_upper_bound


def test_global_reduction_on_authenticated_64_and_128_mark_fixtures() -> None:
    fixtures = load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)
    rows = (
        audit_rank_variance_reduction(COUNTEREXAMPLE_64_POINTS),
        audit_rank_variance_reduction(fixtures.one_hundred_twenty_eight_mark_points),
    )
    assert tuple(row.mark_count for row in rows) == (64, 128)
    for row in rows:
        assert row.scalar_birth_sum == row.telescoped_scalar_sum
        assert Fraction(3, 4) <= row.scalar_to_variance_ratio <= 1
        assert Fraction(4, 49) <= row.h_to_variance_ratio <= Fraction(36, 35)


def test_distinct_gap_lower_bound_on_authenticated_fixtures() -> None:
    fixtures = load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)
    rows = (
        distinct_gap_rank_variance_lower_bound(
            COUNTEREXAMPLE_64_POINTS,
            count=64,
        ),
        distinct_gap_rank_variance_lower_bound(
            fixtures.one_hundred_twenty_eight_mark_points,
            count=128,
        ),
    )
    for row in rows:
        assert row.actual_rank_variance >= row.universal_lower_bound


def test_distinct_gap_lower_bound_rejects_duplicate_real_gaps() -> None:
    with pytest.raises(ValueError):
        distinct_gap_rank_variance_lower_bound(
            (0, 1, 2, 4, 7, 11, 16, 22),
            count=8,
        )


def test_reduction_is_algebraic_and_does_not_require_golomb_uniqueness() -> None:
    non_golomb = (0, 1, 2, 3, 7, 8, 9, 10)
    audit = audit_rank_variance_reduction(non_golomb)
    assert audit.mark_count == 8
    assert audit.scalar_birth_sum == audit.telescoped_scalar_sum


def test_invalid_inputs_are_rejected() -> None:
    with pytest.raises(ValueError):
        weighted_rank_variance((1, 2), count=2)
    with pytest.raises(ValueError):
        scalar_birth_step(PERFECT_FOUR, old_count=3)
    with pytest.raises(ValueError):
        audit_rank_variance_reduction((0, 1, 4))

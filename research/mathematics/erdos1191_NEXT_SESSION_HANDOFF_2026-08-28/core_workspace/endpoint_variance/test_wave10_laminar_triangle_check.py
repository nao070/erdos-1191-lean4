from fractions import Fraction

import pytest

from wave10_laminar_triangle_check import (
    audit_scale,
    bulk_weights,
    coefficient_partition,
    entropy_rank_upper,
    expected_bulk_weights,
    rearrangement_floor,
)


@pytest.mark.parametrize("m", [4, 8, 16, 32, 64])
def test_shell_support_signs_and_exact_masses(m: int) -> None:
    partition = coefficient_partition(m)
    theta = Fraction((m - 1) ** 2, m * m)
    assert all(value > 0 for value in partition["left_positive"].values())
    assert all(value > 0 for value in partition["suffix_positive"].values())
    assert all(value < 0 for value in partition["full_negative"].values())
    assert all(value < 0 for value in partition["bulk_negative"].values())
    assert sum(partition["left_positive"].values()) == theta
    assert sum(partition["suffix_positive"].values()) == theta
    assert -sum(partition["full_negative"].values()) == theta
    assert -sum(partition["bulk_negative"].values()) == theta


@pytest.mark.parametrize("m", [4, 8, 16, 32, 64])
def test_closed_bulk_multiset_matches_direct_indicator_formula(m: int) -> None:
    from collections import Counter

    assert Counter(bulk_weights(m)) == expected_bulk_weights(m)


def test_global_rearrangement_dominates_separate_epoch_floors() -> None:
    scales = (4, 8, 16, 32, 64)
    assert rearrangement_floor(scales) >= sum(rearrangement_floor((m,)) for m in scales)


def test_entropy_rank_bound_dominates_global_floor() -> None:
    scales = (4, 8, 16, 32, 64, 128)
    assert rearrangement_floor(scales) <= entropy_rank_upper(scales)


def test_audit_record_is_internally_consistent() -> None:
    record = audit_scale(32)
    assert record["positive_mass"] == str(2 * Fraction(31**2, 32**2))
    assert record["full_negative_mass"] == record["expected_theta"]
    assert record["bulk_negative_mass"] == record["expected_theta"]

from __future__ import annotations

from collections import Counter
from math import isclose

import pytest

from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave10_log_product_packing import (
    birth_shell_abel_sum,
    birth_shell_cross_ratio_sum,
    bulk_actual_log_mass,
    closed_birth_shell_coefficients,
    coefficient_sign_mass,
    dyadic_bulk_values_and_weights,
    exact_weighted_rearrangement_products,
    formal_birth_shell_coefficients,
    hereditary_bulk_log_floor,
    hereditary_log_product_check,
    negative_bulk_coefficients,
    negative_bulk_profile,
    relaxed_critical_shell_envelope,
    single_shell_rearrangement_floor,
)


@pytest.mark.parametrize("count", [8, 16, 32, 64])
def test_closed_shell_coefficients_match_four_origin_formula(count: int) -> None:
    formal = formal_birth_shell_coefficients(count)
    closed = closed_birth_shell_coefficients(count)
    assert closed == formal
    positive, negative = coefficient_sign_mass(closed)
    assert positive == negative == 2 * (count - 2) ** 2
    assert sum(negative_bulk_coefficients(count).values()) == (count - 2) ** 2


@pytest.mark.parametrize("m", [4, 8, 16, 32])
def test_negative_bulk_coefficient_profile(m: int) -> None:
    profile = negative_bulk_profile(m)
    observed = Counter(negative_bulk_coefficients(2 * m).values())
    expected = Counter({4: profile["weight_four_count"]})
    expected[2] += profile["weight_two_count"]
    expected[1] += profile["weight_one_count"]
    for length in range(2, m - 1):
        expected[2 * length + 1] += 1
    assert observed == expected
    assert sum(observed.values()) == profile["interval_count"]
    assert (
        sum(weight * count for weight, count in observed.items())
        == profile["scaled_mass"]
    )


def test_direct_cross_ratio_shell_equals_abel_expansion() -> None:
    points = COUNTEREXAMPLE_64_POINTS
    for m in (4, 8, 16, 32):
        direct = birth_shell_cross_ratio_sum(points, m)
        expanded = birth_shell_abel_sum(points, m)
        assert isclose(direct, expanded, rel_tol=1e-12, abs_tol=1e-12)


def test_hereditary_rank_lag_product_floor_is_exact_integer_check() -> None:
    points = COUNTEREXAMPLE_64_POINTS[:32]
    selected_product, factorial_floor = hereditary_log_product_check(
        points, {1: 1, 2: 2, 4: 3, 8: 4, 16: 5}
    )
    assert selected_product >= factorial_floor
    assert factorial_floor > 1


def test_global_dyadic_bulk_weighted_rearrangement_floor() -> None:
    points = COUNTEREXAMPLE_64_POINTS[:32]
    values, weights = dyadic_bulk_values_and_weights(points, (4, 8, 16))
    assert len(values) == len(set(values))
    lhs, rhs, denominator = exact_weighted_rearrangement_products(values, weights)
    assert denominator == 32 * 32
    assert lhs >= rhs
    assert (
        hereditary_bulk_log_floor(points, (4, 8, 16))
        <= bulk_actual_log_mass(points, (4, 8, 16)) + 1e-12
    )


def test_non_golomb_input_is_rejected() -> None:
    with pytest.raises(ValueError, match="Golomb"):
        hereditary_log_product_check((0, 1, 2, 3, 4, 5, 6, 7), {4: 2})


def test_relaxation_calibration_is_reproducible() -> None:
    floors = [single_shell_rearrangement_floor(m) for m in (8, 16, 32, 64)]
    envelopes = [relaxed_critical_shell_envelope(m) for m in (8, 16, 32, 64)]
    assert floors == sorted(floors)
    assert envelopes == sorted(envelopes)
    assert floors[-1] == pytest.approx(6.2598533589899565)
    assert envelopes[-1] == pytest.approx(4.8031422299095965)

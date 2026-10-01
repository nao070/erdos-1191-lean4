from __future__ import annotations

from math import log

import pytest
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave9_cross_ratio_telescope import (
    audit_cross_ratio_telescope,
    closed_cross_ratio_coefficients,
    coefficient_sign_mass,
    cross_ratio_argument,
    exact_pair_lower_ratio,
    formal_cross_ratio_coefficients,
    genuine_nonadjacent_scalar_energy,
    golomb_distinctness_cross_ratio_bound,
    weighted_cross_ratio_boundary_bound,
    weighted_cross_ratio_sum,
)

PERFECT_FOUR = (0, 1, 4, 6)


def test_formal_coefficients_equal_the_closed_formula() -> None:
    for count in range(4, 65):
        formal = formal_cross_ratio_coefficients(count)
        closed = closed_cross_ratio_coefficients(count)
        assert formal == closed
        positive, negative = coefficient_sign_mass(closed)
        assert positive == negative == 2 * (count - 2) ** 2


def test_cross_ratio_pair_inequality_is_exactly_oriented() -> None:
    argument = cross_ratio_argument(PERFECT_FOUR, left_gap=1, right_gap=3)
    lower = exact_pair_lower_ratio(PERFECT_FOUR, left_gap=1, right_gap=3)
    assert argument > 1
    assert float(lower) <= log(float(argument))


def test_perfect_four_telescope_and_boundary_bound() -> None:
    direct = weighted_cross_ratio_sum(PERFECT_FOUR)
    assert direct == pytest.approx(log(10 / 9) / 4)
    assert direct <= weighted_cross_ratio_boundary_bound(PERFECT_FOUR)
    assert float(genuine_nonadjacent_scalar_energy(PERFECT_FOUR)) <= direct


def test_full_audit_on_irregular_and_authenticated_rulers() -> None:
    non_golomb = (0, 2, 7, 15, 26, 40, 57, 77)
    for points in (non_golomb, COUNTEREXAMPLE_64_POINTS):
        audit = audit_cross_ratio_telescope(points)
        assert audit["scalar_energy"] <= audit["weighted_cross_ratio_sum"]
        assert audit["weighted_cross_ratio_sum"] <= audit["boundary_upper_bound"]
    authenticated = audit_cross_ratio_telescope(COUNTEREXAMPLE_64_POINTS)
    assert authenticated["golomb_distinctness_upper_bound"] is not None
    assert (
        authenticated["weighted_cross_ratio_sum"]
        <= authenticated["golomb_distinctness_upper_bound"]
        <= authenticated["boundary_upper_bound"]
    )


def test_golomb_distinctness_bound_rejects_a_repeated_difference() -> None:
    with pytest.raises(ValueError):
        golomb_distinctness_cross_ratio_bound((0, 1, 2, 4))


def test_cross_ratio_and_primitive_distinctness_bound_are_scale_invariant() -> None:
    scaled = tuple(17 * point for point in PERFECT_FOUR)
    assert weighted_cross_ratio_sum(scaled) == pytest.approx(
        weighted_cross_ratio_sum(PERFECT_FOUR)
    )
    assert golomb_distinctness_cross_ratio_bound(scaled) == pytest.approx(
        golomb_distinctness_cross_ratio_bound(PERFECT_FOUR)
    )


def test_invalid_inputs_and_adjacent_pairs_are_rejected() -> None:
    with pytest.raises(ValueError):
        formal_cross_ratio_coefficients(3)
    with pytest.raises(ValueError):
        weighted_cross_ratio_sum((1, 2, 4, 8))
    with pytest.raises(ValueError):
        cross_ratio_argument(PERFECT_FOUR, left_gap=1, right_gap=2)

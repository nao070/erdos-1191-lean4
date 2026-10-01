"""Tests for the Wave 19 P28 adaptive-row-cap boundary certificate."""

from __future__ import annotations

from fractions import Fraction

import pytest
import wave19_p28_adaptive_row_cap_certificate as certificate


def test_input_validation_and_hash_replay() -> None:
    with pytest.raises(ValueError):
        certificate.closed_residual_mass(3)
    with pytest.raises(TypeError):
        certificate.closed_residual_mass(True)
    with pytest.raises(ValueError):
        certificate.beta_coefficient(4, 2, 3)
    with pytest.raises(ValueError):
        certificate.log_interval(Fraction(1, 2))

    first = certificate.build_certificate()
    second = certificate.build_certificate()
    assert first == second
    assert certificate.render_certificate(first) == certificate.render_certificate(
        second
    )
    assert certificate.verify_certificate_hash(first)
    assert first["certificate_sha256"] == second["certificate_sha256"]


def test_full_row_residual_mass_and_capacity_formulas() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        direct_mass = Fraction()
        for source in range(2, 2 * epoch - 1):
            assert certificate.row_mass(epoch, source) == certificate.closed_row_mass(
                epoch, source
            )
            residual = certificate.residual_coefficient(epoch, source)
            assert 0 < residual <= certificate.row_mass(epoch, source)
            direct_mass += residual
        assert direct_mass == certificate.closed_residual_mass(epoch)
        assert direct_mass == Fraction(4 * epoch**2 - 12 * epoch + 11, 8 * epoch**2)
        assert direct_mass < Fraction(1, 2)


def test_adaptive_cap_profiles_and_actual_cap_is_only_bounded() -> None:
    for epoch in certificate.CAP_PROFILE_EPOCHS:
        audit = certificate.cap_profile_decimal(epoch)
        assert audit["mass_formula_verified"]
        assert audit["finite_profile_below_requested_bound"]

        # Pi_p=0 is an admissible abstract promotion profile.  Its actual
        # capped sum is zero, whereas every deterministic row height is
        # positive.  Thus the relationship is <=, not equality.
        actual_zero_profile = sum(
            (
                certificate.residual_coefficient(epoch, source)
                * min(Fraction(), certificate.H0)
                for source in range(2, 2 * epoch - 1)
            ),
            Fraction(),
        )
        assert actual_zero_profile == 0
        assert certificate.closed_residual_mass(epoch) * certificate.H0 > 0


def test_rational_log_and_exponential_cap_bounds() -> None:
    log2_lower, log2_upper = certificate.log_interval(Fraction(2))
    log3_lower, log3_upper = certificate.log_interval(Fraction(3))
    assert log2_lower < log2_upper
    assert log3_lower < log3_upper
    assert Fraction(69, 100) < log2_lower < log2_upper < Fraction(70, 100)
    assert Fraction(109, 100) < log3_lower < log3_upper < Fraction(110, 100)

    exp_lower = certificate.exp_lower(certificate.H0)
    cap_limit_upper = Fraction(3, 4) + Fraction(3, 8) / exp_lower
    assert cap_limit_upper < certificate.CAP_LIMIT_DECIMAL_UPPER
    assert Fraction(1, 4) < certificate.CAP_ERROR_DECIMAL_UPPER


def test_wave17_surplus_pays_preceding_adaptive_cap_from_2048() -> None:
    audit = certificate.cap_surplus_comparison_audit()
    assert audit["cap_limit_below_0_8336738101"]
    assert audit["elementary_error_implies_requested_error"]
    assert audit["onset_comparison_strict"]
    assert Fraction(*map(int, audit["onset_margin"].split("/"))) > 0


def test_natural_sbar_is_coefficientwise_below_half_Y() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        audit = certificate.sbar_epoch_audit(epoch)
        assert audit["row_mass_formulas_verified"]
        assert audit["residual_mass_formula_verified"]
        assert audit["all_coefficients_at_most_half_Y"]
        assert audit["all_coefficients_strictly_below_half_Y"]
        assert audit["endpoint_profile"]["every_column_strictly_below_three_quarters"]
        assert audit["endpoint_profile"]["worst_is_midpoint_column"]
        assert audit["all_exact_checks_pass"]


def test_long_short_proof_case_formulas_are_exact_and_positive() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        coefficients = certificate.coefficient_map(epoch)
        long_coefficients = certificate.partial_coefficient_map(epoch, 2, epoch)
        for x_value in range(1, epoch):
            for y_value in range(1, epoch):
                cell = (epoch - x_value, epoch + y_value)
                full = coefficients[cell]
                long_part = long_coefficients[cell]
                short_part = full - long_part
                assert full == long_part + short_part

                if (x_value, y_value) == (1, 1):
                    half_y = Fraction((x_value + y_value) ** 2, 8 * epoch**2)
                    assert half_y - full == Fraction(1, epoch**2 * (2 * epoch - 1))
                    continue

                direct_gap = (
                    Fraction(x_value**2 + 2 * x_value * y_value, 8 * epoch**2)
                    - long_part
                )
                assert direct_gap == certificate.closed_long_gap(
                    epoch, x_value, y_value
                )
                assert direct_gap > 0

                if x_value >= 3 and y_value >= 2:
                    slope = (
                        -4 * epoch * (epoch - 2) * x_value * (x_value - 2)
                        - 3 * x_value * (x_value - 2)
                        - 8 * (epoch - 1)
                    )
                    assert slope < 0
                    assert certificate.generic_long_gap_numerator(
                        epoch, x_value, epoch - 1
                    ) == certificate.generic_long_gap_at_last_y(epoch, x_value)
                    assert certificate.generic_long_gap_numerator(
                        epoch, x_value, y_value
                    ) >= certificate.generic_long_gap_at_last_y(epoch, x_value)

                if x_value >= 3 and y_value == 1:
                    denominator = (
                        8 * epoch**2 * (epoch - 1) * (2 * epoch - 3) * (2 * epoch - 1)
                    )
                    numerator = direct_gap * denominator
                    assert numerator.denominator == 1
                    assert numerator.numerator == certificate.y_one_manifest_numerator(
                        x_value - 3, epoch - x_value - 1
                    )


def test_asymptotically_sharp_terminal_cell_formula() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        coefficients = certificate.coefficient_map(epoch)
        cell = (1, 2 * epoch - 1)
        coefficient = coefficients[cell]
        y_value = certificate.y_coefficient(epoch, *cell)
        assert coefficient == certificate.closed_residual_mass(epoch)
        assert coefficient / y_value == Fraction(
            4 * epoch**2 - 12 * epoch + 11, 8 * (epoch - 1) ** 2
        )
        assert y_value / 2 - coefficient == Fraction(4 * epoch - 7, 8 * epoch**2)
    assert Fraction(4 * 10_000**2 - 12 * 10_000 + 11, 8 * (10_000 - 1) ** 2) > Fraction(
        4999, 10_000
    )


def test_old_c_based_adaptive_split_retains_endpoint() -> None:
    grid = tuple(Fraction(value, 2) for value in range(7))
    for endpoint in grid:
        for cross in grid:
            for tau in grid:
                atom, endpoint_part, cross_bound = certificate.old_c_based_atomic_split(
                    endpoint, cross, tau
                )
                assert endpoint_part <= atom <= endpoint_part + cross_bound

    atom, endpoint_part, cross_bound = certificate.old_c_based_atomic_split(
        Fraction(1), Fraction(), Fraction()
    )
    assert atom == endpoint_part == 1
    assert cross_bound == 0


def test_actual_rank_split_requires_endpoint_term() -> None:
    audit = certificate.atomic_split_audit()
    assert audit["counterexample_invalidates_endpoint_free_atomic_claim"]
    assert audit["endpoint_free_grid_failures"] > 0

    atom, correct, endpoint_free = certificate.actual_rank_atomic_split(
        Fraction(), Fraction(), Fraction(1), Fraction()
    )
    assert atom == correct == 1
    assert endpoint_free == 0


def test_uniform_inner_transport_above_one_third_is_impossible() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        audit = certificate.transport_obstruction(epoch)
        assert audit["ratio_is_one_third"]
        assert audit["uniform_fraction_strictly_above_one_third_impossible"]
        assert not audit["attainment_of_one_third_claimed"]
        assert certificate.residual_coefficient(
            epoch, 2 * epoch - 3
        ) + certificate.residual_coefficient(epoch, 2 * epoch - 2) == Fraction(
            3, 4 * epoch**2
        )

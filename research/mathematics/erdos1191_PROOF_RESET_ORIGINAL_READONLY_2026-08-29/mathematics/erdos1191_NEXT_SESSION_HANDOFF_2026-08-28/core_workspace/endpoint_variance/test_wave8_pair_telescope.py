from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import pytest

from gap_measure_dynamics import is_positive_semidefinite
from innovation_budget import (
    E_MATRIX,
    LYAPUNOV_MATRIX,
    adjoint_transport,
    adjoint_weights,
    matrix_add,
    matrix_scale,
    matrix_subtract,
)
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave7_band_renewal_probe import load_authenticated_wave6_fixtures
from wave8_pair_telescope import (
    audit_pair_telescope,
    constant_h_modulus_audit,
    constant_ratio_fixed_limit_kernel,
    discounted_lyapunov_matrix,
    exact_adjoint_pair_audit,
    finite_horizon_adjoint_weights,
    fixed_h_pair_audit,
    pair_birth_epoch,
)

DIRECTORY = Path(__file__).resolve().parent
SOURCE_CERTIFICATE = DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
PERFECT_FOUR = (0, 1, 4, 6)


def test_arbitrary_modulus_weights_have_exact_half_and_ratio_bounds() -> None:
    audit = constant_h_modulus_audit((7, 11, 20, 83))
    assert audit.birth_weight == Fraction(1, 49)
    assert audit.old_subtraction_weights == (
        Fraction(4, 847),
        Fraction(9, 4400),
        Fraction(63, 137780),
    )
    assert audit.positive_atom_weights == (
        Fraction(1, 49),
        Fraction(93, 5929),
        Fraction(32349, 2371600),
        Fraction(215381721, 16337952400),
    )
    assert audit.half_birth_lower_bound == Fraction(1, 98)
    assert audit.maximum_future_ratio == Fraction(7, 11)
    assert audit.ratio_lower_bound == Fraction(11, 882)
    assert min(audit.positive_atom_weights) >= audit.ratio_lower_bound


def test_closed_horizon_adjoint_is_canonical_adjoint_with_one_extra_zero() -> None:
    moduli = (7, 11, 20, 83)
    closed = finite_horizon_adjoint_weights(moduli)
    canonical = adjoint_weights((*moduli, moduli[-1]))
    assert closed == canonical[:-1]
    assert closed[-1] == E_MATRIX
    for index in range(len(moduli) - 1):
        rho = Fraction(moduli[index], moduli[index + 1])
        assert closed[index] == matrix_add(
            E_MATRIX,
            matrix_scale(rho, adjoint_transport(closed[index + 1])),
        )


def test_constant_h_pair_keeps_more_than_half_its_birth_charge() -> None:
    audit = fixed_h_pair_audit(PERFECT_FOUR, 0, 1)
    assert audit.birth_epoch == 1
    assert audit.state_counts == (2, 4)
    assert audit.moduli == (2, 7)
    assert audit.birth_kernel_coefficient == Fraction(1, 35)
    assert audit.later_negative_coefficient == Fraction(29, 10976)
    assert audit.net_kernel_coefficient == Fraction(1423, 54880)
    assert audit.retention_ratio == Fraction(1423, 1568)
    assert audit.telescope_weights == (Fraction(1, 4), Fraction(39, 196))
    assert audit.lyapunov_telescope_value == audit.net_kernel_coefficient


def test_exact_adjoint_pair_telescope_reconstructs_positive_state_tail() -> None:
    audit = exact_adjoint_pair_audit(PERFECT_FOUR, 0, 1)
    assert audit.state_counts == (1, 2, 4)
    assert audit.moduli == (1, 2, 7)
    assert audit.signed_innovation_coefficient == Fraction(205, 12544)
    assert audit.positive_state_tail_coefficient == Fraction(205, 12544)
    assert audit.birth_e_lower_bound == Fraction(1, 64)
    assert audit.fixed_h_birth_upper_bound == Fraction(1, 35)


def test_all_pair_regroupings_are_exact_on_perfect_four() -> None:
    audit = audit_pair_telescope(PERFECT_FOUR)
    assert audit.fixed_h_local_sum == Fraction(2253, 54880)
    assert audit.fixed_h_pair_sum == audit.fixed_h_local_sum
    assert audit.raw_birth_sum == Fraction(1199, 27440)
    assert audit.half_raw_birth_lower_bound == Fraction(1199, 54880)
    assert audit.minimum_pair_retention == Fraction(1423, 1568)
    assert audit.exact_adjoint_innovation_sum == Fraction(5, 224)
    assert audit.exact_positive_pair_tail_sum == audit.exact_adjoint_innovation_sum
    assert audit.state_functional_sum == audit.exact_adjoint_innovation_sum


def test_global_telescopes_hold_on_independent_64_and_authenticated_128() -> None:
    fixtures = load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)
    rows = (
        audit_pair_telescope(COUNTEREXAMPLE_64_POINTS),
        audit_pair_telescope(fixtures.one_hundred_twenty_eight_mark_points),
    )
    assert tuple(row.pair_count for row in rows) == (2016, 8128)
    assert tuple(row.minimum_pair_retention for row in rows) == (
        Fraction(286851781, 355511025),
        Fraction(15576406729, 18573056089),
    )
    for row in rows:
        assert row.fixed_h_local_sum == row.fixed_h_pair_sum
        assert row.half_raw_birth_lower_bound <= row.fixed_h_local_sum
        assert row.fixed_h_local_sum <= row.raw_birth_sum
        assert row.exact_adjoint_innovation_sum == row.exact_positive_pair_tail_sum
        assert row.exact_adjoint_innovation_sum == row.state_functional_sum


def test_discounted_and_constant_ratio_critical_kernels_are_exact() -> None:
    quarter = discounted_lyapunov_matrix(Fraction(1, 4))
    sixteenth = discounted_lyapunov_matrix(Fraction(1, 16))
    assert discounted_lyapunov_matrix(1) == LYAPUNOV_MATRIX
    assert quarter == (
        (Fraction(64, 63), Fraction(32, 1953)),
        (Fraction(32, 1953), Fraction(176, 9765)),
    )
    assert sixteenth == (
        (Fraction(256, 255), Fraction(128, 32385)),
        (Fraction(128, 32385), Fraction(2752, 680085)),
    )

    critical = constant_ratio_fixed_limit_kernel(Fraction(1, 4))
    assert critical == (
        (Fraction(448, 425), Fraction(23328, 377825)),
        (Fraction(23328, 377825), Fraction(313648, 3400425)),
    )
    assert is_positive_semidefinite(
        matrix_subtract(critical, matrix_scale(Fraction(4, 5), LYAPUNOV_MATRIX))
    )
    assert is_positive_semidefinite(matrix_subtract(LYAPUNOV_MATRIX, critical))


def test_invalid_boundaries_and_parameters_are_rejected() -> None:
    with pytest.raises(ValueError):
        pair_birth_epoch(0)
    with pytest.raises(ValueError):
        constant_h_modulus_audit((7, 11, 11))
    with pytest.raises(ValueError):
        finite_horizon_adjoint_weights((7,))
    with pytest.raises(ValueError):
        exact_adjoint_pair_audit(PERFECT_FOUR, 0, 3, horizon_count=2)
    with pytest.raises(ValueError):
        discounted_lyapunov_matrix(Fraction(5, 4))

"""Tests for the Wave 19 mixed right-greedy transport certificate."""

from __future__ import annotations

from fractions import Fraction
from importlib import import_module

import pytest

certificate = import_module("wave19_p28_mixed_transport_certificate")


def test_validation_and_deterministic_hash_replay() -> None:
    with pytest.raises(ValueError):
        certificate.residual_coefficient(3, 2)
    with pytest.raises(TypeError):
        certificate.beta_coefficient(True, 2, 4)
    with pytest.raises(ValueError):
        certificate.beta_coefficient(4, 2, 3)

    first = certificate.build_certificate()
    second = certificate.build_certificate()
    assert first == second
    assert certificate.render_certificate(first) == certificate.render_certificate(
        second
    )
    assert certificate.verify_certificate_hash(first)


def test_three_transports_have_exact_rows_and_caps() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        natural = certificate.natural_transport(epoch)
        right = certificate.right_greedy_transport(epoch)
        mixed = certificate.mixed_transport(epoch)
        for transport in (natural, right, mixed):
            audit = certificate.transport_audit(epoch, transport)
            assert audit["all_rows_exact"]
            assert audit["all_cells_nonnegative"]
            assert audit["all_cells_within_capacity"]

        for cell in natural:
            assert mixed[cell] == (8 * natural[cell] + right[cell]) / 9


def test_right_fill_minimizes_every_row_prefix() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        natural = certificate.natural_transport(epoch)
        right = certificate.right_greedy_transport(epoch)
        for source in range(2, 2 * epoch - 1):
            for target in range(max(epoch, source), 2 * epoch - 1):
                assert certificate.row_prefix(
                    epoch, right, source, target
                ) <= certificate.row_prefix(epoch, natural, source, target)
                assert certificate.row_prefix(
                    epoch, right, source, target
                ) == certificate.closed_right_prefix(epoch, source, target)


def test_mixed_cross_coefficients_are_below_natural_and_half_y() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        audit = certificate.cross_coefficient_audit(epoch)
        assert audit["right_at_most_natural"]
        assert audit["mixed_at_most_natural"]
        assert audit["natural_at_most_half_y"]
        assert audit["mixed_at_most_half_y"]
        assert Fraction(*map(int, audit["minimum_half_y_gap"].split("/"))) > 0


def test_right_fill_column_formula_and_mixed_two_thirds_bound() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        natural = certificate.natural_transport(epoch)
        right = certificate.right_greedy_transport(epoch)
        mixed = certificate.mixed_transport(epoch)
        for target in range(epoch, 2 * epoch - 1):
            shift = target - epoch
            assert certificate.column_mass(
                epoch, right, target
            ) == certificate.closed_right_column(epoch, target)
            assert certificate.column_mass(
                epoch, natural, target
            ) == certificate.closed_natural_column(epoch, target)
            assert certificate.column_mass(epoch, mixed, target) <= Fraction(
                2, 3
            ) * certificate.endpoint_coefficient(epoch, target)

            normalized_margin = certificate.normalized_endpoint_margin(epoch, target)
            assert normalized_margin > 0
            if shift == 0:
                assert normalized_margin == certificate.midpoint_margin(epoch)
            elif shift == 1:
                assert normalized_margin == certificate.next_column_margin(epoch)
            else:
                assert normalized_margin >= certificate.generic_margin_lower(epoch)


def test_endpoint_energy_bound_is_coefficientwise() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        mixed = certificate.mixed_transport(epoch)
        for target in range(epoch, 2 * epoch - 1):
            assert certificate.column_mass(epoch, mixed, target) <= Fraction(
                2, 3
            ) * certificate.endpoint_coefficient(epoch, target)
        audit = certificate.endpoint_audit(epoch)
        assert audit["every_column_at_most_two_thirds"]
        assert audit["rank_shift_can_only_reduce_endpoint"]


def test_universal_dpre_lower_coefficient_is_exact() -> None:
    for epoch in certificate.AUDIT_EPOCHS:
        direct = sum(
            (
                certificate.endpoint_coefficient(epoch, 2 * epoch - 1 - radius)
                * radius
                * (radius + 1)
                / 2
                for radius in range(1, epoch)
            ),
            Fraction(),
        )
        assert direct == certificate.dpre_lower_numerator(epoch)
        assert direct == Fraction(
            (epoch - 1) * (epoch + 1) * (5 * epoch - 4), 48 * epoch
        )


def test_signed_ledger_rewrite_and_ownership_flags() -> None:
    audit = certificate.signed_ledger_audit()
    assert audit["mixed_minus_old"] == {"Dpre": "-1/12"}
    assert audit["mixed_rewrite"] == {
        "B": "1",
        "Dpre": "2/3",
        "Kint": "-1",
        "ThetaFull": "-1",
        "Y": "1",
    }
    assert audit["dropped_bracket_must_not_be_reused"]
    assert not audit["remaining_fejer_inequality_proved"]
    assert not audit["p28_proved"]


def test_n4_near_arithmetic_golomb_counterexample_is_fully_rational() -> None:
    audit = certificate.counterexample_audit()
    assert audit["marks"] == [0, 101, 204, 309, 416, 525, 636, 749]
    assert audit["all_positive_differences_distinct"]
    assert audit["residual_coefficients"] == {
        "4,6": "259/5760",
        "4,7": "3/32",
        "5,7": "5/128",
    }
    assert audit["cross_ratios"] == {
        "4,6": "15840/11881",
        "4,7": "108891/96800",
        "5,7": "49280/36963",
    }
    residual_lower = Fraction(*map(int, audit["residual_log_lower"].split("/")))
    endpoint_upper = Fraction(*map(int, audit["dpre_over_twelve_log_upper"].split("/")))
    exact_gap = Fraction(*map(int, audit["certified_gap"].split("/")))
    assert residual_lower == Fraction(6_200_141_034_958_231, 177_031_495_611_818_280)
    assert endpoint_upper == Fraction(18_847_349, 1_269_964_800)
    assert exact_gap == residual_lower - endpoint_upper > 0
    assert audit["direct_domination_by_dpre_over_twelve_is_false"]
    assert not audit["signed_cut_corrected_domination_refuted"]

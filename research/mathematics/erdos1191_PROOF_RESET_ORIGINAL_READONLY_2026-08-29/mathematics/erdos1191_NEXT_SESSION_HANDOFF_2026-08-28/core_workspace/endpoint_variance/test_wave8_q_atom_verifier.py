from __future__ import annotations

import random
from fractions import Fraction

import pytest

from wave8_q_atom_verifier import (
    audit_q_atom_identities,
    contiguous_gap_sum,
    is_golomb_from_gap_weights,
    kernel_phi,
    nonadjacent_necessity_audit,
    points_from_gap_weights,
    rank_one_to_shell_ratio,
    shell_kappa,
)


def test_kernel_and_zero_extended_kappa_have_exact_small_values() -> None:
    assert kernel_phi(4, 5, length=8) == Fraction(47, 26880)
    assert shell_kappa(4, 4, old_count=4) == Fraction(-47, 26880)
    assert shell_kappa(4, 7, old_count=4) == Fraction(261, 8960)
    assert shell_kappa(5, 6, old_count=4) == Fraction(59, 13440)
    assert shell_kappa(7, 7, old_count=4) == Fraction(-61, 8960)


def test_matrix_pair_abel_square_and_envelope_identities_on_exact_vectors() -> None:
    rng = random.Random(81191)
    audits = []
    for old_count in range(2, 13):
        for _ in range(4):
            gaps = (1,) + tuple(
                rng.randint(1, 10_000) for _ in range(2 * old_count - 1)
            )
            audits.append(audit_q_atom_identities(gaps, old_count=old_count))
    assert len(audits) == 44
    assert all(audit.shell_h_energy > 0 for audit in audits)
    assert all(audit.rank_one_h_energy > 0 for audit in audits)
    assert all(audit.normalized_q_charge <= audit.positive_envelope for audit in audits)
    assert all(
        audit.negative_kappa_count == 2 * audit.old_count - 2 for audit in audits
    )
    assert all(
        audit.positive_kappa_count
        == audit.old_count * (audit.old_count + 1) // 2 - audit.negative_kappa_count
        for audit in audits
    )


def test_nonadjacent_bulk_atom_is_exactly_necessary_on_golomb_fixture() -> None:
    audit = nonadjacent_necessity_audit()
    assert audit.points == (0, 8, 24, 56, 58, 314, 318, 319)
    assert audit.boundary_debt == Fraction(68589931, 26880)
    assert audit.corner_asset == Fraction(18053109, 8960)
    assert audit.adjacent_asset == Fraction(72403, 280)
    assert audit.nonadjacent_asset == Fraction(49855, 168)
    assert audit.deficit_without_nonadjacent == Fraction(1869979, 6720)
    assert audit.surplus_with_nonadjacent == Fraction(41407, 2240)
    assert audit.shell_h_energy == Fraction(41407, 1178240)


def test_rank_one_to_shell_ratio_has_the_claimed_linear_asymptote() -> None:
    ratios = tuple(rank_one_to_shell_ratio(parameter) for parameter in (10, 100, 1000))
    scaled = tuple(
        ratio / parameter for ratio, parameter in zip(ratios, (10, 100, 1000))
    )
    target = Fraction(46, 45)
    assert abs(scaled[2] - target) < Fraction(1, 100)
    assert abs(scaled[2] - target) < abs(scaled[1] - target)
    assert abs(scaled[1] - target) < abs(scaled[0] - target)


def test_gap_conversion_and_input_mutations() -> None:
    gaps = (1, 8, 16, 32, 2, 256, 4, 1)
    assert points_from_gap_weights(gaps) == (0, 8, 24, 56, 58, 314, 318, 319)
    assert is_golomb_from_gap_weights(gaps)
    assert contiguous_gap_sum(gaps, 4, 6) == 262
    with pytest.raises(ValueError, match="h_0=1"):
        audit_q_atom_identities((2, 3, 5, 7), old_count=2)
    with pytest.raises(ValueError, match="indices"):
        kernel_phi(2, 2, length=4)
    with pytest.raises(ValueError, match="old_count"):
        shell_kappa(1, 2, old_count=2)

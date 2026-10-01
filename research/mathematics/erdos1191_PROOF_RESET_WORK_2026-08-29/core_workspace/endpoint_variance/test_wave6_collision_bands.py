from fractions import Fraction
from math import log

from wave4_nested_search import (
    critical_modulus_cap,
    dyadic_score_rows,
    independent_difference_audit,
)
from wave6_collision_bands import (
    antidiagonal_threshold,
    audit_band_collection,
    dyadic_antidiagonal_band,
    dyadic_shell_length_band,
    dyadic_shell_profile,
    fractional_threshold_sum,
    integer_band_capacity,
    low_band_cutoff,
    positive_integer_band_capacity,
    threshold_count,
    truncated_harmonic_threshold_sum,
)

PERFECT_FOUR = (0, 1, 4, 6)
THREE_RESET_FIXTURE = (
    0,
    1,
    18,
    34,
    79,
    127,
    171,
    218,
    319,
    415,
    509,
    613,
    710,
    808,
    903,
    1002,
)


def test_integer_band_capacity_respects_fractional_endpoints() -> None:
    # Catches replacing ceil(lower) and floor(upper) by truncation.
    assert integer_band_capacity(Fraction(3, 2), Fraction(7, 2)) == 2
    assert integer_band_capacity(Fraction(1, 2), Fraction(3, 2)) == 1
    assert integer_band_capacity(Fraction(5, 2), Fraction(3, 2)) == 0
    assert positive_integer_band_capacity(Fraction(-5, 2), Fraction(9, 4)) == 2


def test_two_shell_common_band_bound_is_exact_at_four_marks() -> None:
    # Catches losing the boundary gap or using a strict real-band count.
    first = dyadic_shell_length_band(PERFECT_FOUR, old_count=1, length=1)
    second = dyadic_shell_length_band(PERFECT_FOUR, old_count=2, length=1)
    assert (first.lower, first.upper, first.differences) == (
        Fraction(1),
        Fraction(1),
        (1,),
    )
    assert (second.lower, second.upper, second.differences) == (
        Fraction(3, 2),
        Fraction(7, 2),
        (3, 2),
    )
    audit = audit_band_collection((first, second))
    assert audit.selected_count == 3
    assert audit.distinct_count == 3
    assert audit.integer_capacity == 3
    assert audit.all_differences_distinct
    assert audit.all_differences_inside_envelope


def test_antidiagonal_band_uses_cross_boundary_differences() -> None:
    # Catches an off-by-one in the pair (m-1-t,m-1+s).
    flat_ruler = (0, 4, 6, 9)
    profile = dyadic_shell_profile(flat_ruler, old_count=2)
    assert profile.old_modulus == 5
    assert profile.shell_total == 5
    assert profile.old_mean == profile.shell_mean == Fraction(5, 2)
    assert profile.old_discrepancy == Fraction(3, 2)
    assert profile.shell_discrepancy == Fraction(1, 2)

    band = dyadic_antidiagonal_band(flat_ruler, old_count=2, antidiagonal=2)
    assert band.differences == (5, 6)
    assert band.lower == 3
    assert band.upper == 7
    assert band.integer_capacity == 5
    assert band.difference_count == 2
    assert band.all_differences_distinct
    assert band.all_differences_inside_band


def test_three_reset_fixture_is_exact_golomb_and_all_prefix_c1() -> None:
    # Catches a hidden difference collision or a floating-point cap decision.
    audit = independent_difference_audit(THREE_RESET_FIXTURE)
    assert audit.is_golomb
    assert audit.pair_count == 120
    assert len(audit.sorted_differences) == 120
    expected_moduli = (
        2,
        19,
        35,
        80,
        128,
        172,
        219,
        320,
        416,
        510,
        614,
        711,
        809,
        904,
        1003,
    )
    assert tuple(THREE_RESET_FIXTURE[n - 1] + 1 for n in range(2, 17)) == (
        expected_moduli
    )
    assert all(
        THREE_RESET_FIXTURE[n - 1] + 1 <= critical_modulus_cap(n, 1)
        for n in range(2, 17)
    )


def test_three_nontrivial_shells_are_flat_reset_and_high_innovation() -> None:
    # Catches normalizing shell discrepancy by the mean instead of total mass.
    expected = {
        2: ((17, 16), 33, Fraction(1, 2), Fraction(1, 66)),
        4: ((45, 48, 44, 47), 184, Fraction(1), Fraction(1, 184)),
        8: (
            (101, 96, 94, 104, 97, 98, 95, 99),
            784,
            Fraction(3),
            Fraction(3, 784),
        ),
    }
    for old_count, (gaps, total, discrepancy, normalized) in expected.items():
        profile = dyadic_shell_profile(THREE_RESET_FIXTURE, old_count=old_count)
        assert profile.shell_gaps == gaps
        assert profile.shell_total == total
        assert profile.shell_discrepancy == discrepancy
        assert profile.normalized_shell_discrepancy == normalized
        assert profile.endpoint_error <= Fraction(-1, 4)

    rows = dyadic_score_rows(THREE_RESET_FIXTURE, sizes=(2, 4, 8, 16))
    expected_innovations = (
        Fraction(159, 89600),
        Fraction(2923819, 1145948160),
        Fraction(24647951033, 7219313737728),
    )
    assert tuple(row.innovation_q00_per_modulus for row in rows[1:]) == (
        expected_innovations
    )
    assert all(value > Fraction(1, 600) for value in expected_innovations)


def test_all_shell_length_spectra_obey_one_global_integer_envelope() -> None:
    # Catches accidental reuse of one endpoint pair at different epochs.
    bands = tuple(
        dyadic_shell_length_band(
            THREE_RESET_FIXTURE, old_count=old_count, length=length
        )
        for old_count in (1, 2, 4, 8)
        for length in range(1, old_count + 1)
    )
    audit = audit_band_collection(bands)
    assert audit.selected_count == 50
    assert audit.distinct_count == 50
    assert audit.selected_count <= audit.integer_capacity
    assert audit.all_differences_distinct
    assert audit.all_differences_inside_envelope


def test_threshold_form_is_equivalent_and_integrates_exactly() -> None:
    # Catches dropping the discrepancy H_m or the weight k in the layer cake.
    profiles = tuple(
        dyadic_shell_profile(PERFECT_FOUR, old_count=old_count)
        for old_count in (1, 2)
    )
    thresholds = tuple(
        antidiagonal_threshold(profile, antidiagonal)
        for profile in profiles
        for antidiagonal in range(1, profile.old_count + 1)
    )
    assert thresholds == (Fraction(1), Fraction(3), Fraction(11, 2))

    for profile in profiles:
        for antidiagonal in range(1, profile.old_count + 1):
            threshold = antidiagonal_threshold(profile, antidiagonal)
            assert low_band_cutoff(profile, threshold) >= antidiagonal
            assert (
                low_band_cutoff(profile, threshold - Fraction(1, 1000))
                < antidiagonal
            )

    assert threshold_count(profiles, Fraction(11, 2)) == 4
    harmonic = truncated_harmonic_threshold_sum(profiles, Fraction(11, 2))
    assert harmonic == Fraction(56, 33)
    assert float(harmonic) <= 1 + log(Fraction(11, 2))

    fractional = fractional_threshold_sum(profiles, epsilon=1)
    assert fractional == Fraction(1282, 1089)
    assert fractional <= 2

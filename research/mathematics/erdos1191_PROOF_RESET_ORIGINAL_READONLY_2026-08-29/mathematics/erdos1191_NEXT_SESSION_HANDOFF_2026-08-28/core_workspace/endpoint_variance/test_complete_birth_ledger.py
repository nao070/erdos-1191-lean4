from fractions import Fraction
from hashlib import sha256

import pytest

from complete_birth_ledger import (
    audit_complete_birth_ledger,
    audit_erdos_turan_1423,
    complete_birth_families,
    complete_w2,
    critical_modulus_cap,
    epoch_birth_families,
    erdos_turan_ruler,
    log_integer_interval,
)
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS


def test_log_enclosure_and_known_critical_caps_are_exact() -> None:
    lower, upper = log_integer_interval(257, 16)
    assert lower < upper
    assert critical_modulus_cap(3) == 19
    assert critical_modulus_cap(4) == 44
    assert critical_modulus_cap(5) == 80
    assert critical_modulus_cap(8) == 266
    assert critical_modulus_cap(256) == 726_817
    assert critical_modulus_cap(257) == 733_021
    assert critical_modulus_cap(512) == 3_270_678


def test_smallest_complete_partition_has_all_six_pairs() -> None:
    points = (0, 1, 4, 6)
    families = complete_birth_families(points)
    pairs = tuple(pair for family in families for pair in family.pairs)
    differences = tuple(
        difference for family in families for difference in family.differences
    )
    assert len(families) == 5
    assert len(pairs) == len(set(pairs)) == 6
    assert len(differences) == len(set(differences)) == 6
    assert set(differences) == {1, 2, 3, 4, 5, 6}
    assert all(
        family.lower <= difference <= family.upper
        for family in families
        for difference in family.differences
    )


def test_64_mark_fixture_checks_every_threshold_and_wedge() -> None:
    audit = audit_complete_birth_ledger(COUNTEREXAMPLE_64_POINTS)
    assert audit.mark_count == 64
    assert audit.family_count == 177
    assert audit.pair_count == audit.distinct_difference_count == 2_016
    assert audit.threshold_count == 177
    assert audit.wedge_check_count == 177 * 63
    assert isinstance(audit.w2, Fraction)
    assert audit.w2_square_at_most_128
    assert audit.w2 == complete_w2(complete_birth_families(COUNTEREXAMPLE_64_POINTS))


def test_non_power_terminal_prefix_is_rejected() -> None:
    with pytest.raises(ValueError, match="power of two"):
        complete_birth_families((0, 1, 4))


def test_p1423_exact_bridge_counterexample_and_all_prefix_caps() -> None:
    audit = audit_erdos_turan_1423()
    assert audit.prime == 1_423
    assert audit.old_count == 256
    assert audit.mark_count == 512
    assert audit.pair_count == 130_816
    assert audit.old_modulus == 726_721
    assert audit.new_modulus == 1_455_019
    assert audit.compatible_prefix_count == 257
    assert audit.minimum_cap_slack == 96
    assert audit.innovation_q00_per_modulus == Fraction(
        72_931_155_410_271_048_281_010_903,
        26_431_687_539_869_343_576_651_464_704,
    )
    assert audit.w2_upper_bound == Fraction(2_304, 2_024_929)
    assert audit.w2 < audit.w2_upper_bound < audit.innovation_q00_per_modulus
    assert audit.comparison_cross_product == (
        86_781_803_501_905_775_924_014_152_122_871
    )
    numerator = audit.w2.numerator.to_bytes(
        (audit.w2.numerator.bit_length() + 7) // 8, "big"
    )
    denominator = audit.w2.denominator.to_bytes(
        (audit.w2.denominator.bit_length() + 7) // 8, "big"
    )
    payload = (
        len(numerator).to_bytes(4, "big")
        + numerator
        + len(denominator).to_bytes(4, "big")
        + denominator
    )
    assert sha256(payload).hexdigest() == (
        "eaff996a08dc4a8082612fe3384de6b7f0ad260732682edebac27c0517a81a0c"
    )


def test_p1423_epoch_partition_contains_every_born_pair_once() -> None:
    points = erdos_turan_ruler(512, 1_423)
    families = epoch_birth_families(points, old_count=256)
    pairs = tuple(pair for family in families for pair in family.pairs)
    expected = {(left, right) for right in range(256, 512) for left in range(right)}
    assert len(families) == 766
    assert len(pairs) == len(set(pairs)) == 98_176
    assert set(pairs) == expected
    assert all(
        family.lower <= difference <= family.upper
        for family in families
        for difference in family.differences
    )

    full_audit = audit_complete_birth_ledger(points)
    assert full_audit.family_count == full_audit.threshold_count == 1_515
    assert full_audit.pair_count == full_audit.distinct_difference_count == 130_816
    assert full_audit.wedge_check_count == 1_515 * 511
    assert full_audit.w2_square_at_most_128

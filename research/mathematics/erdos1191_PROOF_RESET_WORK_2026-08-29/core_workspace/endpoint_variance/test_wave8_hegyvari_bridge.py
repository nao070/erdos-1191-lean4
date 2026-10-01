from __future__ import annotations

import json
from math import comb

import pytest

from wave8_hegyvari_bridge import (
    affine_hegyvari_variants,
    audit_original_construction,
    blocker_for_gap_translations,
    build_certificate,
    common_difference_witness,
    embed_prescribed_differences,
    endpoint_joined_two_block_search,
    exhaustive_compatibility_audit,
    find_compatible_hegyvari_variant,
    hegyvari_gaps,
    hegyvari_marks,
    hegyvari_upper_inequality,
    is_golomb,
    positive_differences,
    safe_separated_shift,
    safely_splice,
    two_block_search,
    universal_affine_differences,
    untranslated_collision_histogram,
)


def test_original_formula_telescopes_and_has_exact_finite_constants() -> None:
    for prime in (3, 5, 7, 11, 13):
        marks = hegyvari_marks(prime)
        gaps = hegyvari_gaps(prime)
        residues = tuple(index * index % prime for index in range(prime + 1))
        assert marks == tuple(
            2 * prime * index + residues[index] for index in range(prime + 1)
        )
        assert gaps == tuple(
            2 * prime + residues[index + 1] - residues[index] for index in range(prime)
        )
        assert marks[-1] == 2 * prime * prime
        assert min(gaps) >= prime + 1
        assert max(gaps) <= 3 * prime - 1
        assert len(positive_differences(marks)) == comb(prime + 1, 2)

        audit = audit_original_construction(prime)
        assert audit.mark_count == prime + 1
        assert audit.gap_count == prime
        assert audit.endpoint == 2 * prime * prime
        assert (
            audit.positive_difference_count == audit.expected_positive_difference_count
        )


def test_exact_upper_counting_inequality_and_two_thirds_limit() -> None:
    gaps = hegyvari_gaps(11)
    previous = None
    for length in (1, 2, 4, 8, 11):
        row = hegyvari_upper_inequality(gaps, length)
        assert (
            row.restricted_sum_count == length * len(gaps) - length * (length - 1) // 2
        )
        assert row.distinct_positive_lower_bound <= row.actual_restricted_sum_total
        assert row.actual_restricted_sum_total <= row.occurrence_upper_bound
        assert row.occurrence_upper_bound <= row.distinct_gap_upper_bound
        if previous is not None:
            assert row.asymptotic_ratio_bound < previous
        previous = row.asymptotic_ratio_bound
    assert previous == pytest.approx(24 / 34)

    with pytest.raises(ValueError, match="not distinct"):
        hegyvari_upper_inequality((1, 2, 3), 2)


def test_every_affine_rotation_and_gap_translation_in_sample_is_golomb() -> None:
    for prime in (3, 5, 7):
        for alpha in range(1, prime):
            for beta in range(prime):
                for gamma in range(prime):
                    for rotation in range(prime):
                        marks = hegyvari_marks(
                            prime,
                            alpha=alpha,
                            beta=beta,
                            gamma=gamma,
                            rotation=rotation,
                            gap_translation=2,
                        )
                        assert is_golomb(marks)
                        assert marks[-1] == prime * (2 * prime + 2)


def test_affine_enumerator_is_deterministic_and_deduplicated() -> None:
    variants = tuple(affine_hegyvari_variants(5))
    rulers = tuple(marks for _, marks in variants)
    assert variants[0][0] == (1, 0, 0)
    assert len(rulers) == len(set(rulers))
    assert all(is_golomb(ruler) for ruler in rulers)


def test_base_and_full_span_are_universal_affine_differences() -> None:
    for prime, translation in ((3, 0), (5, 0), (5, 3), (7, 2), (11, 5)):
        base = 2 * prime + translation
        assert universal_affine_differences(prime, gap_translation=translation) == {
            base,
            prime * base,
        }


def test_every_affine_block_has_the_forced_multiple_skeleton() -> None:
    for prime, translation in ((5, 0), (7, 2), (11, 3)):
        base = 2 * prime + translation
        for _, marks in affine_hegyvari_variants(prime, gap_translation=translation):
            differences = positive_differences(marks)
            for separation in range(1, prime):
                assert (
                    separation * base in differences
                    or (prime - separation) * base in differences
                )


def test_disjoint_internal_differences_are_exact_splice_criterion() -> None:
    first = (0, 1, 4, 6)
    compatible_second = (0, 7, 15)
    assert positive_differences(first).isdisjoint(
        positive_differences(compatible_second)
    )
    shift = safe_separated_shift(first, compatible_second)
    assert shift == 22
    spliced = safely_splice(first, compatible_second)
    assert spliced == (0, 1, 4, 6, 22, 29, 37)
    assert is_golomb(spliced)

    incompatible_second = (0, 2, 7)
    witness = common_difference_witness(first, incompatible_second)
    assert witness is not None
    assert witness.difference == 2
    with pytest.raises(ValueError, match="intersect at 2"):
        safely_splice(first, incompatible_second)

    # The same mixed collision occurs for every shift T:
    # (T+2)-0 = (T+0)-2 when the oriented endpoint pairs are chosen.
    for arbitrary_shift in (8, 100, 10_000):
        union = first + tuple(arbitrary_shift + mark for mark in incompatible_second)
        assert not is_golomb(union)


def test_any_finite_menu_of_universal_spans_can_be_embedded_in_old_ruler() -> None:
    requested = (50, 55, 60, 65)
    old = embed_prescribed_differences(requested)
    assert is_golomb(old)
    assert set(requested) <= positive_differences(old)

    # Regression: the weaker old choice x=2M+1 would make x-50=51 and
    # collide with the prescribed pair of length 51.
    tricky = embed_prescribed_differences((50, 51))
    assert tricky == (0, 50, 102, 153)
    assert is_golomb(tricky)
    assert {50, 51} <= positive_differences(tricky)

    blocker = blocker_for_gap_translations(5, 3)
    assert blocker == old
    for translation in range(4):
        for _, block in affine_hegyvari_variants(5, gap_translation=translation):
            assert block[-1] == requested[translation]
            assert common_difference_witness(blocker, block) is not None
    assert (
        find_compatible_hegyvari_variant(blocker, 5, maximum_gap_translation=3) is None
    )


def test_two_full_blocks_with_same_parameters_can_never_be_concatenated() -> None:
    for prime in (3, 5, 7):
        first = hegyvari_marks(prime)
        for _, second in affine_hegyvari_variants(prime):
            witness = common_difference_witness(first, second)
            assert witness is not None
            # Every variant has the same full-span difference p*(2p).
            assert first[-1] in positive_differences(second)
        assert not two_block_search(prime, prime)["compatible"]


def test_small_old_prefix_searches_are_exact_and_reproducible() -> None:
    audits = (
        exhaustive_compatibility_audit(
            mark_count=4,
            maximum_endpoint=16,
            prime=3,
            maximum_gap_translation=3,
        ),
        exhaustive_compatibility_audit(
            mark_count=4,
            maximum_endpoint=20,
            prime=5,
            maximum_gap_translation=2,
        ),
    )
    assert audits[0].ruler_count > 0
    assert audits[1].ruler_count > audits[0].ruler_count
    assert all(
        audit.compatible_within_range_count <= audit.ruler_count for audit in audits
    )
    assert (
        audits[0].ruler_count,
        audits[0].compatible_at_zero_count,
        audits[0].compatible_within_range_count,
        audits[0].largest_minimum_translation,
    ) == (354, 68, 196, 3)
    assert (
        audits[1].ruler_count,
        audits[1].compatible_at_zero_count,
        audits[1].compatible_within_range_count,
        audits[1].largest_minimum_translation,
    ) == (802, 232, 452, 2)
    assert audits == tuple(
        exhaustive_compatibility_audit(
            mark_count=audit.mark_count,
            maximum_endpoint=audit.maximum_endpoint,
            prime=audit.prime,
            maximum_gap_translation=audit.maximum_gap_translation,
        )
        for audit in audits
    )


def test_distinct_untranslated_blocks_fail_but_translated_blocks_can_splice() -> None:
    untranslated = tuple(
        two_block_search(first, second) for first, second in ((3, 5), (5, 7), (7, 11))
    )
    assert not any(result["compatible"] for result in untranslated)
    assert untranslated_collision_histogram(3, 5) == {6: 20, 7: 20, 11: 20}
    assert untranslated_collision_histogram(5, 7) == {9: 56, 10: 42, 11: 70}
    assert untranslated_collision_histogram(7, 11) == {
        12: 110,
        13: 132,
        14: 154,
        15: 110,
        16: 66,
        17: 88,
    }

    searches = tuple(
        two_block_search(first, second, maximum_gap_translation=120)
        for first, second in ((3, 5), (5, 7), (7, 11), (11, 13))
    )
    for result in searches:
        if result["compatible"]:
            assert is_golomb(result["spliced"])
            assert result["endpoint"] == result["spliced"][-1]
    assert tuple(result["gap_translation"] for result in searches) == (2, 18, 34, 94)


def test_endpoint_joined_blocks_have_exact_small_positive_examples() -> None:
    searches = tuple(
        endpoint_joined_two_block_search(
            first,
            second,
            maximum_gap_translation=maximum,
        )
        for first, second, maximum in (
            (3, 5, 20),
            (5, 7, 40),
            (7, 11, 80),
            (11, 13, 120),
        )
    )
    assert tuple(
        (
            result["gap_translation"],
            tuple(result["second_parameters"]),
            result["mark_count"],
            result["endpoint"],
        )
        for result in searches
    ) == (
        (2, (2, 0, 2), 9, 78),
        (18, (1, 3, 0), 13, 274),
        (50, (4, 4, 8), 19, 890),
        (106, (2, 10, 11), 25, 1958),
    )
    assert all(is_golomb(result["joined"]) for result in searches)


def test_certificate_is_exactly_json_serializable() -> None:
    certificate = build_certificate()
    rendered = json.dumps(certificate, sort_keys=True)
    assert '"schema": "erdos1191.wave8.hegyvari_bridge.v1"' in rendered
    assert certificate["translation_blocker"]["blocks_every_translation"]

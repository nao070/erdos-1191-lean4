from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

import pytest

from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave7_band_renewal_certificate import build_certificate
from wave7_band_renewal_probe import (
    adjacent_half_overlap_debt,
    all_prefix_c1,
    compatible_adjacent_gap_swaps,
    enumerate_compatible_four_mark_rulers,
    enumerate_four_mark_est_failure_region,
    epoch_size_tax_candidate,
    harmonic_epoch_tax_candidate,
    is_golomb,
    load_authenticated_wave6_fixtures,
    renewal_hole_candidate,
    short_shell_eight_mark_audit,
)

DIRECTORY = Path(__file__).resolve().parent
SOURCE_CERTIFICATE = DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
WAVE7_CERTIFICATE = DIRECTORY / "wave7_band_renewal_certificate_2026-08-28.json"


@pytest.fixture(scope="module")
def fixtures():
    return load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)


def test_authenticated_wave6_points_are_exact_finite_golomb_rulers(fixtures) -> None:
    points = (
        *fixtures.sixty_four_mark_points,
        fixtures.one_hundred_twenty_eight_mark_points,
    )
    assert tuple(map(len, points)) == (64, 64, 64, 64, 64, 64, 128)
    assert all(is_golomb(ruler) for ruler in points)
    assert all(all_prefix_c1(ruler) for ruler in points)


def test_local_renewal_hole_candidate_is_refuted_exactly(fixtures) -> None:
    imported = renewal_hole_candidate(fixtures.sixty_four_mark_points[0])
    assert (
        imported.lower,
        imported.upper,
        imported.width,
        imported.occupancy,
        imported.epochs,
        imported.margin,
    ) == (21, 22, 2, 2, (4, 8), -1)
    assert tuple((atom.difference, atom.epoch) for atom in imported.atoms) == (
        (21, 8),
        (22, 4),
    )

    counterexample = renewal_hole_candidate(COUNTEREXAMPLE_64_POINTS)
    assert (
        counterexample.lower,
        counterexample.upper,
        counterexample.epochs,
        counterexample.margin,
    ) == (382, 383, (8, 16), -1)


def test_harmonic_epoch_tax_candidate_is_refuted_exactly(fixtures) -> None:
    row = harmonic_epoch_tax_candidate(fixtures.sixty_four_mark_points[0])
    assert row.threshold == 3
    assert row.cumulative_weight == 2
    assert row.active_epochs == (1, 2)
    assert row.harmonic_number == Fraction(3, 2)
    assert row.reciprocal_threshold_sum == Fraction(4, 3)
    assert row.proposed_tax == Fraction(1, 3)
    assert row.margin == Fraction(-1, 6)


def test_epoch_size_tax_survives_exhaustive_four_mark_scope() -> None:
    rulers = tuple(enumerate_compatible_four_mark_rulers())
    assert len(rulers) == 1672
    rows = tuple(
        (points, epoch_size_tax_candidate(points, minimum_active_epochs=2))
        for points in rulers
    )
    assert sum(row.margin < 0 for _, row in rows) == 0
    assert tuple(points for points, row in rows if row.margin == 0) == (
        (0, 1, 4, 6),
        (0, 2, 5, 6),
    )
    universal_region = tuple(enumerate_four_mark_est_failure_region())
    assert len(universal_region) == 9
    assert all(
        epoch_size_tax_candidate(points, minimum_active_epochs=2).margin >= 0
        for points in universal_region
    )


def test_epoch_size_tax_survives_complete_eight_mark_failure_region() -> None:
    audit = short_shell_eight_mark_audit()
    assert audit.maximum_parent_last_mark == 34
    assert audit.parent_count == 4934
    assert audit.extension_count == 3341161
    assert audit.search_node_count == 37423576
    assert audit.minimum_four_times_first_threshold == 44
    assert audit.minimum_threshold_points == (0, 2, 5, 6, 15, 22, 33, 41)


def test_epoch_size_tax_survives_authenticated_and_swap_scope(fixtures) -> None:
    swaps = tuple(
        variant
        for points in fixtures.sixty_four_mark_points
        for variant in compatible_adjacent_gap_swaps(points)
    )
    assert len(swaps) == 23
    assert tuple(
        len(compatible_adjacent_gap_swaps(points))
        for points in fixtures.sixty_four_mark_points
    ) == (1, 1, 2, 6, 9, 4)

    rulers = (
        tuple(COUNTEREXAMPLE_64_POINTS),
        *fixtures.sixty_four_mark_points,
        fixtures.one_hundred_twenty_eight_mark_points,
        *(variant.points for variant in swaps),
    )
    minima = {}
    for required in range(2, 8):
        rows = []
        for points in rulers:
            try:
                rows.append(
                    epoch_size_tax_candidate(
                        points,
                        minimum_active_epochs=required,
                    )
                )
            except ValueError:
                pass
        minima[required] = min(
            rows,
            key=lambda row: (row.margin, row.threshold, row.cumulative_weight),
        )
    assert tuple(minima[level].margin for level in range(2, 8)) == (
        0,
        30,
        153,
        584,
        2099,
        36608,
    )
    assert minima[7].threshold == Fraction(1198199, 32)
    debt = adjacent_half_overlap_debt(
        fixtures.one_hundred_twenty_eight_mark_points,
        minima[7].threshold,
    )
    assert debt.forced_old_epochs == (64,)
    assert debt.both_cheap_epochs == (1, 2, 4, 8, 16, 32)
    assert (
        debt.epoch_size_tax,
        debt.maximum_distinct_adjacent_charge,
        debt.overlap_debt,
    ) == (120, 63, 57)
    assert (
        debt.selected_boundary_overlap,
        debt.maximum_new_adjacent_charge,
        debt.total_charge_debt,
    ) == (6, 57, 63)


def test_certificate_internal_hash_and_full_replay() -> None:
    committed = json.loads(WAVE7_CERTIFICATE.read_text(encoding="utf-8"))
    internal_hash = committed.pop("certificate_sha256")
    canonical = json.dumps(committed, sort_keys=True, separators=(",", ":"))
    assert sha256(canonical.encode("utf-8")).hexdigest() == internal_hash
    rebuilt = build_certificate(SOURCE_CERTIFICATE)
    assert rebuilt == {**committed, "certificate_sha256": internal_hash}

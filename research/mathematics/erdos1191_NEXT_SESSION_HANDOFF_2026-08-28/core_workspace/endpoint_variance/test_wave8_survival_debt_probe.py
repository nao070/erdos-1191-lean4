from __future__ import annotations

import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path

from wave7_band_renewal_probe import load_authenticated_wave6_fixtures
from wave8_survival_debt_probe import (
    actual_renewal_comparison,
    bounded_golomb_exhaustion,
    build_certificate,
    critical_children,
    critical_survival_audit,
    repayment_audit,
)

DIRECTORY = Path(__file__).resolve().parent
SOURCE_CERTIFICATE = DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
WAVE8_CERTIFICATE = DIRECTORY / "wave8_survival_debt_certificate_2026-08-28.json"


def test_critical_children_use_the_exact_next_prefix_cap() -> None:
    children = critical_children((0, 1, 4, 6))
    assert len(children) == 67
    assert children[0] == (0, 1, 4, 6, 13)
    assert children[-1] == (0, 1, 4, 6, 79)


def test_depth_two_survival_proxy_does_not_remove_global_debt_counterexample() -> None:
    points = (0, 3, 7, 13, 21, 22, 33, 38)
    survival = critical_survival_audit(points, depth=2)
    assert survival.level_counts == (1, 286, 61_448)
    assert survival.survives_requested_depth is True

    row = repayment_audit(points, Fraction(51, 4))
    assert row.active_epochs == (1, 2, 4)
    assert row.wave6_pair_count == 5
    assert row.epoch_size_tax == 4
    assert row.optimal_adjacent_new_count == 1
    assert row.optimal_adjacent_debt == 3
    assert row.certified_reservoir_count == 0
    assert row.certified_debt_margin == -3
    assert row.global_nonadjacent_reservoir_count == 2
    assert row.global_nonadjacent_debt_margin == -1
    assert row.latest_shell_nonadjacent_reservoir_count == 2
    assert row.latest_shell_nonadjacent_debt_margin == -1


def test_actual_single_family_debt_also_exceeds_nonadjacent_reservoir() -> None:
    points = (0, 2, 5, 6, 14, 25, 32, 42)
    survival = critical_survival_audit(points, depth=2)
    assert survival.level_counts == (1, 280, 59_361)

    row = actual_renewal_comparison(points, old_count=4)
    assert row.ancestry_cleared is True
    assert row.new_family_paid is False
    assert row.outstanding_demand == 3
    assert row.actual_new_family_threshold == 11
    assert row.first_cross_threshold == Fraction(43, 4)
    assert row.global_nonadjacent_reservoir_count == 2
    assert row.global_debt_margin == -1
    assert row.latest_shell_nonadjacent_reservoir_count == 1
    assert row.latest_shell_debt_margin == -2
    assert row.normalized_adjoint_innovation == Fraction(731_477, 86_976_960)
    assert row.global_density_innovation_margin == Fraction(15_450_283, 86_976_960)
    assert row.latest_density_innovation_margin == Fraction(7_359_403, 86_976_960)


def test_global_density_bridge_is_false_without_the_critical_cap() -> None:
    base = (0, 8, 24, 56, 58, 314, 318, 319)
    points = tuple(100 * mark for mark in base)
    row = actual_renewal_comparison(points, old_count=4)
    assert row.first_cross_threshold == Fraction(42_449, 2)
    assert row.global_nonadjacent_reservoir_count == 5
    assert row.normalized_adjoint_innovation == Fraction(
        16_828_076_637_395, 7_660_787_849_434_944
    )
    assert row.global_density_innovation_margin == Fraction(
        -637_727_146_686_430_915, 325_192_783_420_663_937_856
    )


def test_rank_lag_half_reservoir_has_an_earlier_depth_two_counterexample() -> None:
    points = (0, 4, 10, 13, 15, 27, 34, 35)
    survival = critical_survival_audit(points, depth=2)
    assert survival.level_counts == (1, 286, 61_427)

    row = repayment_audit(points, Fraction(25, 2))
    assert row.option_signature == (
        (("none", 0),),
        (("old", 1), ("new", 1)),
        (("old", 2),),
    )
    assert row.certified_reservoir_count == 0
    assert row.certified_debt_margin == -3
    assert row.global_nonadjacent_reservoir_count == 3
    assert row.global_nonadjacent_debt_margin == 0


def test_bounded_eight_mark_enumeration_is_complete_and_deterministic() -> None:
    audit = bounded_golomb_exhaustion(mark_count=8, maximum_last_mark=40)
    assert audit.ruler_count == 1_468
    assert audit.search_node_count == 889_645
    assert audit.first_ruler == (0, 1, 3, 7, 15, 24, 35, 40)
    assert audit.last_ruler == (0, 13, 16, 25, 33, 35, 39, 40)


def test_small_global_density_bridge_survives_but_is_only_finite() -> None:
    points = (0, 4, 5, 7, 17, 26, 32, 40)
    row = repayment_audit(points, Fraction(47, 4))
    assert row.global_nonadjacent_reservoir_count == 1
    assert row.normalized_adjoint_innovation == Fraction(55_529, 6_024_704)
    assert row.global_density_innovation_margin == Fraction(21_488_953, 283_161_088)
    assert row.global_density_to_innovation_ratio == Fraction(24_098_816, 2_609_863)


def test_global_reservoir_uses_the_true_minimum_adjacent_debt() -> None:
    fixtures = load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)
    row = repayment_audit(fixtures.sixty_four_mark_points[0], Fraction(4_531, 8))
    assert row.optimal_adjacent_new_count == 4
    assert row.optimal_adjacent_debt == 7
    assert row.maximum_adjacent_new_count == 11
    assert row.minimum_adjacent_debt == 0
    assert row.global_nonadjacent_reservoir_count == 78
    assert row.global_nonadjacent_debt_margin == 78
    assert row.latest_shell_nonadjacent_reservoir_count == 68
    assert row.latest_shell_nonadjacent_debt_margin == 68


def test_certificate_replays_all_owned_finite_scopes() -> None:
    certificate = build_certificate(SOURCE_CERTIFICATE)
    assert certificate["schema"] == "wave8_survival_debt_probe_v1"
    assert certificate["bounded_eight_mark_scope"]["ruler_count"] == 1_468
    assert certificate["bounded_eight_mark_scope"]["search_node_count"] == 889_645
    assert (
        certificate["bounded_eight_mark_scope"]["candidate_results"][
            "global_density_innovation"
        ]["negative_count"]
        == 0
    )
    actual = certificate["actual_single_debt_bounded_eight_scope"]
    assert actual["ruler_count"] == 26_458
    assert actual["search_node_count"] == 2_742_059
    assert actual["old_clear_only_count"] == 1_250
    assert actual["candidate_results"]["global_debt"]["negative_count"] == 6
    assert actual["candidate_results"]["latest_shell_debt"]["negative_count"] == 16
    assert (
        actual["candidate_results"]["global_density_innovation"]["negative_count"] == 0
    )
    assert (
        actual["candidate_results"]["latest_density_innovation"]["negative_count"] == 0
    )
    assert actual["density_ratio_calibration"]["global_minimum_ratio"] == (
        "186624000/10274249"
    )
    assert actual["density_ratio_calibration"]["latest_minimum_ratio"] == (
        "3250176/354757"
    )
    unrestricted = certificate["unrestricted_scaling_no_go"]
    assert unrestricted["scale"] == 100
    assert unrestricted["obeys_all_prefix_c1"] is False
    assert unrestricted["comparison"]["global_density_innovation_margin"] == (
        "-637727146686430915/325192783420663937856"
    )
    assert certificate["conclusions"]["erdos_1191_resolved"] is False
    assert certificate["conclusions"]["infinite_extension_claimed"] is False

    committed = json.loads(WAVE8_CERTIFICATE.read_text(encoding="utf-8"))
    internal_hash = committed.pop("certificate_sha256")
    canonical = json.dumps(committed, sort_keys=True, separators=(",", ":"))
    assert sha256(canonical.encode("utf-8")).hexdigest() == internal_hash
    assert certificate == {**committed, "certificate_sha256": internal_hash}

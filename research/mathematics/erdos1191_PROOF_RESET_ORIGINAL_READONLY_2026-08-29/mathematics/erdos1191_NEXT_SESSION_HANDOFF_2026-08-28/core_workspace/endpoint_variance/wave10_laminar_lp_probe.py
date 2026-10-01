"""Exact finite probe for the Wave 10 laminar incomplete-DTS relaxation.

The finite relaxation has three rigorously separated pieces.

* ``audit_rlp_all_subsets`` checks W9-RLP simultaneously for every finite
  epoch subset and every allowed lag cutoff.  A dynamic program retains the
  smallest right-hand side for each possible selected-difference count, so
  the check is exhaustive without enumerating every selection vector.
* ``audit_laminar_tile_lp`` makes every observed nonadjacent genuine birth
  tile a primal variable.  It imposes the Wave 9 per-epoch tile capacities and
  the cross-epoch magnitude capacity.  Each one-constraint knapsack block is
  solved by an exact greedy primal and an exact threshold dual.
* The exact scalar objective is also the rational lower part of the retained
  cross-ratio potential, because the factors ``D^2`` cancel.  The exact
  fixed-H objective is independently evaluated and is majorized by the tile
  LP.

W9-RLP depends only on the already fixed prefix moduli, whereas the tile LP
variables do not occur in it.  The executable therefore exposes a genuine
zero-column obstruction: merely adjoining all W9-RLP inequalities to this
tile relaxation cannot change its optimum.  This is a no-go for the tested
relaxation, not for stronger survival-conditioned inequalities and not a
resolution of Erdős Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any

from complete_birth_ledger import critical_modulus_cap, erdos_turan_ruler
from wave7_band_renewal_probe import load_authenticated_wave6_fixtures

PERFECT_FOUR = (0, 1, 4, 6)
DIRECTORY = Path(__file__).resolve().parent
DEFAULT_SOURCE_CERTIFICATE = (
    DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
)

TileKey = tuple[int, int, int, int]


def _validated_golomb(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 4
        or marks[0] != 0
        or any(not isinstance(mark, int) for mark in marks)
        or marks != tuple(sorted(set(marks)))
    ):
        raise ValueError(
            "points must be at least four normalized strictly increasing integers"
        )
    differences = {
        marks[right] - marks[left]
        for right in range(1, len(marks))
        for left in range(right)
    }
    if len(differences) != len(marks) * (len(marks) - 1) // 2:
        raise ValueError("points must form a Golomb ruler")
    return marks


def _floor_power_of_two(value: int) -> int:
    if not isinstance(value, int) or value < 1:
        raise ValueError("value must be a positive integer")
    return 1 << (value.bit_length() - 1)


def _dyadic_epochs(
    marks: tuple[int, ...], max_terminal_mark_count: int | None = None
) -> tuple[int, ...]:
    terminal_limit = len(marks)
    if max_terminal_mark_count is not None:
        if not isinstance(max_terminal_mark_count, int) or max_terminal_mark_count < 2:
            raise ValueError("max_terminal_mark_count must be an integer at least two")
        terminal_limit = min(terminal_limit, max_terminal_mark_count)
    epochs: list[int] = []
    old_count = 1
    while 2 * old_count <= terminal_limit:
        epochs.append(old_count)
        old_count *= 2
    return tuple(epochs)


def _gap_weights(marks: tuple[int, ...]) -> tuple[int, ...]:
    return (
        1,
        *(marks[index] - marks[index - 1] for index in range(1, len(marks))),
    )


def _fixed_h_kernel(left: int, right: int, count: int) -> Fraction:
    difference = right - left
    centered_sum = count - left - right
    numerator = (
        difference
        * difference
        * (
            112 * centered_sum * centered_sum
            + 16 * centered_sum * count
            + 12 * count * count
        )
    )
    return Fraction(numerator, 105 * count**4)


def _points_sha256(points: Sequence[int]) -> str:
    encoded = ",".join(str(point) for point in points).encode("ascii")
    return sha256(encoded).hexdigest()


@dataclass(frozen=True)
class RLPAudit:
    epoch_moduli: tuple[tuple[int, int], ...]
    selection_vector_count: int
    reachable_positive_totals: int
    transition_count: int
    minimum_slack: int
    minimum_slack_choices: tuple[tuple[int, int], ...]
    maximum_pressure: Fraction
    maximum_pressure_choices: tuple[tuple[int, int], ...]
    violation_count: int


def audit_rlp_all_subsets(
    points: Sequence[int], *, max_terminal_mark_count: int | None = None
) -> RLPAudit:
    """Exhaust W9-RLP over every epoch subset and every cutoff.

    Giving an epoch cutoff zero means that the epoch is absent from the
    subset.  Thus the Cartesian product ``q_m in {0,...,m}``, apart from its
    all-zero member, is exactly the requested family of all subsets and all
    legal positive cutoffs on selected epochs.
    """
    marks = _validated_golomb(points)
    epochs = _dyadic_epochs(marks, max_terminal_mark_count)
    epoch_moduli = tuple((m, marks[2 * m - 1] + 1) for m in epochs)

    # total M -> (minimum RHS at this M, full q-vector).  Keeping only the
    # minimum RHS is exact because the W9-RLP left side depends only on M.
    states: dict[int, tuple[int, tuple[int, ...]]] = {0: (0, ())}
    selection_vector_count = 1
    transition_count = 0
    for epoch, modulus in epoch_moduli:
        next_states: dict[int, tuple[int, tuple[int, ...]]] = {}
        selection_vector_count *= epoch + 1
        for total, (cost, choices) in states.items():
            for cutoff in range(epoch + 1):
                transition_count += 1
                new_total = total + epoch * cutoff
                new_cost = cost + modulus * cutoff * (cutoff + 1) // 2
                new_choices = (*choices, cutoff)
                incumbent = next_states.get(new_total)
                candidate = (new_cost, new_choices)
                if incumbent is None or candidate < incumbent:
                    next_states[new_total] = candidate
        states = next_states

    positive_rows: list[tuple[int, Fraction, int, tuple[tuple[int, int], ...]]] = []
    for total, (right_side, cutoffs) in states.items():
        if total == 0:
            continue
        left_side = total * (total + 1) // 2
        slack = right_side - left_side
        choices = tuple(
            (epoch, cutoff)
            for (epoch, _), cutoff in zip(epoch_moduli, cutoffs)
            if cutoff
        )
        positive_rows.append((slack, Fraction(left_side, right_side), total, choices))

    minimum = min(positive_rows, key=lambda row: (row[0], row[2], row[3]))
    maximum = max(positive_rows, key=lambda row: (row[1], -row[2], row[3]))
    return RLPAudit(
        epoch_moduli=epoch_moduli,
        selection_vector_count=selection_vector_count - 1,
        reachable_positive_totals=len(positive_rows),
        transition_count=transition_count,
        minimum_slack=minimum[0],
        minimum_slack_choices=minimum[3],
        maximum_pressure=maximum[1],
        maximum_pressure_choices=maximum[3],
        violation_count=sum(row[0] < 0 for row in positive_rows),
    )


@dataclass(frozen=True)
class _TileSupport:
    epoch: int
    terminal: int
    modulus: int
    key: TileKey
    actual_count: int
    capacity: int
    exact_scalar_charge: Fraction
    exact_h_charge: Fraction
    scalar_upper_per_pair: Fraction
    h_upper_per_pair: Fraction


@dataclass(frozen=True)
class _LPBlockSolution:
    primal: Fraction
    dual: Fraction
    threshold: Fraction
    allocated: tuple[tuple[int, int], ...]


def _solve_one_capacity_block(
    rows: Sequence[_TileSupport], *, h_objective: bool
) -> _LPBlockSolution:
    if not rows:
        raise ValueError("at least one tile-support row is required")
    magnitude_capacity = rows[0].key[3]
    if any(row.key != rows[0].key for row in rows):
        raise ValueError("rows must belong to one common tile key")

    def coefficient(row: _TileSupport) -> Fraction:
        return row.h_upper_per_pair if h_objective else row.scalar_upper_per_pair

    ordered = sorted(rows, key=lambda row: (-coefficient(row), row.epoch))
    remaining = magnitude_capacity
    allocations: list[tuple[int, int]] = []
    primal = Fraction(0)
    marginal = Fraction(0)
    for row in ordered:
        amount = min(row.capacity, remaining)
        allocations.append((row.epoch, amount))
        if amount:
            marginal = coefficient(row)
            primal += amount * coefficient(row)
            remaining -= amount

    if sum(row.capacity for row in ordered) <= magnitude_capacity:
        threshold = Fraction(0)
    else:
        threshold = marginal
    dual = magnitude_capacity * threshold + sum(
        row.capacity * max(Fraction(0), coefficient(row) - threshold) for row in rows
    )
    if primal != dual:
        raise AssertionError("the exact tile primal and threshold dual disagree")
    return _LPBlockSolution(
        primal=primal,
        dual=dual,
        threshold=threshold,
        allocated=tuple(allocations),
    )


@dataclass(frozen=True)
class EpochObjectiveAudit:
    epoch: int
    terminal_mark_count: int
    nonadjacent_genuine_pair_count: int
    tile_support_count: int
    exact_retained_cross_ratio_lower_objective: Fraction
    exact_h_objective: Fraction


@dataclass(frozen=True)
class LaminarTileLPAudit:
    name: str
    supplied_mark_count: int
    audited_terminal_mark_count: int
    points_sha256: str
    epoch_count: int
    nonadjacent_genuine_pair_count: int
    tile_key_count: int
    support_variable_count: int
    exact_retained_cross_ratio_lower_objective: Fraction
    exact_h_objective: Fraction
    scalar_tile_lp_primal: Fraction
    scalar_tile_lp_dual: Fraction
    tile_lp_primal: Fraction
    tile_lp_dual: Fraction
    h_lp_to_actual_ratio: Fraction
    scalar_lp_to_actual_ratio: Fraction
    actual_count_capacity_violations: int
    global_magnitude_capacity_violations: int
    primal_dual_mismatches: int
    epoch_rows: tuple[EpochObjectiveAudit, ...]


def _tile_support_rows(
    marks: tuple[int, ...], *, max_terminal_mark_count: int | None
) -> tuple[_TileSupport, ...]:
    accumulators: dict[tuple[int, TileKey], list[int | Fraction]] = defaultdict(
        lambda: [0, Fraction(0), Fraction(0)]
    )
    prefix_data: dict[int, tuple[int, tuple[int, ...], dict[int, int]]] = {}

    for epoch in _dyadic_epochs(marks, max_terminal_mark_count):
        terminal = 2 * epoch
        prefix = marks[:terminal]
        gaps = _gap_weights(prefix)
        modulus = prefix[-1] + 1
        gap_band_counts: defaultdict[int, int] = defaultdict(int)
        for gap in gaps[1:]:
            gap_band_counts[_floor_power_of_two(gap)] += 1
        prefix_data[epoch] = (modulus, gaps, dict(gap_band_counts))

        for right in range(epoch, terminal):
            for left in range(1, right - 1):
                rank_gap = right - left
                difference = prefix[right] - prefix[left - 1]
                key = (
                    _floor_power_of_two(rank_gap),
                    _floor_power_of_two(gaps[left]),
                    _floor_power_of_two(gaps[right]),
                    _floor_power_of_two(difference),
                )
                row = accumulators[epoch, key]
                row[0] += 1
                row[1] += Fraction(
                    gaps[left] * gaps[right] * rank_gap * rank_gap,
                    modulus * modulus * terminal * terminal,
                )
                row[2] += Fraction(
                    gaps[left] * gaps[right], modulus * modulus
                ) * _fixed_h_kernel(left, right, terminal)

    supports: list[_TileSupport] = []
    for (epoch, key), values in sorted(accumulators.items()):
        terminal = 2 * epoch
        modulus, _, gap_band_counts = prefix_data[epoch]
        rank_band, left_band, right_band, magnitude_band = key
        capacity = min(
            gap_band_counts[left_band] * gap_band_counts[right_band],
            magnitude_band,
            2 * rank_band * rank_band * modulus // magnitude_band,
        )
        product_bound = min(4 * left_band * right_band, magnitude_band**2)
        scalar_upper = Fraction(
            4 * rank_band * rank_band * product_bound,
            terminal * terminal * modulus * modulus,
        )
        h_upper = Fraction(36, 35) * scalar_upper
        supports.append(
            _TileSupport(
                epoch=epoch,
                terminal=terminal,
                modulus=modulus,
                key=key,
                actual_count=int(values[0]),
                capacity=capacity,
                exact_scalar_charge=values[1],
                exact_h_charge=values[2],
                scalar_upper_per_pair=scalar_upper,
                h_upper_per_pair=h_upper,
            )
        )
    return tuple(supports)


def audit_laminar_tile_lp(
    name: str,
    points: Sequence[int],
    *,
    max_terminal_mark_count: int | None = None,
) -> LaminarTileLPAudit:
    """Solve the support-conditioned Wave 9 tile LP and its exact dual."""
    marks = _validated_golomb(points)
    supports = _tile_support_rows(
        marks, max_terminal_mark_count=max_terminal_mark_count
    )
    grouped: defaultdict[TileKey, list[_TileSupport]] = defaultdict(list)
    for row in supports:
        grouped[row.key].append(row)

    h_solutions = {
        key: _solve_one_capacity_block(rows, h_objective=True)
        for key, rows in grouped.items()
    }
    scalar_solutions = {
        key: _solve_one_capacity_block(rows, h_objective=False)
        for key, rows in grouped.items()
    }
    exact_scalar = sum((row.exact_scalar_charge for row in supports), Fraction(0))
    exact_h = sum((row.exact_h_charge for row in supports), Fraction(0))
    h_primal = sum((row.primal for row in h_solutions.values()), Fraction(0))
    h_dual = sum((row.dual for row in h_solutions.values()), Fraction(0))
    scalar_primal = sum((row.primal for row in scalar_solutions.values()), Fraction(0))
    scalar_dual = sum((row.dual for row in scalar_solutions.values()), Fraction(0))

    count_violations = sum(row.actual_count > row.capacity for row in supports)
    global_violations = sum(
        sum(row.actual_count for row in rows) > key[3] for key, rows in grouped.items()
    )
    envelope_violations = sum(
        row.exact_h_charge > row.actual_count * row.h_upper_per_pair
        or row.exact_scalar_charge > row.actual_count * row.scalar_upper_per_pair
        for row in supports
    )
    if envelope_violations:
        raise AssertionError("an exact observed tile exceeded its analytic envelope")

    epochs = _dyadic_epochs(marks, max_terminal_mark_count)
    audited_terminal = 2 * epochs[-1]
    epoch_rows = tuple(
        EpochObjectiveAudit(
            epoch=epoch,
            terminal_mark_count=2 * epoch,
            nonadjacent_genuine_pair_count=sum(
                row.actual_count for row in supports if row.epoch == epoch
            ),
            tile_support_count=sum(row.epoch == epoch for row in supports),
            exact_retained_cross_ratio_lower_objective=sum(
                (row.exact_scalar_charge for row in supports if row.epoch == epoch),
                Fraction(0),
            ),
            exact_h_objective=sum(
                (row.exact_h_charge for row in supports if row.epoch == epoch),
                Fraction(0),
            ),
        )
        for epoch in epochs
    )
    return LaminarTileLPAudit(
        name=name,
        supplied_mark_count=len(marks),
        audited_terminal_mark_count=audited_terminal,
        points_sha256=_points_sha256(marks),
        epoch_count=len(epochs),
        nonadjacent_genuine_pair_count=sum(row.actual_count for row in supports),
        tile_key_count=len(grouped),
        support_variable_count=len(supports),
        exact_retained_cross_ratio_lower_objective=exact_scalar,
        exact_h_objective=exact_h,
        scalar_tile_lp_primal=scalar_primal,
        scalar_tile_lp_dual=scalar_dual,
        tile_lp_primal=h_primal,
        tile_lp_dual=h_dual,
        h_lp_to_actual_ratio=h_primal / exact_h,
        scalar_lp_to_actual_ratio=scalar_primal / exact_scalar,
        actual_count_capacity_violations=count_violations,
        global_magnitude_capacity_violations=global_violations,
        primal_dual_mismatches=sum(
            solution.primal != solution.dual
            for solution in (*h_solutions.values(), *scalar_solutions.values())
        ),
        epoch_rows=epoch_rows,
    )


@dataclass(frozen=True)
class ScaleSlackRow:
    scale: int
    all_prefix_c1: bool
    minimum_rlp_slack: int
    maximum_rlp_pressure: Fraction
    retained_cross_ratio_lower_objective: Fraction
    exact_h_objective: Fraction


def scale_slack_no_go(
    points: Sequence[int], *, scales: Sequence[int]
) -> tuple[ScaleSlackRow, ...]:
    """Audit the monotonic common-dilation obstruction on one finite ruler."""
    marks = _validated_golomb(points)
    if not scales or any(not isinstance(scale, int) or scale < 1 for scale in scales):
        raise ValueError("scales must be a nonempty sequence of positive integers")
    rows: list[ScaleSlackRow] = []
    for scale in scales:
        scaled = tuple(scale * mark for mark in marks)
        rlp = audit_rlp_all_subsets(scaled)
        tile = audit_laminar_tile_lp(f"scale_{scale}", scaled)
        rows.append(
            ScaleSlackRow(
                scale=scale,
                all_prefix_c1=all(
                    scaled[count - 1] + 1 <= critical_modulus_cap(count)
                    for count in range(2, len(scaled) + 1)
                ),
                minimum_rlp_slack=rlp.minimum_slack,
                maximum_rlp_pressure=rlp.maximum_pressure,
                retained_cross_ratio_lower_objective=(
                    tile.exact_retained_cross_ratio_lower_objective
                ),
                exact_h_objective=tile.exact_h_objective,
            )
        )
    return tuple(rows)


def _file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _encode(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if hasattr(value, "__dataclass_fields__"):
        return _encode(asdict(value))
    if isinstance(value, tuple | list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _encode(item) for key, item in value.items()}
    return value


def build_certificate(
    source_certificate: str | Path = DEFAULT_SOURCE_CERTIFICATE,
) -> dict[str, Any]:
    """Build the byte-stable finite Wave 10 certificate."""
    source_path = Path(source_certificate).resolve()
    fixtures = load_authenticated_wave6_fixtures(source_path)
    selected = (
        ("perfect_four", PERFECT_FOUR, None),
        ("wave6_authenticated_64_0", fixtures.sixty_four_mark_points[0], None),
        (
            "wave6_authenticated_128",
            fixtures.one_hundred_twenty_eight_mark_points,
            None,
        ),
        ("wave7_erdos_turan_512_p1423", erdos_turan_ruler(512, 1423), 512),
    )
    fixture_rows = []
    for name, points, tile_limit in selected:
        tile = audit_laminar_tile_lp(
            name,
            points,
            max_terminal_mark_count=tile_limit,
        )
        # The all-subset DP is deliberately capped at 128 marks on the large
        # finite ET window.  Every legal selection in that horizon is still
        # checked; the 512-mark tile LP itself uses the full fixture.
        rlp_limit = 128 if len(points) > 128 else None
        rlp = audit_rlp_all_subsets(points, max_terminal_mark_count=rlp_limit)
        fixture_rows.append(
            {
                "name": name,
                "tile_lp": tile,
                "rlp_all_subsets": rlp,
                "rlp_audited_terminal_mark_count": (
                    min(len(points), 128) if len(points) > 128 else len(points)
                ),
            }
        )

    dilation = scale_slack_no_go(PERFECT_FOUR, scales=(1, 2, 3, 4))
    payload: dict[str, Any] = {
        "schema": "wave10_laminar_lp_probe_v1",
        "research_date": "2026-08-29",
        "purpose": (
            "exact all-subset W9-RLP dynamic programming, exact primal-dual "
            "Wave 9 tile relaxation, and finite no-go calibration for the "
            "retained cross-ratio/rank-variance objective"
        ),
        "source_authentication": {
            "wave6_arithmetic_certificate": source_path.name,
            "wave6_arithmetic_certificate_file_sha256": _file_sha256(source_path),
            "wave10_source_sha256": _file_sha256(Path(__file__).resolve()),
            "dependency_sha256": {
                name: _file_sha256(DIRECTORY / name)
                for name in (
                    "complete_birth_ledger.py",
                    "wave7_band_renewal_probe.py",
                )
            },
        },
        "mathematical_contract": {
            "rlp_scope": (
                "q_m in {0,...,m} at every audited dyadic epoch; zero means "
                "the epoch is omitted, so all nonempty epoch subsets and all "
                "positive cutoffs are covered"
            ),
            "tile_primal": (
                "max sum w_(m,t)x_(m,t), 0<=x_(m,t)<=c_(m,t), sum_m x_(m,t)<=Z_t"
            ),
            "tile_dual": (
                "min sum_t (Z_t lambda_t + sum_m c_(m,t)mu_(m,t)), "
                "lambda_t+mu_(m,t)>=w_(m,t), lambda_t,mu_(m,t)>=0"
            ),
            "exact_objective": (
                "sum h_i h_j ((j-i)/L)^2/N_L^2 over genuine nonadjacent "
                "birth pairs; this is the exact rational lower component of "
                "the retained cross-ratio potential"
            ),
            "zero_column_fact": (
                "after prefix moduli are fixed, W9-RLP contains no tile "
                "variable x_(m,t), so adjoining every audited W9-RLP row does "
                "not change the tile primal or its exact dual"
            ),
        },
        "fixture_audits": fixture_rows,
        "common_dilation_no_go": dilation,
        "candidate_verdicts": {
            "RLP_TILE_COUPLING": {
                "candidate": (
                    "adjoining W9-RLP for all epoch subsets and cutoffs directly "
                    "lowers the Wave 9 tile LP objective"
                ),
                "verdict": "NO_COUPLING_IN_THE_TESTED_RELAXATION",
                "reason": (
                    "all W9-RLP rows have zero coefficients in every tile "
                    "occupancy variable once the prefix moduli are fixed"
                ),
            },
            "RLP_SLACK_DAMPING": {
                "candidate": (
                    "larger raw W9-RLP slack by itself forces a smaller retained "
                    "cross-ratio/rank-variance objective"
                ),
                "verdict": "REFUTED_BY_EXACT_COMMON_DILATION_PATTERN",
                "scope": "perfect four-mark ruler at integer scales 1,2,3,4",
            },
            "TILE_LP_SUBLOG": {
                "candidate": (
                    "the present tile capacities plus global magnitude capacity "
                    "already yield a sublogarithmic cumulative objective"
                ),
                "verdict": "NOT_ESTABLISHED",
                "reason": (
                    "the exact support-conditioned dual has no cross-tile or "
                    "survival variable; finite optima remain much larger than "
                    "the realized exact objective"
                ),
            },
        },
        "conclusions": {
            "finite_computation_only": True,
            "infinite_survival_inferred": False,
            "p15_proved": False,
            "erdos_1191_resolved": False,
            "next_required_constraint": (
                "a nonzero coupling between survival-conditioned endpoint "
                "products or primitive Abel state and the hereditary RLP rows"
            ),
        },
    }
    encoded = _encode(payload)
    canonical = json.dumps(encoded, sort_keys=True, separators=(",", ":"))
    encoded["certificate_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-certificate", type=Path, default=DEFAULT_SOURCE_CERTIFICATE
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DIRECTORY / "wave10_laminar_lp_certificate_2026-08-29.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.source_certificate)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(arguments.output)
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()

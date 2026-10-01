#!/usr/bin/env python3
"""Exact nonnegative epochwise-owned cross-scale LP certificate."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from typing import Mapping

import ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate as base
import direct_b_membership_sddm_lp_certificate as membership


SCHEMA = "erdos1191.route_c_epochwise_owned_cross_scale_lp.v1"
STATUS = "EXACT_FIXED_14_CHANNEL_TWO_DEMAND_EPOCHWISE_NO_SAVING_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_EPOCHWISE_OWNED_CROSS_SCALE_LP_certificate.json"

SMALL_PRIMAL = {(0, 2): F(1, 40), (2, 4): F(1, 40)}
SMALL_DUAL = {
    (525, 616): F(698, 5),
    (636, 709): F(1426, 15),
    (749, 816): F(418, 5),
    (836, 864): F(2186, 15),
}
LARGE_PRIMAL = {
    (5, 6): F(13, 512),
    (5, 7): F(131, 2560),
    (11, 13): F(131, 2560),
    (12, 13): F(13, 512),
}
LARGE_DUAL = {
    (1596, 1664): F(933, 10),
    (1664, 1725): F(351, 2),
    (2349, 2396): F(381, 2),
    (2396, 2464): F(1263, 10),
}
ROW_SPLIT_SMALL_DUAL = {
    (525, 616): F(1934, 15),
    (636, 709): F(1586, 15),
    (749, 816): F(1894, 15),
    (836, 864): F(1546, 15),
}
ROW_SPLIT_LARGE_DUAL = LARGE_DUAL
ROW_SPLIT_PRIMAL = {**SMALL_PRIMAL, **LARGE_PRIMAL}


class CertificateError(RuntimeError):
    """Raised when exact replay, integrity, or scope validation fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def _owned_epoch_audit(
    cells: list[dict[str, object]],
    pairs: tuple[tuple[int, int], ...],
    columns: dict[tuple[int, int], tuple[F, ...]],
    costs: dict[tuple[int, int], F],
    demand_key: str,
    primal: dict[tuple[int, int], F],
    dual: dict[tuple[int, int], F],
    owner: str,
) -> dict[str, object]:
    owned_cells = [dict(cell, demand=F(cell[demand_key])) for cell in cells]
    audit = base._verify_lp(owned_cells, pairs, columns, costs, primal, dual)
    cross_pairs = tuple(pair for pair in pairs if pair[0] < 5 <= pair[1])
    cross_margins = {
        pair: costs[pair] - audit["loads"][pair] for pair in cross_pairs
    }
    foreign_pairs = tuple(
        pair
        for pair in pairs
        if (owner == "small" and pair[0] >= 5)
        or (owner == "large" and pair[1] < 5)
    )
    foreign_margins = {
        pair: costs[pair] - audit["loads"][pair] for pair in foreign_pairs
    }
    minimum_cross_pair, minimum_cross_margin = min(
        cross_margins.items(), key=lambda item: item[1]
    )
    minimum_foreign_pair, minimum_foreign_margin = min(
        foreign_margins.items(), key=lambda item: item[1]
    )
    return {
        "objective": F(audit["objective"]),
        "positive_cross_count": sum(
            primal.get(pair, F(0)) > 0 for pair in cross_pairs
        ),
        "minimum_cross_pair": minimum_cross_pair,
        "minimum_cross_margin": minimum_cross_margin,
        "minimum_foreign_pair": minimum_foreign_pair,
        "minimum_foreign_margin": minimum_foreign_margin,
    }


def _coordinate_row_split_audit(
    cells: list[dict[str, object]],
    pairs: tuple[tuple[int, int], ...],
    physical_columns: dict[tuple[int, int], tuple[F, ...]],
    costs: dict[tuple[int, int], F],
) -> dict[str, object]:
    small_columns: dict[tuple[int, int], tuple[F, ...]] = {}
    large_columns: dict[tuple[int, int], tuple[F, ...]] = {}
    negative_cross_entries: list[tuple[tuple[int, int], str, str, F, F]] = []
    for pair in pairs:
        i, j = pair
        small_values: list[F] = []
        large_values: list[F] = []
        for cell in cells:
            state = cell["state"]
            if j < 5:
                small_share = (state[i] - state[j]) ** 2
                large_share = F(0)
            elif i >= 5:
                small_share = F(0)
                large_share = (state[i] - state[j]) ** 2
            else:
                small_share = state[i] * (state[i] - state[j])
                large_share = state[j] * (state[j] - state[i])
                if small_share < 0:
                    negative_cross_entries.append(
                        (pair, str(cell["id"]), "small", small_share, large_share)
                    )
                if large_share < 0:
                    negative_cross_entries.append(
                        (pair, str(cell["id"]), "large", small_share, large_share)
                    )
            if small_share + large_share != physical_columns[pair][len(small_values)]:
                raise AssertionError("coordinate-row shares do not recover root square")
            small_values.append(small_share)
            large_values.append(large_share)
        small_columns[pair] = tuple(small_values)
        large_columns[pair] = tuple(large_values)

    small_slacks: list[F] = []
    large_slacks: list[F] = []
    for row_index, cell in enumerate(cells):
        small_correction = sum(
            (
                weight * small_columns[pair][row_index]
                for pair, weight in ROW_SPLIT_PRIMAL.items()
            ),
            F(0),
        )
        large_correction = sum(
            (
                weight * large_columns[pair][row_index]
                for pair, weight in ROW_SPLIT_PRIMAL.items()
            ),
            F(0),
        )
        small_slack = small_correction - F(cell["small_demand"])
        large_slack = large_correction - F(cell["large_demand"])
        if small_slack < 0 or large_slack < 0:
            raise AssertionError(f"coordinate-row primal violation at {cell['id']}")
        small_slacks.append(small_slack)
        large_slacks.append(large_slack)

    loads = {
        pair: sum(
            (
                ROW_SPLIT_SMALL_DUAL.get(
                    (int(cell["left"]), int(cell["right"])), F(0)
                )
                * small_columns[pair][row_index]
                + ROW_SPLIT_LARGE_DUAL.get(
                    (int(cell["left"]), int(cell["right"])), F(0)
                )
                * large_columns[pair][row_index]
                for row_index, cell in enumerate(cells)
            ),
            F(0),
        )
        for pair in pairs
    }
    if any(loads[pair] > costs[pair] for pair in pairs):
        raise AssertionError("coordinate-row dual root constraint violation")

    primal_objective = sum(
        (weight * costs[pair] for pair, weight in ROW_SPLIT_PRIMAL.items()), F(0)
    )
    dual_objective = sum(
        (
            ROW_SPLIT_SMALL_DUAL.get(
                (int(cell["left"]), int(cell["right"])), F(0)
            )
            * F(cell["small_demand"])
            + ROW_SPLIT_LARGE_DUAL.get(
                (int(cell["left"]), int(cell["right"])), F(0)
            )
            * F(cell["large_demand"])
            for cell in cells
        ),
        F(0),
    )
    if primal_objective != dual_objective:
        raise AssertionError("coordinate-row primal-dual gap is nonzero")
    if any(
        weight > 0 and loads[pair] != costs[pair]
        for pair, weight in ROW_SPLIT_PRIMAL.items()
    ):
        raise AssertionError("coordinate-row complementary slackness failed")
    for row_index, cell in enumerate(cells):
        key = (int(cell["left"]), int(cell["right"]))
        if ROW_SPLIT_SMALL_DUAL.get(key, F(0)) and small_slacks[row_index] != 0:
            raise AssertionError("positive small dual row is not tight")
        if ROW_SPLIT_LARGE_DUAL.get(key, F(0)) and large_slacks[row_index] != 0:
            raise AssertionError("positive large dual row is not tight")

    cross_pairs = tuple(pair for pair in pairs if pair[0] < 5 <= pair[1])
    cross_margins = {pair: costs[pair] - loads[pair] for pair in cross_pairs}
    minimum_cross_pair, minimum_cross_margin = min(
        cross_margins.items(), key=lambda item: item[1]
    )
    if minimum_cross_margin <= 0:
        raise AssertionError("coordinate-row dual does not strictly exclude cross roots")

    aggregate_margins: dict[str, str] = {}
    for label, (small_support, large_support) in {
        "J4": (tuple(range(5)), ()),
        "J8": ((), tuple(range(5, 14))),
        "J_all": (tuple(range(5)), tuple(range(5, 14))),
    }.items():
        small_share_values: list[F] = []
        large_share_values: list[F] = []
        for cell in cells:
            small_sum = sum(cell["state"][index] for index in small_support)
            large_sum = sum(cell["state"][index] for index in large_support)
            total_sum = small_sum + large_sum
            small_share_values.append(small_sum * total_sum)
            large_share_values.append(large_sum * total_sum)
        physical_cost = sum(
            (
                F(cell["length"]) * (small_share + large_share)
                for cell, small_share, large_share in zip(
                    cells, small_share_values, large_share_values
                )
            ),
            F(0),
        )
        dual_load = sum(
            (
                ROW_SPLIT_SMALL_DUAL.get(
                    (int(cell["left"]), int(cell["right"])), F(0)
                )
                * small_share
                + ROW_SPLIT_LARGE_DUAL.get(
                    (int(cell["left"]), int(cell["right"])), F(0)
                )
                * large_share
                for cell, small_share, large_share in zip(
                    cells, small_share_values, large_share_values
                )
            ),
            F(0),
        )
        margin = physical_cost - dual_load
        if margin <= 0:
            raise AssertionError(f"coordinate-row aggregate {label} is not inactive")
        aggregate_margins[label] = ftext(margin)

    example_pair = (3, 5)
    example_index, example_cell = next(
        (index, cell)
        for index, cell in enumerate(cells)
        if cell["id"] == "[749,816)"
    )
    return {
        "small_share_formula": "z_i*(z_i-z_j)",
        "large_share_formula": "z_j*(z_j-z_i)",
        "pointwise_share_sum_equals_physical_root_square": True,
        "signed_negative_cross_cell_entry_count": len(negative_cross_entries),
        "signed_example": {
            "root": "3,5",
            "cell": str(example_cell["id"]),
            "small_share": ftext(small_columns[example_pair][example_index]),
            "large_share": ftext(large_columns[example_pair][example_index]),
            "physical_sum": ftext(physical_columns[example_pair][example_index]),
        },
        "optimal_physical_price": ftext(primal_objective),
        "primal_dual_gap": ftext(primal_objective - dual_objective),
        "positive_cross_scale_root_count": sum(
            ROW_SPLIT_PRIMAL.get(pair, F(0)) > 0 for pair in cross_pairs
        ),
        "minimum_cross_scale_root": (
            f"{minimum_cross_pair[0]},{minimum_cross_pair[1]}"
        ),
        "minimum_cross_scale_root_dual_margin": ftext(minimum_cross_margin),
        "primal_root_weights": {
            f"{pair[0]},{pair[1]}": ftext(weight)
            for pair, weight in sorted(ROW_SPLIT_PRIMAL.items())
        },
        "small_dual_cell_weights": {
            f"[{left},{right})": ftext(weight)
            for (left, right), weight in sorted(ROW_SPLIT_SMALL_DUAL.items())
        },
        "large_dual_cell_weights": {
            f"[{left},{right})": ftext(weight)
            for (left, right), weight in sorted(ROW_SPLIT_LARGE_DUAL.items())
        },
        "aggregate_dual_margins": aggregate_margins,
    }


def epochwise_owned_lp_audit() -> dict[str, object]:
    matrix4 = membership.point_m_matrix(4)
    matrix8 = membership.point_m_matrix(8)
    cells = base._finite_cells(base.CHANNELS, 5, matrix4, matrix8)
    for cell in cells:
        state = cell["state"]
        cell["small_demand"] = membership.quadratic(matrix4, state[:5])
        cell["large_demand"] = membership.quadratic(matrix8, state[5:])

    pairs, columns, costs = base._root_columns(cells, len(base.CHANNELS))
    base._verify_cost_formula(base.CHANNELS, costs)
    small = _owned_epoch_audit(
        cells,
        pairs,
        columns,
        costs,
        "small_demand",
        SMALL_PRIMAL,
        SMALL_DUAL,
        "small",
    )
    large = _owned_epoch_audit(
        cells,
        pairs,
        columns,
        costs,
        "large_demand",
        LARGE_PRIMAL,
        LARGE_DUAL,
        "large",
    )
    aggregate_supports = {
        "J4": tuple(range(5)),
        "J8": tuple(range(5, 14)),
        "J_all": tuple(range(14)),
    }
    aggregate_audit: dict[str, dict[str, dict[str, str]]] = {}
    for owner, dual in (("small_owner", SMALL_DUAL), ("large_owner", LARGE_DUAL)):
        owner_audit: dict[str, dict[str, str]] = {}
        for label, support in aggregate_supports.items():
            column = tuple(
                sum(cell["state"][index] for index in support) ** 2
                for cell in cells
            )
            physical_cost = sum(
                (
                    F(cell["length"]) * value
                    for cell, value in zip(cells, column)
                ),
                F(0),
            )
            dual_load = sum(
                (
                    dual.get((int(cell["left"]), int(cell["right"])), F(0))
                    * value
                    for cell, value in zip(cells, column)
                ),
                F(0),
            )
            margin = physical_cost - dual_load
            if margin <= 0:
                raise AssertionError(f"{owner} aggregate {label} is not strictly inactive")
            owner_audit[label] = {
                "coefficient": "0/1",
                "physical_cost": ftext(physical_cost),
                "dual_margin": ftext(margin),
            }
        aggregate_audit[owner] = owner_audit
    highlight_index, highlight_cell = next(
        (index, cell)
        for index, cell in enumerate(cells)
        if cell["id"] == "[749,816)"
    )
    legacy_small_correction = sum(
        (
            weight * columns[pair][highlight_index]
            for pair, weight in base.JOINT_PRIMAL.items()
            if pair[1] < 5
        ),
        F(0),
    )
    legacy_large_correction = sum(
        (
            weight * columns[pair][highlight_index]
            for pair, weight in base.JOINT_PRIMAL.items()
            if pair[0] >= 5
        ),
        F(0),
    )
    legacy_cross_correction = sum(
        (
            weight * columns[pair][highlight_index]
            for pair, weight in base.JOINT_PRIMAL.items()
            if pair[0] < 5 <= pair[1]
        ),
        F(0),
    )
    highlight_small_demand = F(highlight_cell["small_demand"])
    highlight_large_demand = F(highlight_cell["large_demand"])
    coordinate_row_split = _coordinate_row_split_audit(
        cells, pairs, columns, costs
    )
    total = F(small["objective"]) + F(large["objective"])
    weaker_sum_cover = F(base.cross_scale_lp_audit()["optimal_physical_price"])
    return {
        "common_cell_count": len(cells),
        "owned_demand_row_count": 2 * len(cells),
        "physical_root_identity_count": len(pairs),
        "owner_root_variable_count": 2 * len(pairs),
        "aggregate_column_identity_count": len(aggregate_supports),
        "owner_aggregate_variable_count": 2 * len(aggregate_supports),
        "total_nonnegative_owner_variable_count": 2
        * (len(pairs) + len(aggregate_supports)),
        "small_epoch_optimum": ftext(small["objective"]),
        "large_epoch_optimum": ftext(large["objective"]),
        "total_epochwise_owned_optimum": ftext(total),
        "saving_against_same_scale_separate_optima": "0/1",
        "gap_above_weaker_sum_cover_optimum": ftext(total - weaker_sum_cover),
        "positive_cross_scale_owner_variable_count": (
            int(small["positive_cross_count"]) + int(large["positive_cross_count"])
        ),
        "small_owner_minimum_cross_root_margin": ftext(
            small["minimum_cross_margin"]
        ),
        "large_owner_minimum_cross_root_margin": ftext(
            large["minimum_cross_margin"]
        ),
        "owned_aggregate_audit": aggregate_audit,
        "coordinate_row_split": coordinate_row_split,
        "legacy_sum_cover_highlight": {
            "cell": str(highlight_cell["id"]),
            "small_demand": ftext(highlight_small_demand),
            "small_owned_correction": ftext(legacy_small_correction),
            "small_owned_slack": ftext(
                legacy_small_correction - highlight_small_demand
            ),
            "large_demand": ftext(highlight_large_demand),
            "large_owned_correction": ftext(legacy_large_correction),
            "large_owned_slack": ftext(
                legacy_large_correction - highlight_large_demand
            ),
            "summed_slack": ftext(
                legacy_small_correction
                + legacy_large_correction
                + legacy_cross_correction
                - highlight_small_demand
                - highlight_large_demand
            ),
        },
        "small_owner": {
            "objective": ftext(small["objective"]),
            "primal_root_weights": {
                f"{pair[0]},{pair[1]}": ftext(weight)
                for pair, weight in sorted(SMALL_PRIMAL.items())
            },
            "dual_cell_weights": {
                f"[{left},{right})": ftext(weight)
                for (left, right), weight in sorted(SMALL_DUAL.items())
            },
            "minimum_cross_root": (
                f"{small['minimum_cross_pair'][0]},{small['minimum_cross_pair'][1]}"
            ),
            "minimum_cross_root_margin": ftext(small["minimum_cross_margin"]),
            "minimum_foreign_same_scale_root": (
                f"{small['minimum_foreign_pair'][0]},"
                f"{small['minimum_foreign_pair'][1]}"
            ),
            "minimum_foreign_same_scale_root_margin": ftext(
                small["minimum_foreign_margin"]
            ),
        },
        "large_owner": {
            "objective": ftext(large["objective"]),
            "primal_root_weights": {
                f"{pair[0]},{pair[1]}": ftext(weight)
                for pair, weight in sorted(LARGE_PRIMAL.items())
            },
            "dual_cell_weights": {
                f"[{left},{right})": ftext(weight)
                for (left, right), weight in sorted(LARGE_DUAL.items())
            },
            "minimum_cross_root": (
                f"{large['minimum_cross_pair'][0]},{large['minimum_cross_pair'][1]}"
            ),
            "minimum_cross_root_margin": ftext(large["minimum_cross_margin"]),
            "minimum_foreign_same_scale_root": (
                f"{large['minimum_foreign_pair'][0]},"
                f"{large['minimum_foreign_pair'][1]}"
            ),
            "minimum_foreign_same_scale_root_margin": ftext(
                large["minimum_foreign_margin"]
            ),
        },
    }


def build_certificate() -> dict[str, object]:
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "fixed_14_channel_two_demand_fixture_only": True,
            "nonnegative_global_partition_relaxation": True,
            "each_owner_copy_pays_full_physical_price": True,
            "one_physical_column_credited_twice_for_one_price": False,
            "canonical_signed_coordinate_row_split_audited": True,
            "arbitrary_signed_owned_splits_audited": False,
            "four_owner_26_channel_model_audited": False,
            "signed_cross_term_cancellation_payment_proved": False,
            "direct_M_Gothic_one_for_one_payment_proved": False,
            "birth_gate_final_terminal_ownership_proved": False,
            "active_current_to_past_payment_proved": False,
            "other_scale_ratios_or_histories_proved": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        },
        "epochwise_owned_lp": epochwise_owned_lp_audit(),
    }
    certificate["integrity"] = {
        "canonical_json": True,
        "payload_sha256": payload_hash(certificate),
    }
    return certificate


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    """Return the single canonical JSON representation accepted by the CLI."""
    return (
        json.dumps(
            certificate,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
        )
        + "\n"
    ).encode("utf-8")


def verify_certificate(certificate: Mapping[str, object]) -> None:
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping):
        raise CertificateError("missing integrity row")
    if integrity.get("canonical_json") is not True:
        raise CertificateError("canonical_json must be the boolean true")
    if integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if certificate != build_certificate():
        raise CertificateError("certificate differs from exact semantic replay")


def _rehash(certificate: dict[str, object]) -> None:
    certificate["integrity"]["payload_sha256"] = payload_hash(certificate)  # type: ignore[index]


def self_check(certificate: Mapping[str, object]) -> dict[str, int]:
    mutations: list[dict[str, object]] = []
    for path, value in (
        (("schema",), "wrong.schema"),
        (("status",), "C058_SOLVED"),
        (("scope", "canonical_signed_coordinate_row_split_audited"), False),
        (("scope", "arbitrary_signed_owned_splits_audited"), True),
        (("scope", "four_owner_26_channel_model_audited"), True),
        (("scope", "other_scale_ratios_or_histories_proved"), True),
        (("scope", "C058_Q1_Q2_proved"), True),
        (("epochwise_owned_lp", "total_epochwise_owned_optimum"), "0/1"),
        (
            (
                "epochwise_owned_lp",
                "coordinate_row_split",
                "signed_example",
                "large_share",
            ),
            "0/1",
        ),
        (
            (
                "epochwise_owned_lp",
                "owned_aggregate_audit",
                "small_owner",
                "J4",
                "physical_cost",
            ),
            "0/1",
        ),
        (("epochwise_owned_lp", "small_owner_minimum_cross_root_margin"), "0/1"),
        (
            (
                "epochwise_owned_lp",
                "large_owner",
                "primal_root_weights",
                "5,6",
            ),
            "0/1",
        ),
    ):
        changed = copy.deepcopy(certificate)
        target: object = changed
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]
        _rehash(changed)
        mutations.append(changed)

    rejected = 0
    for changed in mutations:
        try:
            verify_certificate(changed)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("a semantic mutation was accepted")
    return {"mutations_attempted": len(mutations), "mutations_rejected": rejected}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    arguments = parser.parse_args()

    try:
        if arguments.verify is not None:
            raw = arguments.verify.read_bytes()
            certificate = json.loads(raw.decode("utf-8"))
            if raw != rendered_bytes(certificate):
                raise CertificateError("certificate bytes are not canonical JSON")
            verify_certificate(certificate)
        else:
            certificate = build_certificate()

        if arguments.output is not None:
            arguments.output.write_bytes(rendered_bytes(certificate))
        elif arguments.verify is None:
            sys.stdout.buffer.write(rendered_bytes(certificate))

        machine_stdout = arguments.output is None and arguments.verify is None
        if not machine_stdout:
            print(
                "verified "
                f"payload_sha256={certificate['integrity']['payload_sha256']}"
            )
        if arguments.self_check:
            result = self_check(certificate)
            print(
                "self_check "
                f"mutations_attempted={result['mutations_attempted']} "
                f"mutations_rejected={result['mutations_rejected']}",
                file=sys.stderr if machine_stdout else sys.stdout,
            )
    except (CertificateError, OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

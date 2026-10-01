#!/usr/bin/env python3
"""Exact 14-channel cross-scale surplus LP certificate."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
from itertools import combinations
import json
from pathlib import Path
import sys
from typing import Mapping, Sequence

import direct_b_membership_sddm_lp_certificate as membership
import ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate as mixed


SCHEMA = "erdos1191.route_c_cross_scale_surplus_lp.v1"
STATUS = "EXACT_FIXED_14_CHANNEL_CROSS_SCALE_SURPLUS_LP_ONLY_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate.json"
POINTS = tuple(k * (k + 100) for k in range(16))
SMALL_WIDTH = 200
LARGE_WIDTH = 800

# A normalized channel is g_T(x-origin)/sqrt(2T).  At T=200 and S=800
# the square roots are the rational integers 20 and 40.
CHANNELS = tuple(
    [(f"T200:n4:b{k}", SMALL_WIDTH, point, 20) for k, point in enumerate(POINTS[3:8])]
    + [(f"S800:n8:b{k}", LARGE_WIDTH, point, 40) for k, point in enumerate(POINTS[7:16])]
)

JOINT_PRIMAL = {
    (0, 1): F(13, 30720),
    (0, 2): F(3971, 153600),
    (2, 4): F(191, 9600),
    (3, 4): F(13, 7680),
    (5, 6): F(49, 640),
    (6, 7): F(131, 2560),
    (11, 13): F(131, 2560),
    (12, 13): F(13, 512),
}

JOINT_DUAL = {
    (525, 616): F(698, 5),
    (636, 709): F(1426, 15),
    (749, 816): F(418, 5),
    (864, 925): F(2186, 15),
    (1596, 1664): F(3086, 45),
    (1664, 1725): F(2086, 15),
    (2349, 2396): F(381, 2),
    (2396, 2464): F(12743, 90),
}

SMALL_SEPARATE_PRIMAL = {(0, 2): F(1, 40), (2, 4): F(1, 40)}
SMALL_SEPARATE_DUAL = {
    (525, 616): F(698, 5),
    (636, 709): F(1426, 15),
    (749, 816): F(418, 5),
    (836, 925): F(2186, 15),
}
LARGE_SEPARATE_PRIMAL = {
    (0, 1): F(13, 512),
    (0, 2): F(131, 2560),
    (6, 8): F(131, 2560),
    (7, 8): F(13, 512),
}
LARGE_SEPARATE_DUAL = {
    (1596, 1664): F(933, 10),
    (1664, 1725): F(351, 2),
    (2349, 2396): F(381, 2),
    (2396, 2464): F(1263, 10),
}


class CertificateError(RuntimeError):
    """Raised when an exact witness, scope gate, or integrity replay fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def _haar_value(x: int, origin: int, width: int) -> int:
    displacement = x - origin
    if 0 <= displacement < width:
        return 1
    if width <= displacement < 2 * width:
        return -1
    return 0


def _finite_cells(
    channels: Sequence[tuple[str, int, int, int]],
    first_size: int,
    first_matrix: Sequence[Sequence[F]],
    second_matrix: Sequence[Sequence[F]] | None = None,
) -> list[dict[str, object]]:
    endpoints = sorted(
        {origin + shift for _, width, origin, _ in channels for shift in (0, width, 2 * width)}
    )
    rows: list[dict[str, object]] = []
    for left, right in zip(endpoints, endpoints[1:]):
        state = tuple(
            F(_haar_value(left, origin, width), normalizer)
            for _, width, origin, normalizer in channels
        )
        demand = membership.quadratic(first_matrix, state[:first_size])
        if second_matrix is not None:
            demand += membership.quadratic(second_matrix, state[first_size:])
        rows.append(
            {
                "id": f"[{left},{right})",
                "left": left,
                "right": right,
                "length": right - left,
                "state": state,
                "demand": demand,
            }
        )
    return rows


def _root_columns(
    cells: Sequence[Mapping[str, object]], size: int
) -> tuple[
    tuple[tuple[int, int], ...],
    dict[tuple[int, int], tuple[F, ...]],
    dict[tuple[int, int], F],
]:
    pairs = tuple(combinations(range(size), 2))
    columns = {
        pair: tuple((cell["state"][pair[0]] - cell["state"][pair[1]]) ** 2 for cell in cells)
        for pair in pairs
    }
    costs = {
        pair: sum(
            (F(cell["length"]) * value for cell, value in zip(cells, columns[pair])),
            F(0),
        )
        for pair in pairs
    }
    return pairs, columns, costs


def _verify_cost_formula(
    channels: Sequence[tuple[str, int, int, int]], costs: Mapping[tuple[int, int], F]
) -> None:
    for (i, j), cost in costs.items():
        _, width, origin, _ = channels[i]
        _, other_width, other_origin, _ = channels[j]
        square_root = 200 if width == other_width == 200 else 800 if width == other_width else 400
        expected = F(2) - mixed.mixed_haar_inner(width, other_width, other_origin - origin) / square_root
        if cost != expected:
            raise AssertionError(f"mixed root cost mismatch at {(i, j)}")


def _verify_lp(
    cells: Sequence[Mapping[str, object]],
    pairs: Sequence[tuple[int, int]],
    columns: Mapping[tuple[int, int], Sequence[F]],
    costs: Mapping[tuple[int, int], F],
    primal: Mapping[tuple[int, int], F],
    dual: Mapping[tuple[int, int], F],
) -> dict[str, object]:
    if any(pair not in costs or weight < 0 for pair, weight in primal.items()):
        raise AssertionError("invalid primal root")
    if any(value < 0 for value in dual.values()):
        raise AssertionError("negative dual multiplier")
    slacks: list[F] = []
    correction_values: list[F] = []
    for row_index, cell in enumerate(cells):
        correction = sum(
            (weight * columns[pair][row_index] for pair, weight in primal.items()), F(0)
        )
        slack = correction - F(cell["demand"])
        if slack < 0:
            raise AssertionError(f"primal cell violation at {cell['id']}")
        correction_values.append(correction)
        slacks.append(slack)

    loads = {
        pair: sum(
            (
                dual.get((int(cell["left"]), int(cell["right"])), F(0)) * value
                for cell, value in zip(cells, columns[pair])
            ),
            F(0),
        )
        for pair in pairs
    }
    if any(loads[pair] > costs[pair] for pair in pairs):
        raise AssertionError("dual root constraint violation")

    primal_objective = sum((weight * costs[pair] for pair, weight in primal.items()), F(0))
    dual_objective = sum(
        (
            dual.get((int(cell["left"]), int(cell["right"])), F(0)) * F(cell["demand"])
            for cell in cells
        ),
        F(0),
    )
    if primal_objective != dual_objective:
        raise AssertionError("nonzero exact primal-dual gap")
    if any(primal[pair] and loads[pair] != costs[pair] for pair in primal):
        raise AssertionError("positive root violates complementary slackness")
    for index, cell in enumerate(cells):
        key = (int(cell["left"]), int(cell["right"]))
        if dual.get(key, F(0)) and slacks[index] != 0:
            raise AssertionError("positive dual row violates complementary slackness")

    return {
        "objective": primal_objective,
        "dual_objective": dual_objective,
        "slacks": tuple(slacks),
        "correction_values": tuple(correction_values),
        "loads": loads,
    }


def _separate_audit(
    channels: Sequence[tuple[str, int, int, int]],
    matrix: Sequence[Sequence[F]],
    primal: Mapping[tuple[int, int], F],
    dual: Mapping[tuple[int, int], F],
) -> dict[str, object]:
    cells = _finite_cells(channels, len(channels), matrix)
    pairs, columns, costs = _root_columns(cells, len(channels))
    _verify_cost_formula(channels, costs)
    audit = _verify_lp(cells, pairs, columns, costs, primal, dual)
    demand = sum((F(cell["length"]) * F(cell["demand"]) for cell in cells), F(0))
    return {
        "optimal_physical_price": ftext(audit["objective"]),
        "integrated_signed_demand": ftext(demand),
        "surplus_over_demand": ftext(audit["objective"] - demand),
        "positive_length_cell_count": len(cells),
    }


def cross_scale_lp_audit() -> dict[str, object]:
    matrix4 = membership.point_m_matrix(4)
    matrix8 = membership.point_m_matrix(8)
    cells = _finite_cells(CHANNELS, 5, matrix4, matrix8)
    pairs, columns, costs = _root_columns(cells, len(CHANNELS))
    _verify_cost_formula(CHANNELS, costs)
    audit = _verify_lp(cells, pairs, columns, costs, JOINT_PRIMAL, JOINT_DUAL)

    demand = sum((F(cell["length"]) * F(cell["demand"]) for cell in cells), F(0))
    small = _separate_audit(
        CHANNELS[:5], matrix4, SMALL_SEPARATE_PRIMAL, SMALL_SEPARATE_DUAL
    )
    large = _separate_audit(
        CHANNELS[5:], matrix8, LARGE_SEPARATE_PRIMAL, LARGE_SEPARATE_DUAL
    )
    separate_sum = F(small["optimal_physical_price"]) + F(large["optimal_physical_price"])
    cross_pairs = tuple(pair for pair in pairs if pair[0] < 5 <= pair[1])
    cross_margins = {pair: costs[pair] - audit["loads"][pair] for pair in cross_pairs}
    if any(margin <= 0 for margin in cross_margins.values()):
        raise AssertionError("cross-scale roots are not strictly excluded by the dual")
    objective = F(audit["objective"])
    aggregate_supports = {
        "J4": tuple(range(5)),
        "J8": tuple(range(5, 14)),
        "J_all": tuple(range(14)),
    }
    aggregate_audit: dict[str, object] = {}
    for label, support in aggregate_supports.items():
        column = tuple(sum(cell["state"][index] for index in support) ** 2 for cell in cells)
        physical_cost = sum(
            (F(cell["length"]) * value for cell, value in zip(cells, column)), F(0)
        )
        dual_load = sum(
            (
                JOINT_DUAL.get((int(cell["left"]), int(cell["right"])), F(0)) * value
                for cell, value in zip(cells, column)
            ),
            F(0),
        )
        if dual_load >= physical_cost:
            raise AssertionError(f"aggregate column {label} is not strictly inactive")
        aggregate_audit[label] = {
            "support": list(support),
            "coefficient": "0/1",
            "physical_cost": ftext(physical_cost),
            "dual_load": ftext(dual_load),
            "dual_margin": ftext(physical_cost - dual_load),
        }
    root_audit = {
        f"{pair[0]},{pair[1]}": {
            "kind": "cross_scale" if pair in cross_pairs else "within_scale",
            "physical_cost": ftext(costs[pair]),
            "dual_load": ftext(audit["loads"][pair]),
            "dual_margin": ftext(costs[pair] - audit["loads"][pair]),
        }
        for pair in pairs
    }
    cell_audit: dict[str, object] = {}
    for row_index, cell in enumerate(cells):
        state = cell["state"]
        small_demand = membership.quadratic(matrix4, state[:5])
        large_demand = membership.quadratic(matrix8, state[5:])
        small_correction = sum(
            (
                weight * columns[pair][row_index]
                for pair, weight in JOINT_PRIMAL.items()
                if pair[1] < 5
            ),
            F(0),
        )
        large_correction = sum(
            (
                weight * columns[pair][row_index]
                for pair, weight in JOINT_PRIMAL.items()
                if pair[0] >= 5
            ),
            F(0),
        )
        cross_correction = sum(
            (
                weight * columns[pair][row_index]
                for pair, weight in JOINT_PRIMAL.items()
                if pair[0] < 5 <= pair[1]
            ),
            F(0),
        )
        cell_audit[str(cell["id"])] = {
            "length": int(cell["length"]),
            "n4_T200_demand": ftext(small_demand),
            "n8_S800_demand": ftext(large_demand),
            "n4_T200_root_correction": ftext(small_correction),
            "n8_S800_root_correction": ftext(large_correction),
            "cross_scale_root_correction": ftext(cross_correction),
            "total_slack": ftext(audit["slacks"][row_index]),
        }

    return {
        "channel_count": len(CHANNELS),
        "root_count": len(pairs),
        "cross_scale_root_count": len(cross_pairs),
        "positive_length_cell_count": len(cells),
        "event_count": len(cells) + 1,
        "complete_real_line_cell_count": len(cells) + 2,
        "integrated_signed_demand": ftext(demand),
        "optimal_physical_price": ftext(objective),
        "surplus_over_demand": ftext(objective - demand),
        "sum_of_separate_optima": ftext(separate_sum),
        "strict_sharing_saving": ftext(separate_sum - objective),
        "primal_dual_gap": ftext(objective - F(audit["dual_objective"])),
        "positive_cross_scale_root_count": sum(
            JOINT_PRIMAL.get(pair, F(0)) > 0 for pair in cross_pairs
        ),
        "minimum_cross_scale_root_dual_margin": ftext(min(cross_margins.values())),
        "aggregate_J_channels_included": True,
        "aggregate_J_audit": aggregate_audit,
        "channels": [
            {
                "index": index,
                "label": label,
                "width": width,
                "origin": origin,
                "sqrt_2_width": normalizer,
            }
            for index, (label, width, origin, normalizer) in enumerate(CHANNELS)
        ],
        "primal": {
            "positive_root_count": len(JOINT_PRIMAL),
            "root_weights": {
                f"{pair[0]},{pair[1]}": ftext(weight)
                for pair, weight in sorted(JOINT_PRIMAL.items())
            },
        },
        "dual": {
            "positive_cell_count": len(JOINT_DUAL),
            "cell_weights": {
                f"[{left},{right})": ftext(value)
                for (left, right), value in sorted(JOINT_DUAL.items())
            },
        },
        "root_audit": root_audit,
        "cell_audit": cell_audit,
        "separate_audits": {"n4_T200": small, "n8_S800": large},
    }


def build_certificate() -> dict[str, object]:
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "fixed_finite_14_channel_fixture_only": True,
            "common_cell_sum_cover_is_weaker_than_epochwise_cover": True,
            "separate_epochwise_cover_proved": False,
            "strict_saving_over_sum_of_separate_optima": True,
            "positive_cross_scale_root_needed_or_helpful": False,
            "demand_equality_achieved": False,
            "continuum_phase_or_common_history_ledger_proved": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        },
        "cross_scale_lp": cross_scale_lp_audit(),
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
    return (
        json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def verify_certificate(certificate: Mapping[str, object]) -> None:
    expected = build_certificate()
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping):
        raise CertificateError("missing integrity row")
    if integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    if certificate != expected:
        raise CertificateError("certificate differs from exact semantic replay")


def _rehash(certificate: dict[str, object]) -> None:
    certificate["integrity"]["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> dict[str, int]:
    mutations: list[dict[str, object]] = []

    for path, value in (
        (("schema",), "wrong.schema"),
        (("status",), "C058_SOLVED"),
        (("scope", "common_cell_sum_cover_is_weaker_than_epochwise_cover"), False),
        (("scope", "C058_Q1_Q2_proved"), True),
        (("cross_scale_lp", "optimal_physical_price"), "173/1024"),
        (("cross_scale_lp", "integrated_signed_demand"), "0/1"),
        (("cross_scale_lp", "strict_sharing_saving"), "0/1"),
        (("cross_scale_lp", "positive_cross_scale_root_count"), 1),
        (("cross_scale_lp", "minimum_cross_scale_root_dual_margin"), "0/1"),
        (("cross_scale_lp", "primal", "root_weights", "0,2"), "0/1"),
        (("cross_scale_lp", "dual", "cell_weights", "[2396,2464)"), "0/1"),
        (("cross_scale_lp", "aggregate_J_audit", "J4", "physical_cost"), "0/1"),
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


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.verify is not None:
            raw = args.verify.read_bytes()
            certificate = json.loads(raw.decode("utf-8"))
            verify_certificate(certificate)
            if raw != rendered_bytes(certificate):
                raise CertificateError("certificate bytes are not canonical")
        else:
            certificate = build_certificate()

        output = args.output
        if output is None and args.verify is None:
            output = DEFAULT_CERTIFICATE
        if output is not None:
            output.write_bytes(rendered_bytes(certificate))

        result = self_check(certificate) if args.self_check else None
        message = f"payload_sha256={payload_hash(certificate)}"
        if result is not None:
            message += (
                f" mutations_attempted={result['mutations_attempted']}"
                f" mutations_rejected={result['mutations_rejected']}"
            )
        print(message)
        return 0
    except (CertificateError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

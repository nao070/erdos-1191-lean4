#!/usr/bin/env python3
"""Exact certificate for the 26-channel, four-owner cross-scale root LP."""

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

import ROUTE_C_CROSS_SCALE_SURPLUS_LP_certificate as base
import ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate as mixed
import direct_b_membership_sddm_lp_certificate as membership


SCHEMA = "erdos1191.route_c_four_owner_cross_scale_lp.v1"
STATUS = "EXACT_FIXED_FOUR_OWNER_CROSS_SCALE_ROOTS_STRICTLY_EXCLUDED_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_FOUR_OWNER_CROSS_SCALE_LP_certificate.json"
POINTS = tuple(k * (k + 100) for k in range(16))

# The n=4 and n=8 owners at a fixed width share the physical channel based at
# a_7.  Physical channels, rather than owner occurrences, are canonical.
CHANNELS = tuple(
    [(f"T200:a{k}", 200, POINTS[k], 20) for k in range(3, 16)]
    + [(f"T800:a{k}", 800, POINTS[k], 40) for k in range(3, 16)]
)

OWNER_INDICES = {
    "n4_T200": tuple(range(0, 5)),
    "n8_T200": tuple(range(4, 13)),
    "n4_T800": tuple(range(13, 18)),
    "n8_T800": tuple(range(17, 26)),
}

OWNER_PRIMALS = {
    "n4_T200": {(0, 2): F(1, 40), (2, 4): F(1, 40)},
    "n8_T200": {(4, 6): F(1, 128), (10, 12): F(1, 128)},
    "n4_T800": {},
    "n8_T800": {
        (17, 18): F(13, 512),
        (17, 19): F(131, 2560),
        (23, 24): F(131, 2560),
        (24, 25): F(49, 640),
    },
}

OWNER_DUALS = {
    "n4_T200": {
        (525, 616): F(698, 5),
        (636, 709): F(1426, 15),
        (749, 816): F(418, 5),
        (836, 864): F(2186, 15),
    },
    "n8_T200": {
        (981, 1036): F(247, 2),
        (1109, 1149): F(321, 2),
        (1725, 1744): F(351, 2),
        (1796, 1869): F(193, 2),
    },
    "n4_T800": {},
    "n8_T800": {
        (1596, 1621): F(933, 10),
        (1669, 1725): F(351, 2),
        (2349, 2396): F(381, 2),
        (2396, 2464): F(1263, 10),
    },
}

EXPECTED_OWNER_OBJECTIVES = {
    "n4_T200": F(29, 200),
    "n8_T200": F(139, 3200),
    "n4_T800": F(0),
    "n8_T800": F(59841, 512000),
}

EXPECTED_OWNER_DEMANDS = {
    "n4_T200": F(63, 640),
    "n8_T200": F(169, 12800),
    "n4_T800": F(0),
    "n8_T800": F(361, 5120),
}


class CertificateError(RuntimeError):
    """Raised when an exact witness, scope gate, or byte replay fails."""


def ftext(value: F | int) -> str:
    """Render an exact rational with an explicit denominator."""

    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def _haar_value(x: int, origin: int, width: int) -> int:
    displacement = x - origin
    if 0 <= displacement < width:
        return 1
    if width <= displacement < 2 * width:
        return -1
    return 0


def _cells() -> tuple[list[dict[str, object]], list[int]]:
    events = sorted(
        {
            origin + shift
            for _, width, origin, _ in CHANNELS
            for shift in (0, width, 2 * width)
        }
    )
    matrix4 = membership.point_m_matrix(4)
    matrix8 = membership.point_m_matrix(8)
    matrices = {
        "n4_T200": matrix4,
        "n8_T200": matrix8,
        "n4_T800": matrix4,
        "n8_T800": matrix8,
    }
    rows: list[dict[str, object]] = []
    for left, right in zip(events, events[1:]):
        state = tuple(
            F(_haar_value(left, origin, width), normalizer)
            for _, width, origin, normalizer in CHANNELS
        )
        demands = {
            owner: membership.quadratic(
                matrices[owner], tuple(state[index] for index in indices)
            )
            for owner, indices in OWNER_INDICES.items()
        }
        rows.append(
            {
                "id": f"[{left},{right})",
                "left": left,
                "right": right,
                "length": right - left,
                "state": state,
                "demands": demands,
            }
        )
    return rows, events


def _physical_price_formula_audit(
    pairs: Sequence[tuple[int, int]], costs: Mapping[tuple[int, int], F]
) -> int:
    checked = 0
    for pair in pairs:
        i, j = pair
        _, width, origin, normalizer = CHANNELS[i]
        _, other_width, other_origin, other_normalizer = CHANNELS[j]
        square_root_product = F(normalizer * other_normalizer, 2)
        expected = F(2) - mixed.mixed_haar_inner(
            width, other_width, other_origin - origin
        ) / square_root_product
        if costs[pair] != expected:
            raise AssertionError(f"C091 physical root price mismatch at {pair}")
        checked += 1
    return checked


def _owned_cells(
    cells: Sequence[Mapping[str, object]], owner: str
) -> list[dict[str, object]]:
    return [
        {
            "id": cell["id"],
            "left": cell["left"],
            "right": cell["right"],
            "length": cell["length"],
            "state": cell["state"],
            "demand": cell["demands"][owner],
        }
        for cell in cells
    ]


def _owner_audit(
    owner: str,
    cells: list[dict[str, object]],
    pairs: tuple[tuple[int, int], ...],
    columns: dict[tuple[int, int], tuple[F, ...]],
    costs: dict[tuple[int, int], F],
) -> tuple[dict[str, object], dict[tuple[int, int], F], tuple[F, ...]]:
    primal = OWNER_PRIMALS[owner]
    dual = OWNER_DUALS[owner]
    owner_cells = _owned_cells(cells, owner)
    full = base._verify_lp(owner_cells, pairs, columns, costs, primal, dual)

    no_cross_pairs = tuple(
        pair for pair in pairs if CHANNELS[pair[0]][1] == CHANNELS[pair[1]][1]
    )
    no_cross = base._verify_lp(
        owner_cells,
        no_cross_pairs,
        {pair: columns[pair] for pair in no_cross_pairs},
        {pair: costs[pair] for pair in no_cross_pairs},
        primal,
        dual,
    )
    objective = F(full["objective"])
    if objective != EXPECTED_OWNER_OBJECTIVES[owner]:
        raise AssertionError(f"wrong exact owner objective for {owner}")
    if F(no_cross["objective"]) != objective:
        raise AssertionError(f"full/no-cross objective mismatch for {owner}")

    integrated_demand = sum(
        (
            F(cell["length"]) * F(cell["demands"][owner])
            for cell in cells
        ),
        F(0),
    )
    if integrated_demand != EXPECTED_OWNER_DEMANDS[owner]:
        raise AssertionError(f"wrong integrated owner demand for {owner}")

    cross_pairs = tuple(
        pair for pair in pairs if CHANNELS[pair[0]][1] != CHANNELS[pair[1]][1]
    )
    cross_margins = {
        pair: costs[pair] - F(full["loads"][pair]) for pair in cross_pairs
    }
    minimum_cross_margin = min(cross_margins.values())
    if minimum_cross_margin <= 0:
        raise AssertionError(f"cross root is not strictly excluded for {owner}")
    minimum_cross_roots = [
        pair for pair in cross_pairs if cross_margins[pair] == minimum_cross_margin
    ]

    public = {
        "channel_indices": list(OWNER_INDICES[owner]),
        "integrated_demand": ftext(integrated_demand),
        "full_optimum": ftext(objective),
        "no_cross_optimum": ftext(F(no_cross["objective"])),
        "primal_root_weights": {
            f"{pair[0]},{pair[1]}": ftext(weight)
            for pair, weight in sorted(primal.items())
        },
        "dual_cell_weights": {
            f"[{left},{right})": ftext(weight)
            for (left, right), weight in sorted(dual.items())
        },
        "minimum_cross_margin": ftext(minimum_cross_margin),
        "minimum_cross_roots": [
            f"{pair[0]},{pair[1]}" for pair in minimum_cross_roots
        ],
        "positive_cross_root_count": sum(
            primal.get(pair, F(0)) > 0 for pair in cross_pairs
        ),
    }
    return public, cross_margins, tuple(F(value) for value in full["slacks"])


def four_owner_lp_audit() -> dict[str, object]:
    if len(CHANNELS) != 26 or len({(row[1], row[2]) for row in CHANNELS}) != 26:
        raise AssertionError("physical channel deduplication failed")
    if OWNER_INDICES["n4_T200"][-1] != OWNER_INDICES["n8_T200"][0]:
        raise AssertionError("T=200 shared channel was not deduplicated")
    if OWNER_INDICES["n4_T800"][-1] != OWNER_INDICES["n8_T800"][0]:
        raise AssertionError("T=800 shared channel was not deduplicated")

    cells, events = _cells()
    if len(events) != 64 or len(cells) != 63:
        raise AssertionError("wrong common endpoint refinement")
    pairs, columns, costs = base._root_columns(cells, len(CHANNELS))
    formula_checks = _physical_price_formula_audit(pairs, costs)
    same_scale_pairs = tuple(
        pair for pair in pairs if CHANNELS[pair[0]][1] == CHANNELS[pair[1]][1]
    )
    cross_pairs = tuple(pair for pair in pairs if pair not in same_scale_pairs)
    if (len(pairs), len(same_scale_pairs), len(cross_pairs)) != (325, 156, 169):
        raise AssertionError("wrong root census")

    owner_rows: dict[str, object] = {}
    owner_cross_margins: dict[str, dict[tuple[int, int], F]] = {}
    owner_slacks: dict[str, tuple[F, ...]] = {}
    for owner in OWNER_INDICES:
        public, cross_margins, slacks = _owner_audit(
            owner, cells, pairs, columns, costs
        )
        owner_rows[owner] = public
        owner_cross_margins[owner] = cross_margins
        owner_slacks[owner] = slacks

    full_objective = sum(EXPECTED_OWNER_OBJECTIVES.values(), F(0))
    no_cross_objective = sum(
        (F(owner_rows[owner]["no_cross_optimum"]) for owner in OWNER_INDICES),
        F(0),
    )
    integrated_demand = sum(EXPECTED_OWNER_DEMANDS.values(), F(0))
    if full_objective != F(156321, 512000):
        raise AssertionError("wrong total exact objective")
    if integrated_demand != F(4663, 25600):
        raise AssertionError("wrong total integrated demand")

    combined_weights = {
        pair: sum(
            (OWNER_PRIMALS[owner].get(pair, F(0)) for owner in OWNER_INDICES),
            F(0),
        )
        for pair in pairs
    }
    pointwise_identity_checks = 0
    for row_index, cell in enumerate(cells):
        owner_corrections = {
            owner: sum(
                (
                    weight * columns[pair][row_index]
                    for pair, weight in OWNER_PRIMALS[owner].items()
                ),
                F(0),
            )
            for owner in OWNER_INDICES
        }
        combined_correction = sum(
            (
                combined_weights[pair] * columns[pair][row_index]
                for pair in pairs
            ),
            F(0),
        )
        if sum(owner_corrections.values(), F(0)) != combined_correction:
            raise AssertionError("owner correction was credited more than once")
        pointwise_identity_checks += 1

    priced_by_owners = sum(
        (
            weight * costs[pair]
            for owner in OWNER_INDICES
            for pair, weight in OWNER_PRIMALS[owner].items()
        ),
        F(0),
    )
    priced_by_combined_root = sum(
        (combined_weights[pair] * costs[pair] for pair in pairs), F(0)
    )
    if priced_by_owners != priced_by_combined_root or priced_by_owners != full_objective:
        raise AssertionError("physical objective is not paid exactly once")

    n4_t800_nonzero = sum(
        F(cell["demands"]["n4_T800"]) != 0 for cell in cells
    )
    if n4_t800_nonzero:
        raise AssertionError("the certified inactive owner unexpectedly has demand")

    event_sources: dict[int, list[str]] = {}
    for k in range(3, 16):
        for shift in (0, 200, 400, 800, 1600):
            event_sources.setdefault(POINTS[k] + shift, []).append(f"a{k}+{shift}")
    collisions = {
        str(event): labels
        for event, labels in sorted(event_sources.items())
        if len(labels) > 1
    }
    if collisions != {"2125": ["a5+1600", "a15+400"]}:
        raise AssertionError("unexpected event collision census")

    root_price_audit = {
        f"{pair[0]},{pair[1]}": {
            "kind": "cross_scale" if pair in cross_pairs else "same_scale",
            "physical_cost": ftext(costs[pair]),
        }
        for pair in pairs
    }
    return {
        "raw_owner_channel_occurrence_count": 28,
        "physical_channel_count": len(CHANNELS),
        "deduplicated_owner_channel_count": 2,
        "shared_channel_indices": {
            "n4_T200_last_equals_n8_T200_first": 4,
            "n4_T800_last_equals_n8_T800_first": 17,
        },
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
        "finite_event_count": len(events),
        "positive_length_cell_count": len(cells),
        "complete_real_line_cell_count": len(cells) + 2,
        "event_collisions": collisions,
        "physical_root_count": len(pairs),
        "same_scale_root_count": len(same_scale_pairs),
        "cross_scale_root_count": len(cross_pairs),
        "cell_sum_root_price_check_count": len(costs),
        "C091_oriented_formula_check_count": formula_checks,
        "root_price_audit": root_price_audit,
        "owner_count": len(OWNER_INDICES),
        "owner_cell_constraint_count": len(OWNER_INDICES) * len(cells),
        "full_owner_root_variable_count": len(OWNER_INDICES) * len(pairs),
        "full_dual_column_check_count": len(OWNER_INDICES) * len(pairs),
        "no_cross_owner_root_variable_count": len(OWNER_INDICES)
        * len(same_scale_pairs),
        "owners": owner_rows,
        "integrated_signed_demand": ftext(integrated_demand),
        "full_optimum": ftext(full_objective),
        "no_cross_scale_optimum": ftext(no_cross_objective),
        "full_minus_no_cross_gap": ftext(full_objective - no_cross_objective),
        "surplus_over_integrated_demand": ftext(
            full_objective - integrated_demand
        ),
        "full_primal_dual_gap": "0/1",
        "optimal_face_cross_mass": {
            "objective_definition": (
                "sum of all owner-labelled cross-scale root coefficients"
            ),
            "minimum_cross_root_mass": "0/1",
            "minimum_cross_physical_price_contribution": "0/1",
            "cross_free_optimal_witness_present": True,
            "all_676_owner_cross_columns_have_strict_dual_margin": all(
                margin > 0
                for margins in owner_cross_margins.values()
                for margin in margins.values()
            ),
            "cross_roots_forced_zero_on_exposed_optimal_face": True,
        },
        "ownership_ledger": {
            "root_coefficient_identity": "q_e=sum_o x_(o,e)",
            "owner_correction_identity": "P_(o,c)=sum_e R_(c,e)*x_(o,e)",
            "pointwise_sum_identity": "sum_o P_(o,c)=sum_e R_(c,e)*q_e",
            "physical_price_identity": "sum_o,e p_e*x_(o,e)=sum_e p_e*q_e",
            "one_root_unit_credited_to_multiple_owners_for_one_price": False,
            "owner_demands_pooled_before_cover": False,
            "exact_pointwise_identity_check_count": pointwise_identity_checks,
            "exact_objective_identity_verified": True,
        },
        "inactive_owner_caveat": {
            "owner": "n4_T800",
            "zero_demand_cell_count": len(cells),
            "nonzero_demand_cell_count": n4_t800_nonzero,
            "block_span": POINTS[7] - POINTS[3],
            "width": 800,
            "four_active_owner_fixture": False,
        },
    }


def build_certificate() -> dict[str, object]:
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "fixed_16_mark_four_owner_fixture_only": True,
            "four_active_owner_fixture": False,
            "nonnegative_globally_owner_labelled_roots_only": True,
            "cell_dependent_owner_reassignment_allowed": False,
            "signed_coordinate_row_split_included": False,
            "aggregate_J_or_indefinite_cross_blocks_included": False,
            "signed_source_to_sink_owner_flow_included": False,
            "direct_M_Gothic_one_for_one_payment_proved": False,
            "birth_gate_final_terminal_ownership_proved": False,
            "active_current_to_past_payment_proved": False,
            "positive_net_Phi_proved": False,
            "other_scale_ratios_or_histories_proved": False,
            "continuum_phase_or_common_history_ledger_proved": False,
            "C058_Q1_Q2_proved": False,
            "publication_novelty_or_prize_claimed": False,
        },
        "four_owner_lp": four_owner_lp_audit(),
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
    if not isinstance(certificate, Mapping):
        raise CertificateError("certificate root must be an object")
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
    certificate["integrity"]["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> dict[str, int]:
    mutation_specs: tuple[tuple[tuple[str, ...], object], ...] = (
        (("schema",), "wrong.schema"),
        (("status",), "C058_SOLVED"),
        (("scope", "fixed_16_mark_four_owner_fixture_only"), False),
        (("scope", "C058_Q1_Q2_proved"), True),
        (("scope", "publication_novelty_or_prize_claimed"), True),
        (("four_owner_lp", "physical_channel_count"), 27),
        (("four_owner_lp", "deduplicated_owner_channel_count"), 1),
        (("four_owner_lp", "finite_event_count"), 63),
        (("four_owner_lp", "positive_length_cell_count"), 62),
        (("four_owner_lp", "physical_root_count"), 324),
        (("four_owner_lp", "C091_oriented_formula_check_count"), 324),
        (("four_owner_lp", "full_optimum"), "0/1"),
        (("four_owner_lp", "no_cross_scale_optimum"), "0/1"),
        (("four_owner_lp", "full_minus_no_cross_gap"), "1/1"),
        (("four_owner_lp", "optimal_face_cross_mass", "minimum_cross_root_mass"), "1/1"),
        (("four_owner_lp", "optimal_face_cross_mass", "all_676_owner_cross_columns_have_strict_dual_margin"), False),
        (("four_owner_lp", "inactive_owner_caveat", "four_active_owner_fixture"), True),
        (("four_owner_lp", "ownership_ledger", "one_root_unit_credited_to_multiple_owners_for_one_price"), True),
    )
    mutations: list[dict[str, object]] = []
    for path, value in mutation_specs:
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
        raise CertificateError("a semantic or scope mutation was accepted")
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

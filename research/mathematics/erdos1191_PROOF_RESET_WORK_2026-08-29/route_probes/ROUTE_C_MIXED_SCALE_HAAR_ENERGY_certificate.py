#!/usr/bin/env python3
"""Exact mixed-scale Haar inner products and physical-energy audits."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Mapping


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_MIXED_SCALE_HAAR_ENERGY_certificate.json"
SCHEMA = "erdos1191.route_c_mixed_scale_haar_energy.v1"
STATUS = "EXACT_MIXED_SCALE_PHYSICAL_DUAL_NO_GO_ONLY"


def _positive_part(value: F) -> F:
    return max(value, F(0))


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def box_overlap(width: F, other_width: F, shift: F) -> F:
    """Length of [0,width) intersect [shift,shift+other_width)."""
    width = F(width)
    other_width = F(other_width)
    shift = F(shift)
    if width <= 0 or other_width <= 0:
        raise ValueError("widths must be positive")
    return (
        _positive_part(width - shift)
        - _positive_part(width - shift - other_width)
        - _positive_part(-shift)
        + _positive_part(-shift - other_width)
    )


def mixed_haar_inner(width: F, other_width: F, shift: F) -> F:
    """Integral g_width(x) g_other_width(x-shift) dx exactly."""
    width = F(width)
    other_width = F(other_width)
    shift = F(shift)
    return (
        box_overlap(width, other_width, shift)
        - box_overlap(width, other_width, shift + other_width)
        - box_overlap(width, other_width, shift - width)
        + box_overlap(width, other_width, shift + other_width - width)
    )


def mixed_linear_energy(
    width: F,
    other_width: F,
    shift: F,
    coefficient: F,
    other_coefficient: F,
) -> F:
    """Integral of (coefficient*g_T + other_coefficient*tau_shift*g_S)^2."""
    width = F(width)
    other_width = F(other_width)
    coefficient = F(coefficient)
    other_coefficient = F(other_coefficient)
    return (
        2 * width * coefficient * coefficient
        + 2 * other_width * other_coefficient * other_coefficient
        + 2
        * coefficient
        * other_coefficient
        * mixed_haar_inner(width, other_width, F(shift))
    )


def _haar_state(x: F, origin: F, width: F) -> int:
    if origin <= x < origin + width:
        return 1
    if origin + width <= x < origin + 2 * width:
        return -1
    return 0


def mixed_atomic_cells(width: F, other_width: F, shift: F) -> list[dict[str, object]]:
    """Complete half-open cells for g_width(x) and g_other_width(x-shift)."""
    width = F(width)
    other_width = F(other_width)
    shift = F(shift)
    if width <= 0 or other_width <= 0:
        raise ValueError("widths must be positive")
    endpoints = sorted({F(0), width, 2 * width, shift, shift + other_width, shift + 2 * other_width})
    rows: list[dict[str, object]] = [
        {
            "id": f"(-inf,{endpoints[0]})",
            "left": "-infinite",
            "right": endpoints[0],
            "length": "infinite",
            "state": [0, 0],
        }
    ]
    for left, right in zip(endpoints, endpoints[1:]):
        rows.append(
            {
                "id": f"[{left},{right})",
                "left": left,
                "right": right,
                "length": right - left,
                "state": [
                    _haar_state(left, F(0), width),
                    _haar_state(left, shift, other_width),
                ],
            }
        )
    rows.append(
        {
            "id": f"[{endpoints[-1]},inf)",
            "left": endpoints[-1],
            "right": "infinite",
            "length": "infinite",
            "state": [0, 0],
        }
    )
    return rows


def _quadratic_2(matrix: tuple[tuple[F, F], tuple[F, F]], state: tuple[int, int]) -> F:
    return (
        matrix[0][0] * state[0] * state[0]
        + 2 * matrix[0][1] * state[0] * state[1]
        + matrix[1][1] * state[1] * state[1]
    )


def _cross_candidate_rows(
    cells: list[dict[str, object]],
    target: tuple[tuple[F, F], tuple[F, F]],
    correction: tuple[tuple[F, F], tuple[F, F]],
) -> tuple[list[dict[str, str]], F, F]:
    rows = []
    demand = F(0)
    price = F(0)
    for cell in cells:
        if cell["length"] == "infinite":
            continue
        state = tuple(int(value) for value in cell["state"])
        target_value = _quadratic_2(target, state)
        correction_value = _quadratic_2(correction, state)
        slack = correction_value - target_value
        length = F(cell["length"])
        demand += length * target_value
        price += length * correction_value
        rows.append(
            {
                "id": str(cell["id"]),
                "target": ftext(target_value),
                "correction": ftext(correction_value),
                "slack": ftext(slack),
            }
        )
    return rows, demand, price


def two_scale_cross_block_audit() -> dict[str, object]:
    """Exact T=2, S=4 actual-cell audit of a tempting negative cross block."""
    cells = mixed_atomic_cells(F(2), F(4), F(-1))
    target = ((F(1, 4), F(0)), (F(0), F(1, 8)))
    lowering = ((F(1, 4), -F(1, 16)), (-F(1, 16), F(1, 8)))
    feasible = ((F(3, 8), -F(1, 16)), (-F(1, 16), F(1, 8)))
    lowering_rows, demand, lowering_price = _cross_candidate_rows(cells, target, lowering)
    feasible_rows, feasible_demand, feasible_price = _cross_candidate_rows(cells, target, feasible)
    if demand != F(2) or feasible_demand != demand:
        raise RuntimeError("two-scale canonical demand changed")
    violating = next(row for row in lowering_rows if F(row["slack"]) < 0)
    if violating != {
        "id": "[0,2)",
        "target": "3/8",
        "correction": "1/4",
        "slack": "-1/8",
    }:
        raise RuntimeError("price-lowering violation changed")
    if any(F(row["slack"]) < 0 for row in feasible_rows):
        raise RuntimeError("advertised actual-cell cross block is infeasible")
    if lowering_price != F(7, 4) or feasible_price != F(9, 4):
        raise RuntimeError("two-scale prices changed")
    return {
        "fixture": {"T": "2/1", "S": "4/1", "shift": "-1/1"},
        "canonical_target_matrix": [["1/4", "0/1"], ["0/1", "1/8"]],
        "canonical_same_scale_demand": ftext(demand),
        "price_lowering_attempt": {
            "cross_coefficient": "-1/16",
            "physical_price": ftext(lowering_price),
            "below_canonical_demand": True,
            "violating_cell": violating["id"],
            "violating_slack": violating["slack"],
            "cell_rows": lowering_rows,
        },
        "actual_cell_feasible_cross_block": {
            "added_first_scale_diagonal": "1/8",
            "cross_coefficient": "-1/16",
            "physical_price": ftext(feasible_price),
            "excess_over_demand": ftext(feasible_price - demand),
            "cell_rows": feasible_rows,
        },
    }


def cross_block_grid_audit() -> dict[str, object]:
    """Exhaust a rational actual-cell grid around the T=2, S=4 fixture."""
    cells = [
        cell
        for cell in mixed_atomic_cells(F(2), F(4), F(-1))
        if cell["length"] != "infinite"
    ]
    feasible: list[tuple[F, F, F, F]] = []
    negative_excess = 0
    for a_numerator in range(-4, 5):
        for b_numerator in range(-4, 5):
            for c_numerator in range(-4, 5):
                a = F(a_numerator, 16)
                b = F(b_numerator, 16)
                c = F(c_numerator, 16)
                slacks = []
                weighted_slack = F(0)
                for cell in cells:
                    state = tuple(int(value) for value in cell["state"])
                    slack = a * state[0] ** 2 + 2 * b * state[0] * state[1] + c * state[1] ** 2
                    slacks.append(slack)
                    weighted_slack += F(cell["length"]) * slack
                if any(slack < 0 for slack in slacks):
                    continue
                formula_excess = 4 * a + 4 * b + 8 * c
                if formula_excess != weighted_slack:
                    raise RuntimeError("cell-length dual identity failed on the rational grid")
                feasible.append((a, b, c, formula_excess))
                negative_excess += formula_excess < 0
    if not feasible:
        raise RuntimeError("rational grid unexpectedly has no feasible point")
    minimum = min(value[3] for value in feasible)
    zero_points = [(a, b, c) for a, b, c, excess in feasible if excess == 0]
    nonzero_cross_minimum = min(excess for _, b, _, excess in feasible if b != 0)
    return {
        "grid": "a,b,c in {-4,...,4}/16 for added block [[a,b],[b,c]]",
        "total_grid_count": 9**3,
        "actual_cell_feasible_count": len(feasible),
        "feasible_negative_excess_count": negative_excess,
        "minimum_feasible_excess": ftext(minimum),
        "zero_excess_points": [[ftext(value) for value in point] for point in zero_points],
        "zero_excess_only_at_zero_added_block": zero_points == [(F(0), F(0), F(0))],
        "minimum_feasible_excess_with_nonzero_cross": ftext(nonzero_cross_minimum),
        "identity": "physical price - canonical demand = sum_c |c| * pointwise slack",
    }


def mixed_formula_audit() -> dict[str, object]:
    """Replay the hinge formula on a dense exact dyadic/shift grid."""
    widths = tuple(F(2) ** exponent for exponent in range(-2, 4))
    checked = 0
    for width in widths:
        for other_width in widths:
            lower = int(-8 * other_width) - 2
            upper = int(8 * width) + 2
            for numerator in range(lower, upper + 1):
                shift = F(numerator, 4)
                value = mixed_haar_inner(width, other_width, shift)
                cells = mixed_atomic_cells(width, other_width, shift)
                from_cells = sum(
                    (
                        F(cell["length"])
                        * int(cell["state"][0])
                        * int(cell["state"][1])
                        for cell in cells
                        if cell["length"] != "infinite"
                    ),
                    F(0),
                )
                if value != from_cells:
                    raise RuntimeError("mixed Haar hinge/cell formula mismatch")
                if value != mixed_haar_inner(other_width, width, -shift):
                    raise RuntimeError("mixed Haar orientation symmetry failed")
                if 2 * value != mixed_haar_inner(2 * width, 2 * other_width, 2 * shift):
                    raise RuntimeError("mixed Haar common-dilation identity failed")
                checked += 1
    samples = {
        "d=0": ftext(mixed_haar_inner(F(4), F(4), F(0))),
        "d=1": ftext(mixed_haar_inner(F(4), F(4), F(1))),
        "d=4": ftext(mixed_haar_inner(F(4), F(4), F(4))),
        "d=8": ftext(mixed_haar_inner(F(4), F(4), F(8))),
    }
    if samples != {"d=0": "8/1", "d=1": "5/1", "d=4": "-4/1", "d=8": "0/1"}:
        raise RuntimeError("same-scale regression changed")
    return {
        "widths": [ftext(width) for width in widths],
        "shift_grid": "quarter-integers covering [-2S-1/2,2T+1/2]",
        "exact_dyadic_rows_checked": checked,
        "cell_sum_equals_hinge_formula_everywhere": True,
        "orientation_symmetry_everywhere": True,
        "common_dilation_everywhere": True,
        "same_scale_T4_samples": samples,
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (
        json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"
    ).encode("utf-8")


def build_certificate() -> dict[str, object]:
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": {
            "proved": [
                "the exact oriented mixed-scale half-open Haar inner product for arbitrary positive rational, hence dyadic, widths and rational shifts",
                "the exact physical energy of every finite linear combination of translated mixed-scale Haar profiles",
                "the common-refinement cell-length dual lower bound for arbitrary finite scale families and arbitrary actual-cell-valid cross blocks",
                "a sharp T=2, S=4 actual-cell cross-block fixture and an exhaustive 729-point rational adversarial grid",
            ],
            "not_proved": [
                "a cross-scale reduction relative to the sum of separate optimal physical covers",
                "a uniform upper bound on physical cover excess above integrated signed demand",
                "continuum-phase paid ledger",
                "terminal, birth, past-scale, final-row, or shared-endpoint ownership",
                "C058, Q1, or Q2",
                "publication novelty or prize eligibility",
            ],
        },
        "mixed_inner_product_theorem": {
            "profiles": "g_T=1_[0,T)-1_[T,2T); tau_d g_S(x)=g_S(x-d)",
            "box_overlap": "H_(T,S)(d)=(T-d)_+-(T-d-S)_+-(-d)_++(-d-S)_+",
            "formula": "A_(T,S)(d)=H(d)-H(d+S)-H(d-T)+H(d+S-T)",
            "meaning": "A_(T,S)(d)=integral g_T(x) g_S(x-d) dx",
            "support": "A_(T,S)(d)=0 outside [-2S,2T]",
            "piecewise_linear_knots": [
                "-2S",
                "-S",
                "0",
                "T-2S",
                "T-S",
                "T",
                "2T-2S",
                "2T-S",
                "2T",
            ],
            "orientation_symmetry": "A_(T,S)(d)=A_(S,T)(-d)",
            "common_dilation": "A_(lambda*T,lambda*S)(lambda*d)=lambda*A_(T,S)(d)",
            "same_scale_reduction": "A_(T,T)(d)=2T-3|d| for |d|<=T; |d|-2T for T<=|d|<=2T; 0 otherwise",
            "linear_energy": "integral (alpha*g_T+beta*tau_d*g_S)^2=2T*alpha^2+2S*beta^2+2alpha*beta*A_(T,S)(d)",
            "normalized_root_energy": "integral (g_T/sqrt(2T)-tau_d*g_S/sqrt(2S))^2=2-A_(T,S)(d)/sqrt(TS)",
            "formula_audit": mixed_formula_audit(),
        },
        "cell_length_dual_theorem": {
            "arbitrary_finite_scale_family": True,
            "hypothesis": "on every positive-length common atomic cell c, correction density P_c is at least signed target density D_c",
            "identity": "physical_price-integrated_demand=sum_c |c|*(P_c-D_c)",
            "conclusion": "physical_price>=integrated_demand",
            "cross_blocks_cannot_beat_integrated_demand": True,
            "coefficient_PSD_not_needed": True,
            "equality_condition": "P_c=D_c on every positive-length cell",
            "interpretation": "the cell-length measure is a dual feasible point that saturates every within-scale and cross-scale physical-energy column by definition",
        },
        "two_scale_fixture": two_scale_cross_block_audit(),
        "adversarial_grid": cross_block_grid_audit(),
        "route_boundary": {
            "strict_no_go": "no actual-cell-valid mixed-scale cross block can lower total physical price below the integrated same-scale signed demand when both are priced with the same common physical measure",
            "still_open": "cross-scale blocks may lower the sum of separate pointwise-cover optima while remaining above demand; a uniform phase-integrated excess upper bound and a singly owned payment source remain open",
            "continuum_phase_normalization": "the direct-B Haar identity represents W_n/log(2); a unit W_n ledger requires the outer factor log(2)",
            "gothic_ownership": "2M=lambda is a rewrite of the existing Gothic rows, never a second capacity source",
        },
    }
    certificate["integrity"] = {"canonical_json": True, "payload_sha256": payload_hash(certificate)}
    return certificate


def validate_certificate(certificate: Mapping[str, object]) -> None:
    expected = build_certificate()
    if certificate.get("schema") != SCHEMA or certificate.get("status") != STATUS:
        raise ValueError("schema or status mismatch")
    if certificate.get("integrity", {}).get("payload_sha256") != payload_hash(certificate):
        raise ValueError("payload hash mismatch")
    if certificate != expected:
        raise ValueError("semantic replay mismatch")


def rehash(certificate: dict[str, object]) -> None:
    certificate.setdefault("integrity", {})["payload_sha256"] = payload_hash(certificate)


def self_check(certificate: Mapping[str, object]) -> int:
    mutations: list[dict[str, object]] = []

    changed = copy.deepcopy(certificate)
    changed["status"] = "Q1_SOLVED"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["scope"]["not_proved"] = []
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["mixed_inner_product_theorem"]["formula"] = "A=0"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["cell_length_dual_theorem"]["cross_blocks_cannot_beat_integrated_demand"] = False
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["adversarial_grid"]["feasible_negative_excess_count"] = 1
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["two_scale_fixture"]["price_lowering_attempt"]["violating_slack"] = "0/1"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["route_boundary"]["continuum_phase_normalization"] = "no log factor"
    rehash(changed)
    mutations.append(changed)

    changed = copy.deepcopy(certificate)
    changed["integrity"]["payload_sha256"] = "0" * 64
    mutations.append(changed)

    rejected = 0
    for mutation in mutations:
        try:
            validate_certificate(mutation)
        except ValueError:
            rejected += 1
    if rejected != len(mutations):
        raise ValueError("a semantic or hash mutation was accepted")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--verify", type=Path, help="verify an existing exact certificate")
    parser.add_argument("--self-check", action="store_true", help="run semantic/hash mutations")
    args = parser.parse_args()

    certificate = build_certificate()
    if args.verify:
        raw = args.verify.read_bytes()
        loaded = json.loads(raw.decode("utf-8"))
        validate_certificate(loaded)
        if raw != rendered_bytes(certificate):
            raise ValueError("literal raw-byte replay mismatch")
    if args.self_check:
        self_check(certificate)
    if not args.verify:
        args.output.write_bytes(rendered_bytes(certificate))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

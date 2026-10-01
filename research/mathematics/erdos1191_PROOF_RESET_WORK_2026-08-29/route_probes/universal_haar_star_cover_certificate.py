#!/usr/bin/env python3
"""Exact universal star cover for actual ordered Haar block states."""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import sys
from typing import Sequence

import direct_b_membership_sddm_lp_certificate as membership
import direct_b_physical_energy_lp_certificate as physical


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "universal_haar_star_cover_certificate.json"


class CertificateError(RuntimeError):
    """Raised when a semantic or integrity replay fails."""


def build_certificate() -> dict[str, object]:
    """Build the exact theorem and fixed-fixture replay payload."""
    abstract = copy.deepcopy(exhaustive_state_audit(2, 16))
    fixtures = (
        ("n4_T200", 4, membership.ONE_EPOCH_POINTS, 200),
        ("n8_T200", 8, membership.FULL_TWO_EPOCH_POINTS[7:], 200),
        ("n4_T2000", 4, physical.THREE_EPOCH_FULL_POINTS[3:8], 2000),
        ("n8_T2000", 8, physical.THREE_EPOCH_FULL_POINTS[7:16], 2000),
        ("n16_T2000", 16, physical.THREE_EPOCH_FULL_POINTS[15:32], 2000),
    )
    fixture_rows = []
    for label, n, points, width in fixtures:
        audit = actual_cell_audit(n, points, width)
        fixture_rows.append(
            {
                "label": label,
                "n": n,
                "T": width,
                "points": list(points),
                "complete_cell_count": audit["complete_cell_count"],
                "classification_failures": audit["classification_failures"],
                "cover_failures": audit["cover_failures"],
                "physical_star_price": str(audit["cell_sum_star_price"]),
                "weighted_signed_demand": str(audit["weighted_signed_demand"]),
                "star_surplus": str(audit["star_surplus"]),
                "cell_rows": audit["rows"],
            }
        )
    certificate: dict[str, object] = {
        "schema": "erdos1191.universal_haar_star_cover.v1",
        "status": "UNIVERSAL_ACTUAL_HAAR_STATE_COVER_PROVED_PHYSICAL_PAYMENT_OPEN",
        "theorem": {
            "range": "every integer n>=3 and every ordered actual Haar cell state v=0^a(-1)^b(+1)^c0^d",
            "star_weight": "(n-1)/(8n^2)",
            "root_edges": "(0,k) and (k,n) for 1<=k<=n-1",
            "domination": "v^T C_star v >= v^T M_n v",
            "total_root_mass": "(n-1)^2/(4n^2)",
            "coefficient_mass_optimality": "sharp among every nonnegative root-Laplacian cover on all abstract ordered Haar states",
            "sharp_dual_state": "1_[1,n-1]",
            "sharp_state_value": "(n-1)^2/(4n^2)",
            "physical_price": "((n-1)/(8n^2))*sum_(k=1)^(n-1)[chi_T(b_k-b_0)+chi_T(b_n-b_k)]",
        },
        "proof_case_inequalities": {
            "one_internal_sign_block": "b^2 <= (n-1)b for 1<=b<=n-1",
            "two_internal_sign_blocks": "(b-c)^2-2*1_(b=1)-2*1_(c=1) <= (n-1)(b+c)",
            "left_boundary_two_blocks": "4c^2 <= (n-1)(n-1+4c)",
            "right_boundary_two_blocks": "4b^2 <= (n-1)(n-1+4b)",
            "both_boundaries": "direct energy is zero",
        },
        "abstract_state_audit": abstract,
        "fixture_audits": fixture_rows,
        "ungated_low_scale_gate": {
            "fixture": "n4_T1",
            "physical_star_price": str(physical_star_price(membership.ONE_EPOCH_POINTS, 1)),
            "dyadic_low_scale_behavior": "constant positive price once every star-root distance is at least 2T",
            "ungated_sum_over_all_low_scales_diverges": True,
        },
        "scope": {
            "universal_actual_state_feasibility": True,
            "coefficient_mass_optimality_for_state_universal_root_covers": True,
            "scale_or_phase_adaptive_payment_proved": False,
            "active_gate_and_terminal_paid": False,
            "single_ledger_inequality_proved": False,
            "C058_Q1_Q2_or_prize_proved": False,
        },
    }
    certificate["integrity"] = {
        "canonical_json": True,
        "payload_sha256": payload_hash(certificate),
    }
    return certificate


def verify_certificate(certificate: dict[str, object]) -> None:
    """Recompute every theorem table and reject any semantic drift."""
    expected = build_certificate()
    if certificate != expected:
        raise CertificateError("certificate differs from exact semantic replay")
    integrity = certificate.get("integrity")
    if not isinstance(integrity, dict) or integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")


def payload_hash(certificate: dict[str, object]) -> str:
    """Hash canonical JSON after excluding the self-referential integrity row."""
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def rendered_bytes(certificate: dict[str, object]) -> bytes:
    """Return the unique canonical JSON byte representation."""
    return (
        json.dumps(certificate, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode("utf-8")


def self_check(certificate: dict[str, object]) -> dict[str, int]:
    """Require rejection of ten independent overclaim/value mutations."""
    mutations = []
    for path, value in (
        (("schema",), "wrong.schema"),
        (("status",), "SOLVED"),
        (("theorem", "star_weight"), "(n-1)/(4n^2)"),
        (("theorem", "total_root_mass"), "1/4"),
        (("abstract_state_audit", "failures"), 1),
        (("abstract_state_audit", "distinct_states_checked"), 5819),
        (("fixture_audits", 0, "physical_star_price"), "0"),
        (("fixture_audits", 1, "weighted_signed_demand"), "0"),
        (("ungated_low_scale_gate", "physical_star_price"), "0"),
        (("scope", "single_ledger_inequality_proved"), True),
    ):
        changed = copy.deepcopy(certificate)
        target: object = changed
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]
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


@lru_cache(maxsize=None)
def _direct_matrix(n: int) -> tuple[tuple[F, ...], ...]:
    return tuple(tuple(row) for row in membership.point_m_matrix(n))


def haar_block_state(size: int, left: int, turn: int, right: int) -> tuple[int, ...]:
    """Return ``0^left (-1)^(turn-left) 1^(right-turn) 0^*``."""
    if size < 1 or not 0 <= left <= turn <= right <= size:
        raise ValueError("require 0 <= left <= turn <= right <= size")
    return tuple(
        0 if index < left or index >= right else (-1 if index < turn else 1)
        for index in range(size)
    )


def direct_energy(n: int, state: tuple[int, ...]) -> F:
    """Return ``state^T M_n state`` in physical point coordinates."""
    if len(state) != n + 1:
        raise ValueError("state length must be n+1")
    return membership.quadratic(_direct_matrix(n), state)


def star_energy(n: int, state: tuple[int, ...]) -> F:
    """Return the endpoint-to-interior star Laplacian energy."""
    if len(state) != n + 1:
        raise ValueError("state length must be n+1")
    return sum(
        (value * (state[i] - state[j]) ** 2 for (i, j), value in star_root_weights(n).items()),
        F(0),
    )


def physical_star_price(points: Sequence[int], width: int) -> F:
    """Return the exact sum of star weights times ``chi_T(distance)``."""
    n = len(points) - 1
    if n < 2 or width <= 0 or any(points[k] >= points[k + 1] for k in range(n)):
        raise ValueError("points must be strictly increasing and width positive")
    return sum(
        (
            value * physical.physical_root_cost(points[j] - points[i], width)
            for (i, j), value in star_root_weights(n).items()
        ),
        F(0),
    )


def actual_cell_audit(n: int, points: Sequence[int], width: int) -> dict[str, object]:
    """Replay classification, domination, and physical price on every cell."""
    if len(points) != n + 1:
        raise ValueError("points length must be n+1")
    cells = membership.atomic_cells(tuple(points), width)
    abstract_states = {
        haar_block_state(n + 1, left, turn, right)
        for left in range(n + 2)
        for turn in range(left, n + 2)
        for right in range(turn, n + 2)
    }
    classification_failures = 0
    cover_failures = 0
    cell_sum = F(0)
    demand = F(0)
    rows = []
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        classification_failures += state not in abstract_states
        star_value = star_energy(n, state)
        direct_value = direct_energy(n, state)
        cover_failures += star_value < direct_value
        weight = physical.cell_weight(cell, width)
        cell_sum += weight * star_value
        demand += weight * direct_value
        rows.append(
            {
                "id": cell["id"],
                "state": list(state),
                "star_energy": str(star_value),
                "direct_energy": str(direct_value),
                "slack": str(star_value - direct_value),
            }
        )
    root_price = physical_star_price(points, width)
    if cell_sum != root_price:
        raise AssertionError("cell and root physical prices disagree")
    return {
        "complete_cell_count": len(cells),
        "classification_failures": classification_failures,
        "cover_failures": cover_failures,
        "cell_sum_star_price": cell_sum,
        "weighted_signed_demand": demand,
        "star_surplus": cell_sum - demand,
        "rows": rows,
    }


def exhaustive_state_audit(n_min: int, n_max: int) -> dict[str, object]:
    """Return a fresh copy of the exhaustive ordered-Haar audit.

    The cached representation is an immutable JSON string.  Returning a newly
    decoded object prevents a caller from poisoning a later semantic replay by
    mutating a cached dictionary in the same process.
    """
    return json.loads(_exhaustive_state_audit_json(n_min, n_max))


@lru_cache(maxsize=None)
def _exhaustive_state_audit_json(n_min: int, n_max: int) -> str:
    """Cache the exhaustive audit in an immutable canonical representation."""
    if n_min < 2 or n_max < n_min:
        raise ValueError("require 2 <= n_min <= n_max")
    checked = 0
    failures = 0
    sharp_witnesses = 0
    per_n = []
    for n in range(n_min, n_max + 1):
        size = n + 1
        states = {
            haar_block_state(size, left, turn, right)
            for left in range(size + 1)
            for turn in range(left, size + 1)
            for right in range(turn, size + 1)
        }
        for state in states:
            checked += 1
            failures += star_energy(n, state) < direct_energy(n, state)
        target = F((n - 1) ** 2, 4 * n * n)
        sharp_value = None
        if n >= 3:
            sharp = haar_block_state(size, 1, 1, n)
            if star_energy(n, sharp) != target or direct_energy(n, sharp) != target:
                raise AssertionError(f"sharp witness failed for n={n}")
            sharp_witnesses += 1
            sharp_value = str(target)
        per_n.append({"n": n, "distinct_states": len(states), "sharp_value": sharp_value})
    audit = {
        "n_range": [n_min, n_max],
        "failures": failures,
        "sharp_witnesses": sharp_witnesses,
        "distinct_states_checked": checked,
        "per_n": per_n,
    }
    return json.dumps(audit, sort_keys=True, separators=(",", ":"))


def star_root_weights(n: int) -> dict[tuple[int, int], F]:
    """Return the candidate endpoint-to-interior star weights."""
    if n < 2:
        raise ValueError("n must be at least 2")
    weight = F(n - 1, 8 * n * n)
    return {
        edge: weight
        for k in range(1, n)
        for edge in ((0, k), (k, n))
    }


if __name__ == "__main__":
    raise SystemExit(main())

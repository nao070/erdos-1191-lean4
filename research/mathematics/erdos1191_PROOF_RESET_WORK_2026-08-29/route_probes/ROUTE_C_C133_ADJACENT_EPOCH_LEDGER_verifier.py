#!/usr/bin/env python3
"""Exact C133 verifier for the minimal adjacent epoch-8/epoch-16 ledger.

The theorem boundary is intentionally narrow: this file independently replays
the ``L=0, m=1, n=4`` specialization of the C103 finite two-dimensional Abel
identity, its 18-occurrence to 14-row stitch, and the current past-owner
coordinate law at shared rank 15.  All arithmetic is integer or
``fractions.Fraction`` arithmetic.

This is a finite C103 specialization only.  It proves no sign, capacity,
phase-selection, PSD-master, arbitrary-history, arbitrary-rank, C058, Q1, or
Q2 statement.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
import random
from typing import Any, Mapping


SCHEMA = "erdos1191.route_c.c133_adjacent_epoch_ledger.v1"
STATUS = "EXACT_FINITE_C103_ADJACENT_EPOCH_LEDGER_ONLY_C058_OPEN"
EPOCHS = (8, 16)
PREFIXES = (8, 16, 32)
SCALES = (0, 1, 2, 3)
UPPER_SCALE = 4
MULTIPLIERS = (1, 2, 4, 8)
RANDOM_SEED = 1191132
RANDOM_FIXTURES = 512


class CertificateError(RuntimeError):
    pass


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def _prefix_sums(row: Mapping[int, F]) -> dict[int, F]:
    running = F(0)
    result: dict[int, F] = {}
    for scale in SCALES:
        running += row[scale]
        result[scale] = running
    return result


def _band(C: Mapping[tuple[int, int], F], prefix: int, scale: int) -> F:
    return C[prefix, scale] - C[prefix, scale + 1]


def _delta(C: Mapping[tuple[int, int], F], epoch: int, scale: int) -> F:
    return C[2 * epoch, scale] - C[epoch, scale]


def _row_label(key: tuple[str, int, int]) -> str:
    kind, index, scale = key
    return f"{kind}:A{index}:s{scale}" if kind == "band" else f"terminal:e{index}:s{scale}"


def _row_owner(key: tuple[str, int, int]) -> str:
    kind, index, _ = key
    if kind == "band":
        return {8: "past_epoch4", 16: "epoch8", 32: "epoch16"}[index]
    if kind == "terminal":
        return {8: "epoch8", 16: "epoch16"}[index]
    raise CertificateError(f"unknown row key {key!r}")


def adjacent_ledger(
    C: Mapping[tuple[int, int], F],
    coefficients: Mapping[int, Mapping[int, F]],
    weights: Mapping[int, F],
) -> dict[str, Any]:
    """Verify the 14-row identity and the exact two-edge stitch."""

    S = {epoch: _prefix_sums(coefficients[epoch]) for epoch in EPOCHS}
    lhs = sum(
        (
            weights[epoch]
            * coefficients[epoch][scale]
            * _delta(C, epoch, scale)
            for epoch in EPOCHS
            for scale in SCALES
        ),
        F(0),
    )

    rows: dict[tuple[str, int, int], F] = {}
    for scale in SCALES:
        rows["band", 8, scale] = (
            -weights[8] * S[8][scale] * _band(C, 8, scale)
        )
        rows["band", 16, scale] = (
            (weights[8] * S[8][scale] - weights[16] * S[16][scale])
            * _band(C, 16, scale)
        )
        rows["band", 32, scale] = (
            weights[16] * S[16][scale] * _band(C, 32, scale)
        )
    rows["terminal", 8, UPPER_SCALE] = (
        weights[8] * S[8][3] * _delta(C, 8, UPPER_SCALE)
    )
    rows["terminal", 16, UPPER_SCALE] = (
        weights[16] * S[16][3] * _delta(C, 16, UPPER_SCALE)
    )

    if len(rows) != 14:
        raise CertificateError("the frozen C103 specialization lost a row")
    rhs = sum(rows.values(), F(0))
    if lhs != rhs:
        raise CertificateError("the exact adjacent-epoch Abel identity failed")

    occurrences: list[tuple[tuple[str, int, int], F]] = []
    for epoch in EPOCHS:
        left, right = epoch, 2 * epoch
        for scale in SCALES:
            occurrences.append((
                ("band", left, scale),
                -weights[epoch] * S[epoch][scale] * _band(C, left, scale),
            ))
            occurrences.append((
                ("band", right, scale),
                weights[epoch] * S[epoch][scale] * _band(C, right, scale),
            ))
        occurrences.append((
            ("terminal", epoch, UPPER_SCALE),
            weights[epoch] * S[epoch][3] * _delta(C, epoch, UPPER_SCALE),
        ))
    if len(occurrences) != 18:
        raise CertificateError("two one-edge ledgers no longer have 18 occurrences")

    stitched: defaultdict[tuple[str, int, int], F] = defaultdict(F)
    multiplicity: defaultdict[tuple[str, int, int], int] = defaultdict(int)
    for key, value in occurrences:
        stitched[key] += value
        multiplicity[key] += 1
    if dict(stitched) != rows:
        raise CertificateError("the 18-occurrence ledger did not stitch to 14 rows")
    duplicates = {key: count for key, count in multiplicity.items() if count > 1}
    expected_duplicates = {("band", 16, scale): 2 for scale in SCALES}
    if duplicates != expected_duplicates:
        raise CertificateError("only the four A16 rows may repeat before stitching")

    return {
        "lhs": lhs,
        "rhs": rhs,
        "rows": rows,
        "row_owners": {key: _row_owner(key) for key in rows},
        "raw_occurrence_count": len(occurrences),
        "unique_row_count": len(rows),
        "shared_A16_premerge_multiplicity": tuple(
            multiplicity["band", 16, scale] for scale in SCALES
        ),
    }


def birth_atom_audit(
    birth_epoch: int,
    values: Mapping[int, F],
    allocations: Mapping[int, F],
    weights: Mapping[int, F],
) -> dict[str, Any]:
    """Check one owner-labelled atom with coefficients only at its birth."""

    if birth_epoch not in EPOCHS:
        raise CertificateError("birth epoch must be 8 or 16")
    C = {
        (prefix, scale): (
            values[scale] if prefix >= 2 * birth_epoch else F(0)
        )
        for prefix in PREFIXES
        for scale in range(5)
    }
    coefficients = {
        epoch: {
            scale: allocations[scale] if epoch == birth_epoch else F(0)
            for scale in SCALES
        }
        for epoch in EPOCHS
    }
    audit = adjacent_ledger(C, coefficients, weights)
    S = _prefix_sums(allocations)
    o = {scale: values[scale] - values[scale + 1] for scale in SCALES}
    initial = tuple(audit["rows"]["band", 8, scale] for scale in SCALES)
    shared = tuple(audit["rows"]["band", 16, scale] for scale in SCALES)
    final = tuple(audit["rows"]["band", 32, scale] for scale in SCALES)
    if initial != (F(0),) * 4:
        raise CertificateError("a birth-resolved atom has a nonzero A8 initial row")

    if birth_epoch == 8:
        expected_shared = tuple(weights[8] * S[s] * o[s] for s in SCALES)
        if shared != expected_shared or final != (F(0),) * 4:
            raise CertificateError("epoch-8 birth was not placed on the A16 row")
        if audit["rows"]["terminal", 16, UPPER_SCALE] != 0:
            raise CertificateError("epoch-8 atom acquired an epoch-16 terminal")
        active_band = "A16_shared_birth"
        prebirth_A16_zero = None
    else:
        expected_final = tuple(weights[16] * S[s] * o[s] for s in SCALES)
        if shared != (F(0),) * 4 or final != expected_final:
            raise CertificateError("epoch-16 birth was not placed on the A32 final row")
        if audit["rows"]["terminal", 8, UPPER_SCALE] != 0:
            raise CertificateError("epoch-16 atom acquired an epoch-8 terminal")
        active_band = "A32_final_birth"
        prebirth_A16_zero = True

    return {
        "birth_epoch": birth_epoch,
        "active_band": active_band,
        "initial_A8_zero": True,
        "prebirth_A16_zero": prebirth_A16_zero,
        "other_epoch_terminal_zero": True,
        "upper_terminal": audit["rows"]["terminal", birth_epoch, UPPER_SCALE],
    }


def coordinate_owner(rank: int) -> str:
    if rank == 7:
        return "past_epoch4"
    if 8 <= rank <= 15:
        return "epoch8"
    if 16 <= rank <= 31:
        return "epoch16"
    raise CertificateError("rank is outside the frozen rank-7 through rank-31 union")


def coordinate_owner_audit() -> dict[str, Any]:
    coordinates = tuple(
        (rank, multiplier)
        for multiplier in MULTIPLIERS
        for rank in range(7, 32)
    )
    fibers: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)
    for coordinate in coordinates:
        fibers[coordinate_owner(coordinate[0])].append(coordinate)
    counts = {owner: len(rows) for owner, rows in fibers.items()}
    if counts != {"past_epoch4": 4, "epoch8": 32, "epoch16": 64}:
        raise CertificateError("the 100-coordinate owner partition changed")
    if any(coordinate_owner(15) != "epoch8" for _ in MULTIPLIERS):
        raise CertificateError("shared rank 15 lost past-epoch ownership")

    # Independent-block zero-row-sum Gram example; rank 15 is deliberately live.
    v8: defaultdict[tuple[int, int], F] = defaultdict(F)
    v8[8, 1], v8[15, 1] = F(1), F(-1)
    v16: defaultdict[tuple[int, int], F] = defaultdict(F)
    v16[16, 1], v16[31, 1] = F(2), F(-2)
    q: defaultdict[tuple[int, int], F] = defaultdict(F)
    q[8, 1], q[15, 1] = F(2), F(1)
    q[16, 1], q[31, 1] = F(3), F(1)

    def entry(i: tuple[int, int], j: tuple[int, int]) -> F:
        return v8[i] * v8[j] + v16[i] * v16[j]

    def coordinate_row(i: tuple[int, int]) -> F:
        return q[i] * sum((entry(i, j) * q[j] for j in coordinates), F(0))

    energy = sum((coordinate_row(i) for i in coordinates), F(0))
    shares = {
        owner: sum((coordinate_row(i) for i in rows), F(0))
        for owner, rows in fibers.items()
    }
    if sum(shares.values(), F(0)) != energy:
        raise CertificateError("owner fibers no longer recover q^T X q")
    rank15_row = coordinate_row((15, 1))
    if rank15_row == 0:
        raise CertificateError("the verifier accidentally imposed right-zero")

    return {
        "rank_range": [7, 31],
        "multipliers": list(MULTIPLIERS),
        "coordinate_count": len(coordinates),
        "fiber_counts": counts,
        "shared_rank15_owner": "epoch8",
        "shared_rank15_scale_count": 4,
        "rank15_example_coordinate_row": ftext(rank15_row),
        "example_energy": ftext(energy),
        "example_owner_shares": {owner: ftext(value) for owner, value in shares.items()},
        "right_zero_used": False,
    }


def _random_fraction(rng: random.Random) -> F:
    return F(rng.randint(-17, 17), rng.randint(1, 19))


def random_fixture_audit(count: int = RANDOM_FIXTURES, seed: int = RANDOM_SEED) -> None:
    rng = random.Random(seed)
    for _ in range(count):
        C = {
            (prefix, scale): _random_fraction(rng)
            for prefix in PREFIXES
            for scale in range(5)
        }
        coefficients = {
            epoch: {scale: _random_fraction(rng) for scale in SCALES}
            for epoch in EPOCHS
        }
        weights = {epoch: _random_fraction(rng) for epoch in EPOCHS}
        adjacent_ledger(C, coefficients, weights)

        values = {scale: _random_fraction(rng) for scale in range(5)}
        allocations = {scale: _random_fraction(rng) for scale in SCALES}
        birth_atom_audit(8, values, allocations, weights)
        birth_atom_audit(16, values, allocations, weights)


def _deterministic_fixture() -> dict[str, Any]:
    C = {
        (prefix, scale): F(
            prefix + 4 * scale + (prefix // 8) * scale * scale,
            scale + 2,
        )
        for prefix in PREFIXES
        for scale in range(5)
    }
    coefficients = {
        8: {
            scale: F((scale + 1) * (-1 if scale == 2 else 1), scale + 3)
            for scale in SCALES
        },
        16: {scale: F(2 * scale - 3, scale + 5) for scale in SCALES},
    }
    weights = {8: F(25, 49), 16: F(9, 49)}
    audit = adjacent_ledger(C, coefficients, weights)
    if any(value == 0 for value in audit["rows"].values()):
        raise CertificateError("the minimality fixture lost a nonzero formal row")
    return audit


def _jsonify(value: Any) -> Any:
    if isinstance(value, F):
        return ftext(value)
    if isinstance(value, tuple):
        return [_jsonify(item) for item in value]
    if isinstance(value, list):
        return [_jsonify(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _jsonify(item) for key, item in value.items()}
    return value


def payload_hash(certificate: Mapping[str, Any]) -> str:
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_certificate() -> dict[str, Any]:
    random_fixture_audit()
    fixture = _deterministic_fixture()
    owner = coordinate_owner_audit()
    values = {
        0: F(9, 2), 1: F(7, 3), 2: F(5, 4), 3: F(4, 5), 4: F(3, 7)
    }
    allocations = {0: F(1, 3), 1: F(-2, 5), 2: F(4, 7), 3: F(5, 9)}
    weights = {8: F(25, 49), 16: F(9, 49)}
    birth8 = birth_atom_audit(8, values, allocations, weights)
    birth16 = birth_atom_audit(16, values, allocations, weights)

    rows = {
        _row_label(key): ftext(value)
        for key, value in fixture["rows"].items()
    }
    row_owners = {
        _row_label(key): value for key, value in fixture["row_owners"].items()
    }
    certificate: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "theorem_contract": {
            "C103_specialization": "L=0,m=1,n=4; edges 8,16; prefixes A8,A16,A32",
            "delta8": "C_A16,s-C_A8,s",
            "delta16": "C_A32,s-C_A16,s",
            "scale_prefix": "S_e,s=sum_(u=0)^s c_e,u",
            "shared_A16_coefficient": "w8*S8,s-w16*S16,s",
            "row_count": "4 initial + 4 shared + 4 final + 2 upper-terminal = 14",
            "upper_terminal_width": "16t",
            "right_zero_assumption": False,
        },
        "ledger_audit": {
            "active_scale_indices": list(SCALES),
            "active_widths": ["t", "2t", "4t", "8t"],
            "upper_terminal_scale_index": UPPER_SCALE,
            "upper_terminal_width": "16t",
            "initial_A8_rows": 4,
            "shared_A16_rows": 4,
            "final_A32_rows": 4,
            "upper_terminal_rows": 2,
            "raw_one_edge_occurrences": fixture["raw_occurrence_count"],
            "unique_stitched_rows": fixture["unique_row_count"],
            "shared_A16_premerge_multiplicity": list(
                fixture["shared_A16_premerge_multiplicity"]
            ),
            "shared_A16_postmerge_multiplicity": [1, 1, 1, 1],
            "fixture_lhs": ftext(fixture["lhs"]),
            "fixture_rhs": ftext(fixture["rhs"]),
            "every_fixture_row_nonzero": True,
            "fixture_rows": rows,
            "fixture_row_owners": row_owners,
            "random_fraction_fixtures": RANDOM_FIXTURES,
            "random_seed": RANDOM_SEED,
        },
        "coordinate_owner_audit": owner,
        "birth_audit": {
            "epoch8": _jsonify(birth8),
            "epoch16": _jsonify(birth16),
            "unique_birth_hypothesis_required": True,
            "birth_supported_coefficients_required": True,
            "aggregate_C130_C131_decomposition_proved": False,
        },
        "scope": {
            "finite_C103_specialization_only": True,
            "exact_14_row_identity_verified": True,
            "exact_18_to_14_stitch_verified": True,
            "coordinate_partition_verified": True,
            "rank15_right_zero_used": False,
            "sign_or_capacity_claimed": False,
            "nonanticipating_phase_rule_proved": False,
            "PSD_master_inequality_proved": False,
            "C130_C131_global_compatibility_proved": False,
            "fresh_epoch16_factor_constructed": False,
            "arbitrary_history_proved": False,
            "arbitrary_rank_proved": False,
            "C058_resolved": False,
            "Q1_Q2_resolved": False,
            "prize_claim_ready": False,
        },
    }
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate)}
    return certificate


def _strict_equal(actual: Any, expected: Any, path: str = "root") -> None:
    if type(actual) is not type(expected):
        raise CertificateError(f"{path}: exact type changed")
    if isinstance(expected, dict):
        if set(actual) != set(expected):
            raise CertificateError(f"{path}: key set changed")
        for key in expected:
            _strict_equal(actual[key], expected[key], f"{path}.{key}")
        return
    if isinstance(expected, list):
        if len(actual) != len(expected):
            raise CertificateError(f"{path}: list length changed")
        for index, (left, right) in enumerate(zip(actual, expected)):
            _strict_equal(left, right, f"{path}[{index}]")
        return
    if actual != expected:
        raise CertificateError(f"{path}: value changed")


def validate_certificate(certificate: Mapping[str, Any]) -> dict[str, Any]:
    if type(certificate) is not dict:
        raise CertificateError("certificate must be an exact dictionary")
    integrity = certificate.get("integrity")
    if type(integrity) is not dict:
        raise CertificateError("integrity record missing")
    if integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")
    expected = build_certificate()
    _strict_equal(certificate, expected)
    return {
        "status": STATUS,
        "unique_rows": 14,
        "raw_occurrences": 18,
        "random_fixtures": RANDOM_FIXTURES,
        "shared_rank15_owner": "epoch8",
        "C058_open": True,
    }


def rehash(certificate: dict[str, Any]) -> None:
    certificate["integrity"] = {"payload_sha256": payload_hash(certificate)}


def mutation_self_check(certificate: Mapping[str, Any] | None = None) -> dict[str, Any]:
    baseline = build_certificate() if certificate is None else deepcopy(certificate)
    validate_certificate(baseline)

    mutations: list[tuple[str, Any]] = []

    changed = deepcopy(baseline)
    changed["scope"]["C058_resolved"] = True
    mutations.append(("scope_upgrade", changed))

    changed = deepcopy(baseline)
    changed["ledger_audit"]["unique_stitched_rows"] = 15
    mutations.append(("row_count", changed))

    changed = deepcopy(baseline)
    changed["ledger_audit"]["shared_A16_postmerge_multiplicity"][0] = 2
    mutations.append(("A16_double_owner", changed))

    changed = deepcopy(baseline)
    changed["coordinate_owner_audit"]["shared_rank15_owner"] = "epoch16"
    changed["coordinate_owner_audit"]["right_zero_used"] = True
    mutations.append(("rank15_owner_or_right_zero", changed))

    changed = deepcopy(baseline)
    changed["ledger_audit"]["upper_terminal_rows"] = 0
    mutations.append(("upper_terminal_drop", changed))

    changed = deepcopy(baseline)
    changed["birth_audit"]["epoch16"]["prebirth_A16_zero"] = False
    mutations.append(("birth_prestate", changed))

    changed = deepcopy(baseline)
    changed["ledger_audit"]["fixture_lhs"] = "0/1"
    mutations.append(("fixture_identity", changed))

    changed = deepcopy(baseline)
    changed["ledger_audit"]["unique_stitched_rows"] = 14.0
    mutations.append(("exact_type", changed))

    rejected: list[str] = []
    for name, changed in mutations:
        rehash(changed)
        try:
            validate_certificate(changed)
        except CertificateError:
            rejected.append(name)
        else:
            raise CertificateError(f"mutation was accepted: {name}")
    return {
        "normal_verified": 1,
        "mutations_attempted": len(mutations),
        "mutations_rejected": len(rejected),
        "cases": rejected,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-check", action="store_true", help="also run the mutation barrier"
    )
    args = parser.parse_args()
    certificate = build_certificate()
    summary = validate_certificate(certificate)
    if args.self_check:
        mutations = mutation_self_check(certificate)
        print(
            "MUTATION_OK "
            f"rejected={mutations['mutations_rejected']}/{mutations['mutations_attempted']}"
        )
    print(
        "VERIFY_OK C133 "
        f"rows={summary['unique_rows']} raw={summary['raw_occurrences']} "
        f"random={summary['random_fixtures']} rank15_owner=epoch8 "
        "C103_specialization_only C058_open"
    )


if __name__ == "__main__":
    main()

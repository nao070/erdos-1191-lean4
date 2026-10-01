#!/usr/bin/env python3
"""Exact scoped dual no-go for a lacunary four-width epoch-block master.

The numerical SDP was used only to discover the dual weights embedded below.
Every certificate claim is reconstructed with ``fractions.Fraction``.  The
fixture is the exponential Golomb ruler ``a_k=2^k-1`` and is *not* an
eventual fixed-C critical history.  Consequently this closes only a
geometry-free universal extension of the fixed-history epoch-block PSD
mechanism; it does not close C058 or either Erdős question.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

import direct_b_membership_sddm_lp_certificate as membership


SCHEMA = "erdos1191.route_c_lacunary_epoch_block_dual_no_go.v1"
STATUS = "EXACT_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_GLOBAL_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_certificate.json"

POINTS = tuple((1 << rank) - 1 for rank in range(16))
MULTIPLIERS = (1, 2, 4, 8)
CHANNELS = tuple(
    (rank, multiplier, POINTS[rank])
    for multiplier in MULTIPLIERS
    for rank in range(3, 16)
)
T = 6096
BASE_SCALE = F(POINTS[15] - POINTS[8], 8)
NORMALIZED_PHASE = F(3, 2)
FEJER_RATIO = F(9, 16)
DUAL_DENOMINATOR = 100000

# Discovered with an SDP solver, then uniformly halved and rounded.  The
# resulting vector is only accepted after exact nonnegativity, objective,
# and positive-definite dual-slack checks below.
DUAL_NUMERATORS = (
    104917,104917,104917,104917,104917,104917,104917,104917,104917,104917,
    104917,104917,104917,104917,104917,104917,104917,104917,104917,104917,
    191,1,1209,5374,519,7,1504,5556,918,20,417,8011,10212,4,2366,15165,
    0,5506,1115,1053,0,5498,1115,1052,0,5516,1115,1052,0,5516,1115,
    1052,0,5516,1115,1053,30639,5516,1115,1053,2537,1980,1929,2418,
    4725,3985,3978,5298,8822,7590,6962,13176,0,0,3,7357,13907,625,0,
    16609,0,0,4925,5353,0,0,4928,5307,0,0,4928,5307,0,0,4938,5307,
    0,0,4938,5307,0,52370,4938,5323,1329,1935,2065,2776,3109,4085,
    4173,5374,4668,8070,5887,7818,0,0,2483,0,7174,18129,6215,12,8984,
    0,0,11257,4,16945,0,49608,1666,0,0,31263,0,0,0,1724,0,0,0,1724,
    0,0,0,1721,0,0,0,1721,0,0,0,1723,0,3385,34713,1723,1463,2988,
    1197,1264,4107,4682,3531,4080,7403,8175,7812,9901,8766,0,14479,2,
    3793,0,0,2797,104917,20426,35884,31176,104917,5,0,0,2,16433,24399,
    17,0,0,13680,22314,62862,42476,0,908,104917,0,0,4213,104917,0,0,
    4224,104917,0,0,4223,104917,0,0,4221,104917,0,0,4218,104917,0,
    72005,4217,104917,0,4040,789,104917,2,5292,3403,104917,6319,7801,
    9045,104917,16766,8381,12388,104917,6225,21373,22714,104917,1,0,
    3796,104917,104917,8,10118,104917,104917,35,43944,104917,104917,
    104917,6,104917,104917,104917,6,104917,104917,104917,6,104917,
    104917,104917,6,104917,104917,104917,6,104917,104917,104917,6,
    104917,104917,104917,2,104917,104917,104917,1,104917,104917,104917,
    1,104917,104917,104917,0,104917,104917,104917,1,104917,104917,
    104917,2,104917,104917,104917,1,
)


class CertificateError(RuntimeError):
    """Raised when exact replay or a scope gate changes."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")


def _canonical_hash(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    if tuple(points) != tuple(sorted(set(points))):
        raise CertificateError("fixture points are not strictly increasing")
    differences = tuple(
        points[right] - points[left]
        for left in range(len(points))
        for right in range(left + 1, len(points))
    )
    if len(differences) != len(set(differences)):
        raise CertificateError("fixture is not a Golomb ruler")
    return tuple(sorted(differences))


def _haar_sign(x: F, origin: int, multiplier: int) -> int:
    displacement = x - origin
    width = multiplier * T
    if 0 <= displacement < width:
        return 1
    if width <= displacement < 2 * width:
        return -1
    return 0


def _state(x: F) -> tuple[int, ...]:
    return tuple(
        (8 // multiplier) * _haar_sign(x, origin, multiplier)
        for _, multiplier, origin in CHANNELS
    )


def _cells() -> tuple[tuple[F, F, tuple[int, ...]], ...]:
    events = tuple(
        sorted(
            {
                F(origin + shift * multiplier * T)
                for _, multiplier, origin in CHANNELS
                for shift in (0, 1, 2)
            }
        )
    )
    cells = tuple(
        (left, right, _state((left + right) / 2))
        for left, right in zip(events, events[1:])
    )
    if len(events) != 78 or len(cells) != 77:
        raise CertificateError("event or cell census changed")
    return cells


def _epoch_indices(n: int) -> tuple[int, ...]:
    if n == 4:
        return tuple(
            index for index, (rank, _, _) in enumerate(CHANNELS) if rank <= 7
        )
    if n == 8:
        return tuple(
            index for index, (rank, _, _) in enumerate(CHANNELS) if rank >= 8
        )
    raise ValueError("only n=4 and n=8 occur in this fixture")


def _project(vector: Sequence[F | int], indices: Sequence[int]) -> tuple[F, ...]:
    local = tuple(F(vector[index]) for index in indices)
    return tuple(value - local[-1] for value in local[:-1])


def _owner_indices(n: int, multiplier: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    full_ranks = range(3, 8) if n == 4 else range(7, 16)
    group_ranks = range(3, 8) if n == 4 else range(8, 16)
    full = tuple(
        CHANNELS.index((rank, multiplier, POINTS[rank])) for rank in full_ranks
    )
    group = tuple(
        CHANNELS.index((rank, multiplier, POINTS[rank])) for rank in group_ranks
    )
    return full, group


def _zero_matrix(size: int) -> list[list[F]]:
    return [[F(0) for _ in range(size)] for _ in range(size)]


def _epoch_problem(
    n: int,
) -> tuple[list[list[F]], tuple[tuple[tuple[tuple[F, ...], ...], F], ...], F]:
    block = _epoch_indices(n)
    dimension = len(block) - 1
    physical = _zero_matrix(dimension)
    rows: list[tuple[tuple[tuple[F, ...], ...], F]] = []
    demand = F(0)
    point_matrix = membership.point_m_matrix(n)
    for left, right, state in _cells():
        length = right - left
        y = _project(state, block)
        for i in range(dimension):
            for j in range(dimension):
                physical[i][j] += length * y[i] * y[j] / T
        for multiplier in MULTIPLIERS:
            full, group = _owner_indices(n, multiplier)
            local = tuple(state[index] for index in full)
            c = F(multiplier, 128) * membership.quadratic(point_matrix, local)
            group_vector = [F(0) for _ in CHANNELS]
            for index in group:
                group_vector[index] = state[index]
            z = _project(group_vector, block)
            matrix = tuple(
                tuple((z[i] * y[j] + y[i] * z[j]) / 2 for j in range(dimension))
                for i in range(dimension)
            )
            rows.append((matrix, c))
            demand += length * c / T
    return physical, tuple(rows), demand


def _ldl_pivots(matrix: Sequence[Sequence[F]]) -> tuple[F, ...]:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise CertificateError("LDL matrix is not square")
    lower = _zero_matrix(size)
    for i in range(size):
        lower[i][i] = F(1)
    pivots: list[F] = []
    for i in range(size):
        pivot = F(matrix[i][i]) - sum(
            (lower[i][k] * lower[i][k] * pivots[k] for k in range(i)),
            F(0),
        )
        if pivot <= 0:
            raise CertificateError(f"dual slack lost positive definiteness at pivot {i}")
        pivots.append(pivot)
        for j in range(i + 1, size):
            lower[j][i] = (
                F(matrix[j][i])
                - sum(
                    (lower[j][k] * lower[i][k] * pivots[k] for k in range(i)),
                    F(0),
                )
            ) / pivot
    return tuple(pivots)


@lru_cache(maxsize=1)
def _replay() -> dict[str, Any]:
    differences = _positive_differences(POINTS)
    if len(differences) != 120:
        raise CertificateError("positive-difference census changed")
    if BASE_SCALE != 4064 or NORMALIZED_PHASE * BASE_SCALE != T:
        raise CertificateError("normalized phase geometry changed")

    _, rows4, demand4 = _epoch_problem(4)
    physical8, rows8, demand8 = _epoch_problem(8)
    if len(rows4) != 308 or len(rows8) != 308:
        raise CertificateError("owner-row census changed")
    if demand4 != 0 or any(c != 0 for _, c in rows4):
        raise CertificateError("epoch-4 demand is no longer identically zero")
    if len(DUAL_NUMERATORS) != len(rows8):
        raise CertificateError("dual-vector length changed")
    if any(type(value) is not int or value < 0 for value in DUAL_NUMERATORS):
        raise CertificateError("dual weights must be nonnegative integers")

    weights = tuple(F(value, DUAL_DENOMINATOR) for value in DUAL_NUMERATORS)
    slack = [[value for value in row] for row in physical8]
    for weight, (matrix, _) in zip(weights, rows8):
        if not weight:
            continue
        for i in range(31):
            for j in range(31):
                slack[i][j] -= weight * matrix[i][j]
    if any(slack[i][j] != slack[j][i] for i in range(31) for j in range(31)):
        raise CertificateError("dual slack lost symmetry")
    pivots = _ldl_pivots(slack)
    objective = sum(
        (weight * row[1] for weight, row in zip(weights, rows8)), F(0)
    )
    gap = objective - 2 * demand8
    if demand8 != F(981, 16256):
        raise CertificateError("epoch-8 integrated demand changed")
    if objective != F(370911, 2560000):
        raise CertificateError("dual objective changed")
    if gap != F(7865697, 325120000) or gap <= 0:
        raise CertificateError("strict dual obstruction changed")
    phi_upper = -FEJER_RATIO * gap
    if phi_upper != -F(70791273, 5201920000):
        raise CertificateError("Fejer-weighted upper bound changed")

    pivot_text = tuple(ftext(value) for value in pivots)
    return {
        "schema": SCHEMA,
        "status": STATUS,
        "generated_on": "2026-08-30",
        "arithmetic": "fractions.Fraction exact rational arithmetic",
        "fixture": {
            "formula": "a_k=2^k-1 for 0<=k<=15",
            "points": list(POINTS),
            "positive_difference_count": len(differences),
            "all_positive_differences_distinct": True,
            "channels": len(CHANNELS),
            "multipliers": list(MULTIPLIERS),
            "base_scale": ftext(BASE_SCALE),
            "normalized_phase_factor": ftext(NORMALIZED_PHASE),
            "t": ftext(T),
            "event_count": 78,
            "cell_count": 77,
        },
        "epoch4": {
            "projected_dimension": 19,
            "owner_row_count": len(rows4),
            "all_owner_demands_zero": True,
            "integrated_demand": ftext(demand4),
            "zero_correction_is_feasible": True,
        },
        "epoch8": {
            "projected_dimension": 31,
            "owner_row_count": len(rows8),
            "integrated_demand": ftext(demand8),
            "twice_integrated_demand": ftext(2 * demand8),
        },
        "dual": {
            "denominator": DUAL_DENOMINATOR,
            "weight_numerators": list(DUAL_NUMERATORS),
            "nonnegative_weight_count": len(weights),
            "positive_weight_count": sum(value > 0 for value in weights),
            "zero_weight_count": sum(value == 0 for value in weights),
            "objective": ftext(objective),
            "objective_minus_twice_demand": ftext(gap),
            "slack_dimension": 31,
            "ldl_positive_pivot_count": len(pivots),
            "minimum_positive_pivot": ftext(min(pivots)),
            "ldl_pivots_sha256": _canonical_hash(pivot_text),
            "weak_duality_conclusion": "every feasible epoch-8 PSD correction has P8>=dual objective>2D8",
        },
        "fejer": {
            "worst_ratio": ftext(FEJER_RATIO),
            "ratio_range_covered": "rho in [9/16,1]",
            "epoch4_contribution": "0/1",
            "certified_phi_upper_bound": ftext(phi_upper),
            "strictly_negative_for_every_ratio_in_range": True,
        },
        "scope": {
            "single_fixed_lacunary_history": True,
            "single_normalized_phase_point": True,
            "aggregate_four_width_owner_rows_only": True,
            "epoch_block_zero_row_sum_PSD_cone_only": True,
            "cross_epoch_blocks_allowed": False,
            "geometry_free_epoch_block_positivity_refuted": True,
            "eventual_fixed_C_critical_history": False,
            "reason_not_eventual_fixed_C_critical": "2^k eventually exceeds 2*C*k^2*log(k) for every fixed C",
            "compatible_critical_history_counterexample": False,
            "C058_resolved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "publication_novelty_established": False,
            "prize_claim_supported": False,
        },
        "verification": {
            "source_sha256": _file_sha256(Path(__file__)),
            "mutation_rejection_count": 12,
        },
    }


def build_certificate() -> dict[str, Any]:
    payload = copy.deepcopy(_replay())
    payload["payload_sha256"] = _canonical_hash(payload)
    return payload


def verify_certificate(payload: Mapping[str, Any]) -> bool:
    if not isinstance(payload, Mapping):
        raise CertificateError("certificate must be a mapping")
    expected = build_certificate()
    if _canonical_bytes(payload) != _canonical_bytes(expected):
        raise CertificateError("certificate differs from exact canonical replay")
    if payload.get("payload_sha256") != _canonical_hash(
        {key: value for key, value in payload.items() if key != "payload_sha256"}
    ):
        raise CertificateError("payload hash mismatch")
    return True


def run_mutation_suite() -> int:
    baseline = build_certificate()
    mutators: tuple[Callable[[dict[str, Any]], None], ...] = (
        lambda value: value["fixture"]["points"].__setitem__(15, 32766),
        lambda value: value["fixture"].__setitem__("t", "6095/1"),
        lambda value: value["epoch4"].__setitem__("integrated_demand", "1/1"),
        lambda value: value["epoch8"].__setitem__("integrated_demand", "980/16256"),
        lambda value: value["dual"]["weight_numerators"].__setitem__(0, 104918),
        lambda value: value["dual"].__setitem__("denominator", 99999),
        lambda value: value["dual"].__setitem__("objective", "370912/2560000"),
        lambda value: value["dual"].__setitem__("ldl_positive_pivot_count", 30),
        lambda value: value["fejer"].__setitem__("certified_phi_upper_bound", "0/1"),
        lambda value: value["scope"].__setitem__("eventual_fixed_C_critical_history", True),
        lambda value: value["scope"].__setitem__("C058_resolved", True),
        lambda value: value.__setitem__("payload_sha256", "0" * 64),
    )
    rejected = 0
    for mutate in mutators:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        try:
            verify_certificate(candidate)
        except CertificateError:
            rejected += 1
    if rejected != len(mutators):
        raise CertificateError("mutation suite did not reject every semantic change")
    return rejected


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-json", type=Path)
    parser.add_argument("--verify-json", type=Path)
    parser.add_argument("--mutations", action="store_true")
    args = parser.parse_args(argv)

    payload = build_certificate()
    if args.write_json is not None:
        _write_json(args.write_json, payload)
    if args.verify_json is not None:
        verify_certificate(json.loads(args.verify_json.read_text(encoding="utf-8")))
    if args.mutations:
        run_mutation_suite()
    print(
        STATUS,
        "dual_gap=" + payload["dual"]["objective_minus_twice_demand"],
        "phi_upper=" + payload["fejer"]["certified_phi_upper_bound"],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

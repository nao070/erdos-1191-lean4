#!/usr/bin/env python3
"""Exact finite 32-mark stress of the naive C130/C131 affine paste.

The accepted conclusions are deliberately narrow.  The explicit 32-mark
integer ruler is Golomb and satisfies the finite onset-4 C=2 envelope, but a
pinned C130 chamber factor fails the *natural* epoch-16 owner rows after the
obvious affine embedding.  The script also reconstructs the 63-source
cross-half residual omitted by two quarter-scaled M8 blocks.

All load-bearing arithmetic uses integers or ``fractions.Fraction``.  This is
not a C058, arbitrary-rank, infinite-history, Q1, or Q2 certificate.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence


STATUS = "EXACT_FINITE_COMPOSITE32_NAIVE_LOCAL_BANK_PASTE_NO_GO_C058_OPEN"
HERE = Path(__file__).resolve().parent
C130_JSON = HERE / "ROUTE_C_C130_COMPLETE_C123_PHASE_PRIMAL_certificate.json"
C131_JSON = HERE / "ROUTE_C_C131_COMPLETE_C120_PHASE_PRIMAL_certificate.json"
C130_SHA256 = "16dec361580b0f070c660a12f8f3f60a57baff0bbf10ae9e5c2f8e4ae13fb37d"
C131_SHA256 = "6b28874a6c0ffe3d36a5ada27a3b466e0dbcd19447a2da0fb501b0ccc7df5afc"

C120 = (
    0, 22, 60, 83, 102, 173, 303, 513,
    616, 727, 772, 881, 972, 1041, 1103, 1169,
)
C123 = (
    0, 22, 60, 83, 154, 284, 494, 513,
    575, 620, 711, 777, 880, 989, 1100, 1169,
)
COMPOSITE = C120 + tuple(1239 + 5 * x for x in C123)
MULTIPLIERS = (1, 2, 4, 8)
LOG_TERMS = 240


class CertificateError(RuntimeError):
    pass


def ftext(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    if any(type(x) is not int for x in points):
        raise CertificateError("marks must be integers")
    if any(x >= y for x, y in zip(points, points[1:])):
        raise CertificateError("marks must be strictly increasing")
    return tuple(
        points[j] - points[i]
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )


def log_interval_integer(value: int) -> tuple[F, F]:
    """A rational atanh-series enclosure for log(value), value >= 1."""
    if value < 1:
        raise CertificateError("log input must be positive")
    z = F(value - 1, value + 1)
    lower = 2 * sum(
        (z ** (2 * k + 1) / (2 * k + 1) for k in range(LOG_TERMS)), F()
    )
    tail = 2 * z ** (2 * LOG_TERMS + 1) / (
        (2 * LOG_TERMS + 1) * (1 - z * z)
    )
    return lower, lower + tail


def composite_and_cap_audit() -> dict[str, Any]:
    differences = positive_differences(COMPOSITE)
    if len(differences) != 496 or len(set(differences)) != 496:
        raise CertificateError("the pinned 32-mark composite is not Golomb")

    required_c: dict[int, tuple[F, F]] = {}
    slacks: dict[int, F] = {}
    for m in range(4, 33):
        lower_log, upper_log = log_interval_integer(m)
        n_m = COMPOSITE[m - 1] + 1
        required_log = F(n_m, 4 * m * m)
        slacks[m] = lower_log - required_log
        required_c[m] = (
            F(n_m, 2 * m * m) / upper_log,
            F(n_m, 2 * m * m) / lower_log,
        )
    if min(slacks.values()) <= F(7, 100):
        raise CertificateError("clean finite C=2 cap slack disappeared")
    separated_maxima = [
        m for m, (lower, _) in required_c.items()
        if all(other == m or upper < lower for other, (_, upper) in required_c.items())
    ]
    if separated_maxima != [8]:
        raise CertificateError("worst required-C prefix is not uniquely m=8")
    worst_lower, worst_upper = required_c[8]
    if not F(1931, 1000) < worst_lower <= worst_upper < F(483, 250):
        raise CertificateError("clean worst required-C fence changed")
    terminal_lower, terminal_upper = required_c[32]
    if not F(499, 500) < terminal_lower <= terminal_upper < F(999, 1000):
        raise CertificateError("clean terminal required-C fence changed")
    return {
        "points": list(COMPOSITE),
        "mark_count": 32,
        "span": COMPOSITE[-1],
        "positive_differences": 496,
        "distinct_positive_differences": 496,
        "finite_cap_formula": "N_m <= 2*C*m^2*log(m)",
        "finite_cap_C": 2,
        "finite_cap_onset": 4,
        "finite_cap_last_prefix": 32,
        "finite_cap_rows_checked": 29,
        "minimum_certified_log_slack_greater_than": "7/100",
        "worst_required_C_prefix": 8,
        "worst_required_C_inside": ["1931/1000", "483/250"],
        "terminal_required_C_inside": ["499/500", "999/1000"],
        "finite_only_disclaimer": (
            "m=2,3 are outside the onset audit; no infinite compatible branch is claimed"
        ),
    }


def wave_b(n: int) -> tuple[tuple[F, ...], ...]:
    return tuple(tuple(
        F() if i == j or abs(i - j) == 1 else -F((j - i) ** 2, 8 * n * n)
        for j in range(n)
    ) for i in range(n))


def incidence(n: int) -> tuple[tuple[F, ...], ...]:
    return tuple(tuple(F((k == i) - (k == i + 1)) for k in range(n + 1))
                 for i in range(n))


def point_matrix(n: int) -> tuple[tuple[F, ...], ...]:
    b = wave_b(n)
    d = incidence(n)
    return tuple(tuple(
        sum((d[a][i] * b[a][c] * d[c][j]
             for a in range(n) for c in range(n)), F())
        for j in range(n + 1)
    ) for i in range(n + 1))


def quadratic(matrix: Sequence[Sequence[F]], vector: Sequence[int]) -> F:
    return sum((
        F(vector[i]) * matrix[i][j] * vector[j]
        for i in range(len(vector)) for j in range(len(vector))
    ), F())


def residual_audit() -> dict[str, Any]:
    m8 = point_matrix(8)
    m16 = point_matrix(16)
    halves = [[F() for _ in range(17)] for _ in range(17)]
    for i in range(9):
        for j in range(9):
            halves[i][j] += m8[i][j] / 4
            halves[i + 8][j + 8] += m8[i][j] / 4
    residual = tuple(tuple(m16[i][j] - halves[i][j] for j in range(17))
                     for i in range(17))
    if any(residual[i][i] for i in range(17)):
        raise CertificateError("R16 diagonal is not zero")
    if any(sum(row, F()) for row in residual):
        raise CertificateError("R16 row sum is not zero")
    ordered = sum(residual[i][j] != 0
                  for i in range(17) for j in range(17) if i != j)
    unordered = sum(residual[i][j] != 0
                    for i in range(17) for j in range(i + 1, 17))
    if (ordered, unordered) != (160, 80):
        raise CertificateError("R16 support census changed")
    samples = (residual[0][8], residual[1][8], residual[1][9])
    if samples != (-F(1, 32), F(15, 2048), F(1, 1024)):
        raise CertificateError("R16 sample entries changed")

    gamma8 = tuple(F((j - i) ** 2, 4 * 8 * 8)
                   for j in range(10, 16) for i in range(8, j - 1))
    gamma16 = tuple(F((j - i) ** 2, 4 * 16 * 16)
                    for j in range(18, 32) for i in range(16, j - 1))
    data = (
        len(gamma8), sum(gamma8, F()), len(gamma16), sum(gamma16, F()),
        len(gamma16) - 2 * len(gamma8),
        sum(gamma16, F()) - sum(gamma8, F()) / 2,
    )
    if data != (21, F(329, 256), 105, F(5425, 1024), 63, F(4767, 1024)):
        raise CertificateError("cross-half source census changed")
    return {
        "definition": "R16=M16-(M8_left+M8_right)/4",
        "ordered_nonzero_offdiagonal_entries": ordered,
        "unordered_nonzero_offdiagonal_entries": unordered,
        "zero_diagonal": True,
        "zero_row_sums": True,
        "sample_entries": [ftext(value) for value in samples],
        "mixed_sign_and_indefinite": True,
        "Gamma8_source_count": data[0],
        "Gamma8_alpha_mass": ftext(data[1]),
        "Gamma16_source_count": data[2],
        "Gamma16_alpha_mass": ftext(data[3]),
        "omitted_cross_half_source_count": data[4],
        "omitted_cross_half_alpha_mass": ftext(data[5]),
    }


def embed_reduced(column: Sequence[int], block: Sequence[int], size: int) -> tuple[int, ...]:
    if len(column) + 1 != len(block):
        raise CertificateError("reduced column dimension changed")
    result = [0] * size
    for index, value in zip(block[:-1], column):
        result[index] = value
    result[block[-1]] = -sum(column)
    if sum(result) != 0:
        raise CertificateError("reduced column did not recover zero sum")
    return tuple(result)


def haar_sign(x: F, width: F, origin: int, multiplier: int) -> int:
    displacement = x - origin
    return int(0 <= displacement < multiplier * width) - int(
        multiplier * width <= displacement < 2 * multiplier * width
    )


def owner_counterexample() -> dict[str, Any]:
    if sha256(C130_JSON) != C130_SHA256 or sha256(C131_JSON) != C131_SHA256:
        raise CertificateError("pinned C130/C131 dependency hash changed")
    payload = json.loads(C130_JSON.read_text(encoding="utf-8"))
    record = payload["factor_bank"]["records"][43]
    if record["index"] != 43 or (record["left"], record["right"]) != (
        "797/8", "201/2"
    ):
        raise CertificateError("pinned C130 chamber changed")

    local_channels = tuple((rank, multiplier)
                           for multiplier in MULTIPLIERS for rank in range(3, 16))
    epoch4 = tuple(i for i, (rank, _) in enumerate(local_channels) if rank <= 7)
    epoch8 = tuple(i for i, (rank, _) in enumerate(local_channels) if rank >= 8)
    local_columns = tuple(
        embed_reduced(tuple(column), epoch4, 52) for column in record["n4"]["columns"]
    ) + tuple(
        embed_reduced(tuple(column), epoch8, 52) for column in record["n8"]["columns"]
    )
    if (len(record["n4"]["columns"]), len(record["n8"]["columns"])) != (10, 20):
        raise CertificateError("pinned C130 factor ranks changed")
    if record["n4"]["denominator"] != record["n8"]["denominator"]:
        raise CertificateError("C130 epoch denominators differ")

    global_channels = tuple(
        (rank, multiplier, COMPOSITE[rank])
        for multiplier in MULTIPLIERS for rank in range(3, 32)
    )
    global_index = {(rank, multiplier): i
                    for i, (rank, multiplier, _) in enumerate(global_channels)}
    mapped_columns: list[tuple[int, ...]] = []
    for column in local_columns:
        result = [0] * len(global_channels)
        for value, (rank, multiplier) in zip(column, local_channels):
            result[global_index[(16 + rank, multiplier)]] = value
        if sum(result) != 0:
            raise CertificateError("mapped C130 column lost zero sum")
        mapped_columns.append(tuple(result))

    width = F(500)
    midpoint = F(1601, 16)
    denominator = record["n4"]["denominator"]
    gram_scale = F(1, denominator * denominator) / midpoint / 5
    m16 = point_matrix(16)

    def state(x: F) -> tuple[int, ...]:
        return tuple((8 // multiplier) * haar_sign(x, width, origin, multiplier)
                     for _, multiplier, origin in global_channels)

    events = tuple(sorted({
        F(origin) + shift * multiplier * width
        for _, multiplier, origin in global_channels for shift in (0, 1, 2)
    }))
    failures: list[tuple[Any, ...]] = []
    rows = 0
    for left, right in zip(events, events[1:]):
        current = state((left + right) / 2)
        full_dots = tuple(sum(current[i] * column[i] for i in range(len(current)))
                          for column in mapped_columns)
        for multiplier in MULTIPLIERS:
            group = tuple(global_index[(rank, multiplier)] for rank in range(16, 32))
            group_dots = tuple(sum(current[i] * column[i] for i in group)
                               for column in mapped_columns)
            owned = gram_scale * sum((a * b for a, b in zip(group_dots, full_dots)), F())
            natural_state = tuple(current[global_index[(rank, multiplier)]]
                                  for rank in range(15, 32))
            demand = F(multiplier, 128) * quadratic(m16, natural_state)
            margin = width * owned - demand
            rows += 1
            if margin < 0:
                failures.append((margin, left, right, multiplier, owned, demand,
                                 natural_state))
    if len(events) != 174 or rows != 692 or len(failures) != 152:
        raise CertificateError("natural epoch-16 owner census changed")
    strongest = min(failures)
    expected = (
        -F(175_791_028_451_541, 10_006_250_000_000_000),
        F(5169), F(5239), 8,
        F(100_084_829_709, 5_003_125_000_000_000_000), F(9, 512),
        (-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
    )
    if strongest != expected:
        raise CertificateError("strongest natural owner counterexample changed")
    return {
        "C130_chamber_index": 43,
        "C130_chamber": ["797/8", "201/2"],
        "C130_factor_ranks": [10, 20],
        "local_width": "100/1",
        "affine_dilation": 5,
        "global_width": "500/1",
        "global_cells": 173,
        "natural_epoch16_owner_rows_checked": rows,
        "strictly_negative_natural_owner_rows": len(failures),
        "strongest": {
            "margin": ftext(strongest[0]),
            "cell": [ftext(strongest[1]), ftext(strongest[2])],
            "multiplier": strongest[3],
            "owned": ftext(strongest[4]),
            "natural_demand": ftext(strongest[5]),
            "state_ranks15_to31": list(strongest[6]),
        },
        "old_block_zero_contribution_reason": (
            "any C131 factor supported on ranks 3..15 has zero dot with the "
            "natural epoch-16 owner group ranks 16..31, so adding it cannot "
            "repair this owner share"
        ),
    }


def phase_alignment_audit() -> dict[str, Any]:
    if C123[10] - C123[5] != 143 + C123[5] or C123[10] - C123[5] != 427:
        raise CertificateError("phase-alignment collision identity changed")
    q = 5
    translation = 1169 + 143 * q
    aligned = C120 + tuple(translation + q * x for x in C123)
    differences = positive_differences(aligned)
    if len(set(differences)) == len(differences):
        raise CertificateError("phase-aligned q=5 probe unexpectedly became Golomb")
    return {
        "alignment_translation": "T=1169+143*q",
        "identity": "711-284=427=143+284",
        "universal_repeated_difference": (
            "(T+q*C123[5])-1169=(T+q*C123[10])-(T+q*C123[5])=427*q"
        ),
        "all_positive_integer_q_fail_Golomb": True,
        "q5_repeated_difference": 2135,
    }


def build_certificate() -> dict[str, Any]:
    return {
        "schema": "erdos1191.c132.composite32_naive_paste_no_go.v1",
        "status": STATUS,
        "composite": composite_and_cap_audit(),
        "cross_half_residual": residual_audit(),
        "natural_owner_counterexample": owner_counterexample(),
        "phase_alignment_no_go": phase_alignment_audit(),
        "dependencies": {
            C130_JSON.name: C130_SHA256,
            C131_JSON.name: C131_SHA256,
        },
        "scope": {
            "explicit_32_mark_finite_fixture_only": True,
            "finite_C2_cap_from_m4_through_m32_only": True,
            "one_pinned_C130_chamber_factor_only": True,
            "naive_affine_local_bank_paste_refuted": True,
            "fresh_joint_epoch8_16_master_refuted": False,
            "fractional_or_cross_block_owner_refuted": False,
            "arbitrary_rank_proved": False,
            "C058_resolved": False,
            "Q1_Q2_resolved": False,
            "publication_or_prize_claimed": False,
        },
        "required_action": (
            "solve a fresh joint epoch-8/16 program on a common physical phase, "
            "retaining ranks 15..18, all 63 cross-half sources, and every C103 "
            "boundary/terminal row; do not paste the local C130/C131 owner certificates"
        ),
    }


def validate(candidate: Mapping[str, Any], expected: Mapping[str, Any] | None = None) -> None:
    reference = build_certificate() if expected is None else expected
    if candidate != reference:
        raise CertificateError("certificate differs from exact reconstruction")


def mutation_self_check(expected: Mapping[str, Any]) -> int:
    mutations = []
    for path, value in (
        (("status",), "C058_SOLVED"),
        (("composite", "span"), 7083),
        (("cross_half_residual", "omitted_cross_half_source_count"), 62),
        (("natural_owner_counterexample", "strictly_negative_natural_owner_rows"), 151),
        (("scope", "C058_resolved"), True),
    ):
        altered = deepcopy(expected)
        cursor: Any = altered
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        mutations.append(altered)
    rejected = 0
    for altered in mutations:
        try:
            validate(altered, expected)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("mutation self-check failed")
    return rejected


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--write", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)
    expected = build_certificate()
    if args.verify is not None:
        validate(json.loads(args.verify.read_text(encoding="utf-8")), expected)
    if args.write is not None:
        args.write.write_text(
            json.dumps(expected, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )
    rejected = mutation_self_check(expected) if args.self_check else 0
    owner = expected["natural_owner_counterexample"]
    residual = expected["cross_half_residual"]
    print(
        "VERIFY_OK",
        STATUS,
        "span=7084",
        "differences=496",
        f"residual_sources={residual['omitted_cross_half_source_count']}",
        f"owner_rows={owner['natural_epoch16_owner_rows_checked']}",
        f"owner_failures={owner['strictly_negative_natural_owner_rows']}",
        f"mutations_rejected={rejected}",
        "C058_open",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

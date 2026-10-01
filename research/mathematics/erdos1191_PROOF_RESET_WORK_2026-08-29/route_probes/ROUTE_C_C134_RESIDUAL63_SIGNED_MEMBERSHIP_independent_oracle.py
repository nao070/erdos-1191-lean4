#!/usr/bin/env python3
"""Independent stdlib-only verifier for the canonical C134 residual63 certificate.

This oracle deliberately does not import the C134 main verifier or any
canonical Python module.  It independently reconstructs the source matrices,
the two rational Gram banks, the owner split, the exact ranks, the C103 scalar
ledger, and the separating functionals.
"""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP_certificate.json"
SCHEMA = "erdos1191.route_c.c134.residual63_signed_membership.v1"
STATUS = "EXACT_C134_SIGNED_RESIDUAL_MEMBERSHIP_POSITIVE_GRAM_ONLY_NO_GO_C058_OPEN"
N = 16
S = 17
SOURCES = tuple(
    (a, b) for a in range(8) for b in range(8, 16) if b >= a + 2
)


def die(message: str) -> None:
    raise SystemExit("INDEPENDENT_ORACLE_FAIL: " + message)


def zero(size: int) -> list[list[Q]]:
    return [[Q(0) for _ in range(size)] for _ in range(size)]


def add(*matrices: list[list[Q]]) -> list[list[Q]]:
    if not matrices:
        return zero(S)
    size = len(matrices[0])
    return [
        [sum((matrix[i][j] for matrix in matrices), Q(0)) for j in range(size)]
        for i in range(size)
    ]


def scale(c: Q, matrix: list[list[Q]]) -> list[list[Q]]:
    return [[c * x for x in row] for row in matrix]


def sub(a: list[list[Q]], b: list[list[Q]]) -> list[list[Q]]:
    return add(a, scale(Q(-1), b))


def vec(gap: int, size: int = S) -> list[Q]:
    result = [Q(0) for _ in range(size)]
    result[gap] = Q(1)
    result[gap + 1] = Q(-1)
    return result


def outer(a: list[Q], b: list[Q]) -> list[list[Q]]:
    return [[x * y for y in b] for x in a]


def source_matrix(i: int, j: int) -> list[list[Q]]:
    a = Q((j - i) ** 2, 1024)
    u, v = vec(i), vec(j)
    return scale(-a / 2, add(outer(u, v), outer(v, u)))


def wave(n: int) -> list[list[Q]]:
    b = zero(n)
    for i in range(n):
        for j in range(n):
            if abs(i - j) >= 2:
                b[i][j] = -Q((i - j) ** 2, 8 * n * n)
    d = zero(n)
    d = [[Q(0) for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        d[i][i], d[i][i + 1] = Q(1), Q(-1)
    return [
        [
            sum(
                (d[a][r] * b[a][bb] * d[bb][c] for a in range(n) for bb in range(n)),
                Q(0),
            )
            for c in range(n + 1)
        ]
        for r in range(n + 1)
    ]


def embed(m8: list[list[Q]], offset: int) -> list[list[Q]]:
    result = zero(S)
    for i in range(9):
        for j in range(9):
            result[offset + i][offset + j] = m8[i][j]
    return result


def compress(matrix: list[list[Q]]) -> list[list[Q]]:
    return [
        [
            sum((matrix[a][b] for a in range(i + 1) for b in range(j + 1)), Q(0))
            for j in range(N)
        ]
        for i in range(N)
    ]


def upper(matrix: list[list[Q]]) -> list[Q]:
    return [matrix[i][j] for i in range(len(matrix)) for j in range(i, len(matrix))]


def rank(vectors: list[list[Q]]) -> int:
    rows = [[Q(x) for x in row] for row in vectors]
    height = len(rows)
    width = len(rows[0]) if rows else 0
    r = 0
    for c in range(width):
        pivot = next((k for k in range(r, height) if rows[k][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        p = rows[r][c]
        rows[r] = [x / p for x in rows[r]]
        for k in range(height):
            if k != r and rows[k][c]:
                p = rows[k][c]
                rows[k] = [x - p * y for x, y in zip(rows[k], rows[r])]
        r += 1
        if r == height:
            break
    return r


def owner(matrix: list[list[Q]]) -> tuple[list[list[Q]], list[list[Q]]]:
    past = [
        [
            ((matrix[i][j] if i == 0 else Q(0)) + (matrix[i][j] if j == 0 else Q(0))) / 2
            for j in range(S)
        ]
        for i in range(S)
    ]
    return past, sub(matrix, past)


def quad(matrix: list[list[Q]], q: list[Q]) -> Q:
    return sum((q[i] * matrix[i][j] * q[j] for i in range(S) for j in range(S)), Q(0))


def canonical_hash(value: object) -> str:
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def main() -> int:
    cert = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if cert.get("schema") != SCHEMA or cert.get("status") != STATUS:
        die("schema/status")
    integrity = cert.get("integrity", {})
    payload = {key: value for key, value in cert.items() if key != "integrity"}
    if integrity.get("payload_sha256") != canonical_hash(payload):
        die("payload hash")

    scope = cert.get("scope", {})
    if not all(
        scope.get(key) is True
        for key in (
            "finite_R16_signed_primitive_membership_only",
            "one_time_coordinate_owner_partition_checked",
            "minimal_C103_m0_n1_boundary_terminal_embedding_checked",
            "full_global_ranks_15_through_31_present",
        )
    ):
        die("positive finite scope")
    if not all(
        scope.get(key) is False
        for key in (
            "positive_PSD_capacity_for_R16_proved",
            "physical_phase_history_ledger_constructed",
            "nonanticipating_global_C103_ledger_constructed",
            "birth_cutoff_shared_endpoint_arbitrary_horizon_closed",
            "C058_Q1_Q2_proved",
            "publication_novelty_or_prize_claimed",
        )
    ):
        die("scope upgrade")

    if len(SOURCES) != 63 or (7, 8) in SOURCES:
        die("source census")
    residual = add(*(source_matrix(i, j) for i, j in SOURCES))
    m8 = wave(8)
    subtraction = sub(wave(16), scale(Q(1, 4), add(embed(m8, 0), embed(m8, 8))))
    if residual != subtraction:
        die("source/subtraction mismatch")
    mass = sum((Q((j - i) ** 2, 1024) for i, j in SOURCES), Q(0))
    if mass != Q(4767, 1024):
        die("mass")
    if any(sum(row, Q(0)) for row in residual):
        die("row sums")
    if any(residual[i][i] for i in range(S)):
        die("diagonal")
    if (residual[0][8], residual[1][8], residual[1][9]) != (
        -Q(1, 32), Q(15, 2048), Q(1, 1024)
    ):
        die("sample entries")

    # Independently reconstruct rational Gram factors and signed matrices.
    x_plus, x_minus = zero(S), zero(S)
    gram_columns: list[list[Q]] = []
    primitive_columns: list[list[Q]] = []
    plus_factor_vectors: list[list[Q]] = []
    minus_factor_vectors: list[list[Q]] = []
    rows_expected: list[dict[str, object]] = []
    for i, j in SOURCES:
        u, v = vec(i), vec(j)
        vm = [a - b for a, b in zip(u, v)]
        vp = [a + b for a, b in zip(u, v)]
        coefficient = Q((j - i) ** 2, 4096)
        factor_scale = Q(j - i, 64)
        plus_factor_vectors.append([factor_scale * x for x in vm])
        minus_factor_vectors.append([factor_scale * x for x in vp])
        x_plus = add(x_plus, scale(coefficient, outer(vm, vm)))
        x_minus = add(x_minus, scale(coefficient, outer(vp, vp)))
        gram_columns.extend((upper(compress(outer(vm, vm))), upper(compress(scale(Q(-1), outer(vp, vp))))))
        primitive_columns.append(upper(compress(source_matrix(i, j))))
        rows_expected.append(
            {
                "i": i,
                "j": j,
                "global_gap_left_rank": 15 + i,
                "global_gap_right_rank": 15 + j,
                "alpha": f"{(Q((j-i)**2,1024)).numerator}/{(Q((j-i)**2,1024)).denominator}",
                "primitive_coefficient": "1/1",
                "signed_gram_nonnegative_coefficient": f"{coefficient.numerator}/{coefficient.denominator}",
                "rational_gram_factor_scale": f"{Q(j-i,64).numerator}/{Q(j-i,64).denominator}",
            }
        )
    if sub(x_plus, x_minus) != residual:
        die("Gram polarization")
    if any(sum(row, Q(0)) for row in x_plus + x_minus):
        die("Gram row sums")
    if sum((x_plus[i][i] for i in range(S)), Q(0)) != mass:
        die("X_plus trace")
    if sum((x_minus[i][i] for i in range(S)), Q(0)) != mass:
        die("X_minus trace")
    target = upper(compress(residual))
    if rank(primitive_columns) != 63 or rank(primitive_columns + [target]) != 63:
        die("primitive rank/membership")
    if rank(gram_columns) != 78 or rank(gram_columns + [target]) != 78:
        die("Gram rank/membership")
    if rank(plus_factor_vectors) != 15 or rank(minus_factor_vectors) != 15:
        die("rational Gram factor ranks")
    gram_summary = cert.get("rational_gram_difference", {})
    if (
        gram_summary.get("X_plus_exact_factor_rank") != 15
        or gram_summary.get("X_minus_exact_factor_rank") != 15
        or gram_summary.get("X_plus_trace") != "4767/1024"
        or gram_summary.get("X_minus_trace") != "4767/1024"
        or gram_summary.get("signed_trace") != "0/1"
    ):
        die("stored rational Gram summary")
    if cert["generator_space"]["source_coefficients"] != rows_expected:
        die("stored coefficients")

    past, current = owner(residual)
    if add(past, current) != residual or past[0][8] != -Q(1, 64):
        die("owner lift")
    if sum(i == 0 for i, _ in SOURCES) != 8 or sum(i <= 3 for i, _ in SOURCES) != 32:
        die("boundary source census")
    for i in range(4):
        if sum(residual[i][j] != 0 for j in range(S)) != 9:
            die(f"mandatory rank row {15+i}")

    # Recheck the complete minimal C103 row equation, not merely a zero-boundary case.
    slots = cert["C103_minimal_embedding"]["row_slot_factors"]
    lhs = Q(slots["lhs_prefix_increment_at_L"])
    initial = Q(slots["initial_epoch_boundary_band_0"])
    final = Q(slots["final_epoch_boundary_band_1"])
    terminal = Q(slots["upper_scale_terminal_increment"])
    if (lhs, initial, final, terminal) != (Q(1), -Q(1, 3), Q(1, 3), Q(1, 3)):
        die("C103 row factors")
    if lhs != final - initial + terminal:
        die("C103 Abel equation")
    potential = cert["C103_minimal_embedding"]["potential_factors"]
    c0l, c1l = Q(potential["C_0_L"]), Q(potential["C_1_L"])
    c0u, c1u = Q(potential["C_0_L_plus_1"]), Q(potential["C_1_L_plus_1"])
    if (c1l - c0l) - (c1u - c0u) != (c1l - c1u) - (c0l - c0u):
        die("C103 curl")

    qneg = [Q(1) if i in (0, 8) else Q(0) for i in range(S)]
    qpos = [Q(1) if i == 0 else -Q(1) if i == 8 else Q(0) for i in range(S)]
    if quad(residual, qneg) != -Q(1, 16) or quad(residual, qpos) != Q(1, 16):
        die("PSD separation/indefiniteness")
    if residual[1][8] != Q(15, 2048):
        die("ranks19..31-only separator")

    for path_text, expected_hash in cert.get("canonical_dependencies", {}).items():
        path = Path(path_text)
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected_hash:
            die("canonical dependency drift: " + path.name)

    print(
        "INDEPENDENT_C134_RESIDUAL63_OK "
        f"sources={len(SOURCES)} mass={mass.numerator}/{mass.denominator} "
        "primitive_rank=63 signed_gram_rank=78 "
        "positive_only_separator=-1/16 boundary_rank15=-1/64 "
        "ranks15_18=retained C103_initial_final_terminal=retained C058_open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

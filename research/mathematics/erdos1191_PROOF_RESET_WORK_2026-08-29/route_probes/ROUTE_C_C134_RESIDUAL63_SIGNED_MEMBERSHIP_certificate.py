#!/usr/bin/env python3
"""Exact canonical C134 certificate for the 63-source epoch-16 residual.

This finite C134 certificate studies only the finite matrix

    R16 = M16 - (M8_left + M8_right)/4

in the natural 17 prefix coordinates (global ranks 15,...,31).  It constructs
an exact signed primitive certificate, an exact signed difference of rational
PSD Gram banks, the one-time coordinate-owner lift, and a minimal C103
finite-Abel embedding with every initial/final/scale-terminal slot present.

Nothing here proves a physical phase/history ledger, a positive owner master,
C058, Q1, or Q2.
"""

from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
from typing import Iterable, Mapping, Sequence


SCHEMA = "erdos1191.route_c.c134.residual63_signed_membership.v1"
STATUS = "EXACT_C134_SIGNED_RESIDUAL_MEMBERSHIP_POSITIVE_GRAM_ONLY_NO_GO_C058_OPEN"
HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_C134_RESIDUAL63_SIGNED_MEMBERSHIP_certificate.json"
CANONICAL_ROOT = Path(
    "/Users/USER/Documents/ChatGPT/mathematics/"
    "erdos1191_PROOF_RESET_WORK_2026-08-29"
)
CANONICAL_DEPENDENCIES = (
    CANONICAL_ROOT / "lean_kernel/Erdos1191/PrefixScaleFinite.lean",
    CANONICAL_ROOT / "lean_kernel/Erdos1191/OwnershipFinite.lean",
    CANONICAL_ROOT
    / "route_probes/ROUTE_C_REVERSE_PROFILE_FULL_PHASE_STORAGE_certificate.py",
    CANONICAL_ROOT
    / "route_probes/ROUTE_C_WHOLE_STENCIL_CROSS_WIDTH_MASTER_certificate.py",
)

N = 16
STATE_SIZE = 17
GLOBAL_RANKS = tuple(range(15, 32))
LEFT_GAPS = tuple(range(0, 8))
RIGHT_GAPS = tuple(range(8, 16))
CROSS_SOURCES = tuple(
    (i, j)
    for i in LEFT_GAPS
    for j in RIGHT_GAPS
    if j >= i + 2
)


class CertificateError(RuntimeError):
    """Raised when an exact identity, scope gate, or certificate check fails."""


Matrix = tuple[tuple[F, ...], ...]
Vector = tuple[F, ...]


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def parse_ftext(value: str) -> F:
    return F(value)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _canonical_hash(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def zero_matrix(size: int = STATE_SIZE) -> Matrix:
    return tuple(tuple(F(0) for _ in range(size)) for _ in range(size))


def matrix_add(*matrices: Matrix) -> Matrix:
    if not matrices:
        return zero_matrix()
    size = len(matrices[0])
    if any(len(m) != size or any(len(row) != size for row in m) for m in matrices):
        raise CertificateError("matrix shape mismatch")
    return tuple(
        tuple(sum((m[i][j] for m in matrices), F(0)) for j in range(size))
        for i in range(size)
    )


def matrix_scale(value: F | int, matrix: Matrix) -> Matrix:
    value = F(value)
    return tuple(tuple(value * x for x in row) for row in matrix)


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return matrix_add(left, matrix_scale(-1, right))


def outer(left: Vector, right: Vector) -> Matrix:
    if len(left) != len(right):
        raise CertificateError("outer-product shape mismatch")
    return tuple(tuple(x * y for y in right) for x in left)


def vector_add(left: Vector, right: Vector, right_scale: int = 1) -> Vector:
    if len(left) != len(right):
        raise CertificateError("vector shape mismatch")
    return tuple(x + right_scale * y for x, y in zip(left, right))


def d_vector(i: int, size: int = STATE_SIZE) -> Vector:
    if not 0 <= i < size - 1:
        raise CertificateError("gap index outside the prefix state")
    values = [F(0) for _ in range(size)]
    values[i] = F(1)
    values[i + 1] = F(-1)
    return tuple(values)


def alpha(n: int, i: int, j: int) -> F:
    return F((j - i) ** 2, 4 * n * n)


def primitive(n: int, i: int, j: int) -> Matrix:
    """The symmetric source matrix -alpha/2 (d_i d_j^T+d_j d_i^T)."""
    if not (0 <= i < j < n and j >= i + 2):
        raise CertificateError("invalid nonadjacent primitive")
    u = d_vector(i, n + 1)
    v = d_vector(j, n + 1)
    return matrix_scale(
        -alpha(n, i, j) / 2,
        matrix_add(outer(u, v), outer(v, u)),
    )


def wave_matrix(n: int) -> Matrix:
    """Independently build D^T B D from the canonical exact definition."""
    b = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and abs(i - j) >= 2:
                b[i][j] = -F((j - i) ** 2, 8 * n * n)
    d = [[F(0) for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        d[i][i] = F(1)
        d[i][i + 1] = F(-1)
    return tuple(
        tuple(
            sum(
                (d[a][r] * b[a][bb] * d[bb][c] for a in range(n) for bb in range(n)),
                F(0),
            )
            for c in range(n + 1)
        )
        for r in range(n + 1)
    )


def embed_half(matrix8: Matrix, offset: int) -> Matrix:
    if len(matrix8) != 9 or offset not in (0, 8):
        raise CertificateError("invalid M8 half embedding")
    result = [[F(0) for _ in range(STATE_SIZE)] for _ in range(STATE_SIZE)]
    for i in range(9):
        for j in range(9):
            result[offset + i][offset + j] += matrix8[i][j]
    return tuple(tuple(row) for row in result)


def residual16_by_subtraction() -> Matrix:
    m16 = wave_matrix(16)
    m8 = wave_matrix(8)
    halves = matrix_add(embed_half(m8, 0), embed_half(m8, 8))
    return matrix_sub(m16, matrix_scale(F(1, 4), halves))


def residual16_by_sources() -> Matrix:
    return matrix_add(*(primitive(16, i, j) for i, j in CROSS_SOURCES))


def quadratic(matrix: Matrix, vector: Vector) -> F:
    if len(matrix) != len(vector):
        raise CertificateError("quadratic shape mismatch")
    return sum(
        (
            vector[i] * matrix[i][j] * vector[j]
            for i in range(len(vector))
            for j in range(len(vector))
        ),
        F(0),
    )


def trace(matrix: Matrix) -> F:
    return sum((matrix[i][i] for i in range(len(matrix))), F(0))


def is_symmetric(matrix: Matrix) -> bool:
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))


def row_sums(matrix: Matrix) -> tuple[F, ...]:
    return tuple(sum(row, F(0)) for row in matrix)


def gram_root(vector: Vector, sign: int = 1) -> Matrix:
    if sign not in (-1, 1):
        raise CertificateError("Gram-root sign must be +/-1")
    return matrix_scale(sign, outer(vector, vector))


def signed_gram_banks() -> tuple[Matrix, Matrix, tuple[dict[str, object], ...]]:
    """Return X_plus, X_minus with R=X_plus-X_minus and rational factors.

    For gamma=(i,j), alpha/4=((j-i)/64)^2.  Hence the two PSD banks have
    rational Gram columns ((j-i)/64)(d_i-d_j) and
    ((j-i)/64)(d_i+d_j).
    """
    plus_terms: list[Matrix] = []
    minus_terms: list[Matrix] = []
    rows: list[dict[str, object]] = []
    for i, j in CROSS_SOURCES:
        u = d_vector(i)
        v = d_vector(j)
        difference = vector_add(u, v, -1)
        total = vector_add(u, v, 1)
        coefficient = alpha(16, i, j) / 4
        rational_factor_scale = F(j - i, 64)
        if coefficient != rational_factor_scale * rational_factor_scale:
            raise CertificateError("rational Gram square factor changed")
        plus_terms.append(matrix_scale(coefficient, gram_root(difference)))
        minus_terms.append(matrix_scale(coefficient, gram_root(total)))
        rows.append(
            {
                "i": i,
                "j": j,
                "global_gap_left_rank": 15 + i,
                "global_gap_right_rank": 15 + j,
                "alpha": ftext(alpha(16, i, j)),
                "primitive_coefficient": "1/1",
                "signed_gram_nonnegative_coefficient": ftext(coefficient),
                "rational_gram_factor_scale": ftext(rational_factor_scale),
            }
        )
    return matrix_add(*plus_terms), matrix_add(*minus_terms), tuple(rows)


def owner_lift(matrix: Matrix) -> tuple[Matrix, Matrix]:
    """C111-compatible one-time row ownership {rank15}|{ranks16,...,31}.

    Owner energy q^T P X q is represented symmetrically by
    (P X + X P)/2.  The two lifted pieces sum exactly to X.
    """
    size = len(matrix)
    past = tuple(
        tuple(
            ((matrix[i][j] if i == 0 else F(0)) + (matrix[i][j] if j == 0 else F(0))) / 2
            for j in range(size)
        )
        for i in range(size)
    )
    current = matrix_sub(matrix, past)
    return past, current


def c103_slot_factors() -> dict[str, F]:
    """A nondegenerate m=0,n=1 C103 embedding retaining every row slot.

    With w_0=c_0(L)=1, choose matrix-valued potential values
      C(0,L)=-X/3, C(1,L)=2X/3,
      C(0,L+1)=0, C(1,L+1)=X/3.
    Then delta(L)=X, band_0(L)=-X/3, band_1(L)=X/3, and
    delta(L+1)=X/3.  Thus X = final - initial + scale_terminal.
    """
    return {
        "lhs_prefix_increment_at_L": F(1),
        "initial_epoch_boundary_band_0": -F(1, 3),
        "final_epoch_boundary_band_1": F(1, 3),
        "upper_scale_terminal_increment": F(1, 3),
    }


def c103_potential_factors() -> dict[str, F]:
    return {
        "C_0_L": -F(1, 3),
        "C_1_L": F(2, 3),
        "C_0_L_plus_1": F(0),
        "C_1_L_plus_1": F(1, 3),
    }


def verify_c103_embedding(matrix: Matrix) -> None:
    slots = c103_slot_factors()
    lhs = matrix_scale(slots["lhs_prefix_increment_at_L"], matrix)
    initial = matrix_scale(slots["initial_epoch_boundary_band_0"], matrix)
    final = matrix_scale(slots["final_epoch_boundary_band_1"], matrix)
    terminal = matrix_scale(slots["upper_scale_terminal_increment"], matrix)
    if lhs != matrix_add(final, matrix_scale(-1, initial), terminal):
        raise CertificateError("m=0,n=1 C103 Abel row identity failed")

    potential = c103_potential_factors()
    delta_l = potential["C_1_L"] - potential["C_0_L"]
    delta_u = potential["C_1_L_plus_1"] - potential["C_0_L_plus_1"]
    band_0 = potential["C_0_L"] - potential["C_0_L_plus_1"]
    band_1 = potential["C_1_L"] - potential["C_1_L_plus_1"]
    if (
        delta_l != F(1)
        or delta_u != F(1, 3)
        or band_0 != -F(1, 3)
        or band_1 != F(1, 3)
        or delta_l - delta_u != band_1 - band_0
    ):
        raise CertificateError("C103 curl/potential factors failed")

    for slot_matrix in (lhs, initial, final, terminal):
        past, current = owner_lift(slot_matrix)
        if matrix_add(past, current) != slot_matrix:
            raise CertificateError("owner lift failed on a C103 row slot")


def gap_compress(matrix: Matrix) -> Matrix:
    """Compute S^T X S for the exact right inverse D S=I.

    S[a,k]=1 when a<=k (a=0,...,15), and the last state coordinate is 0.
    The map X -> S^T X S is the inverse on symmetric zero-row-sum matrices
    of B -> D^T B D.
    """
    if len(matrix) != STATE_SIZE:
        raise CertificateError("gap compression expects 17 state coordinates")
    return tuple(
        tuple(
            sum(
                (matrix[a][b] for a in range(i + 1) for b in range(j + 1)),
                F(0),
            )
            for j in range(N)
        )
        for i in range(N)
    )


def upper_vector(matrix: Matrix) -> tuple[F, ...]:
    if not is_symmetric(matrix):
        raise CertificateError("upper-vector input is not symmetric")
    return tuple(matrix[i][j] for i in range(len(matrix)) for j in range(i, len(matrix)))


def rational_rank(vectors: Sequence[Sequence[F]]) -> int:
    """Exact Gaussian row rank over Q."""
    if not vectors:
        return 0
    width = len(vectors[0])
    if any(len(row) != width for row in vectors):
        raise CertificateError("rank vectors have inconsistent lengths")
    rows = [[F(x) for x in row] for row in vectors]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        value = rows[pivot_row][column]
        rows[pivot_row] = [x / value for x in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or rows[row][column] == 0:
                continue
            value = rows[row][column]
            rows[row] = [x - value * y for x, y in zip(rows[row], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def _matrix_equal_sum(target: Matrix, terms: Iterable[Matrix]) -> bool:
    return target == matrix_add(*tuple(terms))


def _assert_scope(scope: Mapping[str, object]) -> None:
    required_true = (
        "finite_R16_signed_primitive_membership_only",
        "one_time_coordinate_owner_partition_checked",
        "minimal_C103_m0_n1_boundary_terminal_embedding_checked",
        "full_global_ranks_15_through_31_present",
    )
    required_false = (
        "positive_PSD_capacity_for_R16_proved",
        "physical_phase_history_ledger_constructed",
        "nonanticipating_global_C103_ledger_constructed",
        "birth_cutoff_shared_endpoint_arbitrary_horizon_closed",
        "C058_Q1_Q2_proved",
        "publication_novelty_or_prize_claimed",
    )
    if any(scope.get(key) is not True for key in required_true):
        raise CertificateError("a required finite scope flag is missing")
    if any(scope.get(key) is not False for key in required_false):
        raise CertificateError("a forbidden scope upgrade is present")


@lru_cache(maxsize=1)
def _build_uncached() -> dict[str, object]:
    if len(CROSS_SOURCES) != 63 or (7, 8) in CROSS_SOURCES:
        raise CertificateError("cross-source census changed")
    residual_subtraction = residual16_by_subtraction()
    residual_sources = residual16_by_sources()
    if residual_subtraction != residual_sources:
        raise CertificateError("63 sources do not reconstruct the direct-sum residual")
    residual = residual_sources
    if not is_symmetric(residual) or any(row_sums(residual)):
        raise CertificateError("R16 lost symmetry or zero row sums")
    if any(residual[i][i] != 0 for i in range(STATE_SIZE)):
        raise CertificateError("R16 diagonal changed")

    source_mass = sum((alpha(16, i, j) for i, j in CROSS_SOURCES), F(0))
    if source_mass != F(4767, 1024):
        raise CertificateError("63-source alpha mass changed")

    plus, minus, source_rows = signed_gram_banks()
    if residual != matrix_sub(plus, minus):
        raise CertificateError("signed Gram polarization does not reconstruct R16")
    if trace(plus) != source_mass or trace(minus) != source_mass:
        raise CertificateError("signed Gram trace ledger changed")
    if any(row_sums(plus)) or any(row_sums(minus)):
        raise CertificateError("Gram bank lost exact zero row sums")

    # Exact rational linear-algebra membership in the compressed gap basis.
    target_vector = upper_vector(gap_compress(residual))
    primitive_vectors = tuple(
        upper_vector(gap_compress(primitive(16, i, j))) for i, j in CROSS_SOURCES
    )
    primitive_rank = rational_rank(primitive_vectors)
    primitive_augmented_rank = rational_rank(primitive_vectors + (target_vector,))
    if (primitive_rank, primitive_augmented_rank) != (63, 63):
        raise CertificateError("primitive membership/rank certificate changed")
    if not _matrix_equal_sum(residual, (primitive(16, i, j) for i, j in CROSS_SOURCES)):
        raise CertificateError("unit primitive coefficients fail")

    signed_gram_matrices: list[Matrix] = []
    signed_gram_terms: list[Matrix] = []
    plus_factor_vectors: list[Vector] = []
    minus_factor_vectors: list[Vector] = []
    for i, j in CROSS_SOURCES:
        u = d_vector(i)
        v = d_vector(j)
        difference = vector_add(u, v, -1)
        total = vector_add(u, v, 1)
        h_minus = gram_root(difference)
        negative_h_plus = gram_root(total, sign=-1)
        coefficient = alpha(16, i, j) / 4
        factor_scale = F(j - i, 64)
        plus_factor_vectors.append(tuple(factor_scale * x for x in difference))
        minus_factor_vectors.append(tuple(factor_scale * x for x in total))
        signed_gram_matrices.extend((h_minus, negative_h_plus))
        signed_gram_terms.extend(
            (matrix_scale(coefficient, h_minus), matrix_scale(coefficient, negative_h_plus))
        )
    gram_vectors = tuple(upper_vector(gap_compress(m)) for m in signed_gram_matrices)
    signed_gram_rank = rational_rank(gram_vectors)
    signed_gram_augmented_rank = rational_rank(gram_vectors + (target_vector,))
    if (signed_gram_rank, signed_gram_augmented_rank) != (78, 78):
        raise CertificateError("signed Gram cone membership/rank changed")
    if not _matrix_equal_sum(residual, signed_gram_terms):
        raise CertificateError("nonnegative signed-Gram coefficients fail")
    plus_factor_rank = rational_rank(plus_factor_vectors)
    minus_factor_rank = rational_rank(minus_factor_vectors)
    if (plus_factor_rank, minus_factor_rank) != (15, 15):
        raise CertificateError("rational Gram factor ranks changed")

    # One-time coordinate ownership keeps the shared rank 15 row rather than
    # silently assigning all state to the new epoch.
    past, current = owner_lift(residual)
    if matrix_add(past, current) != residual:
        raise CertificateError("owner pieces do not sum to R16")
    for matrix in (residual, plus, minus):
        p, c = owner_lift(matrix)
        if matrix_add(p, c) != matrix:
            raise CertificateError("owner lift failed on a Gram bank")
    owner_generator_checks = 0
    for matrix in tuple(primitive(16, i, j) for i, j in CROSS_SOURCES) + tuple(signed_gram_matrices):
        p, c = owner_lift(matrix)
        if matrix_add(p, c) != matrix:
            raise CertificateError("owner lift failed on a generator")
        owner_generator_checks += 1
    if owner_generator_checks != 189:
        raise CertificateError("owner generator census changed")

    # C103 m=0,n=1 embedding, checked on the target and all 63 primitives.
    verify_c103_embedding(residual)
    for i, j in CROSS_SOURCES:
        verify_c103_embedding(primitive(16, i, j))
    for matrix in signed_gram_matrices:
        verify_c103_embedding(matrix)

    # Exact separating functionals for stricter, tempting but invalid cones.
    q_negative = tuple(F(1) if i in (0, 8) else F(0) for i in range(STATE_SIZE))
    q_positive = tuple(F(1) if i == 0 else F(-1) if i == 8 else F(0) for i in range(STATE_SIZE))
    negative_value = quadratic(residual, q_negative)
    positive_value = quadratic(residual, q_positive)
    if (negative_value, positive_value) != (-F(1, 16), F(1, 16)):
        raise CertificateError("indefiniteness separator values changed")
    if residual[0][8] != -F(1, 32) or past[0][8] != -F(1, 64):
        raise CertificateError("rank-15 boundary separator changed")
    if residual[1][8] != F(15, 2048):
        raise CertificateError("rank-16 omitted-support separator changed")

    rank_rows = []
    for local_index in range(4):
        nonzero_entries = [
            {
                "other_global_rank": 15 + j,
                "value": ftext(residual[local_index][j]),
            }
            for j in range(STATE_SIZE)
            if residual[local_index][j] != 0
        ]
        if len(nonzero_entries) != 9:
            raise CertificateError("a mandatory rank 15--18 row changed")
        rank_rows.append(
            {
                "global_rank": 15 + local_index,
                "local_state_index": local_index,
                "nonzero_entry_count": len(nonzero_entries),
                "nonzero_entries": nonzero_entries,
            }
        )

    scope = {
        "finite_R16_signed_primitive_membership_only": True,
        "one_time_coordinate_owner_partition_checked": True,
        "minimal_C103_m0_n1_boundary_terminal_embedding_checked": True,
        "full_global_ranks_15_through_31_present": True,
        "positive_PSD_capacity_for_R16_proved": False,
        "physical_phase_history_ledger_constructed": False,
        "nonanticipating_global_C103_ledger_constructed": False,
        "birth_cutoff_shared_endpoint_arbitrary_horizon_closed": False,
        "C058_Q1_Q2_proved": False,
        "publication_novelty_or_prize_claimed": False,
    }
    _assert_scope(scope)

    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "scope": scope,
        "natural_epoch16_coordinates": {
            "global_prefix_ranks": list(GLOBAL_RANKS),
            "state_coordinate_count": STATE_SIZE,
            "gap_coordinate_count": N,
            "one_time_owner_partition": {
                "past_shared_boundary_owner": [15],
                "current_epoch16_owner": list(range(16, 32)),
            },
            "mandatory_rank_rows_15_through_18": rank_rows,
        },
        "residual": {
            "definition": "M16-(M8_left+M8_right)/4",
            "cross_source_rule": "0<=i<=7, 8<=j<=15, j>=i+2",
            "cross_source_count": len(CROSS_SOURCES),
            "alpha_mass": ftext(source_mass),
            "ordered_nonzero_entry_count": sum(x != 0 for row in residual for x in row),
            "unordered_nonzero_offdiagonal_count": sum(
                residual[i][j] != 0 for i in range(STATE_SIZE) for j in range(i + 1, STATE_SIZE)
            ),
            "zero_diagonal": True,
            "zero_row_sums": True,
            "sample_entries": {
                "R_rank15_rank23": ftext(residual[0][8]),
                "R_rank16_rank23": ftext(residual[1][8]),
                "R_rank16_rank24": ftext(residual[1][9]),
            },
        },
        "generator_space": {
            "ambient": (
                "Sym_0(Q^17), lifted injectively to two one-time owner shares and "
                "to all four m=0,n=1 C103 slots"
            ),
            "primitive_generator": "P_ij=-alpha_ij/2*(d_i*d_j^T+d_j*d_i^T)",
            "primitive_column_count": 63,
            "primitive_exact_rank": primitive_rank,
            "primitive_augmented_rank_with_R16": primitive_augmented_rank,
            "primitive_membership_unique": True,
            "primitive_coefficients_all_one": True,
            "signed_gram_generators": (
                "+(d_i-d_j)(d_i-d_j)^T and -(d_i+d_j)(d_i+d_j)^T"
            ),
            "signed_gram_column_count": len(signed_gram_matrices),
            "signed_gram_exact_rank": signed_gram_rank,
            "signed_gram_augmented_rank_with_R16": signed_gram_augmented_rank,
            "signed_gram_conic_membership": True,
            "all_signed_gram_coefficients_nonnegative": True,
            "source_coefficients": list(source_rows),
        },
        "rational_gram_difference": {
            "identity": "R16=X_plus-X_minus",
            "X_plus_factor_columns": 63,
            "X_minus_factor_columns": 63,
            "factor_common_denominator": 64,
            "X_plus_exact_factor_rank": plus_factor_rank,
            "X_minus_exact_factor_rank": minus_factor_rank,
            "X_plus_zero_row_sum_PSD_by_rational_Gram": True,
            "X_minus_zero_row_sum_PSD_by_rational_Gram": True,
            "X_plus_trace": ftext(trace(plus)),
            "X_minus_trace": ftext(trace(minus)),
            "signed_trace": ftext(trace(residual)),
        },
        "owner_lift": {
            "formula": "Own_g(X)=sym(P_g X)",
            "owner_pieces_sum_to_target": True,
            "past_rank15_piece_nonzero": any(x != 0 for row in past for x in row),
            "past_piece_rank15_rank23_entry": ftext(past[0][8]),
            "sources_touching_past_rank15": sum(i == 0 for i, _ in CROSS_SOURCES),
            "sources_touching_omitted_rank_block_15_through_18": sum(i <= 3 for i, _ in CROSS_SOURCES),
            "primitive_generators_owner_lift_checked": 63,
            "signed_gram_generators_owner_lift_checked": 126,
        },
        "C103_minimal_embedding": {
            "finite_horizons": {"m": 0, "n": 1},
            "w_0": "1/1",
            "c_0_L": "1/1",
            "potential_factors": {key: ftext(value) for key, value in c103_potential_factors().items()},
            "row_slot_factors": {key: ftext(value) for key, value in c103_slot_factors().items()},
            "exact_curl_checked": True,
            "exact_Abel_identity": "lhs=final-initial+upper_scale_terminal",
            "initial_boundary_retained_nonzero": True,
            "final_boundary_retained_nonzero": True,
            "upper_scale_terminal_retained_nonzero": True,
            "all_slots_owner_partitioned": True,
            "primitive_generators_all_slots_checked": 63,
            "signed_gram_generators_all_slots_checked": 126,
        },
        "exact_no_go_gates": {
            "positive_Gram_only_cone": {
                "separator_vector_nonzero_indices": [0, 8],
                "separator_vector_values": ["1/1", "1/1"],
                "functional_on_every_positive_Gram_root": "(q dot z)^2 >= 0",
                "functional_on_R16": ftext(negative_value),
                "conclusion": "R16 is not in any nonnegative cone of positive Gram roots",
            },
            "indefinite_second_direction": {
                "vector_nonzero_indices": [0, 8],
                "vector_values": ["1/1", "-1/1"],
                "functional_on_R16": ftext(positive_value),
            },
            "drop_shared_rank15_boundary": {
                "all_allowed_matrices_have_entry_local_0_8": "0/1",
                "target_entry_local_0_8": ftext(residual[0][8]),
                "past_owner_target_entry_local_0_8": ftext(past[0][8]),
            },
            "mapped_C123_support_only_ranks19_through31": {
                "all_allowed_matrices_have_entry_local_1_8": "0/1",
                "target_entry_local_1_8": ftext(residual[1][8]),
            },
        },
        "canonical_dependencies": {
            str(path): sha256(path) for path in CANONICAL_DEPENDENCIES
        },
        "theorem_boundary": {
            "proved": (
                "The exact 63-source residual is in the nonnegative cone of the "
                "stated signed primitive generators and in the nonnegative cone of "
                "126 signed rank-one Gram generators after the one-time rank15|16..31 "
                "owner lift and an explicit finite m=0,n=1 C103 boundary-terminal lift."
            ),
            "not_proved": (
                "The signed negative Gram bank is not a positive capacity.  No actual "
                "32-mark cellwise owner inequalities, common physical phase, adjacent "
                "epoch stitch, birth/cutoff/shared-endpoint/final ledger, arbitrary "
                "horizon, C058, Q1, or Q2 is proved."
            ),
        },
    }
    certificate["integrity"] = {
        "payload_sha256": _canonical_hash(certificate),
    }
    return certificate


def build_certificate() -> dict[str, object]:
    return copy.deepcopy(_build_uncached())


def verify_certificate(certificate: Mapping[str, object]) -> dict[str, object]:
    expected = _build_uncached()
    if certificate.get("schema") != SCHEMA or certificate.get("status") != STATUS:
        raise CertificateError("schema or status changed")
    scope = certificate.get("scope")
    if not isinstance(scope, Mapping):
        raise CertificateError("scope is missing")
    _assert_scope(scope)
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping):
        raise CertificateError("integrity is missing")
    payload = {key: value for key, value in certificate.items() if key != "integrity"}
    if integrity.get("payload_sha256") != _canonical_hash(payload):
        raise CertificateError("payload hash mismatch")
    if dict(certificate) != expected:
        raise CertificateError("certificate differs from exact recomputation")
    return expected


def load_certificate(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise CertificateError("certificate root is not an object")
    return value


def write_certificate(path: Path) -> dict[str, object]:
    certificate = build_certificate()
    path.write_text(
        json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return certificate


def summary(certificate: Mapping[str, object]) -> str:
    residual = certificate["residual"]
    generators = certificate["generator_space"]
    nogo = certificate["exact_no_go_gates"]
    return (
        "C134_RESIDUAL63_EXACT_OK "
        f"sources={residual['cross_source_count']} "
        f"mass={residual['alpha_mass']} "
        f"primitive_rank={generators['primitive_exact_rank']} "
        f"signed_gram_rank={generators['signed_gram_exact_rank']} "
        f"positive_only_separator={nogo['positive_Gram_only_cone']['functional_on_R16']} "
        "ranks15_18=retained C103_rows=retained C058_open"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    certificate = write_certificate(args.certificate) if args.write else load_certificate(args.certificate)
    verified = verify_certificate(certificate)
    if args.pretty:
        print(json.dumps(verified, indent=2, sort_keys=True, ensure_ascii=False))
    print(summary(verified))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

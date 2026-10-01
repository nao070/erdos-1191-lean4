#!/usr/bin/env python3
"""Exact certificate for the conditional centered multiband history carrier.

All numerical checks use ``Fraction`` arithmetic.  The certificate isolates a
centered covariance carrier under a hypothetical eventually C-critical dyadic
history.  It does not supply the still-missing common signed-capacity coupling
to the harmonic-floor inequality, and makes no Q1, Q2, publication, or prize
claim.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path
from typing import Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "centered_multiband_history_certificate.json"
STATUS = "CONDITIONAL_CENTERED_CARRIER_ONLY_JOINT_SIGN_COUPLING_OPEN"

D = ((F(1, 4), F(0), F(0)), (F(0), F(1, 2), F(0)), (F(0), F(0), F(1, 4)))
H = (
    (F(13, 100), F(3, 25), F(0)),
    (F(3, 25), F(13, 50), F(3, 25)),
    (F(0), F(3, 25), F(13, 100)),
)
GAMMA = (F(1, 4), F(1, 2), F(1, 4))
THETA = F(3, 25)
MAX_SPAN = 12
EXPECTED_FIXTURES = 112


class CertificateError(ValueError):
    pass


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def rendered_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def ftext(value: F) -> str:
    return str(value)


def determinant(matrix: Sequence[Sequence[F]]) -> F:
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    return sum(
        ((-1 if column % 2 else 1) * matrix[0][column] * determinant(
            tuple(tuple(row[c] for c in range(size) if c != column) for row in matrix[1:])
        ) for column in range(size)),
        F(0),
    )


def matvec(matrix: Sequence[Sequence[F]], vector: Sequence[F]) -> tuple[F, ...]:
    return tuple(sum((x * y for x, y in zip(row, vector)), F(0)) for row in matrix)


def quadratic(matrix: Sequence[Sequence[F]], vector: Sequence[F]) -> F:
    return sum((x * y for x, y in zip(vector, matvec(matrix, vector))), F(0))


def leading_minors(matrix: Sequence[Sequence[F]]) -> tuple[F, ...]:
    return tuple(determinant(tuple(tuple(row[:size]) for row in matrix[:size])) for size in range(1, len(matrix) + 1))


def is_golomb(ruler: Sequence[int]) -> bool:
    differences = [ruler[j] - ruler[i] for i in range(len(ruler)) for j in range(i + 1, len(ruler))]
    return len(set(differences)) == len(differences)


def spatial_prefix_fixtures() -> tuple[tuple[int, ...], ...]:
    """All normalized four-mark rulers of span at most 12.

    The history is always the increasing spatial prefix A_1=(a_1,a_2),
    A_2=(a_1,...,a_4), never an arbitrary insertion ordering.
    """
    fixtures = []
    for span in range(3, MAX_SPAN + 1):
        for middle in itertools.combinations(range(1, span), 2):
            ruler = (0, *middle, span)
            if gcd(*ruler[1:]) == 1 and is_golomb(ruler):
                fixtures.append(ruler)
    return tuple(fixtures)


def positive_differences(ruler: Sequence[int]) -> tuple[int, ...]:
    return tuple(ruler[j] - ruler[i] for i in range(len(ruler)) for j in range(i + 1, len(ruler)))


def lowpass_energy(ruler: Sequence[int], width: int) -> F:
    if width < 1:
        raise ValueError("width must be positive")
    return F(len(ruler), width) + 2 * sum(
        (F(width - difference, width * width) for difference in positive_differences(ruler) if difference < width),
        F(0),
    )


def centered_lowpass(ruler: Sequence[int], width: int) -> F:
    return lowpass_energy(ruler, width) - F(len(ruler), width)


def centered_band(ruler: Sequence[int], width: int) -> F:
    return centered_lowpass(ruler, width) - centered_lowpass(ruler, 2 * width)


def multiband_path(ruler: Sequence[int], width: int, scale_increment: int) -> F:
    if scale_increment not in (1, 2):
        raise CertificateError("path must contain exactly one or two dyadic bands")
    value = sum((centered_band(ruler, width << offset) for offset in range(scale_increment)), F(0))
    terminal = centered_lowpass(ruler, width) - centered_lowpass(ruler, width << scale_increment)
    if value != terminal:
        raise CertificateError("multiband path telescope failed")
    return value


def ceil_power_of_two_rational(value: F) -> int:
    if value <= 0:
        raise ValueError("threshold must be positive")
    answer = 1
    while F(answer) < value:
        answer *= 2
    return answer


def rational_schedule(alpha: F, first_j: int, last_j: int) -> tuple[dict[str, int], ...]:
    """Exact surrogate q_j=ceilpow2(alpha*(j+1)); alpha models 8 C log 2."""
    rows = []
    previous_s = None
    for j in range(first_j, last_j + 1):
        k = 1 << j
        q = ceil_power_of_two_rational(alpha * (j + 1))
        t = k * q
        s = t.bit_length() - 1
        if 1 << s != t:
            raise CertificateError("scheduled T is not dyadic")
        increment = None if previous_s is None else s - previous_s
        if increment is not None and increment not in (1, 2):
            raise CertificateError("scale increment is not 1 or 2")
        rows.append({"j": j, "k": k, "q": q, "T": t, "s": s, "increment": increment or 0})
        previous_s = s
    return tuple(rows)


def adjacent_new_gaps(ruler: Sequence[int]) -> tuple[int, ...]:
    k = len(ruler)
    if k < 2 or k % 2:
        raise ValueError("dyadic even prefix required")
    # Global gap convention: h_r=a_r-a_(r-1), r=k/2,...,k-1.
    # In zero-based Python edges this is ruler[u+1]-ruler[u] for
    # u=k/2-1,...,k-2.
    return tuple(ruler[index + 1] - ruler[index] for index in range(k // 2 - 1, k - 1))


def verify_adjacent_first_use(
    ruler: Sequence[int], width: int, previous_prefix: Sequence[int] | None = None
) -> dict[str, object]:
    k = len(ruler)
    if tuple(sorted(ruler)) != tuple(ruler):
        raise CertificateError("current prefix must be in increasing spatial order")
    lower_spatial_half = tuple(ruler[: k // 2])
    previous = lower_spatial_half if previous_prefix is None else tuple(previous_prefix)
    if previous != lower_spatial_half:
        raise CertificateError("history must use increasing spatial prefixes")
    gaps = adjacent_new_gaps(ruler)
    small = tuple(gap for gap in gaps if gap <= width // 2)
    if len(small) < k // 4:
        raise CertificateError("adjacent-new-gap count failed")
    delta = centered_lowpass(ruler, width) - centered_lowpass(previous, width)
    lower = F(k, 4 * width)
    if delta < sum((F(1, width) for _ in small), F(0)) or delta < lower:
        raise CertificateError("centered first-use lower bound failed")
    return {
        "ruler": list(ruler),
        "previous_spatial_prefix": list(previous),
        "T": width,
        "adjacent_new_gaps": list(gaps),
        "small_gap_count": len(small),
        "required_count": k // 4,
        "centered_first_use": ftext(delta),
        "lower_bound": ftext(lower),
    }


def fejer_weight(j: int, horizon: int) -> F:
    return F((horizon + 1 - j) ** 2, (horizon + 1) ** 2)


def verify_path_ledger(ruler: Sequence[int]) -> dict[str, object]:
    """Two-stage exact ledger on A_1=(a1,a2), A_2=(a1,...,a4)."""
    prefixes = {1: tuple(ruler[:2]), 2: tuple(ruler[:4])}
    widths = {1: 32, 2: 64, 3: 256}
    horizon = 2
    c = {(j, m): centered_lowpass(prefixes[j], widths[m]) for j in prefixes for m in widths}
    x = {j: c[j, j] - c[j, j + 1] for j in prefixes}
    weights = {j: fejer_weight(j, horizon) for j in prefixes}
    lhs = sum((weights[j] * x[j] for j in prefixes), F(0))
    first_use = c[2, 2] - centered_lowpass(prefixes[1], widths[2])
    rhs = (
        weights[1] * c[1, 1]
        + weights[2] * first_use
        - (weights[1] - weights[2]) * c[1, 2]
        - weights[2] * c[2, 3]
    )
    if lhs != rhs:
        raise CertificateError("Fejer path ledger failed")
    scale_increments = {1: 1, 2: 2}
    for j in prefixes:
        band_sum = multiband_path(prefixes[j], widths[j], scale_increments[j])
        if band_sum != x[j]:
            raise CertificateError("multiband path telescope failed")
    if not all(F(0) <= value < 1 for value in c.values()):
        raise CertificateError("centered lowpass range failed")
    return {
        "ruler": list(ruler),
        "prefixes": {str(j): list(value) for j, value in prefixes.items()},
        "T": {str(j): value for j, value in widths.items()},
        "scale_increments": [scale_increments[1], scale_increments[2]],
        "weights": {str(j): ftext(value) for j, value in weights.items()},
        "C": {f"{j},{m}": ftext(value) for (j, m), value in sorted(c.items())},
        "X": {str(j): ftext(value) for j, value in x.items()},
        "centered_first_use_j2": ftext(first_use),
        "ledger_lhs": ftext(lhs),
        "ledger_rhs": ftext(rhs),
    }


def matrix_certificate() -> dict[str, object]:
    minors = leading_minors(H)
    if minors != (F(13, 100), F(97, 5000), F(13, 20000)):
        raise CertificateError("unexpected H leading minors")
    if matvec(H, (F(1), F(1), F(1))) != GAMMA or matvec(D, (F(1), F(1), F(1))) != GAMMA:
        raise CertificateError("row-sum/constant-cover identity failed")
    samples = ((F(1), F(0), F(0)), (F(2), F(-1), F(3)), (F(7, 3), F(5, 2), F(-4, 7)))
    for vector in samples:
        path = (vector[0] - vector[1]) ** 2 + (vector[1] - vector[2]) ** 2
        if quadratic(D, vector) - quadratic(H, vector) != THETA * path:
            raise CertificateError("retained path-square identity failed")
    return {
        "D": [[ftext(value) for value in row] for row in D],
        "H": [[ftext(value) for value in row] for row in H],
        "theta": ftext(THETA),
        "gamma": [ftext(value) for value in GAMMA],
        "H_leading_minors": [ftext(value) for value in minors],
        "H_row_sums": [ftext(value) for value in matvec(H, (F(1), F(1), F(1)))],
        "D_row_sums": [ftext(value) for value in matvec(D, (F(1), F(1), F(1)))],
        "inverse_metric_constant_cover": "H^{-1}gamma=D^{-1}gamma=(1,1,1)",
        "retained_identity": "y'Dy-y'Hy=theta*((y1-y2)^2+(y2-y3)^2)",
    }


def boundary_record(k: int, q_j_plus_1: int, ambient_length: int) -> dict[str, object]:
    """Check B/N for k_j=k and T_(j+1)=k_(j+1)q_(j+1)=2kq_(j+1)."""
    if q_j_plus_1 < 1 or q_j_plus_1 & (q_j_plus_1 - 1):
        raise CertificateError("q_(j+1) must be a positive power of two")
    t_next = 2 * k * q_j_plus_1
    # The largest of (K_Tj,K_2Tj,K_T(j+1)) has support T_(j+1),
    # hence exactly N+T_(j+1)-1 full-support convolution sites.
    b = ambient_length + t_next - 1
    ratio = F(b - ambient_length, ambient_length)
    sidon_minimum = 1 + k * (k - 1) // 2
    if ambient_length < sidon_minimum:
        raise CertificateError("ambient length violates Sidon counting lower bound")
    q_bound = F(4 * q_j_plus_1, k - 1)
    if ratio > q_bound:
        raise CertificateError("exact boundary ratio bound failed")
    return {
        "k": k,
        "q_next": q_j_plus_1,
        "T_next": t_next,
        "N": ambient_length,
        "B": b,
        "B_over_N_minus_1": ftext(ratio),
        "exact_upper_bound": ftext(q_bound),
        "implication": "if q_(j+1)<16*C*log(4k), ratio<64*C*log(4k)/(k-1)=O_C(j/2^j)",
    }


def build_body() -> dict[str, object]:
    fixtures = spatial_prefix_fixtures()
    if len(fixtures) != EXPECTED_FIXTURES:
        raise CertificateError("fixture enumeration changed")
    first_use_records = [verify_adjacent_first_use(ruler, 64) for ruler in fixtures]
    ledgers = [verify_path_ledger(ruler) for ruler in fixtures]
    min_first = min(first_use_records, key=lambda row: (F(row["centered_first_use"]), tuple(row["ruler"])))
    alphas = (F(1, 3), F(1), F(8), F(1191, 100))
    schedules = [rational_schedule(alpha, 1, 128) for alpha in alphas]
    increment_counts = {1: 0, 2: 0}
    for schedule in schedules:
        for row in schedule[1:]:
            increment_counts[row["increment"]] += 1
    coefficient_margin = F(3, 3200) - F(1, 1536)
    if coefficient_margin != F(11, 38400):
        raise CertificateError("coefficient margin changed")
    return {
        "schema": "erdos1191.centered_multiband_history.v1",
        "status": STATUS,
        "scope": {
            "conditional_on_eventual_C_critical_history": True,
            "centered_scalar_carrier": True,
            "internal_single_owner_ledger": True,
            "common_signed_capacity_coupling": False,
            "q1_resolved": False,
            "q2_resolved": False,
            "publication_ready": False,
            "prize_claim_ready": False,
            "novelty_claim": False,
        },
        "matrix": matrix_certificate(),
        "analytic_identities": {
            "onset": "choose j0(C) so the critical cap holds and 8*C*log(2k_j)>=1 for j>=j0; then q_j and T_j are positive integer powers of two",
            "centered_lowpass": "C_(j,r)=||1_Aj*K_(2^r)||^2-k_j/2^r=2*sum_(d<2^r)(2^r-d)/2^(2r)",
            "centered_band": "O_(2^r)(A_j)=C_(j,r)-C_(j,r+1)",
            "schedule": "q_j=2^ceil(log2(8*C*log(2k_j))), T_j=k_j*q_j=2^s_j; s_(j+1)-s_j in {1,2}",
            "first_use": "Delta_tilde_(j,s_j)=C_(j,s_j)-C_(j-1,s_j)>=k_j/(4T_j)>1/(64*C*log(2k_j))",
            "path": "X_j=sum_(r=s_j)^(s_(j+1)-1) O_(2^r)(A_j)=C_(j,s_j)-C_(j,s_(j+1))",
            "fejer_ledger": "sum w_j X_j=w_j0*C_j0,s_j0+sum_(j>j0)[w_j*Delta_tilde_j,s_j-(w_(j-1)-w_j)*C_(j-1),s_j]-w_J*C_J,s_(J+1)",
            "weighted_lower_bound": "sum w_j X_j >= (64*C*log(2))^-1*log J-O_C(1)",
            "gain": "sum w_j*G_j^off/N_j >= 3/(1600*C*log(2))*log J-O_C(1)",
            "safe_eta": "eta_C=3/(3200*C*log(2))",
        },
        "schedule_checks": {
            "exact_surrogate": "q_j=ceilpow2(alpha*(j+1)), alpha>0; alpha represents 8*C*log(2)",
            "alphas": [ftext(value) for value in alphas],
            "j_range": [1, 128],
            "records": sum(len(value) for value in schedules),
            "increment_counts": {str(key): value for key, value in increment_counts.items()},
            "allowed_increments": [1, 2],
        },
        "finite_fixture_enumeration": {
            "definition": "all increasing normalized four-mark Golomb rulers with span<=12; A_1 is first 2 marks and A_2 is first 4 marks in spatial order",
            "count": len(fixtures),
            "max_span": MAX_SPAN,
            "T_path": [32, 64, 256],
            "first_use_checks": len(first_use_records),
            "ledger_checks": len(ledgers),
            "minimum_first_use_record": min_first,
            "representative_ledger": ledgers[0],
        },
        "boundary": boundary_record(16, 32, 1 + 16 * 15 // 2),
        "coefficient": {
            "raw_numerator": "3/1600",
            "safe_numerator": "3/3200",
            "required_floor_numerator": "1/1536",
            "safe_margin": ftext(coefficient_margin),
        },
        "open_obligation": {
            "checkpoint": "C058 remains OPEN",
            "missing": "one common finite inequality/capacity map placing this centered covariance carrier and the harmonic-floor atoms under opposite signs",
            "warning": "the uncentered diagonal Parseval contribution is harmonic and is not an O(1) error",
            "nonclaim": "No Q1/Q2 resolution, publication-ready proof, prize claim, or novelty claim.",
        },
    }


_EXPECTED: dict[str, object] | None = None


def build_certificate() -> dict[str, object]:
    body = build_body()
    body["payload_sha256"] = hashlib.sha256(canonical_bytes(body)).hexdigest()
    return body


def expected_certificate() -> dict[str, object]:
    global _EXPECTED
    if _EXPECTED is None:
        _EXPECTED = build_certificate()
    return copy.deepcopy(_EXPECTED)


def rehash(value: dict[str, object]) -> None:
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical_bytes(value)).hexdigest()


def validate_certificate(value: dict[str, object]) -> None:
    if not isinstance(value, dict):
        raise CertificateError("certificate must be an object")
    body = dict(value)
    supplied = body.pop("payload_sha256", None)
    if supplied != hashlib.sha256(canonical_bytes(body)).hexdigest():
        raise CertificateError("payload hash mismatch")
    if value != expected_certificate():
        raise CertificateError("semantic replay mismatch")


def self_check(value: dict[str, object]) -> int:
    validate_certificate(value)
    mutations = (
        (("scope", "common_signed_capacity_coupling"), True),
        (("scope", "q1_resolved"), True),
        (("matrix", "theta"), "1/8"),
        (("schedule_checks", "allowed_increments"), [0, 1, 2]),
        (("finite_fixture_enumeration", "count"), 0),
        (("coefficient", "safe_margin"), "0"),
        (("open_obligation", "checkpoint"), "C058 CLOSED"),
        (("open_obligation", "warning"), "diagonal is O(1)"),
    )
    for path, replacement in mutations:
        changed = copy.deepcopy(value)
        cursor = changed
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = replacement
        rehash(changed)
        try:
            validate_certificate(changed)
        except CertificateError:
            pass
        else:
            raise AssertionError(f"mutation accepted: {path}")
    bad_hash = copy.deepcopy(value)
    bad_hash["payload_sha256"] = "0" * 64
    try:
        validate_certificate(bad_hash)
    except CertificateError:
        pass
    else:
        raise AssertionError("hash mutation accepted")
    return len(mutations) + 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", type=Path)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args(argv)
    if args.verify:
        value = json.loads(args.verify.read_text(encoding="utf-8"))
        validate_certificate(value)
        if args.verify.read_bytes() != rendered_bytes(value):
            raise CertificateError("certificate is not byte-canonical")
        print(f"certificate verify: PASS {value['payload_sha256']}")
    else:
        value = build_certificate()
        print(rendered_bytes(value).decode(), end="")
    if args.self_check:
        print(f"self-check: PASS ({self_check(value)} mutations rejected)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

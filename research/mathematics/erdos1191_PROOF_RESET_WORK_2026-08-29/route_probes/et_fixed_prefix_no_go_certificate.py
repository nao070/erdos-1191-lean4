#!/usr/bin/env python3
"""Exact finite ET-family certificate for a fixed-prefix comparison no-go.

The finite fixtures vary with the dyadic cardinality.  They refute a uniform
same-prefix comparison between Wave-19 ``W_n`` and the scheduled centered box
gain.  They do not form one nested infinite Sidon branch and make no claim
about Q1, Q2, publication readiness for Problem #1191, prizes, or novelty.
"""
from __future__ import annotations

import argparse
import copy
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from typing import Sequence


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "et_fixed_prefix_no_go_certificate.json"
DYADIC_K = (8, 16, 32, 64, 128, 256, 512)
STATUS = "FINITE_FIXED_PREFIX_NO_GO_ONLY_INFINITE_HISTORY_OPEN"
LOG_TWO_TERMS = 32


class CertificateError(ValueError):
    pass


def canonical_bytes(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def rendered_bytes(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def ftext(value: F) -> str:
    return str(value)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def least_prime_strictly_above(value: int) -> int:
    candidate = value + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def et_points(k: int, p: int) -> tuple[int, ...]:
    if k < 4 or k & (k - 1):
        raise ValueError("k must be a dyadic integer at least four")
    if not is_prime(p) or not k < p < 2 * k:
        raise ValueError("p must be a prime strictly between k and 2k")
    return tuple(2 * p * index + (index * index % p) for index in range(k))


def positive_differences(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    return tuple(marks[right] - marks[left] for right in range(1, len(marks)) for left in range(right))


def is_sidon(points: Sequence[int]) -> bool:
    marks = tuple(points)
    differences = positive_differences(marks)
    return (
        bool(marks)
        and marks[0] == 0
        and all(left < right for left, right in zip(marks, marks[1:]))
        and len(differences) == len(set(differences))
    )


def adjacent_gaps(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    return tuple(right - left for left, right in zip(marks, marks[1:]))


def centered_lowpass(points: Sequence[int], width: int) -> F:
    if width < 1:
        raise ValueError("width must be positive")
    return 2 * sum(
        (F(width - difference, width * width) for difference in positive_differences(points) if difference < width),
        F(0),
    )


def log_two_interval(terms: int = LOG_TWO_TERMS) -> tuple[F, F]:
    """Rigorous interval from log(2)=2*sum 3^-(2m+1)/(2m+1)."""
    if terms < 1:
        raise ValueError("at least one series term is required")
    x = F(1, 3)
    lower = 2 * sum((x ** (2 * index + 1) / (2 * index + 1) for index in range(terms)), F(0))
    remainder = 2 * x ** (2 * terms + 1) / ((2 * terms + 1) * (1 - x * x))
    return lower, lower + remainder


def ceil_power_of_two(value: F) -> int:
    if value <= 0:
        raise ValueError("threshold must be positive")
    answer = 1
    while F(answer) < value:
        answer *= 2
    return answer


def schedule_record(k: int) -> dict[str, object]:
    if k < 2 or k & (k - 1):
        raise ValueError("k must be dyadic")
    j = k.bit_length() - 1
    lower, upper = log_two_interval()
    threshold_lower = 8 * (j + 1) * lower
    threshold_upper = 8 * (j + 1) * upper
    next_lower = 8 * (j + 2) * lower
    next_upper = 8 * (j + 2) * upper
    q_lower = ceil_power_of_two(threshold_lower)
    q_upper = ceil_power_of_two(threshold_upper)
    q_next_lower = ceil_power_of_two(next_lower)
    q_next_upper = ceil_power_of_two(next_upper)
    if q_lower != q_upper or q_next_lower != q_next_upper:
        raise CertificateError("log(2) interval does not determine the dyadic schedule")
    t = k * q_lower
    t_next = 2 * k * q_next_lower
    if t_next // t not in (2, 4) or t_next % t:
        raise CertificateError("scheduled scale increment is not one or two bands")
    return {
        "j": j,
        "q": q_lower,
        "q_next": q_next_lower,
        "T": t,
        "T_next": t_next,
        "scale_ratio": t_next // t,
        "threshold_lower": ftext(threshold_lower),
        "threshold_upper": ftext(threshold_upper),
        "threshold_next_lower": ftext(next_lower),
        "threshold_next_upper": ftext(next_upper),
    }


def approximation_error_bound(k: int, p: int, width: int) -> F:
    if min(k, p, width) < 1:
        raise ValueError("positive parameters required")
    return F(2 * k, width) + F(4 * p * k, width * width) + F(width, 4 * p * p) + F(1, 2 * p)


def w_atom_weight(epoch: int, left: int, right: int) -> F:
    if epoch <= left <= right - 2 and epoch + 2 <= right <= 2 * epoch - 1:
        return F((right - left) ** 2, 4 * epoch * epoch)
    return F(0)


def formal_w_audit(points: Sequence[int], epoch: int) -> dict[str, object]:
    marks = tuple(points)
    if len(marks) != 2 * epoch:
        raise ValueError("W_n requires exactly 2n marks")
    exponents: defaultdict[int, F] = defaultdict(F)
    cells = 0
    for right in range(epoch + 2, 2 * epoch):
        for left in range(epoch, right - 1):
            weight = w_atom_weight(epoch, left, right)
            middle = marks[right - 1] - marks[left]
            left_gap = marks[left] - marks[left - 1]
            right_gap = marks[right] - marks[right - 1]
            outer = middle + left_gap + right_gap
            exponents[middle + left_gap] += weight
            exponents[middle + right_gap] += weight
            exponents[middle] -= weight
            exponents[outer] -= weight
            cells += 1
    ledger = ";".join(f"{base}:{coefficient}" for base, coefficient in sorted(exponents.items()) if coefficient)
    n = epoch
    layered = sum(
        (F((n - separation) * separation * separation, 36 * n * n * (separation + 1) ** 2)
         for separation in range(2, n)),
        F(0),
    )
    simple = F((n - 2) * (n - 1), 162 * n * n)
    if layered < simple:
        raise CertificateError("layered W lower bound does not imply the simple bound")
    return {
        "cells": cells,
        "formal_nonzero_log_bases": sum(bool(value) for value in exponents.values()),
        "formal_log_sha256": hashlib.sha256(ledger.encode("ascii")).hexdigest(),
        "layered_rational_lower": ftext(layered),
        "simple_rational_lower": ftext(simple),
        "proof": "C_ij>1/[9(r+1)^2] and there are n-r cells of separation r",
    }


def fixture_record(k: int) -> dict[str, object]:
    if k not in DYADIC_K:
        raise ValueError("k is not in the certified dyadic fixture list")
    p = least_prime_strictly_above(k)
    points = et_points(k, p)
    if not is_sidon(points):
        raise CertificateError("ET fixture is not Sidon")
    ambient = points[-1] + 1
    if ambient >= 4 * k * k:
        raise CertificateError("quadratic span bound failed")
    gaps = adjacent_gaps(points)
    if not all(p + 1 <= gap <= 3 * p - 1 for gap in gaps):
        raise CertificateError("ET adjacent-gap bounds failed")
    schedule = schedule_record(k)
    t = int(schedule["T"])
    t_next = int(schedule["T_next"])
    c_t = centered_lowpass(points, t)
    c_next = centered_lowpass(points, t_next)
    target = F(k, 2 * p)
    error_t = approximation_error_bound(k, p, t)
    error_next = approximation_error_bound(k, p, t_next)
    if abs(c_t - target) > error_t or abs(c_next - target) > error_next:
        raise CertificateError("exact fixture violates the analytic approximation bound")
    w_audit = formal_w_audit(points, k // 2)
    boundary = F(t_next - 1, ambient)
    return {
        "k": k,
        "n": k // 2,
        "p": p,
        "index_range": [0, k - 1],
        "N": ambient,
        "N_lt_4k2": ambient < 4 * k * k,
        "gap_min": min(gaps),
        "gap_max": max(gaps),
        "gap_lower": p + 1,
        "gap_upper": 3 * p - 1,
        **schedule,
        "C_T": ftext(c_t),
        "C_T_next": ftext(c_next),
        "X": ftext(c_t - c_next),
        "AP_target": ftext(target),
        "error_bound_T": ftext(error_t),
        "error_bound_T_next": ftext(error_next),
        "X_error_bound": ftext(error_t + error_next),
        "analytic_regime_T": t < 2 * p * (k - 1),
        "analytic_regime_T_next": t_next < 2 * p * (k - 1),
        "B_over_N_minus_1": ftext(boundary),
        "W_cells": w_audit["cells"],
        "W_formal_nonzero_log_bases": w_audit["formal_nonzero_log_bases"],
        "W_formal_log_sha256": w_audit["formal_log_sha256"],
        "layered_rational_lower": w_audit["layered_rational_lower"],
        "simple_rational_lower": w_audit["simple_rational_lower"],
    }


def build_body() -> dict[str, object]:
    records = [fixture_record(k) for k in DYADIC_K]
    lower, upper = log_two_interval()
    return {
        "schema": "erdos1191.et_fixed_prefix_no_go.v1",
        "status": STATUS,
        "scope": {
            "finite_fixed_prefix_no_go": True,
            "changing_family_across_k": True,
            "infinite_counterexample": False,
            "fixed_branch_history_refuted": False,
            "q1_resolved": False,
            "q2_resolved": False,
            "publication_ready_proof_of_1191": False,
            "prize_claim_ready": False,
            "novelty_claim": False,
        },
        "theorem_contract": {
            "quantifiers": "for every fixed C>0 and K<infinity, arbitrarily large dyadic k admit a finite k-mark ET Sidon prefix under N<=C*k^2*log(2k) with W_(k/2)>K*|X_k| and W_(k/2)>K*|G_k^off|/N_k",
            "boundary": "the witnesses are a changing finite family indexed by k; this does not construct one nested infinite branch and does not refute a compatible-history or Fejer telescope theorem",
            "refutes_single_prefix_uniform_comparison": True,
            "refutes_fixed_infinite_branch_history_theorem": False,
            "schedule_scope": "C=1 canonical exact fixtures; the symbolic asymptotic proof holds for every fixed C>0",
        },
        "analytic_proof_contract": {
            "construction": "a_m=2*p*m+rho_m for 0<=m<k, rho_m is the least residue of m^2 mod p, and k<p<2k is prime",
            "Sidon": "equal differences force equal index gaps because the residue error has absolute value <2p; reduction mod p then forces equal left endpoints",
            "span_cap": "N<2pk<4k^2, hence N<=C*k^2*log(2k) for every fixed C>0 and all sufficiently large k",
            "gap_bounds": "p+1<=h_m<=3p-1",
            "W_lower": "W_n>(n-2)(n-1)/(162n^2), so liminf W_n>=1/162",
            "C_S_approximation": "|C_S(A)-k/(2p)|<=2k/S+4pk/S^2+S/(4p^2)+1/(2p) once S<2p(k-1); listed earlier fixtures outside this asymptotic regime are separately replayed exactly",
            "schedule": "T=k*ceilpow2(8*C*log(2k)); T_next=2k*ceilpow2(8*C*log(4k)); T_next/T is 2 or 4",
            "X_limit": "for fixed C, |X|=O(1/[C log k]+1/[C^2 log^2 k]+C log k/k), hence X tends to zero",
            "normalized_gain": "the constant cover has B=N+T_next-1 and B/N tends to 1, so every fixed-theta normalized centered gain also tends to zero",
        },
        "log_two_interval": {
            "series": "log(2)=2*sum_(m>=0) 3^-(2m+1)/(2m+1)",
            "terms": LOG_TWO_TERMS,
            "lower": ftext(lower),
            "upper": ftext(upper),
            "width": ftext(upper - lower),
        },
        "finite_fixtures": records,
        "open_boundary": {
            "not_refuted": "one fixed nested infinite Sidon branch, cross-prefix Fejer ownership, adaptive noncritical widths, and rank-aware continuum dipole carriers",
            "q1_q2": "No Q1/Q2 resolution and no infinite counterexample.",
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
        (("scope", "finite_fixed_prefix_no_go"), False),
        (("scope", "changing_family_across_k"), False),
        (("scope", "infinite_counterexample"), True),
        (("scope", "q1_resolved"), True),
        (("scope", "q2_resolved"), True),
        (("scope", "publication_ready_proof_of_1191"), True),
        (("scope", "prize_claim_ready"), True),
        (("theorem_contract", "refutes_fixed_infinite_branch_history_theorem"), True),
        (("theorem_contract", "quantifiers"), "there exists one infinite counterexample"),
        (("analytic_proof_contract", "W_lower"), "W_n>1"),
        (("analytic_proof_contract", "C_S_approximation"), "error=0"),
        (("finite_fixtures", 0, "p"), 13),
        (("finite_fixtures", -1, "X"), "0"),
        (("finite_fixtures", 2, "W_formal_log_sha256"), "0" * 64),
        (("log_two_interval", "terms"), 1),
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

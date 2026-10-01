#!/usr/bin/env python3
"""Audit the uploaded C143 report's arithmetic and identity, not its proof.

Python 3.9+. No third-party packages. Does not execute the full-pricing oracle,
reconstruct the mathematical objects, or establish Q1.
"""
from __future__ import annotations
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

if hasattr(sys, "set_int_max_str_digits"):
    # The user-supplied exact interval contains intentionally very large integers.
    sys.set_int_max_str_digits(0)

EXPECTED_SHA256 = "d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4"
EXPECTED_BYTES = 144_369_995
ROOT = Path(__file__).resolve().parents[1]


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def approximate(value: Fraction) -> str:
    with localcontext() as context:
        context.prec = 24
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def audit_report(data: dict[str, Any]) -> dict[str, Any]:
    """Verify the report format/claims and exact arithmetic; never replay the oracle."""
    require(isinstance(data, dict), "Report must be a JSON object")
    expected = {
        "status": "C143_INDEPENDENT_EXACT_FULL_PRICING_OK",
        "mode": "full",
        "exit_code": 0,
        "full_root_endpoint_checks": 90_600_510,
        "children_checked": 1_890,
        "endpoints_checked": 961,
        "bank_bytes": EXPECTED_BYTES,
        "bank_sha256": EXPECTED_SHA256,
    }
    for key, value in expected.items():
        require(key in data and type(data[key]) is type(value) and data[key] == value,
                f"Unexpected or missing {key}; this auditor is for the supplied replay report")
    scope = data.get("scope")
    require(isinstance(scope, dict), "Missing scope object")
    require(scope.get("finite_target_fixture_only") is True, "Finite-fixture scope must be explicit")
    for key in ("Q1_resolved", "Q2_resolved", "C058_proved",
                "history_independent_eta_proved", "nonanticipating_global_ledger_proved",
                "single_phase_global_witness_proved", "uniform_over_all_C116_histories"):
        require(scope.get(key) is False, f"Unexpected claimed proof status: {key}")
    for key in ("aggregate_lower", "aggregate_upper", "min_pointwise_child_margin"):
        require(isinstance(data.get(key), str), f"Missing rational string: {key}")
    try:
        lower = Fraction(data["aggregate_lower"])
        upper = Fraction(data["aggregate_upper"])
        margin = Fraction(data["min_pointwise_child_margin"])
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError("Invalid exact rational data") from exc
    require(Fraction(4694333, 100000000) < lower < upper < Fraction(4694335, 100000000),
            "Exact aggregate interval does not satisfy the reported strict bounds")
    require(margin > 0, "Reported minimum child margin must be positive")
    return {
        "status": "REPORT_ARITHMETIC_VERIFIED",
        "scope": "Internal consistency and rational comparisons of the saved report only",
        "recorded_full_root_endpoint_checks": data["full_root_endpoint_checks"],
        "recorded_exit_code": data["exit_code"],
        "strict_enclosure": "0.04694333 < aggregate_lower < aggregate_upper < 0.04694335",
        "lower_approximation": approximate(lower),
        "upper_approximation": approximate(upper),
        "minimum_margin_exact": str(margin),
        "minimum_margin_approximation": approximate(margin),
        "bank_identity_checked": False,
        "payload_hash_recomputed": False,
        "full_pricing_replayed": False,
        "Lean_executed": False,
        "Q1_proved": False,
    }


def no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path,
                        default=ROOT / "inputs/c143_full_pricing_replay.full.json")
    parser.add_argument("--bank", type=Path, help="Optional original bank; only byte-size/hash checked")
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()
    try:
        data = json.loads(args.report.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys)
        result = audit_report(data)
        result["report_bytes"] = args.report.stat().st_size
        result["report_sha256"] = digest_file(args.report)
        if args.bank is not None:
            require(args.bank.is_file(), "Bank path does not point to a file")
            require(args.bank.stat().st_size == EXPECTED_BYTES, "Bank byte size does not match")
            bank_digest = digest_file(args.bank)
            require(bank_digest == EXPECTED_SHA256, "Bank SHA-256 does not match")
            result["bank_identity_checked"] = True
            result["bank_sha256"] = bank_digest
        encoded = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output is not None:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(encoded, encoding="utf-8")
        print(encoded, end="")
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"status": "AUDIT_FAILED", "error": str(exc), "Q1_proved": False}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

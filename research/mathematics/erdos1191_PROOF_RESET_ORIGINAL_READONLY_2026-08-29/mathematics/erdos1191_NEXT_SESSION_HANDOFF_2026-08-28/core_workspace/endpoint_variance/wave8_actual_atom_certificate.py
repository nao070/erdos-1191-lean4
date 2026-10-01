"""Build the deterministic Wave 8 actual-renewal/Q-atom certificate."""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any

from wave7_band_renewal_probe import load_authenticated_wave6_fixtures
from wave8_actual_adjacent_renewal import (
    audit_hybrid_ledger,
    renewal_dichotomy,
    renewal_history,
)
from wave8_q_atom_verifier import (
    audit_q_atom_identities,
    nonadjacent_necessity_audit,
    rank_one_to_shell_ratio,
)

DIRECTORY = Path(__file__).resolve().parent
SOURCE_CERTIFICATE = DIRECTORY / "wave6_arithmetic_mining_certificate_2026-08-28.json"
PERFECT_FOUR = (0, 1, 4, 6)
OLD_CLEAR_ONLY_EIGHT = (0, 76, 413, 471, 595, 1283, 1424, 1624)
NEW_PAY_ONLY_EIGHT = (0, 768, 1064, 1216, 1303, 1423, 1676, 1922)
DEBT_REPAID_SIXTEEN = (
    0,
    76,
    413,
    471,
    595,
    1283,
    1424,
    1624,
    1694,
    1925,
    2015,
    2016,
    2059,
    2188,
    2261,
    2333,
)


def _encode(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [_encode(item) for item in value]
    if isinstance(value, list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {key: _encode(item) for key, item in value.items()}
    return value


def _internal_hash(payload: dict[str, Any]) -> str:
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return sha256(canonical.encode("utf-8")).hexdigest()


def build_certificate() -> dict[str, Any]:
    fixtures = load_authenticated_wave6_fixtures(SOURCE_CERTIFICATE)
    points128 = fixtures.one_hundred_twenty_eight_mark_points
    perfect_audit = audit_hybrid_ledger(PERFECT_FOUR)
    audit128 = audit_hybrid_ledger(points128)
    dichotomy64 = renewal_dichotomy(points128, old_count=64)
    terminal_history = renewal_history(OLD_CLEAR_ONLY_EIGHT)
    repaid_history = renewal_history(DEBT_REPAID_SIXTEEN)

    rng = random.Random(81191)
    q_audits = tuple(
        audit_q_atom_identities(
            (1,) + tuple(rng.randint(1, 10_000) for _ in range(2 * old_count - 1)),
            old_count=old_count,
        )
        for old_count in range(2, 13)
        for _ in range(4)
    )
    encoded_q_audits = _encode(tuple(asdict(audit) for audit in q_audits))
    q_audit_canonical = json.dumps(
        encoded_q_audits,
        sort_keys=True,
        separators=(",", ":"),
    )
    nonadjacent = nonadjacent_necessity_audit()
    ratios = tuple(
        {
            "parameter": parameter,
            "ratio": rank_one_to_shell_ratio(parameter),
            "ratio_divided_by_parameter": (
                rank_one_to_shell_ratio(parameter) / parameter
            ),
        }
        for parameter in (2, 3, 10, 100, 1000)
    )

    payload: dict[str, Any] = {
        "schema": "wave8_actual_atom_certificate_v1",
        "research_date": "2026-08-28",
        "purpose": (
            "exact finite audit of the hybrid actual-adjacent renewal, "
            "single-debt history, and arithmetic Q-atom decompositions"
        ),
        "source_wave6_certificate_file_sha256": (fixtures.certificate_file_sha256),
        "actual_adjacent": {
            "perfect_four": asdict(perfect_audit),
            "authenticated_128": asdict(audit128),
            "authenticated_epoch_64": asdict(dichotomy64),
            "old_clear_only": asdict(
                renewal_dichotomy(OLD_CLEAR_ONLY_EIGHT, old_count=4)
            ),
            "new_pay_only": asdict(renewal_dichotomy(NEW_PAY_ONLY_EIGHT, old_count=4)),
            "terminal_single_debt_history": asdict(terminal_history),
            "later_repaid_history": asdict(repaid_history),
        },
        "q_atoms": {
            "deterministic_identity_audit_count": len(q_audits),
            "deterministic_identity_audit_sha256": sha256(
                q_audit_canonical.encode("utf-8")
            ).hexdigest(),
            "minimum_positive_envelope_margin": min(
                audit.positive_envelope - audit.normalized_q_charge
                for audit in q_audits
            ),
            "minimum_adjacent_bound_margin": min(
                audit.adjacent_debt_bound - audit.adjacent_negative_debt
                for audit in q_audits
            ),
            "nonadjacent_necessity": asdict(nonadjacent),
            "rank_one_to_shell_ratios": ratios,
            "adjacent_debt_critical_sum_constant": Fraction(13, 5),
            "canonical_cap_K_equals_2C_constant": Fraction(26, 5),
            "artificial_boundary_row_sum_bound": Fraction(92, 315),
        },
        "conclusions": {
            "hybrid_capacity_proved": True,
            "single_outstanding_adjacent_family_proved": True,
            "adjacent_kappa_debt_summable_under_critical_cap": True,
            "nonadjacent_bulk_atoms_necessary": True,
            "nonadjacent_boundary_fan_budget_proved": False,
            "rank_one_abel_fan_budget_proved": False,
            "infinite_extension_claimed": False,
            "erdos_1191_resolved": False,
        },
    }
    encoded = _encode(payload)
    encoded["certificate_sha256"] = _internal_hash(encoded)
    return encoded


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=DIRECTORY / "wave8_actual_atom_certificate_2026-08-28.json",
    )
    args = parser.parse_args()
    certificate = build_certificate()
    args.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

from wave8_actual_atom_certificate import build_certificate

DIRECTORY = Path(__file__).resolve().parent
CERTIFICATE = DIRECTORY / "wave8_actual_atom_certificate_2026-08-28.json"


def test_wave8_actual_atom_certificate_hash_and_full_replay() -> None:
    committed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    internal_hash = committed.pop("certificate_sha256")
    canonical = json.dumps(committed, sort_keys=True, separators=(",", ":"))
    assert sha256(canonical.encode("utf-8")).hexdigest() == internal_hash
    assert build_certificate() == {
        **committed,
        "certificate_sha256": internal_hash,
    }


def test_wave8_actual_atom_certificate_keeps_open_boundary_explicit() -> None:
    certificate = build_certificate()
    conclusions = certificate["conclusions"]
    assert conclusions["hybrid_capacity_proved"]
    assert conclusions["single_outstanding_adjacent_family_proved"]
    assert conclusions["adjacent_kappa_debt_summable_under_critical_cap"]
    assert conclusions["nonadjacent_bulk_atoms_necessary"]
    assert not conclusions["nonadjacent_boundary_fan_budget_proved"]
    assert not conclusions["rank_one_abel_fan_budget_proved"]
    assert not conclusions["infinite_extension_claimed"]
    assert not conclusions["erdos_1191_resolved"]
    assert certificate["q_atoms"]["adjacent_debt_critical_sum_constant"] == "13/5"
    assert certificate["q_atoms"]["artificial_boundary_row_sum_bound"] == "92/315"

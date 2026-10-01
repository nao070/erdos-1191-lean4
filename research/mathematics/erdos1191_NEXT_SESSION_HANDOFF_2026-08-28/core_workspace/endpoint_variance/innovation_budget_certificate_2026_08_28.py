"""Deterministic exact certificate for the adjoint innovation-budget reduction."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from innovation_budget import (
    ABSTRACT_COVARIANCE,
    LYAPUNOV_MATRIX,
    abstract_raw_innovation,
    adjoint_transport,
    audit_abstract_orbit,
    determinant,
    matrix_subtract,
    three_point_covariance,
    verify_infinite_horizon_lyapunov_matrix,
)
from gap_measure_dynamics import is_positive_semidefinite


OUTPUT = Path(__file__).with_name("innovation_budget_certificate_2026-08-28.json")


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    arguments = parser.parse_args()

    require(verify_infinite_horizon_lyapunov_matrix(), "Lyapunov identity failed")
    require(three_point_covariance() == ABSTRACT_COVARIANCE, "covariance realization failed")

    minimum_determinant: Fraction | None = None
    minimum_determinant_index: int | None = None
    innovation_checks = 0
    for index in range(1, 513):
        innovation = abstract_raw_innovation(index)
        require(is_positive_semidefinite(innovation), "innovation PSD check failed")
        current = determinant(innovation)
        require(current > 0, "innovation was not positive definite")
        if minimum_determinant is None or current < minimum_determinant:
            minimum_determinant = current
            minimum_determinant_index = index
        innovation_checks += 1

    horizon_checks = 0
    terminal_audit = None
    for horizon in range(1, 129):
        audit = audit_abstract_orbit(horizon)
        require(audit.functional_sum == Fraction(horizon, 72), "linear energy sum failed")
        require(
            audit.functional_sum == audit.boundary_term + audit.innovation_sum,
            "adjoint telescoping check failed",
        )
        terminal_audit = audit
        horizon_checks += 1
    require(terminal_audit is not None, "missing terminal audit")
    require(minimum_determinant is not None, "missing determinant minimum")
    require(minimum_determinant_index is not None, "missing determinant argmin")

    residual = matrix_subtract(LYAPUNOV_MATRIX, adjoint_transport(LYAPUNOV_MATRIX))
    payload = {
        "schema": "erdos1191.innovation_budget_certificate.v1",
        "arithmetic": "fractions.Fraction",
        "lyapunov_matrix": [
            [fraction_text(value) for value in row] for row in LYAPUNOV_MATRIX
        ],
        "lyapunov_residual": [
            [fraction_text(value) for value in row] for row in residual
        ],
        "lyapunov_determinant": fraction_text(determinant(LYAPUNOV_MATRIX)),
        "abstract_covariance": [
            [fraction_text(value) for value in row] for row in ABSTRACT_COVARIANCE
        ],
        "innovation_positive_definite_checks": innovation_checks,
        "innovation_index_range_inclusive": [1, 512],
        "minimum_raw_innovation_determinant": fraction_text(minimum_determinant),
        "minimum_raw_innovation_determinant_index": minimum_determinant_index,
        "adjoint_horizon_checks": horizon_checks,
        "adjoint_horizon_range_inclusive": [1, 128],
        "terminal_horizon": terminal_audit.horizon,
        "terminal_functional_sum": fraction_text(terminal_audit.functional_sum),
        "terminal_boundary_term": fraction_text(terminal_audit.boundary_term),
        "terminal_innovation_sum": fraction_text(terminal_audit.innovation_sum),
        "scope_warning": (
            "The orbit is an abstract PSD-recursion no-go; its innovations are not "
            "claimed to arise from compatible integer Golomb/Sidon birth shells."
        ),
        "all_checks_passed": True,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    arguments.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate the deterministic critical-shell falsification certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

import critical_shell_search as css


def _fraction(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def _envelope(audit: css.EnvelopeAudit) -> dict[str, Any]:
    return {
        "constant": _fraction(audit.constant),
        "compatible": audit.compatible,
        "rows": [
            {
                "j": row.j,
                "mark_count": row.mark_count,
                "modulus": row.modulus,
                "required_log": _fraction(row.required_log),
                "log_lower": _fraction(row.log_lower),
                "log_upper": _fraction(row.log_upper),
                "certified": row.certified,
            }
            for row in audit.rows
        ],
    }


def _decomposition(result: css.ShellDecomposition) -> dict[str, Any]:
    return {
        "j0": result.j0,
        "horizon": result.horizon,
        "level_energies": [_fraction(value) for value in result.level_energies],
        "functional": _fraction(result.functional),
        "shells": [
            {
                "shell": shell.shell,
                "net": _fraction(shell.net),
                "diagonal": _fraction(shell.diagonal),
                "off_diagonal": _fraction(shell.off_diagonal),
            }
            for shell in result.shells
        ],
    }


def _audit(points: tuple[int, ...], j0: int, horizon: int) -> dict[str, Any]:
    results = css.audit_candidates(points, j0=j0, horizon=horizon)
    return {
        name: (
            list(result.first_failure) if result.first_failure is not None else None
        )
        for name, result in results.items()
    }


def _witness(
    points: tuple[int, ...],
    *,
    j0: int,
    horizon: int,
    constant: Fraction,
    failure: tuple[int, int] | None,
) -> dict[str, Any]:
    return {
        "ruler": list(points),
        "diameter": points[-1] - points[0],
        "failure": list(failure) if failure is not None else None,
        "envelope": _envelope(
            css.critical_envelope_audit(
                points, j0=j0, horizon=horizon, constant=constant
            )
        ),
        "candidate_audit": _audit(points, j0, horizon),
        "decomposition": _decomposition(
            css.birth_shell_decomposition(points, j0=j0, horizon=horizon)
        ),
    }


def _first_failure_search(
    rulers: tuple[tuple[int, ...], ...],
    *,
    j0: int,
    horizon: int,
    constant: Fraction,
    first: dict[str, dict[str, Any] | None],
    counts: dict[str, int],
) -> int:
    compatible_count = 0
    for ruler in rulers:
        envelope = css.critical_envelope_audit(
            ruler, j0=j0, horizon=horizon, constant=constant
        )
        if not envelope.compatible:
            continue
        compatible_count += 1
        audit = css.audit_candidates(ruler, j0=j0, horizon=horizon)
        for name, result in audit.items():
            if result.first_failure is None:
                continue
            counts[name] += 1
            if first[name] is None:
                first[name] = _witness(
                    ruler,
                    j0=j0,
                    horizon=horizon,
                    constant=constant,
                    failure=result.first_failure,
                )
    return compatible_count


def _rulers_hash(rulers: tuple[tuple[int, ...], ...]) -> str:
    raw = json.dumps(rulers, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def _random_section(
    *,
    mark_count: int,
    attempts: int,
    scan_limit: int,
    choice_window: int,
    seed: int,
    retain: int,
    oracle: dict[str, int],
) -> dict[str, Any]:
    generated = css.random_dense_greedy_rulers(
        mark_count=mark_count,
        attempts=attempts,
        scan_limit=scan_limit,
        choice_window=choice_window,
        seed=seed,
    )
    horizon = mark_count.bit_length() - 1
    compatible = tuple(
        ruler
        for ruler in generated.rulers
        if css.critical_envelope_audit(
            ruler, j0=1, horizon=horizon, constant=Fraction(2)
        ).compatible
    )
    retained = compatible[:retain]
    witnesses: list[dict[str, Any]] = []
    failure_counts = {
        name: 0 for name in ("H1", "H2", "H3", "H4", "H5", "H6")
    }
    for ruler in retained:
        main = css.birth_shell_decomposition(ruler, j0=1, horizon=horizon)
        literal_energies = tuple(
            css._literal_level_energy(ruler, j)  # independent load oracle
            for j in range(1, horizon + 1)
        )
        oracle["level_energy_checks"] += len(literal_energies)
        if literal_energies != main.level_energies:
            oracle["mismatch_count"] += 1
        audit = css.audit_candidates(ruler, j0=1, horizon=horizon)
        for name, result in audit.items():
            if result.first_failure is not None:
                failure_counts[name] += 1
        witnesses.append(
            {
                "ruler": list(ruler),
                "diameter": ruler[-1],
                "envelope": _envelope(
                    css.critical_envelope_audit(
                        ruler,
                        j0=1,
                        horizon=horizon,
                        constant=Fraction(2),
                    )
                ),
                "candidate_audit": {
                    name: (
                        list(result.first_failure)
                        if result.first_failure is not None
                        else None
                    )
                    for name, result in audit.items()
                },
                "decomposition": _decomposition(main),
            }
        )
    return {
        "mark_count": mark_count,
        "attempts": attempts,
        "scan_limit": scan_limit,
        "choice_window": choice_window,
        "seed": seed,
        "construction_failures": generated.failure_count,
        "unique_rulers": len(generated.rulers),
        "generated_rulers_sha256": _rulers_hash(generated.rulers),
        "compatible_with_C_2": len(compatible),
        "retained_witness_count": len(retained),
        "retained_failure_counts": failure_counts,
        "retained_witnesses": witnesses,
    }


def build_certificate(arguments: argparse.Namespace) -> dict[str, Any]:
    oracle = {
        "shell_decomposition_checks": 0,
        "level_energy_checks": 0,
        "mismatch_count": 0,
    }

    four_first = {
        name: None for name in ("H1", "H2", "H3", "H4", "H5", "H6")
    }
    four_counts = {name: 0 for name in four_first}
    half_first = {name: None for name in four_first}
    half_counts = {name: 0 for name in four_first}
    four_totals = {"candidate_count": 0, "node_count": 0, "golomb_rulers": 0}
    four_compatible_one = 0
    four_compatible_half = 0
    for diameter in range(6, arguments.four_max_diameter + 1):
        enumeration = css.exhaustive_rulers(mark_count=4, diameter=diameter)
        four_totals["candidate_count"] += enumeration.candidate_count
        four_totals["node_count"] += enumeration.node_count
        four_totals["golomb_rulers"] += len(enumeration.rulers)
        for ruler in enumeration.rulers:
            main = css.birth_shell_decomposition(ruler, j0=1, horizon=2)
            literal = css.oracle_birth_shell_decomposition(ruler, j0=1, horizon=2)
            oracle["shell_decomposition_checks"] += 1
            if main != literal:
                oracle["mismatch_count"] += 1
        four_compatible_one += _first_failure_search(
            enumeration.rulers,
            j0=1,
            horizon=2,
            constant=Fraction(1),
            first=four_first,
            counts=four_counts,
        )
        four_compatible_half += _first_failure_search(
            enumeration.rulers,
            j0=1,
            horizon=2,
            constant=Fraction(1, 2),
            first=half_first,
            counts=half_counts,
        )

    eight_first = {name: None for name in four_first}
    eight_counts = {name: 0 for name in four_first}
    eight_rows: list[dict[str, Any]] = []
    eight_totals = {"candidate_count": 0, "node_count": 0, "golomb_rulers": 0}
    eight_compatible = 0
    for diameter in range(
        arguments.eight_min_diameter, arguments.eight_max_diameter + 1
    ):
        enumeration = css.exhaustive_rulers(mark_count=8, diameter=diameter)
        local_counts = {name: 0 for name in four_first}
        local_first = {name: None for name in four_first}
        compatible_count = _first_failure_search(
            enumeration.rulers,
            j0=1,
            horizon=3,
            constant=Fraction(1),
            first=local_first,
            counts=local_counts,
        )
        for name in eight_first:
            eight_counts[name] += local_counts[name]
            if eight_first[name] is None and local_first[name] is not None:
                eight_first[name] = local_first[name]
        eight_compatible += compatible_count
        eight_totals["candidate_count"] += enumeration.candidate_count
        eight_totals["node_count"] += enumeration.node_count
        eight_totals["golomb_rulers"] += len(enumeration.rulers)

        compatible_rulers = tuple(
            ruler
            for ruler in enumeration.rulers
            if css.critical_envelope_audit(
                ruler, j0=1, horizon=3, constant=Fraction(1)
            ).compatible
        )
        oracle_samples = compatible_rulers[:1] + compatible_rulers[-1:]
        for ruler in dict.fromkeys(oracle_samples):
            main = css.birth_shell_decomposition(ruler, j0=1, horizon=3)
            literal = css.oracle_birth_shell_decomposition(ruler, j0=1, horizon=3)
            oracle["shell_decomposition_checks"] += 1
            if main != literal:
                oracle["mismatch_count"] += 1
        eight_rows.append(
            {
                "diameter": diameter,
                "candidate_count": enumeration.candidate_count,
                "node_count": enumeration.node_count,
                "golomb_rulers": len(enumeration.rulers),
                "compatible_with_C_1": compatible_count,
                "failure_counts": local_counts,
            }
        )

    random_sixteen = _random_section(
        mark_count=16,
        attempts=arguments.random16_attempts,
        scan_limit=400,
        choice_window=4,
        seed=1216,
        retain=arguments.random_retain,
        oracle=oracle,
    )
    random_thirty_two = _random_section(
        mark_count=32,
        attempts=arguments.random32_attempts,
        scan_limit=4000,
        choice_window=4,
        seed=1223,
        retain=arguments.random_retain,
        oracle=oracle,
    )

    payload: dict[str, Any] = {
        "schema": "erdos1191-critical-shell-certificate-v1",
        "date": "2026-08-28",
        "scope_warning": (
            "Finite falsification only. Passing ranges do not imply an asymptotic theorem."
        ),
        "configuration": {
            "four_max_diameter": arguments.four_max_diameter,
            "eight_min_diameter": arguments.eight_min_diameter,
            "eight_max_diameter": arguments.eight_max_diameter,
            "random16_attempts": arguments.random16_attempts,
            "random32_attempts": arguments.random32_attempts,
            "random_retain": arguments.random_retain,
        },
        "exhaustive_four": {
            **four_totals,
            "compatible_with_C_1": four_compatible_one,
            "failure_counts_C_1": four_counts,
            "first_failures": four_first,
            "compatible_with_C_1_over_2": four_compatible_half,
            "failure_counts_C_1_over_2": half_counts,
            "first_failures_C_1_over_2": half_first,
        },
        "exhaustive_eight": {
            **eight_totals,
            "compatible_with_C_1": eight_compatible,
            "failure_counts": eight_counts,
            "first_failures": eight_first,
            "per_diameter": eight_rows,
        },
        "random_dense": {
            "sixteen_marks": random_sixteen,
            "thirty_two_marks": random_thirty_two,
        },
        "oracle": oracle,
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()
    payload["certificate_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--four-max-diameter", type=int, default=40)
    parser.add_argument("--eight-min-diameter", type=int, default=34)
    parser.add_argument("--eight-max-diameter", type=int, default=42)
    parser.add_argument("--random16-attempts", type=int, default=40)
    parser.add_argument("--random32-attempts", type=int, default=10)
    parser.add_argument("--random-retain", type=int, default=3)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name(
            "critical_shell_certificate_2026-08-28.json"
        ),
    )
    return parser


def main() -> int:
    arguments = _parser().parse_args()
    if arguments.four_max_diameter < 7:
        raise SystemExit("four-max-diameter must be at least 7")
    if arguments.eight_min_diameter > arguments.eight_max_diameter:
        raise SystemExit("eight diameter range is empty")
    if arguments.random_retain < 1:
        raise SystemExit("random-retain must be positive")
    payload = build_certificate(arguments)
    arguments.output.write_text(
        json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    if payload["oracle"]["mismatch_count"]:
        raise SystemExit("oracle mismatch")
    print(
        "CRITICAL SHELL CERTIFICATE PASSED",
        f"four_rulers={payload['exhaustive_four']['golomb_rulers']}",
        f"eight_rulers={payload['exhaustive_eight']['golomb_rulers']}",
        f"oracle_checks={payload['oracle']['shell_decomposition_checks'] + payload['oracle']['level_energy_checks']}",
        f"sha256={payload['certificate_sha256']}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

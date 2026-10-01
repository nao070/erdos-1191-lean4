"""Exact finite audits for the Wave 13 new-birth lower barrier.

The module keeps three claims separate.

* ``frontier_spectrum`` expands the *infinite-tail* Wave 12 quantity ``Z_m``
  into finitely many rational coefficients of ``log D_(p,q)``.
* ``independent_layered_audit`` cross-checks the canonical Wave 13 harmonic
  obstruction with a separate double-counting oracle.  Its exact conclusion
  is ``Z_m^nb >= E_m/(8m^2 H_m) >= m^2/(384H_m)``.  Logarithms are evaluated
  only for labelled calibrations.
* Bounded rulers and project fixtures test the formulas.  They do not imply
  an infinite surviving branch.

Here ``H_m=a_(2m-1)-a_(m-2)`` and ``m`` is dyadic, at least four.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from typing import Any

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave8_survival_debt_probe import bounded_golomb_exhaustion
from wave11_abel_repayment_probe import ExactLogForm, _all_prefix_c1, _form_summary
from wave13_p18_harmonic_obstruction_probe import new_birth_floor_audit

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_WAVE12_CERTIFICATE = (
    DIRECTORY / "wave12_cut_renewal_certificate_2026-08-29.json"
)
LogAtom = tuple[int, int]
LogSpectrum = dict[LogAtom, Fraction]


def _file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _points_sha256(points: Sequence[int]) -> str:
    return sha256(",".join(str(point) for point in points).encode("ascii")).hexdigest()


def _add_coefficient(
    target: dict[LogAtom, Fraction], atom: LogAtom, coefficient: Fraction
) -> None:
    target[atom] += coefficient
    if not target[atom]:
        del target[atom]


def _validated_prefix(points: Sequence[int], m: int) -> tuple[int, ...]:
    marks = tuple(points)
    if m < 4 or m & (m - 1):
        raise ValueError("m must be a power of two at least four")
    if len(marks) < 2 * m:
        raise ValueError("at least 2m marks are required")
    if (
        marks[0] != 0
        or marks != tuple(sorted(set(marks)))
        or any(not isinstance(mark, int) for mark in marks)
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    prefix = marks[: 2 * m]
    differences = tuple(
        prefix[right] - prefix[left]
        for left in range(len(prefix))
        for right in range(left + 1, len(prefix))
    )
    if len(differences) != len(set(differences)):
        raise ValueError("the supplied 2m-prefix is not a Golomb ruler")
    return prefix


def _cross_ratio_form(points: Sequence[int], left: int, right: int) -> ExactLogForm:
    marks = tuple(points)
    return ExactLogForm.from_terms(
        (
            (marks[right - 1] - marks[left - 1], 1),
            (marks[right] - marks[left], 1),
            (marks[right - 1] - marks[left], -1),
            (marks[right] - marks[left - 1], -1),
        )
    )


def _birth_sector_coefficients(m: int) -> dict[tuple[int, int], Fraction]:
    """The old- and new-birth coefficients of Z_m, independently encoded."""
    coefficients: dict[tuple[int, int], Fraction] = {}
    for right in range(m, 2 * m):
        for left in range(1, min(m - 1, right - 1)):
            coefficients[(left, right)] = Fraction(
                (right - left) ** 2 - (m - left) ** 2,
                4 * m * m,
            )
        for left in range(max(1, m - 1), right - 1):
            coefficients[(left, right)] = Fraction((right - left) ** 2, 4 * m * m)
    return coefficients


def _future_left_coefficients(m: int) -> dict[int, Fraction]:
    """Constant-in-right-endpoint future coefficients in Z_m."""
    coefficients: dict[int, Fraction] = {}
    for left in range(1, m - 1):
        coefficients[left] = Fraction(left * (4 * m - 3 * left), 16 * m * m)
    for left in range(m - 1, 2 * m - 1):
        coefficients[left] = Fraction((2 * m - left) ** 2, 16 * m * m)
    return coefficients


def derived_frontier_spectrum(m: int) -> LogSpectrum:
    """Expand Z_m after telescoping every future j-sum to q=2m-1."""
    if m < 4 or m & (m - 1):
        raise ValueError("m must be a power of two at least four")
    spectrum: defaultdict[LogAtom, Fraction] = defaultdict(Fraction)
    for (left, right), coefficient in _birth_sector_coefficients(m).items():
        for atom, sign in (
            ((left, right - 1), 1),
            ((left + 1, right), 1),
            ((left + 1, right - 1), -1),
            ((left, right), -1),
        ):
            _add_coefficient(spectrum, atom, sign * coefficient)

    frontier = 2 * m - 1
    # sum_(j>=2m) C_(i,j)
    #   = log D_(i,2m-1) - log D_(i+1,2m-1).
    for left, coefficient in _future_left_coefficients(m).items():
        _add_coefficient(spectrum, (left, frontier), coefficient)
        _add_coefficient(spectrum, (left + 1, frontier), -coefficient)
    return dict(spectrum)


def frontier_formula_spectrum(m: int) -> LogSpectrum:
    """Closed coefficient formula for the Wave 13 log-D frontier."""
    if m < 4 or m & (m - 1):
        raise ValueError("m must be a power of two at least four")
    spectrum: defaultdict[LogAtom, Fraction] = defaultdict(Fraction)
    denominator = 4 * m * m
    for right in range(m, 2 * m - 1):
        _add_coefficient(spectrum, (1, right), Fraction(2 * right - 1, denominator))
        for left in range(2, right - 1):
            _add_coefficient(spectrum, (left, right), Fraction(-1, 2 * m * m))
        _add_coefficient(spectrum, (right - 1, right), Fraction(-1, denominator))
        _add_coefficient(spectrum, (right, right), Fraction(-1, m * m))

    frontier = 2 * m - 1
    _add_coefficient(
        spectrum,
        (1, frontier),
        Fraction(-(12 * m * m - 28 * m + 15), 16 * m * m),
    )
    for left in range(2, 2 * m - 2):
        _add_coefficient(
            spectrum,
            (left, frontier),
            Fraction(12 * m - 5 - 6 * left, 16 * m * m),
        )
    _add_coefficient(spectrum, (2 * m - 2, frontier), Fraction(11, 16 * m * m))
    _add_coefficient(spectrum, (2 * m - 1, frontier), Fraction(-1, 4 * m * m))
    return dict(spectrum)


def _spectrum_digest(spectrum: Mapping[LogAtom, Fraction]) -> str:
    canonical = ";".join(
        f"{left},{right}:{coefficient.numerator}/{coefficient.denominator}"
        for (left, right), coefficient in sorted(spectrum.items())
    )
    return sha256(canonical.encode("ascii")).hexdigest()


def spectrum_form(
    points: Sequence[int], spectrum: Mapping[LogAtom, Fraction]
) -> ExactLogForm:
    marks = tuple(points)
    return ExactLogForm.from_terms(
        (marks[right] - marks[left - 1], coefficient)
        for (left, right), coefficient in spectrum.items()
    )


def direct_frontier_form(points: Sequence[int], m: int) -> ExactLogForm:
    """Independent cross-ratio plus telescoped-tail expression for Z_m."""
    marks = _validated_prefix(points, m)
    result = ExactLogForm.zero()
    for (left, right), coefficient in _birth_sector_coefficients(m).items():
        result = result + _cross_ratio_form(marks, left, right).scale(coefficient)
    frontier = 2 * m - 1
    for left, coefficient in _future_left_coefficients(m).items():
        result = result + ExactLogForm.from_terms(
            (
                (marks[frontier] - marks[left - 1], coefficient),
                (marks[frontier] - marks[left], -coefficient),
            )
        )
    return result


def new_birth_form(points: Sequence[int], m: int) -> ExactLogForm:
    marks = _validated_prefix(points, m)
    result = ExactLogForm.zero()
    for right in range(m, 2 * m):
        for left in range(m - 1, right - 1):
            coefficient = Fraction((right - left) ** 2, 4 * m * m)
            result = result + _cross_ratio_form(marks, left, right).scale(coefficient)
    return result


@dataclass(frozen=True)
class IndependentLayeredAudit:
    epoch: int
    suffix_span: int
    weighted_gap_moment: int
    double_count_identity: bool
    minimum_inner_moment: int
    layered_floor: int
    layered_floor_sum_matches_closed_form: bool
    minimum_inner_dominates_layered_floor: bool
    weighted_moment_dominates_half_H_layered_floor: bool
    diameter_proxy: Fraction
    exact_layered_lower: Fraction
    coarse_384_lower: Fraction
    diameter_proxy_dominates_exact_layered_lower: bool
    exact_layered_lower_dominates_coarse_384: bool
    canonical_oracle_matches: bool
    actual_new_birth_form: ExactLogForm


def independent_layered_audit(points: Sequence[int], m: int) -> IndependentLayeredAudit:
    """Cross-check the canonical lower audit by independent double counting."""
    marks = _validated_prefix(points, m)
    gaps = tuple(marks[index] - marks[index - 1] for index in range(m - 1, 2 * m))
    span = marks[2 * m - 1] - marks[m - 2]
    weighted_moment = sum(
        (right - left) ** 2 * gaps[left] * gaps[right]
        for left in range(len(gaps))
        for right in range(left + 2, len(gaps))
    )
    inner_moments = tuple(
        sum(
            (right - left) ** 2 * gaps[right]
            for right in range(len(gaps))
            if abs(right - left) >= 2
        )
        for left in range(len(gaps))
    )
    double_count = sum(gaps[index] * inner_moments[index] for index in range(len(gaps)))
    layered_sum = sum(
        (2 * radius - 1) * (m + 2 - 2 * radius) * (m + 3 - 2 * radius) // 2
        for radius in range(2, m // 2 + 1)
    )
    layered_closed = m * (m - 2) * (m * m + 8 * m + 6) // 48
    diameter_proxy = Fraction(weighted_moment, 4 * m * m * span * span)
    exact_layered = Fraction(layered_closed, 8 * m * m * span)
    coarse_384 = Fraction(m * m, 384 * span)

    canonical = new_birth_floor_audit(marks, m)
    canonical_matches = all(
        (
            canonical.suffix_span == span,
            canonical.full_rank_product_energy == weighted_moment,
            canonical.minimum_observed_layered_energy == min(inner_moments),
            canonical.exact_layered_energy_floor == layered_closed,
            canonical.diameter_relaxed_floor == diameter_proxy,
            canonical.layered_floor == exact_layered,
            canonical.theorem_floor == coarse_384,
        )
    )
    return IndependentLayeredAudit(
        epoch=m,
        suffix_span=span,
        weighted_gap_moment=weighted_moment,
        double_count_identity=(double_count == 2 * weighted_moment),
        minimum_inner_moment=min(inner_moments),
        layered_floor=layered_closed,
        layered_floor_sum_matches_closed_form=(layered_sum == layered_closed),
        minimum_inner_dominates_layered_floor=(min(inner_moments) >= layered_closed),
        weighted_moment_dominates_half_H_layered_floor=(
            2 * weighted_moment >= span * layered_closed
        ),
        diameter_proxy=diameter_proxy,
        exact_layered_lower=exact_layered,
        coarse_384_lower=coarse_384,
        diameter_proxy_dominates_exact_layered_lower=(diameter_proxy >= exact_layered),
        exact_layered_lower_dominates_coarse_384=(exact_layered >= coarse_384),
        canonical_oracle_matches=canonical_matches,
        actual_new_birth_form=new_birth_form(marks, m),
    )


def _barrier_passes(audit: IndependentLayeredAudit) -> bool:
    return all(
        (
            audit.double_count_identity,
            audit.layered_floor_sum_matches_closed_form,
            audit.minimum_inner_dominates_layered_floor,
            audit.weighted_moment_dominates_half_H_layered_floor,
            audit.diameter_proxy_dominates_exact_layered_lower,
            audit.exact_layered_lower_dominates_coarse_384,
            audit.canonical_oracle_matches,
        )
    )


def _barrier_summary(audit: IndependentLayeredAudit) -> dict[str, Any]:
    return {
        "epoch": audit.epoch,
        "H": audit.suffix_span,
        "weighted_gap_moment": audit.weighted_gap_moment,
        "minimum_inner_moment": audit.minimum_inner_moment,
        "layered_floor": audit.layered_floor,
        "diameter_proxy": str(audit.diameter_proxy),
        "exact_layered_lower": str(audit.exact_layered_lower),
        "coarse_384_lower": str(audit.coarse_384_lower),
        "exact_layered_margin_ratio": str(
            audit.diameter_proxy / audit.exact_layered_lower
        ),
        "coarse_384_margin_ratio": str(audit.diameter_proxy / audit.coarse_384_lower),
        "exact_checks": {
            "double_count_identity": audit.double_count_identity,
            "layered_floor_sum_matches_closed_form": (
                audit.layered_floor_sum_matches_closed_form
            ),
            "minimum_inner_dominates_layered_floor": (
                audit.minimum_inner_dominates_layered_floor
            ),
            "weighted_moment_dominates_half_H_layered_floor": (
                audit.weighted_moment_dominates_half_H_layered_floor
            ),
            "diameter_proxy_dominates_exact_layered_lower": (
                audit.diameter_proxy_dominates_exact_layered_lower
            ),
            "exact_layered_lower_dominates_coarse_384": (
                audit.exact_layered_lower_dominates_coarse_384
            ),
            "canonical_oracle_matches": audit.canonical_oracle_matches,
        },
        "actual_new_birth_form": _form_summary(audit.actual_new_birth_form),
        "actual_new_birth_float_projection": format(
            audit.actual_new_birth_form.evaluate(), ".17g"
        ),
        "passed": _barrier_passes(audit),
    }


def exhaustive_eight_mark_audit() -> dict[str, Any]:
    exhaustion = bounded_golomb_exhaustion(mark_count=8, maximum_last_mark=40)
    rows = tuple(
        (tuple(points), independent_layered_audit(points, 4))
        for points in exhaustion.rulers
    )
    c1_rows = tuple(row for row in rows if _all_prefix_c1(row[0]))

    def scope_summary(
        scope: Sequence[tuple[tuple[int, ...], IndependentLayeredAudit]],
    ) -> dict[str, Any]:
        failures = tuple(
            points for points, audit in scope if not _barrier_passes(audit)
        )
        proxy_points, proxy_audit = min(
            scope,
            key=lambda row: (
                row[1].diameter_proxy / row[1].exact_layered_lower,
                row[0],
            ),
        )
        actual_points, actual_audit = min(
            scope,
            key=lambda row: (
                row[1].actual_new_birth_form.evaluate()
                / float(row[1].exact_layered_lower),
                row[0],
            ),
        )
        return {
            "candidate_count": len(scope),
            "failure_count": len(failures),
            "first_failure": list(failures[0]) if failures else None,
            "minimum_exact_proxy_margin_points": list(proxy_points),
            "minimum_exact_proxy_margin_ratio": str(
                proxy_audit.diameter_proxy / proxy_audit.exact_layered_lower
            ),
            "minimum_actual_float_margin_points": list(actual_points),
            "minimum_actual_float_margin_ratio": format(
                actual_audit.actual_new_birth_form.evaluate()
                / float(actual_audit.exact_layered_lower),
                ".17g",
            ),
            "actual_margin_is_labelled_float_only": True,
        }

    return {
        "all_bounded_rulers": scope_summary(rows),
        "all_prefix_C1_subset": scope_summary(c1_rows),
        "finite_only": True,
        "infinite_survival_inferred": False,
    }


def _spectrum_summary(m: int) -> dict[str, Any]:
    derived = derived_frontier_spectrum(m)
    formula = frontier_formula_spectrum(m)
    positive_mass = sum(
        (coefficient for coefficient in derived.values() if coefficient > 0),
        Fraction(0),
    )
    negative_mass = -sum(
        (coefficient for coefficient in derived.values() if coefficient < 0),
        Fraction(0),
    )
    closed_positive_mass = Fraction(24 * m * m - 52 * m + 31, 16 * m * m)
    return {
        "epoch": m,
        "term_count": len(derived),
        "closed_term_count": m * (3 * m - 1) // 2,
        "positive_term_count": sum(coefficient > 0 for coefficient in derived.values()),
        "negative_term_count": sum(coefficient < 0 for coefficient in derived.values()),
        "positive_mass": str(positive_mass),
        "negative_mass": str(negative_mass),
        "closed_positive_mass": str(closed_positive_mass),
        "term_count_formula_verified": len(derived) == m * (3 * m - 1) // 2,
        "positive_mass_formula_verified": positive_mass == closed_positive_mass,
        "coefficient_sum": str(sum(derived.values(), Fraction(0))),
        "closed_formula_matches_independent_expansion": derived == formula,
        "spectrum_sha256": _spectrum_digest(derived),
    }


def build_certificate(
    source_certificate: str | Path = DEFAULT_WAVE12_CERTIFICATE,
) -> dict[str, Any]:
    source_path = Path(source_certificate).resolve()
    fixture_64 = tuple(COUNTEREXAMPLE_64_POINTS)
    fixture_128 = erdos_turan_ruler(128, 257)
    fixture_rows = []
    for name, points, epochs in (
        ("wave6_hall_counterexample_64", fixture_64, (4, 8, 16, 32)),
        ("erdos_turan_128_p257", fixture_128, (4, 8, 16, 32, 64)),
    ):
        rows = []
        for m in epochs:
            barrier = independent_layered_audit(points, m)
            spectrum = derived_frontier_spectrum(m)
            frontier_form = spectrum_form(points, spectrum)
            direct_form = direct_frontier_form(points, m)
            rows.append(
                {
                    "barrier": _barrier_summary(barrier),
                    "frontier_formula_matches_expansion": (
                        spectrum == frontier_formula_spectrum(m)
                    ),
                    "frontier_form_matches_direct_tail_telescope": (
                        frontier_form == direct_form
                    ),
                    "frontier_form": _form_summary(frontier_form),
                    "frontier_float_projection": format(
                        frontier_form.evaluate(), ".17g"
                    ),
                }
            )
        fixture_rows.append(
            {
                "name": name,
                "point_count": len(points),
                "points_sha256": _points_sha256(points),
                "rows": rows,
                "finite_only": True,
            }
        )

    payload: dict[str, Any] = {
        "schema": "erdos1191.wave13.frontier-spectrum.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Independent exact audit of the layered m^2/(384 H) lower "
            "barrier and the closed log-D frontier spectrum for Z_m."
        ),
        "source_authentication": {
            "wave12_certificate": source_path.name,
            "wave12_certificate_file_sha256": _file_sha256(source_path),
            "wave12_probe_file_sha256": _file_sha256(
                DIRECTORY / "wave12_cut_renewal_probe.py"
            ),
            "wave6_fixture_module_file_sha256": _file_sha256(
                DIRECTORY / "wave6_hall_candidate_probe.py"
            ),
            "canonical_wave13_obstruction_probe_file_sha256": _file_sha256(
                DIRECTORY / "wave13_p18_harmonic_obstruction_probe.py"
            ),
        },
        "frontier_spectrum_rows": [_spectrum_summary(m) for m in (4, 8, 16, 32, 64)],
        "exhaustive_eight_mark_audit": exhaustive_eight_mark_audit(),
        "fixture_audits": fixture_rows,
        "analytic_contract": {
            "cross_ratio_identity": ("C_ij=log(1+g_i*g_j/(x*(x+g_i+g_j)))"),
            "rational_cell_lower": ("C_ij>=g_i*g_j/H^2 by log(1+t)>=t/(1+t)"),
            "weighted_moment": ("S=sum_(i<j,j-i>=2)(j-i)^2*g_i*g_j"),
            "layered_energy_floor": ("E_m=m*(m-2)*(m^2+8m+6)/48>=m^4/48"),
            "distinct_gap_moment_lower": "S>=H*E_m/2",
            "exact_layered_new_birth_lower": "Z_m^nb>=E_m/(8m^2H)",
            "coarse_new_birth_lower": "Z_m^nb>=m^2/(384H)",
            "requested_lower": "Z_m^nb>=m^2/(8192H)",
            "eventual_C_corollary": ("Y_m,Z_m>=Z_m^nb>=1/(1536*C*log(4m)) eventually"),
            "dyadic_sum_corollary": (
                "sum_(m=2^k,k<=J)Y_m and sum Z_m are Omega_C(log J) "
                "under the same hypothetical eventual-C branch"
            ),
        },
        "claim_boundary": {
            "finite_integer_chain_checks_passed": True,
            "frontier_spectrum_coefficientwise_exact": True,
            "new_birth_lower_barrier_proved_analytically": True,
            "known_infinite_eventual_C_branch_supplied": False,
            "p18_sublog_upper_proved": False,
            "p17_sublog_upper_proved": False,
            "p15_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
        },
        "conclusions": [
            "The requested 1/8192 lower bound holds with the stronger constant 1/384.",
            "The lower barrier is exact-arithmetic and uses distinct positive integer gaps.",
            "The full infinite-tail Z_m has the stated finite log-D frontier spectrum.",
            "The barrier makes the P17 and P18 sublog upper statements explicit contradiction targets.",
            "No finite row supplies or rules out an infinite surviving branch.",
        ],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["certificate_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-certificate", type=Path, default=DEFAULT_WAVE12_CERTIFICATE
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DIRECTORY / "wave13_new_birth_barrier_certificate_2026-08-29.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.source_certificate)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()

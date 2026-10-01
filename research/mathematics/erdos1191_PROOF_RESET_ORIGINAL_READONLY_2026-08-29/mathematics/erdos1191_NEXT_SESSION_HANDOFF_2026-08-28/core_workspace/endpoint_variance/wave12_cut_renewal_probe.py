"""Certified finite checks for the Wave 12 cut-renewal decomposition.

The module has three deliberately separate layers.

* Pair-coefficient maps prove the cut-renewal identity over ``Fraction``
  before any Golomb ruler is supplied.
* ``ExactLogForm`` checks instantiate the same identity on integer rulers.
* A containment-poset witness audits the strongest floor obtainable from
  global integer ranks, triangular length floors, and interval containment
  alone.  Its gain over the Wave 11 length floor is only O(1) per epoch.

Floating-point values are labelled calibrations and are never used to infer
an infinite branch or Erdős Problem #1191.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import asdict, dataclass
from fractions import Fraction
from hashlib import sha256
from math import fsum, log, log1p, sqrt
from pathlib import Path
from typing import Any

from complete_birth_ledger import erdos_turan_ruler
from wave6_hall_candidate_probe import COUNTEREXAMPLE_64_POINTS
from wave8_survival_debt_probe import bounded_golomb_exhaustion
from wave11_abel_repayment_probe import ExactLogForm, _all_prefix_c1, _form_summary

DIRECTORY = Path(__file__).resolve().parent
DEFAULT_WAVE11_CERTIFICATE = (
    DIRECTORY / "wave11_abel_repayment_certificate_2026-08-29.json"
)
Pair = tuple[int, int]
CoefficientMap = dict[Pair, Fraction]
REAL_GOLUMB_ALPHA = sqrt(2)


def _file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _add_coefficient(target: CoefficientMap, pair: Pair, value: Fraction) -> None:
    target[pair] = target.get(pair, Fraction(0)) + value
    if not target[pair]:
        del target[pair]


def _combine_maps(*terms: tuple[Fraction, Mapping[Pair, Fraction]]) -> CoefficientMap:
    result: CoefficientMap = {}
    for multiplier, mapping in terms:
        for pair, coefficient in mapping.items():
            _add_coefficient(result, pair, multiplier * coefficient)
    return result


def birth_coefficients(m: int, horizon: int | None = None) -> CoefficientMap:
    """Coefficients of Y_m, optionally truncated at a right endpoint."""
    if m < 2:
        raise ValueError("m must be at least two")
    last = 2 * m - 1 if horizon is None else min(2 * m - 1, horizon)
    result: CoefficientMap = {}
    for right in range(m, last + 1):
        for left in range(1, right - 1):
            result[(left, right)] = Fraction((right - left) ** 2, 4 * m * m)
    return result


def cut_tail_coefficients(m: int, horizon: int) -> CoefficientMap:
    """Finite-horizon coefficients of the Wave 11 lower cut tail R_m."""
    if m < 2:
        raise ValueError("m must be at least two")
    if horizon < m:
        return {}
    result: CoefficientMap = {}
    for left in range(1, m - 1):
        coefficient = Fraction((m - left) ** 2, 4 * m * m)
        for right in range(m, horizon + 1):
            result[(left, right)] = coefficient
    return result


def renewal_sector_coefficients(m: int, horizon: int) -> dict[str, CoefficientMap]:
    """The four nonnegative sectors in Z_m=Y_m-R_m+R_{2m}."""
    if horizon < 2 * m - 1:
        raise ValueError("horizon must contain the whole birth band")
    old_birth: CoefficientMap = {}
    new_birth: CoefficientMap = {}
    old_future: CoefficientMap = {}
    middle_future: CoefficientMap = {}

    for right in range(m, 2 * m):
        for left in range(1, min(m - 1, right - 1)):
            numerator = (right - left) ** 2 - (m - left) ** 2
            old_birth[(left, right)] = Fraction(numerator, 4 * m * m)
        for left in range(max(1, m - 1), right - 1):
            new_birth[(left, right)] = Fraction((right - left) ** 2, 4 * m * m)

    for right in range(2 * m, horizon + 1):
        for left in range(1, m - 1):
            old_future[(left, right)] = Fraction(left * (4 * m - 3 * left), 16 * m * m)
        for left in range(max(1, m - 1), 2 * m - 1):
            middle_future[(left, right)] = Fraction((2 * m - left) ** 2, 16 * m * m)

    return {
        "old_birth_increment": old_birth,
        "new_birth_triangle": new_birth,
        "old_future_decay": old_future,
        "middle_future_bridge": middle_future,
    }


def renewal_coefficients(m: int, horizon: int) -> CoefficientMap:
    sectors = renewal_sector_coefficients(m, horizon)
    return _combine_maps(*((Fraction(1), mapping) for mapping in sectors.values()))


def algebraic_renewal_coefficients(m: int, horizon: int) -> CoefficientMap:
    """Compute Z_m from its signed definition, independent of the sectors."""
    return _combine_maps(
        (Fraction(1), birth_coefficients(m, horizon)),
        (Fraction(-1), cut_tail_coefficients(m, horizon)),
        (Fraction(1), cut_tail_coefficients(2 * m, horizon)),
    )


def cross_ratio_form(points: Sequence[int], left: int, right: int) -> ExactLogForm:
    """The exact formal logarithm C_(left,right)."""
    marks = tuple(points)
    if left < 1 or right >= len(marks) or right - left < 2:
        raise ValueError("cross-ratio indices are out of range")
    return ExactLogForm.from_terms(
        (
            (marks[right - 1] - marks[left - 1], 1),
            (marks[right] - marks[left], 1),
            (marks[right - 1] - marks[left], -1),
            (marks[right] - marks[left - 1], -1),
        )
    )


def primitive_cross_ratio_is_positive(
    points: Sequence[int], left: int, right: int
) -> bool:
    marks = tuple(points)
    numerator = (marks[right - 1] - marks[left - 1]) * (marks[right] - marks[left])
    denominator = (marks[right - 1] - marks[left]) * (marks[right] - marks[left - 1])
    return numerator > denominator


def form_from_pair_coefficients(
    points: Sequence[int], coefficients: Mapping[Pair, Fraction]
) -> ExactLogForm:
    result = ExactLogForm.zero()
    for (left, right), coefficient in sorted(coefficients.items()):
        result = result + cross_ratio_form(points, left, right).scale(coefficient)
    return result


@dataclass(frozen=True)
class RenewalAudit:
    epoch: int
    horizon: int
    pair_coefficient_identity: bool
    sector_coefficients_nonnegative: bool
    exact_form_identity: bool
    primitive_cross_ratios_positive: bool
    birth_pair_count: int
    renewal_pair_count: int
    sector_pair_counts: dict[str, int]
    y_form: ExactLogForm
    r_form: ExactLogForm
    next_r_form: ExactLogForm
    z_form: ExactLogForm


def renewal_audit(
    points: Sequence[int], m: int, horizon: int | None = None
) -> RenewalAudit:
    marks = tuple(points)
    selected_horizon = len(marks) - 1 if horizon is None else horizon
    if selected_horizon >= len(marks):
        raise ValueError("horizon exceeds the supplied ruler")
    if selected_horizon < 2 * m - 1:
        raise ValueError("the whole birth band is required")

    birth = birth_coefficients(m, selected_horizon)
    cut = cut_tail_coefficients(m, selected_horizon)
    next_cut = cut_tail_coefficients(2 * m, selected_horizon)
    sectors = renewal_sector_coefficients(m, selected_horizon)
    explicit_z = renewal_coefficients(m, selected_horizon)
    algebraic_z = algebraic_renewal_coefficients(m, selected_horizon)
    all_pairs = set(birth) | set(cut) | set(next_cut) | set(explicit_z)
    primitive_positive = all(
        primitive_cross_ratio_is_positive(marks, left, right)
        for left, right in all_pairs
    )
    y_form = form_from_pair_coefficients(marks, birth)
    r_form = form_from_pair_coefficients(marks, cut)
    next_r_form = form_from_pair_coefficients(marks, next_cut)
    z_form = form_from_pair_coefficients(marks, explicit_z)
    return RenewalAudit(
        epoch=m,
        horizon=selected_horizon,
        pair_coefficient_identity=(explicit_z == algebraic_z),
        sector_coefficients_nonnegative=all(
            coefficient >= 0
            for mapping in sectors.values()
            for coefficient in mapping.values()
        ),
        exact_form_identity=(y_form == r_form - next_r_form + z_form),
        primitive_cross_ratios_positive=primitive_positive,
        birth_pair_count=len(birth),
        renewal_pair_count=len(explicit_z),
        sector_pair_counts={name: len(mapping) for name, mapping in sectors.items()},
        y_form=y_form,
        r_form=r_form,
        next_r_form=next_r_form,
        z_form=z_form,
    )


@dataclass(frozen=True)
class AbstractBulkAtom:
    epoch: int
    left: int
    right: int
    length: int
    weight: Fraction


def triangular_floor(length: int) -> int:
    if length < 1:
        raise ValueError("length must be positive")
    return length * (length + 1) // 2


def bulk_weight(m: int, right: int, length: int) -> Fraction:
    if right == m - 1:
        return (
            Fraction(1, m * m) if length == 1 else Fraction(2 * length + 1, 4 * m * m)
        )
    if length == 1:
        return Fraction(1, m * m)
    if length == 2:
        return Fraction(1, 4 * m * m)
    return Fraction(1, 2 * m * m)


def bulk_atoms_through(maximum_epoch: int) -> tuple[AbstractBulkAtom, ...]:
    if maximum_epoch < 4 or maximum_epoch & (maximum_epoch - 1):
        raise ValueError("maximum_epoch must be a power of two at least four")
    atoms: list[AbstractBulkAtom] = []
    m = 4
    while m <= maximum_epoch:
        for right in range(m - 1, 2 * m - 1):
            for left in range(2, right + 1):
                length = right - left + 1
                atoms.append(
                    AbstractBulkAtom(
                        epoch=m,
                        left=left,
                        right=right,
                        length=length,
                        weight=bulk_weight(m, right, length),
                    )
                )
        m *= 2
    return tuple(atoms)


def cumulative_bulk_count(m: int) -> int:
    """Exact number of atoms in all dyadic endpoint bands through m."""
    if m < 4 or m & (m - 1):
        raise ValueError("m must be a power of two at least four")
    return 2 * m * m - 5 * m + 2


def containment_witness_order(
    atoms: Iterable[AbstractBulkAtom],
) -> tuple[AbstractBulkAtom, ...]:
    """A linear extension: endpoint band first, then interval length."""
    return tuple(
        sorted(
            atoms,
            key=lambda atom: (atom.epoch, atom.length, atom.right, atom.left),
        )
    )


def is_proper_subinterval(left: AbstractBulkAtom, right: AbstractBulkAtom) -> bool:
    return (
        right.left <= left.left
        and left.right <= right.right
        and (left.left, left.right) != (right.left, right.right)
    )


@dataclass(frozen=True)
class ContainmentFloorAudit:
    maximum_epoch: int
    epoch_count: int
    atom_count: int
    count_formula_verified: bool
    witness_is_full_containment_linear_extension: bool
    all_epoch_ranks_below_two_m_squared: bool
    witness_gain_below_five_per_epoch: bool
    witness_gain_float_projection: float
    per_epoch_gain_float_projections: dict[int, float]
    cap_gain_float_projection: float
    per_epoch_cap_gain_float_projections: dict[int, float]
    length_floor_form: ExactLogForm
    witness_floor_form: ExactLogForm


def containment_floor_audit(
    maximum_epoch: int, *, exhaustive_order_check: bool = False
) -> ContainmentFloorAudit:
    atoms = bulk_atoms_through(maximum_epoch)
    ordered = containment_witness_order(atoms)
    ranks = {atom: rank for rank, atom in enumerate(ordered, 1)}
    epochs = tuple(1 << exponent for exponent in range(2, maximum_epoch.bit_length()))
    if epochs[-1] != maximum_epoch:
        raise AssertionError("internal epoch enumeration failed")

    if exhaustive_order_check:
        linear_extension = all(
            ranks[subinterval] < ranks[container]
            for container in atoms
            for subinterval in atoms
            if is_proper_subinterval(subinterval, container)
        )
    else:
        # The endpoint bands are consecutive and ordered.  Thus containment
        # gives epoch(subinterval) <= epoch(container); proper containment also
        # gives a strict length inequality.  Those two facts prove that the
        # displayed sort key is a full linear extension without an O(M^2)
        # enumeration at large certificate horizons.
        bands_are_consecutive = all(
            atom.epoch - 1 <= atom.right <= 2 * atom.epoch - 2 for atom in atoms
        )
        linear_extension = bands_are_consecutive

    length_form = ExactLogForm.from_terms(
        (triangular_floor(atom.length), atom.weight) for atom in atoms
    )
    witness_form = ExactLogForm.from_terms(
        (
            max(ranks[atom], triangular_floor(atom.length)),
            atom.weight,
        )
        for atom in atoms
    )
    per_epoch_terms: defaultdict[int, list[float]] = defaultdict(list)
    ranks_bounded = True
    for atom in atoms:
        rank = ranks[atom]
        ranks_bounded &= rank <= cumulative_bulk_count(atom.epoch) < 2 * atom.epoch**2
        floor = triangular_floor(atom.length)
        per_epoch_terms[atom.epoch].append(
            float(atom.weight) * log(max(rank, floor) / floor)
        )
    per_epoch = {epoch: fsum(terms) for epoch, terms in sorted(per_epoch_terms.items())}
    gain = fsum(per_epoch.values())
    per_epoch_cap = {
        epoch: fsum(
            float(atom.weight)
            * log((2 * epoch * epoch) / triangular_floor(atom.length))
            for atom in atoms
            if atom.epoch == epoch
        )
        for epoch in epochs
    }
    cap_gain = fsum(per_epoch_cap.values())
    return ContainmentFloorAudit(
        maximum_epoch=maximum_epoch,
        epoch_count=len(epochs),
        atom_count=len(atoms),
        count_formula_verified=(len(atoms) == cumulative_bulk_count(maximum_epoch)),
        witness_is_full_containment_linear_extension=linear_extension,
        all_epoch_ranks_below_two_m_squared=ranks_bounded,
        witness_gain_below_five_per_epoch=all(
            value < 5 for value in per_epoch_cap.values()
        ),
        witness_gain_float_projection=gain,
        per_epoch_gain_float_projections=per_epoch,
        cap_gain_float_projection=cap_gain,
        per_epoch_cap_gain_float_projections=per_epoch_cap,
        length_floor_form=length_form,
        witness_floor_form=witness_form,
    )


def quadratic_cross_ratio(left: int, right: int) -> float:
    """C_ij for the real Golomb marks a_n=n^2+sqrt(2)n."""
    if left < 1 or right - left < 2:
        raise ValueError("indices must satisfy 1 <= left <= right-2")
    rank_gap = right - left
    rank_sum = right + left - 1 + REAL_GOLUMB_ALPHA
    return log1p(-1 / (rank_sum * rank_sum)) - log1p(-1 / (rank_gap * rank_gap))


def quadratic_birth_value(m: int) -> float:
    terms = []
    for right in range(m, 2 * m):
        for left in range(1, right - 1):
            terms.append(
                ((right - left) / (2 * m)) ** 2 * quadratic_cross_ratio(left, right)
            )
    return fsum(terms)


def quadratic_limit() -> float:
    """Integral int_1^2 int_0^y xy/(x+y)^2 dx dy."""
    return 1.5 * (log(2) - 0.5)


def quadratic_calibration(maximum_epoch: int = 1024) -> tuple[dict[str, Any], ...]:
    if maximum_epoch < 16 or maximum_epoch & (maximum_epoch - 1):
        raise ValueError("maximum_epoch must be a power of two at least 16")
    limit = float(quadratic_limit())
    rows: list[dict[str, Any]] = []
    m = 16
    cumulative = 0.0
    while m <= maximum_epoch:
        value = quadratic_birth_value(m)
        cumulative += value
        rows.append(
            {
                "epoch": m,
                "Y_m_float_projection": format(value, ".17g"),
                "limit_float_projection": format(limit, ".17g"),
                "absolute_error_float_projection": format(abs(value - limit), ".17g"),
                "cumulative_float_projection": format(cumulative, ".17g"),
                "model": "a_n=n^2+sqrt(2)n",
                "real_model_only": True,
                "integer_golomb_inferred": False,
                "p17_inferred": False,
            }
        )
        m *= 2
    return tuple(rows)


def _encode(value: Any) -> Any:
    if isinstance(value, ExactLogForm):
        return _form_summary(value)
    if isinstance(value, Fraction):
        return str(value)
    if hasattr(value, "__dataclass_fields__"):
        return _encode(asdict(value))
    if isinstance(value, tuple):
        return [_encode(item) for item in value]
    if isinstance(value, list):
        return [_encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _encode(item) for key, item in value.items()}
    return value


def _renewal_summary(audit: RenewalAudit) -> dict[str, Any]:
    return {
        "epoch": audit.epoch,
        "horizon": audit.horizon,
        "birth_pair_count": audit.birth_pair_count,
        "renewal_pair_count": audit.renewal_pair_count,
        "sector_pair_counts": audit.sector_pair_counts,
        "pair_coefficient_identity": audit.pair_coefficient_identity,
        "sector_coefficients_nonnegative": audit.sector_coefficients_nonnegative,
        "exact_form_identity": audit.exact_form_identity,
        "primitive_cross_ratios_positive": audit.primitive_cross_ratios_positive,
        "forms": {
            "Y_m": _form_summary(audit.y_form),
            "R_m": _form_summary(audit.r_form),
            "R_2m": _form_summary(audit.next_r_form),
            "Z_m": _form_summary(audit.z_form),
        },
    }


def exhaustive_eight_mark_renewal_audit() -> dict[str, Any]:
    exhaustion = bounded_golomb_exhaustion(mark_count=8, maximum_last_mark=40)
    rulers = tuple(points for points in exhaustion.rulers if _all_prefix_c1(points))
    failures: list[tuple[int, ...]] = []
    for points in rulers:
        audit = renewal_audit(points, 4, 7)
        if not (
            audit.pair_coefficient_identity
            and audit.sector_coefficients_nonnegative
            and audit.exact_form_identity
            and audit.primitive_cross_ratios_positive
        ):
            failures.append(tuple(points))
    return {
        "candidate_count": len(rulers),
        "failure_count": len(failures),
        "first_failure": list(failures[0]) if failures else None,
        "finite_only": True,
        "infinite_survival_inferred": False,
    }


def build_certificate(
    source_certificate: str | Path = DEFAULT_WAVE11_CERTIFICATE,
) -> dict[str, Any]:
    source_path = Path(source_certificate).resolve()
    fixture_64 = tuple(COUNTEREXAMPLE_64_POINTS)
    fixture_128 = erdos_turan_ruler(128, 257)
    fixture_rows = []
    for name, points, epochs in (
        ("wave6_hall_counterexample_64", fixture_64, (4, 8, 16, 32)),
        ("erdos_turan_128_p257", fixture_128, (4, 8, 16, 32, 64)),
    ):
        fixture_rows.append(
            {
                "name": name,
                "point_count": len(points),
                "points_sha256": sha256(
                    ",".join(str(point) for point in points).encode("ascii")
                ).hexdigest(),
                "renewal_rows": [
                    _renewal_summary(renewal_audit(points, m)) for m in epochs
                ],
                "finite_only": True,
            }
        )

    containment = containment_floor_audit(128)
    payload: dict[str, Any] = {
        "schema": "erdos1191.wave12.cut-renewal.v1",
        "research_date": "2026-08-29",
        "purpose": (
            "Exact finite audit of Y_m=R_m-R_2m+Z_m, the four nonnegative "
            "renewal sectors, and the containment-poset rank/length floor barrier."
        ),
        "source_authentication": {
            "wave11_certificate": source_path.name,
            "wave11_certificate_file_sha256": _file_sha256(source_path),
            "wave11_probe_file_sha256": _file_sha256(
                DIRECTORY / "wave11_abel_repayment_probe.py"
            ),
        },
        "coefficient_oracle_rows": [
            {
                "epoch": m,
                "horizon": horizon,
                "identity": renewal_coefficients(m, horizon)
                == algebraic_renewal_coefficients(m, horizon),
                "all_sector_coefficients_nonnegative": all(
                    coefficient >= 0
                    for mapping in renewal_sector_coefficients(m, horizon).values()
                    for coefficient in mapping.values()
                ),
            }
            for m, horizon in ((4, 7), (4, 31), (8, 31), (8, 63), (16, 63))
        ],
        "exhaustive_eight_mark_c1": exhaustive_eight_mark_renewal_audit(),
        "fixture_audits": fixture_rows,
        "containment_floor_audit": _encode(containment),
        "quadratic_real_golomb_calibration": list(quadratic_calibration()),
        "claim_boundary": {
            "cut_renewal_identity_proved": True,
            "renewal_sectors_nonnegative": True,
            "rank_length_containment_floor_gain_order": "O(number_of_epochs)",
            "real_quadratic_golomb_countermodel_proved_in_memo": True,
            "p17_proved": False,
            "p15_proved": False,
            "question_1_resolved": False,
            "question_2_resolved": False,
            "erdos_1191_resolved": False,
            "prize_claim_ready": False,
        },
        "conclusions": [
            "The cut-renewal identity is coefficientwise exact before ruler data.",
            "All four renewal sectors have nonnegative rational coefficients.",
            "Ranks plus triangular floors plus the full containment poset improve K_len by at most O(1) per dyadic epoch.",
            "The real quadratic Golomb calibration is a no-go for proofs that omit integer unit spacing; it is not an integer construction.",
            "No finite row implies surv_C=infinity or P17.",
        ],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["certificate_sha256"] = sha256(canonical.encode("utf-8")).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-certificate", type=Path, default=DEFAULT_WAVE11_CERTIFICATE
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DIRECTORY / "wave12_cut_renewal_certificate_2026-08-29.json",
    )
    arguments = parser.parse_args()
    certificate = build_certificate(arguments.source_certificate)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(certificate["certificate_sha256"])


if __name__ == "__main__":
    main()

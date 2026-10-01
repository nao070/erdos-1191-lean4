"""Exact cross-epoch telescope for the signed Wave 8 Q-pair identity.

For a gap-index pair ``(i,j)``, let ``b`` be its unique dyadic birth epoch,
so ``b <= j < 2b``.  At birth the short signed Q identity contributes a
positive pair term.  At every later epoch it contributes a negative old-pair
term.  This module keeps those terms instead of discarding them.

Two weights must be distinguished.

* With the constant Lyapunov majorant ``H``, every cumulative pair
  coefficient remains between one half and one times its raw birth
  coefficient.  Thus later negative terms cannot provide a decisive
  cancellation.
* With the exact finite-horizon adjoints, the signed coefficient telescopes
  exactly to a positive sum of future ``E``-energies of the same pair.

All arithmetic is exact.  No finite prefix is treated as evidence of an
infinite critical extension.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import pairwise

from gap_measure_dynamics import dyadic_gap_matrix_update, is_positive_semidefinite
from innovation_budget import (
    E_MATRIX,
    LYAPUNOV_MATRIX,
    Matrix2,
    adjoint_transport,
    frobenius_inner,
    matrix_add,
    matrix_scale,
)


def _validated_marks(points: Sequence[int]) -> tuple[int, ...]:
    marks = tuple(points)
    if (
        len(marks) < 2
        or any(not isinstance(mark, int) for mark in marks)
        or marks[0] != 0
        or marks != tuple(sorted(set(marks)))
    ):
        raise ValueError("points must be normalized strictly increasing integers")
    return marks


def _is_power_of_two(value: int) -> bool:
    return value >= 1 and value & (value - 1) == 0


def _validated_horizon(points: Sequence[int]) -> tuple[int, ...]:
    marks = _validated_marks(points)
    if not _is_power_of_two(len(marks)):
        raise ValueError("the terminal mark count must be a power of two")
    return marks


def _gap_weights(marks: tuple[int, ...]) -> tuple[int, ...]:
    return (1, *(marks[index] - marks[index - 1] for index in range(1, len(marks))))


def _modulus(marks: tuple[int, ...], count: int) -> int:
    if not isinstance(count, int) or not 1 <= count <= len(marks):
        raise ValueError("count must index a nonempty prefix")
    return marks[count - 1] + 1


def _state_counts(horizon_count: int, *, initial_count: int = 1) -> tuple[int, ...]:
    if (
        not _is_power_of_two(initial_count)
        or not _is_power_of_two(horizon_count)
        or initial_count > horizon_count
    ):
        raise ValueError("initial and horizon counts must be compatible powers of two")
    rows = [initial_count]
    while rows[-1] < horizon_count:
        rows.append(2 * rows[-1])
    return tuple(rows)


def pair_birth_epoch(right_index: int) -> int:
    """Return the unique dyadic ``b`` with ``b <= right_index < 2b``."""
    if not isinstance(right_index, int) or right_index < 1:
        raise ValueError("right_index must be a positive integer")
    return 1 << (right_index.bit_length() - 1)


def rank_embedding(index: int, count: int) -> tuple[Fraction, Fraction]:
    if (
        not isinstance(index, int)
        or not isinstance(count, int)
        or count < 1
        or not 0 <= index < count
    ):
        raise ValueError("require integer indices with 0 <= index < count")
    u = Fraction(index, count)
    return (u * (1 - u), u)


def pair_kernel(
    matrix: Matrix2,
    left: int,
    right: int,
    *,
    count: int,
) -> Fraction:
    """Return ``<matrix,(z_j-z_i)(z_j-z_i)^T>`` exactly."""
    if not 0 <= left < right < count:
        raise ValueError("require 0 <= left < right < count")
    first = rank_embedding(left, count)
    second = rank_embedding(right, count)
    delta = (second[0] - first[0], second[1] - first[1])
    return (
        matrix[0][0] * delta[0] ** 2
        + (matrix[0][1] + matrix[1][0]) * delta[0] * delta[1]
        + matrix[1][1] * delta[1] ** 2
    )


def _pair_epochs(
    marks: tuple[int, ...], left: int, right: int, horizon_count: int
) -> tuple[int, ...]:
    if not 0 <= left < right < horizon_count <= len(marks):
        raise ValueError("the pair must lie inside the requested horizon")
    birth = pair_birth_epoch(right)
    return _state_counts(horizon_count, initial_count=2 * birth)


@dataclass(frozen=True)
class FixedHPairAudit:
    left: int
    right: int
    birth_epoch: int
    birth_count: int
    horizon_count: int
    state_counts: tuple[int, ...]
    moduli: tuple[int, ...]
    h_product: int
    birth_kernel_coefficient: Fraction
    later_negative_coefficient: Fraction
    net_kernel_coefficient: Fraction
    half_birth_lower_bound: Fraction
    retention_ratio: Fraction
    lyapunov_telescope_value: Fraction
    telescope_weights: tuple[Fraction, ...]


@dataclass(frozen=True)
class ConstantHModulusAudit:
    """The scalar weights behind the constant-``H`` pair telescope."""

    moduli: tuple[int, ...]
    birth_weight: Fraction
    old_subtraction_weights: tuple[Fraction, ...]
    positive_atom_weights: tuple[Fraction, ...]
    half_birth_lower_bound: Fraction
    maximum_future_ratio: Fraction
    ratio_lower_bound: Fraction


def constant_h_modulus_audit(moduli: Sequence[int]) -> ConstantHModulusAudit:
    """Audit half-retention for an arbitrary strictly increasing modulus list.

    For ``M_0<...<M_T``, the old-pair subtraction at time ``t`` has scalar
    coefficient

    ``alpha_t=(M_t-M_(t-1))/(M_(t-1) M_t^2)``.

    After using ``H-B^T H B=E``, every positive atom has weight
    ``w_r=M_0^-2-sum_(t<=r) alpha_t``.  These weights are at least half the
    birth weight.  If every future ratio ``M_(t-1)/M_t`` is at most ``r``,
    they are at least ``1/(1+r)`` of the birth weight.
    """
    masses = tuple(moduli)
    if (
        not masses
        or any(not isinstance(value, int) or value <= 0 for value in masses)
        or any(left >= right for left, right in pairwise(masses))
    ):
        raise ValueError("moduli must be a strictly increasing positive sequence")

    birth_weight = Fraction(1, masses[0] ** 2)
    alphas: list[Fraction] = []
    positive_weights = [birth_weight]
    ratios: list[Fraction] = []
    cumulative = Fraction(0)
    for previous, current in pairwise(masses):
        ratio = Fraction(previous, current)
        alpha = Fraction(current - previous, previous * current * current)
        reciprocal_drop = Fraction(1, previous * previous) - Fraction(
            1, current * current
        )
        if alpha != ratio / (1 + ratio) * reciprocal_drop:
            raise AssertionError("the modulus-weight factorization failed")
        ratios.append(ratio)
        alphas.append(alpha)
        cumulative += alpha
        positive_weights.append(birth_weight - cumulative)

    maximum_ratio = max(ratios, default=Fraction(0))
    ratio_lower_bound = birth_weight / (1 + maximum_ratio)
    if any(weight < birth_weight / 2 for weight in positive_weights):
        raise AssertionError("a modulus-only weight fell below half birth")
    if any(weight < ratio_lower_bound for weight in positive_weights):
        raise AssertionError("a modulus-only weight failed the ratio bound")

    return ConstantHModulusAudit(
        moduli=masses,
        birth_weight=birth_weight,
        old_subtraction_weights=tuple(alphas),
        positive_atom_weights=tuple(positive_weights),
        half_birth_lower_bound=birth_weight / 2,
        maximum_future_ratio=maximum_ratio,
        ratio_lower_bound=ratio_lower_bound,
    )


def fixed_h_pair_audit(
    points: Sequence[int],
    left: int,
    right: int,
    *,
    horizon_count: int | None = None,
) -> FixedHPairAudit:
    """Audit one pair in the cumulative constant-``H`` innovation sum.

    If ``M_t`` are the prefix moduli from the pair's birth state onward and
    ``Phi_t`` is its aged ``H``-kernel, the exact coefficient per
    ``h_i h_j`` is

    ``Phi_0/M_0^2 - sum_(t>=1) (M_t-M_(t-1))/(M_(t-1)M_t^2) Phi_t``.

    The returned telescope expands this into positive ``E``-atoms by using
    ``H-B^T H B=E``.
    """
    marks = _validated_horizon(points)
    terminal = len(marks) if horizon_count is None else horizon_count
    if not _is_power_of_two(terminal):
        raise ValueError("horizon_count must be a power of two")
    counts = _pair_epochs(marks, left, right, terminal)
    moduli = tuple(_modulus(marks, count) for count in counts)
    kernels = tuple(
        pair_kernel(LYAPUNOV_MATRIX, left, right, count=count) for count in counts
    )
    e_kernels = tuple(
        pair_kernel(E_MATRIX, left, right, count=count) for count in counts
    )
    for index in range(len(counts) - 1):
        if kernels[index] - kernels[index + 1] != e_kernels[index]:
            raise AssertionError("the pairwise Lyapunov identity failed")

    inverse_birth_square = Fraction(1, moduli[0] ** 2)
    positive = inverse_birth_square * kernels[0]
    alphas: list[Fraction] = []
    negative = Fraction(0)
    for index in range(1, len(counts)):
        previous = moduli[index - 1]
        current = moduli[index]
        alpha = Fraction(current - previous, previous * current * current)
        reciprocal_drop = Fraction(1, previous * previous) - Fraction(
            1, current * current
        )
        theta = Fraction(previous, previous + current)
        if alpha != theta * reciprocal_drop or theta > Fraction(1, 2):
            raise AssertionError("the reciprocal-square factorization failed")
        if kernels[index] > kernels[0]:
            raise AssertionError("the transported H-kernel increased")
        alphas.append(alpha)
        negative += alpha * kernels[index]
    net = positive - negative

    cumulative_alpha = Fraction(0)
    telescope_weights = [inverse_birth_square]
    for alpha in alphas:
        cumulative_alpha += alpha
        telescope_weights.append(inverse_birth_square - cumulative_alpha)
    if any(weight < inverse_birth_square / 2 for weight in telescope_weights):
        raise AssertionError("a constant-H telescope weight fell below one half")

    telescope = (
        sum(
            (
                telescope_weights[index] * e_kernels[index]
                for index in range(len(counts) - 1)
            ),
            Fraction(0),
        )
        + telescope_weights[-1] * kernels[-1]
    )
    if telescope != net:
        raise AssertionError("the constant-H positive atom telescope failed")
    lower = positive / 2
    if not lower <= net <= positive:
        raise AssertionError("the constant-H half-birth bounds failed")

    weights = _gap_weights(marks)
    return FixedHPairAudit(
        left=left,
        right=right,
        birth_epoch=pair_birth_epoch(right),
        birth_count=counts[0],
        horizon_count=terminal,
        state_counts=counts,
        moduli=moduli,
        h_product=weights[left] * weights[right],
        birth_kernel_coefficient=positive,
        later_negative_coefficient=negative,
        net_kernel_coefficient=net,
        half_birth_lower_bound=lower,
        retention_ratio=net / positive,
        lyapunov_telescope_value=telescope,
        telescope_weights=tuple(telescope_weights),
    )


def finite_horizon_adjoint_weights(moduli: Sequence[int]) -> tuple[Matrix2, ...]:
    """Adjoints for the closed state horizon ``0,...,T``.

    The terminal weight is ``E`` and
    ``A_t=E+(M_t/M_(t+1))B^T A_(t+1)B``.  Therefore these weights account
    exactly for the observable sum over *all* supplied states, including the
    terminal state.  This is the one-index-shifted version of the canonical
    convention whose extra terminal adjoint is zero.
    """
    masses = tuple(moduli)
    if (
        len(masses) < 2
        or any(not isinstance(value, int) or value <= 0 for value in masses)
        or any(left > right for left, right in pairwise(masses))
    ):
        raise ValueError("moduli must be a nondecreasing positive sequence")
    rows = [E_MATRIX for _ in masses]
    rows[-1] = E_MATRIX
    for index in range(len(masses) - 2, -1, -1):
        rho = Fraction(masses[index], masses[index + 1])
        rows[index] = matrix_add(
            E_MATRIX,
            matrix_scale(rho, adjoint_transport(rows[index + 1])),
        )
    if any(not is_positive_semidefinite(row) for row in rows):
        raise AssertionError("a finite-horizon adjoint was not PSD")
    return tuple(rows)


@dataclass(frozen=True)
class ExactAdjointPairAudit:
    left: int
    right: int
    birth_epoch: int
    horizon_count: int
    state_counts: tuple[int, ...]
    moduli: tuple[int, ...]
    h_product: int
    signed_innovation_coefficient: Fraction
    positive_state_tail_coefficient: Fraction
    birth_e_lower_bound: Fraction
    fixed_h_birth_upper_bound: Fraction


def exact_adjoint_pair_audit(
    points: Sequence[int],
    left: int,
    right: int,
    *,
    horizon_count: int | None = None,
) -> ExactAdjointPairAudit:
    """Telescope one signed pair coefficient under exact horizon adjoints."""
    marks = _validated_horizon(points)
    terminal = len(marks) if horizon_count is None else horizon_count
    birth = pair_birth_epoch(right)
    if not 0 <= left < right < terminal <= len(marks) or terminal < 2 * birth:
        raise ValueError("the pair must lie inside a complete birth horizon")
    counts = _state_counts(terminal, initial_count=birth)
    if not 0 <= left < right < 2 * birth or counts[1] != 2 * birth:
        raise ValueError(
            "the pair and horizon do not determine a complete birth update"
        )
    moduli = tuple(_modulus(marks, count) for count in counts)
    adjoints = finite_horizon_adjoint_weights(moduli)

    birth_coefficient = pair_kernel(adjoints[1], left, right, count=counts[1]) / (
        moduli[1] ** 2
    )
    signed = birth_coefficient
    for index in range(2, len(counts)):
        previous = moduli[index - 1]
        current = moduli[index]
        alpha = Fraction(current - previous, previous * current * current)
        signed -= alpha * pair_kernel(adjoints[index], left, right, count=counts[index])

    state_tail = sum(
        (
            pair_kernel(E_MATRIX, left, right, count=counts[index])
            / (moduli[index] ** 2)
            for index in range(1, len(counts))
        ),
        Fraction(0),
    )
    if signed != state_tail:
        raise AssertionError("the exact-adjoint pair telescope failed")
    fixed_upper = pair_kernel(LYAPUNOV_MATRIX, left, right, count=counts[1]) / (
        moduli[1] ** 2
    )
    birth_e = pair_kernel(E_MATRIX, left, right, count=counts[1]) / (moduli[1] ** 2)
    if not birth_e <= signed <= fixed_upper:
        raise AssertionError("the exact pair coefficient escaped its birth bounds")

    weights = _gap_weights(marks)
    return ExactAdjointPairAudit(
        left=left,
        right=right,
        birth_epoch=birth,
        horizon_count=terminal,
        state_counts=counts,
        moduli=moduli,
        h_product=weights[left] * weights[right],
        signed_innovation_coefficient=signed,
        positive_state_tail_coefficient=state_tail,
        birth_e_lower_bound=birth_e,
        fixed_h_birth_upper_bound=fixed_upper,
    )


def q_pair_charge(
    points: Sequence[int], *, old_count: int, weight: Matrix2 = LYAPUNOV_MATRIX
) -> Fraction:
    """Evaluate ``<weight,Q_m/N_(2m)>`` from the short signed pair identity."""
    marks = _validated_marks(points)
    if (
        not isinstance(old_count, int)
        or not _is_power_of_two(old_count)
        or old_count < 1
        or 2 * old_count > len(marks)
    ):
        raise ValueError("old_count must be a complete dyadic update")
    terminal = 2 * old_count
    weights = _gap_weights(marks)
    old_modulus = _modulus(marks, old_count)
    new_modulus = _modulus(marks, terminal)
    growth = new_modulus - old_modulus
    positive = sum(
        (
            weights[left]
            * weights[right]
            * pair_kernel(weight, left, right, count=terminal)
            for right in range(old_count, terminal)
            for left in range(right)
        ),
        Fraction(0),
    ) / (new_modulus * new_modulus)
    negative = Fraction(growth, old_modulus * new_modulus * new_modulus) * sum(
        (
            weights[left]
            * weights[right]
            * pair_kernel(weight, left, right, count=terminal)
            for right in range(1, old_count)
            for left in range(right)
        ),
        Fraction(0),
    )
    return positive - negative


@dataclass(frozen=True)
class PairTelescopeAudit:
    mark_count: int
    update_count: int
    pair_count: int
    fixed_h_local_sum: Fraction
    fixed_h_pair_sum: Fraction
    raw_birth_sum: Fraction
    half_raw_birth_lower_bound: Fraction
    minimum_pair_retention: Fraction
    exact_adjoint_innovation_sum: Fraction
    exact_positive_pair_tail_sum: Fraction
    state_functional_sum: Fraction


def audit_pair_telescope(points: Sequence[int]) -> PairTelescopeAudit:
    """Audit both telescopes over every dyadic update of one finite prefix."""
    marks = _validated_horizon(points)
    terminal = len(marks)
    counts = _state_counts(terminal)
    moduli = tuple(_modulus(marks, count) for count in counts)
    weights = _gap_weights(marks)

    fixed_local = sum(
        (q_pair_charge(marks, old_count=count) for count in counts[:-1]),
        Fraction(0),
    )
    for count in counts[1:-1]:
        update = dyadic_gap_matrix_update(marks[: 2 * count], count)
        direct = frobenius_inner(LYAPUNOV_MATRIX, update.innovation) / (
            update.new_modulus
        )
        if q_pair_charge(marks, old_count=count) != direct:
            raise AssertionError(
                "the short Q-pair charge failed against the matrix update"
            )

    fixed_pair_sum = Fraction(0)
    raw_birth_sum = Fraction(0)
    minimum_retention = Fraction(1)
    exact_pair_sum = Fraction(0)
    for right in range(1, terminal):
        for left in range(right):
            fixed = fixed_h_pair_audit(marks, left, right)
            exact = exact_adjoint_pair_audit(marks, left, right)
            product = weights[left] * weights[right]
            fixed_pair_sum += product * fixed.net_kernel_coefficient
            raw_birth_sum += product * fixed.birth_kernel_coefficient
            exact_pair_sum += product * exact.positive_state_tail_coefficient
            minimum_retention = min(minimum_retention, fixed.retention_ratio)
    if fixed_local != fixed_pair_sum:
        raise AssertionError("the global constant-H pair regrouping failed")
    if not raw_birth_sum / 2 <= fixed_local <= raw_birth_sum:
        raise AssertionError("the global half-birth comparison failed")

    adjoints = finite_horizon_adjoint_weights(moduli)
    exact_innovations = sum(
        (
            q_pair_charge(marks, old_count=counts[index], weight=adjoints[index + 1])
            for index in range(len(counts) - 1)
        ),
        Fraction(0),
    )
    state_sum = sum(
        (
            sum(
                (
                    weights[left]
                    * weights[right]
                    * pair_kernel(E_MATRIX, left, right, count=count)
                    for right in range(1, count)
                    for left in range(right)
                ),
                Fraction(0),
            )
            / (_modulus(marks, count) ** 2)
            for count in counts
        ),
        Fraction(0),
    )
    if exact_innovations != exact_pair_sum or exact_innovations != state_sum:
        raise AssertionError("the global exact-adjoint telescope failed")
    if exact_innovations > fixed_local:
        raise AssertionError("the exact adjoint sum exceeded the constant-H majorant")

    return PairTelescopeAudit(
        mark_count=terminal,
        update_count=len(counts) - 1,
        pair_count=terminal * (terminal - 1) // 2,
        fixed_h_local_sum=fixed_local,
        fixed_h_pair_sum=fixed_pair_sum,
        raw_birth_sum=raw_birth_sum,
        half_raw_birth_lower_bound=raw_birth_sum / 2,
        minimum_pair_retention=minimum_retention,
        exact_adjoint_innovation_sum=exact_innovations,
        exact_positive_pair_tail_sum=exact_pair_sum,
        state_functional_sum=state_sum,
    )


def discounted_lyapunov_matrix(rho: Fraction | int) -> Matrix2:
    """Solve ``H_rho=E+rho B^T H_rho B`` exactly for ``0<=rho<=1``."""
    ratio = Fraction(rho)
    if not 0 <= ratio <= 1:
        raise ValueError("rho must lie in [0,1]")
    first = Fraction(16, 16 - ratio)
    off_diagonal = ratio * first / (2 * (8 - ratio))
    second = ratio * (first / 4 + off_diagonal) / (4 - ratio)
    matrix: Matrix2 = (
        (first, off_diagonal),
        (off_diagonal, second),
    )
    residual = matrix_add(
        E_MATRIX,
        matrix_scale(ratio, adjoint_transport(matrix)),
    )
    if matrix != residual:
        raise AssertionError("the discounted Lyapunov formula failed")
    return matrix


def constant_ratio_fixed_limit_kernel(rho: Fraction | int) -> Matrix2:
    """Return the infinite cumulative fixed-H pair kernel at constant ratio.

    If every future modulus ratio is ``rho=M_t/M_(t+1)``, retaining all later
    old-pair subtractions changes the raw birth kernel ``H`` into

    ``(H + rho H_(rho^2))/(1+rho)``.
    """
    ratio = Fraction(rho)
    if not 0 <= ratio <= 1:
        raise ValueError("rho must lie in [0,1]")
    return matrix_scale(
        Fraction(1, 1 + ratio),
        matrix_add(
            LYAPUNOV_MATRIX,
            matrix_scale(ratio, discounted_lyapunov_matrix(ratio * ratio)),
        ),
    )

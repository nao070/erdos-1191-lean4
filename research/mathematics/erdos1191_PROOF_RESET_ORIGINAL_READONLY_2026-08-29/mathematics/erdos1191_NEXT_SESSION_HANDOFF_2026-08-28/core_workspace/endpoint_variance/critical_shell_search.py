"""Exact finite experiments for critical-envelope birth shells.

The search arithmetic is :class:`fractions.Fraction` based.  The only
transcendental comparison, the critical-envelope test, uses a rigorous
rational enclosure of ``log(2)`` rather than a floating-point decision.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import comb
from random import Random

from endpoint_variance import diameter_regime_variance
from multiscale_variance import cyclic_arc_covariance


@dataclass(frozen=True)
class EnvelopeRow:
    j: int
    mark_count: int
    modulus: int
    required_log: Fraction
    log_lower: Fraction
    log_upper: Fraction
    certified: bool


@dataclass(frozen=True)
class EnvelopeAudit:
    constant: Fraction
    compatible: bool
    rows: tuple[EnvelopeRow, ...]


@dataclass(frozen=True)
class BirthShell:
    shell: int
    net: Fraction
    diagonal: Fraction
    off_diagonal: Fraction


@dataclass(frozen=True)
class ShellDecomposition:
    j0: int
    horizon: int
    level_energies: tuple[Fraction, ...]
    functional: Fraction
    shells: tuple[BirthShell, ...]


@dataclass(frozen=True)
class CandidateResult:
    name: str
    first_failure: tuple[int, int] | None


@dataclass(frozen=True)
class ExhaustiveRulers:
    mark_count: int
    diameter: int
    candidate_count: int
    node_count: int
    rulers: tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class RandomRulers:
    mark_count: int
    attempts: int
    max_step: int
    seed: int
    failure_count: int
    rulers: tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class DenseRandomRulers:
    mark_count: int
    attempts: int
    scan_limit: int
    choice_window: int
    seed: int
    failure_count: int
    rulers: tuple[tuple[int, ...], ...]


def _validated_ruler(points: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    ruler = tuple(points)
    if len(ruler) < 2:
        raise ValueError("a ruler needs at least two marks")
    if any(not isinstance(point, int) for point in ruler):
        raise TypeError("ruler marks must be integers")
    if tuple(sorted(ruler)) != ruler or len(set(ruler)) != len(ruler):
        raise ValueError("ruler marks must be strictly increasing")
    return ruler


def _validated_levels(ruler: tuple[int, ...], j0: int, horizon: int) -> None:
    if not isinstance(j0, int) or not isinstance(horizon, int):
        raise TypeError("j0 and horizon must be integers")
    if j0 < 1 or horizon < j0:
        raise ValueError("levels must satisfy 1 <= j0 <= horizon")
    if 2**horizon > len(ruler):
        raise ValueError("the ruler is too short for the requested horizon")


def log_two_interval(terms: int = 16) -> tuple[Fraction, Fraction]:
    """Rigorous rational enclosure of ``log(2)``.

    It uses ``log(2)=2*sum_{k>=0}(1/3)^(2k+1)/(2k+1)``.  Replacing every
    denominator in the positive tail by its first denominator gives the
    stated geometric upper bound.
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer")
    if terms < 1:
        raise ValueError("terms must be positive")
    z = Fraction(1, 3)
    lower = 2 * sum(
        (z ** (2 * k + 1) / (2 * k + 1) for k in range(terms)),
        Fraction(0),
    )
    tail = (
        2
        * z ** (2 * terms + 1)
        / ((2 * terms + 1) * (1 - z * z))
    )
    return lower, lower + tail


def critical_envelope_audit(
    points: tuple[int, ...] | list[int],
    *,
    j0: int,
    horizon: int,
    constant: Fraction,
) -> EnvelopeAudit:
    """Certify every dyadic critical-envelope inequality in the range."""
    ruler = _validated_ruler(points)
    _validated_levels(ruler, j0, horizon)
    c = Fraction(constant)
    if c <= 0:
        raise ValueError("the critical-envelope constant must be positive")

    rows: list[EnvelopeRow] = []
    for j in range(j0, horizon + 1):
        mark_count = 2**j
        modulus = ruler[mark_count - 1] - ruler[0] + 1
        required_log = Fraction(modulus, 2 * c * mark_count**2)

        terms = 8
        while True:
            log_two_lower, log_two_upper = log_two_interval(terms)
            lower = j * log_two_lower
            upper = j * log_two_upper
            if required_log <= lower:
                certified = True
                break
            if required_log > upper:
                certified = False
                break
            terms *= 2
            if terms > 512:
                raise ArithmeticError("log enclosure did not decide the inequality")
        rows.append(
            EnvelopeRow(
                j=j,
                mark_count=mark_count,
                modulus=modulus,
                required_log=required_log,
                log_lower=lower,
                log_upper=upper,
                certified=certified,
            )
        )
    return EnvelopeAudit(c, all(row.certified for row in rows), tuple(rows))


@dataclass(frozen=True)
class _Edge:
    left_index: int
    right_index: int
    left: int
    right: int
    birth: int

    @property
    def length(self) -> int:
        return self.right - self.left


def _edges(ruler: tuple[int, ...], j0: int, horizon: int) -> tuple[_Edge, ...]:
    result: list[_Edge] = []
    for left_index, right_index in combinations(range(2**horizon), 2):
        # Indices in the formula are one based.  ceil(log2(v)) is the
        # bit-length of v-1.
        right_one_based = right_index + 1
        birth = max(j0, (right_one_based - 1).bit_length())
        result.append(
            _Edge(
                left_index,
                right_index,
                ruler[left_index],
                ruler[right_index],
                birth,
            )
        )
    return tuple(result)


def birth_shell_decomposition(
    points: tuple[int, ...] | list[int], *, j0: int, horizon: int
) -> ShellDecomposition:
    """Return the exact ordered-interaction birth-shell partition."""
    ruler = _validated_ruler(points)
    _validated_levels(ruler, j0, horizon)
    edges = _edges(ruler, j0, horizon)
    moduli = {
        j: ruler[2**j - 1] - ruler[0] + 1 for j in range(j0, horizon + 1)
    }

    level_energies = tuple(
        diameter_regime_variance(ruler[: 2**j], moduli[j]) / (2**j) ** 3
        for j in range(j0, horizon + 1)
    )
    shells: list[BirthShell] = []
    for shell in range(j0, horizon + 1):
        net = Fraction(0)
        diagonal = Fraction(0)
        for left_edge, right_edge in product(edges, repeat=2):
            if max(left_edge.birth, right_edge.birth) != shell:
                continue
            contribution = Fraction(0)
            for j in range(shell, horizon + 1):
                modulus = moduli[j]
                contribution += cyclic_arc_covariance(
                    left_edge.left,
                    left_edge.length,
                    right_edge.left,
                    right_edge.length,
                    modulus,
                ) / (modulus * (2**j) ** 3)
            net += contribution
            if left_edge == right_edge:
                diagonal += contribution
        shells.append(BirthShell(shell, net, diagonal, net - diagonal))
    return ShellDecomposition(
        j0,
        horizon,
        level_energies,
        sum(level_energies, Fraction(0)),
        tuple(shells),
    )


def literal_arc_covariance(
    left_start: int,
    left_length: int,
    right_start: int,
    right_length: int,
    modulus: int,
) -> Fraction:
    """Independent covariance oracle using literal residue sets."""
    if not isinstance(modulus, int) or modulus < 2:
        raise ValueError("modulus must be an integer at least 2")
    if not 1 <= left_length < modulus or not 1 <= right_length < modulus:
        raise ValueError("arc lengths must lie in [1, modulus)")
    left_arc = {
        (left_start + step) % modulus for step in range(1, left_length + 1)
    }
    right_arc = {
        (right_start + step) % modulus for step in range(1, right_length + 1)
    }
    return Fraction(len(left_arc & right_arc)) - Fraction(
        left_length * right_length, modulus
    )


def _literal_level_energy(ruler: tuple[int, ...], j: int) -> Fraction:
    mark_count = 2**j
    prefix = ruler[:mark_count]
    modulus = prefix[-1] - prefix[0] + 1
    loads = [0] * modulus
    for left_index, right_index in combinations(range(mark_count), 2):
        left = prefix[left_index]
        right = prefix[right_index]
        for step in range(1, right - left + 1):
            loads[(left + step) % modulus] += 1
    mean = Fraction(sum(loads), modulus)
    variance = sum((Fraction(load) - mean) ** 2 for load in loads) / modulus
    return variance / mark_count**3


def oracle_birth_shell_decomposition(
    points: tuple[int, ...] | list[int], *, j0: int, horizon: int
) -> ShellDecomposition:
    """Literal-set oracle for the complete shell decomposition."""
    ruler = _validated_ruler(points)
    _validated_levels(ruler, j0, horizon)
    edges = _edges(ruler, j0, horizon)
    moduli = {
        j: ruler[2**j - 1] - ruler[0] + 1 for j in range(j0, horizon + 1)
    }
    energies = tuple(_literal_level_energy(ruler, j) for j in range(j0, horizon + 1))
    shells: list[BirthShell] = []
    for shell in range(j0, horizon + 1):
        net = Fraction(0)
        diagonal = Fraction(0)
        for left_edge, right_edge in product(edges, repeat=2):
            if max(left_edge.birth, right_edge.birth) != shell:
                continue
            contribution = sum(
                (
                    literal_arc_covariance(
                        left_edge.left,
                        left_edge.length,
                        right_edge.left,
                        right_edge.length,
                        moduli[j],
                    )
                    / (moduli[j] * (2**j) ** 3)
                    for j in range(shell, horizon + 1)
                ),
                Fraction(0),
            )
            net += contribution
            if left_edge == right_edge:
                diagonal += contribution
        shells.append(BirthShell(shell, net, diagonal, net - diagonal))
    return ShellDecomposition(
        j0,
        horizon,
        energies,
        sum(energies, Fraction(0)),
        tuple(shells),
    )


def audit_candidates(
    points: tuple[int, ...] | list[int], *, j0: int, horizon: int
) -> dict[str, CandidateResult]:
    """Return the first exact failure of H1--H6 for one ruler."""
    ruler = _validated_ruler(points)
    _validated_levels(ruler, j0, horizon)
    failures: dict[str, tuple[int, int] | None] = {
        name: None for name in ("H1", "H2", "H3", "H4", "H5", "H6")
    }

    local = {
        level: birth_shell_decomposition(ruler, j0=j0, horizon=level)
        for level in range(j0, horizon + 1)
    }
    for current_horizon in range(j0, horizon + 1):
        decomposition = local[current_horizon]
        for shell in decomposition.shells:
            location = (shell.shell, current_horizon)
            if failures["H1"] is None and shell.off_diagonal > 0:
                failures["H1"] = location
            if failures["H2"] is None and not (
                Fraction(0) <= shell.net <= shell.diagonal
            ):
                failures["H2"] = location
            if failures["H6"] is None and shell.net < 0:
                failures["H6"] = location
            if (
                failures["H4"] is None
                and shell.shell == current_horizon
                and shell.off_diagonal > 0
            ):
                failures["H4"] = location

    for shell_level in range(j0, horizon):
        baseline = local[shell_level].shells[shell_level - j0].net
        for current_horizon in range(shell_level + 1, horizon + 1):
            persisted = local[current_horizon].shells[shell_level - j0].net
            if persisted > baseline:
                failures["H3"] = (shell_level, current_horizon)
                break
        if failures["H3"] is not None:
            break

    final_energies = local[horizon].level_energies
    for offset in range(len(final_energies) - 1):
        if final_energies[offset + 1] > final_energies[offset]:
            left_level = j0 + offset
            failures["H5"] = (left_level, left_level + 1)
            break

    return {
        name: CandidateResult(name, first_failure)
        for name, first_failure in failures.items()
    }


def _new_differences(mark: int, marks: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(mark - prior for prior in marks)


def exhaustive_rulers(*, mark_count: int, diameter: int) -> ExhaustiveRulers:
    """Complete branch-and-bound enumeration at fixed size and diameter."""
    if not isinstance(mark_count, int) or not isinstance(diameter, int):
        raise TypeError("mark_count and diameter must be integers")
    if mark_count < 2 or diameter < 1:
        raise ValueError("mark_count >= 2 and diameter >= 1 are required")
    internal_count = mark_count - 2
    candidate_count = (
        comb(diameter - 1, internal_count)
        if 0 <= internal_count <= diameter - 1
        else 0
    )
    rulers: list[tuple[int, ...]] = []
    node_count = 1

    def visit(marks: tuple[int, ...], used: frozenset[int]) -> None:
        nonlocal node_count
        selected_internal = len(marks) - 1
        if selected_internal == internal_count:
            new = _new_differences(diameter, marks)
            if len(new) == len(set(new)) and used.isdisjoint(new):
                node_count += 1
                rulers.append((*marks, diameter))
            return

        remaining_after_choice = internal_count - selected_internal - 1
        maximum = diameter - remaining_after_choice - 1
        for mark in range(marks[-1] + 1, maximum + 1):
            new = _new_differences(mark, marks)
            if len(new) != len(set(new)) or not used.isdisjoint(new):
                continue
            node_count += 1
            visit((*marks, mark), used.union(new))

    if candidate_count:
        visit((0,), frozenset())
    return ExhaustiveRulers(
        mark_count,
        diameter,
        candidate_count,
        node_count,
        tuple(rulers),
    )


def random_greedy_rulers(
    *, mark_count: int, attempts: int, max_step: int, seed: int
) -> RandomRulers:
    """Seeded targeted construction of Golomb rulers by random greedy steps."""
    if any(not isinstance(value, int) for value in (mark_count, attempts, max_step, seed)):
        raise TypeError("random-search parameters must be integers")
    if mark_count < 2 or attempts < 1 or max_step < 1:
        raise ValueError("mark_count >= 2, attempts >= 1 and max_step >= 1")
    generator = Random(seed)
    retained: set[tuple[int, ...]] = set()
    failures = 0
    for _ in range(attempts):
        marks = [0]
        used: set[int] = set()
        while len(marks) < mark_count:
            candidates = list(range(marks[-1] + 1, marks[-1] + max_step + 1))
            generator.shuffle(candidates)
            chosen: tuple[int, tuple[int, ...]] | None = None
            for mark in candidates:
                new = _new_differences(mark, tuple(marks))
                if len(new) == len(set(new)) and used.isdisjoint(new):
                    chosen = mark, new
                    break
            if chosen is None:
                failures += 1
                break
            mark, new = chosen
            marks.append(mark)
            used.update(new)
        if len(marks) == mark_count:
            retained.add(tuple(marks))
    return RandomRulers(
        mark_count,
        attempts,
        max_step,
        seed,
        failures,
        tuple(sorted(retained)),
    )


def random_dense_greedy_rulers(
    *,
    mark_count: int,
    attempts: int,
    scan_limit: int,
    choice_window: int,
    seed: int,
) -> DenseRandomRulers:
    """Seeded greedy search choosing among the first few valid next marks."""
    parameters = (mark_count, attempts, scan_limit, choice_window, seed)
    if any(not isinstance(value, int) for value in parameters):
        raise TypeError("dense-random-search parameters must be integers")
    if mark_count < 2 or attempts < 1 or scan_limit < 1 or choice_window < 1:
        raise ValueError("positive parameters and mark_count >= 2 are required")
    generator = Random(seed)
    retained: set[tuple[int, ...]] = set()
    failures = 0
    for _ in range(attempts):
        marks = [0]
        used: set[int] = set()
        while len(marks) < mark_count:
            valid: list[tuple[int, tuple[int, ...]]] = []
            for mark in range(marks[-1] + 1, marks[-1] + scan_limit + 1):
                new = _new_differences(mark, tuple(marks))
                if len(new) == len(set(new)) and used.isdisjoint(new):
                    valid.append((mark, new))
                    if len(valid) == choice_window:
                        break
            if not valid:
                failures += 1
                break
            mark, new = generator.choice(valid)
            marks.append(mark)
            used.update(new)
        if len(marks) == mark_count:
            retained.add(tuple(marks))
    return DenseRandomRulers(
        mark_count,
        attempts,
        scan_limit,
        choice_window,
        seed,
        failures,
        tuple(sorted(retained)),
    )

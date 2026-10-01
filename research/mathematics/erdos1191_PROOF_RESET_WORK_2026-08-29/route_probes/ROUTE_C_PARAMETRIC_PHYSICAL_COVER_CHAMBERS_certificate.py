#!/usr/bin/env python3
"""Exact chamber certificate for one fixed-history physical-cover LP.

The final verifier uses only fractions.Fraction.  SciPy was used offline to
discover primal supports and endpoint-dual bases; neither generation nor
verification imports a numerical optimizer.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import hashlib
from itertools import combinations
import json
from pathlib import Path
from typing import Mapping, Sequence

import direct_b_membership_sddm_lp_certificate as membership
import direct_b_physical_energy_lp_certificate as physical


HERE = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = HERE / "ROUTE_C_PARAMETRIC_PHYSICAL_COVER_CHAMBERS_certificate.json"
SCHEMA = "erdos1191.route_c_parametric_physical_cover_chambers.v1"
STATUS = "EXACT_FIXED_HISTORY_ONE_PHASE_ROOT_SDDM_PLUS_J_ONLY_GLOBAL_LEDGER_OPEN"
PHASE_LOWER = F(128)
PHASE_UPPER = F(256)
FULL_POINTS = tuple(k * (k + 100) for k in range(16))
POINTS = FULL_POINTS[3:]
MATRIX, SUPPORT4, SUPPORT8 = membership.two_epoch_matrix()
SUPPORTS = (SUPPORT4, SUPPORT8)
PAIRS = tuple(combinations(range(len(POINTS)), 2))
VARIABLE_LABELS = tuple(f"{i},{j}" for i, j in PAIRS) + ("kappa4", "kappa8")

SEED_JSON = r'''{"breakpoints":["128/1","129/1","327/2","333/2","339/2","345/2","351/2","357/2","363/2","369/2","375/2","381/2","216/1","220/1","224/1","228/1","232/1","236/1","240/1","244/1","248/1","252/1","256/1"],"events":[{"lower":"128/1","pieces":[{"demand_alpha":"87/256","demand_beta":"-6559/128","left_dual":{"columns":[1,24,43,76,79],"rows":[4,11,16,34,35]},"lower":"128/1","objective_alpha":"827/3360","objective_beta":"-579/40","primal":{"1":"113/4480","24":"27/1120","43":"17/13440","76":"7/960","79":"1/480"},"right_dual":{"columns":[1,24,43,76,79],"rows":[4,11,16,34,35]},"upper":"129/1"}],"upper":"129/1"},{"lower":"129/1","pieces":[{"demand_alpha":"87/256","demand_beta":"-6559/128","left_dual":{"columns":[1,24,43,76],"rows":[4,11,16,35]},"lower":"129/1","objective_alpha":"53/224","objective_beta":"-213/16","primal":{"1":"45/1792","24":"11/448","43":"3/1792","76":"1/128"},"right_dual":{"columns":[1,24,42,43,76],"rows":[4,11,16,35]},"upper":"577/4"},{"demand_alpha":"87/256","demand_beta":"-6559/128","left_dual":{"columns":[1,24,42,43,76],"rows":[4,11,16,35]},"lower":"577/4","objective_alpha":"103/448","objective_beta":"-22125/1792","primal":{"1":"45/1792","24":"11/448","42":"3/1792","76":"1/128"},"right_dual":{"columns":[0,1,24,42,76],"rows":[4,11,16,35]},"upper":"6493/44"},{"demand_alpha":"87/256","demand_beta":"-6559/128","left_dual":{"columns":[0,1,24,42,76],"rows":[4,11,16,35]},"lower":"6493/44","objective_alpha":"5/32","objective_beta":"-189/128","primal":{"0":"3/128","24":"1/32","76":"1/128"},"right_dual":{"columns":[0,24,76,77],"rows":[4,11,35]},"upper":"643/4"},{"demand_alpha":"87/256","demand_beta":"-6559/128","left_dual":{"columns":[0,24,76,77],"rows":[4,11,35]},"lower":"643/4","objective_alpha":"1/8","objective_beta":"227/64","primal":{"0":"3/128","24":"1/32","77":"1/128"},"right_dual":{"columns":[0,24,33,77],"rows":[4,11,35]},"upper":"2573/16"},{"demand_alpha":"87/256","demand_beta":"-6559/128","left_dual":{"columns":[0,24,33,77],"rows":[4,11,35]},"lower":"2573/16","objective_alpha":"0/1","objective_beta":"3027/128","primal":{"0":"1/32","33":"1/32","77":"1/128"},"right_dual":{"columns":[0,33,77],"rows":[4,11,35]},"upper":"327/2"}],"upper":"327/2"},{"lower":"327/2","pieces":[{"demand_alpha":"107/256","demand_beta":"-4097/64","left_dual":{"columns":[0,1,33,42,77],"rows":[4,6,11,16,35]},"lower":"327/2","objective_alpha":"45/448","objective_beta":"3795/448","primal":{"0":"11/1792","1":"45/1792","33":"11/448","42":"3/1792","77":"1/128"},"right_dual":{"columns":[0,1,33,42,77],"rows":[4,6,11,16,35]},"upper":"333/2"}],"upper":"333/2"},{"lower":"333/2","pieces":[{"demand_alpha":"127/256","demand_beta":"-9859/128","left_dual":{"columns":[0,1,14,24,42,77],"rows":[4,6,9,11,16,35]},"lower":"333/2","objective_alpha":"89/448","objective_beta":"-13123/1792","primal":{"1":"45/1792","24":"11/448","42":"3/1792","77":"1/128"},"right_dual":{"columns":[0,1,14,24,42,77],"rows":[4,6,9,11,16,35]},"upper":"339/2"}],"upper":"339/2"},{"lower":"339/2","pieces":[{"demand_alpha":"127/256","demand_beta":"-9859/128","left_dual":{"columns":[1,2,14,24,25,42,77],"rows":[4,6,9,11,12,16,35]},"lower":"339/2","objective_alpha":"1/5","objective_beta":"-2879/384","primal":{"1":"1/40","24":"47/1920","25":"1/1920","42":"1/640","77":"1/128"},"right_dual":{"columns":[0,1,24,25,33,42,77],"rows":[4,6,9,11,12,16,35]},"upper":"345/2"}],"upper":"345/2"},{"lower":"345/2","pieces":[{"demand_alpha":"127/256","demand_beta":"-9859/128","left_dual":{"columns":[0,1,14,24,25,42,77],"rows":[4,6,9,11,12,16,35]},"lower":"345/2","objective_alpha":"1/5","objective_beta":"-2879/384","primal":{"1":"1/40","24":"47/1920","25":"1/1920","42":"1/640","77":"1/128"},"right_dual":{"columns":[0,1,14,24,25,42,77],"rows":[4,6,9,11,12,16,35]},"upper":"351/2"}],"upper":"351/2"},{"lower":"351/2","pieces":[{"demand_alpha":"33/64","demand_beta":"-41191/512","left_dual":{"columns":[0,1,24,25,33,42,43,77],"rows":[4,6,9,11,12,16,18,35]},"lower":"351/2","objective_alpha":"23/112","objective_beta":"-1061/128","primal":{"1":"45/1792","24":"11/448","43":"3/1792","77":"1/128"},"right_dual":{"columns":[0,1,24,25,33,42,43,77],"rows":[4,6,9,11,12,16,18,35]},"upper":"357/2"}],"upper":"357/2"},{"lower":"357/2","pieces":[{"demand_alpha":"65/128","demand_beta":"-40477/512","left_dual":{"columns":[0,1,24,25,33,42,43,77],"rows":[4,6,9,11,12,16,18,35]},"lower":"357/2","objective_alpha":"23/112","objective_beta":"-1061/128","primal":{"1":"45/1792","24":"11/448","43":"3/1792","77":"1/128"},"right_dual":{"columns":[0,1,24,25,33,42,43,77],"rows":[4,6,9,11,12,16,18,35]},"upper":"363/2"}],"upper":"363/2"},{"lower":"363/2","pieces":[{"demand_alpha":"1/2","demand_beta":"-39751/512","left_dual":{"columns":[0,1,24,25,33,42,43,77],"rows":[4,6,9,11,12,16,18,35]},"lower":"363/2","objective_alpha":"23/112","objective_beta":"-1061/128","primal":{"1":"45/1792","24":"11/448","43":"3/1792","77":"1/128"},"right_dual":{"columns":[0,1,24,25,33,42,43,77],"rows":[4,6,9,11,12,16,18,35]},"upper":"369/2"}],"upper":"369/2"},{"lower":"369/2","pieces":[{"demand_alpha":"63/128","demand_beta":"-39013/512","left_dual":{"columns":[0,1,24,25,33,42,43,77],"rows":[4,6,9,11,12,16,18,35]},"lower":"369/2","objective_alpha":"23/112","objective_beta":"-1061/128","primal":{"1":"45/1792","24":"11/448","43":"3/1792","77":"1/128"},"right_dual":{"columns":[0,1,24,33,35,42,43,77],"rows":[4,6,9,11,15,16,18,35]},"upper":"375/2"}],"upper":"375/2"},{"lower":"375/2","pieces":[{"demand_alpha":"31/64","demand_beta":"-38263/512","left_dual":{"columns":[0,1,24,33,35,42,43,77],"rows":[4,6,9,11,15,16,18,35]},"lower":"375/2","objective_alpha":"23/112","objective_beta":"-1061/128","primal":{"1":"45/1792","24":"11/448","43":"3/1792","77":"1/128"},"right_dual":{"columns":[0,1,24,33,35,42,43,77],"rows":[4,6,9,11,15,16,18,35]},"upper":"381/2"}],"upper":"381/2"},{"lower":"381/2","pieces":[{"demand_alpha":"129/256","demand_beta":"-5021/64","left_dual":{"columns":[0,1,14,24,35,42,43,74,76],"rows":[4,6,9,11,15,16,18,33,35]},"lower":"381/2","objective_alpha":"53/224","objective_beta":"-213/16","primal":{"1":"45/1792","24":"11/448","43":"3/1792","76":"1/128"},"right_dual":{"columns":[0,1,12,24,33,42,43,75,76],"rows":[4,6,9,11,15,18,33,35]},"upper":"216/1"}],"upper":"216/1"},{"lower":"216/1","pieces":[{"demand_alpha":"97/256","demand_beta":"-3293/64","left_dual":{"columns":[0,1,12,24,33,42,43,75,76],"rows":[4,6,9,11,15,18,33,35]},"lower":"216/1","objective_alpha":"61/448","objective_beta":"939/112","primal":{"1":"45/1792","24":"11/448","43":"3/1792","76":"1/128"},"right_dual":{"columns":[0,1,12,14,24,33,43,50,75,76],"rows":[4,6,9,12,15,16,18,33,35]},"upper":"220/1"}],"upper":"220/1"},{"lower":"220/1","pieces":[{"demand_alpha":"69/256","demand_beta":"-1753/64","left_dual":{"columns":[0,2,14,33,76,77],"rows":[5,6,9,10,33,35]},"lower":"220/1","objective_alpha":"27/160","objective_beta":"199/16","primal":{"0":"5/128","14":"11/640","2":"11/640","33":"5/128","76":"1/128"},"right_dual":{"columns":[0,2,14,33,75,76],"rows":[5,6,9,10,33,35]},"upper":"224/1"}],"upper":"224/1"},{"lower":"224/1","pieces":[{"demand_alpha":"37/256","demand_beta":"39/64","left_dual":{"columns":[0,2,14,33,76,77],"rows":[5,6,9,10,33,35]},"lower":"224/1","objective_alpha":"27/160","objective_beta":"199/16","primal":{"0":"5/128","14":"11/640","2":"11/640","33":"5/128","76":"1/128"},"right_dual":{"columns":[0,2,14,33,75,76],"rows":[5,6,9,10,33,35]},"upper":"228/1"}],"upper":"228/1"},{"lower":"228/1","pieces":[{"demand_alpha":"37/256","demand_beta":"39/64","left_dual":{"columns":[0,2,14,33,76,77],"rows":[5,6,9,11,33,35]},"lower":"228/1","objective_alpha":"27/160","objective_beta":"199/16","primal":{"0":"5/128","14":"11/640","2":"11/640","33":"5/128","76":"1/128"},"right_dual":{"columns":[0,2,14,33,76,77],"rows":[5,6,9,11,33,35]},"upper":"232/1"}],"upper":"232/1"},{"lower":"232/1","pieces":[{"demand_alpha":"29/256","demand_beta":"503/64","left_dual":{"columns":[0,2,14,33,75,76],"rows":[5,6,9,11,33,35]},"lower":"232/1","objective_alpha":"27/160","objective_beta":"199/16","primal":{"0":"5/128","14":"11/640","2":"11/640","33":"5/128","76":"1/128"},"right_dual":{"columns":[0,2,14,33,75,76],"rows":[5,6,9,11,33,35]},"upper":"236/1"}],"upper":"236/1"},{"lower":"236/1","pieces":[{"demand_alpha":"19/128","demand_beta":"-7/16","left_dual":{"columns":[0,2,14,15,33,36,75,76],"rows":[5,6,9,10,11,16,33,35]},"lower":"236/1","objective_alpha":"37/192","objective_beta":"5255/576","primal":{"0":"5/128","14":"35/2304","2":"35/2304","33":"5/128","36":"23/2304","76":"1/128"},"right_dual":{"columns":[0,2,14,33,36,75,76],"rows":[5,6,9,11,16,33,35]},"upper":"240/1"}],"upper":"240/1"},{"lower":"240/1","pieces":[{"demand_alpha":"19/128","demand_beta":"-7/16","left_dual":{"columns":[0,2,14,33,36,44,76,77],"rows":[5,6,9,11,16,19,33,35]},"lower":"240/1","objective_alpha":"323/1664","objective_beta":"3557/384","primal":{"0":"5/128","14":"301/19968","2":"105/6656","33":"5/128","36":"155/19968","44":"7/3328","76":"1/128"},"right_dual":{"columns":[0,2,14,33,36,44,76,77],"rows":[5,6,9,11,16,19,33,35]},"upper":"244/1"}],"upper":"244/1"},{"lower":"244/1","pieces":[{"demand_alpha":"19/128","demand_beta":"-7/16","left_dual":{"columns":[0,2,14,33,36,44,75,76],"rows":[5,6,9,11,16,19,33,35]},"lower":"244/1","objective_alpha":"323/1664","objective_beta":"3557/384","primal":{"0":"5/128","14":"301/19968","2":"105/6656","33":"5/128","36":"155/19968","44":"7/3328","76":"1/128"},"right_dual":{"columns":[0,2,14,33,36,44,50,75,76],"rows":[5,6,9,11,16,19,33,35]},"upper":"2197/9"},{"demand_alpha":"19/128","demand_beta":"-7/16","left_dual":{"columns":[0,2,14,33,36,44,50,75,76],"rows":[5,6,9,11,16,19,33,35]},"lower":"2197/9","objective_alpha":"1655/8576","objective_beta":"245417/25728","primal":{"0":"5/128","14":"1561/102912","2":"525/34304","33":"663/17152","36":"1025/102912","50":"7/4288","76":"1/128"},"right_dual":{"columns":[0,2,14,33,36,50,75,76],"rows":[5,6,9,11,16,19,33,35]},"upper":"248/1"}],"upper":"248/1"},{"lower":"248/1","pieces":[{"demand_alpha":"19/128","demand_beta":"-7/16","left_dual":{"columns":[0,2,14,33,36,50,75,76],"rows":[5,6,9,11,16,19,33,35]},"lower":"248/1","objective_alpha":"1655/8576","objective_beta":"245417/25728","primal":{"0":"5/128","14":"1561/102912","2":"525/34304","33":"663/17152","36":"1025/102912","50":"7/4288","76":"1/128"},"right_dual":{"columns":[0,2,14,23,24,33,36,50,75,76],"rows":[5,6,9,11,16,19,33,35]},"upper":"1005/4"},{"demand_alpha":"19/128","demand_beta":"-7/16","left_dual":{"columns":[0,2,14,23,24,33,36,50,75,76],"rows":[5,6,9,11,16,19,33,35]},"lower":"1005/4","objective_alpha":"5/32","objective_beta":"1931393/102912","primal":{"0":"5/128","14":"77/12864","2":"525/34304","24":"315/34304","33":"663/17152","36":"1025/102912","50":"7/4288","76":"1/128"},"right_dual":{"columns":[0,2,14,23,24,33,36,50,75,76],"rows":[5,6,9,11,14,16,19,33,35]},"upper":"252/1"}],"upper":"252/1"},{"lower":"252/1","pieces":[{"demand_alpha":"47/256","demand_beta":"-595/64","left_dual":{"columns":[0,2,14,23,24,33,36,45,71,74,77,79],"rows":[5,6,9,11,14,16,19,32,33,34,35]},"lower":"252/1","objective_alpha":"607/2368","objective_beta":"-28399/28416","primal":{"0":"5/128","14":"1/444","2":"361/18944","24":"227/18944","33":"315/9472","36":"73/56832","45":"13/14208","71":"3/296","74":"25/4736","77":"115/56832","79":"55/7104"},"right_dual":{"columns":[0,2,14,23,24,33,36,45,71,74,77,79],"rows":[5,6,9,11,14,16,19,32,34,35]},"upper":"27355/108"},{"demand_alpha":"47/256","demand_beta":"-595/64","left_dual":{"columns":[0,2,14,23,24,33,36,45,71,74,77,79],"rows":[5,6,9,11,14,16,19,32,34,35]},"lower":"27355/108","objective_alpha":"53/272","objective_beta":"31711/2176","primal":{"0":"5/128","14":"37/6528","2":"199/13056","24":"41/4352","33":"5/128","36":"43/4352","45":"1/2176","71":"29/6528","74":"5/384","77":"15/4352"},"right_dual":{"columns":[0,2,14,23,24,33,34,36,42,45,71,74,77,79],"rows":[5,6,9,10,11,14,16,19,32,34,35]},"upper":"4929829/19428"},{"demand_alpha":"47/256","demand_beta":"-595/64","left_dual":{"columns":[0,2,14,23,24,33,34,36,42,45,71,74,77,79],"rows":[5,6,9,10,11,14,16,19,32,34,35]},"lower":"4929829/19428","objective_alpha":"27977/161664","objective_beta":"39000917/1939968","primal":{"0":"5/128","2":"15407/969984","24":"1603/107776","33":"757/20208","34":"259/161664","36":"7303/969984","45":"217/242496","71":"287/60624","74":"757/60624","77":"6545/1939968","79":"259/484992"},"right_dual":{"columns":[0,2,23,24,33,34,36,42,45,71,74,77,79],"rows":[5,6,9,10,11,14,16,19,32,34,35]},"upper":"256/1"}],"upper":"256/1"}],"transport_actual_breakpoints":[{"T":"216/1","dual":{"columns":[0,1,12,24,33,42,43,75,76],"rows":[3,5,7,9,13,16,31,33]}},{"T":"220/1","dual":{"columns":[0,1,12,14,24,33,43,50,75,76],"rows":[4,5,7,9,12,13,15,30,32]}}]}'''
SEED = json.loads(SEED_JSON)


class CertificateError(RuntimeError):
    """Raised when an exact chamber, LP, integral, or scope check fails."""


def ftext(value: F | int) -> str:
    value = F(value)
    return f"{value.numerator}/{value.denominator}"


def exact_breakpoints() -> tuple[F, ...]:
    values = {PHASE_LOWER, PHASE_UPPER}
    for i, j in PAIRS:
        distance = POINTS[j] - POINTS[i]
        for divisor in (1, 2):
            value = F(distance, divisor)
            if PHASE_LOWER <= value <= PHASE_UPPER:
                values.add(value)
    return tuple(sorted(values))


def rref_unique(
    matrix: Sequence[Sequence[F]], rhs: Sequence[F]
) -> tuple[F, ...]:
    if not matrix or len(matrix) != len(rhs):
        raise CertificateError("invalid exact linear system")
    column_count = len(matrix[0])
    if not column_count or any(len(row) != column_count for row in matrix):
        raise CertificateError("ragged exact linear system")
    rows = [list(row) + [value] for row, value in zip(matrix, rhs)]
    row_count = len(rows)
    pivot_row = 0
    pivots: list[int] = []
    for column in range(column_count):
        found = next(
            (row for row in range(pivot_row, row_count) if rows[row][column]),
            None,
        )
        if found is None:
            continue
        rows[pivot_row], rows[found] = rows[found], rows[pivot_row]
        pivot = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot for value in rows[pivot_row]]
        for row in range(row_count):
            if row != pivot_row and rows[row][column]:
                factor = rows[row][column]
                rows[row] = [
                    rows[row][j] - factor * rows[pivot_row][j]
                    for j in range(column_count + 1)
                ]
        pivots.append(column)
        pivot_row += 1
    for row in rows:
        if not any(row[:-1]) and row[-1]:
            raise CertificateError("inconsistent exact linear system")
    if len(pivots) < column_count:
        raise CertificateError("exact linear system is not uniquely determined")
    result = [F(0)] * column_count
    for row, column in enumerate(pivots):
        result[column] = rows[row][-1]
    return tuple(result)


def chamber_system(lower: F, upper: F) -> dict[str, object]:
    width = (lower + upper) / 2
    cells = membership.atomic_cells(POINTS, width)
    constraint_matrix: list[tuple[F, ...]] = []
    rhs: list[F] = []
    states: list[tuple[int, ...]] = []
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        states.append(state)
        constraint_matrix.append(
            tuple(F((state[i] - state[j]) ** 2) for i, j in PAIRS)
            + tuple(F(sum(state[i] for i in support) ** 2) for support in SUPPORTS)
        )
        rhs.append(membership.quadratic(MATRIX, state))
    if len(cells) != 40:
        raise CertificateError("generic chamber does not have 40 complete cells")
    return {
        "cells": cells,
        "states": tuple(states),
        "A": tuple(constraint_matrix),
        "b": tuple(rhs),
    }


def aggregate_cost(support: Sequence[int], width: F) -> F:
    # Gamma_T(S)=|S|+2 sum rho_T(d), and 2 rho_T(d)=2-chi_T(d).
    return F(len(support)) + sum(
        (
            F(2) - physical.physical_root_cost(POINTS[j] - POINTS[i], width)
            for i, j in combinations(support, 2)
        ),
        F(0),
    )


def cost_vector(width: F) -> tuple[F, ...]:
    return tuple(
        physical.physical_root_cost(POINTS[j] - POINTS[i], width)
        for i, j in PAIRS
    ) + tuple(aggregate_cost(support, width) for support in SUPPORTS)


def demand_value(width: F) -> F:
    cells = membership.atomic_cells(POINTS, width)
    return sum(
        (
            F(cell["length"]) / (2 * width)
            * membership.quadratic(MATRIX, tuple(int(value) for value in cell["state"]))
            for cell in cells
            if cell["length"] != "infinite"
        ),
        F(0),
    )


def affine_coefficients(first_width: F, second_width: F, first: F, second: F) -> tuple[F, F]:
    if first_width == second_width:
        raise CertificateError("two distinct widths are required")
    beta = (first - second) / (1 / first_width - 1 / second_width)
    return first - beta / first_width, beta


def vector_from_seed(seed: Mapping[str, str]) -> tuple[F, ...]:
    vector = [F(0)] * len(VARIABLE_LABELS)
    for raw_index, raw_value in seed.items():
        index = int(raw_index)
        if not 0 <= index < len(vector) or vector[index]:
            raise CertificateError("invalid sparse primal seed")
        vector[index] = F(raw_value)
    if any(value < 0 for value in vector):
        raise CertificateError("negative sparse primal seed")
    return tuple(vector)


def dual_from_seed(
    pack: Mapping[str, object], width: F, seed: Mapping[str, object]
) -> tuple[tuple[F, ...], tuple[F, ...]]:
    matrix = pack["A"]
    rhs = pack["b"]
    row_indices = tuple(int(value) for value in seed["rows"])
    column_indices = tuple(int(value) for value in seed["columns"])
    if len(set(row_indices)) != len(row_indices) or len(set(column_indices)) != len(column_indices):
        raise CertificateError("duplicate dual support index")
    if any(not 0 <= row < len(matrix) for row in row_indices):
        raise CertificateError("dual row index out of range")
    if any(not 0 <= column < len(VARIABLE_LABELS) for column in column_indices):
        raise CertificateError("dual column index out of range")
    costs = cost_vector(width)
    values = rref_unique(
        tuple(tuple(matrix[row][column] for row in row_indices) for column in column_indices),
        tuple(costs[column] for column in column_indices),
    )
    if any(value <= 0 for value in values):
        raise CertificateError("listed dual support is not strictly positive")
    weights = [F(0)] * len(matrix)
    for row, value in zip(row_indices, values):
        weights[row] = value
    loads = tuple(
        sum((matrix[row][column] * weights[row] for row in range(len(matrix))), F(0))
        for column in range(len(VARIABLE_LABELS))
    )
    if any(loads[column] > costs[column] for column in range(len(costs))):
        raise CertificateError("dual endpoint is not feasible")
    return tuple(weights), loads


def affine_audit(
    lower: F,
    upper: F,
    vector: Sequence[F],
    seeded_alpha: F,
    seeded_beta: F,
    seeded_demand_alpha: F,
    seeded_demand_beta: F,
) -> tuple[F, F, F, F]:
    first_width = (2 * lower + upper) / 3
    second_width = (lower + 2 * upper) / 3
    first_objective = sum(
        (cost * value for cost, value in zip(cost_vector(first_width), vector)), F(0)
    )
    second_objective = sum(
        (cost * value for cost, value in zip(cost_vector(second_width), vector)), F(0)
    )
    alpha, beta = affine_coefficients(
        first_width, second_width, first_objective, second_objective
    )
    first_demand = demand_value(first_width)
    second_demand = demand_value(second_width)
    demand_alpha, demand_beta = affine_coefficients(
        first_width, second_width, first_demand, second_demand
    )
    if (alpha, beta, demand_alpha, demand_beta) != (
        seeded_alpha,
        seeded_beta,
        seeded_demand_alpha,
        seeded_demand_beta,
    ):
        raise CertificateError("seeded affine objective or demand changed")
    harmonic_width = 2 * lower * upper / (lower + upper)
    for column, (left_cost, right_cost) in enumerate(
        zip(cost_vector(lower), cost_vector(upper))
    ):
        if cost_vector(harmonic_width)[column] != (left_cost + right_cost) / 2:
            raise CertificateError("cost column is not affine in 1/T on a chamber")
    if demand_value(harmonic_width) != demand_alpha + demand_beta / harmonic_width:
        raise CertificateError("demand is not affine in 1/T on a chamber")
    return alpha, beta, demand_alpha, demand_beta


def primal_rows(pack: Mapping[str, object], vector: Sequence[F]) -> tuple[F, ...]:
    matrix = pack["A"]
    rhs = pack["b"]
    slacks = tuple(
        sum((row[column] * vector[column] for column in range(len(vector))), F(0)) - value
        for row, value in zip(matrix, rhs)
    )
    if any(slack < 0 for slack in slacks):
        raise CertificateError("parametric primal is not feasible on its event chamber")
    return slacks


def canonical_measure_audit(pack: Mapping[str, object], width: F) -> dict[str, object]:
    weights = tuple(
        F(0) if cell["length"] == "infinite" else F(cell["length"]) / (2 * width)
        for cell in pack["cells"]
    )
    loads = tuple(
        sum(
            (pack["A"][row][column] * weights[row] for row in range(len(weights))),
            F(0),
        )
        for column in range(len(VARIABLE_LABELS))
    )
    objective = sum(
        (weight * rhs for weight, rhs in zip(weights, pack["b"])), F(0)
    )
    if loads != cost_vector(width):
        raise CertificateError("canonical cell-length dual does not saturate every cost column")
    if objective != demand_value(width):
        raise CertificateError("canonical cell-length dual objective changed")
    return {
        "sample_T": ftext(width),
        "all_80_cost_columns_saturated": True,
        "objective_equals_signed_demand": ftext(objective),
    }


def dual_record(
    pack: Mapping[str, object],
    seed: Mapping[str, object],
    width: F,
    target: F,
) -> dict[str, object]:
    weights, loads = dual_from_seed(pack, width, seed)
    objective = sum((weight * value for weight, value in zip(weights, pack["b"])), F(0))
    if objective != target:
        raise CertificateError("endpoint dual has a nonzero exact gap")
    return {
        "T": ftext(width),
        "positive_cell_weights": [
            {
                "row": row,
                "state": list(pack["states"][row]),
                "weight": ftext(weight),
            }
            for row, weight in enumerate(weights)
            if weight
        ],
        "tight_cost_columns_used_to_recover_dual": [
            VARIABLE_LABELS[int(column)] for column in seed["columns"]
        ],
        "objective": ftext(objective),
        "all_80_cost_column_loads_feasible": all(
            load <= cost for load, cost in zip(loads, cost_vector(width))
        ),
    }


def build_parametric_audit() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    breakpoints = exact_breakpoints()
    if [ftext(value) for value in breakpoints] != SEED["breakpoints"]:
        raise CertificateError("event breakpoint seed changed")
    if len(breakpoints) != 23:
        raise CertificateError("event breakpoint count changed")
    event_records: list[dict[str, object]] = []
    piece_records: list[dict[str, object]] = []
    expected_piece_lower = PHASE_LOWER
    for event_index, (lower, upper, event_seed) in enumerate(
        zip(breakpoints, breakpoints[1:], SEED["events"])
    ):
        if (F(event_seed["lower"]), F(event_seed["upper"])) != (lower, upper):
            raise CertificateError("event chamber seed bounds changed")
        pack = chamber_system(lower, upper)
        event_piece_start = len(piece_records)
        local_lower = lower
        for piece_seed in event_seed["pieces"]:
            piece_lower = F(piece_seed["lower"])
            piece_upper = F(piece_seed["upper"])
            if piece_lower != local_lower or not piece_lower < piece_upper <= upper:
                raise CertificateError("optimality chambers do not tile an event chamber")
            local_lower = piece_upper
            if piece_lower != expected_piece_lower:
                raise CertificateError("optimality chambers do not tile the phase")
            expected_piece_lower = piece_upper
            vector = vector_from_seed(piece_seed["primal"])
            slacks = primal_rows(pack, vector)
            alpha, beta, demand_alpha, demand_beta = affine_audit(
                lower,
                upper,
                vector,
                F(piece_seed["objective_alpha"]),
                F(piece_seed["objective_beta"]),
                F(piece_seed["demand_alpha"]),
                F(piece_seed["demand_beta"]),
            )
            left_target = alpha + beta / piece_lower
            right_target = alpha + beta / piece_upper
            left_dual = dual_record(pack, piece_seed["left_dual"], piece_lower, left_target)
            right_dual = dual_record(pack, piece_seed["right_dual"], piece_upper, right_target)
            excess_alpha = alpha - demand_alpha
            excess_beta = beta - demand_beta
            left_excess = excess_alpha + excess_beta / piece_lower
            right_excess = excess_alpha + excess_beta / piece_upper
            if left_excess < 0 or right_excess < 0:
                raise CertificateError("optimal cover falls below the canonical demand dual")
            piece_records.append(
                {
                    "piece_index": len(piece_records),
                    "event_chamber_index": event_index,
                    "T_interval": {
                        "lower": ftext(piece_lower),
                        "upper": ftext(piece_upper),
                        "open_for_generic_cell_system": True,
                    },
                    "primal": {
                        "root_weights": {
                            VARIABLE_LABELS[index]: ftext(value)
                            for index, value in enumerate(vector[: len(PAIRS)])
                            if value
                        },
                        "kappas": {
                            VARIABLE_LABELS[index]: ftext(value)
                            for index, value in enumerate(vector[len(PAIRS) :], start=len(PAIRS))
                            if value
                        },
                        "feasible_on_every_cell_state_in_open_event_chamber": True,
                        "minimum_cell_slack": ftext(min(slacks)),
                    },
                    "optimal_value_formula": {
                        "form": "alpha+beta/T",
                        "alpha": ftext(alpha),
                        "beta": ftext(beta),
                    },
                    "signed_demand_formula": {
                        "form": "alpha+beta/T",
                        "alpha": ftext(demand_alpha),
                        "beta": ftext(demand_beta),
                    },
                    "cover_excess_formula": {
                        "form": "alpha+beta/T",
                        "alpha": ftext(excess_alpha),
                        "beta": ftext(excess_beta),
                        "nonnegative_at_both_endpoints_hence_throughout": True,
                    },
                    "left_limiting_dual": left_dual,
                    "right_limiting_dual": right_dual,
                    "optimality_transport": "affine interpolation of the two exact endpoint duals in x=1/T",
                    "zero_gap_for_every_T_in_open_piece": True,
                }
            )
        if local_lower != upper:
            raise CertificateError("event chamber seed has an uncovered tail")
        event_records.append(
            {
                "event_chamber_index": event_index,
                "T_interval": {"lower": ftext(lower), "upper": ftext(upper)},
                "generic_complete_real_line_cell_count": len(pack["states"]),
                "first_piece_index": event_piece_start,
                "piece_count": len(piece_records) - event_piece_start,
                "canonical_cell_length_dual": canonical_measure_audit(
                    pack, (lower + upper) / 2
                ),
            }
        )
    if expected_piece_lower != PHASE_UPPER or len(piece_records) != 30:
        raise CertificateError("phase is not tiled by exactly 30 optimality chambers")
    return event_records, piece_records


def old_transport_vector() -> tuple[F, ...]:
    weights = {
        (0, 2): F(45, 1792),
        (2, 4): F(11, 448),
        (4, 6): F(3, 1792),
        (10, 12): F(1, 128),
    }
    vector = [F(0)] * len(VARIABLE_LABELS)
    for edge, value in weights.items():
        vector[PAIRS.index(edge)] = value
    return tuple(vector)


def actual_breakpoint_audit(width: F, seed: Mapping[str, object]) -> dict[str, object]:
    cells = membership.atomic_cells(POINTS, width)
    matrix: list[tuple[F, ...]] = []
    rhs: list[F] = []
    states: list[tuple[int, ...]] = []
    for cell in cells:
        state = tuple(int(value) for value in cell["state"])
        states.append(state)
        matrix.append(
            tuple(F((state[i] - state[j]) ** 2) for i, j in PAIRS)
            + tuple(F(sum(state[i] for i in support) ** 2) for support in SUPPORTS)
        )
        rhs.append(membership.quadratic(MATRIX, state))
    pack = {"A": tuple(matrix), "b": tuple(rhs), "states": tuple(states)}
    vector = old_transport_vector()
    slacks = primal_rows(pack, vector)
    target = sum((cost * value for cost, value in zip(cost_vector(width), vector)), F(0))
    dual = dual_record(pack, seed["dual"], width, target)
    return {
        "T": ftext(width),
        "actual_complete_cell_count": len(cells),
        "primal_feasible": True,
        "minimum_slack": ftext(min(slacks)),
        "optimal_value": ftext(target),
        "exact_actual_cell_dual": dual,
        "zero_gap": True,
    }


def transport_audit(piece_records: Sequence[Mapping[str, object]]) -> dict[str, object]:
    roots = {
        "0,2": "45/1792",
        "2,4": "11/448",
        "4,6": "3/1792",
        "10,12": "1/128",
    }
    matching = [
        record
        for record in piece_records
        if record["primal"]["root_weights"] == roots
        and record["T_interval"] in (
            {"lower": "381/2", "upper": "216/1", "open_for_generic_cell_system": True},
            {"lower": "216/1", "upper": "220/1", "open_for_generic_cell_system": True},
        )
    ]
    if len(matching) != 2:
        raise CertificateError("two-chamber transported primal changed")
    actual = []
    for expected_width, seed in zip((F(216), F(220)), SEED["transport_actual_breakpoints"]):
        if F(seed["T"]) != expected_width:
            raise CertificateError("actual breakpoint transport seed changed")
        actual.append(actual_breakpoint_audit(expected_width, seed))
    failure_width = F(221)
    failure_cells = membership.atomic_cells(POINTS, failure_width)
    vector = old_transport_vector()
    rows = []
    for cell in failure_cells:
        state = tuple(int(value) for value in cell["state"])
        lhs = sum(
            (
                vector[index] * (state[i] - state[j]) ** 2
                for index, (i, j) in enumerate(PAIRS)
            ),
            F(0),
        )
        rhs = membership.quadratic(MATRIX, state)
        rows.append((lhs - rhs, cell, lhs, rhs))
    slack, cell, lhs, rhs = min(rows, key=lambda row: row[0])
    if (
        slack,
        cell["id"],
        tuple(cell["state"]),
        lhs,
        rhs,
    ) != (
        F(-5, 32),
        "[636,637)",
        (-1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        F(1, 8),
        F(9, 32),
    ):
        raise CertificateError("T=221 transported-primal failure changed")
    return {
        "same_primal_root_weights": roots,
        "same_primal_is_optimal_on_both_adjacent_open_event_chambers": True,
        "open_chambers": ["(381/2,216)", "(216,220)"],
        "actual_breakpoints": actual,
        "piecewise_dual_transport": "separate affine-in-1/T endpoint-dual interpolation on each event chamber",
        "no_single_fixed_dual_claim": True,
        "literal_fixed_primal_fails_beyond_transport_window": {
            "T": "221/1",
            "cell": cell["id"],
            "state": list(cell["state"]),
            "lhs": ftext(lhs),
            "rhs": ftext(rhs),
            "slack": ftext(slack),
        },
        "not_transportable_as_one_full_phase_fixed_optimum": True,
    }


def phase_integral_audit(piece_records: Sequence[Mapping[str, object]]) -> dict[str, object]:
    terms = []
    rational_part = F(0)
    for record in piece_records:
        lower = F(record["T_interval"]["lower"])
        upper = F(record["T_interval"]["upper"])
        alpha = F(record["cover_excess_formula"]["alpha"])
        beta = F(record["cover_excess_formula"]["beta"])
        rational_term = beta * (1 / lower - 1 / upper)
        rational_part += rational_term
        terms.append(
            {
                "T_interval": [ftext(lower), ftext(upper)],
                "log_ratio": ftext(upper / lower),
                "log_coefficient": ftext(alpha),
                "rational_term": ftext(rational_term),
            }
        )
    obstruction = next(
        record
        for record in piece_records
        if record["T_interval"]["lower"] == "381/2"
        and record["T_interval"]["upper"] == "216/1"
    )
    alpha = F(obstruction["cover_excess_formula"]["alpha"])
    beta = F(obstruction["cover_excess_formula"]["beta"])
    if (alpha, beta) != (F(-479, 1792), F(4169, 64)):
        raise CertificateError("obstruction chamber excess formula changed")
    lower = F(381, 2)
    upper = F(216)
    minimum_excess = alpha + beta / upper
    lower_bound = minimum_excess * (upper - lower) / upper
    exact_rational_term = beta * (1 / lower - 1 / upper)
    if (
        minimum_excess,
        lower_bound,
        upper / lower,
        exact_rational_term,
    ) != (
        F(3317, 96768),
        F(56389, 13934592),
        F(144, 127),
        F(70873, 1755648),
    ):
        raise CertificateError("phase obstruction arithmetic changed")
    if lower_bound <= 0:
        raise CertificateError("phase obstruction is not positive")
    return {
        "normalization": "ln(2)*integral_theta=integral_T dT/T for T=128*2^theta",
        "full_phase_exact_symbolic_sum": terms,
        "combined_rational_part": ftext(rational_part),
        "log_terms_are_not_claimed_rational": True,
        "pointwise_optimum_minus_signed_demand_is_nonnegative": True,
        "certified_positive_subinterval": {
            "T_interval": ["381/2", "216/1"],
            "excess_formula": "-479/1792+4169/(64T)",
            "minimum_excess": ftext(minimum_excess),
            "exact_integral_expression": "-479/1792*ln(144/127)+70873/1755648",
            "rational_lower_bound": ftext(lower_bound),
        },
        "full_phase_integrated_cover_excess_at_least": ftext(lower_bound),
        "zero_telescoping_on_this_fixture_is_impossible": True,
    }


def payload_hash(certificate: Mapping[str, object]) -> str:
    payload = copy.deepcopy(dict(certificate))
    payload.pop("integrity", None)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_certificate() -> dict[str, object]:
    if tuple(FULL_POINTS) != membership.FULL_TWO_EPOCH_POINTS:
        raise CertificateError("fixed Golomb history changed")
    differences = membership.positive_differences(FULL_POINTS)
    if len(differences) != 120:
        raise CertificateError("fixed 16-mark history is not Golomb")
    events, pieces = build_parametric_audit()
    certificate: dict[str, object] = {
        "schema": SCHEMA,
        "status": STATUS,
        "fixture": {
            "single_fixed_history": "a_k=k(k+100), 0<=k<=15",
            "full_points": list(FULL_POINTS),
            "all_120_positive_differences_distinct": True,
            "joint_union_points_a3_through_a15": list(POINTS),
            "epochs": [4, 8],
            "supports": [list(SUPPORT4), list(SUPPORT8)],
            "shared_endpoint": 749,
            "mu_each": "1/1",
            "dyadic_phase": {"T_lower": "128/1", "T_upper": "256/1"},
            "not_a_changing_family": True,
        },
        "chamber_theorem": {
            "event_breakpoint_rule": "T=d or T=d/2 for a positive union-point difference d",
            "event_breakpoints": [ftext(value) for value in exact_breakpoints()],
            "open_event_chamber_count": len(events),
            "open_optimality_chamber_count": len(pieces),
            "event_chambers": events,
            "optimality_chambers": pieces,
            "breakpoint_values_have_measure_zero_in_phase_integration": True,
            "actual_breakpoint_optima_certified_separately_only_at_T_216_and_T_220": True,
        },
        "transport": transport_audit(pieces),
        "phase_integrated_cover_excess": phase_integral_audit(pieces),
        "scope": {
            "proved": [
                "the complete open-chamber, hence phase-almost-everywhere, 22-event-chamber and 30-optimality-chamber exact LP description on the stated fixed finite history and T phase",
                "piecewise constant exact optimal primals with affine-in-1/T endpoint-dual transport",
                "a local optimal primal transported across T=216 and a literal failure at T=221",
                "a strictly positive exact rational lower obstruction for the full phase-integrated optimal cover excess",
            ],
            "not_proved": [
                "a compatible infinite Sidon history",
                "a uniform theorem over arbitrary finite Golomb histories",
                "the isolated actual LP optima at event breakpoints other than the separately checked T=216 and T=220",
                "a telescoping upper bound or a paid universal ledger",
                "payment by Gothic, birth, phase, terminal, final, cross-scale, or external reserve rows",
                "C058, Q1, Q2, Erdos Problem 1191, novelty, publication, or prize eligibility",
            ],
            "root_SDDM_plus_two_J_class_only": True,
            "budget_owner_supplied": False,
            "same_scale_only": True,
        },
    }
    certificate["integrity"] = {
        "canonical_json": True,
        "payload_sha256": payload_hash(certificate),
    }
    return certificate


def rendered_bytes(certificate: Mapping[str, object]) -> bytes:
    return (json.dumps(certificate, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def validate_certificate(
    certificate: Mapping[str, object], expected: Mapping[str, object] | None = None
) -> None:
    if expected is None:
        expected = build_certificate()
    if dict(certificate) != expected:
        raise CertificateError("semantic replay mismatch")
    integrity = certificate.get("integrity")
    if not isinstance(integrity, Mapping) or integrity.get("payload_sha256") != payload_hash(certificate):
        raise CertificateError("payload hash mismatch")


def self_check() -> int:
    expected = build_certificate()
    mutations = []
    for mutate in (
        lambda c: c["fixture"]["full_points"].__setitem__(4, 750),
        lambda c: c["chamber_theorem"]["event_breakpoints"].__setitem__(1, "130/1"),
        lambda c: c["chamber_theorem"]["optimality_chambers"][0]["primal"]["root_weights"].__setitem__("0,2", "1/1"),
        lambda c: c["chamber_theorem"]["optimality_chambers"][0]["optimal_value_formula"].__setitem__("alpha", "0/1"),
        lambda c: c["chamber_theorem"]["optimality_chambers"][0]["left_limiting_dual"]["positive_cell_weights"][0].__setitem__("weight", "0/1"),
        lambda c: c["chamber_theorem"]["optimality_chambers"][5]["signed_demand_formula"].__setitem__("beta", "0/1"),
        lambda c: c["transport"]["literal_fixed_primal_fails_beyond_transport_window"].__setitem__("slack", "0/1"),
        lambda c: c["phase_integrated_cover_excess"]["certified_positive_subinterval"].__setitem__("rational_lower_bound", "0/1"),
        lambda c: c["phase_integrated_cover_excess"].__setitem__("zero_telescoping_on_this_fixture_is_impossible", False),
        lambda c: c["scope"].__setitem__("budget_owner_supplied", True),
        lambda c: c["scope"]["not_proved"].remove("C058, Q1, Q2, Erdos Problem 1191, novelty, publication, or prize eligibility"),
        lambda c: c["integrity"].__setitem__("payload_sha256", "0" * 64),
    ):
        candidate = copy.deepcopy(expected)
        mutate(candidate)
        mutations.append(candidate)
    rejected = 0
    for candidate in mutations:
        try:
            validate_certificate(candidate, expected)
        except CertificateError:
            rejected += 1
    if rejected != len(mutations):
        raise CertificateError("not every semantic mutation was rejected")
    return rejected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, help="write the deterministic certificate")
    parser.add_argument("--verify", type=Path, help="verify a certificate")
    parser.add_argument("--self-check", action="store_true", help="run semantic mutation checks")
    args = parser.parse_args()
    built = build_certificate()
    if args.write:
        args.write.write_bytes(rendered_bytes(built))
    if args.verify:
        raw = args.verify.read_bytes()
        loaded = json.loads(raw)
        validate_certificate(loaded)
        if raw != rendered_bytes(built):
            raise CertificateError("literal raw-byte replay mismatch")
    if args.self_check:
        self_check()
    if not args.write and not args.verify and not args.self_check:
        print(rendered_bytes(built).decode("utf-8"), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Bounded floating search followed by exact integer witness checks, if found.

This search concerns general centered rank-one PSD corrections, not the
selected low-frequency Fourier carrier. A failed search proves nothing.
"""
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import json
import math
import random
import time

P = [1, 2, 4, 8, 13, 21, 37, 47, 62, 84, 102, 132, 174, 201, 252, 280, 336]
p = len(P)
birth = {P[j] - P[i]: j + 1 for i in range(p) for j in range(i + 1, p)}
assert len(birth) == p * (p - 1) // 2
ss = [x + y for x, y in combinations_with_replacement(P, 2)]
assert len(ss) == len(set(ss))
F, q = sorted(birth), len(birth)
E, Hist = [], []
for i, j in combinations(range(q), 2):
    d, e = F[i], F[j]
    t = e - d
    if t not in birth:
        E.append((i, j))
    if t not in birth or birth[t] > max(birth[d], birth[e]):
        Hist.append((i, j))

def center(v):
    m = sum(v) / q
    return [x - m for x in v]

def adj(v, edges):
    out = [0.0] * q
    for i, j in edges:
        out[i] += v[j]
        out[j] += v[i]
    return out

def quads(v):
    S = sum(x * x for x in v)
    B = -2 * sum(v[i] * v[j] for i, j in E) - p * S
    C = 2 * sum(v[i] * v[j] for i, j in Hist)
    return B, C, S

start = time.monotonic()
rows, witness = [], None
grid = [0.0] + [2.0 ** (j / 4) for j in range(-20, 25)]
for sample, lam in enumerate(grid):
    rng = random.Random(1191000 + sample)
    v = center([rng.uniform(-1, 1) for _ in F])
    shift = q * (1 + lam) + p
    for it in range(260):
        av, cv = adj(v, E), adj(v, Hist)
        w = center([(shift - p) * v[i] - av[i] + lam * cv[i] for i in range(q)])
        norm = math.sqrt(sum(x * x for x in w))
        v = [x / norm for x in w]
    B, C, S = quads(v)
    rows.append({"lambda": lam, "B_float": B, "C_float": C})
    if B > 1e-6 and C > 1e-6:
        ints = [round(1000000 * x) for x in v]
        total = sum(ints)
        ints = [q * x - total for x in ints]
        assert sum(ints) == 0
        Bi, Ci, Si = quads(ints)
        assert isinstance(Bi, int) and isinstance(Ci, int)
        if Bi > 0 and Ci > 0:
            witness = {"integer_vector": ints, "exact_B": str(Bi),
                       "exact_C": str(Ci), "exact_S": str(Si)}
            break

report = {"status": "EXACT_PSD_COUNTEREXAMPLE" if witness else "BOUNDED_SEARCH_NO_WITNESS",
    "scope": "One finite 17-point Sidon history; general centered PSD residual, not the selected Fourier residual",
    "P": P, "F": F, "p": p, "q": q, "iterations_per_parameter": 260,
    "grid": grid, "completed_parameter_results": rows, "witness": witness,
    "wall_seconds_display_only": time.monotonic() - start,
    "not_claimed": ["fixed-cap counterexample", "Q1 closure", "Fourier-specific no-go"]}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({"status": report['status'], "completed_parameters": len(rows),
    "witness_found": witness is not None, "report": str(out),
    "seconds": report['wall_seconds_display_only']}, indent=2))

#!/usr/bin/env python3
"""One exact historical-envelope check. No floating-point inference."""
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import hashlib
import json

Q = Fraction
P = [1, 2, 4, 8, 13, 21, 37, 47, 62, 84, 102, 132, 174, 201, 252, 280, 336]
p = len(P)
ss = [x + y for x, y in combinations_with_replacement(P, 2)]
assert len(ss) == len(set(ss))
birth = {}
banks = [set()]
for n in range(1, p + 1):
    new = {P[n - 1] - x for x in P[:n - 1]}
    assert len(new) == n - 1 and not (new & set(birth))
    birth.update({d: n for d in new})
    banks.append(set(birth))
F = sorted(birth)
q = len(F)
H = P[-1] - P[0]
r = p // 8
central_D = P[p - r - 1] - P[r]
assert q == p * (p - 1) // 2

# Same rational phase as the separately recorded centered Fourier example.
b = 2 * central_D
re, im, h = b * b - 1, 2 * b, b * b + 1
assert re * re + im * im == h * h
powers = [(1, 0)]
for n in range(H):
    x, y = powers[-1]
    powers.append((x * re - y * im, x * im + y * re))
common = h ** H
unit = {d: (powers[d][0] * h ** (H - d),
            powers[d][1] * h ** (H - d)) for d in range(H + 1)}
mu_num = (sum(unit[d][0] for d in F), sum(unit[d][1] for d in F))
z = {d: (q * unit[d][0] - mu_num[0],
         q * unit[d][1] - mu_num[1]) for d in F}
zden = q * common
gram_den = zden ** 2
assert sum(x for x, y in z.values()) == sum(y for x, y in z.values()) == 0

def dot(d, e):
    return z[d][0] * z[e][0] + z[d][1] * z[e][1]

S = sum(dot(d, d) for d in F)
assert Q(1, 24576) <= Q(S, q * gram_den) <= 1
old_R = old_J = ret_R = ret_J = mate_R = 0
dead_R = dead_J = live_R = live_J = 0
step_ret = [0] * (p + 1)
step_dead = [0] * (p + 1)
for d, e in combinations(F, 2):
    t, w = e - d, dot(d, e)
    assert -4 * gram_den <= w <= 4 * gram_den
    born_pair = max(birth[d], birth[e])
    if t in birth:
        old_J += 1
        old_R += w
    if t in birth and birth[t] > born_pair:
        ret_J += 1
        ret_R += w
        mate_R += dot(t, e)
        step_ret[birth[t]] += w
        assert max(birth[t], birth[e]) == birth[t]
        assert birth[d] < birth[t] and e - t == d
        # Exact Fourier potential difference, on a common denominator.
        hdiff_num = ((q * common + mu_num[0]) * (unit[t][0] - unit[d][0])
                     + mu_num[1] * (unit[t][1] - unit[d][1]))
        assert w - dot(t, e) == q * hdiff_num
    if t in birth and birth[t] <= born_pair:
        dead_J += 1
        dead_R += w
        step_dead[born_pair] += w
    else:
        live_J += 1
        live_R += w

assert old_J == ret_J + dead_J
assert old_R == ret_R + dead_R
assert 2 * sum(dot(d, e) for d, e in combinations(F, 2)) == -S
assert 2 * live_R == -S - 2 * dead_R
assert old_J >= 2 * ret_J
assert live_J == q * (q - 1) // 2 - dead_J

# Independently compute fibre maxima from the actual nonnegative W.
max_num = {t: 0 for t in range(1, H)}
prefix_records = []
for n in range(1, p + 1):
    Fn = banks[n]
    kn = {}
    for d, e in combinations(sorted(Fn), 2):
        t = e - d
        kn[t] = kn.get(t, 0) + 8 * gram_den + dot(d, e)
    for t, val in kn.items():
        assert val >= 0
        if t not in Fn:
            max_num[t] = max(max_num[t], val)
    sx = sum(z[d][0] for d in Fn)
    sy = sum(z[d][1] for d in Fn)
    M_extra_num = sx * sx + sy * sy
    assert sum(dot(d, e) for d in Fn for e in Fn) == M_extra_num
    prefix_records.append({"n": n, "q_n": len(Fn),
        "mass_extra_display_only": float(Q(M_extra_num, 8 * gram_den))})
assert sum(max_num.values()) == 8 * gram_den * live_J + live_R

row_capacity_gain = Q(S + 2 * old_R, 16 * gram_den)
row_gap_gain = Q(2 * old_R - (p - 1) * S, 16 * gram_den)
historical_capacity_gain = -Q(live_R, 8 * gram_den)
retirement_correction = Q(ret_R, 8 * gram_den)
assert historical_capacity_gain == row_capacity_gain - retirement_correction
assert row_gap_gain > 0

def exact(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator),
            "decimal_display_only": float(x)}

report = {
    "status": "EXACT_FINITE_CHECK_PASS_Q1_UNRESOLVED",
    "points": P, "p": p, "q": q, "H": H, "central_D": central_D,
    "phase": "theta=2 arctan(1/(2 central_D))",
    "phase_variance": exact(Q(S, q * gram_den)),
    "uniform_old_mask": old_J, "uniform_retirement": ret_J,
    "uniform_dead_birth": dead_J, "uniform_historical_capacity": live_J,
    "row_gap_gain_m_equals_p": exact(row_gap_gain),
    "row_capacity_gain": exact(row_capacity_gain),
    "retirement_residual_correction": exact(retirement_correction),
    "historical_capacity_gain": exact(historical_capacity_gain),
    "weighted_injection_imbalance": exact(Q(ret_R - mate_R, 8 * gram_den)),
    "prefix_masses": prefix_records,
    "not_claimed": ["fixed-cap all-history counterexample", "Q1 closure", "Lean proof"]
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({"status": report["status"], "p": p, "q": q,
    "row_gap_gain_display_only": float(row_gap_gain),
    "row_capacity_gain_display_only": float(row_capacity_gain),
    "historical_capacity_gain_display_only": float(historical_capacity_gain),
    "retirement_correction_display_only": float(retirement_correction),
    "exact_report": str(out), "exact_report_sha256": hashlib.sha256(out.read_bytes()).hexdigest()
}, indent=2))

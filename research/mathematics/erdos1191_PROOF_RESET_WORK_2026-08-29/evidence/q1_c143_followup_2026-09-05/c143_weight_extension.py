#!/usr/bin/env python3
"""Exact consequences of the hash-pinned C143 pilot, independent of solver code.

This verifies demand/margin identities and weight transfer, not full-root
optimality. The latter has its own independent oracle replay.
"""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
BANK = Path('/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/runs/pilot_s32_n16_r1/C143_BANK.json')
EXPECTED_SHA = 'd680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4'


def point_matrix_integer(e):
    # 8 e^2 M = D^T (8 e^2 B) D. Zero diagonal follows from B's zero
    # diagonal AND zero first off-diagonal; both are retained here.
    m = [[0] * (e + 1) for _ in range(e + 1)]
    for i in range(e):
        for j in range(e):
            b = -(i-j)**2 if abs(i-j) >= 2 else 0
            m[i][j] += b
            m[i][j+1] -= b
            m[i+1][j] -= b
            m[i+1][j+1] += b
    assert all(m[i][i] == 0 and sum(m[i]) == 0 for i in range(e+1))
    return m


def demand_affine(points, e, left, right):
    """(intercept,slope) of integrated unweighted epoch demand.

    Haar autocorrelation is 2W-3d (0<=d<=W), d-2W (W<=d<=2W),
    zero otherwise. The amplitude and direct normalization give 1/m
    times M_ij times this autocorrelation for each unordered pair.
    """
    origins = points[e-1:2*e]
    matrix = point_matrix_integer(e)
    s = (left+right)/2
    intercept = slope = F(0)
    for m in (1, 2, 4, 8):
        for i in range(e+1):
            for j in range(i+1, e+1):
                a = F(matrix[i][j], 8*e*e*m)
                if not a:
                    continue
                d = origins[j]-origins[i]
                assert not left < F(d,m) < right
                assert not left < F(d,2*m) < right
                if d <= m*s:
                    intercept -= 3*a*d
                    slope += 2*a*m
                elif d <= 2*m*s:
                    intercept += a*d
                    slope -= 2*a*m
    return intercept, slope


def evaluate(affine, phase):
    return affine[0]+affine[1]*phase


def direct_cell_integral(points, e, t):
    """Independent half-open Haar cell integration, used to check pair formula."""
    origins = points[e-1:2*e]
    total = F(0)
    for m in (1, 2, 4, 8):
        w = m*t
        events = sorted({a+k*w for a in origins for k in (0,1,2)})
        for l,r in zip(events, events[1:]):
            x = (l+r)/2
            q = [(8//m)*(int(a<=x<a+w)-int(a+w<=x<a+2*w)) for a in origins]
            d = [(i,q[i]-q[i+1]) for i in range(e) if q[i] != q[i+1]]
            bval = sum(-(i-j)**2*di*dj for i,di in d for j,dj in d if abs(i-j)>=2)
            total += (r-l)*F(m*bval, 128*8*e*e)
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bank', type=Path, default=BANK)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    raw = args.bank.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == EXPECTED_SHA
    b = json.loads(raw)
    assert b['case_id'] == 'n16-contract-s32-r1' and F(b['new_weight']) == 1
    n, points = b['n'], b['points']
    diffs = [points[j]-points[i] for i in range(len(points)) for j in range(i+1,len(points))]
    assert len(diffs) == len(set(diffs)) == 2016
    parents = {}
    for p in b['geometry_parents']:
        l,r = F(p['left']),F(p['right'])
        parents[p['parent_id']] = (demand_affine(points,n,l,r),demand_affine(points,2*n,l,r))
    checks = []
    checked_affine_identities = 0
    for child in b['children']:
        old,new = parents[child['parent_id']]
        ma = child['margin_affine']
        margin = F(ma['intercept']),F(ma['slope'])
        pa = child['basis']['primal_objective']
        price = F(pa['intercept']),F(pa['slope'])
        assert all(2*(old[i]+new[i])-price[i] == margin[i] for i in (0,1))
        checked_affine_identities += 1
        for end in ('left','right'):
            t = F(child[end])
            checks.append((evaluate(margin,t),evaluate(new,t),t,child['child_id']))
    for ep in b['geometry_endpoints']:
        t = F(ep['phase'])
        old,new = demand_affine(points,n,t,t),demand_affine(points,2*n,t,t)
        assert evaluate(old,t)+evaluate(new,t) == F(ep['D_exact'])
        checks.append((F(ep['margin']),evaluate(new,t),t,ep['endpoint_id']))
    # Every transferred support remains feasible for 0<rho<=1 because the
    # old graph already covers max(d,0), which dominates max(rho*d,0).
    assert all(margin > 0 for margin,_,_,_ in checks)
    loss_budget, controlling = min((margin/(2*dn), label) for margin,dn,_,label in checks if dn>0)
    # A strict rational choice, expressed as a simple hundredth if possible.
    for denom in (100,1000,10000,100000,1000000):
        integer_loss = int(loss_budget*denom)
        if integer_loss:
            delta = F(integer_loss,denom)
            if delta == loss_budget:
                delta -= F(1,denom)
            if delta > 0:
                break
    assert 0 < delta < loss_budget
    rho = 1-delta
    transferred = [(margin-2*delta*dn,t,label) for margin,dn,t,label in checks]
    min_margin,t_at_min,label_at_min = min(transferred)
    min_normalized = min(margin/t for margin,t,_ in transferred)
    assert min_margin > 0 and min_normalized > 0
    # A coarse exact integration bound needs no logarithmic transcendental:
    # integral_L^(2L) M/t^2 >= min(M)/(2L).
    phase_left = F(b['children'][0]['left'])
    integral_floor = min_margin/(2*phase_left)
    fejer_m = 1
    while F(fejer_m*fejer_m,(fejer_m+1)**2) < rho:
        fejer_m += 1
    samples = [phase_left,2*phase_left,F(300),F(400),F(500)]
    for t in samples:
        for e in (n,2*n):
            assert direct_cell_integral(points,e,t) == evaluate(demand_affine(points,e,t,t),t)
    certified_lower,certified_upper = F(b['integral']['lower']),F(b['integral']['upper'])
    assert F(4694333,10**8) < certified_lower < certified_upper < F(4694335,10**8)
    result = {
        'status':'EXACT_FIXED_HISTORY_WEIGHT_EXTENSION_OK',
        'bank_sha256':sha,'bank_bytes':len(raw),'case_id':b['case_id'],
        'distinct_positive_differences':len(diffs),
        'parents':len(parents),'child_affine_demand_identities':checked_affine_identities,
        'collapsed_endpoint_demand_identities':len(b['geometry_endpoints']),
        'half_open_cell_crosschecks':2*len(samples),
        'phase':[str(phase_left),str(2*phase_left)],
        'original_min_margin':str(min(margin for margin,_,_,_ in checks)),
        'original_min_normalized_margin':str(min(margin/t for margin,_,t,_ in checks)),
        'original_integral_strict_rational_fences':['4694333/100000000','4694335/100000000'],
        'max_allowable_weight_loss_for_nonnegative_margin':str(loss_budget),
        'controlling_certificate':controlling,
        'transferred_weight_interval':[str(rho),'1'],
        'transferred_min_margin':str(min_margin),
        'transferred_min_phase':str(t_at_min),'transferred_min_certificate':label_at_min,
        'transferred_min_normalized_margin':str(min_normalized),
        'transferred_integral_lower_bound':str(integral_floor),
        'fejer_ratio_convention':'rho=m^2/(m+1)^2',
        'minimum_fejer_m':fejer_m,
        'proof_dependencies':['C143 independent primal gate replay','No new dual optimality claim for rho<1'],
        'scope':{'fixed_64_mark_history_only':True,'conditional_on_bank_primal_verification':True,
                 'all_histories':False,'all_ranks':False,'global_owner_payment':False,'Q1_resolved':False}
    }
    text = json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text,end='')


if __name__ == '__main__':
    main()

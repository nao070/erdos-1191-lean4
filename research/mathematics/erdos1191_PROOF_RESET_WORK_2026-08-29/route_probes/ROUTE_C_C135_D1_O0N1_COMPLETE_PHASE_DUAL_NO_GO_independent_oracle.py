#!/usr/bin/env python3
"""Independent exact replay of the canonical C135 O0N1 source banks.

This oracle does not import the C135 verifier. It independently reconstructs
the fixture, parent and refined partitions, exact dual objectives, endpoint
positive-definiteness, complete-phase log integral, target, and separator.
"""
from __future__ import annotations

import copy
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / 'ROUTE_C_C135_D1_O0N1_COMPLETE_PHASE_DUAL_NO_GO_source.json'
PARENT = HERE / 'ROUTE_C_C135_D1_O0N1_ONE_DUAL_PER_CHAMBER_parent_source.json'
ROUTE = Path('/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/route_probes')
sys.path.insert(0, str(ROUTE))
import ROUTE_C_C126_COMMON_COMPLETED_SHELL_PHASE_certificate as c126

EXPECTED_ARTIFACT_SHA = '2949602baa0cb68aa3131bcb003fa2ac35156743bb2202e9a02f906ccf960c6b'
EXPECTED_PARENT_SHA = '93efb6b9846800f4025d72bd79536cc052f46f750e706b2966efa90928002912'
EXPECTED_INTERNAL_SHA = '8c19def256d58813a22220d80fe1ec96fcd5da1a3cb580381e5fee70fb38310d'
EXPECTED_PARENT_INTERNAL_SHA = '325d1c4e5556ab654a21c698583628478e750c61859622140a414ac0228aac43'
PREFIX = (22, 38, 23)
OLD = (71, 130, 210, 19)
NEW_CANONICAL = (62, 45, 91, 66, 103, 109, 111, 69)
NEW_O0N1 = NEW_CANONICAL[1:] + NEW_CANONICAL[:1]
RHO = F(9, 16)
TERMS = 30


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def obj_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()


def need(condition: bool, label: str) -> None:
    if not condition:
        raise RuntimeError('INDEPENDENT_ORACLE_FAIL: ' + label)


def log_interval(x: F, terms: int = TERMS) -> tuple[F, F]:
    need(x >= 1, 'log input')
    z = (x - 1) / (x + 1)
    lower = 2 * sum((z ** (2*k+1) / (2*k+1) for k in range(terms)), F())
    tail = 2 * z ** (2*terms+1) / ((2*terms+1) * (1-z*z))
    return lower, lower + tail


def variation(gaps: tuple[int, ...]) -> F:
    return F(1) - F(sum(gaps) ** 2, len(gaps) * sum(g*g for g in gaps))


def vrt(gaps: tuple[int, ...]) -> F:
    n = len(gaps)
    L = n.bit_length() - 1
    need(n == 2**L, 'dyadic Vrt length')
    total = sum(gaps)
    crt = sum((F(sum(gaps[-2**ell:]), total) for ell in range(L)), F()) / L - F(n-1, n*L)
    return (8*crt + 3) / 11


def grid_floor(x: F, d: int) -> F:
    return F((x*d).numerator // (x*d).denominator, d)


def grid_ceil(x: F, d: int) -> F:
    y=x*d
    return F(-((-y.numerator)//y.denominator), d)


def main() -> None:
    need(sha(ARTIFACT) == EXPECTED_ARTIFACT_SHA, 'refined outer sha256')
    need(sha(PARENT) == EXPECTED_PARENT_SHA, 'parent outer sha256')
    payload = json.loads(ARTIFACT.read_text())
    parent_payload = json.loads(PARENT.read_text())
    clone = copy.deepcopy(payload)
    embedded_internal = clone.pop('payload_sha256_without_hash')
    calculated_internal = obj_sha(clone)
    need(embedded_internal == calculated_internal == EXPECTED_INTERNAL_SHA, 'refined internal sha256')
    parent_clone = copy.deepcopy(parent_payload)
    parent_internal = parent_clone.pop('payload_sha256_without_hash')
    need(
        parent_internal == obj_sha(parent_clone) == EXPECTED_PARENT_INTERNAL_SHA,
        'parent internal sha256',
    )

    need(payload['schema'] == 'erdos1191.d1.o0n1.refined_complete_phase_dual.scratch.v1', 'refined schema')
    need(payload['scope'] == 'scratch-only exact falsification search; no canonical claim', 'refined source scope')
    need(payload['rotation'] == [0, 1], 'rotation')
    need(payload['uniform_subdivision_factor'] == 4, 'subdivision factor')
    need(payload['parent_sha256'] == EXPECTED_PARENT_SHA, 'parent link')

    gaps = PREFIX + OLD + NEW_O0N1
    points = [0]
    for g in gaps:
        points.append(points[-1] + g)
    points = tuple(points)
    need(tuple(payload['points']) == points, 'stored points')
    need(points == (0,22,60,83,154,284,494,513,558,649,715,818,927,1038,1107,1169), 'reconstructed points')

    witnesses = {}
    for i in range(16):
        for j in range(i+1,16):
            d=points[j]-points[i]
            need(d > 0, 'positive difference')
            if d in witnesses:
                raise RuntimeError(('INDEPENDENT_ORACLE_FAIL: Golomb collision',d,witnesses[d],(i,j)))
            witnesses[d]=(i,j)
    need(len(witnesses) == math.comb(16,2) == 120, 'Golomb census')
    need(points[7]-points[3] == 430 and points[15]-points[7] == 656, 'H2/H3')

    delta_v = variation(NEW_O0N1) - variation(OLD)
    delta_vrt = vrt(NEW_O0N1) - vrt(OLD)
    need(delta_v == -F(443_620_417,1_928_247_678), 'Delta V')
    need(delta_vrt == F(5034,96965), 'Delta Vrt')

    log_eta_lo, log_eta_hi = log_interval(F(215,82))
    rational = F(1,1000) + F(1,2)*abs(delta_v) - F(1,10)*delta_vrt
    target = ((rational + F(1,1000)*log_eta_lo)/3,
              (rational + F(1,1000)*log_eta_hi)/3)
    need(F(0) < target[0] <= target[1], 'target interval')

    model = c126._load_model(points, 'independent_o0n1_replay')
    canonical = model._breakpoints()
    need(canonical[0] == F(82) and canonical[-1] == F(164) and len(canonical) == 135, 'parent partition')

    # Replay the earlier stored one-dual-per-parent-chamber bank independently.
    need(parent_payload['schema'] == 'erdos1191.c058_eta_negative_full_phase_dual.discovery.v1', 'parent schema')
    need(parent_payload['scope'] == 'temporary exploratory exact replay; not canonical or registered', 'parent source scope')
    need(tuple(parent_payload['points']) == points, 'parent points')
    need(parent_payload['base'] == '82/1' and F(parent_payload['rho']) == RHO, 'parent phase/rho')
    need(parent_payload['H2'] == 430 and parent_payload['H3'] == 656, 'parent H2/H3')
    need(tuple(F(x) for x in parent_payload['breakpoints']) == tuple(canonical), 'parent breakpoints')
    parent_records = parent_payload['records']
    need(type(parent_records) is list and len(parent_records) == 134, 'parent records')
    parent_raw_lo=F(); parent_raw_hi=F(); parent_pd=0
    for gi,(record,left,right) in enumerate(zip(parent_records,canonical,canonical[1:])):
        need(set(record) == {'index','left','right','Dc4','Do4','Dc8','Do8','n4','n8'}, 'parent record keys')
        need(type(record['index']) is int and record['index'] == gi, 'parent record index')
        need(F(record['left']) == left and F(record['right']) == right, 'parent record interval')
        objectives={}
        for epoch in (4,8):
            dual=record[f'n{epoch}']
            need(set(dual) == {'alpha','denominator','float_objective','min_pivot_left','min_pivot_right','objective','status','support','weights'}, 'parent dual keys')
            den=dual['denominator']; weights=dual['weights']
            need(type(den) is int and den > 0, 'parent denominator')
            need(type(weights) is list and len(weights) == 308, 'parent weight count')
            need(all(type(w) is int and w >= 0 for w in weights), 'parent weights')
            hc,ho,weighted,dc,do,objective=model._dual_epoch_reconstruction(left,right,epoch,den,tuple(weights))
            need(dc == F(record[f'Dc{epoch}']) and do == F(record[f'Do{epoch}']), 'parent scalars')
            need(objective == F(dual['objective']), 'parent objective')
            objectives[epoch]=objective
            for endpoint in (left,right):
                need(model._bareiss_positive_definite(model._integer_slack(hc,ho,weighted,den,endpoint)), 'parent endpoint PD')
                parent_pd += 1
        a=2*(F(record['Dc4'])+RHO*F(record['Dc8']))-(objectives[4]+RHO*objectives[8])
        b=2*(F(record['Do4'])+RHO*F(record['Do8']))
        ll,lu=log_interval(right/left)
        reciprocal=b*(F(1,left)-F(1,right))
        if a >= 0:
            plo,phi=a*ll+reciprocal,a*lu+reciprocal
        else:
            plo,phi=a*lu+reciprocal,a*ll+reciprocal
        parent_raw_lo += plo; parent_raw_hi += phi
    log2_lo,log2_hi=log_interval(F(2))
    parent_corners=(parent_raw_lo/log2_lo,parent_raw_lo/log2_hi,parent_raw_hi/log2_lo,parent_raw_hi/log2_hi)
    parent_normalized=(min(parent_corners),max(parent_corners))
    parent_gap=parent_normalized[0]-target[1]
    need(F(1887,10**6) < parent_gap < F(1888,10**6), 'parent NO_SEPARATION gap')
    need(parent_pd == 536, 'parent endpoint PD census')

    selected = payload['selected_parent_chambers']
    need(selected == sorted(set(selected)) and len(selected) == 60, 'selected census/order')
    need(all(type(i) is int and 0 <= i < 134 for i in selected), 'selected index types/range')
    selected_set=set(selected)

    expected=[]
    for pi,(left,right) in enumerate(zip(canonical,canonical[1:])):
        factor=4 if pi in selected_set else 1
        for si in range(factor):
            expected.append((pi,si,left+(right-left)*si/factor,left+(right-left)*(si+1)/factor))
    records=payload['records']
    need(len(expected) == len(records) == 314, 'refined partition census')
    need(expected[0][2] == F(82) and expected[-1][3] == F(164), 'refined endpoints')
    need(all(expected[i][3] == expected[i+1][2] for i in range(len(expected)-1)), 'refined coverage')

    raw_lo=F(); raw_hi=F(); endpoint_checks=0; epoch_duals=0; weight_count=0
    denominators=set(); support=[]; improved=0
    last_right=None
    for gi,(record,(pi,si,left,right)) in enumerate(zip(records,expected)):
        need(set(record) == {'index','parent_index','sub_index','left','right','Dc4','Do4','Dc8','Do8','n4','n8'}, 'refined record keys')
        need(type(record['index']) is int and type(record['parent_index']) is int and type(record['sub_index']) is int, 'refined integer indices')
        need(record['index'] == gi and record['parent_index'] == pi and record['sub_index'] == si, 'refined indices')
        need(F(record['left']) == left and F(record['right']) == right and left < right, 'refined interval')
        if last_right is not None:
            need(last_right == left, 'refined adjacency')
        last_right=right
        objectives={}
        for epoch in (4,8):
            dual=record[f'n{epoch}']
            required={'alpha','denominator','fallback','float_objective','improvement_over_parent','objective','status','weights'}
            need(required <= set(dual) <= required | {'min_pivot_left','min_pivot_right','support'}, 'dual keys')
            den=dual['denominator']; weights=dual['weights']
            need(type(den) is int and den > 0, 'dual denominator')
            need(type(weights) is list and len(weights) == 308, 'dual weight count')
            need(all(type(w) is int and w >= 0 for w in weights), 'dual weights')
            denominators.add(den); support.append(sum(w>0 for w in weights)); weight_count += len(weights)
            hc,ho,weighted,dc,do,objective=model._dual_epoch_reconstruction(left,right,epoch,den,tuple(weights))
            need(dc == F(record[f'Dc{epoch}']) and do == F(record[f'Do{epoch}']), 'dual scalars')
            need(objective == F(dual['objective']), 'dual objective')
            objectives[epoch]=objective
            parent_objective=F(parent_payload['records'][pi][f'n{epoch}']['objective'])
            need(F(dual['improvement_over_parent']) == objective-parent_objective, 'dual improvement')
            if objective > parent_objective: improved += 1
            need((pi in selected_set) == (objective > parent_objective), 'strict refinement status')
            for endpoint in (left,right):
                exact_slack=model._integer_slack(hc,ho,weighted,den,endpoint)
                need(model._bareiss_positive_definite(exact_slack), 'refined endpoint PD')
                endpoint_checks += 1
            epoch_duals += 1
        a=2*(F(record['Dc4'])+RHO*F(record['Dc8']))-(objectives[4]+RHO*objectives[8])
        b=2*(F(record['Do4'])+RHO*F(record['Do8']))
        ll,lu=log_interval(right/left)
        reciprocal=b*(F(1,left)-F(1,right))
        if a >= 0:
            plo,phi=a*ll+reciprocal,a*lu+reciprocal
        else:
            plo,phi=a*lu+reciprocal,a*ll+reciprocal
        need(plo <= phi, 'piece interval order')
        raw_lo += plo; raw_hi += phi

    need(last_right == F(164), 'complete phase end')
    log2_lo,log2_hi=log_interval(F(2))
    need(F(0) < raw_lo <= raw_hi and F(0) < log2_lo <= log2_hi, 'normalization inputs')
    corners=(raw_lo/log2_lo,raw_lo/log2_hi,raw_hi/log2_lo,raw_hi/log2_hi)
    normalized=(min(corners),max(corners))
    need(normalized[1] < target[0], 'complete-phase separator')
    margin=target[0]-normalized[1]
    need(parent_normalized[0] - normalized[1] > F(461159269,2*10**11), 'parent/refined improvement')
    need(
        normalized[1] < F(36849435771,10**12)
        < F(18634061003,5*10**11) < target[0],
        'clean U/T fences',
    )
    need(margin > F(83737247,2*10**11) > F(1,2500), 'clean margin fences')

    # Only after independent reconstruction, compare the producer's embedded exact fields.
    embedded=payload['exact_replay']
    need(embedded['classification'] == 'EXACT_SEPARATOR_KILL', 'embedded classification')
    need(embedded['refined_pieces'] == len(records), 'embedded pieces')
    need(embedded['epoch_duals'] == epoch_duals, 'embedded dual census')
    need(embedded['endpoint_PD_checks'] == endpoint_checks, 'embedded PD census')
    need(tuple(F(x) for x in embedded['raw_interval']) == (raw_lo,raw_hi), 'embedded raw interval')
    need(tuple(F(x) for x in embedded['normalized_interval']) == normalized, 'embedded normalized interval')
    need(tuple(F(x) for x in embedded['target_interval']) == target, 'embedded target interval')
    need(F(embedded['classification_margin']) == margin, 'embedded margin')

    report={
      'status':'INDEPENDENT_EXACT_REPLAY_OK_KILL',
      'artifact_sha256':sha(ARTIFACT),'internal_sha256':calculated_internal,
      'parent_sha256':sha(PARENT),'points':list(points),'golomb_positive_differences':len(witnesses),
      'delta_V':str(delta_v),'delta_Vrt':str(delta_vrt),
      'canonical_chambers':len(canonical)-1,'selected_parent_chambers':len(selected),
      'refined_pieces':len(records),'partition_start':str(expected[0][2]),'partition_end':str(expected[-1][3]),
      'epoch_duals':epoch_duals,'weights':weight_count,'endpoint_PD_checks':endpoint_checks,
      'denominators':sorted(denominators),'support_range':[min(support),max(support)],
      'strictly_improved_epoch_pieces_recomputed':improved,
      'parent_classification':'EXACT_STORED_DUAL_NO_SEPARATION_NOT_PRIMAL_FEASIBILITY',
      'parent_endpoint_PD_checks':parent_pd,
      'parent_normalized_interval_grid_1e15':[str(grid_floor(parent_normalized[0],10**15)),str(grid_ceil(parent_normalized[1],10**15))],
      'raw_interval_grid_1e15':[str(grid_floor(raw_lo,10**15)),str(grid_ceil(raw_hi,10**15))],
      'normalized_interval_grid_1e15':[str(grid_floor(normalized[0],10**15)),str(grid_ceil(normalized[1],10**15))],
      'target_interval_grid_1e15':[str(grid_floor(target[0],10**15)),str(grid_ceil(target[1],10**15))],
      'kill_margin_grid_1e15':[str(grid_floor(margin,10**15)),str(grid_ceil(margin,10**15))],
      'kill_margin_gt_1_over_2500':margin > F(1,2500),
      'raw_interval_exact_sha256':obj_sha([str(raw_lo),str(raw_hi)]),
      'normalized_interval_exact_sha256':obj_sha([str(normalized[0]),str(normalized[1])]),
      'target_interval_exact_sha256':obj_sha([str(target[0]),str(target[1])]),
      'margin_exact_sha256':hashlib.sha256(str(margin).encode()).hexdigest(),
      'margin_numerator_digits':len(str(margin.numerator)),'margin_denominator_digits':len(str(margin.denominator)),
      'embedded_exact_fields_match_after_replay':True,
    }
    print(json.dumps(report,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()

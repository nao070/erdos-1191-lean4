#!/usr/bin/env python3
"""Independent integer-label scan and fixed-point gates for the one saved row/bin."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from independent_checker import rank_conditions, output_condition, log_fixed, SCALE, decide

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=HERE/'A47_ROW_BIN_EXACT.json';ref=json.loads(rp.read_text())
sp=HERE/ref['input'];data=json.loads(sp.read_text())
assert sha(sp)==ref['source_sha256'][sp.name]
oldvalues=data['a'][:24];oldrank={value:index+1 for index,value in enumerate(oldvalues)}
allvalues=data['a']; output_values={allvalues[r-1]:r for r in range(43,49)}
got=[];passed=[];unknown=[]
for e in range(297,330):
    pairs=[]
    for wvalue,w in oldrank.items():
        z=oldrank.get(wvalue+e)
        if z is not None: pairs.append((w,z))
    assert len(pairs)<=1
    if not pairs: continue
    w,z=pairs[0];r=output_values.get(3578-e)
    disjoint=len({1,22,w,z})==4
    got.append((e,w,z,3578-e,r,disjoint))
    if r is None: continue
    assert disjoint and len({1,22,w,z,42,r})==6
    d=allvalues[21]-allvalues[0];t=allvalues[r-1]-allvalues[41]
    c,s=max(22,z),min(22,z)
    assert c<25<42<r<=48 and 0<e<d and t==d-e
    try:
        assert rank_conditions(c,s,42,r) and output_condition(c,t)
        lc,uc=log_fixed(c)
        quad=sorted((1,22,w,z));gaps=[allvalues[v-1]-allvalues[u-1] for u,v in zip(quad,quad[1:])]
        assert all(decide(g*lc**3,g*uc**3,c*c*SCALE**3) for g in gaps)
    except ArithmeticError:
        unknown.append(e);continue
    assert e>144 and t>33 and all(g>33 for g in gaps)
    passed.append([d,e,1,22,w,z,c,s,42,r,t])
expected=[(v['e'],*v['unique_old_pair'],v['mapped_output_value'],v['actual_future_rank'],v['source_endpoints_disjoint']) for v in ref['labels']]
assert got==expected and passed==[v['original_record'] for v in ref['labels'] if v['strict_core_status']=='PASS']
assert not unknown
u=F(0)
for j in range(43,97):
    alpha=F(1,j*j*(j-1)**2);alpha_next=F(1,j*j*(j+1)**2)
    u+=(alpha-alpha_next)/(allvalues[j-1]-allvalues[0])**2
assert str(u)==ref['genuine_price']['u_r_M_exact']
lam=(F(1,48**2*47**2)-F(1,48**2*49**2))/(allvalues[47]-allvalues[0])**2
assert str(lam)==ref['genuine_price']['lambda_k_exact']
out={'date':'2026-09-09','attempt':'A47','status':'PASS_INDEPENDENT_ONE_BIN_ROW_CHECK',
 'input':sp.name,'old_label_integer_scan_inclusive':[297,329],
 'candidate_endpoint_values_tested_only_within_bin':True,'bin_label_count':len(got),
 'bin_sum_e':sum(v[0] for v in got),'actual_output_intersection':[[43,3266]],
 'exact_label_endpoint_and_source_exclusion_equality':True,
 'strict_and_remainder_record_set_equality':True,'strict_count':len(passed),
 'strict_records':passed,'genuine_component_price_equal':True,
 'genuine_full_tail_equal_via_alpha_differences':True,'unknown_comparisons':unknown,
 'source_sha256':{p.name:sha(p) for p in (rp,sp,HERE/'independent_checker.py',Path(__file__))},
 'independence':'Does not import the reference evaluator; scans integer labels297..329 by endpoint-value membership, uses independent fixed-point log gates and direct alpha differences for the genuine price.',
 'scope':'One prescribed bin and physical row only; no new old-label bin, terminal, component, history, or full-profile search.'}
(HERE/'A47_ROW_BIN_INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['source_sha256','independence','scope']},indent=2))

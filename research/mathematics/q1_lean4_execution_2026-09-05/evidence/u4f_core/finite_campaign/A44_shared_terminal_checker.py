#!/usr/bin/env python3
"""Independent exact checker of the only138 authorized endpoint candidates."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib
import itertools
import json
from independent_checker import rank_conditions,output_condition,log_fixed,SCALE

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=HERE/'A44_SHARED_TERMINAL_EXACT.json';ref=json.loads(rp.read_text())
sp=HERE/ref['input'];data=json.loads(sp.read_text())
for name,expected in ref['source_sha256'].items():assert sha(HERE/name)==expected
a=[None]+data['a'];x,i,b,k=1,42,25,48
D={}
for w in range(1,b):
    for z in range(w+1,b):
        e=a[z]-a[w]
        assert e>0 and e not in D
        D[e]=(w,z)
assert len(D)==276
found=[];candidates=[];unknown=[]
for y in range(2,25):
    for r in range(43,49):
        d=a[y]-a[x];t=a[r]-a[i];e=d-t
        row={'y':y,'r':r,'e':e}
        if e<=0:
            row['status']='NONPOSITIVE_E';candidates.append(row);continue
        if e not in D:
            row['status']='E_NOT_OLD_DIFFERENCE';candidates.append(row);continue
        w,z=D[e]
        if len({x,y,w,z,i,r})!=6:
            row['status']='ENDPOINT_OVERLAP';candidates.append(row);continue
        c,s=max(y,z),min(y,z)
        record=[d,e,x,y,w,z,c,s,i,r,t]
        assert d>e>0 and c<b<i<r<=k and t==d-e
        try:
            core=rank_conditions(c,s,i,r) and output_condition(c,t)
        except ArithmeticError:
            row['status']='UNKNOWN_CORE';unknown.append(row);candidates.append(row);continue
        if not core:
            row['status']='STRICT_GATE_FAIL';candidates.append(row);continue
        quad=sorted((x,y,w,z));gaps=[a[v]-a[u] for u,v in zip(quad,quad[1:])]
        try:large=all(output_condition(c,g) for g in gaps)
        except ArithmeticError:
            row['status']='UNKNOWN_LARGE';unknown.append(row);candidates.append(row);continue
        row['status']='STRICT_CORE';row['record']=record;row['all_large']=large
        candidates.append(row);found.append(row)
assert len(candidates)==138
observed={tuple(r['record']) for r in found}
expected={tuple(r['original_record']) for r in ref['edges']}
assert observed==expected and not unknown
by_record={tuple(r['original_record']):r for r in ref['edges']}
price=(F(1,k*k*(k-1)**2)-F(1,(k+1)**2*k*k))/(a[k]-a[1])**2
for row in found:
    cert=by_record[tuple(row['record'])]
    assert row['all_large']==cert['all_large_old_gaps']
    assert F(cert['genuine_component_price_exact'])==price
    assert F(cert['priced_de_exact'])==row['record'][0]*row['record'][1]*price

def witnesses(large_only):
    rows=sorted([r for r in found if not large_only or r['all_large']],key=lambda q:(q['y'],q['r'],q['e']))
    result={}
    for coordinate in ('y','r'):
        pair=next((pair for pair in itertools.combinations(rows,2) if pair[0][coordinate]==pair[1][coordinate]),None)
        result[coordinate]=None if pair is None else [{
            'y':q['y'],'r':q['r'],'e':q['e'],'record':q['record'],
            'original_bank_index':by_record[tuple(q['record'])]['original_bank_index'],
            'all_large':q['all_large']} for q in pair]
    return result

for large_only,key in [(False,'all_strict_summary'),(True,'all_large_summary')]:
    rows=[r['record'] for r in found if not large_only or r['all_large']]
    assert len(rows)==ref[key]['count']
    assert sum(r[0]*r[1] for r in rows)==ref[key]['sum_de']
    assert sum(r[1] for r in rows)==ref[key]['sum_e']
logs={str(n):[str(F(lo,SCALE)),str(F(hi,SCALE))] for n in sorted({q['record'][6] for q in found}|{q['r'] for q in found})
      for lo,hi in [log_fixed(n)]}
out={'date':'2026-09-09','attempt':'A44','status':'PASS_INDEPENDENT_138_CANDIDATE_CHECK',
 'input':sp.name,'b':b,'k':k,'terminal':[x,i],'candidate_count':138,
 'candidate_status_counts':dict(Counter(q['status'] for q in candidates)),
 'candidates':candidates,'strict_count':len(found),'all_large_count':sum(q['all_large'] for q in found),
 'strict_reference_record_set_equality':True,'all_large_reference_set_equality':True,
 'minimal_strict_coordinate_reuse':witnesses(False),'minimal_all_large_coordinate_reuse':witnesses(True),
 'independent_log_intervals':logs,'unknown_comparisons':unknown,'genuine_component_price_exact':str(price),
 'source_sha256':{p.name:sha(p) for p in (sp,rp,HERE/'independent_checker.py',Path(__file__))},
 'independence':'Only y2..24 and r43..48 were reconstructed from endpoint values and the actual old difference map. Original reference rows were not used to decide membership; existing independent fixed-point gates were applied. Exact full selected row set and weights then matched the reference.',
 'scope':'Single prescribed terminal and cell only. No other terminal, cell, shift campaign, history generation or full-profile evaluation.'}
op=HERE/'A44_SHARED_TERMINAL_INDEPENDENT_CHECK.json';op.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'counts':out['candidate_status_counts'],'strict':len(found),'all_large':out['all_large_count'],
 'minimal_all_large_reuse':out['minimal_all_large_coordinate_reuse'],'unknown':len(unknown)},indent=2))

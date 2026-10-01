#!/usr/bin/env python3
"""Only reclassify the ten saved edges; no new endpoint candidates."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import itertools
import json
from reference_evaluator import log_bounds
from independent_checker import log_fixed,SCALE

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=HERE/'A44_SHARED_TERMINAL_EXACT.json'
cp=HERE/'A44_SHARED_TERMINAL_INDEPENDENT_CHECK.json'
ref=json.loads(rp.read_text());check=json.loads(cp.read_text())
assert check['status']=='PASS_INDEPENDENT_138_CANDIDATE_CHECK'
assert check['source_sha256'][rp.name]==sha(rp)
data_path=HERE/ref['input'];data=json.loads(data_path.read_text())
assert sha(data_path)==ref['source_sha256'][data_path.name]
b,k=25,48
H,Hk=data['a'][b-1]-data['a'][0],data['a'][k-1]-data['a'][0]

def inverse_floor(base,num,den,lo,hi):
    left,right=0,base+1
    while right-left>1:
        mid=(left+right)//2
        if mid**den*hi**num<=base**den:left=mid
        elif mid**den*lo**num>base**den:right=mid
        else:raise ArithmeticError('UNKNOWN fractional-power threshold')
    assert left**den*hi**num<=base**den<(left+1)**den*lo**num
    return left

def forward_ceil(base,num,den,lo,hi):
    lower,upper=base**den*lo**num,base**den*hi**num
    left,right=0,1
    while right**den<upper:right*=2
    while right-left>1:
        mid=(left+right)//2
        if mid**den<lower:left=mid
        elif mid**den>=upper:right=mid
        else:raise ArithmeticError('UNKNOWN fractional-power threshold')
    assert (right-1)**den<lower<=upper<=right**den
    return right

lo,hi=log_bounds(b)
il,iu=log_fixed(b);ilo,ihi=F(il,SCALE),F(iu,SCALE)
threshold=inverse_floor(b*b,5,4,lo,hi)
short=inverse_floor(b,3,4,lo,hi)
far=forward_ceil(b,5,8,lo,hi)
assert threshold==inverse_floor(b*b,5,4,ilo,ihi)
assert short==inverse_floor(b,3,4,ilo,ihi)
assert far==forward_ceil(b,5,8,ilo,ihi)
near_margin=H*lo**2-Hk
assert near_margin>0 and H*ilo**2-Hk>0
assert b+short<k<far+1
remaining=[r for r in ref['edges'] if r['all_large_old_gaps'] is True and r['e']>threshold]
reuses={}
for coordinate in ('y','r'):
    pair=next((pair for pair in itertools.combinations(remaining,2) if pair[0][coordinate]==pair[1][coordinate]),None)
    reuses[coordinate]=None if pair is None else [q['original_bank_index'] for q in pair]
out={'date':'2026-09-09','attempt':'A44_REMAINDER','status':'PASS_EXACT_SAVED_EDGE_SUBCLASS',
 'input':ref['input'],'C_exact':'1','m0':2,'M':96,'T':96,'b':b,'k':k,'terminal':ref['terminal'],
 'reference_log_interval':[str(lo),str(hi)],'independent_log_interval':[str(ilo),str(ihi)],
 'A45_small_source_threshold':threshold,'A45_threshold_proof':{
    'statement':'L^4*(log25)^5 <= 625^4 < (L+1)^4*(log25)^5',
    'left_upper':str(threshold**4*hi**5),'middle':625**4,
    'right_lower':str((threshold+1)**4*lo**5)},
 'A43_short_s':short,'A43_short_floor_proof':{
    'statement':'s^4*(log25)^3 <= 25^4 < (s+1)^4*(log25)^3',
    'left_upper':str(short**4*hi**3),'middle':25**4,'right_lower':str((short+1)**4*lo**3)},
 'A42_far_ceil':far,'A42_far_ceil_proof':{
    'statement':'(N-1)^8 < 25^8*(log25)^5 <= N^8',
    'left':(far-1)**8,'middle_lower':str(b**8*lo**5),'middle_upper':str(b**8*hi**5),'right':far**8},
 'central_rank_interval_strict':[b+short,far+1],'k_in_central_band':True,
 'H_b':H,'H_k':Hk,'near_span_lower_margin_exact':str(near_margin),'near_span':True,
 'saved_edges_considered':len(ref['edges']),'new_endpoint_candidates_examined':0,
 'remaining_edges':remaining,'remaining_count':len(remaining),
 'remaining_sum_de':sum(r['de'] for r in remaining),'remaining_sum_e':sum(r['e'] for r in remaining),
 'coordinate_reuse_witness_indices':reuses,'unknown_comparisons':[],
 'genuine_component_price_exact':ref['genuine_component_price_exact'],
 'source_sha256':{p.name:sha(p) for p in (rp,cp,data_path,HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__))},
 'scope':'Only subclassify the existing ten strict edges at the same terminal/cut/component. Uses rational log intervals and integer fourth/eighth-power comparisons. No new history, terminal, cell, or edge candidate search.'}
op=HERE/'A44_SHARED_TERMINAL_REMAINDER_EXACT.json';op.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'small_source_L':threshold,'short_s':short,'far_ceil':far,
 'central':out['central_rank_interval_strict'],'k':k,'near_span':True,
 'remaining':[[r['y'],r['r'],r['e'],r['de']] for r in remaining],
 'sum_de':out['remaining_sum_de'],'sum_e':out['remaining_sum_e'],'reuses':reuses},indent=2))

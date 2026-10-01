#!/usr/bin/env python3
"""Exactly six authorized extra cells, only after all initial penalties vanish."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prior=HERE/'A36_mixed_pair_547_twelve_cells_exact.json'
old=json.loads(prior.read_text())
assert len(old['cells'])==12 and old['all_penalties_zero'] and not old['unknown_comparisons']
source=HERE/old['input'];data=json.loads(source.read_text())
assert sha(source)==old['source_sha256'][source.name]
a=[None]+data['a']
v=60;c=547
price=(F(1,v*v*(v-1)**2)-F(1,v*v*(v+1)**2))/(a[v]-a[1])**2
rows=[]
for cut in old['cuts']:
    b,H,S=cut['b'],cut['H_b'],cut['S_b']
    U=cut['canonical_predelete_allowed_U'];after=[t for t in U if t!=c]
    h=(v-b)*(v-b-1)//2
    before=sum((F(H-t,H) for t in U[:h]),F(0))
    later=sum((F(H-t,H) for t in after[:h]),F(0))
    penalty=before-later
    rows.append({'b':b,'v':v,'M':96,'T':v,'component_k':v,'h':h,
        'r':cut['canonical_rank_r'],'N':cut['N_predelete'],
        'p_exact':str(penalty),'H_times_p_exact':str(H*penalty),
        'S_times_p_exact':str(S*penalty),'rho_exact':str(penalty/F(H-c,H)),
        'predelete_packing_exact':str(before),'postdelete_packing_exact':str(later),
        'genuine_component_price_exact':str(price),'priced_p_exact':str(price*penalty),
        'priced_H_times_p_exact':str(price*H*penalty),
        'priced_S_times_p_exact':str(price*S*penalty),
        'next_selected_label_or_none':U[h] if h<len(U) else None})
checks=[]
for before,after in zip(rows,rows[1:]):
    checks.append({'v':v,'b_before':before['b'],'b_after':after['b'],
     'differences':{key:str(F(after[key])-F(before[key])) for key in ('p_exact','H_times_p_exact','S_times_p_exact','rho_exact')},
     'nonincreasing_candidates':{key:F(after[key])<=F(before[key]) for key in ('p_exact','H_times_p_exact','S_times_p_exact','rho_exact')}})
out={'date':'2026-09-09','attempt':'A36','input':source.name,'C_exact':'1','m0':2,
     'target_pair':old['target_pair'],'reason':'All twelve initially prescribed penalties were exactly zero.',
     'additional_output_horizon':60,'source_M':96,'H_60':a[v]-a[1],
     'prebank_evidence_reference':prior.name,'cells':rows,'adjacent_cut_comparisons':checks,
     'source_sha256':{p.name:sha(p) for p in (source,prior,Path(__file__))},
     'scope':'Only six authorized additional cells for the same physical pair; no other pairs or histories.'}
path=HERE/'A36_mixed_pair_547_horizon60_exact.json';path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS_EXACT_REFERENCE','price':str(price),'rows':rows,'comparisons':checks},indent=2))

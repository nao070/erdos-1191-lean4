#!/usr/bin/env python3
"""One birth-span flag on the already saved A53 winner; no record search."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from reference_evaluator import log_bounds
from independent_checker import log_fixed,SCALE
HERE=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
wp=HERE/'A53_EXISTING_RESTART_WITNESS_EXACT.json';old=json.loads(wp.read_text());w=old['witness']
sp=HERE/old['input'];data=json.loads(sp.read_text());assert sha(sp)==old['source_sha256'][sp.name]
a=data['a'];c,k=w['birth_c'],w['k'];Hc,Hk=a[c-1]-a[0],a[k-1]-a[0]
lo,hi=log_bounds(c);il,iu=log_fixed(c);ilo,ihi=F(il,SCALE),F(iu,SCALE)
assert Hc*lo**2-Hk>0 and Hc*ilo**2-Hk>0
out={'date':'2026-09-09','attempt':'A54_EXISTING_WITNESS_FLAG','status':'PASS_ONE_SAVED_WITNESS_ONLY',
 'input':old['input'],'original_bank_index':w['original_bank_index'],'record':w['record'],
 'cut_b':w['b'],'component_k':k,'birth_c':c,'H_c':Hc,'H_k':Hk,
 'q_exact':'2','A54_unpaid_at_component':True,
 'reference_log_interval':[str(lo),str(hi)],'independent_log_interval':[str(ilo),str(ihi)],
 'reference_positive_lower_margin_exact':str(Hc*lo**2-Hk),
 'independent_positive_lower_margin_exact':str(Hc*ilo**2-Hk),
 'original_lambda48_exact':w['lambda48_exact'],
 'price_scope':'Only classify the saved component; original full u_r and A53 split remain in prior evidence. No full tail is claimed to belong to every remaining selector.',
 'new_record_candidates_examined':0,'unknown_comparisons':[],
 'source_sha256':{p.name:sha(p) for p in (wp,sp,HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__))}}
(HERE/'A54_EXISTING_WITNESS_FLAG_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({q:out[q] for q in ['status','original_bank_index','cut_b','component_k','birth_c','H_c','H_k','A54_unpaid_at_component']},indent=2))

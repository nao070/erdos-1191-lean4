#!/usr/bin/env python3
"""One existing physical row and one old-label bin, not a profile search."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from reference_evaluator import differences, rank_core, physical_core

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'C1_m02_dense_variant1_M96.json'
certificate=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
prior_path=HERE/'A44_SHARED_TERMINAL_REMAINDER_EXACT.json'
gap_path=HERE/'A46_SHARED_TERMINAL_REMAINDER_EXACT.json'
data=json.loads(source.read_text());cert=json.loads(certificate.read_text())
prior=json.loads(prior_path.read_text());gap=json.loads(gap_path.read_text())
assert sha(source)==cert['input_sha256']==prior['source_sha256'][source.name]
assert cert['status']=='PASS' and data['C_exact']=='1' and data['m0']==2
assert data['M']==data['T']==96 and data['cap_all_ranks_certified']
a=[None]+data['a']; b,k,M,T,x,y,i,J,h=25,48,96,96,1,22,42,33,9
assert gap['J']==J and prior['A45_small_source_threshold']==144
d=a[y]-a[x];K=d+a[i]; assert (d,K)==(603,3578)
old=differences(data['a'][:b-1]);lo,hi=h*J,(h+1)*J
future={a[r]:r for r in range(b+1,k+1)}
bank=sorted((e,*pair) for e,pair in old.items() if lo<=e<hi)
rows=[]
for e,w,z in bank:
    target=K-e; r=future.get(target)
    assert K-hi<target<=K-lo
    disjoint=len({x,y,w,z})==4
    c,s=max(y,z),min(y,z)
    row={'e':e,'unique_old_pair':[w,z],'old_endpoint_values':[a[w],a[z]],
         'mapped_output_value':target,'actual_future_rank':r,
         'source_endpoints_disjoint':disjoint,
         'shared_fixed_source_endpoints':sorted({x,y}&{w,z}),
         'source_births':[c,s], 'strict_core_status':'NOT_APPLICABLE_NO_ACTUAL_OUTPUT',
         'full_remainder_status':'NOT_APPLICABLE_NO_ACTUAL_OUTPUT',
         'unused_reasons':[]}
    if r is None: row['unused_reasons'].append('MAPPED_VALUE_NOT_IN_ACTUAL_FUTURE')
    if not disjoint: row['unused_reasons'].append('SOURCE_ENDPOINT_OVERLAP')
    if r is not None:
        assert i<r<=k and len({x,y,w,z,i,r})==6
        t=a[r]-a[i]; record=[d,e,x,y,w,z,c,s,i,r,t]
        assert d>e>0 and d-e==t and c<b<i
        assert rank_core(c,s,i,r) is True and physical_core(c,t) is True
        saved=next(v for v in prior['remaining_edges'] if v['original_record']==record)
        gsave=next(v for v in gap['rows'] if v['record']==record)
        assert saved['all_large_old_gaps'] and gsave['survives_A46']
        row.update({'original_record':record,'original_bank_index':saved['original_bank_index'],
           'de':d*e,'strict_core_status':'PASS','full_remainder_status':'PASS',
           'original_strict_margin_intervals':saved['strict_margin_intervals'],
           'strict_gate_decisions':saved['strict_gate_decisions'],
           'all_large_old_gap_margin_intervals':saved['large_gap_margin_intervals'],
           'old_quad':saved['old_quad'],'old_gaps':saved['old_gaps'],
           'covered_cut_interval_inclusive':saved['covered_cut_interval_inclusive'],
           'remainder_checks':{'e_gt_L25':e>144,'all_gaps_gt_J25':all(v>J for v in saved['old_gaps']),
             't_gt_J25':t>J,'original_all_large_old_gaps':True,
             'central_component':prior['k_in_central_band'],'near_span':prior['near_span']}})
    rows.append(row)
used=[v for v in rows if v['strict_core_status']=='PASS']
assert len(used)==1 and used[0]['e']==312
lam=F(4,k*(k*k-1)**2*(a[k]-a[1])**2)
assert str(lam)==prior['genuine_component_price_exact']
r=used[0]['actual_future_rank']
u=sum((F(4,j*(j*j-1)**2*(a[j]-a[1])**2) for j in range(r,M+1)),F(0))
summary={'bin_label_count':len(rows),'bin_sum_e':sum(v['e'] for v in rows),
 'source_disjoint_count':sum(v['source_endpoints_disjoint'] for v in rows),
 'source_disjoint_sum_e':sum(v['e'] for v in rows if v['source_endpoints_disjoint']),
 'mapped_actual_output_count':sum(v['actual_future_rank'] is not None for v in rows),
 'strict_count':len(used),'remainder_count':sum(v['full_remainder_status']=='PASS' for v in rows),
 'used_sum_e':sum(v['e'] for v in used),'unused_sum_e':sum(v['e'] for v in rows if v not in used),
 'bin_d_sum_e':d*sum(v['e'] for v in rows),'actual_d_sum_e':sum(v['de'] for v in used),
 'unused_d_sum_e':d*sum(v['e'] for v in rows if v not in used),
 'exact_used_label_mass_fraction':str(F(sum(v['e'] for v in used),sum(v['e'] for v in rows)))}
result={'date':'2026-09-09','attempt':'A47','status':'PASS_EXACT_ONE_BIN_ROW_REFERENCE',
 'input':source.name,'C_exact':'1','m0':2,'M':M,'T':T,'b':b,'k':k,
 'fixed_row':{'x':x,'y':y,'d':d,'i':i,'a_x':a[x],'a_y':a[y],'a_i':a[i],'K':K},
 'old_bin':{'h':h,'J':J,'left_inclusive':lo,'right_exclusive':hi},
 'mapped_output_window':{'left_exclusive':K-hi,'right_inclusive':K-lo,
   'actual_future_intersection':[[rank,value] for value,rank in future.items() if K-hi<value<=K-lo]},
 'labels':rows,'summary':summary,
 'genuine_price':{'component_k':k,'lambda_k_exact':str(lam),
   'actual_component_mass_exact':str(lam*summary['actual_d_sum_e']),
   'bin_allowance_component_mass_exact':str(lam*summary['bin_d_sum_e']),
   'output_r':r,'full_tail_component_range_inclusive':[r,M],
   'u_r_M_exact':str(u),'actual_record_full_tail_mass_exact':str(u*used[0]['de']),
   'alpha_M_plus_1_preserved':True,
   'distinction':'The single component coefficient lambda48 differs from the genuine u43^[96] sum across components43..96. No full tail is assigned to unused labels with no actual output.'},
 'unknown_comparisons':[],
 'source_sha256':{p.name:sha(p) for p in (source,certificate,prior_path,gap_path,HERE/'reference_evaluator.py',Path(__file__))},
 'scope':'Exactly one existing row (x1,y22,loweroutput42), one bin [297,330), cut25/component48. Reconstruct old bin only; no other bin/row, new history, or full-profile enumeration. Strict comparisons are only applicable after an actual output exists.'}
(HERE/'A47_ROW_BIN_EXACT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'labels':[[v['e'],v['unique_old_pair'],v['mapped_output_value'],v['actual_future_rank'],v['unused_reasons']] for v in rows],
                  'summary':summary,'lambda48':str(lam)},indent=2))

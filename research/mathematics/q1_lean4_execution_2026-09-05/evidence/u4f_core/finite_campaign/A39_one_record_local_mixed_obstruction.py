#!/usr/bin/env python3
"""Only the specified existing A24 record; no other-record search."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from reference_evaluator import log_bounds
from independent_checker import rank_conditions,output_condition,log_fixed,SCALE

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
dp=HERE/'C1_m02_dense_variant1_M96.json'
cp=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
ap=HERE/'cut_shift_b24_compact_counterexamples.json'
data=json.loads(dp.read_text());cert=json.loads(cp.read_text());a24=json.loads(ap.read_text())
assert sha(dp)=='d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e'
assert cert['status']=='PASS' and cert['input_sha256']==sha(dp)
entry=a24['weighted_counterexample_despite_count_decrease']['complete_birth_records'][2]
assert entry['quad']==[1,6,20,24] and entry['type']==3 and (entry['i'],entry['r'])==(42,43)
row=entry['original_record']
assert row==[713,422,1,24,6,20,24,20,42,43,291]
a=[None]+data['a'];d,e,x,y,u,z,c,s,i,r,t=row
b,k=25,48
assert d==a[y]-a[x] and e==a[z]-a[u] and t==a[r]-a[i]==d-e
assert len({x,y,u,z,i,r})==6 and c<b<i<r<=k<=96
Hb,Hi,Hk=a[b]-a[1],a[i]-a[1],a[k]-a[1]
assert Hi>=2*Hb
mixed=[]
for future in (i,r):
    for past in sorted((x,y,u,z)):
        label=a[future]-a[past]
        mixed.append({'past':past,'future':future,'label':label,
             'eligible_0_to_Hb':0<label<Hb,'kernel_mass_exact':str(max(F(0),F(Hb-label,Hb)))})
assert all(m['label']>=Hb for m in mixed)
assert len({m['label'] for m in mixed})==8
lc,uc=log_bounds(c);lr,ur=log_bounds(r)
margin_intervals={
 's_logc_squared_minus_c':[s*lc**2-c,s*uc**2-c],
 'i_minus_c_logc_squared_minus_c':[(i-c)*lc**2-c,(i-c)*uc**2-c],
 'r_minus_i_logr_cubed_minus_r':[(r-i)*lr**3-r,(r-i)*ur**3-r],
 'c_logc_minus_r':[c*lc-r,c*uc-r],
 't_logc_cubed_minus_c_squared':[t*lc**3-c*c,t*uc**3-c*c]}
assert all(lo>0 for lo,hi in margin_intervals.values())
assert rank_conditions(c,s,i,r) and output_condition(c,t)
price=F(4,k*(k*k-1)**2*Hk*Hk)
assert price==F(1,1148518878296832)
U,V=a[r]-a[y],a[i]-a[x]
assert V-U==e
independent_logs={str(n):[str(F(lo,SCALE)),str(F(hi,SCALE))] for n in (c,r)
                  for lo,hi in [log_fixed(n)]}
out={'date':'2026-09-09','attempt':'A39','status':'PASS_EXACT_SINGLE_RECORD_COUNTEREXAMPLE',
 'input':dp.name,'C_exact':'1','m0':2,'M':96,'T':96,'cut_b':b,'component_k':k,
 'A24_record_path':'weighted_counterexample_despite_count_decrease.complete_birth_records[2]',
 'original_record':row,'old_quad':entry['quad'],'matching_type':3,
 'actual_endpoint_values':{str(n):a[n] for n in sorted({x,y,u,z,i,r,b,k})},
 'positive_sidon_and_cap_evidence':'Existing independent full M96 certificate reused, hash bound below.',
 'strict_margin_intervals':{q:[str(v) for v in vals] for q,vals in margin_intervals.items()},
 'independent_fixed_point_log_intervals':independent_logs,
 'independent_rank_conditions':'PASS','independent_physical_condition':'PASS',
 'six_distinct_endpoints':True,'covered_cut_interval_inclusive':[c+1,i-1],
 'H_b':Hb,'H_i':Hi,'H_k':Hk,'H_i_ge_twice_H_b':True,
 'eight_actual_mixed_labels':mixed,'eligible_local_labels':[],
 'local_eligible_kernel_mass_exact':'0','source_product_de':d*e,
 'genuine_component_price_exact':str(price),'genuine_record_component_mass_exact':str(d*e*price),
 'identity_U_V':{'source_x':x,'source_y':y,'U_a_r_minus_a_y':U,'V_a_i_minus_a_x':V,'V_minus_U':V-U,'equals_e':True},
 'source_sha256':{p.name:sha(p) for p in (dp,cp,ap,HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__))},
 'rejected_candidate':'Every original strict-core record has an eligible (0,H_b) mixed label joining one of its two output endpoints to one of its four old endpoints.',
 'scope':'Only the one prescribed certified A24 record. Refutes output-endpoint-local charging for that record; not absence of payment from the complete mixed bank, nor U4-F or Q1.'}
p=HERE/'A39_one_record_local_mixed_obstruction_exact.json';p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'d':d,'e':e,'t':t,'H_b':Hb,'H_i':Hi,
 'mixed_labels':[m['label'] for m in mixed],'local_mass':0,'de':d*e,'price':str(price),
 'priced_record_mass':str(d*e*price),'U':U,'V':V,'V_minus_U':V-U},indent=2))

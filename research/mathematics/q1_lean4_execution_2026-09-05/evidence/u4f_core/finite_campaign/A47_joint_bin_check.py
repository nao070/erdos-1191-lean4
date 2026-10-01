#!/usr/bin/env python3
"""Thirteen already saved labels, fixed d603/b25/k48, all possible lower outputs."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from reference_evaluator import log_bounds, strict_positive
from independent_checker import rank_conditions, output_condition, log_fixed, SCALE, decide

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
singlepath=HERE/'A47_ROW_BIN_EXACT.json'
checkpath=HERE/'A47_ROW_BIN_INDEPENDENT_CHECK.json'
single=json.loads(singlepath.read_text());check=json.loads(checkpath.read_text())
assert check['status']=='PASS_INDEPENDENT_ONE_BIN_ROW_CHECK'
assert sha(singlepath)==check['source_sha256'][singlepath.name]
source=HERE/single['input'];data=json.loads(source.read_text())
assert sha(source)==single['source_sha256'][source.name]
poolpath=HERE/'A29_forbidden_output_packing_four_cells_exact.json'
pool=json.loads(poolpath.read_text())['original_core_record_pool']
priorpath=HERE/'A44_SHARED_TERMINAL_REMAINDER_EXACT.json'
prior=json.loads(priorpath.read_text())
a=[None]+data['a'];index={v:r for r,v in enumerate(data['a'],1)}
b,k,M,T,d,x,y=25,48,96,96,603,1,22
rows=[];unknown=[]
for old in single['labels']:
    e=old['e'];w,z=old['unique_old_pair'];t=d-e
    # Exactly this one output label is looked up, without constructing a full bank.
    pairs=[(i,index[a[i]+t]) for i in range(1,M+1) if a[i]+t in index]
    # Independent reverse endpoint membership for the same thirteen labels.
    reverse=[(index[a[r]-t],r) for r in range(1,M+1) if a[r]-t in index]
    assert pairs==reverse and len(pairs)<=1
    item={'e':e,'unique_old_pair':[w,z],'t':t,'actual_output_pair':None if not pairs else list(pairs[0]),
      'source_endpoints_disjoint':old['source_endpoints_disjoint'],
      'component_eligible':False,'strict_core_status':'NOT_APPLICABLE_OUTSIDE_COMPONENT',
      'remainder_status':'NOT_APPLICABLE_OUTSIDE_COMPONENT','unused_reasons':[]}
    if not old['source_endpoints_disjoint']:item['unused_reasons'].append('SOURCE_ENDPOINT_OVERLAP')
    if not pairs:
        item['unused_reasons'].append('OUTPUT_DIFFERENCE_ABSENT_IN_EXISTING_HISTORY')
    else:
        i,r=pairs[0]
        if i<=b:item['unused_reasons'].append('LOWER_OUTPUT_NOT_AFTER_CUT')
        if r>k:item['unused_reasons'].append('UPPER_OUTPUT_AFTER_COMPONENT')
        if len({x,y,w,z,i,r})!=6:item['unused_reasons'].append('SIX_ENDPOINT_DISTINCTNESS_FAILS')
        item['component_eligible']=b<i<r<=k
        if item['component_eligible']:
            c,s=max(y,z),min(y,z);assert c<b and len({x,y,w,z,i,r})==6
            lc,uc=log_bounds(c);lr,ur=log_bounds(r)
            margins={'older_birth':[s*lc**2-c,s*uc**2-c],
             'birth_output_gap':[(i-c)*lc**2-c,(i-c)*uc**2-c],
             'output_top_gap':[(r-i)*lr**3-r,(r-i)*ur**3-r],
             'upper_rank':[c*lc-r,c*uc-r],
             'physical_output':[t*lc**3-c*c,t*uc**3-c*c]}
            flags={key:strict_positive(*value,0) for key,value in margins.items()}
            if None in flags.values():unknown.append(e)
            assert all(v is True for v in flags.values())
            quad=sorted((x,y,w,z));gaps=[a[v]-a[u] for u,v in zip(quad,quad[1:])]
            gm=[[v*lc**3-c*c,v*uc**3-c*c] for v in gaps]
            assert all(strict_positive(*v,0) is True for v in gm)
            # Independent fixed-point gates and actual endpoints.
            assert rank_conditions(c,s,i,r) and output_condition(c,t)
            il,iu=log_fixed(c)
            assert all(decide(v*il**3,v*iu**3,c*c*SCALE**3) for v in gaps)
            assert e>144 and t>33 and all(v>33 for v in gaps)
            assert prior['k_in_central_band'] and prior['near_span']
            record=[d,e,x,y,w,z,c,s,i,r,t]
            bankindices=[int(j) for j,v in pool.items() if v==record]
            assert len(bankindices)==1
            u=sum((F(4,j*(j*j-1)**2*(a[j]-a[1])**2) for j in range(r,M+1)),F(0))
            uind=sum(((F(1,j*j*(j-1)**2)-F(1,j*j*(j+1)**2))/(a[j]-a[1])**2 for j in range(r,M+1)),F(0))
            assert u==uind
            item.update({'strict_core_status':'PASS','remainder_status':'PASS',
              'original_record':record,'original_bank_index':bankindices[0],'de':d*e,
              'strict_margin_intervals':{key:[str(v) for v in vals] for key,vals in margins.items()},
              'strict_gate_decisions':flags,'old_quad':quad,'old_gaps':gaps,
              'all_large_old_gap_margin_intervals':[[str(v) for v in vals] for vals in gm],
              'covered_cut_interval_inclusive':[c+1,i-1],
              'remainder_checks':{'e_gt_144':True,'t_gt_33':True,'all_old_gaps_gt_33':True,
                  'original_all_large':True,'central_component':True,'near_span':True},
              'u_r_M_exact':str(u),'actual_record_full_tail_mass_exact':str(d*e*u)})
    rows.append(item)
used=[v for v in rows if v['strict_core_status']=='PASS']
assert len(rows)==13 and sorted(v['e'] for v in used)==[302,312] and not unknown
B=d*sum(v['e'] for v in rows);Q=sum(v['de'] for v in used)
perrow=[]
for i in range(b+1,k):
    rowused=sum(v['de'] for v in used if v['actual_output_pair'][0]==i)
    perrow.append({'lower_output_i':i,'row_used':rowused,'independently_reset_bin_minus_row_used':B-rowused})
fake=sum(v['independently_reset_bin_minus_row_used'] for v in perrow)
truth=B-Q;over=(len(perrow)-1)*B
assert fake-truth==over
lam=F(single['genuine_price']['lambda_k_exact'])
out={'date':'2026-09-09','attempt':'A47_JOINT_BIN','status':'PASS_EXACT_THIRTEEN_LABEL_JOINT_CHECK',
 'input':source.name,'C_exact':'1','m0':2,'M':M,'T':T,'b':b,'k':k,
 'fixed_source':{'x':x,'y':y,'d':d},'bin':single['old_bin'],
 'looked_up_output_labels':len(rows),'new_source_pairs_or_bins':0,'labels':rows,
 'used_labels':[v['e'] for v in used],'used_sum_e':sum(v['e'] for v in used),
 'unused_labels':[v['e'] for v in rows if v not in used],
 'unused_sum_e':sum(v['e'] for v in rows if v not in used),
 'primary_disjoint_failure_partition':{
   'output_absent':sum(v['actual_output_pair'] is None for v in rows),
   'lower_output_not_after_cut':sum(v['actual_output_pair'] is not None and v['actual_output_pair'][0]<=b for v in rows),
   'upper_output_after_component':sum(v['actual_output_pair'] is not None and v['actual_output_pair'][0]>b and v['actual_output_pair'][1]>k for v in rows),
   'strict_and_remainder_used':len(used)},
 'source_and_six_endpoint_exclusion_flags_may_overlap_primary_failure':True,
 'bin_allowance_B':B,'actual_shared_Q':Q,'shared_deficit_B_minus_Q':truth,
 'lower_output_rows':perrow,'number_of_lower_output_rows':len(perrow),
 'sum_of_independently_reset_row_deficits':fake,
 'overcount_exact':over,'overcount_identity':'sum_i(B-row_used_i)-(B-Q)=(number_rows-1)*B',
 'genuine_component':{'lambda48_exact':str(lam),'actual_shared_mass_exact':str(lam*Q),
    'shared_deficit_exact':str(lam*truth),'independent_row_deficit_sum_exact':str(lam*fake),
    'overcount_exact':str(lam*over)},
 'full_tail_note':'Each actual record has its original u_r^[96], recorded separately. The component deficit identity uses only lambda48; unused labels have no assigned full output price.',
 'unknown_comparisons':unknown,
 'independent_checks':{'forward_reverse_output_endpoint_lookup':True,'independent_log_gates_for_both_actual_records':True,'exact_saved_original_pool_record_lookup':True,'two_genuine_tail_formulas':True,'component_deficit_identity':True},
 'source_sha256':{p.name:sha(p) for p in (singlepath,checkpath,source,poolpath,priorpath,HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__))},
 'scope':'Only the same thirteen old labels in one fixed source/bin/cut/component. Each output label has one forward and reverse membership lookup; no new source, bin, history, or full-profile scan. Shared scalar deficit is not a global norm estimate.'}
(HERE/'A47_JOINT_BIN_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'used':[[v['e'],v['actual_output_pair'],v['de'],v['old_gaps'],v['original_bank_index']] for v in used],
   'partition':out['primary_disjoint_failure_partition'],'B':B,'Q':Q,'shared_deficit':truth,
   'row_count':len(perrow),'independent_deficit_sum':fake,'overcount':over,'unknown':len(unknown)},indent=2))

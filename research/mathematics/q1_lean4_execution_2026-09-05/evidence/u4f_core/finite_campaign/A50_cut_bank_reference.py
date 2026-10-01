#!/usr/bin/env python3
"""Only33 labels, one source/bin/component, cuts23..47 of a certified history."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from reference_evaluator import log_bounds,strict_positive

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'C1_m02_dense_variant1_M96.json';certpath=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
data=json.loads(source.read_text());cert=json.loads(certpath.read_text())
assert cert['status']=='PASS' and cert['input_sha256']==sha(source)
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
a=[None]+data['a'];idx={v:r for r,v in enumerate(data['a'],1)}
M=T=96;v=48;d=603;x,y=1,22
assert a[y]-a[x]==d
lam=F(4,v*(v*v-1)**2*(a[v]-a[1])**2)
unknown=[];labels=[];records=[]
for e in range(297,330):
    sp=[(w,idx[a[w]+e]) for w in range(1,M+1) if a[w]+e in idx]
    t=d-e;op=[(i,idx[a[i]+t]) for i in range(1,M+1) if a[i]+t in idx]
    assert len(sp)<=1 and len(op)<=1
    item={'e':e,'t':t,'source_pair':None if not sp else list(sp[0]),'output_pair':None if not op else list(op[0]),
      'original_strict_status':'NOT_APPLICABLE','source_overlap_with_fixed_pair':[],
      'six_endpoint_distinctness':None,'reasons':[]}
    if not sp:item['reasons'].append('SOURCE_DIFFERENCE_ABSENT')
    if not op:item['reasons'].append('OUTPUT_DIFFERENCE_ABSENT')
    if sp:
        w,z=sp[0];item['source_overlap_with_fixed_pair']=sorted({x,y}&{w,z})
        item['bank_first_cut']=max(23,z+1)
        item['source_births']=[max(y,z),min(y,z)]
    if sp and op:
        w,z=sp[0];i,r=op[0];c,s=max(y,z),min(y,z)
        distinct=len({x,y,w,z,i,r})==6;item['six_endpoint_distinctness']=distinct
        if not distinct:item['reasons'].append('SIX_ENDPOINT_DISTINCTNESS_FAILS')
        if not c<i:item['reasons'].append('SOURCES_NOT_BEFORE_LOWER_OUTPUT')
        if r>v:item['reasons'].append('UPPER_OUTPUT_AFTER_FIXED_COMPONENT')
        if distinct and c<i and r<=v:
            lc,uc=log_bounds(c);lr,ur=log_bounds(r)
            margins={'older_birth':[s*lc**2-c,s*uc**2-c],
             'birth_output_gap':[(i-c)*lc**2-c,(i-c)*uc**2-c],
             'output_top_gap':[(r-i)*lr**3-r,(r-i)*ur**3-r],
             'upper_rank':[c*lc-r,c*uc-r],
             'physical_output':[t*lc**3-c*c,t*uc**3-c*c]}
            flags={q:strict_positive(*z,0) for q,z in margins.items()}
            item['strict_margin_intervals']={q:[str(z) for z in zs] for q,zs in margins.items()}
            item['strict_gate_decisions']=flags
            if None in flags.values():unknown.append({'e':e,'kind':'ORIGINAL_STRICT'})
            if all(z is True for z in flags.values()):
                item['original_strict_status']='PASS'
                quad=sorted((x,y,w,z));gaps=[a[r2]-a[r1] for r1,r2 in zip(quad,quad[1:])]
                gm=[[g*lc**3-c*c,g*uc**3-c*c] for g in gaps]
                large=[strict_positive(*p,0) for p in gm]
                if None in large:unknown.append({'e':e,'kind':'OLD_LARGE'})
                rec={'e':e,'record':[d,e,x,y,w,z,c,s,i,r,t],'de':d*e,
                   'original_coverage_inclusive':[c+1,i-1],'old_quad':quad,'old_gaps':gaps,
                   'original_all_large_old_gaps':all(p is True for p in large),
                   'old_large_margin_intervals':[[str(q) for q in p] for p in gm],
                   'u_r_M_exact':str(sum((F(4,j*(j*j-1)**2*(a[j]-a[1])**2) for j in range(r,M+1)),F(0)))}
                records.append(rec)
            else:item['original_strict_status']='FAIL_OR_UNKNOWN';item['reasons'].extend(q for q,p in flags.items() if p is False)
    labels.append(item)
assert sorted(r['e'] for r in records)==[302,312,318] and not unknown

def selected_flags(rec,b):
    lo,hi=log_bounds(b);m=v-b;s=rec['record'][7];t=rec['record'][10]
    # All powers are integer powers of exact rational log endpoints.
    comparisons={
      'e_gt_b2_log_5over4':[rec['e']**4*lo**5,rec['e']**4*hi**5,b**8],
      't_gt_b2_log_5over2':[t*t*lo**5,t*t*hi**5,b**4],
      'central_above_short':[m**4*lo**3,m**4*hi**3,b**4],
      'central_below_far':[b**8*lo**5,b**8*hi**5,(v-1)**8],
      'near_span':[(a[b]-a[1])*lo**2,(a[b]-a[1])*hi**2,a[v]-a[1]],
      'source_birth_support':[16*s**8*lo**9,16*s**8*hi**9,b**8]}
    for j,g in enumerate(rec['old_gaps']):comparisons['old_gap_'+str(j+1)+'_gt_b2_log_5over2']=[g*g*lo**5,g*g*hi**5,b**4]
    flags={q:strict_positive(*vals) for q,vals in comparisons.items()}
    flags['original_all_large_old_gaps']=rec['original_all_large_old_gaps']
    if None in flags.values():unknown.append({'e':rec['e'],'b':b,'kind':'OPTIONAL_SELECTOR'})
    return flags

cuts=[]
for b in range(23,48):
    bank=[p['e'] for p in labels if p['source_pair'] is not None and p['source_pair'][1]<b]
    active=[r for r in records if r['record'][6]<b<r['record'][8]]
    B=d*sum(bank);Q=sum(r['de'] for r in active);D=B-Q
    flags={str(r['e']):selected_flags(r,b) for r in active}
    sel=[r for r in active if all(flags[str(r['e'])].values())]
    u=sum((r['de']*F(r['u_r_M_exact']) for r in active),F(0))
    cuts.append({'b':b,'bank_labels':bank,'B':B,'active_original_labels':[r['e'] for r in active],
      'Q':Q,'D':D,'D_over_B_exact':None if B==0 else str(F(D,B)),
      'genuine_lambda48_Q_exact':str(lam*Q),'genuine_lambda48_D_exact':str(lam*D),
      'fixed_original_record_subset_full_tail_mass_exact':str(u),
      'optional_A46_flags_on_active_original_records':flags,
      'optional_selected_labels':[r['e'] for r in sel],
      'optional_selected_Q':sum(r['de'] for r in sel),'optional_D':B-sum(r['de'] for r in sel),
      'log_b_interval':[str(z) for z in log_bounds(b)]})

steps=[]
for old,new in zip(cuts,cuts[1:]):
    b=old['b'];B,D=old['B'],old['D'];db=new['B']-B
    born=[r for r in records if r['record'][6]==b and b+1<r['record'][8]]
    retired=[r for r in records if r['record'][6]<b and r['record'][8]==b+1]
    A=sum(r['de'] for r in born);R=sum(r['de'] for r in retired);delta=new['D']-D
    assert new['Q']-old['Q']==A-R and delta==db-A+R and db-A>=0
    normalized=F(new['D'],new['B'])-F(D,B)
    numerator=B*delta-D*db
    assert normalized==F(numerator,B*(B+db))
    so,sn=set(old['optional_selected_labels']),set(new['optional_selected_labels'])
    rawo,rawn=set(old['active_original_labels']),set(new['active_original_labels'])
    enter=(sn-so)&rawo&rawn;exit_=(so-sn)&rawo&rawn
    sb=[r for r in born if r['e'] in sn];sr=[r for r in retired if r['e'] in so]
    em=sum(r['de'] for r in records if r['e'] in enter);xm=sum(r['de'] for r in records if r['e'] in exit_)
    assert new['optional_selected_Q']-old['optional_selected_Q']==sum(r['de'] for r in sb)+em-sum(r['de'] for r in sr)-xm
    steps.append({'b_to_b_plus_1':[b,b+1],'new_bank_labels':sorted(set(new['bank_labels'])-set(old['bank_labels'])),
      'delta_B':db,'new_active_original_labels':[r['e'] for r in born],'new_active_mass_A':A,
      'retired_original_labels':[r['e'] for r in retired],'retired_mass_R':R,
      'unused_new_source_mass':db-A,'delta_D':delta,'raw_identity_and_nonnegativity':True,
      'delta_D_over_B_exact':str(normalized),'normalized_increment_numerator':numerator,
      'normalized_increment_denominator':B*(B+db),
      'optional_selector_entries_of_already_active_records':sorted(enter),
      'optional_selector_entry_mass':em,'optional_selector_exits_of_still_active_records':sorted(exit_),
      'optional_selector_exit_mass':xm,'optional_delta_D':new['optional_D']-old['optional_D']})
assert not unknown
out={'date':'2026-09-09','attempt':'A50','status':'PASS_EXACT_33_LABEL_25_CUT_REFERENCE',
 'input':source.name,'C_exact':'1','m0':2,'M':M,'T':T,'fixed_component_v':v,'fixed_source':[x,y,d],
 'fixed_integer_bin':[297,330],'cut_range_inclusive':[23,47],
 'bank_definition':'B_b=603 sum e over existing source pairs(w,z) with z<b; includes source overlaps and labels having no usable output. Absent source differences never enter.',
 'labels':labels,'original_strict_records':records,'cuts':cuts,'steps':steps,
 'raw_D_nondecreasing_in_this_scope':all(z['delta_D']>=0 for z in steps),
 'normalized_decrease_steps':[z for z in steps if F(z['delta_D_over_B_exact'])<0],
 'optional_selected_D_decrease_steps':[z for z in steps if z['optional_delta_D']<0],
 'genuine_lambda48_exact':str(lam),'full_tail_scope':'u28/u41/u43^[96] are exact original full prices for the fixed strict record subset with r<=48. They are separate from the component coefficient and from any k-dependent remainder-selected price. alpha97 is preserved.',
 'unknown_comparisons':unknown,
 'source_sha256':{p.name:sha(p) for p in (source,certpath,HERE/'reference_evaluator.py',Path(__file__))},
 'scope':'Only integer labels297..329, one source/bin/component and cuts23..47. No new source/bin/history or full-profile enumeration. Optional A46 flags use only the three recovered original records and are not part of the primary raw law.'}
(HERE/'A50_CUT_BANK_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'strict_records':[r['record'] for r in records],
 'first_three_cuts':[{q:c[q] for q in ['b','B','Q','D','D_over_B_exact','optional_selected_labels','optional_D']} for c in cuts[:3]],
 'normalized_decreases':[(s['b_to_b_plus_1'],s['delta_D_over_B_exact']) for s in out['normalized_decrease_steps']],
 'optional_D_decreases':[(s['b_to_b_plus_1'],s['optional_delta_D'],s['optional_selector_entries_of_already_active_records']) for s in out['optional_selected_D_decrease_steps']],
 'raw_nondecreasing':out['raw_D_nondecreasing_in_this_scope'],'unknown':len(unknown)},indent=2))

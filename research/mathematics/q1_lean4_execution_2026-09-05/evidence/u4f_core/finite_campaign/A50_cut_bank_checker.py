#!/usr/bin/env python3
"""Independent reverse lookups and fixed-point gates for the specified33 labels/cuts."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from independent_checker import log_fixed,decide,SCALE

HERE=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=HERE/'A50_CUT_BANK_EXACT.json';ref=json.loads(rp.read_text())
sp=HERE/ref['input'];data=json.loads(sp.read_text());assert sha(sp)==ref['source_sha256'][sp.name]
a=[None]+data['a'];idx={v:r for r,v in enumerate(data['a'],1)}
labels={};records={};strict_decisions={};unknown=[]
def signs(c,s,i,r,t):
    lc,uc=log_fixed(c);lr,ur=log_fixed(r)
    return {'older_birth':decide(s*lc**2,s*uc**2,c*SCALE**2),
      'birth_output_gap':decide((i-c)*lc**2,(i-c)*uc**2,c*SCALE**2),
      'output_top_gap':decide((r-i)*lr**3,(r-i)*ur**3,r*SCALE**3),
      'upper_rank':decide(c*lc,c*uc,r*SCALE),
      'physical_output':decide(t*lc**3,t*uc**3,c*c*SCALE**3)}
for e in range(297,330):
    source=[(idx[a[z]-e],z) for z in range(1,97) if a[z]-e in idx]
    t=603-e;output=[(idx[a[r]-t],r) for r in range(1,97) if a[r]-t in idx]
    assert len(source)<=1 and len(output)<=1
    old=next(j for j in ref['labels'] if j['e']==e)
    assert (None if not source else list(source[0]))==old['source_pair']
    assert (None if not output else list(output[0]))==old['output_pair']
    labels[e]=(None if not source else source[0],None if not output else output[0])
    if source:
        w,z=source[0];assert sorted({1,22}&{w,z})==old['source_overlap_with_fixed_pair']
    if source and output:
        w,z=source[0];i,r=output[0];c,s=max(22,z),min(22,z)
        if len({1,22,w,z,i,r})==6 and c<i and r<=48:
            try:flags=signs(c,s,i,r,t)
            except ArithmeticError:unknown.append({'e':e,'kind':'STRICT'});continue
            assert flags==old['strict_gate_decisions'];strict_decisions[e]=flags
            if all(flags.values()):records[e]=[603,e,1,22,w,z,c,s,i,r,t]
assert list(records)==[302,312,318]
assert list(records.values())==[r['record'] for r in ref['original_strict_records']]

def optional(record,b):
    d,e,x,y,w,z,c,s,i,r,t=record;lc,uc=log_fixed(b);m=48-b
    def decision(coefficient,power,target):
        return decide(coefficient*lc**power,coefficient*uc**power,target*SCALE**power)
    flags={'e_gt_b2_log_5over4':decision(e**4,5,b**8),
      't_gt_b2_log_5over2':decision(t*t,5,b**4),
      'central_above_short':decision(m**4,3,b**4),
      'central_below_far':decision(b**8,5,47**8),
      'near_span':decision(a[b]-a[1],2,a[48]-a[1]),
      'source_birth_support':decision(16*s**8,9,b**8)}
    quad=sorted((x,y,w,z));gaps=[a[v]-a[u] for u,v in zip(quad,quad[1:])]
    cl,cu=log_fixed(c)
    flags['original_all_large_old_gaps']=all(decide(g*cl**3,g*cu**3,c*c*SCALE**3) for g in gaps)
    for j,g in enumerate(gaps):flags['old_gap_'+str(j+1)+'_gt_b2_log_5over2']=decision(g*g,5,b**4)
    return flags

full_tails={}
for e,record in records.items():
    r=record[9]
    u=sum(((F(1,k*k*(k-1)**2)-F(1,k*k*(k+1)**2))/(a[k]-a[1])**2 for k in range(r,97)),F(0))
    saved=next(s for s in ref['original_strict_records'] if s['e']==e)
    assert str(u)==saved['u_r_M_exact'];full_tails[e]=u
lam=(F(1,48**2*47**2)-F(1,48**2*49**2))/(a[48]-a[1])**2
assert str(lam)==ref['genuine_lambda48_exact']
cuts=[]
for b in range(23,48):
    bank=[e for e,(source,_) in labels.items() if source and source[1]<b]
    active=[e for e,row in records.items() if row[6]<b<row[8]]
    B=603*sum(bank);Q=603*sum(active);D=B-Q
    saved=next(c for c in ref['cuts'] if c['b']==b)
    assert (bank,active,B,Q,D)==(saved['bank_labels'],saved['active_original_labels'],saved['B'],saved['Q'],saved['D'])
    assert str(F(D,B))==saved['D_over_B_exact']
    selected=[]
    for e in active:
        try:flags=optional(records[e],b)
        except ArithmeticError:unknown.append({'e':e,'b':b,'kind':'OPTIONAL'});continue
        assert flags==saved['optional_A46_flags_on_active_original_records'][str(e)]
        if all(flags.values()):selected.append(e)
    assert selected==saved['optional_selected_labels']
    W=sum((603*e*full_tails[e] for e in active),F(0))
    assert str(W)==saved['fixed_original_record_subset_full_tail_mass_exact']
    cuts.append({'b':b,'B':B,'Q':Q,'D':D,'active':active,'selected':selected,'optional_D':B-603*sum(selected)})
decreases=[];raw_steps=[]
for old,new,saved in zip(cuts,cuts[1:],ref['steps']):
    b=old['b'];newactive=set(new['active'])-set(old['active']);retired=set(old['active'])-set(new['active'])
    assert all(records[e][6]==b and b+1<records[e][8] for e in newactive)
    assert all(records[e][8]==b+1 for e in retired)
    dB=new['B']-old['B'];A=603*sum(newactive);R=603*sum(retired);dD=new['D']-old['D']
    assert dD==dB-A+R and dB-A>=0
    assert (dB,A,R,dD)==(saved['delta_B'],saved['new_active_mass_A'],saved['retired_mass_R'],saved['delta_D'])
    dn=F(new['D'],new['B'])-F(old['D'],old['B'])
    assert str(dn)==saved['delta_D_over_B_exact']
    assert dn==F(old['B']*dD-old['D']*dB,old['B']*new['B'])
    if dn<0:decreases.append({'cuts':[b,b+1],'exact_difference':str(dn)})
    raw_steps.append({'cuts':[b,b+1],'delta_B':dB,'new_active_mass':A,'retired_mass':R,'unused_new_source_mass':dB-A,'delta_D':dD})
assert not unknown and decreases==[{'cuts':[23,24],'exact_difference':'-20989/316448'}]
out={'date':'2026-09-09','attempt':'A50','status':'PASS_INDEPENDENT_33_LABEL_25_CUT_CHECK',
 'input':sp.name,'source_and_output_reverse_lookups':33,'matched_original_strict_records':list(records.values()),
 'strict_gate_decisions':strict_decisions,'verified_cuts':25,'verified_adjacent_steps':24,
 'raw_delta_identity_verified_at_all_steps':True,'raw_D_nondecreasing':True,
 'normalized_decrease_witnesses':decreases,'independent_raw_steps':raw_steps,
 'optional_selectors_independently_match':True,
 'optional_selected_D_counterexample':{'cuts':[23,24],'before':cuts[0]['optional_D'],'after':cuts[1]['optional_D'],
    'difference':cuts[1]['optional_D']-cuts[0]['optional_D'],'existing_records_entering_by_selector':[312,318],
    'new_original_record_source_birth':[302]},
 'genuine_original_prices_verified_via_alpha_differences':True,'component_lambda48_verified':True,
 'unknown_comparisons':unknown,'source_sha256':{p.name:sha(p) for p in (rp,sp,HERE/'independent_checker.py',Path(__file__))},
 'scope':'Independent reverse endpoint-value lookups, fixed-point log decisions, cut set differences and alpha-difference prices for exactly the specified33 labels/25cuts. No reference evaluator import, new bin/source/history, full profile or external search.'}
(HERE/'A50_CUT_BANK_INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k in ['status','verified_cuts','verified_adjacent_steps','raw_D_nondecreasing','normalized_decrease_witnesses','optional_selected_D_counterexample','unknown_comparisons']},indent=2))

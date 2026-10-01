#!/usr/bin/env python3
"""A53 applicability to three saved rows, then stop at first certified remainder record/cut."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import hashlib,json
from reference_evaluator import log_bounds,strict_positive,rank_core,physical_core
from independent_checker import log_fixed,SCALE,decide,rank_conditions,output_condition

HERE=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'C1_m02_dense_variant1_M96.json';certpath=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
bankpath=HERE/'C1_m02_dense_variant1_M96_records.json';boundpath=HERE/'A29_forbidden_output_packing_four_cells_exact.json'
threepath=HERE/'A50_CUT_BANK_EXACT.json'
data=json.loads(source.read_text());cert=json.loads(certpath.read_text());binding=json.loads(boundpath.read_text())
assert cert['status']=='PASS' and cert['input_sha256']==sha(source)
assert sha(bankpath)==binding['source_sha256'][bankpath.name]
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
a=[None]+data['a'];M=T=96;k=48;unknown=[]
def ceil_power(c,lo,hi):
    low=c**8*lo**5;high=c**8*hi**5
    left,right=0,1
    while right**8<high:right*=2
    while right-left>1:
        mid=(left+right)//2
        if mid**8<low:left=mid
        elif mid**8>=high:right=mid
        else:raise ArithmeticError('UNKNOWN birth threshold')
    assert (right-1)**8<low<=high<=right**8
    return right
@lru_cache(None)
def birth_bound(c):
    lo,hi=log_bounds(c);il,iu=log_fixed(c);ilo,ihi=F(il,SCALE),F(iu,SCALE)
    q=ceil_power(c,lo,hi);assert q==ceil_power(c,ilo,ihi)
    return {'c':c,'L_c':q+1,'ceil_f_c':q,'reference_log_interval':[str(lo),str(hi)],
      'independent_log_interval':[str(ilo),str(ihi)],
      'power_proof':{'statement':'(L-2)^8 < c^8(log c)^5 <= (L-1)^8',
        'left':(q-1)**8,'middle_lower':str(c**8*lo**5),'middle_upper':str(c**8*hi**5),'right':q**8}}
three=json.loads(threepath.read_text())['original_strict_records']
applies=[]
for rec in three:
    c=rec['record'][6];proof=birth_bound(c)
    applies.append({'e':rec['e'],'record':rec['record'],'birth_c':c,'L_c':proof['L_c'],
      'k48_paid_by_A53':48>=proof['L_c'],'genuine_selected_tail_begins_at':max(rec['record'][9],proof['L_c'])})
assert all(r['k48_paid_by_A53'] for r in applies)

def flags(row,b,independent=False):
    d,e,x,y,w,z,c,s,i,r,t=row
    if independent:
        li,ui=log_fixed(b);lo,hi=F(li,SCALE),F(ui,SCALE)
        ci,cu=log_fixed(c);cl,ch=F(ci,SCALE),F(cu,SCALE)
    else:lo,hi=log_bounds(b);cl,ch=log_bounds(c)
    quad=sorted((x,y,w,z));gaps=[a[v]-a[u] for u,v in zip(quad,quad[1:])]
    vals={'central_above_short':[(k-b)**4*lo**3,(k-b)**4*hi**3,b**4],
      'central_below_far':[b**8*lo**5,b**8*hi**5,(k-1)**8],
      'near_span':[(a[b]-a[1])*lo**2,(a[b]-a[1])*hi**2,a[k]-a[1]],
      'small_source_removed':[e**4*lo**5,e**4*hi**5,b**8],
      'small_output_removed':[t*t*lo**5,t*t*hi**5,b**4],
      'source_birth_support':[16*s**8*lo**9,16*s**8*hi**9,b**8]}
    for j,g in enumerate(gaps):
        vals['gap_'+str(j+1)+'_small_removed']=[g*g*lo**5,g*g*hi**5,b**4]
        vals['gap_'+str(j+1)+'_original_large']=[g*cl**3,g*ch**3,c*c]
    if independent:
        result={name:decide(*v) for name,v in vals.items()}
    else:
        result={name:strict_positive(*v) for name,v in vals.items()}
    return result,quad,gaps

records=json.loads(bankpath.read_text())['records']
counts={'stored_records_visited':0,'records_with_r_le48':0,'birth_tail_already_paid_records':0,
        'candidate_original_covered_cuts_tested':0}
winner=None
for bank_index,row in enumerate(records):
    counts['stored_records_visited']+=1
    if row[9]>k:continue
    counts['records_with_r_le48']+=1
    c=row[6]
    try:proof=birth_bound(c)
    except ArithmeticError:unknown.append({'bank_index':bank_index,'kind':'BIRTH_THRESHOLD'});continue
    if k>=proof['L_c']:
        counts['birth_tail_already_paid_records']+=1;continue
    for b in range(max(4,c+1),row[8]):
        counts['candidate_original_covered_cuts_tested']+=1
        ff,quad,gaps=flags(row,b)
        if None in ff.values():unknown.append({'bank_index':bank_index,'b':b,'kind':'A46_SELECTOR'});continue
        if not all(ff.values()):continue
        independent_flags,iq,ig=flags(row,b,True)
        assert independent_flags==ff and iq==quad and ig==gaps
        d,e,x,y,w,z,c,s,i,r,t=row
        assert len({x,y,w,z,i,r})==6 and c<b<i<r<=k
        assert d==a[y]-a[x] and e==a[z]-a[w] and t==a[r]-a[i]==d-e>0
        assert rank_core(c,s,i,r) is True and physical_core(c,t) is True
        assert rank_conditions(c,s,i,r) and output_condition(c,t)
        value_rank={value:rank for rank,value in enumerate(data['a'],1)}
        recovery={}
        for label,pair in [(d,[x,y]),(e,[w,z]),(t,[i,r])]:
            found=[[j,value_rank[a[j]+label]] for j in range(1,97) if a[j]+label in value_rank]
            assert found==[pair];recovery[str(label)]=found[0]
        lc,uc=log_bounds(c);lr,ur=log_bounds(r)
        margins={'older_birth':[s*lc**2-c,s*uc**2-c],
          'birth_output_gap':[(i-c)*lc**2-c,(i-c)*uc**2-c],
          'output_top_gap':[(r-i)*lr**3-r,(r-i)*ur**3-r],
          'upper_rank':[c*lc-r,c*uc-r],
          'physical_output':[t*lc**3-c*c,t*uc**3-c*c]}
        def tail(q):return sum((F(4,j*(j*j-1)**2*(a[j]-a[1])**2) for j in range(q,97)),F(0))
        original=tail(r);L=proof['L_c'];paid=tail(max(r,L));remaining=original-paid
        original_ind=sum(((F(1,j*j*(j-1)**2)-F(1,j*j*(j+1)**2))/(a[j]-a[1])**2 for j in range(r,97)),F(0))
        assert original==original_ind and remaining>0
        lam=F(4,k*(k*k-1)**2*(a[k]-a[1])**2)
        winner={'original_bank_index':bank_index,'record':row,'b':b,'k':k,'birth_c':c,'L_c':L,
          'A53_unpaid_at_component':k<L,'A46_6_and_original_large_flags':ff,
          'source_endpoint_values':[a[j] for j in [x,y,w,z]],'output_values':[a[i],a[r]],
          'old_quad':quad,'old_gaps':gaps,'de':d*e,'original_covered_cut_interval_inclusive':[c+1,i-1],
          'strict_margin_intervals':{name:[str(q) for q in vv] for name,vv in margins.items()},
          'reference_and_independent_log_intervals_at_cut':[list(map(str,log_bounds(b))),[str(F(q,SCALE)) for q in log_fixed(b)]],
          'unique_physical_endpoint_recovery':recovery,'lambda48_exact':str(lam),'component_mass_exact':str(lam*d*e),
          'original_u_r_96_exact':str(original),'A53_paid_part_u_exact':str(paid),'A53_unpaid_part_u_exact':str(remaining),
          'price_scope':'Original full u_r^[96] is distinct from lambda48. The A53-only split sums original finite components; its unpaid part is not asserted to satisfy the cut-dependent A46 selectors at every component.'}
        break
    if winner is not None:break
out={'date':'2026-09-09','attempt':'A53_EXISTING_RESTART_WITNESS','status':'PASS_FIRST_CERTIFIED_REMAINDER_WITNESS' if winner else 'NO_WITNESS_IN_FIXED_STORED_BANK_SCAN',
 'input':source.name,'C_exact':'1','m0':2,'M':M,'T':T,'component_k':k,'p_exact':'5/8',
 'three_A50_records_birth_tail_applicability':applies,
 'birth_threshold_certificates':{str(c):birth_bound(c) for c in sorted({22,23}|({winner['birth_c']} if winner else set()))},
 'scan_order':'Original stored record-bank order; filter r<=48, then covered integer cuts in increasing order. Stop immediately on first certified passing record/cut.',
 'scan_counts':counts,'witness':winner,'unknown_comparisons_before_stop':unknown,
 'independent_checks':'Dual rational log enclosures, direct actual endpoint recovery, independent original strict gates, and two formulas for the winner original genuine tail.',
 'source_sha256':{p.name:sha(p) for p in (source,certpath,bankpath,boundpath,threepath,HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__))},
 'scope':'A separate A53 restart check, not an extension of the A50 fixed-bin trace. No new history, full-profile reevaluation, broad bin scan or continued witness search after the first passing record/cut. The witness establishes nonemptiness only at this one existing finite component.'}
(HERE/'A53_EXISTING_RESTART_WITNESS_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'A50_applicability':[(r['e'],r['birth_c'],r['L_c'],r['k48_paid_by_A53']) for r in applies],
 'counts':counts,'winner':None if not winner else {q:winner[q] for q in ['original_bank_index','record','b','k','birth_c','L_c','old_gaps','de']},
 'unknown':len(unknown)},indent=2))

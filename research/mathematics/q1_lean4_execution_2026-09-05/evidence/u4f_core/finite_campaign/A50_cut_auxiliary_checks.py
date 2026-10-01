#!/usr/bin/env python3
"""Existing trace only: selector applicability at23/24 and first moving-price failure."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from reference_evaluator import log_bounds
from independent_checker import log_fixed,SCALE

HERE=Path(__file__).resolve().parent;sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rp=HERE/'A50_CUT_BANK_EXACT.json';cp=HERE/'A50_CUT_BANK_INDEPENDENT_CHECK.json'
ref=json.loads(rp.read_text());check=json.loads(cp.read_text())
assert check['status']=='PASS_INDEPENDENT_33_LABEL_25_CUT_CHECK'
assert check['source_sha256'][rp.name]==sha(rp)
source=HERE/ref['input'];data=json.loads(source.read_text());a=[None]+data['a']
assert sha(source)==ref['source_sha256'][source.name]
def floor_inverse(base,power,root,lo,hi):
    left,right=0,base+1
    while right-left>1:
        mid=(left+right)//2
        if mid**root*hi**power<=base**root:left=mid
        elif mid**root*lo**power>base**root:right=mid
        else:raise ArithmeticError('UNKNOWN threshold')
    assert left**root*hi**power<=base**root<(left+1)**root*lo**power
    return left
selector_scope=[]
for b in (23,24):
    lo,hi=log_bounds(b);il,iu=log_fixed(b);ilo,ihi=F(il,SCALE),F(iu,SCALE)
    J=floor_inverse(b*b,5,2,lo,hi);L=floor_inverse(b*b,5,4,lo,hi)
    assert J==floor_inverse(b*b,5,2,ilo,ihi) and L==floor_inverse(b*b,5,4,ilo,ihi)
    cut=next(c for c in ref['cuts'] if c['b']==b)
    perrecord=[]
    for rec in ref['original_strict_records']:
        e=rec['e'];r=rec['record'];s=r[7]
        perrecord.append({'e':e,'earlier_source_birth_s':s,'source_s_ge_m0':s>=2,
          'raw_record_covers_cut':r[6]<b<r[8],
          'old_quad_ranks':rec['old_quad'],'actual_old_quad_values':[a[j] for j in rec['old_quad']],
          'adjacent_old_gaps':rec['old_gaps'],'output_t':r[10],
          'small_source_cutoff_L':L,'all_gaps_gt_J':all(g>J for g in rec['old_gaps']),
          'e_gt_L':e>L,'t_gt_J':r[10]>J,
          'displayed_A46_6_flags_if_originally_active':cut['optional_A46_flags_on_active_original_records'].get(str(e))})
    selector_scope.append({'b':b,'J_b':J,'L_b':L,'reference_log_interval':[str(lo),str(hi)],
      'independent_log_interval':[str(ilo),str(ihi)],
      'J_proof':{'inequality':'J^2(log b)^5 <= b^4 < (J+1)^2(log b)^5','left_upper':str(J*J*hi**5),'middle':b**4,'right_lower':str((J+1)**2*lo**5)},
      'L_proof':{'inequality':'L^4(log b)^5 <= b^8 < (L+1)^4(log b)^5','left_upper':str(L**4*hi**5),'middle':b**8,'right_lower':str((L+1)**4*lo**5)},
      'initial_case_input_checks':{'M_ge_m0':96>=2,'b_ge_max_3_m0':b>=3,
        'C_exact':'1','m0':2,'all_existing_three_source_births_ge_m0':True,
        'same_fixed_all_rank_cap_certificate_reused':True,
        'no_additional_large_b_asymptotic_threshold_needed_for_displayed_A45_A46_conditions':True},
      'records':perrecord})

candidate=None
for old,new in zip(ref['cuts'],ref['cuts'][1:]):
    if old['B']==new['B'] and old['fixed_original_record_subset_full_tail_mass_exact']==new['fixed_original_record_subset_full_tail_mass_exact']:
        candidate=(old,new);break
assert candidate is not None
old,new=candidate;b=old['b'];assert (b,new['b'])==(25,26)
def tail(r):
    return sum((F(4,k*(k*k-1)**2*(a[k]-a[1])**2) for k in range(r,97)),F(0))
def tail_independent(r):
    return sum(((F(1,k*k*(k-1)**2)-F(1,k*k*(k+1)**2))/(a[k]-a[1])**2 for k in range(r,97)),F(0))
B=old['B'];P=F(old['fixed_original_record_subset_full_tail_mass_exact'])
u=tail(b+1);un=tail(b+2)
assert u==tail_independent(b+1) and un==tail_independent(b+2)
moving_lambda=F(4,(b+1)*((b+1)**2-1)**2*(a[b+1]-a[1])**2)
F_before=B*u-P;F_after=B*un-P
assert F_after-F_before==-moving_lambda*B<0
out={'date':'2026-09-09','attempt':'A50_AUXILIARY','status':'PASS_EXACT_EXISTING_TRACE_AUXILIARY_CHECKS',
 'input':source.name,'selector_scope':{
   'checked_predicate':'Every displayed A46.6 necessary condition, plus the original all-three-old-gaps-large flag, on active original records. This is not merely central/near selection.',
   'all_rank_cap':'Reuse certified fixed C1,m02 M96 input; no cap belowm0 or prefix extension is assumed.',
   'initial_conditions':'b23/24>=max(3,m0), M>=m0, and all three earlier source births>=m0. Thus the initial-cut/early-source exceptions to the displayed A45/A46 implications do not occur here.',
   'logical_boundary':'PASS of displayed necessary conditions does not certify that no other historically paid subset could contain the record or that a global unproved remainder theorem holds.',
   'two_cuts':selector_scope,
   'negative_selected_deficit_event':{'cuts':[23,24],'D_selected_before':2056230,'D_selected_after':1676340,
     'delta':-379890,'original_new_source_record':[302],'previously_active_records_entering_only_by_selector':[312,318],
     'cause':'k48 fails the central-below-far test at b23 and passes all displayed conditions at b24; no original strict gate changes.'}},
 'moving_cut_price_counterexample':{'output_record_subset':'Only fixed original strict records with r<=48, priced by original full u_r^[96]. No assertion that this is the entire bin profile through output T96.',
   'component_expansion':'P_b_subset=sum_{k=b+1}^{96} lambda_k Q_b(min(k,48)); original alpha97 preserved.',
   'cut_step':[b,b+1],'B_b':B,'B_b_plus_1':B,'active_labels_before':old['active_original_labels'],'active_labels_after':new['active_original_labels'],
   'P_b_equals_P_b_plus_1_exact':str(P),'F_definition':'F_b=B_b*u_(b+1)^[96]-P_b_subset',
   'u_b_plus_1_exact':str(u),'u_b_plus_2_exact':str(un),
   'F_before_exact':str(F_before),'F_after_exact':str(F_after),
   'lambda_b_plus_1_exact':str(moving_lambda),'negative_increment_exact':str(F_after-F_before),
   'identity':'F_(b+1)-F_b=-lambda_(b+1)*B_b<0 when DeltaB=0 and P is unchanged.',
   'genuine_lambda48_exact':ref['genuine_lambda48_exact'],
   'price_distinction':'The negative step uses lambda26, not the fixed component lambda48. B*u_(b+1) is an auxiliary upper allowance, not an invented genuine price for unused labels.'},
 'unknown_comparisons':[],
 'source_sha256':{p.name:sha(p) for p in (rp,cp,source,HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__))},
 'scope':'Existing33-label/three-record/25-cut trace only. Two cut thresholds and the first unchanged-bank/unchanged-actual-mass step; no additional source, bin, history, profile scan or asymptotic construction.'}
(HERE/'A50_AUXILIARY_CUT_COUNTEREXAMPLES.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'thresholds':[(c['b'],c['J_b'],c['L_b']) for c in selector_scope],
  'moving_price_step':[b,b+1],'B':B,'lambda26':str(moving_lambda),'negative_F_increment':str(F_after-F_before)},indent=2))

#!/usr/bin/env python3
"""A32: only prescribed b24/25, v29/30/47/48 cells from existing A29 data."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
CELLS = tuple((b,v) for b in (24,25) for v in (29,30,47,48))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def kernel_pack(U, h, H, ell):
    chosen = U[:h]
    value = sum((F(H-t,H) for t in chosen), F(0))
    Uset = set(U)
    cumulative = 0
    numerator = 0
    prefix = []
    for j in range(ell,H):
        cumulative += j in Uset
        count = min(h,cumulative)
        numerator += count
        prefix.append([j,cumulative,count])
    assert value == F(numerator,H)
    return value,chosen,prefix


ap = HERE/'A29_forbidden_output_packing_four_cells_exact.json'
mp = HERE/'A29_forbidden_output_packing_manifest.json'
old = json.loads(ap.read_text())
manifest = json.loads(mp.read_text())
assert digest(ap) == manifest['source_and_evidence_sha256'][str(ap)]
for name in ('C1_m02_dense_variant1_M96.json',
             'C1_m02_dense_variant1_M96_records.json',
             'C1_m02_dense_variant1_M96_independent_check.json'):
    assert digest(HERE/name) == old['source_sha256'][name]
data_path = HERE/'C1_m02_dense_variant1_M96.json'
cert_path = HERE/'C1_m02_dense_variant1_M96_independent_check.json'
data = json.loads(data_path.read_text())
cert = json.loads(cert_path.read_text())
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
assert cert['status']=='PASS' and cert['input_sha256']==digest(data_path)
a = [None]+old['actual_prefix_through48']
assert a[1:] == data['a'][:48]
pool = {int(index):row for index,row in old['original_core_record_pool'].items()}
old_cells = {(x['b'],x['k']):x for x in old['cells']}
results = {}

for b,v in CELLS:
    cut = old['cut_data'][str(b)]
    H,S,ell = cut['H_b'],cut['S_old_difference_square_sum'],cut['ell']
    low,high = map(F,cut['L_b_interval_exact'])
    assert low.numerator//low.denominator == high.numerator//high.denominator == ell-1
    D = {int(t):tuple(pair) for t,pair in cut['old_difference_endpoint_map'].items()}
    assert S == sum(t*t for t in D)
    m = v-b
    h = m*(m-1)//2
    past = {}
    for p in range(1,b+1):
        for q in range(p+1,b+1):
            t = a[q]-a[p]
            assert t>0 and t not in past
            past[t] = (p,q)
    mixed = {}
    for p in range(1,b+1):
        for f in range(b+1,v+1):
            t = a[f]-a[p]
            assert t>0 and t not in past and t not in mixed
            mixed[t] = (p,f)
    forbidden = past | mixed
    assert len(forbidden) == b*(b-1)//2+b*m
    assert D.keys() <= past.keys()
    future = {}
    for i in range(b+1,v+1):
        for r in range(i+1,v+1):
            t = a[r]-a[i]
            assert t>0 and t not in future and t not in forbidden
            future[t] = (i,r)
    assert len(future)==h
    assert len(forbidden)+len(future)==v*(v-1)//2
    U = [t for t in range(ell,H) if t not in forbidden]
    FU,chosen,prefix = kernel_pack(U,h,H,ell)
    FD,_,_ = kernel_pack(cut['allowed_integer_labels_U'],h,H,ell)
    L = sum((F(H-t,H) for t in future if ell<=t<H),F(0))
    active = [index for index,row in pool.items() if row[6]<b<row[8] and row[9]<=v]
    Q = sum(pool[index][0]*pool[index][1] for index in active)
    larger = {}
    K = {}
    for index in active:
        d,e,pd,qd,pe,qe,c,s,i,r,t = pool[index]
        assert d in D and e in D and t in future and future[t]==(i,r)
        assert ell<=t<H and d not in larger.setdefault(t,set())
        larger[t].add(d)
        K[t] = K.get(t,0)+d*e
    assert Q == sum(K.values())
    assert all(F(x)<=S*F(H-t,H) for t,x in K.items())
    assert F(Q)<=S*L<=S*FU<=S*FD
    price = (F(1,v*v*(v-1)**2)-F(1,v*v*(v+1)**2))/(a[v]-a[1])**2
    reuse = v in (47,48)
    if reuse:
        prior = old_cells[(b,v)]
        assert FD == F(prior['FD_selected_labels_exact'])
        assert L == F(prior['actual_future_kernel_L_exact'])
        assert Q == prior['Q_actual_core_unpriced']
        assert price == F(prior['genuine_component_price_exact'])
        assert active == prior['original_core_bank_indices']
    results[(b,v)] = {'b':b,'v':v,'M':96,'T':96,'H_b':H,'H_v':a[v]-a[1],
       'ell':ell,'ell_interval_certificate_reused_from_A29':True,'S_source_first_b_minus_1':S,
       'source_D_count':len(D),'past_point_count':b,'m_future_points':m,'h_future_internal_pairs':h,
       'past_internal_difference_endpoint_map':dict(sorted(past.items())),
       'mixed_difference_endpoint_map':dict(sorted(mixed.items())),
       'joint_forbidden_count':len(forbidden),'eligible_joint_forbidden_labels':sorted(t for t in forbidden if ell<=t<H),
       'future_internal_difference_endpoint_map':dict(sorted(future.items())),
       'actual_Sidon_disjointness_and_pair_counts':'PASS',
       'allowed_U':U,'allowed_U_count':len(U),'selected_smallest_allowed_labels':chosen,
       'selected_kernel_FU_exact':str(FU),'cumulative_prefix_rows_j_card_min':prefix,
       'cumulative_formula_status':'PASS_EXACT_RATIONAL',
       'old_source_only_FD_exact':str(FD),'actual_future_kernel_L_exact':str(L),
       'joint_forbidden_gain_FD_minus_FU_exact':str(FD-FU),
       'E_joint_exact':str(FU-L),'A29_source_only_values_reused_and_checked':reuse,
       'core_count':len(active),'Q_original_core_unpriced':Q,'core_original_bank_indices':active,
       'strict_core_evidence':'All selected rows are from the unchanged A29 independently strict-checked original record pool.',
       'chain_Q_SL_SFU_SFD_exact':[str(F(Q)),str(S*L),str(S*FU),str(S*FD)],
       'genuine_component_price_exact':str(price),
       'priced_chain_Q_SL_SFU_SFD_exact':[str(price*x) for x in (Q,S*L,S*FU,S*FD)],
       'chain_status':'PASS_EXACT_RATIONAL'}

# One actual new-point difference bank per appended rank, reused at both cuts.
new_point_banks = {}
for r in (30,48):
    bank = {}
    for i in range(1,r):
        t = a[r]-a[i]
        assert t>0 and t not in bank
        bank[t]=(i,r)
    new_point_banks[r] = bank

increments = []
for b in (24,25):
    for v in (29,47):
        before,after = results[(b,v)],results[(b,v+1)]
        H,ell,m,h = before['H_b'],before['ell'],before['m_future_points'],before['h_future_internal_pairs']
        assert after['h_future_internal_pairs']==h+m
        bank = new_point_banks[v+1]
        C = {t:pair for t,pair in bank.items() if pair[0]<=b}
        new_future = {t:pair for t,pair in bank.items() if pair[0]>b}
        assert len(C)==b and len(new_future)==m and C.keys().isdisjoint(new_future)
        assert C.keys() | new_future.keys() == bank.keys()
        old_forbidden = before['past_internal_difference_endpoint_map'] | before['mixed_difference_endpoint_map']
        new_forbidden = after['past_internal_difference_endpoint_map'] | after['mixed_difference_endpoint_map']
        assert C.keys().isdisjoint(old_forbidden)
        assert new_forbidden == old_forbidden | C
        old_future = before['future_internal_difference_endpoint_map']
        assert new_future.keys().isdisjoint(old_future)
        assert after['future_internal_difference_endpoint_map'] == old_future | new_future
        assert after['allowed_U']==[t for t in before['allowed_U'] if t not in C]
        hypothetical,old_selected,_ = kernel_pack(before['allowed_U'],h+m,H,ell)
        A = hypothetical-F(before['selected_kernel_FU_exact'])
        R = hypothetical-F(after['selected_kernel_FU_exact'])
        J = sum((F(H-t,H) for t in new_future if ell<=t<H),F(0))
        mixed_mass = sum((F(H-t,H) for t in C if ell<=t<H),F(0))
        assert A>=0 and R>=0 and J>=0
        assert R<=mixed_mass
        assert J == F(after['actual_future_kernel_L_exact'])-F(before['actual_future_kernel_L_exact'])
        delta_E = F(after['E_joint_exact'])-F(before['E_joint_exact'])
        assert delta_E==A-R-J
        increments.append({'b':b,'v_before':v,'new_point_rank':v+1,'old_m':m,'old_h':h,'new_h':h+m,
           'common_actual_new_difference_bank_reference':v+1,
           'new_mixed_forbidden_C_labels':sorted(C),'new_mixed_forbidden_C_count':len(C),
           'eligible_new_forbidden_C_labels':sorted(t for t in C if ell<=t<H),
           'new_future_difference_labels':sorted(new_future),'new_future_difference_count':len(new_future),
           'eligible_positive_new_future_labels':sorted(t for t in new_future if ell<=t<H),
           'old_allowed_packing_at_new_h_exact':str(hypothetical),
           'new_C_deleted_from_old_selected_at_new_h':sorted(set(old_selected)&C.keys()),
           'capacity_gain_A_exact':str(A),'forbidden_loss_R_exact':str(R),'new_future_kernel_J_exact':str(J),
           'new_mixed_total_kernel_mass_exact':str(mixed_mass),
           'R_le_new_mixed_mass':R<=mixed_mass,'R_ge_new_mixed_mass_candidate':R>=mixed_mass,
           'E_before_exact':before['E_joint_exact'],'E_after_exact':after['E_joint_exact'],
           'delta_E_exact':str(delta_E),
           'delta_E_sign':'POSITIVE' if delta_E>0 else 'NEGATIVE' if delta_E<0 else 'ZERO',
           'identity_A_minus_R_minus_J':'PASS_EXACT_RATIONAL',
           'scope':'Unpriced kernel deficit at one fixed cut; each cell retains its own genuine component coefficient. No monotonicity is assumed.'})

out={'date':'2026-09-09','attempt':'A32','input':'C1_m02_dense_variant1_M96','C_exact':'1','m0':2,'M':96,'T':96,
     'specified_cells':[list(x) for x in CELLS],'cells':[results[x] for x in CELLS],
     'actual_new_point_difference_banks':{r:dict(sorted(bank.items())) for r,bank in new_point_banks.items()},
     'increments':increments,
     'core_pool_reference':{'path':ap.name,'json_key':'original_core_record_pool','sha256':digest(ap)},
     'strict_ell_reference':{'path':ap.name,'json_key':'cut_data','sha256':digest(ap)},
     'source_sha256':{str(x.relative_to(HERE)):digest(x) for x in (ap,mp,data_path,cert_path,Path(__file__))},
     'original_A29_source_sha256':old['source_sha256'],'frozen_source_sha256':old['frozen_source_sha256'],
     'scope':'Exactly eight prescribed cells and four prescribed new-point/cut increments in one existing certified C1,m02 M96 history. Reuses A29 strict-log certificates and original core pool. No new history, broader scan, full-horizon evaluation or general monotonicity claim.'}
dest=HERE/'A32_joint_forbidden_eight_cells_exact.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cells':[{key:x[key] for key in ['b','v','h_future_internal_pairs','allowed_U_count','core_count','Q_original_core_unpriced','actual_future_kernel_L_exact','selected_kernel_FU_exact','old_source_only_FD_exact','E_joint_exact','genuine_component_price_exact']} for x in out['cells']],
                 'increments':[{key:x[key] for key in ['b','v_before','new_point_rank','old_m','eligible_new_forbidden_C_labels','eligible_positive_new_future_labels','capacity_gain_A_exact','forbidden_loss_R_exact','new_future_kernel_J_exact','new_mixed_total_kernel_mass_exact','R_ge_new_mixed_mass_candidate','E_before_exact','E_after_exact','delta_E_exact','delta_E_sign']} for x in increments]},indent=2))

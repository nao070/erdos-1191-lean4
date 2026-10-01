#!/usr/bin/env python3
"""Exactly four prescribed cells in the already certified variant M96."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from independent_checker import SCALE, log_fixed, output_condition, rank_conditions

HERE = Path(__file__).resolve().parent
STEM = 'C1_m02_dense_variant1_M96'
CELLS = ((24,47),(24,48),(25,47),(25,48))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


dp = HERE/(STEM+'.json')
rp = HERE/(STEM+'_records.json')
cp = HERE/(STEM+'_independent_check.json')
binding = HERE/'integer_middle_gap_signed_measure_existing_exact.json'
prior = json.loads(binding.read_text())
for path in (dp,rp,cp,HERE/'independent_checker.py'):
    assert digest(path) == prior['source_sha256'][path.name]
data = json.loads(dp.read_text())
cert = json.loads(cp.read_text())
assert cert['status'] == 'PASS' and cert['input_sha256'] == digest(dp)
assert data['C_exact'] == '1' and data['m0'] == 2
assert data['M'] == data['T'] == 96
a = [None]+data['a']
rows = json.loads(rp.read_text())['records']
assert len(rows) == data['core_records']

cut_data = {}
for b in (24,25):
    H = a[b]-a[1]
    lo,hi = log_fixed(b)
    Llo = F(b*b*SCALE**5,hi**5)
    Lhi = F(b*b*SCALE**5,lo**5)
    f0,f1 = Llo.numerator//Llo.denominator,Lhi.numerator//Lhi.denominator
    assert f0 == f1
    ell = f0+1
    D = {}
    for i in range(1,b):
        for r in range(i+1,b):
            t = a[r]-a[i]
            assert t > 0 and t not in D
            D[t] = (i,r)
    S = sum(d*d for d in D)
    U = [t for t in range(ell,H) if t not in D]
    cut_data[b] = {'b':b,'H_b':H,'S_old_difference_square_sum':S,
       'old_difference_count':len(D),'old_difference_endpoint_map':dict(sorted(D.items())),
       'log_b_interval_exact':[str(F(lo,SCALE)),str(F(hi,SCALE))],
       'L_b_interval_exact':[str(Llo),str(Lhi)],'L_b_floor_certified':f0,'ell':ell,
       'ell_status':'CERTIFIED_INTERVAL_UNKNOWN0','allowed_integer_labels_U':U,'U_size':len(U)}

# Read existing core rows once; later cells only filter this existing bank.
core_pool = {}
for index,row in enumerate(rows):
    d,e,pd,qd,pe,qe,c,s,i,r,t = row
    if r > 48 or not any(c < b < i for b in (24,25)):
        continue
    assert len({pd,qd,pe,qe,i,r}) == 6
    assert rank_conditions(c,s,i,r) and output_condition(c,t)
    assert a[qd]-a[pd] == d and a[qe]-a[pe] == e
    assert d-e == a[r]-a[i] == t
    core_pool[index] = row

results = {}
for b,k in CELLS:
    info = cut_data[b]
    H,S,ell = info['H_b'],info['S_old_difference_square_sum'],info['ell']
    D = info['old_difference_endpoint_map']
    U = info['allowed_integer_labels_U']
    m = k-b
    h = m*(m-1)//2
    future = {}
    for i in range(b+1,k+1):
        for r in range(i+1,k+1):
            t = a[r]-a[i]
            assert t > 0 and t not in future and t not in D
            future[t] = (i,r)
    assert len(future) == h
    chosen = U[:h]
    FD = sum((F(H-t,H) for t in chosen),F(0))
    count = 0
    cumulative_rows = []
    cumulative_numerator = 0
    for j in range(ell,H):
        if j not in D:
            count += 1
        truncated = min(h,count)
        cumulative_numerator += truncated
        cumulative_rows.append([j,count,truncated])
    assert FD == F(cumulative_numerator,H)
    z = min(h,max(0,H-ell))
    Fold = z*(1-F(ell,H))-F(z*(z-1),2*H)
    L = sum((F(H-t,H) for t in future if ell <= t < H),F(0))
    active_ids = [idx for idx,row in core_pool.items() if row[6] < b < row[8] and row[9] <= k]
    Q = sum(core_pool[idx][0]*core_pool[idx][1] for idx in active_ids)
    larger_at_output = {}
    K = {}
    for idx in active_ids:
        d,e,pd,qd,pe,qe,c,s,i,r,t = core_pool[idx]
        assert d in D and e in D and t in future and future[t] == (i,r)
        assert ell <= t < H
        assert d not in larger_at_output.setdefault(t,set())
        larger_at_output[t].add(d)
        K[t] = K.get(t,0)+d*e
    assert Q == sum(K.values())
    assert all(F(value) <= S*F(H-t,H) for t,value in K.items())
    assert F(Q) <= S*L <= S*FD <= S*Fold
    assert 0 <= L <= FD <= Fold
    price = (F(1,k*k*(k-1)**2)-F(1,k*k*(k+1)**2))/(a[k]-a[1])**2
    results[(b,k)] = {'b':b,'k':k,'T':96,'m_future_points':m,'h_future_pairs':h,
       'H_b':H,'H_k':a[k]-a[1],'ell':ell,'S':S,
       'future_difference_endpoint_map':dict(sorted(future.items())),
       'future_vs_old_differences_disjoint':'PASS_ACTUAL_ENDPOINTS',
       'future_positive_kernel_labels':sorted(t for t in future if ell <= t < H),
       'chosen_smallest_allowed_U':chosen,'chosen_label_count':len(chosen),
       'FD_selected_labels_exact':str(FD),'FD_cumulative_rank_exact':str(F(cumulative_numerator,H)),
       'cumulative_rank_rows_j_count_min':cumulative_rows,
       'old_integer_F_exact':str(Fold),'actual_future_kernel_L_exact':str(L),
       'old_forbidden_label_gain_F_minus_FD_exact':str(Fold-FD),
       'remaining_output_deficit_E_exact':str(FD-L),
       'original_core_record_count':len(active_ids),'original_core_bank_indices':active_ids,
       'original_core_K_by_output':dict(sorted(K.items())),
       'Q_actual_core_unpriced':Q,
       'chain_Q_SL_SFD_SF_exact':[str(F(Q)),str(S*L),str(S*FD),str(S*Fold)],
       'chain_status':'PASS_EXACT_RATIONAL',
       'genuine_component_price_exact':str(price),
       'priced_chain_Q_SL_SFD_SF_exact':[str(price*x) for x in (Q,S*L,S*FD,S*Fold)],
       'original_strict_gate_recheck':'PASS_UNKNOWN0'}

increments = []
for b in (24,25):
    before,after = results[(b,47)],results[(b,48)]
    old = before['future_difference_endpoint_map']
    new = after['future_difference_endpoint_map']
    new_bank = {a[48]-a[i]:(i,48) for i in range(b+1,48)}
    assert len(new_bank) == 47-b
    assert old.keys().isdisjoint(new_bank)
    assert new.keys() == old.keys() | new_bank.keys()
    assert all(new[t] == pair for t,pair in new_bank.items())
    H,ell = after['H_b'],after['ell']
    delta_L = sum((F(H-t,H) for t in new_bank if ell <= t < H),F(0))
    assert delta_L == F(after['actual_future_kernel_L_exact'])-F(before['actual_future_kernel_L_exact'])
    newly_chosen = after['chosen_smallest_allowed_U'][len(before['chosen_smallest_allowed_U']):]
    delta_FD = sum((F(H-t,H) for t in newly_chosen),F(0))
    assert delta_FD == F(after['FD_selected_labels_exact'])-F(before['FD_selected_labels_exact'])
    delta_E = delta_FD-delta_L
    assert delta_E == F(after['remaining_output_deficit_E_exact'])-F(before['remaining_output_deficit_E_exact'])
    increments.append({'b':b,'k_before':47,'k_after':48,
       'h_increment':after['h_future_pairs']-before['h_future_pairs'],
       'new_future_difference_endpoint_map':dict(sorted(new_bank.items())),
       'new_future_positive_kernel_labels':sorted(t for t in new_bank if ell <= t < H),
       'newly_chosen_allowed_packing_slots':newly_chosen,
       'delta_FD_exact':str(delta_FD),'delta_L_exact':str(delta_L),'delta_E_exact':str(delta_E),
       'delta_E_sign':'POSITIVE' if delta_E > 0 else 'NEGATIVE' if delta_E < 0 else 'ZERO',
       'E_increment_identity':'PASS_EXACT_RATIONAL',
       'scope':'One specified future-point addition only. Raw E increments are unpriced; the separate genuine component prices differ between k47 and k48.'})

out = {'date':'2026-09-09','attempt':'A29','input':STEM,'C_exact':'1','m0':2,'M':96,'T':96,
       'specified_cells':[list(x) for x in CELLS],
       'actual_prefix_through48':a[1:49],
       'cut_data':cut_data,'cells':[results[x] for x in CELLS],
       'original_core_record_pool':core_pool,'future_addition_increments':increments,
       'source_sha256':{str(path.relative_to(HERE)):digest(path) for path in
                        (dp,rp,cp,binding,HERE/'independent_checker.py',Path(__file__))},
       'frozen_source_sha256':data['source_sha256'],
       'scope':'Exactly four requested cells, two actual cuts and one future-point addition at each cut in one existing certified M96 history. No new history, broader scan, full-horizon profile, assumed deficit monotonicity or Q1 claim.'}
dest = HERE/'A29_forbidden_output_packing_four_cells_exact.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cut_data':{b:{key:x[key] for key in ['H_b','S_old_difference_square_sum','old_difference_count','ell','U_size']} for b,x in cut_data.items()},
       'cells':[{key:x[key] for key in ['b','k','m_future_points','h_future_pairs','original_core_record_count','Q_actual_core_unpriced','actual_future_kernel_L_exact','FD_selected_labels_exact','old_integer_F_exact','remaining_output_deficit_E_exact','genuine_component_price_exact','priced_chain_Q_SL_SFD_SF_exact']} for x in out['cells']],
       'increments':increments},indent=2))

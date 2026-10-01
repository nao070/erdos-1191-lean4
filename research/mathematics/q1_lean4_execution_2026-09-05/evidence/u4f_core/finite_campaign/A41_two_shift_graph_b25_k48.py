#!/usr/bin/env python3
"""Only b25,k=v48, shifts48 and422 in the existing certified variant."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib
import json
from reference_evaluator import rank_core,physical_core,log_bounds,strict_positive
from independent_checker import rank_conditions,output_condition

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'C1_m02_dense_variant1_M96.json'
certpath=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
priorpath=HERE/'A29_forbidden_output_packing_four_cells_exact.json'
bankpath=HERE/'C1_m02_dense_variant1_M96_records.json'
data=json.loads(source.read_text());cert=json.loads(certpath.read_text())
prior=json.loads(priorpath.read_text())
assert sha(source)==prior['source_sha256'][source.name]
assert sha(bankpath)==prior['source_sha256'][bankpath.name]
assert cert['status']=='PASS' and cert['input_sha256']==sha(source)
a=[None]+data['a'];b,v,k=25,48,48;n,m=b-1,v-b;H=a[b]-a[1]
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
pool={int(index):row for index,row in prior['original_core_record_pool'].items()}
# Direct indexed readback of prior candidate rows only; no whole-bank enumeration.
bank=json.loads(bankpath.read_text())['records']
vertices={}
for old in range(1,b):
    for future in range(b+1,v+1):
        label=a[future]-a[old]
        assert label>0 and label not in vertices
        vertices[label]=(old,future)
assert len(vertices)==n*m==552
price=F(4,k*(k*k-1)**2*(a[k]-a[1])**2)

def path_data(edges):
    successor={x['U']:x['V'] for x in edges}
    predecessor={x['V']:x['U'] for x in edges}
    assert len(successor)==len(predecessor)==len(edges)
    incident=set(successor)|set(predecessor)
    paths=[]
    for start in sorted(set(successor)-set(predecessor)):
        path=[start]
        while path[-1] in successor:path.append(successor[path[-1]])
        paths.append(path)
    assert sum(len(p)-1 for p in paths)==len(edges)
    degrees={x:int(x in successor)+int(x in predecessor) for x in incident}
    length_distribution=dict(sorted(Counter(len(p)-1 for p in paths).items()))
    candidates=sorted(x for x in successor if successor[x] in successor)
    first=candidates[0] if candidates else None
    return {'nontrivial_maximal_paths':paths,'path_edge_length_distribution':length_distribution,
     'isolated_vertex_count':len(vertices)-len(incident),
     'max_in_degree':int(bool(edges)),'max_out_degree':int(bool(edges)),
     'max_total_degree':max(degrees.values(),default=0),
     'is_matching':not candidates,
     'minimal_two_edge_chain':None if first is None else [first,successor[first],successor[successor[first]]],
     'minimal_chain_order':'Smallest starting numeric mixed label U among two-edge strict chains.'}

results=[]
unknown=[]
for e,w,z in [(48,6,9),(422,6,20)]:
    assert a[z]-a[w]==e
    classes={'same_future':[],'future_decreases':[],'future_increases':[]}
    strict=[];large=[];source_disjoint_decreasing=[]
    for U,(y,r) in sorted(vertices.items()):
        V=U+e
        if V not in vertices:continue
        x,i=vertices[V]
        edge={'U':U,'V':V,'from_old_future':[y,r],'to_old_future':[x,i]}
        if i==r:
            assert (x,y)==(w,z)
            classes['same_future'].append(edge)
            continue
        if i>r:
            classes['future_increases'].append(edge)
            continue
        classes['future_decreases'].append(edge)
        d=a[y]-a[x];t=a[r]-a[i]
        assert x<y and d>e and d-e==t>0
        if len({x,y,w,z})<4:continue
        source_disjoint_decreasing.append(edge)
        c,s=max(y,z),min(y,z)
        row=[d,e,x,y,w,z,c,s,i,r,t]
        rk,pk=rank_core(c,s,i,r),physical_core(c,t)
        if rk is None or pk is None:
            unknown.append({'shift':e,'edge':edge,'record':row,'status':'UNKNOWN_CORE'})
            continue
        refcore=bool(rk and pk)
        independent=rank_conditions(c,s,i,r) and output_condition(c,t)
        assert refcore==independent
        if not refcore:continue
        full={**edge,'original_record':row,'de':d*e,'priced_de_exact':str(price*d*e)}
        strict.append(full)
        quad=sorted((x,y,w,z));gaps=[a[q]-a[p] for p,q in zip(quad,quad[1:])]
        lc,uc=log_bounds(c)
        decisions=[strict_positive(g*lc**3,g*uc**3,c*c) for g in gaps]
        if None in decisions:
            unknown.append({'shift':e,'record':row,'status':'UNKNOWN_LARGE_GAPS'})
            continue
        islarge=all(decisions)
        assert islarge==all(output_condition(c,g) for g in gaps)
        full['old_quad']=quad;full['old_gaps']=gaps;full['all_large_old_gaps']=islarge
        if islarge:large.append(full)
    assert len(classes['same_future'])==m
    expected={tuple(row):index for index,row in pool.items() if row[1]==e and row[6]<b<row[8] and row[9]<=v}
    assert len(expected)==sum(row[1]==e and row[6]<b<row[8] and row[9]<=v for row in pool.values())
    if not unknown:assert {tuple(edge['original_record']) for edge in strict}==set(expected)
    for edge in strict:
        index=expected[tuple(edge['original_record'])]
        assert bank[index]==edge['original_record']
        edge['original_bank_index']=index
    expected_large=[]
    for row,index in expected.items():
        quad=sorted(row[2:6]);gaps=[a[q]-a[p] for p,q in zip(quad,quad[1:])]
        if all(output_condition(row[6],g) for g in gaps):expected_large.append(index)
    assert sorted(x['original_bank_index'] for x in large)==sorted(expected_large)
    total_edges=[edge for items in classes.values() for edge in items]
    sd,ld=path_data(strict),path_data(large)
    if sd['minimal_two_edge_chain']:
        byU={edge['U']:edge for edge in strict}
        sd['minimal_chain_records']=[byU[q] for q in sd['minimal_two_edge_chain'][:-1]]
        sd['minimal_chain_vertices']=[{'label':q,'old_future':vertices[q]} for q in sd['minimal_two_edge_chain']]
    de=sum(edge['de'] for edge in strict);lde=sum(edge['de'] for edge in large)
    results.append({'shift_e':e,'unique_old_source_pair':[w,z],
      'old_pair_values':[a[w],a[z]],'vertex_count':len(vertices),'future_count_m':m,
      'classes':classes,'class_counts':{name:len(items) for name,items in classes.items()},
      'source_disjoint_future_decreasing_count':len(source_disjoint_decreasing),
      'strict_edges':strict,'all_large_strict_edges':large,'strict_count':len(strict),
      'all_large_count':len(large),'strict_de_sum':de,'all_large_de_sum':lde,
      'priced_strict_de_sum_exact':str(price*de),'priced_all_large_de_sum_exact':str(price*lde),
      'all_shift_path_data':path_data(total_edges),'strict_path_data':sd,'all_large_path_data':ld,
      'original_bank_comparison':'PASS' if not unknown else 'UNKNOWN','old_span_H24':a[24]-a[1],
      'twice_shift_gt_old_span':2*e>a[24]-a[1]})

out={'date':'2026-09-09','attempt':'A41','status':'PASS_EXACT_TWO_SHIFT_CELL' if not unknown else 'UNKNOWN',
 'input':source.name,'C_exact':'1','m0':2,'M':96,'T':96,'b':b,'component_k':k,'output_v':v,
 'n_old':n,'m_future':m,'H_b':H,'genuine_component_price_exact':str(price),
 'mixed_vertices':{str(label):pair for label,pair in sorted(vertices.items())},
 'shifts':results,'unknown_comparisons':unknown,
 'source_sha256':{p.name:sha(p) for p in [source,certpath,priorpath,bankpath,HERE/'reference_evaluator.py',HERE/'independent_checker.py',Path(__file__)]},
 'scope':'Exactly one existing C1,m02 cell b25,k=v48 and shifts48,422. Strict orientation d>e,i<r and original gates preserved. Full bank used only for indexed readback of the A29 candidate rows; no new full-core enumeration, other shift or new history.'}
op=HERE/'A41_two_shift_graph_b25_k48_exact.json';op.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'vertices':len(vertices),'price':str(price),
 'shifts':[{key:r[key] for key in ['shift_e','class_counts','source_disjoint_future_decreasing_count','strict_count','all_large_count','strict_de_sum','all_large_de_sum','strict_path_data']} for r in results],
 'unknown':len(unknown)},indent=2))

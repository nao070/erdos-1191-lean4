#!/usr/bin/env python3
"""A44: only terminal(old1,future42), b25,k48, existing variant M96."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import hashlib
import itertools
import json
from reference_evaluator import log_bounds,strict_positive

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
source=HERE/'C1_m02_dense_variant1_M96.json'
certpath=HERE/'C1_m02_dense_variant1_M96_independent_check.json'
priorpath=HERE/'A29_forbidden_output_packing_four_cells_exact.json'
bankpath=HERE/'C1_m02_dense_variant1_M96_records.json'
data=json.loads(source.read_text());cert=json.loads(certpath.read_text());prior=json.loads(priorpath.read_text())
assert sha(source)==prior['source_sha256'][source.name]
assert sha(bankpath)==prior['source_sha256'][bankpath.name]
assert cert['status']=='PASS' and cert['input_sha256']==sha(source)
assert data['C_exact']=='1' and data['m0']==2 and data['M']==data['T']==96
a=[None]+data['a'];b,k,x,i=25,48,1,42
selected=[(int(index),row) for index,row in prior['original_core_record_pool'].items()
          if row[2]==x and row[8]==i and row[6]<b<row[8] and row[9]<=k]
bank=json.loads(bankpath.read_text())['records']
price=F(4,k*(k*k-1)**2*(a[k]-a[1])**2)
V=a[i]-a[x]
edges=[];unknown=[]
for index,row in selected:
    assert bank[index]==row
    d,e,xx,y,w,z,c,s,ii,r,t=row
    assert (xx,ii)==(x,i) and len({x,y,w,z,i,r})==6
    assert 2<=y<=24 and 43<=r<=48 and d==a[y]-a[x] and e==a[z]-a[w]
    assert t==a[r]-a[i]==d-e>0 and d>e>0
    lc,uc=log_bounds(c);lr,ur=log_bounds(r)
    margins={
      'older_birth':[s*lc**2-c,s*uc**2-c],
      'birth_output_gap':[(i-c)*lc**2-c,(i-c)*uc**2-c],
      'output_top_gap':[(r-i)*lr**3-r,(r-i)*ur**3-r],
      'upper_rank':[c*lc-r,c*uc-r],
      'physical_output':[t*lc**3-c*c,t*uc**3-c*c]}
    decisions={q:strict_positive(lo,hi,0) for q,(lo,hi) in margins.items()}
    if None in decisions.values():unknown.append({'index':index,'status':'UNKNOWN_CORE'})
    assert False not in decisions.values()
    quad=sorted((x,y,w,z));gaps=[a[v]-a[u] for u,v in zip(quad,quad[1:])]
    gap_margins=[[g*lc**3-c*c,g*uc**3-c*c] for g in gaps]
    gap_decisions=[strict_positive(lo,hi,0) for lo,hi in gap_margins]
    if None in gap_decisions:unknown.append({'index':index,'status':'UNKNOWN_LARGE_GAPS'})
    large=None if None in gap_decisions else all(gap_decisions)
    U=a[r]-a[y];assert V-U==e
    edges.append({'y':y,'r':r,'e':e,'unique_e_old_pair':[w,z],'d':d,'t':t,'de':d*e,
      'x':x,'i':i,'U_incoming_label':U,'V_common_terminal_label':V,
      'source_births':[c,s],'original_record':row,'original_bank_index':index,
      'strict_margin_intervals':{q:[str(v) for v in vals] for q,vals in margins.items()},
      'strict_gate_decisions':decisions,'strict_status':'UNKNOWN' if None in decisions.values() else 'PASS',
      'old_quad':quad,'old_gaps':gaps,'all_large_old_gaps':large,
      'large_gap_margin_intervals':[[str(v) for v in vals] for vals in gap_margins],
      'large_gap_decisions':gap_decisions,'covered_cut_interval_inclusive':[c+1,i-1],
      'genuine_component_price_exact':str(price),'priced_de_exact':str(price*d*e)})
edges.sort(key=lambda q:(q['y'],q['r'],q['e']))

def summarize(rows):
    by_y=defaultdict(list);by_r=defaultdict(list)
    for row in rows:by_y[row['y']].append(row);by_r[row['r']].append(row)
    def witness(coordinate):
        for a,b in itertools.combinations(rows,2):
            if a[coordinate]==b[coordinate]:return [a['original_bank_index'],b['original_bank_index']]
        return None
    return {'count':len(rows),'sum_de':sum(r['de'] for r in rows),'sum_e':sum(r['e'] for r in rows),
      'distinct_y':sorted(by_y),'distinct_r':sorted(by_r),'distinct_e':sorted({r['e'] for r in rows}),
      'by_y':{str(y):{'record_indices':[r['original_bank_index'] for r in rs],
                       'sum_de':sum(r['de'] for r in rs),'sum_e':sum(r['e'] for r in rs),
                       'priced_de_sum_exact':str(price*sum(r['de'] for r in rs))} for y,rs in sorted(by_y.items())},
      'by_r':{str(r):[q['original_bank_index'] for q in rs] for r,rs in sorted(by_r.items())},
      'minimal_repeated_y_pair':witness('y'),'minimal_repeated_r_pair':witness('r'),
      'is_y_r_matching':witness('y') is None and witness('r') is None,
      'priced_de_sum_exact':str(price*sum(r['de'] for r in rows))}

result={'date':'2026-09-09','attempt':'A44','status':'UNKNOWN' if unknown else 'PASS_EXACT_SHARED_TERMINAL_REFERENCE',
 'input':source.name,'C_exact':'1','m0':2,'M':96,'T':96,'b':b,'component_k':k,
 'terminal':{'old_x':x,'future_i':i,'a_x':a[x],'a_i':a[i],'mixed_label_V':V},
 'genuine_component_price_exact':str(price),'edges':edges,'all_strict_summary':summarize(edges),
 'all_large_summary':summarize([r for r in edges if r['all_large_old_gaps'] is True]),
 'unknown_comparisons':unknown,'witness_order':'Lexicographic edge order (y,r,e), then first pair with repeated coordinate.',
 'source_sha256':{p.name:sha(p) for p in [source,certpath,priorpath,bankpath,HERE/'reference_evaluator.py',Path(__file__)]},
 'scope':'Only the fixed physical terminal(old1,future42), cut25, component48 in the existing C1,m02 M96. Records filtered from existing A29 subset and read back at original bank indices. No other terminal, cell, history or full-profile enumeration.'}
op=HERE/'A44_SHARED_TERMINAL_EXACT.json';op.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'rows':[[r[q] for q in ['y','r','e','unique_e_old_pair','d','t','de','all_large_old_gaps']] for r in edges],
 'strict_summary':result['all_strict_summary'],'all_large_summary':result['all_large_summary'],'unknown':len(unknown)},indent=2))

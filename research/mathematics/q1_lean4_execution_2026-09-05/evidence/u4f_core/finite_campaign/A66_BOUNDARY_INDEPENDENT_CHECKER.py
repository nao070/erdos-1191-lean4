#!/usr/bin/env python3
"""Independent integer checks from saved A65 rows; no evaluator or new scan."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict,Counter
import hashlib,json

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ep=HERE/'A66_BOUNDARY_EXACT.json';result=json.loads(ep.read_text())
for name,h in result['source_sha256'].items():assert sha(HERE/name)==h
sp=HERE/'A65_SPARSE_FIBER_FOLLOWUP_EXACT.json';s=json.loads(sp.read_text())
hp=HERE/'C1_m02_dense_variant1_M96.json';a=json.loads(hp.read_text())['a']
value=lambda rank:a[rank-1]
rows=[x for x in s['records'] if x['category'].startswith('unpaid_')]
assert len(rows)==125 and len({x['bank_index'] for x in rows})==125
assert result['scope']=={'C_exact':'1','m0':2,'M':96,'T':96,'b':25,'k':48,'c':24,'input':'125 A65-unpaid saved physical rows only'}
betas=Counter();positive=defaultdict(list);groups=defaultdict(list);products=0
for item in rows:
 d,e,p,q,w,z,c,older,i,r,t=item['record'];idx=item['bank_index']
 assert c==24 and c<25<i<r<=48 and len({p,q,w,z,i,r})==6
 assert d==value(q)-value(p)>e==value(z)-value(w)>0
 assert t==d-e==value(r)-value(i)
 xx=p if q==c else w
 h=value(c)-value(xx);g=e if q==c else d
 assert g==item['g'] and xx==item['fresh_x']
 product=d*e;charge=max(0,product-g*g)
 assert charge==g*max(0,h-g)
 assert 4*charge<=h*h  # Individual parabola bound is compatible with aggregate failure.
 betas[xx]+=charge;products+=product
 if charge:positive[xx].append(idx)
 groups[g].append({'index':idx,'x':xx,'h':h,'i':i,'r':r,'sign':1 if h>g else -1,'product':product})

reference_budgets={x['fresh_x']:x for x in result['fresh_lower_budgets']}
violations=[];ratios={}
for x in range(1,24):
 h=value(24)-value(x);v=reference_budgets[x];beta=betas[x]
 assert v['beta']==beta and v['h']==h and v['h_squared']==h*h
 assert Fraction(v['beta_over_h_squared'])==Fraction(beta,h*h)
 assert Fraction(v['beta_over_h_squared_quarter'])==Fraction(beta, h*h)*4
 assert sorted(e['bank_index'] for e in v['positive_contributors'])==sorted(positive[x])
 if beta>h*h:violations.append(x)
 ratios[x]=Fraction(beta,h*h)
assert violations==result['summary']['violating_fresh_x']
assert max(ratios,key=ratios.get)==result['summary']['worst_fresh_x']
assert max(ratios.values())==Fraction(result['summary']['worst_beta_over_h_squared'])

allcomponents=[];pathpositive=0;component_histogram=Counter()
for g,edges in groups.items():
 # Vertex union-find, independent of reference edge-index traversal.
 parent={v:v for e in edges for v in [e['i'],e['r']]}
 def find(v):
  while parent[v]!=v:
   parent[v]=parent[parent[v]];v=parent[v]
  return v
 for edge in edges:parent[find(edge['i'])]=find(edge['r'])
 components=defaultdict(list)
 for edge in edges:components[find(edge['i'])].append(edge)
 reference=next(x for x in result['actual_residual_graphs'] if x['g']==g)
 assert {frozenset(e['index'] for e in es) for es in components.values()}=={frozenset(x['bank_indices']) for x in reference['components']}
 for es in components.values():
  degree=Counter();coeff=Counter()
  for e in es:
   degree[e['i']]+=1;degree[e['r']]+=1
   coeff[e['i']]-=e['sign'];coeff[e['r']]+=e['sign']
  assert max(degree.values())<=2
  leaves=[v for v,d in degree.items() if d==1];kind='path' if leaves else 'cycle'
  assert len(leaves) in [0,2]
  assert all(coeff[v]==0 for v in degree if degree[v]==2)
  if leaves:assert sorted(coeff[v] for v in leaves)==[-1,1]
  B=sum(value(v)*coeff[v] for v in leaves)
  pc=g*max(B,0) if leaves else 0
  direct_sum=sum(e['product'] for e in es)
  assert direct_sum==len(es)*g*g+g*B
  rc=next(c for c in reference['components'] if set(c['bank_indices'])=={e['index'] for e in es})
  assert rc['kind']==kind and rc['signed_output_boundary']==B
  assert rc['positive_path_boundary_mass']==pc and rc['original_product_mass']==direct_sum
  pathpositive+=pc;component_histogram[(kind,len(es))]+=1
  allcomponents.append({'g':g,'kind':kind,'bank_indices':sorted(e['index'] for e in es),'B_from_boundary_vertices':B,'positive_path_boundary_mass':pc})

beta=sum(betas.values());lam=Fraction(1,48**2*47**2)-Fraction(1,49**2*48**2)
lam/= (value(48)-value(1))**2
assert lam==Fraction(result['lambda48_exact'])
assert beta==pathpositive==8716524
assert products==21922039
assert beta==result['summary']['sum_beta_x'] and products==result['summary']['residual_original_mass']
assert pathpositive==result['summary']['positive_path_boundary_mass']
for name,val in [('positive_path_boundary_mass',pathpositive),('sum_beta_x',beta),('residual_original_mass',products)]:
 assert Fraction(result['genuine_component_prices'][name])==val*lam
assert allcomponents and component_histogram=={('path',1):110,('path',2):6,('path',3):1}
out={'date':'2026-09-09','attempt':'A66','status':'PASS_INDEPENDENT_SAVED_ROW_ARITHMETIC',
 'scope':result['scope'],'physical_rows_checked':125,'original_enumeration_or_new_history':False,
 'candidate_beta_le_h_squared':'FALSE','violating_fresh_x':violations,
 'worst_fresh_x':10,'worst_h':625,'worst_beta':betas[10],
 'worst_beta_over_h_squared':str(ratios[10]),'worst_beta_over_h_squared_quarter':str(4*ratios[10]),
 'individual_positive_edge_parabola_bound':'Every one of the 125 saved rows satisfies 4*g*max(h-g,0)<=h^2.',
 'component_histogram':{str(k):v for k,v in sorted(component_histogram.items())},
 'positive_path_boundary_mass':pathpositive,'sum_beta_x':beta,'residual_original_mass':products,
 'lambda48_exact':str(lam),'actual_components_by_vertex_union_find':allcomponents,
 'unknown_comparisons':0,'new_log_comparisons':0,
 'source_sha256':{p.name:sha(p) for p in [Path(__file__),ep,sp,hp,HERE/'A62_CELL_INDEPENDENT_CHECK.json']},
 'scope_limits':['Integer arithmetic on previously certified original residual rows only.',
  'No inference from this finite boundary-budget failure to CoreUniform or Q1.',
  'Full original u_r unchanged; priced totals use only the same genuine component48.']}
(HERE/'A66_BOUNDARY_INDEPENDENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['actual_components_by_vertex_union_find','source_sha256']},indent=2))

#!/usr/bin/env python3
"""Only the 125 saved A65-unpaid physical records at b25,k48,c24."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
import hashlib,json

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
sp=HERE/'A65_SPARSE_FIBER_FOLLOWUP_EXACT.json'
rp=HERE/'A62_CELL_EXACT.json'
assert sha(sp)=='0fca7f0a59c48f0694afca5b720aa4c4946ad2db2c3f853f69dd26c3917ca6e9'
assert sha(rp)=='1b65f56df21a43ce7b4dc2ef6a502e6b6d984d3d156b989742f425ea8becdd46'
s=json.loads(sp.read_text());ref=json.loads(rp.read_text())
for name,hsh in s['source_sha256'].items():assert sha(HERE/name)==hsh
hp=HERE/ref['input'];history=json.loads(hp.read_text())
assert history['C_exact']=='1' and history['m0']==2 and history['M']==history['T']==96
A=[None]+history['a'];c=24;b=25;k=48
saved={e['original_bank_index']:e for e in ref['survivors']}
selected=[e for e in s['records'] if e['category']!='paid_sparse_support']
assert len(selected)==125 and len({e['bank_index'] for e in selected})==125
lam=Q(4,k*(k*k-1)**2*(A[k]-A[1])**2)
assert lam==Q(ref['lambda48_exact'])
byx=defaultdict(list);byg=defaultdict(list);rows=[]
for item in selected:
 row=item['record'];d,e,x,y,w,z,cc,ss,i,r,t=row;idx=item['bank_index'];old=saved[idx]
 assert row==old['record'] and cc==c and c<b<i<r<=k
 assert d==A[y]-A[x] and e==A[z]-A[w] and t==d-e==A[r]-A[i]>0
 assert len({x,y,w,z,i,r})==6 and all(v is True for v in old['flags'].values())
 if y==c:xx=x;h=d;g=e;source=[w,z];sigma=1
 else:
  assert z==c
  xx=w;h=e;g=d;source=[x,y];sigma=-1
 assert source[1]<c and g==A[source[1]]-A[source[0]] and h==A[c]-A[xx]
 assert g==item['g']==old['g'] and xx==item['fresh_x']==old['fresh_x']
 assert sigma*t==h-g
 out={'bank_index':idx,'record':row,'fresh_x':xx,'h':h,'g':g,'old_pair':source,
      'sigma':sigma,'positive_edge_boundary_charge':g*max(h-g,0),
      'signed_edge_boundary_charge':g*(h-g),'product':g*h,
      'source_values':[A[j] for j in [x,y,w,z]],'output_values':[A[i],A[r]],
      'inherited_strict_selector_evidence':'A62_CELL_EXACT.json survivor with this bank index',
      'A65_unpaid_category':item['category']}
 rows.append(out);byx[xx].append(out);byg[g].append(out)

fresh=[]
for x in range(1,c):
 h=A[c]-A[x];terms=byx[x];beta=sum(e['positive_edge_boundary_charge'] for e in terms)
 fresh.append({'fresh_x':x,'fresh_value':A[x],'h':h,'record_count':len(terms),
  'positive_contributor_count':sum(e['positive_edge_boundary_charge']>0 for e in terms),
  'beta':beta,'h_squared':h*h,'beta_over_h_squared':str(Q(beta,h*h)),
  'beta_over_h_squared_quarter':str(Q(4*beta,h*h)),
  'beta_minus_h_squared':beta-h*h,'candidate_beta_le_h_squared':beta<=h*h,
  'bank_indices':[e['bank_index'] for e in terms],
  'positive_contributors':[e for e in terms if e['positive_edge_boundary_charge']>0]})

graphs=[]
for g,edges in sorted(byg.items()):
 incidence=defaultdict(list)
 for j,e in enumerate(edges):
  for v in e['record'][8:10]:incidence[v].append(j)
 assert max(map(len,incidence.values()))<=2
 unused=set(range(len(edges)));components=[]
 while unused:
  pending=[min(unused)];ids=set()
  while pending:
   j=pending.pop()
   if j in ids:continue
   ids.add(j)
   for vertex in edges[j]['record'][8:10]:pending.extend(incidence[vertex])
  unused-=ids
  vertices=sorted({v for j in ids for v in edges[j]['record'][8:10]})
  degrees={v:sum(j in ids for j in incidence[v]) for v in vertices}
  boundary_coeff=defaultdict(int)
  for j in ids:
   edge=edges[j];i,r=edge['record'][8:10];boundary_coeff[i]-=edge['sigma'];boundary_coeff[r]+=edge['sigma']
  kind='cycle' if all(v==2 for v in degrees.values()) else 'path'
  if kind=='cycle':assert all(boundary_coeff[v]==0 for v in vertices)
  else:
   ends=[v for v in vertices if degrees[v]==1]
   assert len(ends)==2 and sorted(boundary_coeff[v] for v in ends)==[-1,1]
   assert all(boundary_coeff[v]==0 for v in vertices if degrees[v]==2)
  B=sum(edges[j]['sigma']*edges[j]['record'][10] for j in ids)
  assert B==sum(boundary_coeff[v]*A[v] for v in vertices)
  product=sum(edges[j]['product'] for j in ids)
  assert product==g*g*len(ids)+g*B
  edgepositive=sum(edges[j]['positive_edge_boundary_charge'] for j in ids)
  pathpositive=g*max(B,0) if kind=='path' else 0
  assert pathpositive<=edgepositive
  components.append({'kind':kind,'vertices':vertices,'edge_count':len(ids),
   'bank_indices':sorted(edges[j]['bank_index'] for j in ids),
   'signed_output_boundary':B,'signed_boundary_mass':g*B,
   'positive_path_boundary_mass':pathpositive,'positive_edge_boundary_mass':edgepositive,
   'edge_to_path_cancellation':edgepositive-pathpositive,
   'quadratic_base_mass':g*g*len(ids),'original_product_mass':product,
   'boundary_coefficients':dict(boundary_coeff)})
 graphs.append({'c':c,'g':g,'old_pair':edges[0]['old_pair'],'record_count':len(edges),
  'components':components,'positive_path_boundary_mass':sum(e['positive_path_boundary_mass'] for e in components),
  'positive_edge_boundary_mass':sum(e['positive_edge_boundary_mass'] for e in components)})

beta=sum(x['beta'] for x in fresh);pathmass=sum(g['positive_path_boundary_mass'] for g in graphs)
mass=sum(e['product'] for e in rows);base=sum(e['g']**2 for e in rows)
signed=sum(e['signed_edge_boundary_charge'] for e in rows)
assert mass==base+signed==21922039
assert pathmass<=beta<=mass
violations=[x for x in fresh if not x['candidate_beta_le_h_squared']]
summary={'records':len(rows),'nonempty_g_cells':len(graphs),
 'path_components':sum(x['kind']=='path' for g in graphs for x in g['components']),
 'cycle_components':sum(x['kind']=='cycle' for g in graphs for x in g['components']),
 'positive_path_boundary_mass':pathmass,'sum_beta_x':beta,
 'edge_to_path_cancellation':beta-pathmass,'quadratic_base_mass':base,
 'signed_boundary_mass':signed,'residual_original_mass':mass,
 'pre_A64_original_mass':ref['summary']['unpriced_mass'],
 'sum_beta_over_residual_mass':str(Q(beta,mass)),
 'path_boundary_over_residual_mass':str(Q(pathmass,mass)),
 'path_boundary_over_sum_beta':str(Q(pathmass,beta)),
 'candidate_beta_le_h_squared':'FALSE' if violations else 'PASSED_THIS_FINITE_SCOPE',
 'violating_fresh_x':[v['fresh_x'] for v in violations],
 'worst_fresh_x':max(fresh,key=lambda v:Q(v['beta_over_h_squared']))['fresh_x'],
 'worst_beta_over_h_squared':str(max(Q(v['beta_over_h_squared']) for v in fresh))}
out={'date':'2026-09-09','attempt':'A66','status':'EXACT_REFERENCE_COMPLETE',
 'scope':{'C_exact':'1','m0':2,'M':96,'T':96,'b':25,'k':48,'c':24,'input':'125 A65-unpaid saved physical rows only'},
 'summary':summary,'fresh_lower_budgets':fresh,'strict_violations':violations,
 'actual_residual_graphs':graphs,'records':rows,
 'retained_g163_g214':[g for g in graphs if g['g'] in [163,214]],
 'shared_x13_contributors':[e for e in rows if e['fresh_x']==13],
 'lambda48_exact':str(lam),
 'genuine_component_prices':{key:str(Q(summary[key])*lam) for key in ['positive_path_boundary_mass','sum_beta_x','residual_original_mass']},
 'UNKNOWN':0,'source_sha256':{p.name:sha(p) for p in [Path(__file__),sp,rp,HERE/'A62_CELL_MANIFEST.json',HERE/'A62_CELL_INDEPENDENT_CHECK.json',hp]},
 'limits':['No new history, cut, birth, horizon, core enumeration or full profile.',
  'Fresh budget and path boundary are exact proposed charging quantities; not independent physical prices.',
  'One fixed original component coefficient; no original u_r has been replaced or reset.',
  'Finite failure of the stated common budget does not refute CoreUniform or Q1.']}
(HERE/'A66_BOUNDARY_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(summary,indent=2))

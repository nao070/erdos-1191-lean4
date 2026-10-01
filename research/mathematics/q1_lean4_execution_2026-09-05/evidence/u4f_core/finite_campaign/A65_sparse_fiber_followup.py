#!/usr/bin/env python3
"""New F3 selector only, on the 126 independently certified A62 survivors.

No new history, original-record enumeration, or full profile evaluation.
Two different exact constructions of unordered old three-point fibers agree.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter, defaultdict
import hashlib,json
from reference_evaluator import log_bounds
from independent_checker import log_fixed,SCALE

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
cp=HERE/'A62_CELL_EXACT.json'; mp=HERE/'A62_CELL_MANIFEST.json'
m=json.loads(mp.read_text()); assert sha(cp)==m['file_sha256'][cp.name]
d=json.loads(cp.read_text()); hp=HERE/d['input']; history=json.loads(hp.read_text())
assert sha(hp)==m['file_sha256'][hp.name]
assert (d['C_exact'],d['m0'],d['M'],d['T'],d['b'],d['k'])==('1',2,96,96,25,48)
A=[None]+history['a']; rows=d['survivors']; assert len(rows)==126
allfibers={}
for c in {row['record'][6] for row in rows}:
    bysum=defaultdict(list)
    for triple in combinations(range(1,c),3):
        bysum[sum(A[x] for x in triple)].append(triple)
    allfibers[c]=bysum

def sparse(q,c,lo,hi):
    if q*q*hi**5<=c*c:return True
    if q*q*lo**5>c*c:return False
    raise ArithmeticError('UNKNOWN sparse F3 threshold')

fibers={};results=[];counts=Counter();weights=Counter();paid=set()
for row in rows:
    record=row['record'];c=record[6];g=row['g'];x=row['fresh_x'];target=3*(A[c]-g)
    key=(c,g)
    if key not in fibers:
        ref=allfibers[c].get(target,[])
        rank={A[j]:j for j in range(1,c)}
        # Independent pair-plus-lookup reconstruction, increasing ranks once.
        ind=[]
        for u in range(1,c):
            for v in range(u+1,c):
                w=rank.get(target-A[u]-A[v])
                if w is not None and v<w:ind.append((u,v,w))
        assert sorted(ref)==sorted(ind)
        q=len(ref);support=[x for t in ref for x in t]
        assert len(support)==len(set(support)) and 3*q<=c-1
        lo,hi=log_bounds(c); il,iu=log_fixed(c)
        flag=sparse(q,c,lo,hi)
        assert flag==sparse(q,c,Q(il,SCALE),Q(iu,SCALE))
        fibers[key]={'c':c,'g':g,'target_three_sum':target,'q':q,
          'triples':[list(t) for t in ref],'support':support,'sparse_p5over2':flag,
          'reference_log_interval':list(map(str,(lo,hi))),
          'independent_log_interval':[str(Q(il,SCALE)),str(Q(iu,SCALE))]}
    f=fibers[key];in_support=x in f['support']
    pay=in_support and f['sparse_p5over2']
    category='paid_sparse_support' if pay else 'unpaid_outside_support' if not in_support else 'unpaid_rich_support'
    counts[category]+=1;weights[category]+=record[0]*record[1]
    if pay:paid.add(row['original_bank_index'])
    results.append({'bank_index':row['original_bank_index'],'record':record,'g':g,'fresh_x':x,
                    'q':f['q'],'in_support':in_support,'sparse':f['sparse_p5over2'],
                    'category':category,'products':record[0]*record[1]})
assert sum(weights.values())==d['summary']['unpriced_mass']
remaining_components=[]
for cell in d['nonempty_graph_cells']:
    for comp in cell['components']:
        remaining=[j for j in comp['bank_indices'] if j not in paid]
        if len(remaining)>=2:
            remaining_components.append({'c':cell['c'],'g':cell['g'],
              'original_component':comp,'unpaid_bank_indices':remaining,
              'all_edges_still_unpaid':len(remaining)==len(comp['bank_indices'])})
out={'date':'2026-09-09','attempt':'A65','status':'EXACT_FINITE_F3_SELECTOR_PASS',
 'scope':{'C_exact':'1','m0':2,'M':96,'T':96,'b':25,'k':48,'births':[23,24],
          'input_residual_records':126,'new_histories':0,'full_profile_evaluations':0},
 'counts':dict(counts),'unpriced_products_by_class':dict(weights),
 'component_prices_by_class':{s:str(Q(v)*Q(d['lambda48_exact'])) for s,v in weights.items()},
 'fibers':list(fibers.values()),'records':results,
 'old_components_with_at_least_two_unpaid_edges':remaining_components,'UNKNOWN':0,
 'certification':'All F3 fibers agree between triple enumeration and pair-plus-lookup. Sparse comparisons use both existing exact logarithm methods. Original record/cap/genuine-price certification is reused by hash.',
 'limits':['Only this new static selector is evaluated here; no asymptotic sparse/rich-frequency claim.',
           'A component with some edges deleted can split; no connectivity is inferred for its remainder without checking.',
           'One selected component coefficient, not the complete original u_r, is totaled.'],
 'source_sha256':{p.name:sha(p) for p in [Path(__file__),cp,mp,hp,HERE/'reference_evaluator.py',HERE/'independent_checker.py']}}
(HERE/'A65_SPARSE_FIBER_FOLLOWUP_EXACT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'counts':out['counts'],'products':out['unpriced_products_by_class'],
 'unpaid_multiple_edge_components':[(x['g'],len(x['unpaid_bank_indices']),x['all_edges_still_unpaid']) for x in remaining_components],'UNKNOWN':0}))

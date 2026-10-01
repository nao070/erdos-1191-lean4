#!/usr/bin/env python3
"""Independent exact primal/dual checker. Imports no reference implementation.

Only the prescribed 23-by-23 old/future right-vertex domain and the 125
already certified A65-unpaid original rows are examined.
"""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import hashlib,json

HERE=Path(__file__).resolve().parent
CERT=HERE/'A70_FEASIBLE_MATCHING_EXACT.json'
OUT=HERE/'A70_FEASIBLE_MATCHING_CHECK.json'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def integer(x,where):
    assert type(x) is int, ('Expected integer',where,type(x).__name__)
    return x

def verify():
    data=json.loads(CERT.read_text())
    bindings=data['source_sha256']
    assert type(bindings) is dict
    for name,expected in bindings.items():
        p=HERE/name
        assert p.is_file(), ('Missing bound source',name)
        assert sha(p)==expected, ('Source hash mismatch',name)

    hp=HERE/'C1_m02_dense_variant1_M96.json'
    sp=HERE/'A65_SPARSE_FIBER_FOLLOWUP_EXACT.json'
    assert bindings[hp.name]==sha(hp)=='d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e'
    assert bindings[sp.name]==sha(sp)=='0fca7f0a59c48f0694afca5b720aa4c4946ad2db2c3f853f69dd26c3917ca6e9'
    history=json.loads(hp.read_text());prior=json.loads(sp.read_text())
    for name,expected in prior['source_sha256'].items():
        assert sha(HERE/name)==expected, ('A65 source hash mismatch',name)
    assert history['C_exact']=='1' and history['m0']==2
    assert history['M']==history['T']==96
    assert prior['scope']['C_exact']=='1' and prior['scope']['m0']==2
    assert (prior['scope']['M'],prior['scope']['T'],prior['scope']['b'],prior['scope']['k'])==(96,96,25,48)
    a=history['a'];value=lambda r:a[r-1]
    c,b,k=24,25,48
    old=data['old_values'];future=data['future_values'];H=integer(data['H_c'],'H_c')
    assert old==a[:23] and future==a[25:48] and len(old)==len(future)==23
    assert H==value(c)-value(1)==713
    n,m=len(old),len(future)

    # Recover actual incoming endpoints directly from the saved physical rows.
    actual=defaultdict(list);positive=defaultdict(list)
    rows=[r for r in prior['records'] if r['category']!='paid_sparse_support']
    assert len(rows)==125 and len({r['bank_index'] for r in rows})==125
    mass=0
    for item in rows:
        d,e,p,y,w,z,cc,s,i,r,t=item['record']
        assert cc==c and c<b<i<r<=k and len({p,y,w,z,i,r})==6
        assert d==value(y)-value(p)>e==value(z)-value(w)>0
        assert t==d-e==value(r)-value(i)
        if y==c:
            ow,oz,j,q=w,z,i-b,r-b
            g,h=e,d
        else:
            assert z==c
            ow,oz,j,q=p,y,r-b,i-b
            g,h=d,e
        fresh=p if y==c else w
        assert fresh==item['fresh_x'] and g==item['g']
        assert h==value(c)-value(fresh)
        assert 1<=ow<oz<=n and 1<=j<=m and 1<=q<=m and j!=q
        assert value(c)+old[ow-1]+future[j-1]==value(fresh)+old[oz-1]+future[q-1]
        assert g==old[oz-1]-old[ow-1]
        entry={'bank_index':item['bank_index'],'old_lower_position':ow,
               'future_lower_position':j,'g':g,'h':h,'t':t,
               'positive_charge':g*(h-g) if h>g else 0}
        actual[oz,q].append(entry)
        if h>g:
            assert j<q and g+t==h<=H
            assert t==future[q-1]-future[j-1]
            positive[oz,q].append(entry)
        mass+=d*e
    for cell,entries in actual.items():
        assert len({e['old_lower_position'] for e in entries})==len(entries), ('Actual old-coordinate collision',cell)
        assert len({e['future_lower_position'] for e in entries})==len(entries), ('Actual future-coordinate collision',cell)
    assert mass==21922039

    nodes=data['nodes'];assert len(nodes)==n*m==529
    cells=set();checked=[];total=0;unrestricted=0;matrix_checks=0;minimum_dual_slack=None
    for node in nodes:
        z=integer(node['z'],'z');q=integer(node['q'],'q');cell=(z,q)
        assert 1<=z<=n and 1<=q<=m and cell not in cells, ('Bad/duplicate node',cell)
        cells.add(cell)
        L,R=z-1,q-1;N=max(L,R)
        opt=integer(node['value'],('value',cell));assert opt>=0
        dl=node['dual_left'];dr=node['dual_right'];assignment=node['assignment']
        assert len(dl)==len(dr)==len(assignment)==N, ('Dual/assignment length',cell)
        assert all(type(x) is int for x in dl+dr+assignment)
        assert sorted(assignment)==list(range(N)), ('Assignment is not a permutation',cell)

        # Reconstruct every entry from actual coordinates, including all zeros.
        W=[]
        for row in range(N):
            line=[]
            for col in range(N):
                weight=0
                if row<L and col<R:
                    g=old[z-1]-old[row];t=future[q-1]-future[col]
                    assert g>0 and t>0
                    if g+t<=H:weight=g*t
                slack=dl[row]+dr[col]-weight
                assert slack>=0, ('Dual infeasible',cell,row,col,slack)
                minimum_dual_slack=slack if minimum_dual_slack is None else min(minimum_dual_slack,slack)
                line.append(weight);matrix_checks+=1
            W.append(line)
        assignment_value=sum(W[row][assignment[row]] for row in range(N))
        assert assignment_value==opt, ('Assignment objective differs',cell,assignment_value,opt)
        assert sum(dl)+sum(dr)==opt, ('Dual objective differs',cell)

        # The advertised real matching contains no dummy or infeasible edge.
        left_used=set();right_used=set();matching_value=0
        for pair in node['matching']:
            assert type(pair) is list and len(pair)==2
            w,j=pair;integer(w,('matching w',cell));integer(j,('matching j',cell))
            assert 1<=w<=L and 1<=j<=R
            assert w not in left_used and j not in right_used, ('Matching capacity violation',cell,w,j)
            left_used.add(w);right_used.add(j)
            g=old[z-1]-old[w-1];t=future[q-1]-future[j-1]
            assert g+t<=H, ('Advertised edge infeasible',cell,w,j,g,t)
            matching_value+=g*t
        assert matching_value==opt, ('Real matching objective differs',cell,matching_value,opt)
        beta=sum(e['positive_charge'] for e in positive[cell])
        assert beta<=opt, ('Actual beta exceeds certified optimum',cell,beta,opt)
        node_unrestricted=sum((old[z-1]-old[l])*(future[q-1]-future[l]) for l in range(min(L,R)))
        assert opt<=node_unrestricted, ('Constrained exceeds unrestricted',cell)
        total+=opt;unrestricted+=node_unrestricted
        checked.append({'z':z,'q':q,'N':N,'value':opt,'actual_beta':beta,
                        'unrestricted_matching_allowance':node_unrestricted,
                        'actual_positive_bank_indices':[e['bank_index'] for e in positive[cell]],
                        'actual_positive_contributors':positive[cell],
                        'matching_edges':len(node['matching']),
                        'primal_dual_gap':0})
    assert cells=={(z,q) for z in range(1,n+1) for q in range(1,m+1)}
    beta=sum(e['positive_charge'] for es in positive.values() for e in es)
    assert beta==8716524 and unrestricted==1181503640
    for key in ['Phi_H','Phi_H_exact','total_value']:
        if key in data:assert Fraction(data[key])==total, ('Published total mismatch',key)
    U=sum(old[z]-old[w] for z in range(n) for w in range(z))
    G=sum(value(c)-x for x in old)
    assert U==58548 and G==11745
    lam=(Fraction(1,k*k*(k-1)**2)-Fraction(1,(k+1)**2*k*k))/(value(k)-value(1))**2
    assert lam==Fraction(1,1148518878296832)
    if 'lambda48_exact' in data:assert Fraction(data['lambda48_exact'])==lam

    return {'date':'2026-09-09','attempt':'A70','status':'PASS_INDEPENDENT_PRIMAL_DUAL_AND_ACTUAL_ROW_CHECK',
      'scope':{'C_exact':'1','m0':2,'M':96,'T':96,'c':c,'b':b,'k':k,
               'old_values':n,'future_values':m,'actual_unpaid_records':125,'nodes':529},
      'certificate_sha256':sha(CERT),'bound_sources_all_match':True,
      'Phi_H':total,'provisional_80331512_matches':total==80331512,
      'Phi':unrestricted,'U':U,'G':G,'UG':U*G,'actual_Beta':beta,
      'actual_original_products':mass,'node_results':checked,
      'dual_matrix_inequalities_checked':matrix_checks,'minimum_dual_slack':minimum_dual_slack,
      'primal_dual_gaps_all_zero':True,'each_assignment_is_permutation':True,
      'each_real_matching_feasible_and_equal_weight':True,'actual_beta_bounded_at_every_node':True,
      'lambda48_exact':str(lam),
      'component_values_exact':{'Phi_H':str(total*lam),'Phi':str(unrestricted*lam),
                                'UG':str(U*G*lam),'actual_Beta':str(beta*lam)},
      'source_sha256':{p.name:sha(p) for p in [Path(__file__),CERT,sp,hp,
        HERE/'A70_GREEDY_MATCHING_REVIEW.md',HERE/'A66_BOUNDARY_MANIFEST.json']},
      'proof_of_optimality':'Dual feasibility bounds every complete padded assignment; the supplied assignment and feasible real matching attain that dual value. Zero padding and nonnegative weights identify the unrestricted-cardinality partial-matching optimum.',
      'scope_limits':['No reference implementation imported; no new optimization or greedy search was needed.',
        'Only the prescribed existing cell and its 125 saved rows were checked.',
        'Phi_H is the optimum under g+t<=H_c alone; actual fresh-label membership and other gates can further restrict edges.',
        'Allowances are not physical record masses; all quoted prices use the same component48 only.',
        'No new history, original core enumeration, full profile, Lean build, uniform norm or Q1 conclusion.'],
      'unknown_comparisons':0}

if __name__=='__main__':
    answer=verify()
    OUT.write_text(json.dumps(answer,indent=2)+'\n')
    print(json.dumps({k:v for k,v in answer.items() if k not in ['node_results','source_sha256']},indent=2))

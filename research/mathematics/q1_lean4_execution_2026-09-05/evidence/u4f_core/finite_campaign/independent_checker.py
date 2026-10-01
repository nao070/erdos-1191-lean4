#!/usr/bin/env python3
"""Separate output-endpoint enumeration with integer fixed-point log bounds.

This file does not import the reference evaluator. It also verifies Sidon
using repeated two-sum uniqueness, then reconstructs every core record and
profile coefficient from exact direct component sums.
"""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict

SCALE=10**40
TERMS=50

def ceildiv(a,b):
    return (a+b-1)//b

def small_log(p,q):
    # log(p/q), 1 <= p/q <= 2; z=(p-q)/(p+q) <= 1/3.
    znum=p-q;zden=p+q
    low=0
    for k in range(TERMS):
        numerator=2*SCALE*znum**(2*k+1)
        denominator=(2*k+1)*zden**(2*k+1)
        low+=numerator//denominator
    tailnum=2*SCALE*znum**(2*TERMS+1)*zden*zden
    tailden=(2*TERMS+1)*zden**(2*TERMS+1)*(zden*zden-znum*znum)
    # Each floor incurs <1/SCALE. The omitted positive tail has this upper bound.
    return low,low+TERMS+ceildiv(tailnum,tailden)

@lru_cache(None)
def log_fixed(n):
    k=n.bit_length()-1
    lo,hi=small_log(n,1<<k)
    l2,u2=small_log(2,1)
    return lo+k*l2,hi+k*u2

def decide(lo,hi,target):
    if lo>target:
        return True
    if hi<=target:
        return False
    raise ArithmeticError('UNKNOWN strict logarithm comparison')

@lru_cache(None)
def rank_conditions(c,s,i,r):
    lc,uc=log_fixed(c);lr,ur=log_fixed(r)
    return (decide(s*lc*lc,s*uc*uc,c*SCALE*SCALE)
            and decide((i-c)*lc*lc,(i-c)*uc*uc,c*SCALE*SCALE)
            and decide((r-i)*lr**3,(r-i)*ur**3,r*SCALE**3)
            and decide(c*lc,c*uc,r*SCALE))

@lru_cache(None)
def output_condition(c,t):
    lc,uc=log_fixed(c)
    return decide(t*lc**3,t*uc**3,c*c*SCALE**3)

def check(path):
    data=json.loads(path.read_text())
    a=data['a'];M=len(a)
    assert all(v>0 for v in a) and all(x<y for x,y in zip(a,a[1:]))
    two_sums={}
    for x in range(M):
        for y in range(x,M):
            s=a[x]+a[y]
            assert s not in two_sums,('Sidon failure',x,y,two_sums.get(s))
            two_sums[s]=(x,y)
    C=F(data['C_exact']);m0=data['m0']
    for n in range(m0,M+1):
        lo,hi=log_fixed(2*n)
        assert (a[n-1]-a[0])*SCALE*C.denominator<=C.numerator*n*n*lo
    endpoint={a[q-1]-a[p-1]:(p,q) for q in range(2,M+1) for p in range(1,q)}
    records=[]
    raw=defaultdict(int)
    for i in range(4,M):
        old=[(v,p,q) for v,(p,q) in endpoint.items() if q<i]
        for r in range(i+1,M+1):
            t=a[r-1]-a[i-1]
            for d,p,q in old:
                e=d-t
                other=endpoint.get(e)
                if other is None:
                    continue
                pe,qe=other
                c=max(q,qe);s=min(q,qe)
                if c>=i or c<3 or len({p,q,pe,qe,i,r})!=6:
                    continue
                if not rank_conditions(c,s,i,r) or not output_condition(c,t):
                    continue
                records.append((d,e,p,q,pe,qe,c,s,i,r,t))
                for b in range(c+1,i):
                    raw[b,r]+=d*e
    u={r:sum((F(1,k*k*(k-1)**2)-F(1,k*k*(k+1)**2))
               /(a[k-1]-a[0])**2 for k in range(r,M+1)) for r in range(2,M+1)}
    profile={b:sum((F(raw[b,r])*u[r] for r in range(b+1,M+1)),F(0)) for b in range(2,M)}
    actual={str(b):str(p) for b,p in profile.items() if p}
    assert actual==data['profile_exact'],'independent profile mismatch'
    saved=path.with_name(path.stem+'_records.json')
    old_records=json.loads(saved.read_text())['records']
    assert sorted(records)==sorted(tuple(x) for x in old_records),'independent record mismatch'
    assert len(records)==data['core_records']
    for block in data['blocks']:
        I=sum((profile[b]/b for b in range(block['cut_start'],block['cut_end_exclusive'])),F(0))
        assert str(I)==block['I_exact'],'independent I mismatch'
    result={'input':path.name,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'M':M,'core_records':len(records),'status':'PASS',
            'verified':['repeated two-sum Sidon','all-rank fixed cap','strict core membership',
                        'every core record by output-centric reconstruction','genuine component prices',
                        'all exact nonzero profile coefficients','all exact I_j'],
            'not_verified':['uniform K','asymptotic decay','Lean theorem','certified square-root enclosures'],
            'unknown_comparisons':0}
    path.with_name(path.stem+'_independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('files',nargs='+');args=p.parse_args()
    for file in args.files:
        check(Path(file))

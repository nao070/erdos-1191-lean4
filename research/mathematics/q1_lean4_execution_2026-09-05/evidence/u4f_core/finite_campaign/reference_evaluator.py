#!/usr/bin/env python3
"""Minimal exact reference for Q1191-U4F-CORE-UNIFORM-01, T=M.

Record enumeration is source-pair based. Prices, profile and I_j are
rational. Decimal N, block square-root sums and cap usage are presentation
only. Strict log comparisons use rigorous rational enclosures or UNKNOWN.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from functools import lru_cache
from collections import defaultdict
from pathlib import Path
import argparse, hashlib, json, math, time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCES = [ROOT / 'research/NEXT_THEOREM_CONTRACT.md',
           ROOT / 'q1_lean4_execution_2026-09-05/research/future_covariance_rank_localization.md',
           ROOT / 'q1_lean4_execution_2026-09-05/research/causal_fourier_rank_commutator.md']

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def series(q, terms=40):
    z = (q-1)/(q+1)
    zz = z*z
    zp = z
    ans = F(0)
    for k in range(terms):
        ans += 2*zp/(2*k+1)
        zp *= zz
    return ans, ans + 2*zp/((2*terms+1)*(1-zz))

@lru_cache(None)
def log_bounds(n):
    k = n.bit_length()-1
    q = F(n, 2**k)
    lo, hi = series(q)
    l2, u2 = series(F(2))
    return lo+k*l2, hi+k*u2

def strict_positive(lhs_lo, lhs_hi, rhs):
    if lhs_lo > rhs:
        return True
    if lhs_hi <= rhs:
        return False
    return None

@lru_cache(None)
def rank_core(c, s, i, r):
    lc, uc = log_bounds(c)
    lr, ur = log_bounds(r)
    comparisons = [strict_positive(s*lc**2, s*uc**2, c),
                   strict_positive((i-c)*lc**2, (i-c)*uc**2, c),
                   strict_positive((r-i)*lr**3, (r-i)*ur**3, r),
                   strict_positive(c*lc, c*uc, r)]
    if False in comparisons:
        return False
    if None in comparisons:
        return None
    return True

@lru_cache(None)
def physical_core(c, t):
    lc, uc = log_bounds(c)
    return strict_positive(t*lc**3, t*uc**3, c*c)

def differences(a):
    assert len(a) >= 2 and a[0] > 0
    assert all(x<y for x,y in zip(a,a[1:]))
    d = {}
    for q in range(2,len(a)+1):
        for p in range(1,q):
            t=a[q-1]-a[p-1]
            assert t not in d, ('duplicate positive difference',t,p,q,d.get(t))
            d[t]=(p,q)
    return d

def cap_check(a, C=F(1), m0=2):
    cert=[]
    for n in range(m0,len(a)+1):
        lo,hi=log_bounds(2*n)
        width=a[n-1]-a[0]
        lower=C*n*n*lo
        upper=C*n*n*hi
        status='PASS' if width<=lower else 'FAIL' if width>upper else 'UNKNOWN'
        cert.append({'n':n,'H':width,'status':status,
                     'log_lower':str(lo),'log_upper':str(hi)})
    assert all(row['status']=='PASS' for row in cert), 'cap not certified'
    return cert

def greedy(M, prefix=(1,), choices=()):
    a=list(prefix)
    used=set(differences(a)) if len(a)>1 else set()
    for step in range(len(a),M):
        x=a[-1]+1
        skip=choices[step] if step<len(choices) else 0
        while True:
            fresh=[x-y for y in a]
            if not any(d in used for d in fresh):
                if skip==0:
                    break
                skip-=1
            x+=1
        a.append(x)
        used.update(fresh)
    return a

def enumerate_core(a):
    dif=differences(a)
    labels=sorted(dif)
    records=[]
    unknown=[]
    for ix,d in enumerate(labels):
        p,q=dif[d]
        for e in labels[:ix]:
            t=d-e
            out=dif.get(t)
            if out is None:
                continue
            i,r=out
            pe,qe=dif[e]
            c=max(q,qe)
            if not 3<=c<i<r:
                continue
            if len({p,q,pe,qe,i,r})!=6:
                continue
            s=min(q,qe)
            rank=rank_core(c,s,i,r)
            phys=physical_core(c,t)
            if rank is False or phys is False:
                continue
            record=[d,e,p,q,pe,qe,c,s,i,r,t]
            if rank is None or phys is None:
                unknown.append(record)
            else:
                records.append(record)
    return records,unknown

def decimal(q):
    return Decimal(q.numerator)/Decimal(q.denominator)

def evaluate(a, name, C=F(1), m0=2):
    began=time.monotonic()
    cap=cap_check(a,C,m0)
    records,unknown=enumerate_core(a)
    if unknown:
        raise RuntimeError(f'UNKNOWN strict comparisons: {unknown[:5]}')
    M=len(a)
    u=[F(0)]*(M+2)
    for r in range(M,1,-1):
        alpha=F(1,r*r*(r-1)*(r-1))
        next_alpha=F(1,r*r*(r+1)*(r+1))
        u[r]=u[r+1]+(alpha-next_alpha)/(a[r-1]-a[0])**2
    raw_by_cut=[defaultdict(int) for b in range(M)]
    by_clock=defaultdict(lambda:defaultdict(int))
    by_birth=defaultdict(lambda:defaultdict(int))
    by_output=defaultdict(int)
    for d,e,p,q,pe,qe,c,s,i,r,t in records:
        raw=d*e
        for b in range(c+1,i):
            raw_by_cut[b][r]+=raw
        by_clock[(c,i,r)][r]+=raw
        by_birth[c][r]+=raw
        by_output[r]+=raw
    profile=[sum((u[r]*v for r,v in rr.items()),F(0)) for rr in raw_by_cut]
    intervals=[]
    for (c,i,r),rr in by_clock.items():
        ell=sum((F(1,b) for b in range(c+1,i)),F(0))
        mass=u[r]*rr[r]
        intervals.append({'c':c,'i':i,'r':r,'cuts':[c+1,i-1],
                          'record_mass':str(mass),'harmonic_coverage':str(ell),
                          'I_all_contribution':str(mass*ell)})
    intervals.sort(key=lambda x:F(x['I_all_contribution']),reverse=True)
    with localcontext() as ctx:
        ctx.prec=55
        N=sum((decimal(profile[b]).sqrt()/b for b in range(2,M)),Decimal(0))
        blocks=[]
        j=1
        while 2**j<M:
            lower=2**j;upper=min(2**(j+1),M)
            W=sum((F(1,b) for b in range(lower,upper)),F(0))
            I=sum((profile[b]/b for b in range(lower,upper)),F(0))
            actual=sum((decimal(profile[b]).sqrt()/b for b in range(lower,upper)),Decimal(0))
            # Re-expand every physical record on the identical cut, independently of profile aggregation.
            coverage=F(0)
            for d,e,p,q,pe,qe,c,s,i,r,t in records:
                ell=sum((F(1,b) for b in range(max(lower,c+1),min(upper,i))),F(0))
                coverage+=u[r]*d*e*ell
            assert I==coverage
            blocks.append({'j':j,'cut_start':lower,'cut_end_exclusive':upper,
                           'W_exact':str(W),'I_exact':str(I),'I_approx':str(decimal(I)),
                           'actual_block_approx':str(actual),'sqrt_WI_approx':str(decimal(W*I).sqrt()),
                           'I_times_1_plus_j_cubed_approx':str(decimal(I)*(1+j)**3)})
            j+=1
        capratios=[(Decimal(a[n-1]-a[0])/(decimal(C)*n*n*Decimal(2*n).ln()),n)
                   for n in range(m0,M+1)]
        capmax,caprank=max(capratios,default=(Decimal(0),0))
        result={'campaign':name,'C_exact':str(C),'m0':m0,'M':M,'T':M,'a':a,
                'status':'CERTIFIED_RATIONAL_PROFILE','unknown_core_comparisons':0,
                'positive_differences':M*(M-1)//2,'core_records':len(records),
                'u_M_exact':str(u[M]),'alpha_M_plus_1_preserved':True,
                'N_approx':str(N),'sqrt_sum_I_approx':str(sum((decimal(F(b['I_exact'])).sqrt() for b in blocks),Decimal(0))),
                'profile_exact':{str(b):str(profile[b]) for b in range(2,M) if profile[b]},
                'blocks':blocks,'cap_use_max_approx':str(capmax),'cap_use_argmax':caprank,
                'cap_all_ranks_certified':True,'cap_certificates':cap,
                'dominant_intervals_by_total_I':intervals[:20],
                'birth_mass_exact':{str(c):str(sum((u[r]*v for r,v in rr.items()),F(0))) for c,rr in by_birth.items()},
                'output_mass_exact':{str(r):str(u[r]*v) for r,v in by_output.items()},
                'elapsed_seconds':time.monotonic()-began,
                'source_sha256':{str(p.relative_to(ROOT)):sha(p) for p in SOURCES},
                'evaluator_sha256':sha(__file__),
                'arithmetic_scope':'Fractions certify all prices, P_b, I_j, coverage, Sidon and caps. 55-digit Decimal square roots and cap ratios are approximations, not certified enclosures.',
                'logical_scope':'Finite diagnostics only; neither existence nor nonexistence of uniform K(C,m0) is proved.'}
    return result,records

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--sizes',default='12,24,48,96')
    p.add_argument('--campaign',default='C1_m02_greedy')
    p.add_argument('--variant',type=int,default=0)
    args=p.parse_args()
    sizes=[int(x) for x in args.sizes.split(',')]
    choices=() if args.variant==0 else tuple(1 if k in (3,6,9) else 0 for k in range(10))
    all_a=greedy(max(sizes),choices=choices)
    for M in sizes:
        result,records=evaluate(all_a[:M],args.campaign)
        if M==12 and args.variant==0:
            assert result['a']==[1,2,4,8,13,21,31,45,66,81,97,123]
            assert result['core_records']==20
            expected={7:F(42967789,23906323584000),8:F(16592136787,1577817356544000),
                      9:F(24872453269,2524507770470400),10:F(993,152181458)}
            assert {int(k):F(v) for k,v in result['profile_exact'].items()}==expected
            result['fixture_exact_match']=True
        path=HERE/f'{args.campaign}_M{M}.json'
        path.write_text(json.dumps(result,indent=2)+'\n')
        record_path=HERE/f'{args.campaign}_M{M}_records.json'
        record_path.write_text(json.dumps({'columns':['d','e','p_d','q_d','p_e','q_e','c','s','i','r','t'],
                                           'records':records},separators=(',',':'))+'\n')
        print(json.dumps({'path':str(path),'M':M,'core':result['core_records'],
                          'N':result['N_approx'],'maxcap':result['cap_use_max_approx'],
                          'blocks':[(b['j'],b['I_approx'],b['actual_block_approx']) for b in result['blocks']],
                          'seconds':result['elapsed_seconds']}),flush=True)

if __name__=='__main__':
    main()

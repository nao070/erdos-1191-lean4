#!/usr/bin/env python3
"""Retain and integrate the actual C143 contraction's C133 terminal rows.

Exact finite accounting; a terminal is not declared paid merely because
the fourteen-row identity holds.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from c143_weight_extension import BANK, EXPECTED_SHA, point_matrix_integer


def u_affine(points, epoch, mult, left, right):
    # U=q^T M q, q amplitude 8/m. Off-diagonal pair coefficient is
    # 2*(8/m)^2*M_ij = 16*K_ij/(m^2*epoch^2).
    matrix = point_matrix_integer(epoch)
    origins = points[epoch-1:2*epoch]
    sample = (left+right)/2
    a=b=F(0)
    for i in range(epoch+1):
        for j in range(i+1,epoch+1):
            coeff = F(16*matrix[i][j],mult*mult*epoch*epoch)
            if not coeff:
                continue
            d=origins[j]-origins[i]
            if d<=mult*sample:
                a-=3*coeff*d; b+=2*coeff*mult
            elif d<=2*mult*sample:
                a+=coeff*d; b-=2*coeff*mult
    return a,b


def log_bounds(q,terms=40):
    assert 1<=q<=2
    z=(q-1)/(q+1)
    low=sum((2*z**(2*k+1)/F(2*k+1) for k in range(terms)),F(0))
    return low,low+2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))


def integrate(a,b,l,r):
    lo,hi=log_bounds(r/l)
    rat=a*(1/l-1/r)
    return (rat+b*lo,rat+b*hi) if b>=0 else (rat+b*hi,rat+b*lo)


def fence(lo,hi,den=10**12):
    flo=(lo.numerator*den)//lo.denominator
    cei=-((-hi.numerator*den)//hi.denominator)
    return [str(F(flo,den)),str(F(cei,den))]


def main():
    raw=BANK.read_bytes();assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA
    bank=json.loads(raw);points=bank['points'];n=bank['n']
    L,R=F(bank['children'][0]['left']),F(bank['children'][-1]['right'])
    epochs=(n//2,n,2*n)
    breaks={L,R}
    for e in epochs:
        origins=points[e-1:2*e]
        for i in range(e+1):
            for j in range(i+1,e+1):
                d=origins[j]-origins[i]
                for m in (1,2,4,8,16):
                    for t in (F(d,m),F(d,2*m)):
                        if L<t<R:breaks.add(t)
    breaks=sorted(breaks)
    totals={}; minimum_old=None;maximum_old=None;max_ledger_error=F(0)
    for l,r in zip(breaks,breaks[1:]):
        U={(e,s):u_affine(points,e,2**s,l,r) for e in epochs for s in range(5)}
        rows={}
        for s in range(4):
            pref=F(2**(s+1)-1,128)
            rows[f'initial:A{n}:s{s}']=tuple(-pref*(U[n//2,s][i]-U[n//2,s+1][i]) for i in (0,1))
            rows[f'shared:A{2*n}:s{s}']=(F(0),F(0)) # rho=1
            rows[f'final:A{4*n}:s{s}']=tuple(pref*sum(U[e,s][i]-U[e,s+1][i] for e in epochs) for i in (0,1))
        rows[f'terminal:e{n}:s4']=tuple(F(15,128)*x for x in U[n,4])
        rows[f'terminal:e{2*n}:s4']=tuple(F(15,128)*x for x in U[2*n,4])
        assert U[2*n,4] == (0,0) # C141 applies to later shell
        assert U[n//2,4] == (0,0)
        for i in (0,1):
            D=sum(F(2**s,128)*U[e,s][i] for e in (n,2*n) for s in range(4))
            assert sum(v[i] for v in rows.values()) == D
        for label,(a,b) in rows.items():
            lo,hi=integrate(a,b,l,r)
            prev=totals.get(label,(F(0),F(0)))
            totals[label]=prev[0]+lo,prev[1]+hi
        a,b=rows[f'terminal:e{n}:s4']
        for t in (l,r):
            entry=(a+b*t,t)
            minimum_old=entry if minimum_old is None or entry<minimum_old else minimum_old
            maximum_old=entry if maximum_old is None or entry>maximum_old else maximum_old
    old=totals[f'terminal:e{n}:s4']
    original=(F(bank['integral']['lower']),F(bank['integral']['upper']))
    # Diagnostic only: removing twice the old terminal from 2D-P gives
    # 2*(D-terminal)-P. This is not a derived necessity of every legal ledger.
    diagnostic=(original[0]-2*old[1],original[1]-2*old[0])
    result={
        'status':'EXACT_C143_SAME_ATOM_TERMINAL_LEDGER_RECONSTRUCTED',
        'bank_sha256':EXPECTED_SHA,'phase':[str(L),str(R)],
        'H_old':points[2*n-1]-points[n-1],'H_new':points[4*n-1]-points[2*n-1],
        'ledger_keys':len(totals),'integration_pieces':len(breaks)-1,
        'all_fourteen_row_affine_identities_pass':True,
        'row_integral_outward_rational_fences':{k:fence(*v) for k,v in totals.items()},
        'old_terminal_minimum':str(minimum_old[0]),'old_terminal_min_phase':str(minimum_old[1]),
        'old_terminal_maximum':str(maximum_old[0]),'old_terminal_max_phase':str(maximum_old[1]),
        'old_terminal_integral_positive':old[0]>0,
        'new_terminal_identically_zero':True,
        'diagnostic_integral_2D_minus_2oldterminal_minus_P_fences':fence(*diagnostic),
        'scope':{'general_global_terminal_payment':False,'Q1_resolved':False,
                 'diagnostic_subtraction_is_not_a_universal_no_go':True}
    }
    out=Path(__file__).with_name('C143_TERMINAL_LEDGER.json')
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':main()

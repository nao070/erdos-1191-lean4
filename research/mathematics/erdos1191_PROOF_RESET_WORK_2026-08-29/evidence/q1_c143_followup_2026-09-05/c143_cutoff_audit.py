#!/usr/bin/env python3
"""Compare C143's four-scale demand with the complete Wave box integral."""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from c143_weight_extension import BANK, EXPECTED_SHA, point_matrix_integer
from c143_terminal_audit import log_bounds, fence

DEN=10**30


def enclosure_round(lo,hi):
    return F((lo.numerator*DEN)//lo.denominator,DEN),F(-((-hi.numerator*DEN)//hi.denominator),DEN)


def logarithm(q):
    assert q>=1
    k=0
    while q>2:
        q/=2;k+=1
    lo,hi=log_bounds(q)
    l2,h2=log_bounds(F(2))
    return enclosure_round(lo+k*l2,hi+k*h2)


def Q_integral(points,e,A,B):
    # Q(T)=sum_{i<j}2M_ij (T-d_ij)_+/T^2, direct box energy.
    origins=points[e-1:2*e];mat=point_matrix_integer(e)
    lo=hi=F(0)
    for i in range(e+1):
        for j in range(i+1,e+1):
            coeff=F(mat[i][j],4*e*e)
            if not coeff:continue
            d=F(origins[j]-origins[i]);a=max(A,d)
            if a>=B:continue
            ll,hh=logarithm(B/a)
            rat=d*(1/B-1/a)
            ll+=rat;hh+=rat
            if coeff>=0:lo+=coeff*ll;hi+=coeff*hh
            else:lo+=coeff*hh;hi+=coeff*ll
    return enclosure_round(lo,hi)


def lincomb(terms):
    lo=hi=F(0)
    for coeff,(a,b) in terms:
        if coeff>=0:lo+=coeff*a;hi+=coeff*b
        else:lo+=coeff*b;hi+=coeff*a
    return lo,hi


def main():
    raw=BANK.read_bytes();assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA
    b=json.loads(raw);points=b['points'];n=b['n'];L=F(b['children'][0]['left'])
    results={};Ws=[];Is=[]
    for e in (n,2*n):
        H=F(points[2*e-1]-points[e-1])
        # Exact zero tail: sum_{i<j} M_ij = sum_{i<j} M_ij*d_ij=0.
        mat=point_matrix_integer(e);origins=points[e-1:2*e]
        assert sum(mat[i][j] for i in range(e+1) for j in range(i+1,e+1))==0
        assert sum(mat[i][j]*(origins[j]-origins[i]) for i in range(e+1) for j in range(i+1,e+1))==0
        W=Q_integral(points,e,F(0),H)
        low=Q_integral(points,e,F(0),L)
        next_band=Q_integral(points,e,L,2*L)
        tail16=Q_integral(points,e,16*L,max(16*L,H))
        tail32=Q_integral(points,e,32*L,max(32*L,H))
        I=lincomb([(2,Q_integral(points,e,L,16*L)),(-1,Q_integral(points,e,2*L,32*L))])
        correction=lincomb([(-1,low),(1,next_band),(-2,tail16),(1,tail32)])
        independent=lincomb([(1,W),(1,correction)])
        assert not (I[1]<independent[0] or independent[1]<I[0])
        Ws.append(W);Is.append(I)
        results[str(e)]={
            'W_complete':fence(*W),'four_scale_D_integral':fence(*I),
            'lower_cutoff_0_to_b':fence(*low),'band_b_to_2b':fence(*next_band),
            'tail_16b_to_infinity':fence(*tail16),'tail_32b_to_infinity':fence(*tail32),
            'D_integral_minus_W':fence(*correction),
        }
    margin=F(b['integral']['lower']),F(b['integral']['upper'])
    price=lincomb([(2,x) for x in Is]+[(-1,margin)])
    full_W_comparison=lincomb([(2,x) for x in Ws]+[(-1,price)])
    data={
        'status':'EXACT_C143_FULL_WAVE_CUTOFF_COMPARISON_OK',
        'bank_sha256':EXPECTED_SHA,'base_phase':str(L),
        'identity':'I_e = W_e - integral_0^b Q_e + integral_b^(2b) Q_e - 2 integral_(16b)^infinity Q_e + integral_(32b)^infinity Q_e',
        'epochs':results,'integrated_graph_price':fence(*price),
        'diagnostic_2W_old_plus_2W_new_minus_integrated_price':fence(*full_W_comparison),
        'diagnostic_strictly_negative':full_W_comparison[1]<0,
        'scope':{'cutoff_free_identification_D_equals_W':False,
                 'all_global_ledger_routes_refuted':False,'Q1_resolved':False}
    }
    Path(__file__).with_name('C143_CUTOFF_AUDIT.json').write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    print(json.dumps(data,indent=2,sort_keys=True))


if __name__=='__main__':main()

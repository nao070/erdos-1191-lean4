#!/usr/bin/env python3
"""Independent exact oracle for the load-bearing C132 conclusions.

This file does not import the main C132 verifier or any canonical Python
module.  It parses the pinned C130 JSON and independently reconstructs the
32-mark Golomb count, M16 residual, and natural epoch-16 owner failure.
"""

from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
C130_JSON = HERE / "ROUTE_C_C130_COMPLETE_C123_PHASE_PRIMAL_certificate.json"
A = (0,22,60,83,102,173,303,513,616,727,772,881,972,1041,1103,1169)
B = (0,22,60,83,154,284,494,513,575,620,711,777,880,989,1100,1169)
P = A + tuple(1239 + 5*x for x in B)
MULTIPLIERS = (1,2,4,8)


def differences(points):
    return [points[j]-points[i]
            for i in range(len(points)) for j in range(i+1,len(points))]


def wave_b(n):
    return [[
        F() if i == j or abs(i-j) == 1 else -F((j-i)**2,8*n*n)
        for j in range(n)
    ] for i in range(n)]


def incidence(n):
    return [[F((k == i)-(k == i+1)) for k in range(n+1)] for i in range(n)]


def point_m(n):
    b=wave_b(n); d=incidence(n)
    return tuple(tuple(
        sum((d[a][i]*b[a][c]*d[c][j]
             for a in range(n) for c in range(n)),F())
        for j in range(n+1)
    ) for i in range(n+1))


def quadratic(matrix,vector):
    return sum((F(vector[i])*matrix[i][j]*vector[j]
                for i in range(len(vector)) for j in range(len(vector))),F())


def residual_gate():
    m8=point_m(8); m16=point_m(16)
    half=[[F() for _ in range(17)] for _ in range(17)]
    for i in range(9):
        for j in range(9):
            half[i][j]+=m8[i][j]/4
            half[i+8][j+8]+=m8[i][j]/4
    residual=[[m16[i][j]-half[i][j] for j in range(17)] for i in range(17)]
    assert all(residual[i][i] == 0 for i in range(17))
    assert all(sum(row,F()) == 0 for row in residual)
    assert sum(residual[i][j] != 0
               for i in range(17) for j in range(17) if i != j)==160
    assert residual[0][8] == -F(1,32)
    assert residual[1][8] == F(15,2048)
    assert residual[1][9] == F(1,1024)
    gamma=lambda n:[F((j-i)**2,4*n*n)
                    for j in range(n+2,2*n) for i in range(n,j-1)]
    g8=gamma(8); g16=gamma(16)
    omitted_count=len(g16)-2*len(g8)
    omitted_mass=sum(g16,F())-sum(g8,F())/2
    assert (len(g8),sum(g8,F()),len(g16),sum(g16,F())) == (
        21,F(329,256),105,F(5425,1024)
    )
    assert (omitted_count,omitted_mass)==(63,F(4767,1024))
    return omitted_count,omitted_mass


def embed_reduced(column,block,size):
    assert len(column)+1==len(block)
    out=[0]*size
    for index,value in zip(block[:-1],column):
        out[index]=value
    out[block[-1]]=-sum(column)
    assert sum(out)==0
    return tuple(out)


def haar(x,width,origin,multiplier):
    d=x-origin
    return int(0<=d<multiplier*width)-int(
        multiplier*width<=d<2*multiplier*width
    )


def owner_oracle():
    payload=json.loads(C130_JSON.read_text(encoding="utf-8"))
    record=payload["factor_bank"]["records"][43]
    assert record["index"]==43
    assert (record["left"],record["right"]) == ("797/8","201/2")
    local_channels=tuple((rank,multiplier)
                         for multiplier in MULTIPLIERS for rank in range(3,16))
    epoch4=tuple(i for i,(rank,_) in enumerate(local_channels) if rank<=7)
    epoch8=tuple(i for i,(rank,_) in enumerate(local_channels) if rank>=8)
    local_columns=tuple(
        embed_reduced(tuple(column),epoch4,52) for column in record["n4"]["columns"]
    )+tuple(
        embed_reduced(tuple(column),epoch8,52) for column in record["n8"]["columns"]
    )
    assert (len(record["n4"]["columns"]),len(record["n8"]["columns"]))==(10,20)

    global_channels=tuple((rank,multiplier,P[rank])
                          for multiplier in MULTIPLIERS for rank in range(3,32))
    gi={(rank,m):i for i,(rank,m,_) in enumerate(global_channels)}
    mapped=[]
    for column in local_columns:
        out=[0]*len(global_channels)
        for value,(rank,m) in zip(column,local_channels):
            out[gi[(16+rank,m)]]=value
        assert sum(out)==0
        mapped.append(tuple(out))

    width=F(500)
    midpoint=F(1601,16)
    scale=F(1,100_000_000**2)/midpoint/5
    m16=point_m(16)

    def state(x):
        return tuple((8//m)*haar(x,width,origin,m)
                     for _,m,origin in global_channels)

    events=tuple(sorted({F(origin)+shift*m*width
                         for _,m,origin in global_channels for shift in (0,1,2)}))
    failures=[]
    for left,right in zip(events,events[1:]):
        current=state((left+right)/2)
        dots=tuple(sum(current[i]*c[i] for i in range(len(current))) for c in mapped)
        for m in MULTIPLIERS:
            group=tuple(gi[(rank,m)] for rank in range(16,32))
            gdots=tuple(sum(current[i]*c[i] for i in group) for c in mapped)
            owned=scale*sum((a*b for a,b in zip(gdots,dots)),F())
            z=tuple(current[gi[(rank,m)]] for rank in range(15,32))
            demand=F(m,128)*quadratic(m16,z)
            margin=width*owned-demand
            if margin<0:
                failures.append((margin,left,right,m,owned,demand,z))
    assert len(events)-1==173
    assert len(failures)==152
    strongest=min(failures)
    assert strongest == (
        -F(175_791_028_451_541,10_006_250_000_000_000),
        F(5169),F(5239),8,
        F(100_084_829_709,5_003_125_000_000_000_000),
        F(9,512),
        (-1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0),
    )
    return len(failures),strongest


def main():
    d=differences(P)
    assert len(d)==len(set(d))==496
    assert B[10]-B[5] == 143+B[5] == 427
    omitted_count,omitted_mass=residual_gate()
    failure_count,strongest=owner_oracle()
    print(
        "INDEPENDENT_EXACT_ORACLE_OK",
        f"span={P[-1]}",
        "differences=496",
        f"residual_sources={omitted_count}",
        f"residual_mass={omitted_mass}",
        "owner_rows=692",
        f"owner_failures={failure_count}",
        f"strongest_margin={strongest[0]}",
        "C058_open",
    )


if __name__=="__main__":
    main()

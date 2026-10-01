#!/usr/bin/env python3
"""One bounded, fixed-before-trial padding campaign; no new search harness."""
from collections import defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib, json, math, random
from reference_evaluator import evaluate, differences, log_bounds
from independent_checker import check, log_fixed, SCALE

HERE = Path(__file__).resolve().parent
OUT = HERE / 'C1000000_m02_M12_target'
OUT.mkdir(exist_ok=True)
SEED = 119100012
MAX_TRIALS = 1000
C = F(1000000)
M0 = 2
ANCHORS = {1:1, 3:30001, 6:32001, 8:67001, 11:100001, 12:105001}
FORCED = frozenset(( (3,6,12), (1,8,11) ))

def write(name, data):
    (OUT/name).write_text(json.dumps(data, indent=2)+'\n')

manifest = {'C_exact':str(C), 'm0':M0, 'M':12, 'T':12,
            'seed':SEED, 'maximum_padding_trials':MAX_TRIALS,
            'fixed_anchors':ANCHORS,
            'rejection_tests':['duplicate positive differences',
                'any disjoint distinct-index triple collision except the forced collision'],
            'forced_rank_triples':[list(x) for x in sorted(FORCED)],
            'scope':'One fixed finite campaign, not an unbounded family or Q1 counterexample.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
write('campaign_fixed_before_trials.json', manifest)
rng = random.Random(SEED)
rejections = defaultdict(int)
chosen = None
for trial in range(1,MAX_TRIALS+1):
    mid1 = sorted(rng.sample(range(30002,32001),2))
    mid2 = sorted(rng.sample(range(67002,100001),2))
    a = [1,rng.randrange(2,30001),30001,*mid1,32001,
         rng.randrange(32002,67001),67001,*mid2,100001,105001]
    assert all(a[k-1]==v for k,v in ANCHORS.items())
    try:
        differences(a)
    except AssertionError:
        rejections['positive_difference_collision'] += 1
        continue
    by_sum = defaultdict(list)
    collisions=[]
    for tri in combinations(range(1,13),3):
        total = sum(a[k-1] for k in tri)
        for old in by_sum[total]:
            if set(old).isdisjoint(tri):
                collisions.append((old,tri,total))
        by_sum[total].append(tri)
    if any(frozenset((x,y)) != FORCED for x,y,total in collisions):
        rejections['additional_disjoint_triple_collision'] += 1
        continue
    assert len(collisions)==1 and frozenset(collisions[0][:2])==FORCED
    chosen=(a,trial,collisions)
    break

if chosen is None:
    write('bounded_search_result.json', {'status':'NO_WITNESS_WITHIN_BUDGET',
          'trials':MAX_TRIALS,'rejections':dict(rejections)})
    raise SystemExit('No witness within the authorized fixed budget')
a,trial,collisions=chosen
data, records = evaluate(a, 'C1000000_m02_M12_target', C=C, m0=M0)
path = OUT/'C1000000_m02_M12_target.json'
write(path.name,data)
write(path.stem+'_records.json', {'columns':['d','e','p_d','q_d','p_e','q_e','c','s','i','r','t'],
      'records':records})
check(path)
assert len(records)==2
assert all(sorted((rec[2],rec[3],rec[4],rec[5]))==[1,3,6,8] for rec in records)
assert all(rec[8:]==[11,12,5000] for rec in records)
assert {rec[7] for rec in records}=={3,6}
u = F(data['u_M_exact'])
A,B,Cgap,H = 30000,2000,35000,67000
AC,BH=A*Cgap,B*H
assert sum(rec[0]*rec[1] for rec in records)==2*AC+BH
lc,uc=log_fixed(8)
threshold_lo=F(64*SCALE**3,uc**3)
threshold_hi=F(64*SCALE**3,lc**3)
assert min(A,B,Cgap)>threshold_hi
Iac = 2*AC*u*F(19,90)
Ibh = BH*u*F(19,90)
assert Iac>Ibh

def sqrt_enclosure(x, scale=10**40):
    z=math.isqrt(x.numerator*scale*scale//x.denominator)
    assert F(z,scale)**2<=x<F(z+1,scale)**2
    return F(z,scale),F(z+1,scale)

components={}
with localcontext() as ctx:
    ctx.prec=60
    for key,p in [('AC',2*AC*u),('BH',BH*u),('full',(2*AC+BH)*u)]:
        lo,hi=sqrt_enclosure(p)
        hlo,hhi=lo*F(19,90),hi*F(19,90)
        dec=(Decimal(p.numerator)/Decimal(p.denominator)).sqrt()*Decimal(19)/90
        components[key]={'profile_at_each_of_9_10_exact':str(p),
                         'I_j3_exact':str(p*F(19,90)),
                         'actual_j3_sqrt_harmonic_sum_approx':str(dec),
                         'actual_j3_certified_lower':str(hlo),
                         'actual_j3_certified_upper':str(hhi)}
result={'status':'CERTIFIED_POINTWISE_AND_DYADIC_COUNTEREXAMPLE',
        'a':a, 'success_trial':trial, 'trials_used':trial,
        'rejections':dict(rejections),
        'C_exact':str(C), 'm0':M0, 'M':12, 'T':12,
        'only_disjoint_triple_collision':collisions,
        'core_records':len(records), 'unknown_comparisons':0,
        'old_quad_ranks':[1,3,6,8], 'old_quad_points':[1,30001,32001,67001],
        'gaps_A_B_C':[A,B,Cgap], 'H_quad':H, 'AC':AC, 'BH':BH,
        'log8_lower_scaled':lc, 'log8_upper_scaled':uc, 'log_scale':SCALE,
        'small_gap_threshold_lower_exact':str(threshold_lo),
        'small_gap_threshold_upper_exact':str(threshold_hi),
        'all_three_gaps_strictly_large_certified':True,
        'actual_output_ranks':[11,12], 'actual_output_points':[100001,105001],
        'actual_cut_interval':[9,10], 'genuine_u12_M12_exact':str(u),
        'alpha13_retained':True,
        'Q_AC_minus_Q_BH_at_b9_and_b10_exact':str((2*AC-BH)*u),
        'I_AC_minus_I_BH_j3_exact':str(Iac-Ibh),
        'Q_AC_over_Q_BH_exact':str(F(2*AC,BH)),
        'block_cut':[8,12], 'components':components,
        'certified_sqrt_method':'Integer square root at scale 10^40; the profile has exactly two equal nonzero cuts.',
        'scope':'Rejects constant-one cut and dyadic AC<=BH estimates on the unchanged strict all-large-old-gap core, at one fixed finite cap. Does not reject uniform K(C,m0), any different-constant estimate, or Q1.',
        'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'source_sha256':data['source_sha256']}
write('bounded_search_result.json',result)
print(json.dumps({k:result[k] for k in ['status','a','success_trial','core_records',
      'genuine_u12_M12_exact','Q_AC_minus_Q_BH_at_b9_and_b10_exact',
      'I_AC_minus_I_BH_j3_exact','Q_AC_over_Q_BH_exact','components']},indent=2))

"""Preserved exact code from three separately executed review cells.

Saved after execution on 2026-09-05; not rerun merely for archiving.
Section 1 output: 864496 presentations; 5735 negative; all assertions PASS.
Section 2 output: every stage k=0..6 passed, final 128 marks / 8128 differences.
Section 3 output: exact rearrangement inequality and common collision passed.
These are finite checks, not a Q1 proof or Lean verification.
"""

from fractions import Fraction

# Cell 1: exact moment/state verification, as executed.
checks = 0
negative = 0
for e in range(1, 65):
    for left in range(e + 2):
        for minus in range(e + 2 - left):
            for plus in range(e + 2 - left - minus):
                right = e + 1 - left - minus - plus
                q = [0]*left + [-1]*minus + [1]*plus + [0]*right
                delta = [(i, q[i]-q[i+1]) for i in range(e) if q[i] != q[i+1]]
                s0 = sum(v for i,v in delta)
                s1 = sum(i*v for i,v in delta)
                s2 = sum(i*i*v for i,v in delta)
                adj = sum(v*w for i,v in delta for j,w in delta if j == i+1)
                direct = -sum((i-j)**2*v*w for i,v in delta for j,w in delta if j >= i+2)
                moment = s1*s1-s0*s2+adj
                assert direct == moment
                expected_negative = left >= 1 and right >= 1 and (minus, plus) in {(1,1),(1,2),(2,1)}
                assert (moment < 0) == expected_negative, (e,q,moment)
                assert moment >= -4
                if q[0] != q[-1]:
                    assert len(delta) <= 2 and moment >= 0
                norm2 = sum(v*v for i,v in delta)
                assert 3*moment + 2*norm2 >= 0
                checks += 1
                negative += moment < 0
print({'ranks': '1..64', 'pattern_presentations_checked': checks, 'negative_presentations': negative, 'identity_classification_and_K_positivity': 'PASS'})
e=3
q=[3,2,1,0]
delta=[q[i]-q[i+1] for i in range(e)]
N=-sum((i-j)**2*delta[i]*delta[j] for i in range(e) for j in range(i+2,e))
K=Fraction(N,4*e*e)+Fraction(sum(v*v for v in delta),6*e*e)
assert K == Fraction(-1,18)
print({'non_PSD_example': {'e': e, 'q': q, 'qKq': str(K)}})

# Cell 2: recursively constructed infinite-Sidon example, finite corroboration.
A=[0]
for k in range(7):
    e=2**k
    b0=A[-1]
    S=b0+1
    L=2*e*e+1
    block=[b0+S*(L*i+i*i) for i in range(e+1)]
    A.extend(block[1:])
    ds={}
    for j in range(len(A)):
        for i in range(j):
            d=A[j]-A[i]
            assert d not in ds,(k,d,ds.get(d),(i,j))
            ds[d]=(i,j)
    assert len(A) == 2*e
    assert (A[-1]+1) == S*(2*e**3+e**2+e+1)
    gaps=[block[i+1]-block[i] for i in range(e)]
    assert max(gaps) < 2*min(gaps)
    lower=Fraction((e-1)*(e-2),32*e*e)
    print({'k':k,'epoch':e,'marks':len(A),'max_mark_digits':len(str(A[-1])),'unique_positive_differences':len(ds),'W_lower_bound':str(lower) if e>=4 else 'not asserted'})

# Cell 3: exact falsification of two further candidate shortcuts.
def cross_ratio_product(h):
    e=len(h)
    p=[0]
    for x in h:p.append(p[-1]+x)
    result=Fraction(1)
    for i in range(e):
        for j in range(i+2,e):
            m=p[j]-p[i+1]
            result *= Fraction((m+h[i])*(m+h[j]),m*(m+h[i]+h[j]))**((j-i)**2)
    return result

sorted_gaps=(1,2,4,8,16)
permuted_gaps=(1,4,16,8,2)
for h in [sorted_gaps,permuted_gaps]:
    marks=[0]
    for g in h: marks.append(marks[-1]+g)
    diffs=[marks[j]-marks[i] for j in range(len(marks)) for i in range(j)]
    assert len(diffs)==len(set(diffs))
a,b=cross_ratio_product(sorted_gaps),cross_ratio_product(permuted_gaps)
assert b<a
print({'exact_W_rearrangement_comparison':'W(1,4,16,8,2) < W(1,2,4,8,16)','both_prefix_rulers':'Sidon','ratio_numerator_bit_length':(a/b).numerator.bit_length(),'ratio_denominator_bit_length':(a/b).denominator.bit_length()})
B=[0]
for n in range(1,118): B.append(B[-1]+n*(n&-n))
assert B[104]-B[76] == B[117]-B[93] == 9512
assert 104**2-76**2 == 117**2-93**2 == 5040
print({'hierarchical_collision_values':{i:B[i] for i in [76,93,104,117]},'common_B_difference':9512,'common_square_difference':5040,'all_real_quadratic_coefficients':'collision persists'})

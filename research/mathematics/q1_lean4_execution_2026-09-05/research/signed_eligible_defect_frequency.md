# The full eligible geometry defect diverges under the fixed cap

2026-09-05. Author: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Status.** For the actual raw signed feature and every fixed
0<=lambda<=1, the FULL stage defect
G_(lambda,r)=(1+lambda)DeltaY_r-8H_(lambda,r) has

```
sum_(r<=T)u_r G_(lambda,r) -> infinity
```

under the existing one-fixed-onset cap and its established good-epoch
consequence.
The proof uses all equal-three-sum fibers, including collisions with
repeated newest endpoints. It gives a quantitative cumulative defect
bound and does not assume a frequency distribution of individual small
deficits. Consequently the larger energy budget minus eligible capacity,
and hence that energy budget minus any permitted optimized demand,
diverges. The smaller eligible-capacity-minus-demand comparison remains
unresolved. This is not an original-Q1 proof.

The parent suggested seeking an energy/defect tradeoff instead of losing
a logarithm in a pointwise rank-separation bound. The fiber potential
below implements that direction. Both the moment agent and the causal
agent independently confirmed the matching identity for every distinct
multiset pair, including newest-repeated groups. This note is analytical:
no numerical test, old-check rerun, Lean execution, or new formal
verification was used. Only this new note was written.

Inputs are the exact source constructions and identities in
`signed_output_energy_closure.md`, `signed_eligible_separation_deficit.md`,
`signed_multiset_born_retirement.md`, and the existing good-index result
used in `signed_born_quantitative_gain.md`.

Throughout, P_N={a_1<...<a_N} is the actual integer Sidon prefix,
Q_N=N(N-1), H_N=a_N-a_1, alpha_N=Q_N^-2,
kappa_N=alpha_N-alpha_(N+1), w_N=alpha_N/H_N^2, and
u_N=sum_(k>=N)kappa_k/H_k^2. The price u is fixed from the one
complete history. Y_N=E_N-N Z_N is the raw signed energy with its
diagonal removed. The symbol H_(lambda,r) denotes the stage-r eligible
carrier mass, not a prefix width: it sums |de|+lambda de over actual
source pairs whose unique output endpoints have ranks b<i<r, where
b is their latest source birth. G_(lambda,r) includes the full Y
increment at stage r and subtracts eight times only this eligible mass.

## 1. A symmetric triple potential controlled by the full defect

For a three-point multiset U, sort its occurrences as x<=y<=z and define

```
Ptop(U)=(z-x)(z-y)>=0,
sigma_U^2=sum_(a in U)(a-mean(U))^2,
aut(U)=product_(point values a)(multiplicity_U(a))!.
```

Ptop is well-defined even when the largest point repeats: its value is
then zero. It is independent of any ordering of equal slots. If
p=z-x and q=z-y, then

```
sigma_U^2=(2/3)(p^2+q^2-pq),
Ptop(U)=pq<=(3/2)sigma_U^2.                          (1)
```

Fix distinct equal-sum multisets U,V from the actual Sidon prefix.
Their supports are disjoint, by cancellation and repeated two-sum
uniqueness. Write A=aut(U)aut(V).

First suppose the collision has an eligible output, so

```
U={ell,u,v}, V={n,x,y}, n>ell>max(u,v,x,y),
t=n-ell, p=ell-u, q=ell-v,
Aold=ell-x, Bold=ell-y, s=p+q,
Aold+Bold=s+t.
```

The exact eligible carrier calculation already proves

```
G_lambda(U,V)
 >=8(1+lambda)[pq+Aold Bold+ts+t^2]/A.
```

But Ptop(U)=pq and
Ptop(V)=(t+Aold)(t+Bold)=Aold Bold+ts+2t^2. Hence

```
G_lambda(U,V)
 >=4(1+lambda)[Ptop(U)+Ptop(V)]/A.                   (2)
```

The difference between the bracket with coefficient 8 and the bracket
with coefficient 4 is 4[pq+Aold Bold+ts]>=0. Thus (2) retains a
symmetric positive potential of both triples; it does not replace the
defect by a potentially vanishing relative separation factor.

If the collision has no eligible output, its entire defect is
(1+lambda) times its full contribution to Y. The matching proof below
gives that contribution as 12(sigma_U^2+sigma_V^2)/A. Equation (1)
then proves (2) again, even with coefficient 8 instead of 4. Thus the
weaker common coefficient 4 works for every DISTINCT multiset pair.

## 2. Full matching energy does not require a unique newest endpoint

Give all slots auxiliary labels and consider their six bijections from
U to V. Each matching has three nonzero signed edge values d1,d2,d3
whose sum is zero. Its formal full signed Schur-group product sum is

```
d1^2+d2^2+d3^2.
```

For distinct numeric magnitudes x+y=z, this equals the six-entry sum
2yz+2xz-2xy=x^2+y^2+z^2. In the doubled case x+x=2x, the formal
list deliberately counts each of the three actual pairs twice, and the
same edge-square identity remains valid.

Across all six labeled matchings, each possible U-to-V edge occurs
twice. If s0=sum U=sum V, their total square sum is therefore

```
2sum_(u in U,v in V)(u-v)^2
 =6sum_U u^2+6sum_V v^2-4s0^2
 =6(sigma_U^2+sigma_V^2).                            (3)
```

The same exact orbit normalization applies independently of newest-point
multiplicity. A physical pattern with distinct edges has A labeled
realizations. A repeated edge has A/2 realizations and twice the actual
formal pair list. These factors cancel when the six formal matching
totals are divided by A. Therefore the full raw product sum and the
full Y contribution of this collision are exactly

```
raw total=6(sigma_U^2+sigma_V^2)/A,
DeltaY(U,V)=12(sigma_U^2+sigma_V^2)/A.                (4)
```

If the newest endpoint repeats, no record can retire: a retired record
would express its unique new output endpoint once against four old source
endpoints and its old lower output endpoint. Thus all its groups are
Born-only, the eligible carrier is zero, and (4) supplies its full defect.

Every actual numeric Schur group uniquely recovers its actual physical
edges and hence its unordered pair {U,V}, including repeated slots.
Conversely every pair of distinct equal-sum multisets supplies exactly
the groups counted by this matching construction. Thus summing (2)
over unordered distinct multiset pairs neither omits such groups nor
duplicates them. Groups with U=V are the separate automatic remainder;
they have no eligible output and nonnegative full Y contribution. They
are retained as a nonnegative remainder, rather than given a false free
orbit formula.

## 3. Exact fiber grouping and its finite diagonal

Fix the actual prefix P_N and write H=H_N>=1. For each integer s let
T_s be ALL three-point multisets from P_N with sum s, including repeated
point values. Define

```
w(U)=1/aut(U),
S_s=sum_(U in T_s)w(U),
P_s=sum_(U in T_s)w(U)Ptop(U),
Ptot_N=sum_s P_s.
```

Let Gcum_N(lambda)=sum_(r=2..N)G_(lambda,r). Its complete multiset
partition and (2) imply

```
Gcum_N(lambda)
 >=4(1+lambda)sum_s
       [S_s P_s-sum_(U in T_s)w(U)^2 Ptop(U)].        (5)
```

Indeed the bracket equals the sum over UNORDERED distinct {U,V}
of w(U)w(V)[Ptop(U)+Ptop(V)]. The single diagonal subtraction is
essential. There is no independent capacity being assigned to fibers.

Each multiset has exactly 6/aut(U) ordered realizations. Therefore

```
sum_U w(U)=N^3/6,
sum_U w(U)^2 Ptop(U)<=H^2 sum_U w(U)=N^3H^2/6.       (6)
```

Here w(U)<=1 and Ptop(U)<=H^2. The diagonal error is finite and explicit,
including all repeated triples; it is not a heuristic O(N^3) exception.

The possible sums lie in the integer interval [3a_1,3a_N], of length
3H+1. Pointwise P_s<=H^2 S_s, so Cauchy gives

```
sum_s S_sP_s >=sum_s P_s^2/H^2
             >=Ptot_N^2/[H^2(3H+1)].
```

Consequently, on EVERY actual finite prefix,

```
Gcum_N(lambda)
 >=4(1+lambda){Ptot_N^2/[H^2(3H+1)]-N^3H^2/6}.      (7)
```

The first term is a full positive weighted triple-fiber energy. In
particular no independent distributional assumption about near-saturated
collisions has entered. Concentration of their triples also enters this
same energy rather than being charged solely through a small relative
gap.

## 4. A good prefix forces a quantitative defect

Take the already established good dyadic ranks N, divisible by four,
with

```
H_(N/2)>=2H_(N/4),
H_N<=K H_(N/2),
H_(2N)<=K H_N,                    K=32.              (8)
```

The last condition will be used only for compatible-price weighting.
Choose the largest triple slot from ranks N/2+1,...,N and the two
other slots, with repetition permitted, from ranks 1,...,N/4. Each
top gap is at least H_N/(2K). For a fixed largest slot, the sum of
weights 1/aut over the unordered two smaller slots is exactly

```
binom(N/4,2)+(N/4)/2=(N/4)^2/2.
```

Thus these actual triples alone give

```
Ptot_N >=beta N^3H_N^2,
beta=1/(256K^2)=2^-18 at K=32.                      (9)
```

Every counted triple has its specified upper-half slot as its unique
maximum. The diagonal case of the two lower slots has weight 1/2,
which is why (9) counts occurrences correctly.

Use 3H+1<=4H in (7). Equations (7)--(9) yield

```
Gcum_N(lambda)
 >=(1+lambda)[beta^2 N^6H_N-(2/3)N^3H_N^2].          (10)
```

Assume now ONE fixed C>0 and onset n0 such that
H_n<=C n^2 log(2n) for every n>=n0. For every good N beyond that
onset, multiplying by w_N=1/(Q_N^2H_N^2) proves

```
w_N Gcum_N(lambda)
 >=(1+lambda)[beta^2/(C log(2N))-2N/(3(N-1)^2)].      (11)
```

For the positive term use N^6/Q_N^2>=N^2; the displayed negative term
is exact. Its dyadic sum converges. In particular (11) is eventually
positive and supplies a reciprocal-log lower bound on an actual
cumulative defect, not on an abstract substitute history.

## 5. Weighted defect divergence with the actual fixed prices

The full stage defects are nonnegative by their exact complete-group
decomposition, so Gcum_N is nondecreasing. For the compatible price,
finite summation by parts gives

```
Gcal_T(lambda,u):=sum_(r=2..T)u_r G_(lambda,r)
 =u_T Gcum_T(lambda)
    +sum_(n=2..T-1) kappa_n Gcum_n(lambda)/H_n^2.      (12)
```

All terms are nonnegative. On [N,2N) for a good N, monotonicity and
H_n<=H_(2N)<=K H_N imply that its Abel interior contributes at least

```
Gcum_N/H_(2N)^2 sum_(n=N..2N-1)kappa_n
 >=gamma_* w_N Gcum_N,
gamma_*=15/(16K^2).                                (13)
```

Here alpha_N-alpha_(2N)>=15alpha_N/16. Distinct good dyadic intervals
are disjoint. The established good-index theorem gives
sum_good 1/log(2N)=infinity. Inserting (11) into (13), retaining
the finite initial ranks and the absolutely summable dyadic negative
terms, proves

```
Gcal_T(lambda,u) -> infinity.                         (14)
```

This holds for lambda=0, lambda=1, and all intermediate fixed values.
The lower bound divided by 1+lambda is uniform over this interval.
Exactly the same argument for w uses
w_N-w_(2N)>=15w_N/16, and proves divergence for the direct price
with the larger interval factor 15/16. No source-price substitution
on retired records occurs: G_(lambda,r) is always priced at its actual
full stage r.

Keeping the previously established quantitative good-index bound,
sum_(good k<=J)1/k >=(1/6)log log J-O(1) with N=2^(k+1), gives
for T>=2^(J+2), at K=32,

```
Gcal_T(lambda,u)
 >=(1+lambda)5/[2^51 C log 2] log log J-O_(C,history)(1). (15)
```

Replacing 1/k by 1/(k+2) changes the sum by only a bounded amount.
The rate concerns the exponent cutoff J; it is not a log log T lower
bound. The qualitative result (14) needs only the divergent good-index
sum, not this optional rate.

## 6. Consequence for the exact physical energy budget

The output-source identities retain the actual same budget:

```
Elig_T(Psi_lambda)
 =(1+lambda)Ycal_T(u)/8-Gcal_T(lambda,u)/8,
Dstar_T(lambda)<=Elig_T(Psi_lambda).
```

Therefore under the single fixed cap,

```
(1+lambda)Ycal_T(u)/8-Elig_T(Psi_lambda)
 =Gcal_T(lambda,u)/8 -> infinity,

(1+lambda)Ycal_T(u)/8-Dstar_T(lambda) -> infinity.     (16)
```

The second, LARGER energy-minus-demand bounded-margin criterion in
`signed_output_energy_closure.md` consequently cannot hold under that
cap. This conclusion uses the full defect, including all Born-only
and ineligible collision energy. No physical label or component budget
is spent again to obtain it.

Equivalently, if q_k is that note's nonnegative residual
(1+lambda)Y_k/8-Pi_k, its series sum_k kappa_k q_k/H_k^2 diverges:
q_k>=Gcum_k(lambda)/8 and the same disjoint good windows apply.

This does NOT establish divergence or boundedness of the SMALLER
eligible-capacity-minus-demand residual r_k. The geometry defect is
already removed from that smaller capacity. Nor is (14) a contradiction
between two quantities known to be equal: the exact accounting identity
explicitly retains their positive difference.

The new result answers the frequency question through a full-fiber
energy bound. It proves actual weighted defect divergence and its rate
under the same capped history, while leaving the eligible allocation
and projection residual, and original Q1, unresolved.

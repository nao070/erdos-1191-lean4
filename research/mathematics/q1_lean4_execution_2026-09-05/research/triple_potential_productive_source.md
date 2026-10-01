# A triple-potential source financed by the full geometry defect

2026-09-05. Author: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Status.** The symmetric triple potential produces one permanent PSD,
entrywise nonnegative source Theta. It has finite total trace. Its literal
historical capacity, including never-used outputs and the full future
component tail, is financed by the exact full geometry defect plus an
explicit constant. On an actual history with one fixed cap, the source
also pays nonsummable future demands. The productive allocation uses each
fixed component across many later physical intervals; it does not renew
the component's label budget at any interval.

This does not bound the smaller eligible-capacity-minus-demand residual
or prove original Q1. The final section gives the precise combined budget
and the remaining obstruction. No numerical test, prior-check replay, or
Lean execution was used. Only this new note was written.

The input is `signed_eligible_defect_frequency.md`, frozen SHA256
`292ce3b077858c742921bd59fe5d24c46a7aa35d630fad0e6e92f28d6ac9d3cd`,
and the fixed source/payment conventions in
`signed_output_energy_closure.md` and `signed_output_clock_source.md`.
The parent suggested spending a fixed component across a longer physical
horizon to avoid the extra logarithmic loss of a single nearby block.

## 1. Exact generating object and a positive Gram source

Fix one complete increasing integer Sidon history, including repeated
two-sum uniqueness. Write

```
P_k={a_1<...<a_k}, Fhat_k=Delta P_k union(-Delta P_k),
Q_k=k(k-1), H_k=a_k-a_1,
alpha_k=Q_k^-2, kappa_k=alpha_k-alpha_(k+1),
u_r=sum_(k>=r)kappa_k/H_k^2.
```

All sources below have these physical signed difference labels. The
complete-history component sequence is fixed once, and existing entries
are not renormalized when a terminal prefix grows.

For a triple multiset U with sorted slots x<=y<=z, set
Ptop(U)=(z-x)(z-y) and w(U)=1/aut(U). Define the actual full fibers

```
S_k(s)=sum_(U subset_multiset P_k, sum U=s)w(U),
P_k^top(s)=sum_(U subset_multiset P_k, sum U=s)w(U)Ptop(U).
```

The second coefficient sequence has the exact Laurent-polynomial formula

```
sum_s P_k^top(s) z^s
 =1/2 sum_(j<=k) z^(a_j)
       [sum_(i<j)(a_j-a_i)z^(a_i)]^2.                (1)
```

Indeed Ptop vanishes when a largest endpoint repeats. For a unique
largest endpoint j, distinct smaller endpoints occur in two orders in
the square, and equal smaller endpoints occur once with coefficient
1/2. These are precisely their weights 1 and 1/2.

Let

```
R_k(s)=sqrt(S_k(s)P_k^top(s))>=0,
L_k=sum_s R_k(s)^2,
A_k(d,e)=sum_s R_k(s+d)R_k(s+e)/(Q_k^2H_k^2),
Theta=sum_(k>=2)kappa_k A_k.                         (2)
```

Here A_k is zero off Fhat_k in each matrix index. It is a Gram matrix
of translates of R_k, and every entry is nonnegative. Thus Theta is PSD
and entrywise nonnegative on every finite restriction. Its diagonal,
its future component tail, and its capacity are priced below; no output
mask or unpriced completion is implicit in (2).

This uses the actual fiber product S_k P_k^top, not the unnormalized
autocorrelation of the polynomial in (1). The square root in (2) makes
the squared feature norm exactly the fiber quantity controlled by G.

## 2. Complete fiber bounds, trace, and terminal tail

Distinct equal-sum triples have disjoint supports. Moreover
1/aut(U)<=|support(U)|/3 in all three multiplicity cases: distinct,
one doubled slot, or three equal slots. Hence

```
S_k(s)<=k/3,        P_k^top(s)<=H_k^2 S_k(s),
sum_s S_k(s)=k^3/6,
0<=L_k<=k^4H_k^2/18.                                (3)
```

The full-defect theorem gives a second, structurally different bound.
For any fixed 0<=lambda<=1, let

```
G_(lambda,r)=(1+lambda)DeltaY_r-8H_(lambda,r)>=0,
Gcum_k(lambda)=sum_(r=2..k)G_(lambda,r),
Gcal_N(lambda,u)=sum_(r=2..N)u_rG_(lambda,r).
```

Here H_(lambda,r) is the actual eligible carrier mass at output stage r;
it is not a prefix width. The exact full-fiber partition, with its
diagonal retained, implies

```
L_k<=Gcum_k(lambda)/[4(1+lambda)]+k^3H_k^2/6.        (4)
```

Write M_k for the full matrix mass of A_k and T_k for its trace. Then

```
M_k<=L_k/H_k^2,
T_k=L_k/(Q_kH_k^2)<=k^4/(18Q_k)<=k^2/9.
```

The mass bound uses Cauchy on each translate pair, equivalently
A_k(d,e)<=L_k/(Q_k^2H_k^2). The exact telescoping sums

```
sum_(k>=2)kappa_k k^2=5/4,
sum_(k>=2)kappa_k k^3=2 zeta(2)+1/4=:D_3            (5)
```

show that tr Theta<=5/36. For example summation by parts gives
sum kappa_k k^p=2^p alpha_2+
sum_(k>=3)alpha_k[k^p-(k-1)^p]; the p=2 sum telescopes,
and the p=3 sum uses sum_(k>=2)alpha_k=2zeta(2)-3.

For a restriction to Fhat_N, the mass from components k>N obeys

```
M_tail,N
 <=Q_N^2/18 sum_(k>N)kappa_k k^4/Q_k^2
 <=(N-1)^2/(18N^2)<=1/18.                            (6)
```

The second inequality uses k/(k-1)<=(N+1)/N and
sum_(k>N)kappa_k=alpha_(N+1). Thus the complete infinite tail is
finite on every restriction. The tail is part of the source, not an
error that permits deleting its entries under extension.

## 3. Literal capacity is financed by the same full defect

For a permanent nonnegative source its historical maximum over old banks
equals the sum of its original unordered pairs whose output is still
unused at their later source birth. Consequently its literal capacity
C_N is at most half its full matrix mass on Fhat_N. This bound includes
never-used outputs and outputs first appearing beyond N.

Equations (4)--(6) therefore prove

```
M_N(Theta)
 <=Gcal_N(lambda,u)/[4(1+lambda)]+D_3/6+1/18,

(1+lambda)C_N(Theta)
 <=Gcal_N(lambda,u)/8
       +(1+lambda)[zeta(2)/6+7/144].                 (7)
```

For the first line, the finite component sum
sum_(k<=N)kappa_k Gcum_k/H_k^2 is at most Gcal_N: its omitted
k>N terms are nonnegative and the exact terminal value is Gcum_N.
No source clock was substituted for a retirement clock in (7).
The old full-stage G remains at its exact output stage through this
layer identity.

In particular, with the original source Psi_lambda unchanged, the new
single source

```
Omega_lambda=Psi_lambda+(1+lambda)Theta              (8)
```

is PSD and entrywise nonnegative, and has the actual eligible budget

```
Elig_N(Omega_lambda)
 <=(1+lambda)Ycal_N(u)/8
       +(1+lambda)[zeta(2)/6+7/144].                 (9)
```

This follows from the exact old identity
Elig_N(Psi_lambda)=(1+lambda)Ycal_N(u)/8-Gcal_N/8
and Elig_N(Theta)<=C_N(Theta). The source in (8) genuinely has both
sets of additive entries. Assigning a fraction of one component's entry
to a row does not grant another copy of that component to a later row.

## 4. One nearby block and its exact tensor payment

For comparison with the longer allocation, fix k>=n>=2 and a nonempty
actual block B strictly after old rank n. Put m=|B|, and let L be its physical span
plus one. The component's unnormalized tensor shadow is

```
q(x,s)=sum_(d in Fhat_n)R_k(s+d)1_B(x-d).
```

It vanishes for x in B by actual Sidon difference uniqueness. Its total
mass is mQ_n sum_s R_k(s), and its squared energy has exact diagonal
term mQ_n L_k. Its supporting rectangle has at most
(L+2H_n-m)(3H_k+2H_n+1) integer sites. Therefore that same component
pays at least the positive part of

```
J_(k;n,B)
 =1/(2Q_k^2H_k^2) {
    m^2Q_n^2 (sum_s R_k(s))^2
      /[(L+2H_n-m)(3H_k+2H_n+1)]
    -mQ_n L_k }.                                    (10)
```

The coefficient kappa_k is applied afterwards. This is a tensor Gram
calculation. It is not a convolution by a Fourier multiplier, nor an
entrywise comparison obtained from PSD ordering.

For k in a good component window [N,2N), one has
sum_s R_k(s)>=Ptot_N/H_k, where Ptot_N=sum_s P_N^top(s).
The known good bound Ptot_N>=beta N^3H_N^2 gives an elementary
nearby-half-block lower bound of order 1/log(2N)^2 after summing the
window coefficients, with a summable O(1/N) trace loss. The known
divergent sum of 1/log(2N) over good windows alone does not make this
weaker local lower bound nonsummable. A different allocation is needed.

## 5. A single component can be spent across a longer physical horizon

The following argument uses only the actual future points and the
component's mass, trace, and fixed source radius. Translate a_1 to zero.
Fix k and set D=H_k. For positive integers j let

```
B_j=P_infinity intersect (a_k+(j-1)D, a_k+jD],
m_j=|B_j|,          F_j=sum_(h<=j)m_h.
```

Every B_j is strictly after k and has span plus one at most D. The
blocks have disjoint point sets, hence disjoint positive difference sets
by actual Sidon uniqueness. Use the SAME bank Fhat_k and the SAME
component A_k on every one of them. The elementary mass projection of
each feature gives the genuine pair demand

```
J_j=1/2[m_j^2 M_k/(3D)-m_j T_k].                    (11)
```

For empty blocks this is zero; negative values, including any singleton
case, may be discarded. Thus their summed positive demands are at least
M_k sum_j m_j^2/(6D)-T_k sum_j m_j/2. All their payments together
use each eligible pair entry of A_k at most once.

Assume one fixed onset and C>0 with H_n<=C n^2 log(2n) thereafter.
If A(X)=#{i:H_i<=X}, its next endpoint and the cap imply

```
A(X)>=sqrt(X/[C log(2X+4)])-1
```

once that next rank is beyond the onset. Indeed A(X)+1<=X+2 by
integer spacing and H_(A(X)+1)>X. Applied at X=(j+1)D, this gives

```
F_j>=sqrt(jD/[C log(4jD+4)])-k-1.                   (12)
```

A short Hardy calculation converts these simultaneous cumulative bounds
into a lower bound on the one actual occupancy sequence. If f(x)=m_j
on (j-1,j] and F(x)=integral_0^x f, integration by parts gives

```
integral_0^J [F(x)/x]^2 dx
 <=2 integral_0^J F(x)f(x)/x dx
 <=2 sqrt(integral_0^J [F(x)/x]^2 dx)
       sqrt(sum_(j<=J)m_j^2).
```

The nonpositive terminal term was omitted, and F(x)^2/x tends to zero
at zero. Since F(x)>=F_j on [j,j+1], it follows that

```
sum_(j<=J)m_j^2 >=1/4 sum_(j<J)F_j^2/(j+1)^2.       (13)
```

No separately selected shell or independent budget enters (13).

Take J=floor(k^(3/2)), and retain the terms with
ceil(k^(1/2))<=j<J. Integer Sidon packing and the one cap give

```
k(k-1)/2<=D<=C k^2 log(2k).
```

Uniformly on these j, the square root in (12) dominates k+1.
For sufficiently large k it follows from (12)--(13) that

```
sum_(j<=J)m_j^2
 >=D/(16C) sum_(ceil(k^(1/2))<=j<J)
          j/[(j+1)^2 log(4jD+4)]
 =D/(16C)[log(7/5)+o(1)].                           (14)
```

The last equality is elementary integral comparison:
log D=2log k+O_C(log log k), and the ratio of the logarithms at
the two endpoints tends to (2+3/2)/(2+1/2)=7/5.

The terminal point count has the unconditional Sidon bound
A(X)<=sqrt(2X)+1. Hence

```
sum_(j<=J)m_j=O_C(k^(7/4)sqrt(log k)).
```

Consequently, on any sequence of components satisfying
T_k/M_k=O(log k/k^2), their entire diagonal expenditure in (11)
is o(M_k). Equations (11)--(14) prove, eventually along that sequence,

```
sum_(j<=floor(k^(3/2))) J_j^+
 >=[log(7/5)/(192C)] M_k.                            (15)
```

This is a positive fraction of the one fixed component mass, not a new
unit allowance per interval. The points needed lie at coordinate at most
(J+1)H_k and at rank O_C(k^(7/4)sqrt(log k)); thus every allocation
above is finite and has an explicit finite terminal horizon.

## 6. The triple source meets that trace-to-mass condition and is productive

For a nonnegative sequence R_k, its translates over Fhat_k have total
mass Q_k sum_s R_k(s), supported on at most 5H_k+1 integer sites.
Cauchy therefore gives the actual component mass lower bound

```
M_k>= (sum_s R_k(s))^2/[H_k^2(5H_k+1)].
```

Fix a good dyadic N with
H_N<=K H_(N/2), H_(N/2)>=2H_(N/4), H_(2N)<=K H_N,
where K=32 and beta=1/(256K^2). For every N<=k<2N,
Ptot_k>=Ptot_N>=beta N^3H_N^2 and
R_k(s)>=P_k^top(s)/H_k. Hence

```
M_k>=beta^2 N^6/(6K^5 H_N),
T_k<=4N^2/9,
T_k/M_k=O_(C,K,beta)(log N/N^2).                    (16)
```

The constants are uniform within all sufficiently late good windows.
The fixed-component allocation (15) therefore applies to every component
in these windows. Their actual weighted masses satisfy

```
sum_(N<=k<2N)kappa_k M_k
 >=5 beta^2/[32 K^5 C log(2N)].                     (17)
```

Here sum_(N<=k<2N)kappa_k>=15/(16Q_N^2) and
N^6/Q_N^2>=N^2. Combining (15) and (17) yields a permitted demand
from this good component window of at least

```
5 beta^2 log(7/5)/[6144 K^5 C^2 log(2N)].            (18)
```

The good-window reciprocal-log sum diverges, and different good windows
have disjoint component index sets. Within each component, its cells
spend each entry at most once. Across components, every spent coefficient
is a distinct summand of the single matrix Theta in (2), even when the
underlying physical labels coincide. Thus (18) proves nonsummable actual
future demands against ONE Theta. At any finite horizon only rows whose
actual endpoints lie inside it are retained. Taking the horizon to
infinity eventually includes every row of every fixed finite component
window; nonnegative demand sums then diverge.

## 7. What is improved, and the exact remaining budget issue

Let D_Theta,N be any finite sum of the positive demands just constructed,
using only blocks within P_N. They are genuine allocations of Theta,
so D_Theta,N<=Elig_N(Theta). If D_old,N is a permitted component
allocation of the original Psi_lambda, their additive demand is feasible
for Omega_lambda. Equation (9) gives the finite one-budget inequality

```
D_old,N+(1+lambda)D_Theta,N
 <=Elig_N(Omega_lambda)
 <=(1+lambda)Ycal_N(u)/8
       +(1+lambda)[zeta(2)/6+7/144].                 (19)
```

The original coefficients, source clocks, and output-clock prices have
not been changed. The full defect pays a new, bounded-trace physical
source, and a long-horizon allocation makes that source productive at
the nonsummable scale. A nearby-block lower bound alone missed this.

Nevertheless defect financing is an UPPER cost bound. It is not an
identity equating the new payments to all of Gcal/8. In fact for the
additive allocations above the smaller residual decomposes exactly as

```
Elig_N(Omega_lambda)-[D_old,N+(1+lambda)D_Theta,N]
 =[Elig_N(Psi_lambda)-D_old,N]
    +(1+lambda)[Elig_N(Theta)-D_Theta,N].             (20)
```

Both terms are nonnegative. Thus merely appending these additive rows
cannot prove that a previously uncontrolled smaller residual is bounded.
A further joint allocation or a recursive inequality must quantitatively
control an actual residual, rather than count the divergent paid amount
as a negative term twice.

The longer-horizon argument also quantifies its own limitation. With
j between k^epsilon and k^(2-epsilon), its logarithmic factor is
log[(4-epsilon)/(2+epsilon)], approaching log 2 as epsilon tends to
zero. The trace-to-mass estimate here only justifies that finite range
of physical exponents. It does not license infinitely many independent
log-2 allowances for the same source, nor supply a fraction uniform in
the arbitrary cap constant C. Equation (19) is a new productive source
and a valid defect-financed inequality; equation (20) records why it is
not yet original-Q1 closure.

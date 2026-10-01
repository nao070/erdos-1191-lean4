# Signed source-clock transport and its terminal-unused capacity

2026-09-05. Author: /root/causal_telescoping, GPT-6 Astra Ultra.

**Status.** Exact collision and global formulas identify the difference
between source-priced and output-priced retirement. A new absolute
summability theorem removes rank lags at most b/(log b)^gamma for
every gamma>1/2: unconditionally for the compatible layer price, and
under one fixed cap for the direct linear price. The remaining net
commutator is charged exactly to a terminal-unused part of the same
physical source budget, disjoint from actual demands through that
horizon. Neither a uniform upper bound for the full commutator nor a closing
physical-margin estimate is proved. Original Q1 is unresolved.

Sources read in full:

- signed_multiset_born_retirement.md, SHA256
  324a0eb718acc0f7b5830bbd6723546e9963b457df7dc26256e5b0a1e85e8487;
- signed_retirement_fibers.md, SHA256
  af256edc1cd1812a9069823b906f89328de6fb85aec6e087a7ff6a4a851cc8c9.

The positive-star incidence proof in clock_core_localization.md was
also read; the all-signed extension needed below is proved here.
No numerical experiment, checker rerun, Lean edit, status mutation,
or new formal verification is used. Other source notes are preserved.

## 1. Prices, clocks, and the different positive parts

Fix an actual increasing integer Sidon history, including repeated
two-sum uniqueness. Let

~~~
F_n=Delta P_n, Fhat_n=F_n union(-F_n),
Q_n=n(n-1),   H_n=a_n-a_1,       g(d)=d.
~~~

Signed labels exclude zero and have their actual endpoint birth.
For a retired unordered signed source pair e={d,e'}, write

~~~
b(e)=max(tau(d),tau(e')),  r(e)=tau(|d-e'|)>b(e),
p(e)=d e'.
~~~

Both equal and unequal source births are allowed. For any
nonnegative nonincreasing sequence c_b define, at a finite horizon T,

~~~
R_T^src(c)=sum_(retired, r<=T)c_b p(e),
R_T^out(c)=sum_(retired, r<=T)c_r p(e),
J_T(c)=R_T^src(c)-R_T^out(c)
      =sum_(retired,r<=T)(c_b-c_r)p(e).             (1)
~~~

The net positive part [J_T(c)]_+ is different from the sum of
positive record contributions

~~~
J_T^pos(c)=sum_(retired,r<=T)(c_b-c_r)[p(e)]_+.
~~~

The near-clock theorem below bounds the total variation
sum (c_b-c_r)|p(e)| on its specified subset. The terminal-unused
identity later charges the net quantity, not J_T^pos.

The quantitative prices of interest are

~~~
alpha_b=Q_b^-2,   w_b=alpha_b/H_b^2,
kappa_b=alpha_b-alpha_(b+1),
u_b=sum_(k>=b)kappa_k/H_k^2.                       (2)
~~~

The u source is fixed from one complete history; it is not an
online prefix-only rule. Both prices are decreasing and satisfy
0<=c_b<=w_b. Statements for u do not reselect its tail at T.
The finite identities remain valid for other decreasing c, with
their own diagonal and background costs.

## 2. Each multiset collision has at most two source prices

Use a distinct disjoint pair of equal-sum triple multisets

~~~
U={u,v,m},       V={x,y,n},       sum U=sum V=s,
~~~

where the newest point value n occurs once. In polynomials n
denotes that point value; its rank is r. Write
A=aut(U)aut(V), retaining multiplicities as in the reviewed
multiset theorem.

For each of the three slots m in U, let u,v be the other slots.
The four formal retired records with output n-m have raw total

~~~
rho_m^formal
 =2[(u-x)(y-v)+(u-y)(x-v)]
 =2[(u+v)(x+y)-2uv-2xy].                         (3)
~~~

All four have later source clock

~~~
b_m=rank(max(U with this slot m removed, V with n removed)).
~~~

Division of their formal matching sum by A gives the actual sum,
including doubled numeric labels and repeated physical endpoints.
Since every output clock is r,

~~~
J_(U,V)(c)
 =(1/A)sum_(m slots in U)(c_(b_m)-c_r)rho_m^formal. (4)
~~~

The source clock is not the clock of an individual source label.
The two source labels in a record may have different births.

Let ell be the largest endpoint remaining after n is removed and
k=rank(ell). If ell belongs to V, or occurs at least twice in U,
removing one U-slot never removes every copy of ell: all b_m=k.
Otherwise ell occurs exactly once in U. Only its slot is exceptional;
write

~~~
k'=rank(max(U without ell, V without n)),  k'<k,
rho_ell=rho_ell^formal/A.
~~~

In this exceptional case, and with the second term omitted otherwise,

~~~
R_(U,V)^src(c)=c_k R(U,V)+(c_(k')-c_k)rho_ell,
J_(U,V)(c)=(c_k-c_r)R(U,V)+(c_(k')-c_k)rho_ell.   (5)
~~~

This is an exact reduction to two actual prices. Neither R(U,V)
nor rho_ell has been assigned a sign.

The parent independently derived this two-price reduction and the
following useful exact deficit. With mu=s/3 and c_0=n-mu,

~~~
G(U,V):=2B(U,V)-R(U,V)
 =[6sigma_U^2+12(n-x)(n-y)]/A>=0.                 (6)
~~~

Indeed the other centered V-slots X,Y satisfy X+Y=-c_0, and
6c_0^2-sigma_V^2=2(c_0-X)(c_0-Y).
Thus the exact source-priced excess for this collision is

~~~
R_(U,V)^src(c)-2c_r B(U,V)
 =J_(U,V)(c)-c_r G(U,V).                         (7)
~~~

The repeated-endpoint stabilizer in (3)-(7) is essential. A
retirement-free group contributes only nonnegative Born mass,
and hence a nonpositive remainder to a full excess of the form (7).

The earlier actual six-point example remains relevant:
P={0,13,29,35,37,40} has one six-distinct collision with
R=4008, B=3500, common source clock 5 and output clock 6. For
the nonnegative prices alpha_j=Q_j^-2,

~~~
alpha_5 R-2alpha_6 B=1009/450>0.                  (8)
~~~

No new execution is used here. Equation (8) rules out the naive
clock transfer for those prices, not a cap-sensitive bounded error
on one infinite history. The results below are not repetitions of
that finite observation.

## 3. Exact all-signed incidence at a fixed pair of clocks

Let I_(b,r) count all retired signed records with later source birth
b and output birth r>b. Then

~~~
I_(b,r)<=(b-1)(4b-7)<=4(b-1)^2.                   (9)
~~~

Here is a proof retaining same-birth opposite sources.

For a positive product, both sources have the same sign. Their
magnitudes cannot have the same birth: the difference of two
positive labels in G_b belongs to F_(b-1) and cannot retire.
Orient by the newer magnitude d=a_b-a_i and older magnitude e.
For output t=a_r-a_j, the case d-e=t gives a unique nonzero
difference a_j-a_i=a_r-a_b+e. The case e-d=t gives the
two-sum equation a_i+a_j=a_b+a_r-e, with at most two
ordered solutions. For each old e there are therefore at most
three positive-source records. The negative reflection doubles
this to at most 6q_(b-1) signed records.

For a negative product, write the source magnitudes as d,e>0
with d+e=a_r-a_j. If d=a_b-a_i is new, then

~~~
a_j-a_i=a_r-a_b-e.
~~~

The right side is nonzero: a_r-a_b belongs to G_r, while
e belongs to F_b, so they are different actual labels.
Nonzero-difference uniqueness gives at most one solution for each e.
An old e yields at most two signed records, namely {-d,e} and
{-e,d}; these are distinct because the births differ. This costs
at most 2q_(b-1).

When both magnitudes are new, their signed pairs correspond exactly
to ordered positive magnitude pairs. Fixing the second magnitude
gives at most one first magnitude by the same equation, so there
are at most b-1 such records. The repeated-magnitude pair {-d,d}
is counted once; unequal magnitudes give both ordered choices.

Adding the counts gives
6q_(b-1)+2q_(b-1)+(b-1)=(b-1)(4b-7).
This establishes (9), rather than importing a same-birth exclusion
from the positive source bank.

## 4. Compatible-price commutators at near clocks are summable

Fix gamma>1/2. For b>=3 let

~~~
L_b=floor[b/(log b)^gamma].
~~~

Since log b>1, L_b<=b. The near set consists of
0<r-b<=L_b. For the price u,

~~~
H_b^2(u_b-u_r)
 =sum_(k=b..r-1)kappa_k H_b^2/H_k^2
 <=alpha_b-alpha_r.                              (10)
~~~

For r=b+h the elementary derivative bound for
alpha(x)=1/[x^2(x-1)^2] gives

~~~
alpha_b-alpha_(b+h)<=4h alpha_b/(b-1).            (11)
~~~

Multiplying (10)-(11) by the incidence bound (9), and summing
h=1,...,L_b, proves the absolute per-b estimate

~~~
sum_(retired at b, 0<r-b<=L_b)(u_b-u_r)|de|
 <=8L_b(L_b+1)/[b^2(b-1)]
 <=12/[b(log b)^(2gamma)]
       +12/[b^2(log b)^gamma].                  (12)
~~~

The factor (r-b)/b in the price difference is what improves
the summability threshold from the unweighted incidence cutoff.
Both series in (12) converge for gamma>1/2.
Thus, including the finite b=2 part,

~~~
sum_(all near-clock retirements)(u_b-u_r)|de|<infinity. (13)
~~~

This is uniform over terminal horizons and requires no cap.
It bounds the total variation, including opposite-sign and
same-birth sources; it is stronger than a bound on a signed sum.

## 5. The direct price has the same threshold under one fixed cap

For c=w, separate the price change exactly:

~~~
H_b^2(w_b-w_r)
 =(alpha_b-alpha_r)+alpha_r[1-H_b^2/H_r^2].
~~~

Because 1-exp(-2x)<=2x for x>=0 and alpha_r<=alpha_b,

~~~
(w_b-w_r)|de|
 <=alpha_b-alpha_r+2alpha_b log(H_r/H_b).        (14)
~~~

The first term is bounded by (12). For the second term, (9)
gives at each b

~~~
radius_cost_b<=8/b^2 sum_(h=1..L_b)log(H_(b+h)/H_b). (15)
~~~

There is no assumption of a small diameter ratio for every
individual near pair of clocks. Its changes are summed instead.

For a dyadic N=2^j with j>=2, use b in [N,2N). Then
L_b<=L_*:=floor[2N/(log N)^gamma]<=2N. Write
eta_l=log(H_(l+1)/H_l)>=0 and expand each logarithm in (15).
For a fixed l, at most L_* values of b can satisfy
b<=l<b+L_b. For each such b at most L_* of the h terms
cross that increment. Also b^-2<=N^-2 and every contributing
increment lies between N and 4N. Consequently

~~~
sum_(b=N..2N-1)radius_cost_b
 <=8L_*^2/N^2 sum_(l=N..4N-1)eta_l
 <=32 log(H_(4N)/H_N)/(log N)^(2gamma).           (16)
~~~

The integer count uses b in (l-L_*,l], which contains at most
L_* integers. Thus no omitted rounding factor is needed.

Now assume one infinite actual history and fixed C_cap>0,n_0
such that H_n<=C_cap n^2 log(2n) for every n>=n_0.
Sidon uniqueness always gives H_N>=Q_N/2>=N^2/4.
For all dyadic N beyond the one onset,

~~~
H_(4N)/H_N<=64 C_cap log(8N)
             =64 C_cap(j+3)log 2.                (17)
~~~

After the finite initial ranks, the total radius cost is bounded by

~~~
32 sum_(j>=j_0)
   log(max(1,64 C_cap(j+3)log 2))/(j log 2)^(2gamma)
 <infinity.                                     (18)
~~~

The summand is O(log(j+2)/j^(2gamma)). This is where the
single eventual cap enters; there is no replacement by unrelated
terminal caps. The finite initial ranks contribute finitely many
source records, uniformly in T. Combining (12),(15)-(18) proves

~~~
sum_(all near-clock retirements)(w_b-w_r)|de|<infinity,
                         gamma>1/2.             (19)
~~~

Thus for either c=w or c=u there is a constant K_gamma,
with the stated cap dependence for w, such that
|J_T(c)-J_T^far(c)|<=K_gamma for all T, where the far sum
keeps r-b>L_b. No summable bound for that remaining sum is
asserted. This removal may split a collision; only the commutator
is removed in absolute value. The full geometric deficit (6)
is retained when comparing Born with retirement.

## 6. Global reindexing over labels not yet used

Let k_n(t) be the raw correlation of g(d)=d on Fhat_n at
positive output t. Define

~~~
L_(n,T)=sum_(t in F_T \ F_n)k_n(t).
~~~

A retired pair contributes to L_(n,T) exactly for b<=n<r.
Since c_b-c_r=sum_(n=b..r-1)(c_n-c_(n+1)), exact finite
reindexing gives

~~~
J_T(c)=sum_(n=2..T-1)(c_n-c_(n+1))L_(n,T).       (20)
~~~

This is integration over the actual interval between its two
clocks, not an independent physical copy at each intermediate n.

Write Z_n=sum_(d in Fhat_n)d^2 and
E_n=||1_(P_n)*g_(Fhat_n)||_2^2. The total raw off-diagonal
source product is -Z_n/2. The used output sum is
(E_n-nZ_n)/2. Therefore

~~~
sum_(t>0,t notin F_n)k_n(t)=[(n-1)Z_n-E_n]/2,

L_(n,T)=[(n-1)Z_n-E_n]/2
                   -sum_(t>0,t notin F_T)k_n(t). (21)
~~~

The second term is indispensable. It refers to outputs not yet
used by horizon T, not outputs known never to appear in the
infinite history. A subcollection of future-used outputs does not
inherit the sign of the full current-unused correlation.

There is a compact version using the fixed source itself.
Set U^c_de=c_maxbirth de on Fhat_T, and let

~~~
s_T(c)=tr U^c,
p_T(c)=sum_(t>0,t notin F_T)K_(U^c)(t),
B_T(c)=sum_(Born, b<=T)c_b de.
~~~

Every signed class is centered, so U^c has zero matrix mass.
Partitioning its off-diagonal entries into Born, retired and
terminal-unused pairs gives

~~~
p_T(c)=-s_T(c)/2-B_T(c)-R_T^src(c).              (22)
~~~

Use the fresh full-signed diagonal
Dhat_n=Z_(n-1)+n(Z_n-Z_(n-1)), and define

~~~
D_T(c)=sum_(n=2..T)c_n Dhat_n,
A_T(c)=c_T E_T+sum_(n=2..T-1)(c_n-c_(n+1))E_n
      =D_T(c)+2B_T(c)+2R_T^out(c).
~~~

Combining with (22) proves the exact terminal-unused identity

~~~
J_T(c)+p_T(c)=[D_T(c)-s_T(c)-A_T(c)]/2.          (23)
~~~

For c=w or u, the already directly derived signed diagonal obeys
0<=D_T(c)<=2zeta(2)-1, since c_n<=w_n and Dhat_n>=0.
Also s_T(c)>=0 and A_T(c)>=0. No positive-bank diagonal is used.

## 7. An unused part of one physical budget pays the net transport

For c=w or u choose the same fixed background and carrier

~~~
V_de=alpha_maxbirth,    W=V+lambda U^c,
                         0<lambda<=1.
~~~

The decreasing nonnegative price sequences give PSD by the nested
prefix decomposition. The bound c_b H_b^2<=alpha_b separately
gives entrywise nonnegativity of W.
Use the current terminal capacity

~~~
C_cur,T(A)=sum_(t>0,t notin F_T)K_(A|Fhat_T)(t).
~~~

This is a linear functional of a fixed matrix with a fixed mask.
It is not a historical maximum. Equation (23) becomes

~~~
J_T(c)+A_T(c)/2
 =[D_T(c)-s_T(c)]/2
       +[C_cur,T(V)-C_cur,T(W)]/lambda.          (24)
~~~

In particular

~~~
[J_T(c)+A_T(c)/2]_+
 <=C_cur,T(V)/lambda+[2zeta(2)-1]/2.             (25)
~~~

It also bounds [J_T(c)]_+, since A_T(c)>=0.
One may take lambda=1 for the strongest coefficient.
This charges the net positive transport to actual terminal-unused
baseline capacity, plus a bounded diagonal, rather than postulating
summability of all individual positive products.

To check that this charge does not duplicate the actual demands,
split the literal historical capacity of any fixed nonnegative
matrix A by its physical outputs:

~~~
C_hist,T(A)=C_ret,T(A)+C_cur,T(A),

C_ret,T(A)=sum_(t in F_T)
                   max_(n<=T)1[t notin F_n]K_(A|Fhat_n)(t).
                                                               (26)
~~~

For t notin F_T the kernel is increasing throughout the history
and reaches its maximum at T, proving the split. Every actual
future block lying in P_T has Delta B contained in F_T. If its
old source restriction is from a prefix preceding that block,
its demand uses only the retired-output part in (26). Pairwise
disjoint block difference sets, with literal fixed-source kernels
or dominated subsources, are therefore paid by C_ret,T(A).

The capacity on the right of (25) lives on the complementary
physical labels and has not been spent on those blocks. It may
become usable by blocks after T; no permanence beyond that horizon
is asserted. This exact separation is unavailable if one silently
substitutes independently normalized rows for the fixed source.

There is also a coarser recordwise check: (c_b-c_r)|de|<=alpha_b,
so the total commutator variation is at most C_hist,T(V).
For positive products, W_de>=(1+lambda)c_b de, hence

~~~
J_T^pos(c)<=C_hist,T(W)/(1+lambda).               (27)
~~~

These latter bounds do not make that capacity available a second
time for demands. They do not imply a bounded global commutator.
In contrast, (24)-(26) explicitly identify a currently unspent
physical part, but only for the net commutator.

## 8. The remaining global estimate is now narrower

The exact multiset theorem gives R_T^out(c)<=2B_T(c).
Write its nonnegative deficit as

~~~
G_T(c)=2B_T(c)-R_T^out(c)
      =sum_(active collisions through T)c_r G(U,V)
          +2 sum_(Born-only groups through T)c_b B_group.
~~~

Consequently

~~~
R_T^src(c)-2B_T(c)=J_T(c)-G_T(c).                (28)
~~~

Near commutator records may be removed at the finite cost
(13) or (19), but the full deficit in (28) must be kept.
Equations (4)-(7) then leave a concrete far-clock expression
with at most two source prices per collision, and the explicit
variance/top-gap deficit. Bounding that remaining excess by O(1)
on the same capped history would prove a source-priced comparison
with finite error. Such an estimate is not supplied here.

Alternatively, a uniform upper bound on the net commutator would follow
from the narrower current-tail estimate

~~~
C_cur,T(V)-C_cur,T(W)<=lambda A_T(c)/2+O(1).     (29)
~~~

The equivalence up to bounded diagonal terms follows directly from
(24). The trace s_T(c) is bounded for these two prices. For the
weaker goal R_T^src(c)<=2B_T(c)+O(1), (22) gives the exact
condition

~~~
-p_T(c)<=3B_T(c)+s_T(c)/2+O(1).                 (30)
~~~

Thus the unresolved transport can be placed entirely on the actual
terminal-unused output set, or on the explicit collision deficit.
Neither set of formulas proves (29) or (30). In particular a
divergent Born saving does not by itself control this leftover
capacity, and no cap-sensitive summability of the full far
commutator has been established.

The concrete new conclusions are the all-signed incidence bound,
the gamma>1/2 absolute near-transport theorem, the two-price
multiset reduction, and the exact unused-capacity charge. They
retain all source/output clocks, doubled labels, and one physical
budget. They do not complete original Q1.

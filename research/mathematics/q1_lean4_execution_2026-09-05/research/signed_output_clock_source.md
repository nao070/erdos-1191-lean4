# A fixed output-clock source and its financed future demands

2026-09-05. Author: /root/linear_causal_sign, GPT-6 Astra Ultra.

**Status.** The full absolute retired sum at output stage j is at most
twice the raw Born sum at source stage j, including repeated endpoints.
This strengthens the earlier signed comparison. A fixed complete-history
Gram source realizes that output price, is PSD and entrywise nonnegative,
has bounded trace, and has its historical capacity financed by the Born
saving of the existing compatible source. Actual half-sized future
blocks receive an additional nonsummable demand under the existing good
epochs and one fixed cap. The outstanding baseline capacity-minus-demand
upper bound is stated explicitly. This does not settle original Q1.

The parent proposed the output mask and the sharp absolute inequality;
the derivations below independently check both and supply the full
finite-restriction and physical-payment accounting. No numerical test,
Lean execution, or new formal verification is used.

Dependencies read in their current form:

- `signed_multiset_born_retirement.md`, SHA256
  `324a0eb718acc0f7b5830bbd6723546e9963b457df7dc26256e5b0a1e85e8487`;
- `signed_causal_source.md`, SHA256
  `8806a3f6f5f5cc7964a43d34b64c014c1fddcc09182ab6db65a31da2e11d772d`;
- the explicit good-shape estimates in `signed_radius_localization.md`
  and `signed_born_quantitative_gain.md`.

## 1. Absolute retirement, with the same exact orbit normalization

Use the actual signed-bank conventions of the multiset note. An unordered
pair of distinct sources has later source birth b and positive output
birth r. It is Born for r<=b and retired for b<r. Define

```
B_j = sum of de over Born pairs of source clock j,
Rabs_j = sum of |de| over retired pairs of output clock j.
```

Fix an active collision of disjoint equal-sum triple multisets U,V, with
newest endpoint n occurring exactly once in V={x,y,n}. Repeated slots
are retained. Write A=aut(U)aut(V), s=sum U=sum V and c=n-s/3. Put

```
delta_i=n-u_i>0,       S=sum_i delta_i=3c,
a=n-x>0,              b=n-y>0,          a+b=S,
g_ij=(a-delta_i)(b-delta_j),             i!=j.          (1)
```

Here a,b are endpoint distances, not rank clocks. Across the six labeled
matchings, each ordered assignment of the two old edges gives two
formal retired records of raw contribution -g_ij. Therefore

```
Rabs(U,V)=(2/A) sum_(i!=j)|g_ij|,
B(U,V)=(4/A) sum_i delta_i^2.                          (2)
```

The normalization in (2) is exact even for doubled Schur labels. A
physical matching pattern occurs A times if its three edges are distinct,
and A/2 times if an edge occurs twice. In the latter case the formal
six-entry Schur list counts each actual pair twice. Taking absolute
values preserves this duplication, its clock, and its cancellation
against A/2. There is no exceptional repeated-endpoint error.

For i!=j let k be the third slot. Both factors in g_ij cannot be
negative, since delta_i+delta_j<S=a+b. If g_ij>0, set
p=delta_i<=a and q=delta_j<=b. The denominator-free identity

```
ab(S-p-q)-S(a-p)(b-q)
 =a^2 q+b^2 p-S p q
 =a q(a-p)+b p(b-q)>=0
```

gives (g_ij)_+<=ab delta_k/S. The same inequality is automatic if
g_ij<=0. Each third slot occurs twice among the six ordered pairs,
so sum g_+<=2ab. Direct expansion also gives

```
sum_(i!=j)g_ij=6ab-S^2-sum_i delta_i^2.
```

Combining these facts proves the sharper estimate

```
Rabs(U,V)
 <= 2[S^2+sum_i delta_i^2-2ab]/A
 = 2B(U,V)-[6 sigma_U^2+4ab]/A
 <= 2B(U,V),                                           (3)
```

where sigma_U^2=sum_i(u_i-s/3)^2=sum_i delta_i^2-S^2/3.
In particular the correction displayed in (3) is positive for an actual
active collision. Nevertheless the per-collision coefficient 2 is sharp:
the already checked families with R/B tending to 2 also have
Rabs>=R, while (3) supplies the opposite asymptotic bound. This does
not assert sharpness after all other groups at a stage are added.

All retired groups lie in these active collisions. The remaining complete
Schur groups have no retired record and have nonnegative raw Born total.
Consequently, at every actual stage, and for any nonnegative stage prices,

```
Rabs_j<=2B_j,
sum_(j<=N) omega_j Rabs_j <=2 sum_(j<=N) omega_j B_j.    (4)
```

The left price is the OUTPUT price; the right is the SOURCE price.
No claim replaces a retired source price by its output price.

## 2. A positive Gram mask with the actual output clock

Fix one complete increasing integer Sidon history. For k>=2 put

```
Fhat_k=(Delta P_k) union(-(Delta P_k)),
Q_k=k(k-1), H_k=a_k-a_1, alpha_k=Q_k^-2,
kappa_k=alpha_k-alpha_(k+1)>0,
u_b=sum_(k>=b) kappa_k/H_k^2,  w_b=alpha_b/H_b^2.
```

Thus 0<u_b<=w_b and u is decreasing. It is fixed from the complete
history and generally cannot be determined online from P_b alone.
All infinite matrices below mean compatible finite restrictions.

The autocorrelation of the actual point indicator is

```
m_k(t)=sum_z 1_(P_k)(z)1_(P_k)(z+t)
      =k 1[t=0]+1[t in Fhat_k].
```

The second equality is exactly Sidon difference uniqueness. Hence
K_k(d,e)=m_k(d-e), for d,e in Fhat_k, is the Gram matrix of translated
point indicators. It is PSD and entrywise nonnegative. Define, for
0<=lambda<=1, the fixed source

```
Psi_lambda
 =sum_(k>=2) kappa_k/H_k^2
       K_k circ (abs(d)_k abs(d)_k^T+lambda d_k d_k^T). (5)
```

Here vectors and matrices are zero outside Fhat_k and circ is the
entrywise product. Each summand is PSD by the Gram tensor product and
is entrywise nonnegative, since |de|+lambda de>=0. For a finite bank N,
every component is restricted to Fhat_min(k,N); its tail is not replaced
by a new terminal normalization.

For distinct sources let b be their later birth, t=|d-e|, and r=tau(t)
in the COMPLETE history; set r=infinity if t never appears. Summing the
actual components gives exactly

```
(Psi_lambda)_(d,e)
 =u_max(b,r)(|de|+lambda de),  if r<infinity,
 =0,                         if r=infinity.             (6)
```

In particular all Born and retired records in an active collision receive
the same newest-endpoint price. At the diagonal, the indispensable factor
k remains:

```
(Psi_lambda)_(d,d)
 =(1+lambda)d^2 sum_(k>=tau(d)) k kappa_k/H_k^2.         (7)
```

It is not legitimate to replace this diagonal by the offdiagonal formula.
The whole infinite diagonal is summable. With Z_k=sum_(d in Fhat_k)d^2,

```
tr Psi_lambda
 =(1+lambda)sum_(k>=2) k kappa_k Z_k/H_k^2
 <=(1+lambda)sum_(k>=2) k kappa_k Q_k
 =(1+lambda)(2 zeta(2)-1).                              (8)
```

For the last equality,
k kappa_k Q_k=4k/[(k-1)(k+1)^2]
=1/(k-1)-1/(k+1)+2/(k+1)^2. This also proves convergence of
each finite restriction. Bounded trace alone does not assert bounded
matrix mass; that cost is addressed in Section 4.

## 3. Exact capacity, including outputs beyond a finite terminal bank

For a fixed entrywise nonnegative source A define its physical pair kernel
K_n^A(t) on the signed bank Fhat_n, and its literal historical capacity by

```
C_N(A)=sum_(t>0) max_(2<=n<=N) 1[t notin Delta P_n] K_n^A(t).
```

Permanent nonnegative pair entries make each kernel increase until its
output is used. The maximum therefore equals the SINGLE pair sum over
later-source birth b<output birth r, with sources present by N. This
remains valid for the anticipatively chosen fixed source (5).

Write B_N(u)=sum_(j<=N)u_j B_j. Equation (6) gives the exact split

```
C_N(Psi_lambda)
 =sum_(j<=N)u_j(Rabs_j+lambda R_j)+Boundary_N(lambda),   (9)
```

where Boundary_N contains sources born by N with output birth r>N;
never-used outputs have zero entry. Since |de|+lambda de>=0,

```
0<=Boundary_N(lambda)
 <=(1+lambda)u_(N+1)/2 [sum_(d in Fhat_N)|d|]^2
 <=(1+lambda)/2.                                      (10)
```

The last step uses u_(N+1)<=1/(Q_(N+1)^2 H_(N+1)^2) and
sum|d|<=Q_N H_N. Thus the permanent tail beyond N has a uniform
cost; deleting it would change the source under extension.
Equations (4),(9),(10) imply

```
C_N(Psi_lambda)<=(2+2lambda)B_N(u)+(1+lambda)/2.        (11)
```

All pairs whose output has already appeared are priced at that actual
output stage. The boundary is separately priced instead of being assigned
to Born companions lying outside the finite source bank.

## 4. Full matrix mass is controlled, but need not be finite globally

Let Babs_j denote the absolute Born sum at source stage j. Retain the
endpoint distances a,b and delta_i of (1). For a labeled matching with
latest slot m and old slots i,j, its formal absolute Born total is
2 delta_m(|a-delta_i|+|b-delta_j|), regardless of the numerical
position of its latest label. Sum both old assignments for each m
and then reindex by the old slot i. The same exact orbit factor gives

```
Babs(U,V)
 =(2/A)sum_i(S-delta_i)(|a-delta_i|+|b-delta_i|)
 <=4S^2/A<=12 sum_i delta_i^2/A=3B(U,V).              (12)
```

Indeed a+b=S and 0<=delta_i<=S imply
|a-delta_i|+|b-delta_i|<=S: the three ranges cut out by a,b
give S-2delta_i, |a-b|, or 2delta_i-S. Also
sum_i(S-delta_i)=2S and S^2<=3sum_i delta_i^2.
For a Born-only distinct-label group the ratio
of absolute to raw total is
(x^2+3xy+y^2)/(x^2+xy+y^2)<=5/3; the doubled group has exactly
that ratio. Thus Babs_j<=3B_j at every stage. The parent supplied
this sharper reindexing, independently checked by this author and the
causal-telescoping agent.

Let M_N(A)=1^T A_N 1. The full Born sum of Psi_lambda is
sum_(j<=N)u_j(Babs_j+lambda B_j), so the exact mass partition and
(11),(12) yield

```
M_N(Psi_lambda)
 =tr(Psi_lambda)_N+2 Born_N(Psi_lambda)+2C_N(Psi_lambda)
 <=tr(Psi_lambda)_N+(10+6lambda)B_N(u)+(1+lambda).      (13)
```

For the existing compatible source V+U', where
V_de=alpha_maxbirth and U'_de=u_maxbirth de, the reviewed capacity
identity is

```
C_N(V)-C_N(V+U')=tr(U'_N)/2+B_N(u).
```

Its left side is at most C_N(V)<=M_N(V)/2. Since
M_N(V)=4(h_N-h_N^(2))=4 log N+O(1), equations (8),(13) give
M_N(Psi_lambda)=O(log N) with an explicit bound independent of a cap.
Under the fixed cap and good-epoch assumptions below, the previously
proved B_N(u) diverges. The lower bound
M_N(Psi_lambda)>=2(1+lambda)B_N(u) then shows that this source
does NOT have finite global mass. Its controlled historical capacity,
rather than an unsupported finite-mass claim, is used next.

## 5. What the mask does to a future energy

There is a useful obstruction to an incorrect convolution shortcut.
For any old scalar feature g, let
C_g(t)=sum_d g(d)g(d+t), and let m_B be the autocorrelation of an
actual future point block. Expanding the quadratic form gives exactly

```
E_B(K_k circ gg^T)=sum_t m_B(t)m_k(t)C_g(t).            (14)
```

This is a tensor Gram expression. It is generally NOT the energy of
the ordinary triple convolution 1_B*1_(P_k)*g. If every point of B is
in P_k, all its nonzero differences have m_k(t)=1. Therefore

```
E_B(K_k circ gg^T)=E_B(gg^T)+(k-1)|B| sum_d g(d)^2.   (15)
```

The additional diagonal is exactly canceled when passing to the actual
pair kernel by subtracting |B| tr(K_k circ gg^T). There is no extra
k-fold moment amplification. On every ACTUAL output in Delta B,
the masked and unmasked pair kernels agree.

Let B occur after old rank n, end at rank e, contain m points, and have
integer interval length L. For all k>=e the tail of (5), restricted to
old sources Fhat_n, has on Delta B the same kernel as the ordinary
nonnegative PSD source

```
T_n(lambda)=u_e[abs(d)_n abs(d)_n^T+lambda d_n d_n^T]. (16)
```

This is an equality on the actual used outputs, not a claim that (16)
is globally an entrywise or PSD subsource of Psi_lambda. The remaining
actual components are entrywise nonnegative, which is exactly the
comparison needed for payment.

Put A_n=sum_(d in Fhat_n)|d| and Z_n=sum_(d in Fhat_n)d^2. The signed
shadow lies in the integer interval of length T=L+2H_n and vanishes
at all m points of B. Write D=T-m>0. The even feature has mass A_n;
the odd feature has zero mass and first moment Z_n. Cauchy and the
centered first-moment inequality give the raw demand

```
ell_n=12m^2 Z_n^2/[T(T^2-1)],
delta_n(lambda)
 =u_e[m^2 A_n^2/D+lambda ell_n-m(1+lambda)Z_n]/2.       (17)
```

The trace subtraction is m(1+lambda)Z_n, not (m-1) times that
quantity. If Aactual_n denotes the sum of the kernel of (16) on
Delta B, then Aactual_n>=max(delta_n(lambda),0). By (15),(16) this
is paid by the real tail of Psi_lambda on those actual differences.

## 6. An exact single-budget unused-capacity identity

Choose finitely many actual blocks B_i after old ranks n_i and ending
at e_i, all lying in P_N, whose difference sets are pairwise disjoint.
Disjoint actual point blocks have this property by Sidon uniqueness.
For an unordered signed source pair h={d,e}, of later birth b and
output birth r, put

```
v_k(h)=(|de|+lambda de)/H_k^2,
p_k(h)=sum_i 1[|d-e| in Delta B_i]1[b<=n_i]1[e_i<=k].
```

Whenever p_k(h)=1, b<=n_i<r<=e_i<=k. Also p_k is either 0 or 1,
because the physical output belongs to at most one chosen block.
Expanding the fixed source into its nonnegative actual components gives

```
C_N(Psi_lambda)-sum_i delta_(n_i)(lambda)^+
 =sum_(k>=2) kappa_k
    sum_(h in Fhat_min(k,N), b<r<=k) v_k(h)[1-p_k(h)]
      +sum_i[Aactual_(n_i)-delta_(n_i)(lambda)^+].      (18)
```

Every term is nonnegative. Infinite tails converge on the finite bank.
This formula retains source births, output clocks, membership in actual
blocks, and unspent components. Reusing a component in several displayed
rows never creates a second physical budget at a label. Outputs beyond
N are included in the first sum exactly as in (10).

## 7. Half-sized blocks retain a quantitative good-epoch demand

Use good dyadic old ranks n=2p with p even, satisfying the previously
established two-lookahead conditions

```
H_p>=2H_(p/2), H_n<=K H_p, H_(2n)<=K H_n,   K=32,
H_n<=C n^2 log(2n) beyond one fixed onset.              (19)
```

The existing good-index lemma gives sum_good 1/log(2n)=infinity.
Take the ACTUAL block of points with ranks n+1 through e=3n/2.
It has m=n/2 and L<=H_(2n)<=K H_n. These blocks are disjoint
at different dyadic n. This choice leaves an interval [e,2n) of
controlled source components, without requiring a third lookahead.

Define epsilon=1/(8K), eta=1/(16K^2), and c_tail=7/(144K^2).
There are p^2/2 positive cross gaps from ranks 1,...,p/2 to ranks
p+1,...,2p, each at least H_p/2. Their actual labels are distinct.
Counting both signs proves

```
A_n>=epsilon Q_n H_n,
Z_n>=eta Q_n H_n^2.                                  (20)
```

Also Q_e/Q_n<=3 and Q_(2n)/Q_n>4. Consequently

```
u_e>=sum_(k=e..2n-1)kappa_k/H_(2n)^2
   =(alpha_e-alpha_(2n))/H_(2n)^2
   >=c_tail w_n,              u_e<=w_n.               (21)
```

Here alpha_e-alpha_(2n)>=(1/9-1/16)alpha_n. In particular the
ordinary even tail in (16) has mass between c_tail epsilon^2 and 1.
Since D<=T<=(K+2)H_n and Z_n<=Q_n H_n^2, equations (17)--(21)
give the explicit mass-only estimate

```
delta_n(0)
 >=c_tail epsilon^2/[8(K+2)C log(2n)]-1/[4(n-1)].     (22)
```

The raw demand is eventually positive and its sum over good dyadic ranks
diverges. The error has a finite dyadic sum. If lambda>0 is desired,
the additional first-moment estimate is

```
delta_n(lambda)-delta_n(0)
 >=3lambda c_tail eta^2/[2(K+2)^3 C log(2n)]
      -lambda/[4(n-1)].                              (23)
```

This too is eventually positive and nonsummable. Already lambda=0
suffices for a new demand that can be financed by historical Born saving.
These estimates concern actual blocks and the single allocation (18).

## 8. Financing the new source within the old background capacity

Let W'_(lambda0)=V+lambda0 U', 0<lambda0<=1, be the permanent
compatible source of the earlier note. Its exact saving is

```
C_N(V)-C_N(W'_(lambda0))
 =lambda0[tr(U'_N)/2+B_N(u)].                         (24)
```

Fix theta>0 with theta(2+2lambda)<=lambda0 and form ONE permanent
source S=W'_(lambda0)+theta Psi_lambda. It is PSD and entrywise
nonnegative. Historical capacity is linear for fixed nonnegative sources,
by the common pair-lifetime mask b<r. From (11),(24),

```
C_N(S)
 <=C_N(V)-lambda0 tr(U'_N)/2+theta(1+lambda)/2.        (25)
```

At lambda=0 the useful choice theta=lambda0/2 has uniform added
boundary cost lambda0/4. Its trace is bounded by the previously bounded
trace of W' plus theta times (8), and its mass is O(log N) by (13).
The construction finances a real nonnegative additional kernel; it does
not infer future payment from PSD ordering of signed differences.

At the same half-blocks let d_i^(lambda0) be the existing compatible
tail demand, namely the earlier formula with m_i=n_i/2:

```
d_i^0=[m_i^2/D_i-m_i/Q_(n_i)]/2,
d_i^(lambda0)
 =d_i^0+lambda0 u_(n_i)[ell_(n_i)-m_i Z_(n_i)]/2.      (26)
```

The ordinary even unit tail and odd tail of W' pay this actual demand.
Its positive part and theta times the positive part of (17) are paid
by the SUM of the actual kernels of S. The selected physical outputs
remain disjoint, so there is a single-budget inequality

```
sum_i (d_i^(lambda0))^+ +theta sum_i delta_(n_i)(lambda)^+
 <=C_N(S)
 <=C_N(V)-lambda0 tr(U'_N)/2+theta(1+lambda)/2.        (27)
```

All sufficiently large good half-blocks have d_i^0>0 and
d_i^(lambda0)>=d_i^0. To check the latter quantitatively, use
u_n>=gamma_* w_n, gamma_*=15/(16K^2), in the same derivation as
(23). Its improvement is at least
3lambda0 gamma_* eta^2/[2(K+2)^3 C log(2n)]
-lambda0/[4(n-1)], which is eventually positive.

Thus the extra reciprocal-log demand in (22) is compatible with the
old tail demand and is financed by the same old capacity up to a
uniform constant. The finite output boundary is already included in
(27); it is not recharged for every block.

## 9. Exact remaining scope

For the selected sufficiently late half-blocks define the old baseline
margin Mbase_N=C_N(V)-sum_i(d_i^0)^+. Rearranging (27) proves

```
Mbase_N
 >=sum_i[(d_i^(lambda0))^+-(d_i^0)^+]
    +theta sum_i delta_(n_i)(lambda)^+
    +lambda0 tr(U'_N)/2-theta(1+lambda)/2.            (28)
```

Under the fixed cap the right side diverges. This is a necessary LOWER
bound on the baseline margin. No upper bound for that margin is proved
here. The known logarithmic upper bound on total matrix mass or capacity
does not contradict the much smaller good-index divergence. Nor does
bounded trace imply bounded historical capacity.

The progress is the exact absolute stage theorem, the physical latest-clock
carrier, its uniformly bounded future-output boundary, and a financed
additional demand on actual blocks. Closing Q1 still requires a sufficiently
strong upper comparison for the same baseline margin, or a different
global argument. No scalar-price replacement, independent per-layer
capacity, extra moment amplification, or theorem closure is asserted.

# Joint uniform and signed first-moment projection on the actual shadow

2026-09-05. Author: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

**Status.** A stronger actual-demand formula, affine in the scalar–moment carrier parameters, is proved together with its exact finite allocation dual and the complete residual Gram-matrix identity. The odd signed-bank case has an additional useful consequence: at fixed physical kernel, the stronger demand optimally chooses a scalar sign using the actual future centroid. A precise sufficient condition gives a reciprocal-logarithmic increase, but its frequency and the remaining physical-margin bound are not proved. No Lean edit, numerical experiment, or optimization run is used. Original Q1 remains unresolved.

The complete current `scalar_moment_physical_cone.md` and `physical_allocation_shadow_slack.md` were read. Their source text was preserved. The argument below is independently derived from the actual finite shadows; no positive-bank causal Abel formula is imported into a signed bank.

## 1. Project both shadows onto the same two-dimensional space

For one positive-bank row, use the actual old bank F, `q=|F|>0`, its centered normalized birth-linear feature z, and its actual compatible future block B of m points. Let b be the minimum of B, L its inclusive interval length, and H the old diameter. Keep

```
J={b+1,...,b+L+H-1},    Omega=J\B,
D=|Omega|=L+H-m>=1,
f_0=1_B*1_F,           f_z=1_B*z,
M=mq,                 S=sum_d z_d^2,
mu=sum_d d*z_d.
```

Both shadows are supported on Omega. They have sums M and zero, respectively. Put

```
c_Omega=mean(Omega),    phi(x)=x-c_Omega,
V=sum_(x in Omega)phi(x)^2,
Delta0=<phi,f_0>,       Iz=<phi,f_z>=m*mu.
```

Assume first `V>0`. Define the residuals

```
u=f_0-(M/D)1_Omega-(Delta0/V)phi,
v=f_z-(Iz/V)phi.
```

Each residual is orthogonal to both `1_Omega` and phi. Thus the exact Gram decomposition is

```
E0=M^2/D+Delta0^2/V+R00,
Qcross:=<f_0,f_z>=Delta0*Iz/V+R01,
Ez=Iz^2/V+R11,
R00=||u||^2,    R01=<u,v>,    R11=||v||^2.              (1)
```

The residual matrix R is PSD: `R00,R11>=0` and `R01^2<=R00*R11`. This is one common orthogonal projection, rather than independent inequalities that discard the projected cross term.

Choose `0<ell<=1`, `t^2<=s<=ell`, and the same full matrix

```
W(t,s)=J+t(1z^T+z1^T)+szz^T.
```

Its previously verified nonnegative PSD domain and trace `q+sS` are unchanged. Equation (1) gives

```
E_W=M^2/D+(Delta0^2+2t*Delta0*Iz+s*Iz^2)/V
                         +R00+2t*R01+s*R11,
R00+2t*R01+s*R11
 =||u+t*v||^2+(s-t^2)||v||^2>=0.                       (2)
```

In particular the proposed joint energy lower bound holds. Its moment numerator is also `(Delta0+t*Iz)^2+(s-t^2)Iz^2`, so it is nonnegative throughout the carrier domain.

If `V=0`, Omega consists of one integer point. Then phi, Delta0, and Iz are zero, and the centered signed shadow is zero. Define all three moment quotients in (1)–(2) to be zero and omit the phi projection. The formulas still hold. In the actual unit-shadow setting its unique leftmost value is one, so `M=1` in this case. No division by a zero variance is used. If only `Iz=0` while V is positive, the formulas require no special division by Iz.

## 2. An affine normalized raw demand and exact dominance

Subtract the complete diagonal `m(q+sS)` from (2), then divide by `2q^2`. Define

```
delta0=[M^2/D-mq]/(2q^2),
chi=Delta0^2/(2q^2 V),
delta_bar=delta0+chi,
beta=Delta0*Iz/(q^2 V),
d=(Iz^2/V-mS)/(2q^2).
```

The stronger normalized raw demand is

```
delta_joint(t,s)=delta_bar+t*beta+s*d.                  (3)
```

All quotients have the zero-variance convention above. The term beta has no extra factor two: the energy cross term `2t*Delta0*Iz/V` is divided by `2q^2`. No factor ell is included in beta or d.

For comparison let `LB_old` be the earlier full-interval signed-moment lower bound, or the hole-aware bound `Iz^2/V`. In either case `LB_old<=Iz^2/V`. The old cone demand in the source note satisfies exactly

```
delta_joint(t,s)-delta_old(t,s)
 =[(Delta0+t*Iz)^2/V
      +(s-t^2)(Iz^2/V-LB_old)]/(2q^2) >= 0.             (4)
```

For the full-interval comparison, the inequality follows because the centered variance of Omega is no larger than the full-interval variance. At `s=t^2`, formula (3) is the actual scalar mass-plus-first-moment demand; it does not charge the same first moment a second time. At `(0,0)`, it already improves the unit baseline by chi.

These are raw demands. The full local physical kernel is nonnegative, so each positive part is payable as well, but an affine positive-part formula is not asserted. At the established sufficiently large extended good epochs, with the actual next block `m=N`, one fixed cap, and the common trace bound `q+sS<=2q`, all the old raw demands on the domain are positive. Equation (4) transfers that positivity to the new demands. The general finite identities below use raw demands; on this positive range they also describe positive-part bookkeeping.

## 3. One exact physical allocation dual

For a finite actual row family, keep the same masked normalized kernels a, l, and r as in the cone note. Both literal old exclusion and actual future-span masks are retained. The full row is `a_k+t_k*l_k+s_k*r_k`; its physical maximum and capacity are C. The new margin is

```
Margin(t,s)=C(t,s)-sum_k delta_bar_k
                         -sum_k(t_k*beta_k+s_k*d_k)>=0. (5)
```

The inequality is the actual disjoint-future-difference budget. Each demand in (5) is derived from that row's same future block, not from independently chosen moment data.

Use the column-simplex allocation polytope A and set

```
A_k(alpha)=sum_t alpha_(k,t)*l_k(t),
rho_k(alpha)=sum_t alpha_(k,t)*r_k(t),
L(alpha)=C(0,0)-sum_(k,t)alpha_(k,t)*a_k(t)>=0.
```

Retain the earlier continuous function

```
Psi_ell(a,kappa)=max_(|t|<=sqrt(ell))[-a*t-kappa*t^2],
                 kappa>=0.
```

For a fixed allocation the row expression is now

```
(A_k-beta_k)t_k+(rho_k-d_k)s_k.
```

Its minimum over `t^2<=s<=ell` is

```
ell*min(rho_k-d_k,0)
 -Psi_ell(A_k-beta_k,(rho_k-d_k)_+).                    (6)
```

Indeed a nonnegative coefficient of s selects `s=t^2`; a negative one selects `s=ell`. There is no remaining old coefficient `c*t^2` in this affine-demand problem.

Finite compact convex minimax applies: after introducing alpha the payoff is continuous and affine in both parameter pairs and allocation. Therefore, with improvement measured from the **new projected unit baseline** `Margin(0,0)`,

```
I_max=min_(alpha in A) [L(alpha)
    +ell*sum_k(d_k-rho_k(alpha))_+
    +sum_k Psi_ell(A_k(alpha)-beta_k,(rho_k(alpha)-d_k)_+)].
                                                               (7)
```

Both extrema are attained. All summands are nonnegative. Since ell is positive, the zero-improvement criterion is exactly the existence of an allocation on the full simplex of baseline-maximal ties such that

```
rho_k(alpha)>=d_k,       A_k(alpha)=beta_k    for all k. (8)
```

The balancing target has changed from zero to the projected cross coefficient beta. This is an exact finite criterion; its failure alone gives no uniform asymptotic size.

## 4. The actual allocation leaves a residual Gram matrix

Let `alpha^B` allocate every actual difference of each future block to that block. The blocks have disjoint differences, and both masks equal one there. The exact shadow expansions give

```
sum_(Delta B)a=(E0-mq)/(2q^2),
A(alpha^B)=Qcross/q^2,
rho(alpha^B)=(Ez-mS)/(2q^2).
```

Using (1), the three local allocation quantities are exactly

```
sum_(Delta B)a-delta_bar=R00/(2q^2),
A(alpha^B)-beta=R01/q^2,
rho(alpha^B)-d=R11/(2q^2)>=0.                          (9)
```

Thus the moment-deficit penalties at the actual allocation still vanish. The remaining scalar penalty is bounded by the same residual matrix:

```
Psi_ell(R01/q^2,R11/(2q^2))
 =[R00-min_(|t|<=sqrt(ell))||u+t*v||^2]/(2q^2)
 <=R00/(2q^2).                                       (10)
```

If `R11=0`, then v and R01 vanish, and this penalty is zero. Otherwise its scalar optimizer is `-R01/R11` clipped to the amplitude interval. No inverse of a zero residual variance is taken.

Let `L_B(t,s)` be capacity minus the sum of the selected full rows on the actual future differences. It is nonnegative and exactly includes the unallocated physical maxima and the maximum-minus-selected-row slack, as in the previous notes. The full identity is

```
Margin(t,s)=L_B(t,s)
  +sum_k [||u_k+t_k*v_k||^2+(s_k-t_k^2)||v_k||^2]/(2q_k^2).
                                                               (11)
```

This is also an independent direct check of every sign in the dual. In particular the actual allocation supplies the nonnegative lower bound

```
Margin_min >= sum_k min_(|t|<=sqrt(ell))
                                      ||u_k+t*v_k||^2/(2q_k^2).
```

The projected unit increment chi was already part of the old unit Cauchy slack: `e_old=chi+R00/(2q^2)`. Likewise the previous signed slack splits as `(Iz^2/V-LB_old)/(2q^2)+R11/(2q^2)`. The old full-interval hole-based lower bounds therefore cannot simply be reused as lower bounds on the new residuals. That hole variance improvement has now been paid into the demand itself.

## 5. What would give a closing-scale projection increase

The uniform first moment is the exact centroid discrepancy

```
Delta0=mq*[mean(B)+A_F-c_Omega],
A_F=(1/q)*sum_(d in F)d.                              (12)
```

On the known good epochs `m=N`, `L<=32H`, and `H<=C N^2 log(2N)`. If one additionally proved

```
|mean(B)+A_F-c_Omega|>=epsilon*H
```

on a selection preserving reciprocal-log divergence, then `V<=33^3*H^3/12` would give

```
chi >= 6*epsilon^2/[33^3*C*log(2N)].                    (13)
```

This identifies a concrete sufficient scale; the centroid separation and its frequency have not been established. Mean identities alone do not force it. For example, the actual Sidon history `{0,1,3,7}` with old prefix `{0,1,3}` and singleton future block `{7}` has `F={1,2,3}`, nonzero birth-linear z, and a unit shadow constant on its three-point Omega. Thus Delta0 is zero. Its six differences `{1,2,3,4,6,7}` verify actual Sidonicity directly. This finite example does not concern large good epochs and does not refute a cap-sensitive theorem there; it excludes an unqualified inference that actual Sidonicity makes Delta0 nonzero.

The already proved signed first-moment contribution has reciprocal-logarithmic size on good epochs. The new exact projection strengthens its denominator and adds (12), but supplies no estimate eliminating the remaining residual matrix or `L_B` in (11). Even a divergent sum of the individual increases in (13) would still need the actual shared maximum and its remaining margin. The previous endpoint-value and hole-square bounds, after their now-paid portions are removed, do not give a new non-summable residual estimate here.

## 6. Odd signed-bank shadows: zero cross energy does not mean zero projected cross

For this section only, replace the source bank by `Fhat=F union(-F)` of size `Q=2q` and use an odd feature psi. Keep a compatible actual future block B. The signed enclosing interval and its holes are

```
Jhat=[b-H,b+L-1+H],    T=|Jhat|=L+2H,
Omega=Jhat\B,         D=T-m,
c_J=b+(L-1)/2.
```

All m future points are removed, in contrast with the positive-bank convention. Use Q in every normalization above. Oddness gives the pointwise physical linear kernel `l=0` and the actual cross energy `<f_0,f_psi>=0`. But the projected cross is generally `Delta0*Iz/V`, and the residual cross is its negative. The residual matrix remains PSD and compensates exactly for that projection.

The signed uniform bank has zero first label moment. Since `sum_(Omega)x=T*c_J-m*mean(B)`, one obtains the exact formula

```
Delta0=mQ*[mean(B)-c_Omega]
      =mQ*T/(T-m)*[mean(B)-c_J].                       (14)
```

Thus a future centroid away from its interval midpoint is precisely the source of the uniform projected moment in this odd case.

For fixed s, the physical kernel and actual full energy are independent of t. The affine joint demand is maximized at

```
t=sign(beta)*sqrt(s),
```

with either sign when beta is zero. Choosing this parameter in the joint projection proves

```
E0+s*Ez >= M^2/D+(|Delta0|+sqrt(s)*|Iz|)^2/V.           (15)
```

Equivalently, the optimized raw demand at that same physical kernel is `delta_bar+s*d+sqrt(s)*|beta|`. Formula (15) also follows from the residual cross `R01=-Delta0*Iz/V` and its PSD inequality. The extra projected cross is not free energy; its payment is visible in the compensating residual matrix.

An explicit hand-derived finite example shows that the distinction occurs in actual endpoints. Take the Sidon history

```
P={0,4,10,11,13},
old prefix {0,4},    B={10,11,13},    Fhat={-4,4},
psi=sign.
```

The ten positive differences are `{1,2,3,4,6,7,9,10,11,13}`, all distinct. Here `Q=2`, `Jhat={6,...,17}`, `D=9`, `c_Omega=104/9`, `V=1244/9`, `Delta0=-4/3`, and `Iz=24`, while the full cross energy is zero. Consequently `beta=-18/311` is nonzero. These numbers come from the six shadow locations `{6,7,9,14,15,17}` and direct finite sums, not a search or tool execution. Its raw demands remain negative, so the example proves the projected-cross distinction, not a payable large-epoch gain.

Since l is identically zero for every allocation, (8) in the odd family requires beta to vanish for every row. Any nonzero beta therefore gives a strict finite improvement for this stronger demand. This does not conflict with the earlier t=0 optimum for the different, coarser demand. A general Lipschitz argument only gives a quadratic small-beta lower scale: changing one row with `t=sign(beta)*h`, `s=h^2` gives improvement at least `|beta|h-Kh^2`, where `K=sum|r|+|d|`. It supplies no automatic non-summable size.

## 7. A genuine reciprocal-logarithmic odd increment, conditional on future asymmetry

There is a stronger comparison when s is already fixed: changing only t leaves the full physical maximum exactly unchanged and increases the demand by `sqrt(s)*|beta|`. Suppose the actual next blocks satisfy

```
|mean(B)-c_J|>=epsilon*H,
|Iz|>=nu*mQH,
L<=32H,    m=N,    H<=C N^2 log(2N),
```

with fixed positive epsilon and nu. Equations (14), `V<=T^3/12`, and `T<=34H` then give

```
sqrt(s)*|beta|
 >=12*sqrt(s)*epsilon*nu/[34^3*C*log(2N)].              (16)
```

For the sign and linear odd features, the old good-prefix variance does supply a fixed nu. To see this using only finite old geometry, write `S_raw=sum_j v_j>=eta*q*H^2` for the earlier raw birth-linear variance. Each `v_j` is at most the full point variance `V_P=sum_(a in P)(a-mean(P))^2`, so `S_raw<=(N-1)V_P`. Since `sum_(d in F)d^2=N V_P` and `d<=H`,

```
(1/q)*sum_F d >= eta*N*H/(N-1),
(1/(qH))*sum_F d^2 >= eta*N*H/(N-1).
```

These are respectively the signed first moment divided by Q for `psi=sign` and `psi(d)=d/H`. Hence one may take `nu=eta` for those features at these good old prefixes. This is a finite variance calculation, not a signed-bank causal Abel argument.

The missing premise in (16) is the required future-block centroid asymmetry with sufficient frequency. No such frequency theorem is proved here, and symmetric-centroid blocks give beta zero. Even if (16) accumulated divergently over a suitable family, its demand increase would have to be compared with the actual remaining physical margin in (11). In particular the sign endpoint has the previously identified positive-unit kernel, so improvement over a coarse signed demand is not automatically improvement over the best existing positive-bank demand for that kernel.

The joint projection removes additional identifiable paid slack and yields a sharper affine dual. It supplies a concrete closing-scale conditional increment and an actual geometric variable on which that increment depends. It does not establish the needed frequency, residual control, shared-margin contradiction, or original Q1 theorem.

Primary source snapshots: `scalar_moment_physical_cone.md`, SHA-256 `220e45b46ca8e0da5fe767c322f2b68ae29d529754de454879a22ff085076351`; `physical_allocation_shadow_slack.md`, SHA-256 `8660411a22fc4c52811ee71fc1723287fb1f1aeb7709b3a156a2184ee424d281`. Existing files and Lean sources were preserved.

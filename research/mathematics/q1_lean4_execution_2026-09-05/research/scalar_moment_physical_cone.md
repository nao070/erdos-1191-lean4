# A convex family joining scalar signs and future-moment demand

2026-09-05. Author: `/root`, GPT-6 Astra Ultra.

Status: a finite exact family of nonnegative PSD carriers, its shared
physical optimization dual, and an exact actual-shadow decomposition.
This includes both the scalar and pure moment directions studied
previously. It supplies neither the fixed-cap contradiction nor a final
Lean theorem for original Q1. No optimization solver or Lean run was
used. Standard finite-dimensional convex minimax is used below as a
mathematical theorem, not as a currently formalized declaration.

## 1. A two-parameter carrier with every prefix mass preserved

Fix each actual old prefix F_k with q_k labels, its actual birth-linear
normalized vector z_k, and its actual disjoint future block B_k. Use
the same interval with holes removed, of positive size D_k, and the
same first-moment lower bound LB_k as in `future_moment_demand.md`.
Suppress k temporarily. Complete actual birth classes have sum z=0,
and |z_d|<=1. Fix 0<ell<=1 and choose

```
t^2<=s<=ell.
```

Consider the full matrix

```
W(t,s)=J+t(1 z^T+z 1^T)+s z z^T
      =(1+t z)(1+t z)^T+(s-t^2)z z^T.                   (1)
```

It is PSD. Its entries are also nonnegative: the bilinear function
`1+t(x+y)+sxy` on [-1,1]^2 takes its minimum at a corner. Its corner
values are `1+2t+s`, `1-2t+s`, and `1-s`. The first two are at least
`(1-|t|)^2` because s>=t^2, and the last is nonnegative.

On every literal prefix its mass is the uniform matrix mass, since
that prefix has sum z=0. On the full bank its mass is q^2 and its
trace is q+sS, where S=sum z^2. No linear trace term remains. The
parameter domain K_ell is compact and convex; s is an epigraph
coordinate for t^2, not a second independent sign choice.

## 2. A demand valid for the entire convex family

Let f_0 and f_z be the actual future shadows, and let Omega be the
hole-deleted interval of size D. Both shadows vanish at the actual
future points. On Omega,

```
sum f_0=mq,       sum f_z=0,       E_z:=sum f_z^2>=LB.
```

The scalar channel in (1) has mass mq. Cauchy on that channel and
the moment bound on the other channel give

```
E_W=||f_0+t f_z||^2+(s-t^2)E_z
    >=(mq)^2/D+(s-t^2)LB.
```

The normalized raw demand is consequently

```
delta(t,s)=delta0+s d-c t^2,
delta0=[(mq)^2/D-mq]/(2q^2),
c=LB/(2q^2)>=0,       d=(LB-mS)/(2q^2).                 (2)
```

At t=0 this is the existing moment demand. At s=t^2 it is precisely
the mass-only scalar demand `delta0-t^2 mS/(2q^2)`. Thus the new
family does not charge the moment lower bound to a pure scalar
channel a second time. All these are raw inequalities. On sufficiently
large extended good epochs, with m=N and fixed cap, the trace bound
q+sS<=2q proves their positivity throughout K_ell; no such positivity
is claimed for arbitrary future blocks.

## 3. The physical maximum remains one copy per actual label

Retain the literal old-label exclusion and actual future-span masks.
Let a_k(u) be the normalized masked unit kernel. Define the two masked
directions without an ell factor by

```
l_k(u) = masks/q_k^2 * sum_(v,v+u in F_k)(z_v+z_(v+u)),
r_k(u) = masks/q_k^2 * sum_(v,v+u in F_k)z_v z_(v+u).
```

Then |l_k|<=2a_k, |r_k|<=a_k, and the matrix proof above gives
`a_k+t_k l_k+s_k r_k>=0` on K_ell. With T a finite set containing
all supports, put

```
C(t,s)=sum_(u in T) max(0,max_k[a_k(u)+t_k l_k(u)+s_k r_k(u)]),
D0=sum_k delta0_k,
M(t,s)=C(t,s)-D0+sum_k[c_k t_k^2-s_k d_k]>=0.            (3)
```

The last inequality is the actual disjoint-block label budget. Its
proof permits deterministic choices made from this complete finite
instance. It asserts neither an online prefix selector nor a uniform
choice theorem over all capped infinite histories.

## 4. Exact allocation dual and its closed per-row penalty

Use the same physical allocation polytope A as in
`physical_envelope_allocation_dual.md`: alpha_(k,u)>=0 and every
column sums to at most one. Define

```
A_k(alpha)=sum_u alpha_(k,u) l_k(u),
rho_k(alpha)=sum_u alpha_(k,u) r_k(u),
B_k(alpha)=rho_k(alpha)-d_k,
L(alpha)=C(0,0)-sum_(k,u)alpha_(k,u)a_k(u)>=0.
```

For real A and kappa>=0 define the nonnegative continuous function

```
Psi_ell(A,kappa)=max_(|t|<=sqrt(ell))[-At-kappa t^2].
```

It has the explicit form

```
A^2/(4kappa),                         if kappa>0 and |A|<=2kappa sqrt(ell),
sqrt(ell)|A|-ell kappa,                otherwise.
                                                               (4)
```

The second line includes kappa=0. For a fixed allocation, minimizing
the row expression `At+Bs+c t^2` over K_ell gives

```
ell min(B,0)-Psi_ell(A,c+max(B,0)).                      (5)
```

Indeed for B>=0 the minimizing s is t^2, leaving coefficient c+B;
for B<0 it is ell, leaving the constant ell B and coefficient c.
In both cases that quadratic coefficient is nonnegative.

Writing M_min for the minimum of (3) and I_max=M(0,0)-M_min gives
the exact dual improvement formula

```
I_max=min_(alpha in A) [ L(alpha)
       +ell sum_k(d_k-rho_k(alpha))_+
       +sum_k Psi_ell(A_k(alpha),c_k+(rho_k(alpha)-d_k)_+) ].       (6)
```

To justify the equality, express the finite maximum C as the maximum
over A of `sum alpha(a+t l+s r)`. Its resulting payoff is continuous,
convex in the product of the compact convex K_ell domains (c_k>=0),
and affine in the compact convex allocation domain. Finite-dimensional
convex minimax therefore exchanges min_(t,s) and max_alpha. Applying
(5) proves (6), with attained extrema. Weak duality also follows
directly by substituting any allocation into the maximum in (3).

All terms in (6) are nonnegative. Thus I_max=0 exactly when there
is one allocation on baseline-maximal rows, including all their ties,
such that rho_k>=d_k and A_k=0 for every k. The condition A_k=0
follows because ell>0 and Psi_ell(A,kappa)=0 if and only if A=0.
The older pure-moment criterion lacked these linear balance equations.
A failure of this finite feasibility system gives a strict improvement,
but no uniform size or negative final margin.

## 5. What an actual block allocation pays, and what it can reduce

Use the allocation alpha^B that assigns each actual positive difference
of B_k to that block. Its masks equal one on those differences. Write

```
E0_k=||f0_k||^2,    Ez_k=||fz_k||^2,
Q_k=<f0_k,fz_k>,
v_k=f0_k-(m_k q_k/D_k)1_(Omega_k),
e_k=||v_k||^2/(2q_k^2).
```

The exact convolution expansions and complete centering imply

```
rho_k(alpha^B)=(Ez_k-m_k S_k)/(2q_k^2),
A_k(alpha^B)=Q_k/q_k^2,
rho_k(alpha^B)-d_k=(Ez_k-LB_k)/(2q_k^2)>=0,
c_k+(rho_k(alpha^B)-d_k)=Ez_k/(2q_k^2).                 (7)
```

The linear expansion has no diagonal term because sum z_k=0. These
identities keep the actual finite shadows, not their interval-average
relaxations. In particular the pure-moment deficit at this allocation
is zero; it does not need to be covered by e_k.

The scalar penalty from (6) is instead

```
Psi_ell(Q_k/q_k^2,Ez_k/(2q_k^2))
 = [||v_k||^2-min_(|t|<=sqrt(ell))||v_k+t fz_k||^2]/(2q_k^2)
 <=e_k.                                                (8)
```

Here Q_k=<v_k,fz_k> since fz has zero mass. If Ez=0 then Q=0 and
the penalty is zero. Otherwise the minimizing t is the projection
of -Q/Ez onto [-sqrt(ell),sqrt(ell)]. When that bound is inactive,
the remaining local slack is exactly
`||v_k-(Q_k/Ez_k)fz_k||^2/(2q_k^2)`.

Consequently the explicit allocation gives the rigorous bound

```
M_min >= sum_k [e_k-Psi_ell(Q_k/q_k^2,Ez_k/(2q_k^2))]>=0. (9)
```

The same fact has an exact primal decomposition. Set

```
L_B(t,s)=C(t,s)-sum_k sum_(u in Delta B_k)
                         [a_k(u)+t_k l_k(u)+s_k r_k(u)]>=0.
```

Then

```
M(t,s)=L_B(t,s)
 +sum_k [||v_k+t_k fz_k||^2
              +(s_k-t_k^2)(Ez_k-LB_k)]/(2q_k^2).        (10)
```

This is an identity with all unused-label and maximum slack in L_B,
the scalar-adjustable local shadow variance in the first square, and
the nonnegative moment excess in the last term. It verifies all
signs in (6)--(9) independently of minimax. The linear scalar choice
can remove only the component of that variance in its feature
direction, with an additional amplitude restriction. It does not
automatically pay the remaining orthogonal variance or L_B.

## 6. Remaining route to original Q1

The family strictly combines the previously separate choices rather
than adding an independent physical budget for each. To turn it into
a Q1 contradiction requires a cap-sensitive assertion about the
minimum in (6), or an equivalent bound on the actual quantities in
(10), at a finite horizon of every hypothetical capped infinite
history. The explicit allocation and nonnegative decomposition show
why a finite improvement or moment divergence alone does not do that.
The uniform assertion remains unproved, as does the required original
Q1 theorem and its final Lean verification.

# Actual-difference allocation has no moment-deficit penalty

2026-09-05. Author: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

**Status.** This note strengthens the actual-history witness in `physical_envelope_allocation_dual.md` without changing that previously audited source. The residual allocation satisfies every moment requirement exactly up to a nonnegative signed-shadow square slack. All deficit penalties vanish at this allocation. Exact local and full-envelope slack decompositions, strictness statements, and two modest cap-sensitive lower bounds are proved below. No numerical optimization, experiment, or Lean execution is used. The required asymptotic physical-margin estimate and Q1 remain unresolved.

## 1. The same blocks, masks, and normalization

Use one finite family from the allocation note. For row k, let F be its actual old bank, `q=|F|>0`, `H>=max F`, and z its centered normalized birth-linear feature, with `|z_d|<=1`. Let B be that row's actual future block of m points, with minimum b and interval length L. It is Sidon and `Delta B` is disjoint from F. Write

```
J={b+1,...,b+L+H-1},    T=|J|=L+H-1,
Omega=J\B,             D=|Omega|=L+H-m,
f_0=1_B*1_F,           f_z=1_B*z,
E_0=sum_x f_0(x)^2,    E_z=sum_x f_z(x)^2,
S=sum_d z_d^2,         mu=sum_d d*z_d.
```

Both shadows vanish on B and outside J, with `sum f_0=mq`, `sum f_z=0`, and `sum x*f_z=m*mu`. Since `L>=m` and `H>=1`, `D>=H>=1`; the mass denominator is never zero.

For `T>=2`, put `V_J=T(T^2-1)/12` and `LB=(m*mu)^2/V_J`. When `mu=0`, use `LB=0`, including the possible `T=1` case. If `T=1`, centering forces the signed shadow to vanish, so this convention has no lost positive term. No division by zero is used.

The row kernels a and r retain the two masks `1[t notin F]` and `1[t<=L-1]`, and both are divided by `q^2`. The residual r has no factor `1/8`. For `t in Delta B` both masks are exactly one. Set

```
delta^0 = [(mq)^2/D-mq]/(2q^2),
d       = (LB-mS)/(2q^2),
rho^B   = sum_(t in Delta B) r(t),
e       = sum_(t in Delta B) a(t)-delta^0.
```

As before `0<=lambda<=ell=1/8`, and the normalized raw demand for the full matrix `J+lambda zz^T` is `delta^0+lambda d`.

## 2. Exact signed energy gives the stronger witness

Expanding the signed square over the actual future points gives

```
E_z = mS+2*sum_(t in Delta B)
                         sum_(d,d+t in F) z_d*z_(d+t)
    = mS+2q^2*rho^B.                                  (1)
```

The diagonal comes from equal future points. Each distinct future-point pair has one positive difference, and Sidon difference uniqueness makes its multiplicity one. The factor two comes from the two orders of that pair. This algebra is valid for signed z and signed residual kernels; it does not use nonnegativity of the residual.

The first-moment bound `E_z>=LB` therefore gives the exact nonnegative slack

```
h := rho^B-d = (E_z-LB)/(2q^2) >= 0.                    (2)
```

There is no extra factor `1/8` in (1)–(2). The factor ell is applied only when a parameter is set to its endpoint. In particular `(d-rho^B)_+=0`, even when either d or rho is negative.

The unit shadow satisfies the companion exact expansion `E_0=mq+2q^2*sum_(Delta B)a`. Thus

```
e = [E_0-(mq)^2/D]/(2q^2)
  = sum_(x in Omega)[f_0(x)-mq/D]^2/(2q^2) >= 0.         (3)
```

Combining these two identities proves the exact local raw margin

```
sum_(t in Delta B)[a(t)+lambda*r(t)]
                         -delta^0-lambda*d
 = e+lambda*h.                                         (4)
```

The earlier witness used only `ell*(d-rho^B)_+<=e`. Equation (2) is strictly stronger: that positive-part penalty is identically zero, so none of e is needed to pay it.

## 3. The complete physical margin retains both kinds of slack

Restore row indices. Let `U=union_k Delta B_k`, let `T_phys` contain every row support, and define

```
mu_lambda(t)=max(0,max_k[a_k(t)+lambda_k*r_k(t)]),
C(lambda)=sum_(t in T_phys)mu_lambda(t),
L_B(lambda)=C(lambda)
    -sum_k sum_(t in Delta B_k)[a_k(t)+lambda_k*r_k(t)].
```

Actual Sidonness makes the sets `Delta B_k` pairwise disjoint. Outside `T_phys` all relevant rows are zero. Consequently

```
L_B(lambda)
 = sum_(t in T_phys\U)mu_lambda(t)
   +sum_k sum_(t in Delta B_k intersect T_phys)
          [mu_lambda(t)-a_k(t)-lambda_k*r_k(t)]
 >= 0.                                                 (5)
```

This retains all unallocated physical labels and the maximum-versus-selected-row slack. It includes labels unused by the whole chosen family, other actual endpoint pairs, and unused integer labels in the envelope support. No extra source copy is assigned.

Summing (4) and then (5) gives the exact decomposition

```
M(lambda)=L_B(lambda)+sum_k e_k+sum_k lambda_k*h_k
         >= sum_k e_k+sum_k lambda_k*(E_z,k-LB_k)/(2q_k^2).
                                                               (6)
```

The actual allocation `alpha^B` from the LP note has `L(alpha^B)=L_B(0)`. Since every `rho_k^B>=d_k`, all its dual penalties vanish. Both directly from (6) and by inserting this allocation into the exact dual,

```
M_min >= sum_k e_k,
I_max <= L(alpha^B)=M(0)-sum_k e_k.                     (7)
```

More precisely, at any box point,

```
M(0)-M(lambda)
   = L_B(0)-L_B(lambda)-sum_k lambda_k*h_k.              (8)
```

The perturbations can reduce the allocation/envelope portion of the unit margin. They leave the unit local Cauchy slack e intact and add the nonnegative signed-shadow slack weighted by lambda. This does not assert that the actual allocation is optimal in the dual.

These are raw-demand identities. They need no positivity assumption. If positive-part demands replace the raw demands, the exact margin is instead `M(lambda)-sum_k(-delta_k(lambda_k))_+`; the lower floor in (7) cannot simply be copied to that expression. On the established sufficiently large extended good epochs, all raw demands in the entire box are positive, so the same identities and bounds do apply to positive-part bookkeeping there. This range uses the same actual next blocks `m=N`, their actual denominators, and one fixed cap onset; the blocks in (1), (4), and the allocation must not be replaced independently.

## 4. Exact projection slack and finite strictness

For `T>=2`, let `c_J` be the mean of J and `phi(x)=x-c_J`. Since `sum phi*f_z=m*mu`, completing the square gives

```
E_z-LB
 = sum_(x in J)[f_z(x)-(m*mu/V_J)*phi(x)]^2.             (9)
```

In particular the actual holes `Q=B\{min B}` contribute to this square with `f_z=0`. If `mu!=0` and `m>=3`, at least one of their `m-1` distinct positions is not the center `c_J`. Hence `h>0` in this case. When `mu=0`, equation (9) reduces to the nonnegative norm `E_z`; when the signed shadow is zero, no positive h is asserted.

For any fixed finite family with every `h_k>0` and `L_B(0)>0`, (6) and compactness even give `M_min>sum e_k`: equality would require every `lambda_k=0` and `L_B(0)=0` simultaneously. Equivalently `I_max<L_B(0)`. This is finite strictness, not a uniform quantitative gap across horizons.

## 5. What elementary cap-sensitive slack bounds supply

The local slacks cannot be discarded merely because their exact formulas are nonnegative. Some explicit lower bounds are available, but the following bounds alone have insufficient divergent scale.

First, the leftmost nonzero unit-shadow value is exactly

```
f_0(min B+min F)=1.
```

Only the two minima can give that sum, and the position belongs to Omega by compatibility. If `D>1`, apply Cauchy to the other `D-1` values, whose sum is `mq-1`. Equation (3) then gives

```
e >= [(mq-D)^2]/[2q^2 D(D-1)].                          (10)
```

For `D=1`, the unique shadow value and its total imply `mq=1`, so e is zero and (10) is not used. At good epochs with `m=N`, `D<=33H_N<=33C N^2 log(2N)`, eventually `Nq>=2D`. Consequently

```
e >= 1/[8*33^2*C^2*N^2*log(2N)^2].                     (11)
```

This is a positive lower bound with constants fixed by the cap. Its own sum is finite even over all integer N, so it proves no divergent lower bound on the actual accumulated e. It is not an upper bound on that accumulated slack either.

There is also a bound from the actual Sidon holes in (9). Put `r=m-1>=2`, `q_r=binom(r,2)`, and

```
W_Q=sum_(x in Q)(x-c_J)^2.
```

Centering Q at its own mean can only reduce this sum. Its pair-difference variance identity and its `q_r` distinct positive integer differences give

```
W_Q >= (1/r)*sum_(x<y in Q)(y-x)^2
    >= q_r*(q_r+1)*(2q_r+1)/(6r).
```

The first comparison is an equality after replacing `c_J` by Q's own mean. Inserting the hole part of (9) therefore proves

```
h >= [LB/(2q^2)] * [W_Q/V_J].                          (12)
```

For the same large good epochs, suppose `LB>=c*q^2/log(2N)`, with fixed `c>0`. Since `r=N-1>=N/2`, `q_r>=r^2/4`, `W_Q>=r^5/192`, and `V_J<=T^3/12`, the bounds `T<=33C N^2 log(2N)` give the explicit estimate

```
h >= c/[1024*33^3*C^3*N*log(2N)^4].                    (13)
```

Its displayed lower scale is again summable over the dyadic good ranks (indeed over all sufficiently large integer N). It establishes positivity and a definite cost for nonzero lambda, but not the missing non-summable or fixed-fraction physical-margin estimate. Stronger information on the actual unit shadow variance, signed projection error, or envelope allocation would be needed for that purpose.

The new result is the exact strengthening (2), the surviving local floor and complete physical decomposition (6)–(8), and the qualified slack estimates above. The prior LP note remains valid but its actual-history witness bound can now be sharpened as in (7). No cap-sensitive exclusion of the actual witness, asymptotic closing inequality, or original Q1 proof is supplied.

Sources read at derivation: `physical_envelope_allocation_dual.md`, SHA-256 `e5b42230d969755e0c0f18c66190724ad3278fb3584e221e2c38d28832df5eeb`; `future_moment_demand.md`, SHA-256 `2b3a5f47c7addc35ff4a323c3561b076cd2880ec21ec6d25108ce8f516bb05d4`. Their text was preserved.

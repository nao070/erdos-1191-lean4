# The full completed-fiber mean correction as a square and an endpoint term

Date: 2026-09-05. Owner: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

Status: an exact formula for the **full** `Mean_s` from
`completed_fiber_gram_route.md`, followed by an exact square completion
with its retained `Gram_s`. The remaining signed endpoint term is
explicit in actual ambient prefix means and complete-fiber endpoints.
The available bound for it is quadratic in the fiber size, not linear.
Thus this does not establish that `Mean_s` can be paid by the retained
squares plus `O(R)`, a cubic global lower bound, an actual counterexample
family, or Q1. The skew correction is unchanged. No Lean file was edited.

## 1. Notation and the mean correction to be evaluated

Use exactly the setting and definitions of the preceding note. In
particular, `P={a_1<...<a_N}` is actual integer Sidon, repeated two-sums
included; `H=a_N-a_1>0`. For a fixed sum `s`, the triples
`U_1,...,U_R` are **all** distinct-point triples of that sum, ordered by
their largest endpoint `n_r`. Their supports are pairwise disjoint.
Write `E` for their union, so `|E|=3R`, and put

```
c=s/3,  x_i=(a_i-c)/H,  mu_i=(m_i-c)/H,
b_i=x_i-mu_i,  t_i=x_i+mu_i,
Q_ji=mu_j-x_i if i<j, and Q_ji=0 otherwise.
```

Here `m_i` is the original ambient prefix mean, with the formal
convention `m_1=a_1`. Let `nu_r` be the incidence vector of `U_r` and

```
v_r=sum_(u<=r)nu_u,  e=v_R/R,  xi_r=v_r-r e,
lambda_r=2mu_(n_r),  Delta_r=lambda_(r+1)-lambda_r >= 0.
```

The positive vector `e` has mass **3**, zero `x` moment, and value
`1/R` on `E`. Each `xi_r` has zero mass and zero `x` moment. Set

```
C_R = R(R-1)/2,
B_lambda = sum_(r=1..R)(r-1)lambda_r,
rho = sum_(r<R)(r-1)Delta_r xi_r,
Base_s = C_R e^T diag(x)Qe+B_lambda e^T Qe.                (1)
```

Then the original, untruncated mean correction is exactly

```
Mean_s = Base_s-rho^T Q^T e.                             (2)
```

The vector `rho` also has zero mass and zero `x` moment. Its endpoint
coefficients have a useful closed expression. If an endpoint belongs
to `U_u`, define

```
omega_u = sum_(r=u..R-1)(r-1)Delta_r,
baromega = (1/R)sum_(u=1..R)omega_u.
```

Then `rho_i=omega_u-baromega`. The `omega_u` are nonincreasing in
completion ordinal. They need not be monotone in endpoint rank: a
later-completing triple can contain early endpoints. This distinction
prevents inserting an unproved sign into the formula below.

## 2. Applying the min kernel with positive mass retained

Put `K_ij=min(t_i,t_j)`. The full symmetric identity is

```
Q+Q^T = diag(b)+mu 1^T+1 mu^T-K.                         (3)
```

Because `rho` has zero mass and zero `x` moment, but `e` has mass 3,

```
rho^T(Q+Q^T)e
 = (1/R)rho.b+3rho.mu-rho^T Ke
 = -(3-1/R)rho.b-rho^T Ke.                               (4)
```

In the first line the diagonal coefficient is exactly `1/R`, since
`e_i=1/R` on the support of `rho`. The factor 3 comes from the mass
of `e`. No zero-mass quadratic identity has been applied to `e`.

For any vector `u` supported on `E`, write
`T_u(y)=sum_i u_i 1[t_i>y]`. Let
`I=[min_(i in E)t_i,max_(i in E)t_i]`. Since `rho` has zero mass,
the constant part of the min-kernel representation vanishes, giving

```
rho^T Ke = integral_I T_rho T_e,
integral_I T_rho = rho.t = -rho.b.                       (5)
```

Define `f_s(y)=T_e(y)-3+1/R` on `I`, and zero outside `I`. Combining
(2)--(5) proves the closed form

```
Mean_s = A_end,s+integral_I T_rho(y) f_s(y)dy,
A_end,s = Base_s+rho^T Qe.                               (6)
```

For completeness, the positive-mass self term in (1) is

```
e^T Qe
 = (1/4)sum_(i,j in E)e_i e_j |t_i-t_j|
   - ((3-1/R)/2)sum_(i in E)e_i b_i.                     (7)
```

Indeed `min(t_i,t_j)=(t_i+t_j-|t_i-t_j|)/2`, and
`e.t=e.mu=-e.b`. Equation (7) retains the signed mass term and does
not assert positivity of `e^T Qe`.

## 3. A formula involving only ordered endpoints and completion counts

Sort the complete endpoint set as `i_1<...<i_(3R)`. For `k>=2` set

```
d_k = mu_(i_k)-(1/(k-1))sum_(ell<k)x_(i_ell)
    = [m_(i_k)-(1/(k-1))sum_(ell<k)a_(i_ell)]/H.          (8)
```

Thus `d_k` is the difference between the actual ambient prefix mean
and the preceding **fiber-endpoint** mean. These are different means;
neither is substituted for the other. Directly from the definition of
`Q`,

```
(Qe)_(i_k) = (k-1)d_k/R,

A_end,s = (1/R^2)sum_(k=2..3R)(k-1)d_k
                [C_R x_(i_k)+B_lambda+R rho_(i_k)].      (9)
```

The `k=1` term is zero, so it requires no prefix average. Every
quantity in (9) is determined by the actual endpoints, their complete
triple membership, and the original ambient prefix means.

For the integral in (6), let

```
ell_k = t_(i_(k+1))-t_(i_k) > 0,
C_r(k) = |{i_1,...,i_k} intersect (U_1 union ... union U_r)|.
```

On the open interval between these two consecutive endpoint times,

```
f_s = -(k-1)/R,
T_(xi_r) = rk/R-C_r(k).                                 (10)
```

Consequently the full answer (6) can equivalently be written as the
finite sum

```
Mean_s = A_end,s
  - sum_(k=1..3R-1)ell_k (k-1)/R
       sum_(r<R)(r-1)Delta_r [rk/R-C_r(k)].              (11)
```

In particular, the correction involves completion-count discrepancy,
not merely the final endpoint mean `c`. Formula (11) includes every
triple of the fixed fiber and every endpoint of those triples.

## 4. Completing the retained Gram term

The previous note retains the nonnegative term

```
Gram_s = (1/4)sum_(r<R)Delta_r ||T_(xi_r)||_(L2(I))^2.
```

Define

```
W2_s = sum_(r<R)(r-1)^2 Delta_r,
J_s = ||f_s||_2^2
    = sum_(k=1..3R-1)ell_k ((k-1)/R)^2,

Endpoint_s = A_end,s-W2_s J_s,
NewGram_s = (1/4)sum_(r<R)Delta_r
                    ||T_(xi_r)+2(r-1)f_s||_2^2 >= 0.   (12)
```

Expansion, using `T_rho=sum_(r<R)(r-1)Delta_r T_(xi_r)`, now gives
the exact identity

```
                 Gram_s+Mean_s=NewGram_s+Endpoint_s.     (13)
```

This isolates one explicit signed endpoint term. A sufficient
fiberwise estimate would be `Endpoint_s>=-C R`, with a universal
constant. A weaker sufficient global estimate would be
`sum_s Endpoint_s>=-C N^3`, or such an estimate after charging a
specified portion of the actual automatic-column squares. None of
these estimates has been proved here.

The elementary bounds explain the remaining scale gap. The actual
normalizations give

```
|d_k|<=1,  |x_i|<=1,  |lambda_r|<=2,
sum_r Delta_r<=2,  |rho_i|<=2(R-1),
W2_s<=2(R-1)^2,  |I|<=2,  J_s<=18.
```

Equation (9) therefore gives

```
|A_end,s| <= (63/4)R^2,
W2_s J_s <= 36R^2,
|Endpoint_s| <= 52R^2.                                 (14)
```

For the first bound use `|B_lambda|<=R(R-1)` and
`sum_(k=2..3R)(k-1)<=9R^2/2`. Since
`sum_s R_s=binom(N,3)` and `R_s<=N/3`, summing (14) only yields
an `O(N^4)` bound. This failure of the available estimate does not
give an actual family attaining the quartic scale and is not a
counterexample to cubic control. For `R=1` all terms are zero; for
`R=2`, `rho=W2_s=0`, although the base term can remain.

Substitution in the earlier global identity retains the same error:

```
X_z = (1/2)sum_i C_i^2+sum_s NewGram_s
        +sum_s Circ_s+sum_s Endpoint_s+E_N,
|E_N|<=17N^3.                                          (15)
```

Here `C_i=sum_(j>i)Q_ji` is the actual full ambient column. The
skew correction `Circ_s` is still present; controlling `Endpoint_s`
alone would not close the entire argument.

## 5. An alternative exact use of automatic columns, with omitted endpoints paid

It is possible to complete the actual automatic square against the
original mean term, but the outside-fiber contribution must remain.
For `i in E_s` define

```
C_i^out(s)=sum_(j>i,j not in E_s)Q_ji,
O_s=(1/R_s)sum_(i in E_s)rho_i^(s) C_i^out(s),
zeta_i=sum_(s:i in E_s)rho_i^(s)/R_s.                   (16)
```

All fibers use the same ambient `Q`: its entries are
`(m_j-a_i)/H` and thus independent of the fiber center `c`. Also

```
(Q^T e_s)_i = [C_i-C_i^out(s)]/R_s     for i in E_s.
```

Summing (2) over fibers and completing the global square once gives

```
sum_s Mean_s = sum_s(Base_s+O_s)-sum_i C_i zeta_i,

(1/2)sum_i C_i^2+sum_s Mean_s
 = (1/2)sum_i(C_i-zeta_i)^2
    +sum_s(Base_s+O_s)-(1/2)sum_i zeta_i^2.              (17)
```

This is an alternative accounting identity, not additional capacity
to add a second time to (13). It shows exactly what is lost if a
restricted fiber column is silently replaced by a full ambient
column. The residual in (17) has no proved cubic lower bound. The
crude bounds `|rho_i^(s)|/R_s<=2` and at most `binom(N-1,2)`
triples through a fixed point allow `sum_i zeta_i^2=O(N^5)`, so
they do not provide the needed estimate. Any improvement must use
the actual relations between these endpoint coefficients and the
same ambient columns.

## 6. One fixed exact identity check and its provenance

The new script `evidence/completed_fiber_mean_exact.py` uses exact
`fractions.Fraction` arithmetic on the fixed ambient Sidon set

```
1,3,4,12,25,29,44,71,89,123,167,197,204,259,273,279,
362,410,420,483,519,700,705,800,854,887,971,1032,1259,
1297,1421,1518.
```

It verifies unique positive differences and the complete sum-1533
fiber, whose three triples in completion order are
`(259,420,854)`, `(1,273,1259)`, `(3,12,1518)`. It checks
the positive-mass identity (7), (9), (11), (13), and the
single-fiber instance of the automatic-column identity (17), as
well as the mass/moment and stated elementary bounds. This is one
fixed identity check, with no parameter sweep or asymptotic inference.

Observed results include

```
Mean_s       = 140483860774477/912870110401704,
Gram_s       = 8858311156405/342326291400639,
NewGram_s    = 3070798527536401/5477220662410224,
Endpoint_s   = -77265273495817/202860024533712.
All stated exact identities: PASS.
```

The negative endpoint value illustrates the signed residual only;
it refutes neither a linear bound nor a global cubic bound.

Execution records are
`evidence/completed_fiber_mean_exact.run.json`, `.txt`, and
`.stderr.txt`. The observed subprocess returned 0, with empty
stderr. It ran from this workspace using
`/opt/homebrew/opt/python@3.14/bin/python3.14` and the script's
absolute path. The instrumented start was
`2026-09-05T08:59:28.875407+00:00`; the finish was
`2026-09-05T08:59:28.911590+00:00`.
Before and after source SHA-256 were both
`b37be27ce60d1ecb4b1d5a65070b1eafe96f3dcd41c9d8291d4e319e19d6fa7d`.
The recorded source-unchanged gate was actually performed and passed.
The JSON retains the exact argv, cwd, complete stdout/stderr, hashes,
and subprocess timing. The passed unchanged evidence was not rerun.

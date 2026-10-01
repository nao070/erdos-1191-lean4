# Independent review of the physical-envelope allocation dual

2026-09-05. Reviewer: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

Result: no mathematical defect identified in the finite dual identities, the active-tie criterion, or the explicit actual-history witness. The full target note was read. The two literal masks and normalization were checked against `coherent_birth_linear_envelope.md` sections 2–4 and the exact local demand against `future_moment_demand.md` sections 1–3. The LP derivation was independently expanded below. No LP solver, numerical test, or Lean command was run; no new formal verification is claimed.

## The physical row and demand normalization

Each `a_k` includes the actual span indicator `1[t<=L_k-1]` and the literal exclusion of `F_(N_k)`. The new `r_k` includes these same masks and `q_k^-2`, but has no factor `1/8`. For `|z_d|<=1`, termwise domination gives `|r_k(t)|<=a_k(t)`. Consequently every row `a_k+lambda_k*r_k` is nonnegative on the entire box, with lower bound `(1-ell)*a_k`. The corresponding full matrix `J+lambda_k*z_k*z_k^T` is PSD and entrywise nonnegative, including its diagonal.

The exact normalized moment demand is

```
[m_k^2*q_k^2/D_k-m_k*q_k
    +lambda_k*(LB_k-m_k*S_k)]/(2*q_k^2)
 = delta_k^0+lambda_k*d_k.
```

Thus at `ell=1/8` the increment is `(LB_k-m_k*S_k)/(16*q_k^2)`. There is no further factor `1/8` in either `r_k` or `d_k`. The diagonal cost `m_k*S_k` is retained once. These are matrix masses `q_k^2`, already normalized by `q_k^2`, not scalar masses to be squared again.

On `Delta B_k` the span indicator is one, and the old-label exclusion is one by actual Sidon difference uniqueness. Disjoint actual point blocks have pairwise disjoint positive-difference sets. Therefore summing the actual local raw lower bounds uses each physical label at most once and proves `M(lambda)>=0`. This proof remains valid for negative raw demands; it does not assert an affine formula for their positive parts.

At the sufficiently large extended good epochs, `m_k=N_k`, `D_k<=33H_(N_k)`, and the fixed cap gives the uniform trace bound

```
delta_mass,k(lambda_k)
 >= (N_k*q_k/2)*[(N_k-1)/(66C*log(2N_k))-9/8] > 0
```

before normalization. The moment demand is no smaller. This bound holds throughout the parameter box, so the common eventual positivity assertion is correct there even without assuming `d_k>=0` for the general finite identities.

## The dual sign, extrema, and improvement

Attach a nonnegative multiplier `alpha_(k,t)` to the inequality `a_k(t)+lambda_k*r_k(t)-mu_t<=0`. With `mu_t>=0` retained in the primal domain, its Lagrangian is

```
sum_t mu_t*(1-sum_k alpha_(k,t))
 +sum_(k,t) alpha_(k,t)*a_k(t)-D0
 +sum_k lambda_k*(rho_k(alpha)-d_k).
```

The infimum over `mu>=0` is finite precisely when each column sum of `alpha` is at most one. Its value is then zero. The independent box minimizations in `lambda` give

```
min_(0<=lambda_k<=ell) lambda_k*(rho_k-d_k)
 = -ell*(d_k-rho_k)_+.
```

This proves the dual objective and its sign in (2). The displayed weak inequality in the target also follows directly for every feasible `alpha` and `lambda`. The primal has a finite attained minimum: for each box point the minimizing `mu` is the finite row maximum, and that maximum sum is continuous on a compact box. The allocation polytope is compact and nonempty; its continuous dual objective attains its maximum. Finite LP strong duality therefore gives the claimed equality. This is a standard mathematical use of strong duality, not a claim about a current Lean declaration.

Subtracting this maximum from `M(0)=C0-D0` gives exactly (3), with a minimum, the allocation loss `L`, and the positive sign before `ell*sum(d-rho)_+`. Both extrema are attained. Since `lambda=0` is available, `I_max>=0`; independently every summand in the minimization formula is nonnegative. The zero row is correctly represented by the unused mass in a column of `alpha`.

## Ties and the zero-improvement condition

Put `m_t=max(0,max_k a_k(t))`. At every physical label,

```
m_t-sum_k alpha_(k,t)*a_k(t)
 = m_t*(1-sum_k alpha_(k,t))
   +sum_k alpha_(k,t)*(m_t-a_k(t)).
```

All terms are nonnegative. Therefore `L=0` requires a full allocation at every positive maximum and support only on rows attaining that maximum. At a zero maximum all nonnegative `a_k(t)` vanish, and `|r_k(t)|<=a_k(t)` also makes every residual zero there; the allocation at that label is irrelevant.

Compactness and continuity imply that the nonnegative cost in (3) has minimum zero exactly when one feasible allocation simultaneously has `L=0` and every `rho_k>=d_k`. This is (4). Tied active rows must remain available as an allocation simplex; choosing one tie in advance can remove a valid witness. Failure of the feasibility condition implies a strictly positive attained improvement but gives no uniform lower bound on its size and no negative final margin.

## The actual-difference allocation retains every slack

Assign each `t in Delta B_k` to its actual block. Actual difference disjointness makes this an element of the single-column-simplex polytope. If a future difference lies outside the finite support set `T`, every row is zero there; omitting that zero contribution leaves all displayed sums unchanged.

The local inequality at `lambda_k=0` gives `e_k>=0`. At `lambda_k=ell` it gives exactly

```
e_k+ell*(rho_k^B-d_k)>=0.
```

If `d_k-rho_k^B` is positive this bounds `ell` times that difference by `e_k`; otherwise the positive part is zero and `e_k>=0` suffices. This proves both parts of (5), including their signs. Evaluating (2) at this actual allocation gives precisely `sum_k[e_k-ell*(d_k-rho_k^B)_+]>=0`, establishing (6) as a constructive dual lower bound for `M_min`.

Moreover the baseline decomposition is exact:

```
M(0)=L(alpha^B)+sum_k e_k.
```

Using this allocation in the minimum (3) and then applying (5) proves (7). The allocation loss contains all unallocated physical maxima and all differences between a maximum and its selected block's row. The `e_k` contain the actual local shadow surplus. Both are retained; neither is a reusable separate source capacity.

## Finite identity versus the remaining asymptotic contradiction

The construction is deterministic and finite. Its allocation uses actual future blocks, as the note states, and supplies no nonanticipating selection theorem. The finite LP and the active-tie criterion optimize only the specified moment directions, fixed masks, and fixed block family. They do not optimize all scalar carriers or all block partitions.

For every actual finite history, the explicit allocation proves that the infimum in the target's final display is at most `M(0)`. Thus the proposed strict reverse inequality is a contradiction target to be derived using the hypothetical full-cap infinite history, not an additional consequence of finite duality or positive individual demand increments. It would have to exclude the actual witness using a new cap-sensitive argument. A positive finite improvement, or failure of the zero-improvement feasibility system, supplies neither that exclusion nor a quantitative asymptotic margin bound.

The target preserves this distinction. No source correction was requested. Original Q1 and its required proof remain unresolved.

Reviewed target SHA-256: `e5b42230d969755e0c0f18c66190724ad3278fb3584e221e2c38d28832df5eeb`.

Supporting source SHA-256 values: `coherent_birth_linear_envelope.md` = `0b9327dbed49d7086238954e9cb5d120b6864cb59bbb2597c8d6c2763bf35d00`; `future_moment_demand.md` = `2b3a5f47c7addc35ff4a323c3561b076cd2880ec21ec6d25108ce8f516bb05d4`.

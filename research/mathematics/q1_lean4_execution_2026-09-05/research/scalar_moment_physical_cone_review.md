# Independent review of the scalar–moment physical family

2026-09-05 08:52 UTC. Reviewer: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

Result: no mathematical defect identified in equations (1)–(10), the convex minimax formulation, the zero-improvement criterion, or the actual-shadow identities. The full target note was read and all formulas independently expanded. The local demand and masks were compared with the previously read primary moment and physical-envelope notes. No solver, finite experiment, or Lean command was used. Original Q1 remains unresolved.

## Domain, full matrix, and raw demand

The set `K_ell={(t,s):t^2<=s<=ell}` is nonempty, compact, and convex for `0<ell<=1`. In particular `|t|<=sqrt(ell)<=1`. The decomposition in (1) proves PSD since `s-t^2>=0`. For fixed x or y, the entry `1+t(x+y)+sxy` is affine in the other variable; its minimum over the square occurs at a corner. The same-sign corners are bounded below by `1-2|t|+s>=(1-|t|)^2`, and the opposite-sign corners equal `1-s>=0`. Thus full entrywise nonnegativity holds even though the separately written residual terms are signed.

Complete-class centering kills the restricted coefficient sum on every actual prefix, so its matrix mass remains its uniform mass. On the full bank `1^T W 1=q^2`, and `tr W=q+2t*sum z+s*S=q+s*S`. These are full matrix masses and traces, with no second squaring of `q^2` and no dropped linear diagonal.

The actual scalar channel has sum `mq`, giving `||f_0+t*f_z||^2>=(mq)^2/D`. Multiplying the moment estimate by `s-t^2>=0` and subtracting the full diagonal `m(q+s*S)` proves precisely

```
delta(t,s)=delta0+s*(LB-m*S)/(2q^2)-t^2*LB/(2q^2).
```

At `t=0` this is the moment demand; at `s=t^2` it is `delta0-t^2*m*S/(2q^2)`, the mass-only scalar demand. The moment energy is not charged twice on the scalar edge. That edge covers `|t|<=sqrt(ell)`; choosing `ell=1` includes the whole previously allowed scalar amplitude range `|t|<=1`.

All formulas concern raw demands. The stated positivity application is correctly restricted to actual next blocks `m=N` at sufficiently large extended good epochs. There `D<=33H_N`, the fixed cap holds, and `tr W<=2q`. The lower bound `(Nq/2)*[(N-1)/(66C*log(2N))-2]` is positive eventually, uniformly over the whole domain. Since `s-t^2>=0`, the additional moment term cannot invalidate this bound. Arbitrary future blocks have no such assertion.

The denominator `D=L+H-m` is positive in the compatible nonempty integer setting. The earlier moment convention uses `LB=0` when the first moment is zero, including any degenerate one-point interval; no singular moment denominator is silently introduced by c or d.

## Kernels, linear normalization, and minimax

The same literal old-label and actual-span masks multiply a, l, and r. Summing the complete matrix entries on each physical source pair gives exactly `a+t*l+s*r`, with `|l|<=2a` and `|r|<=a`. The row is nonnegative by the full matrix proof. Its physical maximum has one copy per actual difference. Actual future difference disjointness therefore proves (3) for every deterministic parameter choice in the finite product domain.

For a fixed physical allocation write `A=sum alpha*l` and `B=rho-d`. If `B>=0`, minimizing over `s` selects `s=t^2`, leaving `At+(c+B)t^2`. If `B<0`, it selects `s=ell`, leaving `ell*B+At+c*t^2`. Both quadratic coefficients are nonnegative. Thus the row infimum is exactly

```
ell*min(B,0)-Psi_ell(A,c+max(B,0)).
```

The unconstrained optimizer for `-At-kappa*t^2` is `-A/(2kappa)` when `kappa>0`; clipping it to the stated interval gives (4). The two branches agree at their boundary. For `kappa=0` the maximum is `sqrt(ell)*|A|`, including zero at A=0. The function is nonnegative and continuous, and for `ell>0` it vanishes exactly when A=0.

Representing the row maximum as a maximum over column simplexes gives a payoff affine in allocation and convex in `(t,s)`, with its only quadratic term `sum c_k*t_k^2`. Both domains are compact convex sets and the payoff is continuous. Convex minimax applies with the stated attained extrema. Substituting the row infimum and subtracting from `C(0,0)-D0` gives (6), including the plus sign before both penalties and the argument `c_k+(rho_k-d_k)_+` of Psi.

Since all terms in (6) are nonnegative, zero improvement is equivalent to one allocation simultaneously satisfying `L=0`, `rho_k>=d_k`, and `A_k=0` for every row. The first condition retains the full simplex of baseline-maximal ties and full column mass at each positive maximum; at a zero maximum all directions vanish. The extra linear balance equations are necessary because Psi cannot vanish for a nonzero A. Strict finite improvement from infeasibility carries no uniform lower bound or negative-margin conclusion.

## Actual shadows and the factor in the linear term

At the actual-block allocation the masks are one on `Delta B`. The signed square expands to `Ez=m*S+2q^2*rho^B`, as in the shadow-slack note. The mixed unit/signed inner product has zero diagonal `m*sum z=0`. For each unordered future-point pair of positive difference u, its two ordered contributions are respectively `z_v` and `z_(v+u)`. Therefore

```
Q=<f_0,f_z>
 =sum_(u in Delta B) sum_(v,v+u in F)(z_v+z_(v+u)),
A(alpha^B)=Q/q^2.
```

There is no additional factor two in this linear identity. It is the coefficient `2t*Q` in the full shadow energy that contains a two. This proves all q factors in (7), including

```
rho^B-d=(Ez-LB)/(2q^2)>=0,
c+(rho^B-d)=Ez/(2q^2).
```

Consequently the pure-moment penalty at the actual allocation is zero.

Centering `v=f_0-(mq/D)*1_Omega` gives `Q=<v,f_z>` and `e=||v||^2/(2q^2)`. Expanding the square proves (8) exactly. If `Ez=0`, the real square norm makes `f_z=0`, hence Q=0 and Psi=0; no division by Ez is used. Otherwise the minimizing t is `-Q/Ez` clipped to the interval. In the inactive-bound case the residual norm is the stated orthogonal projection. Nonnegativity of the minimized norm gives `Psi<=e`, proving the final sign in (9).

## The full exact slack decomposition and remaining scope

The local row sum on `Delta B` minus its raw demand is

```
[||v||^2+2t*Q+s*(Ez-LB)+t^2*LB]/(2q^2)
 =[||v+t*f_z||^2+(s-t^2)*(Ez-LB)]/(2q^2).
```

This independently verifies every sign in (10). The selected future differences are disjoint. Thus `L_B` is precisely the sum of the unallocated physical maxima plus the maximum-minus-selected-row differences on the allocated labels, all nonnegative. Labels outside the common finite support have zero row values and add no missing term. Adding these local margins proves the complete identity (10).

The scalar parameter can remove the component of the unit-shadow variance in its one feature direction, subject to the amplitude bound. Neither this projection nor the moment direction removes the remaining orthogonal variance or the actual allocation/envelope slack. The family, demand, masks, and future blocks in the identity are the same finite instance throughout. No online selection, separate per-direction budget, uniform cap-sensitive gap, or Q1 completion follows. No source correction was requested.

Reviewed target SHA-256: `220e45b46ca8e0da5fe767c322f2b68ae29d529754de454879a22ff085076351`.

Relevant current strengthening read and used: `physical_allocation_shadow_slack.md`, SHA-256 `8660411a22fc4c52811ee71fc1723287fb1f1aeb7709b3a156a2184ee424d281`. Existing source notes were preserved.

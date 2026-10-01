# Independent review of the prefix scalar gain dichotomy

2026-09-05 08:18 UTC. Reviewer: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

Result: the current note's equations (1)–(6) are correct under their stated hypotheses. Two application-scope clarifications were requested and incorporated by the parent: the positive-part comparison concerns the actual next block `m=N` at the sufficiently large extended good epochs, and this application takes `R>=1`. The arbitrary-block result for `m<=RN` remains a raw-demand comparison. No further correction was identified.

The entire target was read and the identities were independently expanded. Supporting definitions were checked in `retirement_shadow_review.md`, `future_moment_demand.md`, and `causal_birth_energy_telescoping.md`. No finite checker, numerical experiment, Lean build, or prior successful verification was rerun. This is a mathematical review, not new machine verification.

## Pair conventions and the sign of the comparison

For an unordered pair of distinct labels let `b` be the later source birth and `r` its actual output birth. A Born pair has `r<=b`; a mixed-born pair additionally has distinct source births. Both conventions use the actual Sidon endpoint clocks. In this review write `L=sum_born z_d z_e`. Within each centered birth class the unordered product sum is minus one half of its square sum, so

```
L = X-S/2.
```

Thus the target's `X` is the mixed-born quadratic total. It is not `L`, a signed retirement correction, or the linear statistic `B`. Same-birth classes contribute zero to the linear statistic, since each coefficient occurs the same number of times there.

Put `a=s*t` temporarily and let `u=1+a*z`. Complete-class centering gives `sum_(F_j)u=q_j` on every literal prefix. On the full bank the scalar sum is `q`, the matrix mass of `u*u^T` is `q^2`, and its trace is `q+a^2*S`. Matrix mass is not squared a second time.

For a fixed nonnegative matrix the exact historical capacity is the total strict-upper-triangle sum minus the Born-used sum. The total linear perturbation is `(q-1)*sum z=0`; the total quadratic perturbation is `-a^2*S/2`. The Born perturbation is `a*B+a^2*L`. Therefore

```
C_hist(J)-C_hist(u*u^T) = a*B+a^2*(L+S/2)
                       = a*B+a^2*X.
```

With the same actual positive denominator `D`, the full raw demand is `[m^2*q^2/D-m*(q+a^2*S)]/2`. Hence `delta_u-delta_J=-m*a^2*S/2`, proving exactly

```
[C_hist(J)-delta_J]-[C_hist(u*u^T)-delta_u]
    = s*t*B+t^2*(X-m*S/2).
```

The sign is the reduction of capacity minus demand relative to uniform. It does not assert a positive absolute physical margin for either carrier. The same expansion works when `s=-1`; it does not invoke the positive high-to-low scalar injection for that sign.

## Optimization and its uniform quantifiers

There are at most `q*(q-1)/2` Born pairs, each contributing at most two in absolute value to `B`. Thus `|B|<=q*(q-1)<=q^2`, and the chosen `t=|B|/(q^2+RNq)` lies in `[0,1]`. This proves entrywise nonnegativity of `u` and of its outer product for both signs.

The mixed-born pairs are a subset of all unordered pairs, giving `|X|<=(sum |z|)^2/2<=q^2/2`; also `S<=q`. For every compatible block with `m<=RN`,

```
X-m*S/2 >= -(q^2+RNq)/2 = -D_*/2.
```

Since `s*B=|B|`, substituting `t` proves (3) with exactly the factor `1/(2D_*)`. The sign and amplitude use only the old prefix and the one fixed bound `R`; they do not depend on the realized future size, span, or moment. When `B=0`, `t=0` and the comparison is exactly zero. If (4) holds, then for `N-1>=2R` its normalized raw gain is at least `kappa^2/[4*log(2N)]`.

## Both raw demands before taking positive parts

The general bound `m<=RN` supplies no lower bound on `m*q/D`. It alone cannot ensure positive raw demands. The target now explicitly restricts this application to `m=N`, `R>=1`, `D<=33H_N`, and `H_N<=C*N^2*log(2N)`, with one fixed `C`. For this actual next block,

```
delta_u >= (Nq/2)*[(N-1)/(66C*log(2N))-2] > 0
```

eventually. The threshold is uniform over these epochs for the fixed cap constant. Because `delta_J-delta_u=N*t^2*S/2>=0`, the uniform demand is positive too. Thus replacing both raw demands in the scalar comparison by their positive parts is valid on precisely that stated range.

For `W=J+zz^T/8`, its mass is `q^2`, trace is `q+S/8<=9q/8`, and entries are at least `7/8`. Its mass-only demand is eventually positive by the same calculation with `9/8` in place of `2`. The actual moment demand is no smaller. Moreover `delta_J>=delta_mass(W)>0`. Therefore both demands actually compared in (5), namely `delta_J` and `delta_mom(W)`, are positive there. This also confirms the qualifier for the second branch of the proposed dichotomy.

## Complementary branch and remaining scope

The capacity change for `W` is `X/8`. Its actual moment-demand change relative to uniform is `(LB-m*S)/16`. Their sum is exactly (5). Under `LB>=c*q^2/log(2N)` and `X>=-c*q^2/[4*log(2N)]`, one has `2X+LB>=c*q^2/[2*log(2N)]`. Dividing by 16 and retaining `m*S<=N*q` gives the asserted lower bound. After normalization it is

```
c/[32*log(2N)] - 1/[8*(N-1)],
```

which is at least `c/[64*log(2N)]` for all sufficiently large `N`. The constants and inequality directions in (5)–(6) therefore agree.

The note proves neither that the linear threshold occurs sufficiently often nor that the alternative quadratic threshold covers its failures. It also retains the need for one physical source, its actual envelope, and the baseline/overlap/span margin. Selecting the sign from each old prefix introduces no separate budget for that sign or prefix. Original Q1 remains unresolved.

Reviewed target SHA-256: `20ed91ecc39d72d7ca2f506645ee842b2e8c28cb25444eec50f477bbeb5af88a`.

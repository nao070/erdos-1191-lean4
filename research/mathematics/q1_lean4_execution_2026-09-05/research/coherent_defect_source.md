# A direct coherent source for the full geometry defect

2026-09-05. Parent derivation. Original Q1 remains unresolved. This note
constructs a replacement physical source, not a PSD subtraction from an
already chosen source. All quantities refer to one actual complete Sidon
history and the previous exact full-stage defect. No experiment or Lean
execution is used in the proof.

## 1. A rank-one realization of a monotone scalar potential

Use H_k, Q_k=k(k-1), alpha_k=Q_k^-2, kappa_k=alpha_k-alpha_(k+1),
and u_r=sum_(k>=r) kappa_k/H_k^2 for k,r>=2. Suppose the actual scalar
potential has V_1=0 and

```
0<=V_k<=V_(k+1),                 V_k<=Q_k^2 H_k^2.
```

On Fhat_k define the constant Gram matrix

```
C_k^V(d,e)=V_k/(4 Q_k^2 H_k^2),
Gamma_V=sum_(k>=2) kappa_k C_k^V,                    (1)
```

with each component zero outside Fhat_k in either index. Its feature is
one constant real coordinate. It is PSD and entrywise nonnegative. The
matrix is fixed consistently on all finite restrictions; no terminal
normalization or independent new allowance is introduced.

The full component mass and trace are exactly

```
M_k=V_k/(4H_k^2),    T_k=V_k/(4Q_kH_k^2),
T_k/M_k=1/Q_k whenever V_k>0.                        (2)
```

Since C_k^V<=1/4 entrywise and T_k<=Q_k/4,

```
tr Gamma_V <= 1/4 sum_(k>=2) kappa_k Q_k
             =1-zeta(2)/2.                         (3)
```

Indeed kappa_k Q_k=4/[(k-1)(k+1)^2]
=1/(k-1)-1/(k+1)-2/(k+1)^2; the total is 4-2zeta(2).
On Fhat_N, all components k>N have combined matrix mass at most

```
Q_N^2 alpha_(N+1)/4
 = (N-1)^2/[4(N+1)^2] <1/4.                         (4)
```

This also proves finite convergence of every restriction and preserves
its PSD and nonnegative properties. The complete tail remains part of
the permanent source, including pairs with never-used outputs.

Let Vcal_N=sum_(r=2..N)u_r(V_r-V_(r-1)). The exact nonnegative layer
identity is Vcal_N=sum_(k>=2)kappa_k V_min(k,N)/H_k^2. The full mass on
Fhat_N differs from Vcal_N/4 only by

```
sum_(k>N) kappa_k/(4H_k^2)
            [Q_N^2 V_k/Q_k^2 - V_N].
```

Each of the two nonnegative terms in this difference is bounded by the
quantity in (4): for the second use V_N<=Q_N^2H_N^2 and H_k>=H_N.
Consequently

```
|mass_N(Gamma_V)-Vcal_N/4|
 <=(N-1)^2/[4(N+1)^2] <1/4.                         (5)
```

Literal historical capacity is at most half the full mass, so

```
C_N(Gamma_V)<=Vcal_N/8+1/8.                         (6)
```

Equations (1)-(6) are valid for the stated scalar potential on an actual
history. They do not claim that V itself is the mass of a pre-existing
reserve matrix from which Gamma is subtracted.

## 2. Applying the realization directly to the full defect

Fix 0<=lambda<=1 and set

```
V_k=Gcum_k(lambda)/(1+lambda).
```

The previously proved actual stage defects are nonnegative. Their exact
identity gives Gcum_k=(1+lambda)Y_k-8Hcum_k(lambda), so
0<=V_k<=Y_k. Young's inequality gives
Y_k<=Q_k Z_k<=Q_k^2H_k^2. Hence every premise of (1) holds.
Call the resulting source Gamma_lambda. Now Vcal_N=Gcal_N/(1+lambda),
and (6) becomes

```
(1+lambda) C_N(Gamma_lambda)
 <= Gcal_N/8+(1+lambda)/8.                          (7)
```

This realizes the full defect directly, with no cubic fiber-diagonal
error in its financing. The actual single combined source

```
Upsilon_lambda=Psi_lambda+(1+lambda)Gamma_lambda
```

therefore satisfies

```
Elig_N(Upsilon_lambda)
 <=(1+lambda)Ycal_N/8+(1+lambda)/8.                  (8)
```

The maximum historical charge in (7) includes ineligible and never-used
pairs, so (8) does not delete them by an unsupported PSD mask.

## 3. Relation to the previous triple source without a false PSD debit

Let R_k(s)=sqrt(S_k(s)P_k^top(s)), L_k=sum_s R_k(s)^2, and let A_k be
the previous normalized translate Gram. Cauchy gives entrywise

```
A_k(d,e)<=L_k/(Q_k^2H_k^2)=:B_k(d,e).               (9)
```

Here B_k is a new constant rank-one Gram on Fhat_k and has exactly the
same diagonal and trace as A_k. Its entries dominate all actual pair
payments of A_k. In general B_k-A_k is NOT PSD: that difference has
zero diagonal and nonzero off-diagonal entries. This is consistent with
the actual obstruction in triple_source_remainder_analysis.md. Replacing
A by B as the physical source needs no PSD remainder; claiming a second
source from B-A would need one and is not done.

The exact fiber financing inequality says

```
L_k <= Gcum_k/[4(1+lambda)] + k^3H_k^2/6.
```

Thus (9) gives an entrywise comparison of actual matrices

```
Theta <= Gamma_lambda + E,
E=sum_(k>=2) kappa_k [k^3/(6Q_k^2)] J_(Fhat_k).     (10)
```

Every component of E is PSD and nonnegative, and its TOTAL full matrix
mass over the infinite physical label set is finite:

```
mass(E)=sum_(k>=2) kappa_k k^3/6
        =[2zeta(2)+1/4]/6.                         (11)
```

Hence the sum of all its unordered pair entries is at most
[2zeta(2)+1/4]/12. This one error allowance includes unused and historical
pairs. It is not recreated for each block or component.

In particular, take an actual feasible component allocation for Theta.
There is a small support issue: its original pair constraints may only
apply where A_k(h)>0, whereas Gamma and E can have extra positive entries.
For each component and physical unordered pair define the transferred
portion c_k(h)=(A_k(h)-E_k(h))^+. Then c_k(h)<=C_k^V(h), it vanishes
where A_k(h)=0, and
```
A_k(h)<=c_k(h)+E_k(h)1[A_k(h)>0].
```
For each row subtract ONLY this restricted E payment from its proved
Theta demand and keep the positive part. The result is at most the
clipped Gamma payment on that row. On every pair where these payments
are nonzero, the original Theta allocation constraint bounds its total
row fraction by one. Thus the summed transferred portions fit within
Gamma, and the summed restricted errors are bounded by the ONE full
mass allowance (11). Across components their coefficients are distinct
summands. The retained demand is therefore at least

```
D_Theta - [2zeta(2)+1/4]/12.                        (12)
```

This is a valid transfer of nonsummable actual demands up to one finite
nonnegative error. The clipped portions are physical entry allocations;
no clipped matrix is asserted PSD, and no identification with the
unchanged affine-row LP for Gamma is claimed. For the previously used
disjoint-cell allocation, all pair masks are already disjoint regardless
of A's zero entries, so the support issue is absent. In either case the
argument uses entrywise domination and the actual positive pair expansion,
not the invalid inference that Gamma-Theta is PSD.

## 4. A sharper direct finite-horizon allocation

There is also a direct demand argument for (1), independently of (12).
Fix a component k, D=H_k, and partition actual future points into cells
```
B_j=P_infinity intersect (a_k+(j-1)D,a_k+jD],
m_j=|B_j|, F_j=sum_(h<=j)m_h.
```
Each cell has physical width at most D and is strictly after bank k.
The same constant feature and mass projection give
J_j=1/2[m_j^2 M_k/(3D)-m_j T_k]. Distinct cells have disjoint actual
output differences, so their payments use each component pair at most once.

Assume one fixed eventual cap H_n<=C n^2 log(2n). The already derived
counting and finite Hardy inequalities give

```
F_j>=sqrt(jD/[C log(4jD+4)])-k-1,
sum_(j<=J)m_j^2>=1/4 sum_(j<J)F_j^2/(j+1)^2.
```

Take j0=ceil((log k)^2) and J=floor(k^2/(log k)^2), for sufficiently
large k. Uniformly for j0<=j<J, the square-root term dominates k+1:
its ratio to k is at least a constant times sqrt(log k). Thus
F_j^2>=(1-o(1))jD/[C log(4jD+4)] on this whole range.
The Sidon lower radius and fixed cap give log D=2log k+O_C(log log k).
Integral comparison consequently proves

```
sum_(j<=J)m_j^2 >= [D/(4C)] [log 2-o(1)].           (13)
```

The upper terminal coordinate relative to a_1 is (J+1)D. The unconditional Sidon count
is O_C(k^2/sqrt(log k)). Since T_k/M_k=1/Q_k exactly, the entire
diagonal cost is o(M_k), without any additional ratio hypothesis.
Therefore every component with V_k>0, for all sufficiently large k,
has a finite actual allocation satisfying

```
sum_(j<=J)J_j^+ >= [log 2/(24C)-o(1)] M_k,
                   >= log 2 M_k/(48C).             (14)
```

The o(1) is uniform for the one cap and the stated radius bounds. It
does not require V_k to have a particular size, because the exact
trace-to-mass ratio removes V_k from the error comparison. No infinite
row or repeated component allowance is used.

For the actual full-defect V, the previous good-window inequality gives
eventually V_N>=beta^2 N^6 H_N/2 on good dyadic N, where K=32 and
beta=1/(256K^2). For N<=k<2N, monotonicity of V and H_k<=K H_N imply
M_k>=beta^2 N^6/(8K^2 H_N). Summing the fixed component coefficients,
then using (14), gives a permitted good-window demand at least

```
5 beta^2 log 2/[2048 K^2 C^2 log(2N)].              (15)
```

The calculation uses sum_(N<=k<2N)kappa_k>=15/(16Q_N^2) and the one
fixed cap. Good windows have disjoint component indices and divergent
reciprocal-log sum. Thus (15) independently proves nonsummable actual
Gamma demands. Every row has a finite terminal horizon and appears
eventually as that horizon increases.

## 5. The unresolved comparison is still substantive

The direct coherent source improves the scalar financing constant and
shows that a failed PSD debit from gamma J is no objection to choosing
a rank-one source in the first place. It also replaces the previous
translate source up to a globally finite entrywise error.

Nevertheless (8) remains an upper cost bound. For additive actual rows,
the residual is exactly
```
Elig(Upsilon)-[D_old+(1+lambda)D_Gamma]
 = [Elig(Psi)-D_old]+(1+lambda)[Elig(Gamma)-D_Gamma].
```
Both terms are nonnegative. The source does not make an uncontrolled
old residual negative, nor permit allocating the same full defect twice.
The fraction in (14) still depends on the arbitrary fixed cap C.
No uniform capacity bound, cap contradiction, final Q1 theorem or Lean
verification of these new source formulas is claimed.

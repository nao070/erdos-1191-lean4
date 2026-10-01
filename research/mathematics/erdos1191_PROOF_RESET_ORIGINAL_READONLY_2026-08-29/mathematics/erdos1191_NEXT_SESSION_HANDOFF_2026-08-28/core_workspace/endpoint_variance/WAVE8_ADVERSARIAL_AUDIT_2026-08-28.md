# Wave 8 independent adversarial audit

**Date:** 2026-08-28  
**Role:** independent verifier; no source theorem or probe file was edited  
**Overall verdict:** the actual-adjacent renewal theorems, the exact `Q_m`
decompositions, the `kappa` sign theorem, the positive envelope, and the two
documented no-go witnesses survive audit.  The literal local
`global_density_innovation` inequality is already false, even on a four-mark
`C=1` prefix, and is also false at a genuine old-clear event without a
critical cap.  The narrower statement needed for P13--an asymptotic global
density-to-innovation budget on one infinite eventually critical branch--is
**OPEN**.

No finite survival computation below is promoted to infinite survival, and
no resolution or prize claim is justified.

## 1. Audited artifacts and method

The audit covered:

- `WAVE8_ACTUAL_ADJACENT_RENEWAL_2026-08-28.md` and its implementation/tests;
- `WAVE8_Q_ATOM_DECOMPOSITION_2026-08-28.md` and its verifier/tests;
- `WAVE8_SURVIVAL_DEBT_PROBE_RESULTS_2026-08-28.md`, its probe, tests, and
  deterministic JSON certificate;
- the combined `wave8_actual_atom_certificate` replay.

The exact test replay gave:

```text
23 passed, 1 deselected   # the three focused Wave 8 suites without the slow replay
1 passed                 # full survival-certificate rebuild and byte comparison
2 passed                 # combined actual-renewal/Q-atom certificate
```

All decisive quantities use integers or `Fraction`.  Independently of the
shipped verifier, I recomputed every `kappa_(p,q)` directly from `z` and `H`
for every interval at all `2 <= m <= 64` and at
`m=128,256,512`.  All coefficients were nonzero and had exactly the claimed
sign.  The largest audit, `m=512`, had 1,022 negative and 130,306 positive
coefficients.

The committed certificate files also replayed their internal hashes.  Their
whole-file SHA-256 values at audit time were:

```text
wave8_survival_debt_certificate_2026-08-28.json
  7ed2650c8901ee74a32d5404d1dc6426f28db392b8b797f140673482cf45ebb2

wave8_actual_atom_certificate_2026-08-28.json
  6da00b367e23b7f2a91b483b40ae8ccdd89ec6af719aa760f980b3a56c8eab6c
```

## 2. Exact verdict table

| Claim | Verdict | Audit reason |
|---|---|---|
| Hybrid cross plus actual-internal capacity (4) | **PROVED** | selected endpoint pairs are globally disjoint; Golomb uniqueness turns them into distinct integers in `[1,floor(T)]` |
| Harmonic activation bound (5) | **PROVED** | after expanding demand into unit atoms, cumulative capacity gives `r <= gamma_r`, hence `sum 1/gamma_r <= H_P` |
| Old-clear/new-pay dichotomy | **PROVED** | assuming both certified bounds exceed `tau_m` forces both `D^- > D^+` and `D^+ > D^-` |
| At most one outstanding internal-adjacent family | **PROVED** | induction on one fixed dyadic history; an ancestry clear repays the old debt before any new unpaid family is installed |
| Shell secant factorization and constants | **PROVED** | direct factorization gives `(u-v)^2 q(1-u-v)`; the minimum is `16/147` at `x=-1/14`, and the supremum is `36/35` at `x=-1` |
| Pair forms (12)--(14) for `S_m`, `R_m`, and `Q_m` | **PROVED** | all mass factors `1/G`, `1/N'`, `G/(NN')`, and `N/(GN')` agree with the weighted one- and two-sample covariance identities |
| Abel fan (17), lower bound (21), upper bound (22) | **PROVED** | prefix/suffix indexing and the artificial `h_0=1` convention are consistent; the Schur complement is exactly `16/147` |
| Positive non-adjacent envelope (25)--(27) | **PROVED** | AM--GM contributes the stated `1/4`; normalization by `N'` is correct; the isolated `i=0` row is at most `23G/(105N'^2)` |
| Global artificial-row sum `<=92/315` | **PROVED** | `N_{2m} >= binom(2m,2)+1 >= m^2` gives a geometric `sum 4^{-j}` |
| Complete `kappa` sign classification | **PROVED** | proof algebra checks; direct exact enumeration through `m=512` found no zero or sign exception |
| Local boundary-debt repayment (38) | **PROVED** | it is exactly nonnegativity of the shell covariance after separating positive and negative square atoms |
| Adjacent `kappa`-debt sum `<= (13/5)K log 2` | **PROVED** | `tau_m <= 3N'/2`, `delta_m <= N'`, `G >= m(m+1)/2`, and `sum_(j>=1)(j+1)/4^j=7/9`; constants multiply to `13/5` |
| Non-adjacent bulk atom is necessary | **REFUTED strengthening / PROVED no-go** | the eight-mark power-gap ruler has exact deficit `1869979/6720` if the positive non-adjacent bulk atom is deleted |
| Rank-one energy is bounded by a constant times shell covariance | **REFUTED** | for `(0,D,3D,3D+1)`, the ratio divided by `D` tends exactly to `46/45` |
| Raw certified/global/latest non-adjacent cardinality pays adjacent debt | **REFUTED** | exact `C=1` eight-mark witnesses survive two more finite levels but still have negative margins |
| Literal local `U_global/T >= I_m` | **REFUTED** | already fails for `(0,1,4,6)` at `m=2`; also fails at an old-clear event after unrestricted scaling |
| `U_global/T` controls the summed innovation on one infinite eventually critical branch | **OPEN** | no finite search proves the required quantifier or `o(log J)` sum |

## 3. Normalization and indexing checks

### 3.1 Hybrid capacity

For fixed `(m,k)`, the selected cross pairs are

```text
(m-1-t, m-1+k-t),  0 <= t < k.
```

Their right endpoints lie in the unique dyadic newborn index block
`[m,2m)`.  Cross families at different epochs therefore cannot reuse a
pair.  Their left endpoints are below `m`, whereas the internal family
`I_m` has both endpoints at least `m`; this also rules out cross/internal
reuse.  Internal families from different epochs have disjoint newborn
blocks.  These observations validate the quantifier "all active epochs at
one threshold," not merely a per-epoch capacity statement.

The rounding is also correct: an active positive difference is an integer
at most real `T`, hence lies in `{1,...,floor(T)}`.  The sharp four-mark row
at `T=11/2` has cumulative demand 5 and capacity 5.

### 3.2 Renewal history

Let `B^- = mu^-+2D^-`, `B^+=mu^++2D^+`, and
`tau=D^-+D^++max(mu^-,mu^+)`.  If `B^->tau`, then

```text
D^- - D^+ > max(mu^-,mu^+) - mu^- >= 0.
```

The analogous implication from `B^+>tau` has the opposite strict sign, so
at least one side is certified.  Old clearing includes every earlier
internal gap and every earlier dyadic boundary gap because all their indices
lie in `1,...,m-1`.

The single-debt induction is sound but its scope must be kept exact:

- it counts **families**, not demand or energy;
- it concerns the internal-adjacent families only, not the proper
  non-adjacent `kappa` boundary fan or the Abel fan;
- it is a statement along one fixed sequence of prefixes.

### 3.3 Fixed-adjoint shell comparison

Since

```text
z(u)-z(v) = (u-v)(1-u-v, 1),
```

direct multiplication by `H` gives

```text
q(x) = (16/15)x^2 + (16/105)x + 4/35.
```

Completing the square places its minimum at `x=-1/14` with value `16/147`.
On `[-1,0]`, the maximum is `q(-1)=36/35`.  The actual newborn grid uses
`u<1`, so `36/35` is normally a supremum; using the closed interval in the
inequality is harmless.  The pairwise covariance factor `1/2` is present in
both the proof and implementation.

### 3.4 `Q_m` pair and Abel forms

Writing within-block pair sums as `N^2 Cov_O` and `G^2 Cov_S`, the cross sum
is

```text
NG(Cov_O + Cov_S + dd^T).
```

This reproduces the three coefficients in (13).  Adding
`S_m=G Cov_S=(1/G) shell_pairs` leaves coefficient `1/N'` on the shell
pairs in (14), so there is no missing factor of `G` or `N'`.

For the Abel identity, `P_t=sum_(k<t)h_k=N_t` and
`R_s=sum_(k>=m+s)h_k=N'-N_(m+s)`.  Each rank increment has second coordinate
`1/L`, making `d_1=-C_m/L` with no cancellation.  Multiplying its squared
Schur lower bound by `NG/N'^2` gives exactly (21).

### 3.5 Positive envelope and unique atoms

The shell term in `I_m` begins with `1/(GN')`; AM--GM changes this to
`1/(4GN')`.  The normalized rank-one cross upper bound begins with
`1/N'^2`, hence becomes `1/(4N'^2)`.  The non-adjacent interval
`D_(i,j)=a_j-a_(i-1)` has rank lag `j-i+1>=2`.

Right endpoints lie in disjoint dyadic newborn blocks, and shell versus
cross atoms have disjoint left-endpoint ranges.  Thus the numerical atoms
are globally unique on a Golomb ruler.  The only artificial object is the
`i=0` row, which is separately bounded by `23/105` and is summable.

### 3.6 Adjacent-debt constant

Restoring both factors omitted from the unnormalized signed-square identity
gives `B_adj/(2GN')`, exactly as in (38e).  Substituting
`L=2m`, `tau<=3N'/2`, and `delta<=N'` gives

```text
B_adj/(2GN') <= (117/280) N'/(m^2 G).
```

The critical cap `N'<=K(2m)^2 log(2m)` and distinct positive shell gaps give

```text
B_adj/(2GN') <= (117K/35) log(2m)/m^2.
```

For `m=2^j`, `j>=1`, summation is exactly `(13/5)K log 2`.  If the cap is
only eventual, this proves a summable tail and leaves a finite initial
constant; it does not provide the missing non-adjacent-fan or Abel-fan
budget.

## 4. Survival-probe verdicts and quantifier hazards

The finite extension enumeration is correctly bounded: the next mark runs
through every integer satisfying `a_n+1 <= floor(2(n+1)^2 log(n+1))`, and
new differences are checked both internally and against all old
differences.  Therefore the reported depth-one and depth-two counts are
exact finite tree counts.  They are not evidence of an infinite branch.

The three main cardinality no-go conclusions replay exactly:

1. `(0,4,10,13,15,27,34,35)` refutes the certified rank-lag repayment and
   has 61,427 depth-two leaves;
2. `(0,3,7,13,21,22,33,38)` refutes global raw non-adjacent repayment and
   has 61,448 depth-two leaves;
3. `(0,2,5,6,14,25,32,42)` is old-clear/new-unpaid at `m=4`, has actual
   demand 3 but only 2 global and 1 latest-shell reservoir atoms, and has
   59,361 depth-two leaves.

### 4.1 The density label must be split into three propositions

The result note's table says GDQ "survives the bounded scopes," but its own
complete four-mark section records 601 negative GDQ events.  The exact
minimum witness is

```text
P=(0,1,4,6),  T=3,  U_global=0,
I_2=137/10976,
U_global/T-I_2=-137/10976.
```

This prefix obeys every `C=1` cap and has exact depth-two counts
`(1,67,4879)`.  It refutes the **literal per-epoch factor-one inequality**,
but it occurs at the first nontrivial epoch, where both actual sides are
paid.  It therefore does not refute an eventual statement which permits a
finite initial error and is restricted to old-clear/new-unpaid epochs.

The unrestricted scaled witness is a different and stronger local no-go in
the relevant renewal category.  For 100 times
`(0,8,24,56,58,314,318,319)`, the event is old-clear/new-unpaid and

```text
T=42449/2, U_global=5,
I_4=16828076637395/7660787849434944,
U_global/T-I_4
 = -637727146686430915/325192783420663937856.
```

Scaling preserves the Golomb property, but this ruler violates `C=1`.
Hence the **unconditional** local GDQ is refuted, while the critical-branch
version remains open.

### 4.2 New adversarial latest-shell counterexample

The terminal-`<=45` actual-renewal scope found no density failure, but that
finite observation does not extend through the full `C=1` range.  An exact
counterexample found in this audit is

```text
P=(0,4,5,7,78,86,166,199),  m=4.
```

It is Golomb and obeys every `C=1` prefix cap.  Exact values are

```text
tau_(4,1)=72, delta_4=80,
ancestry_cleared=True, new_family_paid=False,
outstanding demand=3,
U_global=1, U_latest=0,
I_4=5539453/1075200000.
```

Therefore

```text
U_latest/72-I_4 = -5539453/1075200000 < 0,
```

while the global density still wins by
`28181641/3225600000`.  The prefix has exact finite survival counts
`(1,121,16030)` through depth two.  Thus the latest-shell density candidate
is **REFUTED** even with `C=1`, a genuine outstanding family, and finite
depth-two survival.  The global version is not refuted by this witness.

### 4.3 Independent stress search of the remaining global version

To attack the remaining global candidate beyond the committed scopes, I
used deterministic sequential Golomb extensions within every `C=1` prefix
cap.

- Seed `8841191`: 30,000 eight-mark roots, including 3,222
  old-clear/new-unpaid `m=4` events.  No negative global margin occurred.
  The minimum was the witness above, with margin
  `28181641/3225600000`.
- Seed `8161191`: 4,000 sixteen-mark roots, including 142
  old-clear/new-unpaid `m=8` events.  No negative global margin occurred.
  The smallest audited global margin was
  `16385344064927/349281820446720`.
- Structured power-of-two gap permutations satisfying all `C=1` prefix
  caps (2,132 admissible eight-mark rulers) also produced no negative global
  event.

These are **FINITE-EVIDENCE** only.  They neither prove a universal local
inequality for `m>=4` nor address conditioning on infinite survival.

### 4.4 API scope caveat

`actual_renewal_comparison` sets `outstanding_demand=0` whenever the current
newborn family is paid.  That is history-correct at a both-paid event or when
no older debt exists, but not automatically at a **new-pay-only** event: an
older outstanding family may persist because ancestry was not cleared.

The certificate's actual-debt conclusions are unaffected, because it scores
only old-clear/new-unpaid rows, where older debt is cleared and the new debt
is exactly `m-1`.  Nevertheless, future callers must either reconstruct
`renewal_history` or restrict this helper to the old-clear/new-unpaid scope;
its returned debt field is not a universal local-state oracle.

## 5. Two no-go witnesses

The non-adjacent-bulk witness is exact.  For
`(0,8,24,56,58,314,318,319)`, deleting the sole positive non-adjacent bulk
interval leaves deficit

```text
1869979/6720 > 0.
```

Restoring it leaves surplus `41407/2240`, and division by `2G=526` gives
the shell energy `41407/1178240`.  Thus a proof using only adjacent assets
and the full shell span cannot work.

For the rank-one witness `(0,D,3D,3D+1)`, all six differences are distinct
for every integer `D>=2`.  The shell energy tends to `1/112`, while the
rank-one prefactor grows linearly.  Direct simplification confirms

```text
lim_(D->infinity) (1/D) <H,R_2>/<H,S_2> = 46/45.
```

This refutes every unconditional constant comparison.  It does not claim
that the family lies on a fixed critical infinite branch.

## 6. Final audit boundary

What Wave 8 has genuinely proved is substantial but local:

- the nested adjacent-set overcount is replaced by one-family renewal;
- signed shell energy is decomposed into exactly classified square atoms;
- adjacent endpoint debt is globally summable under the critical cap;
- the artificial boundary row is globally summable;
- non-adjacent bulk and the rank-one Abel fan are shown to be indispensable.

What remains unproved is precisely the hard part:

```text
on one infinite branch with surv_C=infinity,
sum_(j<=J) <H,Q_(m_j)/N_(2m_j)> = o(log J).
```

Neither pair uniqueness, the harmonic activation ledger, finite survival to
depth two, nor the surviving finite global-density experiments imply this
asymptotic statement.  The correct status is therefore
`UNRESOLVED_AT_HARD_LIMIT`, with the infinite survival-sensitive global
density/innovation bridge as the next target.

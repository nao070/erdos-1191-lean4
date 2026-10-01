# Erdős #1191 continuation — Wave 19 cross-ratio absorption and sparse-spike boundary

Date: 2026-08-29 (Asia/Tokyo)  
Status: `UNRESOLVED_AT_HARD_LIMIT`

This is the authoritative current continuation.  It preserves all earlier
identities, certificates, counterexamples, and claim boundaries.  Wave 19
proves two new coefficientwise absorptions, replaces the isolated positive
P23 target by a narrower signed target, retains certified rank slack to
obtain the dilation-invariant P25 remainder, removes its summable pairing
slack to obtain the sharper rank-free P26 remainder, decomposes that
remainder into nonnegative channels, proves the P26/P27 route is saturated by
an untouched inner-birth floor, identifies a linear obstruction
to the naive Fejér shift, and extends the finite nested spike witness through
512 marks.  It does **not** construct an infinite critical Sidon/Golomb
branch, complete P28, answer either Erdős question, establish publication
novelty, or support a prize claim.

## 1. Cross-ratio half absorption

For `n>=4`, write

```text
A=a_(2n-1),  d_(n,p)=D_(p,2n-1),
X_(n,p,q)=a_q d_(n,p)/(A D_(p,q)).
```

The exact rectangle telescope is

```text
log X_(n,p,q)=sum_(i=1)^(p-1) sum_(j=q+1)^(2n-1) C_(i,j).
```

At height `h=5/2`, the Wave 18 descendant functional splits as

```text
J_n^(h)<=E_n^(h)+S_n,
```

where `E` depends only on the endpoint ratios `A/a_q` and `S` is the
positive cross-ratio rectangle part.  An exact four-case coefficient audit,
with `x=n-i` and `y=j-n`, proves

```text
S_n<=(1/2)Y_n.
```

This holds for every strictly increasing real sequence.  The factor `1/2`
is coefficientwise sharp in the limit at `(i,j)=(n-1,n+1)`.

## 2. Endpoint overshoot is paid by the prefix deficit

Let

```text
lambda_(n,q)=sum_(p=2)^n alpha_(n,p) beta_(n,p,q),
c_(n,q)=(2q-1)/(4n^2),
Dpre_n=sum_(q=n)^(2n-2)c_(n,q)log(A/a_q).
```

The exact endpoint comparison is

```text
lambda_(n,q)<(3/4)c_(n,q).
```

The maximum ratio occurs at `q=n` and equals

```text
(12n^3-40n^2+29n+10)/(2(2n-3)(2n-1)^2),
```

whose positive gap from `3/4` is

```text
(20n^2-16n-29)/(4(2n-3)(2n-1)^2).
```

Consequently

```text
E_n^(5/2)<=(3/4)Dpre_n,
(mathfrak P_n-mathfrak F_n)+E_n^(5/2)
 <=-(1/4)Dpre_n+epsilon_n,
epsilon_n=((4n-3)/(16n^2))log A.
```

The `epsilon` tail is dyadically summable on one fixed eventual-`C` branch.
This step uses the uncontracted Wave 13 frontier spectrum.  It may not be
combined with a second expansion of the Wave 16 terminal potential, because
that would spend `mathfrak F_n` twice.

## 3. Exact signed frontier and P24

Keep the Wave 18 nonnegative remainders

```text
U_n^cap=D_n-Theta_(n/2)^[5/2],
Q_n=H_n^loc+J_n^(5/2)-Theta_n^(exc,5/2).
```

Then the sign-faithful Wave 19 inequality is

```text
Z_n <= (1/2)Y_n + G_n + epsilon_n
       -(U_n^cap+Q_n+mathfrak e_n),

G_n=mathfrak U_n-K_n^int
    -Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)
    -(1/4)Dpre_n.
```

Choose `k_0` after every fixed onset and put

```text
omega_(k,J)=((J+1-k)/(J+1))^2.
```

The decreasing-weight cut renewal gives

```text
(1/2)sum_(k=k0)^J omega_(k,J)Y_(2^k)
 <=O_(C,a,k0)(1)+sum_(k=k0)^J omega_(k,J)G_(2^k).
```

Wave 13 supplies the opposite bound

```text
(1/2)sum omega Y
 >=[1/(3072 C log2)]log J+O_(C,k0)(1).
```

Therefore the exact directly sufficient target is

```text
limsup_(J->infinity)
 [sum_(k=k0)^J omega_(k,J)G_(2^k)]/log J
 <1/(3072 C log2).
```

The cleaner stronger target is P24:

```text
sum_(k=k0)^J omega_(k,J)G_(2^k)=o_(C,a)(log J).
```

P24 is open.  To settle Question 1, it must hold for every `C` and every
fixed compatible infinite eventual-`C` integer Golomb branch.

## 4. Current-scale target and the linear mismatch obstruction

Put

```text
Ghat_(2^k)=mathfrak U_(2^k)-K_(2^k)^int
            -Theta_(2^k)^[5/2]-Theta_(2^k)^(exc,5/2)
            -(1/4)Dpre_(2^k).
```

Exact cap reindexing yields

```text
sum omega G <= sum omega Ghat +15/16.
```

Thus a sufficient next lemma is

```text
sum omega (Ghat_(2^k))_+=o_(C,a)(log J).
```

The pointwise statement `(Ghat_(2^k))_+=o_(C,a)(1/k)` or the block statement
`sum_(k=L)^(2L)(Ghat_(2^k))_+=o_(C,a)(1)` would be stronger sufficient
forms, not established facts.

The obvious one-step proof fails by a quantified leading term.  On the full
suffix range write `u=v+bar r`, including the exceptional last residual
`bar r_(n,2n-2)=3/(8n^2)`.  With

```text
delta_(k,J)=omega_(k,J)-omega_(k+1,J)
           =(2(J-k)+1)/(J+1)^2,
B_n^v=sum_(p=2)^(2n-2)v_(n,p)log d_(n,p),
```

the triangular rank floor and eventual cap give

```text
B_n^v=(1/2)log n+O_C(log log n),
sum_(k<J)delta_(k,J)B_(2^k)^v
 =(log2/6)J+O_C(log J).
```

The macroscopic half already contributes `(log2/8)J+O_C(log J)`.  Wave 14's
`Phi` rebate changes this only by a nonnegative `O_C(log J)` mismatch and
lives in a different lower-shell ledger from `K_n^int`.  Hence neither the
bounded Wave 15 `Delta` mismatch nor a raw terminal shift proves P24.  Section
5 retains the exact rank slack before this loss and replaces bare `Ghat` by a
dilation-invariant certified remainder.

## 5. Certified rank slack, P25, and the sharper P26 remainder

Sort all `c_n=(n-1)(3n-4)/2` Gothic interior differences increasingly as
`x_(n,j)` while carrying their actual coefficients `gamma_(n,j)`.  Then

```text
Srank_n=sum_j gamma_(n,j)log(x_(n,j)/j)>=0,
Pair_n=sum_j gamma_(n,j)log j-F_n^(loc,int)>=0,
H_n^loc=Srank_n+Pair_n.
```

The Wave 18 spent row is bounded by `Srank_n` alone: if an atom has sorted
rank `j`, then `j<=c_n`, `x_(n,j)>=j`, and `alpha<=1`.  Therefore

```text
Theta_n^(exc,5/2)<=Srank_n+J_n^(5/2),
Q_n^cert=Srank_n+J_n^(5/2)-Theta_n^(exc,5/2)>=0,
Q_n=Q_n^cert+Pair_n.
```

Retaining `Ucap`, `Qcert`, and `mathfrak e_n` instead of discarding them
gives the finite-prefix quantity

```text
Rcert_n=mathfrak U_n-F_n^(loc,int)-Srank_n-J_n^(5/2)
        -(1/4)Dpre_n-mathfrak e_n+epsilon_n
```

and the exact signed inequality

```text
Z_n<=(1/2)Y_n+Rcert_n.
```

The previous-source cap cancels exactly, so the `15/16` cap-shift error is no
longer needed.  Also

```text
Rcert_n=Z_n+(3/4)Dpre_n-J_n^(5/2)+Pair_n,
```

and `Rcert_n` is invariant under multiplying the entire ruler by any positive
integer.  This removes the fatal local dilation defect of bare `Ghat`.

The P25 target is

```text
sum_(k=k0)^J omega_(k,J)(Rcert_(2^k))_+=o_(C,a)(log J).
```

The exact weaker sufficient signed threshold remains
`1/(3072C log2)`.  A stronger uniform finite-window form would require
`sum_(k=L)^(2L)(Rcert_(2^k))_+=o_C(1)` over all sufficiently deep finite
Golomb prefixes satisfying the cap throughout the required window.  Neither
form is proved.

The pairing slack is itself universally tiny.  If `a=n-1` and
`c=(n-1)(3n-4)/2`, the exact three-level coefficient multiset and the reverse
rearrangement bound give

```text
0<=Pair_n<=[3/(4n^2)]log binom(c,a)
          <=[3/(4n)]log(3en/2).
```

Thus `sum_(k>=2)Pair_(2^k)<infinity`.  Keeping the actual Gothic bulk defines

```text
Rsharp_n=mathfrak U_n-mathfrak B_n-J_n^(5/2)
         -(1/4)Dpre_n-mathfrak e_n+epsilon_n
        =Z_n+(3/4)Dpre_n-J_n^(5/2),
Rcert_n=Rsharp_n+Pair_n.
```

Directly from the endpoint and cross-ratio bounds,

```text
Z_n<=(1/2)Y_n+Rsharp_n.
```

Hence P25 is equivalent up to a uniformly bounded dyadic error to the
rank-free target P26

```text
sum_(k=k0)^J omega_(k,J)(Rsharp_(2^k))_+=o_(C,a)(log J).
```

The same equivalence holds for the sharp signed threshold and the uniform
finite-window form because the corresponding `Pair` tail is `o(1)`.  P26 is
open.

There is one final same-scale sharpening.  Put

```text
Zfin_n=Z_n^ob+Z_n^nb,  Zfut_n=Z_n^of+Z_n^mf,
hstar_n=log(c_n/L_(n,n)),
Jstar_n=J_n^(hstar_n),
E0_n=sum_q lambda_(n,q)log(A/a_q).
```

An exact boundary-case audit strengthens `S_n<=(1/2)Y_n` to
`S_n<=Zfin_n`.  Also `Jstar_n<=E0_n+S_n`,
`E0_n<=(3/4)Dpre_n`, and `Jstar_n>=J_n^(5/2)`.  Therefore

```text
Rsharp_n=[(3/4)Dpre_n-E0_n]+[Zfin_n-S_n]
         +[E0_n+S_n-Jstar_n]+Zfut_n
         +[Jstar_n-J_n^(5/2)] >=0.
```

Thus the positive part in P26 is redundant.  The resulting P27 candidate was
the nonnegative packing theorem

```text
sum_(k=k0)^J omega_(k,J)Rsharp_(2^k)=o_(C,a)(log J).
```

However, a row-exact audit gives

```text
Rprof_n=Z_n+Erow_n-J_n^(5/2)
       =(Zfin_n-S_n)+Zfut_n+(S_n-Delta_n^abs)>=0,
Rsharp_n=Rprof_n+[(3/4)Dpre_n-Erow_n].
```

The cross rectangles have `i<=n-1`, so `Rprof` retains the full inner
new-birth sector with `i>=n`.  Reapplying the Wave 13 layered integer-gap
floor to that strict inner set proves, on every hypothetical eventual-`C`
branch,

```text
liminf [sum omega Rsharp]/log J >=1/(1536C log2).
```

This is twice the strict sufficient threshold `1/(3072C log2)`.  Hence the
P26/P27 little-o, sharp-threshold, and uniform-block forms are closed as
standalone intermediate targets, not proved.  The current open P28 design
obligation is to move this inner sector against the negative renewal cuts or
absorb it using a new disjoint descendant carrier.

A separate locally `C=32` prime Erdős--Turán append prefix at
each scale has `Rsharp_n>(39/256)log2`; hence pointwise smallness cannot follow
from same-scale facts.  The prefixes differ with `n`, so this is not a
compatible-branch counterexample.

A separate prime Erdős--Turán append family, scaled by
`floor(log(2n))`, satisfies the same-scale local `C=32` cap and proves

```text
Ghat_n>=(7/32)log floor(log(2n))
       -[1/4+(3/8)log64+(3/16)log4].
```

Different `n` use different prefixes.  Hence this does not refute P24 on a
compatible branch, but it rigorously rules out deriving the bare pointwise
or block `Ghat` bounds from same-scale Golomb, rank, and cap facts alone.

## 5A. P28 full-row and adaptive-cap boundary

The full-row audit separates an illegal allocation from the legal one.
Allocating the complete terminal coefficient `u_p` fails coefficientwise
from `n=6` onward (first dyadic failure `n=8`), and the worst ratio tends to
`9/8`.  It is also ownership-invalid because

```text
u_p=v_p+bar_r_p,
```

where `v_p` is already owned by the retained next negative cut.  The only
legal current descendant demand is `bar_r_p`.

The natural transport

```text
t0_(p,q)=(bar_r_p/w_p) beta_(p,q)
```

fits every full Gothic row and proves

```text
S_(t0)<=Y_n/2,
E_(t0)^rank<=3Dpre_n/4.
```

The half constant is asymptotically sharp at `C_(1,2n-1)`, and on the inner
`W_n` sector this transport leaves more than `W_n/2`.  Thus it does not
cross the old strict threshold.

For every row set

```text
h_(n,p)=max(3/2,log(c_n/L_(n,p))).
```

The actual cap is bounded by the deterministic profile,

```text
Theta_n^cap<=Cdet_n=sum_p bar_r_p h_(n,p),
Cdet_n<0.8336738101+0.3009853/n.
```

The displayed relationship is generally an inequality, not an equality.
With the source/target indices aligned correctly, Wave 17 gives

```text
D_N>Cdet_(N/2)>=Theta_(N/2)^cap  for every N>=2048.
```

Hence the adaptive cap capacity is paid.

Actual Gothic ranks do not remove the endpoint term.  For any feasible
transport, the correct bound is

```text
Theta_n^exc<=Srank_n+S_(t),n+E_(t),n^rank,
E_(t),n^rank=sum t_(p,q)[log(A/a_q)-sigma_(p,q)]_+.
```

The endpoint-free shortcut would require
`j_(p,q)<=exp(h_p)L_p a_q/A`, which is not proved.

Allowing an arbitrary energy-aware feasible transport does not eliminate
the inner residual.  For every dyadic `n>=64`,

```text
E_n^res(t)>=n^2/(2^25 H_n').
```

On any hypothetical eventual-`C` branch its Fejer liminf is at least
`1/(2^27 C log2)`.  The corner `C_(2n-4,2n-1)` has exact coverage ratio
`1/3` for every transport.  These are universal residual floors, not a
contradiction.

The verified mixed transport strengthens the endpoint without worsening the
cross coefficient.  Let `tR` fill each row from the right and put

```text
t=(8t0+tR)/9.
```

Row-prefix dominance gives `S_t<=S_(t0)<=Y_n/2`, while an exact all-column
calculation gives

```text
E_t^rank<=2Dpre_n/3.
```

Thus the current exact target is the stronger signed whole-cut functional

```text
Gmix_n=R_n+Pcoef_n log(A)-K_n^int-T_n-Theta_n^full-Dpre_n/3
      =Gold_n-Dpre_n/12.
```

After cap reindexing, a sufficient theorem is

```text
limsup [sum omega Gmix_(2^k)]/log J < 1/(3072 C log2),
```

or the clean stronger bound `sum omega (Gmix_(2^k))_+=o(log J)`.  This must be
proved from the intact whole-cut/terminal ledger.  Improving the transport
alone, extracting `v` while retaining its cut, or reusing a dropped
`D-cap+Q+Pair` bracket is forbidden.

The endpoint gain does not directly pay the inner residual.  The exact
eight-mark Golomb ruler

```text
(0,101,204,309,416,525,636,749)
```

at `n=4` satisfies

```text
W_4-S_t|W_4 > Dpre_4/12
```

with a fully rational logarithmic separation.  This refutes the unsigned
shortcut only; it does not refute a cut-corrected signed bound for `Gmix`.

## 6. Certified finite sparse-spike boundary

The Wave 19 sparse-spike certificate begins with the exact 32-mark Golomb
ruler

```text
(0,15,32,44,58,74,85,200,202,205,223,224,233,269,273,1418,
 1425,1431,1479,1514,1534,1571,1657,1696,1790,1798,1850,1912,
 1984,2047,2072,7096).
```

It joins a translated 95-mark scaled Erdős--Turán block

```text
b_j=7(346j+((63j^2) mod 173)),  0<=j<95,
```

to obtain a certified 127-mark union.  Appending either terminal `5,087,721`
or the reserve terminal `1,271,930` produces a 128-mark Golomb prefix obeying
every rational `C=32` prefix cap.  The primary row has
`J_64=0.3139371484...`; the reserve row has `J_64=0.0689106185...`.

For each resulting fixed 255-mark core, the exact largest legal 256th mark
under the cap is `23,258,158`.  The reserve branch then has

```text
J_128=0.3091860771777816204... .
```

A deterministic first-legal cooldown extends this fixed branch to 511
marks, ending at `24,032,260`.  It tests 774,102 candidates in total; each
chosen next mark is minimal for its then-fixed prefix, but alternative
branches were not searched.  For that fixed 511-mark core, the cap maximum
`104,661,718` is automatically legal because it lies above the exact
forbidden-shadow upper bound `48,064,520`.  The resulting 512-mark witness
has all `130,816` positive differences distinct, satisfies every `C=32`
prefix cap, and has

```text
J_256=0.005709533721666033398... .
```

Terminal maximality at stages 256 and 512 is exact for the fixed cores.  The
cooldown branch is not a globally exhaustive search.  The displayed `J`
values are 80-digit transcendental projections; all marks, differences,
caps, separation inequalities, and maximal-terminal statements are checked
with exact integer/rational arithmetic.

The general spike lower bound remains useful.  If the first `2n-1` marks
form a Golomb core of endpoint `H` and a legal terminal `X` is appended, then

```text
J_n^(h)>=[(n-1)(3n-5)/(8n^2)]
          [log((X-H)/(2 exp(h)H))]_+.
```

If `H=O(n^2)` and `X` is of order `n^2 log n`, this is
`(3/8)log log n+O(1)`.  Repeated spikes must be separated by at least

```text
n_(r+1)>=n_r sqrt((c/K)log n_r),
k_(r+1)-k_r>=(1/2)log_2 k_r+O(1),
```

to let the cap catch up.  This sparsity does not make the literal positive
P23 estimate plausible, but no infinite compatible spike/cooldown tower has
been constructed.  The finite witness therefore does not refute P23 or
either Erdős question.

## 7. Primary-literature boundary

The scripted Wave 19 literature state contains 345 deduplicated records and
10 manually verified Sidon/Golomb selections.  Six were read in full, one
has an explicit `paywall_no_oa` exception, and three are shallow records.
The closest exact finite energy source is Carter--Hunter--O'Bryant; the
closest qualitative birth construction is Cilleruelo--Nathanson.  Neither
controls birth delay, terminal atoms, or a nested fixed branch at the
critical scale.  Consensus supplied no evidence because its quota was
exhausted.  SciSpace supplied adjacent records but no matching theorem.

The resulting null is scoped to the audited corpus.  It is not a theorem of
nonexistence and not a novelty claim.  Martikainen's current v1 relevant
packing results are Theorems 1.3 and 1.11, correcting the earlier numbering.

## 8. Exact next work order

1. Attack the signed whole-cut P28 target `Gmix_n`, retaining every negative
   intermediate/terminal cut and the complete cap/rank/Pair bracket.
2. Search for exact cancellation or domination inside `Gmix_n`; transport-only
   optimization is now ruled out by the universal residual floor.
3. Reject any proposal that extracts `v` while retaining its cut, drops the
   actual-rank endpoint, or reuses a bracket already discarded as
   nonnegative.
4. Reject any proposal that merely upper-bounds `Rsharp`, `Rprof`, or their
   nonnegative channels; their harmonic lower floor already exceeds the
   sufficient threshold by a factor of two.
5. Test spike/cooldown branches against the proposed P28 carrier at repeated scales; finite
   repetition and separately chosen prefixes are discovery evidence only.
6. In parallel, investigate a rigorously compatible spike/cooldown induction;
   success would be a construction theorem rather than a P28 proof.
7. Before any solution or prize claim, obtain independent expert review and
   rerun a formula-level primary-source novelty search.

## 9. Primary Wave 19 artifacts

- `endpoint_variance/WAVE19_CROSS_RATIO_HALF_ABSORPTION_2026-08-29.md`
- `endpoint_variance/wave19_cross_ratio_half_absorption_certificate.py`
- `endpoint_variance/test_wave19_cross_ratio_half_absorption_certificate.py`
- `endpoint_variance/wave19_cross_ratio_half_absorption_certificate_2026-08-29.json`
- `endpoint_variance/WAVE19_CERTIFIED_RANK_SLACK_REMAINDER_2026-08-29.md`
- `endpoint_variance/WAVE19_SHARP_BULK_REMAINDER_AND_PAIR_SUMMABILITY_2026-08-29.md`
- `endpoint_variance/WAVE19_NONNEGATIVE_SHARP_REMAINDER_DECOMPOSITION_2026-08-29.md`
- `endpoint_variance/WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md`
- `endpoint_variance/WAVE19_P28_FULL_ROW_OWNERSHIP_AUDIT_2026-08-29.md`
- `endpoint_variance/wave19_p28_full_row_ownership_certificate.py`
- `endpoint_variance/test_wave19_p28_full_row_ownership_certificate.py`
- `endpoint_variance/wave19_p28_full_row_ownership_certificate_2026-08-29.json`
- `endpoint_variance/WAVE19_P28_ADAPTIVE_ROW_CAP_CANDIDATE_2026-08-29.md`
- `endpoint_variance/wave19_p28_adaptive_row_cap_certificate.py`
- `endpoint_variance/test_wave19_p28_adaptive_row_cap_certificate.py`
- `endpoint_variance/wave19_p28_adaptive_row_cap_certificate_2026-08-29.json`
- `endpoint_variance/WAVE19_P28_ARBITRARY_TRANSPORT_RESIDUAL_FLOOR_2026-08-29.md`
- `endpoint_variance/wave19_p28_transport_residual_floor_certificate.py`
- `endpoint_variance/test_wave19_p28_transport_residual_floor_certificate.py`
- `endpoint_variance/wave19_p28_transport_residual_floor_certificate_2026-08-29.json`
- `endpoint_variance/WAVE19_P28_MIXED_RIGHT_GREEDY_ENDPOINT_GAIN_2026-08-29.md`
- `endpoint_variance/wave19_p28_mixed_transport_certificate.py`
- `endpoint_variance/test_wave19_p28_mixed_transport_certificate.py`
- `endpoint_variance/wave19_p28_mixed_transport_certificate_2026-08-29.json`
- `endpoint_variance/wave19_certified_remainder_certificate.py`
- `endpoint_variance/test_wave19_certified_remainder_certificate.py`
- `endpoint_variance/wave19_certified_remainder_certificate_2026-08-29.json`
- `endpoint_variance/WAVE19_SPARSE_SPIKE_COOLDOWN_BOUNDARY_2026-08-29.md`
- `endpoint_variance/wave19_sparse_spike_certificate.py`
- `endpoint_variance/wave19_sparse_spike_search.py`
- `endpoint_variance/wave19_sparse_spike_test.py`
- `endpoint_variance/wave19_sparse_spike_certificate_2026-08-29.json`
- `../research_sources/wave19_literature_state/PRIMARY_SOURCE_AUDIT.md`
- `../research_sources/wave19_literature_state/RESEARCH_REPORT.md`
- `../research_sources/wave19_literature_state/research_state.json`

The finite certificates audit algebra, coefficients, integer constructions,
and deterministic replay.  They do not certify an asymptotic theorem, an
infinite branch, P24/P25/P26/P27/P28, Questions 1 or 2, publication novelty, or a prize
claim.

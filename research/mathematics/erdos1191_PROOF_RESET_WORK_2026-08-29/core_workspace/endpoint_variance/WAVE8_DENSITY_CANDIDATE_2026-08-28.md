# Wave 8 density candidate: exact refutations and the surviving repair

**Date:** 2026-08-28  
**Status:** the literal local factor-one inequality is **REFUTED**, including
inside the all-prefix `C=1` class.  The latest-shell version is also
**REFUTED** at a finitely extendable `m=4` renewal event.  A global statement
restricted to `m>=4`, and its cumulative finite-initial-error form, remain
**OPEN** with finite positive evidence only.  Nothing in this note proves an
infinite extension or resolves Erdős Problem #1191.

## 1. Candidate being tested

At a Wave 6 activation threshold `T=tau_(m,k)`, let `W_6(T)` be the selected
cross-antidiagonal endpoint pairs.  Among non-adjacent pairs in the history
`A_(2m)`, define

\[
 U_{\rm global}(T)=\#\{(i,j):j-i\ge2,\ a_j-a_i\le\lfloor T\rfloor\}
                     \setminus W_6(T).
\]

The proposed bridge was

\[
 \boxed{\frac{U_{\rm global}(T)}T\ \ge\
 I_m:=\left\langle H,\frac{Q_m}{N_{2m}}\right\rangle.}
 \tag{D1}
\]

`wave8_density_candidate_search.py` independently reconstructs the Wave 6
pairs, the actual unused differences, and `I_m` with exact `Fraction`
arithmetic.  It evaluates every activation of the newest complete dyadic
epoch.  No floating-point comparison decides any conclusion below.

## 2. Two decisive local refutations

### 2.1 `C=1` refutation at four marks

The normalized Golomb ruler

\[
 P=(0,1,4,6)
\]

obeys every `C=1` prefix cap.  At the first `m=2` activation,

\[
 T=3,\qquad U_{\rm global}(T)=0,\qquad
 I_2=\frac{137}{10976}>0.
\]

Consequently

\[
 \frac{U_{\rm global}(T)}T-I_2=-\frac{137}{10976}<0.
\]

This is not an isolated hand-picked calculation.  Exhausting all `1,672`
four-mark all-prefix-`C=1` Golomb rulers and both `m=2` activations gives
`3,344` exact events, of which `601` violate (D1).  The displayed ruler is
the minimum-margin witness.  It also has exact extension level counts
`(1,67,4879)` through depth two.  This is still only finite survival.
Therefore:

- **REFUTED:** (D1) as a universal inequality over every epoch of every
  finite all-prefix-`C=1` ruler (the witness is not known to lie on an
  infinite-survival branch);
- **REFUTED:** replacing the count by the low-difference square asset defined
  in Section 5, without allowing an initial error, because the reservoir is
  empty in the same `601` events.

### 2.2 The critical assumption cannot simply be deleted

Let

\[
 P=100(0,8,24,56,58,314,318,319).
\]

This is a Golomb ruler but violates the all-prefix critical cap.  At the
first `m=4` activation the exact audit is

\[
 T=\frac{42449}{2},\qquad U_{\rm global}(T)=5,
\]

\[
 I_4=\frac{16828076637395}{7660787849434944},
\]

and

\[
 \frac5T-I_4
 =-\frac{637727146686430915}
          {325192783420663937856}<0.
\]

Thus no unrestricted, scale-insensitive proof of the unweighted count
version is possible.

## 3. Latest-shell repayment is also false

The all-prefix-`C=1` ruler

\[
 P=(0,4,5,7,78,86,166,199)
\]

has a genuine old-clear/new-unpaid `m=4` event with

\[
 T=72,\qquad \delta_4=80,\qquad\text{outstanding demand}=3.
\]

At this threshold,

\[
 U_{\rm latest}(T)=0,
 \qquad I_4=\frac{5539453}{1075200000},
\]

so the latest-shell density margin is exactly `-5539453/1075200000`.
The global reservoir has one pair and still has positive margin
`28181641/3225600000`.  Exact extension enumeration gives level counts

\[
 (1,121,16030)
\]

through depth two.  This proves only finite extendability; it does not imply
`surv_1(P)=infinity`.

Hence a viable repair must remain **global across birth epochs**.  Restricting
the reservoir to the latest shell loses an essential old atom.

## 4. What survived at `m>=4` (finite evidence only)

No global factor-one failure was found in the retained deterministic
eight- and sixteen-mark searches.  Two exact near-side witnesses are:

| marks | witness | minimizing newest-epoch activation | `U_global` | `I_m` | exact margin |
|---:|---|---:|---:|---:|---:|
| 8 | `(0,2,3,8,79,128,161,234)` | `m=4,k=1,T=303/4` | 1 | `207413/35532000` | `26427287/3588732000` |
| 16 | `(0,3,18,27,34,84,94,200,261,317,437,473,512,690,743,1384)` | `m=8,k=8,T=14141/8` | 59 | `771145152181/82911515904000` | `28229471909696479/1172451746398464000` |

Both margins are positive.  Their exact finite extension counts are

\[
 (1,90,10838)\quad\text{through depth two at 8 marks},
\]

and

\[
 (1,193)\quad\text{through depth one at 16 marks}.
\]

The module also supplies a seeded full-cap generator and audits every newest
epoch activation of every generated ruler exactly.  The search is
deterministic and reproducible, but it is not exhaustive at 8 or 16 marks.
With the displayed default seeds, the retained scopes were:

- 8 marks: `5,001` unique rulers (the fixed adversarial seed plus `5,000`
  generated rulers), `20,004` activation events, zero negative global or
  low-square margins;
- 16 marks: `1,201` unique rulers, `9,608` activation events, zero negative
  global or low-square margins.

The correct label is therefore:

> **FINITE-EVIDENCE / OPEN:** (D1) restricted to `m>=4` on prefixes with
> finite `C=1` survival.

Finite survival conditioning does not repair the missing quantifier over one
infinite branch.

### 4.1 Long secondary fixture: all 510 events through `m=256`

A public working report described a perturbed Mian--Chowla construction but
did not supply a machine artifact.  The rule was independently reconstructed:

1. start with `b_0=0`;
2. take the least admissible Golomb mark through index `660`;
3. at index `661`, take the **third** admissible mark;
4. resume the least-admissible rule through index `681`.

The reconstruction exactly matches all three reported checkpoints:

\[
 b_{661}=4466351,\qquad b_{680}=4795424,\qquad b_{681}=4848816.
\]

It has `682` marks and all `232,221=binom(682,2)` positive differences are
unique.  The SHA-256 of the comma-separated decimal marks is

```text
523c509485873262cf5c51c4ee974a8a9cd5b89b46cec24f9ed59c1f05d57a60
```

The SHA-256 of all `510` exact event rows (epoch, antidiagonal, threshold,
reservoir count, innovation, count margin, and square margin, in canonical
pipe-delimited rational form) is

```text
470ac1e6ff85a2b65ff75ce3e10198b55814686b393a9b6adc394e728e3c4ff8
```

Using 60-digit `Decimal` logarithms, the reported working envelope

\[
 b_k\le k^2\log_2(2k)
\]

holds for every `1<=k<=680` and fails at `k=681`, again matching the report.
The density audit uses only prefixes through index `511` and tests every
newest-epoch activation for

\[
 m=2,4,8,16,32,64,128,256.
\]

There are `510` such events.  Exact shared-precompute arithmetic found zero
negative global margins and zero negative low-square margins.  The minimum
global margin occurs at `m=256,k=256`:

\[
 T=\frac{586977593}{256},\qquad U_{\rm global}=86368,
\]

\[
 I_{256}=
 \frac{5519259934588816529861353}
      {630054861249549663805112320},
\]

\[
 \frac{U_{\rm global}}T-I_{256}
 =\frac{10690962122092402001644475250899231}
        {369828085914209633994284050688245760}>0.
\]

This is a much longer **FINITE-EVIDENCE** audit, not a theorem.  Its
provenance is secondary (a reported algorithm reconstructed locally), the
working envelope itself fails at `681`, and no infinite branch is inferred.

## 5. Square weights: what is proved and what is not

The program also records the scale-matched exploratory asset

\[
 S_{\rm low}(T)=
 \sum_{(i,j)\in U_{\rm global}(T)}
 \left(\frac{a_j-a_i}{T}\right)^2.
 \tag{D2}
\]

Unlike `U/T`, this does not collapse under a common large scaling (apart from
the harmless artificial `+1` in the moduli).  It has positive margin on the
unrestricted scaling witness and on the retained `m=4,8` finite witnesses.
It still fails at `m=2` whenever the reservoir is empty, and there is no proof
that its `m>=4` version dominates `I_m`.

There is, however, a different **PROVED** square-weight statement already
available in `WAVE8_Q_ATOM_DECOMPOSITION_2026-08-28.md`, equation (25):
`I_m` is bounded by two positive, globally disjoint sums of actual
non-adjacent Golomb differences squared, plus a boundary term whose entire
dyadic-history sum is at most `92/315`.  That theorem is stronger
structurally than (D2), because it charges the actual kernel and mass
coefficients of `Q_m` rather than a uniform heuristic weight.

The remaining obstruction is directional.  Integer uniqueness gives

\[
 \#\{d\le T\}\le T
\]

and Wave 7 controls inverse activation thresholds.  The positive envelope
contains `d^2`, including atoms above a given `T`.  Replacing `d` by an upper
activation threshold makes an upper bound larger, not smaller.  Thus integer
capacity alone does **not** prove the required square-moment sum is
`o(log J)`.  This is the exact point at which the attractive square-weighted
repair remains open.

## 6. A weak critical-cap factor that is provable

There is one rigorous but asymptotically inadequate repair.  Write

\[
 A=N_m,\qquad G=N_{2m}-N_m,\qquad N'=A+G.
\]

For `m` positive weights of total mass `A`, the linear discrepancy is at
most `(m-1)A/m`; similarly the shell discrepancy is at most `(m-1)G/m`.
Therefore the first activation satisfies

\[
 \tau_{m,1}
 \le \frac{m-1}{m}(A+G)+\frac{\max(A,G)}m
 =N'-\frac{\min(A,G)}m<N'.
 \tag{D3}
\]

The exact secant kernel obeys `Phi<=4/3`.  If `r=G/N'`, the covariance pair
identity and Jensen's inequality give

\[
 I_m\le \frac{2r}{3}+\frac{4r(1-r)}3\le\frac34.
 \tag{D4}
\]

Let `K_(2m)=floor(2(2m)^2 log(2m))`, the exact `C=1` terminal modulus cap.
If, and only if, `U_global(tau_(m,1))>=1`, then (D3)--(D4) prove

\[
 \boxed{
 \frac{U_{\rm global}(\tau_{m,1})}{\tau_{m,1}}
 \ge \frac4{3K_{2m}}I_m.}
 \tag{D5}
\]

Under a corresponding general `C` cap the coefficient is of order
`1/(C m^2 log m)`.  This is **PROVED CONDITIONAL ON `U>=1`**, but it cannot
yield the target `o(log J)` estimate: its factor decays quadratically, and
the four-mark refutation shows that reservoir non-emptiness is not universal.

## 7. The only coherent cumulative repair

The exhaustive four-mark minimum shows that a single initial error

\[
 E_0=\frac{137}{10976}
\]

covers every `m=2` all-prefix-`C=1` deficit.  Hence a possible later theorem
would be

\[
 \sum_{2\le m_j\le m_J} I_{m_j}
 \le E_0+
 \sum_{2\le m_j\le m_J}
 \frac{U_{\rm global}(\tau_{m_j,1})}{\tau_{m_j,1}}.
 \tag{D6}
\]

The fixed eight- and sixteen-mark examples have positive exact corrected
margins, and equality holds for the four-mark counterexample after adding
`E_0`.  This is only **FINITE-EVIDENCE / OPEN**, because the local `m>=4`
inequality has not been proved.  Moreover, even (D6) would not finish P13:
the same global unused pair may be counted at more than one later threshold,
so a disjoint or bounded-overlap charge is still required to prove the
right-hand side is `o(log J)`.

## 8. Renewal-state correction

The actual-adjacent dichotomy has three possible state transitions:

| event type | older outstanding debt | current family | state afterward |
|---|---|---|---|
| both sides paid | cleared | paid | none |
| old-clear only | cleared | unpaid | current debt only |
| new-pay only | **retained** | paid | the same older debt |

A new-pay-only event cannot reset an older debt: `new_family_paid` certifies
only the current internal maximum, while `ancestry_cleared=false` says the
old maximum still exceeds the current threshold.  The executable transition
in `renewal_outstanding_transition` tests this truth table.  The dichotomy
still guarantees at most one adjacent family debt, but it does not guarantee
progress at a new-pay-only epoch.

## 9. Reproduction and exact status

From `core_workspace/endpoint_variance/`:

```bash
python wave8_density_candidate_search.py --trials8 5000 --trials16 1200
python -m pytest -q test_wave8_density_candidate_search.py
```

The default CLI reports exact rational strings and explicitly sets
`infinite_survival_inferred=false` and `erdos_1191_resolved=false`.  It also
adds `report_sha256`, computed from the canonical JSON payload before that
field is inserted.  The dedicated file has `13` deterministic tests covering
the two local refutations, exhaustive four-mark scope, fixed 8/16-mark
witnesses, finite extension counts, weak cap factor, renewal truth table,
fast/independent event equivalence, all 510 long-fixture rows, and the report
hash.

Final classification:

- **REFUTED:** literal local global factor-one bridge universally over all
  finite `C=1` prefixes and epochs;
- **REFUTED:** latest-shell factor-one bridge, even at a depth-two-extendable
  `m=4` old-clear/new-unpaid event;
- **PROVED:** weak cap factor (D5), conditional on a nonempty reservoir;
- **PROVED elsewhere in Wave 8:** positive globally disjoint square-atom
  envelope for the actual `Q_m`, with summable boundary term;
- **FINITE-EVIDENCE / OPEN:** global factor-one bridge for `m>=4`;
- **FINITE-EVIDENCE / OPEN:** cumulative initial-error bridge (D6);
- **OPEN HARD LIMIT:** turn the globally disjoint square atoms into an
  `o(log J)` budget on one infinite `surv_C=infinity` branch.

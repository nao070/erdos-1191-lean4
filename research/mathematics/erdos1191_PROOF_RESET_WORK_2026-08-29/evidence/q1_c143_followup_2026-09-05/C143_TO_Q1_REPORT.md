# C143 V2 restored state and the remaining Q1 obstruction

Date: 2026-09-05 (Asia/Tokyo).

**Q1 remains unresolved.** The primary current computational object is the
completed C143 V2 pilot in Downloads, not the older C139-era registry. This
follow-up recovers that object, derives additional exact consequences, and
isolates a rigorous obstruction to the proposed fixed-window global lift.

## 1. Primary data, identity and recoverable execution state

The authoritative input is

`/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/runs/pilot_s32_n16_r1/C143_BANK.json`

- Size: **144,369,995 bytes** (about 137.68 MiB).
- SHA-256: `d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4`.
- Payload SHA-256: `3961c6caa68c9d5dfbfbc0fdd2e433a1cf310618584ef617a892ce9b79a6725c`.
- Case: `n16-contract-s32-r1`; 64 integer marks, epochs 16 and 32,
  later weight 1, 196 channels, **19,110 graph roots**.
- All 2,016 positive differences of the 64 marks are distinct.
- Complete phase: `[2075/8,2075/4]`.
- **960 geometry parents, 1,890 parametric children, 961 collapsed endpoints**.

The parent checkpoint contains 743 `CERTIFIED_SUBINTERVAL` and 1,147
`CERTIFIED_FULL` records; their 1,890 child payloads equal the bank children
exactly. The endpoint checkpoint contains 961 `FULLROOT_ENDPOINT_CERTIFIED`
records, again identical to the bank. IDs are unique and both state files
have `pending: []`. All 28 run source hashes and all 79 package hashes
match. The saved configuration agrees with the bank's run metadata.

The run directory has seven files. It contains no saved oracle stdout,
`SUMMARY.json`, or `PILOT_CANONICAL_PASS.txt`. Shell history records V2 pilot
invocations, including `PYTHONINTMAXSTRDIGITS=0`, and attempts to sample the
parent/oracle processes. `/Users/USER/Desktop/c143_sample.txt` records
parent PID 53447, launched 2026-09-04 12:59:32 and sampled at 15:55:14 JST.
The named oracle and after-oracle sample files were absent. These traces
support execution activity; they do not recover the lost final result.
The user's report of completed full pricing is retained as such.

The new durable independent replay **passed**, exit 0, in 213.41 seconds:
**90,600,510 exact root-at-phase checks** (72,235,800 at child limits and
18,364,710 at collapsed endpoints). It reestablishes complete phase
coverage, every primal owner inequality, exact signed demands and physical
prices, dual feasibility over the complete root universe, primal-dual
equality, and every logarithmic integration record and aggregate.

The replay uses bounded signed-digit integer matrix products, with an
explicit int64 overflow bound followed by Python big-integer reconstruction;
no floating-point sign decision is trusted. An independent equivalence check
matched representative original Fraction/original integer oracle results,
including 38,220 original all-root sign checks. A separate all-bank primal
and margin replay passed in 105.90 seconds. All 11 adversarial rejection
checks passed, including malformed coverage/bases and unsafe integer
accumulation bounds. Evidence and exact commands are
in `C143_ORACLE_AUDIT.md` and `c143_full_pricing_replay.*`.

The original oracle omitted some semantic checks, including the child
margin-to-demand/price identity and exact child coverage. The new replay
checks those explicitly. This is a fresh strengthened independent replay,
not a recovered copy of the lost terminal output. No original Downloads
source or run artifact is changed.

### Surrounding checkpoints

The earlier C140 runner has durable canonical PASS and oracle outputs under
`/Users/USER/Downloads/C140_ALL563_MAC_RUNNER_2026-09-03/runs/canonical_20260903_012332/`:
563 generic chambers, 564 endpoints, 29,063 support roots, 98 negatively
integrated chambers, ranks 36--57. Those saved records were inspected here;
that historical C140 full run was not rerun in this follow-up.

C141 supplies the general same-M terminal vanishing theorem, with the exact
span hypothesis used below. C142's saved overnight summary records 358
tasks, 157 verified exact finite primal certificates, 92 stress candidates
and zero task errors. Its restricted-pool/phase-sampling failures were not
full-cone impossibility results. C143 refines six selected stress cases;
the completed run recovered here certifies specifically
`n16-contract-s32-r1`. It does not certify all six targets merely by having
finished every parent and endpoint of this pilot.

## 2. Stronger exact fixed-history result

The bank contains a stronger result than merely a positive signed integral.
Every child interval has strictly positive physical margin

\[
 M_1(t)=2D_1(t)-P_1(t).
\]

The exact minimum over all child interval limits and all separately
certified collapsed endpoints is

\[
 M_1(t)\ge\frac{18976473121}{3065610240}>6.1901.
\]

The minimum of the child-limit margin is attained at `t=2075/4`. The
separately optimized value at a collapsed endpoint can be larger because
zero-length cells have disappeared. The normalized lower bound is

\[
 \frac{M_1(t)}{t}\ge
 \frac{18976473121}{1590285312000}>0.01193.
\]

The correctly signed integral, with measure `dt/t²`, obeys the exact
outward rational fences

\[
 \boxed{0.04694333<\int_{2075/8}^{2075/4}M_1(t)\frac{dt}{t^2}
                     <0.04694335.}
\]

The stored rational lower and upper endpoints have decimal approximations
`0.046943338126180654` and `0.046943347894433531`; the enclosure width is
less than `9.77e-9`. The displayed short decimals above are deliberately
outward fences, not rounded endpoints presented as exact equalities.

### A continuum of Fejér weights, without another optimization

The same graphs remain feasible when the later epoch weight decreases from
1 to any `0<rho<=1`: for any signed demand `d`,
`max(rho*d,0)<=max(d,0)`. The earlier and past-owner inequalities are
unchanged. Writing the integrated later demand as `D_new(t)`, the transferred
margin is exactly

\[
 M_\rho(t)=M_1(t)-2(1-\rho)D_{\rm new}(t).
\]

An independent Haar-autocorrelation reconstruction agrees with every stored
child demand affine and all endpoint demand values. It proves, for the
entire rectangle of phases and weights,

\[
 \boxed{97/100\le\rho\le1\quad\Longrightarrow\quad
 M_\rho(t)\ge\frac{6975267967}{7664025600}>0.910.}
\]

Consequently the transferred signed integral is at least

\[
 \frac{6975267967}{3975713280000}>0.00175.
\]

This is a primal feasibility and positive-margin result for `rho<1`, not a
claim that the transferred graphs are still optimal. For the Fejér ratio
`rho=m²/(m+1)²`, it covers every `m>=66`. With the alternative variable
`s=J+1-k`, this means `s>=67`; the indexing must not be shifted silently.
The fixed tail length causes an asymptotically negligible excision cost
only once the complete baseline/global accounting is available.

Evidence: `c143_weight_extension.py`, `C143_WEIGHT_EXTENSION.json`, and
the independent `WEIGHT_EXTENSION_REVIEW.md`. No history or rank
quantifier is enlarged by this calculation.

## 3. Actual nonzero terminal and cutoff accounting

The pilot has

\[
 H_{\rm old}=76869,\qquad H_{\rm new}=4150.
\]

C141's general terminal-vanishing theorem applies to the new epoch on this
phase. Its span hypothesis fails for the old epoch. We reconstructed all
fourteen same-atom C133 rows over 458 exact integration pieces, rather than
assuming either terminal away. The new terminal is identically zero. The
old terminal changes sign, with spatially integrated phase values ranging
from `-691395/131072` to `671805/524288`. Its signed phase integral satisfies

\[
 -0.007017837969\le I_{\rm terminal,old}
                    \le-0.007017837968.
\]

At weight 1 the four shared prefix-band coefficients are zero; all four
keys are still retained. The fourteen rows sum coefficientwise to the
actual demand. This proves finite accounting, not that a global source
has paid each row.

There is also a lower-cutoff issue, even when an upper terminal vanishes.
For the box energy `Q_e(T)` and `b=2075/8`, direct derivation from the literal
C143 channel normalization gives

\[
 I_e:=\int_b^{2b}d_e(t)\frac{dt}{t^2}
 =W_e-\int_0^bQ_e+\int_b^{2b}Q_e
     -2\int_{16b}^{\infty}Q_e+\int_{32b}^{\infty}Q_e,
 \quad W_e=\int_0^\infty Q_e.
\]

The exact enclosed values, shown here as approximations, are:

| Quantity | Old epoch 16 | New epoch 32 |
|---|---:|---:|
| Complete `W_e` | 0.103342097372 | 0.122187283861 |
| Four-scale `I_e` | -0.007230289027 | 0.128883128028 |
| `I_e-W_e` | -0.110572386399 | 0.006695844168 |

The integrated graph price is approximately `0.19636233`. The diagnostic
comparison `2(W_old+W_new)-integrated_price` remains positive, approximately
`0.2546964`; these cutoff terms do not refute this fixture. Its significance
is that `I_e=W_e` would be a false identification, and the actual signed
adjustments must appear in any global argument.

Evidence: `c143_terminal_audit.py`, `C143_TERMINAL_LEDGER.json`,
`c143_cutoff_audit.py`, `C143_CUTOFF_AUDIT.json`, and the separate mathematical
review. Neither diagnostic subtraction is asserted to be a necessary
condition for every possible Route-C proof.

## 4. A rigorous obstruction to the simple global lift

Let `W_n` be the canonical positive cross-ratio sum with original weights
`alpha_ij=(j-i)²/(4n²)`, and let `W_n^(<=L)` retain only rank distances
`j-i<=L`. For every increasing integer ruler of shell span `H`,

\[
 W_n^{\le L}\le\frac{L(L+1)(2L+1)}{24n}\log H.
\]

For dyadic `n>=16`, the distinct-gap inner-birth floor gives
`W_n>=n²/(384H)`. On a fixed-`C` critical-cap tower this implies

\[
 \frac{W_n^{\le L}}{W_n}
 =O_C\!\left(\frac{L^3(\log n)^2}{n}\right).
\]

Thus **every fixed-size positive-window pasting scheme captures a vanishing
fraction of the original harmonic mass**, if each primitive is used at most
once at its original capacity. Even all 16-mark windows have `L<=14`.
C116's supply of linearly many good windows cannot close this gap by itself.
The same conclusion holds for slowly growing windows satisfying
`L³(log n)²/n -> 0`.

More sharply, for fixed `L` the dyadic contributions satisfy
`W_(2^k)^(<=L)=O_(C,L)(k/2^k)`. Their whole Fejér-weighted sum is **O(1)**,
whereas the full inner sector has **Ω(log J)** mass. The obstruction is a
loss of asymptotic order, not merely a weak finite numerical constant.

There is a second exact obstruction: a sum of matrices supported in windows
of at most `L+1` ranks has zero entries beyond rank distance `L`, whereas
the full direct matrix has `M_ij=1/(4n²)` for separated interior ranks.
Literal local matrix pasting therefore cannot reproduce the full matrix.

Both statements have proofs, with explicit hypotheses, in
`GLOBAL_OBSTRUCTION_ANALYSIS.md` and independent review in
`LOCALIZATION_REVIEW.md`. They rule out these particular lifts. They do not
rule out a new signed source, a genuinely long-range correction, or Q1.

## 5. The exact remaining theorem, and a less restrictive strategy

Q1 is equivalent to the following finite-tree assertion: for every fixed
integer `C>0` and fixed onset `m0`, some finite length admits no Sidon
sequence satisfying `a_m<=C m² log(2m)` at **every** rank from `m0` to that
length. König's lemma proves the equivalence; the fixed constants and all
intermediate-rank caps are essential.

A sufficient Route-C continuation is a single legal certificate for every
such capped finite tower, with uniform constants, which establishes both

\[
 0\le R_J=B_J-\sum_k\omega_{k,J}\Phi_k,\qquad B_J=O_C(1),
\]

and

\[
 \sum_k\omega_{k,J}\Phi_k\ge\epsilon_C\log J-O_C(1),
 \qquad\epsilon_C>0.
\]

The first formula must be an actual same-source identity and sign proof,
with all initial, birth, shared-owner, cutoff, final and terminal terms
accounted for once. It is not supplied by adding the local inequalities.
The second needs arbitrary-history and arbitrary-rank control. C115 already
supplies a signed shell-span telescope, but the required capacity estimate
and global identity remain unproved.

**An online optimizer is not logically required for this strategy.** A
certificate may depend on the entire finite tower and its horizon. Its
constants and boundary bounds must be uniform. Nonanticipation remains
necessary only when a particular martingale or causal argument actually
uses that hypothesis. This removes an unnecessary restriction from the
search without changing the target.

The next substantive object is therefore an arbitrary-rank, whole-tower
signed capacity/transport theorem with long-range interactions and complete
owned cutoff terms. More positive finite banks, by themselves, cannot
establish either displayed uniform assertion. The current C143 pilot is
retained as a fully specified test case for that theorem.

The primary-source literature check found no applicable resolution in the
papers inspected; its exact versions and access limits are documented in
`PRIMARY_SOURCE_AUDIT.md`. Global project status stays
`UNRESOLVED_AT_HARD_LIMIT`.

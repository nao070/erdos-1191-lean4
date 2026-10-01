# Wave 5: 64-mark nested extension and reset shell-overlap

## Outcome and scope

The saved Wave 4 certificate was authenticated and all four retained 32-mark
witnesses were used as beam roots.  Three 64-mark witnesses were retained for
each of the two objectives (six total); the leading retained witness for each
objective is displayed below.  Every retained ruler obeys the same `C=1`
envelope at **every** prefix:

\[
N_m=a_m-a_1+1\le 2m^2\log m,\qquad 2\le m\le64.
\]

The target 64 was reached for both objectives.  The extension search is
heuristic: beam width 128, at most 32 retained valid extensions per state,
127,104 accepted state expansions per objective.  There is no exhaustive or
optimality claim beyond the complete four-mark layer recorded in Wave 4.

## Signed reset profile

For the transition from `m` to `2m`, let the old gap weights be
`h_0,...,h_(m-1)` and the newborn shell weights be
`h_m,...,h_(2m-1)`.  Reset both halves to the same local rank grid and put

\[
p_r=\frac{h_r}{N_m},\qquad
q_r=\frac{h_{m+r}}{N_{2m}-N_m},\qquad
\delta^{(m)}_r=q_r-p_r\quad(0\le r<m).
\]

Thus `sum_r delta_r=0` exactly.  The certificate records the complete signed
cell vector, its cumulative profile

\[
D_m(s)=\sum_{r<s}\delta^{(m)}_r,
\]

and the earliest boundary, sign, and magnitude at which `|D_m|` is maximal.
This preserves where and in which direction a reset discrepancy occurs; it is
not only a scalar epsilon.

For consecutive epochs, coarsen the finer vector by adjacent pairs,

\[
\widetilde\delta^{(2m)}_r
=\delta^{(2m)}_{2r}+\delta^{(2m)}_{2r+1}.
\]

Let `A` be the sum of `min(|delta_r|,|tilde_delta_r|)` over cells with the
same nonzero sign, and `O` the corresponding sum over opposite signs.  The
exact signed shell-overlap statistic is

\[
P_m=\frac{A-O}
{\min(\|\delta^{(m)}\|_1,\|\widetilde\delta^{(2m)}\|_1)}\in[-1,1],
\]

with value zero if the denominator vanishes.

This \(P_m\) is a signed **shell-overlap statistic**: it compares separately
normalized old-versus-newborn gap discrepancies after coarsening consecutive
epoch grids.  It is not the exact chord-persistence identity for the diameter
profile, which instead says that subtracting the new endpoint chord leaves an
exact \(N_m/N_{2m}\) multiple of the old profile.  The two diagnostics address
different kinds of cross-epoch persistence.

## Best retained beam witness for shell-overlap persistence

Seed `501191`; descending objective order: latest normalized signed
shell-overlap, aligned mass, negative opposed mass, historical innovation
minimum, final innovation, and minimum dyadic gap variance, followed by the
lexicographic point tuple.

```text
(0, 1, 4, 6, 28, 36, 43, 81,
 102, 133, 143, 152, 166, 221, 297, 570,
 586, 599, 656, 690, 800, 826, 846, 893,
 918, 1081, 1317, 1588, 1939, 2314, 2840, 4094,
 4154, 4205, 4288, 4457, 4468, 4758, 4823, 5168,
 5323, 5335, 13902, 14642, 14737, 14754, 15036, 15125,
 15186, 15204, 20423, 20549, 22091, 22164, 23713, 23886,
 26270, 26679, 26903, 26947, 27075, 27320, 27360, 27562)
```

| `m` | `N_m` | exact `G_m` | exact `Q_(m/2),00/N_m` |
|---:|---:|---:|---:|
| 4 | 7 | `3/448` | `15/3584` |
| 8 | 82 | `120081/27541504` | `743151/192790528` |
| 16 | 571 | `58070349/10683711488` | `9008375897/1752128684032` |
| 32 | 4095 | `13110580663/2197949644800` | `28748230342177/5020116988723200` |
| 64 | 27563 | `4294792442795/1593246155276288` | `2044607601929603/815542875732049920` |

At the latest epoch,

\[
P_{16\text{-cell}\to32\text{-cell}}
=\frac{3215178426043}{4519699714530}
\approx0.7113699204.
\]

The final innovation is approximately `0.0025070510`.  All 2,016 positive
pair differences are distinct; their canonical list hash is
`b9a0ca3bcd89b2300f12b0de86df5cc5c74fc1a73eb397252ded66d888f1f517`.

## Best retained beam witness for innovation

Seed `502191`; descending objective order: the minimum innovation over all
five dyadic transitions, final innovation, latest shell-overlap, aligned mass,
negative opposed mass, and minimum dyadic gap variance, followed by the
lexicographic point tuple.

```text
(0, 1, 4, 6, 28, 36, 43, 81,
 102, 133, 143, 152, 166, 221, 297, 570,
 586, 599, 656, 690, 800, 826, 846, 893,
 918, 1081, 1317, 1588, 1939, 2314, 2840, 4094,
 4105, 4277, 4317, 4434, 4452, 4717, 4734, 5213,
 5471, 5642, 5852, 6065, 6144, 6226, 6459, 6913,
 7837, 8992, 10440, 12404, 14259, 16084, 19090, 22899,
 25301, 26786, 28159, 29390, 30549, 31711, 32878, 34067)
```

| `m` | `N_m` | exact `G_m` | exact `Q_(m/2),00/N_m` |
|---:|---:|---:|---:|
| 4 | 7 | `3/448` | `15/3584` |
| 8 | 82 | `120081/27541504` | `743151/192790528` |
| 16 | 571 | `58070349/10683711488` | `9008375897/1752128684032` |
| 32 | 4095 | `13110580663/2197949644800` | `28748230342177/5020116988723200` |
| 64 | 34068 | `76954273845347/19472117120630784` | `100987452359053759/26579439869661020160` |

Consequently,

\[
\min_{m\in\{4,8,16,32,64\}}Q_{m/2,00}/N_m
=\frac{100987452359053759}{26579439869661020160}
\approx0.0037994575,
\]

while the latest signed shell-overlap statistic remains

\[
P=\frac{25349788905953}{38483313318450}
\approx0.6587215788.
\]

Here `G_64≈0.0039520240`.  All 2,016 positive differences are distinct; the
canonical list hash is
`15f0e299cbf8a56b417ce7be829f3ef53144c6b11996de6702490adcc9fc7e0c`.

## Discrepancy location and sign across five epochs

Both displayed witnesses use the same authenticated Wave 4 parent and hence
share the first four rows.

| transition | max `|D|` | boundary | sign | shell-overlap `P` from prior epoch |
|---:|---:|---:|:---:|---:|
| 2 -> 4 | `1/10` | `1/2` | `+` | n/a |
| 4 -> 8 | `116/525` | `3/4` | `-` | `1` |
| 8 -> 16 | `7211/40098` | `5/8` | `-` | `1` |
| 16 -> 32 | `123009/1006102` | `15/16` | `+` | `1402802485/8777111367` (`≈0.159825`) |
| 32 -> 64, persistence witness | `17310907/24025365` | `25/32` | `+` | `3215178426043/4519699714530` (`≈0.711370`) |
| 32 -> 64, innovation witness | `20164318/40913145` | `13/16` | `+` | `25349788905953/38483313318450` (`≈0.658722`) |

This table exhibits information that a scalar discrepancy norm loses.  For
example, the extremal cumulative sign changes from positive to negative at
`4 -> 8`, even though the adjacent-pair-coarsened cell signs have exact
persistence `P=1`.  The latest epoch has both a positive extremum near the
right side and substantial same-sign persistence from the previous epoch.

## All-prefix envelope for the new half

The first 32 prefixes are the authenticated Wave 4 parent.  The table below
shows every newly added prefix.  The cap is the rigorously determined integer
`floor(2m^2 log m)`.

| `m` | cap | `N_m`, persistence witness | `N_m`, innovation witness |
|---:|---:|---:|---:|
| 33 | 7615 | 4155 | 4106 |
| 34 | 8152 | 4206 | 4278 |
| 35 | 8710 | 4289 | 4318 |
| 36 | 9288 | 4458 | 4435 |
| 37 | 9886 | 4469 | 4453 |
| 38 | 10505 | 4759 | 4718 |
| 39 | 11144 | 4824 | 4735 |
| 40 | 11804 | 5169 | 5214 |
| 41 | 12485 | 5324 | 5472 |
| 42 | 13186 | 5336 | 5643 |
| 43 | 13908 | 13903 | 5853 |
| 44 | 14652 | 14643 | 6066 |
| 45 | 15416 | 14738 | 6145 |
| 46 | 16202 | 14755 | 6227 |
| 47 | 17009 | 15037 | 6460 |
| 48 | 17838 | 15126 | 6914 |
| 49 | 18688 | 15187 | 7838 |
| 50 | 19560 | 15205 | 8993 |
| 51 | 20453 | 20424 | 10441 |
| 52 | 21368 | 20550 | 12405 |
| 53 | 22305 | 22092 | 14260 |
| 54 | 23263 | 22165 | 16085 |
| 55 | 24244 | 23714 | 19091 |
| 56 | 25247 | 23887 | 22900 |
| 57 | 26271 | 26271 | 25302 |
| 58 | 27318 | 26680 | 26787 |
| 59 | 28387 | 26904 | 28160 |
| 60 | 29479 | 26948 | 29391 |
| 61 | 30593 | 27076 | 30550 |
| 62 | 31729 | 27321 | 31712 |
| 63 | 32888 | 27361 | 32879 |
| 64 | 34069 | 27563 | 34068 |

The final independent audit checks all 63 prefixes, not only these displayed
new rows or the five dyadic checkpoints.

## Finite calibration and counterexample value

Under the recorded finite hypotheses—one nested Golomb ruler, the all-prefix
`C=1` envelope through 64 marks, and the five displayed dyadic
checkpoints—the innovation-priority witness simultaneously has

\[
\min Q_{00}/N>0.0037994,\qquad
\min G_m>0.0039520,
\]

and latest signed shell-overlap `P>0.6587`.  Thus those recorded finite
hypotheses do not force either a small innovation or a near-complete
shell-overlap reset within these five transitions.  The shell-overlap-priority
witness pushes the latest statistic above `0.7113`, at the cost of lowering
the last innovation to about `0.0025071`.

These are finite counterexamples only to bounded-depth claims whose hypotheses
are no stronger than the recorded finite ones and whose thresholds are below
the displayed values.  They suggest a shell-overlap/innovation tradeoff worth
testing at longer depths, but do not establish such a tradeoff as an
inequality.

## What this does not show

- The 64-mark rulers are not known to extend to 128 marks under `C=1`.
- No asymptotic lower bound for `G_m`, innovations, or the shell-overlap
  statistic is claimed.
- The results do not contradict an unbounded-history amortized budget such as
  `sum_(j<=J) G_j=o(log J)`.
- No value at 64 marks is claimed optimal; every post-Wave-4 extension is a
  beam-search observation.
- Nothing here resolves Erdős Problem #1191.

## Reproduction

```bash
cd /Users/USER/Documents/ChatGPT/mathematics/erdos1191_NEXT_SESSION_HANDOFF_2026-08-28/core_workspace/endpoint_variance
WAVE5_PYTHON=/tmp/erdos1191-wave4-pytest.KuCNgr/venv/bin/python
"$WAVE5_PYTHON" -m unittest wave5_nested_test.py
"$WAVE5_PYTHON" wave5_nested_certificate.py \
  --wave4-certificate wave4_nested_certificate_2026-08-28.json \
  --beam-width 128 \
  --candidates-per-state 32 \
  --retain 3 \
  --seeds 501191,502191 \
  --output wave5_nested_certificate_2026-08-28.json
```

The committed certificate records `retain=3`, runtime `CPython 3.13.13`, and
the SHA-256 manifest of its local executable dependency closure:

| source | SHA-256 |
|---|---|
| `wave5_nested_search.py` | `3b3aa024713c911f7dce45e884904f15a0bce726e1e513b0f7c159b0f80e10ad` |
| `wave5_nested_certificate.py` | `6d1176c061ddbfacef230ee049f6f676c3bcf914ba2b641caef239d4c2870162` |
| `wave4_nested_search.py` | `04856da051fd5d39c73d3eeba1210bdc13bc4fb020b2466f40178b7f9131aa56` |
| `gap_measure_dynamics.py` | `86f6e3bdba9aa12d5e456f8208ab0468b9462a3c7866d104aa68d2cfef29f095` |
| `sidon_block_variance.py` | `b9090db7dd32d031b2a0b79667cd7763a62c76982026909fd5b178bf1481ecbb` |
| `endpoint_variance.py` | `ac4e0d5d67c5acfa57770f0cab2b13ee48d56be1c8d2294eb346dfffea66519a` |

Canonical byte identity is asserted only for that recorded Python runtime;
exact rational fields, rather than float-derived decimal projections, are
hash-bearing.

The Wave 5 canonical certificate hash is
`a26c13574002eb442731bcbec465a5fa7553a25728e2225ddba942e6df4d3ceb`.
The authenticated Wave 4 parent-certificate hash is
`36437444becc16c7520d0abe4c825dae13e9f7a01dbdaf9e30aa50ffe6fda81b`.

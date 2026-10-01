# Wave 11 continuation: triangular Abel repayment and the secondary survival frontier

Date: 2026-08-29  
Research status: **UNRESOLVED_AT_HARD_LIMIT**  
Claim boundary: **P17 is open; P15 is open; Erdős Problem #1191 is open; no prize claim is ready.**

## Abstract

Wave 11 removes the leading obstruction left by the Wave 10 weighted Abel
spectrum.  If

\[
0=a_0<a_1<a_2<\cdots,
\qquad h_r=a_r-a_{r-1},
\qquad D_{p,q}=a_q-a_{p-1}=\sum_{r=p}^q h_r
\]

is a Golomb ruler, then the adjacent gaps are pairwise distinct positive
integers.  Every interval containing `ell` gaps therefore satisfies the
unconditional triangular floor

\[
D_{p,q}\geq 1+2+\cdots+\ell=\binom{\ell+1}{2}.
\]

Inserted into the exact dyadic Abel coefficients, this gives

\[
K_J^{\rm len}=2\sum_{m\in E_J}\log m+O(|E_J|),
\]

which repays exactly the leading quarter missing from the Wave 10 floor
`F_E=(7/4) sum log m+O(|E|)`.  The exact residual identity becomes

\[
\sum_{m\in E_J}Y_m
=(T_J-K_J^{\rm len})-(G_J^{\rm len}+S_J),
\qquad G_J^{\rm len},S_J\geq0.
\]

On one fixed infinite eventually `C`-critical branch this improves the
available upper envelope from order `J^2` to `O_C(J log J)`.  It does not
give the required `o(log J)`.  Exact finite computation, a positive
future-tail identity, and a multi-provider primary-source audit isolate the
remaining burden as a genuinely survival-conditioned secondary repayment;
none closes it.

Evidence labels below use only the authoritative vocabulary from
`00_START_HERE_PROMPT.txt`.  In particular, `[RIGOROUS — SELF-CONTAINED]`
marks a proof in the project text, `[CONDITIONAL]` preserves an explicit
infinite-branch hypothesis, `[COMPUTATIONAL — CERTIFIED FINITE]` never implies
infinitude, `[REFUTED]` has only its stated mechanism scope,
`[LITERATURE STATUS — PUBLIC RECORD ONLY]` is a qualified search disposition,
and `[BLOCKED]` marks an unproved obligation.

## 1. Exact dyadic state

Fix a dyadic `m>=4` and write

\[
n=2m,\qquad g=2m-1,\qquad
w_r={r^2\over4m^2},\qquad
\theta_m=w_{g-1}=\left({m-1\over m}\right)^2.
\]

For `j-i>=2`, define the positive cross-ratio atom

\[
C_{ij}=\log{D_{i,j-1}D_{i+1,j}\over
                  D_{i+1,j-1}D_{i,j}}>0
\]

and the shell

\[
Y_m=\sum_{j=m}^{2m-1}\sum_{i=1}^{j-2}
       \left({j-i\over2m}\right)^2C_{ij}.
\]

Let

\[
\mathcal I_m={(p,q):2\leq p\leq q,\ m-1\leq q\leq2m-2\}.
\]

For `ell=q-p+1`, the negative-bulk coefficient is exactly

\[
4m^2\beta_m(p,q)=
\begin{cases}
4,&q=m-1,\ \ell=1,\\
2\ell+1,&q=m-1,\ \ell\geq2,\\
4,&q\geq m,\ \ell=1,\\
1,&q\geq m,\ \ell=2,\\
2,&q\geq m,\ \ell\geq3.
\end{cases}
\]

Define

\[
A_m=\sum_{(p,q)\in\mathcal I_m}\beta_m(p,q)\log D_{p,q},
\qquad T_m=\theta_m\log D_{1,2m-1}.
\]

The positive fan is

\[
\begin{aligned}
Q_m={}&w_{m-1}\log D_{1,m-1}
+\sum_{q=m}^{2m-2}(w_q-w_{q-1})\log D_{1,q}\\
&+w_2\log D_{2m-2,2m-1}
+\sum_{\ell=3}^{2m-2}(w_\ell-w_{\ell-1})
 \log D_{2m-\ell,2m-1}.
\end{aligned}
\]

The upper endpoints here are exact: the first sum ends at `2m-2`, and the
suffix of length `ell` begins at `2m-ell`.

**[RIGOROUS — SELF-CONTAINED]** Abel summation gives the exact identity

\[
\boxed{Y_m=Q_m-T_m-A_m.}
\tag{1}
\]

The two boundary-fan coefficient families each have mass `theta_m`.  Hence

\[
S_m:=2T_m-Q_m
=\sum c^L_{m,q}\log{D_{1,2m-1}\over D_{1,q}}
 +\sum c^R_{m,\ell}\log{D_{1,2m-1}\over D_{2m-\ell,2m-1}}
\geq0.
\tag{2}
\]

For `E_J={4,8,...,2^J}`, quantities with subscript `J` denote sums over
`m in E_J`.  If `F_{E_J}` is the Wave 10 floor obtained by decreasingly
sorting all `beta` coefficients against `log 1,log 2,...`, then

\[
P_J=A_J-F_{E_J},\qquad S_J=2T_J-Q_J,\qquad
U_{E_J}=T_J-F_{E_J},
\]

and

\[
\boxed{\sum_{m\in E_J}Y_m=U_{E_J}-P_J-S_J=T_J-A_J-S_J.}
\tag{3}
\]

## 2. Triangular interval theorem and repayment of the leading quarter

### Theorem 1: triangular interval floor

**[RIGOROUS — SELF-CONTAINED]** For every interval of `ell=q-p+1` adjacent
gaps,

\[
\boxed{D_{p,q}\geq L_\ell:=\binom{\ell+1}{2}.}
\tag{4}
\]

**Proof.** Each `h_r` is itself a positive difference of the Golomb ruler.
The Golomb property makes the `ell` gaps in the interval pairwise distinct
positive integers.  Their sum is therefore at least the sum of the `ell`
smallest positive integers.  This proves (4).  No critical cap, asymptotic
argument, or infinite extension is used. `□`

Define the all-length floor and its nonnegative premium by

\[
K_m^{\rm len}
=\sum_{(p,q)\in\mathcal I_m}\beta_m(p,q)\log L_{q-p+1},
\]

\[
G_m^{\rm len}=A_m-K_m^{\rm len}
=\sum_{(p,q)\in\mathcal I_m}\beta_m(p,q)
  \log{D_{p,q}\over L_{q-p+1}}\geq0.
\tag{5}
\]

Combining (1), (2), and (5) yields the strongest exact local form obtained
in Wave 11.

### Theorem 2: exact nonnegative three-channel identity

**[RIGOROUS — SELF-CONTAINED]**

\[
\boxed{
H_m^{\rm len}:=T_m-K_m^{\rm len}
=Y_m+G_m^{\rm len}+S_m,
\qquad Y_m,G_m^{\rm len},S_m\geq0.}
\tag{6}
\]

Consequently,

\[
\boxed{
\sum_{m\in E_J}Y_m
=(T_J-K_J^{\rm len})-(G_J^{\rm len}+S_J).}
\tag{7}
\]

This allocation is termwise and canonical: each interval pays with its own
`log(D/L_ell)`.  It does not reuse a fan or a globally sorted rank.

### Theorem 3: exact asymptotic size of the new floor

On the lower shell `q=m-1`, the exact floor is

\[
K_m^{\rm low}
={1\over4m^2}
 \left(4\log L_1+
 \sum_{\ell=2}^{m-2}(2\ell+1)\log L_\ell\right),
\tag{8}
\]

whose coefficient mass is exactly `(m-1)^2/(4m^2)`.  For the interior
`m<=q<=2m-2`, the number of intervals of length `ell>=3` is

\[
N_m(\ell)=
\begin{cases}
m-1,&3\leq\ell\leq m-1,\\
2m-\ell-2,&m\leq\ell\leq2m-3,
\end{cases}
\]

and

\[
K_m^{\rm int}
={1\over4m^2}\left((m-1)\log3
+2\sum_{\ell=3}^{2m-3}N_m(\ell)\log L_\ell\right).
\tag{9}
\]

**[RIGOROUS — SELF-CONTAINED]** Writing
`log L_ell=2 log m+log((ell/m)(ell/m+1/m)/2)`, equations (8)--(9) are bounded
Riemann sums; their only endpoint singularities are integrable multiples of
`|log x|` or `x|log x|`.  Their principal coefficient masses are
`1/4+O(1/m)` and `3/4+O(1/m)`.  Therefore

\[
\boxed{
K_m^{\rm low}={1\over2}\log m+O(1),\qquad
K_m^{\rm int}={3\over2}\log m+O(1),}
\tag{10}
\]

uniformly for `m>=4`, and

\[
\boxed{K_J^{\rm len}=2\sum_{m\in E_J}\log m+O(|E_J|).}
\tag{11}
\]

Wave 10 proved

\[
F_{E_J}={7\over4}\sum_{m\in E_J}\log m+O(|E_J|).
\]

Thus

\[
\boxed{
K_J^{\rm len}-F_{E_J}
={1\over4}\sum_{m\in E_J}\log m+O(|E_J|).}
\tag{12}
\]

For consecutive dyadic epochs, the leading term on the right is
`(log 2)J^2/8+O(J)`.  Equation (12) is the rigorous repayment of the entire
leading quarter absent from the plain Wave 10 spectrum.

### Independent mixed certificate

There is a second, disjoint certificate.  Apply (4) only to the lower shell,
delete those atoms, and globally rearrange only the remaining `q>=m`
interior coefficients.  With the latter floor denoted `F_J^int`,

\[
K_J^{\rm mix}:=K_J^{{\rm len},{\rm low}}+F_J^{\rm int}\leq A_J,
\]

\[
F_J^{\rm int}={3\over2}\sum_{m\in E_J}\log m+O(|E_J|),
\qquad
K_J^{\rm mix}=2\sum_{m\in E_J}\log m+O(|E_J|).
\tag{13}
\]

The all-length and mixed certificates must not be added.  The safe
stronger-of-two choice is

\[
K_J^\star=\max\{K_J^{\rm len},K_J^{\rm mix}\}\leq A_J,
\]

with the exact residual identity

\[
\sum Y_m=(T_J-K_J^\star)-((A_J-K_J^\star)+S_J).
\tag{14}
\]

The audited values have `K_J^mix>K_J^len` for `2<=J<=9`; that finite
comparison is not promoted to an all-horizon ordering theorem.

## 3. Numerical ranks, holes, and the exact premium decomposition

The dyadic right-end bands tile the complete triangle

\[
\mathcal B_J
=\bigcup_{m\in E_J}\mathcal I_m
=\{(p,q):2\leq p\leq q,\ 3\leq q\leq2^{J+1}-2\}.
\tag{15}
\]

The bands `[3,6],[7,14],...,[2^J-1,2^(J+1)-2]` are disjoint and consecutive,
so every bulk interval appears once.  Order their distinct numerical values
as `d_1<...<d_M` and let `gamma_r` be the coefficient attached to `d_r`.
If `beta_r^down` is the decreasing rearrangement of the same coefficients,
define

\[
H_J^{\rm num}=\sum_r\gamma_r\log{d_r\over r},
\qquad
H_J^{\rm perm}=\sum_r\gamma_r\log r
-\sum_r\beta_r^\downarrow\log r.
\]

**[RIGOROUS — SELF-CONTAINED]** Since `d_r>=r`, and decreasing
weights minimize their pairing with increasing `log r`,

\[
\boxed{P_J=H_J^{\rm num}+H_J^{\rm perm},
\qquad H_J^{\rm num},H_J^{\rm perm}\geq0.}
\tag{16}
\]

For an interval of length `ell`, set

\[
\tau(p,q)=\binom{\ell+1}{2}-{\bf1}_{\{p=2\}}.
\]

All proper contained subintervals are strictly smaller differences; the whole
interval supplies the rank endpoint.  All lie in `B_J` except `[2,2]` when
`p=2`.  Hence its rank obeys
`r_J(p,q)>=tau(p,q)`.  With

\[
K_J^{\rm rank}=\sum\beta_m(p,q)\log\tau(p,q),
\quad
C_J^{\rm rank}=\sum_r\gamma_r
 \log{r\over\tau(p_r,q_r)}\geq0,
\]

one obtains the exact finer decomposition

\[
\boxed{
A_J=K_J^{\rm rank}+C_J^{\rm rank}+H_J^{\rm num},}
\tag{17}
\]

\[
\boxed{
\sum Y_m=(T_J-K_J^{\rm rank})
 -(C_J^{\rm rank}+H_J^{\rm num}+S_J).}
\tag{18}
\]

Only intervals with `p=2` distinguish `K^len` from `K^rank`, and their total
difference is `O(m^-3)` in one epoch.  The rank and length floors therefore
have the same asymptotic repayment, while `K^len` is slightly stronger and
needs no numerical-rank allocation.

## 4. Conditional improvement and the exact open target

From (7), universally for every finite prefix,

\[
0\leq\sum_{m\in E_J}Y_m\leq T_J-K_J^{\rm len}.
\tag{19}
\]

**[CONDITIONAL]** Suppose all prefixes come from one
fixed infinite Golomb branch that is eventually `C`-critical.  The critical
cap gives

\[
\log a_{2m-1}\leq2\log m+\log\log(4m)+O_C(1).
\]

Using `theta_m=1+O(1/m)` and (10),

\[
\boxed{
0\leq\sum_{m\in E_J}Y_m
\leq T_J-K_J^{\rm len}=O_C(J\log J).}
\tag{20}
\]

This is a genuine order improvement over the Wave 10 displayed certificate,
whose unfilled leading quarter was `Theta(J^2)`.  It remains far larger than
`o(log J)`.

Let

\[
\mathcal D_J:=G_J^{\rm len}+S_J.
\]

Then the exact surviving P17 obligation is

\[
\boxed{
\mathcal D_J\geq T_J-K_J^{\rm len}-\epsilon_J,
\qquad \epsilon_J=o(\log J),}
\tag{21}
\]

on that same fixed infinite eventually critical branch.  By (7), this is
equivalent to

\[
\sum_{m\in E_J}Y_m=o(\log J).
\tag{22}
\]

**[BLOCKED]** Neither (21) nor (22) is proved.  The leading-quarter theorem does
not establish survival, eventual criticality, or a sublogarithmic shell sum.

## 5. Exact future-tail identity and the obstruction to same-atom charging

Fix one epoch, let `A=a_(m-1)`, and put

\[
x_\ell=D_{m-\ell,m-1},\qquad1\leq\ell\leq m-2.
\]

The lower coefficients are

\[
\gamma_1={1\over m^2},\qquad
\gamma_\ell={2\ell+1\over4m^2}\quad(2\leq\ell\leq m-2),
\]

and their mass is exactly `w_(m-1)`.  Thus the lower boundary minus the
lower shell is

\[
\mathcal R_m^{\rm low}
=w_{m-1}\log A-\sum_{\ell=1}^{m-2}\gamma_\ell\log x_\ell\geq0.
\]

A second Abel summation gives

\[
\boxed{
\mathcal R_m^{\rm low}
=w_{m-1}\log{A\over x_{m-2}}
+\sum_{\ell=1}^{m-3}w_{\ell+1}
 \log{x_{\ell+1}\over x_\ell}.}
\tag{23}
\]

On an infinite branch, define

\[
f_{m,i}(t)=
\log{a_{m-1}-a_{i-1}+t\over a_{m-1}-a_i+t}.
\]

For `j>=m` and `t_j=a_j-a_(m-1)`, direct substitution gives
`C_ij=f_(m,i)(t_(j-1))-f_(m,i)(t_j)`.  Since `f_(m,i)(t_j)` decreases to
zero,

\[
f_{m,i}(0)=\sum_{j=m}^{\infty}C_{ij}.
\]

Matching this telescope with (23) proves the exact positive future-tail
identity

\[
\boxed{
\mathcal R_m^{\rm low}
=\sum_{i=1}^{m-2}\left({m-i\over2m}\right)^2
 \sum_{j=m}^{\infty}C_{ij}.}
\tag{24}
\]

Across dyadic epochs,

\[
\sum_{m\in E_J}\mathcal R_m^{\rm low}
=\sum_{i<j}\Omega_J(i,j)C_{ij},
\]

\[
\Omega_J(i,j)=
\sum_{\substack{m\in E_J\\i+2\leq m\leq j}}
\left({m-i\over2m}\right)^2.
\tag{25}
\]

For long-separated pairs this coefficient is
`Theta(1+log_2(j/i))`, up to the horizon cutoff.

**[REFUTED]** A fixed pair's coefficient in its single birth
shell is bounded below and above by constants when `i<=j/2`, whereas (25) is
unbounded as `j/i` grows.  Therefore the whole future tail cannot be charged
term by term, with one uniform constant, to that pair's single birth atom.
This does not refute a collective inequality using other pairs, endpoint
profiles, or the condition `surv_C=infinity`.

## 6. Exact finite computation and its boundary

The Wave 11 probe represents every logarithmic expression as a canonical
formal sum `sum_d c_d log d` with rational `c_d`.  Equality is checked with
`fractions.Fraction`; exhaustive sign checks clear rational exponents and
compare integers.  Floating values are labelled projections used only to
rank or display finite margins.

**[COMPUTATIONAL — CERTIFIED FINITE]** The certificate verifies:

- `U-P-S=sum Y` and `P=H^num+H^perm` exactly on every audited row (the raw
  probe fields use the aliases `H:=H^num` and `R:=H^perm`);
- the finite-horizon form of (24), including its nonnegative terminal ratio;
- the triangular lower floor, the disjoint mixed floor, and the exact
  strengthened residual;
- 1,468 normalized eight-mark Golomb rulers with terminal mark at most 40,
  including the complete 1,146-ruler subfamily satisfying every `C=1`
  prefix cap;
- the Wave 6 Hall counterexample, six authenticated 64-mark fixtures, one
  authenticated 128-mark continuation, a deterministic 512-mark
  Erdős--Turán ruler, and a reconstructed 682-mark modified-greedy fixture
  audited through its complete 512-mark prefix.

In the exhaustive 1,146-ruler `C=1` family, each literal candidate
`P>=U`, `S>=U`, `H^num>=U`, lower-hole-quarter, and `P+S>=U` fails on all 1,146
rulers.  Their minimum-terminal then lexicographic witness is

```text
(0,1,4,9,15,22,32,34)
```

The normalized-harmonic candidate has no bounded failure; its minimum exact
positive margin is `0.2103363225...`.  This observation is not a theorem and,
even when combined with (20), reaches only an `O(log J)` scale rather than
`o(log J)`.  The largest observed `sum Y` is `0.4116926365...`; the largest
observed `Y/U` is `0.3309272266...`, both at
`(0,3,14,22,23,27,29,39)`.

The last-epoch fractions of the exact lower residual consumed in one new
block include `0.614729` for the 512-mark Erdős--Turán fixture and `0.882481`
for the modified-greedy fixture audited through 512 marks.  Thus a single
future block need not consume nearly all of the tail.

**[COMPUTATIONAL — CERTIFIED FINITE]** Changing Erdős--Turán
windows at `m=16,...,1024` have
`Y_m/(T_m-K_m^mix)` increasing from `0.121183` to `0.126889`.  The analytic
construction is separate from this finite observation.

**[RIGOROUS — MODULO NAMED THEOREM]** For the same changing family, the
explicit interval comparison proves `G_m^len+S_m=O(1)`.  Combining this with
the positive absolute lower calibration for the retained cross-ratio state
proved in the named Wave 9 Carleson analysis gives a nonvanishing local shell
along the changing family.  This refutes pointwise vanishing derived only from
a terminal finite critical window or the triangular floor.  The prime and
ruler change with `m`, so it is not an infinite-branch counterexample.

The certificate explicitly records:

```text
finite_computation_only = true
infinite_survival_inferred = false
p16_proved = false
p15_proved = false
erdos_1191_resolved = false
```

The raw certificate was sealed before the canonical ledger split P17 out of
the broader P16 umbrella.  Its `p16_proved=false` field and P16 wording are
retained for byte reproducibility; the exact remaining Route A statement is
P17 in Section 5.  No `p17=true` inference is made.

## 7. Primary literature and plugin boundary

**[LITERATURE STATUS — PUBLIC RECORD ONLY]** The checked primary literature
supplies useful method templates but no black-box theorem proving (21), (22),
or the separate Route B alternative.  No equivalence between Routes A and B
is claimed.  The conclusion is restricted to the logged queries and verified
pages.

The most relevant checked consequences are:

- Beck--Bogart--Pham supply the positive gap-vector formulation, not a
  logarithmic product estimate.  Within one fixed length class, numerical
  distinctness gives
  `D_(r)>=L_ell+r-1`, hence a shifted-factorial product floor.  Its gain over
  the termwise triangular floor is only `O(m^-1/2)` per shell and is summable
  over dyadic epochs; it cannot cancel an `O(log log m)` secondary level.
- Carter--Hunter--O'Bryant improve the finite Sidon diameter to
  `k^2-1.96365 k^(3/2)-O(k)`.  After taking logarithms this changes only an
  `O(k^-1/2)` correction to its `2log k` main term.  Applied to a contained
  interval, `k` records its length and gives a constant-order improvement over
  the triangular full-span logarithm, but it carries no endpoint placement,
  cross-length coupling, or nested-survival state.
- Beker proves strong finite consecutive-sum constructions, while the
  Ruzsa--Shakan--Solymosi--Szemerédi Example 2 shows that distinct adjacent
  gaps alone can coexist with third energy of order `|A|^4`.  This blocks an
  adjacent-only energy-stability inference, not P17 under full Golomb
  uniqueness.
- Fabian--Rué--Spiegel obtain quantitative separation for specially
  constructed strong infinite Sidon sets.  That extra strong-Sidon property
  is not known on an arbitrary eventually critical branch.
- O'Bryant's weighted Abel and separated finite-extension lemmas are close
  templates, but naive iteration is too costly and does not couple the
  future tail to `G+S`.
- The radial-tree, locally finite tree, and sharp Dirichlet one-box papers
  identify qualitative or Dini-summable analytic endpoints.  They neither
  construct the required positive bi-/tri-tree measure nor prove its
  summably vanishing box profile.

The persisted audit records **26 successful scholarly requests**:
Crossref `8/185` result slots, arXiv `11/215`, and OpenAlex `7/49`, yielding
449 ingested slots and **351 deduplicated records**.  Four malformed arXiv
field-query attempts failed and were logged.  Fourteen records have
structured evidence, thirteen from full text and one abstract-only.

The explicitly requested providers were used as follows:

- Exa: 18 searches / 180 reviewed slots;
- Firecrawl: 8 searches / 120 slots, 3 related-paper calls / 45 slots,
  4 inspect calls, and 6 in-body reads;
- SciSpace: 4 searches / 40 slots;
- Consensus: one blocked attempt because the monthly allowance was 30/30;
  the reported reset date was 2026-09-01.

Provider results overlap and are not added to the 351-record scholarly
corpus.  Crossref met the configured four-axis saturation rule; arXiv and
OpenAlex did not, so overall saturation is **false**.  The theorem ledger
relies on checked primary pages and theorem text, not provider summaries.

## 8. Remaining obligations

1. **[BLOCKED] P17 secondary survival repayment.**  Prove (21), equivalently
   (22), on one fixed eventually `C`-critical infinite Golomb branch.  The
   proof must recover almost all of the residual endpoint `log log` profile
   through `G`, `S`, or an exactly coupled combination.
2. **[BLOCKED] Fixed-branch coupling.**  Any use of later horizons
   `H(m)`, prefix ranks, or cross-ratio tails must be simultaneous on the
   same infinite branch.  Changing finite rulers cannot discharge this
   obligation.
3. **[BLOCKED] Route B positive product-box encoding.**  If Route B
   is pursued, construct the full bi-/tri-tree measure for both endpoint- and
   difference-limited regimes and prove a summable vanishing profile strong
   enough for `o(log J)`.
4. **[BLOCKED] P15 and #1191 final implication.**  Even a new finite inequality or
   an `O_C(J log J)` bound is not P15.  The canonical P15 reduction and its
   quantifiers must be closed before any resolution or prize submission.

## 9. Single highest-value next lemma

**[BLOCKED] P17 secondary survival repayment lemma.**  For every fixed
`C>0` and every fixed infinite Golomb branch that is eventually
`C`-critical,

\[
\boxed{
\sum_{m\in E_J}Y_m=o_C(\log J).}
\tag{W11-NEXT}
\]

Equivalently, with the exact same `K^len`, `G^len`, and `S` from (5)--(7),

\[
G_J^{\rm len}+S_J
\geq T_J-K_J^{\rm len}-o_C(\log J).
\]

The most concrete attack is to choose later horizons `H(m)` on that one
branch, use the finite-horizon version of (24), and couple its terminal
ratios to hereditary cross-length rank lag.  The lemma must be aggregate:
the logarithmic overlap (25), the exhaustive failures, and the changing
Erdős--Turán windows rule out the corresponding uniform same-atom or purely
local versions.

## 10. Reproduction and integrity

Run from `core_workspace/endpoint_variance`:

```sh
erdos1191_wave11_tmp="$(mktemp -d)"
/Users/USER/miniforge3/bin/python3 wave11_abel_repayment_probe.py \
  --source-certificate wave6_arithmetic_mining_certificate_2026-08-28.json \
  --output "$erdos1191_wave11_tmp/replayed.json"
cmp wave11_abel_repayment_certificate_2026-08-29.json \
  "$erdos1191_wave11_tmp/replayed.json"

PYTHONDONTWRITEBYTECODE=1 uv run --no-project --with pytest \
  python -m pytest -q -p no:cacheprovider \
  test_wave11_abel_repayment_probe.py

uvx --from ruff==0.16.5 ruff check \
  wave11_abel_repayment_probe.py test_wave11_abel_repayment_probe.py
uvx --from ruff==0.16.5 ruff format --check \
  wave11_abel_repayment_probe.py test_wave11_abel_repayment_probe.py
/Users/USER/miniforge3/bin/python3 -m py_compile \
  wave11_abel_repayment_probe.py test_wave11_abel_repayment_probe.py
```

The focused suite was independently observed as `7 passed in 47.85s`.
Ruff check, Ruff format verification, and `py_compile` were clean for the two
Wave 11 Python files.  The integrated package runner passes 268 tests and 42
subtests, every dated certificate through Wave 11 regenerates byte-identically,
and the closing 275-entry self-excluding manifest verifies.  The final ZIP
passes `unzip -t`, manifest verification after independent extraction, and the
same complete runner in the extracted copy.  Exact scope and commands are in
`integrity/WAVE11_TEST_VERIFICATION_2026-08-29.json`.

Current key input hashes after integration (the continuation's own hash is
recorded in the verification JSON to avoid a self-reference):

```text
e11e329a728baebdddc125801ef41065ad5c940e4318653b6e89e5376b243cb9  WAVE11_SURVIVAL_ABEL_REPAYMENT_ANALYSIS_2026-08-29.md
82170ee7333f93ff62d7382561b6d291177d27299a207df7f3abc3413277d72c  wave11_abel_repayment_probe.py
b52c6a4258b12aadd783a9a7dff96e61956d15a35e92e6867cc52e7d4aeafaf8  test_wave11_abel_repayment_probe.py
ce29a441673d03ff4485658df0e4924d73839456a3be7e158ac56021522762c6  WAVE11_ABEL_REPAYMENT_PROBE_2026-08-29.md
0ddedc739ce3dd8161c3bd0b8d98222bf9439dfc37ed679afdfa37cb2f907e07  wave11_abel_repayment_certificate_2026-08-29.json
9bf0bcc52d51e7dc0da12e1cfbc72f10c66f99831e992959bfb66efef46d3e2c  WAVE11_SURVIVAL_ABEL_LITERATURE_DELTA_2026-08-29.md
6d4988428d9681635ab4866c3db05407bd06fdaba20c70035fa76d83c5f04d59  research_sources/wave11_literature_state/research_state.json
```

Certificate internal digest:

```text
1e9eb7627991687a22b1abf0cb36c52a876846d203374d830f545ddfb44d220b
```

## Final disposition

Wave 11 proves a material theorem: interval consistency alone supplies the
missing leading quarter and converts the exposed Abel deficit from quadratic
order to the secondary `O_C(J log J)` frontier.  It also gives an exact
nonnegative three-channel decomposition and an exact positive future-tail
identity.  Those results narrow the problem; they do not solve it.  The only
honest terminal status is:

**UNRESOLVED_AT_HARD_LIMIT**

# Wave 11 exact Abel-repayment probe

Date: 2026-08-29

Status: exact finite identities and bounded exhaustive computation.  This note
does **not** prove P16, P15, an infinite critical branch, or Erdős Problem
#1191.

## 1. Scope and reproducible artifacts

The executable probe is `wave11_abel_repayment_probe.py`; its focused tests are
`test_wave11_abel_repayment_probe.py`; its deterministic output is
`wave11_abel_repayment_certificate_2026-08-29.json`.

All logarithmic identities are represented as canonical formal sums

\[
 \sum_{d\geq2}c_d\log d,\qquad c_d\in\mathbb Q.
\]

Thus equality, addition, subtraction, and scalar multiplication use
`fractions.Fraction` only.  Fields named `float_projection` are numerical
evaluations and are never used to certify an identity.  In the complete
eight-mark search, signs are additionally certified after clearing rational
exponents and comparing two integers.

The finite data consist of:

- all 1,468 normalized eight-mark Golomb rulers with last mark at most 40;
- the complete 1,146-ruler subfamily satisfying every `C=1` prefix cap;
- the Wave 6 Hall counterexample and six hash-authenticated 64-mark fixtures;
- the hash-authenticated 128-mark continuation;
- the deterministic 512-mark scaled Erdős--Turán fixture;
- the independently reconstructed 682-mark modified-greedy fixture, audited
  through its complete 512-mark dyadic prefix.

No row in the certificate is assigned `surv_C=infinity`.

## 2. Exact Wave 10 repayment state

For each dyadic epoch set `E`, the probe computes the actual negative bulk
mass `A_E`, positive fan `Q_E`, terminal term `T_E`, global rank-only floor
`F_E`, and

\[
 P_E=A_E-F_E,\quad S_E=2T_E-Q_E,\quad U_E=T_E-F_E.
\]

It independently expands every primitive cross ratio and checks

\[
 \boxed{U_E-P_E-S_E=\sum_{m\in E}Y_m}
\]

as an exact formal-log identity.  It also globally ranks the actual bulk
differences and splits

\[
 P_E=H_E+R_E,
\]

where `H_E` is the numerical-hole premium at fixed actual weights and `R_E`
is the coefficient-rearrangement premium.  The certificate records atom
counts, actual ranks, prefix holes, ideal weight-rank ranges, and the maximum
rank displacement of every lower-ramp atom.

## 3. Exact finite-horizon lower-tail identity

Fix one epoch `m`, put

\[
 v_i=\left({m-i\over2m}\right)^2,
 \qquad 1\leq i\leq m-2,
\]

and write `D_(i,j)=a_j-a_(i-1)`.  The positive lower boundary minus the full
negative lower shell is

\[
 R_m=\sum_{i=1}^{m-2}v_i
       \log {D_{i,m-1}\over D_{i+1,m-1}}.
\]

For every finite `H>=m`, the primitive cross-ratio definition telescopes in
the second coordinate:

\[
 \sum_{j=m}^{H}C_{ij}
 =\log {D_{i,m-1}\over D_{i+1,m-1}}
  -\log {D_{i,H}\over D_{i+1,H}}.
\]

Consequently the probe verifies, coefficient by coefficient,

\[
 \boxed{
 R_m=\sum_{i=1}^{m-2}v_i\left(
      \sum_{j=m}^{H}C_{ij}
      +\log {D_{i,H}\over D_{i+1,H}}
      \right).}
\]

Every primitive cross-ratio comparison is also checked directly as an exact
integer product inequality.  The logarithms are used only to report the
consumed fraction.

At the last audited epoch, the fraction of `R_m` consumed during the single
new block `[m,2m)` was:

| fixture | `m` | `R_m` | consumed fraction |
|---|---:|---:|---:|
| Hall 64 | 32 | 0.0595501 | 0.806283 |
| authenticated 64 fixtures | 32 | 0.0210969 | 0.868560--0.894004 |
| authenticated 128 | 64 | 0.0513752 | 0.878093 |
| Erdős--Turán 512 | 256 | 0.125125 | 0.614729 |
| modified-greedy 682, audited to 512 | 256 | 0.0391993 | 0.882481 |

The 512-point Erdős--Turán row is a useful warning: one new block need not
consume a fraction close to one.  This is finite evidence only and says
nothing by itself about a fixed surviving infinite branch.

## 4. Length-aware lower floor and the mixed `2 log m` floor

The lower-shell interval of gap length `ell` is a sum of `ell` distinct
positive adjacent gaps.  Therefore

\[
 D\geq1+2+\cdots+\ell={\ell(\ell+1)\over2}.
\]

This gives the exact universal lower-shell floor

\[
 \boxed{
 L_m={1\over4m^2}
 \sum_{\ell=2}^{m-2}(2\ell+1)
 \log {\ell(\ell+1)\over2}.}
\]

The exceptional length-one coefficient contributes `4 log(1)=0`.  A direct
Riemann-sum estimate gives

\[
 L_m={1\over2}\log m+O(1).
\]

After deleting all `q=m-1` atoms, the upper bulk contains, at epoch `m`,

- `m-1` copies of weight `1/m^2`;
- `(m-1)(3m-8)/2` copies of weight `1/(2m^2)`;
- `m-1` copies of weight `1/(4m^2)`.

Global sorting over any finite dyadic epoch set gives

\[
 F_E^{\rm upper}={3\over2}\sum_{m\in E}\log m+O(|E|).
\]

Indeed the middle block has mass `3/4+O(1/m)` and occupies ranks comparable
to `m^2`, uniformly even for a sparse dyadic set; it contributes
`(3/2)log m+O(1)`.  The other two blocks have total mass `O(1/m)` and cost
only `O(1)` per epoch.  Hence

\[
 \boxed{K_E^{\rm mix}:=\sum_{m\in E}L_m+F_E^{\rm upper}
       =2\sum_{m\in E}\log m+O(|E|).}
\]

The code checks the exact finite inequality

\[
 A_E\geq K_E^{\rm mix}
\]

by the termwise triangular bounds and the global upper-bulk rearrangement.
It also checks the strengthened exact residual identity

\[
 \boxed{
 \sum_{m\in E}Y_m
 =(T_E-K_E^{\rm mix})-(A_E-K_E^{\rm mix})-S_E.}
\]

Under the hypothetical eventual critical cap, the old `7/4` floor left an
`O_C(J^2)` envelope on `E_J={4,8,...,2^J}`.  The mixed floor cancels the full
`2 sum log m` endpoint main term and leaves

\[
 T_{E_J}-K_{E_J}^{\rm mix}
 \leq\sum_{m\in E_J}\log\log m+O_C(J)
 =O_C(J\log J).
\]

This is a real order improvement, but it is still much larger than the
`o(log J)` required by P16.  It is not a resolution.

For the consecutive finite sets available in the fixtures, the mixed-floor
coefficient ratio `K_mix/sum log m` rises from `1.40193` through 64 marks to
`1.53648` through 128 and `1.69824` through 512, consistent with convergence
toward 2.  It is weaker than the old finite rank floor at the small 64- and
128-mark cutoffs and first exceeds it in the audited 512 rows; only the
asymptotic leading coefficient is uniformly stronger.

## 5. Exhaustive eight-mark candidate audit

The following literal candidate inequalities were tested on all 1,146
eight-mark `C=1` rulers.  A failure sign was exact.

| candidate | contract | failures | verdict |
|---|---|---:|---|
| bulk only | `P>=U` | 1,146 | universally false in this bounded scope |
| boundary only | `S>=U` | 1,146 | universally false in this bounded scope |
| all-hole only | `H>=U` | 1,146 | universally false in this bounded scope |
| lower-hole quarter | `H_lower >= (1/4) sum log m` | 1,146 | universally false in this bounded scope |
| zero residual | `P+S>=U` | 1,146 | false because the exact residual `Y` is positive |
| normalized harmonic | `sum Y <= U/floor(log2 max E)` | 0 | no bounded failure found |

The minimum-terminal, then lexicographic counterexample for each failed
candidate is

`(0,1,4,9,15,22,32,34)`.

The surviving normalized candidate has minimum observed margin `0.2103363`,
at `(0,3,14,22,23,27,29,39)`, with exact positive sign.  It is not a P16
theorem and, even combined with an `O(J log J)` envelope, would yield only an
`O(log J)` scale rather than `o(log J)`.

The largest residual in the exhaustive family is

\[
 \max Y=0.41169263645582849,
\]

and the largest envelope ratio is

\[
 \max {Y\over U}=0.33092722656045681.
\]

Both occur at `(0,3,14,22,23,27,29,39)`.  Thus the minimum observed repaid
fraction `(P+S)/U` is `0.66907277343954319`.  The maximizing selection uses
labelled floating evaluations; the two formal-log forms and all surrounding
identities are stored exactly in the certificate.

## 6. Authenticated long-fixture outcome

All literal candidates except `NORMALIZED_HARMONIC` fail on every final long
fixture row.  The normalized candidate has positive projected margin on all
rows, ranging from `0.640650` to `1.94109` at the 512-mark cutoffs.  Again,
this is a finite survivor, not an inferred law.

For the two longest audited rows:

| fixture | `sum Y` | old `U` | mixed `T-K_mix` | `Y/(T-K_mix)` |
|---|---:|---:|---:|---:|
| Erdős--Turán 512 | 2.35364 | 34.3578 | 33.6823 | 0.0698777 |
| modified-greedy 682, audited to 512 | 1.65431 | 18.3597 | 17.6842 | 0.0935475 |

The old and mixed finite floors are close at these sizes; the significance of
the new floor is its asymptotic cancellation, not a dramatic finite ratio.

## 7. Changing Erdős--Turán calibration

For each `m=16,...,1024`, let `p` be the least prime at least `2m` and build a
new `2m`-mark Erdős--Turán ruler.  These are changing finite windows, not
prefixes of one branch.

| `m` | `Y_m` | `T_m-K_mix,m` | ratio |
|---:|---:|---:|---:|
| 16 | 0.354619 | 2.92631 | 0.121183 |
| 32 | 0.359149 | 2.92649 | 0.122724 |
| 64 | 0.366938 | 2.94472 | 0.124609 |
| 128 | 0.370520 | 2.94214 | 0.125935 |
| 256 | 0.372813 | 2.96238 | 0.125849 |
| 512 | 0.373975 | 2.95429 | 0.126587 |
| 1024 | 0.374428 | 2.95083 | 0.126889 |

The nonvanishing ratio refutes any inference that the leading-quarter repair
alone forces pointwise vanishing on arbitrary finite critical windows.  It
does not refute a survival-conditioned statement on a fixed infinite branch.

## 8. What remains

The computation isolates the remaining analytic burden more sharply:

1. the missing leading quarter is supplied unconditionally by interval
   length, improving the crude envelope from `O_C(J^2)` to `O_C(J log J)`;
2. the exact lower tail identifies how repayment can move into later
   cross-ratio triangles;
3. neither a one-block consumed fraction nor any literal bulk-, boundary-, or
   hole-only inequality closes P16;
4. a successful theorem must use fixed-branch survival to turn the terminal
   lower-tail remainders and/or the strengthened premium into an additional
   summable gain beyond `O(J log J)`.

The most concrete next target is therefore a survival-conditioned estimate
for the terminal ratios

\[
 \sum_{m\in E_J}\sum_{i=1}^{m-2}v_i
 \log {D_{i,H(m)}\over D_{i+1,H(m)}}
\]

after choosing later horizons `H(m)` on one branch, coupled to hereditary
rank-lag constraints.  A finite changing-family calibration cannot replace
that quantifier.

## 9. Verification

Run from `core_workspace/endpoint_variance`:

```text
python wave11_abel_repayment_probe.py
python -m pytest -q -p no:cacheprovider test_wave11_abel_repayment_probe.py
ruff check wave11_abel_repayment_probe.py test_wave11_abel_repayment_probe.py
ruff format --check wave11_abel_repayment_probe.py test_wave11_abel_repayment_probe.py
```

Final hashes and replay output are recorded in the parent handoff after the
source and certificate are sealed.

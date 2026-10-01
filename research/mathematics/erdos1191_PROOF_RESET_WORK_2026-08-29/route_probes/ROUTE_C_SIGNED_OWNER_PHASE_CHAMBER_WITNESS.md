# Signed-owner phase midpoint: exact rational PSD witness

Date: 2026-08-30  
Status: `EXACT_FIXED_RATIONAL_PSD_PHASE_MIDPOINT_WITNESS_C058_OPEN`

This note records one exact finite midpoint witness.  It is conditional on the
aggregate coordinate-owner accounting being the intended finite whole-stencil
constraint.  It does **not** prove that accounting law, a phase interval, the
C067 terminal/Gothic ledger, a compatible infinite history, C058, either
Erdős question, novelty, or any prize claim.

## 1. Exact fixture

Use

\[
 a_k=k(k+100),\qquad 0\le k\le15,
\]

and the first rational point in the event chamber immediately following the
old witness's endpoint:

\[
 {805\over8}<t={4835\over48}<{605\over6}.
\]

The four widths and the recorded upper terminal width are

\[
 t={4835\over48},\quad 2t={4835\over24},\quad
 4t={4835\over12},\quad 8t={4835\over6},\qquad
 16t={4835\over3}.
\]

For ranks `k=3,...,15`, put

\[
 h_{k,T}={g_T(\cdot-a_k)\over2T},\qquad
 q_{k,T}=16t\,h_{k,T}={8t\over T}g_T(\cdot-a_k).
\]

There are 52 physical coordinates, 78 distinct finite events, 77
positive-length common cells, eight owners `(n,T)` with `n=4,8`, and hence
616 aggregate owner-cell inequalities.  The two zero exterior cells are also
checked under the half-open convention.  At each width the shared `a_7`
coordinate belongs once to the earlier `n=4` group; the eight groups
partition all 52 coordinates.

For an owner with `T=m*t`, its cell demand is

\[
 d_{n,m,c}=2mt\,h_{A_n}(c)^TM_nh_{A_n}(c)
 ={m\over128t}\,q_{A_n}(c)^TM_nq_{A_n}(c).
\]

For a zero-row-sum PSD matrix `X`, its signed coordinate-owner share is

\[
 q_{G_{n,m}}(c)^TXq(c).
\]

The owner shares sum pointwise to the physical energy `q(c)^T X q(c)`.

## 2. Rational Gram witness

The certificate stores an integer matrix with shape `52 x 11` and common
denominator

\[
 2{,}000{,}000.
\]

Every integer column sums to zero and its largest absolute entry is `20,983`.
Writing the resulting rational matrix as `B` and `X=BB^T` proves exactly that

\[
 X\succeq0,\qquad X\mathbf 1=0.
\]

Exact `Fraction` replay gives:

- all 616 owner rows feasible;
- 259 structural equality rows and 357 strictly positive rows;
- minimum positive owner-row slack
  `40498647/1934000000000000`;
- 77 pointwise owner-sum/physical-energy identities;
- integrated signed demand
  \[
  D={6221\over30944};
  \]
- physical price
  \[
  P={951134501701\over3000000000000};
  \]
- strictly positive aggregate margin
  \[
  2D-P={246690436855133\over2901000000000000}>0.
  \]

The eight integrated owner demands, in width-major order, are

\[
 -{439\over7736},\ -{5721\over154720},\
 {6223\over61888},\ {17239\over1237760},\
 {801\over30944},\ {106079\over1237760},\
 0,\ {8503\over123776}.
\]

## 3. Exact boundary of the conclusion

The certified statement is only this:

> At `t=4835/48`, the stored rational zero-row-sum PSD Gram factor satisfies
> every one of the 616 canonical aggregate coordinate-owner rows and has
> `P<2D`.

The witness was found numerically and then replaced completely by the stored
rational factor.  The executable replay uses no floating-point solver and
does not claim that this factor is optimal.

In particular, this midpoint success does not repair the previous fixed
witness, prove uniform validity on `(805/8,605/6)`, or justify subtracting the
physical price from a legal global Gothic resource.  The upper terminal
`16t` is recorded as fixture data but no terminal payment identity is asserted
here.

## 4. Replay

From `route_probes/` run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  ROUTE_C_SIGNED_OWNER_PHASE_CHAMBER_WITNESS_test.py
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  ROUTE_C_SIGNED_OWNER_PHASE_CHAMBER_WITNESS_certificate.py \
  --verify ROUTE_C_SIGNED_OWNER_PHASE_CHAMBER_WITNESS_certificate.json \
  --self-check
```

The canonical semantic payload SHA-256 is
`3f10228fdd1087c7809c5ad55910059993da352ebae886236ac591a104b43e84`.

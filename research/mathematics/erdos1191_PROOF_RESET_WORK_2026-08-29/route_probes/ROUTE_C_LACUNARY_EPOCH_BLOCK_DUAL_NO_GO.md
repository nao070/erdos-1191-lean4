# Route C: exact lacunary epoch-block dual no-go

Status: `EXACT_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_GLOBAL_C058_OPEN`.

This note records one exact obstruction to a **geometry-free** extension of
the four-width aggregate epoch-block PSD master.  It is not an obstruction on
an eventual fixed-`C` critical history and it does not resolve C058.

## Exact finite statement

Take the 16-mark Golomb ruler

`a_k=2^k-1`, `0<=k<=15`,

and the normalized scale

`t=(3/2)(a_15-a_8)/8=6096`.

Use the same 52 scale-labelled coordinates, multipliers `1,2,4,8`, aggregate
owner rows, and zero-row-sum epoch-block PSD cone as the fixed-history
four-width master.  The past block has projected dimension 19 and the current
block has projected dimension 31.  At this scale there are 78 event points,
77 positive cells, and 308 owner rows in each epoch.

Every past-epoch owner demand is exactly zero, so `D_4=0` and the zero past
correction is feasible.  For the current epoch,

`D_8=981/16256`, hence `2D_8=981/8128`.

The certificate stores 308 nonnegative rational dual weights with denominator
`100000`; 243 are positive.  If `H` is the exact integrated physical-price
matrix and `A_r,c_r` are the current-epoch owner rows, then

`S=H-sum_r y_r A_r`

is positive definite.  Fraction-only LDL elimination gives 31 strictly
positive pivots.  The exact dual objective is

`sum_r y_r c_r = 370911/2560000`,

and therefore

`sum_r y_r c_r - 2D_8 = 7865697/325120000 > 0`.

Weak SDP duality now proves, for every feasible correction in this exact
epoch-block PSD cone,

`P_8 >= 370911/2560000 > 2D_8`.

At the worst Fejér ratio `rho=9/16`, and hence throughout
`rho in [9/16,1]`, the total weighted margin obeys

`Phi = (2D_4-P_4)+rho(2D_8-P_8)`

`<= -70791273/5201920000 < 0`.

Thus no feasible matrix in the stated cone has positive `Phi` on this
fixture and phase point.

## Exact scope boundary

The infinite ruler `2^k-1` is not eventually fixed-`C` critical.  Indeed,
`log k<=k`, while `2^k/k^3` is unbounded (from a fixed index onward its
successive ratio is bounded strictly above one).  Hence `2^k` eventually
exceeds `2C k^2 log k` for every fixed `C`.

Accordingly the certificate proves only:

- a theorem uniform over all Golomb geometries is false for this particular
  aggregate four-width epoch-block PSD cone;
- Golomb distinctness alone cannot force positive phase margin;
- a history-sensitive geometric invariant, cross-epoch correction, or a
  separately paid span-jump term is mathematically necessary.

It does **not** prove failure on a compatible eventual fixed-`C` branch, does
not cover cross-epoch PSD blocks or a larger indefinite master, and does not
settle any birth, final, terminal, small-`m`, C058, Q1, Q2, novelty, or prize
gate.

The strongest honest next finite theorem is therefore a dichotomy.  For each
adjacent dyadic history and normalized phase, either the combined two-epoch
four-width SDP has a quantitatively positive phase-integrated margin, or a
precisely defined current-epoch lacunarity/span-jump potential pays its
negative part and telescopes through the complete finite Abel ledger.  A
separate positive statement for each epoch is already too strong: exploratory
critical-history runs have negative past-epoch margins at some phases while
their combined weighted margins remain positive.

## Reproduction

From `route_probes/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  ROUTE_C_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_certificate.py \
  --verify-json ROUTE_C_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_certificate.json \
  --mutations

PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  ROUTE_C_LACUNARY_EPOCH_BLOCK_DUAL_NO_GO_certificate_test.py
```

The first command replays the Golomb census, event geometry, all demands, the
nonnegative dual vector, exact objective, exact 31-pivot LDL factorization,
strict Fejér bound, payload hash, and 12 semantic mutation rejections.

Canonical payload SHA-256:
`4831e0395932c3fab9c51fd4a4607d4f6d4474626e364e6017f743ec6f451dbb`.

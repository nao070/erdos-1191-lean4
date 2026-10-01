# Route C: C132 exact 32-mark naive-paste obstruction

Date: 2026-08-31 (Asia/Tokyo)  
Status: `EXACT_FINITE_COMPOSITE32_NAIVE_LOCAL_BANK_PASTE_NO_GO_C058_OPEN`

## 1. Exact finite stress fixture

Let `A` be the fixed C120 row and `B` the fixed C123 row.  The explicit
32-mark concatenation

\[
P=A\cup(1239+5B)
\]

is

```text
(0,22,60,83,102,173,303,513,616,727,772,881,972,1041,1103,1169,
 1239,1349,1539,1654,2009,2659,3709,3804,4114,4339,4794,5124,
 5639,6184,6739,7084).
```

Exact integer replay checks all 496 positive differences and finds all 496
distinct.  For every prefix `4<=m<=32`, a 240-term rational logarithm
enclosure proves

\[
N_m\le 2C m^2\log m\qquad(C=2).
\]

The worst required finite constant occurs at `m=8` and lies strictly in

\[
1931/1000<C_{\rm req}<483/250.
\]

This is an onset-4 finite fixture, not an infinite eventual-`C` history.

## 2. The missing cross-half residual

Let `M_n=D_n^TB_nD_n` be the canonical point matrix.  Embed one `M8` in each
9-point half of the 17-point `M16` state, sharing the middle coordinate, and
put

\[
R_{16}=M_{16}-{1\over4}(M_{8,L}+M_{8,R}).
\]

Exact reconstruction gives:

- zero diagonal and zero row sums;
- 160 ordered / 80 unordered nonzero off-diagonal entries;
- mixed signs and indefiniteness;
- 21 sources and mass `329/256` in `Gamma8`;
- 105 sources and mass `5425/1024` in `Gamma16`;
- exactly 63 omitted cross-half sources, with mass `4767/1024`.

Therefore two quarter-scaled local `M8` banks are not the natural `M16`
demand.  Any genuine epoch-8/16 continuation must keep the 63 cross-half
sources rather than silently replacing `M16` by its two halves.

## 3. Exact natural epoch-16 owner failure

Map the pinned C130 chamber-43 factor

```text
[797/8,201/2], midpoint 1601/16, ranks (10,20)
```

by `rank -> rank+16`, `x -> 1239+5x`, and `width -> 5*width`.  The factor
remains an integer Gram, zero-row-sum PSD form supported inside the natural
epoch-16 coordinate block.  This algebraic embedding is legal.

The natural owner audit instead uses the full state ranks 15--31 and owns
ranks 16--31.  Across 173 exact cells and four multipliers it checks 692
owner rows.  Exactly 152 rows are strictly negative.  The strongest is

```text
cell             [5169,5239)
multiplier       8
natural demand   9/512
mapped owned     100084829709/5003125000000000000
margin          -175791028451541/10006250000000000
```

Adding an old C131 factor supported on ranks 3--15 cannot repair this owner
share: its dot product with the epoch-16 owned group 16--31 is zero.  Thus the
naive C130/C131 affine paste fails even though its component factors remain
PSD and zero-sum.

## 4. Exact phase-alignment obstruction for this paste family

Matching the natural shell phase to the `q`-dilated C123 phase forces
`T=1169+143q`.  But

```text
711-284=427=143+284.
```

Hence, for every positive integer `q`,

\[
(T+qB_5)-1169=(T+qB_{10})-(T+qB_5)=427q,
\]

so the aligned concatenation has a repeated positive difference and is not
Golomb.  This rules out exact phase alignment only in the displayed affine
paste family; it is not a no-go for a new common physical phase program.

## 5. Verification

The canonical verifier uses integer and `Fraction` arithmetic.  Seven focused
tests pass and five conclusion/provenance mutations are rejected.  A second
oracle imports neither the main verifier nor any canonical Python module; it
independently reconstructs the decisive Golomb, residual, and owner facts.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  route_probes/ROUTE_C_C132_COMPOSITE32_NAIVE_PASTE_NO_GO_certificate.py \
  --verify route_probes/ROUTE_C_C132_COMPOSITE32_NAIVE_PASTE_NO_GO_certificate.json \
  --self-check

PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  route_probes/ROUTE_C_C132_COMPOSITE32_NAIVE_PASTE_NO_GO_test.py

PYTHONDONTWRITEBYTECODE=1 python3 -B \
  route_probes/ROUTE_C_C132_COMPOSITE32_NAIVE_PASTE_NO_GO_independent_oracle.py
```

## 6. Exact claim boundary

C132 refutes only the explicit affine reuse of the local C130/C131 owner
certificates.  It does not refute:

- a fresh joint epoch-8/16 Gram or signed master;
- fractional or cross-block ownership;
- a different 32-mark ruler or common phase;
- arbitrary-rank localization;
- C058, Q1, or Q2.

The next program must include ranks 15--18, all 63 cross-half sources, one
common physical phase, and all C103 boundary and terminal rows.  The global
status remains `UNRESOLVED_AT_HARD_LIMIT`.

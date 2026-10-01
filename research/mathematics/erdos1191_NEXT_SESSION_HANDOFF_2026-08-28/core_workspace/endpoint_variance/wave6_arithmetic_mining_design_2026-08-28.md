# Wave 6 arithmetic mining design

**Date:** 2026-08-28  
**Status:** approved direction, pending written-design review before implementation

## Purpose and scope

Mine the six authenticated 64-mark Wave 5 Golomb rulers for an arithmetic
quantity that sees full contiguous-sum uniqueness across several dyadic
epochs.  Compare it exactly with the deliberately non-Sidon sawtooth profile,
and run one explicitly heuristic 64-to-128 extension experiment when feasible.

This work is finite calibration and candidate-lemma discovery.  It will not
claim an asymptotic reset-renewal theorem, an optimal 128-mark witness, or a
solution of Erdős Problem #1191.

Only new files whose names start with `wave6_arithmetic_mining_` may be
created.  Wave 5 artifacts are authenticated inputs and remain read-only.

## Exact birth-lag interval family

Let

\[
A_M=(a_0<a_1<\cdots<a_{M-1}),\qquad M=2^J.
\]

For every pair of ranks `0 <= i < r < M`, let `n(r)` be the unique power of
two satisfying

\[
n(r)/2\le r<n(r).
\]

Thus `r` lies in the newborn shell of the dyadic prefix of size `n(r)`.  Give
the pair three labels:

- birth epoch `n=n(r)`;
- category `ON` if `i<n/2`, and `NN` if `i>=n/2`;
- rank lag `ell=r-i`.

For every nonempty label triple define

\[
F_{n,c,\ell}=\{(i,r):n(r)=n,\ c(i,r)=c,\ r-i=\ell\}.
\]

These families partition all `binom(M,2)` rank pairs.  Their exact difference
spectra and integer hulls are

\[
\Delta_F=\{a_r-a_i:(i,r)\in F\},\qquad
I_F=[L_F,U_F]\cap\mathbb Z,
\]

where `L_F=min Delta_F`, `U_F=max Delta_F`, demand `d_F=|F|`, and integer
width `w_F=U_F-L_F+1`.

The certificate will retain every family row, including its ranks,
differences, demand, distinct count, collision deficit, endpoints, and width.
This makes the pair partition and every contiguous sum independently
checkable.

## Exact Hall-pressure theorem

For a selected subfamily `C` and integer interval `K=[x,y]`, define its
contained-band demand

\[
D_C(K)=\sum_{F\in C:I_F\subseteq K}d_F.
\]

For nonempty qualifying intervals put

\[
\Lambda_C=\max_K\frac{D_C(K)}{|K|},\qquad |K|=y-x+1.
\]

The oracle will support category filters, epoch filters, a minimum family
demand, and a minimum number of represented epochs.  The principal
reset-renewal statistic uses category `NN`, family demand at least two, and at
least two distinct epochs.  Adjacent-epoch rows restrict the epoch set to
`{8,16}`, `{16,32}`, `{32,64}`, and, for the experimental witness,
`{64,128}`.

If `A_M` is a Golomb ruler, all differences belonging to all families are
globally distinct.  Whenever `I_F` is contained in `K`, all `d_F` differences
are distinct integers in `K`.  Therefore

\[
D_C(K)\le |K|\quad\hbox{and hence}\quad\boxed{\Lambda_C\le1}.
\]

This is an exact theorem, not an empirical inequality.  It uses difference
injectivity and does not follow from the scalar diameter profile or covariance
moments alone.

It is sufficient to scan candidate intervals whose endpoints are family-band
endpoints.  Any interval with positive demand can be shrunk to the minimum
`L_F` and maximum `U_F` among its contained families; this cannot lose those
families, and any newly contained families only increase demand.

For the 64-mark sawtooth, the two consecutive newborn shells at epochs 32 and
64 both have adjacent gap 64.  Thus

\[
I_{32,NN,1}=I_{64,NN,1}=[64,64],
\quad d_{32,NN,1}=15,
\quad d_{64,NN,1}=31,
\]

so the interval `[64,64]` has demand 46 and `Lambda_NN=46`.  This is the
sharp finite contrast to be certified.  It does not by itself prove that
near-flat Sidon shells have a summable long-history cost; it identifies the
integer-packing quantity such a proof would have to control.

## Descriptive old-new versus new-new rows

For each dyadic transition `m -> 2m`, record the whole `ON` and `NN` spectra:

- pair count and distinct count;
- minimum, maximum, and integer hull width;
- hull-intersection interval and width;
- distinct occupied values from each category inside that intersection;
- actual cross-category collision values.

These rows expose range overlap and packing holes, but no new theorem will be
claimed from their ratios.  They are descriptive approach B, subordinate to
the exact Hall theorem.

## Inputs and experimental extension

The canonical generator will:

1. authenticate `wave5_nested_certificate_2026-08-28.json` by its internal
   hash and require the recorded Wave 5 hash;
2. mine all three retained witnesses from both Wave 5 objectives;
3. independently recompute all positive differences and require Golomb
   uniqueness for those six witnesses;
4. construct the exact non-Sidon sawtooth through 64 marks and retain its full
   collision data;
5. run one seeded heuristic extension of the leading Wave 5 persistence
   witness to 128 marks with `beam_width=32`, `candidates_per_state=16`,
   `seed=601191`, and `retain=1`;
6. independently audit the resulting 128-mark witness, every-prefix `C=1`
   envelope, all `8128` positive differences, and all birth-lag rows.

The exact Hall theorem applies to every Golomb witness regardless of how it
was found.  Existence of the recorded 128 witness is an exact finite fact after
audit; its discovery, quality, and failure to find alternatives remain
heuristic beam-search observations.

## Files and data flow

- `wave6_arithmetic_mining_search.py`: validated pair partition, spectra,
  transition summaries, exact Hall maximizer, audits, and targeted extension.
- `wave6_arithmetic_mining_test.py`: hand fixtures, RED/GREEN regression tests,
  sawtooth overload, Golomb Hall bound, certificate integrity, and 128 audit.
- `wave6_arithmetic_mining_certificate.py`: authenticated input loading,
  deterministic exact serialization, runtime/source manifest, source-mutation
  guard, and canonical hash.
- `wave6_arithmetic_mining_certificate_2026-08-28.json`: full exact rows and
  witnesses.
- `wave6_arithmetic_mining_results_2026-08-28.md`: theorem, exact findings,
  candidate interpretation, reproduction, and limitations.

Fractions are serialized as rational strings.  No float-derived values enter
the hash-bearing payload.  The certificate records the Python implementation
and version and limits byte-identity claims to that runtime.

## Tests and completion gates

Tests will be written before production code and observed failing for the
missing behavior.  Required cases are:

1. the four-mark ruler `(0,1,4,6)` partitions all six pairs into the expected
   birth/category/lag families;
2. its two-demand `F_(4,ON,2)` spectrum is exactly `(4,5)` with band `[4,5]`;
3. every pair appears exactly once and stored differences equal the point
   differences;
4. every tested Golomb fixture has Hall pressure at most one;
5. sawtooth64 has the two exact `[64,64]` families and cross-epoch NN pressure
   exactly 46;
6. transition `ON`/`NN` rows reproduce hand-computed collision-free and
   collision-bearing fixtures;
7. the committed certificate opens, validates its internal hash and source
   manifest, authenticates Wave 5, and contains six 64-mark plus one 128-mark
   audited witnesses.

Before completion, run the focused Wave 6 tests, the relevant Wave 5 tests,
and an independent certificate replay that recomputes every retained
difference, family band, Hall maximizer, and envelope row.

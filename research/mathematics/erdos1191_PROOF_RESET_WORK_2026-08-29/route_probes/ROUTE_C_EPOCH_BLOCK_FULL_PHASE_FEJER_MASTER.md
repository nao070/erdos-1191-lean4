# Route C: epoch-block full-phase Fejer master

Date: 2026-08-30  
Status: `EXACT_FIXED_FULL_PHASE_FEJER_MASTER_GLOBAL_C058_OPEN`

This bundle gives an exact, gap-free phase certificate for the fixed history

\[
 a_k=k(k+100),\qquad 0\le k\le15,
\]

with the two aggregate epochs (n=4,8), base width (t\in[100,200]), and
sampled widths (t,2t,4t,8t).  For every phase and every Fejer epoch-weight
ratio (r\in[9/16,1]), a rational positive-semidefinite owner master has
strictly positive weighted margin.

The result is a finite fixed-history lemma.  It does not prove C058 or either
question in Erdos Problem 1191.

## 1. Exact phase decomposition

The 52 coordinates are the Haar channels

\[
 (k,m,a_k),\qquad 3\le k\le15,\quad m\in\{1,2,4,8\}.
\]

Their left, middle, and right boundaries are the 78 affine event lines

\[
 a_k+smt,\qquad s\in\{0,1,2\}.
\]

All crossings in (100\le t\le200) give 109 distinct rational phase
endpoints and 108 open event chambers.  A generic chamber has 77
positive-length cells and eight owner rows per cell.  The certificate includes
one closed-chamber witness for every chamber, so there is no uncovered phase
interval.  Collapsed cells at all chamber endpoints are separately rebuilt
with the half-open Haar convention and audited exactly.

The shared coordinate at (a_7) occurs in both physical epoch formulae but is
owned once: it lies in the past (n=4) Gram block, while the current owner
groups begin at (a_8).

## 2. Rational epoch-block Gram witnesses

For chamber \(\nu\), the embedded witness has the form

\[
 X_\nu={B_\nu B_\nu^T\over 2000000^2}.
\]

Every integer column of (B_\nu) has length 52, sums to zero, and is supported
entirely in either the 20-coordinate (n=4) block or the 32-coordinate (n=8)
block.  Consequently, without a floating-point eigenvalue test,

\[
 X_\nu\succeq0,\qquad X_\nu\mathbf1=0,
 \qquad X_\nu[\text{past},\text{current}]=0.
\]

The 108 factors contain 2315 rational Gram columns in total; the largest
absolute stored integer is 19791.  Cross-width entries inside an epoch are
allowed and are the finite mechanism inherited from the preceding
cross-width reopening.

For an owner (G=(n,m)), state (q), and point-matrix demand (c_G(q)), the
canonical cell row is

\[
 t\,q_G^T X_\nu q\ \ge\ c_G(q),
 \qquad
 c_G(q)={m\over128}q_A^TM_nq_A.
\]

Because the state is fixed in an open chamber, each row is affine in (t).
It is therefore enough to check both rational chamber endpoints.  The replay
checks 66,528 open-chamber owner rows, or 133,056 limiting endpoint
inequalities.  It also checks 129,280 owner rows on the actual collapsed
endpoint cell decompositions, with shared endpoints repeated for the two
adjacent factors.  All arithmetic uses `fractions.Fraction`.

## 3. Exact price and margin polynomials

On one chamber every cell length is

\[
 \Delta a+\Delta b\,t.
\]

For epoch (n), write the integrated price and demand as

\[
 P_n(t)=A_{P,n}+B_{P,n}t,
 \qquad
 D_n(t)={A_{D,n}\over t}+B_{D,n}.
\]

Then the exact quadratic stored by the certificate is

\[
 t\Phi_n(t)
 =-B_{P,n}t^2+(2B_{D,n}-A_{P,n})t+2A_{D,n}.
\]

For an epoch-weight ratio (r),

\[
 t\Phi_r(t)=t\Phi_4(t)+r\,t\Phi_8(t).
\]

Every chamber quadratic is minimized exactly at its two endpoints and, when
applicable, its interior vertex.  This is done at both (r=9/16) and (r=1).
Since the expression is affine in (r), strict positivity at those two
ratios proves strict positivity for every (r\in[9/16,1]).

The global minima are

\[
 \min_{t,\nu}t\Phi_{9/16}(t)
 ={255996752651\over2560000000000},
\]

attained at the right endpoint (t=605/6) of chamber 1, and

\[
 \min_{t,\nu}t\Phi_1(t)
 ={54555211621\over500000000000}.
\]

Thus the uniform all-ratio constant is

\[
 \mu={255996752651\over2560000000000}>0.
\]

With (t=100\,2^\theta),

\[
 \int_0^1\Phi_r(100\,2^\theta)\,d\theta
 ={1\over\log2}\int_{100}^{200}{\Phi_r(t)\over t}\,dt
 \ge {\mu\over200\log2}
 >{\mu\over200}.
\]

The exact rational lower bound recorded in the certificate is therefore

\[
 {\mu\over200}
 ={255996752651\over512000000000000}>0.
\]

## 4. Whole signed Abel-Gothic ledger

The phase replay imports only the exact whole-stencil theorem from the prior
bundle, whose payload hash is

`5879f3b774b8b044f01f6a7d529946d620478191b7a9ed8b7e246c6e16063e57`.

Its ledger has 24 primitives, 96 four-corner occurrences, 42 distinct
nonzero Gothic rows, and 28 rows reused with mixed signs.  All 46 coefficient
identities \(\lambda=2M\) hold.  Hence the physical demand identity is
coordinatewise and does not depend on a sampled phase.

For every primitive \(\gamma\), the four-scale Abel identity is

\[
 \sum_{s=0}^3 2(2^st)\alpha_\gamma
 \bigl(\psi_\gamma(2^st)-\psi_\gamma(2^{s+1}t)\bigr)
 =2t\alpha_\gamma\psi_\gamma(t)
  +\sum_{s=1}^3 2^st\alpha_\gamma\psi_\gamma(2^st).
\]

The omitted last term is legitimate because
\(\psi_\gamma(16t)=0\) throughout the phase interval.  The lower
\(t\)-boundary is retained; it is not silently discarded.  As regressions,
the program replays all 24 identities and the aggregate direct-demand identity
at the 109 endpoints and 108 chamber midpoints: 5208 primitive checks and 217
aggregate checks.

This remains an aggregate, one-for-one replacement of the net Gothic ledger.
Mixed reuse means the 96 primitive corner occurrences cannot be declared
independent capacities.  No primitive-owned cover or directed epoch flow is
claimed.

## 5. Integrity and independent replay

The self-contained embedded factor manifest has canonical raw SHA-256

`45060f68702057a81718ca452502c9f3cdd322edc07c9884583d802f5e18e49c`.

An independent arbitrary-precision reconstruction of the original 108 factor
files produced semantic manifest SHA-256

`d99bc33fb238b1a755a8c7ba4270cb5cf81dd6cf8b621059214ce83edc1edcc3`.

The committed certificate payload SHA-256 is

`27daefedfac382d4a9c1a88ec1214b842f6c65f85a190557914fa1a198116b9f`.

The verifier rebuilds every Gram value from integer dot products, replays the
complete phase audit, requires canonical JSON bytes, rejects nonobject roots,
distinguishes Boolean values from integers, isolates its cache by returning a
fresh decoded object, and rejects 16 rehashed semantic mutations.

## 6. Exact scope boundary

Certified:

- the fixed 16-mark history (a_k=k(k+100));
- the two aggregate epochs (n=4,8);
- every (t\in[100,200]) and every (r\in[9/16,1]);
- independent zero-row-sum PSD epoch blocks with within-epoch cross-width
  coupling;
- all canonical owner rows, collapsed endpoints, and quadratic minima;
- the aggregate whole-stencil Abel-Gothic replacement.

Not certified:

- a primitive-owned Gothic cover or directed primitive flow;
- the terminal Fejer epochs (m=3,2,1);
- a global birth, final, or terminal ledger;
- an arbitrary horizon, arbitrary history, or compatible infinite family;
- C058, Q1, Q2, publication novelty, or prize eligibility.

## 7. Replay

From `route_probes/`:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  ROUTE_C_EPOCH_BLOCK_FULL_PHASE_FEJER_MASTER_test.py

PYTHONDONTWRITEBYTECODE=1 python3 \
  ROUTE_C_EPOCH_BLOCK_FULL_PHASE_FEJER_MASTER_certificate.py \
  --verify ROUTE_C_EPOCH_BLOCK_FULL_PHASE_FEJER_MASTER_certificate.json \
  --self-check
```

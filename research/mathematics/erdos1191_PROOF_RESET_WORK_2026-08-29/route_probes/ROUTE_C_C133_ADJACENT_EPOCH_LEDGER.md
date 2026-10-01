# Route C: C133 exact adjacent epoch-8/epoch-16 ledger

Date: 2026-08-31 (Asia/Tokyo)  
Status: `FORMAL_FINITE_ADJACENT_EPOCH_LEDGER_CLOSED_C058_OPEN`

## 1. Frozen finite statement

Let the three consecutive spatial prefixes be `A8,A16,A32`.  At the four
active widths `t,2t,4t,8t`, write

\[
\Delta_{8,s}=C_{16,s}-C_{8,s},\qquad
\Delta_{16,s}=C_{32,s}-C_{16,s},
\]

\[
O_{P,s}=C_{P,s}-C_{P,s+1},\qquad
S_{e,s}=\sum_{u=0}^{s}c_{e,u}.
\]

Over an arbitrary commutative ring, the exact ledger is

\[
\begin{aligned}
&w_8\sum_{s=0}^{3}c_{8,s}\Delta_{8,s}
 +w_{16}\sum_{s=0}^{3}c_{16,s}\Delta_{16,s}\\
={}&-\sum_{s=0}^{3}w_8S_{8,s}O_{8,s}\\
&+\sum_{s=0}^{3}(w_8S_{8,s}-w_{16}S_{16,s})O_{16,s}\\
&+\sum_{s=0}^{3}w_{16}S_{16,s}O_{32,s}\\
&+w_8S_{8,3}\Delta_{8,4}+w_{16}S_{16,3}\Delta_{16,4}.
\tag{1}
\end{aligned}
\]

The last two terms are the explicit upper scale terminals at width `16t`.
The ledger therefore has exactly fourteen formal keys: four initial `A8`
bands, four shared `A16` bands, four final `A32` bands, and two upper
terminals.

Two separate one-edge expansions have eighteen occurrences.  Their only
duplicate physical keys are the four `A16` bands.  For every `s`, the old
final and new initial occurrences combine as

\[
+w_8S_{8,s}O_{16,s}-w_{16}S_{16,s}O_{16,s}
=(w_8S_{8,s}-w_{16}S_{16,s})O_{16,s}.
\]

Thus `A16` is one net row, not two independently spendable rows.

## 2. Formal verification and C103 correspondence

Lean 4 proves (1) as

`Erdos1191.adjacentEpochTwoEdgeFourScaleLedger`

in `lean_kernel/Erdos1191/AdjacentEpochLedger.lean`.  It is the fully
expanded `L=0,m=1,n=4` specialization of C103's
`finiteEpochScaleAbel_transport_fromPotential`:

- `C 0=A8`, `C 1=A16`, `C 2=A32`;
- the single interior epoch term is exactly the net `A16` row;
- the two members of `Finset.range (m+1)` are the two upper terminals.

The pinned Lean 4.33.0 project builds cleanly.  `lean_verify` reports only
`propext`, `Classical.choice`, and `Quot.sound`, with no suspicious source
pattern.

## 3. Physical coordinate ownership is a separate layer

For the two direct demands, use the 100 coordinates

\[
\{(r,2^\ell):7\le r\le31,\ 0\le\ell\le3\}.
\]

The past-owner convention is

\[
\operatorname{owner}(r,2^\ell)=
\begin{cases}
\mathrm{pre8},&r=7,\\
8,&8\le r\le15,\\
16,&16\le r\le31.
\end{cases}
\]

The three fibers have sizes `4,32,64`.  In particular all four rank-15 rows
belong to epoch 8 exactly once.  No `right-zero` condition is used.  C111's
formal owner-fiber theorem then recovers the full quadratic energy from these
three coordinate fibers.

The prefix-band ledger and the physical coordinate owner map are different
bookkeeping layers.  The shared `A16` band has one net Abel coefficient,
whereas the shared physical rank 15 is past-owned by epoch 8.  Neither fact
may be substituted for the other.

## 4. Exact claim boundary

C133 closes the minimal finite algebraic stitch only.  It does not provide:

1. a nonanticipating phase rule on every compatible history;
2. a unique-birth decomposition of the actual signed Gothic/Gram demand;
3. a master paying all fourteen rows with the required signs;
4. a fresh epoch-16 factor on ranks 15--31;
5. cutoff, diagonal-completion, carrier, or other residual payment;
6. arbitrary-rank or full-phase uniformity.

Consequently C133 does not prove a local master inequality, C058, Q1, Q2,
publication novelty, or prize eligibility.  The global state remains
`UNRESOLVED_AT_HARD_LIMIT`.

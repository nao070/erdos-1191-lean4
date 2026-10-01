# Route C: exact 26-channel four-owner cross-scale no-go

Date: 2026-08-30  
Status: `EXACT_FIXED_FOUR_OWNER_NONNEGATIVE_CROSS_ROOTS_EXCLUDED_C058_OPEN`

This is the owner-separated falsification gate requested after C097--C100.
It keeps four direct-demand ledgers separate, deduplicates their physical Haar
channels, and charges every owner-labelled root coefficient at its full
physical price.  The exact full LP and the LP with every unequal-width root
removed have the same optimum.  A strict dual margin forces every cross-scale
root to vanish on the optimal face.

The result is a fixed finite no-go for nonnegative globally owner-labelled
root pieces.  It is not a signed Abel--Gothic master, not a continuum-phase or
common-history result, and not a proof of C058 or either Erdős question.

## 1. Physical channel census

On

\[
 a_k=k(k+100),\qquad 0\le k\le15,
\]

use the normalized channels

\[
 \phi_{T,k}(x)={g_T(x-a_k)\over\sqrt{2T}},
 \qquad k=3,\ldots,15,\qquad T\in\{200,800\}.
\]

At either width, the `n=4` and `n=8` owner lists share the channel based at
`a_7`.  The 28 owner occurrences therefore reduce to 26 physical identities:
13 at each width.  Keeping 28 independent identities would manufacture two
zero-cost roots between duplicate channels.

The 65 nominal events have one collision,

\[
 a_5+1600=a_{15}+400=2125,
\]

so there are 64 distinct finite events and 63 positive-length common cells,
plus the two zero exterior cells.  The root census is

\[
 {26\choose2}=325,
 \qquad156\text{ same-scale},
 \qquad169\text{ cross-scale}.
\]

For every pair `e=(i,j)`, the certificate checks

\[
 p_e=\sum_c|c|(z_{c,i}-z_{c,j})^2
\]

against the independent oriented C091 mixed-Haar formula.  All 325 equalities
hold exactly.

## 2. Four separately owned demand ledgers

The owners are

\[
 (4,200),\ (8,200),\ (4,800),\ (8,800).
\]

For every owner `o` and physical root `e`, introduce `x_(o,e)>=0`.  Put

\[
 q_e=\sum_o x_{o,e},\qquad
 P_{o,c}=\sum_eR_{c,e}x_{o,e},\qquad
 R_{c,e}=(z_{c,i}-z_{c,j})^2.
\]

The owner rows are kept separate:

\[
 P_{o,c}\ge D_{o,c}
 \quad\text{for every one of the }4\cdot63=252\text{ rows}.
\]

The physical objective is

\[
 \sum_{o,e}p_ex_{o,e}=\sum_ep_eq_e.
\]

Thus a unit assigned to two owners is paid twice; a single physical price is
never credited as a full correction in several ledgers.  The full model has
1,300 owner-root variables and 1,300 exact dual-column checks.  The no-cross
model has 624 variables.

## 3. Exact primal--dual values

| owner | integrated demand | full optimum | no-cross optimum | minimum cross margin |
|---|---:|---:|---:|---:|
| `(4,200)` | `63/640` | `29/200` | `29/200` | `161/300` |
| `(8,200)` | `169/12800` | `139/3200` | `139/3200` | `21/100` |
| `(4,800)` | `0` | `0` | `0` | `41/40` |
| `(8,800)` | `361/5120` | `59841/512000` | `59841/512000` | `29/100` |

Consequently

\[
 \boxed{E_{\rm full}=E_{\rm no\text{-}cross}={156321\over512000}.}
\]

The total integrated demand and unavoidable cover surplus in this model are

\[
 \mathcal D={4663\over25600},\qquad
 E_{\rm full}-\mathcal D={63061\over512000}.
\]

One exact optimal primal uses only the following same-scale roots:

| owner | positive roots |
|---|---|
| `(4,200)` | `(0,2)=(2,4)=1/40` |
| `(8,200)` | `(4,6)=(10,12)=1/128` |
| `(4,800)` | none |
| `(8,800)` | `(17,18)=(24,25)=13/512,49/640`; `(17,19)=(23,24)=131/2560` |

All 252 primal rows, all 1,300 dual columns, both objective values, and
complementary slackness are replayed with exact rational arithmetic.

## 4. Cross-root essentiality gate

Let

\[
 m_\times=\sum_o\sum_{e\ {\rm cross\ scale}}x_{o,e}.
\]

On the full optimal face,

\[
 \boxed{\min m_\times=0.}
\]

and the displayed exact dual is strictly feasible on all
`4*169=676` owner-labelled cross-root columns.  The minimum witnesses are:

- `(4,200)`: root `(0,13)`, margin `161/300`;
- `(8,200)`: root `(6,13)`, margin `21/100`;
- `(4,800)`: roots `(9,17)` and `(10,18)`, margin `41/40`;
- `(8,800)`: roots `(9,19)` through `(9,22)`, margin `29/100`.

Since every margin is positive, complementary slackness forces every
cross-scale coefficient to zero in every primal optimum paired with this
optimal dual.  A merely sparse displayed primal is not being used as the
essentiality argument.

## 5. Caveat and C058 consequence

The owner `(4,800)` has zero demand on all 63 cells: width 800 exceeds the
440-span of the five-point block and only zero-energy ordered states occur.
The fixture therefore has four named ledgers but only three active demands.
This caveat is machine-visible in the certificate.

The exact conclusion is limited to nonnegative globally owner-labelled graph
roots.  It does not test arbitrary signed shares, indefinite cross blocks,
aggregate columns, other width ratios, continuum phase, compatible histories,
or the full boundary/terminal ledger.  In particular it cannot replace the
one-for-one `2M=lambda` Gothic accounting.

The negative gate sharpens the next C058 target: use whole signed rows and an
explicit directed source-to-sink flow, retain every initial/final/active-gate
and scale-terminal row, charge physical excess only once, and optimize the net

\[
 \Phi=G_{\rm off}^{\rm owned}
 -(P_{\rm phys}-D)-\operatorname{terminal}^{\rm owned}.
\]

A useful positive finite result must have `Phi>0` and must retain strictly
positive cross/current-to-past flow on the whole optimal face.  Neither fact
is supplied here.  C058, Question 1, Question 2, publication novelty, and all
prize claims remain open.

Replay with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B -m unittest -v \
  ROUTE_C_FOUR_OWNER_CROSS_SCALE_LP_test.py
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  ROUTE_C_FOUR_OWNER_CROSS_SCALE_LP_certificate.py \
  --verify ROUTE_C_FOUR_OWNER_CROSS_SCALE_LP_certificate.json --self-check
```

The current semantic payload SHA-256 is
`10e944762044c0c0da499bc9c68723aefac953c14805f00412190d3bfa7b4956`.

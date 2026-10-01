# A29: exact forbidden-output packing in four prescribed cells

2026-09-09. Every requested equality and upper-bound chain is PASS.
Only (b,k)=(24,47),(24,48),(25,47),(25,48) was evaluated, using the
existing certified C=1,m0=2 variant M=T=96 history. No new history,
broader scan, full-horizon profile recomputation or Lean run occurred.

## Actual sets and certified strict cutoff

For each cut, D is the actual positive-difference set of the first b-1
points, H=H_b, and S=sum_(d in D)d^2. The existing independent fixed-point
logarithm interval gives rational enclosures for

    L_b=b^2/(log b)^5.

Both enclosure endpoints have floor1 in both cases. Therefore the
strict integer threshold is certified as ell=floor(L_b)+1=2, with
UNKNOWN=0. The full rational intervals are saved in the exact JSON.

| b | H | S | card D | ell | card U |
|---:|---:|---:|---:|---:|---:|
| 24 | 713 | 21743814 | 253 | 2 | 459 |
| 25 | 773 | 28686807 | 276 | 2 | 496 |

Here U={ell,...,H-1} minus D, formed from the actual integer labels.
The exact data bind every forbidden difference to its unique old
endpoint pair. Every future pair among ranks b+1,...,k was checked
directly: its positive difference is unique among those future pairs
and is disjoint from D.

## The exact cumulative formula

Let h=binom(k-b,2). Select the smallest min(h,card U) elements of U.
For an integer j between ell and H-1, the number of selected elements
at most j is exactly min(h,card(U intersect[ell,j])). Thus finite
interchange, with H-u counting integers j=u,...,H-1, gives

    F_D(h)=sum_(selected u)(1-u/H)
      =(1/H)sum_(j=ell)^(H-1) min(h,card(U intersect[ell,j])). (1)

Both sides were computed exactly and agree in all four cells. The
complete U, selected labels, cumulative counts and summands are saved.
This is the packing bound for one common forbidden set D; different
thresholds in (1) are not independent budgets.

## Exact actual-core and output-kernel chain

Let L be the actual future-output kernel sum over differences t>=ell,
using (1-t/H)_+. Let F be the old A28 packing bound that allows the
forbidden labels as well. Q is the sum d*e over original strict-core
records covering b and with upper output rank r<=k. Each physical
record is counted once in its cell. No BH-only restriction is made.

All retained original records pass the existing independent strict-gate
functions. At each actual output, no larger source label is duplicated.
The exact comparisons are

    Q<=S L<=S F_D<=S F.                              (2)

| b | k | h | Original core records | Q | L | F_D | F |
|---:|---:|---:|---:|---:|---|---|---|
| 24 | 47 | 253 | 3155 | 179039739 | 30861/713 | 108090/713 | 148005/713 |
| 24 | 48 | 276 | 3254 | 185480132 | 31898/713 | 113306/713 | 158286/713 |
| 25 | 47 | 231 | 3568 | 241829853 | 34063/773 | 114898/773 | 151536/773 |
| 25 | 48 | 253 | 3686 | 250572623 | 35280/773 | 121572/773 | 163185/773 |

The corresponding exact genuine component coefficients are

    k=47: kappa_47/H_47^2=1/934509479323392, H_47=4039;
    k=48: kappa_48/H_48^2=1/1148518878296832, H_48=4248.

The JSON records all four entries of (2) as exact rationals, and also
all four after multiplication by their cell's genuine coefficient.
It does not substitute alpha_k/H_k^2 or reset any terminal alpha.
The H appearing inside the output kernel remains H_b, not H_k.

## One future-point addition at each fixed cut

Put E=F_D-L. The two specified additions k47->48 give

| b | E at47 | E at48 | Delta F_D | Delta L | Delta E |
|---:|---|---|---|---|---|
| 24 | 77229/713 | 81408/713 | 5216/713 | 1037/713 | 4179/713 |
| 25 | 80835/773 | 86292/773 | 6674/773 | 1217/773 | 5457/773 |

Both deficit increments are strictly positive in these two tests.
This is not a proof of general monotonicity.

The new actual future bank is exactly the differences a_48-a_i, with
i=25,...,47 at b24, or i=26,...,47 at b25. These have23 and22 labels
respectively and no overlap with the previously existing future bank
or old forbidden D. The b25 new bank is the b24 bank with the one
label3475=(a_48-a_25) removed; their common labels are the same actual
physical differences, not separately generated resources.

Only three new labels have positive kernel at either cut:

| Difference | Actual endpoint ranks |
|---:|---|
| 209 | (47,48) |
| 344 | (46,48) |
| 549 | (45,48) |

All remaining new labels are at least960, exceeding both H_b values.
Thus Delta L equals(504+369+164)/713=1037/713 at b24 and
(564+429+224)/773=1217/773 at b25. The corresponding new virtual
packing slots are23 and22 explicitly saved allowed integers; their
kernel sums are5216/713 and6674/773. Subtracting gives the displayed
exact Delta E values.

These are increments of the unpriced kernel deficit at fixed b.
The genuine coefficients change between k47 and k48, so a sign claim
for a different price-weighted quantity is not inferred from them.

## Evidence, logical role and next action

A29_forbidden_output_packing_four_cells.py is the one bounded check.
A29_forbidden_output_packing_four_cells_exact.json stores the actual
prefix, old/future endpoint maps, certified logarithm intervals,
allowed and selected integer labels, original record IDs and rows,
all exact chains, prices and the two new-point banks. The companion
manifest binds these files to the original M96 certificate and prior
source hashes. No previously certified history or evaluator was edited.

The forbidden-label improvement is strictly visible in these four
cells, and (1)-(2) are exactly consistent with their actual records.
The two tested E increments are positive; monotonicity, a weighted
increment bound and a uniformly summable loss estimate remain
unproved. None of these finite values refutes or proves frozen U4-F
or original Q1.

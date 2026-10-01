# A50: exact moving-cut bank, normalized failure, selector and price failures

Date: 2026-09-09. Status: reference and independent bounded checks PASS.

Use only the certified C=1,m0=2,M=T=96 variant, the fixed larger source
(x,y)=(1,22),d603, integer labels297,...,329, and component/output cutoff
v=48. Evaluate cuts23,...,47. Both source and output differences were
looked up forward and independently backward from the existing integer
points. No new source/bin/history or full-profile enumeration occurred.

For each cut, the raw bank is exactly

    B_b=603 sum_{e with an actual source(w,z), z<b} e.

It includes source-overlap labels and labels with no usable output.
Those exclusions have separate flags. An absent source label never
enters the bank; an absent output is given neither a rank nor a price.
All original strict inequalities are fixed independently of the cut.
Their exact rational margins and independent fixed-point decisions
are saved. UNKNOWN comparisons: zero.

## Three original strict records, including the earlier retiring one

The only original strict records with r<=48 among these 33 labels are

    e302: [603,302,1,22,18,23,23,22,39,41,301], de182106,
    e312: [603,312,1,22,10,19,22,19,42,43,291], de188136,
    e318: [603,318,1,22,7,18,22,18,25,28,285], de191754.

Their respective original cut intervals are24,...,38; 23,...,41;
and23,...,24. The e318 record retired at cut25 in A47, but is present
at cuts23/24 here. The initial parent prediction omitting it was a
prediction only; the following independently checked values supersede it.
The e299 candidate fails the original birth/output-gap inequality and
is not silently included.

## Raw and normalized quantities

Put Q_b=sum de over the three original records active at b, D_b=B_b-Q_b.
At each adjacent step, let A be the original active weight newly born
from source birth c=b, R the original weight retiring at i=b+1, and
DeltaB the weight of newly available bank labels with source upper z=b.
All 24 steps satisfy exactly

    DeltaQ=A-R,
    DeltaD=DeltaB-A+R,
    DeltaB-A>=0,  R>=0.

Thus raw D is nondecreasing in this finite scope. The full25-cut trace
records B,Q,D,D/B, each birth/retirement, and both genuine prices.

| cut b | B | Q | D | exact D/B |
|---:|---:|---:|---:|---|
| 23 | 2056230 | 379890 | 1676340 | 278/341 |
| 24 | 2238336 | 561996 | 1676340 | 695/928 |
| 25 | 2427075 | 370242 | 2056833 | 3411/4025 |

At23->24, only e302 enters the bank, and its full de182106 is already
an active original record. There is no retirement. Raw D stays constant
but its denominator increases, giving

    Delta(D/B)=-20989/316448<0.

This is the sole normalized decrease in the requested cut range. At
every step the checker also verifies

    Delta(D/B)=(B*DeltaD-D*DeltaB)/(B*(B+DeltaB)).

Raw monotonicity therefore does not imply normalized monotonicity.

## The full displayed A46.6 selector is a different quantity

The optional selection checks every displayed A46.6 condition, plus the
original all-three-old-gaps-large flag, on these same originally active
records. It is not merely the central/near predicate. Independent rational
log intervals give

    J23=30, J24=31,
    L23=126, L24=135,

where J_b=floor(b^2/log^(5/2)b) and L_b=floor(b^2/log^(5/4)b).
The e318 quadruple uses the actual variant values (1,33,351,604), hence
gaps(32,318,253), earlier source birth s18 and output difference285.
The other earlier source births are s22 for e302 and s19 for e312.
All explicit small-label/gap and source-birth inequalities are saved,
including the powered rational check of
s>b/[sqrt(2) log^(9/8)b]. No values from a different fixture were used.

The applicability conditions for the displayed A45/A46 implications
hold at both cuts: M>=m0, b>=max(3,m0), and each earlier source birth
is >=m0. The same fixed all-rank cap certificate applies. Neither an
initial-cut nor an early-source exception is being ignored. Passing
these necessary conditions is not asserted to prove nonmembership in
every other historical paid subset or to solve the global remainder.

At cut23 the component k48 fails the central-below-far condition, so no
original record is selected. At cut24 all three records pass every
displayed condition. The two old active records e312/e318 enter solely
because the selector changes, in addition to original source birth e302.
For the separate quantity D_selected=B-Q_selected,

    D_selected(23)=2056230,
    D_selected(24)=1676340,
    Delta D_selected=-379890.

This coexists with raw DeltaD=0. The selector entries are separately
recorded and are not counted as new original source records. Full cut
flags and later selector exits are in the evidence. Raw monotonicity
cannot be transferred to a selector that admits existing records.

## A moving-cut auxiliary price also breaks monotonicity

The original component price throughout the raw trace is
lambda48=1/1148518878296832. Separately, each of the three actual records
has its genuine full u_r^[96], with r28,41,43. These were independently
checked from alpha_k-alpha_(k+1), preserving alpha97.

Let P_b be the full-price sum only for the fixed original record subset
with r<=48, not a claim about the entire bin through T96. Its component
expansion keeps Q_b(min(k,48)) and the original prices for k>48.
Consider the distinct auxiliary expression

    F_b=B_b*u_(b+1)^[96]-P_b.

The first step in the saved trace with unchanged B and unchanged P is
25->26. Here B=2427075 and the active labels remain e302/e312. Exact
direct tails and an independent alpha-difference calculation certify

    lambda26=2/4894165648125,
    F26-F25=-lambda26*2427075=-21574/21751847325<0.

This step uses lambda26, not lambda48. The term B_b*u_(b+1) is an
auxiliary upper allowance; unused labels have not acquired genuine
output prices. The full exact P, u26/u27, F25/F26 are preserved in JSON.
Raw-bank monotonicity does not establish monotonicity of this moving
price allowance. The separately proposed source-birth-fixed allowance
is not this expression and is not tested by this counterexample.

## Scope and restart

Evidence: `A50_CUT_BANK_EXACT.json`, the independent check, and
`A50_AUXILIARY_CUT_COUNTEREXAMPLES.json`. All33 label lookups, 25 cuts,
24 original increment identities, the displayed-selector decisions,
and the first moving-price failure are certified within the stated
existing history. There is no additional search, full profile rebuild,
or Lean claim here. Hashes are in `A50_review_manifest.json`.

The counterexamples reject normalized, selector-transferred, and
moving-price monotonicity shortcuts. They do not refute the original
raw identity, a source-birth-fixed potential, U4-F, or Q1. A uniform
norm is not obtained. The next bounded mathematical review concerns
the separately defined birth-price compensation and a common activation
for this particular monotone-threshold selector. This finite task is
complete; no process or finite search remains running.

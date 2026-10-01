# A32 independent review: past and mixed forbidden labels

Date: 2026-09-09. Status: PASS for the eight prescribed exact cells;
the proposed lower bound of immediate deletion loss by total new mixed
kernel mass is FALSE in the existing actual Sidon history.

## Fixed scope and definitions

The only history is the already certified C=1, m0=2 variant M=T=96.
The cells are b in {24,25} and v in {29,30,47,48}. No history was
generated and no full profile was recomputed. Original strict-core
rows, their source-bank indices, and the certified strict thresholds
ell=2 were reused from the A29 exact evidence. Its original row pool
had already been checked with the independent strict-condition checker.

At a fixed cell let H=H_b, D=Delta(first b-1 points), S=sum_D d^2,
P=first b points, F=points b+1 through v, and

    Bbank = Delta(P) union {a_f-a_p : p<=b<f<=v},
    U = {ell,...,H-1} minus Bbank, h=binom(v-b,2),
    phi(t) = max(0,1-t/H) for t>=ell.

All actual positive differences of the three disjoint endpoint-pair
classes (past/past, past/future, future/future) are unique and disjoint,
as directly verified here. The future-internal eligible labels thus
belong to U. The source D is unchanged: it uses b-1 old points, whereas
the enlarged forbidden bank uses b past points. This distinction is
intentional.

F_U(h) is the sum of phi over the first min(h,card U) allowed integers.
For each cell both this definition and the independent cumulative
formula

    H F_U(h) = sum_{j=ell}^{H-1} min(h,card(U intersect [ell,j]))

were evaluated exactly and agreed. With L the actual future kernel
sum and Q the sum of original strict-core de at this cut through r<=v,
all eight chains

    Q <= S L <= S F_U(h) <= S F_D(h)

passed over rational numbers. Every inequality was also retained
after multiplication by the genuine component kappa_v/H_v^2.

## Exact results

At b24, H=713 and S=21743814; at b25, H=773 and S=28686807.
The table lists numerators for kernel quantities, all over H.

| b | v | h | card U | core rows | Q | H L | H F_U | H F_D | H(F_U-L) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|24|29|10|392|555|29828541|5004|6649|6671|1645|
|24|30|15|389|789|42481454|7256|9813|9859|2557|
|24|47|253|388|3155|179039739|30861|103016|108090|72155|
|24|48|276|388|3254|185480132|31898|107303|113306|75405|
|25|29|6|436|408|25044908|3634|4421|4421|787|
|25|30|10|431|664|42546350|5900|7249|7263|1349|
|25|47|231|427|3568|241829853|34063|111260|114898|77197|
|25|48|253|427|3686|250572623|35280|117245|121572|81965|

The genuine component coefficients at v=29,30,47,48 are respectively
1/7739391240000, 1/9623249307000, 1/934509479323392,
and 1/1148518878296832. They are kappa_v/H_v^2, not alpha_v/H_v^2.

## Four exact increments and the rejected candidate

For v to v+1, put m=v-b, h'=h+m. Let C be the b new mixed labels,
J the actual new future kernel sum, and

    A=F_Uold(h')-F_Uold(h),
    R=F_Uold(h')-F_Unew(h'), E=F_U(h)-L.

All four identities Delta E=A-R-J passed exactly. The following entries
are numerators over H_b.

| b | v to v+1 | H A | H R | H J | H Delta E | H sum_C phi |
|---:|:---:|---:|---:|---:|---:|---:|
|24|29 to 30|3164|0|2252|912|327|
|24|47 to 48|4287|0|1037|3250|0|
|25|29 to 30|2828|0|2266|562|845|
|25|47 to 48|5985|0|1217|4768|0|

At b24, point 30 adds eligible mixed labels {547,608,657}, with total
kernel mass 327/713. At b25 it adds {487,547,608,657,721}, with mass
845/773. In both cases none of these labels belongs to the old selected
set at the new capacity, so R=0 exactly. Thus the immediate inequality
R >= sum_C phi is false in an actual fixed-cap history. The general
valid direction is 0<=R<=sum_C phi: remove the deleted labels from an
old optimizing subset; the retained subset remains admissible for Unew.

The actual new-point difference bank is stored once per new rank
(30 or 48), with endpoint maps. At each cut its disjoint parts are
C={a_new-a_p:p<=b} and the m future-internal differences. Changing the
cut changes this partition of the same physical bank; it does not
create independent budgets. At rank48 the only positive eligible
new future labels are 209,344,549, with endpoint pairs (47,48), (46,48),
(45,48). All newly mixed labels exceed H for both cuts.

The four positive Delta E values establish no general monotonicity.
They are unpriced fixed-cut increments; the cell coefficients vary
with v, so their signs do not automatically describe a different
price-weighted increment.

## Evidence and remaining gap

A32_joint_forbidden_eight_cells.py is the bounded reference calculation.
A32_joint_forbidden_eight_cells_exact.json stores every actual pair
bank, allowed/selected labels, cumulative terms, original core indices,
exact chains, genuine prices, and increments. The companion manifest
binds source hashes and the unchanged A29 strict certificates. No new
independent full-horizon certification is claimed.

This improves a valid component majorant and rejects immediate payment
of all new mixed mass. It does not prove uniform U4-F, refute Q1, or
bound the sum over cuts. The next distinct question is how the same
deleted label's penalty grows with later component capacity, while
retaining its single physical identity and both horizons.

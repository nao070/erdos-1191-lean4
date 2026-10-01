# A53: a uniformly paid tail relative to each actual source birth

Date: 2026-09-09. Independent hand-proof review: PASS.

Fix p>1/2. For each original six-endpoint strict record let
c=max(y,z)>=4 be its source birth, and set

    L(c)=ceil(c(log c)^p)+1.

Select only its genuine components k>=L(c). Its selected price is

    sum_{k=max(r,L(c))}^M kappa_k/H_k^2,

with an empty range giving zero. This is a component selector attached
to the physical record. The original output horizon T, original strict
gates, cut interval, and alpha_(M+1) are retained. No value at rank L(c)
is accessed if L(c)>M.

## A genuine fresh-source bound

Let D_c be the actual positive difference bank of the first c points,
F_c=sum_{d>e in D_c}de. Actual Sidon uniqueness gives the disjoint union
of D_(c-1) and the c-1 new labels a_c-a_j. Write U_old for the old label
sum, G_new for the new label sum, and S_new for their squared sum. Then

    DeltaF_c=U_old G_new+(G_new^2-S_new)/2.

Actual endpoint bounds give U_old<=(c-1)^2 H_c/4,
G_new<=(c-1)H_c, and S_new>=0. Hence

    DeltaF_c <= (c-1)^2(c+1)H_c^2/4
             <= c^3 H_c^2/4.

Each physical record at birth c injects into one of these source pairs;
the unique positive output difference recovers its output endpoints.
Thus the total de of all such original records is <=DeltaF_c. There is
no independent budget for repeated cuts or different physical outputs
of the same source pair.

If L=L(c)<=M, then L>c and width monotonicity gives

    u_L^[M] <= (alpha_L-alpha_(M+1))/H_L^2
             <= 1/[c^4(log c)^(4p) H_c^2].

Use L-1=ceil(c(log c)^p)>=c(log c)^p and
alpha_L=1/[L^2(L-1)^2]<=(L-1)^(-4). The selected birth-c price mass
is consequently at most 1/[4c(log c)^(4p)]. This bounds a real finite
genuine tail; it does not change the final coefficient.

## Birth-block price is paid once, then its exact cut support is used

For c in [2^ell,2^(ell+1)), ell>=2, let E_ell be the sum of the
selected prices times de over all original records in that birth block,
each physical record counted once. Since the bin has 2^ell integers,

    sum_{c=2^ell}^{2^(ell+1)-1}1/c<=1,
    E_ell <=1/[4(ell log2)^(4p)].

Every covered cut of these records satisfies

    2^ell<b<2^(ell+1)(ell+1)log2.

The lower bound follows from c<b. The upper bound follows from the
original strict r<c log c and b<i<r. It is independent of the component
index, so k>T tail terms preserve the same cut support.

The profile of this block at any cut is at most E_ell. For an integer
A=2^ell and real U=2^(ell+1)(ell+1)log2,
sum_{A<b<U}1/b<=log(U/A), by integrating 1/x over [b-1,b]. There is
no extra endpoint term because the lower cut inequality is strict.
Therefore its square-root harmonic norm is at most

    sqrt(E_ell)*log(2(ell+1)log2).

Square-root subadditivity between birth blocks proves, uniformly over
every original finite M,T,

    N_selected <= 1/[2(log2)^(2p)]
       *sum_{ell=2}^infinity log(2(ell+1)log2)/ell^(2p) < infinity.

Convergence follows from 2p>1. The last infinite sum is a numerical
majorant of a finite-history sum, not an assumed infinite capped
history. No cap is used anywhere in this subclass proof.

## Stronger remaining birth support

For the same p and c<b, the function x(log x)^p is increasing on x>=4,
so L(c)<=L(b). Thus this paid class contains the earlier cut-relative
A42 tail; it can also pay components excluded from that earlier class.

An unpaid integer component satisfies k<L(c). It follows that
k-1<c(log c)^p. Original causal endpoints give k>c+1, hence
log(k-1)>log c>0. Therefore, strictly,

    c>(k-1)/(log(k-1))^p.

One may fix p=5/8. This is a new necessary condition on the remaining
original class, not a changed core definition. The selected components
keep the physical record's original cut interval; the selection here
depends on c and k, not on b. Previous cut-dependent selectors must
still stay inside their component sums when combined with it.

This proves a noncircular uniform subclass estimate and narrows the
remaining problem. It does not prove the norm of that complement,
CoreUniform, or Q1. Full Lean formalization is not claimed here. The
separate finite applicability/restart witness checks use existing
certified records only; they are not premises of this hand proof.

## Separate finite applicability and the next surviving record

At p=5/8, two independent rational log enclosures certify L(22)=46 and
L(23)=48. Thus all three saved A50 records at component k48 are paid:
e312/e318 have birth22, and e302 has birth23. These are source-birth
thresholds, not the thresholds at their varying covered cuts.

A separately authorized single pass over the original certified M96
record bank, filtering r<=48 and testing original covered cuts in
increasing order, stopped immediately at bank index1487 and cut25:

    [215,174,14,19,21,24,24,19,27,28,41], k48,
    old quad values (186,401,540,714), gaps(215,139,174),
    birth c=max(19,24)=24, L(24)=51, de37410.

All original strict gates, six endpoints, the full displayed A46.6
selector plus original all-large condition, and k48<L(24) are verified
by independent rational log and actual endpoint checks. The source birth
is 24, not the upper endpoint19 of the numerically larger source d215.
The original coverage is25,...,26, and the tested cut is25.

The pass visited1488 stored rows, of which1355 had r<=48;1199 were
already paid by the new birth tail. It tested1324 candidate covered cuts
and had zero UNKNOWN comparisons before stopping. This is a new single
restart witness, explicitly separate from A50's fixed33-label trace.
It is not a profile recalculation or another history campaign.

The evidence stores lambda48, the original u28^[96], and its A53-only
paid/unpaid split separately. The A53-unpaid part is not asserted to
pass the cut-dependent A46 selector at every component. A54 adds only
one birth-span flag to this same witness, without a new record scan.
All supporting hashes are in `A51_A54_review_manifest.json`.

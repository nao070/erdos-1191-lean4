# A36 independent review: one mixed pair across its cuts

Date: 2026-09-09. The bounded actual check and the fixed-threshold
relative-penalty theorem below PASS. Three stronger monotonicity
candidates are FALSE. All computations use the existing C=1,m0=2
variant M96; no history or whole profile was generated.

## The one physical pair and the exact prebank

The source has a_24=714, a_30=1261, hence the specified label is
c=547=a_30-a_24, with (p,f)=(24,30). Its eligible cuts are precisely
b=24,...,29. The original threshold ell_b was certified to equal 2
at all six cuts by rational log intervals, then independently by
50-term fixed-point intervals. There were zero UNKNOWN comparisons.

The canonical sequential bank before deleting this pair is exactly
the complement in [ell_b,H_b-1] of

    D_b^-={a_y-a_x:1<=x<=b, x<y<f}
            union {a_f-a_q:1<=q<p}.               (1)

The first set combines the initial past-internal bank with every
earlier-birth mixed pair; the second lists preceding pairs with the
same future birth f. All physical labels are distinct by Sidon.
Labels outside the eligible universe have no deletion effect. The
independent checker constructed (1) directly and verified equality
with the reference's sequential prebank, including the allowed label
list, the target's 1-based rank r_b and the pre-deletion size N_b.

| b | H_b | S_b | r_b | N_b | h at v47 | h at v48 | h at v60 |
|---:|---:|---:|---:|---:|---:|---:|---:|
|24|713|21743814|278|390|253|276|630|
|25|773|28686807|274|433|231|253|595|
|26|909|37125600|271|541|210|231|561|
|27|1017|49613113|269|625|190|210|528|
|28|1058|65986250|268|656|171|190|496|
|29|1230|83995000|268|807|153|171|465|

Here S_b is the squared-difference sum of the first b-1 points and
h=binom(v-b,2). All twelve prescribed v47/v48 cells have h<r_b,
so p_b=H_b p_b=S_b p_b=0. Accordingly only the six explicitly
authorized v60 cells for this same pair were added.

## Exact counterexamples at v60

Let p_b denote the deletion penalty and rho_b=p_b/(1-c/H_b).
The additional values are

| b | p_b | H_b p_b | S_b p_b | rho_b |
|---:|:---|---:|:---|:---|
|24|166/713|166|3609473124/713|1|
|25|226/773|226|6483218382/773|1|
|26|362/909|362|4479822400/303|1|
|27|115/339|345|5705507995/339|69/94|
|28|307/1058|307|10128889375/529|307/511|
|29|9/41|270|755955000/41|270/683|

Thus all three proposed global cut-nonincreasing quantities fail
already at b24 to b25:

    Delta p=32820/551149>0,
    Delta(H p)=60>0,
    Delta(S p)=1832411981514/551149>0.

Moreover b26 to b27 has Delta p<0 and Delta(H p)=-17, but
Delta(S p)=23345458765/11413>0. Source weighting can defeat even a
decrease in the unweighted penalty. These are actual finite
counterexamples to the named monotonicity candidates only.

Every cell retains its original component coefficient k=v:

    lambda_47=1/934509479323392,
    lambda_48=1/1148518878296832,
    lambda_60=1/10659568914462735.

The exact priced p, H p and S p values are saved. At fixed v the same
positive coefficient is used at all cuts, so the counterexample signs
also persist after multiplying by that genuine coefficient. No
alpha_{M+1} or terminal price is modified.

The separate checker uses the closed endpoint bank, integer-prefix
counting instead of two packing sums, the variance identity instead
of squared-difference enumeration, independent logarithm intervals,
and 4/[v(v^2-1)^2 H_v^2] for the genuine coefficient. All 18 cells
passed. Existing full-history Sidon/cap certification was reused;
these are penalty checks, not another original-core enumeration.

## A valid fixed-threshold relative-penalty law

The following is a hand proof for any actual Sidon history. Fix one
integer threshold ell, a physical pair c=a_f-a_p>=ell, a horizon
v>=f, and consecutive eligible cuts p<=b<b+1<f with c<H_b.
Let A_b(x) be the number of allowed integers in [ell,x] in the
prebank (1), h_b=binom(v-b,2), and Z_b(x)=A_b(x)-h_b.

When b increases by one, the closed forbidden bank adds only

    G={a_y-a_{b+1}:b+1<y<f}, card G=f-b-2.

These labels are distinct and absent from the old forbidden bank.
For common x<=H_b-1,

    A_{b+1}(x)=A_b(x)-card(G intersect [ell,x]),
    h_{b+1}=h_b-(v-b-1),
    Z_{b+1}(x)>=Z_b(x)+(v-f+1)>Z_b(x).            (2)

For ell=1 all positive G labels satisfy its lower threshold. For a
larger fixed ell the intersection [ell,x] must be retained in the
exact equality; its cardinal bound is still at most f-b-2.

The exact integer-prefix representation of this single deletion is

    H_b p_b=sum_{x=c}^{H_b-1} 1[A_b(x)<=h_b].      (3)

It follows directly from the rank replacement formula: if h_b<r_b
the sum is zero; if r_b<=h_b<N_b it counts c through the integer
preceding the next selected label; if h_b>=N_b it equals H_b-c.

If the old penalty is not full, then h_b<N_b, so
Z_b(H_b-1)=N_b-h_b>0. By (2), the new Z is positive there and, by
monotonicity in x, on the entire newly added span as well. Thus no
new-span integers pay. On the common span its paying indicator can
only decrease, yielding H_{b+1}p_{b+1}<=H_b p_b. Since
H_{b+1}-c>H_b-c>0, (3) gives rho_{b+1}<=rho_b. If the old penalty
is full, rho_b=1 and the conclusion follows from rho_{b+1}<=1.

Therefore rho_b is nonincreasing across all eligible cuts for every
fixed threshold. Once a nonfull stage is reached, later stages are
also nonfull and both p_b and H_b p_b are nonincreasing; this does
not cover preceding full stages or imply source-weighted monotonicity.
The finite ell=2 sequence above is consistent with this theorem.

For moving thresholds ell and ell' at the two cuts, let tau be the
signed low-label change measured against the old closed forbidden bank:

    tau= card([ell',ell-1] minus D_b^-)  if ell'<ell,
    tau=-card([ell,ell'-1] minus D_b^-)  if ell'>ell,
    tau=0                              if ell'=ell.

On common x>=max(ell,ell') the exact formula becomes

    A_{b+1}(x)=A_b(x)+tau-card(G intersect [ell',x]),
    Z_{b+1}(x)>=Z_b(x)+(v-f+1)+tau.

The G labels are disjoint from D_b^-. Using the new threshold in its
intersection avoids double-counting deleted low labels. A rising
threshold can make tau negative, so the fixed-threshold monotonicity
argument cannot simply be reused. A37 pays the allowance error from
using the fixed auxiliary threshold 1 while preserving every original
strict-core condition.

## Evidence and logical boundary

The two small reference scripts, their twelve-cell and six-cell JSON
outputs, the separate checker, and its exact certificate are bound
by A36_A38_review_manifest.json. The first script was run once; its
all-zero result triggered the authorized six-cell extension. No other
pair, cut, horizon or new history was searched.

The relative-penalty theorem supplies a useful common-pair law. It
does not prove that the source-weighted loss is monotone, bound all
physical pairs jointly, or control the required square-root harmonic
core norm. Frozen U4-F and Q1 remain unresolved.

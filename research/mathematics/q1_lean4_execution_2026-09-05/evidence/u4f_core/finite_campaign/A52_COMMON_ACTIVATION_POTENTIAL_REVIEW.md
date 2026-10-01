# A52: one common activation and monotone subsequent deletion

Date: 2026-09-09. Independent hand-proof review: PASS.
No new finite search or Lean run.

Fix C>0, B=max(4,m0), a component k>=6, and v=min(k,T). Work on the
original available cuts B<=b<T, retaining all original strict records.
For b>=4, the following functions are nondecreasing:

    f(b)=b(log b)^(5/8),
    g(b)=b+floor(b/(log b)^(3/4)),
    L(b)=b^2/(log b)^(5/4),
    J(b)=b^2/(log b)^(5/2),
    h(b)=b/[sqrt(2C)(log b)^(9/8)].

This follows by differentiating the continuous factors. Their derivative
signs reduce respectively to log b+5/8, log b-3/4,
2log b-5/4, 2log b-5/2, and log b-9/8. All are positive at b>=4
since log4>5/4. The floor in g preserves monotonicity. The actual
quantity H_b(log b)^2 also increases with b.

Consequently the two record-independent conditions

    k<ceil(f(b))+1,     H_k<H_b(log b)^2

have a common one-time activation. Define a_k as the first integer
b in [B,v-2] satisfying both. If this interval is empty or no such b
exists, the selected component is zero: no cut can have two future
endpoints and satisfy the common conditions. Its auxiliary bank is
defined as zero. Using v=min(k,T), rather than k, in this range is
essential when k>T.

After activation, every remaining displayed A46.6 condition is directed
toward retirement for a fixed physical record: k>g(b), e>L(b),
t and each old adjacent gap>J(b), and s>h(b). Each can cease to hold
but cannot become true again. Original all-large and strict-core gates
are fixed record predicates. Intersecting these conditions with the
original interval [c+1,i-1] therefore gives exactly an interval

    [max(c+1,a_k),h_record]

or the empty set, with the endpoint also bounded by v-2. This is a
stronger conclusion for this particular selector than for a general
cut-dependent selector. Here retirement includes threshold failure as
well as the original lower-output boundary.

Let F_n be the actual source-pair weight sum from A42, and define

    K_bk=1[b>=a_k] F_min(b-1,v-2),
    D_bk=K_bk-Q_selected(b,k).

At the activation cut all existing source-pair allowance is added once.
Actual physical records inject into (d,e), so the selected Q at that cut
is at most the newly activated F bank. After activation, an old active
record can only retire. Every new selected record must use a newly
available source pair, and its de is paid by the corresponding increase
of F. Summing with the positive weights proves DeltaD_bk>=0. Once
b>=v-1, the selected record set is empty and the bank freezes at F_(v-2).
If a_k=B, the same injection proves nonnegativity at the initial cut;
there is no need to postulate a preceding cut in the domain.

Thus D_bk is nonnegative and nondecreasing. With original fixed genuine
lambda_k=kappa_k/H_k^2, the finite sum over k=6,...,M has the same
property. Components k>T remain present with v=T. There is no reset of
u_r, no component selector is moved outside the k sum, and no infinite
interchange or arbitrarily long capped-history assumption is used.

For an activated component, terminal bank <=F_(v-2). Therefore

    lambda_k F_(v-2)
       <=kappa_k (k-2)^4/32 <=1/(8k),
    sum_k lambda_k K_terminal,k <=sum_{k=6}^M1/(8k).

Here F_n<=n^4 H_n^2/32, v<=k, and H_(v-2)<=H_k suffice; inactive
components contribute zero. The bound can be sharpened while retaining
the entire common tail: for k<=T use the individual bound, whereas
all k>T have v=T. Their combined bank is at most

    F_(T-2) u_(T+1)^[M] < 1/32.

For T>=6 this follows from
(T-2)^4/[32T^2(T+1)^2]<1/32; for smaller T no component can activate
on b>=4. If M=T the tail is zero. Thus the terminal bank obeys

    Gbar_(T-1) <= (1/8)sum_{k=6}^{T}1/k + 1/32.

This is uniform in M but only logarithmic in T. No tail coefficient
has been replaced or reset. Positive monotonicity by itself still does
not prove a uniform norm or solve Q1. It creates a potential consistent
with the particular selector, while exposing the bank-size problem.

The proof also allows additional fixed-per-record predicates at a fixed
component: they delete records without introducing later activations.
No claim that all historical paid classes are characterized by A46.6
is needed for this upper-bound construction. Hash bindings are in
`A51_A54_review_manifest.json`; this is a hand review, not a claim of
full Lean verification.

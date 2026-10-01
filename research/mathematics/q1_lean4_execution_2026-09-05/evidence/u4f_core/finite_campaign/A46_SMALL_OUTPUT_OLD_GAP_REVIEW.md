# A46: uniform payments for small output and adjacent old gaps

Date: 2026-09-09. Independent hand-proof review: PASS.
Exact subclassification of two previously saved edges only; no new search.

## Common hypotheses and preserved price

Use the same actual finite integer Sidon history, original strict records,
genuine lambda_k=kappa_k/H_k^2 and u_r^[M]=sum_{k=r}^M lambda_k as in A45.
Fix q>2 once. For each b>=3 put n=b-1 and J_b=floor(b^2/(log b)^q).
Both subclasses below are selected among the original records covering
that cut. All original component tails, including k>T, are retained.
No cap is required for either uniform payment.

## Small actual output differences

Select records with actual t=d-e=a_r-a_i<=J_b. At any fixed component,
each positive output label is used by at most one actual output pair.
The source shifted-edge estimate K_t<=S_b, S_b=sum_{d in D}d^2, therefore
gives Q_small_output<=J_b S_b. Thus

    P_small_output(b)
       <= J_b S_b/H_b^2 * (alpha_(b+2)-alpha_(M+1))
       <= J_b n^2/[4(b+2)^2(b+1)^2]
       <= 1/[4(log b)^q].

If the component range is empty, use zero. The second step uses actual
variance S_b/H_b^2<=n^2/4; the last uses J_b<=b^2/(log b)^q. Hence

    sum_{b=3}^{T-1} sqrt(P_small_output(b))/b
      <= (log 2)^(1-q/2)/[2(q/2-1)].

At q=5/2 the constant is 2/(log 2)^(1/4).

## A small adjacent gap in the old quadruple

For an old quadruple p<q0<s<c, write its adjacent physical gaps A,B,Cgap,
and Hquad=A+B+Cgap. Select records for which at least one of these three
gaps is <=J_b. An actual old endpoint pair with a positive difference
<=J_b has at most J_b choices in total by Sidon uniqueness. Each pair is
contained in at most binom(n-2,2) old quadruples. Using all containing
quadruples may count the same quadruple several times or count a
nonadjacent selected pair; both are legitimate nonnegative overcounts.

The original A10 three matching products on one quadruple are
ACgap, ACgap+B Hquad, and B Hquad. Their total is
2(ACgap+B Hquad)<=2Hquad^2<=2H_b^2. Each matching has at most one actual
output pair by positive-difference uniqueness; gates only delete records.
Consequently, for n>=4,

    Q_small_old_gap <= 2 J_b binom(n-2,2) H_b^2,
    P_small_old_gap <= J_b(n-2)(n-3)/[(b+2)^2(b+1)^2]
                    <= 1/(log b)^q.

For n<4 or J_b=0 this subclass is empty. The genuine finite alpha tail
may be kept in the intermediate bound; dropping its nonnegative terminal
subtraction yields the displayed expression. Therefore

    sum_{b=3}^{T-1} sqrt(P_small_old_gap(b))/b
       <= (log 2)^(1-q/2)/(q/2-1).

At q=5/2 the constant is 4/(log 2)^(1/4). The integral comparison starts
at 2 and requires q/2>1, explaining the strict condition q>2.

## Exact two-row scope and surviving remainder

Use only the two rows saved by the A44/A45 subclass check. Independent
rational log enclosures certify

    J25=floor(625/(log25)^(5/2))=33

via 33^2*(log25)^5 <= 625^2 < 34^2*(log25)^5. The existing row at bank
index 9681 has old quad (1,10,19,22), adjacent gaps (88,312,203), t291,
e312, de188136. It survives. Index 12711 has old quad (1,6,20,24), gaps
(18,422,273), t291, e422, de300886. It is paid by the small-old-gap
subclass. The original common component price remains
lambda48=1/1148518878296832. UNKNOWN comparisons: zero.

Thus the earlier common-column two-row matching counterexample does not
remain after these further restrictions in this single cell. No general
matching claim for the reduced remainder follows from one survivor.

## Logical role and remaining gap

Use a fixed payment order for overlapping subclasses, or nonnegative
domination. At each original covered cut, a physical record can be assigned
to a single selected class. For an individual class, the selected coverage
on a block sums 1/b only over cuts in the original interval satisfying
that class's cut-dependent selector. Selected plus complementary coverage
equals the original once-per-cut coverage; no selected piece is asserted
to retain the full interval. The genuine price is unchanged. The proof
never treats cuts as independent copies of a resource.

After these two payments with q=5/2, all remaining t,A,B,Cgap are strictly
greater than b^2/(log b)^(5/2), since they are integers greater than J_b.
Combine this with A45's e>b^2/(log b)^(5/4), the existing central rank
strip, near-span condition, and any already retained original large-gap
condition. These are sufficient reductions inside the frozen profile,
not a redefinition of core or Gate 0. The remaining norm, U4-F, and Q1
are unproved. No Lean execution or claim of full formalization is made
by this note. The next nonduplicate action is joint control of the
remaining weighted source/output transport. Content hashes are in
`A44_A46_review_manifest.json`.

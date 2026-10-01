# Independent review of A13: actual cap-free BH divergence

2026-09-09. Verdict: the A13 hand proof is mathematically sound with the
displayed generous constants. It uses the already MATH-REVIEWED Gate 0
pointwise omitted-class bounds, not a core theorem or a capped-extension
assumption. This note does not claim Lean verification. The reviewed text
and source hashes are pinned in `A13_A15_review_source_manifest.json`.

## Actual Sidon block and the raw correlation lower bound

For an odd prime p, put x_j=2pj+(j^2 mod p), 0<=j<p. A difference equality
forces equal j-i: the difference of the two residue corrections has
absolute value <2p. Reducing modulo p, the nonzero common j-i fixes j+i,
and hence both indices modulo p; their ranges fix them as integers.
Thus all positive differences are unique. Also x_j-x_i>=p(j-i), since
2p(j-i)-(p-1)>=p(j-i), and x_(p-1)<2p^2.

For n=floor(p/3), and future indices ceil(p/2)..floor(3p/4), the coarse
n>=p/4 and m>=p/8 hold at the stated enormous onset. Therefore

    U>=p*n*(n^2-1)/6>=p*n^3/8>=p^4/512,
    mU>=p^5/4096,  mS<=2p^7.

The shadow f(z)=sum_(i,d:x_i+d=z) d has mass mU and fewer than 4p^2
integer sites. Its exact squared norm is mS+2 sum_t K_D^+(t): diagonal
future indices force equal labels, and each off-diagonal future pair has
its one actual positive output difference. This identity does not assign
independent budgets to outputs or cuts. Cauchy and p>=2^28 give

    sum_t K_D^+(t)
      >= (p^8/2^26-2p^7)/2 >= p^8/2^28.

Shared old endpoints can occur in this raw lower bound; they are removed
later by the existing repeated-endpoint part of Gate 0. They were not
silently assumed absent in the shadow calculation.

## Concatenation and the exact two horizons

Append Q(1+x_j) to an earlier positive Sidon prefix with N points and
maximum V, taking Q>2V. Old differences are <V<Q; new-new differences
are nonzero multiples of Q; cross differences are >V and have nonzero
residue -a_old modulo Q. Distinct old residues fix the old endpoint of
any equal cross differences, then the new endpoint. These cases exhaust
positive-difference equalities. No earlier point is changed or rescaled.

The hypothesis p>=16(N+1) implies the chosen output ranks satisfy
r<=N+floor(3p/4)+1<=13p/16. For ell=ceil(7p/8) and p>=16,
r<=ell<=15p/16<=p<=M=N+p. Every global diameter is <3Qp^2.
Using only the actual components k=ell,...,p inside the full horizon M,

    u_r^[M] >= (alpha_ell-alpha_(p+1))/(9Q^2p^4)
             >= 1/(36Q^2p^8).

The last inequality follows from alpha_ell>=ell^-4,
alpha_(p+1)<=p^-4 and (16/15)^4-1>1/4. The use of p as a subinterval
endpoint inside M does not reset alpha_(M+1) or redefine a diameter.

Scaling both source labels by Q cancels the Q^-2 price lower bound.
The resulting eligible profile is at least eta=1/(36*2^28) at every
cut N+n+1<=b<=N+ceil(p/2). Those cuts are above every chosen old source
and strictly below every chosen lower output endpoint. Their number is
at least p/6 and their maximum at most 9p/16, so harmonic length is
at least 8/27>1/4. The same records cover these cuts once each.

## Strict core and all three large adjacent old gaps

Section 3 of the fixed NEXT_THEOREM_CONTRACT supplies cap-independent
pointwise upper bounds tending to zero for the six omitted classes.
Their finite sum F(b) tends to zero uniformly in history and horizon.
Since b>=p/4, an absolute threshold p0 makes F(b)<=eta/4 throughout
the chosen cut interval. Finite genuine prices satisfy exactly the
upper comparisons used by those bounds. This is a justified numerical
limit threshold, not a hidden maximum-prefix assertion.

Set epsilon=eta/384. Among the unscaled block's old points, there are at
most floor(epsilon*p^2) endpoint pairs of positive difference at most
epsilon*p^2, by actual Sidon uniqueness. Completing one such pair to an
old quadruple has at most p^2/2 choices; at most three source matchings
can arise, and each has at most one actual output. This union may count
a quadruple more than once, harmless for an upper bound. With r>=p/2,
every record weight is <=alpha_r<=64/p^4. Thus removing all quadruples
with one small adjacent old gap costs <=96epsilon=eta/4 per cut.

The retained strict-core contribution is at least eta/2. Its gaps are
>epsilon*Q*p^2. For epsilon*Q>=1 and c<=N+n<p/2, c>=4, these exceed
c^2/log(c)^3. The chosen subprofile really lies inside the original
all-large-old-gap class.

Finally Hquad<2Qp^2 and B>epsilon*Q*p^2 imply
AC/(BHquad)<1/(2epsilon). The original implication
G_minus,q<=G_minus,s survives restriction to the chosen future endpoint
set because the two minus records share the same output and price.
Thus each retained quadruple's full mass is at most
(1+1/epsilon)BHquad(G_minus,s+G_plus,s). Missing plus outputs are not
inserted. Summing gives the actual large-gap BH lower bound

    Q_BH(b)>=(eta/2)*epsilon/(1+epsilon)
            >=delta=eta*epsilon/4>0.

## Infinite concatenation and why it is outside fixed cap

Recursively choosing primes p>=max(p0,2^28,16(N+1)) and integers
Q>2V, Q>=1/epsilon, Q>=(N+1)^4 gives one actual infinite integer Sidon
history. The cut intervals of successive blocks are disjoint. Future
extension leaves existing record membership unchanged and increases
each genuine price by positive components. Hence after L blocks the
BH square-root harmonic norm is at least (L/4)sqrt(delta).

This is a genuine cap-FREE divergence theorem, including strict core,
all three large old gaps, physical output order and one shared component
clock. At the first rank k=N+1 of each appended block, however,
H_k=Q-1>=k^4-1, so H_k/(k^2 log(2k)) tends to infinity. Every fixed
C,m0 is violated at infinitely many such ranks. Indeed at x=Q-1 the
count is N; since log(x)/x decreases eventually and Q>=k^4,
N*sqrt(log(x)/x) tends to zero along these gaps, consistent with Q1.

No numerical block was generated, no hidden infinity or cap hypothesis
was used, and neither the frozen theorem nor Q1 is refuted. This theorem
rejects efforts to close the BH term using only cap-independent inputs.
Next nonduplicate action: inspect the new fixed-cap first-moment A15
estimate and seek a genuinely cap-sensitive BH bound.

## Final source binding

Final `research/u4f_core/WORKING_PROOF.md` SHA-256:
`5545ad8821bbaa0a5f24a4a74a3b3143537f98b42b8f71a84a87364edb8c8c4c`.

A13 section SHA-256:
`bce5182b867b1a4da250e5755306d535ad85361ca27f947f9b29a108b65bd8c6`.

The changes from the first reviewed section only update review/Lean
status; the mathematical contents are unchanged. Both versions are
retained in `A13_A15_review_source_manifest.json`.

# A77 independent review: exact membership and the penalty identity

Status: PASS. The integrated A77 hand argument is valid, and both prescribed finite enlarged domains were independently reconstructed by two methods. No new strict-core or residual-gate certification is claimed.

## Scope of the exact domain

Fix c<b and v=min(k,T), with old points a_1,...,a_(c-1) and actual future points f_1,...,f_m at ranks b+1,...,v. In the enlarged domain E*, the source indices satisfy w<z<c, x<c, x distinct from w,z; future indices j,q belong to 1,...,m and are distinct. The exact equation is

    a_c+a_w+f_j=a_x+a_z+f_q.

It gives h_x=a_c-a_x=g+f_q-f_j>0, where g=a_z-a_w. If j<q, then h_x>g and the fresh source is larger; if j>q, then h_x<g and the old source is larger. The actual output gap is |h_x-g|=|f_q-f_j|>0. Four distinct old endpoints and two distinct later endpoints give six distinct points. Conversely, an actual source/output collision with these causal ranges determines this orientation uniquely.

These conditions deliberately omit the original strict-log gates and later residual selectors. An element of E* is an actual causal six-endpoint collision, but is not thereby a strict-core or current residual record. Empty future domains and insufficient old endpoints give no such edge and do not invalidate the formulas.

## Exact graph matching and source injectivity

At fixed right node (z,q), a repeated w would give the same positive mixed difference f_j-a_x. Literal Sidon therefore fixes j,x. A repeated j would give the same signed old difference a_w-a_x. This difference is nonzero because w!=x; after fixing its sign, Sidon determines w,x. A repeated x fixes a_w+f_j. Sidon two-sum uniqueness, with old/future index separation resolving the unordered pair, fixes w,j.

Consequently the whole exact candidate graph at a node, before strict filtering, is a matching in w,j and also has injective fresh coordinate x. This is stronger than saying only the already selected original records form a matching. Deleting edges by the fixed original gates or residual selector preserves the property.

Fixing a physical source (w,z,x) fixes g,h_x and their nonzero absolute difference. Actual positive-difference uniqueness fixes the output pair, and the sign h_x-g fixes which endpoint is q. Thus a physical source occurs at most once across all nodes and both orientations. There is no second source-budget copy for the other orientation.

## Source-dependent penalty is an identity here

Put Q*_g=sum_(E* with source g) g*h_x and S_g=g*sum_(x<c; x!=w,z) h_x. Source injectivity proves Q*_g<=S_g for every physical g, independently of any penalty.

On an exact candidate, y=h_actual belongs to the eligible fresh bank, hence hmin=y. Its A76 residual is (1-theta_g)*g*h_actual>=0. Since all candidate edges at each node already form a matching, a maximum matching may include all of them, including harmless zero-weight edges. Therefore

    Dexact_theta = sum_g theta_g*S_g + sum_g (1-theta_g)*Q*_g
                 = Q* + sum_g theta_g*(S_g-Q*_g),
    min_(theta_g in [0,1]) Dexact_theta = Q*.

The all-zero vector attains the minimum. Uniqueness of the minimizer is not claimed: a zero source slack permits other choices. If every strict and residual condition is imposed too, the same proof gives the identical statement with the filtered Q_selected and its source masses.

This proves that penalty optimization after exact incidence restoration cannot yield a strict improvement over the exact correlation mass it already contains. It does not rule out useful analytic bounds on that mass, the original uniform norm, or improvements obtained by exploiting other information in an upper relaxation.

## Independent finite reconstruction

Only the existing c=24,b=25 domains with (k,M,T)=(48,96,96) for C=1,m0=2 and (50,50,50) for C=2^67,m0=2 were used. For each cell, one method checks every physical source triple (w,z,x), computes |h_x-g|, and looks up its unique actual future output pair. A separate method checks the exact node equation using old-value lookup. The physical-source method tests 5,313 possible source triples per cell; the second method checks the prescribed node equations. No new history, full profile, or strict-gate scan is involved.

The two reconstructed record sets exactly equal the saved A77 certificate, including all integer labels and endpoint coordinates. Every node's w,j,x projections are injective; every physical source is used once; all 253 per-source slack records agree and are nonnegative. The selected A76 records are checked to be subsets of these enlarged domains by their exact coordinates.

C1 results:

- |E*|=663 over 338 nonempty right nodes.
- Fresh-larger: 577 records, mass 70,289,519.
- Fresh-smaller: 86 records, mass 9,593,029.
- Q*=79,882,548, source bank=634,824,292.
- The existing selected 125-row mass is 21,922,039, so Q*-Q_selected=57,960,509.
- The A76 theta-zero threshold allowance exceeds Q* by 133,115,666.

A72 results:

- |E*|=1, fresh-larger, over one right node.
- Q*=Q_selected=319014718988636095646352980968623575040.
- Source bank=1591346439643469596457552815054114237739600.

The scalar identity at theta=0,1/2,1 also agrees exactly with both saved certificates. The vector minimum follows from the per-source nonnegative slacks and the hand identity, not from sampling those three scalar values.

UNKNOWN=0 for the integer computations. No reference script was imported or executed. The independent computation exited successfully; no process remains running.

## Original prices and unresolved boundary

All objects above are at the same actual fixed component v=min(k,T). Original strict/residual selectors must remain inside their own component sums. Multiplication by the original lambda_k preserves the inequalities and identities, without changing any u_r^[M], removing k>T tails, or setting alpha_(M+1)=0.

The enlarged-domain mass has not been bounded uniformly over histories, births, cuts, and components. The exact-domain identity is not a uniform square-root harmonic estimate. Frozen U4F and Q1 remain unresolved. An analytical estimate for the joint exact incidence, or a justified deficit for the threshold relaxation, is still needed.

## Exact source binding

Reviewed root WORKING_PROOF snapshot:

- Whole SHA-256: `1c0ea84d9ed0f34d4378239b26ac0e7308f932d450c038fa273f869474434141`.
- A77 section SHA-256: `a683939afb136a611ca258140150423f46a7461e7d0794e53301d0ec0f9533a4` (from its `## A77.` heading through before the next `##` heading, exact saved newlines).

Evidence:

- `A77_EXACT_MEMBERSHIP.json`: `c4b2c01bba7ab8b35e5a12c2df59a99f22666930c4a74803e388508d19ad1d32`.
- `A77_INDEPENDENT_CHECK.json`: `590e3be31fa7b4f2dc0bfe9eaab254471e5d369eb6a90a9853a5b1f99ca4b405`.
- `A76_FULL_MASS_EXACT.json`: `352bba86f180deb757fd46501e9be5c1aeb7862a5fddd6c9e52f47dcd9842082`.
- `A76_FULL_MASS_CHECK.json`: `7052a16aa119832134fb81f3685a7927766daf1973b9469d3474033197dbbc90`.
- `A76_FULL_MASS_REVIEW.md`: `3e34f1cfd0f149a7915c470cf77284147efc2f85152ff0d604253868551539a2`.

The independent JSON binds all further input/source hashes and records its exact reconstructed record sets, orientations, and individual source slacks. This is a snapshot binding, not a claim that the concurrently maintained root proof will never change. No root proof, ledger, checkpoint, Lean, or other worker file was edited.

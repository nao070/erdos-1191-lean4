# A74 independent finite parametric-dual certificate review

Status: PASS_INDEPENDENT_GLOBAL_PARAMETRIC_MINIMUM_CERTIFICATE. The independent checker exited 0. Here “global” refers to every theta in [0,1] for each of the two prescribed finite cells, not to all histories, cuts, or component horizons.

## Reconstruction and exact certificate checks

`A74_PARAMETRIC_DUAL_CHECKER.py` uses only the Python standard library. It imports no reference implementation, runs no optimizer, and performs no new history generation, original-record enumeration, profile evaluation, or Lean build.

The checker independently reconstructs the actual old/future values, a_c, every fresh h_x, the source bank Bsrc, and each candidate hmin with fresh x=w,z excluded. It checks all declared source hashes in the two source inputs and both supplied A74 certificates. Original fixed-cap, strict-core, and residual membership certifications are reused from their bound existing artifacts rather than recomputed here.

At theta=p/d it reconstructs every padded integer matrix entry as

    W=max(d*g*t-p*g*(hmin-g),0),

with dummy or ineligible entries zero. For every node it checks the supplied assignment is a permutation, its objective equals the claimed integer value, every dual_left+dual_right entry dominates W, and the total dual objective equals that value. Discarding zero assignment edges leaves a valid partial matching attaining the same value; conversely every partial matching extends to a padded assignment with nonnegative weights. Thus the checked values are exact node maxima.

There are 1,104 nodes at the two optimal theta values, plus 3,312 nodes in the previously saved theta=0,1/2,1 certificates. All 4,416 node certificates and 1,156,164 integer dual inequalities pass. All primal-dual gaps are zero.

Each affine lower support is reconstructed from its actual feasible edge lists. The checker verifies no w or j repeats within a node, every hmin exists, and

    A=sum g*t,
    S=Bsrc-sum g*(hmin-g).

The line A+theta*S is a lower bound for Dtheta at every theta. The checker then verifies an active slope with the correct endpoint sign, or active opposite-sign slopes at an interior point, as required by the hand proof in `A74_SOURCE_DUAL_REVIEW.md`.

## C=1, m0=2, M=T=96, c=24, b=25, k=48

The independently reconstructed Bsrc is 240,661,543. The exact minimum over all theta in [0,1] is

    theta*=0,
    D*=80,331,512.

The active lower support has intercept 80,331,512 and slope 157,145,694>=0, using 1,670 feasible positive edges. Together with the node duals at zero, this certifies the endpoint is globally optimal for this cell.

The additional three-theta values are exactly

    D0=80,331,512,
    D_(1/2)=159,521,445,
    D1=240,661,543.

From the already certified 125 A65-unpaid rows, the checker directly reconstructs 106 positive-boundary rows and Beta=8,716,524. Each actual node is a matching, no physical source triple is reused across nodes, and actual hmin equals the actual fresh h=g+t. Both every node's residual charge and the total Beta are bounded by the corresponding certified values. Original product mass is distinct from Beta and is recorded separately in the JSON.

## C=2^67, m0=2, c=24, b=25, k=M=T=50

The independently reconstructed Bsrc is

    422576201368410987027775267105236195815784.

The exact minimum over all theta in [0,1] is

    theta*=46116895368612413440/58222535982653112321,
    D*=21471112705524970501873327890317959759277864452032807370219072
       /58222535982653112321.

The two independently reconstructed active affine lines have coefficients

    A0=369697913824732770117335942103902613134912,
    S0=-1163074496203593353989007796171863285672,

    A1=367677485729677844738882077551790592613952,
    S1=1387714027708225982975008359060045504592.

Their feasible edge counts are 2,189 and 2,188. Their opposite slopes and equal values D* at theta*, together with all node upper duals attaining D*, certify the global minimum. No reliance on the optimizer's search trace or reported oracle count is needed.

The additional exact values at theta=0,1/2,1 are

    1873838559098723261261523023654144201219520,
    530658573041259555304430771038787839190660,
    422576201368410987027775267105236195815784.

The single independently certified original record gives, by direct source/output arithmetic,

    Beta=127605887595579202812083736393554006016 < D*.

It uses its physical source triple once, and its actual residual node charge satisfies the checked matching bound. The auxiliary matching edges used in the certificate are not asserted to be original records.

## Prices, scope, and unresolved gap

This certifies the exact coefficient allowance Dtheta for the two fixed actual cells and its minimum in theta. It does not price missing auxiliary edges, change lambda_k, reset alpha_(M+1), or replace an original u_r^[M]. Applying the hand inequality at other components must keep v=min(k,T), original component-dependent selectors, and all k>T tails.

No monotonicity across cuts, independent source budgets across components, all-history improvement, complete core profile bound, uniform square-root harmonic norm, frozen U4F theorem, or Q1 conclusion follows. The mathematical A74 bound is a hand proof; the finite integer/rational certificates here are not Lean formalization.

The check completed with UNKNOWN=0. No processes remain running from this task.

## SHA-256 binding

- `A74_PARAMETRIC_DUAL_EXACT.json`: `7d32e6598f38cb0ad8917076ce5a77feda28b9ed187b4fe72c8e3b2879a37c7a`
- `A74_SOURCE_DUAL_EXACT.json`: `f264a8d54fe10bc2b10ad29adc0ff2c52f78a69ffd829150ad7fa793f873343e`
- `A74_PARAMETRIC_DUAL_CHECKER.py`: `210987e25efcf1d8867052e5e9740dbf8ff557e114762d2c27b32aded05fd6e8`
- `A74_PARAMETRIC_DUAL_CHECK.json`: `04aa0fa904bd873a01e7ccea7bb9590ad2bc943fd31817d97ab3eaf775daf727`
- `A74_SOURCE_DUAL_REVIEW.md`: `d7c62f0badb11eb796ee28ab29a64d557a96624dde38193f563ce23f6222ce56`

The check JSON contains the complete input/history/evidence/source hashes and every node result. Root-owned mathematical sources and ledgers were not edited.

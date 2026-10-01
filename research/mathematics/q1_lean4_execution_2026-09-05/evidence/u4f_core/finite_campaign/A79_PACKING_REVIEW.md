# A79 independent hand review: isolated-fiber integer packing

Status: PASS for the stated allowance comparison. No new finite campaign, profile, or numerical certificate was run. This is separate from the completed C18 A66–A78 readback.

## Pointwise kernel upper bound

Let H>=0, 0<=L,J<=H, and t>=0. For the A78 kernel, put

    U=(L+J)^2-t^2, V=(L-J)^2-t^2, U>=V.

If U<=0, the kernel is zero. If U>0 but V<=0, then

    K=U/4 <= H^2-t^2/4,

and the right side is positive because t<L+J<=2H. If V>0, both terms are active and

    K=(L^2+J^2-t^2)/2
      <=H^2-t^2/2 <=H^2-t^2/4.

Here t<|L-J|<=H, so the final right side is positive as well. Thus in every case

    K(L,J,t) <= max(H^2-t^2/4,0).

This includes degenerate boundary values. Actual distinct future points give t>0, but the upper bound itself also holds at zero. H may be the old bank's diameter, or any larger nonnegative diameter allowance satisfying the same packing lower bound.

## Packing the actual future differences

Fix one actual A78 fiber of size q. Its future coordinates are distinct, and its old pairs are pairwise disjoint. Let n=b-1 be the number of old points and N=binom(q,2). Then 2q<=n. The N positive differences between these actual future points are distinct positive integers by literal Sidon. In increasing order t_1<...<t_N, this gives t_j>=j.

The envelope phi(t)=max(H^2-t^2/4,0) decreases for t>=0. Therefore the actual unfiltered kernel mass in this fiber satisfies

    sum_pairs K <= sum_(j=1)^N phi(t_j)
                <= Bpack := sum_(j=1)^N phi(j).

No realization of the packed labels 1,...,N as the actual difference set is assumed. This step deliberately forgets their additive and old/future correlation structure.

For n integer Sidon points, their binom(n,2) distinct positive integer differences all lie in [1,H], hence

    H >= n(n-1)/2 >= q(2q-1) >= 2q(q-1)=4N.

Thus for 1<=j<=N, j<=H/4 and j^2/4<=H^2/64. The truncation in Bpack is inactive, and the exact finite square-sum formula gives

    Bpack = N*H^2 - N(N+1)(2N+1)/24,
    (63/64)*N*H^2 <= Bpack <= N*H^2.

For q=0 or 1, N=0 and every displayed sum is zero, so no division or positive-diameter exception is required. For N>0, H>0 automatically. The constant 63/64 is valid; sharpness is not claimed.

## What this does and does not reject

The lower bound is on the packed allowance Bpack, not on the actual kernel mass. Actual spacings may be much larger than the fictitious j, actual K can be zero, and original strict/residual gates can delete contributions.

Relative to the crude allowance N*H^2, this particular isolated-fiber packing relaxation saves at most a fraction 1/64. Therefore it cannot by itself produce a vanishing logarithmic factor relative to that crude allowance. The same comparison persists under common nonnegative weights and finite sums. It says nothing about whether other information already makes the crude allowance summable.

This does not reject joint-fiber estimates, actual endpoint/cap correlations, stronger use of the future differences, or an analytic bound for the selected kernel. It proves no actual-profile lower bound, no existence of arbitrarily long fixed-cap prefixes, and no counterexample to the frozen U4F proposition or Q1.

At a genuine component the actual future horizon is min(k,T). If the comparison is later priced, the same lambda_k and all selectors must be retained, including k>T components. No original record price, terminal alpha_(M+1), physical cut coverage, or source budget is changed here.

## Source and execution scope

This is an independent hand check of the parent's A79 candidate, deriving the bound directly from the A78 kernel definition and literal Sidon integer packing. No external theorem, new finite calculation, reference script, Skill, subagent, or Lean build was used.

- `A78_KERNEL_REVIEW.md`: `f53d4b95b6982b59d601977a3d52d44a4e60ee812d2f5706af99dbed79f6427c`.
- `A78_INDEPENDENT_CHECK.json`: `b8831ee9a770c2087c32115c158384f62fb0a43fc79ac4713c9296a237e36e01`.
- `lean/Q1/U4FFiberKernel.lean`: `e3c651935b253bf0e2d57a4482cff8ae52fe7d0b1b2c144cab893bfd751a5bf3` (definition and existing A78 case algebra; it does not formalize the new A79 bound).

Only this new review file was written. Root proof, ledger, checkpoint, and Lean sources were not edited. No process remains running from this hand review.

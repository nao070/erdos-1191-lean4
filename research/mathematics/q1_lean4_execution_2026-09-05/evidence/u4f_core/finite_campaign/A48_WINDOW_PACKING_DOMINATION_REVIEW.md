# A48: why a common per-row window capacity is a weaker allowance

Date: 2026-09-09. Independent hand-proof review: PASS.
No additional finite computation or history search.

## Integer-window convention and actual Sidon packing

Let J>=1 be an integer. A47's output window is of the form (K-J,K]
with integer K: it contains J integer positions and has maximum distance
J-1 between occupied integer points. Put

    rho=max{r in Nat : binom(r,2)<=J-1}.

This is finite and rho>=1. An actual integer Sidon set of r points in
the window has binom(r,2) distinct positive differences, each between
1 and J-1, so r<=rho. Maximality of rho and integrality give

    J-1 < binom(rho+1,2),
    J <= rho(rho+1)/2.

The endpoint convention matters: a closed interval of diameter J has
J+1 integer positions and would use J instead of J-1 in the definition.
No such alternative window is used here.

## Domination by the existing joint cardinality allowance

At a fixed cut/component let m=v-b be the number of actual future points.
For m=0 or m=1 no output pair exists. Assume m>=2, so there are m-1
possible lower-output rows. Each row has at most rho possible output
points in its translated width-J window. Summing the same row capacity
gives (m-1)rho.

The shared output-label allowance already has

    h=min(J,binom(m,2))

labels, by the integer bin width and global Sidon output-pair uniqueness.
Always h<=(m-1)rho:

- If m<=rho+1, then m/2<=rho since rho>=1. Hence
  binom(m,2)<=rho(m-1).
- If m>rho+1, then J<=rho(rho+1)/2<=rho(m-1).

Thus replacing every actual row by this same worst-case window count
and adding those counts cannot improve the existing shared cardinality
bound. The argument does not require the windows to be disjoint, and it
does not assert that all capacities can be simultaneously realized.

## Common nonnegative weights obey the same domination

Take a single finite nonnegative list of bin weights, sorted in decreasing
order. Let W(s) be the sum of the largest min(s,N) weights, with W(0)=0.
If h<=(m-1)rho, partition the first min(h,N) weights into at most m-1
groups of size at most rho. Each group's sum is at most W(rho), so

    W(h)<=(m-1)W(rho).

This includes zero weights, ties, or rho/h exceeding N. In particular,
giving every row the same largest-rho common weights independently is
a weaker upper bound than the existing shared top-h allowance. At one
genuine component the common factor lambda_k does not change the
comparison. One cannot silently use this conclusion for different
row-dependent weight lists or prices while discarding their dependence.

## Exact scope and next information to retain

This is a proved domination relation between two upper bounds. It is
not a lower bound for any actual core profile, a claim that Sidon windows
achieve rho, or a disproof of the frozen uniform norm. The finite A47
example gives concrete shared-budget overcount; it is not needed for
the general proof here.

Actual translated windows may contain very different endpoint sets;
source exclusions, original strict gates, output birth ranks, and their
shared compatibility can improve a bound that retains them. A48 does
not rule out such an estimate. It only rejects the shortcut that first
replaces every row by the same integer-packing maximum and then adds
independently. The next action must keep those actual common incidences
and genuine prices. U4-F, the A46.6 remainder norm, and Q1 remain open.
No Lean formalization is claimed by this independent note. Content hashes
are in `A47_A48_review_manifest.json`.

# A33 independent hand review: uniformly paying far components

Date: 2026-09-09. Status: PASS as a finite-history theorem for the
unchanged original strict core. This is a uniform subclass bound,
not a proof of the entire frozen U4-F statement or Q1.

## Exact claim and proof

Fix one real p>1, independent of b, C, M and T. For 3<=b<T<=M let
S_b be the squared-difference sum of the first b-1 points, and let
Q_bk be the original core sum of de at cut b with r<=min(k,T).
Define the component subclass

    PFar_b = sum_{k=b+2}^M 1[H_k>=H_b(log b)^p]
                       (kappa_k/H_k^2) Q_bk.

An actual output difference has weighted source-edge sum at most S_b.
There are at most binom(min(k,T)-b,2) actual future output pairs, so

    Q_bk <= S_b binom(min(k,T)-b,2).

Nonnegativity, the far condition, and min(k,T)<=k give

    PFar_b <= S_b/[H_b^2(log b)^(2p)]
               sum_{k=b+2}^M kappa_k binom(k-b,2).

The existing finite Abel identity, with alpha_{M+1} preserved, is

    sum_{k=b+2}^M kappa_k binom(k-b,2)
      = sum_{r=b+2}^M alpha_r(r-b-1)
           - binom(M-b,2) alpha_{M+1}
      <= 1/(6b^2).

It follows from alpha_r<=((r-1)^(-3)-r^(-3))/3 and a numerical
tail integral. It does not assume a bound on actual prefix length.
For n=b-1 old points, the actual variance bound gives
S_b<=n^2 H_{b-1}^2/4<=n^2 H_b^2/4. Hence

    PFar_b <= (b-1)^2/[24 b^2(log b)^(2p)].

Taking square roots and using that 1/[x(log x)^p] decreases for x>1,

    sum_{b=3}^{T-1} sqrt(PFar_b)/b
       <= (1/sqrt(24)) integral_2^infinity dx/[x(log x)^p]
       = (log 2)^(1-p)/[sqrt(24)(p-1)].

The b=2 core is empty. Thus no original cut contribution was dropped
without justification. For p=2 the displayed absolute bound is
1/[sqrt(24) log 2]. The far bound itself does not require the cap.

## Remaining near components and both horizons

Partition every original component at each cut by the displayed far
condition and its strict complement. Then exactly

    P_b=P_near_b+P_far_b.

The original u_r^[M]=sum_{k=r}^M kappa_k/H_k^2 is unchanged. A record
with an early output r can have a later far component k: this argument
pays components, and is stronger than classifying output ranks alone.
For fixed T and k>T the original output bank stays fixed at T, while
the genuine component tail remains present. Replacing min(k,T) by k
only in an upper bound is legitimate.

Since sqrt(x+y)<=sqrt(x)+sqrt(y), a uniform near norm estimate would
combine with this constant to prove the original uniform core norm.
No such near estimate has been established here.

If b>=m0, the fixed original cap and Sidon integer packing imply that
each near component satisfies

    k(k-1)<2 C b^2 log(2b)(log b)^p,
    k<1+sqrt(2C) b sqrt(log(2b))(log b)^(p/2).

Indeed H_k>=k(k-1)/2 and H_b<=C b^2 log(2b); also
(k-1)^2<=k(k-1). The cap deduction is restricted to b>=m0. Equality
at H_k=H_b(log b)^p belongs to the far class, so there is no boundary
overlap or omitted component.

## Scope and source binding

This review uses the original source-edge bound, actual variance bound,
and A27's finite Abel inequality. It needs no infinite capped history,
Q1 premise, compactness conclusion, or maximal-prefix assertion.
Infinite sums above are numerical upper bounds for finite actual sums.
No computation or Lean build was run for this review. The companion
A32_A34_review_manifest.json binds the frozen sources and the previously
reviewed A27 price note. Full near-component control, the frozen K,
and final Lean Q1 verification remain open.

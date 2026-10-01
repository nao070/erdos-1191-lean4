# A43 independent review: uniformly paying short-rank components

Date: 2026-09-09. Status: PASS hand theorem for a component subclass
of the unchanged full original profile. No new finite experiment,
history or Lean build was used.

Fix one real q>2/3, independent of b,M,T,C,m0. For b>=3 define

    L_b=floor(b/(log b)^q),
    P_short_b=sum_{k=b+2}^{min(M,b+L_b)}
                        (kappa_k/H_k^2) Q_bk,
    Q_bk=sum_original_core de through r<=min(k,T).

If L_b<2 or the displayed component interval is empty, the sum is
zero. Otherwise use the actual output bound
Q_bk<=S_b binom(min(k,T)-b,2), S_b/H_b^2<=(b-1)^2/4 and
H_k>=H_b. For k>=b+2,

    kappa_k=4/[k(k^2-1)^2]<=4/b^5.

Putting n=b-1 and enlarging only the nonnegative upper sum gives

    P_short_b<=n^2/b^5 sum_{m=2}^{L_b}binom(m,2)
              =n^2 binom(L_b+1,3)/b^5
              <=L_b^3/(6b^3)
              <=1/[6(log b)^(3q)].               (1)

The finite hockey-stick identity also holds for L_b=0,1 with both
sides zero. The cubic inequality uses
binom(L+1,3)=(L^3-L)/6<=L^3/6 for nonnegative integer L, and n<=b.

Since 3q/2>1, a decreasing-integral bound yields

    sum_{b=3}^{T-1}sqrt(P_short_b)/b
      <=(log 2)^(1-3q/2)/[sqrt(6)(3q/2-1)].      (2)

For q=3/4 this is the absolute constant
8/[sqrt(6)(log 2)^(1/8)]. The b2 core is empty. No cap is needed.
The infinite integral bounds a finite actual sum and assumes no
infinite capped history or maximal-prefix statement.

This classification is by the genuine component k, not by output
rank alone. If k>T lies in the short interval, its original fixed-T
output bank and its original price are still present. Replacing
min(k,T)-b by k-b occurs solely in an upper bound. No terminal alpha
or component coefficient is altered.

Combine the q=3/4 short bound with A42's p=5/8 far bound by paying
short components first and then the far components outside that
short class. Termwise domination preserves the A42 constant. This
ordering matters because the two nominal classes can overlap for
small b; their unmodified sums need not be a disjoint identity.
The exact remaining original component interval is

    b+floor(b/(log b)^(3/4)) < k
                       < ceil(b(log b)^(5/8))+1.

An empty central interval contributes zero. The square-root triangle
inequality legitimizes the sum of the two paid constants, but no
uniform estimate for this remaining central class has been proved.
Original strict gates, all intermediate-rank caps and both horizons
remain unchanged. A42/A43 narrow the live norm question rather than
prove CoreUniform or Q1.

Evidence and source dependencies are bound in
A41_A43_followup_review_manifest.json.

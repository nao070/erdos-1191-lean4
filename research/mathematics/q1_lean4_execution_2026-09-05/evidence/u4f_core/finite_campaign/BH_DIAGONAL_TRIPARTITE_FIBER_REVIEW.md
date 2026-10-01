# Independent review: BH diagonal charge and tripartite Sidon fibers

2026-09-09. Verdict: PASS as a finite mathematical argument. It proves
Q_BH(b)<=((b-1)/b)^3/48<1/48 on the original core at both horizons.
No fixed cap is needed for this pointwise estimate, and it does not prove
square-root harmonic summability. No Lean verification is claimed here.

## Scope and the diagonal identity

Fix an actual finite increasing positive integer Sidon history, 2<=T<=M,
and a cut 2<=b<T. Set n=b-1 and g_l=a_(l+1)-a_l for 1<=l<n.
For a covered old quadruple h=(p,q,s,c), p<q<s<c<b, put
A=a_q-a_p, B=a_s-a_q, Cgap=a_c-a_s, Hquad=A+B+Cgap. The original
strict-core gates and genuine prices define

    w_h=G_minus,s+G_plus,s,
    D_l=K_ll=sum_h 1[q<=l<s]*w_h.

This is indeed the diagonal of the previously considered symmetric
kernel: its indicators satisfy x_h(l)<=y_h(l), so x_h(l)y_h(l)=x_h(l).
The fact that that kernel need not be PSD does not affect this identity.
Finite interchange and the actual adjacent gaps give

    sum_l g_l D_l=sum_h B*w_h,
    Q_BH=sum_h B*Hquad*w_h <=H_b*sum_l g_l D_l.       (1)

Here Hquad<=H_(b-1)<=H_b and sum_(1<=l<n)g_l=H_(b-1)<=H_b.
Both facts are inequalities between actual diameters, not replacements
for the component diameters H_k. The gaps at or after index b-1 are not
silently included in this old-source sum.

For b<5 there is no old quadruple, hence Q_BH=0. The remaining argument
can be restricted to b>=5 and 1<=l<n, so both old sides are nonempty.

## Exact component collision correspondence

For an actual component k>=b+1 define disjoint rank sets

    L={1,...,l}, R={l+1,...,n},
    F_k={b+1,...,min(k,T)}, m_k=|F_k|=min(k,T)-b.

Let v_z be the number of triples (u,v,f) in L x R x F_k for which
a_u+a_v+a_f=z. Distinct triples in one fiber cannot share a coordinate.
For example a common left coordinate leaves a repeated two-sum equality
between one right and one future point; Sidon uniqueness and the disjoint
rank intervals force both remaining coordinates equal. The other two
coordinate projections are treated identically. Consequently

    v_z<=min(l,n-l,m_k),
    sum_z v_z=l(n-l)m_k.                              (2)

Every unordered pair of distinct triples in the same fiber thus has
SIX distinct endpoints. Sorting the two left indices gives p<q<=l,
the two right indices l<s<c<b, and the two future indices b<i<r<=min(k,T).
There are exactly two possible old-coordinate pairings:

1. Parallel pairing: the triples are (p,s,r) and (q,c,i), because
   a_p+a_s<a_q+a_c. Their equality is equivalent to
   a_r-a_i=(a_q-a_p)+(a_c-a_s)=A+Cgap. It gives the plus matching
   {B,Hquad}, whose older birth is s and whose BH coefficient is BHquad.
2. Cross pairing: the old pairs are (p,c) and (q,s). Their sum difference
   is Cgap-A, which cannot be zero by positive-difference uniqueness.
   If Cgap>A, the triples are (p,c,i) and (q,s,r); if Cgap<A, their future
   assignments are exchanged. The output is |Cgap-A|, giving the minus
   type-2 matching {A+B,B+Cgap}, again with older birth s. Its product is
   ACgap+BHquad, and D_l counts its BH term once.

Conversely each of these actual minus/plus BH matchings with q<=l<s
and r<=min(k,T) reconstructs that unique unordered triple pair. Sidon
gives one output endpoint pair for a specified numeric output. The plus
and minus numeric outputs differ, since A+Cgap>|Cgap-A|.

There is NO extra factor two. The type-1 matching {A,Cgap} shares the
minus triple equality, but contributes ACgap only; it is not an
additional BH term in D_l. The two permutations of an unordered pair
are likewise not two records.

Therefore, after dropping only the remaining strict-core gates, the
unweighted BH-diagonal component count is EXACTLY

    C_l(k,T)=sum_z binom(v_z,2).                       (3)

The core component count C_l^core(k,T) is its subset. Equation (3)
counts the two BH matchings, not every matching in the full profile.
It already enforces six distinct endpoints, the one-cut old/future
separation and actual integer triple correlations. Its extra records
may fail the strict old-birth, coverage-length, top-lag, far-output or
physical-output tests; this is precisely why it is only an upper count
for core.

## Both horizons and the capacity estimate

Exact interchange of the original component sum gives

    D_l=sum_(k=b+1)^M (kappa_k/H_k^2)*C_l^core(k,T).

For k>T, F_k is fixed at {b+1,...,T}; its count remains present at every
later k with the genuine shared price coefficient kappa_k/H_k^2.
Thus this formula preserves the fixed-T, M-to-infinity route. Components
are not truncated at T, and alpha_(M+1) is never reset.

Writing v_max=min(l,n-l,m_k)>=1, equations (2)-(3) imply

    C_l^core(k,T)<=sum_z v_z(v_z-1)/2
                  <=l(n-l)m_k*(v_max-1)/2.           (4)

In particular m_k=1 gives zero, as it must: a triple collision needs
two different future points. Replacing v_max-1 by v_max is an upper
relaxation, not an asserted exact count. Since

    l(n-l)<=n^2/4,
    v_max<=min(l,n-l)<=n/2,
    m_k<=k-b,

equation (4) gives

    D_l <=(n^3/16)*sum_(k=b+1)^M kappa_k*(k-b)/H_k^2. (5)

All factors 1/2 and 1/16 follow explicitly from the unordered collision
count and the two side-size bounds. Dropping strict gates enlarges the
same physical component count; it does not create independent output
or cut budgets.

## Numerical telescope and the resulting constant

Insert (5) into (1), then use sum_l g_l<=H_b and H_k>=H_b:

    Q_BH <=(n^3/16)*sum_(k=b+1)^M kappa_k*(k-b).

The exact finite telescope is

    sum_(k=b+1)^M (alpha_k-alpha_(k+1))*(k-b)
      =sum_(r=b+1)^M alpha_r-(M-b)*alpha_(M+1).

Its terminal correction is nonnegative before subtraction. For r>=2,

    alpha_r <= ((r-1)^(-3)-r^(-3))/3,

the difference being exactly 1/[3r^3(r-1)^3]. Thus the finite sum is
at most 1/(3b^3), and

    Q_BH(b) <= n^3/(48b^3)=((b-1)/b)^3/48<1/48.      (6)

The estimate is valid for arbitrary T<=M and for any restricted
collection of old quadruples; removing quadruples only decreases the
nonnegative BH side. It retains the original G_minus,s/G_plus,s
definitions throughout. No assumption of an infinite capped extension,
maximum prefix length, Q1, or an unproved K occurs.

## Information lost and the remaining task

Although (6) is a new pointwise bound for the BH channel, its right side
tends to 1/48. Summing its square root with weight 1/b diverges. On a
full dyadic block it gives only I_BH<=(log(2)+2^(-j))/48, a nondecaying
majorant. This says that this particular majorant does not close the
norm, not that the actual capped profile is nondecaying.

The decisive loss is replacing the actual fiber-size distribution by
its rank-only maximum in (4), then replacing every cut gap arrangement
and component diameter ratio by its common upper bound. The exact
tripartite collision representation and the genuine coefficients before
these relaxations remain available. A next estimate must use additional
actual joint fiber/gap or fixed-cap information. Neither this bound nor
the previous PSD counterexample solves the frozen theorem or Q1.

Source paths and hashes for the unchanged definitions, A10 matching
representation and prior exact kernel counterexample are recorded in
`BH_diagonal_tripartite_review_sources.json`. The proof is independent
symbolic review; no new history, large calculation or Lean run was used.

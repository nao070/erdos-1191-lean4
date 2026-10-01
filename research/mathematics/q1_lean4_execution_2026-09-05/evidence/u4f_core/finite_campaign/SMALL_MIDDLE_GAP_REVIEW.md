# Small physical middle gaps have a uniformly summable core profile

2026-09-09. Independent mathematical review of the main researcher's
whole-core estimate. Verdict: the count, constants, summability and
large-gap comparison are valid with the scopes stated below. No Lean
verification and no new finite history.

The frozen core and its strict inequalities are unchanged. This note
decomposes that already-defined profile into subclasses; it does not
change Gate 0's status or assume a new core bound.

## Uniform count and profile estimate, without a cap

For the unique sorted old quadruple p<q<s<c of a core record, let
B=a_s-a_q. Call a record small-B when

```
B <= c^2/(log c)^3.
```

Fix c>=4. Positive-difference uniqueness gives at most
floor(c^2/(log c)^3) actual middle pairs (q,s), because their positive
integer differences are distinct. Each admits at most c choices of p,
and each resulting old quadruple admits at most three source matchings.
Each source matching has only one possible actual output pair over all
future ranks. Therefore the number of such records at source birth c is

```
<= 3c floor(c^2/(log c)^3) <= 3c^3/(log c)^3.
```

This is a one-copy count over physical source records, not a separate
allowance for every future output or cut. Strict-core restrictions can
only reduce the count.

At a covered cut b, c<b<i<r and each genuine record weight obeys
u_r^[M]de<=alpha_r<=4/b^4. Thus for every actual history and horizons
2<=T<=M,

```
P_b^smallB(M,T)
 <= (12/b^4) sum_(4<=c<b) c^3/(log c)^3
 <= 12/b^2 + 24/(log b)^3.
```

For the second line, split c at sqrt(b). In the lower range log c>1,
and sum c^3<=b^2. In the upper range log c>=(log b)/2, and
sum_(c<b)c^3=[b(b-1)/2]^2<b^4/4. These produce exactly 12/b^2
and 24/(log b)^3. Empty small initial ranges pose no exception.

It follows by square-root subadditivity that

```
sum_(b=2..T-1) sqrt(P_b^smallB)/b
 <= sqrt(12) sum_(b>=2) b^-2
    +sqrt(24) sum_(b>=2) 1/[b(log b)^(3/2)] < infinity.
```

For example, a completely explicit absolute upper constant is

```
K_smallB = sqrt(12)
 +sqrt(24) [1/(2(log2)^(3/2)) + 2/sqrt(log2)].
```

The displayed constant uses sum_(b>=2)b^-2<=1 and decreasing-function
integral comparison from 2 for the second series. It is independent of
C,m0,M,T and the history. The original genuine component price, including
alpha_(M+1), is retained throughout.

## The remaining AC contribution is bounded by BH with a logarithmic loss

Retain only quadruples with B>c^2/(log c)^3 and c>=m0. Write
A=a_q-a_p, Cgap=a_c-a_s, and Hquad=A+B+Cgap=a_c-a_p.
The cap controls Hquad<=H_c<=Ccap*c^2 log(2c). Then

```
ACgap/(B Hquad)
 <= Hquad/(4B)
 < (Ccap/4) log(2c)(log c)^3.
```

Here ACgap<=(A+Cgap)^2/4<=Hquad^2/4. The local quadruple width
Hquad has not been confused with the global H_c.

Use the exact G notation from WHOLE_CORE_MATCHING_REVIEW. Since the
minus output and coverage are shared and q<s,
G_(minus,q)<=G_(minus,s). Therefore at each covered cut, the retained
part of the full profile satisfies

```
P_remaining(b)
 <= [1+(Ccap/2)log(2b)(log b)^3] P_BH,remaining(b).
```

The factor 2 comes from
ACgap(G_(minus,q)+G_(minus,s))<=2ACgap G_(minus,s).
Monotonicity of log(2c)(log c)^3 for c>=4 and c<b supplies the b
version. P_BH,remaining is the exact BH profile restricted to these same
quadruples and the original strict core conditions. Replacing it by the
larger full-core BH profile also gives a valid upper bound.

This does not identify the plus/minus endpoints, cut intervals or prices.
In particular the M15 physical-output/rank reversal remains present.

## Early source births and the actual sufficient condition

For c<m0 one cannot discard all future outputs just from the source birth.
The existing frozen condition r<c log c supplies the required control:
every covered cut of such a core record obeys

```
b<r<c log c<m0 log m0.
```

Thus P_b<=1/8 uniformly bounds their total square-root cost by
(1/sqrt(8)) sum_(2<=b<m0 log m0)1/b, a constant depending only on m0.
For m0<=4 there are no such old quadruples; the displayed upper bound is
still harmless. This argument retains the possibly long component horizon.

After assigning overlap with small-B to that first class, the remaining
early-birth class and the c>=m0 large-B class form a disjoint decomposition
of the frozen core. The first two classes now have proved finite costs.

The last comparison leaves the explicit sufficient condition

```
sum_b sqrt(1+(Ccap/2)log(2b)(log b)^3)
       *sqrt(P_BH,remaining(b))/b <= K(Ccap,m0).
```

Its extra factor grows like a constant times (log b)^2. Mere uniform
boundedness of the unweighted N(P_BH) does not establish this sufficient
condition. It is an attack option, not a newly frozen theorem or a proved
closing estimate. Direct joint treatment of AC and BH may avoid this loss.

## Exact classification on existing M96 histories

For each integer c=4,...,95, rigorous log intervals were used to certify
the single integer floor(c^2/(log c)^3). Every record's B was then compared
to that exact threshold. UNKNOWN count is zero. The remaining profiles
were computed by summing the same already-certified records and prices.

| Existing history | Small-B core records | Small-B old quadruples | Fraction of record mass | Fraction of harmonic I |
|---|---:|---:|---:|---:|
| Greedy M96 | 2,118 | 1,369 | 1.481156% | 2.402528% |
| Variant M96 | 2,238 | 1,422 | 2.252475% | 2.177363% |

The percentages are approximate presentations of exact rational fractions.
The small/large profile partition, the displayed small-B scalar upper
bound, and the large-B-to-BH comparison all pass at every cut by rational
arithmetic with certified log enclosures. Removing small-B changes the
finite N by approximately 2.759510% and 1.473214%, respectively; those
square-root percentages are Decimal approximations, not certificates.

`small_middle_gap_existing_M96.json` contains the certified thresholds,
exact small-B, large-B and remaining-BH profiles, exact fractions,
verification statuses and original source hashes.

## Status

The new all-history result is a valid uniformly summable subclass bound,
plus a correct cap-dependent comparison on its complement. The difficult
joint BH/profile estimate remains unproved, including the displayed
logarithmic loss if this particular comparison is used. The frozen theorem,
its final Lean chain, and original Q1 remain unresolved.

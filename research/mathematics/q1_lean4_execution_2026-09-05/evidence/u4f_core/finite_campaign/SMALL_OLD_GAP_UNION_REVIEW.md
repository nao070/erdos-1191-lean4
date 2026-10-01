# Uniform finite cost when any adjacent old gap is small

2026-09-09. Independent adversarial review of the proposed extension of
A11. Verdict: valid, with the explicit constants below. This is a hand
proof; no finite histories were generated or re-enumerated and no Lean
verification is claimed.

The frozen core remains unchanged. For its unique old quadruple p<q<s<c
write A=a_q-a_p, B=a_s-a_q, Cgap=a_c-a_s, and restrict to the subclass

```
min(A,B,Cgap) <= c^2/(log c)^3.
```

For every actual positive integer Sidon history and 2<=T<=M, let S_b
be the profile of this subclass using the original genuine prices and
the original exact cuts c<b<i. Then

```
S_b <= 1/(2b^2) + 48/(log b)^3                 (b>=5),
S_b = 0                                       (2<=b<=4).
```

In particular its square-root harmonic cost has an absolute upper bound
independent of C,m0,M,T and the actual history.

## Proof of the count and constants

At a covered cut b every old endpoint lies among ranks 1,...,b-1.
Every physical record satisfies

```
u_r^[M]de <= alpha_r-alpha_(M+1) <= alpha_r <= 4/b^4.
```

The first inequality uses de<=H_c^2<=H_k^2 for every k>=r. Nothing
resets alpha_(M+1) or substitutes a terminal price.

Split the records according to c<=sqrt(b) and c>sqrt(b).

**Low source ranks.** Put n=floor(sqrt(b)). Ignore the small-gap
condition entirely. There are at most binom(n,4) old quadruples and
three source matchings per quadruple. Each matching has at most one
actual future output pair, by positive-difference uniqueness. Thus

```
S_b^low <= (4/b^4)*3*binom(n,4)
        <= (4/b^4)*(b^2/8) = 1/(2b^2).
```

The same inequality holds when n<4, since the binomial count is zero.

**High source ranks.** Here c>sqrt(b) and c<b, so a small adjacent old
gap has value at most

```
L_b = 8b^2/(log b)^3.
```

In the whole prefix of length b-1 there are at most floor(L_b) endpoint
pairs with positive difference at most L_b. This counts all three possible
positions of a small gap at once, because integer positive differences
have unique actual endpoint pairs.

For each such small pair, choose the other two old endpoints in at most
binom(b-3,2) ways. Some choices put the selected pair non-adjacently;
including them is harmless overcount. Every qualifying quadruple is
covered because it has at least one small adjacent pair. There is no
extra factor for choosing whether that pair was A, B or Cgap.

Each quadruple has at most three actual source matchings. Therefore

```
S_b^high
 <= (4/b^4)*3*floor(L_b)*binom(b-3,2)
 <= (4/b^4)*3*(8b^2/(log b)^3)*(b^2/2)
  = 48/(log b)^3.
```

Several small pairs can cause a quadruple to be counted more than once.
This is a nonnegative upper union count, not extra spendable capacity.
Likewise, a physical record is inserted once per actual covered cut,
as required by the original profile. No independent copies are created
for its future output or for different cut intervals.

These two ranges prove the stated bound. Since four distinct old
endpoints require c>=4 and coverage requires b>c, the profile is empty
for b<=4. No further small-rank exception is needed.

## Explicit summability and scope

Square-root subadditivity gives

```
sum_(b=2..T-1) sqrt(S_b)/b
 <= (1/sqrt(2)) sum_(b>=5) b^-2
    +sqrt(48) sum_(b>=5) 1/[b(log b)^(3/2)]
 <= 1/(4sqrt(2)) + 8sqrt(3)/sqrt(log4).
```

The final line compares the two decreasing positive series with their
integrals from 4. This is a completely explicit absolute constant.

The cutwise use of the entire prefix's unique small positive differences
is essential for this proof. A fixed-c count for the outer gap Cgap could
leave two free old endpoints and an extra factor of c; that weaker count
is not imported here. The low-rank split handles thresholds at much
smaller births without assuming monotonicity of c^2/(log c)^3.

This establishes a uniformly summable subclass of the existing frozen
core and subsumes the earlier small-middle-gap class. It does not change
the frozen statement, prove the large-gap profile bounded, or alter Q1's
unresolved status. Original definitions and source identities are those
bound by the source hashes in the existing certified profile JSON files.

Next independent mathematical obligation: control the unchanged-core
records whose three adjacent old gaps all exceed c^2/(log c)^3, using
their actual endpoint correlations and genuine component prices.

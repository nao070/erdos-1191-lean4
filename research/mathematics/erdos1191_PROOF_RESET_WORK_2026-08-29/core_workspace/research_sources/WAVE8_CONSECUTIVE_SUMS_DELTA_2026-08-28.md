# Wave 8 literature delta: distinct consecutive sums

**Date:** 2026-08-28  
**Status:** primary-source bridge identified; finite and non-nested only

## 1. Exact equivalence

For a normalized Golomb ruler

\[
0=s_0<s_1<\cdots<s_k,
\qquad h_i=s_i-s_{i-1},
\]

the positive differences `s_v-s_u` are exactly the consecutive sums
`h_(u+1)+...+h_v`.  Thus a positive gap sequence has all consecutive sums
distinct if and only if its partial sums form a Golomb ruler.  This is the
finite gap-sequence formulation used by N. Hegyvári.

## 2. Hegyvári's finite theorem and construction

Hegyvári defines `f(n)` to be the maximum length of a sequence of distinct
integers in `[1,n]` whose consecutive sums are all distinct and proves

\[
 (1/3+o(1))n\le f(n)\le(2/3+o(1))n.
\]

For a prime `p` with `(1-epsilon)n/3 <= p <= n/3`, his lower-bound
construction is

\[
 h_{i+1}=2p+[(i+1)^2]_p-[i^2]_p,
 \qquad 0\le i<p,
\]

where `[x]_p` is the representative in `{0,...,p-1}`.  Its partial sums are

\[
 s_i=2pi+[i^2]_p,\qquad 0\le i\le p.
\]

The usual finite-field argument makes `{s_i}` a Golomb ruler.  Moreover
`1<=h_i<3p<=n` and `s_p=2p^2`.  Hence this is an explicit `(p+1)`-mark
ruler of diameter `2p^2`, equivalently the familiar finite
Erdos--Turan/parabola ruler written in gap coordinates.

Primary source: N. Hegyvári, *On consecutive sums in sequences*, Acta
Mathematica Hungarica 48 (1986), 193--200,
https://doi.org/10.1007/BF01949064.  The complete scanned volume was checked
at https://real-j.mtak.hu/7472/1/MTA_ActaMathHung_48.pdf.  Konieczny's later
paper independently restates the same `(1/3,2/3)` asymptotic bounds:
https://arxiv.org/abs/1504.07156.

## 3. Consequence and limitation for Problem 1191

Every contiguous block of gaps from an infinite Golomb ruler is itself a
finite Hegyvári sequence.  In particular, if a block of `k` consecutive gaps
is contained in `[1,n]`, Hegyvári's upper bound gives

\[
 k\le(2/3+o(1))n.
\]

This is a genuine local strengthening of the fact that adjacent gaps are
distinct.  It only changes a constant, however, and does not supply the
logarithmic multiscale gain required by Question 1.

The lower-bound construction is also not a construction for Question 2.
Changing `p` changes every early gap by order `p`; the rulers for different
primes do not form compatible prefixes.  Compactness cannot be applied,
because a fixed coordinate or fixed early gap has no uniform bound across
this family.  In fact, this is the same terminal-dependent finite-field
family already used in the project as an obstruction to finite-window and
fixed-depth innovation inequalities.

The remaining constructive question is therefore not finite density but a
quantitative **compatible-prefix gluing theorem**.  No such implication is
claimed from Hegyvári's result.

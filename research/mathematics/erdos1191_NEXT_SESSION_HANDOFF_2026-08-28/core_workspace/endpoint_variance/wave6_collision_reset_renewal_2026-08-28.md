# Exact cross-epoch collision bands and the finite reset-renewal obstruction

**Date:** 2026-08-28  
**Status:** rigorous integer-band and cross-boundary packing lemmas, plus an
exact finite Golomb obstruction.  No unbounded-history innovation estimate is
proved, and Erdős Problem #1191 is not resolved.

The principal global result is Theorem C, the exact cumulative low-band
ledger (28) for cross-boundary differences from every available dyadic
epoch.  The sixteen-mark construction is only a finite three-cycle
obstruction and is not an asymptotic counterexample.

## 1. Notation

Let

\[
A=(a_0<a_1<a_2<\cdots)
\]

be an integer sequence, put (h_0=1),
(h_i=a_i-a_{i-1}) for (i\geq1), and use the canonical modulus

\[
N_0=0,
\qquad
N_n=a_{n-1}-a_0+1=\sum_{i=0}^{n-1}h_i.
\tag{1}
\]

Fix a dyadic boundary (m=2^j), and suppose that the first (2m) marks
exist.  The newborn gap shell is

\[
\mathcal H_m=(h_m,h_{m+1},\ldots,h_{2m-1}),
\qquad
G_m=N_{2m}-N_m.
\tag{2}
\]

Define its old and new mean gaps by

\[
\mu_m^-={N_m\over m},
\qquad
\mu_m^+={G_m\over m},
\tag{3}
\]

and the raw cumulative discrepancies by

\[
D_m^-=
 \max_{0\leq r\leq m}\left|N_r-r\mu_m^-\right|,
\tag{4}
\]

\[
D_m^+=
 \max_{0\leq s\leq m}
 \left|N_{m+s}-N_m-s\mu_m^+\right|.
\tag{5}
\]

Thus the normalized newborn-shell discrepancy is

\[
\delta_m^+={D_m^+\over G_m}.
\tag{6}
\]

All intervals below are closed real intervals.  Their exact positive-integer
capacity is

\[
\operatorname{cap}_+(L,U)
=\max\{0,\lfloor U\rfloor-\max(1,\lceil L\rceil)+1\}.
\tag{7}
\]

The Sidon/Golomb hypothesis means that all positive differences
(a_v-a_u), (u<v), are distinct.  Equivalently, all contiguous sums of
the genuine gaps (h_1,h_2,\ldots) are distinct.

## 2. Newborn-shell common-band packing

### Theorem A (exact multi-shell band count)

Let the available dyadic boundaries be pairwise distinct.  For each selected
pair ((m,r)), with (1\leq r\leq m), put

\[
I_{m,r}=
\left[r\mu_m^+-2D_m^+,\ r\mu_m^++2D_m^+\right].
\tag{8}
\]

If the containing prefix is Sidon, then for every finite set
(\mathcal S) of such pairs,

\[
\boxed{
\sum_{(m,r)\in\mathcal S}(m-r+1)
\leq
\operatorname{cap}_+(L_{\mathcal S},U_{\mathcal S}),
}
\tag{9}
\]

where

\[
L_{\mathcal S}=\min_{(m,r)\in\mathcal S}
 (r\mu_m^+-2D_m^+),
\qquad
U_{\mathcal S}=\max_{(m,r)\in\mathcal S}
 (r\mu_m^++2D_m^+).
\tag{10}
\]

More locally, if all the intervals (I_{m,r}) lie in one prescribed band
([L,U]), the right side of (9) may be replaced by
(\operatorname{cap}_+(L,U)).

#### Proof

Write

\[
E_m^+(s)=N_{m+s}-N_m-s\mu_m^+.
\]

For (0\leq s\leq m-r), the length-(r) newborn-shell sum is

\[
\begin{aligned}
N_{m+s+r}-N_{m+s}
 &=a_{m+s+r-1}-a_{m+s-1}\\
 &=r\mu_m^++E_m^+(s+r)-E_m^+(s).
\end{aligned}
\tag{11}
\]

It therefore lies in (I_{m,r}).  There are exactly (m-r+1) such
endpoint pairs.  Inside one shell, ((r,s)) determines the pair uniquely.
Across distinct dyadic shells, the right endpoint belongs to the disjoint
rank block ({m,m+1,\ldots,2m-1}), so the endpoint pairs are again
different.  Sidon uniqueness makes all their numerical differences
different positive integers.  Counting those integers in the common real
envelope gives (9), including the ceiling and floor in (7).  \(\square\)

For one shell and one rank length, (9) gives the useful necessary condition

\[
m-r+1
\leq
\operatorname{cap}_+
 (r\mu_m^+-2D_m^+,r\mu_m^++2D_m^+).
\tag{12}
\]

Ignoring only endpoint rounding, this implies (4D_m^+\geq m-r); at
(r=1),

\[
D_m^+\geq {m-1\over4}.
\tag{13}
\]

The exact rounded statement is (12), not the weaker real-width version.

### Sharp smallest equality obstruction

The perfect four-mark Golomb ruler

\[
(0,1,4,6)
\tag{14}
\]

shows that no universal strict saving can be inserted into (9).  The
(m=1,r=1) shell contributes the difference (1) in ([1,1]).  The
(m=2,r=1) shell has gaps ((3,2)), total (5), mean (5/2), and
(D_2^+=1/2), so it contributes (3,2) in
([3/2,7/2]).  The common envelope ([1,7/2]) contains exactly the three
positive integers (1,2,3).  Hence both sides of (9) equal (3).

This is the smallest possible nested two-shell example.  It disproves a
strict-improvement claim, not the non-strict theorem.

## 3. Cross-boundary anti-diagonal packing

The next form uses old--new cross differences, rather than only differences
internal to a newborn shell.

For (1\leq k\leq m) and (0\leq t<k), put (s=k-t) and define

\[
d_{m,k,t}
=a_{m-1+s}-a_{m-1-t}
=N_{m+s}-N_{m-t}.
\tag{15}
\]

These are exactly (k) differences crossing the boundary between ranks
(m-1) and (m), on the rank anti-diagonal (t+s=k).  Define

\[
H_m=D_m^-+D_m^+,
\tag{16}
\]

\[
c_{m,k}^{(0)}=k\mu_m^+,
\qquad
c_{m,k}^{(1)}=(k-1)\mu_m^-+\mu_m^+,
\tag{17}
\]

and

\[
J_{m,k}=
\left[
 \min(c_{m,k}^{(0)},c_{m,k}^{(1)})-H_m,
 \max(c_{m,k}^{(0)},c_{m,k}^{(1)})+H_m
\right].
\tag{18}
\]

### Theorem B (exact cross-epoch anti-diagonal count)

For every finite collection (\mathcal T) of pairs ((m,k)),

\[
\boxed{
\sum_{(m,k)\in\mathcal T}k
\leq
\operatorname{cap}_+
\left(
 \min_{(m,k)\in\mathcal T}\inf J_{m,k},
 \max_{(m,k)\in\mathcal T}\sup J_{m,k}
\right).
}
\tag{19}
\]

Again, any smaller prescribed common containing band may replace the
envelope on the right.

#### Proof

Put (E_m^-(r)=N_r-r\mu_m^-).  Since (E_m^-(m)=0), the left arm of
(15) is

\[
N_m-N_{m-t}=t\mu_m^- -E_m^-(m-t),
\tag{20}
\]

while its right arm is

\[
N_{m+s}-N_m=s\mu_m^+ +E_m^+(s).
\tag{21}
\]

Consequently

\[
d_{m,k,t}
=t\mu_m^-+(k-t)\mu_m^+
 +E_m^+(k-t)-E_m^-(m-t).
\tag{22}
\]

The center in (22) is affine in (t); its extrema on
(0\leq t\leq k-1) are the two values in (17).  The error has magnitude at
most (H_m), proving (d_{m,k,t}\in J_{m,k}).

Every selected pair crosses the boundary (m), and its right endpoint lies
in the newborn block ({m,\ldots,2m-1}).  Distinct dyadic epochs have
disjoint newborn blocks.  Thus all selected endpoint pairs are different,
and Sidon uniqueness plus (7) proves (19).  \(\square\)

Since (k) distinct integers require real width at least (k-1), one
boundary already gives the exact necessary real-width inequality

\[
\boxed{
(k-1)|\mu_m^--\mu_m^+|+2(D_m^-+D_m^+)\geq k-1.
}
\tag{23}
\]

At an exactly endpoint-flat step, (N_{2m}=2N_m), so (G_m=N_m) and the
two means coincide.  Taking (k=m) in (23) yields

\[
\boxed{D_m^-+D_m^+\geq {m-1\over2}.}
\tag{24}
\]

More generally, with

\[
\varepsilon_m=e_{2m}(m)={N_m\over N_{2m}}-{1\over2},
\qquad
|\mu_m^--\mu_m^+|={2N_{2m}|\varepsilon_m|\over m},
\tag{25}
\]

(23) gives

\[
D_m^-+D_m^+
\geq {k-1\over2}
\left(1-{2N_{2m}|\varepsilon_m|\over m}\right)_+.
\tag{26}
\]

This quantifies a real restriction, but note its scale: under a critical
diameter (N_{2m}\asymp m^2\log m), (26) is informative about endpoint
flatness only at the much finer level
(|\varepsilon_m|=O(1/(m\log m))).

### Theorem C (cumulative low-band cross-epoch count)

Put (M_m=\max(\mu_m^-,\mu_m^+)).  For real (T\geq0), define

\[
R_m(T)=
\min\left\{
 m,
 \max\left(0,
  \left\lfloor{T-H_m\over M_m}\right\rfloor
 \right)
\right\}.
\tag{27}
\]

For any finite family of available dyadic epochs in one Sidon prefix,

\[
\boxed{
\sum_m {R_m(T)(R_m(T)+1)\over2}\leq\lfloor T\rfloor.
}
\tag{28}
\]

Indeed, for every (k\leq R_m(T)), (18) has upper endpoint at most
(kM_m+H_m\leq T).  Theorem B then counts all
(1+2+\cdots+R_m(T)) distinct positive cross differences below (T).
This is a genuine unbounded-history double count, with no asymptotic or
probabilistic input.

## 4. Theorem D: integrated global Carleson budgets

The cutoff in Theorem C has an exact threshold form.  For every available
pair \((m,k)\), \(1\leq k\leq m\), set

\[
\tau_{m,k}=H_m+kM_m.
\tag{28a}
\]

All genuine gaps are positive integers, so \(N_m\geq m\) and \(G_m\geq m\).
Consequently \(M_m\geq1\), \(H_m\geq0\), and

\[
\tau_{m,k}\geq1.
\]

Moreover, directly from (27),

\[
R_m(T)\geq k
\quad\Longleftrightarrow\quad
T\geq\tau_{m,k}.
\]

Thus (28) is equivalently the exact threshold ledger

\[
\boxed{
S(T):=
\sum_m\sum_{k=1}^m
k\,\mathbf 1_{\{\tau_{m,k}\leq T\}}
\leq\lfloor T\rfloor.
}
\tag{28b}
\]

For every real \(X\geq1\), this ledger implies the truncated endpoint
budget

\[
\boxed{
\sum_m\sum_{\substack{1\leq k\leq m\\ \tau_{m,k}\leq X}}
{k\over\tau_{m,k}}
\leq 1+\log X.
}
\tag{28c}
\]

For every real \(\epsilon>0\), it also implies the fractional Carleson
budget

\[
\boxed{
\sum_m\sum_{k=1}^m
{k\over\tau_{m,k}^{\,1+\epsilon}}
\leq {1+\epsilon\over\epsilon}.
}
\tag{28d}
\]

These claims hold for every finite family of dyadic epochs in one Sidon
prefix.  If one global infinite Sidon sequence supplies infinitely many
epochs, the same bounds follow by monotone convergence over its finite
initial epoch families.

#### Proof

For \(\tau\leq X\),

\[
{1\over\tau}
={1\over X}+\int_\tau^X{dT\over T^2}.
\]

Summing this identity with weight \(k\), exchanging the finite nonnegative
sum and integral, and then applying (28b) gives

\[
\begin{aligned}
\sum_{\tau_{m,k}\leq X}{k\over\tau_{m,k}}
 &={S(X)\over X}+\int_1^X{S(T)\over T^2}\,dT\\
 &\leq {\lfloor X\rfloor\over X}+\int_1^X{dT\over T}\\
 &\leq1+\log X.
\end{aligned}
\]

Likewise,

\[
{1\over\tau^{1+\epsilon}}
=(1+\epsilon)\int_\tau^\infty{dT\over T^{2+\epsilon}},
\]

so

\[
\begin{aligned}
\sum_{m,k}{k\over\tau_{m,k}^{1+\epsilon}}
 &=(1+\epsilon)\int_1^\infty
 {S(T)\over T^{2+\epsilon}}\,dT\\
 &\leq(1+\epsilon)\int_1^\infty{dT\over T^{1+\epsilon}}\\
 &={1+\epsilon\over\epsilon}.
\end{aligned}
\]

This proves (28c)--(28d).  \(\square\)

The endpoint is exactly where the present route stops.  At
\(\epsilon=0\), (28d) diverges and only the logarithmic truncation (28c)
survives.  The target for Problem #1191 requires a strict \(o(\log J)\)
innovation budget, so an \(O(\log)\) ledger is insufficient.  The
growing-depth Erdős--Turán family realizes the competing logarithmic order
on the innovation side of its compatible finite window.  Thus Theorem D
clarifies the endpoint obstruction; it does not solve it.

## 5. A minimal three-cycle finite obstruction

The following sixteen marks form one Golomb ruler:

\[
\begin{split}
(0,1,18,34,79,127,171,218,{}&319,415,509,613,\\
 &710,808,903,1002).
\end{split}
\tag{29}
\]

An independent exact recomputation gives all (\binom{16}{2}=120)
positive differences distinct.  Its three nontrivial newborn shells are

\[
\begin{array}{c|c|c|c|c}
m&\mathcal H_m&G_m&D_m^+&\delta_m^+\\ \hline
2&(17,16)&33&1/2&1/66\\
4&(45,48,44,47)&184&1&1/184\\
8&(101,96,94,104,97,98,95,99)&784&3&3/784
\end{array}
\tag{30}
\]

Thus every one of the three shells has

\[
\delta_m^+\leq {1\over66}.
\tag{31}
\]

The dyadic moduli are

\[
N_2=2,
\qquad N_4=35,
\qquad N_8=219,
\qquad N_{16}=1003.
\tag{32}
\]

The signed reset errors are exactly

\[
e_4(2)=-{31\over70},
\qquad
e_8(4)=-{149\over438},
\qquad
e_{16}(8)=-{565\over2006},
\tag{33}
\]

so every transition has (e_{2m}(m)\leq-1/4).

The exact normalized innovations are

\[
{(Q_2)_{00}\over N_4}={159\over89600},
\tag{34}
\]

\[
{(Q_4)_{00}\over N_8}
 ={2923819\over1145948160},
\qquad
{(Q_8)_{00}\over N_{16}}
 ={24647951033\over7219313737728}.
\tag{35}
\]

Each is strictly larger than (1/600).

This example also satisfies the canonical all-prefix (C=1) envelope,
not only its dyadic part.  The exact integer caps and moduli are

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
n&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16\\ \hline
N_n&2&19&35&80&128&172&219&320&416&510&614&711&809&904&1003\\
\lfloor2n^2\log n\rfloor
 &5&19&44&80&129&190&266&355&460&580&715&866&1034&1218&1419
\end{array}
\tag{36}
\]

The logarithmic floors in (36) are certified by rational atanh-series
enclosures, not floating-point comparisons.

This is a counterexample to every assertion of the form

> three consecutive nontrivial, strongly negative reset epochs with
> nearly rank-uniform newborn shells and uniformly positive (Q_{00}/N)
> must already collide.

Sixteen is the smallest possible terminal mark count for *three nontrivial
dyadic shells* (m=2,4,8).  No claim is made that (29) has smallest span or
optimal discrepancies.  Most importantly, (29) is finite.  It is not shown
to extend to one infinite globally critical Sidon sequence, so it does not
refute an unbounded-history theorem.

## 6. Why the exact inequalities do not give (o(\log J))

Theorems A--D give global distinctness charges, but their raw capacities
still contain the critical logarithmic slack.  At terminal scale (M), even
counting every complete dyadic shell gives only

\[
\sum_{\substack{m\leq M\\ m\ \mathrm{dyadic}}}m^2=O(M^2),
\]

whereas the critical diameter permits (O(M^2\log M)) integer values.
The low-band form (28) localizes the count, but changing mean gaps can renew
which value band is accessible.

The growing-depth Erdős--Turán rulers make the constant failure exact.  For

\[
b_i=2pi+r_i,
\qquad r_i=i^2\bmod p,
\qquad M\leq p<2M,
\tag{37}
\]

every rank-(k) difference lies in the same integer band

\[
b_{i+k}-b_i
\in \bigl[2pk-(p-1),\ 2pk+(p-1)\bigr],
\tag{38}
\]

whose exact capacity is (2p-1).  This includes both the length-(k)
shell sums in Theorem A and the anti-diagonal differences in Theorem B.

For the growing dyadic window with boundaries
(m_q=M/2^q), a fixed anti-diagonal (k) can occur at (q) boundaries
only if (k\leq M/2^q).  Hence its total selected cross differences obey

\[
qk\leq {qM\over2^q}\leq {M\over2}\leq {p\over2},
\tag{39}
\]

while (38) has capacity (2p-1).  Adjacent rank-lag bands are separated:
the upper endpoint for (k) is (2pk+p-1), whereas the lower endpoint for
(k+1) is (2pk+p+1).  Thus different lags cannot be pooled into one
overcrowded band.  For shell-internal length (k), the counts across the
dyadic shells are at most (sum_qm_q<M\leq p), again below the same
(2p-1) capacity.

So even the Erdős--Turán family with
((Q_m)_{00}/N_{2m}\to1/360) satisfies the exact band counts with a fixed
factor of slack.  This supplies the requested constant-level failure of a
direct (Q\)-to-band contradiction.  The family is finite and changes with
the terminal scale, so it remains a no-go for local-history proofs, not a
counterexample to the global problem.

Therefore (9), (19), and (28a)--(28d) do **not** imply

\[
\sum_{j\leq J}\operatorname{Var}_{\nu_j}(u(1-u))=o(\log J)
\]

or an (o(\log J)) adjoint innovation budget.

## 7. Sharp next candidate

The missing statement must couple **band renewal** to the old-history
profile.  A viable next lemma would have to show that, in one infinitely
extendible critical Sidon sequence, every large shift of the accessible mean
gap band either

1. spends a summable amount of signed old-profile variation, or
2. forces a positive fraction of the new anti-diagonals (J_{m,k}) to
   overlap bands already occupied at much older, non-comparable scales.

Theorem C is the exact arithmetic ledger for such a statement.  What is not
known is an inequality that prevents its cutoff (R_m(T)) from being renewed
at a sequence of increasing (T)'s.  High (Q_{00}) alone does not provide
that link, and the finite ruler (29) shows that three
reset-with-flat-newborn-shell cycles are insufficient.  It does not assert
that the complete old-plus-new profile is flat at those epochs.

`wave6_collision_bands.py` evaluates every endpoint using exact rational
arithmetic.  `test_wave6_collision_bands.py` checks the rounded capacities,
the equality example (14), the cross-boundary indexing, all 120 differences
of (29), all fifteen critical caps, the shell discrepancies, and the exact
innovations.  It also checks
\(R_m(T)\geq k\Longleftrightarrow T\geq\tau_{m,k}\) on both sides of every
fixture threshold, together with exact rational instances of (28c) and
(28d).

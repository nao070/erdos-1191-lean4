# Independent review of signed clock transport

2026-09-05. Reviewer: /root/moment_evidence_audit, GPT-6 Astra Ultra.

**Result.** The mathematical formulas and claimed summability ranges
are supported. One scope wording correction was requested and applied:
condition (29) characterizes a uniform upper bound for the net
commutator, not a two-sided bound for its absolute value. The final
reviewed source is `research/signed_clock_commutator.md`, SHA-256
`f7f02d6138e86f6e01048358ec3a83d0084e7975af257429d0d95dfdc40db8c5`.
The initial complete read had hash `b106c5a2...a73c5ad`; the final
changes clarify this upper-bound scope and distinguish the two reasons
for PSD and entrywise nonnegativity. No equations changed. The final
hash and changed passages were read back from disk.

This is an independent mathematical review, not formal verification.
No numerical experiment or repeated checker result is used as evidence.
The brand-new absolute-retirement comparison is not needed anywhere
in the reviewed argument. Other source notes were preserved. Q1 remains
unresolved.

## 1. Exact collision prices and the geometric deficit

The four formal retired records at a fixed U-slot m have later-source
clock equal to the maximum of their four source endpoints. This is a
record clock, not the birth of each individual label. The previously
reviewed automorphism normalization preserves these actual clocks, so
the slot sum in (4) is exact, including doubled labels.

There are at most two such source clocks per collision. Let ell be the
largest endpoint after the unique latest endpoint n is removed. A U-slot
removal changes that maximum only if ell occurs exactly once in U.
In that case only the ell-slot has the smaller source clock k'. This
proves both terms and signs in (5). Repetition of ell in U, or its
membership in V, leaves every source clock equal to k.

The identity
`6c_0^2-sigma_V^2=2(c_0-X)(c_0-Y)` follows from
`X+Y=-c_0`. Therefore
`G=2B-R=[6sigma_U^2+12(n-x)(n-y)]/A`, with the positive
automorphism divisor retained. This proves (6) and the exact
source-price excess (7). The displayed fixed-fixture arithmetic
`4008/400-7000/900=1009/450` is correct; its limited role is to
exclude an unconditional source-clock transfer for those prices.

## 2. The all-signed incidence count retains the tied clocks

For a same-sign retirement the positive magnitudes cannot share a
birth, since two labels in one positive birth star have an older
difference. For each older magnitude e, the newer magnitude satisfies
either a fixed nonzero difference equation, with at most one solution,
or a fixed two-sum equation, with at most two ordered solutions.
Including negative reflection gives at most `6q_(b-1)` records.

For opposite sources, the equation
`a_j-a_i=a_r-a_b-e` has nonzero right side: `a_r-a_b` is born
at r, while e is in the bank by b<r. Uniqueness applies equally
when that signed difference is positive or negative. Mixed old/new
magnitudes therefore give at most `2q_(b-1)` records.

For two new magnitudes, fixing the second magnitude permits at most
one first magnitude. Ordered magnitude pairs correspond exactly to
the actual unordered signed pairs, because their positive and negative
members are distinguishable. Equal magnitudes contribute one pair;
unequal magnitudes retain both reflected pairs. The bound is `b-1`.
Thus (9) is exactly

~~~
I_(b,r)<=8q_(b-1)+(b-1)=(b-1)(4b-7)<=4(b-1)^2.
~~~

This stronger bound does not omit same-birth opposite sources or
replace the actual birth stars with independent labels.

## 3. The near-clock exponent and every displayed constant

For the fixed compatible price u, monotonicity of H gives
`H_b^2(u_b-u_r)<=alpha_b-alpha_r`. The derivative of
`alpha(x)=1/[x^2(x-1)^2]` has magnitude
`2alpha(x)[1/x+1/(x-1)]`, bounded above by
`4alpha_b/(b-1)` for x>=b. Integrating over length h proves
(11). Multiplying by (9), using `|de|<=H_b^2`, and summing
h proves `8L_b(L_b+1)/[b^2(b-1)]`. For b>=3,
`b/(b-1)<=3/2`, giving exactly both constants 12 in (12).
The main series has exponent `2gamma>1`; the second is already
dominated by a convergent inverse-square series.

The u tail is fixed from one complete history, is convergent, and
is not reselected at T. This argument needs no cap. The b=2 bank
has just one possible source pair, whose total variation contribution
is at most `1/4`; it can be absorbed regardless of the convention
for its initial near set.

For w, the decomposition preceding (14) is exact.
`1-exp(-2x)<=2x` and `alpha_r<=alpha_b` give (14).
Combining with `I_(b,r)<=4(b-1)^2` gives the coefficient
`8/b^2` in (15).

For b in `[N,2N)`, the lag is at most
`L_*=floor[2N/(log N)^gamma]`. A radius increment indexed by l
can be crossed only by integers b in `(l-L_*,l]`, at most
L_* choices, each with at most L_* choices of h. This proves
the square count without a rounding loss, also when L_*=0.
All contributing increments lie inside `[N,4N)`. Hence the
coefficient 32 and the exact telescoped radius ratio in (16)
are correct.

The actual integer Sidon bank gives `H_N>=Q_N/2>=N^2/4`
for N>=2. Applying the one fixed cap to 4N then gives
`H_(4N)/H_N<=64 C_cap log(8N)`. After one dyadic onset,
(18) is bounded by a constant times
`sum_j log(j+2)/j^(2gamma)`, which converges precisely throughout
the asserted range gamma>1/2. No pointwise small radius ratio is
assumed. Finite initial source ranks contain finitely many records
and give a horizon-independent initial charge. Thus (19) is valid
with the stated fixed-cap dependence.

The estimates remove the commutator in total variation on the near
record set. They can split complete collisions and do not authorize
discarding the full geometric deficit when using (28).

## 4. Global identities use the same physical outputs

Each retired record belongs to `L_(n,T)` exactly on the integer
interval `b<=n<r`. Telescoping the coefficient difference over that
interval proves (20), with no copied intermediate budget.

The full raw off-diagonal signed sum is `-Z_n/2`; the used-output
sum is `(E_n-nZ_n)/2`. Their difference proves (21), including
the indispensable terminal-unused subtraction. The terminal-unused
set means not used by T, not permanently absent from the history.

Signed class centering gives zero matrix mass for the fixed weighted
source U^c. Its Born/retired/terminal-unused partition yields (22).
Combining that identity with the full signed Abel identity gives
`J+p=(D-s-A)/2` exactly, verifying (23) and all factors of two.

For c=w or u the prices are nonnegative and decreasing. Their
nonnegative nested-prefix decomposition proves PSD. The separate
pointwise bound `c_b H_b^2<=alpha_b` gives entrywise nonnegativity
of `W=V+lambda U^c`; these two justifications are now correctly
distinguished in the final source.

With a fixed terminal mask, current capacity is linear, so
`C_cur(V)-C_cur(W)=-lambda p`. Substitution proves (24).
Dropping nonnegative `C_cur(W)`, s, and then taking the positive
part proves (25), including its coefficient `1/lambda` and the
diagonal constant `[2zeta(2)-1]/2`.

For an entrywise nonnegative fixed source, a label outside F_T has
an increasing kernel until T. Its historical maximum is therefore
the terminal value, proving the exact split (26). Actual blocks
inside P_T have differences in F_T; with an old source prefix before
the block, those differences were unused at that source time. Thus
the stated blocks charge only the retired-output part. The current
unused part is physically disjoint at that horizon, without implying
it stays unused later. The restriction to literal fixed-source
kernels or dominated subsources is necessary and is retained.

The recordwise carrier bounds are also correct. Each retired record
contributes its fixed entry once to historical capacity; for positive
products, `W_de>=(1+lambda)c_b de`. This proves (27), while
preserving the distinction between a net positive part and the sum
of positive record contributions. These coarser bounds do not make
the same capacity available twice.

## 5. The remaining scope is an upper bound, not absolute boundedness

The exact multiset comparison proves the nonnegative full deficit
used in (28), including twice the nonnegative Born-only remainder.
Equations (28) and (30) are correct equivalent formulations of the
stated source-price excess bound.

From (24),

~~~
J_T = [C_cur,T(V)-C_cur,T(W)]/lambda-A_T/2+(D_T-s_T)/2.
~~~

The trace is bounded for these prices: since
`v_n<=2(n-1)H_n^2` and `c_n<=w_n`, one may use
`s_T<=sum_(n>=2)2/[n^2(n-1)]=4-2zeta(2)`.
Together with the recorded bounded diagonal, this shows that (29)
is equivalent up to bounded terms to `J_T<=O(1)`. It does not
control a negative divergence of J_T and therefore is not equivalent
to `|J_T|<=O(1)`. The final wording explicitly says “upper bound,”
resolving the review's sole scope correction.

No bound for the entire far-clock variation, no proof of (29) or
(30), and no closing shared-budget estimate is inferred. The reviewed
new contributions are the exact two-price reduction, all-signed
incidence count, gamma>1/2 near-transport summability, and the precise
terminal-unused capacity identity.

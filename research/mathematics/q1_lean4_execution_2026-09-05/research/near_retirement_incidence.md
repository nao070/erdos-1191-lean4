# Near retirement: summable boundary pieces and an actual six-endpoint incidence core

Date: 2026-09-05T08:01:47.210005+00:00. Owner: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

**Status.** Three additional absolute summability statements and deterministic endpoint-incidence bounds are proved below. Together with the existing late-retirement tail, they isolate a six-distinct, nearly quadratic physical-scale core. An explicit cap-sensitive incidence estimate sufficient to make retirement less than half the Abel energy is stated, not proved. The physical-margin obligation remains separate. Original Q1 and its Lean proof are unresolved. No numerical experiment or Lean execution was used, and other source files were preserved.

The assigned notes `causal_birth_energy_telescoping.md`, `late_retirement_tail.md`, `endpoint_batch_entropy_obstruction.md`, `nested_small_difference_bank.md`, and `fixed_width_bank_density.md` were read. The repeated-triple counting argument in the reviewed `birth_linear_total_causal_sign.md` is also used, with its weighted consequence derived here. No independent-label model or failed general centered-operator estimate is reused.

## 1. Literal births, weights, and the scalar incidence matrix

Fix one increasing infinite integer Sidon history, with repeated two-sums unique. Retain its actual banks and permanent birth-linear coefficients:

```
F_n=Delta P_n,  G_n=F_n\F_(n-1),  q_n=binom(n,2),
H_n=a_n-a_1,
g_(a_j-a_i)=mean(P_(j-1))-a_i,
v_n=sum_(d in G_n)g_d^2,  S_n=sum_(d in F_n)g_d^2,
w_n=1/(q_n^2 H_n^2).
```

For a retired source pair write `b=max(tau(d),tau(e))`, `r=tau(|d-e|)>b`, and `t=|d-e|`. Same-birth sources cannot retire: their difference is in the earlier bank. Thus there is exactly one source `d in G_b` and one `e in F_(b-1)`. Every such pair has at most one actual output birth. Always

```
w_r |g_d g_e| <= w_b |g_d g_e| <= 1/q_b^2.                 (1)
```

For fixed `b<r`, let I_(b,r) be the number of these retired pairs. This is a bipartite incidence count between G_b and F_(b-1), with output in G_r.

**Endpoint intersection lemma.** For any fixed old source e, at most three new sources d can give such an incidence at r.

Write `d=a_b-a_i`, `t=a_r-a_j`, with i<b and j<r. If d>e, the equality d-e=t becomes

```
a_j-a_i=a_r-a_b+e>0.
```

Positive-difference uniqueness permits at most one ordered pair (i,j). If d<e, e-d=t becomes

```
a_i+a_j=a_b+a_r-e.
```

Repeated-summand Sidonness permits at most one unordered pair, hence at most two ordered assignments. The two cases are disjoint. In particular

```
I_(b,r) <= 3q_(b-1).                                      (2)
```

This is a bound for one literal pair of birth stars. It is not an operator-norm assertion for the entire retirement graph.

## 2. The ultra-near retirement clock is absolutely summable

Fix gamma>1. At source birth b>=3, the ranks satisfying

```
0<r-b<=floor[b/(log b)^gamma]
```

number at most b/(log b)^gamma. Equations (1)–(2) give

```
sum_(these retired pairs at b) w_r |g_d g_e|
 <= 3q_(b-1) floor[b/(log b)^gamma]/q_b^2
 <= 6/[b(log b)^gamma].                                  (3)
```

Therefore

```
sum_(0<r-b<=b/(log b)^gamma) w_r |g_d g_e|
 <= 6 sum_(b>=3)1/[b(log b)^gamma] < infinity.              (4)
```

The bound is independent of the history, its cap, and the terminal horizon. Birth b=2 has no mixed pair. Formula (3) uses `3q_(b-1)/q_b²=6(b-2)/(b²(b-1))`; no second sum over possible realizations of one output label occurs.

Thus the closest births, including any fixed additive lag, cannot carry the divergent retirement-clock contribution. The remaining close-time problem is broader than just the next few ranks.

## 3. Subquadratic output labels give another summable piece

Fix beta>1 and put `D_b=floor[b²/(log b)^beta]`. For a fixed source birth b and a fixed positive target t, each d in G_b permits at most two old partners: e=d-t or e=d+t. Consequently at most

```
2(b-1)D_b
```

source pairs at b can have output t<=D_b, over **all** future retirement ranks together. Each pair retires at most once. By (1),

```
sum_(retired, t<=b²/(log b)^beta) w_r |g_d g_e|
 <= 8 sum_(b>=3)1/[(b-1)(log b)^beta]
 <= 12 sum_(b>=3)1/[b(log b)^beta] < infinity.              (5)
```

This does not introduce a fresh budget for each retirement rank or width. The target is a literal numeric difference, and the count is attached once to its source pair. No cap or density premise is used.

## 4. Repeated-endpoint near retirements are also summable

Fix alpha>1/4, as in `late_retirement_tail.md`. For a dyadic source scale N>=2, set

```
L_N=ceil[2N(log(2N))^alpha].
```

A near retirement with `N<=b<2N` and `r<b(log b)^alpha` uses only points of P_(L_N). A retired pair yields a nontrivial equality of unordered triple multisets. The automatic coincident-triple case cannot retire.

Distinct equal-sum triple multisets have disjoint supports, by cancellation and Sidon two-sum uniqueness. There are at most L_N² repeated-point triples, and each has at most L_N partners. At most six slot matchings and two possible used source pairs per matching give at most `12L_N³` records involving a repeated point. This is the same safe unweighted counting bound used in the full-causal-total note; it includes all repeated slots and can overcount.

Each record at this source scale costs at most 1/q_N² by (1). Hence the absolute weighted contribution is bounded by

```
12L_N³/q_N² = O_alpha((log(2N))^(3alpha)/N).               (6)
```

Summing (6) over N=2^k is finite. Equivalently, the history-independent constant

```
C_rep(alpha)=12 sum_(k>=1) L_(2^k)³/q_(2^k)²
```

is finite. This weighted conclusion does not assert that all unweighted repeated-triple counts are small at an arbitrary infinite horizon.

The three new estimates (4), (5), and (6) remain true with w_b in place of w_r, and therefore also bound their source/retirement lag-weight difference on these same sets, because their proofs use the stronger part of (1). The older **late-rank** tail is still specific to w_r; it must not be transferred to w_b.

## 5. The residual core and exact short-star packing

Define R_T^core to retain only retired pairs through T satisfying all four conditions:

```
r-b > b/(log b)^gamma,
r < b(log b)^alpha,
t > b²/(log b)^beta,
the associated two triple multisets have six distinct endpoints.
```

Combining (4)–(6) with the saved late-tail estimate proves, for every T,

```
|R_T(w)-R_T^core| <= C_(alpha,beta,gamma).                  (7)
```

The omitted sets may overlap; the triangle inequality and the sum of their finite absolute bounds suffice. The constant is independent of the actual history. In particular the exact Abel identity becomes

```
2B_T(w)+2R_T^core+D_T(w)=A_T(w)+O_(alpha,beta,gamma)(1).    (8)
```

There are additional deterministic bounds on the surviving incidence. Let

```
m_(b,r)=|G_r intersect [1,H_b]|.
```

This is the number of actual points a_j preceding a_r in its backward interval of length H_b. Its corresponding label star is a reflected subset of the actual Sidon sequence, and its differences belong to F_(r-1). Thus

```
binom(m_(b,r),2)<=H_b-1,
m_(b,r)<=sqrt(2H_b)+1.                                   (9)
```

For the bipartite incidence of section 1, the new-source degree is at most 2m_(b,r); the old-source degree is at most three. Cauchy therefore gives the valid local weighted estimate

```
|sum_(d in G_b,e in F_(b-1), |d-e| in G_r)g_d g_e|
 <= sqrt(6m_(b,r) v_b S_(b-1)).                           (10)
```

The same bound holds for any restricted core edge set, and the unweighted count is at most `min(3q_(b-1),2(b-1)m_(b,r))`. For the core one may replace m_(b,r) by the smaller number of target-star labels in `(D_b,H_b]`.

Physical-label disjointness also gives the literal packing identity and bound

```
sum_(r=b+1..R) m_(b,r)
 = |(F_R\F_b) intersect [1,H_b]| <= H_b-q_b.              (11)
```

This retains the already-used-old-label mask. If only targets in `(D_b,H_b]` are allowed, replace the right side by the cardinality of that interval minus its intersection with F_b (zero if D_b>=H_b).

To express (11) in dyadic point batches without dropping cross terms, partition point ranks into disjoint dyadic sets B_j, putting any finite initial ranks in a separate initial batch. For each i<=j, retain every pair with lower endpoint in B_i and upper endpoint in B_j; when i=j use the internal pairs. Their positive-difference sets are pairwise disjoint by actual Sidon injectivity. The output stars are partitioned by **all** these rectangles. Summing only the internal sets Delta B_j would omit cross-batch differences and would not prove (11).

Equations (9)–(11) are genuine deterministic clique/intersection constraints. They do not supply the missing logarithmic saving: a physical target can still meet many source pairs. For example, at a source dyad N, a fixed t occurs in at most

```
2 sum_(b=N..2N-1)(b-1)=3N(N-1)
```

candidate pairs. This multiplicity must remain when a target-label budget is used across different source births. One cannot apply (11) independently at every b and then claim a single copy of the resulting right sides.

## 6. Why the remaining incidence is cap-sensitive

Under one fixed-onset diameter cap `H_b<=C b² log(2b)`, the surviving physical outputs lie in

```
b²/(log b)^beta < t <= C b² log(2b).                      (12)
```

For every large b this occupies only `O_(C,beta)(log log b)` dyadic physical bands. The source/retirement dyadic rank indices differ by at most `alpha log_2(log b)+1`. All six endpoints remain actual, and the distinct-triple relations are imposed, not relaxed away.

This is exactly the boundary where the existing fixed-width density result cannot be applied with a fixed positive constant. If D is comparable to b² times a power of log b, the exponent `theta=log b/log D` tends to 1/2. The proved uniform density bound requires theta in a **fixed compact subinterval** of (1/2,1). Substituting these drifting exponents would be invalid. For any fixed delta>0, widths up to b^(2-delta) are eventually inside the already summable set of section 3.

Thus the cap supplies a narrow physical and rank window for the remaining six-point incidences, but not their required upper bound. Neither independence of real difference labels nor a uniform-density replacement of their kernels is asserted.

## 7. A concrete incidence estimate sufficient for subcritical retirement

Let I_N^core be the **unweighted number of actual core retired source pairs** with `N<=b<2N`, including all their near future outputs up to L_N. All endpoint identifications, the original Sidon property, the two time inequalities, and the physical cutoff are part of this definition. Each pair is counted once, at its source birth dyad. For a dyadic terminal T,

```
R_T^core <= sum_(N=2^k<T) I_N^core/q_N².                  (13)
```

Future retirements beyond T may enter the right side; this only enlarges a nonnegative upper bound. Source births at or beyond T do not enter the left side. This is a new incidence-count route to an upper bound, not an equality replacing signed products by arbitrary positive coefficients.

For comparison put

```
Eblock_N=sum_(n=N..2N-1)(w_n-w_(n+1))E_n,
Lambda_N=(45/32)N² S_N²/(q_N² H_N² H_(2N)³).
```

The same moment argument as in the causal note, without assuming a good epoch, proves

```
Eblock_N>=Lambda_N>=0.                                   (14)
```

Indeed every E_n in this block is at least `(3/2)N²S_N²/H_(2N)³`, and `w_N-w_(2N)>=15w_N/16`. On dyadic terminal horizons these energy blocks are disjoint parts of the Abel interior.

One explicit **sufficient incidence theorem**, presently unproved, would be: for some fixed kappa<1/2, beyond a fixed onset along the capped actual history,

```
I_N^core <= kappa*(45/32) N² S_N²/(H_N² H_(2N)³)
                                                   for every dyadic N.    (15)
```

Combining (7), (13)–(15) would give

```
R_T(w)<=kappa A_T(w)+O(1)                               (16)
```

along unbounded dyadic terminal horizons. The uniformly summable tails and the finite initial source dyads are included in O(1).

There is a less pointwise version which keeps every nongood dyad. Let G be the existing productive dyadic old ranks, with `S_N>=eta q_N H_N²`, `H_(2N)<=K H_N`, and divergent reciprocal-log weight. Write `c_*=45eta²/(32K³)`. A sufficient alternative is

```
sum_(all dyadic N<T) I_N^core/q_N²
 <= kappa*c_* sum_(N in G, N<T) N²/H_N + O(1).             (17)
```

The causal note gives `A_T>=c_* sum_(N in G,N<T)N²/H_N`, so (17) again yields (16). No nongood source dyad is discarded on the left. Under the cap the productive right side diverges, but that fact does not prove the upper incidence inequality.

At a good dyad, the natural count scale in (15) is `N²q_N²/H_N`, of order `N^4/log N` when H_N is of critical order. The elementary star and packing bounds above allow order N^4 records and do not by themselves give this saving or its coefficient. An argument for (15) or (17) must exploit the cap together with the actual six-endpoint equations. These are sufficient targets, not necessary conditions: a signed-cancellation argument could prove (16) without such an unweighted upper bound.

Finally, (16) and the divergent Abel identity would imply divergence of B_T(w). They would **not** pay the separate physical margin in equation (24) of `causal_birth_energy_telescoping.md`. Neither that margin nor the source-time late-retirement commutator is removed by this note.

## 8. Outcome

The newly proved absolute bounds remove ultra-near rank lags, sufficiently short output labels, and repeated-endpoint near configurations. The local birth-star intersection bound, weighted Cauchy inequality, and exact dyadic-rectangle packing retain the real endpoints and used-label exclusions. The remaining task is a cap-sensitive upper bound for six-distinct incidences in the narrow window (12), with a precise sufficient target (15) or (17). That bound, the shared physical margin, and Q1 remain unresolved.

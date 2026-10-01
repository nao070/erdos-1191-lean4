# Parent review of the joint projection and new signed-source accounting

2026-09-05. Reviewer: `/root`, GPT-6 Astra Ultra.

This review records independent mathematical checks of the current
nonformal source notes. It does not extend the existing Lean scope,
constitute a new Lean run, or establish original Q1. The complete
joint-projection note and the source/radius notes were read; the
final additional comparison in the causal-source note was read
separately after the author's final update.

## Joint projection: exact coefficients and the residual matrix

Reviewed source: `research/joint_shadow_projection.md`, SHA-256
`8aa71fd552b68c44f1dc87249210683fb9428ebd2d0cb378466474872b0dc5b5`.

The projection onto the constant and centered coordinate vectors
uses their orthogonality, squared norms D and V, and the exact
shadow masses M and zero. Subtracting both projected components
therefore gives all three identities in (1), including the cross
coefficient Delta0*Iz/V. Expanding the full matrix energy gives
the residual `||u+t v||^2+(s-t^2)||v||^2`, with no diagonal or
cross coefficient omitted. On V=0 the integer support is a singleton,
the centered signed shadow is zero, and all moment quotients are
correctly assigned zero.

Division by 2q^2 gives beta=Delta0*Iz/(q^2 V), without an extra
factor two. Subtracting the previous cone demand gives exactly

```
[(Delta0+t Iz)^2/V+(s-t^2)(Iz^2/V-LB_old)]/(2q^2).
```

The full-interval variance dominates the variance of its subset
Omega after optimal recentering, so this is nonnegative. The raw
demand qualification is necessary outside the already established
large good blocks. The common trace bound and that dominance
justify the positive-part comparison on those blocks only.

For fixed allocation the row objective is linear:
`(A-beta)t+(rho-d)s`. Minimizing first over s chooses t^2 when
rho-d>=0 and ell otherwise. This gives (6) and then the stated
finite minimax expression (7). Its zero criterion requires both
rho>=d and A=beta, together with baseline-maximal allocation;
replacing the latter equality by A=0 would lose the projected
cross term. The finite parameter domain is compact and convex,
and the introduced allocation payoff is affine in both variables,
so the stated finite minimax use is valid.

At the actual future-block allocation, the exact pair expansions
give respectively R00/(2q^2), R01/q^2, and R11/(2q^2).
Thus its moment positive-part penalty remains zero. Expanding
`||u+t v||^2` proves (10), including the clipped optimizer and
the R11=0 case. Adding the literal maximum-minus-selected-row
terms proves (11). Neither the old hole-variance lower bound nor
the old unit projection increment remains an unpaid residual
after it has been included in this new demand.

The centroid identity (12) follows by summing the convolution
first moment. The conditional estimate (13) uses
V<=33^3 H^3/12, and its constant six is correct. The singleton
future-block example has an exactly constant unit shadow, so it
correctly illustrates that Sidonness alone does not force a nonzero
centroid discrepancy. It makes no large-good-epoch assertion.

## Odd signed shadows: orthogonality and the sharper fixed-kernel demand

The odd signed kernel has zero linear physical correlation at
every output. Hence its full cross energy is zero, but the two
projected first moments need not have zero product. Subtracting
the exact projection makes the residual cross its negative.

The signed support is the interval of length T=L+2H with all m
future points removed. Direct summation of its coordinates gives
`Delta0=mQ*T/(T-m)*(mean(B)-c_J)`, exactly (14). At fixed s,
t does not affect capacity; maximizing the affine demand over
|t|<=sqrt(s) therefore gives t=sign(beta)*sqrt(s). This proves

```
E0+s Ez >= M^2/D+(|Delta0|+sqrt(s)|Iz|)^2/V.
```

The same formula follows from the residual Gram inequality, so
the extra cross contribution is fully paid. This sharpens the
specified demand; it does not add a new physical source.

For the actual five-point example {0,4,10,11,13}, the six shadow
locations sum to 68, whereas the nine support coordinates sum
to 104. Their square sum is 1340. Consequently V=1244/9,
Delta0=-4/3, Iz=24, and beta=-18/311, as stated. The full
cross energy is zero by the three positive and three negative
shadow values. The raw demand stays negative throughout the
stated parameter domain; for instance d<0 and
delta0+chi+|beta|<0 already give a uniform upper bound. This
example is therefore correctly limited to the projected-cross
distinction, not a positive payable demand.

For the conditional good-block estimate, (14) gives
|Delta0|>=mQ epsilon H, and the assumed first moment gives
|Iz|>=nu mQH. Dividing their product by Q^2 V and using
T<=34H gives exactly the constant 12 in (16). The old variance
also gives nu=eta for sign and linear features: each prefix
variance is at most the final point variance, and
sum_(positive differences)d^2=N V_P. The further step
sum d>=sum d^2/H is valid term by term. The future asymmetry
condition and its necessary frequency are still unproved.

All formulas (1)--(16) and their boundary conditions are supported.
The actual shared physical margin is not estimated by these
projection identities.

## Permanent, layered and radius sources

The complete `signed_causal_source.md` was independently checked,
including final equations (14a)--(14b), at final source SHA-256
`8806a3f6f5f5cc7964a43d34b64c014c1fddcc09182ab6db65a31da2e11d772d`.
The exact prefix mass and traces telescope as stated. Whole-prefix
Hilbert-space Cauchy has matrix mass M_N, rather than its square,
and its moment numerator is d^T U_N d. Its stated eventual
negative certificate follows from J_N<=H_N^2 M_N and the
strictly positive permanent early trace. The negative combined
layer entry and the distinction between PSD and entrywise
nonnegativity are correct.

For the alternative source, the complete-history tail is convergent
and explicitly distinguished from an online rule. Its actual current
tails are nonnegative component subsets. The pair indicator in
(18) is zero or one because the actual block difference sets are
disjoint. Expanding the same component weights on both sides
therefore gives the exact unspent-pair and demand-slack identity.
The factor 15/(16*32^2), mS diagonal subtraction, and both
current-unused capacity constants are correct. Subtracting the
coefficient tails proves (14a); its signed kernel does not transfer
the other source's future payments merely by PSD ordering.

The complete `signed_radius_localization.md` was also checked,
at source SHA-256
`f9cd27d8c90f595661de07f8889f1bf0dd3161cb7a32f319ee0b11f7e331d4c7`.
The radius-boundary group formulas agree with the full signed
Schur partition. Their integrated A_* formulas, doubled-label
coefficients, and finite missing tail all agree. The finite
background identity (12) retains its extra rank-one mass and
trace. The direct threshold representation removes that extra
background by constructing a different, fully priced matrix.
The first-moment cross-gap count gives kappa=1/256, with the
stated good-row demand and single physical maximum. The lambda=1
endpoint really has the same normalized kernel as the positive
weighted-minimum source.

Separate full independent reviews are saved for both source notes,
the annular capacity bound, and the five-point retirement boundary.
No finite test was repeated by this parent mathematical review.
The new fixed retirement executions have separate instrumented
records and byte readbacks; their finite scopes remain distinct
from these analytic statements and from Lean verification.

## Complete retirement fibers and quantitative permanent Born saving

The complete retirement-fiber derivation was independently read and
rederived, with its final clock clarification checked at source SHA-256
`af256edc1cd1812a9069823b906f89328de6fb85aec6e087a7ff6a4a851cc8c9`.
For six distinct endpoints, pairing the newest endpoint with each of
the three opposite endpoints gives two matchings and four retirement
records. Summing their products gives the stated centered expression
`R=2 sigma_U^2+6 sigma_V^2-12c^2`; the companion Born total is
`B=4 sigma_U^2+12c^2`. The complete-fiber coefficients follow by
counting separately how often a triple is earlier and later in an
unordered pair. The repeated-point cumulative and stagewise absolute
bounds are valid as weaker estimates, not exact error formulas.

The six-point example has core retirement 4008 and Born 3500.
All its core retirement source clocks are 5, whereas the Born and
retirement output clocks are 6. Thus the exact rational difference
`4008/400-7000/900=1009/450` really is positive. It rules out the
asserted source-price transfer even for a complete six-distinct
collision. The fixed execution separately confirms the retirement
enumeration and centered formula, not the general Born theorem.

The complete quantitative Born note was independently read, including
the added signed Abel section, at final source SHA-256
`6e463ac1b8e24c9d950a81550b4c91bd0df18c0eb75a8aab2739d613f0628ddb`.
The full preceding version was read first; its sole subsequent
wording correction about energy monotonicity was then reread.
The independent review retains the earlier version binding and
appends the current one. No formula in that note changed.
Its first-moment estimate uses support length `3H+1` and numerator
`N^2 Z^2`, giving `E>=N^2 Z^2/(5H^3)`. Combining this with the
weaker repeated-point bound gives the stated weighted Born lower
bound. The good cross-gap count allows eta=2^-14; no positive
proportion of all good indices is assumed. The Abel lower bound
uses disjoint rank intervals `[N,2N)` and actual nonnegative Born
increments. The alternative u-price uses its own difference
`u_b-u_(b+1)=kappa_b/H_b^2`, without a global u/w comparability
assumption. Both divergences are therefore supported.

The signed increment has diagonal `Z_(j-1)+j v_j`. Its coefficient
is j, not j-1. The weighted bound splits as
`2/j^2+1/[j(j-1)]` and sums to `2 zeta(2)-1`. The good-window
lower bound for the Abel interior does not assume E_n is monotone:
it uses monotone Z_n and the actual good bound `H_(2N)<=32H_N`.
The stated logarithmic rate is in the dyadic exponent J. These
facts prove divergence of the specified historical Born savings;
they do not bound the remaining common physical margin.

## Exact multiset extension: removal of the repeated-point error

The full final `signed_multiset_born_retirement.md` was independently
read and its orbit cases and formulas rederived by the parent, at
SHA-256
`324a0eb718acc0f7b5830bbd6723546e9963b457df7dc26256e5b0a1e85e8487`.
The separate full independent review binds to the same final bytes.

Cancellation of a common triple endpoint uses the original Sidon
condition with repeated two-sums, so distinct equal-sum triple
multisets have disjoint support. The newest endpoint in a retired
record occurs once. A labeled edge pattern has multiplicity
`aut(U)aut(V)/product c_(u,v)!`. Positive-difference uniqueness
leaves exactly two relevant stabilizers: one for three distinct
edges, two for a doubled edge. In the second case the formal
six-entry Schur list counts each actual pair twice, exactly
cancelling the stabilizer. The counting rule is therefore valid
separately for Born and retirement, including their clocks.

For A=aut(U)aut(V), all active collision contributions are

```
B=(4 sigma_U^2+12c^2)/A,
R=(2 sigma_U^2+6 sigma_V^2-12c^2)/A.
```

Writing the other centered V-slots as X,Y, the constraints
X+Y=-c and X,Y<=c imply `(c-X)(c-Y)>=0` and hence
`X^2+Y^2+c^2<=6c^2`. Thus
`2B-R=6(sigma_U^2+6c^2-sigma_V^2)/A>=0`.
This argument remains valid with repeated slots. Groups outside
these active collisions have no retirement and a nonnegative
whole Born total. Their clocks are the latest label clock, so
the stage partition proves exactly `R_j<=2B_j`, with no error.

The repeated examples and both parameterized Sidon families were
checked analytically. The ratio approaching two is a statement
about a single collision, not an optimal full-stage ratio or an
infinite capped history. No finite test was added by this review.

## Parent corollary: sharper constants in the quantitative note

Keep the reviewed quantitative note unchanged as a valid weaker
result. Its exact multiset strengthening is immediate as follows.
From `E_N=N Z_N+2B_(<=N)+2R_(<=N)` one now has

```
B_(<=N) >= (E_N-N Z_N)/6.
```

At a good N with Z_N>=eta Q_N H_N^2 and
H_N<=Ccap N^2 log(2N), multiplication by
w_N=1/(Q_N^2 H_N^2) therefore gives

```
w_N B_(<=N)
 >= eta^2/[30 Ccap log(2N)] - 1/[6(N-1)].
```

The former `4N/(N-1)^2` error is absent. Indeed the positive
term is `eta^2 N^2/(30H_N)` and the diagonal bound is
`N Z_N/(6 Q_N^2 H_N^2)<=N/(6Q_N)`.
The same disjoint-window Abel arguments prove both w- and
u-priced Born divergence with the stronger summable error.

For any finite terminal T, define
`A_T(w)=w_T E_T+sum_(n<T)(w_n-w_(n+1))E_n` from the initial
zero state. The exact signed increment and nonnegative stage
weights give

```
A_T(w)=D_T(w)+2B_T(w)+2R_T^out(w)
      <=6B_T(w)+2 zeta(2)-1.
```

The former repeated-point constant is absent here as well.
This still prices retirement by output time. It neither replaces
the source-price commutator nor estimates the unused/span/overlap
part of a common physical source. These sharper constants are
analytical consequences, not additional Lean verification.

## Lower retirement bound and energy monotonicity

The parent independently derived the lower collision identity and
read the full final `research/signed_energy_two_sided.md`, SHA-256
`1364dd87dc4290f50e3a7367500c1059519beba24eb076202c1a559c87d6dcb2`.
It is separately independently reviewed. Since X+Y=-c,
`2 sigma_V^2-3c^2=(X-Y)^2`; hence

```
R+B/4=3[sigma_U^2+(x-y)^2]/A>=0.
```

The Born-only remainder has the right sign for the lower bound:
minus one quarter of active Born is at least minus one quarter
of full Born. Therefore `-B_j/4<=R_j<=2B_j`, and the exact signed
increment gives

```
Dhat_j+(3/2)B_j <= E_j-E_(j-1) <= Dhat_j+6B_j.
```

The new variance increment is strictly positive at each actual
j>=2. Thus E_j is strictly increasing, and Y_j=E_j-jZ_j is
nondecreasing. The arbitrary nonnegative-price comparisons in
(8), the nonnegative Abel expressions for decreasing prices,
and the stated uniform diagonal constants all follow directly.
The raw current-unused sum equals `-[Z_N+Y_N]/2`, giving the
exact same-row saving in (12)--(13). This does not assign a sign
to a permanent source evaluated on a later unused mask, nor
transfer a sum through maxima of differently normalized rows.

The former quantitative note's sentence suggesting E_n need not
be monotone was incorrect for this particular raw-linear bank.
It is now minimally corrected to state that its argument does
not require monotonicity. The earlier proof and constants remain
valid. No finite experiment, Lean replay or final-Q1 conclusion
is claimed for these new analytical consequences.

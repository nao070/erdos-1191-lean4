# Causal birth energy with separate source and retirement clocks

Date: 2026-09-05. Owner: `/root/causal_telescoping`, GPT-6 Astra Ultra.

**Status.** Proved finite weighted identities, a uniformly summable
diagonal charge, and divergence of a nonnegative Abel energy under the
existing full-history cap and good-epoch hypotheses. A single physical
source matrix realizes the weighted causal term exactly. Its mass and
its actual demand costs are retained. The needed joint retirement and
physical-margin estimate is stated, not proved. Original Q1 and its
required Lean verification remain unresolved. No finite sign search,
numerical experiment, external theorem, or new Lean declaration is used.

The six inputs requested for this task were read:
`birth_linear_good_epoch.md`, `retirement_shadow_review.md`,
`weighted_birth_envelope.md`, `coherent_birth_linear_envelope.md`,
`future_moment_demand.md`, and `birth_linear_born_term.md`.
The causal increment definition in `birth_centered_transport.md` §2
was also read and rederived below for the real, fixed birth-linear
coefficients. The older terminal-cap counterexamples are not repeated.

## 1. Fixed raw coefficients and the two actual clocks

Let `P_N={a_1<...<a_N}` be an actual integer Sidon set, including
repeated two-sums. Set `P_n={a_1,...,a_n}`, `F_n=Delta P_n`,
`G_n=F_n\F_(n-1)`, `q_n=n(n-1)/2`, and `H_n=a_n-a_1>0`
for `n>=2`. The symbol `H_n` here always denotes diameter.

The actual birth `tau(a_j-a_i)=j` is unique. Fix permanently

```
g_(a_j-a_i) = mean(a_1,...,a_(j-1)) - a_i,  i<j.
v_j = sum_(d in G_j) g_d^2,
S_n = sum_(j=2..n) v_j,
f_n = 1_(P_n) * (g 1_(F_n)),
E_n = ||f_n||_2^2.
```

Thus `S_n` and `E_n` are raw quantities, before division by `H_n^2`.
Every class and prefix sums to zero, and

```
sum_(d in F_n) d g_d = S_n,
v_n <= (n-1) H_n^2,    S_n <= q_n H_n^2.          (1)
```

For an unordered pair of distinct source labels `{d,e}`, write

```
b(d,e) = max(tau(d),tau(e)),
r(d,e) = tau(|d-e|),
```

where `r=infinity` if the output is absent from the specified terminal
history. A mixed-born pair has different source births and `r<=b`.
A retirement has `b<r<=N`. These are properties of the literal integer
labels and their unique endpoints. Source birth and output retirement
are never assigned independently. Same-birth pairs always have `r<b`;
their contribution in a centered class is `-v_b/2`.

At step `n`, put

```
h_n = delta_(a_n) * (g 1_(F_(n-1))),
k_n = 1_(P_n) * (g 1_(G_n)),
x_n = <f_(n-1)+h_n, k_n>,
rho_n = <f_(n-1), h_n>,
D_n = S_(n-1) + (n-1)v_n.
```

Use `f_1=0` and `S_1=0`. Difference uniqueness and class centering give

```
||h_n||^2 = S_(n-1),
||k_n||^2 = (n-1)v_n,
E_n-E_(n-1) = D_n + 2 x_n + 2 rho_n.              (2)
```

For the second norm, the coincident position `a_n` has coefficient
`sum_(G_n) g=0`. Every other position is `a_n+a_k-a_i`, with `i<n`,
`k<=n`, and `k!=i`; nonzero signed differences have unique ordered
endpoints, and each input coefficient occurs `n-1` times.

Each mixed pair has a unique overlap position whenever its output
belongs to `F_n`. Hence `x_n` is exactly the sum of `g_d g_e` on
mixed-born pairs with `b=n`; there is no factor two. Likewise `rho_n`
is the sum on retiring pairs with `r=n`. In particular

```
X_N := sum_(n=2..N) x_n,
R_N := sum_(n=2..N) rho_n,
E_N = (N-1)S_N + 2X_N + 2R_N.                    (3)
```

## 2. Exact Abel identity and a finite diagonal charge

For any nonincreasing nonnegative sequence `w_2,...,w_N`, define

```
B_N(w) = sum_(n=2..N) w_n x_n,
R_N(w) = sum_(n=2..N) w_n rho_n,
D_N(w) = sum_(n=2..N) w_n D_n,
A_N(w) = w_N E_N + sum_(n=2..N-1) (w_n-w_(n+1)) E_n.
```

Summation by parts in (2) proves the exact identity

```
                 2 B_N(w) + 2 R_N(w) + D_N(w) = A_N(w).     (4)
```

Every term defining `A_N(w)` is nonnegative. Its pair clocks are
explicitly

```
B_N(w) = sum_(mixed-born, b<=N) w_b g_d g_e,
R_N(w) = sum_(retired, r<=N)    w_r g_d g_e.        (5)
```

In particular the retirement uses `w_r`, not the earlier `w_b`.

Now choose, without tuning to signs,

```
w_n = 1/(q_n^2 H_n^2).                            (6)
```

This decreases strictly. From (1),

```
w_n D_n
 <= [q_(n-1)+(n-1)^2]/q_n^2
 = 2(3n-4)/(n^2(n-1))
 = 8/n^2 - 2/[n(n-1)].                            (7)
```

Consequently, uniformly over every terminal rank and every history,

```
0 <= D_N(w) <= 8 zeta(2)-10 < 3.16.               (8)
```

Here the numerical inequality is merely the familiar value
`zeta(2)=pi^2/6`; the exact bound preceding it is sufficient. This
finite charge includes both old-label replication and the new-class
diagonal. It is stronger than a dyadic-only summability statement.

Young's inequality for convolution gives `E_N<=N^2 S_N`, so

```
0 <= w_N E_N <= N^2/q_N = 2N/(N-1) <= 4.          (9)
```

Thus the endpoint in (4) is bounded and the entire diagonal charge is
finite. Any unbounded contribution to `A_N(w)` is in its nonnegative
Abel interior. Equation (4) still does not assign that contribution
to `B_N(w)` instead of `R_N(w)`.

## 3. The full cap forces the Abel interior to diverge

Assume one infinite actual Sidon history and one fixed onset and
constant `C>0` satisfy

```
H_n <= C n^2 log(2n)
```

at every rank beyond that onset. Suppose a dyadic old rank `N`
satisfies the already proved good-epoch conclusions

```
S_N >= eta q_N H_N^2,       H_(2N) <= K H_N,       (10)
```

where `eta>0` and `K>=1` are fixed. The application from
`coherent_birth_linear_envelope.md` has `K=32`, `eta=2^-17`, and
an infinite collection of disjoint intervals `[N,2N)` for which
`sum 1/log(2N)` diverges. This is where the single fixed-onset cap,
and not a sequence of unrelated terminal caps, enters.

For every `N<=n<=2N`, the raw first-moment argument gives

```
E_n >= (3/2) n^2 S_n^2/H_n^3
    >= (3 eta^2/(2K^3)) N^2 q_N^2 H_N.            (11)
```

For completeness, `sum f_n=0` and `sum_x x f_n(x)=n S_n`.
The support consists of at most the `2H_n` consecutive integer
positions `a_1+1,...,a_1+2H_n`. Their centered square sum is
`H_n(4H_n^2-1)/6`; Cauchy proves the first inequality in (11).
The second uses `S_n>=S_N` and `H_n<=K H_N`. It makes no claim
that `E_n` itself is monotone.

Since `q_(2N)>4q_N` and `H_(2N)>=H_N`,

```
w_(2N) <= w_N/16.
```

Multiplying the minimum in (11) by the telescoping weight loss gives

```
sum_(n=N..2N-1) (w_n-w_(n+1)) E_n
 >= (45 eta^2/(32K^3)) N^2/H_N
 >= 45 eta^2/[32K^3 C log(2N)].                   (12)
```

The selected dyadic intervals are disjoint, so the existing
reciprocal-log divergence and (12) prove

```
A_T(w) -> infinity                              (13)
```

as terminal ranks `T` increase. More precisely its nonnegative
interior has an increasing divergent lower bound. The bounded endpoint
is not being reused. Equations (4), (8), and (13) yield the genuine
conclusion `B_T(w)+R_T(w)->infinity`. They do not yield divergence
or positivity of either summand separately.

## 4. The source/retirement commutator, with its age diagonal

Let `Z_N` be the PSD matrix on the final label bank with entries

```
(Z_N)_(d,e) = w_(max(tau(d),tau(e))) g_d g_e.       (14)
```

Its exact nested decomposition is

```
Z_N = w_N g_(F_N) g_(F_N)^T
    + sum_(j=2..N-1) (w_j-w_(j+1)) g_(F_j) g_(F_j)^T.
```

Write `T_N(w)` for its actual convolution energy under all smoothing
points `P_N`; explicitly replace each outer product in this display by
the squared norm after convolution by `1_(P_N)`. Thus `T_N(w)>=0`.
Let

```
t_N = tr Z_N = sum_(j=2..N) w_j v_j,
C_N^lag = sum_(retired, r<=N) (w_b-w_r) g_d g_e,
J_N^age = sum_(2<=j<n<=N) (w_j-w_n) v_j >= 0.
```

Then the new exact two-clock comparison is

```
T_N(w) - A_N(w) = J_N^age + 2 C_N^lag.            (15)
```

To verify it, expand the final convolution using literal pair
differences. Its mixed-born weights are `w_b`, retired weights are
also `w_b`, and centered same-birth pairs contribute `-t_N/2`.
Therefore

```
T_N(w) = (N-1)t_N + 2B_N(w)
                       + 2 sum_(retired, r<=N) w_b g_d g_e.
```

Subtract (4). The diagonal difference is exactly

```
(N-1)t_N-D_N(w)
 = sum_j [(N-j)w_j-sum_(n=j+1..N) w_n] v_j
 = J_N^age.
```

Equivalently, the left side of (15) is

```
sum_(j=2..N-1) (w_j-w_(j+1))
  [ ||1_(P_N)*g_(F_j)||^2 - ||1_(P_j)*g_(F_j)||^2 ].        (16)
```

These formulas retain every source birth, actual output retirement,
and replication age. Positivity of each separate convolution energy
does not give a sign to their difference in (16). In particular,
replacing `w_r` by `w_b` in (5) costs exactly `C_N^lag`; a positive
coefficient `w_b-w_r` does not make its signed products positive.

## 5. One literal physical source realizes B_N(w)

There is an exact source construction for the direct weights (6).
Put `alpha_n=q_n^-2`, choose one fixed `0<lambda<=1`, and define the fixed matrices
on the terminal bank by

```
(V_N)_(d,e) = alpha_b,
(W_N)_(d,e) = alpha_b + lambda w_b g_d g_e,
b = max(tau(d),tau(e)).                           (17)
```

Both summands are PSD by the decreasing-tail decomposition used in
(14), with `1_(F_j)` replacing `g_(F_j)` for `V_N`. Also

```
(1-lambda) alpha_b <= (W_N)_(d,e) <= (1+lambda) alpha_b,
```

because both raw coefficients have magnitude at most `H_b`.
Thus the full matrices have nonnegative physical kernels. Their
entries on existing labels remain fixed under extension.

Every full birth class sums to zero, so the residual in (17) has zero
row sums on every complete prefix. Its exact mass is zero. Here matrix
mass means `M(X)=1^T X 1`. In terms
of harmonic sums `h_N^(s)=sum_(n=1..N) n^-s`, the full masses are

```
M(V_N)=M(W_N)
 = sum_(n=2..N) (q_n^2-q_(n-1)^2)/q_n^2
 = 4(h_N^(1)-h_N^(2)) = 4 log N + O(1).           (18)
```

The diagonal traces obey

```
tr V_N = sum_(n=2..N) 4/[n^2(n-1)] <= 4(2-zeta(2)),
tr Z_N <= 4(2-zeta(2)),
tr W_N <= (1+lambda)4(2-zeta(2)).                 (19)
```

These are exact history-independent mass and trace statements, rather
than a counterexample family. The cap does not change the growing mass.
They do not establish that the *masked* capacity grows at that rate.

Let `C_hist` denote the single fixed-matrix historical physical
envelope of `weighted_birth_envelope.md`, with all actual prefix
states and no extra future-span mask. Its linearity on nonnegative
matrices and the pair classification give

```
C_hist(V_N) - C_hist(W_N) = lambda B_N(w).         (20)
```

Indeed, the total off-diagonal residual is `-t_N/2`, while its born
sum is `B_N(w)-t_N/2`. Their difference is `-B_N(w)`.
This is a single physical matrix and one envelope; it does not sum
independent source budgets. The signs in (20) do not require the
residual itself to be nonnegative.

The construction still does not make a free bounded margin. Its
baseline mass is (18), and the corresponding future demands have to
be proved for this matrix itself. For example, use its entire old
prefix against an actual future block of `m=N` points. For the usual
hole-corrected support denominator `D=L+H_N-N`, one has `D>=H_N>=q_N`
because `L>=N`. Its mass-only raw demand is
`delta_0=(N^2 M(V_N)/D-N tr V_N)/2`, with no second squaring of matrix
mass. Since `tr V_N>=1`, it satisfies

```
delta_0 <= [4 M(V_N)-N]/2 < 0
```

for all sufficiently large `N`. Thus the entire-prefix mass-only
demand of (17) cannot simply replace the positive normalized
current-row demands in the existing good-epoch argument. An additional
moment or separately justified allocation would require its own proof.

## 6. Direct causal weights and sums of terminal rows differ

The quantity in (20) is `sum_n w_n x_n`. An individual normalized
terminal row involves `w_N X_N`, where `X_N=sum_(n<=N)x_n`.
For any nonnegative finite selection `beta_k` at old ranks `N_k`,

```
sum_k beta_k w_(N_k) X_(N_k)
 = sum_n theta_n x_n,
theta_n = sum_(k:N_k>=n) beta_k w_(N_k).           (21)
```

Applying (4) to `theta` gives exactly

```
2 sum_n theta_n x_n + 2 sum_n theta_n rho_n
       + sum_n theta_n D_n
 = sum_k beta_k w_(N_k) E_(N_k).                  (22)
```

Thus the tail of the terminal coefficients, not those coefficients
themselves, belongs on the causal increments and retirements. Neither
the signs of `x_n,rho_n` nor an equality `theta_n=w_n` is available.
The direct-weight divergence proved in §3 cannot be silently
substituted into a selected current-row maximum. That maximum still
has the overlap and span terms in `coherent_birth_linear_envelope.md`.

## 7. A precise sufficient closing inequality, still unproved

For the single physical source (17), suppose `D_0,D_W` are any
separately justified total nonnegative demands for compatible actual
blocks, paid by its respective historical envelopes. All the blocks
must come from this same history and have disjoint physical difference
sets. Put

```
M_0 = C_hist(V_N)-D_0 >= 0,
M_W = C_hist(W_N)-D_W >= 0,
Delta_D = D_W-D_0.
```

Then (20), with no demand approximation, gives

```
M_0-M_W = lambda B_N(w)+Delta_D.
```

Combine this with (4) and `M_W>=0`:

```
A_N(w)/2 <= D_N(w)/2 + R_N(w)
                         + (M_0-Delta_D)/lambda.             (23)
```

Since (8) is uniformly bounded and (13) diverges under the stated
full-history hypotheses, an actual sufficient new estimate would be

```
R_N(w) + (M_0-Delta_D)/lambda
 <= (1/2-epsilon) A_N(w) + O(1)                  (24)
```

for one fixed `epsilon>0`, along unbounded terminal horizons. It
would contradict (23). The constants and demand construction in
(24) would have to apply to the one capped history beyond one fixed
onset. No such estimate is proved here.

A retirement-only estimate
`R_N(w)<=(1/2-epsilon)A_N(w)+O(1)` would prove that the causal
source improvement diverges. It would still leave the actual
physical margin `(M_0-Delta_D)/lambda` to pay for it; divergence
of two different capacities' difference is not itself a contradiction.
Conversely, a trace bound cannot replace that margin, by (18) and
the demand calculation after (20).

The accomplished reduction is therefore specific: the normalization
(6) yields a finite total diagonal charge, a bounded endpoint, a
divergent nonnegative Abel interior, the exact source/retirement lag
identity (15), and one physical realization (20). Retirement and the
remaining shared margin have not been bounded at the required scale.
These supporting statements do not constitute original Q1.

Subsequent supporting reduction: `late_retirement_tail.md`, independently
checked in `late_retirement_tail_review.md`, proves for every fixed
`alpha>1/4` that the part of `R_N(w)` with actual retirement
`r>=b(log b)^alpha` is uniformly absolutely summable. Thus (23)–(24)
may replace `R_N(w)` by its remaining near-birth part at a bounded
error. The result prices pairs at `w_r`; it does not control the
source-time commutator (15), the near-birth sum, or the physical margin.

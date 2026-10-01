# Exact allocation dual for simultaneous future-moment improvements

2026-09-05. Author: `/root`, GPT-6 Astra Ultra.

Status: a finite exact optimization identity for the existing single
physical envelope, with a constructive actual-history dual witness. It
does not prove the required asymptotic cost bound or original Q1. No
numerical optimization or Lean execution is claimed here.

## 1. Keep the literal masks and all competing rows

Take a finite family of actual old prefixes and actual disjoint future
point blocks, as in `coherent_birth_linear_envelope.md`, sections 2--4.
Use the same literal old-label exclusion and actual future-span mask.
Write `a_k(t)` for the normalized unit row after both masks and put

```
r_k(t) = sigma_k(t) 1[t notin F_(N_k)] / q_k^2
           * sum_(d,d+t in F_(N_k)) z_d z_(d+t).
```

Unlike the earlier note's r, this r has no factor 1/8. Thus
`|r_k(t)|<=a_k(t)`. Let T be a finite set containing every row's
support. Let `delta_k^0` be its normalized raw mass-only demand and

```
d_k = (LB_k-m_k S_k)/(2q_k^2),
ell = 1/8,
W_k(lambda_k) = J + lambda_k z_k z_k^T,
0<=lambda_k<=ell.
```

The proved actual moment demand is exactly
`delta_k(lambda_k)=delta_k^0+lambda_k d_k`. Each full matrix is
PSD with nonnegative entries, including its diagonal. No hypothesis
that d_k is positive is needed for the identities below. At the
previous extended good epochs, all the raw demands on this parameter
box are positive beyond one fixed onset; elsewhere they remain valid
raw lower bounds without applying a positive part.

The one-copy physical margin is

```
C(lambda)=sum_(t in T) max(0, max_k[a_k(t)+lambda_k r_k(t)]),
D0=sum_k delta_k^0,
M(lambda)=C(lambda)-D0-sum_k lambda_k d_k >= 0.          (1)
```

The inequality follows from actual disjointness of all Delta B_k and
the same local demand inequalities. Parameters are chosen for a
finite deterministic instance; no random future, filtration, or
nonanticipating selection theorem is invoked. A uniform theorem
asserting useful choices for all capped histories is still required.

## 2. An exact finite dual with one allocation per physical label

Let A be the compact polytope of nonnegative arrays alpha_(k,t) with

```
sum_k alpha_(k,t)<=1       for every t in T.
```

The unused part is the allocation to the zero row. Define

```
rho_k(alpha)=sum_t alpha_(k,t) r_k(t),
C0=C(0),
L(alpha)=C0-sum_(k,t)alpha_(k,t)a_k(t) >= 0.
```

The smallest margin obtainable on the entire box and its largest
improvement from the unit baseline satisfy

```
M_min = max_(alpha in A)
          [sum_(k,t)alpha_(k,t)a_k(t)-D0
                     -ell sum_k (d_k-rho_k(alpha))_+],   (2)

I_max := M(0)-M_min
       = min_(alpha in A)
          [L(alpha)+ell sum_k(d_k-rho_k(alpha))_+].       (3)
```

Here `(x)_+=max(x,0)`. Both extrema are attained.

For completeness, these are standard finite linear-program duality,
with the primal written without any hidden physical copies:

```
min sum_t mu_t-D0-sum_k lambda_k d_k,
mu_t>=0,
mu_t>=a_k(t)+lambda_k r_k(t)       for every k,t,
0<=lambda_k<=ell.
```

Multipliers alpha for the second inequalities must satisfy the column
simplex condition when mu is minimized. Minimizing the remaining
term `lambda_k(rho_k-d_k)` on `[0,ell]` gives
`-ell(d_k-rho_k)_+`, proving its dual objective. The primal is feasible
and has a finite attained optimum: lambda lies in a compact box and
mu can be chosen to be the displayed finite maxima. The dual is
feasible (alpha=0) and compact. Finite LP strong duality applies and
gives (2); subtracting from C0-D0 gives (3). This use of LP strong
duality is mathematical, not a claim that it has been formalized in
the current Lean project.

Weak duality can also be checked directly without an optimizer:
for every alpha and lambda,

```
M(lambda) >= sum alpha a-D0
                    +sum_k lambda_k(rho_k-d_k)
          >= sum alpha a-D0-ell sum_k(d_k-rho_k)_+.
```

Thus (3) prices both reassignment away from the baseline-maximal rows
and any remaining per-row moment-demand deficit. Its first term is
an actual allocation loss; it is not an independently reusable old
capacity or a new envelope for each row.

## 3. Exactly when every such moment perturbation fails to improve

Because every summand on the right of (3) is nonnegative and A is
compact, the following are equivalent:

```
I_max=0;
there exists alpha in A with L(alpha)=0 and rho_k(alpha)>=d_k for all k.
                                                               (4)
```

The condition L=0 means that at each t with positive baseline
maximum all its mass is allocated among rows attaining that maximum.
At a zero maximum every a and r is zero, so its allocation is
irrelevant. Thus ties are retained as a simplex of possible
allocations. Replacing a tie by an arbitrary chosen row would change
the condition and need not preserve (4).

Equivalently, failure of that finite feasibility system guarantees a
strictly positive improvement for some lambda in the box. It does
not give a uniform size. An arbitrarily small minimum in (3) is
consistent with failure of the zero-improvement system. Nor does a
strict improvement imply a negative final physical margin.

This criterion concerns simultaneous fixed moment directions. It
does not assert optimization over all scalar carriers, Fourier
features, physical masks, or possible future block partitions.

## 4. An actual-history allocation exposes the retained local slack

There is a particularly important explicit allocation. If
`t in Delta B_k`, set alpha_(k,t)=1, and otherwise set every entry
at t to zero. Actual Sidonness makes these Delta B_k disjoint. It
is therefore a feasible single-copy allocation, denoted alpha^B.
Put

```
e_k = sum_(t in Delta B_k) a_k(t)-delta_k^0 >= 0,
rho_k^B = sum_(t in Delta B_k) r_k(t).
```

The exact endpoint demands at lambda_k=ell also give

```
e_k+ell(rho_k^B-d_k)>=0,
ell(d_k-rho_k^B)_+ <= e_k.                              (5)
```

Consequently the value of the dual objective (2) at this explicit
allocation is

```
sum_k [e_k-ell(d_k-rho_k^B)_+] >= 0.                    (6)
```

This is a constructive dual witness consistent with M_min>=0 for
every actual history. Its entries use the actual future blocks;
they are a proof of the finite dual inequality, not a purported
causal predictor. It also proves directly from (3) that

```
I_max <= L(alpha^B)+sum_k e_k = M(0).                   (7)
```

All baseline margin not allocated to the chosen future differences,
including unused labels, other endpoint pairs, and maximum slack,
is retained in L(alpha^B). All local convolution slack is retained
in the e_k. No sign of a centered residual has been discarded.

## 5. The remaining asymptotic theorem, in allocation form

On a hypothetically fixed-cap infinite Sidon history, the saved
extended good epochs supply divergent positive demand increments.
That does not show that (3) exceeds the existing margin M(0).
The demand must be compared with rho for every single-copy
allocation, while retaining the allocation loss L.

An endgame through this family would require a uniform finite-horizon
statement forcing

```
inf_(alpha in A)[L(alpha)+ell sum_k(d_k-rho_k(alpha))_+] > M(0)
```

at some horizon of every capped history. Equations (5)--(7) show
exactly which actual-history witness such a cap-sensitive theorem
would have to rule out. Merely computing a positive direction, or
showing that no baseline-active allocation meets all d_k, is weaker.

This note supplies the exact shared-budget optimization and its
explicit feasible witness. It does not supply the cap-sensitive
exclusion of that witness, a proof or counterexample to Q1, or a
new Lean-verified declaration.

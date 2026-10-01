# Endpoint batches exclude the independent early-label model

2026-09-05. Author: `/root`, GPT-6 Astra Ultra. Status: an exact probabilistic
obstruction to a relaxed bank model, not a theorem excluding actual capped
Sidon histories and not a Q1 resolution. No Lean verification is claimed.

## 1. A finite bound that retains endpoint incidence

Let `F` be a random subset of `[1,D]`. Assume its membership events are
independent and every marginal is at most a fixed `b<1`, with `b>0`.
Write `lambda=log(1/b)>0`. For any integer `2<=k<=D`,

```
Pr(exists integer Sidon G subset [1,D], |G|=k, Delta G subset F)
  <= binom(D,k) b^(k(k-1)/2)
  <= exp(k log D - lambda k(k-1)/2).                         (1)
```

For a fixed Sidon `G`, its `binom(k,2)` positive differences are distinct
physical labels in `[1,D]`. Independence makes the probability that they
all belong to `F` at most `b^binom(k,2)`. Sum over possible `G`; bounding
their number by all `k`-subsets proves (1). If `k>D`, the event is empty.
No randomness of an actual Sidon sequence is assumed.

For `D>=2` put `k_D=ceil(4 log D/lambda)+2`. Whenever `k_D<=D`, (1) gives

```
Pr(exists such G of size at least k_D)
   <= exp(-4(log D)^2/lambda).                             (2)
```

A larger witness contains a `k_D`-point witness. Also
`lambda(k_D-1)/2 >= 2 log D + lambda/2`, so the exponent in (1) is at
most `-k_D log D`, proving the displayed bound. These probabilities
are summable over integer `D`: eventually the bound is at most `D^-2`.
The first Borel--Cantelli lemma therefore shows that, for one coupled
random bank with the specified independent marginals at each width,
almost surely every sufficiently large width has no such Sidon clique
larger than `O_b(log D)`. Independence between different widths is not
needed for this conclusion.

## 2. Application to actual birth batches

For an actual increasing integer Sidon sequence, fix one physical width
`D` and set

```
F_n(D)=Delta P_n intersect [1,D],
G_n(D)={a_n-a_i : i<n and a_n-a_i<=D}.
```

The batches are disjoint, and `F_p(D)` is their union for `n<=p`.
Every `G_n(D)` is itself Sidon, since it is the reflection of a subset
of the actual sequence. Moreover

```
Delta G_n(D) subset F_(n-1)(D).                            (3)
```

Both statements concern literal endpoints, not independently assigned
label births. If all the old banks lie in a bank `F` with no Sidon
clique of size `k_D`, then (3) forces

```
|F_p(D)| = sum_(n<=p) |G_n(D)| < p k_D.                   (4)
```

The fixed-onset cap already proved in `fixed_width_bank_density.md`
implies, for any fixed `theta` strictly between `1/2` and `1`,
`|F_floor(D^theta)(D)|>=cD` for all sufficiently large `D`, with fixed
`c>0`. But `D^theta k_D=o(D)`. Thus this cap consequence is incompatible
with (4) at all sufficiently large widths.

## 3. What this proves for the saved coherent birth field

The particular model in `coherent_birth_field.md` independently assigns
each label `d>=2` a finite exponent with probability `1/10`, and exponent
infinity otherwise; label `1` is deterministically never born. Its
eventual born-label set `F_infinity` therefore has independent membership
with every marginal at most `1/10`. Every one of its earlier banks is a
subset of that same set.

Apply (2)--(4) with `b=1/10`. Almost surely this model cannot be the
actual short-difference birth history of any Sidon sequence satisfying
one fixed-onset critical cap. This is an additional endpoint-incidence
obstruction, even without using the model's previously established
failure of the exact total count `|Delta P_n|=binom(n,2)`.

The quantifiers are uniform over potential actual endpoint realizations:
the probability bound first excludes every large Sidon clique, then (4)
applies to every sequence whose labels lie in the bank. It is not merely
a statement about one sequence selected before the random bank.

## 4. Information retained, and the unresolved transfer

At a single terminal height `H`, the same elementary bound gives

```
Pr(exists n-point Sidon P subset [1,H], Delta P subset F)
 <= exp(n log H - lambda n(n-1)/2).                       (5)
```

In particular, when `H<=C n^2 log(2n)`, this probability is at most
`exp(-lambda n^2/4)` for all sufficiently large `n` (depending on `C,b`).
Indeed `log H=o(n)` and the linear `lambda n/2` term is lower order.
The exact correlations among the differences of actual finite rulers
are therefore essential; an independent label approximation discards
constraints of quadratic order. Low probability under this artificial
measure does not imply nonexistence of deterministic rulers.

For comparison, the primary paper by Kohayakawa, Lee, Rodl, and Samotij,
[The number of Sidon sets and the maximum size of Sidon sets contained
in a sparse random set of integers](https://www.math.tau.ac.il/~samotij/papers/Sidon.pdf),
was retrieved from the author's site. Its Theorem 2.1 and Lemma 3.2 count
finite Sidon sets and extensions using a locally dense graph of forbidden
differences. Those bounds count possible finite extensions; they do not
assert that every fixed-onset infinite branch becomes empty. Equations
(1)--(5) above use only a direct union bound and do not invoke the paper
as a proof of the missing infinite-history statement.

Primary PDF SHA256:
`6e7737eeb998dcbe2b49a499d15cfefc81075a522a4529237f24b9ef2d630bce`.
Saved PDF and extracted text are in `research/evidence/` under
`kohayakawa_lee_rodl_samotij_sidon`.

The remaining task is a deterministic, cap-sensitive estimate for the
correlated actual banks. No such transfer theorem is supplied here.
In particular this note neither assumes that real difference labels
are independent nor turns a probability-zero relaxed model into a
proof of Q1. It rules out reusing that model as an endpoint realization.

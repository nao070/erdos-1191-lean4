# Absolute deletion whenever two of the three birth clocks are close

2026-09-05. Author: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

**Status.** A uniform all-history absolute summability theorem at the actual Born/retirement price is proved below. It removes every used mixed record with an ultra-close pair of distinct birth ranks, all repeated birth ranks, and the repeated-numeric-label case. This strengthens the clock separation in `clock_core_localization.md`. It gives no sign or required-scale estimate for the remaining core, and no physical-margin bound or proof of Q1. No computation or Lean execution is used.

## 1. One actual price and one numeric Schur triple per record

Keep the actual integer Sidon history and the causal note's notation:

```
F_n=Delta P_n,    G_n=F_n\F_(n-1),    |G_n|=n-1,
q_n=binom(n,2),   H_n=a_n-a_1,
g_(a_j-a_i)=mean(P_(j-1))-a_i,
w_n=1/(q_n^2 H_n^2).
```

A used mixed record is an unordered pair of distinct source labels `{d,e}` of different source birth ranks, with used positive output `t=|d-e|`. Write

```
b=max(tau(d),tau(e)),   r=tau(t),
m=max(tau(d),tau(e),tau(t))=max(b,r).
```

For a Born record `r<=b`, its actual price is `w_b=w_m`. For a retired record `r>b`, its actual price is `w_r=w_m`. Thus both types have **exactly the common latest-birth price**, including cases of equal clocks. This is an equality of the existing prices, not a replacement of retirement weights by source-time weights.

Since every source coefficient in this record is bounded by `H_m`,

```
w_m*|g_d*g_e| <= 1/q_m^2.                              (1)
```

Orient the sources numerically as `d<e`, and set `x=d`, `y=e-d`, `z=e`. Then `x+y=z`. The unordered Schur triple, allowing `x=y`, is uniquely determined by the record. Conversely a Schur triple with `x<y` has at most the two used source pairs

```
{x,z}, with output y;       {y,z}, with output x.        (2)
```

Only pairs with different source birth ranks enter B or R. If `x=y`, the two displayed pairs coincide, leaving just one candidate. The source pair `{x,y}` has output `|x-y|`, and is not another record of this Schur triple.

Given two distinct positive numeric labels `u,v` in a Schur triple, the third label must be one of

```
u+v,    |u-v|.                                          (3)
```

Each numeric label has at most one actual birth in the history. Thus fixing the two labels leaves at most two realized Schur triples, each with at most two record contributions. There is no further count over possible birth ranks of the third label, even if its actual birth is arbitrarily late.

## 2. Any ultra-close pair of distinct clock values is summable

Fix one `gamma>1`. For a rank `n>=3` let

```
P_gamma(n)={p: 2<=p<n, n-p<=n/(log n)^gamma}.
```

Consider every used mixed record having any two of its label birth ranks `p<n` with `p in P_gamma(n)`. Choosing one such pair of actual labels gives at most

```
|G_n|*sum_(p in P_gamma(n))|G_p|
 <= (n-1)^2*floor[n/(log n)^gamma]                       (4)
```

candidate label pairs at the larger chosen rank `n`. Each such pair yields at most four record contributions by (2)–(3). Their latest clock satisfies `m>=n`, so each contribution costs at most `1/q_n^2` by (1). Therefore

```
sum_(used mixed records with some ultra-close p<n)
                         w_m*|g_d*g_e|
 <= 4*sum_(n>=3) [(n-1)^2/q_n^2]
                              *floor[n/(log n)^gamma]
 <= 16*sum_(n>=3) 1/[n*(log n)^gamma]
 =: C_close(gamma) < infinity.                          (5)
```

The last convergence uses `gamma>1`. The estimate applies in particular when all three clock values are distinct, and also remains an upper bound if another equality is present. The chosen close pair need not include the latest clock `m` or both original sources. This is the extra symmetry over a restriction involving only `|r-b|`.

A record with several close pairs can occur several times on the right. This only enlarges a nonnegative upper bound; the deletion on the left counts the actual record once. Alternatively one can choose its first close pair in a fixed ordering. No factor for possible third-label realization times or a separate capacity per clock has been introduced.

## 3. Distinct numeric labels with equal birth ranks

For two distinct labels in `G_n`, their positive difference is the difference of their two old lower endpoints. Hence

```
Delta G_n subset F_(n-1).                               (6)
```

In particular a Schur triple cannot have all three labels in `G_n`: if `x+y=z`, then `z-x=y` would belong both to the old bank and the new class. This also rules out `x,2x in G_n`.

Now count records whose Schur triple contains two **distinct numeric labels** with the same birth `n`. There are `binom(n-1,2)` choices for that equal-birth label pair. Equations (2)–(3) again give at most four record contributions per pair. With `m>=n`,

```
sum_(these records) w_m*|g_d*g_e|
 <= 4*sum_(n>=3) binom(n-1,2)/q_n^2
 <= 8*sum_(n>=3) 1/n^2
 =: C_equal < infinity.                                 (7)
```

This bound deliberately allows overcounting. More explicitly, if the equal-birth labels are a summand and the largest label, their difference is old by (6); the pair consisting of these two new labels is a same-birth source pair and is excluded from B and R. The other pair in (2) is an actual mixed-born record with output born at the same time as its later source. These include the automatic endpoint-triangle records counted by `<h_n,k_n>` in the causal notes. If the equal-birth labels are the two summands, the sum completion may produce two mixed records, and (7) bounds both without a sign assumption.

Thus automatic mixed contributions are included in the absolute deletion. Genuine same-birth source pairs are still excluded from B and R throughout; their centered contribution belongs to the separate diagonal accounting. No change to `D_T` is made here.

A retired mixed record already has three distinct birth ranks: its two source ranks differ and its output rank is strictly larger than both. Thus the repeated-clock records counted here are Born records; the joint B/R bound remains valid without assigning any of them to R.

## 4. Repeated numeric label: x+x=2x

The preceding equal-birth count requires two distinct labels. It therefore does not cover the case `x=y`: the clock `tau(x)` is repeated because the same physical label appears twice.

For each actual label `x`, there is at most one candidate record `{x,2x}`. If `2x` is absent there is none. If it is present, (6) implies `tau(2x)!=tau(x)`, so its sources have different births. Its output is `x`, and its output birth cannot exceed its later source birth. The record is Born, never retired, and its price is again `w_m`.

Count by `p=tau(x)`. There are `p-1` choices for `x`, and `m>=p`; hence

```
sum_(records {x,2x}) w_m*|g_x*g_(2x)|
 <= sum_(p>=2) (p-1)/q_p^2
 = 4*sum_(p>=2) 1/[p^2*(p-1)]
 = 4*(2-zeta(2))
 =: C_repeat < infinity.                                (8)
```

For the last equality use `1/[p^2*(p-1)]=1/(p-1)-1/p-1/p^2`. Each record has a unique smaller numeric label `x`, so no duplicated source pair occurs in this sum. This is a repeated physical-label case, not a diagonal source pair `{d,d}`.

Equations (7)–(8) exhaust repeated-clock cases. All three clock values equal are impossible by (6), whether or not a numeric label repeats.

## 5. A core with all three clocks separated

For a finite horizon T retain in `B_T^sep` and `R_T^sep` only their existing records for which the three numeric labels are distinct, their three birth ranks are distinct, and every pair `p<n` of those ranks satisfies

```
n-p > n/(log n)^gamma.                                  (9)
```

Keep each record's original Born or retirement weight. The preceding bounds prove uniformly over every actual history and every T that

```
|B_T-B_T^sep|+|R_T-R_T^sep|
 <= C_close(gamma)+C_equal+C_repeat
 =: C_gamma < infinity.                                (10)
```

The omitted sets may overlap; adding their absolute bounds is legitimate. The B and R records themselves are disjoint, so (10) gives one combined deletion bound. No cap, independent-label model, cancellation hypothesis, or density theorem was used. Only literal star cardinalities, numeric Schur completions, coefficient size, and the actual latest-clock price enter the proof.

In sorted clock order `n_1<n_2<n_3`, it suffices to impose (9) for the two adjacent pairs: the separation of `n_3` from `n_2` also separates it from `n_1`. The new condition therefore deletes closeness of the two earlier clocks as well as closeness involving the latest one.

The exact causal Abel identity consequently gives

```
2B_T^sep+2R_T^sep+D_T = A_T + E_T^err,
|E_T^err| <= 2C_gamma.                                  (11)
```

This bounded error can be combined with all the independent rank-ratio, physical-output, and repeated-endpoint deletions in `clock_core_localization.md`: intersect its existing cores with (9), and add the finite absolute error constants. The remaining three clocks are then separated pairwise on the additive scale in (9), while retaining the earlier multiplicative and physical restrictions.

The latest-clock price in (1) is the actual B/R price. Equation (5) by itself is not a license to replace a retired record's price by `w_b` when comparing different source-time matrices or lag commutators. Such changes have different coefficients and require their own argument.

The theorem localizes both sides of the Abel identity; it does not prove a sign for either separated core, that the Born core alone diverges, or that any improvement pays the shared physical margin. Original Q1 remains unresolved.

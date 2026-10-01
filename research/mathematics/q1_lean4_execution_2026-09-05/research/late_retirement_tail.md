# An absolutely summable tail for retirement-clock weights

2026-09-05. `/root`, GPT-6 Astra Ultra. This is an all-history tail
estimate for the actual retirement term in `causal_birth_energy_telescoping.md`.
The remaining near-birth retirement sum is not bounded here; Q1 is unresolved.
No Lean or finite computation is used.

Let an increasing infinite integer Sidon sequence have prefix diameters
`H_n=a_n-a_1`, label birth `tau`, and `q_n=binom(n,2)`. Keep the permanent
raw birth-linear coefficients `g_(a_j-a_i)=m_j-a_i` and

```
w_n = 1/(q_n^2 H_n^2).
```

For a retired unordered source pair `{d,e}`, set
`b=max(tau(d),tau(e))` and `r=tau(|d-e|)>b`. Fix a real `alpha>1/4`.
Then

```
sum_(retired pairs with r >= b(log b)^alpha) w_r |g_d g_e|
 <= 8 sum_(b=3..infinity) 1/[b(log b)^(4alpha)] < infinity.    (1)
```

This bound is independent of the sequence, the cap constant, onset,
and terminal horizon. In particular no global density hypothesis is
needed for this part of the weighted transport.

Proof: two labels born in the same class cannot retire against one
another, because their difference belongs to the strictly earlier bank.
Therefore every retired pair with source birth `b` has one label in
`G_b` and one in `F_(b-1)`. There are at most

```
|G_b| |F_(b-1)| = (b-1)q_(b-1) <= b^3/2                    (2)
```

such pairs. Both raw coefficients have absolute value at most `H_b`.
Since `H_r>=H_b` and `q_r>=r^2/4` for `r>=2`,

```
w_r |g_d g_e| <= 1/q_r^2 <= 16/r^4.
```

For a pair in (1), this is at most
`16/[b^4(log b)^(4alpha)]`. Multiply by (2), then sum over `b`.
Each source pair has at most one actual output birth: there is no
additional sum over possible retirement ranks. Birth `b=2` has no
mixed source pair. This proves (1).

For an explicit upper constant, put `p=4alpha>1`. Decreasing-integral
comparison gives

```
8 sum_(b>=3) 1/[b(log b)^p]
 <= 8/[3(log 3)^p] + 8 (log 3)^(1-p)/(p-1).                 (3)
```

Write `R_T(w)` for the exact signed retirement sum through rank `T`,
as in the causal note. Define `R_T^near` by retaining only pairs with

```
b < r < b(log b)^alpha.
```

Then (1) proves `|R_T(w)-R_T^near|<=C_alpha` for every `T`; indeed the
discarded signed series converges absolutely. The divergent Abel identity
from that note consequently becomes

```
2 B_T(w) + 2 R_T^near + D_T(w) = A_T(w) + O_alpha(1).        (4)
```

Thus any obstruction at the divergent scale must already occur within
this polylogarithmic rank lag. In real base-two logarithmic rank coordinates,
these remaining pairs have a lag less than `alpha log_2(log b)`;
integer dyadic bin indices require adding `1` to this upper bound.
This bound still grows. It is not a bounded-lag result,
and no sign or subcritical bound for `R_T^near` follows from (1).

This controls weights charged at the **output retirement time** `r`.
It does not control the source-time-weighted retirement
`sum w_b g_dg_e`, or the commutator with coefficient `w_b-w_r`.
Those have different prices, and applying (1) to them would be invalid.
The single physical-margin term of the causal note's equation (24)
also remains. Neither cost has been omitted from the Q1 obligation.

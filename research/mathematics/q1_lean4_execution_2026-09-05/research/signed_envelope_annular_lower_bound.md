# An unavoidable annular cost for the unspanned signed envelope

2026-09-05. Author: `/root`, GPT-6 Astra Ultra.

Status: a deterministic lower bound for a specified physical capacity,
not a proof of original Q1. It quantifies an obstruction to bounding
the literal unspanned maximum of the new signed rows. It does not
apply unchanged after actual future-span masks, and does not by itself
bound the capacity-minus-demand margin. No computation or Lean run is
used. The current-unused linear estimate in section 2 was proposed
by `/root/causal_telescoping`; its counting proof is rederived here.

## 1. The signed unit source retains a fixed amount of unused capacity

Let F be any finite set of q positive integers, H=max F, and
Fhat=F union(-F), Q=2q. Neither Sidon endpoint realization nor a
birth order is needed for this section. For t>0 let

```
D(t)=#{d in F:d+t in F},
S(t)=#{x in F:t-x in F},
K_J(t)=2D(t)+S(t).
```

The second count is ordered in x, so an unequal pair contributes
twice and a doubled label once. Define the ordered Schur count

```
A=#{(x,y) in F^2:x+y in F}.
```

Both sum_(t in F)D(t) and sum_(t in F)S(t) equal A, so the
used signed source-pair count is exactly 3A. If z is the kth
smallest member of F, there are at most k-1 choices of x in F
with z-x in F. Consequently A<=q(q-1)/2. There are
binom(Q,2)=2q^2-q signed unordered source pairs in total. Hence

```
sum_(t>0,t notin F)K_J(t)
 =2q^2-q-3A >=(q^2+q)/2,
sum_(t>0,t notin F)K_J(t)/Q^2 >=1/8+1/(4Q).       (1)
```

All counts include the doubled-label case. The elementary example
F={1,...,q} attains the ordered-Schur upper bound; no actual Sidon
realization of that example for arbitrary q is asserted.

If |phi(d)|<=1 and 0<=lambda<=lambda_bar<1, then the full matrix
J+lambda phi phi^T is entrywise at least (1-lambda_bar)J. Thus
(1) gives current unused normalized mass at least
c=(1-lambda_bar)/8. Its pointwise normalized kernel is at most
b/Q, where b=1+lambda_bar: at a fixed positive t there are at
most Q source pairs d,d+t. Oddness and PSD are not needed for
these two entrywise bounds.

## 2. The linear odd feature also has a uniform bound at lambda=1

For phi(d)=d/H, consider W_lambda=J+lambda phi phi^T,
0<=lambda<=1. For q>=2,

```
sum_(t>0,t notin F)K_(W_lambda)(t)/Q^2 >=1/800.    (2)
```

First take lambda=1. Split F into h high labels in (H/2,H]
and l=q-h low labels. Every same-sign source pair has weight
at least one. Every opposite-sign pair except possibly a high/high
pair has weight 1-xy/H^2>=1/2. There are exactly h^2
opposite-sign high/high pairs, including all doubled labels.

If h<=7q/10, at least (q^2+q)/2-h^2 of the unused pairs
from (1) have weight at least 1/2. Their total weight is at least

```
(1/2)[(q^2+q)/2-h^2] >=q^2/200.                  (3)
```

If h>7q/10, the two same-sign high-source groups have h(h-1)
pairs altogether. Each output is strictly less than H/2. At most
l labels at those outputs are used, and each such output has at
most h-1 realizations in each same-sign group. Therefore at least

```
h(h-1)-2l(h-1)=(h-1)(3h-2q)
```

of these pairs are unused. Here q>=2 and h>7q/10 force h>=2,
so h-1>=h/2>7q/20 and 3h-2q>q/10. Their weight is at
least one, giving a total greater than 7q^2/200. This is stronger
than (3). Division by Q^2=4q^2 proves (2) at lambda=1.
The current unused sum is affine in lambda. Equation (1) is
stronger at lambda=0, so convexity proves (2) throughout [0,1].

The q>=2 condition matters: when q=1, lambda=1 kills the sole
pair {-H,H}. For actual Sidon prefixes of rank n>=3, q>=3,
so that exception is absent. At every positive t the normalized
kernel for (2) is at most 2/Q.

## 3. A general annular packing lemma for a single maximum

Suppose rows indexed by a finite set E of dyadic exponents j have
N_j=2^j>=4, Q_j=N_j(N_j-1), and H_j>0. Let k_j(t)>=0
be the current-unused normalized physical kernel, zero on the old
positive difference set. Assume, uniformly in j,

```
sum_(t>0)k_j(t)>=c>0,
k_j(t)<=b/Q_j,
k_j(t)=0 for t>2H_j,
H_j<=C N_j^2 log(2N_j),                          (4)
```

where C>0, b>0 and c>0 are fixed. This is a finite statement;
in an eventual cap application, use only ranks beyond its fixed
onset. Set alpha=c/(2b). Discard the terms t<=alpha Q_j.
There are at most alpha Q_j positive integers in that range,
so its total mass is at most c/2. The remaining row

```
k_j^tail(t)=k_j(t) 1[t>alpha Q_j]
```

has mass at least c/2. Since Q_j>=N_j^2/2, it is supported in

```
I_j=(alpha 4^j/2, 2C 4^j (j+1)log 2].            (5)
```

Take E subset {j_0,...,J}, and define

```
R_J=max(1,4C(J+1)log 2/alpha),
B_J=2+ceil(log(R_J)/log 4).
```

For a fixed t to lie in I_j, j must lie between
log_4(t/[2C(J+1)log 2]) and log_4(2t/alpha).
The length of this interval is at most log_4 R_J, so at most
B_J integer exponents can occur. Therefore, pointwise,

```
sum_(j in E)k_j^tail(t) <= B_J max_(j in E)k_j(t).
```

Summing over the one physical t and retaining the mass of each
tail proves

```
sum_(t>0)max_(j in E)k_j(t) >= c |E|/(2B_J).      (6)
```

This is a lower bound for the literal single maximum. No separate
source budget is allocated to a row. Ties in that maximum do not
affect the inequality. All sums are finite because the row family
and its source supports are finite.

## 4. Consequences for the new signed linear rows

For actual integer Sidon prefixes and

```
k_j(t)=1[t notin F_(N_j)] K_(J+lambda_j dd^T/H_j^2)(t)/Q_j^2,
0<=lambda_j<=1,
```

section 2 gives c=1/800 and b=2. Thus alpha=1/3200 and

```
B_J=2+ceil(log_4(max(1,12800C(J+1)log 2))),
sum_t max_(j in E)k_j(t) >= |E|/(1600B_J).        (7)
```

For all exponents j_0,...,J this is Omega_C(J/log(J+2)).
It holds even when lambda_j is chosen separately for each old
prefix, and includes lambda_j=1. A historical family containing
these current rows has at least the same capacity. Changing the
admissible linear amplitude within this prescribed Q_j^2-normalized
family cannot make its unspanned capacity uniformly bounded. This
does not prohibit rescaling the entire kernel and its demand.

The existing two-lookahead good set has gaps O(log j), proved in
`coherent_birth_linear_envelope.md` section 1. In particular, apply
its counting bound to good indices in [M,2M-1]. Their corresponding
old ranks are N=2^(k+1), so (7) applies with the shifted exponent
j=k+1 and J=2M. It yields an unspanned good-row capacity at least

```
floor(M/L_M)/(1600 B_(2M)),
L_M=floor(3 log_2(A_good(2M+1)))+1.               (8)
```

Here A_good>=1 is the fixed upper/lower diameter-ratio constant
from that lookahead lemma; it is unrelated to the finite Schur
count A in section 1.

For the fixed constants and sufficiently large M this is
Omega(M/(log M)^2), and therefore also diverges. This uses the
actual previously proved gap count, not an assumed positive
proportion of good exponents. The individual gain lower bounds
of order 1/k do not on their own control this surviving capacity.

The more general bounded-feature result in section 1 also fits
(6), with c=(1-lambda_bar)/8 and b=1+lambda_bar. It covers
arbitrary prefix-dependent bounded features at amplitudes uniformly
below one, without requiring a new sign theorem for those features.

## 5. Exact scope and the remaining route

Equations (6)--(8) concern current unused kernels without an actual
future-span mask. Multiplying a row by 1[t<L_j] may remove most
of its annular mass. The lower bound c/2 must then be replaced by
the actual retained tail mass; the overlap proof remains valid,
but no uniform positive retained mass has been proved here.

Nor does a divergent capacity alone imply that its difference
from the sum of actual demands diverges. Original-Q1 closure
requires estimating that difference, or a differently constructed
productive shared source. These statements do not exclude an
improvement based on span masks, sharper shadow demands, another
carrier, or the full signed causal accounting.

The result does rule out a specific shortcut: the newly proved
nonnegative Born functional and individually nonsummable gains
cannot be combined with an assumed bounded literal unspanned
signed-linear envelope. That envelope has the explicit divergent
lower bound (7), even on the existing good epochs via (8).
Original Q1 and its final Lean verification remain unresolved.

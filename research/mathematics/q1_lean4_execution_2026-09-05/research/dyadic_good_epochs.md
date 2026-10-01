# Dyadic good epochs under one fixed critical cap

Date: 2026-09-05. Owner: `/root/global_route`, GPT-6 Astra Ultra.
Status: proved elementary sequence lemma and its Sidon application.
The proposed argument was supplied by `/root` and independently checked
here, including its endpoints and harmonic divergence. Original Q1
remains unresolved. No Lean verification is asserted in this note.

## 1. Abstract hypotheses and constants

Let `H_k>0` for integers `k≥k_0`, with `k_0≥1`, and suppose
`H_k` is strictly increasing. Assume fixed constants `c,C>0` satisfy

\[
 c4^k\le H_k\le Ck4^k\qquad(k\ge k_0).           \tag{1}
\]

Increasing `C` if necessary, assume `C≥c`. Put

\[
 s_k=H_k/4^k,\quad A=C/c\ge1,\quad
 r_k=H_k/H_{k-1}\quad(k\ge k_0+1).
\]

Then `c≤s_k≤Ck` and `s_k/s_(k−1)=r_k/4`.
Fix any `K>4` and define

\[
 \rho=K/4>1,\qquad
 \alpha=\frac1{\log2}+\frac1{\log\rho},\qquad
 {\cal G}=\{k\ge k_0+1:r_k\ge2,\ r_{k+1}\le K\}.       \tag{2}
\]

All logarithms are natural unless a base is indicated. The bounds in
(1) have one fixed onset and fixed constants; they are not reset on
the intervals used in the proof.

## 2. Exact bound on a consecutive interval without good epochs

**Lemma.** If integers `k_0+1≤a≤b` satisfy
`[a,b]∩G=∅`, then

\[
 b-a+1\le
    \frac{\log(A(a-1))}{\log2}
   +\frac{\log(A(b+1))}{\log\rho}
 \le\alpha\log(A(b+1)).                          \tag{3}
\]

**Proof.** First suppose `r_i<2` for every `i∈[a,b]`. Each such
step multiplies `s` by a factor less than `1/2`, so, with `L=b−a+1`,

\[
 c\le s_b<2^{-L}s_{a-1}\le2^{-L}C(a-1).
\]

Thus `L<log(A(a−1))/log2`, which is stronger than (3).

Otherwise let `j` be the first index in `[a,b]` with `r_j≥2`.
The initial `j−a` steps have ratios less than two. Applying the same
argument to them gives

\[
 j-a\le\frac{\log(A(a-1))}{\log2}.               \tag{4}
\]

This also holds if `j=a`, because its left side is zero and
`A(a−1)≥1`.

Since `j` is not good and `r_j≥2`, necessarily `r_(j+1)>K`.
Because `K>4>2`, this next ratio is again at least two. If `j+1≤b`,
its failure to be good forces `r_(j+2)>K`. Inductively,

\[
 r_i>K\qquad(j+1\le i\le b+1).                 \tag{5}
\]

There are exactly `b−j+1` ratios in (5). They multiply `s_j` by
factors greater than `ρ`, whence

\[
 c\rho^{b-j+1}<s_{b+1}\le C(b+1),\qquad
 b-j+1<\frac{\log(A(b+1))}{\log\rho}.             \tag{6}
\]

Adding (4) and (6) proves the first bound in (3), since
`(j−a)+(b−j+1)=b−a+1`. In particular no extra, uncontrolled
transition step is omitted: the first ratio `r_j≥2` is accounted for
by the compulsory growing ratio at the right endpoint `b+1`.
Finally `a−1≤b+1` proves the second bound. ∎

The use of `s_(b+1)≤C(b+1)` in (6) is deliberate. Replacing this by
`Ca` or pretending the upper bound is constant throughout the interval
would be unjustified. Formula (3) keeps the varying index exactly.

## 3. Infinitely many good epochs and logarithmic gaps

For every integer `M≥k_0+1`, define

\[
 L_M=\lfloor\alpha\log(2AM)\rfloor+1.             \tag{7}
\]

Every consecutive subinterval of `[M,2M−1]` of length `L_M`
contains a good index. Otherwise its right endpoint `b≤2M−1`
would give `L_M≤α log(A(b+1))≤α log(2AM)` by (3), contrary
to (7). Partitioning `[M,2M−1]` into such disjoint intervals gives

\[
 |{\cal G}\cap[M,2M-1]|\ge
             \left\lfloor\frac{M}{L_M}\right\rfloor.          \tag{8}
\]

Since `L_M=O_(A,K)(log M)`, this proves that good epochs are infinite.
For two consecutive sufficiently large good indices `g<h`, applying
(3) to `[g+1,h−1]`, if nonempty, gives

\[
 h-g\le1+\alpha\log(Ah).                         \tag{9}
\]

The same bound holds trivially when `h=g+1`.
It is also `O_(A,K)(log g)`: for sufficiently large `g`, one must
have `h<2g`. Indeed if `h≥2g`, (9) would imply
`h/2≤1+α log(Ah)`, impossible for sufficiently large `h`.
Thus eventually

\[
 h-g\le1+\alpha\log(2Ag).                        \tag{10}
\]

These statements include gaps that straddle a power-of-two boundary;
they are not obtained by resetting the scale at every good epoch.

## 4. Quantitative divergence of the reciprocal sum

In each integer-index block `[M,2M−1]`, every `k` is less than
`2M`. Therefore (8) and `floor(x)≥x−1` imply

\[
 \sum_{k\in{\cal G}\cap[M,2M-1]}\frac1k
 \ge\frac1{2M}\left\lfloor\frac M{L_M}\right\rfloor
 \ge\frac1{2L_M}-\frac1{2M}.                     \tag{11}
\]

Take `M=2^j`, and choose once `j_0` with `2^(j_0)≥k_0+1`.
Set

\[
 B=\alpha\log2>0,\qquad d=\alpha\log A+1>0.
\]

Equation (7) gives `L_(2^j)≤B(j+1)+d`. The blocks used in (11)
are disjoint, so for every integer `J≥j_0`,

\[
 \sum_{\substack{k\in{\cal G}\\k<2^{J+1}}}\frac1k
 \ge\frac12\sum_{j=j_0}^{J}\frac1{B(j+1)+d}
           -\frac12\sum_{j=j_0}^{J}2^{-j}.        \tag{12}
\]

The second sum is bounded. Since `1/(B(x+1)+d)` is decreasing,

\[
 \sum_{j=j_0}^{J}\frac1{B(j+1)+d}
 \ge\int_{j_0}^{J+1}\frac{dx}{B(x+1)+d}
 =\frac1B\log\frac{B(J+2)+d}{B(j_0+1)+d}.        \tag{13}
\]

It follows, for all sufficiently large real `N`, that

\[
 \boxed{\quad
 \sum_{\substack{k\in{\cal G}\\k\le N}}\frac1k
   \ge\frac1{2\alpha\log2}\log\log N
                  -O_{A,K,k_0}(1),\qquad
 \sum_{k\in{\cal G}}\frac1k=\infty.
 \quad}                                          \tag{14}
\]

For the passage to arbitrary `N`, use all complete blocks with
`2^(J+1)≤N`; then `J=log_2 N+O(1)`. This changes the logarithm
in (13) by a bounded quantity and does not assume `N` is dyadic.

For the intended choice **`K=8`**, one has `ρ=2`,
`α=2/log2`, and the explicit leading coefficient in (14) is **`1/4`**.
This conservative coefficient is not claimed optimal.

## 5. Application to the fixed-onset Sidon hypothesis

Let `a_1<a_2<...` be an infinite positive integer Sidon sequence,
including uniqueness for repeated two-sums, and suppose that one fixed
constant `C_0>0` and onset `n_0` satisfy

\[
 a_n\le C_0 n^2\log(2n)\qquad(n\ge n_0).         \tag{15}
\]

Write `h(n)=a_n−a_1` and `H_k=h(2^k)` for `k≥1`.
There are `binom(n,2)` distinct positive integer differences at most
`h(n)`, so

\[
 h(n)\ge\binom n2\ge n^2/4\qquad(n\ge2).       \tag{16}
\]

Consequently `H_k≥4^k/4` for `k≥1`. From (15), for all sufficiently
large `k≥1`,

\[
 H_k\le a_{2^k}
      \le C_0\log2\,(k+1)4^k
      \le2C_0\log2\,k4^k.                       \tag{17}
\]

Choose once an integer `k_0≥1` beyond this onset, let `c=1/4`,
and take `C=max(c,2C_0 log2)`. These give exactly (1).
Strict increase of `a_n` gives strict increase of `H_k`. There is
no division by `H_0=h(1)=0`: ratios are used only for
`k≥k_0+1≥2`.

Apply the lemma with `K=8`. For every good `k`, putting `p=2^k`
gives simultaneously

\[
 \boxed{\quad h(p)\ge2h(p/2),\qquad
                   h(2p)\le8h(p).\quad}         \tag{18}
\]

Moreover their weighted supply is divergent:

\[
 \sum_{\substack{p=2^k\\k\in{\cal G}}}
             \frac1{\log p}
       =\frac1{\log2}\sum_{k\in{\cal G}}\frac1k
       =\infty.                                  \tag{19}
\]

Replacing `log p` by `log(2p)` still gives divergence, since
`1/(k+1)≥1/(2k)` for `k≥1`. Therefore a subsequently proved
uniform positive contribution of size `c_*/log p` on just these
good epochs would have divergent total size. This final observation
does not assert that such contributions can be added against one
shared source budget; that remains a separate obligation.

The lemma uses the whole fixed-onset upper bound together with the
Sidon lower bound. It does not produce the proposed new carrier,
prove its historical retention, or close original Q1.

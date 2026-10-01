# Causal eligible capacity as an analytic coefficient functional

2026-09-05. Parent derivation. Original Q1 remains unresolved. These finite
identities have not been Lean-verified. No numerical experiment was needed.
The source conventions are those of `signed_output_energy_closure.md`; the
quartic identity is already proved in `nested_fourier_route.md`.

## 1. A finite exact formula with the actual order retained

Fix one actual increasing positive integer Sidon sequence, with repeated
two-sums included in the Sidon condition. Write

```
H_n=a_n-a_1, Q_n=n(n-1),
alpha_n=Q_n^-2, kappa_n=alpha_n-alpha_(n+1),
u_r=sum_(k>=r) kappa_k/H_k^2.
```

The positive differences of a prefix are distinct. On the unit circle set

```
h_n(z)=sum_(d in Delta P_n) d z^d,   h_1=0,
K_n^+(t)=sum_(d>0; d,d+t in Delta P_n) d(d+t), t>0.
```

Let Pi_+ select the strictly positive Fourier coefficients of a Laurent
polynomial. For the signed bank Fhat_n and 0<=lambda<=1, direct separation
into the two same-sign cases and the one positive-output opposite-sign
case gives

```
sum_(d,e in Fhat_n; d-e=t) (|de|+lambda de)
 = 2(1+lambda) K_n^+(t)+(1-lambda)[z^t]h_n(z)^2,

C_n^lambda(z)
 =2(1+lambda) Pi_+(|h_n(z)|^2)+(1-lambda)h_n(z)^2.       (1)
```

Every coefficient of C_n^lambda is nonnegative, and its constant term
vanishes. In the opposite-sign term t=d+|e|; the coefficient of h_n^2
counts every ordered split exactly once, including the equal split. For
each unordered signed source pair, choosing d-e>0 selects exactly one
orientation. Consequently there is no extra unordered-pair factor in (1).

For a finite terminal rank T define the actual analytic polynomial

```
Q_T^lambda(z)=sum_(i=2..T-1) z^(a_i) C_(i-1)^lambda(z).
```

Then the eligible capacity of the permanent output-clock source satisfies
the exact identity

```
Elig_T(Psi_lambda)
 = sum_(r=2..T) u_r [z^(a_r)] Q_T^lambda(z).             (2)
```

Indeed, an actual output t=a_r-a_i has both source labels available before
its lower endpoint exactly when both lie in Fhat_(i-1). Its source birth
b then obeys b<i<r. The output is absent from every P_k with k<r; for
k>=r its nonzero difference multiplicity is exactly one. Thus the full
complete-history coefficient of this pair in Psi is u_r times its weight
in (1). Summing all i<r counts every eligible source pair once because
the output has unique actual endpoints. Conversely, terms indexed by
i>=r cannot contribute to [z^(a_r)]: all their frequencies exceed a_i.
This proves (2) without assuming any filtration or martingale property.

If F_(u,T)(z)=sum_(r=2..T)u_r z^(a_r), (2) can equivalently be written
as the Haar integral of Q_T^lambda conjugate(F_(u,T)). This does not
change the physical source or grant another copy of its label budget.
Although all sources are priced by the complete history, (2) includes
only outputs whose actual endpoints occur by T.

## 2. What ordinary Carleson theory actually controls here

For a fixed terminal T, the point polynomials

```
F_n(z)=sum_(j<=n)z^(a_j), n<=T,
```

are ordinary Fourier-frequency partial sums of F_T: the numerical cutoff
a_n selects precisely the first n frequencies. The actual Sidon quartic
identity gives ||F_T||_4^4=2T^2-T. The primary variation-norm Carleson
theorem of Oberlin--Seeger--Tao--Thiele--Wright, Theorem 1.1, applies for
r>2 and r'<p<infinity. Taking r=3 and p=4 therefore gives, in particular,

```
||max_(n<=T)|F_n|||_4 <= C_4 (2T^2-T)^(1/4).            (3)
```

The same conclusion applies to ordinary partial sums with any fixed
coefficients c_j. The quartic norm in that case is
2(sum|c_j|^2)^2-sum|c_j|^4. It therefore also applies to the point
coefficients c_j=a_j-a_1, with the corresponding finite weighted norm.
The theorem does not assert a general r=2 variation estimate.

Primary sources checked on 2026-09-05:
[arXiv record](https://arxiv.org/abs/0910.1555) and
[author-hosted paper, Theorem 1.1](https://webhomes.maths.ed.ac.uk/~wright/papers/osttw0710.pdf).
The applicability statement (3), rather than the theorem itself, is the
parent's deduction for these actual Sidon polynomials.

In contrast, h_n is ordered by endpoint birth, not by the numerical value
of its difference frequency. The actual Sidon set {1,11,12} has old gap
10 after its second endpoint and new gaps 1 and 11 after its third.
Its unordered two-sums are 2,12,13,22,23,24, all distinct. Thus h_2=10z^10
is not an ordinary frequency truncation of h_3=z+10z^10+11z^11.
The hypotheses allowing (3) do not directly turn the sequence h_n into
frequency partial sums of one gap polynomial.

There is a valid algebraic relation. With D=z(d/dz) on Laurent
polynomials,

```
D(|F_n|^2)=h_n-conjugate(h_n),
h_n=Pi_+ D(|F_n|^2).                                   (4)
```

Equation (4) retains a quadratic product, a derivative, and a projection
whose input varies with n. A scalar Lp bound for Pi_+ on each input does
not allow exchanging Pi_+ with a pointwise supremum. Neither (3) nor
(4) alone bounds the order-sensitive coefficient functional (2).
No impossibility result about Fourier methods is asserted here.

## 3. The elementary bound still stops at a harmonic cost

Let Z_n=sum_(d in Fhat_n)d^2. For every t>0, the positive-output edges
d-e=t form a graph of degree at most two on Fhat_n. The inequality
|de|<= (d^2+e^2)/2 therefore gives

```
[z^t] C_n^lambda <= (1+lambda) Z_n
                           <= (1+lambda) Q_n H_n^2.   (5)
```

Since u_r<=1/(Q_r^2 H_r^2), summing at most r-1 lower output endpoints
in (2), each with n=i-1<r, gives for r>=3

```
u_r sum_(i<r)[z^(a_r-a_i)] C_(i-1)^lambda
 <= (1+lambda)(r-1)Q_(r-2)/Q_r^2
 <= (1+lambda)/r.                                     (6)
```

The stage r=2 contributes zero. All estimates in (5)--(6) are on the
actual output and label set; the graph bound is not an assumption about
an arbitrary incidence table. The resulting O_lambda(log T) bound is
consistent with the previously proved divergent actual demands under a
single fixed cap. It is not a uniform finite bound.

Consequently the new formulation identifies a concrete possible target:
a stronger order-sensitive estimate for the positive coefficients in
(2), using the same Sidon history and one fixed cap. A uniform-in-T upper
bound for (2) under that cap would contradict the already established
eligible-demand divergence and imply original Q1. Such a bound is not
proved here. Replacing h_n by numerical Fourier truncations, or inserting
an unproved quadratic maximal estimate, would alter this missing step.

## 4. Current related primary paper and scope

The primary arXiv record for Kevin O'Bryant, *On the Thickness of Infinite
Generalized Sidon Sets, I*, was checked at version 3 (26 July 2026). Its
abstract proves a positive-constant upper bound for the corresponding
liminf, 2 sqrt(g)/sqrt(log 2); it does not state the zero liminf required
here. Section 3.1 presents suggested further directions rather than a
proof of original Q1. This is a scope check, not a claim about the optimal
constant among all literature.

Sources: [primary record](https://arxiv.org/abs/2606.28651) and
[version 3 text](https://arxiv.org/html/2606.28651v3).
No other theorem from that paper, and no normalization inferred from a
rendered display, is used in (1)--(6).

The mathematical contribution of this note is the exact causal analytic
coefficient identity (2), its source-clock justification, and the explicit
limit of the proposed direct Carleson application. It is not a completed
proof or refutation of Q1 and does not change the final Lean status.

# The output-rank commutator and its surviving future covariance

2026-09-05. Author: `/root/linear_causal_sign`, GPT-6 Astra Ultra.

**Status.** Summation by parts at actual output ranks is compatible with
the B2 quartic identity. That identity removes the fresh same-sign star
and makes a precise diagonal contribution uniformly summable. However,
an exact rank commutator retains the causal functional rather than
canceling it. A new bound below isolates a nonnegative correlated future
covariance profile. An explicit family of actual Sidon sets also shows
that strict endpoint order alone does not give the tempting unweighted
bound O(T^3H_T^2): the raw causal functional can have order T^4H_T^2.

These are analytical statements about actual histories and exact finite
families. No numerical experiment, prior-check replay, or Lean execution
was used. They do not prove or refute original Q1. Only this new note was
written; the inputs are `causal_fourier_coefficient_route.md` and
`nested_fourier_route.md`.

## 1. Output Abel weights and the genuine fresh-star identity

Use one actual increasing positive integer Sidon history, with repeated
two-sum uniqueness. Write h_n, Q_n, H_n, alpha_n, kappa_n, and u_n as in
the causal coefficient note. In particular
u_r=sum_(k>=r)kappa_k/H_k^2 and alpha_k=Q_k^-2.
Define the actual birth increment

```
g_b(z)=h_b(z)-h_(b-1)(z)
     =z^(a_b) sum_(j<b)(a_b-a_j)z^(-a_j),
s_b=||g_b||_2^2,        S_n=||h_n||_2^2.
```

Different birth stars have disjoint difference frequencies, so
S_n=sum_(b<=n)s_b. This is L2 orthogonality, not a martingale assertion.

Fix a finite terminal rank T. For b<T, set

```
F_(b,r](z)=sum_(b<i<=r)z^(a_i),
V_b(z)=u_T|F_(b,T](z)|^2
       +sum_(r=b+1..T-1)(u_r-u_(r+1))|F_(b,r](z)|^2,
m_b=sum_(r=b+1..T)u_r.
```

Set V_T=0 and m_T=0. This is the exact positive Abel representation

```
V_b=sum_(b<i,j<=T)u_max(i,j) z^(a_i-a_j).             (1)
```

In particular V_b is nonnegative on the unit circle, its constant
coefficient is m_b, and every future output is priced at its actual
upper endpoint. Nothing orders the gap frequencies numerically.

For any actual point block B strictly after b, the weighted B2 quartic
identity applied to the disjoint point supports gives

```
||F_B g_b||_2^2=|B| s_b.
```

Equivalently, distinct terms of
F_B sum_(j<b)(a_b-a_j)z^(-a_j) have distinct difference frequencies:
their two actual endpoints determine them uniquely. Thus

```
integral |g_b|^2 V_b=m_b s_b.                        (2)
```

The same-sign off-diagonal coefficients of |g_b|^2 lie in the old
positive difference set Delta P_(b-1), and cannot be internal differences
of any such B. Hence the fresh same-sign star pays ZERO eligible pairs.

## 2. Exact source-increment expansion, including the repeated class

All integrals below use Haar probability measure. Define

```
X_b=Re integral h_(b-1) conjugate(g_b) V_b,
Y_b=integral h_(b-1) g_b V_b,
Z_b=integral g_b^2 V_b.
```

These are real and nonnegative: the gap coefficients and all coefficients
of V_b are nonnegative. Expanding the source note's C_n^lambda into birth
increments, and using (2) for the fresh same-sign term, gives exactly

```
Elig_T(Psi_lambda)
 =2(1+lambda)sum_(b=2..T)X_b
    +2(1-lambda)sum_(b=2..T)Y_b
    +(1-lambda)sum_(b=2..T)Z_b.                      (3)
```

The source pair in each mixed term has one unique later birth b. Its
lower and upper output endpoints both lie in the suffix after b. Thus
the suffixes in (1) are not independent physical budgets; the unique
source birth is what prevents duplication in (3).

The term Z_b retains the same-birth opposite-sign pairs, including a
doubled numeric label. These pairs can be eligible and must not be
deleted by the older positive-bank convention. Nevertheless they have
an absolute finite price. If U_b^star=sum_(j<b)(a_b-a_j), the actual distinct
future output labels and u_r<=w_b=alpha_b/H_b^2 imply

```
0<=sum_b Z_b<=sum_(b>=2)w_b (U_b^star)^2
             <=sum_(b>=2)1/b^2=zeta(2)-1.
```

The comparison u_r<=w_b is used only as an upper bound on this
nonnegative discarded class. It does not replace the prices in (3).
For lambda=1 the entire fresh remainder in (3) is zero exactly.
There is also a sharper bound using the actual positive measure V_b:
Z_b<=integral |g_b|^2V_b=m_b s_b. The elementary estimate for m_b
proved in Section 4 yields

```
0<=sum_b Z_b<=[zeta(2)-zeta(3)]/3.                  (4)
```

Thus even this fresh opposite-sign class is paid using the actual
quartic norm before any mixed covariance is estimated.

## 3. Summation by parts leaves an exact rank commutator

Let W_b(z)=sum_(r=b+1..T)u_r z^(a_r). Removing the first point of
the future suffix gives

```
V_(b-1)-V_b
 =u_b+z^(-a_b)W_b+z^(a_b)conjugate(W_b).             (5)
```

Define the nonnegative lower-endpoint payment

```
L_b=sum_(r=b+1..T)u_r K_(b-1)^+(a_r-a_b)
```

and the diagonal-subtracted commutator
J_b=V_(b-1)-V_b-u_b. Then

```
integral |h_(b-1)|^2 J_b=2L_b.                      (6)
```

In particular the rank commutator is not orthogonal to the old source.
For E_b=integral |h_b|^2V_b, equations (2),(5) give the exact update

```
E_b-E_(b-1)
 =2X_b+m_b s_b-u_b S_(b-1)-2L_b.                    (7)
```

Both endpoint energies vanish: E_1=0 and E_T=0. Moreover

```
sum_(b=2..T)m_b s_b=sum_(b=2..T)u_b S_(b-1).
```

Thus summing (7) gives sum_b X_b=sum_b L_b. The quartic diagonals
cancel, while the boundary commutator is exactly the original causal
same-sign coefficient functional divided by its factor 2(1+lambda).
Omitting that commutator would erase the quantity to be estimated.

The analytic opposite-sign part behaves consistently. If
E'_b=integral h_b^2V_b, its diagonal coefficient is zero, and (5)
gives

```
E'_b-E'_(b-1)=2Y_b+Z_b
       -sum_(r>b)u_r[z^(a_r-a_b)]h_(b-1)^2.          (8)
```

Only one of the two nonconstant terms in (5) contributes because h^2
is strictly analytic. Its endpoint energies also vanish. This retains
all factors in the opposite-sign part of the source note's identity.

## 4. A summable quartic diagonal and the remaining covariance profile

Introduce the actual weighted future covariance

```
P_b=sum_(b<i<r<=T)u_r K_(b-1)^+(a_r-a_i)>=0.
```

It has the exact expression

```
integral |h_(b-1)|^2V_b=m_b S_(b-1)+2P_b.            (9)
```

Weighted Cauchy on the nonnegative measure V_b gives both
X_b and Y_b at most sqrt(m_b s_b[m_b S_(b-1)+2P_b]). Since their
coefficients in (3) sum to 4, (3)--(4) imply

```
Elig_T(Psi_lambda)
 <=4 sum_b m_b sqrt(s_b S_(b-1))
    +4sqrt(2)sum_b sqrt(m_b s_b P_b)
    +(1-lambda)[zeta(2)-zeta(3)]/3.                  (10)
```

The first sum really is uniformly finite, without a cap. The elementary
inequality

```
alpha_r<=1/3[(r-1)^(-3)-r^(-3)]
```

and H_r>=H_b give m_b<=1/(3b^3H_b^2). Also
s_b<=(b-1)H_b^2 and
S_(b-1)<=(b-1)(b-2)H_b^2/2. Consequently

```
m_b sqrt(s_b S_(b-1))<=1/(3sqrt(2)b^(3/2)),
m_b s_b<=1/(3b^2).
```

The resulting bound is

```
Elig_T(Psi_lambda)
 <=C_lambda+4sqrt(2/3)sum_(b=2..T-1)sqrt(P_b)/b,

C_lambda=4[zeta(3/2)-1]/(3sqrt(2))
                 +(1-lambda)[zeta(2)-zeta(3)]/3.    (11)
```

This isolates a genuinely multilinear obligation after every contribution
controlled by the fresh B2 quartic identity has been paid at finite cost.
The P_b are correlated: a fixed physical pair can occur in several of
them as the cut b varies. Equation (11) is an analytic estimate using
those overlapping quantities, not an allocation of their sum as fresh
capacity. Any summability proof for its right-hand covariance series
must retain that correlation and the actual history.

The trivial bound P_b<=1/8 follows from
P_b<=w_b (U_(b-1)^old)^2/2, where
U_(b-1)^old=sum_(d in Delta P_(b-1))d
             <=((b-1)(b-2)/2)H_b. That recovers a harmonic estimate but
does not settle the new covariance series. No improvement of that kind
is assumed in (11).

## 5. Strict triangular order does not yield a quartic-scale raw bound

One precise tempting intermediate estimate would be

```
A_T^lambda:=sum_(r<=T)sum_(i<r)
                [z^(a_r-a_i)]C_(i-1)^lambda
       <=K_lambda T^3H_T^2                           (12)
```

uniformly over actual finite Sidon prefixes. It would save a factor T
over the elementary bound before output Abel weighting. The actual
quartic identity and the strict source-before-lower-endpoint order do
NOT imply (12): it is false already for lambda=1.

For any odd prime p let r_i be the least residue of i^2 modulo p and set

```
x_i=2pi+r_i,     0<=i<p,
a_(i+1)=1+x_i.                                    (13)
```

These are strictly increasing positive integers and form an actual
Sidon set. Indeed equality of two positive differences first forces
their index differences d to agree, because the residue corrections
lie strictly between -p and p. Reducing the remaining equality modulo
p gives d(2i+d)=d(2j+d); since 0<d<p and p is odd, i=j.
Thus all positive differences, and hence repeated two-sums, are unique.
The actual terminal width obeys H_p<2p^2.

Take old rank n=(p-1)/2 and the actual future block of the remaining
m=(p+1)/2 points. Let U=sum_(d in Delta P_n)d and
S=sum_(d in Delta P_n)d^2. For p>=5, every gap x_j-x_i is at least
p(j-i), n>=2p/5, and H_n<p^2. Therefore

```
U>=p n(n^2-1)/6>=p n^3/8>=p^4/125,
S<=p^6/8.                                        (14)
```

The positive-gap shadow of this actual future block has total mass mU
and support on fewer than 2p^2 integers. For the latter, its interval
length is at most x_(p-1)+x_(n-1)-x_n<2p^2.
Its exact trace term is mS, and its remaining energy is twice the
physical positive-bank pair sum on Delta B. Cauchy thus gives

```
sum_(t in Delta B)K_n^+(t)
 >=1/2[p^8/125000-p^7/8].                           (15)
```

Every pair counted in (15) has sources born by n and both output
endpoints after n. It is therefore an actual term of the strictly
triangular causal functional. Since C^1 has same-sign factor 4,

```
A_p^1>=p^8/62500-p^7/4.
```

For every odd prime p>=31250 this yields

```
A_p^1>=p^8/125000,
A_p^1/(p^3H_p^2)>=p/500000 -> infinity.              (16)
```

This disproves (12) analytically on actual Sidon families, without a
parameter sweep or an off-realizable incidence model. In fact the order
p^4H_p^2 is attained up to an absolute constant, matching the elementary
raw rank upper scale. The single old-half/future-half block already
forces it; no repeated future-block budget is involved.

This is not an infinite capped counterexample and does not refute a
uniform weighted bound under a single infinite-history cap. In particular
the complete-history prices u_r in the original target are not replaced
by unrelated finite-terminal prices in (16). A successful output-Abel
argument must exploit cross-scale structure of the actual covariance
profile or its commutator, beyond the false unweighted power saving (12).

The new retained target is thus concrete: control the profile in (11),
or prove another genuinely correlated bound on (6)--(9), using one actual
history. The exact quartic cancellations, the finite repeated-star cost,
and the raw finite obstruction specify which terms such an argument
must still handle. Original Q1 remains unresolved.

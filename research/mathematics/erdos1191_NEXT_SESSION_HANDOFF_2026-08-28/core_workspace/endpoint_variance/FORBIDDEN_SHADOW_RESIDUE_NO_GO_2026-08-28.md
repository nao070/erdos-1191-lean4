# Wave 6: a residue-class no-go for forbidden-shadow amortization

**Date:** 2026-08-28  
**Status:** exact finite construction and a growing-window asymptotic no-go.  
**Global status:** Erdős Problem #1191 remains unresolved.

## 1. Purpose and boundary

For a normalized finite Golomb ruler $A$, define the one-point forbidden
shadow

$$
\Delta^+(A)=\{a_j-a_i:0\le i<j<|A|\},
\qquad
F(A)=A+\Delta^+(A).
$$

Older project logs reported that $F(A)$ was nearly full immediately above the
endpoint for the particular dense rulers tested there. The source and raw
data for those experiments are absent from this handoff, and the trend is not
universal. This note gives primitive critical-scale Golomb rulers for which
$F(A)$ occupies at most four residue classes and has vanishing local density.
A growing compatible finite window can simultaneously retain the positive
covariance innovation of the Erdős--Turán family.

This refutes a local proof based only on the density of $F(A)$. It does not
construct one infinite critical Sidon sequence and does not resolve either
question in Problem #1191.

## 2. Exact one-point extension criterion

Let

$$
A=\{0=a_0<a_1<\cdots<a_{n-1}=D\}
$$

be a Golomb ruler and let $x>D$. The old differences are already distinct,
and the new differences $x-a$, $a\in A$, are mutually distinct. Hence

$$
\boxed{
A\cup\{x\}\text{ is Golomb}
\quad\Longleftrightarrow\quad
x\notin F(A).
}
\tag{1}
$$

Indeed, $x-a=d\in\Delta^+(A)$ is equivalent to
$x=a+d\in F(A)$. There are no other possible collisions in a one-point
extension.

## 3. Residue-lift theorem

Let

$$
B=\{0=b_0<b_1<\cdots<b_{r-1}\}
$$

be any normalized Golomb ruler, and let $L\ge3$. Define the $(r+1)$-mark
ruler

$$
A_L(B)=\{0,1,Lb_1,\ldots,Lb_{r-1}\}.
\tag{2}
$$

Then $A_L(B)$ is Golomb. Its complete positive-difference list splits as

$$
\boxed{
\Delta^+(A_L(B))
=\{1\}
\;\dot\cup\;
L\Delta^+(B)
\;\dot\cup\;
\{Lb_j-1:1\le j<r\}.
}
\tag{3}
$$

The middle family is collision-free because $B$ is Golomb. The last family is
collision-free because the $b_j$ are distinct. The three families are
pairwise disjoint: their residues modulo $L$ are respectively $1,0,-1$,
and $L\ge3$ also rules out $Lb_j-1=1$. Their cardinalities add to

$$
1+\binom r2+(r-1)=\binom{r+1}{2},
$$

so every positive difference has been accounted for exactly once.

The marks of $A_L(B)$ occupy only residues $0,1\pmod L$, while (3) gives

$$
\Delta^+(A_L(B))\bmod L\subseteq\{-1,0,1\}.
$$

Consequently

$$
\boxed{
F(A_L(B))\bmod L\subseteq\{-1,0,1,2\}.
}
\tag{4}
$$

For any interval $I$ of $H\ge1$ consecutive integers, one residue class
contains at most $\lceil H/L\rceil$ members of $I$. Thus

$$
\boxed{
|F(A_L(B))\cap I|
\le4\left\lceil\frac HL\right\rceil
\le\frac{4H}{L}+4.
}
\tag{5}
$$

In particular, in the entire next-diameter interval,

$$
\frac{|F(A_L(B))\cap(D,2D]|}{D}
\le\frac4L+\frac4D.
\tag{6}
$$

By (1), every point of the complement is individually appendable. This says
nothing about simultaneous compatibility among several such points.

The same construction also calibrates a pair-sum attack. Golomb uniqueness
implies uniqueness of all unordered pair sums: a nontrivial equality of two
such sums rearranges to an equality of two positive differences. But

$$
A_L(B)+A_L(B)\bmod L\subseteq\{0,1,2\}.
$$

The dilation simply stretches the available integer bands by $L$. Thus
pair-sum injectivity or interval capacity alone does not remove a logarithmic
dilation; a successful reset-renewal argument must compare genuinely
different epochs or use more structure than one-dimensional occupancy.

## 4. Critical-scale finite family

Let $p$ be an odd prime and $2\le r\le p$. The integer Erdős--Turán ruler

$$
b_i=2pi+(i^2\bmod p),\qquad0\le i<r,
\tag{7}
$$

is Golomb. Strict increase follows because the residue correction changes by
less than $p$. If two positive differences are equal, their rank increments
are equal because the intervals

$$
2pd+[-(p-1),p-1]
$$

are disjoint for distinct positive $d$. Reduction modulo $p$ then gives
$2d(i-k)=0\pmod p$, hence $i=k$.

Its diameter is less than $2pr$. For every sufficiently large desired mark
count $n=r+1$, Bertrand's theorem supplies an odd prime $r<p<2r$. Taking

$$
L_n=\max(3,\lceil\log n\rceil)
$$

in (2) gives a primitive $n$-mark Golomb ruler (it contains $0,1$) with

$$
D_n<4L_n n^2=O(n^2\log n),
\tag{8}
$$

but (6) tends to zero. Therefore critical diameter and primitivity do not
force the one-point forbidden shadow to be locally dense.

## 5. Growing compatible-window obstruction

The preceding no-go is not confined to isolated rulers. Let $M=2^J$, put

$$
t=\log M,
\qquad
R=\left\lfloor\frac12\log_2t\right\rfloor,
\qquad
L=\lceil\sqrt t\rceil,
\tag{9}
$$

and choose a prime $M<p<2M$. Form one terminal ruler from (7) with $M-1$
base marks and apply (2). Its first $n$ marks, for every dyadic

$$
n=M/2^s,\qquad0\le s\le R,
$$

are compatible prefixes of the same finite ruler and have

$$
D_n<4LMn.
$$

For $t\ge4$,

$$
L\le\frac32\sqrt t,
\qquad
M/n\le\sqrt t,
\qquad
\log n\ge t-\tfrac12\log t\ge\frac34t.
$$

Consequently, for all sufficiently large $M$, their endpoint moduli obey

$$
\boxed{N_n=D_n+1\le9n^2\log n.}
\tag{10}
$$

For an adjacent transition $n\to2n$, put

$$
H_n=D_{2n}-D_n,
\qquad
\theta_n=
\frac{|F(A_n)\cap(D_n,D_{2n}]|}{H_n}.
$$

This is the forbidden-shadow density in the actual numerical band occupied by
the newly appended marks. Equation (5) gives

$$
\theta_n\le\frac4L+\frac4{H_n}.
$$

Writing $r_i=i^2\bmod p$, the difference
$b_{2n-2}-b_{n-2}=2pn+r_{2n-2}-r_{n-2}$ is at least
$2pn-(p-1)$. Hence $H_n\to\infty$ uniformly in the window, and therefore

$$
\sum_{s<R}\theta_{M/2^{s+1}}
=O\!\left(\frac{R}{L}\right)=o(1).
\tag{11}
$$

On the other hand, dilation and the extra mark $1$ do not change the
normalized Erdős--Turán gap-profile limit. Uniformly over this window, the
diameter-gap measures tend to Lebesgue measure and

$$
\frac{N_n}{N_{2n}}\longrightarrow\frac12.
$$

Here is the endpoint check. For $k\ge2$, the $k$-th mark of the lifted ruler
is

$$
a_k=L(2p(k-1)+r_{k-1}),
\qquad 0\le r_{k-1}<p,
$$

and

$$
N_n=L(2p(n-2)+r_{n-2})+1.
$$

The cumulative mass of the diameter-gap measure through rank $k$ is exactly
$(a_k+1)/N_n$. Since

$$
\left|
\frac{2pi+r_i}{2ps+r_s}-\frac{i}{s}
\right|
\le\frac1s
\qquad(0\le i\le s),
$$

putting $s=n-2$ and $i=k-1$ gives the explicit grid bound

$$
\epsilon_n:=
\max_{0\le k<n}
\left|\nu_n([0,k/n])-\frac{k}{n}\right|
\le
\frac{2}{n-2}+\frac{1}{Lp(n-2)}.
\tag{12a}
$$

The first term pays once for the Erdős--Turán residue and once for the rank
shift

$$
\frac{i}{n-2}\longleftrightarrow\frac{i+1}{n}.
$$

The second term pays for replacing $Lb_i/Lb_{n-2}$ by
$(Lb_i+1)/(Lb_{n-2}+1)$. The two exceptional ranks $0,1$ satisfy the same
displayed bound because their total mass is $2/N_n$. Between consecutive grid
points the uniform distribution function moves by at most $1/n$, so

$$
d_K(\nu_n,\lambda)
\le
\frac{3}{n-2}+\frac{1}{Lp(n-2)}.
\tag{12b}
$$

The endpoint ratio has a similarly explicit rank-shift estimate. Writing
$s=n-2$ and $s'=2n-2=2s+2$,

$$
\left|
\frac{N_n}{N_{2n}}-\frac12
\right|
=
\frac{
\left|2[L(2ps+r_s)+1]-[L(2ps'+r_{s'})+1]\right|
}{
2[L(2ps'+r_{s'})+1]
}
\le
\frac{7}{8(n-1)}
+\frac{1}{8Lp(n-1)}.
\tag{12c}
$$

This proves both uniform weak convergence and the displayed endpoint-modulus
ratio with all shifts retained.

For $z=(u(1-u),u)$, the limiting covariance has

$$
\operatorname{Var}(u(1-u))=\frac1{180},
\quad
\operatorname{Cov}(u(1-u),u)=0,
\quad
\operatorname{Var}(u)=\frac1{12}.
$$

Using the exact dyadic transport matrix

$$
B=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix},
$$

write $\mathcal R_n=\operatorname{Cov}_{\nu_n}z$. The exact recursion gives

$$
\frac{Q_n}{N_{2n}}
=\mathcal R_{2n}
-\frac{N_n}{N_{2n}}B\mathcal R_nB^{\mathsf T}.
$$

For the limiting covariance $\mathcal R$, direct multiplication gives
$(B\mathcal RB^{\mathsf T})_{00}=1/180$. Therefore, uniformly for the $R$
adjacent transitions,

$$
\boxed{
\frac{(Q_n)_{00}}{N_{2n}}=\frac1{360}+o(1).
}
\tag{12}
$$

More precisely, bounded variation of the polynomial entries of $zz^{\mathsf
T}$ and (12b)--(12c) give

$$
\frac{(Q_n)_{00}}{N_{2n}}-\frac1{360}
=O\!\left(
\frac1{n_{\min}}+\frac1{Lp\,n_{\min}}
\right),
\qquad
n_{\min}=M/2^R.
\tag{12d}
$$

Since $n_{\min}\ge M/\sqrt{\log M}$ and $R=O(\log\log M)$, multiplying the
right side by all $R$ transitions still gives $o(1)$.

Thus the innovation sum is in fact $R/360+o(1)\to\infty$, while the total local
forbidden-shadow density in (11) tends to zero. For any fixed constants
$C_0,C_1$, these finite compatible windows refute an estimate of the form

$$
\sum_n\frac{(Q_n)_{00}}{N_{2n}}
\le C_0+C_1\sum_n
\frac{|F(A_n)\cap(D_n,D_{2n}]|}{D_{2n}-D_n}.
\tag{13}
$$

As in the earlier growing-window obstructions, the terminal family depends on
$M$. It is not one infinite globally critical Sidon sequence, so an
unbounded-history arithmetic theorem remains possible.

## 6. Reproduction

From core_workspace/endpoint_variance/ run

    python wave6_forbidden_shadow.py
    python -m unittest -v test_wave6_forbidden_shadow.py

The verifier checks the Erdős--Turán base, the complete difference taxonomy,
the residue confinement, the exact criterion (1) for every candidate in one
next-diameter interval, the interval bound (5), compatible dyadic prefixes,
and exact rational $Q_{00}/N$ values. It is finite verification of the
algebra, not evidence for an infinite construction.

## 7. Surviving target

The forbidden shadow remains relevant only with additional global structure.
A viable reset-renewal proof must show that the residue classes or other holes
available to one epoch cannot be chosen coherently through an unbounded
history. Critical size, primitivity, single-epoch pair-sum injectivity,
single-point appendability, and even a growing recent compatible window do not
supply that conclusion.

# Fixed-depth Erdős--Turán no-go and interval-spectrum packing

Date: 2026-08-28  
Status: rigorous local packing lemmas and an asymptotic obstruction to every
uniform fixed-depth upper estimate based only on finite compatible prefixes.
Global critical-sequence amortization remains open.

## 1. Interval-sum band packing

Let

\[
A=\{a_0<a_1<\cdots<a_{m-1}\}
\]

be a Sidon ruler.  Every rank interval \([i,j]\), \(i<j\), has the distinct
integer sum \(a_j-a_i\).  Consequently, at most \(R+1\) such sums can lie in
any integer band \([L,L+R]\).

Two immediate forms will be useful.  If \(0\le r<s<m\),
\(W=a_s-a_r\), and \(D=a_{m-1}-a_0\), then the internal differences of the
block \(a_r,\ldots,a_s\) give

\[
\boxed{\binom{s-r+1}{2}\le W.}
\tag{1}
\]

The \((r+1)(m-s)\) cross differences with \(i\le r\) and \(j\ge s\) all lie
in \([W,D]\).  Hence

\[
\boxed{D-W+1\ge(r+1)(m-s).}
\tag{2}
\]

For the adjacent gap \(h_k=a_k-a_{k-1}\), take \(r=k-1,s=k\) in (2) and
put \(N=D+1\).  This yields the sharp local ceiling

\[
\boxed{h_k\le N-k(m-k).}
\tag{3}
\]

These inequalities use full contiguous-sum uniqueness, but they are
compatible with constant normalized endpoint variance and therefore do not
by themselves give the missing upper budget.

## 2. Disjoint block-spectrum packing

Take pairwise disjoint consecutive mark blocks \(B_t\), discarding singleton
blocks, so every \(q_t\ge2\).  Let \(q_t\) be the
number of marks, \(R_t\) the span, and
\(P_t=\binom{q_t}{2}\) the number of internal positive differences.  Global
Sidon uniqueness makes the internal spectra of distinct blocks disjoint.

Order the spans increasingly.  The first \(r\) spectra contain
\(\sum_{i\le r}P_{(i)}\) distinct positive integers, all at most
\(R_{(r)}\).  Therefore

\[
\boxed{R_{(r)}\ge\sum_{i\le r}P_{(i)}.}
\tag{4}
\]

Writing \(S_r=\sum_{i\le r}P_{(i)}\), the integral comparison
\(P_{(r)}/S_r\le\int_{S_{r-1}}^{S_r}dx/x\) for \(r\ge2\) gives

\[
\boxed{
\sum_t\frac{P_t}{R_t}
\le1+\log\frac{\sum_tP_t}{P_{(1)}}.
}
\tag{5}
\]

This is a genuine compatible-block Carleson estimate, but for dyadic block
sizes its right side is \(O(J)\), not \(o(\log J)\).

## 3. The fixed-depth Erdős--Turán family

Let \(M=2^j\) and choose any prime \(p\) with \(M\le p<2M\).  Define

\[
b_i=2pi+(i^2\bmod p),
\qquad0\le i<M.
\tag{6}
\]

This is the classical integer Erdős--Turán Sidon ruler.
For completeness, equality of two differences first forces their rank
increments to agree, because the residual discrepancy has absolute value
strictly below \(2p\).  If that increment is \(0<d<p\), reduction modulo
\(p\) gives \(2d(i-k)=0\pmod p\); since \(p\) is odd, the starting ranks also
agree.  Thus all positive differences are distinct.

Fix a depth \(L\).
For \(0\le\ell\le L\), put \(n=M/2^\ell\).  Its prefix diameter satisfies

\[
N_n=b_{n-1}+1\le2pn+1<4Mn+1.
\]

Since \(M/n=2^\ell\), for all sufficiently large \(M\), uniformly over this
fixed window,

\[
N_n\le2n^2\log n.
\tag{7}
\]

More explicitly, the convention \(N_n\le2Cn^2\log n\) holds with \(C=1\)
whenever \(\log(M/2^L)\ge2^{L+1}\).  Thus the quantifier is
\(\forall L\,\exists j_0(L)\,\forall j\ge j_0(L)\): every fixed number of
recent prefixes is compatible with the same critical envelope.  The depth is
not allowed to grow with \(M\).  This is a family of arbitrarily large finite
windows; it is not one nested infinite critical sequence.

## 4. Uniform gap-measure limit

For a prefix of \(n\) marks from (6),

\[
b_k=2pk+O(p),
\qquad
N_n=2pn+O(p).
\]

With \(h_0=1\), the cumulative mass of the diameter-gap measure through rank
\(k\) is exactly \((b_k+1)/N_n\).  Its distribution function differs from
\(k/n\) by \(O(1/n)\), uniformly in \(k\) and in the choice of
\(M<p<2M\).  This includes the endpoint correction.  For every fixed
\(\ell\), the normalized gap
measure therefore converges to Lebesgue measure on \([0,1]\).

For \(f(u)=u(1-u)\),

\[
\int_0^1f=\frac16,
\qquad
\int_0^1f^2=\frac1{30},
\]

so

\[
\boxed{\operatorname{Var}_{\nu_M}f\longrightarrow\frac1{180}.}
\tag{8}
\]

The limiting covariance matrix of \(z=(f,u)\) has

\[
\operatorname{Var}f=1/180,
\quad \operatorname{Cov}(f,u)=0,
\quad \operatorname{Var}u=1/12.
\]

For the transition \(m=M/2\to M\), define explicitly
\(Q_m=\mathcal M_M-B\mathcal M_mB^{\mathsf T}\), using each prefix's own
diameter modulus.  Then \(N_m/N_M\to1/2\), while the
\((1,1)\)-entry of \(BRB^{\mathsf T}\) is again \(1/180\).  The exact matrix
update then gives

\[
\boxed{\frac{Q_{m,00}}{N_M}\longrightarrow\frac1{360}.}
\tag{9}
\]

## 5. The local signed birth shell stays positive

This is a different object from the same-modulus signed shell.  To define the
latter, evaluate both prefixes at the final containing modulus \(N_M\), and put

\[
L_m=
\frac{
\operatorname{Var}C_{N_M}(A_M)
-\operatorname{Var}C_{N_M}(A_m)}{M^4}.
\]

The full term tends to \(1/180\) by (8).  For the old prefix, asymptotically
half the modulus is the outside gap with load zero; the other half carries a
uniform rank variable and load \(m^2f=M^2f/4\).  Therefore

\[
\frac{\operatorname{Var}C_{N_M}(A_m)}{M^4}
\longrightarrow
\frac1{32}\int_0^1f^2
-\frac1{64}\left(\int_0^1f\right)^2
=\frac7{11520}.
\]

It follows that

\[
\boxed{L_m\longrightarrow\frac1{180}-\frac7{11520}
=\frac{19}{3840}>0.}
\tag{10}
\]

The exact number of born edges is
\((3M^2-2M)/8\), and each individual cyclic-arc indicator has variance at
most \(1/4\).  Thus the normalized born diagonal is at most
\(3/(32M^2)-1/(16M^3)=O(M^{-2})\).  The ordered off-diagonal part of the same
birth shell also tends to \(19/3840\).

## 6. Exact logical consequence

For every fixed \(L\), (6)--(10) give arbitrarily large Sidon windows whose
last \(L+1\) dyadic prefixes share a critical envelope, but whose newest
normalized matrix innovation and signed birth shell stay bounded below by a
positive constant.  The same calculation applies at every fixed transition
inside the window, so fixed-window averaging does not help.  Therefore no
**uniform finite-window theorem using only
those prefixes, their Sidon property, and their critical compatibility** can
force either local quantity to be \(o(1/j)\).

This strengthens the isolated three-rank obstruction.  It still does not
exclude a bounded-depth formula whose hypotheses include verified
embeddability into one infinite globally critical Sidon sequence, because the
finite Erdős--Turán windows are not shown to have such extensions.  Nor does
it refute an amortized inequality using an unbounded history.

The remaining possibility is precise:

> Repetition of high innovations at many widely separated scales of one
> global critical Sidon sequence must force a collision between cross-block
> contiguous sums.

Internal block-spectrum disjointness gives only (5); a solution must use
cross-scale cross differences.  `fixed_depth_no_go.py` and
`test_fixed_depth_no_go.py` audit the exact finite quantities behind
(8)--(10).

# Gap-measure dynamics and the optimized two-step lower bound

Date: 2026-08-28  
Status: rigorous exact update, positive matrix potential, sharper critical
lower bound, and scalar no-go examples.  The required upper budget remains
open.

## 1. Exact dyadic update

For an \(m\)-mark prefix at its diameter modulus, define the probability
measure

\[
\nu_m=\frac1{N_m}\sum_{k=0}^{m-1}h_k\delta_{k/m},
\qquad h_0=1,
\]

and put \(f(u)=u(1-u)\).  Then

\[
\frac{\operatorname{Var}C_{N_m}(A_m)}{m^4}
=\operatorname{Var}_{\nu_m}f.
\tag{1}
\]

Let the next prefix have \(2m\) marks, set

\[
N=N_m,\quad N'=N_{2m},\quad G=N'-N,\quad T(u)=u/2,
\]

and let \(\sigma\) be the probability measure formed by the new gap weights
\(h_m,\ldots,h_{2m-1}\) at locations \(k/(2m)\).  Then exactly

\[
\boxed{\nu_{2m}=\frac N{N'}T_*\nu_m+\frac G{N'}\sigma.}
\tag{2}
\]

The mixture-variance formula gives

\[
\operatorname{Var}_{\nu_{2m}}f
=\frac N{N'}\operatorname{Var}_{\nu_m}(f\circ T)
+\frac G{N'}\operatorname{Var}_\sigma f
+\frac{NG}{N'^2}(\mu_{\rm old}-\mu_{\rm new})^2.
\tag{3}
\]

Thus all three contributions are nonnegative, but the old scalar test changes
from \(f\) to \(f\circ T\).

## 2. Diameter-compensated covariance matrix

Because

\[
f(u/2)=\frac{f(u)+u}{4},
\]

put

\[
z(u)=\binom{f(u)}u,
\qquad
B=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix},
\qquad
\mathcal M_m=N_m\operatorname{Cov}_{\nu_m}z.
\]

The vector mixture-covariance identity refines (3) to

\[
\boxed{
\mathcal M_{2m}
=B\mathcal M_mB^{\mathsf T}
+G\operatorname{Cov}_\sigma z
+\frac{NG}{N'}
(B\bar z_{\nu_m}-\bar z_\sigma)
(B\bar z_{\nu_m}-\bar z_\sigma)^{\mathsf T}.
}
\tag{4}
\]

In particular,

\[
\boxed{\mathcal M_{2m}\succeq B\mathcal M_mB^{\mathsf T}.}
\tag{5}
\]

This is a genuine positive cross-prefix potential.  It does not close on the
single \(f\)-coordinate because \(B\) rotates that direction toward \(u\).

The iteration is also explicit:

\[
B^r=
\begin{pmatrix}
4^{-r}&2^{-r}-4^{-r}\\
0&2^{-r}
\end{pmatrix},
\]

and, writing \(Q_t\) for the PSD innovation born in the update
\(2^tm\to2^{t+1}m\),

\[
\mathcal M_{2^rm}
=B^r\mathcal M_m(B^{\mathsf T})^r
+\sum_{t=0}^{r-1}B^{r-1-t}Q_t(B^{\mathsf T})^{r-1-t}.
\tag{5a}
\]

Thus every innovation remains positive after transport.  Formula (5a)
identifies the exact quantities whose accumulated *upper* budget is missing.

## 3. Optimized distinct-adjacent-gap bound

Let \(A_M\) be increasing, where \(M=4m\), \(m\ge4\), and \(4\mid m\).
Assume that its first \(m\) marks form a Sidon ruler.  This is weaker than
requiring the full \(M\)-mark prefix to be Sidon, although that stronger
hypothesis is the one used in the application.  The \(m-1\) adjacent gaps of
the old prefix are distinct positive integers.  Select the largest

\[
q=\frac{3m}{4}
\]

of them.  Every selected gap is at least \(m/4\).  Their indices are \(q\)
distinct integers, and for every real \(x\),

\[
\sum_{k\in S}(k-x)^2\ge\frac{q(q^2-1)}{12};
\]

the minimum is attained by consecutive indices centered at their mean.
Consequently

\[
\boxed{
\operatorname{Var}_{\nu_m}U
\ge\frac{9m^2-16}{1024N_m}.
}
\tag{6}
\]

Now pass two dyadic steps to \(M=4m\).  The old component has mass
\(N_m/N_M\) and is mapped by \(u\mapsto u/4\).  Since

\[
\frac d{du}f(u/4)=\frac14-\frac u8\ge\frac18
\qquad(0\le u\le1),
\]

the pairwise variance formula implies

\[
\operatorname{Var}_{\nu_m}(f(U/4))
\ge\frac1{64}\operatorname{Var}_{\nu_m}U.
\]

Keeping only the old component in the mixture variance and applying (6)
gives the optimized two-step theorem

\[
\boxed{
\operatorname{Var}_{\nu_M}f
\ge\frac{9m^2-16}{65536N_M}
=\frac{9M^2-256}{1048576N_M}.
}
\tag{7}
\]

Only distinct adjacent gaps were used; the stronger condition that every
contiguous gap sum is distinct remains unused.

More generally, after \(r\ge2\) steps,

\[
\frac d{du}f(u/2^r)
\ge a_r:=2^{-r}(1-2^{1-r}),
\]

so the same argument gives

\[
\operatorname{Var}_{\nu_M}f
\ge
\frac{(1-2^{1-r})^2(9M^2-16\cdot4^r)}
     {1024\cdot16^rN_M},
\qquad M=2^rm.
\tag{7a}
\]

The asymptotic coefficient decreases strictly for \(r\ge2\): the ratio from
depth \(r\) to \(r+1\) is

\[
\frac1{16}
\left(\frac{1-2^{-r}}{1-2^{1-r}}\right)^2<1.
\]

Hence the two-step choice is optimal within this entire co-Lipschitz aging
family; searching deeper scalar aging cannot improve the leading constant.

Under the hypothetical critical envelope
\(N_M\le2CM^2\log M\), (7) yields

\[
\boxed{
\frac{\operatorname{Var}C_{N_M}(A_M)}{M^4}
\ge\frac{9-256/M^2}{2097152C\log M}.
}
\tag{8}
\]

For the dyadic prefixes \(m_j=2^j\), put \(N_j=N_{m_j}\).  Choose \(j_0\)
so that \(m_j\ge16\) and the critical envelope holds for every \(j\ge j_0\).
Then

\[
\boxed{
\sum_{j=j_0}^{J}\frac{\operatorname{Var}C_{N_j}(A_{m_j})}{m_j^4}
\ge\frac{9+o(1)}{2097152C\log2}\log J.
}
\tag{9}
\]

This constant is sixteen times the direct eight-block constant in the earlier
proof, while retaining the same stronger \(m^{-4}\) weight.

## 4. Why the new weight materially tightens the upper problem

Write the ordered cyclic-arc expansion at scale \(j\) as

\[
V_{N_j}=\sum_{p,q}
\operatorname{Cov}(\mathbf 1_{B_{p,j}},\mathbf 1_{B_{q,j}}),
\]

where \(B_{p,j}\) is the boundary arc of the oriented pair \(p\).  By
Cauchy--Schwarz, one fixed ordered interaction has covariance of absolute
value at most \(1/4\), hence contributes at most \(1/(4m_j^4)\) after the
new normalization.  Its dyadic tail from birth scale \(s\) is at most

\[
\frac14\sum_{j\ge s}m_j^{-4}=\frac4{15m_s^4}.
\]

Only \(O(m_s^4)\) ordered interactions are born at scale \(s\), so the crude
absolute loss is now \(O(1)\) per shell, rather than \(O(m_s)\) for the old
\(m^{-3}\) weight.  Summing still gives only \(O(J)\); the missing theorem is
an \(o(\log J)\) signed or structural upper budget.

## 5. Scalar compensations fail

The matrix in (4) is needed for an exact one-step positive-semidefinite
recursion: one-step scalar aging can move in either direction.  Exact Golomb
fixtures are

\[
A=(0,1,4,6):\quad
V=\frac3{448},\quad V_{\rm aged}=\frac{297}{50176}<V,
\]

and

\[
A=(0,1,3,7):\quad
V=\frac{87}{16384},\quad
V_{\rm aged}=\frac{1615}{262144}>V.
\]

There is no positive universal one-step lower factor.  Start with any
\((r-2)\)-mark Golomb base of diameter \(D\), and append adjacent gaps
\(H,H+c\), where \(H>D\) and \(c>D\).  The four difference ranges

\[
[1,D],\quad[H,H+D],\quad\{H+c\},\quad
[2H+c,2H+c+D]
\]

are disjoint, so the resulting \(r\)-mark ruler is Golomb.  As
\(H\to\infty\), its gap measure concentrates equally at
\(u_1=1-2/r\) and \(u_2=1-1/r\), and direct subtraction gives

\[
\frac{\operatorname{Var}f(U/2)}{\operatorname{Var}f(U)}
\longrightarrow\frac9{16(r-3)^2}.
\]

Letting \(r\to\infty\) rules out every positive universal one-step factor.
This does not affect the two-step scalar lower bound (7), which uses the
uniform derivative bound for \(f(u/4)\).

There is no finite universal upper factor either.  The gap family
\((H,1,H+2)\) is Golomb for \(H\ge2\).  Its original measure concentrates at
the symmetric locations \(1/4,3/4\), where \(f=3/16\), so the original
variance is \(O(H^{-1})\).  After aging, the two limiting values are
\(7/64\) and \(15/64\), and the variance tends to \(1/256\).  Thus the
aged/original variance ratio tends to infinity.

Nor can a fixed scalar diameter power repair monotonicity.  For the old prefix
\(A_2=(0,D-3)\) and full prefix
\(A_4=(0,D-3,D-2,D)\), \(D\ge7\), put
\(N_2=D-2\) and \(N_4=D+1\).  For every fixed real \(\alpha\), exact algebra
gives

\[
R_{D,\alpha}
=\frac{N_4^\alpha\operatorname{Var}_{\nu_4}f}
       {N_2^\alpha\operatorname{Var}_{\nu_2}f}
=\frac{5D+3}{8(D-3)}
 \left(\frac{D+1}{D-2}\right)^{\alpha-2}
\longrightarrow\frac58<1.
\]

Thus no scalar \(N^\alpha\operatorname{Var}_\nu f\) is universally
nondecreasing.  The exact surviving one-step object is the covariance matrix,
not a scalar diameter power.

## 6. Scope

Equations (2)--(9) are rigorous.  They improve and structurally explain the
critical lower accumulation, but do not resolve Problem #1191: no matching
\(o(\log J)\) upper budget is known.  The finite aging searches and fixtures
are falsification evidence only.  `gap_measure_dynamics.py` and
`test_gap_measure_dynamics.py` implement the exact rational identities.

# Fixed-modulus doubled-prefix variance is not monotone

Date: 2026-08-28  
Status: rigorous counterexample, infinite counterfamily, and analytic global
minimality proof for comparisons \(A_r\subset A_{2r}\).  General
non-doubling extensions can fail earlier and are not covered by the minimality
statement.

## 1. Exact same-modulus formula

Let \(A_M=\{a_1<\cdots<a_M\}\), let \(N>a_M-a_1\), and set
\(g_k=a_{k+1}-a_k\).  For the first \(m\) marks, the crossing load is
\(k(m-k)\) on the \(g_k\) phases of the kth internal gap and zero on all
remaining phases.  Therefore

\[
\boxed{
\operatorname{Var}_NC(A_m)
=\frac1N\sum_{k=1}^{m-1}g_kk^2(m-k)^2
-\frac1{N^2}\left(\sum_{k=1}^{m-1}g_kk(m-k)\right)^2.
}
\tag{1}
\]

## 2. Minimal Sidon counterexample for a doubled prefix

Take

\[
N=40,qquad A_4=\{0,20,21,39\},qquad A_2=\{0,20\}.
\]

The positive differences are

\[
\{1,18,19,20,21,39\},
\]

so \(A_4\) is Sidon.  The two-point load has twenty zeros and twenty ones,
hence

\[
\operatorname{Var}_{40}C(A_2)=\frac14.
\]

For \(A_4\), the phase weights at load levels \(0,3,4\) are respectively
\(1,38,1\).  Thus

\[
\operatorname{Var}_{40}C(A_4)=\frac{99}{400}
<\frac14,
\]

an exact decrease of \(1/400\).

## 3. Infinite Sidon counterfamily

For every \(N\ge40\), put

\[
x=\lceil N/2\rceil,
\qquad A_N=\{0,x,x+1,N-1\}.
\]

For even \(N=2t\), its differences are

\[
\{1,t-2,t-1,t,t+1,2t-1\};
\]

for odd \(N=2t+1\), they are

\[
\{1,t-2,t-1,t+1,t+2,2t\}.
\]

They are distinct for \(N\ge40\).  Exact load counts give

\[
\operatorname{Var}_NC(A_2)=\frac{\lfloor N^2/4\rfloor}{N^2},
\qquad
\operatorname{Var}_NC(A_4)=\frac{10N-4}{N^2}.
\tag{2}
\]

The second is strictly smaller for every \(N\ge40\), and tends to zero while
the first tends to \(1/4\).  Consequently no universal positive constant
\(c\) can satisfy \(V(A_{2r})\ge cV(A_r)\) at a common containing modulus.

## 4. Why modulus 40 is globally minimal for \(A_r\subset A_{2r}\)

For four marks, write the phase counts as \(w\ge1\) at level 0,
\(p=g_1+g_3\ge2\) at level 3, and \(y=g_2\ge1\) at level 4.  Weighted
polarization gives

\[
N^2\operatorname{Var}C(A_4)=9wp+16wy+py.
\]

For fixed \(p\), this is concave in \(w\), and after checking the endpoint
cases it is concave in \(p\).  Its sharp minimum is

\[
\boxed{\operatorname{Var}_NC(A_4)\ge\frac{10N-4}{N^2}.}
\tag{3}
\]

The two-point variance is at most \(1/4\).  For \(4\le N\le39\), the right
side of (3) is at least \(1/4\), so no four-mark counterexample exists.

For a prefix of \(r\ge3\) marks and a full set of \(2r\) marks, the mandatory
level theorem and Popoviciu's range bound give

\[
\operatorname{Var}_NC(A_{2r})
\ge\frac{2r(4r^2-1)(4r^2+11)}{180N},
\]

and

\[
\operatorname{Var}_NC(A_r)
\le\frac14\left\lfloor\frac{r^2}{4}\right\rfloor^2
\le\frac{r^4}{64}.
\]

At \(N\le39\), the first bound dominates the last for every \(r\ge3\), since

\[
64(4r^2-1)(4r^2+11)-3510r^3\ge0;
\]

it is positive at \(r=3\) and increasing thereafter.  The case \(r=1\) is
trivial because the prefix variance is zero.  Hence \(N=40\) is globally
minimal over all doubled-prefix sizes.

This qualifier is essential.  For a general non-doubling inclusion, the
Sidon example

\[
N=11,\qquad \{0,3,4\}\subset\{0,3,4,10\}
\]

already decreases the variance from \(112/121\) to \(106/121\).

## 5. What survives

The inclusion \(A\subseteq B\) gives pointwise \(C_B\ge C_A\ge0\), so the
uncentered second moment is monotone:

\[
\frac1N\sum_rC_B(r)^2\ge\frac1N\sum_rC_A(r)^2.
\]

Equivalently,

\[
\operatorname{Var}C_B\ge
\operatorname{Var}C_A+\overline C_A^{,2}-\overline C_B^{,2}.
\]

The counterfamily works because the increase of the mean is large enough to
outweigh the increase of the second moment after centering.  Thus the finite
survival of H6 cannot be proved through fixed-modulus variance monotonicity.

## 6. Verification

`prefix_monotonicity_certificate_2026_08_28.py` exhausts all positive gap
configurations for doubled prefixes with \(r=1\), with \(r=2,N\le40\), and
with \(r=3,N\le39\), and
checks the infinite family through \(N=100\).  Formula (1) is compared with an
independent literal cyclic-load oracle throughout the four-mark scan.  These
finite checks support the analytic minimality proof above; they do not replace
it.

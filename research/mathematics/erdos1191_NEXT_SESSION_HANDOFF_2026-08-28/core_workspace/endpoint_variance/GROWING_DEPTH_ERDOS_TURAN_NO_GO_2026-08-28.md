# Growing-depth Erdős--Turán no-go

Date: 2026-08-28  
Status: rigorous obstruction to local-history upper budgets of logarithmically
growing depth.  This is not an infinite globally critical Sidon sequence and
does not resolve Erdős Problem #1191.

## 1. Statement

Let (J\ge8), put

\[
M=2^J,
\qquad
L_J=\lfloor\log_2J\rfloor-2,
\]

and choose a prime (M\le p<2M), whose existence follows from Bertrand's
postulate.  Define the (M)-mark Erdős--Turán
ruler

\[
b_i=2pi+(i^2\bmod p),
\qquad 0\le i<M.
\tag{1}
\]

For (0\le\ell\le L_J), let (A_{J,\ell}) be its first
(n_{J,\ell}=M/2^\ell) marks and put

\[
N_{J,\ell}=\operatorname{diam}(A_{J,\ell})+1.
\]

Then every prefix in this growing final window satisfies the same critical
envelope

\[
\boxed{N_{J,\ell}\le2n_{J,\ell}^2\log n_{J,\ell}.}
\tag{2}
\]

If (\nu_{J,\ell}) is its diameter-gap probability measure and
(f(u)=u(1-u)), then uniformly over the whole window,

\[
\operatorname{Var}_{\nu_{J,\ell}}f=\frac1{180}+o(1).
\tag{3}
\]

Consequently

\[
\boxed{
\sum_{\ell=0}^{L_J}
\operatorname{Var}_{\nu_{J,\ell}}f
=\frac{\log J}{180\log2}+O(1).
}
\tag{4}
\]

For every adjacent transition (n\to2n) inside the window, let (Q_n) be
the own-diameter covariance-matrix innovation.  Uniformly,

\[
\frac{(Q_n)_{00}}{N_{2n}}=\frac1{360}+o(1),
\tag{5}
\]

and the same-final-modulus normalized birth shell is

\[
\frac{
 \operatorname{Var}C_{N_{2n}}(A_{2n})
 -\operatorname{Var}C_{N_{2n}}(A_n)
}{(2n)^4}
=\frac{19}{3840}+o(1).
\tag{6}
\]

The errors in (3), (5), and (6) are uniform over all (L_J+1) prefixes.
In particular their sums over the window are respectively

\[
\frac{L_J+1}{180}+o(1),
\qquad
\frac{L_J}{360}+o(1),
\qquad
\frac{19L_J}{3840}+o(1).
\tag{7}
\]

## 2. Sidon property

Write (r_i=i^2\bmod p\), so (0\le r_i<p).  If two positive
differences from (1) are equal, then

\[
2p\bigl((j-i)-(v-u)\bigr)
=(r_v-r_u)-(r_j-r_i).
\]

The right side has absolute value strictly below (2p), so the two rank
increments are equal, say to (d).  Equality of the residual parts, reduced
modulo (p), then gives

\[
2d(i-u)\equiv0\pmod p.
\]

Here (0<d<M\le p), and (p) is odd.  Hence (i=u), and the two pairs are
identical.  Thus (1) is a Sidon ruler.

## 3. The logarithmically growing critical window

For a prefix of (n=M/2^\ell) marks,

\[
N_n=b_{n-1}+1<2pn<4Mn=2^{\ell+2}n^2.
\tag{8}
\]

It is therefore enough to prove

\[
2^{\ell+1}\le\log n=(J-\ell)\log2.
\tag{9}
\]

We use only the elementary strict inequality (\log2>2/3).  For
(J\ge8), one has (L_J\le J/4), while

\[
2^{\ell+1}\le2^{L_J+1}\le J/2
\le\frac23(J-L_J)\le\frac23(J-\ell).
\tag{10}
\]

Equations (9), (8), and (10) prove (2).  Notice the quantifier strength:
the depth is not fixed.  It tends to infinity like

\[
L_J=\frac{\log J}{\log2}+O(1).
\tag{11}
\]

## 4. Uniform gap-measure convergence

For a prefix of (n) marks, write

\[
N_n=2p(n-1)+r_{n-1}+1.
\]

With (h_0=1) and the usual adjacent gap weights, the cumulative mass at
the rank grid point (k/n) is exactly

\[
F_n(k/n)=\frac{b_k+1}{N_n}.
\]

Direct subtraction gives

\[
n(b_k+1)-kN_n
=n(r_k+1)+k(2p-r_{n-1}-1).
\tag{12}
\]

The right side lies between (0) and (3np), while (N_n\ge pn) for
(n\ge2).  Hence

\[
0\le F_n(k/n)-\frac kn\le\frac3n.
\]

Between consecutive grid points the uniform distribution function moves by
at most (1/n).  Therefore the exact Kolmogorov bound is

\[
\boxed{\|F_n-F_{[0,1]}\|_\infty\le\frac4n.}
\tag{13}
\]

The smallest prefix in the window has

\[
n_{\min}=2^{J-L_J}=\Theta\!\left(\frac{2^J}{J}\right)
\longrightarrow\infty.
\]

Thus (13) is uniform over all (0\le\ell\le L_J).  Integration by parts
for each bounded-variation polynomial in
(1,u,u^2,f,f^2,uf) gives uniform convergence of every entry of
\(\operatorname{Cov}_{\nu_n}(f,u)\).  Since

\[
\int_0^1f=\frac16,
\qquad
\int_0^1f^2=\frac1{30},
\]

(3) follows.  Its per-prefix error is (O(1/n_{\min})), so multiplying by
(L_J+1=O(\log J)) still gives (o(1)).  This proves (4).

## 5. Uniform transition limits

For adjacent prefixes (n\to2n), uniformly over the growing window,

\[
\frac{N_n}{N_{2n}}=\frac12+O(1/n_{\min}).
\tag{14}
\]

The limiting covariance matrix for (z=(f,u)) is

\[
R=\begin{pmatrix}1/180&0\\0&1/12\end{pmatrix}.
\]

Because the old component is transported by

\[
B=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix},
\]

the normalized innovation tends uniformly to

\[
R-\frac12BRB^{\mathsf T}
=
\begin{pmatrix}
1/360&-1/192\\
-1/192&7/96
\end{pmatrix}.
\tag{15}
\]

Its determinant is (97/552960>0), and (5) is its first diagonal entry.

For (6), evaluate the old (n)-mark prefix at the final modulus (N_{2n}).
Put (r=N_n/N_{2n}\).  Its normalized variance is exactly

\[
\frac r{16}\,\mathbb E_{\nu_n}f^2
-\frac{r^2}{16}\bigl(\mathbb E_{\nu_n}f\bigr)^2.
\tag{16}
\]

Using (r\to1/2), this tends to

\[
\frac1{32\cdot30}-\frac1{64\cdot36}=\frac7{11520}.
\]

The full normalized variance tends to (1/180), so their difference is

\[
\frac1{180}-\frac7{11520}=\frac{19}{3840}.
\]

All errors are (O(1/n_{\min})); summing over (L_J) transitions proves
(7).

## 6. Exact consequence for the remaining proof route

At terminal dyadic index (J), the desired global theorem would give

\[
\sum_{j\le J}\operatorname{Var}_{\nu_j}f=o(\log J).
\]

The finite family above has only its final (L_J+1\asymp\log J) prefixes,
yet those prefixes already contribute the main-order quantity in (4).  The
finite-horizon adjoint identity also shows that its adjoint-weighted
innovation sum is (L_J/180-O(1)): the initial boundary term is uniformly
bounded.

Therefore no theorem whose hypotheses inspect only the last

\[
\boxed{\lfloor\log_2J\rfloor-1}
\]

dyadic prefixes, their Sidon property, and their common critical envelope can
prove the required (o(\log J)) conclusion uniformly.  This closes not only
fixed-depth locality, but logarithmically growing locality on the scale-index
axis.

The caveat is essential.  For every terminal (J) the construction chooses
a new finite ruler and a new prime.  Although ordinary Sidon extension to an
infinite sequence is easy, nothing here gives an extension that keeps the
same critical envelope at all sufficiently large prefixes.  A valid solution
may still use:

1. global embeddability into one infinite sequence;
2. history reaching more than (\asymp\log J) dyadic scales behind the
   terminal prefix; or
3. a global invariant not determined by the final window.

`growing_depth_no_go.py`, `test_growing_depth_no_go.py`, and the dated JSON
certificate audit the exact depth arithmetic, Kolmogorov bound, variances,
innovations, and same-modulus shells.  The finite checks support the algebra;
the asymptotic theorem is the proof above.

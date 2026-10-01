# Sidon block variance and a positive multiscale functional

Date: 2026-08-28  
Status: the identities and inequalities labelled **Theorem** below are proved.
They do **not** resolve Erdős Problem #1191.  The final amortized upper bound is
an explicit open obligation.

## 1. Diameter-regime positive gap identity

Let

\[
A_m=\{a_1<\cdots<a_m\},\qquad D_m=a_m-a_1,
\qquad N_m=D_m+1.
\]

Set

\[
h_0=1,qquad h_k=a_{k+1}-a_k\quad(1\le k<m),
\qquad x_m(k)=k(m-k).
\]

At modulus \(N_m\), the crossing load is zero on the unique phase outside
\([a_1,a_m]\), and is \(x_m(k)\) on exactly \(h_k\) phases.  Weighted-variance
polarization therefore gives the exact identity

\[
\boxed{
V_m:=\operatorname{Var}C_{N_m}
=\frac1{N_m^2}\sum_{0\le k<\ell<m}
h_kh_\ell\bigl(x_m(k)-x_m(\ell)\bigr)^2.
}
\tag{1}
\]

Since

\[
x_m(\ell)-x_m(k)=(\ell-k)(m-k-\ell),
\]

(1) is equivalently

\[
\boxed{
V_m=\frac1{N_m^2}\sum_{0\le k<\ell<m}
h_kh_\ell(\ell-k)^2(m-k-\ell)^2.
}
\tag{2}
\]

Every summand is nonnegative.  This removes the sign obstruction present in
the earlier pairwise covariance kernel.

## 2. Sidon block-variance theorem

**Theorem.**  If \(A_m\) is Sidon and \(m=8q\) with \(q\ge2\), then

\[
\boxed{
V_m\ge \frac{9D_mq^5(q-1)}{16N_m^2}
\ge \frac{9m^6}{16\,777\,216N_m}.
}
\tag{3}
\]

### Proof

Partition the internal gap indices into

\[
I_0=\{1,\ldots,q-1\},
\qquad
I_t=\{tq,\ldots,(t+1)q-1\}\quad(1\le t\le7),
\]

and put \(H_t=\sum_{k\in I_t}h_k\).  These blocks partition
\(\{1,\ldots,8q-1\}\), so some \(t\) has \(H_t\ge D_m/8\).

Choose

\[
s(t)=
\begin{cases}
3,&t\in\{0,1,6,7\},\\
0,&t\in\{2,3,4,5\}.
\end{cases}
\]

A consecutive \(r\)-mark subset of a Sidon ruler has \(\binom r2\) distinct
positive integer differences, all bounded by its span.  Consequently

\[
H_0=a_q-a_1\ge\binom q2,
\qquad
H_3=a_{4q}-a_{3q}\ge\binom{q+1}{2}\ge\binom q2.
\tag{4}
\]

Direct evaluation of \(x_m(k)=k(8q-k)\) on these index blocks gives

\[
\begin{array}{c|cccccccc}
I_t&t=0&t=1&t=2&t=3&t=4&t=5&t=6&t=7\\ \hline
x_m(k)&<7q^2&<12q^2&\ge12q^2&\ge15q^2&>15q^2&\ge12q^2&\le12q^2&\le7q^2.
\end{array}
\]

Thus every level from \(I_t\) is separated from every level in
\(I_{s(t)}\) by at least \(3q^2\).  Retaining only those nonnegative terms in
(1), then using (4), yields

\[
V_m\ge
\frac{H_tH_{s(t)}(3q^2)^2}{N_m^2}
\ge\frac{D_m}{8}\frac{q(q-1)}2\frac{9q^4}{N_m^2},
\]

which is the first inequality in (3).  Finally,
\(D_m=N_m-1\ge N_m/2\), \(q-1\ge q/2\), and \(q=m/8\), proving the second.
\(\square\)

## 3. Critical consequence

Suppose, toward the negation of Question 1, that for some fixed \(C>0\),

\[
a_m\le C m^2\log m
\]

for all sufficiently large \(m\).  After translation,
\(N_m=D_m+1\le2Cm^2\log m\) for all sufficiently large \(m\).  For dyadic
\(m_j=2^j\), (3) gives

\[
\frac{V_{m_j}}{m_j^4}
\ge \frac{9}{33\,554\,432\,C\log m_j}.
\]

For dyadic scales starting at \(j_0\ge4\), and after increasing \(j_0\) so
that the critical envelope holds at every retained scale, the strengthened
critical functional

\[
\mathcal G_J=\sum_{j=j_0}^J\frac{V_{m_j}}{m_j^4}
\]

satisfies

\[
\boxed{
\mathcal G_J\ge
\frac{9}{33\,554\,432\,C\log2}
\sum_{j=j_0}^J\frac1j
=\Omega_C(\log J).
}
\tag{5}
\]

The previous proof state only reached the weight \(m^{-3}\); (5) gains a full
power of \(m\).

## 4. Exact positive birth-shell expansion

For an infinite sequence, retain the global gaps

\[
h_0=1,\qquad h_\ell=a_{\ell+1}-a_\ell\quad(\ell\ge1),
\]

and let \(s(\ell)=\min\{j\ge j_0:\ell<m_j\}\).  Exchanging the finite sums in
(2) gives

\[
\boxed{
\mathcal G_J
=\sum_{0\le k<\ell<m_J}h_kh_\ell\Lambda_J(k,\ell),
}
\tag{6}
\]

where

\[
\boxed{
\Lambda_J(k,\ell)=\sum_{j=s(\ell)}^J
\frac{(\ell-k)^2(m_j-k-\ell)^2}{m_j^4N_j^2}\ge0.
}
\tag{7}
\]

The only birth condition is \(\ell<m_j\).  There is no short-pair truncation
because \(N_j=D_{m_j}+1\).

For \(j\ge s=s(\ell)\),

\[
\frac{(\ell-k)^2(m_j-k-\ell)^2}{m_j^4N_j^2}
\le4^{-(j-s)}\frac{(\ell-k)^2}{m_s^2N_s^2},
\]

so

\[
\Lambda_J(k,\ell)\le\frac43
\frac{(\ell-k)^2}{m_s^2N_s^2}.
\tag{8}
\]

Let \(H_{j_0}=D_{m_{j_0}}\) and
\(H_s=D_{m_s}-D_{m_{s-1}}\) for \(s>j_0\).  Grouping (6) by the birth shell
and using, for each fixed \(\ell\) with \(s(\ell)=s\), the crude estimate

\[
\sum_{0\le k<\ell}h_k(\ell-k)^2
\le m_s^2\sum_{k<\ell}h_k\le m_s^2N_s
\tag{9}
\]

gives

\[
\mathcal G_J\le\frac43\sum_{s=j_0}^J\frac{H_s}{N_s}
\le\frac43\log N_J.
\tag{10}
\]

Here the last inequality uses
\((N_s-N_{s-1})/N_s\le\log(N_s/N_{s-1})\), together with the analogous
initial inequality, so the logarithms telescope.  Under the critical
envelope, (10) is only \(O(J)\).  To contradict (5), the
needed estimate is

\[
\boxed{\mathcal G_J=o(\log J).}
\tag{11}
\]

A principal explicit loss is (9); (8) also discards kernel geometry.  Any
successful proof must improve their total effect using compatibility across
many nested prefixes.

## 5. Rigorous one-shell obstruction

Let \(B=\{b_1<\cdots<b_m\}\) be any Sidon ruler with \(4\mid m\), diameter
\(R\), and \(G=R+1\).  Put \(r=m/4\), \(s=m/2\), and

\[
\alpha_i=
\begin{cases}
0&i\le r,\\
1&r<i\le s,\\
2&s<i\le m,
\end{cases}
\qquad a_i=b_i+G\alpha_i.
\]

The difference ranges for rank increments 0, 1, and 2 are respectively

\[
[1,R],\quad[R+2,2R+1],\quad[2R+3,3R+2],
\]

so they are disjoint; equality within a range reduces to equality of two
differences of \(B\).  Thus \(A\) is Sidon.  Its modulus is \(N_A=3G\), while
the two rank-boundary gaps obey \(h_r,h_s\ge G\).  Since

\[
|x_m(s)-x_m(r)|=m^2/16,
\]

one term of (1) yields

\[
\boxed{\frac{V_m}{m^4}\ge\frac1{2304}.}
\tag{12}
\]

Taking, for prime \(p\in[m,2m)\), the Erdős--Turán base ruler

\[
b_i=2pi+(i^2\bmod p),\qquad0\le i<m,
\]

keeps the lifted diameter \(O(m^2)\).  Therefore arbitrarily large isolated
finite Sidon rulers with \(N=O(m^2)\) can have constant normalized energy.
This rigorously rules out any uniform pointwise conclusion
\(V_m/m^4=o(1)\) derived solely from the Sidon property and the one-prefix
diameter bound.  It does **not** rule out a bounded-depth theorem that uses
actual compatibility with neighboring prefixes or embeddability into one
global critical sequence.

## 6. Remaining theorem target

With

\[
\nu_j=\frac1{N_j}\sum_{k=0}^{m_j-1}h_k\,\delta_{k/m_j},
\]

(1) can be viewed as a weighted variance of \(u(1-u)\).  The unresolved target
is the long-range statement

\[
\sum_{j\le J}\operatorname{Var}_{\nu_j}(u(1-u))=o(\log J).
\]

Single-scale Sidon structure alone is insufficient by (12).  A future proof
must add compatibility information from neighboring or more distant prefixes;
(12) does not itself exclude every bounded-depth compatible inequality.

## 7. Machine checks

The exact implementations are:

- `sidon_block_variance.py`;
- `test_sidon_block_variance.py`;
- `sidon_block_variance_certificate_2026_08_28.py`.

They compare (1) against the independent crossing-load computation, verify the
block witness and constant chain, check (6) term by term, and test the lifted
obstruction.  These checks support the algebra; they are not substitutes for
the proof above.

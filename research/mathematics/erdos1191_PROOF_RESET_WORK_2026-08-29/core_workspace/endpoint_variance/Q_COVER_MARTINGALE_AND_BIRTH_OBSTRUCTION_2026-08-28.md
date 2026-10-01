# Exact q-cover martingale identity and the birth-edge obstruction

Date: 2026-08-28  
Status: exact theorem plus rigorous obstructions.  This route does not yet
provide the missing critical multiscale budget.

## 1. Exact cover projection

Let \(N,q\in\mathbb Z\) with \(N,q\ge2\), and use normalized cyclic
\(L^2\).  Let \(\mathcal P\) be a finite multiset of
oriented pairs \(p=(a,b)\), with \(0<d_p=b-a<qN\), and define

\[
C_M^{\mathcal P}(x)=\sum_{p\in\mathcal P}
1_{\{a+1,\ldots,b\}\bmod M}(x).
\]

Write \(d_p=k_pN+s_p\), \(0\le s_p<N\), and let

\[
R_N^{\mathcal P}(r)=\sum_{p:s_p>0}
1_{\{a+1,\ldots,a+s_p\}\bmod N}(r).
\]

**Theorem.**

\[
\boxed{
q^2\operatorname{Var}_{qN}C_{qN}^{\mathcal P}
=\operatorname{Var}_NR_N^{\mathcal P}+\mathcal I_{N,q}(\mathcal P),
}
\tag{1}
\]

where

\[
\boxed{
\mathcal I_{N,q}(\mathcal P)=\frac1{qN}
\sum_{r\bmod N}\sum_{t=0}^{q-1}
\left(qC_{qN}^{\mathcal P}(r+tN)
-\sum_{u=0}^{q-1}C_{qN}^{\mathcal P}(r+uN)\right)^2\ge0.
}
\tag{2}
\]

### Proof

For one pair, its \(k_pN+s_p\) consecutive residues contain \(k_p\)
representatives of every residue modulo \(N\), with one extra representative
exactly on the residual arc.  Thus, with \(K=\sum_pk_p\),

\[
\sum_{t=0}^{q-1}C_{qN}^{\mathcal P}(r+tN)=K+R_N^{\mathcal P}(r).
\tag{3}
\]

If \(X\) is uniform modulo \(qN\), \(\pi(X)=X\bmod N\), and
\(f=C_{qN}^{\mathcal P}-\overline C\), then (3) gives

\[
\mathbb E[f(X)\mid\pi(X)=r]
=\frac1q\left(R_N^{\mathcal P}(r)-\overline R\right).
\]

Apply the orthogonal conditional-expectation decomposition in normalized
\(L^2\) and multiply by \(q^2\).  The projection term is
\(\operatorname{Var}_NR_N^{\mathcal P}\), and the orthogonal term expands to
(2).  \(\square\)

Equivalently, after applying the cyclic \(H^{-1}\) identity and normalization
defined in `ENDPOINT_IMBALANCE_THEOREM.md`, this is an exact \(H^{-1}\)
projection formula: the pushforward of the fine endpoint imbalance is
\(\Delta R_N\).

## 2. Genuine frozen-edge martingale

If every pair distance is below \(N\), then \(R_N=C_N\).  Couple uniform
offsets by \(X_j=X_{j+1}\bmod n_j\) on the compatible spaces
\(n_j=q^jN\).  Then

\[
M_j=q^jC_{n_j}^{\mathcal P}(X_j)
\]

is a nonnegative martingale.  Its centered square function satisfies

\[
q^{2J}\operatorname{Var}_{n_J}C_{n_J}^{\mathcal P}
=\operatorname{Var}_NC_N^{\mathcal P}
+\sum_{j=0}^{J-1}\mathbb E[(M_{j+1}-M_j)^2].
\tag{4}
\]

For \(q=2\), one step is

\[
\boxed{
4\operatorname{Var}_{2N}C_{2N}^{\mathcal P}
=\operatorname{Var}_NC_N^{\mathcal P}
+\frac1N\sum_{r\bmod N}
\bigl(C_{2N}(r)-C_{2N}(r+N)\bigr)^2.
}
\tag{5}
\]

This is a valid martingale only for a fixed edge multiset.

## 3. Minimal birth obstruction

Take \(N=2\), \(q=2\), and the Sidon set

\[
A=\{0,1,4\}.
\]

At modulus 2 only the length-1 pair is short, so

\[
C_2=(0,1),\qquad\operatorname{Var}C_2=\frac14.
\]

At modulus 4 the newly admitted length-3 arc exactly complements the old
length-1 arc:

\[
C_4=(1,1,1,1),\qquad\operatorname{Var}C_4=0.
\]

More generally, \(A=\{0,1,qN\}\) is Sidon and has

\[
\operatorname{Var}C_N=\frac{N-1}{N^2},
\qquad C_{qN}\equiv1,
\qquad\operatorname{Var}C_{qN}=0.
\tag{6}
\]

Therefore the canonical complete loads across scales cannot be a martingale
under any nonzero scalar normalization, and no inequality
\(q^2V_{qN}\ge cV_N\), \(c>0\), is possible.  Sidon uniqueness does not
prevent exact cancellation by one newborn edge.

## 4. Subtracting newborn residuals

Write

\[
R_N=C_N^{\mathrm{old}}+B_N,
\]

where \(B_N\) is the residual-arc load of edges born in
\(N\le d<qN\).  The triangle inequality in centered \(L^2\), together with
(1), gives the rigorous dichotomy

\[
\boxed{
\frac12\operatorname{Var}C_N^{\mathrm{old}}
\le q^2\operatorname{Var}C_{qN}+\operatorname{Var}B_N.
}
\tag{7}
\]

This recovers old energy either in the finer scalar load or in the folded
birth load.  It does not close a telescoping budget: the cross term between
old and newborn residual loads has no sign.

Nor does distinctness of edge lengths make an arbitrary newborn
**subfamily** almost orthogonal.  For a sufficiently large odd prime \(p\),
take the Erdős--Turán ruler

\[
b_i=2pi+(i^2\bmod p),\qquad N=p^2,
\]

and retain the mark 0 together with indices in

\[
I=[5p/8,2p/3],\qquad J=[5p/6,7p/8]
\]

(integer endpoints rounded inward).  Every star edge \((0,b_i)\) has length
in \([N,2N)\), while every difference between two retained nonzero marks is
below \(N\).  Thus the star edges form a legitimate newborn subfamily.  Their
residual arcs share one start and are nested.  For \(i\in I\),
\(s_i/N\ge1/4\); for \(j\in J\), \(s_j/N\le3/4+1/p\).  Hence, for \(p\ge8\),

\[
\operatorname{Cov}(1_{[1,s_i]},1_{[1,s_j]})
=\frac{s_i}{N}\left(1-\frac{s_j}{N}\right)\ge\frac1{32}.
\]

Both blocks contain \(\Omega(p)\) indices.  If
\(B_N^{\rm star}\) denotes only this subfamily load, then

\[
\operatorname{Var}B_N^{\rm star}=\Omega(p^2),
\qquad
\sum_i\operatorname{Var}1_{[1,s_i]}=O(p).
\]

This does not assert the same lower bound for the complete newborn load,
whose additional arcs could cancel after centering.  It proves the precise
negative statement needed here: distinct edge lengths alone give no uniform
Bessel bound for every newborn subfamily.

## 5. Consequence for the research program

The cover identity supplies a clean positive innovation for frozen edges, but
births are an unavoidable and quantitatively sharp obstruction.  A viable
martingale route now needs one of:

1. a multiscale anti-alignment theorem for old and newborn residual loads;
2. a weighted global bound on birth-shell energies;
3. a different filtration in which the changing edge family is encoded in
   additional orthogonal coordinates.

One-step uniqueness, scalar normalization, and direct newborn subtraction are
rigorously insufficient.

## 6. Machine checks

`cover_martingale.py` implements (1), (2), (5), and (7) exactly with rational
arithmetic.  `test_cover_martingale.py` checks random pair multisets, the
frozen square identity, the zero-innovation three-cycle, and the full family
(6).  These checks are an algebra audit, not a proof substitute.

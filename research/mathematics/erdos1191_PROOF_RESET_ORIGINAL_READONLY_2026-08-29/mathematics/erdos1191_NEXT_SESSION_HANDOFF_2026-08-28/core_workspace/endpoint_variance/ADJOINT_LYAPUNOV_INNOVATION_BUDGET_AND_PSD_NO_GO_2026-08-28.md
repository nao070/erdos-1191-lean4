# Adjoint Lyapunov innovation budget and the PSD-only no-go

Date: 2026-08-28  
Status: exact reduction of the missing upper budget to arithmetic innovations,
plus a rigorous no-go for proofs using only the abstract PSD recursion and
critical growth.  This does not resolve Erdős Problem #1191.

## 1. Normalized recursion

For dyadic prefixes, the gap-measure covariance note proves

\[
\mathcal M_{j+1}=B\mathcal M_jB^{\mathsf T}+Q_j,
\qquad Q_j\succeq0,
\qquad
B=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix}.
\]

Write

\[
R_j=\frac{\mathcal M_j}{N_j},
\qquad
\rho_j=\frac{N_j}{N_{j+1}},
\qquad
\widehat Q_j=\frac{Q_j}{N_{j+1}},
\qquad
E=e_1e_1^{\mathsf T}.
\]

Then

\[
R_{j+1}=\rho_jBR_jB^{\mathsf T}+\widehat Q_j,
\qquad
G_j:=\langle E,R_j\rangle
=\operatorname{Var}_{\nu_j}(u(1-u)).
\tag{1}
\]

The matrices \(Q_j\) arising from an actual prefix are much more special than
arbitrary PSD matrices: they are sums of a newborn-shell covariance and a
rank-one mixture term.  We deliberately postpone that arithmetic structure
until Section 7.

## 2. Exact finite-horizon adjoint identity

Fix a horizon \(J\), put \(H_{J+1}=0\), and define backwards

\[
H_j=E+\rho_jB^{\mathsf T}H_{j+1}B
\qquad(1\le j\le J).
\tag{2}
\]

Every \(H_j\) is PSD.  Taking Frobenius inner products in (1) and using (2)
gives, without an inequality,

\[
G_j
=\langle H_j,R_j\rangle
-\langle H_{j+1},R_{j+1}\rangle
+\langle H_{j+1},\widehat Q_j\rangle.
\]

Therefore

\[
\boxed{
\sum_{j=1}^{J}G_j
=\langle H_1,R_1\rangle
+\sum_{j=1}^{J}\langle H_{j+1},\widehat Q_j\rangle.
}
\tag{3}
\]

This is the exact Abel/adjoint-Lyapunov form of the upper-budget problem.  It
does not discard off-diagonal covariance and introduces no sign loss.

## 3. Uniform Lyapunov majorant

The diameter moduli are increasing, so \(0<\rho_j\le1\).  The unique PSD
solution of

\[
H-B^{\mathsf T}HB=E
\]

is

\[
\boxed{
H=\begin{pmatrix}
16/15&8/105\\
8/105&4/35
\end{pmatrix},
\qquad
\det H=\frac{256}{2205}.
}
\tag{4}
\]

Backward induction in (2) gives \(0\preceq H_j\preceq H\).  In particular,

\[
\sum_{j=1}^{J}G_j
\le \langle H,R_1\rangle
+\sum_{j=1}^{J}\langle H,\widehat Q_j\rangle.
\tag{5}
\]

Because \(z=(u(1-u),u)\) is uniformly bounded on \([0,1]\), the first term
is uniformly \(O(1)\).  Thus a sufficient theorem is

\[
\sum_{j\le J}\langle H,Q_j/N_{j+1}\rangle=o(\log J).
\tag{6}
\]

The horizon-dependent version in (3) is exact, so an estimate for its
weighted innovations is also necessary up to the bounded initial term.

## 4. Critical abstract orbit with linear energy

The conditions \(Q_j\succeq0\) and critical growth alone are far too weak.
Let \(L\) be a positive integer and set

\[
N_j=L4^jj,
\qquad
R_j=R:=\begin{pmatrix}1/72&0\\0&1/6\end{pmatrix},
\qquad
\mathcal M_j=N_jR.
\tag{7}
\]

For \(m_j=2^j\), this has exactly the critical form
\(N_j=(L/\log2)m_j^2\log m_j\).  Moreover, \(R\) is not an arbitrary PSD
matrix: it is the covariance of \(z=(U(1-U),U)\) when \(U\) is uniform on
\(\{0,1/2,1\}\).

Direct multiplication gives

\[
BRB^{\mathsf T}
=\begin{pmatrix}13/1152&1/48\\1/48&1/24\end{pmatrix}.
\]

Define \(Q_j=\mathcal M_{j+1}-B\mathcal M_jB^{\mathsf T}=N_jA_j\), where

\[
A_j=
\begin{pmatrix}
17/384+1/(18j)&-1/48\\
-1/48&5/8+2/(3j)
\end{pmatrix}.
\]

Both diagonal entries are positive and

\[
\det A_j
=\frac{251}{9216}+\frac{37}{576j}+\frac1{27j^2}>0,
\]

so \(Q_j\succ0\) for every \(j\).  Nevertheless,

\[
G_j=\frac1{72},
\qquad
\boxed{\sum_{j=1}^{J}G_j=\frac J{72}.}
\tag{8}
\]

Equation (3) then says exactly

\[
\sum_{j=1}^{J}\langle H_{j+1},\widehat Q_j\rangle
=\frac J{72}-\langle H_1,R\rangle,
\]

and \(0\le\langle H_1,R\rangle\le\langle H,R\rangle=32/945\).

The orbit (7) is an **abstract no-go witness**.  Although each normalized
matrix is the covariance of a genuine function of a compactly supported
random variable, we do not claim that the complete sequence of innovations
comes from nested integer gap profiles, much less from one Golomb ruler.  It
rules out only arguments that use the recursion, PSD, and critical growth
while ignoring the arithmetic birth-shell constraints.

## 5. No uniformly controlled useful telescope from arbitrary PSD linear potentials

Let

\[
\Phi_j=\langle P_j,\mathcal M_j\rangle,
\qquad P_j\succeq0.
\]

Then

\[
\Phi_{j+1}-\Phi_j
=\langle B^{\mathsf T}P_{j+1}B-P_j,\mathcal M_j\rangle
+\langle P_{j+1},Q_j\rangle.
\tag{9}
\]

If \(G_j\le\Phi_{j+1}-\Phi_j\) is to hold for every pair
\(\mathcal M_j,Q_j\succeq0\), it is necessary that

\[
B^{\mathsf T}P_{j+1}B-P_j\succeq E/N_j.
\]

Putting \(p_j=e_1^{\mathsf T}P_je_1\) and using \(Be_1=e_1/4\) yields

\[
p_{j+1}\ge16p_j+16/N_j.
\]

Thus a forward-oriented telescope is possible only at the cost of rapidly
growing coefficient matrices; it cannot furnish a uniformly controlled
terminal bound of the required size.  On the abstract orbit (7), \(R\) is
positive definite and \(\mathcal M_j=N_jR\), so this coefficient growth makes
the terminal boundary cost still larger rather than controlling the linear
sum.  A fixed PSD \(P\) fails even one step because

\[
e_1^{\mathsf T}(B^{\mathsf T}PB-P)e_1=-15P_{11}/16\le0.
\]

Conversely, requiring \(G_j\le\Phi_j-\Phi_{j+1}\) for every PSD innovation
forces \(-P_{j+1}\succeq0\).  Together with \(P_{j+1}\succeq0\), this gives
\(P_{j+1}=0\), which is incompatible with the state coefficient over
successive steps.  Hence the forward orientation admits only an unusably
exploding terminal potential, while the reverse orientation cannot absorb
arbitrary PSD innovations over consecutive steps.  This is a no-go for a
**uniformly controlled upper-budget proof**, not a nonexistence claim for
formal forward telescopes with unbounded coefficients.

## 6. Eigenmodes and determinant do not repair the loss

The diagonalization

\[
B=S\operatorname{diag}(1/4,1/2)S^{-1},
\qquad
S=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]

shows that both transported state modes contract.  Persistent energy is
therefore replenished entirely by innovations.  Determinants only give the
one-sided persistence

\[
\det R_{j+1}\ge\frac{\rho_j^2}{64}\det R_j,
\]

because for PSD \(A,Q\) in two dimensions,
\(\det(A+Q)=\det A+\det Q+\operatorname{tr}(\operatorname{adj}(A)Q)\).
This lower relation supplies no upper innovation budget.  The constant orbit
(7) also defeats every scale-independent function of normalized trace,
determinant, or eigenvalues.

## 7. Exact remaining arithmetic lemma

For an actual gap update from \(m\) to \(2m\), let \(G=N_{2m}-N_m\), let
\(\sigma_m\) be the newborn-shell gap measure, and let \(d_m\) be the
difference between the transported old mean and the newborn mean.  Then

\[
Q_m
=G\operatorname{Cov}_{\sigma_m}z
+\frac{N_mG}{N_{2m}}d_md_m^{\mathsf T}.
\tag{10}
\]

Combining (3) and (10) isolates the precise theorem still needed:

> Use the fact that all contiguous sums of one global integer gap sequence
> are distinct, together with the critical diameter envelope, to prove a
> sub-logarithmic bound for the adjoint-weighted sum of the two nonnegative
> arithmetic innovations in (10).

No theorem in this note provides that estimate.  What is now proved is that
generic uniformly controlled Lyapunov, trace, determinant, eigenbasis, or
arbitrary-PSD arguments cannot provide it; the next proof must see the actual
Sidon birth shell.

`innovation_budget.py` and `test_innovation_budget.py` verify (3)--(8) using
exact rational arithmetic.

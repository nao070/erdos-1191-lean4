# Cross-epoch profile persistence and the reset-amortization obstruction

**Date:** 2026-08-28  
**Status:** exact persistence and signed-reset theorems, a conditional flat-run
amortization, and a rigorous non-Sidon counterprofile.  The missing arithmetic
innovation budget is not proved, and Erdős Problem #1191 is not resolved.

## 1. Notation

Let

\[
A=\{a_0<a_1<a_2<\cdots\}
\]

be an increasing integer sequence.  For every \(n\ge1\), put

\[
N_0=0,
\qquad
N_n=a_{n-1}-a_0+1.
\]

Thus \(N_n\), not the diameter \(N_n-1\), is the modulus used throughout.
For \(0\le r\le n\), define the diameter-profile error

\[
e_n(r)=\frac{N_r}{N_n}-\frac rn.
\tag{1}
\]

Put \(h_0=1\) and \(h_k=a_k-a_{k-1}\) for \(k\ge1\).  The diameter-gap
measure and its covariance state are

\[
\nu_n=\frac1{N_n}\sum_{k=0}^{n-1}h_k\delta_{k/n},
\qquad
z(u)=\binom{u(1-u)}u,
\qquad
\mathcal M_n=N_n\operatorname{Cov}_{\nu_n}z.
\tag{2}
\]

All logarithms below are natural.  The critical hypothesis is written

\[
N_n\le K n^2\log n.
\tag{3}
\]

The canonical convention \(N_n\le2C n^2\log n\) corresponds to \(K=2C\).

## 2. Theorem A: exact chord inheritance across an arbitrary epoch

Let \(M=qm\), where \(q\ge2\) is an integer, and set

\[
\alpha=\frac{N_m}{N_M}.
\]

Then, for every integer \(0\le r\le m\),

\[
\boxed{
e_M(r)=\alpha e_m(r)+\frac rm e_M(m),
\qquad
e_M(m)=\alpha-\frac1q.
}
\tag{4}
\]

Equivalently,

\[
\boxed{
e_M(r)-\frac rm e_M(m)=\alpha e_m(r).
}
\tag{5}
\]

Thus subtracting the chord from \((0,0)\) to \((m,e_M(m))\) leaves exactly a
positive scalar copy of the complete old profile.  In particular, the rank
location and sign of every non-affine old-profile extremum persist.  There is
no cancellation hidden in this statement; only its amplitude is reduced by
\(\alpha\).

### Proof

Since \(r\le m\),

\[
\frac{N_r}{N_M}=\alpha\frac{N_r}{N_m}.
\]

Substitute this identity and \(M=qm\) into (1):

\[
e_M(r)
=\alpha\left(\frac{N_r}{N_m}-\frac rm\right)
+\frac rm\left(\alpha-\frac1q\right).
\]

Taking \(r=m\) gives the second formula in (4), and (5) follows.  No Sidon or
critical-growth hypothesis was used.  \(\square\)

### Direct \(q\)-step covariance form

Let \(g=N_M-N_m\), let \(T_q(u)=u/q\), and let

\[
\sigma_{m,M}=\frac1g\sum_{k=m}^{M-1}h_k\delta_{k/M}.
\]

Then exactly

\[
\nu_M=\alpha(T_q)_*\nu_m+(1-\alpha)\sigma_{m,M}.
\tag{6}
\]

Moreover,

\[
z(T_q u)=B_qz(u),
\qquad
B_q=
\begin{pmatrix}
q^{-2}&(q-1)q^{-2}\\
0&q^{-1}
\end{pmatrix}.
\tag{7}
\]

Writing \(\bar z_m=\int z\,d\nu_m\) and
\(\bar z_\sigma=\int z\,d\sigma_{m,M}\), the vector mixture-covariance
identity gives the direct epoch update

\[
\boxed{
\mathcal M_M=B_q\mathcal M_mB_q^{\mathsf T}+Q_{m,M},
}
\tag{8}
\]

where

\[
Q_{m,M}
=g\operatorname{Cov}_{\sigma_{m,M}}z
+\frac{N_mg}{N_M}
(B_q\bar z_m-\bar z_\sigma)(B_q\bar z_m-\bar z_\sigma)^{\mathsf T}
\succeq0.
\tag{9}
\]

This is the arbitrary-\(q\) version of the adjacent dyadic recursion.  Formula
(5) and the PSD transport (8) are exact manifestations of the same old-mass
persistence.

## 3. Theorem B: global cross-block packing forces a signed reset

Assume now that the first \(M=qm\) marks form a Sidon ruler and that only the
old prefix satisfies

\[
N_m\le K m^2\log m.
\tag{10}
\]

Partition the \(M\) ranks into \(q\) consecutive blocks of \(m\) marks.
There are exactly \(\binom q2m^2\) mark pairs belonging to different blocks.
Their positive differences are all distinct integers in
\(\{1,\ldots,N_M-1\}\).  Hence

\[
N_M-1\ge\binom q2m^2.
\tag{11}
\]

Combining (10), (11), and the signed identity in (4) gives

\[
\boxed{
e_M(m)
\le
\frac{K m^2\log m}{\binom q2m^2+1}-\frac1q.
}
\tag{12}
\]

In particular, if

\[
q-1\ge4K\log m,
\tag{13}
\]

then

\[
\frac{N_m}{N_M}
\le\frac{2K\log m}{q(q-1)}
\le\frac1{2q},
\]

and therefore

\[
\boxed{e_M(m)\le-\frac1{2q}.}
\tag{14}
\]

All integer endpoint corrections are retained in (11) and (12).  No critical
upper bound at \(M\) is used.  For dyadic prefixes one takes \(q\) to be a
power of two.  Equations (5) and (14) together say more than an unsigned
discrepancy bound: the deep reset has a forced negative chord, while the
old non-affine curvature remains attached to it with factor \(N_m/N_M\).

The limitation is equally explicit.  Under (13), that persistence factor may
be only \(O(K\log m/q^2)\).  A sufficiently deep reset can therefore make the
old curvature very small without violating either theorem.

## 4. Theorem C: a bound on one endpoint-flat run

Let \(m_j=2^j\), write \(N_j=N_{m_j}\), and put

\[
\kappa_j=\frac{N_j}{m_j^2},
\qquad
\rho_j=\frac{N_j}{N_{j+1}}.
\tag{15}
\]

Sidon uniqueness alone gives

\[
N_j-1\ge\binom{m_j}{2},
\]

and hence, for every \(j\ge1\),

\[
\kappa_j
\ge\frac12-2^{-j-1}+4^{-j}
\ge\frac7{16}.
\tag{16}
\]

Also,

\[
\frac{\kappa_{j+1}}{\kappa_j}=\frac1{4\rho_j},
\qquad
e_{m_{j+1}}(m_j)=\rho_j-\frac12.
\tag{17}
\]

Fix \(0\le\eta<1/4\).  Suppose that for
\(j=s,\ldots,s+L-1\),

\[
e_{m_{j+1}}(m_j)\ge-\eta,
\tag{18}
\]

and that the starting prefix obeys \(N_s\le K m_s^2\log m_s\).  Then
\(\rho_j\ge1/2-\eta\), so iteration of (17) and (16) yields

\[
\frac7{16}
\le\kappa_{s+L}
\le\frac{K s\log2}{(2-4\eta)^L}.
\]

Consequently

\[
\boxed{
L\le
\frac{\log\!\bigl((16/7)Ks\log2\bigr)}
     {\log(2-4\eta)}.
}
\tag{19}
\]

The integer length is at most the floor of the right side.  In particular, a
run with nonnegative midpoint errors, and therefore also a run of exactly
endpoint-flat steps, has length at most

\[
\log_2\!\bigl((16/7)Ks\log2\bigr)=O_K(\log s)
=O_K(\log\log m_s).
\tag{20}
\]

This is a genuine cross-epoch oscillation restriction for one Sidon sequence,
but it is only a single-run bound.

## 5. The exact conditional amortization and its missing term

For integers \(S<T\), set \(x_j=\log\kappa_j\) and define the upward and
downward variations

\[
U_{S,T}=\sum_{j=S}^{T-1}(x_{j+1}-x_j)_+,
\qquad
D_{S,T}=\sum_{j=S}^{T-1}(x_j-x_{j+1})_+.
\tag{21}
\]

Let \(F_\eta(S,T)\) be the number of indices in this interval satisfying
(18).  At every such index, (17) gives

\[
x_j-x_{j+1}\ge\log(2-4\eta).
\]

Since \(x_T-x_S=U_{S,T}-D_{S,T}\), (16) proves the exact conditional bound

\[
\boxed{
F_\eta(S,T)\log(2-4\eta)
\le U_{S,T}+\log\frac{\kappa_S}{7/16}.
}
\tag{22}
\]

If the start is critical, then

\[
F_\eta(S,T)
\le
\frac{U_{S,T}+\log((16/7)KS\log2)}{\log(2-4\eta)}.
\tag{23}
\]

Thus an upper budget for the upward normalized-diameter resets would
immediately amortize all endpoint-flat runs.  The critical envelope controls
the endpoints \(x_j=O(\log j)\), but it does **not** control the positive
variation \(U_{S,T}\).  The next construction shows that this is not a
technical gap.

## 6. Counterexample to profile-only reset amortization

This section constructs one infinite nested positive-integer gap profile.  It
obeys a fixed critical envelope, the scalar difference-capacity lower bound,
the exact measure recursion, and a uniform positive innovation bound.  It is
deliberately not Sidon.

Define powers of two \(k_j\) by

\[
k_1=1,
\qquad
k_j=
\begin{cases}
k_{j-1}/2,&k_{j-1}>1,\\
2^{\lfloor\log_2j\rfloor},&k_{j-1}=1,
\end{cases}
\quad(j\ge2),
\tag{24}
\]

and set

\[
n_j=2^j,
\qquad
N_j=4^jk_j.
\tag{25}
\]

The first fifteen multipliers are

\[
1,2,1,4,2,1,4,2,1,8,4,2,1,8,4.
\tag{26}
\]

Every \(k_j\) is a power of two with \(1\le k_j\le j\).  The modulus grows
by a factor \(2\) on a halving step and by a factor at least \(8\) on a reset.
Moreover,

\[
N_j=n_j^2k_j\le jn_j^2<2n_j^2\log n_j,
\tag{27}
\]

where the strict last inequality uses \(\log2>1/2\).  Thus the canonical
\(C=1\) bound holds at every dyadic prefix.  Also \(N_j\ge n_j^2\), so the
scalar Sidon capacity \(N_j-1\ge\binom{n_j}{2}\) holds with room to spare.

Now set \(h_0=1,h_1=3\).  Having constructed the first \(m=2^j\) gaps with
sum \(N_j\), append \(m\) equal positive integer gaps

\[
h_m=\cdots=h_{2m-1}=c_j,
\qquad
c_j=\frac{N_{j+1}-N_j}{m}
=2^j(4k_{j+1}-k_j).
\tag{28}
\]

The right side is a positive integer, so (28) defines one infinite increasing
integer sequence with the exact dyadic moduli (25).  For an intermediate
prefix \(n=m+s\), \(0\le s\le m\),

\[
N_n=N_j+s c_j.
\tag{29}
\]

Since \(c_j\ge m\) and \(N_j\ge m^2\), (29) also gives

\[
N_n-1\ge\binom n2.
\tag{30}
\]

Furthermore \(N_n\le4(j+1)m^2\), while \(\log2>2/3\) gives
\(12n^2\log n>8jn^2\ge4(j+1)m^2\).  Thus one fixed all-prefix envelope

\[
N_n<12n^2\log n\qquad(n\ge2)
\tag{31}
\]

holds, not merely its dyadic restriction.

### Exact flattening and recurrent resets

For one transition \(m\to2m\), put \(\alpha=N_m/N_{2m}\).  Equal shell
weights give, for \(0\le s\le m\),

\[
e_{2m}(m+s)=
\left(\alpha-\frac12\right)\left(1-\frac sm\right).
\tag{32}
\]

On a halving step in (24), \(\alpha=1/2\).  Equations (5) and (32) then give

\[
e_{2m}(r)=\frac12e_m(r)\quad(0\le r\le m),
\qquad
e_{2m}(r)=0\quad(m\le r\le2m).
\tag{33}
\]

Thus the **entire** old profile error is halved and the newborn half is
exactly rank-flat.  On a reset to height
\(h=2^{\lfloor\log_2j\rfloor}\), one has

\[
\alpha=\frac1{4h},
\qquad
e_{n_j}(n_{j-1})=\frac1{4h}-\frac12<0.
\tag{34}
\]

At every dyadic prefix, all grid errors in this construction are nonpositive
and have absolute value at most \(1/2\), by induction from (4) and (32).
After the
\(\log_2h\) flat steps following a reset, (33) gives

\[
\max_r|e(r)|\le\frac1{2h}<\frac1j.
\tag{35}
\]

Thus near-uniform profiles of order \(O(1/j)\) recur, separated
by signed resets of size nearly \(1/2\).

Let \(R_J\) be the number of reset transitions through level \(J\).  Two
successive resets starting at level \(j\) are separated by
\(\lfloor\log_2j\rfloor+1\) levels.  For \(J\ge4\), splitting at
\(\sqrt J\) gives the elementary bound

\[
R_J\le\lceil\sqrt J\rceil+1+\frac{2J}{\log_2J}=o(J).
\tag{36}
\]

All other \(J-1-R_J\) transitions are exactly endpoint-flat.  The total
endpoint-reset magnitude is less than \(R_J/2=o(J)\).  Each flat transition
decreases \(x_j=\log k_j\) by exactly \(\log2\), so
\(D_{1,J}=(J-1-R_J)\log2=\Theta(J)\).  Since
\(U_{1,J}=D_{1,J}+x_J-x_1\) and \(0\le x_J\le\log J\), the upward log
variation is also \(\Theta(J)\).  This is the precise scalar term that the
critical envelope leaves uncontrolled.

### Uniform positive innovation on every flat and reset step

The shell measure in (28) is uniform on

\[
\left\{\frac12,\frac12+\frac1{2m},\ldots,1-\frac1{2m}\right\}.
\]

Writing \(f(u)=u(1-u)\), exact power sums give

\[
\operatorname{Var}_\sigma f
=\frac{(m-1)(2m-1)(8m^2-3m-11)}{2880m^4}.
\tag{37}
\]

For \(m\ge2\),

\[
\operatorname{Var}_\sigma f-\frac1{1024}
=\frac{(m-2)(211m^3-58m^2-196m+88)}{46080m^4}
\ge0.
\tag{38}
\]

Indeed, the cubic equals \(1152\) at \(m=2\), and its derivative is positive
for \(m\ge2\).  Since \(N_m/N_{2m}\le1/2\), the shell-covariance term in
(9), with \(q=2\), proves

\[
\boxed{
\frac{(Q_m)_{00}}{N_{2m}}
\ge
\left(1-\frac{N_m}{N_{2m}}\right)
\operatorname{Var}_\sigma f
\ge\frac1{2048}
}
\tag{39}
\]

at every transition.  The nonnegative rank-one mixture term was discarded.
Hence

\[
\sum_{j=1}^{J-1}\frac{(Q_j)_{00}}{N_{j+1}}
\ge\frac{J-1}{2048}.
\tag{40}
\]

With the finite-horizon convention of
`ADJOINT_LYAPUNOV_INNOVATION_BUDGET_AND_PSD_NO_GO_2026-08-28.md`, where
\(E=e_1e_1^{\mathsf T}\), the adjoint matrices satisfy
\(H_{j+1}\succeq E\) away from the final boundary.  The corresponding
adjoint-weighted innovation sum is therefore linear as well.

Consequently, for every fixed constant \(C\), the natural endpoint-reset
candidate

\[
\sum_{j<J}\frac{(Q_j)_{00}}{N_{j+1}}
\le C\left(
1+\log(1+J)
+\sum_{j<J}\left|e_{n_{j+1}}(n_j)\right|
\right)
\tag{41}
\]

is false even for one infinite nested positive-integer gap profile satisfying
(30), (31), and the exact covariance recursion.  The same is true if the last
sum in (41) is replaced by the number of nonflat endpoint resets.

This is **not** a counterexample in the Sidon class.  Already at four marks
the gaps are \((1,3,14,14)\), so the positive difference \(14\) occurs twice.
Every later uniform shell has many more repeated contiguous sums.  The
construction therefore isolates the missing hypothesis exactly: all
contiguous gap sums must be distinct.

## 7. What follows, and what does not

The rigorous conclusions are:

1. deep global packing forces a negative reset chord, not merely an unsigned
   discrepancy;
2. old non-affine curvature persists exactly after that chord is removed;
3. one almost-flat run is only \(O(\log\log m)\) generations long;
4. endpoint-flat steps admit the exact conditional amortization (22); and
5. neither critical growth, scalar difference capacity, profile persistence,
   endpoint-reset magnitude, nor PSD gap dynamics can control the missing
   innovations without Sidon arithmetic.

These statements do **not** imply

\[
\sum_{j\le J}\operatorname{Var}_{\nu_j}(u(1-u))=o(\log J)
\]

or the equivalent adjoint innovation budget.  In particular, (22) is useless
until one controls \(U_{S,T}\), and the counterprofile has
\(U_{1,J}=\Theta(J)\) while remaining critical.

## 8. Sharp next candidate

The next lemma must be an arithmetic **reset-renewal exclusion**.  A viable
statement has to use actual cross differences from more than
\(\Theta(\log J)\) recent scales and prove that repeated nearly uniform
newborn shells cannot be perturbed into distinct contiguous sums inside the
same critical diameter budget.  Equivalently, it must charge the two terms in
(9) to globally distinct cross-epoch mark pairs, with overlapping integer
bands shared by several reset-to-flat cycles.

The exact obstruction is now narrow:

- the chord identity (5) supplies sign, location, and persistence of the old
  curvature;
- same-rank-lag band endpoints are already known exactly in the cross-block
  packing note;
- the balanced-shell construction above shows that any charge depending only
  on those profiles or covariance moments can renew forever; and
- the growing-depth Erdős--Turán family shows that the required collision
  charge cannot inspect only the last \(\Theta(\log J)\) scale indices.

What remains is to quantify the extra diameter or band occupation forced when
the repeated equal-shell model is replaced by one global gap sequence whose
**all** contiguous sums are distinct.  No such cross-epoch inequality is
proved here.

`wave5_cross_epoch.py` and `test_wave5_cross_epoch.py` verify the exact chord
identity, the \(q\)-step transport matrix, the balanced-shell profile update,
the sawtooth moduli, the collision, and the rational innovation values.

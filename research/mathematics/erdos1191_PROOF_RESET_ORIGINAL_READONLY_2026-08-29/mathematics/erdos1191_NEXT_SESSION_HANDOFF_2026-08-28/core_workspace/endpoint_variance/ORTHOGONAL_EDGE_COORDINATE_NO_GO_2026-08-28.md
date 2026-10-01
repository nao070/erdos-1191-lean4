# Orthogonal edge-coordinate trace no-go theorem

Date: 2026-08-28  
Status: rigorous negative theorem for the stated diagonal Hilbert architecture.
It does not exclude structured off-diagonal or block-coordinate filtrations.

## 1. Static coordinate factorization

Let \(A_m\) be Sidon, \(N=D_m+1\), and let its
\(P=\binom m2\) distinct pair differences be \(d_p\in\{1,\ldots,N-1\}\).
For the centered cyclic arc indicator put

\[
x_p(r)=1_{B_p}(r)-\frac{d_p}{N},
\qquad
v_p=\|x_p\|_{2,N}^2=\frac{d_p(N-d_p)}{N^2}.
\]

Every positive diagonal weighting has the realization

\[
F(r)=(\sqrt{w_p}x_p(r))_p,
\qquad
u=(w_p^{-1/2})_p,
\qquad
C_N^\circ(r)=\langle F(r),u\rangle.
\]

Its trace and synthesis cost are

\[
T_w=\sum_pw_pv_p,
\qquad U_w=\sum_p\frac1{w_p},
\]

so the diagonal coordinate/Cauchy architecture yields
\(V_N\le U_wT_w\).  But the cost cannot be made small.

**Theorem.**  For every choice of positive \(w_p\),

\[
\boxed{U_wT_w\ge\frac{P^3}{9N}.}
\tag{1}
\]

### Proof

Cauchy in the reverse direction gives

\[
U_wT_w\ge\left(\sum_p\sqrt{v_p}\right)^2.
\tag{2}
\]

Let \(r_p=\min(d_p,N-d_p)\), sorted increasingly.  At most two distinct
differences have a given \(r_p\), hence

\[
r_k\ge\lceil k/2\rceil\ge k/2.
\]

Since \(r_k\le N/2\),

\[
v_k=\frac{r_k(N-r_k)}{N^2}\ge\frac{k}{4N}.
\]

Therefore

\[
\sum_{k=1}^P\sqrt{v_k}
\ge\frac1{2\sqrt N}\sum_{k=1}^P\sqrt{k}
\ge\frac{P^{3/2}}{3\sqrt N},
\]

which proves (1). \(\square\)

Because \(P\ge m^2/4\), the critical envelope
\(N\le Cm^2\log m\) forces

\[
\boxed{\frac{U_wT_w}{m^4}\ge\frac1{576C\log m}.}
\tag{3}
\]

At dyadic \(m=2^j\), the diagonal coordinate budget alone therefore costs
\(\Omega_C(\log J)\).  Weight optimization cannot make it summable or
\(o(\log J)\).

## 2. Exact vector q-cover martingale trace

Freeze edges with \(d_p<N\), let \(n_\ell=q^\ell N\), and define

\[
M_{p,\ell}=q^\ell
\left(1_{B_{p,n_\ell}}-\frac{d_p}{n_\ell}\right).
\]

Each coordinate is a martingale.  Direct computation gives

\[
\mathbb E M_{p,\ell}^2=q^\ell\frac{d_p}{N}-\frac{d_p^2}{N^2},
\]

and orthogonality of martingale increments therefore yields

\[
\boxed{
\mathbb E\|\mathbf M_{\ell+1}-\mathbf M_\ell\|^2
=(q-1)q^\ell\sum_p\frac{d_p}{N}.
}
\tag{4}
\]

The ordinary square-function trace grows exponentially.  The natural
\(q^{-2\ell}\)-discounted trace is finite but equals

\[
\boxed{
\sum_{\ell\ge0}q^{-2\ell}
\mathbb E\|\mathbf M_{\ell+1}-\mathbf M_\ell\|^2
=q\sum_p\frac{d_p}{N}.
}
\tag{5}
\]

With coordinate weights, combining (5) with the synthesis norm gives an even
larger lower cost

\[
\left(\sum_p\frac1{w_p}\right)
\left(q\sum_pw_p\frac{d_p}{N}\right)
\ge\frac{4qP^3}{9N}.
\tag{6}
\]

The same argument applied only to the
\(P_b=\binom m2-\binom{m/2}{2}\ge m^2/4\) edges born between two dyadic
prefixes already creates a harmonic critical cost.  At
\(N=N_m\le Cm^2\log m\), (6) gives

\[
\frac1{m^4}\frac{4qP_b^3}{9N_m}
\ge\frac{q}{144C\log m},
\]

whose dyadic sum is harmonic.

## 3. Zero-mode audit and interpretation

Exact examples expose the lost information:

| Oriented pair configuration and modulus | scalar variance | coordinate trace | q=2 vector increment |
|---|---:|---:|---:|
| `(0,3),(3,7),(7,12); N=6` | `0` | `11/18` | `2` |
| all pairs of `A=(0,1,3,7); N=8` | `87/64` | `69/64` | `23/8` |
| `(0,1),(1,4); N=4` | `0` | `3/8` | `1` |

The three-cycle has zero scalar variance at both compatible moduli but spends
positive vector square-function energy.  Separate edge coordinates remember
“ghost energy” that endpoint alignment cancels exactly in the scalar load.

Thus the route is blocked in its fully diagonal form.  A viable filtration
must retain structured off-diagonal information, for example endpoint-sharing
or rank-bin covariance blocks.  Merely assigning every difference its own
orthogonal coordinate cannot produce the missing critical budget.

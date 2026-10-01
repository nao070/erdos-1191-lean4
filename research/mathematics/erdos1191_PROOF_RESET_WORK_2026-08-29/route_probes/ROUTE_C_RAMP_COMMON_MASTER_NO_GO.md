# Route C: active ramp versus the fixed centered common master

Date: 2026-08-30  
Status: `FIXED_THREE_CHANNEL_AND_POSITIVE_GOTHIC_RAMP_PAYMENT_NO_GO`

The ordered-Gram root-cone theorem proves, at every fixed box scale, both
the exact identity `Q_n(T)=<B,G_T>` and a rank-one ramp square which dominates
`Q_n(T)`.  This note audits whether that ramp square can simply be inserted
into the already certified centered three-channel carrier from C061--C067.

The answer is **no for that specific insertion**.  The ramp is a new
rank-weighted input channel, its ungated scale integral diverges, a legal
positive extension has a nonzero Schur/energy price, and an exact affine
Golomb family shows that even the optimally shifted active ramp baseline has
logarithmically more mass than the complete positive same-epoch Gothic
`lambda=beta` sector.  The unused nonpositive finite-potential sector has no
logarithmic reserve on that family.

This is a scoped no-go.  The indefinite Wave matrix `B` itself has zero
surplus in the actual ordered-root dual cone.  A genuinely signed
membership-sensitive whole-cut theorem which uses the labeled root cells
directly is not ruled out.  Nor are cross-epoch/cross-phase payment, a
disjoint external reserve, a larger master, C058, either Erdős question, or
a prize claim resolved.

## 1. The two objects do not have the same channel architecture

At one epoch the fixed centered carrier has the three full-prefix fields

\[
 y=(\mathbf1_A*K_T,\mathbf1_A*K_{2T},
       \mathbf1_A*K_{T^+}).
 \tag{1.1}
\]

Its channel matrices act only on these three coordinates.  Formally, every
mark of `A` therefore receives the same kernel-coefficient row
`(v_1,v_2,v_3)` in any channel-space linear combination.

For the ordered gap block `I={n,...,2n-1}`, the ramp field is instead

\[
 r_{c,T}=\sum_{i=n}^{2n-1}{i-c\over2n}
  (\delta_{a_{i-1}}-\delta_{a_i})*K_T.
 \tag{1.2}
\]

Summation by parts gives

\[
 r_{c,T}={1\over2n}\left[
 (n-c)q_{a_{n-1}}+\sum_{p=n}^{2n-2}q_{a_p}
 -(2n-1-c)q_{a_{2n-1}}\right],
 \quad q_a=\delta_a*K_T.
 \tag{1.3}
\]

Thus the spatial coefficients depend on rank and sum to zero.  For `n=4`
and the midpoint shift `c=11/2`, the eight-mark coefficient vector is

\[
 (0,0,0,-3/16,1/8,1/8,1/8,-3/16).
 \tag{1.4}
\]

It is nonconstant and therefore is not in the **formal fixed full-prefix
channel span** of (1.1).  This is an architectural statement: a new
membership/rank-sensitive input is required.  It does not assert that no
accidental pointwise functional equality can occur on an isolated prefix.

There is also a scale mismatch.  The exact cross-ratio identity requires the
continuum log-phase average over all active `T`, while the fixed carrier uses
only the one or two dyadic bands between `T_j` and `T_(j+1)`.  C064--C065
already prove that finitely many fixed phases and ordinary fixed-prefix
domination cannot replace the continuum identity.

## 2. A zero-mass fourth channel is boundary-free but not energy-free

The fixed three-channel matrix is

\[
 H_3=\begin{pmatrix}
 13/100&3/25&0\\
 3/25&13/50&3/25\\
 0&3/25&13/100
 \end{pmatrix},
 \qquad H_3\mathbf1=\gamma=(1/4,1/2,1/4)^T.
 \tag{2.1}
\]

Consider the most favorable abstract extension by a zero-mass ramp channel,

\[
 \widehat H=\begin{pmatrix}H_3&b\\b^T&d\end{pmatrix},
 \qquad \widehat m=(1,1,1,0)^T.
 \tag{2.2}
\]

Keeping the old constant cover `(gamma,0)` requires `b^T 1=0`.  If
`widehat H` is positive definite, the Schur complement gives the exact
necessary and sufficient inequality

\[
 \boxed{d>b^TH_3^{-1}b\ge0.}
 \tag{2.3}
\]

The leading cover normalization can indeed remain one, because

\[
 (\gamma,0)=\widehat H\widehat m,
 \qquad
 (\gamma,0)^T\widehat H^{-1}(\gamma,0)=1.
 \tag{2.4}
\]

But completing the square in the energy shows the unavoidable distinction:

\[
 y^TH_3y+2r\,b^Ty+d r^2
 =(y+H_3^{-1}br)^TH_3(y+H_3^{-1}br)
 +(d-b^TH_3^{-1}b)r^2.
 \tag{2.5}
\]

Hence boundary normalization being unchanged does **not** mean that a
nonconstant ramp coupling has zero energy price.  For the exact test vector

\[
 b=(1,-2,1)^T/100,
 \quad H_3^{-1}b=(1,-1,1)^T,
 \quad b^TH_3^{-1}b=1/25.
 \tag{2.6}
\]

Taking `d=1/20` leaves the strictly positive residual `1/100`, while the
inverse cover price is still exactly one.

This calculation also explains the ownership issue.  A retained comparison
may subtract a ramp square only after a positive baseline square has been
placed in the master.  Calling the baseline “free” because its mass is zero
confuses boundary cost with energy cost.

## 3. Active gating is necessary and creates explicit boundary rows

Let `eta_i=(i-c)/(2n)` and

\[
 S_c(T)=\left\|\sum_i\eta_i f_{i,T}\right\|_2^2.
\]

For the optimal small-scale shift `c_0=(3n-1)/2`, if
`0<T<min_i h_i`, the ordered-root decomposition gives exactly

\[
 \boxed{S_{c_0}(T)={n^2-1\over8n^2T}.}
 \tag{3.1}
\]

Thus `int_0 S_(c_0)(T)dT` diverges logarithmically, even though
`Q_n(T)=0` there.  At `n=4` the coefficient is `15/128`.  Any ramp insertion
must therefore be active-scale gated.

For a fixed log phase write `T_r=2^(r+theta)`, let `a_r>=0` be supported on a
finite active interval `L<=r<=U`, and set

\[
 s_r=\sum_{t=L}^r a_t,
 \qquad S_r=S_c(T_r).
\]

The box/Haar identity applies to every finite signed input, so `S_r-S_(r+1)`
is a nonnegative band square.  Finite Abel summation is

\[
 \boxed{
 \sum_{r=L}^Ua_rS_r
 =\sum_{r=L}^Us_r(S_r-S_{r+1})+s_US_{U+1}.}
 \tag{3.2}
\]

The last term cannot be dropped.  The ramp measure in (1.3) is nonzero, and
its convolution with a finite uniform box is nonzero: immediately to the
right of its leftmost nonzero atom, only that translate is present.  Hence
`S_(U+1)>0` at every finite terminal width.  The first active row, the last
active row, and the post-gate low-pass terminal all need one explicit owner.

The C067 unique-birth argument does not automatically dispose of these rows.
It applies to one persistent physical pair owner.  The aggregate ramp mixes
both block terminals and all interior ranks and changes with the epoch and,
under optimal shifting, with `T`.

## 4. An affine Golomb family with a sharp logarithmic ramp price

For real `L>25` define

\[
 A_L=(0,2,5,16,16+L,17+L,25+L,25+3L).
 \tag{4.1}
\]

All 28 positive differences are distinct.  Indeed, every difference is an
affine function `sL+b`.  No two with the same slope have the same intercept,
and every positive collision root between different slopes is at most `25`.
For integer `L>=26`, (4.1) is therefore an integer Golomb/Sidon prefix.

At `n=4` its current gap block is

\[
 (h_4,h_5,h_6,h_7)=(L,1,8,2L).
 \tag{4.2}
\]

On the whole interval `9<T<L`, all three Wave edges are active.  Direct
ordered-cell accounting gives

\[
 \rho_4=\rho_7={1\over T},\qquad \rho_5=\rho_6=0,
 \tag{4.3}
\]

\[
 \psi_{45}={1\over T^2},\qquad
 \psi_{56}=0,\qquad
 \psi_{67}={8\over T^2}.
 \tag{4.4}
\]

The nonadjacent overlaps are

\[
 \psi_{46}={8\over T^2},\qquad
 \psi_{47}={T-9\over T^2},\qquad
 \psi_{57}={1\over T^2}.
 \tag{4.5}
\]

With Wave weights `(1/16,9/64,1/16)`, this yields

\[
 \boxed{Q_4(T)={9\over64T}-{45\over64T^2}.}
 \tag{4.6}
\]

The optimal ramp shift is `c_*=11/2`.  Its exact surplus from the two
singleton cells and the adjacent cells is

\[
 \boxed{
 S_{c_*}(T)-Q_4(T)
 ={9\over128T}+{9\over64T^2}.}
 \tag{4.7}
\]

Consequently

\[
 \boxed{S_{c_*}(T)={27\over128T}-{9\over16T^2},}
 \tag{4.8}
\]

and

\[
 \boxed{
 \int_9^L S_{c_*}(T)dT
 ={27\over128}\log{L\over9}-{1\over16}+{9\over16L}.}
 \tag{4.9}
\]

The coefficient one on the ramp baseline is not optional in a cellwise
ordered-root/SOS completion.  If `H=eta eta^T` is replaced by `aH`, then on
an active Wave root

\[
 (e_j-e_i)^T(aH-B)(e_j-e_i)=(a-1)\alpha_{ij}.
 \tag{4.10}
\]

Thus rootwise nonnegativity forces `a>=1`.  Formula (4.9) is already a lower
bound for every such insertion over the complete active union.  Choosing a
smaller scalar only because its *integrated numerical value* happens to
cancel on one prefix would leave negative pointwise root directions and would
not supply the positive metric needed by the existing Cauchy master.

## 5. The positive Gothic sector cannot pay this baseline

Here the box-dipole horizon is `H=3L+9`.  The complete positive
strict-interior finite-potential sector consists of the three owners of
lengths `1,9,8`:

\[
 \mathcal G_L={1\over16}F_H(1)+{1\over64}F_H(9)
              +{1\over16}F_H(8),
 \qquad
 F_H(d)=\log(H/d)+d/H-1.
 \tag{5.1}
\]

Its exact leading logarithmic coefficient is

\[
 {1\over16}+{1\over64}+{1\over16}={9\over64}={18\over128}.
 \tag{5.2}
\]

By (4.9), the optimally shifted active ramp baseline has coefficient
`27/128`.  Therefore

\[
 \boxed{
 \int_9^L S_{c_*}(T)dT-\mathcal G_L
 ={9\over128}\log L+O(1)\longrightarrow+\infty.}
 \tag{5.3}
\]

The certificate also records a finite exact separation.  At `L=2^18`, use

\[
 \log2>{2\over3},\qquad \log9<3,\qquad \log4<2,
 \qquad 3L+9\le4L.
\]

Dropping only positive terms in the exact difference gives

\[
 \int_9^L S_{c_*}(T)dT-\mathcal G_L
 >{9\cdot12-27\cdot3-18\cdot2+10\over128}
 ={1\over128}>0.
 \tag{5.4}
\]

This is not merely a bad choice of scalar shift.  On `9<T<L`, the Wave edge
`(4,7)` forces squared Hilbert distance at least `alpha_(4,7)=9/64` in **any**
sum-of-squares/ramp completion.  Since `rho_4=rho_7=1/T`, the parallelogram
inequality gives

\[
 {\|v_4\|^2+\|v_7\|^2\over T}
 \ge {\|v_4-v_7\|^2\over2T}
 \ge {9\over128T}.
 \tag{5.5}
\]

Thus the leading singleton price in (4.7) is sharp even after replacing one
rank-one ramp by an arbitrary Hilbert family.

The actual Wave mass on (4.1) is

\[
\begin{aligned}
 \mathcal W_L={}&{1\over16}\log{9(L+1)\over L+9}
 +{1\over16}\log{9(2L+8)\over8(2L+9)}\\
 &+{9\over64}\log{(L+9)(2L+9)\over9(3L+9)}.
\end{aligned}
 \tag{5.6}
\]

It also has leading coefficient `9/64`.  Hence

\[
 \mathcal G_L-\mathcal W_L=O(1),
 \tag{5.7}
\]

whereas the ramp surplus has coefficient `9/128`.  The unused/nonpositive
finite-potential sector from C067 therefore cannot pay the missing ramp
surplus on this family.

## 6. Why the exact dual matrix `B` remains a live caveat

Let `B` have diagonal zero and
`B_(i,j)=-alpha_(i,j)/2` on Wave edges.  The ordered-Gram theorem gives

\[
 \boxed{\langle B,G_T\rangle=Q_n(T)\ge0.}
 \tag{6.1}
\]

`B` lies in the dual of the labeled ordered-root cone: its singleton values
are zero, its Wave-root values are `alpha_(i,j)`, and its other root values
are zero.  It is nevertheless indefinite as an ordinary coefficient matrix,
and `-B` leaves the ordered-root dual whenever a Wave edge is active.

This matters for the scope of (5.3).  The ramp chooses the positive baseline
`H=eta eta^T` and the legal residual `H-B`; it consequently pays the
singleton and adjacent surplus.  The matrix `B` itself has no such surplus.
But positivity of the auxiliary contraction `+Q_n(T)` does not turn it into
the needed negative term `-Q_n(T)` in the existing Cauchy master.  Appending
`+B` and then subtracting the same block simply returns the old master unless
the entire signed Gothic/cut ledger is simultaneously rewritten.

Therefore (5.3) closes the **ramp-baseline payment** from the positive Gothic
sector; it does not close a direct cell-labeled signed insertion of `B`.

## 7. Exact surviving obligation

The fixed three-channel shortcut is now excluded for four independent
reasons:

1. the ramp is not a full-prefix channel-space combination;
2. the continuum active scales cannot be replaced by the carrier's fixed one
   or two bands;
3. a zero-mass fourth channel preserves boundary normalization but still has
   a positive Schur/energy baseline and an explicit finite terminal; and
4. the full positive `lambda=beta` sector, including its unused negative
   potential, cannot pay that baseline on (4.1).

A surviving proof must instead do at least one of the following:

- use the exact labeled cells and `B` in one membership-sensitive signed
  whole-cut/Cauchy theorem;
- find a genuinely disjoint logarithmic reserve for the sharp singleton and
  terminal price;
- create cross-epoch or cross-phase cancellation with every gate boundary
  retained; or
- replace the fixed carrier by a larger legal master whose cover dual is
  computed rather than assumed.

In every case the `lambda=beta` Gothic rows must be rewritten, never added a
second time, and the C067 pair terminal plus the ramp gate terminal must each
have exactly one owner.  C058 and the global Erdős problem remain open.

## 8. Exact replay

From `route_probes/`, run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v \
  test_ramp_common_master_no_go_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 ramp_common_master_no_go_certificate.py \
  --verify ramp_common_master_no_go_certificate.json --self-check
```

The replay verifies the affine Golomb family, the formal non-span tensor,
the exact three-to-four-channel Schur calculation, the active-gate Abel
terminal, every rational density coefficient, the finite `L=2^18`
separation, the sharp Hilbert endpoint bound, the ordered-dual caveat,
byte-canonical JSON replay, and ten rejected semantic/hash mutations.

# Route C: centered multiband critical-history carrier

Date: 2026-08-29  
Status: `CONDITIONAL_CENTERED_CARRIER_ONLY_JOINT_SIGN_COUPLING_OPEN`

This note proves the centered covariance carrier and its internal single-owner
ledger, conditional on a compatible eventually `C`-critical dyadic history.
It does **not** prove the common signed capacity inequality coupling this
carrier to the harmonic-floor atoms.  Consequently C058 stays open, and no
Question 1, Question 2, publication-ready, prize, or novelty claim is made.

## 1. Critical schedule

Let `k_j=2^j`, let `A_j` be the first `k_j` marks in increasing spatial order,
and normalize `A_j` into `{0,...,N_j-1}`.  Assume eventually

\[
 N_j\le Ck_j^2\log(2k_j).
\]

Choose an explicit onset `j_0>=1` so that the critical cap holds and
`8C log(2k_j)>=1` for every `j>=j_0`.  Put

\[
q_j=2^{\lceil\log_2(8C\log(2k_j))\rceil},\qquad
T_j=k_jq_j=2^{s_j}.
\]

Then

\[
8C\log(2k_j)\le q_j<16C\log(2k_j).
\]

Since `log(2k_j)=(j+1)log 2`, its ratio at consecutive indices is
`(j+2)/(j+1)<2`.  Therefore `q_(j+1)/q_j` is `1` or `2`, and

\[
s_{j+1}-s_j\in\{1,2\}.
\tag{1.1}
\]

The rule depends only on `C,j`, not on future marks or a terminal horizon.
The exact certificate tests the equivalent rational surrogate
`q_j=ceilpow2(alpha*(j+1))` for four rational `alpha` values through `j=128`.

## 2. Centered first-use mass

For a finite set `A`, write

\[
C_T(A)=\|1_A*K_T\|_2^2-|A|/T
=2\sum_{d\in\Delta(A),\ d<T}{T-d\over T^2}.
\tag{2.1}
\]

Thus `0<=C_T(A)<1` for a Sidon set.  For the spatial prefix history define

\[
\widetilde\Delta_{j,T}=C_T(A_j)-C_T(A_{j-1})\ge0.
\]

The `k_j/2` adjacent gaps (using the global convention
`h_r=a_r-a_(r-1)`)

\[
h_r=a_r-a_{r-1},\qquad r=k_j/2,\ldots,k_j-1,
\]

all involve the newly born upper half.  Their sum is at most `N_j-1`.  If
fewer than `k_j/4` were at most `T_j/2`, their sum would exceed
`k_j T_j/8 >= C k_j^2 log(2k_j) >= N_j`.  Hence at least `k_j/4` are short.
Each contributes at least `1/T_j` in (2.1), so

\[
\boxed{\widetilde\Delta_{j,T_j}\ge{k_j\over4T_j}
={1\over4q_j}>{1\over64C\log(2k_j)}.}
\tag{2.2}
\]

The spatial-order qualification is essential: `A_(j-1)` is the lower half of
`A_j`, not an arbitrary insertion-order subset.

When this carrier is compared with the Wave-19 epoch `n`, the current prefix
has `k_j=2n` marks.  Thus the gaps in the display are exactly
`h_n,...,h_(2n-1)`, the full new gap block underlying `W_n`; using `k_j=n`
would introduce a one-epoch mismatch.

## 3. Multiband path and Fejer ownership

Let

\[
O_T(A)=\|1_A*(K_T-K_{2T})\|_2^2-|A|/(2T)
=C_T(A)-C_{2T}(A).
\]

Group the one or two bands selected by (1.1):

\[
X_j=\sum_{r=s_j}^{s_{j+1}-1}O_{2^r}(A_j)
=C_{T_j}(A_j)-C_{T_{j+1}}(A_j).
\tag{3.1}
\]

For `w_j=((J+1-j)/(J+1))^2`, exact reindexing gives

\[
\begin{aligned}
\sum_{j=j_0}^Jw_jX_j
={}&w_{j_0}C_{T_{j_0}}(A_{j_0})\\
&+\sum_{j>j_0}\{w_j\widetilde\Delta_{j,T_j}
 -(w_{j-1}-w_j)C_{T_j}(A_{j-1})\}\\
&-w_JC_{T_{J+1}}(A_J).
\end{aligned}
\tag{3.2}
\]

All reindexing and terminal losses total less than `1`.  More explicitly,

\[
\sum_{j=j_0}^J{w_j\over j+1}
\ge H_{J+1}-H_{j_0}-2
\ge \log(J+1)-H_{j_0}-2.
\tag{3.3}
\]

Combining (2.2) with (3.3) yields

\[
\boxed{\sum_jw_jX_j\ge {1\over64C\log2}\log J-O_C(1).}
\tag{3.4}
\]

This is a genuinely centered/off-diagonal carrier.  The exact replay checks
(2.1)--(3.2) on all 112 normalized four-mark Golomb rulers of span at most 12,
always using increasing spatial prefixes.  Its finite path uses scale jumps
`1` and `2`, so it executes both the one-band case and the two-band case whose
third kernel is at `4T`.

## 4. Fixed three-channel realization

Use the channels `(K_Tj,K_2Tj,K_T(j+1))`; when the scale jump is one, the last
two channels coincide and the second contrast vanishes.  Set

\[
D=\operatorname{diag}(1/4,1/2,1/4),\qquad \theta=3/25,
\]

and

\[
H=\begin{pmatrix}
13/100&3/25&0\\
3/25&13/50&3/25\\
0&3/25&13/100
\end{pmatrix}.
\]

The leading principal minors are

\[
13/100,\qquad97/5000,\qquad13/20000,
\]

so `H` is positive definite.  Both row-sum vectors equal
`gamma=(1/4,1/2,1/4)`, hence
`H^{-1}gamma=D^{-1}gamma=(1,1,1)`.  The exact retained identity is

\[
y^TDy-y^THy={3\over25}\{(y_1-y_2)^2+(y_2-y_3)^2\}.
\tag{4.1}
\]

The corresponding full retained-square gain is

\[
G_j={3\over25}B_j
 \sum_{r=s_j}^{s_{j+1}-1}\|1_{A_j}*(K_{2^r}-K_{2^{r+1}})\|_2^2.
\]

Its centered off-diagonal component is, by definition,

\[
G_j^{\rm off}:={3\over25}B_jX_j.
\]

The difference `G_j-G_j^off` is the zero-lag diagonal contribution.  It is
harmonic in `j`, not an `O_C(1)` error, and is kept separate throughout.

The constant full-support cover `z=gamma` has no inverse-metric price.  The
largest kernel has support `T_(j+1)`, so the exact site count is
`B_j=N_j+T_(j+1)-1`.  Since Sidon counting gives
`N_j>=1+k_j(k_j-1)/2`, the exact bound

\[
{B_j\over N_j}-1\le {4q_{j+1}\over k_j-1}=O_C(j/2^j)
\tag{4.2}
\]

makes the boundary replacement summable.  Indeed, because
`q_(j+1)<16C(j+2)log 2` and `|X_j|<1`, its absolute total is at most

\[
E_{C,j_0}:=64C\log2
 \sum_{j=j_0}^{\infty}{j+2\over2^j-1}
\le64C\log2\,{j_0+3\over2^{j_0-2}}.
\tag{4.3}
\]

Equations (3.4)--(4.3) give

\[
\sum_jw_j{G_j^{\rm off}\over N_j}
\ge {3\over1600C\log2}\log J-O_C(1).
\]

The safe coefficient `eta_C=3/(3200 C log 2)` clears the required floor:

\[
{3\over3200}-{1\over1536}={11\over38400}>0.
\tag{4.4}
\]

There is no hidden asymptotic constant: for every `J>=j_0`, one may take

\[
K_{C,j_0}={3(H_{j_0}+2)\over1600C\log2}
 +{3\over25}(1+E_{C,j_0})
\tag{4.5}
\]

and obtain

\[
\sum_{j=j_0}^Jw_j{G_j^{\rm off}\over N_j}
\ge {3\over3200C\log2}\log J-K_{C,j_0}.
\tag{4.6}
\]

## 5. Exact replay and remaining obstruction

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v test_centered_multiband_history_certificate.py
PYTHONDONTWRITEBYTECODE=1 python3 centered_multiband_history_certificate.py --verify centered_multiband_history_certificate.json --self-check
```

The JSON is deterministic, byte-canonical, hash-bound, semantically replayed,
and mutation tested.  The remaining obligation is not scalar positivity: it is
one common finite inequality/capacity map that places this centered covariance
carrier and the harmonic-floor atoms under opposite signs.  The uncentered
diagonal Parseval contribution is harmonic and must not be discarded as
`O(1)`.  C058 therefore remains open.

The companion `ROUTE_C_CROSS_RATIO_BOX_DIPOLE_BRIDGE.md` subsequently proves
an exact continuous-scale map from every Wave-19 cross ratio to a
nonnegative box-dipole tent, the pointwise first-use capacity bound, and the
finite-horizon `lambda=beta` Gothic coefficient match.  This narrows C058 but
does not close it: the matched `beta` atoms are already owned by the Gothic
bulk and must enter through a legal signed rewrite, not as a second payment.

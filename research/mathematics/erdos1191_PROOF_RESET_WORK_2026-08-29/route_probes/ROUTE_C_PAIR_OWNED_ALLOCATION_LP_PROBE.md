# Route C: pair-owned allocation LP and birth-supported transport

Date: 2026-08-30  
Status: `PAIR_POTENTIAL_LP_AND_OWNER_LIFT_SOLVED_SCALAR_AGGREGATE_TRANSPORT_NO_GO_PSD_PRICE_OPEN`

This note keeps the strict-interior interval pair which owns each positive
`beta` coefficient.  At that resolution the local scale allocation has an
explicit feasible solution, and the apparent adjacent-epoch sign gate
disappears algebraically: the negative coefficient is attached to the
pre-birth zero state of the pair.  What remains is not an epoch-flow LP but a
pair-weighted positive-semidefinite completion, its diagonal price, and the
finite scale terminal.  An exact nested-Sidon fixture below proves that
aggregating the owners into one scalar coefficient before transport is a
genuine loss and cannot always be repaired by a data-dependent fractional
choice below the universal envelope.

This is a scoped Route-C advance.  It does not insert the resulting
pair-weighted bands into the full Gothic signed ledger, pay their diagonal
completion, prove a compatible infinite history contradiction, resolve C058,
answer either Erdős question, or support a prize claim.

## 1. Positive potential owners at one Wave epoch

Fix a Wave epoch `n` and use the notation of
`ROUTE_C_CROSS_RATIO_BOX_DIPOLE_BRIDGE.md`.  Thus

\[
 H=D_{n,2n-1},\qquad
 F_H(d)=\int_0^H R_T(d)\,dT
 =\log(H/d)+d/H-1.
\]

Let

\[
 \Gamma_n=\{\gamma=(p,q):n+1\le p\le q\le2n-2\}
\]

be the strict-interior positive-potential owners, with
`d_gamma=D_(p,q)` and `beta_gamma=beta_n(p,q)`.  The complete mixed
difference table gives, for `0<T<=H`,

\[
 Q_n(T)=P_n(T)-N_n(T),\qquad
 P_n(T)=\sum_{\gamma\in\Gamma_n}\beta_\gamma R_T(d_\gamma),
 \tag{1.1}
\]

where `N_n(T)>=0` is the absolute contribution of the negative `lambda`
rows.  The positive full-span row is absent from (1.1), because its value is
`R_T(H)=0` on this finite interval.  Since `Q_n(T)>=0`,

\[
 0\le Q_n(T)\le P_n(T).
 \tag{1.2}
\]

Fix a logarithmic phase `theta`, put `T_r=2^(r+theta)`, and retain the
scales `T_r<=H`.  Define the demand and pair capacity

\[
 d_{n,r}=T_rQ_n(T_r),\qquad
 u_{\gamma,r}=T_r\beta_\gamma R_{T_r}(d_\gamma).
 \tag{1.3}
\]

The finite pair LP is

\[
 \sum_{\gamma}x_{\gamma,r}=d_{n,r},\qquad
 0\le x_{\gamma,r}\le u_{\gamma,r}.
 \tag{1.4}
\]

It is always feasible.  Indeed, if `P_n(T_r)>0`, take

\[
 \boxed{
 x_{\gamma,r}=u_{\gamma,r}{Q_n(T_r)\over P_n(T_r)}.}
 \tag{1.5}
\]

If `P_n(T_r)=0`, then (1.2) gives `d_(n,r)=0` and all variables may be
zero.  Thus no optimizer or compactness argument is needed.

The phase integral preserves each owner separately:

\[
 (\log2)\int_0^1\sum_{r:T_r\le H}u_{\gamma,r}\,d\theta
 =\beta_\gamma F_H(d_\gamma).
 \tag{1.6}
\]

Consequently

\[
 (\log2)\int_0^1\sum_{\gamma,r}x_{\gamma,r}\,d\theta
 =\mathcal W_n,
 \tag{1.7}
\]

and the unused positive-potential budget is exactly the negative-potential
part:

\[
 \boxed{
 \sum_{\gamma}\beta_\gamma F_H(d_\gamma)-\mathcal W_n
 =\sum_{\lambda_{p,q}<0}(-\lambda_{p,q})F_H(D_{p,q})\ge0.}
 \tag{1.8}
\]

Equations (1.5)--(1.8) are a singly owned allocation in the finite-potential
basis.  They are not permission to add `beta F_H` as a second resource on top
of `mathfrak B_n`: the whole `lambda` identity must replace the corresponding
Gothic rows, including the unused/negative part in (1.8).

## 2. Birth-supported owner lift removes the adjacent sign gate

The owner `gamma=(p,q)` represents the physical point pair

\[
 (a_{p-1},a_q).
\]

Both endpoint indices lie in the new dyadic block:

\[
 n\le p-1\le q\le2n-2.
 \tag{2.1}
\]

Hence this pair has one and only one birth epoch `b=b(gamma)`.  Indeed, the
dyadic new-index blocks partition the positive ranks, so the same physical
pair cannot become a strict-interior positive owner again at a later epoch.
With

\[
 v_{\gamma,r}=2R_{T_r}(d_\gamma),
\]

define its prefix-resolved state by

\[
 C^\gamma_{j,r}={\bf1}_{j\ge b}v_{\gamma,r},\quad
 O^\gamma_{j,r}=C^\gamma_{j,r}-C^\gamma_{j,r+1},\quad
 \Delta^\gamma_{j,r}=C^\gamma_{j,r}-C^\gamma_{j-1,r}.
 \tag{2.2}
\]

Thus `Delta^gamma_(j,r)` is supported only at `j=b`, and

\[
 O^\gamma_{b-1,r}=0,\qquad
 O^\gamma_{b,r}=v_{\gamma,r}-v_{\gamma,r+1}.
 \tag{2.3}
\]

Convert (1.5) into a coefficient of this pair state:

\[
 a_{\gamma,r}=
 \begin{cases}
 x_{\gamma,r}/v_{\gamma,r},&v_{\gamma,r}>0,\\
 0,&v_{\gamma,r}=0.
 \end{cases}
 \tag{2.4}
\]

Then

\[
 0\le a_{\gamma,r}\le {T_r\beta_\gamma\over2},\qquad
 \sum_\gamma a_{\gamma,r}v_{\gamma,r}=T_rQ_n(T_r).
 \tag{2.5}
\]

Put `s_(gamma,r)=sum_(t=L)^r a_(gamma,t)`.  Finite scale Abel summation gives

\[
 \sum_{r=L}^Ua_{\gamma,r}v_{\gamma,r}
 =\sum_{r=L}^Us_{\gamma,r}
   (O^\gamma_{b,r}-O^\gamma_{b-1,r})
  +s_{\gamma,U}v_{\gamma,U+1}.
 \tag{2.6}
\]

The first potentially active scale is finite because `R_T(d_gamma)=0` for
`T<=d_gamma`.

Now insert the coefficient row

\[
 a_{j,\gamma,r}={\bf1}_{j=b}a_{\gamma,r}
\]

into the exact prefix/scale transport formula.  At the preceding epoch edge
the formal coefficient is `-w_b s_(gamma,r)`, but it multiplies
`O^gamma_(b-1,r)=0`.  At the birth edge the coefficient is
`+w_b s_(gamma,r)` and multiplies `O^gamma_(b,r)`.  All later coefficient
rows vanish.  Therefore

\[
 \boxed{
 \text{the adjacent-epoch inequality }
 w_js_{j,r}\ge w_{j+1}s_{j+1,r}
 \text{ is unnecessary after retaining the owner label.}}
 \tag{2.7}
\]

This conclusion also covers finite epoch boundaries.  If `b` is the first
epoch, the initial negative boundary is zero by (2.3).  If `b` is the last
epoch, its terminal epoch row is precisely the positive birth row, not an
unpaid negative term.

## 3. Finite scale terminal and the explicit PSD price

Take `U=U(theta)` at the last phase width at most `H`.  The last
term of (2.6) must not be called `O(1)` by fiat.  It has the exact tail-band
representation

\[
 s_{\gamma,U}v_{\gamma,U+1}
 =\sum_{r>U}s_{\gamma,U}(v_{\gamma,r}-v_{\gamma,r+1}),
 \tag{3.1}
\]

because `v_(gamma,r)` tends to zero as `r` tends to infinity.  Thus the
terminal can be kept as one low-pass row or as a constant-coefficient
infinite band tail.

Owner-dependent band coefficients do not yet constitute the existing common
PSD master.  For one band let `z_u=delta_(a_u)*(K_T-K_(2T))`.  Then
`O^gamma_(b,r)=2<z_u,z_v>` for the endpoints of `gamma`.  Put
`m_(u,v)=w_b s_(gamma,r)>=0` on every allocated owner edge.  The exact
signless-Laplacian completion is

\[
 \sum_{u<v}m_{u,v}\|z_u+z_v\|_2^2
 =2\sum_{u<v}m_{u,v}\langle z_u,z_v\rangle
  +\sum_u\left(\sum_{v\ne u}m_{u,v}\right)\|z_u\|_2^2\ge0.
 \tag{3.2}
\]

The first term is the desired pair-weighted off-diagonal band.  Since
`||K_T-K_(2T)||_2^2=1/(2T)`, the added diagonal price at scale `r` is

\[
 {w_b\over T_r}\sum_\gamma s_{\gamma,r}.
 \tag{3.3}
\]

Including the tail (3.1), its exact total at a fixed phase is

\[
 \boxed{
 \mathcal D_{b,\theta}
 =2w_b\sum_{\gamma}\sum_{r\le U}
 {a_{\gamma,r}\over T_r}.}
 \tag{3.4}
\]

Indeed

\[
 \sum_{r=t}^U{1\over T_r}+{1\over T_U}={2\over T_t}.
\]

The terminal-tail portion alone is controlled: from (2.5),

\[
 {s_{\gamma,U}\over T_U}\le\beta_\gamma,\qquad
 \sum_{\gamma\in\Gamma_n}\beta_\gamma
 ={(n-1)^2\over4n^2}< {1\over4}.
 \tag{3.5}
\]

But (3.4) can accumulate over all active scales.  No current theorem pays
this diagonal price with a disjoint signed reserve.  Thus (2.7) removes the
aggregate epoch sign gate but does not close the PSD/diagonal gate.

## 4. Exact scalar-aggregation no-go on a nested Sidon pair

The owner lift above is not equivalent to choosing one scalar coefficient
for the whole first-use increment.  Consider the nested prefixes

\[
\begin{aligned}
 A^-={}&(0,1,3,7,12,20,30,44),\\
 A^+={}&(0,1,3,7,12,20,30,44,1044,1094,2095,2155,\\
      &\hspace{41mm}2225,2305,2395,2495).
\end{aligned}
 \tag{4.1}
\]

They are Golomb/Sidon prefixes.  For an exact short audit, the 28 positive
differences inside `A^-` are

\[
 1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,19,20,23,24,
 27,29,30,32,37,41,43,44.
\]

The 28 differences within the new eight-point block are

\[
 50,60,70,80,90,100,130,150,170,190,210,240,270,300,
 340,400,1001,1051,1061,1111,1131,1181,1211,1261,1301,
 1351,1401,1451.
\]

The 64 cross differences occur in the eight disjoint intervals
`[b-44,b]`, one for each new mark `b`.  The only possible intersections with
the displayed new-block list in the first two intervals are `1001,1051,1061`;
directly, the two cross rows are

\[
 \{1000,1014,1024,1032,1037,1041,1043,1044\},
\]

\[
 \{1050,1064,1074,1082,1087,1091,1093,1094\},
\]

so there is no collision.  The third cross interval starts at `2051`, above
all remaining new-block differences.  Hence all 120 differences in `A^+`
are distinct.

Let `n_-=4`, `n_+=8`.  For the preceding epoch,

\[
 H_-=D_{4,7}=44-7=37.
 \tag{4.2}
\]

Suppose one attempts the scalar LP from the phase-transport note, even with
arbitrary data-dependent coefficients:

\[
 0\le c_{j,r}(\theta)\le
 {T_r\over2n_j^2}{\bf1}_{T_r\le H_j},
 \tag{4.3}
\]

\[
 D_j(\theta):=\sum_rT_rQ_{n_j}(T_r)
 \le\sum_rc_{j,r}(\theta)\widetilde\Delta_{j,r},
 \tag{4.4}
\]

and

\[
 w_-s_{-,r}(\theta)\ge w_+s_{+,r}(\theta)
 \quad\hbox{for every }r,\qquad
 s_{j,r}=\sum_{t\le r}c_{j,t}.
 \tag{4.5}
\]

Take the consecutive Fejer-weight ratio

\[
 {w_-\over w_+}={100\over81};
 \tag{4.6}
\]

for example, the actual `j=3,4` rows at horizon `J=12`.

For every phase, the total preceding capacity satisfies

\[
 s_{-,\infty}\le {H_-\over n_-^2}={37\over16}.
 \tag{4.7}
\]

For `A^+`, the 92 first-use differences are the 28 new-new differences and
the 64 old-new differences.  If their increasing order is
`d_1<...<d_92` and `S_m=sum_(i<=m)d_i`, then on
`d_m<=T<=d_(m+1)` one has exactly

\[
 \widetilde\Delta_+(T)={2(mT-S_m)\over T^2}.
 \tag{4.8}
\]

Its only interior critical point is `T=2S_m/m`.  Exact substitution of the
sets displayed above gives the following three finite checks:

\[
\begin{array}{c|c|c|c}
 m\text{ range}&\max\widetilde\Delta_+&m&T\\ \hline
 1\le m\le16&18/385&12&770/3\\
 17\le m\le44&11/389&44&1556\\
 45\le m\le92&2116/71445&92&71445/23.
\end{array}
\]

Therefore

\[
 \boxed{\sup_{T>0}\widetilde\Delta_+(T)={18\over385}.}
 \tag{4.9}
\]

Letting `r` tend to infinity in (4.5), equations (4.4), (4.7), and
(4.9) imply, phase by phase (and hence after integration),

\[
 \int_0^1D_+(\theta)\,d\theta
 \le {18\over385}{100\over81}{37\over16}
 ={185\over1386}.
 \tag{4.10}
\]

On the other hand, the exact continuum-phase identity says

\[
 \int_0^1D_+(\theta)\,d\theta={\mathcal W_8\over\log2}.
 \tag{4.11}
\]

Seven positive cross-ratio atoms already contradict (4.10).  Their
`(i,j)`, coefficient, and cross-ratio are

\[
\begin{array}{c|c|c}
(i,j)&\alpha_{ij}&\exp(C_{ij})\\ \hline
(8,10)&1/64&3153/293\\
(10,15)&25/256&5204/4203\\
(10,14)&1/16&1730/1301\\
(10,13)&9/256&261/173\\
(10,12)&1/64&1061/522\\
(8,15)&49/256&3411301/3311301\\
(13,15)&1/64&323/243.
\end{array}
\]

Using `log x>=2(x-1)/(x+1)`, their contributions are respectively at
least

\[
 {715\over27568},\ {25025\over1204096},\ {429\over24248},
 {99\over6944},\ {539\over50656},\ {153125\over26890408},
 {5\over1132}.
\]

These are termwise larger than

\[
 {1\over40},{1\over50},{1\over60},{1\over72},{1\over100},
 {1\over180},{1\over230},
\]

whose sum is

\[
 {494\over5175}>{37\over396}
 \quad\left(\text{gap }{461\over227700}\right).
 \tag{4.12}
\]

Finally `log2<7/10`, since the first four terms of the exponential series
give

\[
 e^{7/10}>1+{7\over10}+{49\over200}+{343\over6000}
 ={12013\over6000}>2.
\]

Thus (4.10) would force

\[
 \mathcal W_8\le {185\over1386}\log2
 <{37\over396},
\]

while (4.12) gives `mathcal W_8>37/396`, a contradiction.

Therefore no measurable family of scalar coefficients can satisfy
(4.3)--(4.5) on this nested Sidon pair.  This rules out not only the full
universal profile but every data-dependent fractional scalar allocation
below it, even after the exact continuum-phase average.  It does not rule out
the owner-resolved construction in Sections 1--3.

## 5. Exact remaining LP/master obligation

The useful conclusion is a separation of issues:

1. **Solved locally:** the positive finite-potential rows admit the explicit
   pair allocation (1.5), with exact phase budget and residual identity
   (1.6)--(1.8).
2. **Solved algebraically across births:** preserving the unique pair owner
   makes the preceding negative epoch coefficient multiply a zero state, so
   the adjacent scalar sign gate is not a genuine owner-level obstruction.
3. **Closed as a universal fallback:** aggregating all owners into one scalar
   `c_(j,r)` and trying any fractional profile below the pointwise envelope
   fails on the exact nested Sidon fixture (4.1).
4. **Still open:** place the pair-weighted off-diagonal bands into one legal
   signed master while paying (3.4), or prove a sharper PSD completion whose
   diagonal price is absorbed by a singly owned negative/terminal reserve.
   The finite tail (3.1), the unused negative potential (1.8), and every
   original Gothic row must each have exactly one owner.

Longer epoch transport, a genuinely signed whole-cut identity, a different
PSD completion, or another Route-C/D mechanism remain logically available.
Nothing here proves C058 or either Erdős question.

## 6. Exact certificate

The companion files

- `pair_owned_allocation_certificate.py`,
- `pair_owned_allocation_certificate.json`, and
- `test_pair_owned_allocation_certificate.py`

replay the proportional LP on exact dyadic scales, the prebirth-zero and
finite-terminal identities, the diagonal-price summation, all 120 distinct
differences of (4.1), the 92 first-use differences, the exact supremum
`18/385`, and the rational contradiction gap `461/227700`.  The focused suite
passes 10 tests, deterministic semantic/byte replay, and seven mutation
rejections.  Payload SHA-256:

`25a84d6a534cb0be83d851b312579c3253268064b24b209e93a8bddee327d618`.

The certificate's universal statements remain tied to the displayed human
proofs; finite fixtures are not substituted for the quantified algebra.  Its
scope flags keep the PSD payment, Gothic rewrite, C058, both Erdős questions,
and every prize claim false.

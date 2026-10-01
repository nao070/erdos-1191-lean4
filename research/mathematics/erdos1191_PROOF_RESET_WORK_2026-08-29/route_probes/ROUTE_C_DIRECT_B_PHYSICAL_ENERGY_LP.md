# Route C: direct-`B` physical Haar-energy LP

**Status:** exact finite physical-objective primal/dual certificate; strict
two- and three-epoch savings on stated common-scale fixtures; exact nearby-scale
countercheck; no universal paid ledger.

The earlier membership-SDDM probe minimized coefficient trace.  That was the
correct objective for its stated finite target, but it was not the actual
Haar translation energy: a root with coefficient-trace cost `2` can have
physical cost as large as `3`.  This note replaces that objective by the
exact cell-length-weighted quantity requested for a physical common carrier.

Sections 1--7 use `T=200`, `mu=1`; Section 8 states its own widths and keeps
`mu=1`.  In every fixture,

\[
 C=\sum_{i<j}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T},
 \qquad w_{ij}\ge0,
 \tag{1}
\]

and all Haar cells use the same half-open box convention as C079--C083.  Thus
`C` is a singular positive-semidefinite graph Laplacian.  No positive
definiteness claim is made.

## 1. The exact physical objective

Put

\[
 h_T=K_T-K_{2T},\qquad
 g_T=2T h_T=\mathbf1_{[0,T)}-\mathbf1_{[T,2T)}.
\]

On an actual atomic cell `c`, let `v_c` be the vector of translated values of
`g_T`, and for block `s` write

\[
 s_{c,s}=\sum_{i\in S_s}v_{c,i}.
\]

The new objective is

\[
 \boxed{
 \mathcal E(C,\kappa)
 =\sum_c\frac{|c|}{2T}
 \left(v_c^{\mathsf T}Cv_c+
       \sum_s\kappa_s s_{c,s}^2\right).}
 \tag{2}
\]

Because `v=2T h`, this is exactly `2T` times the integrated Haar correction
energy.  It is not the coefficient-trace objective and is not approximated by
one in the certificate.

The pointwise constraints remain

\[
 v_c^{\mathsf T}Cv_c+\sum_s\kappa_s s_{c,s}^2
 \ge v_c^{\mathsf T}M_{\rm total}v_c
 \quad\text{for every actual cell }c.
 \tag{3}
\]

Both zero exterior cells are included.  Their state and every term in (2)--
(3) vanish.

## 2. Exact root cost: the three-piece tent

For `d>=0`, let

\[
 A_T(d)=\int g_T(x)g_T(x-d)\,dx.
\]

Direct overlap of the positive and negative half-boxes gives

\[
 A_T(d)=
 \begin{cases}
 2T-3d,&0\le d\le T,\\
 d-2T,&T\le d\le2T,\\
 0,&d\ge2T.
 \end{cases}
 \tag{4}
\]

Since `||g_T||_2^2=2T`, the physical coefficient of one root is

\[
 \chi_T(d)
 :=\frac1{2T}\int(g_T(x)-g_T(x-d))^2\,dx
 =2-\frac{A_T(d)}T.
\]

Therefore

\[
 \boxed{
 \chi_T(d)=
 \begin{cases}
 3d/T,&0\le d\le T,\\
 4-d/T,&T\le d\le2T,\\
 2,&d\ge2T.
 \end{cases}}
 \tag{5}
\]

In particular, `chi_T(T)=3`, which is the missing distinction from the
constant root trace `2`.

Equivalently, with `x=d/T`,

\[
 \rho_T(d):=2T\langle h_T,\tau_dh_T\rangle
 =\begin{cases}
 1-3x/2,&0\le x\le1,\\
 x/2-1,&1\le x\le2,\\
 0,&x\ge2,
 \end{cases}
\]

and `chi_T(d)=2-2rho_T(d)`.  For a block `S`, the exact aggregate cost is

\[
 \Gamma_T(S)
 =\frac1{2T}\int\left(\sum_{i\in S}g_T(x-b_i)\right)^2dx
 =|S|+2\sum_{i<j}\rho_T(|b_i-b_j|).
 \tag{6}
\]

The generator independently obtains every root and aggregate coefficient by
summing the complete atomic cells.  It checks (5) exactly on 456 integer
parameter rows, including both breakpoints, and on every root used below.

## 3. Exact physical LP dual

For cell multiplier `y_c>=0`, the dual root constraint is now

\[
 \sum_c y_c(v_{c,i}-v_{c,j})^2\le\chi_T(|b_i-b_j|),
 \tag{7}
\]

and each aggregate constraint is

\[
 \sum_c y_c s_{c,s}^2\le\Gamma_T(S_s).
 \tag{8}
\]

The dual objective is

\[
 \sum_c y_c\,v_c^{\mathsf T}M_{\rm total}v_c.
 \tag{9}
\]

The displayed `y_c` values below are abstract LP multipliers, not cell
lengths or physical measures.  Every unlisted multiplier is zero.

There is also a canonical, non-optimized dual point that explains the signed
demand lower bound.  Set

\[
 \bar y_c=\frac{|c|}{2T}
\]

on every finite cell and zero on the two exteriors.  By the definitions of
`chi_T` and `Gamma_T`, its root loads equal every root cost in (7), and its
aggregate loads equal every aggregate cost in (8).  It is therefore dual
feasible, with objective

\[
 \sum_c\frac{|c|}{2T}v_c^{\mathsf T}M_{\rm total}v_c,
\]

the weighted signed Haar-band demand.  Hence that demand is automatically a
lower bound for every feasible physical correction in this LP.  The
certificate checks all these column equalities exactly for each fixture.  The
surpluses reported below measure the improvement from this canonical lower
bound to the optimized dual/primal value; they are not unspent capacity.

## 4. Separate `n=4` optimum

Use

\[
 (309,416,525,636,749).
\]

All 16 real-line cells from the stable membership bundle are replayed.  The
aggregate cost is

\[
 \Gamma_4=3.
\]

The exact primal point is

\[
 w_{02}=w_{24}=\frac1{40},\qquad \kappa_4=0.
 \tag{10}
\]

The two active root costs are

\[
 \chi(216)=\frac{73}{25},\qquad
 \chi(224)=\frac{72}{25},
\]

so

\[
 \mathcal E_4
 =\frac1{40}\left(\frac{73}{25}+\frac{72}{25}\right)
 =\frac{29}{200}.
 \tag{11}
\]

An exact dual is

\[
\begin{array}{c|c}
\text{cell}&y_c\\ \hline
[525,616)&349/1000\\
[636,709)&713/3000\\
[749,816)&209/1000\\
[836,925)&1093/3000
\end{array}
 \tag{12}
\]

All ten root loads satisfy (7); the `(0,2)` and `(2,4)` loads equal their
respective costs `73/25` and `72/25`.  The aggregate load is

\[
 \frac{107}{150}<3.
\]

The dual value equals `29/200`, proving

\[
 \boxed{\min\mathcal E_4=\frac{29}{200}.}
 \tag{13}
\]

The weighted signed direct-`B` demand is `63/640`; hence the pointwise cover
has physical surplus `149/3200`.  This surplus is a cost difference inside
the LP, not a newly owned positive budget.

## 5. Separate `n=8` optimum

Use the next consecutive block from the finite Golomb fixture
`a_k=k(k+100)`, `0<=k<=15`:

\[
 (749,864,981,1100,1221,1344,1469,1596,1725).
\]

All 28 real-line cells are replayed, and

\[
 \Gamma_8=\frac{97}{25}.
\]

The exact primal is

\[
 w_{02}=w_{68}=\frac1{128},\qquad \kappa_8=0.
 \tag{14}
\]

Here the active distances are `232` and `256`, with costs `71/25` and
`68/25`.  Thus

\[
 \mathcal E_8
 =\frac1{128}\left(\frac{71}{25}+\frac{68}{25}\right)
 =\frac{139}{3200}.
 \tag{15}
\]

The exact dual is

\[
\begin{array}{c|c}
\text{cell}&y_c\\ \hline
[981,1064)&217/800\\
[1100,1149)&351/800\\
[1725,1744)&157/800\\
[1796,1869)&387/800
\end{array}
 \tag{16}
\]

The active edge loads equal `71/25` and `68/25`; all other root loads are
below their exact costs.  The aggregate load is

\[
 \frac{151}{200}<\frac{97}{25}.
\]

Primal and dual values agree, so

\[
 \boxed{\min\mathcal E_8=\frac{139}{3200}.}
 \tag{17}
\]

The weighted signed demand and cover surplus are respectively `169/12800`
and `387/12800`.

## 6. Joint `n=4/n=8` common-scale optimum

Deduplicate the shared endpoint `749`, giving the 13-point union

\[
 (309,416,525,636,749,864,981,1100,1221,1344,1469,1596,1725).
\]

All 40 real-line cells are imposed on the signed sum `M_4+M_8`.  The two
aggregate costs remain `3` and `97/25`.  An exact joint primal is

\[
\begin{aligned}
 w_{02}&=\frac{45}{1792},&
 w_{24}&=\frac{11}{448},\\
 w_{46}&=\frac3{1792},&
 w_{10,12}&=\frac1{128},\\
 \kappa_4&=0,&\kappa_8&=0.
\end{aligned}
 \tag{18}
\]

The four active root costs are, in the same order,

\[
 \frac{73}{25},\quad\frac{72}{25},\quad
 \frac{71}{25},\quad\frac{68}{25}.
\]

Consequently

\[
 \mathcal E_{4,8}^{\rm joint}=\frac{3809}{22400}.
 \tag{19}
\]

An exact joint dual is

\[
\begin{array}{c|c@{\qquad}c|c}
\text{cell}&y_c&\text{cell}&y_c\\ \hline
[525,616)&5297/15400 &[636,709)&623/2200\\
[749,816)&3529/15400 &[836,864)&401/2200\\
[981,1036)&1249/3850 &[1036,1064)&7/1760\\
[1100,1149)&223/800 &[1725,1744)&283/600\\
[1796,1869)&5/24&&
\end{array}
 \tag{20}
\]

All 78 root loads are at most their exact costs.  The four positive-primal
roots meet their costs exactly, as complementary slackness requires.  Five
inactive roots `(0,1)`, `(1,3)`, `(3,6)`, `(4,5)`, and `(9,12)` are also
tight because the optimum is dual-degenerate; no positive primal weight is
inferred for them.  The aggregate loads are

\[
 \frac{16221}{7700}<3,
 \qquad
 \frac{15929}{16800}<\frac{97}{25}.
\]

The dual objective splits strictly positively between the two epochs:

\[
 \underbrace{\frac{727}{5600}}_{n=4}
 +\underbrace{\frac{901}{22400}}_{n=8}
 =\frac{3809}{22400}.
 \tag{21}
\]

This proves the exact joint optimum (19).  The weighted signed direct demand
is

\[
 400\left(\frac{63}{256000}+\frac{169}{5120000}\right)
 =\frac{1429}{12800},
\]

and the pointwise-cover surplus is `5233/89600`.

The shared coordinate is represented once in the single global matrix `C`.
This is an accounting statement only: no external budget owner is supplied.

## 7. Joint versus separate

Embedding (10) and (14) in the union gives the exact jointly feasible root
weights

\[
 w_{02}=w_{24}=\frac1{40},\qquad
 w_{46}=w_{10,12}=\frac1{128}.
\]

Their physical objective is the sum of the separate optima,

\[
 \frac{29}{200}+\frac{139}{3200}
 =\frac{603}{3200}
 =\frac{4221}{22400}.
\]

Comparison with (19) gives

\[
 \boxed{
 \mathcal E_{4,8}^{\rm joint}
 <\mathcal E_4+\mathcal E_8,
 \qquad
 (\mathcal E_4+\mathcal E_8)-\mathcal E_{4,8}^{\rm joint}
 =\frac{103}{5600}.}
 \tag{22}
\]

The inequality is strict because the joint LP is required to dominate only
the signed sum `M_4+M_8` on each union cell, not to dominate each epoch
separately.  A single global root correction can therefore serve aligned
demands from both epochs.  Concretely, the expensive separate `n=8` weight
`w_46=1/128` falls to `3/1792`, with small compensating changes in the two
earlier roots.

This is a genuine two-active-epoch saving, but it is not automatically a
global payment mechanism.  In particular, summing signed demands can exploit
local cancellation that may fail to persist across other scales, phases, or
epoch configurations.

## 8. Exact three-epoch extension and a scale countercheck

The same finite program remains exactly solvable with three genuinely active
consecutive epochs.  Use

\[
 a_k=k(k+1000),\qquad 0\le k\le31,
\]

at common scale `T=2000`.  Exact enumeration verifies all `496` positive
differences are distinct.  The three blocks are

\[
 \{a_3,\ldots,a_7\},\qquad
 \{a_7,\ldots,a_{15}\},\qquad
 \{a_{15},\ldots,a_{31}\},
\]

with sizes `n=4,8,16`.  Deduplication gives 29 union coordinates and 88
complete real-line cells.  The direct-`M` pair supports are disjoint; only the
two consecutive endpoints are shared.

The physical aggregate costs are

\[
 \Gamma_4=3,\qquad
 \Gamma_8=\frac{386}{125},\qquad
 \Gamma_{16}=\frac{444}{125}.
\]

### 8.1 Separate physical optima

Exact primal/dual zero gaps give

\[
 \boxed{
 \mathcal E_4^{\rm sep}=\frac{299}{2000},\quad
 \mathcal E_8^{\rm sep}=\frac{1489}{32000},\quad
 \mathcal E_{16}^{\rm sep}=\frac{1477}{128000}.}
 \tag{23}
\]

The sparse separate primals are

- `n=4`: `w_02=w_24=1/40`;
- `n=8`: `w_02=w_68=1/128`;
- `n=16`: `w_02=w_(14,16)=1/512`;

with all aggregate coefficients zero.  The `n=16` active root costs are
`371/125` and `147/50`.  Its exact dual uses

\[
\begin{array}{c|c}
\text{cell}&y_c\\ \hline
[17289,18256)&2837/8000\\
[18324,19225)&3099/8000\\
[31961,32784)&2697/8000\\
[32900,33841)&3183/8000
\end{array}
\]

and has aggregate load `301/400 < 444/125`.  The generator stores and checks
the corresponding exact four-cell duals for `n=4` and `n=8` as well.

The separate weighted signed demands are

\[
 \frac{783}{6400},\qquad
 \frac{3769}{128000},\qquad
 \frac{3333}{512000}.
\]

### 8.2 Joint three-epoch optimum

On the 29-point union, an exact primal is

\[
\begin{aligned}
 w_{02}&=\frac{45}{1792},&
 w_{24}&=\frac{11}{448},&
 w_{46}&=\frac3{1792},\\
 w_{10,12}&=\frac1{128},&
 w_{26,28}&=\frac1{512},&
 \kappa_4&=\kappa_8=\kappa_{16}=0.
\end{aligned}
 \tag{24}
\]

The five active root costs are

\[
 \frac{374}{125},\quad\frac{747}{250},\quad
 \frac{373}{125},\quad\frac{743}{250},\quad\frac{147}{50}.
\]

The exact joint dual is

\[
\begin{array}{c|c@{\qquad}c|c}
\text{cell}&y_c&\text{cell}&y_c\\ \hline
[5025,6016)&270559/840000 &[6036,7009)&38303/120000\\
[7049,8016)&23323/105000 &[8036,8064)&3071/15000\\
[9081,10036)&14443/56000 &[10100,11049)&3051/8000\\
[15225,16144)&3081/8000 &[16196,16256)&49547/168000\\
[18324,19225)&661/2625 &[31961,32784)&3177/8000\\
[32900,33841)&2703/8000&&
\end{array}
 \tag{25}
\]

Every one of the 406 root loads is at most its physical cost.  The five
positive roots in (24) are tight.  Six inactive roots `(0,1)`, `(2,12)`,
`(3,4)`, `(5,6)`, `(10,11)`, and `(26,27)` are also tight by dual
degeneracy.  The three aggregate loads are

\[
 \frac{162947}{84000}<3,\qquad
 \frac{2463}{2000}<\frac{386}{125},\qquad
 \frac{171011}{168000}<\frac{444}{125}.
\]

The dual objective has a strictly positive contribution from every epoch:

\[
 \frac{7477}{56000}
 +\frac{1979}{48000}
 +\frac{20723}{2688000}
 =\frac{163481}{896000}.
\]

It equals the physical cost of (24), proving

\[
 \boxed{\mathcal E_{4,8,16}^{\rm joint}
 =\frac{163481}{896000}.}
 \tag{26}
\]

The total weighted signed demand is `81049/512000`; the exact pointwise-cover
surplus is `86581/3584000`.  As before, the canonical cell-length dual proves
the demand lower bound, while the optimized dual proves (26).

### 8.3 Strict three-epoch saving

Embedding all three separate sparse corrections is jointly feasible and has
objective

\[
 \frac{299}{2000}+\frac{1489}{32000}+\frac{1477}{128000}
 =\frac{26569}{128000}
 =\frac{185983}{896000}.
\]

Therefore

\[
 \boxed{
 (\mathcal E_4^{\rm sep}+\mathcal E_8^{\rm sep}
 +\mathcal E_{16}^{\rm sep})
 -\mathcal E_{4,8,16}^{\rm joint}
 =\frac{11251}{448000}>0.}
 \tag{27}
\]

This extends the two-epoch phenomenon: one global correction of the signed
sum can be strictly cheaper than separately dominating every epoch.

### 8.4 The same sparse weights fail at `T=2500`

The exact three-epoch construction is not a scale-independent recurrence.
Keep the weights (24), change only to `T=2500`, and inspect the actual cell

\[
 [6036,6516).
\]

Its 29-coordinate state is `(-1,1,1,1,0,...,0)`.  Exact evaluation gives

\[
 v^{\mathsf T}Cv=\frac18,\qquad
 v^{\mathsf T}(M_4+M_8+M_{16})v=\frac9{32},
\]

so

\[
 \boxed{\text{slack}=\frac18-\frac9{32}=-\frac5{32}<0.}
 \tag{28}
\]

Thus the fixed sparse `T=2000` weights fail even on one nearby scale.  This
refutes only their literal scale-independent reuse.  It does not refute a
different `T=2500` correction, scale-dependent weights, or a genuine
cross-scale recurrence.

There is a second, independent history-compatibility boundary.  For the
structured family `a_k=k(k+C)` with fixed integer `C`, one has

\[
 a_3-a_0=3C+9=a_{C+5}-a_{C+4}.
\]

Hence it cannot itself provide a compatible infinite Sidon history.  Raising
`C` to obtain arbitrary finite depth changes all earlier marks and also the
chosen scale `T`; such experiments remain C065-style changing-family
evidence, not one fixed-prefix recurrence.

## 9. Strict boundary

The certificate proves only:

1. the exact physical root-cost theorem (5);
2. exact physical-objective optima inside the root-SDDM-plus-`J` LP for the
   stated `n=4`, `n=8`, and joint fixtures at `T=200`, `mu=1`;
3. the exact strict joint saving (22);
4. the fixed finite three-epoch optima and saving (23)--(27), together with
   the fixed-weight `T=2500` countercheck (28).

It does **not** prove:

- a uniform result for arbitrary Golomb or Sidon configurations;
- a correction valid simultaneously at all dyadic scales or log phases;
- a scale-universal recurrence from the fixed `T=2000` sparse weights or the
  changing quadratic finite family;
- optimality among arbitrary PSD, indefinite, signed, or nonlinear repairs;
- payment by an already-owned Gothic, birth, phase, cross-scale, or external
  reserve budget;
- C058, Q1, Q2, or Erdős Problem #1191;
- publication novelty or prize eligibility.

The main next question is therefore no longer the local physical cost: it is
whether the strict joint saving can be organized coherently across every
active scale and charged once to a legal disjoint resource.

## 10. Reproducibility

The exact bundle consists of

- `direct_b_physical_energy_lp_certificate.py`;
- `direct_b_physical_energy_lp_certificate.json`;
- `test_direct_b_physical_energy_lp_certificate.py`.

The final certificate requires no numerical optimization package.  Floating
LP output was used only to discover active supports.  Every retained primal,
dual, cell constraint, root cost, aggregate cost, complementary-slackness
identity, and comparison is replayed using `fractions.Fraction`.  Verification
also enforces literal raw-byte equality with the deterministic JSON and
rejects scoped semantic mutations.

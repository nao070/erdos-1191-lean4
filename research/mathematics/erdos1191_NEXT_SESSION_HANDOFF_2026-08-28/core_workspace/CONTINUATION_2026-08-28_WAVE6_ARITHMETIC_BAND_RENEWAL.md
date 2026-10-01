# Wave 6 continuation: arithmetic band renewal

**Date:** 2026-08-28  
**Global status:** UNRESOLVED_AT_HARD_LIMIT  
**Prize-claim status:** not ready  
**Authority:** this note consolidates the current Wave 6 arithmetic results and
supersedes any interpretation of a finite empirical Hall pattern as a
conjectural law.

Certificate and source hashes are fixed in the finalized package manifest and
Wave 6 verification report. No theorem below depends on a hash.

## 1. Outcome

Wave 6 does not resolve Erdős Problem #1191. It replaces the qualitative
reset-renewal target by an exact integer-band ledger and identifies the
remaining endpoint failure.

1. The birth-lag Hall construction gives one universal exact statement:
   every selected family demand contained in an integer interval is at most
   the interval's inclusive capacity. Equivalently, its Hall pressure is at
   most one.
2. A seeded heuristic search found a 128-mark ruler. After discovery, all
   8,128 differences and every prefix of its critical C=1 envelope were
   audited exactly. The witness is an exact finite object, but the search was
   not exhaustive.
3. The stronger finite pattern
   \(\Lambda_{NN}(n,2n)\leq1/(4\sqrt n)\), seen in 22 serialized transition
   rows, is false. One exactly audited 64-mark C=1 Golomb ruler violates it at
   three consecutive transitions, beginning with
   \(\Lambda_{NN}(8,16)=9/14\).
4. Cross-boundary Theorems A--D count newborn-shell and old--new
   anti-diagonal differences across all available dyadic epochs. Their
   integrated endpoint budget is exact but only logarithmic.
5. The same sixteen-mark ruler survives three strongly negative resets with
   nearly uniform newborn shells and positive normalized innovation. Three
   cycles therefore cannot prove the desired collision.
6. A residue lift makes the one-point forbidden shadow occupy at most four
   residue classes. Growing compatible finite windows retain
   \(1/360+o(1)\) innovation per transition while their total local shadow
   density is \(o(1)\).
7. The bounded literature delta found no checked theorem giving either a
   compatible critical all-prefix integer Sidon tower or the missing
   \(o(\log J)\) renewal/innovation budget.

The surviving issue is not whether individual epochs obey an integer
capacity bound. They do. The issue is whether a single globally compatible
Sidon sequence can repeatedly move the active cutoff to fresh numerical
bands without paying an old-history charge.

## 2. Common notation

Let

\[
A=(0=a_0<a_1<a_2<\cdots)
\]

be a normalized integer ruler. Put

\[
h_0=1,\qquad h_i=a_i-a_{i-1}\ (i\geq1),
\qquad
N_n=a_{n-1}+1=\sum_{i=0}^{n-1}h_i.
\tag{1}
\]

The Golomb condition says that all positive mark differences are distinct.
Equivalently, all contiguous sums of the genuine gaps
\((h_1,h_2,\ldots)\) are distinct.

At a dyadic boundary \(m\), define

\[
G_m=N_{2m}-N_m,\qquad
\mu_m^-={N_m\over m},\qquad
\mu_m^+={G_m\over m},
\tag{2}
\]

\[
D_m^-=\max_{0\leq r\leq m}|N_r-r\mu_m^-|,
\qquad
D_m^+=\max_{0\leq s\leq m}
 |N_{m+s}-N_m-s\mu_m^+|.
\tag{3}
\]

For a real interval \([L,U]\), its exact positive-integer capacity is

\[
\operatorname{cap}_+(L,U)
=\max\{0,\lfloor U\rfloor-\max(1,\lceil L\rceil)+1\}.
\tag{4}
\]

## 3. Exact birth-lag Hall theorem

Consider a finite power-of-two-mark ruler. A pair of zero-based ranks
\((i,r)\), \(i<r\), is assigned to the first dyadic prefix containing its
right endpoint. If that birth epoch is \(n\), then
\(n/2\leq r<n\). Its category is

- ON when \(i<n/2\), so the pair crosses the epoch boundary;
- NN when \(n/2\leq i<r\), so both endpoints are newborn;

and its rank lag is \(\ell=r-i\). These data partition every rank pair into
families

\[
\mathcal F_{n,c,\ell}.
\tag{5}
\]

For a family \(F\), let \(q_F\) be its number of pairs and let
\([L_F,U_F]\) be the inclusive integer hull of its numerical differences.
For an integer interval \(K=[L,U]\), define the contained demand

\[
\mathcal D(K)=
\sum_{F:\,[L_F,U_F]\subseteq K}q_F,
\qquad
\Lambda=\max_K{\mathcal D(K)\over U-L+1}.
\tag{6}
\]

### Hall birth-lag theorem

If the ruler is Golomb, then

\[
\boxed{\mathcal D(K)\leq U-L+1\quad\hbox{for every }K,}
\qquad
\boxed{\Lambda\leq1.}
\tag{7}
\]

Every pair counted in \(\mathcal D(K)\) contributes a distinct integer in
\(K\), which proves (7). The endpoint scan implemented in
endpoint_variance/wave6_arithmetic_mining_search.py is complete, not sampled:
any positive-demand interval can be shrunk to the smallest interval spanning
the family hulls it contains. This cannot lose a contained family and cannot
decrease the pressure. Thus a maximizer has endpoints among the recorded
family endpoints.

Equation (7) is universal for the stated finite dyadic partition. It is the
only Hall-pressure bound promoted to theorem.

### Closed empirical strengthening

The mining certificate contains 22 Golomb transition rows for which

\[
16n\Lambda_{NN}(n,2n)^2\leq1.
\tag{8}
\]

That finite observation is not a law. For the sixteen-mark ruler in Section
6, the epochs \(8,16\), category NN, minimum family demand two, and minimum
epoch count two give the exact maximizing interval

\[
[91,104],\qquad
\mathcal D=9,\qquad
\Lambda_{NN}(8,16)={9\over14}.
\tag{9}
\]

Consequently

\[
16\cdot8\left({9\over14}\right)^2
={2592\over49}>1.
\tag{10}
\]

The proposed \(1/(4\sqrt n)\) strengthening is therefore refuted exactly and
must not be used as the next candidate invariant. This correction does not
affect the universal bound (7).

The same C=1 Golomb ruler extends this failure through three consecutive
transitions. Exact endpoint scans give

| Transition | Maximizing interval | Demand / width | \(16n\Lambda_{NN}^2\) |
|---:|---:|---:|---:|
| \(8\to16\) | \([91,104]\) | \(9/14\) | \(2592/49\) |
| \(16\to32\) | \([488,515]\) | \(17/28\) | \(4624/49\) |
| \(32\to64\) | \([398,515]\) | \(45/118\) | \(259200/3481\) |

All 2,016 differences and all 63 prefix-envelope inequalities for that
64-mark witness were recomputed independently. The two extensions were found
by seeded, non-exhaustive beams, so neither minimality nor an asymptotic lower
bound is claimed.

## 4. The finite 128-mark witness

The current Wave 6 certificate records one continuation from a retained
64-mark persistence witness to 128 marks. Its discovery used

\[
\text{beam width }32,\qquad
\text{candidates per state }16,\qquad
\text{seed }601191,\qquad
\text{retain }1,
\]

and expanded 32,003 states. That search was heuristic and non-exhaustive.

After the point set was found, the following facts were recomputed exactly:

- it has 128 strictly increasing integer marks;
- its final mark is 136,282, hence \(N_{128}=136,283\);
- all \(\binom{128}{2}=8,128\) positive differences are distinct;
- it has zero difference collisions;
- all 127 prefixes from 2 through 128 marks satisfy the C=1 envelope

  \[
  N_n\leq\left\lfloor2n^2\log n\right\rfloor;
  \tag{11}
  \]

- the minimum normalized \(Q_{00}\) innovation over its recorded dyadic rows
  is exactly

  \[
  {2044607601929603\over815542875732049920}>0;
  \]

- the normalized signed profile persistence at the new \(64\to128\)
  transition is exactly

  \[
  {245589681743053\over402372206022787}>0;
  \]

- every birth-lag family, Hall interval endpoint, and requested ON/NN
  transition was recomputed with integers and exact rationals.

The leading chain's adjacent NN pressures are

| Older/newer epochs | Exact \(\Lambda_{NN}\) |
|---:|---:|
| \(8,16\) | \(32/431\) |
| \(16,32\) | \(72/1715\) |
| \(32,64\) | \(339/11465\) |
| \(64,128\) | \(858/34429\) |

These values describe one finite witness. In light of (9)--(10), they do not
support a universal decay theorem. The witness proves finite existence only:
no optimality, uniqueness, exhaustive-search claim, infinite extension, or
asymptotic conclusion follows.

The exact payload is
endpoint_variance/wave6_arithmetic_mining_certificate_2026-08-28.json. Its
hashes are recorded in the finalized package manifest and Wave 6 verification
report.

## 5. Cross-boundary Theorems A--D

These theorems use actual difference injectivity and do not depend on the
false empirical strengthening (8).

### Theorem A: exact multi-shell common-band count

For \(1\leq r\leq m\), define

\[
I_{m,r}=
[r\mu_m^+-2D_m^+,\ r\mu_m^++2D_m^+].
\tag{12}
\]

There are exactly \(m-r+1\) length-\(r\) contiguous sums inside the newborn
shell at boundary \(m\), and every one lies in \(I_{m,r}\). For any finite
set \(\mathcal S\) of pairs \((m,r)\) at distinct dyadic boundaries in one
Sidon prefix,

\[
\boxed{
\sum_{(m,r)\in\mathcal S}(m-r+1)
\leq
\operatorname{cap}_+
\left(
\min_{\mathcal S}\inf I_{m,r},
\max_{\mathcal S}\sup I_{m,r}
\right).
}
\tag{13}
\]

This is an exact rounded integer count. The four-mark ruler
\((0,1,4,6)\) attains equality across its first two shells, so no universal
strict constant saving can be inserted into (13).

### Theorem B: exact cross-boundary anti-diagonal count

For \(1\leq k\leq m\) and \(0\leq t<k\), put

\[
d_{m,k,t}=N_{m+k-t}-N_{m-t}.
\tag{14}
\]

These are the \(k\) differences on the rank anti-diagonal crossing the
boundary \(m\). Let

\[
H_m=D_m^-+D_m^+,
\tag{15}
\]

\[
J_{m,k}=
\left[
\min(k\mu_m^+,(k-1)\mu_m^-+\mu_m^+)-H_m,\ 
\max(k\mu_m^+,(k-1)\mu_m^-+\mu_m^+)+H_m
\right].
\tag{16}
\]

For every finite collection \(\mathcal T\) of pairs \((m,k)\),

\[
\boxed{
\sum_{(m,k)\in\mathcal T}k
\leq
\operatorname{cap}_+
\left(
\min_{\mathcal T}\inf J_{m,k},
\max_{\mathcal T}\sup J_{m,k}
\right).
}
\tag{17}
\]

At an exactly endpoint-flat step, \(N_{2m}=2N_m\), taking \(k=m\) gives

\[
D_m^-+D_m^+\geq{m-1\over2}.
\tag{18}
\]

This is a real arithmetic restriction, but at critical diameter its
near-flatness resolution is only \(O(1/(m\log m))\).

### Theorem C: cumulative low-band ledger

Put

\[
M_m=\max(\mu_m^-,\mu_m^+),
\]

\[
R_m(T)=
\min\left\{
m,\ 
\max\left(0,\left\lfloor{T-H_m\over M_m}\right\rfloor\right)
\right\}.
\tag{19}
\]

For every finite family of available dyadic epochs in one Sidon prefix,

\[
\boxed{
\sum_m{R_m(T)(R_m(T)+1)\over2}
\leq\lfloor T\rfloor.
}
\tag{20}
\]

This counts, without probability or asymptotics, all selected cross-boundary
differences that are forced below the common cutoff \(T\).

### Theorem D: integrated endpoint budgets

Define the threshold

\[
\tau_{m,k}=H_m+kM_m,\qquad1\leq k\leq m.
\tag{21}
\]

Then (20) is equivalent to

\[
\boxed{
S(T):=\sum_m\sum_{k=1}^m
k\,\mathbf 1_{\{\tau_{m,k}\leq T\}}
\leq\lfloor T\rfloor.
}
\tag{22}
\]

Integration gives, for \(X\geq1\) and \(\epsilon>0\),

\[
\boxed{
\sum_m\sum_{\substack{1\leq k\leq m\\\tau_{m,k}\leq X}}
{k\over\tau_{m,k}}
\leq1+\log X,
}
\tag{23}
\]

\[
\boxed{
\sum_m\sum_{k=1}^m
{k\over\tau_{m,k}^{1+\epsilon}}
\leq{1+\epsilon\over\epsilon}.
}
\tag{24}
\]

Equations (22)--(24) hold for every finite epoch family. For one infinite
Sidon sequence they extend to all its epochs by monotone convergence over
finite initial families.

The endpoint \(\epsilon=0\) is the hard limit. Equation (23) is only
\(O(\log X)\), and changing mean gaps can renew which numerical band lies
below the useful cutoff. The lower-bound side of the project already
accumulates logarithmically. Therefore Theorem D is exact global history,
but it does not give the required \(o(\log J)\) innovation budget.

## 6. Sixteen-to-sixty-four marks: exact finite obstructions

The ruler

\[
(0,1,18,34,79,127,171,218,
319,415,509,613,710,808,903,1002)
\tag{25}
\]

has all 120 positive differences distinct and satisfies the C=1 envelope at
every prefix. Its three nontrivial newborn shells have

| Boundary \(m\) | Shell gaps | \(G_m\) | \(D_m^+\) | \(D_m^+/G_m\) |
|---:|---|---:|---:|---:|
| 2 | \((17,16)\) | 33 | \(1/2\) | \(1/66\) |
| 4 | \((45,48,44,47)\) | 184 | \(1\) | \(1/184\) |
| 8 | \((101,96,94,104,97,98,95,99)\) | 784 | \(3\) | \(3/784\) |

The reset errors are

\[
e_4(2)=-{31\over70},\qquad
e_8(4)=-{149\over438},\qquad
e_{16}(8)=-{565\over2006},
\tag{26}
\]

so every transition has reset at most \(-1/4\). The exact normalized
innovations are

\[
{(Q_2)_{00}\over N_4}={159\over89600},
\tag{27}
\]

\[
{(Q_4)_{00}\over N_8}
={2923819\over1145948160},
\qquad
{(Q_8)_{00}\over N_{16}}
={24647951033\over7219313737728}.
\tag{28}
\]

Each value in (27)--(28) is greater than \(1/600\).

This one ruler closes two local claims:

1. Three consecutive nontrivial, strongly negative reset epochs with nearly
   rank-uniform newborn shells and positive innovation need not collide.
2. The scaled empirical Hall law (8) fails by the exact computation
   (9)--(10).

Sixteen is the smallest possible terminal mark count for three nontrivial
dyadic shells \(m=2,4,8\). No smallest-span or discrepancy optimality is
claimed. The ruler is finite and is not known to extend to one infinite
critical Sidon sequence. It does not refute an unbounded-history theorem.

### Three consecutive Hall violations in one extension

The same sixteen-mark prefix was extended first to 32 marks and then to 64
marks. The 32-mark prefix is

\[
\begin{split}
(0,1,18,34,79,127,171,218,319,415,509,613,710,808,903,1002,\\
1135,1385,1636,1885,2133,2380,2632,2885,3139,3396,3651,3909,\\
4165,4424,4669,4930).
\end{split}
\]

It has 496 distinct positive differences and satisfies every C=1 prefix
envelope through 32 marks. At \(16\to32\), the two contained families have
data

\[
(16,\ell=5,q=3,[488,493]),\qquad
(32,\ell=2,q=14,[495,515]),
\]

so their common interval has demand 17 and inclusive width 28. The 64-mark
extension adds

\[
\begin{split}
(5080,5578,6074,6564,7066,7569,8079,8573,9040,9513,9970,10431,\\
10852,11311,11723,12133,12607,13079,13488,13896,14303,14708,\\
15109,15559,15961,16359,16765,17164,17618,18051,18451,18854).
\end{split}
\]

It has 2,016 distinct differences and satisfies every C=1 prefix envelope
through 64 marks. At \(32\to64\), the interval \([398,515]\) contains the
32-epoch lag-two family of demand 14 and the 64-epoch lag-one family of demand
31, giving \(\Lambda_{NN}=45/118\). These are exact properties of the fixed
marks. The discovery beams expanded 528,317 and 39,716 states respectively
and were not exhaustive.

## 7. Residue-lift forbidden-shadow no-go

For a finite Golomb ruler \(A\), define

\[
\Delta^+(A)=\{a_j-a_i:i<j\},
\qquad
F(A)=A+\Delta^+(A).
\tag{29}
\]

If \(x>\operatorname{diam}(A)\), then exactly

\[
\boxed{
A\cup\{x\}\text{ is Golomb}
\quad\Longleftrightarrow\quad
x\notin F(A).
}
\tag{30}
\]

Let \(B=\{0=b_0<b_1<\cdots<b_{r-1}\}\) be any normalized Golomb ruler and
let \(L\geq3\). The residue lift

\[
A_L(B)=\{0,1,Lb_1,\ldots,Lb_{r-1}\}
\tag{31}
\]

is Golomb, with the exact disjoint difference decomposition

\[
\boxed{
\Delta^+(A_L(B))
=\{1\}\ \dot\cup\ L\Delta^+(B)\
\dot\cup\ \{Lb_j-1:1\leq j<r\}.
}
\tag{32}
\]

The marks occupy residues \(0,1\pmod L\), and their positive differences
occupy residues \(-1,0,1\pmod L\). Hence

\[
F(A_L(B))\pmod L\subseteq\{-1,0,1,2\}.
\tag{33}
\]

For every interval \(I\) of \(H\) consecutive integers,

\[
\boxed{
|F(A_L(B))\cap I|
\leq4\left\lceil{H\over L}\right\rceil
\leq{4H\over L}+4.
}
\tag{34}
\]

Equations (30)--(34) are exact finite statements.

Applying the lift to finite Erdős--Turán rulers gives primitive \(n\)-mark
Golomb rulers of diameter \(O(n^2\log n)\) whose shadow density in the next
diameter interval tends to zero. Thus critical scale and primitivity do not
force local shadow density.

The stronger growing-window form uses \(M=2^J\),

\[
R=\left\lfloor{1\over2}\log_2\log M\right\rfloor,
\qquad
L=\lceil\sqrt{\log M}\rceil,
\tag{35}
\]

and the dyadic prefixes \(n=M/2^s\), \(0\leq s\leq R\), of one finite lifted
ruler. Uniformly in that window,

\[
N_n\leq9n^2\log n.
\tag{36}
\]

If \(\theta_n\) is the forbidden-shadow density in the actual extension band
\((D_n,D_{2n}]\), then

\[
\sum_{s<R}\theta_{M/2^{s+1}}=o(1).
\tag{37}
\]

At the same transitions,

\[
{(Q_n)_{00}\over N_{2n}}={1\over360}+o(1)
\tag{38}
\]

uniformly, so their innovation sum is

\[
{R\over360}+o(1)\longrightarrow\infty.
\tag{39}
\]

This refutes every fixed-constant local estimate that bounds the innovation
sum by a constant plus total extension-band shadow density. The terminal
ruler depends on \(M\). Equations (35)--(39) are a growing family of
compatible finite windows, not one infinite construction and not a
counterexample to #1191.

## 8. Bounded literature boundary

The focused Wave 6 searches covered disjoint difference packings,
\(A+A-A\) and one-point extension shadows, and Singer/finite-field nesting.
The exact raw semantic-query wording and result counts were not preserved;
the search log marks them unavailable rather than reconstructing counts.
Consensus returned no evidence because its 30/30 monthly quota was exhausted,
with reset reported for 2026-09-01.

Primary arXiv checks establish only adjacent results:

- Ma--Yi pack pairwise disjoint **internal** difference spectra of separate
  finite rulers. Their theorem omits every mixed difference created by taking
  a union.
- Alexeev--Mixon give qualitative completion of each finite Sidon set to some
  infinite perfect difference set. Their claim has no density, coordinate,
  displacement, cumulative-cost, or compatible ordered-prefix bound.
- Singer/norm-graph, subdifference-set, nested-design, and disjoint-ruler hits
  do not provide checked compatible integer embeddings across sizes.

No checked source in this bounded delta supplies a compatible all-prefix
\(O(n^2\operatorname{polylog}n)\) integer Sidon tower or an
\(o(\log J)\) innovation/band-renewal theorem. This is a qualified null, not
an absence theorem or novelty claim. See
research_sources/LITERATURE_DELTA_WAVE6_ARITHMETIC_BANDS_2026-08-28.md.

## 9. Scope ledger and closed routes

| Result | Scope | What it does not say |
|---|---|---|
| Hall pressure \(\Lambda\leq1\) | Exact, every finite power-of-two Golomb ruler under the stated family selection | No scale decay, summability, or innovation control |
| 128-mark witness | Exact finite object after heuristic discovery | No exhaustive search, optimality, uniqueness, or infinite extension |
| \(16n\Lambda_{NN}^2\leq1\) on 22 certificate rows | Finite observation, now exactly refuted at three consecutive transitions by one 64-mark ruler | Not a conjecture or theorem |
| Theorems A--C | Exact finite integer counts across all available epochs in one prefix | No strict endpoint saving |
| Theorem D | Exact finite ledger; infinite extension by monotone convergence | Only \(O(\log)\) at the endpoint, not \(o(\log J)\) |
| Sixteen-mark three-cycle ruler | Exact finite Golomb obstruction | No unbounded-history counterexample |
| Residue lift and four-class shadow | Exact finite theorem | Individual appendability does not give simultaneous or infinite compatibility |
| Growing residue-lift window | Uniform asymptotic statement for a family of finite compatible windows | The family changes with its terminal scale |
| Literature delta | Bounded primary-source audit | No exhaustive absence or priority certification |

The following proof routes are now closed in their unqualified forms:

- a strict improvement of the common-band capacity theorem;
- the empirical \(1/(4\sqrt n)\) Hall-pressure law;
- collision after only three reset-to-nearly-uniform cycles;
- innovation control by local one-point forbidden-shadow density;
- packing only internal spectra of separate finite rulers;
- any argument using the endpoint \(O(\log)\) ledger without an additional
  no-renewal self-improvement.

What remains possible is specifically global: old history may stop a single
infinite sequence from choosing the residue holes or shifted mean-gap bands
that are independently available in every finite recent window.

## 10. Single next theorem

Let \(A\) be one infinite normalized Golomb ruler satisfying, for some fixed
\(C<\infty\),

\[
N_n\leq Cn^2\log(2n)
\qquad\text{for all sufficiently large }n.
\tag{40}
\]

At dyadic marks \(m_j=2^j\), let \(Q_j\) be the actual arithmetic covariance
innovation in

\[
\mathcal M_{2m_j}=B\mathcal M_{m_j}B^{\mathsf T}+Q_j,
\qquad
B=\begin{pmatrix}1/4&1/4\\0&1/2\end{pmatrix},
\tag{41}
\]

and put

\[
H=
\begin{pmatrix}
16/15&8/105\\
8/105&4/35
\end{pmatrix}.
\tag{42}
\]

> **Global band-renewal self-improvement theorem, exact next target.**
> Using the distinctness of every contiguous gap sum together with the
> thresholds \(\tau_{m,k}=D_m^-+D_m^++k\max(\mu_m^-,\mu_m^+)\), prove that
> the cutoffs \(R_m(T)\) from Theorem C cannot renew through unboundedly many
> increasing numerical bands without an old-history capacity charge, and
> consequently
> \[
> \boxed{
> \sum_{j\leq J}
> \left\langle
> H,\frac{Q_j}{N_{2m_j}}
> \right\rangle
> =o(\log J)
> \qquad(J\to\infty).
> }
> \tag{43}
> \]
> The theorem must hold for the one globally compatible sequence in (40),
> not merely for a terminal-scale-dependent finite window. Combined with the
> exact adjoint identity and the established logarithmic lower ledger, (43)
> would give the required contradiction; until (43) is proved, the global
> status remains UNRESOLVED_AT_HARD_LIMIT and no prize claim is ready.

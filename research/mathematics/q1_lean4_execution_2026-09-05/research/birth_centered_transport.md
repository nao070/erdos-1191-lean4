# Transport for a carrier centered in every actual birth class

Date: 2026-09-05. Owner: `/root/c143_mathematics`, GPT-6 Astra Ultra.
Status: exact transport, an explicit averaged row carrier, a signed-fibre
obstruction, and a normalization barrier for polynomial phase measures.
Original Q1 remains unresolved. No new Lean
verification or numerical experiment is asserted in this note.

## 1. Reviewed hypotheses and quantifiers

The complete proof in `birth_centered_fourier_carrier.md` was read and
independently rederived. Let \(P=\{a_1<\cdots<a_p\}\) be actual Sidon,
\(p\ge16\), \(F=\Delta P\), \(q=\binom p2\), and \(H=a_p-a_1\).
Let \(G_j=\{a_j-a_i:i<j\}\) be the actual birth classes. They are
disjoint because positive differences have unique endpoint pairs.

With \(r=\lfloor p/8\rfloor\) and
\(D=a_{p-2r}-a_{r+1}\), the parent selects
\(0\le\theta\le1/(2D)\). For \(d=a_j-a_i\), put
\[
 \mu_j=e^{i\theta a_j}\frac1{j-1}\sum_{k<j}e^{-i\theta a_k},
 \qquad z_d=e^{i\theta d}-\mu_j,\qquad
 R_{de}=\Re(z_d\overline{z_e}),\qquad W=J+R/8.       \tag{1}
\]
The following facts, including their constants, were checked:
\[
 \sum_{d\in G_j}z_d=0,\quad
 S_j:=\sum_{d\in G_j}|z_d|^2
  =(j-1)-\frac{|\widehat P_{j-1}(\theta)|^2}{j-1},
\]
\[
 \eta q\le S:=\sum_jS_j\le q,\quad \eta=1/49152,
 \qquad Z_n(-\theta)=\sum_{j\le n}S_j,
 \quad Z_n(\xi)=\sum_{d\in F_n}z_de^{id\xi}.        \tag{2}
\]
In particular every literal prefix is centered. The matrix is PSD, its
entries lie in \([1/2,3/2]\), and its prefix mass is exactly \(q_n^2\).
There is no missing-centering mass term at any prefix.

For completeness, the frequency proof has \(p-3r\ge5p/8\) central
points, giving \(|\widehat P(\xi)|\ge p/8\) for \(|\xi|\le1/D\).
Two separated \(r\)-point sets lie inside each of the last \(r\)
old prefixes. Their gaps exceed \(D\). Averaging their ordered pairs
uses \(1-\operatorname{sinc}x\ge1/48\) for all \(x\ge1/2\), hence
\(\operatorname{Av}\sum_jS_j\ge r^3/(24p)\ge\eta q\).
The exact peak (2), \(|Z_p'|\le2qH\), and an interval of length
\(\eta/(2H)\) give
\[
 E_P(R):=\|1_P*z_F\|_2^2
 \ge\frac{\eta^3p^2q^2}{1024\pi H}.                \tag{3}
\]
All of this agrees with the parent's proof. For a compatible future
block of size \(m=O(p)\), the terminal row-gap guarantee is
\[
 I_m=\frac1{16}\{E_P(R)-(p+m-1)S\}
     =\Omega_C(q^2/\log p)-O(pq)                    \tag{4}
\]
under the fixed critical cap, with the explicit positive constant in
the parent note.

The quantifier is: for each terminal prefix there is one terminally
chosen phase whose restrictions are all centered. It is not asserted
that this one phase supplies the lower variance \(\eta q_n\) or the
row bound (4) at every earlier prefix. Nor is a single phase asserted to
work at all terminal sizes.

## 2. The historical gain becomes a causal cross-energy sum

Keep the features in (1) fixed throughout the history. At step \(n\),
write
\[
 f_{n-1}=1_{P_{n-1}}*z_{F_{n-1}},\quad
 h_n=\delta_{a_n}*z_{F_{n-1}},\quad
 g_n=1_{P_n}*z_{G_n},
\]
\[
 \mathcal R_n=\Re\langle f_{n-1},h_n\rangle,
 \qquad X_n=\Re\langle f_{n-1}+h_n,g_n\rangle.
\]
Thus \(f_n=f_{n-1}+h_n+g_n\). The pairing convention takes real
parts, so the choice of which inner-product argument is conjugated
does not affect the displayed real identities.

For the new class, the position \(a_n\) collects
\(\sum_{d\in G_n}z_d=0\). Every other position is
\(a_n+(a_k-a_i)\), \(i<n\), \(k\le n\), \(k\ne i\), whose
nonzero signed difference has unique ordered endpoints. Each input
coefficient occurs exactly \(n-1\) times. Consequently
\[
 \|g_n\|_2^2=(n-1)S_n,\qquad
 E_n-E_{n-1}=S(F_{n-1})+2\mathcal R_n+(n-1)S_n+2X_n.
                                                               \tag{5}
\]
The sum of the two diagonal contributions is
\(\sum_n[S(F_{n-1})+(n-1)S_n]=(p-1)S\). The literal pair
interpretation of \(\mathcal R_n\) is exactly the signed retirement
functional in `weighted_birth_envelope.md`. Hence
\[
 \boxed{E_P(R)=(p-1)S+2\mathcal R+2X,\qquad
        \mathcal R=\sum_n\mathcal R_n,\quad X=\sum_nX_n.}      \tag{6}
\]

Let \(T_{\rm born}(R)\) sum \(R_{de}\) on the actual label pairs whose
positive difference was already present when both source labels became
available. The weighted birth identity gives
\[
 \boxed{2T_{\rm born}(R)=2X-S.}                     \tag{7}
\]
One can also see this directly: \(X_n\) is the weight on the mixed
old/new pairs whose difference is in \(F_n\). All new/new pairs have
old difference and total weight
\(\tfrac12(|\sum_{G_n}z|^2-S_n)=-S_n/2\).

For the full historical envelope with unit time coefficients,
\[
 \boxed{\quad
 C_{\rm hist}(J)-C_{\rm hist}(W)=X/8,\qquad
 I_m^{\rm hist}=\frac18(X-mS/2)=I_m-\mathcal R/8.
 \quad}                                            \tag{8}
\]
The second expression compares capacity minus the **same terminal raw
future demand**, and retains its increased diagonal cost. Thus the new
centering removes the prefix mass error completely; it does not remove
the signed retirement correction or prove a lower bound for \(X\).

For several fixed prefix rows and raw demands, all prefix masses are
also unchanged. If their sizes are \(m_j\) and old prefixes \(n_j\),
the full-envelope gap comparison is exactly
\[
 \frac18\left[X-\frac12\sum_jm_jS(F_{n_j})\right].  \tag{9}
\]
This retains every diagonal loss, and assumes the same actual denominator
in each component comparison. It introduces no separate capacity at each
row or each width.

## 3. The old scalar injection potential acquires class-mean terms

For a label \(s\), abbreviate \(\mu_s=\mu_{\tau(s)}\), where
\(\tau(s)\) is its actual birth. On a retirement \(t=e-d\), expansion
now gives
\[
 R_{de}-R_{t,e}
 =h_e(t)-h_e(d)
       +\Re\{(\mu_t-\mu_d)\overline{z_e}\},
 \qquad h_e(s)=\Re\{(1+\overline{\mu_e})e^{i\theta s}\}.       \tag{10}
\]
The terms involving \(e^{i\theta e}\) use \(e=d+t\); the remaining
class-mean difference has the displayed sign. Unlike terminal-only
centering, there is no single common \(\mu\), so \(h_e\) depends on
the larger source label and the final term must be kept. The zero sums
on whole classes do not cancel sums on irregular retirement incidences.
Using the older one-label formula without these terms would be invalid.

## 4. Automatic terms and actual equal-three-sum fibres

Expand \(X_n\) at a position with old smoothing point \(a_k\) and
new smoothing point \(a_l\). An old label \(a_j-a_h\), \(h<j<n\),
and a new label \(a_n-a_i\), \(i<n\), contribute precisely when
\[
 a_k+a_j+a_i=a_l+a_n+a_h.                            \tag{11}
\]

### 4.1 The channel with old smoothing point \(a_k=a_n\)

If \(k=n\), Sidon two-sum uniqueness reduces (11) to
\(j=l\), \(i=h\). Put \(u_i=e^{-i\theta a_i}\) and
\(M_j=(j-1)^{-1}\sum_{i<j}u_i\). Then
\(z_{a_j-a_i}=e^{i\theta a_j}(u_i-M_j)\), and
\[
 \sum_{i<j}z_{a_j-a_i}\overline{z_{a_n-a_i}}
 =e^{i\theta(a_j-a_n)}S_j.
\]
The class-mean difference vanishes because
\(\sum_{i<j}(u_i-M_j)=0\). Therefore the parent's automatic-channel
formula is exactly
\[
 X_n^{\rm auto}=\sum_{j<n}\cos(\theta(a_n-a_j))S_j,
 \qquad \left|\sum_nX_n^{\rm auto}\right|\le pS.    \tag{12}
\]
This is only order \(pq\), below the desired \(q^2/\log p\) scale.

### 4.2 Disjoint triple representations and a full fibre expression

If \(k<n\), the two three-point multisets in (11) are different,
because only the right side contains the largest point \(a_n\).
They have no shared vertex: cancelling one would give a two-sum equality
and force the two multisets to coincide. For fixed sum \(s\), the
distinct three-element subset representations
\[
 \mathcal T_s=\{T\subset P:|T|=3,\ \sum_{a\in T}a=s\}
\]
are consequently pairwise vertex-disjoint. They form a matching of
three-element subsets, not an arbitrary family with overlapping vertices.

Take one unordered pair \(T,U\in\mathcal T_s\), and let \(a_n\) be
the largest point in their union, lying in \(U\). Every corresponding
six-distinct-index cross record chooses \(a_h\in U\setminus\{a_n\}\),
\(a_j\in T\) with \(a_j>a_h\), and \(a_i\in T\setminus\{a_j\}\).
The remaining members of \(T\) and \(U\) are the smoothing points.
Its entire contribution is exactly
\[
 \Phi(T,U)=\Re\sum_{a_h\in U\setminus\{a_n\}}
       \sum_{a_j\in T,\ a_j>a_h}
       z_{a_j-a_h}
       \overline{\sum_{a_i\in T\setminus\{a_j\}}z_{a_n-a_i}}.
                                                               \tag{13}
\]
This has at most 12 ordered records, each counted once. If
\(B_n(T)=\sum_{a_i\in T}z_{a_n-a_i}\), it factors as
\[
 \Re\left[
 \left(\sum_{a_h\in U\setminus\{a_n\}}
       \sum_{a_j\in T,\ a_j>a_h}z_{a_j-a_h}\right)
       \overline{B_n(T)}
 -\sum_{a_h\in U\setminus\{a_n\}}
       \sum_{a_j\in T,\ a_j>a_h}
                z_{a_j-a_h}\overline{z_{a_n-a_j}}
 \right].                                          \tag{14}
\]
The subtraction enforces \(i\ne j\); dropping it would add forbidden
repeated-index records to this six-distinct channel. The time-varying
class means and the order restriction \(a_j>a_h\) remain explicit.

The repeated-index remainder is at most \(144p^3\) in absolute value.
Indeed there are exactly \(p^2\) three-point multisets having a repeated
value. Different representations of a fixed sum have disjoint supports,
so there are at most \(p\) of them. Thus at most \(p^3\) unordered
collisions involve a repeated representation. At most \(6\cdot6=36\)
ordered assignments produce (11) from a collision, and each coefficient
has absolute value at most \(4\). This conservative bound includes all
within-side diagonals. Accordingly
\[
 X=\sum_nX_n^{\rm auto}+\sum_s\sum_{\{T,U\}\subset\mathcal T_s}
                                      \Phi(T,U)+E_{\rm rep},
 \qquad |E_{\rm rep}|\le144p^3.                     \tag{15}
\]

## 5. Individual six-distinct fibres can be negative for the selected carrier

The matching property in §4 does not make each \(\Phi(T,U)\) positive.
Start with the actual Sidon points
\[
 P_6=\{0,1,4,10,18,31\}.
\]
Their 15 positive differences are
\(1,3,4,6,8,9,10,13,14,17,18,21,27,30,31\), all distinct.
The sum-32 fibre consists of
\(U=\{0,1,31\}\) and \(T=\{4,10,18\}\). No third representation
is possible, by the disjointness property and the six available points.

For small \(\theta\), the birth-centered feature has expansion
\[
 z_{a_j-a_h}=i\theta(\overline a_{j-1}-a_h)+O(\theta^2),
 \qquad \overline a_{j-1}=(j-1)^{-1}\sum_{i<j}a_i.
\]
Here the old upper points \(4,10,18\) have preceding means
\(1/2,5/3,15/4\), and the new upper point 31 has preceding mean
\(33/5\). All three old upper points exceed both \(h=0,1\), so
(13) includes all 12 records. The coefficient of \(\theta^2\), grouped
by the old upper point, is

| \(a_j\) | \(\sum_{h=0,1}(\overline a_{j-1}-h)\) | \(\sum_{a_i\in T\setminus\{a_j\}}(33/5-a_i)\) | Product |
|---:|---:|---:|---:|
| 4 | 0 | \(-74/5\) | 0 |
| 10 | \(7/3\) | \(-44/5\) | \(-308/15\) |
| 18 | \(13/2\) | \(-4/5\) | \(-26/5\) |

Thus
\[
 \Phi(T,U)=-\frac{386}{15}\theta^2+O(\theta^4).     \tag{16}
\]
The real expression is even in \(\theta\), giving the stated remainder
order. An explicit uniform negative neighborhood does not require that
refinement: since all involved labels are at most 31,
\[
 |z_d-i\theta(d-\operatorname{mean}G_{\tau(d)})|
 \le31^2\theta^2,\qquad |z_d|\le31|\theta|.
\]
Each product differs from its quadratic term by at most
\(2\cdot31^3|\theta|^3\), so the 12 records give error at most
\(714984|\theta|^3\). For \(0<\theta\le1/100000\), this is less
than \(8\theta^2\), whereas \(386/15>25\). Therefore the fibre is
strictly negative throughout that entire interval.

This can be made compatible with the actual phase-selection theorem,
not only with a six-point calculation. Append
\[
 100,301,904,2713,8140,50005,150016,450049,1350148,4050445
\]
to obtain 16 points. Every appended point exceeds three times the
previous maximum, so its new cross differences are larger than every
old difference and mutually distinct. Inductively the set is Sidon.
Translate all points by 1 if positivity is required. The old fibre and
its old class means are unchanged; every new point is too large to
participate in that sum. For \(p=16\), \(r=2\), the parent's quantile
width is \(D=a_{12}-a_3=50001\). Consequently every allowed nonzero
phase is at most \(1/100002<1/100000\). A selected phase with
\(S\ge\eta q\) is nonzero, and so its contribution from this fibre is
strictly negative.

This is an exact obstruction to **individual-fibre positivity**, even
under the carrier's actual selected-phase conditions. It does not make
the total cross energy negative, and the separated extension supplies
no long fixed-onset critical cap. It is not a Q1 counterexample.

## 6. A positive cross-energy packet nevertheless has the required scale

A slightly more precise choice of the same allowed phase gives a real
positive packet for the causal cross energy itself. Let
\(L=\{p-r+1,\ldots,p\}\), and choose \(\theta\) to maximize
\(Y=\sum_{n\in L}S_n\) over \([0,1/(2D)]\). The average proof in
§1 already gives \(\operatorname{Av}\sum_{n\in L}S_n\ge\eta q\),
so this choice has \(Y\ge\eta q\) and preserves all the parent's
conclusions. It is still made from the terminal prefix alone.

Define the real spectral cross sum
\[
 A(\xi)=\sum_{n=2}^p|\widehat P_n(\xi)|^2
                   \Re\{Z_{n-1}(\xi)\overline{Z_{G_n}(\xi)}\},
 \qquad X=\frac1{2\pi}\int_{-\pi}^{\pi}A(\xi)\,d\xi.        \tag{17}
\]
At \(-\theta\), every summand is nonnegative by (2). For \(n\in L\),
\(P_n\) already contains all the central \(p-3r\) points, so
\(|\widehat P_n(-\theta)|\ge p/8\) by the same quantile proof.
Also \(S_n\le p\), and
\[
 \sum_{n\in L}S(F_{n-1})S_n
 \ge\frac12\left(Y^2-\sum_{n\in L}S_n^2\right)
 \ge\frac12(Y^2-pY).
\]
If \(p-1\ge4/\eta\), then \(Y\ge\eta q\ge2p\), giving
\[
 A(-\theta)\ge\frac{\eta^2p^2q^2}{256}.             \tag{18}
\]

Translate \(a_1\) to zero for derivative bounds. Globally,
\(|\widehat P_n|\le p\), \(|\widehat P_n'|\le pH\),
\(|Z_{n-1}|\le2q\), \(|Z_{n-1}'|\le2qH\), and
\(|Z_{G_n}|\le2|G_n|\), \(|Z_{G_n}'|\le2|G_n|H\).
Differentiating each summand in (17), and summing
\(\sum_n|G_n|=q\), gives the uniform bound
\[
 |A'(\xi)|\le16p^2q^2H.                             \tag{19}
\]
On
\(I=[-\theta-\eta^2/(8192H),-\theta+\eta^2/(8192H)]\),
the variation is at most half the lower bound in (18). This interval
lies in \([-\pi,\pi]\), and therefore
\[
 \boxed{\quad
 \frac1{2\pi}\int_I A(\xi)\,d\xi
 \ge\frac{\eta^4p^2q^2}{2^{22}\pi H}.
 \quad}                                            \tag{20}
\]
Under \(H\le Cp^2\log(2p)\), this is a positive contribution of order
\(q^2/\log p\), with the explicit conservative constant displayed.

## 7. The signed complement remains a necessary obligation

Equation (20) bounds a contribution to \(X\), not \(X\) itself. Define
\[
 X_{\rm out}=\frac1{2\pi}
           \int_{[-\pi,\pi]\setminus I}A(\xi)\,d\xi.
\]
The exact comparison is
\[
 I_m^{\rm hist}=\frac18\left[
       \frac1{2\pi}\int_I A+X_{\rm out}-\frac{mS}{2}\right].  \tag{21}
\]
The omitted frequency integral has no proved sign. If the historical
gap is nonpositive, (20)--(21) force
\[
 X_{\rm out}\le\frac{mS}{2}
                    -\frac{\eta^4p^2q^2}{2^{22}\pi H}.        \tag{22}
\]
For \(m=O(p)\), the diagonal is \(O(pq)\), negligible compared with
the capped packet scale. Thus failure of retention requires a negative
complement of order \(q^2/\log p\). No bound excluding this cancellation
under the full fixed-onset cap has been established here.

The automatic channel and repeated-index remainder in (15) also have
only \(O(p^3)\) magnitude. The large-scale issue is consequently the
sum of genuinely different three-point representations, with all their
signed class-centered weights retained. Section 5 shows why the matching
structure alone cannot certify this sum term by term.

Finally, the four nonnegative scalar carriers in the parent construction
are fixed on the terminal bank and each is centered relative to its
uniform mass on every birth class. They share every physical fibre's
last eligible prefix time. Their historical capacities and raw-demand
comparisons therefore average exactly, as proved in §11 of
`weighted_birth_envelope.md`. This removes a selection obstruction,
but does not change the unproved sign control in (21).

No frequency complement, repeated-index channel, or diagonal term was
discarded. No independent copies of (20) were summed across widths.
The proof of Q1 and its required Lean verification remain incomplete.

## 8. Carrier-phase averaging is different from the spectral integral

Here \(\theta\) denotes the carrier phase in (1), while \(\xi\) denotes
the convolution Fourier frequency in (17). These are two independent
variables. Put \(g_j=j-1\), and let \(C_j\) be the real orthogonal
projection \(I-J/g_j\) on the coordinates of \(G_j\), extended by zero
off that class. Write \(C=\sum_jC_j\), and
\(e(\theta)_d=e^{i\theta d}\). The full feature vector is exactly
\(z(\theta)=Ce(\theta)\). For a nonnegative probability measure
\(\nu\) on carrier phases, define
\[
 K^\nu_{de}=\int\cos(\theta(d-e))\,d\nu(\theta),\qquad
 R^\nu=\int R(\theta)\,d\nu(\theta)=CK^\nu C.       \tag{23}
\]
This is PSD and centered on each actual birth class. Moreover
\(|R^\nu_{de}|\le4\), \(S^\nu:=\operatorname{tr}R^\nu\le q\),
and \(W^\nu=J+R^\nu/8\) has entries in \([1/2,3/2]\) and all
prefix masses exactly \(q_n^2\). Prefix trace and energy are literal
averages; no new recentering is performed.

For every physical difference, all nonnegative fixed matrices
\(W(\theta)\) have the same last eligible prefix. Therefore their
full historical capacities commute with this average. The common raw
demands do too. This statement concerns the full history with unit time
coefficients, exactly as in (8); it does not replace an arbitrary
time-dependent envelope by a linear functional.

For the uniform measure \(d\theta/(2\pi)\) on \([-\pi,\pi]\), the
distinct integer labels give \(K^\nu=I\), hence \(R^\nu=C\).
The trace is \(q-(p-1)\), and all cross-class entries are zero. Thus
\[
 \operatorname{Av}_\theta X(\theta)=0,\qquad
 \operatorname{Av}_\theta I_m^{\rm hist}(\theta)
       =-\frac{m\{q-(p-1)\}}{16}.                 \tag{24}
\]
The historical capacity improvement alone has mean zero. Its gap
comparison has the strictly negative diagonal in (24). In particular,
uniform full-circle averaging does not retain the positive packet.

## 9. An explicit nonnegative low-phase average keeps the terminal row bound

One need not choose a single maximizing carrier phase to obtain a
terminal row bound. Keep the quantile width \(D\) from §1, put
\(T=1/(2D)\), and use the probability density
\[
 d\nu_T(\theta)=\frac1T(1-|\theta|/T)_+\,d\theta.
\]
It has support \([-T,T]\) and exactly
\[
 K^{\nu_T}_{de}=\kappa_D(d-e),\qquad
 \kappa_D(t)=\operatorname{sinc}^2(t/(4D)).          \tag{25}
\]
The value at zero is 1. This is the elementary Fourier transform of
the triangular density; in particular its entries are nonnegative as
well as forming a PSD matrix.

For \(x\ge1/4\),
\[
 1-\operatorname{sinc}^2x\ge1/192.                 \tag{26}
\]
Indeed, on \([1/4,2]\), \(0\le\operatorname{sinc}x\le1\), and
\(1-\operatorname{sinc}x\ge x^2/12\). The latter follows from
\(\sin x\le x-x^3/6+x^5/120\) and \(x\le2\). On \([2,\infty)\),
\(|\operatorname{sinc}x|\le1/2\). These give (26) with room in
the constants.

Each of the last \(r\) old prefixes contains two \(r\)-point sets
whose pairwise gaps exceed \(D\). The exact class-variance identity is
\[
 S_j(\theta)=\frac1{j-1}\sum_{i,k<j}
                   [1-\cos(\theta(a_i-a_k))].
\]
Its average and the \(2r^2\) ordered separated pairs give
\(\int S_j\,d\nu_T\ge r^2/(96p)\) at each such stage. Since
\(r\ge p/16\),
\[
 S^{\nu_T}\ge\sum_{j\in L}\int S_j\,d\nu_T
       \ge\frac{r^3}{96p}
       \ge\frac{p^2}{393216}
       \ge\varepsilon q,\qquad \varepsilon=1/196608.         \tag{27}
\]

For completeness the row-energy estimate can be averaged without
assuming a pointwise positive variance. For every \(|\theta|\le T\),
let \(S=S(\theta)\). The peak identity is \(Z_p(-\theta)=S\),
and \(|Z_p'|\le2qH\). If \(S>0\), the interval of radius
\(S/(4qH)\) centered at \(-\theta\) has \(|Z_p|\ge S/2\).
Its frequencies satisfy
\[
 |\xi|\le\frac1{2D}+\frac1{4H}\le\frac3{4D}<\frac1D,
\]
so \(|\widehat P(\xi)|\ge p/8\). Parseval on this interval yields
\[
 E_P(R(\theta))\ge\frac{p^2S(\theta)^3}{1024\pi qH}.       \tag{28}
\]
For \(S=0\), (28) holds trivially. Energy is linear in the matrix,
and Jensen's inequality for the cube now proves
\[
 E_P(R^{\nu_T})\ge
 \frac{p^2}{1024\pi qH}\left(\int S(\theta)\,d\nu_T\right)^3
 \ge\frac{\varepsilon^3p^2q^2}{1024\pi H}.         \tag{29}
\]
Thus the single explicit matrix
\(W^{\nu_T}=J+C[\kappa_D(d-e)]C/8\) has the terminal row guarantee
\[
 \frac{I_m(W^{\nu_T})}{q^2}
 \ge\frac{\varepsilon^3p^2}{16384\pi H}
       -\frac{p+m-1}{16q}.                        \tag{30}
\]
Writing \(C_0\) for the scalar cap constant to distinguish it from
the projection \(C\), if \(H\le C_0p^2\log(2p)\) and
\(m\le R_0p\), the right side of (30) is at
least
\(\varepsilon^3/[16384\pi C_0\log(2p)]-(1+R_0)/[8(p-1)]\).
This is an explicit phase mixture, still with the same terminal row
scale. It does not yet prove any historical gap improvement.

## 10. The required correlation is a centered Born-adjacency correlation

Let \(A_{\rm born}\) be the symmetric, zero-diagonal adjacency matrix
on label pairs born with their difference already used. Every two
labels in one actual class have an old difference. Consequently
\[
 A_{\rm within}=\bigoplus_j(J_{g_j}-I_{g_j}),\qquad
 A_{\rm cross}=A_{\rm born}-A_{\rm within},\qquad
 C A_{\rm within} C=-C.
\]
The identities for any averaged carrier in (23) are exactly
\[
 X^\nu=\frac12\operatorname{tr}(C A_{\rm cross} C K^\nu),
 \qquad
 I_m^{\rm hist}(W^\nu)=\frac1{16}
       \operatorname{tr}\{C[A_{\rm born}-(m-1)I]C K^\nu\}.
                                                               \tag{31}
\]
Hence retaining the row gain requires positive correlation with the
actual **doubly class-centered** mixed Born adjacency, at scale
\(q^2/\log p\) after its diagonal cost. The entrywise nonnegativity
of the explicit kernel (25) does not establish this correlation.

For instance, if \(d\in G_j,e\in G_k\), its centered entry is
\[
 \kappa_D(d-e)-\frac1{g_j}\sum_{a\in G_j}\kappa_D(a-e)
 -\frac1{g_k}\sum_{b\in G_k}\kappa_D(d-b)
 +\frac1{g_jg_k}\sum_{a\in G_j,b\in G_k}\kappa_D(a-b).       \tag{32}
\]
All four terms matter. Any matrix constant on each rectangular class
block is annihilated by multiplication by \(C\) on both sides. Thus
unweighted cross-class edge densities, even large ones, give no term
in (31) by themselves. One needs actual position-dependent covariance
with these four-term kernels, or an equivalent operator estimate.

The negative fibre in §5 stays negative for every nonzero phase in the
support of (25) for that explicit extension. Its triangular average is
therefore also negative. This does not determine the total correlation,
but it rules out an individual-fibre positivity proof for this specific
nonnegative phase mixture as well. No new finite experiment is used.

Sections 1--7 were independently reviewed by the parent and by
`/root/global_route`; the signed-fibre coefficients, repeated-index
bound, packet constants, and scope were supported. `/root/global_route`
also independently reviewed §§8--10 and supported the triangular
transform, all constants, the Jensen step, and the Born coefficients.
These analytic derivations supply an explicit averaged carrier and
the exact remaining correlation, not the missing all-history estimate.

## 11. Two-frequency symmetry and the exact positive step-weighted identity

The parent proposed a second useful averaging identity. Its Fourier
signs and normalization can be checked without any estimate. For a
single class,
\[
 Z_{G_j}(\xi;\theta)=e^{i(\theta+\xi)a_j}
 \left[\widehat P_{j-1}(-\theta-\xi)
 -\frac{\widehat P_{j-1}(-\theta)
         \widehat P_{j-1}(-\xi)}{j-1}\right].       \tag{33}
\]
This is exactly symmetric under \(\theta\leftrightarrow\xi\).
Put \(C_{<n}=\sum_{j<n}C_j\). On the fixed terminal label space,
let \(H_n\) be the convolution Gram matrix
\[
 (H_n)_{de}=\frac1{2\pi}\int_{-\pi}^{\pi}
       |\widehat P_n(\theta)|^2e^{i(d-e)\theta}\,d\theta
 =n\mathbf1_{d=e}+\mathbf1_{|d-e|\in F_n}.        \tag{34}
\]
The second indicator is zero when \(d=e\). Equation (34) uses
actual signed-difference uniqueness. It is a real symmetric PSD matrix.
The real cross energy is
\(X_n(\theta)=\Re[e(\theta)^*C_{<n}H_nC_ne(\theta)]\).
Therefore the parent identity is precisely
\[
 \boxed{\quad
 \frac1{2\pi}\int_{-\pi}^{\pi}
       |\widehat P_n(\theta)|^2X_n(\theta)\,d\theta
 =\operatorname{tr}(C_{<n}H_nC_nH_n)
 =\|C_{<n}H_nC_n\|_{\rm HS}^2\ge0.
 \quad}                                             \tag{35}
\]
For the last equality insert the two idempotent projections in the
trace. There is no additional factor of two. The probability density
is \(|\widehat P_n|^2/n\) relative to \(d\theta/(2\pi)\), so its
expectation of \(X_n\) is the right side of (35) divided by \(n\).

The measure in (35) depends on the step. It therefore does not supply
a single fixed terminal matrix whose historical cross sum is the sum
of those positive averages. If instead the single measure is
\(|\widehat P_p|^2/p\), define
\[
 B_n=C_{<n}H_nC_n,\qquad D_n=C_{<n}H_pC_n,
 \quad b=\sum_n\|B_n\|_{\rm HS}^2,
 \quad d=\sum_n\|D_n\|_{\rm HS}^2,
 \quad e=\sum_n\|D_n-B_n\|_{\rm HS}^2.
\]
Here \(e\) is a scalar norm budget, not a label coordinate. Its
matrix \(D_n-B_n\) retains precisely the future-difference adjacency:
the diagonal \((p-n)I\) in \(H_p-H_n\) is annihilated by the
orthogonal class supports. For this fixed averaged carrier,
\[
 X^\nu=\frac1p\sum_n\langle B_n,D_n\rangle_{\rm HS}
       =\frac{b+d-e}{2p}.                         \tag{36}
\]
Writing \(r_C=\operatorname{tr}C=q-(p-1)\), every diagonal class
block of \(CH_pC\) equals \((p-1)C_j\), so
\[
 S^\nu=\frac{p-1}{p}r_C,\qquad
 I_m^{\rm hist}=\frac{b+d-e-m(p-1)r_C}{16p}.       \tag{37}
\]
The signed future correction has been represented by an exact
difference of nonnegative norm budgets; it has not been removed.
For example, \(e\le(1-\delta)^2b\), \(0\le\delta\le1\), would
imply \(X^\nu\ge\delta b/p\) by Cauchy--Schwarz. No such
cap-sensitive relation has been proved here.

## 12. Polynomial phase weights face a quantitative normalization barrier

The positivity (35) is useful structurally, but its natural normalized
phase family cannot preserve the large terminal gain of (29). The
following upper bound holds already for arbitrary actual Sidon
prefixes, without using the critical cap.

Let \(Q\subseteq P\) have \(\ell\ge1\) points, and average the
birth-centered carrier against the probability density
\(|\widehat Q(\theta)|^2/\ell\). The corresponding matrix is
\[
 K^Q=I+A_Q/\ell,\qquad
 (A_Q)_{de}=\mathbf1_{|d-e|\in\Delta Q},\qquad
 R^Q=C(I+A_Q/\ell)C.                              \tag{38}
\]
For each positive difference \(t\), at most \(q\) label pairs
\((d,e)\) with \(d<e\) have \(e-d=t\). Consequently
\[
 \|A_Q\|_{\rm HS}^2
 \le2q\binom\ell2\le q\ell^2.                    \tag{39}
\]
Also \(\|A_{\rm cross}\|_{\rm HS}\le q\). Since the mixed
adjacency has no within-class entries,
\(\operatorname{tr}(C A_{\rm cross}C)=0\). Equations (31), (38),
and contraction by orthogonal projections give the absolute bound
\[
 \boxed{\quad |X^Q|
 =\left|\frac1{2\ell}
          \operatorname{tr}(C A_{\rm cross}C A_Q)\right|
 \le\frac{q^{3/2}}2=O(p^3).
 \quad}                                             \tag{40}
\]
Every probability mixture of these subset-polynomial measures obeys
the same bound. Thus choosing smaller prefix polynomials or mixing
different prefixes does not avoid the order loss in (40).

Even its terminal energy is too small for the desired gain. On the
terminal label space put \(A_P=H_p-pI\). Each diagonal class block
of \(A_P\) is \(J-I\), whence
\(\operatorname{tr}(A_PC)=-r_C\). Furthermore
\(\|A_P\|_{\rm HS}\le\sqrt2\,q\) by (39) with \(Q=P\).
Since \(\operatorname{tr}R^Q\le q\),
\[
 \begin{split}
 E_P(R^Q)
 &=p\operatorname{tr}R^Q-r_C
             +\frac1\ell\operatorname{tr}(A_PC A_QC)\\
 &\le pq+\sqrt2\,q^{3/2}\le2pq.
 \end{split}                                        \tag{41}
\]
This upper bound also survives probability mixtures. For
\(q=\binom p2\), both (40) and (41) are negligible compared with
\(q^2/\log p\). Consequently replacing the low-frequency carrier
by this positive-step polynomial family cannot keep its terminal
\(\Omega(q^2/\log p)\) bound, irrespective of how well its
historical sign behaves.

For comparison, even the separately normalized positive quantities
in (35) satisfy
\[
 \sum_{n=2}^p\frac{\|C_{<n}H_nC_n\|_{\rm HS}^2}{n}
 \le\sum_{n=2}^p\frac{|F_{n-1}|\,|G_n|}{n}
 \le\frac12\sum_{n=2}^pn^2=O(p^3).                \tag{42}
\]
The first inequality uses that the unprojected mixed block is a
zero-one matrix. Without normalization its total mass and diagonal
cost increase; that different budget cannot be suppressed.

The explicit triangular measure (25) is not asserted to belong to the
subset-polynomial mixture family. A general feature construction with
class-dependent phase measures is also outside the conclusion of
(40)--(41), and would need its own positive-kernel and diagonal audit.
The proved obstacle closes this particular positivity-preserving
replacement, not the remaining full-history covariance problem (31).
No new numerical search, Lean theorem, or assertion of Q1 closure is
part of §§8--12.

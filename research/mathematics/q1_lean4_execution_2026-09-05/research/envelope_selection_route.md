# Quantitative mask saving and the next envelope selections

Date: 2026-09-05. Owner: /root/c143_mathematics.
This task changes only this file. Other agents' edits and original inputs are
preserved. The selected model configuration has not been changed.

Status: Q1 remains unresolved. A new mask lower bound, uniform over productive
weights, is proved below. Its positive-semidefinite extension and the cost of
survival conditioning are explicit. Two envelope selections are also analyzed
exactly. None of these results yet supplies the additional all-history gain
needed for Q1. No new Lean verification or numerical experiment is claimed.

We use the notation and proved shadow/envelope inequalities in
[growing_label_budget.md](growing_label_budget.md), §§5–6. In particular,
\(P_p=\{a_1<\cdots<a_p\}\) is an actual Sidon prefix, including diagonal
sums in the Sidon condition; \(\Delta P_p\) has unique positive-difference
endpoints. Logarithms are natural. The critical hypothesis, when used, is

\[
 a_n\le Cn^2\log(2n)\quad\text{for every }n\ge n_0,     \tag{1}
\]

with one fixed \(C>0\) and one fixed \(n_0\). Finite counterexamples in this
note do not assert a bound from one fixed onset across an infinite history.

## 1. A mask lower bound for every productive weight vector

Let \(P\) be any finite Sidon set, \(|P|=p\ge2\), with span
\(H=\max P-\min P\). Let \(F\subseteq\Delta P\) be nonempty. Let \(u_d\)
be any real weights supported on \(F\), with

\[
 U=\sum_du_d,\qquad S=\sum_du_d^2,\qquad
 K_u(t)=\sum_du_du_{d+t}\quad(t>0).
\]

Nonnegativity of \(u\) is not required for the identity or inequality in this
section; it will be required when interpreting every term as a nonnegative
capacity expenditure. Put

\[
 T_P(u)=\sum_{t\in\Delta P}K_u(t),\qquad
 L=\operatorname{diam}P+\operatorname{diam}F+1\le2H.    \tag{2}
\]

The last bound uses \(F\subseteq[1,H]\). Expand the square of the old-prefix
convolution to obtain the exact identity

\[
 \boxed{\quad
 pS+2T_P(u)=\sum_z\left(\sum_{a\in P}u_{z-a}\right)^2.
 \quad}                                               \tag{3}
\]

Equal choices of \(a\) give \(pS\); unequal choices give \(K_u(t)\) twice
for each distinct old difference \(t\). The convolution is supported on an
integer interval of length \(L\), and its sum is \(pU\). Cauchy–Schwarz gives

\[
 \boxed{\quad
 T_P(u)\ge\frac12\left(\frac{p^2U^2}{L}-pS\right)
 \ge\frac{p^2U^2}{4H}-\frac{pS}{2}.
 \quad}                                               \tag{4}
\]

This is not a forbidden-difference argument with \(B=P\): such a use would
be invalid. It is the direct convolution identity (3), which counts the old
differences positively.

For \(P=P_p\) under (1), \(p\ge n_0\), (4) implies

\[
 T_{P_p}(u)\ge\frac{U^2}{4C\log(2p)}-\frac{pS}{2}.      \tag{5}
\]

In particular, if

\[
 M(u):=U^2/S\ge4Cp\log(2p),                            \tag{6}
\]

then

\[
 \boxed{\quad T_{P_p}(u)\ge\frac{U^2}{8C\log(2p)}.\quad} \tag{7}
\]

The precise coarse-demand positivity threshold from the previous note is
\(M(u)>5Cp\log(4p)\), which implies (6). Thus every vector productive for
that mechanism necessarily loses at least the amount (7) to the already-used
mask. This is uniform over its selected labels and their weights. For unit
weights on the old label bank the normalized saving has order \(1/\log p\),
larger than the \(O(1/p)\) compulsory shared-endpoint contribution. The
statement is a proved saving, not a claim that it suffices after taking the
envelope maximum.

For \(u\ge0\), the available row budget therefore satisfies the explicit bound

\[
 \mathcal E_P(u)=\frac{U^2-S}{2}-T_P(u)
 \le\frac{U^2-S}{2}
       -\left(\frac{U^2}{4C\log(2p)}-\frac{pS}{2}\right)_+ . \tag{8}
\]

No all-history conclusion is inferred by adding (7) over prefixes: the
envelope charges physical labels, and sums over prefix masks may count the
same removed source many times.

## 2. Positive-semidefinite matrix extension

Let \(W\) be a real symmetric positive-semidefinite matrix indexed by \(F\).
Write

\[
 Q=\mathbf1^TW\mathbf1,\qquad S=\operatorname{tr}W,
 \qquad T_P(W)=\sum_{d<e,\ e-d\in\Delta P}W_{de}.        \tag{9}
\]

Define \(V_{z,d}=1[z-d\in P]\), with rows covering the same integer interval
of length \(L\) as in (2). Sidon injectivity gives

\[
 \operatorname{tr}(VWV^T)=pS+2T_P(W),\qquad
 \mathbf1^TVWV^T\mathbf1=p^2Q.                        \tag{10}
\]

For any positive-semidefinite \(L\)-by-\(L\) matrix \(Z\),
\(\operatorname{tr}Z\ge L^{-1}\mathbf1^TZ\mathbf1\): the matrix
\(I-L^{-1}\mathbf1\mathbf1^T\) is positive semidefinite and its trace pairing
with \(Z\) is nonnegative. Hence

\[
 \boxed{\quad pS+2T_P(W)\ge p^2Q/L.\quad}              \tag{11}
\]

Equivalently, for the old-difference adjacency matrix
\(A_{de}=1[d\ne e,\ |d-e|\in\Delta P]\),

\[
 pI+A-(p^2/L)\mathbf1\mathbf1^T\succeq0.              \tag{12}
\]

Thus (4)–(7) extend with \(U^2\) replaced by \(Q\). If \(W\) also has
nonnegative entries, its off-diagonal contributions remain nonnegative, as
required by the positive one-label capacity. This is an extension to the
intersection of the positive-semidefinite and entrywise-nonnegative cones;
no closure under subsequent masking is assumed.

The same convolution-matrix calculation with a future Sidon shell of size
\(m\) gives the diagonal term \(mS\) and the off-diagonal sum over its actual
difference labels. Since \(F\subseteq\Delta P\), rows corresponding to points
of that compatible future shell vanish. Consequently the denominator
\(L_{\mathrm{future}}+\max F-m\) from the earlier shadow inequality is valid
for these matrices as well. The diagonal term does not disappear in the
matrix extension.

## 3. Survival masking fails even for productive finite capped prefixes

Let

\[
 P_0=\{1,2,5,11\},\qquad
 \Delta P_0=\{1,3,4,6,9,10\},\qquad F_0=\{1,3,10\}.
\]

This is a Sidon set. Of the differences between labels in \(F_0\), only
\(10-1=9\) is in \(\Delta P_0\); \(3-1=2\) and \(10-3=7\) are not.
Starting from \(W=\mathbf1\mathbf1^T\), remove the old off-diagonal entries
and retain the diagonal. The resulting principal matrix is

\[
 M=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix},
 \qquad (1,-1,1)M(1,-1,1)^T=-1.                       \tag{13}
\]

So this nonnegative survival mask does not preserve positive semidefiniteness.
The defect is not confined to weights with low effective rank. Here is an
explicit extension preserving the principal obstruction.

For any odd prime \(r\), let

\[
 S_r=\{4ri+(i^2\bmod r):0\le i<r\},\qquad
 P=P_0\cup(150+100S_r).                               \tag{14}
\]

The set \(S_r\) is Sidon. Equality of two positive differences first forces
their index differences to agree: the difference of their remainder errors
has absolute value less than \(2r\), whereas a nonzero main-term difference
has absolute value at least \(4r\). For the common index difference
\(d\in\{1,\ldots,r-1\}\), reduction modulo \(r\) then gives
\(2d(i-i')=0\), whence \(i=i'\) and both endpoints agree.

Internal labels in the new block are positive multiples of 100, whereas old
labels are at most 10. Every cross label exceeds 10 and has residue
\(50-a\pmod{100}\), \(a\in P_0\), which is nonzero. Thus cross/internal
collisions are excluded. Cross-star injectivity follows from the disjoint
internal difference sets, as in the exact prefix extension criterion.
Therefore \(P\) is an actual Sidon set.

Its new internal or cross labels cannot equal 2 or 7, while 9 remains an old
label. Hence (13) remains a principal submatrix of the survival mask on the
full label set \(F=\Delta P\). Write \(p=r+4\). Then

\[
 \operatorname{diam}P<400r^2+150,
 \qquad |F|=\binom p2.
\]

For any fixed \(C>0\), all sufficiently large choices of \(r\) satisfy both
\(\max P\le Cp^2\log(2p)\) and
\(|F|>5Cp\log(4p)\). Uniform weights on this full label bank are therefore
productive in the sense of §1, yet their survival matrix is not positive
semidefinite. This is a finite, local-cap counterexample to automatic
positive-semidefinite closure. These prefixes as \(r\) varies are not one
nested infinite history with one fixed onset.

## 4. A positive-semidefinite repair has an unavoidable diagonal cost

Suppose a repaired symmetric matrix \(W\succeq0\), with \(Q>0\), has zero
entries at every old off-diagonal edge. Equation (11) immediately forces

\[
 \frac{Q}{\operatorname{tr}W}\le\frac{L}{p}
 \le2Cp\log(2p).                                     \tag{15}
\]

This is incompatible with the coarse-demand productive threshold
\(Q/\operatorname{tr}W>5Cp\log(4p)\). It applies regardless of how the repair
was constructed. Fully removing the old mask while returning to this cone
cannot preserve the effective rank needed for that lower-bound mechanism.

There is a quantitative version for diagonal repair. Let a symmetric
entrywise-nonnegative surviving matrix have total mass \(Q\), trace \(S\),
and zero old edges, and add a nonnegative diagonal of total trace \(\tau\).
If the result is positive semidefinite, (11) gives, whenever \(L>p\),

\[
 \boxed{\quad
 \tau\ge\left(\frac{pQ/L-S}{1-p/L}\right)_+.
 \quad}                                               \tag{16}
\]

The total mass as well as the trace increases by \(\tau\), which is why the
denominator in (16) is present. The future shadow's diagonal cost increases
by \(m\tau\), so it must be included in any attempted iterative gain.
One cannot subtract the old-mask mass, restore positivity for free, and
reapply (7) to the survivor.

More generally, if some old entries remain, (11) states the exact tradeoff
\(2T_P(W)\ge p^2Q/L-p\operatorname{tr}W\). A productive matrix must retain
positive old expenditure. The mask lower bound is therefore not a uniform
independent hazard on arbitrary conditioned pairs: conditioning leaves the
cone on which its proof operates, or a repair pays the displayed diagonal
cost.

## 5. A stationary row choice has an exact masked-envelope formula

Here keep nonnegative old vectors \(u_k\), so \(K_k(t)\ge0\), and suppress
only the future-span mask. This gives a valid upper envelope; the possibility
of extra span saving is analyzed separately in §6. Consider the natural
coefficient choice

\[
 \alpha_{kj}=c_k\ge0\qquad(j\ge k),\qquad
 G_j(t)=1[t\notin\Delta P_j]\sum_{k\le j}c_kK_k(t),      \tag{17}
\]

over a finite contiguous range of dyadic indices. Let \(\rho(t)\) be the first
dyadic index at which \(t\in\Delta P_{\rho(t)}\), or \(\infty\) if it is
unused in the terminal history. Before that index the sum in (17) increases;
at and after that index the mask sets it to zero. Thus

\[
 \boxed{\quad
 \max_jG_j(t)=\sum_k c_kK_k(t)1[t\notin\Delta P_k].
 \quad}                                               \tag{18}
\]

In particular

\[
 \sum_{t>0}\max_jG_j(t)=\sum_kc_k\mathcal E_{P_k}(u_k).  \tag{19}
\]

This is an identity for the **masked physical-label envelope**, not for a
raw unmasked pair budget. Although taking a maximum saves repeated copies
relative to summing over all future shells, it does not create an additional
saving beyond the row remainders on the right of (19) for this coefficient
choice. The new bound (8) may be inserted there, but no additional factor is
generated by the maximum itself.

There is a related warning even with only one fixed old vector. If its
coefficient is the same at every later epoch and the span masks are inactive,
every label still unused at the first epoch already achieves its envelope
value there. Masking that label at a later time leaves this earlier maximum
unchanged. Consequently the sum of later mask expenditures cannot simply be
subtracted from the envelope cost.

For genuinely time-dependent \(\alpha_{kj}\), (18) need not hold. Thus the
next coefficient search must retain its dependence on both old and future
indices, or use the actual-span information or a different signed kernel.

## 6. The actual-span mask disappears outside a short near-diagonal band

Let \(p_k=2^k\), \(m_j=2^j\), and
\(B_j=\{a_{m_j+1},\ldots,a_{2m_j}\}\). Its actual interval length is
\(L_j=a_{2m_j}-a_{m_j+1}+1\). Sidon injectivity within this shell yields

\[
 L_j-1\ge\binom{m_j}{2}\ge m_j^2/4\quad(m_j\ge2).      \tag{20}
\]

Every old vector supported on \(\Delta P_k\) has
\(K_k(t)=0\) for \(t>H_k-1\), where
\(H_k=\operatorname{diam}P_k\). Under (1),
\(H_k\le Cp_k^2\log(2p_k)\). Hence if

\[
 j-k\ge r_k:=
 \max\left(0,\left\lceil\log_2\bigl(2\sqrt{C\log(2p_k)}\bigr)
                       \right\rceil\right),           \tag{21}
\]

then \(m_j^2/4\ge H_k\), and

\[
 1[t\le L_j-1]K_k(t)=K_k(t)\quad\text{for every }t.      \tag{22}
\]

Thus actual-span suppression of this old kernel is possible only for
\(j-k<r_k=O_C(\log k)\). This conclusion uses both the cap on the old span
and full difference uniqueness in the future shell. It is uniform over
endpoint/rank weights on the old label set.

For unit-normalized row coefficients, the sum of the specified coarse demand
lower bounds within this near band is at most

\[
 \frac{r_kU_k^2}{10C\log(4p_k)}
 =O_C\!\left(U_k^2\frac{\log k}{k}\right).              \tag{23}
\]

For a full old bank, the useful range extends through order \(k\) future
epochs, and its total coarse demand is of order \(U_k^2\), with constants
depending on \(C\). Thus the near band contributes a vanishing fraction of
that particular row demand. This is not a general impossibility result:
time-dependent coefficients can concentrate on the near band, in which case
their capacity must be compared anew. It does show that span savings cannot
be assumed throughout the long useful window.

## 7. Cross-label expenditure need not have a positive local lower bound

An independent review by /root/global_route supplied the following exact
separation example. Take any finite Sidon set split in position order as
\(R=P\dot\cup B\), with equal block sizes, and let
\(H=\operatorname{diam}R\). Translate just the upper block by \(2H+1\).
Internal labels remain those of \(R\), hence remain disjoint. All cross
labels are now larger than \(H\); cross-star injectivity still follows from
the disjoint internal labels. The translated union is therefore Sidon.

Its span is \(3H+1\). For every old vector supported on \(\Delta P\),
\(K_u(t)\) vanishes for \(t\ge H\). Consequently its old/new cross expenditure
is exactly zero. Starting with near-quadratic finite Sidon sets, such as the
elementary prime construction used in (14), preserves a total span of order
the square of the block size. Thus a uniform positive local cross-cost claim
is false even in finite configurations meeting a critical local cap.

This does not settle a cumulative cross-cost lower bound for one infinite
history satisfying (1). The construction changes with the finite size; its
cap onset is not fixed across all those examples.

## 8. Complete time-coefficient reduction for one old kernel

Fix one old vector \(u\ge0\), and a consecutive range of future epochs
\(j=a,\ldots,b\) in which its actual-span masks are identically one. Section 6
supplies such a far range under (1). Write

\[
 K(t)=K_u(t),\qquad
 E_j=\sum_{t\notin\Delta P_j}K(t),\qquad
 \delta_j=\frac12\left(
 \frac{m_j^2U^2}{L_j+\max F-m_j}-m_jS\right)_+ .       \tag{25}
\]

For arbitrary nonnegative time coefficients \(\alpha_j\), the demand and
exact envelope cost are

\[
 D(\alpha)=\sum_{j=a}^b\alpha_j\delta_j,\qquad
 C(\alpha)=\sum_t K(t)\max_{\substack{a\le j\le b\\
                                      t\notin\Delta P_j}}\alpha_j, \tag{26}
\]

where a maximum over an empty set is zero. The masks are nested: for a fixed
label, the eligible epochs form an initial segment of this range.

Set \(b_j=\max_{a\le\ell\le j}\alpha_\ell\). Then
\[
 C(b)=C(\alpha),\qquad D(b)\ge D(\alpha).               \tag{27}
\]
Indeed the maximum on every initial segment is unchanged, while demand
coefficients increase. Thus nondecreasing time coefficients suffice for the
entire one-kernel variational problem, not merely a selected test family.

Define \(\gamma_a=b_a\) and
\(\gamma_r=b_r-b_{r-1}\ge0\) for \(a<r\le b\). Finite summation gives

\[
 \boxed{\qquad
 C(b)=\sum_{r=a}^b\gamma_r E_r,\qquad
 D(b)=\sum_{r=a}^b\gamma_r\sum_{j=r}^b\delta_j.
 \qquad}                                             \tag{28}
\]

The cost identity follows label by label: a source contributes exactly those
increments \(\gamma_r\) occurring before it becomes an old difference.
Equivalently, with \(E_j-E_{j+1}\) the new-label expenditure between adjacent
prefixes,

\[
 C(b)=\sum_{j=a}^b b_j(E_j-E_{j+1})+b_bE_{b+1}.        \tag{29}
\]

Here \(E_j-E_{j+1}\) includes both the internal labels of \(B_j\) and the
old/new cross labels. The last term is the terminal surviving-label cost.
Thus increasing time coefficients truly weight retirement times, but do
not remove the cross or terminal terms.

For \(E_r>0\), define \(R_r=(\sum_{j=r}^b\delta_j)/E_r\). If \(E_r=0\), an
actual Sidon history also has \(\sum_{j=r}^b\delta_j=0\), by the common-budget
inequality; such a zero term can be ignored. Equation (28) proves the exact
variational value

\[
 \boxed{\quad
 \sup_{\alpha\ge0,\ C(\alpha)>0}
       \frac{D(\alpha)}{C(\alpha)}
 =\max_{a\le r\le b,\ E_r>0}
       \frac{\sum_{j=r}^b\delta_j}{E_r}.
 \quad}                                               \tag{30}
\]

If all \(E_r\) vanish the useful demand is zero. Every nonzero ratio in
(30) is attained by the step choice
\(\alpha_j=1[j\ge r]\). This is a complete analytic reduction of the finite
time-coefficient choice for one old kernel. It is not merely the observation
that an actual history has value at most one.

The quantitative mask bound transfers through the envelope correctly via
(28):
\[
 C(b)\le\sum_r\gamma_r
 \left[\frac{U^2-S}{2}
 -\left(\frac{p_r^2U^2}{2(\operatorname{diam}P_r+
                                 \operatorname{diam}F+1)}
                          -\frac{p_rS}{2}\right)_+\right]. \tag{31}
\]
This uses each mask with the increment \(\gamma_r\), rather than subtracting
an unweighted sum of masks after a maximum. The right side is still only an
upper bound for the actual cap-compatible history; no uniform strict
demand/capacity separation has been obtained from it.

With several old kernels, replacing each row by its separate running maximum
can increase the envelope: old-kernel peaks may occur at different epochs
and their sum is what one epoch must pay. Thus (30) does not reduce the full
coupled problem to independent rows. That coupling, or actual-span
information in the near band, is where an additional time-selection gain
would have to enter.

## 9. Remaining variational obligation

For fixed old vectors, actual interval lengths, and used-label masks, the
finite linear program in the previous note remains the precise candidate:
choose \(\alpha_{kj}\ge0\), set

\[
 G_j(t)=1[t\le L_j-1]1[t\notin\Delta P_j]
             \sum_{k\le j}\alpha_{kj}K_k(t),\qquad
 \mu(t)=\max_jG_j(t),                                  \tag{32}
\]

and compare its total exact diagonal-corrected shadow demand with
\(\sum_t\mu(t)\). Equations (7) and (11) now give a quantitative constraint
on each productive old carrier, while (15)–(16) prevent cost-free repeated
conditioning. Equation (19) settles the stationary row choice, (22) locates
the range where actual-span information can affect the kernels, and (30)
solves the time selection for one old kernel outside that range.

A genuinely new gain would require a proved relation between the locations
of the maxima in (32), the first appearance times of their physical labels,
and the evolution of productive old carriers. An all-prefix cap gives (7)
but has not yet been shown to force that relation. Summing mask lower bounds
before taking the maximum, or treating conditional survivors as independent
productive carriers, would both leave a mathematical gap.

No uniform choice of the time-dependent coefficients has been proved to
make demand exceed capacity under (1). The new quantitative mask saving is
real, but its conversion into the original Q1 contradiction is unresolved.

## 10. Verification scope

The weighted convolution identity, its matrix extension, and the productive
diagonal obstruction were also independently derived by the parent. The
parent checked the finite principal obstruction and the modular separation
used for its productive padding. /root/global_route supplied the exact
zero cross-cost construction in §7. The proofs of all claims used here are
included above; reported agreement is not substituted for their arguments.

No new solver, numerical test, enumeration, or Lean run was executed for this
note. In particular an LP value at most one for an actual finite Sidon
history is not reported as progress toward theorem closure. Original Q1
remains unresolved.

## 11. Localized productive carriers have a constant old-mask expenditure

Let \(p=2^k\to\infty\), fix \(0<\eta<1\), and put \(D=p^{1+\eta}\).
Let \(u=u_p\ge0\) have finite integer support of diameter at most \(D\), and
suppose
\[
 M:=U^2/S,\qquad M/p\longrightarrow\infty.             \tag{33}
\]
The support may be a subset of \(\Delta P_p\), but that restriction is not
needed for the next identity. For each past dyadic block
\[
 B_m=\{a_{m+1},\ldots,a_{2m}\},\qquad
 \sqrt D\le m\le p/2,
\]
write \(L_m=a_{2m}-a_{m+1}+1\). Sidon and Cauchy–Schwarz give
\[
 mS+2\Psi_u(B_m)
 =\sum_z\left(\sum_{a\in B_m}u_{z-a}\right)^2
 \ge\frac{m^2U^2}{L_m+\operatorname{diam}(\operatorname{supp}u)}
 \ge\frac{m^2U^2}{L_m+D}.                             \tag{34}
\]
This version does not exclude the points of \(B_m\) from the convolution
support, and retains the diagonal \(mS\).

For large \(p\), every selected block is beyond the same fixed onset.
We have \(L_m\le4Cm^2\log(4m)\), \(D\le m^2\), and \(1\le C\log(4m)\).
Thus
\[
 \Psi_u(B_m)\ge\frac{U^2}{10C\log(4m)}-\frac{mS}{2}.  \tag{35}
\]
The internal difference sets of these past blocks are pairwise disjoint
subsets of \(\Delta P_p\). Since \(K_u(t)\ge0\),
\[
 T_{P_p}(u)\ge
 \frac{U^2}{10C}\sum_{\sqrt D\le2^r\le p/2}
                         \frac1{\log(4\cdot2^r)}
 -\frac S2\sum_{\sqrt D\le2^r\le p/2}2^r.             \tag{36}
\]
The second sum is less than \(p\), giving normalized error at most
\(p/(2M)=o(1)\). The reciprocal-log sum tends to
\((\log2)^{-1}\log(2/(1+\eta))\), with rounding error \(O(1/\log p)\).
Therefore
\[
 \boxed{\quad
 \liminf_{p\to\infty}\frac{T_{P_p}(u_p)}{U_p^2}
 \ge\frac1{10C\log2}\log\frac2{1+\eta}>0 .
 \quad}                                               \tag{37}
\]
This proves the correlation with the old mask for **every** family of
localized nonnegative productive weights satisfying (33). It does not infer
correlation from the density of small old differences. The whole compatible
past, and its fixed-onset cap, are used in the sum (36).

A literal label selection supplies such weights. There are \(q=\binom p2\)
distinct old labels in \([1,H]\), \(H\le Cp^2\log(2p)\).
For \(w=\lfloor D\rfloor+1\), average the occupancies of all integer windows
of length \(w\), including those crossing either endpoint of \([1,H]\).
Each label is counted \(w\) times among \(H+w-1\) windows. One window thus
contains at least \(qw/(H+w-1)\) labels. It selects an actual
\(F\subseteq\Delta P_p\) with diameter at most \(D\) and
\[
 |F|\ge c_C D/\log p.
\]
For its unit weights, \(M=|F|\gg p\), and indeed \(M/(p\log p)\to\infty\).

The diameter version (34) is also a valid future-demand inequality. For old
label support, one may use the larger of it and the earlier lower bound
using the maximum label and excluding \(m\) points. The matrix proof in §2
applies block by block, so (37) also holds for entrywise-nonnegative PSD
matrices on a label interval of diameter \(D\), replacing \(U^2\) by
\(Q=\mathbf1^TW\mathbf1\) and assuming \(Q/(p\,\operatorname{tr}W)\to\infty\).
The parent and /root/global_route independently checked (34)–(37).

## 12. The matching past/future coefficient tradeoff

For \(D=p^{1+\eta}\), suppose
\[
 \log M=(1+\eta)\log p+O(\log\log p).                  \tag{38}
\]
The selected cluster above has this property, since its size lies between a
fixed multiple of \(D/\log p\) and \(D+1\). For future dyadic \(m\ge p\),
\(D\le m^2\), so the diameter bound supplies
\[
 \ell_m=\left(\frac{U^2}{10C\log(4m)}-\frac{mS}{2}\right)_+ .
\]
It is positive precisely when \(m<M/(5C\log(4m))\), and
\[
 \frac1{U^2}\sum_{\substack{m\ge p\\m\text{ dyadic}}}\ell_m
 \longrightarrow\frac1{10C\log2}\log(1+\eta).          \tag{39}
\]
The last positive rank has logarithm \(\log M-O_C(\log\log M)\).
Reciprocal-log summation gives (39); the total normalized diagonal loss is
\((2M)^{-1}\sum m=O_C(1/\log M)\), and the final boundary term is
\(O(1/\log p)\). A shorter range ending at \(M/(\log p)^2\) gives the same
lower asymptotic.

The coefficients of the past lower bound (37) and the future lower bound
(39) add to
\[
 \frac1{10C\log2}
 \left(\log\frac2{1+\eta}+\log(1+\eta)\right)
 =\frac1{10C}.                                      \tag{40}
\]
The new constant mask saving is real, but narrowing the carrier also
shortens its useful future rank window. A direct addition still gives a
constant normalized expenditure. The parent independently derived the same
complementary coefficients. This does not rule out a coupled-envelope gain;
it prevents mistaking (37) alone for Q1 closure.

One must next prove that this past expenditure removes a useful part of the
**actual maxima** of the coupled physical-label envelope, beyond the
tradeoff (40). That peak-alignment statement remains unresolved in general;
the next section proves a specific nested-bank saving.

## 13. A nested current bank loses at least half its final old mask in the historical maximum

Fix an integer width \(D\ge1\) and an actual finite Sidon sequence
\(a_1<\cdots<a_N\), with unique positive differences. Define the state
**after** point \(a_n\) has been added by
\[
 F_n=\Delta P_n\cap[1,D],\quad q_n=|F_n|,\quad
 K_n(t)=\sum_d1_{F_n}(d)1_{F_n}(d+t)\quad(t>0).
\]
Thus \(F_1=\varnothing\). Use unit weights on the current bank, keeping
one carrier at each time, rather than summing copies of older banks. Put
\[
 T_n=\sum_{t\in F_n}K_n(t),\qquad
 E_n=\sum_{t>0,\ t\notin F_n}K_n(t)=\binom{q_n}{2}-T_n,
 \qquad
 \mathcal C_N=\sum_{t>0}\max_{1\le n\le N}
                       1[t\notin F_n]K_n(t).        \tag{41}
\]
All kernels vanish for \(t\ge D\). On their support this mask equals
\(1[t\notin\Delta P_n]\). Omitting an additional actual future-span mask
only increases the envelope, so (41) also bounds selections with that mask.

### 13.1 Exact maximum on every physical-label fibre

Let \(\tau(t)\) be the first index with \(t\in F_n\), or \(\infty\)
if it has not appeared by \(N\). Before this time the mask is one and
\(K_n(t)\) is nondecreasing, because \(F_n\) is nested. At and after
this time the mask is zero. Therefore
\[
 \max_{1\le n\le N}1[t\notin F_n]K_n(t)
 =\begin{cases}
    K_{\tau(t)-1}(t),&\tau(t)\le N,\\
    K_N(t),&\tau(t)=\infty.
  \end{cases}                                      \tag{42}
\]
The earliest possible finite birth is two, and its previous bank is empty.
Thus a retired label is charged at its actual last state before retirement;
the final mask has not been subtracted from an earlier maximum.

At step \(n\ge2\), abbreviate
\[
 F=F_{n-1},\quad G=F_n\setminus F_{n-1},\quad g=|G|,
 \qquad R_n=\sum_{t\in G}K_F(t).
\]
The sets \(G\) partition the finite-birth labels. Summing (42) over those
fibres and over the labels that have not appeared gives the exact identity
\[
 \boxed{\mathcal C_N=E_N+R^{\rm tot}_N,\qquad
 R^{\rm tot}_N=\sum_{n=2}^N R_n.}                   \tag{43}
\]
The entire terminal unretired mass \(E_N\) is retained.

### 13.2 Every retirement has an accompanying pair born with a used difference

Each \(G\) consists exactly of the new labels \(a_n-a_i\le D\).
Positive-difference uniqueness gives \(F\cap G=\varnothing\). Two
distinct labels in \(G\) have positive difference in \(F\): their common
upper endpoint cancels, leaving an old difference at most \(D-1\).
Also \(G\) is sum-free, including repeated summands. The contrary equality
\((a_n-a_i)+(a_n-a_j)=a_n-a_k\) would give
\(a_n+a_k=a_i+a_j\), a forbidden Sidon equality with \(i,j,k<n\).

Use ordered representations
\(r_{X+Y}(z)=|\{(x,y)\in X\times Y:x+y=z\}|\), and define
\[
 S^{00}_n=\sum_{z\in G}r_{F+F}(z),\quad
 S^{11}_n=\sum_{z\in F}r_{G+G}(z),\quad
 Z_n=S^{00}_n+2\binom g2+S^{11}_n\ge0.               \tag{44}
\]
The equality \(T(F)=\sum_{z\in F}r_{F+F}(z)\) counts a repeated summand
once and distinct summands in both orders. Expanding it for \(F\cup G\)
has these exhaustive contributions:

- For old output \(z\in F\), the old \(F+F\) term is unchanged;
  \(F+G\) and \(G+F\) total \(2R_n\), and \(G+G\) gives \(S^{11}_n\).
- For new output \(z\in G\), \(F+F\) gives \(S^{00}_n\). The two mixed
  terms total \(2\binom g2\), because all positive \(G-G\) differences
  lie in \(F\). The \(G+G\) term is zero by sum-freeness.

It follows, with no omitted diagonal representations, that
\[
 T_n-T_{n-1}=2R_n+Z_n,\qquad
 T_N=2R^{\rm tot}_N+Z^{\rm tot}_N,\qquad
 Z^{\rm tot}_N=\sum_{n=2}^N Z_n.                    \tag{45}
\]
Equivalently, \(R_n\) old label pairs retire at this step. Among the new
label pairs, exactly \(R_n+Z_n\) have their positive difference already
in \(F_n\). They never contribute a positive historical-envelope value.
In particular each retirement has at least one such simultaneous birth.
This is a literal count of pairs and their times, not a renewed budget.

Combining (41), (43), and (45) proves
\[
 \boxed{\displaystyle
 \mathcal C_N
 =\binom{q_N}{2}-R^{\rm tot}_N-Z^{\rm tot}_N
 =\binom{q_N}{2}-\frac{T_N}{2}-\frac{Z^{\rm tot}_N}{2}
 \le\binom{q_N}{2}-\frac{T_N}{2}.}                  \tag{46}
\]
At least half the final old mask is therefore absent from the **actual
historical maximum** for this selection. The other half can have produced
a peak immediately before its physical label appeared; removing all of
\(T_N\) would be incorrect without additional information.

Selecting a subset of states \(n\le N\), including dyadic current carriers
with only \(\alpha_{jj}=1\), gives an envelope at most \(\mathcal C_N\).
An actual future-span mask can reduce it further. This argument does not
establish (46) for arbitrary sums of several old carriers at one epoch or
for arbitrary time-dependent coefficients.

The upper bound by half the mask also has a direct injection proof, which
shows that this part needs only nested positive-label banks. If an old
pair \(\{d,e\}\), \(d<e\), retires when \(t=e-d\) is born, then the
new pair \(\{t,e\}\) has difference \(d\), which was already present.
The map \(\{d,e\}\mapsto\{e-d,e\}\) is injective: its larger element
is \(e\), so it recovers \(d\). The case \(t=d\) cannot retire an old
pair, since it would require \(d\) to be both present and newly born.
Consequently the count of pairs born with used differences is at least
the retirement count. This proves \(T_N\ge2R^{\rm tot}_N\) and the
upper bound in (46) even for arbitrary nested banks. The explicit
nonnegative decomposition (44)--(45), with its common-endpoint and
sum-free birth properties, retains more information from actual Sidon
histories than this injection alone.

### 13.3 Consequence under the same fixed-onset cap

Let \(D\to\infty\), fix \(1/2<\theta<1\), and take
\(N=2^{\lfloor\theta\log_2 D\rfloor}\). The fixed-width bank-density
proof in `fixed_width_bank_density.md` gives \(q_N\ge c_{C,\theta}D\)
for all sufficiently large \(D\), using the same fixed onset. Its dyadic
rounding variant follows directly from the proof there. This is not a new
independent density assumption. For completeness the required argument is:
convolve each past block \(B_m\), \(\sqrt D\le m\le N/2\), with the
integer interval of length \(D\). Its exact energy is
\(mD+2\sum_{t\in\Delta B_m}(D-t)_+\). Support Cauchy--Schwarz and
\(L_m+D-1\le5Cm^2\log(4m)\) give
\[
 \frac1D\sum_{t\in F_N}(1-t/D)
 \ge\frac1{10C}
       \sum_{\sqrt D\le2^r\le N/2}\frac1{\log(4\cdot2^r)}
       -\frac{N}{2D}
 =\frac{\log(2\theta)}{10C\log2}-o(1).
\]
In particular \(q_N/D\) has a positive lower bound. For unit weights on
\(F_N\), the past-block proof of (36) now gives
\[
 \liminf_{D\to\infty}\frac{T_N}{q_N^2}
 \ge\frac{\log(2\theta)}{10C\log2}.
\]
The normalized diagonal error is at most \(N/(2q_N)=o(1)\). Dyadic
rounding contributes \(O(1/\log D)\) to the reciprocal-log sum. Thus
\[
 \boxed{\displaystyle
 \limsup_{D\to\infty}\frac{\mathcal C_N}{q_N^2}
 \le\frac12-\frac{\log(2\theta)}{20C\log2}.}         \tag{47}
\]
This is a nonzero loss in a history-sensitive envelope. It remains a
constant loss; neither (46) nor (47) gives a contradiction for every fixed
\(C\), or a growing saving across widths. Additional control of the
retirement flux, the \(S^{00}\) birth term, or the interaction of different
widths is still required. Original Q1 remains unresolved.

The birth flux was derived independently by /root/global_route in
`nested_small_difference_bank.md`; its expansion is reproduced above.
That agent also independently checked the fibre maximum (42) and the
identity (46). No numerical experiment, enumeration, or new Lean check was
used for this section.

## 14. The half-mask coefficient is sharp without the fixed critical cap

For every integer \(D\ge2\), an actual finite Sidon history realizes the
descending single-label bank births
\[
 \varnothing,\ \{D\},\ \{D-1,D\},\ldots,\{1,\ldots,D\}.
                                                               \tag{48}
\]
This supplies a counterexample to strengthening the coefficient \(1/2\)
in (46) by Sidon compatibility and nesting alone.

Here is a full construction. Start with no points and \(H_0=0\). For
\(s=1,\ldots,D\), set
\[
 d_s=D+1-s,\qquad X_s=4H_{s-1}+4D+1,
 \qquad H_s=X_s+d_s,
\]
and append the two points \(X_s,X_s+d_s\). At every stage all differences
between distinct two-point blocks exceed \(D\). Suppose the old set is
Sidon and has maximum \(H_{s-1}\). Every new difference to an old point
is at least \(X_s-H_{s-1}>\max(H_{s-1},D)\), so it cannot equal an old
difference or the new internal difference \(d_s\). Each of the two new
cross stars is injective. Equality between a difference from one star and
a difference from the other would give an old positive difference equal
to \(d_s\). This is impossible: its value is at most \(D\), and the
previous internal labels \(d_1,\ldots,d_{s-1}\) are distinct from it.
Thus all positive differences remain unique. The first point of a new
block produces no new label at most \(D\); the second produces only
\(d_s\). This proves (48), including the intermediate unchanged states.

At the birth of \(t=d_s\), the old bank is \(F=\{t+1,\ldots,D\}\)
and \(G=\{t\}\). Hence
\[
 R_t=K_F(t)=(D-2t)_+,\qquad S^{00}_t=0,\qquad
 2\binom{|G|}{2}=0,\qquad S^{11}_t=1[2t\le D].
\]
There is one ordered \(G+G\) representation when \(2t\in F\), so the
last term has coefficient one even on this repeated-summand diagonal.
At the end, with \(N=2D\), every kernel-supported difference belongs to
\(F_N=[1,D]\), and therefore \(E_N=0\). Exact summation gives
\[
 \mathcal C_N=R^{\rm tot}_N
   =\sum_{t=1}^D(D-2t)_+
   =\left\lfloor\frac{(D-1)^2}{4}\right\rfloor,
 \quad T_N=\binom D2,\quad
 Z^{\rm tot}_N=\left\lfloor\frac D2\right\rfloor.   \tag{49}
\]
In particular \(\mathcal C_N/T_N\to1/2\). No universal improvement
\(\mathcal C_N\le\binom{q_N}{2}-(1/2+\varepsilon)T_N\), with a
fixed \(\varepsilon>0\), holds for all actual Sidon histories.

This family lies outside the cap-relevant early-rank regime. It uses
\(N=2D\), not \(D^\theta\) with \(\theta<1\), and
\[
 H_D\ge(4D+1)(4^D-1)/3.
\]
For any fixed \(C\), even its terminal critical bound
\(H_D\le C(2D)^2\log(4D)\) fails for large \(D\). The construction is
not a counterexample to Q1 or to a stronger estimate using the full
fixed-onset cap. It identifies why iterating the half-mask saving requires
additional cap-sensitive information, rather than just the same nesting
identity again. All of (48)--(49) is symbolic; no computation was run.
The agent /root/global_route independently read and verified the complete
construction, the cross-star collision exclusion, the diagonal coefficient,
the even/odd summation, and the stated scope.

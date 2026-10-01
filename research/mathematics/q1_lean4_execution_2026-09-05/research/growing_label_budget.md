# Growing prefixes: birth accounting and a physical-label envelope

Date: 2026-09-05. Owner: `/root/c143_mathematics`.
Other researchers' files and original evidence were left unchanged.

Status: the original Erdős #1191 Q1 remains unresolved. This note proves
exact finite bookkeeping identities, counterexamples to two overstrong
amortization claims, and a different variational inequality with a genuine
global upper bound on one copy of each physical difference label. It does not
prove that the latter inequality closes under the fixed-onset critical cap.
No statement in this note is claimed to have been checked by Lean.

All logarithms are natural. Write \(A_p=\{a_1<\cdots<a_p\}\) for prefixes of
one Sidon sequence of positive integers. Repeated summands are included in
the Sidon condition. Every positive difference therefore has unique
endpoints. The conventions and finite weighted shadow inequality used below
are proved in [difference_extension_route.md](difference_extension_route.md).

## 1. A relation has distinct birth, first-endpoint, and last-endpoint times

For a used positive label \(d=a_j-a_i\), \(i<j\), let \(b(d)=j\). This is
its first appearance rank. Let a **relation** mean an unordered pair of
different used positive labels; order it as \(d_1>d_2\), and put

\[
 t(R)=d_1-d_2>0,\qquad h(R)=\max(b(d_1),b(d_2)).       \tag{1}
\]

The four old endpoints, with repetitions if two labels share an endpoint,
are part of the identity of \(R\). Different relations can have the same
\(t\); Sidon does not prohibit those six-point equations.

If \(t\) is itself a difference of the sequence, write its unique endpoints
as \(t=a_{v(t)}-a_{u(t)}\), with \(u(t)<v(t)\). If \(t\) is not used, set
both times to \(\infty\). For a finite horizon, the same convention is used
for labels not used within that horizon.

For every prefix rank \(p\ge h(R)\), the classification of this relation is
exactly:

\[
\begin{array}{c|c}
 p<u(t)<v(t)<\infty&\text{both endpoints of }t\text{ are future}\\
 u(t)\le p<v(t)<\infty&\text{one old and one future endpoint}\\
 v(t)\le p&\text{both endpoints are old}\\
 u(t)=v(t)=\infty&\text{unused label}.
\end{array}                                                    \tag{2}
\]

Consequently a relation can contribute to a future/internal-shell demand
only at prefix ranks

\[
 h(R)\le p<u(t),\quad v(t)<\infty.                    \tag{3}
\]

Its two future endpoints must additionally be in the particular shell under
consideration. The condition \(h\le p<v\) alone is insufficient: it includes
old/new cross differences. The birth rank of \(t\) is \(v\), whereas the
end of the both-future period is \(u\).

For \(p_k=2^k\), define \(\kappa(r)=\lceil\log_2 r\rceil\). With an infinite
future available, the eligible dyadic indices for a used label are

\[
 \kappa(h(R))\le k<\kappa(u(t(R))).                  \tag{4}
\]

The formula also handles an empty interval. A finite terminal horizon imposes
the further condition that \(v(t)\) is within that horizon.

## 2. Exact injection and retirement conservation

Fix a finite terminal set \(A_M\), and a fixed nonnegative weight \(w_R\) for
each relation formed from its difference labels. Set

\[
 E_p=\sum_R w_R\,1[h(R)\le p<v(t(R))].               \tag{5}
\]

This potential includes both future categories in (2) and labels unused at
the terminal horizon. Define the birth injection and completed retirement by

\[
 B_p=\sum_R w_R\,1[h(R)=p<v(t(R))],\qquad
 D_p=\sum_R w_R\,1[h(R)<p=v(t(R))].                  \tag{6}
\]

Then, without approximation or resetting a budget,

\[
 E_p-E_{p-1}=B_p-D_p.                                \tag{7}
\]

A relation born with \(h=v=p\) never enters \(E_p\), so it belongs to neither
term in (6). Each other relation enters at most once and retires at most once.
For any scalar sequence \(\lambda_p\), Abel summation gives

\[
\begin{split}
 \sum_{p=p_0+1}^{M}\lambda_pD_p
 ={}&\lambda_{p_0}E_{p_0}-\lambda_ME_M
       +\sum_{p=p_0+1}^{M}\lambda_pB_p\\
    &+\sum_{p=p_0+1}^{M}(\lambda_p-\lambda_{p-1})E_{p-1}.
\end{split}                                                    \tag{8}
\]

In particular the last term is nonpositive for decreasing \(\lambda\), but
the birth term remains. Dropping the last term can give a valid upper bound;
dropping the birth term does not. An analogous identity for only the first
category in (2) replaces the retirement time \(v\) by \(u\) and excludes
unused labels. It depends on the specified terminal history, since the later
endpoint must actually exist.

For a dyadic coefficient \(c_k\ge0\), define its finite tail
\(T_r=\sum_{k=r}^{K}c_k\), with \(T_{K+1}=0\). A used relation's exact
occupation charge is

\[
 \sum_{k=0}^{K}c_k1[h(R)\le2^k<u(t(R))]
 =T_{\kappa(h(R))}-T_{\min(\kappa(u(t(R))),K+1)},      \tag{9}
\]

where the right side is interpreted as zero if the first index exceeds the
second. Thus its charge is a difference of a birth-tail and an exit-tail.
This is a way to allocate repeated uses to one relation, but does not bound
the sum of the birth-tails over different relations.

## 3. Why summable charge for each relation is not a finite global budget

First consider the unfiltered old-pair budget, with coefficient
\(c_k=\beta_kp_k^{-4}\), \(\beta_k\ge0\). A relation born at \(h\) has raw
charge

\[
 W_{h,K}=\sum_{k=\kappa(h)}^K\beta_k16^{-k}.           \tag{10}
\]

For \(\beta_k=1\), its infinite charge is
\((16/15)16^{-\kappa(h)}\), in particular finite and comparable to
\(h^{-4}\).

However, put \(q_p=|\Delta A_p|=\binom p2\). The exact number of relations
born at rank \(h\) is

\[
 \binom{q_h}{2}-\binom{q_{h-1}}{2}
 =\frac{h(h-1)(h-2)}2.                               \tag{11}
\]

Interchanging two finite sums gives

\[
\begin{split}
 \sum_R W_{h(R),K}
 &=\sum_{k=0}^{K}\beta_kp_k^{-4}\binom{q_{p_k}}2\\
 &=\sum_{k=0}^{K}\beta_k
 \left(\frac18-\frac1{4p_k}-\frac1{8p_k^2}
                       +\frac1{4p_k^3}\right).       \tag{12}
\end{split}
\]

Thus unit coefficients give \(K/8+O(1)\). For arbitrary nonnegative
coefficients, convergence of this raw budget is equivalent to convergence of
\(\sum_k\beta_k\), after omitting finitely many initial ranks. Reassignment
to first appearance changes neither (11) nor (12).

This identity does not depend on the positions of the Sidon points. It is
not an actual counterexample to a cap-dependent theorem: the nonexistence of
arbitrarily long fixed-onset capped histories would be an additional
mathematical result. It does show that rank bookkeeping alone cannot make
the positive term in (12) bounded independently of the number of prefixes.

### 3.1 Actual Sidon example with a large permanently unused budget

Take \(a_i=10^i\). A vanishing signed sum involving at most six such powers
must have zero coefficient at every exponent after equal powers are
collected: otherwise its largest nonzero power dominates the at most five
remaining smaller signed terms. This also proves the Sidon property,
including repeated summands.

For two different old labels, \(d_1-d_2\) is another difference of this
sequence precisely when their two physical intervals share their left
endpoint or share their right endpoint. All other four-endpoint expressions
retain too many nonzero powers of ten. Hence, for this actual infinite set,

\[
 \#\{R\subseteq\Delta A_p:t(R)\text{ is used}}
 =2\binom p3.                                      \tag{13}
\]

These represented labels are already old when the relation is born. All
other relations have an unused label forever. Their normalized raw sum over
dyadic prefixes is still \(K/8+O(1)\). Thus excluding already-used old labels
does not repair the inference from per-relation summability to a globally
finite budget. This example violates the critical cap; it isolates the
invalid inference from Sidon and birth accounting alone.

## 4. Actual future usage can also have divergent normalized total charge

The previous example leaves many labels unused. The following stronger
counterexample makes every positive integer an actual difference and still
has divergent normalized charge in the **both-future** category of (2).

Construct pairs recursively. At stage \(s\), let

\[
 d_s=\min\bigl(\mathbb N_{>0}\setminus\Delta A_{2s-2}\bigr),
 \qquad x_s=10^{10^s},\qquad
 (a_{2s-1},a_{2s})=(x_s,x_s+d_s).                    \tag{14}
\]

The empty initial set is allowed. Since there are at most
\(\binom{2s-2}{2}\) old positive labels,

\[
 1\le d_s\le\binom{2s-2}{2}+1\le2s^2.              \tag{15}
\]

The choice of \(x_s\) satisfies \(x_s>2\max A_{2s-2}+d_s\). All newly added
cross labels are larger than old labels and larger than \(d_s\). The two
cross stars can collide only through
\(x_s-a=x_s+d_s-b\), which would mean \(b-a=d_s\in\Delta A_{2s-2}\), contrary
to its choice. Within each star labels are distinct. Thus (14) preserves
the Sidon condition at every step.

After stage \(s\), every integer from \(1\) through \(s\) is represented,
by induction on the least missing label. Therefore the resulting infinite
Sidon set has

\[
 \Delta A=\mathbb N_{>0}.                            \tag{16}
\]

Let \(p=2s\) be dyadic, \(p\ge32\), and consider the last \(s/2=p/4\)
completed blocks. Choose four distinct block indices from them, use the base
points \(x_i\) in those blocks, and partition the four indices into two
unordered pairs in any of the three possible ways. Their two positive
differences are distinct labels, and define a relation \(R\).

For every such relation,

\[
 t(R)\notin\Delta A_p.                              \tag{17}
\]

Here is an explicit dominance proof. If \(t(R)\) equaled an old physical
difference, move its two endpoints to the other side. The expression has at
most six base terms \(x_i\), with total absolute coefficient at most six,
and offsets of total absolute value at most \(12s^2\) by (15). The two
candidate endpoints cannot cancel all four distinct late block indices, so
the largest nonzero base coefficient is at an index \(J>s/2\). But

\[
 x_J>6x_{J-1}+12s^2
\]

for these indices, making the equality impossible. The displayed dominance
follows directly from \(x_j=10^{10^j}\) and \(s<2J\); it is much stronger
than needed.

Also \(t(R)\le\operatorname{diam}A_p\). Every subsequently introduced cross
label exceeds this old span. In view of (16), \(t(R)\) must therefore first
appear as the internal difference \(d_r\) of a later two-point block. Both
of its endpoints have rank greater than \(p\). Thus every relation just
counted is an actual both-future relation, not a permanently unused label.

Different block selections or pairings give different pairs of labels,
because labels retain their unique endpoints. Their values of \(t\) need
not be different, which is permitted. Consequently

\[
 \#\{R:h(R)\le p<u(t(R)),\ v(t(R))<\infty\}
 \ge3\binom{p/4}{4}\ge2^{-15}p^4\quad(p\ge32).      \tag{18}
\]

The last constant is deliberately conservative. Multiplying (18) by
\(p^{-4}\) and summing over dyadic \(p\) proves divergence. Each individual
relation still has finite charge by (10). For any finite number of these
prefixes, all the finitely many required future realizations occur in a
sufficiently long finite terminal segment, so this is also a family of
literal finite counterexamples to a horizon-independent bound based solely
on those hypotheses.

The positions in (14) grow far faster than \(Cn^2\log(2n)\). Thus (18)
refutes a general Sidon-only assertion about actual future usage. It does
not refute an assertion using the fixed-onset critical cap materially.

## 5. Arbitrary nonnegative old-label weights do not fix raw birth cost

The issue in (12) is not confined to unit weights. At prefix \(p_k\), choose
any nonnegative label vector \(u_k\) supported on \(\Delta A_{p_k}\), and put

\[
 U_k=\sum_d u_k(d),\quad S_k=\sum_d u_k(d)^2,
 \quad M_k=U_k^2/S_k\quad(U_k>0).                    \tag{19}
\]

The effective number of labels satisfies \(1\le M_k\le q_{p_k}\).
For arbitrary \(\beta_k\ge0\), the raw charge of a pair of labels is
\(\sum_k\beta_ku_k(d_1)u_k(d_2)\), over the prefixes containing both labels.
Its sum over all relations is exactly

\[
 \mathcal B_K=\frac12\sum_{k\le K}\beta_k(U_k^2-S_k). \tag{20}
\]

This remains true if every term is assigned to the relation's first
appearance. Adaptively selecting the support or its weights does not change
the identity.

For comparison with demands, assume the same fixed \(C,n_0\) cap as in the
previous note,

\[
 a_n\le Cn^2\log(2n)\qquad(n\ge n_0).               \tag{21}
\]

For \(p=p_k\ge\max(n_0,2)\), use a future dyadic shell of size
\(m=2^rp\). The coarse cap gives a valid lower bound

\[
 \Psi_{u_k}(B)
 \ge\left(\frac{U_k^2}{10C\log(4m)}-\frac{mS_k}{2}\right)_+ . \tag{22}
\]

If this lower bound is positive for even one \(m\ge p_k\), then necessarily

\[
 M_k>5Cp_k\log(4p_k).                               \tag{23}
\]

In particular \(S_k/U_k^2\to0\) on the prefixes selected by this particular
lower-bound mechanism. On these prefixes, finiteness of (20) is equivalent
to finiteness of \(\sum_k\beta_kU_k^2\).

Furthermore positivity in (22) requires \(m<M_k/(5C\log(4m))\), and
\(M_k\le q_{p_k}\). The sum of its reciprocal-log terms over all relevant
dyadic \(m\) is bounded by an absolute constant for sufficiently large
\(p_k\), with a harmless initial range depending on \(C\). It follows that
the sum of all the **coarse lower bounds** in (22), for a single prefix, is
at most \(O_C(U_k^2)\).

Consequently no choice of nonnegative \(u_k,\beta_k\) can make the raw
positive pair budget (20) finite while making this collection of cap-derived
lower bounds diverge. This is a statement about the specified mechanism,
not about all weighted inequalities: old-label spending, the distribution
of relation labels, actual smaller intervals, or a signed cancellation can
contain information not used in (20)–(23).

A useful boundary example is a star of old labels sharing one endpoint.
All pair differences of that star are already old labels, so its actual
remaining future budget is zero. But the star has only \(O(p)\) labels,
violates (23) for large \(p\), and cannot give the proposed positive lower
bound through (22). Thus suppressing the remaining budget and suppressing
the diagonal loss are separate requirements.

## 6. A different selection: one physical difference label as the source

To move beyond raw pair budgets, consider one fixed finite history, with
dyadic old prefixes \(P_k=A_{p_k}\), \(p_k=2^k\), and disjoint future shells

\[
 B_j=\{a_{p_j+1},\ldots,a_{2p_j}\},\qquad m_j=p_j.
\]

Take finitely many \(j\), with all endpoints within the terminal history.
Let \(L_j=a_{2p_j}-a_{p_j+1}+1\) be their actual integer interval lengths.
At each old prefix \(k\), choose \(u_k\ge0\), \(U_k>0\), and define

\[
 H_k=\max\operatorname{supp}u_k,
 \qquad K_k(t)=\sum_d u_k(d)u_k(d+t),\quad t>0.       \tag{24}
\]

For every \(k\le j\), the exact shadow inequality gives

\[
 \delta_{kj}:=
 \frac12\left(
 \frac{m_j^2U_k^2}{L_j+H_k-m_j}-m_jS_k\right)_+
 \le\sum_{t\in\Delta B_j}K_k(t).                    \tag{25}
\]

All denominators are positive. Let \(\alpha_{kj}\ge0\) be arbitrary finite
coefficients. Define an epoch kernel and its physical-label envelope by

\[
\begin{split}
 G_j(t)&=1[1\le t\le L_j-1]\,1[t\notin\Delta P_j]
               \sum_{k\le j}\alpha_{kj}K_k(t),\\
 \mu(t)&=\max_jG_j(t).
\end{split}                                                    \tag{26}
\]

The masks in (26) are exact on \(t\in\Delta B_j\): such a label lies within
the actual span and has not already been used by the prefix preceding that
shell. Since the label sets \(\Delta B_j\) are pairwise disjoint,

\[
 \boxed{\quad
 \sum_{k\le j}\alpha_{kj}\delta_{kj}
 \le\sum_j\sum_{t\in\Delta B_j}G_j(t)
 \le\sum_{t>0}\mu(t).
 \quad}                                             \tag{27}
\]

The double sum on the left ranges over all selected \((k,j)\).
Every sum is finite. Relation pairs with different births but the same
numeric label \(t\) have now been bundled before the upper bound is taken.
The maximum over possible spending shells, rather than a sum over shells,
charges one copy of the physical label. Within a single spending shell all
old-prefix contributions are summed, since that shell must actually pay
them simultaneously.

This is an unconditional global upper bound for the selected finite history.
It follows from full difference-label injectivity; it does not infer an
upper bound from feasible local owner graphs. Unlike (20), the upper bound
can exploit overlap between relation kernels of different old prefixes.
There is no reason established here for it to be uniformly bounded in the
number of prefixes.

### 6.1 Exact old/new/cross accounting for the same source

For a contiguous family of these shells and their initial prefix, partition
the positive difference labels of the terminal set into labels internal to
one selected shell, and all other used labels. The latter include the initial
prefix, old/new cross pairs, and pairs from different shells. Let this second
set be \(\mathcal C\), and let \(\mathcal U\) be the positive integers not
used as differences in the terminal set. Then

\[
 \sum_{t>0}\mu(t)
 =\sum_j\sum_{t\in\Delta B_j}\mu(t)
    +\sum_{t\in\mathcal C}\mu(t)+\sum_{t\in\mathcal U}\mu(t). \tag{28}
\]

Each shell also has a nonnegative envelope slack
\(\sum_{t\in\Delta B_j}(\mu(t)-G_j(t))\). Subtracting these terms from (28)
gives an exact identity for the middle expression in (27). Thus all old,
cross, unused, and envelope slack terms occur on the same physical source.
For a noncontiguous family, put all omitted points' used labels into
\(\mathcal C\); the same partition is valid.

Discarding these nonnegative terms yields (27). Recovering a useful lower
bound on their aggregate expenditure is a possible arithmetic improvement;
their signs alone do not provide one.

### 6.2 An explicit finite variational problem

For fixed old vectors \(u_k\), the following is a finite linear program in
\(\alpha_{kj}\) and \(\mu_t\):

\[
\begin{array}{ll}
 \text{maximize}&\displaystyle\sum_{k\le j}\alpha_{kj}\delta_{kj},\\
 \text{subject to}&\alpha_{kj}\ge0,\quad \mu_t\ge0,\\
 &\displaystyle\sum_t\mu_t\le1,\\
 &\displaystyle\mu_t\ge
  1[t\le L_j-1]\,1[t\notin\Delta P_j]
  \sum_{k\le j}\alpha_{kj}K_k(t)\quad\text{for every }j,t.
\end{array}                                                    \tag{29}
\]

Only labels \(t\) in the finite support of some \(K_k\) are necessary.
At the minimum cost the epigraph variables equal the envelope (26).
Equation (27) proves that an actual Sidon history has optimal value at most
one. Selecting the vectors \(u_k\) as well is a further variational choice;
the linearity assertion in (29) is only for fixed vectors.

Thus a prospective proof route has a concrete next obligation: use the
fixed-onset cap and the compatible growing history to construct vectors and
coefficients for which the required demand exceeds this single physical-label
capacity, or to force enough of the nonnegative expenditures in (28) that it
does. No such uniform construction or strict inequality has been proved.
A finite optimum at most one, by itself, neither proves nor refutes that
all-history obligation. No solver run is being claimed for (29).

## 7. What has and has not been gained

The initial-appearance allocation is now exact, including the separate
first-endpoint and last-endpoint times and the aging term in (8). Two actual
infinite Sidon constructions show why either permanently unused relations
or eventual actual future relations can defeat a general finite-total-charge
claim. They intentionally isolate a Sidon-only inference and do not satisfy
the critical cap.

For arbitrary nonnegative old-label weights, (20)–(23) rule out obtaining the
desired divergence by combining a finite **raw** pair budget with only the
specified coarse cap demand. They do not discard actual label-dependent
cancellation or stronger geometric information.

The physical-label envelope (27) is a different exact common-source upper
bound and has the explicit selection problem (29). Its diagonal term,
prefix masks, cross-shell terms, and possible repeated old-prefix uses have
all been accounted for. No saving beyond the constant/logarithmic barriers
has yet been established from (21). The remaining step is a mathematical
inequality about the full compatible fixed-onset history, not missing
bookkeeping and not a Lean implementation detail. Q1 is not resolved here.

## 8. Independent checks and execution scope

`/root/global_route` independently rederived (10)–(13), including the exact
birth count and the powers-of-ten classification. It also checked the
construction (14), the late-block dominance proof, future realization of the
counted labels, and the bound (18). In particular, different relations are
allowed to share the same \(t\); no false uniqueness of six-point relations
is assumed.

The same independent reviewer subsequently checked the arbitrary-weight
identity (20), the strict positivity threshold (23), the bounded sum of the
specified coarse lower bounds, and the masked physical-label envelope
(26)–(29), and reported agreement. The normalization in (29) makes the
homogeneous finite program explicit.

No enumeration, floating-point sample, or optimizer was executed for this
note. The counterexamples and bounds are proved symbolically above. There
is consequently no numerical output or unsaved verification script behind
these claims. This task wrote only this research note.

# Independent adversarial review of the direct-M Haar lift

Date: 2026-09-05. Scope: independent hand proof and exact integer checks; **no Lean claim and no Q1 resolution**.

Reviewed source: `research/c143_lift.md` as read during this run. The matrix normalization was separately compared with `ROUTE_C_DIRECT_ORDERED_B_INTERVAL_HAAR.md`, including its displayed rank-4 matrix. Only this new review file is edited by this agent.

## 1. Verdict on the stated new results

The moment identity, complete Haar-state sign classification, negative-mass bound, explicit adjacent correction, exact integrated correction cost, and uniform dyadic summability are correct under their stated hypotheses. No missing boundary-negative case was found. The restriction to actual Haar states and the cutoff T>=1/2 are essential.

The new all-rank result does not itself supply an upper source capacity. Section 4 below constructs an actual infinite Sidon sequence having summable negative mass and summable correction cost while every sufficiently large dyadic Wave mass stays uniformly positive. It refutes the stronger upper-capacity inference even with genuine Sidonicity, not merely with a numerical relaxation. The example violates the critical cap; it shows exactly that the cap must have another role beyond making the new correction summable.

## 2. Independent sign and integration derivation

Use the source notation: e+1 ordered marks, delta_i=q_i-q_(i+1), i=0,...,e-1, B_ij=-(i-j)^2/(8e^2) for |i-j|>=2 and zero otherwise, M=D^TBD. Set N(q)=4e^2 q^TMq.

Directly expanding the three moments gives

\[
(\sum i\delta_i)^2-(\sum\delta_i)(\sum i^2\delta_i)
=-\sum_{i<j}(j-i)^2\delta_i\delta_j.
\]

Adding sum delta_i delta_(i+1) removes exactly the distance-one pairs and produces N(q). This confirms both the sign and the factor 4e^2.

An actual raw Haar state is a truncation of `0,-1,+1,0` in increasing mark order. If endpoint values differ, at most two jumps remain. The only two-jump value pairs are (+1,-2) and (-2,+1). If their rank separation is d, their energy is

\[
N(q)=2d^2\,1_{d\ge2}\ge0.
\]

A single jump has zero energy. Equal nonzero endpoint values force a constant state. With both endpoints zero, one sign plateau of length l gives N=l^2 1_(l>=2). Two sign plateaus of lengths a,b give

\[
N(q)=(a-b)^2-2\,1_{a=1}-2\,1_{b=1}.
\]

Its only negative cases are (1,1), (1,2), (2,1), with N=-4,-1,-1. The two boundary cases therefore require no separate negative-loss telescope.

For a negative state, both endpoint marks lie outside the nonempty active interval (x-2T,x]. Since the active marks are internal, b_0<=x-2T and x<b_e, giving 2T<H. Two active distinct integer marks force 2T>1. For each fixed T, all negative x lie in the union of e-1 intervals [b_i,b_i+2T), whose measure is at most 2(e-1)T. Therefore

\[
\int\!\int(-q^TMq)_+\,dx\,{dT\over T^2}
\le {2(e-1)\over e^2}\int_{1/2}^{H/2}{dT\over T}
={2(e-1)\log H\over e^2}.
\]

Changing strict endpoints to closed integration bounds does not affect this integral. Integer separation is doing real work in the lower cutoff.

In a negative state ||delta||^2=6, so K=M+D^TD/(6e^2) is nonnegative on every actual Haar state. The coefficient is sharp: e=3 and the Sidon ruler (0,1,4,6) at T=2,x=9/2 give q=(0,-1,+1,0), N=-4, ||delta||^2=6.

For a gap h>=1, the raw Haar translate difference has squared L2 norm 4T, 8T-2h, and 6h on T<=h/2, h/2<=T<=h, and T>=h. Its three integrals against dT/T^2 from 1/2 to infinity are

\[
4\log h,\qquad8\log2-2,\qquad6.
\]

Hence the source's correction price

\[
R_e={4\sum_i\log h_i+e(8\log2+4)\over6e^2}
\]

is exact. The Jensen bound and equations (20)-(21) of `c143_lift.md` have the stated constants. The C143 multiplier conversion contributes the separate factor 1/2 in its physical normalization; it is correctly included in that source.

## 3. Exact checks and an important non-PSD witness

An independent Python integer check enumerated all presentations

`0^left, (-1)^a, (+1)^b, 0^right`

of length e+1 for every e=1,...,64. It checked the direct pair formula against the moment formula, the exact negative-state classification, the boundary nonnegativity, N>=-4, and 3N+2||delta||^2>=0. Result: **864,496 presentations checked, all assertions passed; 5,735 negative presentations**. These counts include duplicate presentations of the same state when a sign block has zero length. They are finite corroboration; the all-rank proof is in section 2.

Actual-state positivity cannot be used as arbitrary-vector PSD. The exact counterexample is

\[
e=3,\quad q=(3,2,1,0),\quad\delta=(1,1,1),
\quad q^TKq=-1/18.
\]

This witness was recomputed with rational arithmetic. A graph-root or Gram-carrier argument that needs PSD must retain its original hypothesis or prove a new source rule for the restricted state family.

## 4. Actual infinite Sidon countermodel to the overstrong lift

The following construction keeps every dyadic epoch almost equally spaced. It has no critical cap, but its logarithmic spans grow only quadratically in epoch index, so all new correction costs are still summable.

Start with a_0=0. At stage k>=0, put e=2^k. The existing prefix ends at a_(e-1)=b_0. Set

\[
S=b_0+1,\qquad L_e=2e^2+1,\qquad f_i=L_e i+i^2\ (0\le i\le e),
\]

and add

\[
a_{e-1+i}=b_0+Sf_i\qquad(1\le i\le e). \tag{A}
\]

This gives exactly the standard epoch block a_(e-1),...,a_(2e-1). A final translation by 1 makes the infinite set positive without changing any assertion about differences or Wave masses.

### 4.1 The union is Sidon at every stage

First, the finite ruler {f_0,...,f_e} is Sidon. A positive difference is

\[
f_j-f_i=(j-i)L_e+(j^2-i^2),\qquad 1\le j^2-i^2\le e^2<L_e.
\]

Its quotient on division by L_e determines j-i. The remainder then determines j+i, and hence the ordered pair (i,j).

Assume the old prefix is Sidon. Every old difference is less than S. A new-to-old difference has the form

\[
Sf_i+r_p,\qquad r_p=b_0-a_p\in\{0,...,S-1\}.
\]

It exceeds every old difference. Equality of two such differences determines the residue r_p, hence p, and then f_i, hence i. A new-to-new difference is divisible by S. It therefore cannot equal a new-to-old difference unless r_p=0, which means a_p=b_0; that remaining case is already a difference in the finite Sidon ruler {f_0,...,f_e}. New-to-new differences are unique for the same reason. This exhausts all pair types and proves induction. Every finite prefix is Sidon, hence so is the infinite union.

### 4.2 The new negative mass and adjacent prices are summable

Writing H_e for this epoch's span, (A) gives

\[
a_{2e-1}+1=(a_{e-1}+1)(2e^3+e^2+e+1).
\]

Since 2e^3+e^2+e+1<=5e^3 for e>=1,

\[
\log(H_{2^k})\le\log(a_{2^{k+1}-1}+1)
\le(k+1)\log5+{3k(k+1)\over2}\log2=O(k^2).
\]

Consequently both the negative-mass upper bound and R_(2^k) are O(k^2/2^k), whose infinite sums converge. Thus the countermodel satisfies every summability conclusion that was obtained from the critical cap in the new Haar argument, although the cap itself is false here.

### 4.3 Every large epoch has a fixed positive Wave mass

The gaps are h_i=S(L_e+2i+1), 0<=i<e. Their ratio max h_i/min h_i is less than 2. For any nonadjacent gap pair i<j of rank distance d=j-i>=2, let m be its middle span, and u,v its endpoint gaps. Then

\[
t={uv\over m(m+u+v)}\ge {1\over4(d^2-1)}.
\]

Using log(1+t)>=t/(1+t), its cross ratio C_ij obeys

\[
C_{ij}\ge {1\over4d^2-3}\ge{1\over4d^2}.
\]

The original weight is d^2/(4e^2), so each such pair contributes at least 1/(16e^2). There are (e-1)(e-2)/2 pairs. Hence

\[
\boxed{W_e\ge{(e-1)(e-2)\over32e^2}\ge{3\over256}
\quad(e\ge4).} \tag{B}
\]

Thus sum W_(2^k) diverges linearly, while the entire negative part and adjacent correction have finite total mass. Fejer weights do not remove this: on k<=floor((J+1)/2), omega_(k,J)>=1/4, so the Fejer sum also grows linearly in J.

The exact construction was checked through k=6: 128 marks and all 8,128 positive differences distinct. The recurrence and gap-ratio assertions also passed. This finite check only corroborates the elementary infinite induction above.

### 4.4 What this refutes, and what it leaves open

It refutes

> Sidonicity, actual-state near positivity, summable negative mass, and summable adjacent correction imply a bounded whole-tower Wave or corrected-Haar mass.

It does **not** refute an upper bound that uses the full critical cap a_n<=C n^2 log(2n) in some additional substantive way. The construction grows much faster than that cap and has Q1's zero liminf. Therefore it is not a counterexample to Q1 or to the explicitly capped target (22) in `c143_lift.md`.

The cap's role in deriving O(k/2^k), by itself, has now been isolated as insufficient: O(k^2/2^k) is just as summable. An upper-capacity proof must exploit another feature of the cap, such as quantitative span-growth control in the main long-range source identity, rather than only in the error estimate.

## 5. Remaining proof boundary

The negative-part obstacle is closed informally at every rank. Arbitrary-PSD legality and the whole-tower upper source bound remain separate obligations. The explicit sequence above is a reusable adversarial test for any proposed source bound that no longer visibly uses the critical cap after substituting a finite correction constant.

## 6. Review of the collaborator's finite capped two-epoch family

The C143 mathematics agent supplied an additional local countermodel, independently checked here. Let e=2^k>=4, choose a prime 4e<p<8e, put ell=ceil(log(8e)) and L=4p ell, and set

\[
a_i=Li+[i^2]_p\qquad(0\le i<4e),
\]

where the bracket is the residue in {0,...,p-1}. Bertrand's theorem supplies such a prime.

* **Sidonicity:** equality of two positive differences fixes the rank difference d because L>2p. Reducing the remaining equality modulo p gives 2d(i-k)=0 modulo p. Since p is odd, 0<d<p, and the starting indices lie in [0,p), this forces i=k and then the other endpoints equal. This argument avoids a possible ambiguity from using the sum of endpoints only modulo p.
* **Gap ratio:** each gap lies in (L-p,L+p), whose ratio is at most 5/3. Thus the consecutive epoch spans obey H_(2e)/(4H_e) in [3/10,5/6]. Their logarithmic ratio eta is negative and bounded independently of e.
* **Local cap:** with N_m=a_(m-1)+1, for every e<=m<=4e,

\[
N_m\le32\ell m^2+8m\le100m^2\log(2m).
\]

Here ell<=log(8m)+1<=3log(2m), and 8m<=4m^2 log(2m) for m>=4.
* **Wave floor:** log(1+t)>=t/(1+t) gives C_ij>=uv/[(M+u)(M+v)]>=uv/(M+u+v)^2. The gap ratio yields C_ij>=(3/5)^2/(d+1)^2, and d^2/(d+1)^2>=4/9 for d>=2. Every weighted edge contributes at least 1/(25e^2), so W_e>=(e-1)(e-2)/(50e^2)>=3/400.

Consequently no uniform estimate on this local class can have the form

\[
W_{2^k}\le{A\eta_k+V_{k+1}-V_k\over k+1}+\varepsilon_k,
\qquad |V_k|\le B,\quad\varepsilon_k\longrightarrow0,
\]

with fixed finite A,B: its right side tends to zero while the left side stays at least 3/400. This supports the collaborator's local no-go. The onset m_0=e moves with k; the family therefore does not refute a fixed-onset whole-tower bound or Q1.

## 7. Review of the full-distance moment correction

The collaborator's alternative uses Btilde_ij=-(i-j)^2/(8e^2), including adjacent entries. Its moment formula and the pointwise domination

\[
q^T\widetilde Mq\ge\max(q^TMq,0)
\]

are correct on actual Haar states. Every nonzero adjacent product of jumps is negative. Removing the adjacency correction from the moment formula therefore increases the energy. Its value is a square when endpoint values agree, and a nonnegative two-jump interaction when they differ.

The exact price on T>=1/2 is

\[
A_e={1\over2e^2}\sum_{i=0}^{e-2}
\left[\log{h_i h_{i+1}\over h_i+h_{i+1}}+2\log2+1\right].
\]

Independent polarization confirms it: the adjacent jump-product integral equals one half the long-gap square integral minus both short-gap square integrals, hence

\[
\int_{1/2}^{\infty}\!\int\delta_i\delta_{i+1}\,dx\,{dT\over T^2}
=2\log{h_i+h_{i+1}\over h_i h_{i+1}}-4\log2-2.
\]

The displayed upper bound A_e<=(e-1)/(2e^2)[log(2H/(e-1))+1] is also correct.

**Essential cutoff clarification.** For 0<T<1/2, at most one integer mark is active. An isolated internal mark contributes q^TMtilde q=1/(4e^2), whereas an isolated endpoint contributes zero. Its x-support has length 2T. Thus

\[
\int_{\mathbb R}q^T\widetilde Mq\,dx
={e-1\over2e^2}T\qquad(0<T<1/2).
\]

For e>=2, the integral of the uncut carrier from T=0 diverges logarithmically. The valid identity is exactly

\[
\int_{1/2}^{\infty}\!\int q^T\widetilde Mq\,dx\,{dT\over T^2}
=2W_e+A_e.
\]

Equivalently, one may integrate the carrier with its indicator 1_(T>=1/2) over all positive widths. The source's current equation (28) uses the correct restricted range. Any later use of an unqualified full-width identity needs this indicator.

## 8. New stronger result: a universal finite-cost transition correction

The logarithmic negative-mass bound can be sharpened without a critical cap and without integer spacing. Let b_0<...<b_e be any strictly increasing **real** ruler, e>=3. Define the nonnegative local transition indicator

\[
I_r(x,T)=1_{\{q_r(x,T)=-1,\ q_{r+1}(x,T)=+1\}}
\quad(1\le r\le e-2).
\]

Every negative state from section 2 has a unique such transition, at the cut between its negative and positive plateaus. Its magnitude is at most 1/e^2. Therefore pointwise

\[
(-q^TMq)_+\le {1\over e^2}\sum_{r=1}^{e-2}I_r. \tag{C}
\]

For two marks at distance h>0, the x-measure of their opposite-sign overlap is exactly

\[
\int I_r(x,T)\,dx=
\begin{cases}
0,&T\le h/2,\\
2T-h,&h/2\le T\le h,\\
h,&T\ge h.
\end{cases}
\]

Indeed the intersection in x is [b_r+T,b_r+2T) intersected with [b_(r+1),b_(r+1)+T). Its exact full-width integral is

\[
\int_0^\infty\!\int I_r(x,T)\,dx\,{dT\over T^2}
=(2\log2-1)+1=2\log2. \tag{D}
\]

This identity is independent of h and includes the entire upper tail. From (C)-(D),

\[
\boxed{\nu_e\le{2\log2\,(e-2)\over e^2}.} \tag{E}
\]

In particular the negative part is O(1/e), not merely O(log H/e). On dyadic epochs it is summable for **every** infinite real ruler, independently of all span growth. This is a new elementary strengthening derived during the independent review.

It also gives an exact nonnegative scalar carrier:

\[
\mathcal C_e(x,T)=q^TMq+{1\over e^2}\sum_{r=1}^{e-2}I_r(x,T)\ge0,
\]

with the full-width identity

\[
\boxed{\int_0^\infty\!\int\mathcal C_e\,dx\,{dT\over T^2}
=2W_e+{2\log2\,(e-2)\over e^2}.} \tag{F}
\]

No lower cutoff is required. Unlike Mtilde, the correction vanishes on a state with only one active mark. For a fixed finite real ruler, direct-M itself vanishes for sufficiently small widths and has compact width support after spatial integration; the transition integrals are explicitly finite by (D). Thus the identity does not hide an interchange of divergent terms.

For k>=k_0>=2 and any weights in [0,1], the entire additional price is at most

\[
2\log2\sum_{k\ge k_0}(2^{-k}-2\cdot4^{-k})
=2\log2\left(2^{1-k_0}-{8\over3}4^{-k_0}\right).
\]

This correction is nonlinear in the state. It is a particular physical adjacent-pair indicator, not an arbitrary PSD matrix or an established C143 graph-root owner rule. Its source positions and total scalar price are explicit, but its use inside a different global identity still needs proof.

## 9. Pointwise localization across dyadic epochs

The collaborator's latest localization claim is also correct. In the full increasing sequence, a fixed raw Haar state has at most three nonzero jumps. Dyadic gap blocks [e-1,2e-2], e=2^k, are pairwise disjoint. Both B and Btilde have zero diagonal, so an epoch with fewer than two nonzero jumps has zero quadratic energy. At most one of these disjoint blocks can contain two of the at most three jumps. Hence at a fixed (x,T), at most one direct-M epoch and at most one full-distance epoch have nonzero energy.

The state formulas give 0<=q^TMtilde q<=1/2: a two-jump interaction has magnitude at most 2(e-1)^2/(4e^2), and the three-jump square is at most (e-1)^2/(4e^2). Thus

\[
\sum_k\omega_{k,J}q_{2^k}^T\widetilde M_{2^k}q_{2^k}\le1/2
\]

pointwise for weights in [0,1]. A finite or infinite sum is harmless pointwise because at most one term is nonzero. This does not give an integral upper bound against dx dT/T^2: that measure has infinite volume, and the uncut small-width divergence is already explicit in section 7. A successful integrated source bound must use more than this pointwise ceiling.

## 10. Further rank-gap investigation and preserved executable checks

The stronger universal correction (E)-(F), rather than just an obstruction, is the additional inequality obtained during the second review. A separate investigation asked whether ordering the distinct gaps could turn the critical span cap into a stronger Wave lower bound and then an upper-storage contradiction. The proposed monotone rearrangement shortcut is false even for finite Sidon rulers:

\[
W(1,4,16,8,2)<W(1,2,4,8,16).
\]

Both gap lists give Sidon prefix rulers. The comparison was verified exactly by exponentiating 4e^2 W: the resulting cross-ratio products are rational, and their strict inequality is an exact integer comparison. Thus ascending gap order need not minimize W; a proof using that assertion cannot proceed.

An alternative hierarchical critical-growth candidate used distinct gaps g_n=n*2^(v_2(n)) and B_n=sum_(j<=n)g_j. The gaps are all distinct because their 2-adic valuations are 2v_2(n). Its recurrence B_(2n)=4B_n+n^2 gives B_(2^k)=(1+k/4)4^k, at precisely the n^2 log n scale. However it is not Sidon, and even adding any fixed real multiple lambda*n^2 fails: the exact identities

\[
B_{104}-B_{76}=B_{117}-B_{93}=9512,
\qquad104^2-76^2=117^2-93^2=5040
\]

leave a collision for every lambda. The values are B_76=12232, B_93=16357, B_104=21744, B_117=25869. This rejects that construction family, not Q1.

The actual executed exact code has been preserved in `research/moment_independent_review_checks.py`. Its three sections reproduce the state enumeration, the finite corroboration of the infinite Sidon example, and these two exact falsifications. It was saved after the observed runs, without rerunning unchanged checks merely to archive them. The universal transition-integral theorem is a hand proof in section 8, not falsely counted as a Python or Lean verification.

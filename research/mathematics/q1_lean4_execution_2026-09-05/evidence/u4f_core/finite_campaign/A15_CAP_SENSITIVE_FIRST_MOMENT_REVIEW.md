# Independent review of A15: a cap-sensitive nonlinear AC/BH bound

2026-09-09. Verdict: PASS as an all-history hand proof, retaining both
genuine horizons. No claim that the whole statement has been Lean
verified. The source excerpts and hashes reviewed here are recorded in
`A13_A15_review_source_manifest.json`.

Let P=Q_AC(b) and Q=Q_BH(b), b>=5. Both channels must use the SAME
collection of old quadruples, e.g. all old quadruples or the all-large-gap
subclass. For every such quadruple keep the original gates, with the
automatic implication G_minus,q<=G_minus,s. Selecting individual matching
records independently could break this implication and is not covered.

## Integer-fiber capacity

Fix a positive integer middle difference B. Actual Sidon uniqueness
determines at most one middle pair q<s. At a covered cut the remaining
endpoints have p<q<s<c<b, so there are exactly at most
(q-1)(b-1-s) possibilities before other restrictions. Since the sum of
these two factors is b-2-(s-q)<=b-3, their product is <=b^2/4.

For each quadruple, AC<=Hquad^2/4 and every contributing component k>=r
has H_k>=Hquad. Thus a single AC term has mass

    AC*u_r^[M] <= (alpha_r-alpha_(M+1))/4 <=alpha_r/4.

The first inequality is an upper comparison only; no terminal price is
changed. Coverage c<b<i<r gives r>=b+2 and hence alpha_r<=b^-4.
There are at most two minus AC terms per quadruple. Therefore the
fiber mass satisfies 0<=mu_B<=D=1/(8b^2), and sum_B mu_B=P. The
integer B labels are unique middle gaps, not freely replicated budgets.

## First moment and the BH charge

With L=sum_(B>=1)B*mu_B, finite support and the capacity imply

    P^2 = sum_B mu_B^2+2 sum_B mu_B sum_(A<B)mu_A
        <= D*P+2D sum_B (B-1)mu_B
        = D(2L-P).

The diagonal uses mu_B^2<=D*mu_B; there are only B-1 positive integer
labels below B, even if many are absent. This confirms the sign of the
linear term: it is 2L-P, not 2L+P. No asymptotic or integral surrogate
is needed.

For a single quadruple let mu_h=AC(G_minus,q+G_minus,s) and
nu_h=BHquad(G_minus,s+G_plus,s). Its actual common gates give
mu_h<=2AC G_minus,s and nu_h>=BHquad G_minus,s. Because
4AC<=Hquad^2<=H_b*Hquad,

    H_b*nu_h >= B*H_b*Hquad*G_minus,s
              >=4B*AC*G_minus,s >=2B*mu_h.

Summing over the same quadruples yields H_b Q>=2L. Combining gives

    8b^2 P^2+P <= H_b Q.

All quantities are those of the actual profile, with the actual numeric
middle B and actual chronological output prices. The proof never
orders prices by numerical t, and works unchanged at T<=M. If the
original cap holds at b>=m0, then H_b<=Ccap*b^2*log(2b) implies

    P^2 <= (Ccap/8)*log(2b)*Q.

It does not require a cap at a source birth below m0. The finitely many
cuts below max(5,m0) have their original universal pointwise cost.

## Actual dyadic consequence and unresolved part

On the actual cut block 2^j<=b<min(2^(j+1),M), restricting to b>=m0,
weighted Cauchy gives

    I_AC^2 <= D_j*I_BH,
    D_j=(Ccap/8)sum_b log(2b)/b
        <=(Ccap/8)(j+2)log(2)*W_j.

Subadditivity of square roots and blockwise Cauchy then give the actual
block norm at most

    sqrt(W_j)*(sqrt(I_BH)+D_j^(1/4)*I_BH^(1/4)).

The hypothetical estimate I_BH<=A(C,m0)/(1+j)^(5+eta), eta>0, would
make the second term O(j^(-1-eta/4)) and hence suffice. It remains
UNPROVED. A bound on sum I_BH or on sum sqrt(I_BH) does not establish
this stronger fourth-root summability. A13 shows the cap cannot simply
be dropped; the fixed C=1000000 M12 witness shows that a linear
constant-one comparison cannot substitute for the nonlinear argument.

No extra finite history, evaluator, campaign or toolchain change was
needed for this review. The finite-cap witness does not contradict this
bound: the H_b factor and the positive quadratic term are essential to
the comparison's form. The unresolved mathematical task is still a
cap-sensitive bound on the BH series sufficient for these actual block
costs, or another direct whole-profile route. U4-F and Q1 remain open.

## Supporting Lean scope added after the mathematical review

The parent then completed the generic finite integer-mass lemma
`Erdos1191Q1.U4FProfile.bounded_integer_mass_first_moment`. I read the
existing `../LEAN_VERIFICATION_03.json` and its theorem-type/axiom log,
and independently matched all seven recorded source/toolchain/log hashes.
The pinned local compile and audit both exited 0; the evidence lists 15
supporting declarations total. The new lemma uses only `propext`,
`Classical.choice`, and `Quot.sound`, with no custom axiom. This readback
is saved in `A15_existing_Lean_evidence_readback.json`; no compile was
rerun by this worker. The actual Sidon fiber capacity, gate/geometry
instantiation, full A15 estimate, BH bound and literal Q1 are still outside
this supporting Lean result.

## Final source binding

Final `research/u4f_core/WORKING_PROOF.md` SHA-256:
`5545ad8821bbaa0a5f24a4a74a3b3143537f98b42b8f71a84a87364edb8c8c4c`.

A15 section SHA-256:
`d05c6d46b224a1937887038ab38462662a03245074910b50fb2db4ad5953e9a8`.

The changes from the first reviewed section only update review/Lean
status; the mathematical contents are unchanged. Both versions are
retained in `A13_A15_review_source_manifest.json`.

# A51: fixed source-birth prices and the exact moving-price correction

Date: 2026-09-09. Independent hand-proof review: PASS.
No new finite search or Lean run.

Fix the actual larger source d with upper source rank y, one fixed bin of
smaller actual old labels e<d, and an output cutoff v<=T<=M. For each
label let c_e=max(y,z_e), w_e=de, and

    omega_e=w_e*u_(c_e+2)^[M].

This is a source-birth auxiliary budget. It is not the output price of
an unused label. Only terms with c_e<b in an available cut are used, so
c_e+2<=b+1<=M in the profile domain. A source with no available cut is
irrelevant. The original selected record subset here has r<=v and fixed
original strict gates; it is not an arbitrary cut/component-dependent
selector. Set

    Bstar_b=sum_{c_e<b} omega_e,
    P_b=sum_valid w_e*u_r^[M] * 1[c_e<b<i],
    Dstar_b=Bstar_b-P_b.

One actual source pair (d,e) determines at most one physical output pair.
For a valid original record r>=c_e+2, so u_r<=u_(c_e+2). At a source
birth, the increment of Dstar is omega_e minus the price of the record
if it immediately becomes active; this is nonnegative. At retirement
the original active price is added back. There is no later activation
for this fixed original record subset other than source birth. Thus
Dstar is nonnegative and nondecreasing, including unused/invalid labels.

Let B_b=sum_{c_e<b} w_e, Bmoving_b=B_b*u_(b+1)^[M], and
C_b=Bstar_b-Bmoving_b. At the first possible cut b0=y+1, every existing
bank label has c_e=y, so C_b0=0. New labels at the step b->b+1 have
c_e=b and the same auxiliary price u_(b+2). Hence, exactly,

    C_(b+1)-C_b=lambda_(b+1)*B_b,
    Dstar_b=(Bmoving_b-P_b)+C_b.

This explains the A50 moving-price counterexample: at an unchanged-bank,
unchanged-P step, Bmoving-P decreases by lambda_(b+1)B_b, while C gains
exactly that amount. No alpha_(M+1) is reset. A selector admitting old
records later would need its own activation treatment; this argument
does not transfer to it automatically.

For all actual old ordered source pairs d>e, define
F_n=sum_{d>e in D_n}de, with F_0=F_1=0. The source-birth layer has
weight F_c-F_(c-1). Finite Abel summation yields

    Bstar_b=u_(b+1)^[M] F_(b-1)
             +sum_{c=2}^{b-2} lambda_(c+2) F_c.

The c=2 term is harmless (F_2=0). For b>=3, A42's actual endpoint
bound F_c<=c^4 H_c^2/32 and width monotonicity give

    u_(b+1)F_(b-1)<1/32,
    lambda_s F_(s-2)<=1/(8s),  s>=4,
    Bstar_b<1/32+(1/8)sum_{s=4}^{b}1/s.

For the first inequality, use
(b-1)^4/[32b^2(b+1)^2]<1/32. For the second, use
kappa_s=4/[s(s^2-1)^2] and (s-2)^4<=(s^2-1)^2.
The Abel index substitution is s=c+2, hence upper endpoint s=b.
The empty b=2 bank is treated separately. All sums are finite within
the original history and use the original genuine coefficients.

This is a valid monotone auxiliary potential with only a logarithmic
bank bound. It does not establish the uniform square-root harmonic norm,
CoreUniform, or Q1. Exact finite A50 prices are illustrative evidence
for the need for compensation, not assumptions in this proof. The next
question is whether a smaller compatible bank can pay the actual norm;
the current independent source-pair budgets do not do so.

Source/review hashes are in `A51_A54_review_manifest.json`. Full
formalization is not claimed by this hand-review note.

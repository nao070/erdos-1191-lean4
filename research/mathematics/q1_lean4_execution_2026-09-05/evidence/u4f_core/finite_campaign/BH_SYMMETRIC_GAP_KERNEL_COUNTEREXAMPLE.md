# The actual BH gap kernel need not be positive semidefinite

2026-09-09. Exact arithmetic on the already-certified A14 history only.
No new history or campaign was generated. This refutes two proposed
kernel inequalities, not U4-F or Q1.

At a fixed cut define adjacent point gaps g_l=a_(l+1)-a_l and, for each
old quadruple h=(p,q,s,c), indicators

    x_h(l)=1[q<=l<s],  y_h(l)=1[p<=l<c],
    w_h=G_minus,s+G_plus,s.

Here w_h includes the actual strict gates, the genuine component price,
and the cut coverage. Since g dot x_h=B and g dot y_h=Hquad,

    Q_BH = sum_h w_h*(g dot x_h)*(g dot y_h) = g^T K g,
    K_lm = sum_h w_h*(x_h(l)y_h(m)+y_h(l)x_h(m))/2.

The matrix is symmetric and entrywise nonnegative. Those properties do
not imply positive semidefiniteness, as this actual instance shows.

## Certified instance and its one BH price

Use the saved C=1000000, m0=2, M=T=12 prefix

    (1,14512,30001,30629,31694,32001,
     63361,67001,71675,84375,100001,105001).

The exact record bank has two strict six-endpoint records, both from
quadruple (p,q,s,c)=(1,3,6,8) and output (i,r)=(11,12), t=5000.
Their source labels are {35000,30000} and {37000,32000}; the former
contributes AC and the latter AC+BH. There is no plus core record.
Thus at either covered cut b=9 or b=10 the BH kernel has ONE weight

    w=u_12^[12]=(alpha_12-alpha_13)/105000^2
               =1/676350675000000.

In particular the other minus matching does not double the BH weight.
The frozen terminal price, strict core and actual cut are unchanged.
The previous independent certificate is bound by its exact input and
checker hashes; both saved records' endpoints and strict inequalities
were also rechecked by the existing independent checker routines.

Now x=1[3..5], y=1[1..7], with all remaining entries through l=11 zero.
For the principal indices l=1 and l=3, the exact matrix is

    [[0,   w/2],
     [w/2, w  ]].

Its determinant is -w^2/4<0. Explicitly,

    K_11=0,
    K_13=1/1352701350000000,
    K_33=1/676350675000000.

The integer vector z=2e_1-e_3 gives

    z^T K z=-w=-1/676350675000000<0.

Hence K is not PSD. The diagonal-Schwarz candidate fails as well:
K_13^2>0=K_11*K_33, equivalently
|K_13|>sqrt(K_11*K_33). This is the complete kernel of the instance,
not a subkernel whose negative direction could be repaired by omitted
positive terms: there is exactly one contributing BH quadruple.

## Agreement with the actual positive gaps

The actual adjacent gap vector is

    g=(14511,15489,628,1065,307,31360,3640,
       4674,12700,15626,5000).

Every entry is positive, and direct exact sums give

    g dot x=628+1065+307=2000=B,
    g dot y=67000=Hquad,
    g^T K g=134000000*w=134/676350675=Q_BH>0.

Direct 11-by-11 matrix multiplication independently agrees with the
BH product. Adding the two AC pieces recovers each saved full profile
coefficient at cuts 9 and 10. Outside those cuts this instance's kernel
and profile are zero. The negative test vector z is not the actual gap
vector and has a negative coordinate; no negative actual BH mass is
claimed. Indeed any entrywise nonnegative K is nonnegative on every
nonnegative vector. What fails is the PSD/diagonal-Schwarz structure
needed for that particular proposed charging argument.

## Evidence and next action

`kernel_from_A14_exact.py` is the narrow reproducible arithmetic check;
it reads only the existing certified fixture and checker routines.
`C1000000_m02_M12_target/BH_symmetric_gap_kernel_exact.json` stores
all exact 121 matrix entries, the actual and test vectors, direct
quadratic forms, original source hashes and local certificate hashes.
No Lean verification is claimed for this counterexample.

The valid bilinear identity with its two distinct interval indicators
remains available. A subsequent estimate must retain that distinction,
use the positive actual gaps and fixed cap, or prove a different positive
operator domination. This example rules out treating K itself as a PSD
Gram kernel merely from its symmetry or nonnegative entries.

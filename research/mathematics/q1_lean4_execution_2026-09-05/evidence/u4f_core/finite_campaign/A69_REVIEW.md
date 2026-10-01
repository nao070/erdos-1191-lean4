# A69: independent allowance comparison review

Date: 2026-09-09. Status: PASS.

The actual source-birth setting has c>=4, n=c-1, and the sufficient
regime additionally assumes m>=n and c>=m0. The latter condition is
explicit in the integrated section; no cap below m0 is used.

Each actual old pair appears exactly once in sum_l O_l, so U=sum_l O_l.
For 1<=l<m-1,

    F_l-F_(l+1)=(m-l)*(f_(l+1)-f_l)>0.

Thus F_(n-1)>=G implies Phi>=G*sum_l O_l=UG. This compares two
actual upper allowances; it does not bound actual record mass from
below. A68 only bounds the positive boundary part by Phi, so adding
the nonnegative g-square part cannot improve this comparison with
the direct whole-record source bank UG.

For d=m-n+1>=1, the actual s+1 consecutive future points starting at
position n-1 have binom(s+1,2) distinct positive integer differences.
Their span is therefore at least s(s+1)/2. Summing for 1<=s<=d gives
F_(n-1)>=d(d+1)(d+2)/6. Combining with the cap at the existing rank c,
G<=n H_c<=n C c^2 log(2c), proves the displayed sufficient condition.
No assumption that a prefix can be extended is used. For k>T, m stays
min(k,T)-b and does not grow with k.

I inspected A69_tail_allowance_check.py and its saved certificate.
Both orientation assignments into the common right vertices, coordinate
matching checks, diagonal-tail identity and coefficient are consistent
with A68. Separately, direct arithmetic on only the already fixed old
first23 values and future26..48 values gives

    n=m=23, U=58548, G=11745, UG=687646260,
    Phi=1181503640, Phi-UG=493857380,
    F22=209<G.

This agrees with the certificate. The actual sufficient condition fails
here, but the actual numerical upper allowance still exceeds UG. The
finite actual Beta is 8716524 and the residual product mass is 21922039;
neither is identified with an allowance. The genuine coefficient is the
same lambda48=1/1148518878296832, not any original full u_r.

Only the existing point tails were checked; no history, core record
enumeration, profile, or Lean build was performed. The full core norm
and Q1 remain unresolved.

Checked source hashes:

- A69_tail_allowance_check.py:
  26ed169a7d6fe4298625e6d341a8cade3c4c8582c3fc6e14fe7afe612188a490
- A69_TAIL_ALLOWANCE_EXACT.json:
  2339b33eeee5b78de687cd97a87509749ed17f719829b6e2fd95aeb12ff82b64
- C1_m02_dense_variant1_M96.json:
  d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e

Every source_sha256 entry in the certificate matched its file.

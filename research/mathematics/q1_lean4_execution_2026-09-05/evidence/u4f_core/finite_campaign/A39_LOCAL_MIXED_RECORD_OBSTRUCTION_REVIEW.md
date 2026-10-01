# A39 independent review: an output-local mixed charge is absent

Date: 2026-09-09. Status: PASS exact counterexample to the specified
record-local eligibility claim. Only one prescribed existing record
was extracted; no other record or new history was searched.

The existing C=1,m0=2 variant M=T=96 A24 witness has, at
weighted_counterexample_despite_count_decrease.complete_birth_records[2],
the old quadruple (1,6,20,24), matching type 3, output (i,r)=(42,43),
and original row

    [713,422,1,24,6,20,24,20,42,43,291].

Thus d=a_24-a_1=713, e=a_20-a_6=422, t=d-e=291=a_43-a_42.
The six endpoint ranks are distinct. The actual values are
a_1=1, a_6=19, a_20=441, a_24=714, a_25=774,
a_42=2975, a_43=3266 and a_48=4249.

The original strict gates were checked on this single saved row
using the existing rational-log and independent fixed-point helpers.
All five certified lower margins are positive: s log(c)^2-c,
(i-c)log(c)^2-c, (r-i)log(r)^3-r, c log(c)-r,
and t log(c)^3-c^2, with source births (c,s)=(24,20).
Their exact interval endpoints are saved in the evidence JSON.
Its original inclusive cut interval is [25,41], and r=43<=k=48.
The full-history Sidon/cap certificate is reused with its input hash.

At the specified cut b=25,

    H_b=773, H_i=2974>=2H_b=1546.

All eight actual differences from the four old endpoints to these
two output endpoints are as follows.

| old rank | label to i=42 | label to r=43 |
|---:|---:|---:|
|1|2974|3265|
|6|2956|3247|
|20|2534|2825|
|24|2261|2552|

Every label exceeds H_b. Consequently the eligible set in (0,H_b)
is empty and its total kernel mass is exactly zero, for threshold 1
as well as the stricter original threshold. On the other hand the
record's product and genuine component mass are positive:

    de=300886,
    kappa_48/H_48^2=1/1148518878296832,
    de*kappa_48/H_48^2=150443/574259439148416.

For the oriented larger source pair (x,y)=(1,24), the identity proposed
for further use is also exact:

    U=a_r-a_y=2552, V=a_i-a_x=2974, V-U=422=e.

The candidate that every original core record has an eligible mixed
label joining its own output endpoints to its own old endpoints is
therefore false. This statement is narrower than the claim that the
complete mixed bank has no payment: labels involving other past or
future endpoints remain available globally. It also does not refute
any valid nonlocal charging estimate, frozen U4-F, or Q1.

A39_one_record_local_mixed_obstruction.py extracts exactly the named
entry and saves the endpoint arithmetic, strict intervals, price,
local zero mass and source hashes. The original row, its evidence,
and both existing strict-condition helpers remain unchanged.

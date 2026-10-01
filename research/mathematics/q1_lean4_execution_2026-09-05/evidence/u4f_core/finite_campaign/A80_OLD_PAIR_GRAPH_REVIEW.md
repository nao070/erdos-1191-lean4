# A80 bounded old-pair graph review

Status: PASS for exact reconstruction of the nine prescribed cells. The proposed bounds `degree <= n` and `degree <= m` have actual finite counterexamples; `degree <= 2m` has no counterexample in these nine cells only.

The input is the existing certified `C1_m02_dense_variant1_M96` history, with C=1, m0=2, M=T=96. The only cells are b in {24,25,26} and k in {47,48,49}. No new history, campaign, whole profile, whole-horizon evaluation, or later residual-selector scan was performed.

## Graph and independent checks

Vertices are all old rank pairs U=(u,v), 1<=u<v<b, with length L_U=a_v-a_u and sum s_U=a_u+a_v. An unordered edge U,V is present exactly when the two intervals overlap and `abs(s_U-s_V)` is an actual positive difference with unique future endpoints `b<i<r<=k`. All encountered adjacent-pair supports are disjoint by the actual Sidon input. The integer kernel is

`K = (max((L_U+L_V)^2-t^2,0)+max((L_U-L_V)^2-t^2,0))/4`.

Each positive edge is counted once. A nested edge has two distinct source records, whose products are added to K; an interlaced edge has one. Separated old intervals contribute no edge. Thus graph degree does not count the two nested source channels twice.

The saved checker uses two enumeration directions: old-pair sums followed by future-difference lookup, and old quadruples followed by their three source matchings and actual output lookup. Every reconstructed record and graph mapping agrees. For a record `[d,e,x,y,w,z,c,s,i,r,t]`, its edge is the unordered pair of old pairs `{(y,w),(x,z)}`, with each internal pair sorted. The two future endpoints and all six physical endpoints are preserved.

At b25,k48, every positive edge, kernel, output pair and individual source product agrees exactly with the existing A78 evidence. Original strict gates are evaluated separately by both existing rational logarithm interval methods. The nine cells contain 5,014 distinct candidate source records; the two methods agree and produce UNKNOWN=0. No A46 or subsequent paid/remainder selector is applied here.

## Exact results

Here Q is the unfiltered sum of source products, D is `sum_U L_U^2 degree(U)/2`, and Q_core is the sum of just the individually strict-core channels. All three are unpriced integers or rationals.

| b | k | edges | Q | D | maximum degree | Q_core |
|---:|---:|---:|---:|---:|---:|---:|
|24|47|2369|184851268|267231193|37|179039739|
|24|48|2450|191415191|277277114|38|185480132|
|24|49|2489|193630261|564491093/2|39|187695202|
|25|47|2651|249075928|712569561/2|35|241829853|
|25|48|2746|257942228|739148279/2|36|250572623|
|25|49|2799|261873758|377875420|37|254504153|
|26|47|2911|326889611|928081077/2|39|317286957|
|26|48|3022|338928884|481697494|40|329202700|
|26|49|3092|345649139|494702183|42|335922955|

The checker verifies `2K <= L_U^2+L_V^2` for every edge and the exact diagonal identity by summing both edge endpoints. Removing the separated K=0 pairs before taking degree explains why the b25,k48 value D=739148279/2 is below the earlier complete-fiber length allowance 430102496. They are different allowances, not inconsistent evaluations of the same sum.

At b25,k48 there are 3,993 source records. Of these 3,686 satisfy the original strict core, leaving 2,554 edges with at least one strict channel. The strict-channel mass is 250572623; its edge-diagonal allowance is 359387761. A partially surviving nested edge retains only its passing channel in Q_core.

## Actual degree counterexample

At b25,k48, U=(4,20) corresponds to the physical interval [9,441], with L_U=432 and s_U=450. Its degree is 36, exceeding n=24 and m=23. Its strict-core edge degree is 35, still exceeding both candidate bounds. The one neighbor whose entire edge is removed by the strict gates is (15,24), with future endpoints (26,31).

`A80_DEGREE_WITNESS_CHECK.json` lists all 36 neighbors, actual future pairs, source records, products and strict flags. It independently reconstructs the same neighborhood by taking each actual future difference t, querying the unique old-pair sums 450-t and 450+t, and checking overlap. All positive differences, old sums, six-endpoint exclusions, record products and output endpoints agree. Its incident unfiltered kernel sum is 3899607, and its incident strict-core product sum is 3752967.

The full JSON also preserves the lexicographically first violating vertex for each n or m candidate in every prescribed cell, with every incident edge index. None of the nine cells has a vertex of degree greater than 2m. This is bounded absence, not a theorem asserting that bound.

## Adjacent cut and component comparisons

At fixed k48, the b24->25 transition adds 456 edges of total K=79882548 and removes 160 edges of total K=13355511, giving delta Q=66527037. The b25->26 transition adds 477 edges of total K=100341886 and removes 201 edges of total K=19355230, giving delta Q=80986656.

At fixed b25, k47->48 adds 95 edges with mass 8866300; k48->49 adds 53 with mass 3931530. No edge is removed in either component transition. All twelve adjacent comparisons across the prescribed grid are stored with exact added/removed edge identities and masses. The checker confirms that cut-added edges contain the newly old rank b, cut-removed edges have lower output i=b+1, and component-added edges have upper output r=k+1. These are finite identity checks; no global analytic flux bound is inferred.

Every cell stores its unchanged genuine component coefficient `lambda_k=4/[k(k^2-1)^2 H_k^2]`. In particular lambda48=1/1148518878296832. Multiplying Q or Q_core by this coefficient gives that single component's mass, not the whole original profile or the full record price u_r^[96]. No original u_r, terminal alpha97, horizon, or coverage interval is replaced.

## Evidence binding

- `A80_OLD_PAIR_GRAPH_CHECKER.py`: `26364f324901fe7bd522e99284879acef7dfafbd5e2c600d56a9cb5c728366ac`.
- `A80_OLD_PAIR_GRAPH_EXACT.json`: `2b72021e6f89ee98251fdd797b876dab7548f2bf580d12074228e5a37e3d5ec2`.
- `A80_DEGREE_WITNESS_CHECK.json`: `e990caf4d1adc5a811803b87b9671264540a8e2ad1d8f7ce4a89238b45ac0836`.
- Existing history: `d2b47d3902725a6d2a7f9283f9ade3bfa9c02cbe9c899d0ce08fe8bc0adbbb3e`.
- Existing A78 kernel evidence: `4ba427024fa1c2431a793e7d46be9ee3b1fde556ccea4fe5cb48edcd07755e9a`.
- Existing A78 independent check: `b8831ee9a770c2087c32115c158384f62fb0a43fc79ac4713c9296a237e36e01`.

The saved original source hashes and cap certificates were preserved; all-rank cap inequalities were read back against the unchanged sequence. The original positive-difference uniqueness was also checked directly. The source JSON additionally binds both logarithm helpers. Root proof, ledger, Lean, historical evidence and original source files were not edited. There is no uniform-K or Q1 conclusion, and this task leaves no running process.

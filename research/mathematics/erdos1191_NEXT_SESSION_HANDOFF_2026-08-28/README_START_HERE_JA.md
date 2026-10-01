# Erdős Problem #1191 次セッション用引き継ぎ

このZIPは、2026年8月29日時点の endpoint-variance / rank-variance /
triangular Abel repayment / cross-ratio absorption / certified rank slack /
nonnegative sharp remainder / inner-birth saturation / P28 full-row ownership /
adaptive cap / arbitrary transport / mixed right-greedy gain
継続研究を、重複・キャッシュ・壊れた内部manifestを除いて整理したものです。

## 新しいセッションでの使い方

1. ZIPを添付する。
2. `NEW_SESSION_LAUNCH_MESSAGE.txt` の全文を貼り付ける。
3. 研究モデルには、最初に `00_START_HERE_PROMPT.txt` を読むよう指示する。
4. ZIP内の `core_workspace/` を現在の正準研究状態として継続させる。

## 最初に読む順番

1. `00_START_HERE_PROMPT.txt`
2. `HANDOFF_MANIFEST.md`
3. `core_workspace/1191_MASTER_STATUS.md`
4. `core_workspace/CONTINUATION_2026-08-29_WAVE19_CROSS_RATIO_AND_SPARSE_SPIKE.md`
5. `core_workspace/endpoint_variance/WAVE19_CROSS_RATIO_HALF_ABSORPTION_2026-08-29.md`
6. `core_workspace/endpoint_variance/WAVE19_CERTIFIED_RANK_SLACK_REMAINDER_2026-08-29.md`
7. `core_workspace/endpoint_variance/WAVE19_SHARP_BULK_REMAINDER_AND_PAIR_SUMMABILITY_2026-08-29.md`
8. `core_workspace/endpoint_variance/WAVE19_NONNEGATIVE_SHARP_REMAINDER_DECOMPOSITION_2026-08-29.md`
9. `core_workspace/endpoint_variance/WAVE19_INNER_BIRTH_SATURATION_NO_GO_2026-08-29.md`
10. `core_workspace/endpoint_variance/WAVE19_P28_FULL_ROW_OWNERSHIP_AUDIT_2026-08-29.md`
11. `core_workspace/endpoint_variance/WAVE19_P28_ADAPTIVE_ROW_CAP_CANDIDATE_2026-08-29.md`
12. `core_workspace/endpoint_variance/WAVE19_P28_ARBITRARY_TRANSPORT_RESIDUAL_FLOOR_2026-08-29.md`
13. `core_workspace/endpoint_variance/WAVE19_P28_MIXED_RIGHT_GREEDY_ENDPOINT_GAIN_2026-08-29.md`
14. `core_workspace/endpoint_variance/WAVE19_SPARSE_SPIKE_COOLDOWN_BOUNDARY_2026-08-29.md`
15. Wave 19の7組のgenerator・test・dated JSON certificate
16. `research_sources/wave19_literature_state/PRIMARY_SOURCE_AUDIT.md`
17. `core_workspace/CONTINUATION_2026-08-29_WAVE18_DESCENDANT_JUMP_AND_BIRTH_LOCALITY.md`
18. `core_workspace/endpoint_variance/WAVE18_EXCESS_DESCENDANT_JUMP_AND_BIRTH_LOCALITY_2026-08-29.md`
19. Wave 18のgenerator・test・dated JSON certificate
20. `core_workspace/CONTINUATION_2026-08-29_WAVE17_DISJOINT_CAPACITY_AND_EXCESS.md`
21. `core_workspace/endpoint_variance/WAVE17_DISJOINT_RESIDUAL_CAPACITY_AND_EXCESS_BOUNDARY_2026-08-29.md`
22. Wave 17のgenerator・test・dated JSON certificate
23. `core_workspace/CONTINUATION_2026-08-29_WAVE16_CONSTANT_FRACTION_AND_TERMINAL_POTENTIAL.md`
24. Wave 16とWave 13--15のproof memo・promotion・allocation文書
25. `core_workspace/CONTINUATION_2026-08-29_WAVE12_CUT_RENEWAL_INTEGER_PACKING.md`
26. `core_workspace/proof_obligations.md`
27. `core_workspace/approach_registry.md`
28. `core_workspace/counterexamples.md`
29. `core_workspace/research_log.md`
30. Wave 0--12の証明・監査・反例文書（履歴と導出確認用）

Wave 19の7組は次の通りです。

- `wave19_cross_ratio_half_absorption_certificate.py` / `test_wave19_cross_ratio_half_absorption_certificate.py` / `wave19_cross_ratio_half_absorption_certificate_2026-08-29.json`
- `wave19_certified_remainder_certificate.py` / `test_wave19_certified_remainder_certificate.py` / `wave19_certified_remainder_certificate_2026-08-29.json`
- `wave19_p28_full_row_ownership_certificate.py` / `test_wave19_p28_full_row_ownership_certificate.py` / `wave19_p28_full_row_ownership_certificate_2026-08-29.json`
- `wave19_p28_adaptive_row_cap_certificate.py` / `test_wave19_p28_adaptive_row_cap_certificate.py` / `wave19_p28_adaptive_row_cap_certificate_2026-08-29.json`
- `wave19_p28_transport_residual_floor_certificate.py` / `test_wave19_p28_transport_residual_floor_certificate.py` / `wave19_p28_transport_residual_floor_certificate_2026-08-29.json`
- `wave19_p28_mixed_transport_certificate.py` / `test_wave19_p28_mixed_transport_certificate.py` / `wave19_p28_mixed_transport_certificate_2026-08-29.json`
- `wave19_sparse_spike_certificate.py` / `wave19_sparse_spike_test.py` / `wave19_sparse_spike_certificate_2026-08-29.json`

旧Wave 0--12の endpoint theorem、multiscale kernel、有限Golomb最適化も
正準履歴として残っていますが、古い要約と矛盾する場合は上記Wave 19文書を
現在状態として扱います。

## Wave 19 の現在地

Wave 18のdescendant functionalをendpoint part `E_n`とcross-ratio rectangle
part `S_n`へ分解し、exact coefficientwiseに

`S_n<=(1/2)Y_n`

を証明しました。またendpoint weightsについてsharpなuniform supremum

`lambda_(n,q)<(3/4)c_(n,q)`

を得たため、既存prefix deficitの4分の3でendpoint overshootを払い、負の
4分の1を残せます。これをuncontracted Wave 13 spectrumへ一度だけ入れると

`Z_n<=(1/2)Y_n+G_n+epsilon_n-(U_n^cap+Q_n+mathfrak e_n)`

となります。ここまでで得られた上流目標P24は、すべてのfixed compatible
infinite eventual-`C` branchについて

`sum_(k=k0)^J omega_(k,J)G_(2^k)=o_(C,a)(log J)`

を証明することです。P24自体は未解決ですが、ここから得られた中間Route A
目標が次のP25です。

current-scale `Ghat`へのcap reindexingは`15/16`以下ですが、raw `v log d`
を一段ずらすと`(log2/6)J+O_C(log J)`の線形項が残ります。従って単純な
Fejer shiftでは閉じません。さらに、scaleごとに異なるscaled prime
Erdős--Turán prefixでは、同じlocal `C=32` capの下でも
`Ghat_n=Omega(log log n)`となります。これはlocal-onlyなP24証明を閉じますが、
正確にはsame-scale Golomb uniqueness・integer rank・local capだけからbare boundを
導く道を閉じるもので、一つのcompatible branch上のP24を反証しません。

Wave 18のlocal remainderを

`H_n^loc=Srank_n+Pair_n`

とexactに分けると、実際に使ったrowはrank slackだけで支払えて

`Theta_n^(exc,5/2)<=Srank_n+J_n^(5/2)`,
`Q_n^cert=Srank_n+J_n^(5/2)-Theta_n^(exc,5/2)>=0`

となり、`Q_n=Q_n^cert+Pair_n`です。このcertified payment、cap surplus、
`mathfrak e_n`を捨てずに残すと

`Rcert_n=mathfrak U_n-F_n^(loc,int)-Srank_n-J_n^(5/2)`
`-(1/4)Dpre_n-mathfrak e_n+epsilon_n`

および

`Z_n<=(1/2)Y_n+Rcert_n`

を得ます。previous-source capはexactに相殺されるため`15/16` lossは不要です。
また`Rcert_n`は全rulerの正整数dilationに対してexact invariantです。

中間段階のcertified target P25は

`sum_(k=k0)^J omega_(k,J)(Rcert_(2^k))_+=o_(C,a)(log J)`

です。exactに十分な弱いsigned定数形は
`limsup(sum omega Rcert)/log J<1/(3072C log2)`です。より強いuniform finite
window形は`sum_(k=L)^(2L)(Rcert_(2^k))_+=o_C(1)`です。いずれも未証明で、
dilation invarianceそのものは`Rcert`の上界を与えません。

さらにpairing slackについて

`0<=Pair_n<=[3/(4n^2)]log binom((n-1)(3n-4)/2,n-1)`

をexactに証明したため、`sum_(k>=2)Pair_(2^k)<infinity`です。actual Gothic bulkを
そのまま残して

`Rsharp_n=mathfrak U_n-mathfrak B_n-J_n^(5/2)`
`-(1/4)Dpre_n-mathfrak e_n+epsilon_n`
`=Z_n+(3/4)Dpre_n-J_n^(5/2)`

とおくと

`Z_n<=(1/2)Y_n+Rsharp_n`,
`Rcert_n=Rsharp_n+Pair_n`

です。従ってP25とP26のsigned/positive-part Fejer targetの差は`O(1)`、
block targetの差は`o(1)`です。中間段階のP26は

`sum_(k=k0)^J omega_(k,J)(Rsharp_(2^k))_+=o_(C,a)(log J)`

で、exactに十分な弱いsigned定数形は
`limsup(sum omega Rsharp)/log J<1/(3072C log2)`です。より強いblock形は
`sum_(k=L)^(2L)(Rsharp_(2^k))_+=o_C(1)`です。Pairのsummabilityは
bookkeeping slackを除くだけで`Rsharp`を支配しません。

さらに

`Zfin_n=Zob_n+Znb_n`, `Zfut_n=Zof_n+Zmf_n`,
`hstar_n=log(c_n/L_(n,n))`, `Jstar_n=J_n^(hstar_n)`,
`E0_n=sum lambda_(n,q)log(A/a_q)`

とおくexact auditにより

`Rsharp_n=((3/4)Dpre_n-E0_n)+(Zfin_n-S_n)`
`+(E0_n+S_n-Jstar_n)+Zfut_n+(Jstar_n-J_n^(5/2))>=0`

を証明しました。そのためP26のpositive partは不要で、P27は

`sum_(k=k0)^J omega_(k,J)Rsharp_(2^k)=o_(C,a)(log J)`

というnonnegative targetになります。scaleごとに異なるlocal `C=32`の
scaled prime Erdős--Turán prefixでは
`Rsharp_n>(39/256)log2`です。ただし同じbranchではないため、これは
local dataだけによるpointwise証明を閉じる結果であり、compatible branch上の
P27反証ではありません。

最終のinner-birth auditは、P27を証明するのではなく、単独のupper-bound route
として閉じます。row-exact endpoint partを`Erow_n`、
`Deltaabs_n=J_n^(5/2)-Erow_n`とおくと`0<=Deltaabs_n<=S_n`であり、

`Rprof_n=Z_n+Erow_n-J_n^(5/2)=Z_n-Deltaabs_n`
`=(Zfin_n-S_n)+Zfut_n+(S_n-Deltaabs_n)>=0`

とおくと

`Z_n<=S_n+Rprof_n<=(1/2)Y_n+Rprof_n`

で、`Rsharp_n>=Rprof_n>=W_n`です。ここで`i>=n`の未使用
inner-new-birth sector `W_n`は、任意の仮想的なeventual-`C` branch上で

`W_n>1/[1536 C log(4n)]`

を満たします。このFejer liminf係数は`1/(1536 C log2)`以上で、以前の
sharp-threshold routeが必要としたstrictな`1/(3072 C log2)`の2倍です。
従ってP26/P27の`o(log J)`、sharp-threshold、uniform block形は、既知の
compatible-branch lower floorと衝突するため「より簡単な次補題」としては
使えません。これはP27の証明でも、仮想branchの排除でも、#1191の解決でも
ありません。

現在の最高価値方向P28は、`W_n`をnegative renewal cutに対して保持または
移動するか、descendant absorptionをinner birthsまで拡張し、atom ownershipを
exactに保ってdouble spendingを避けることです。P28はopen design obligationで、
十分定数まで証明された定理statementではありません。

その後のP28監査で、次の有限定理と境界が確定しました。

- 全terminal係数`u_p`の配分は、early rowのbeta容量超過と、次のnegative cutが
  所有する`v_p`の二重使用のため不適法です。cut-valid demandは
  `bar r_p=u_p-v_p`です。
- natural `bar r` transportは全有限atomで`Sbar_n<=Y_n/2`を満たしますが、
  inner sectorでは`3W_n/10<=Sbar_n|W_n<W_n/2`です。従って`W_n/2`より
  大きい残差が残り、旧strict thresholdをちょうど飽和します。
- 固定高さ`5/2`のshort rowではthresholdが負になります。row-dependent height
  `h_(n,p)=max{3/2,log(c_n/L_(n,p))}`は符号を直し、そのcap upperはtarget
  epoch `N>=2048`で次scale rank surplusから支払えます。actual rankを使っても
  endpoint term自体は消えません。
- complete signed ledgerでは`Sbar_n<=Y_n/2`と`E0_n<=3Dpre_n/4`を同時に保ち、
  残る量は
  `Gad_n=R_n+Pcoef_n log A-K_n^int-T_n-Theta_n^full-Dpre_n/4`です。
- 任意のfeasibleかつenergy-awareなtransportでも、dyadic `n>=64`で
  `Eres_n(t)>=n^2/(2^25 H'_n)`が残ります。eventual-`C` branchでは
  `>1/(2^27 C log(4n))`で、Fejer liminf係数は`1/(2^27 C log2)`以上です。
  cornerの最大coverageはexactに`1/3`です。
- `t_mix=(8t_natural+t_right)/9`というmixed right-greedy transportは全row sumと
  beta capを保ち、cross側の`Y_n/2` boundを維持したままendpointを
  `E_mix<=2Dpre_n/3`へ改善します。従って
  `Gmix_n=R_n+Pcoef_n log A-K_n^int-T_n-Theta_n^full-Dpre_n/3`となり、
  adaptive ledgerよりexactに`Dpre_n/12`改善します。

ただし、8点の完全有理Golomb反例により、inner residualを`Dpre_n/12`だけで
直接支払うことはできません。whole cutを含むsigned cancellationは反証されて
いません。現在の最小の未解決補題は

`limsup_(J->infinity) [sum omega_(k,J)Gmix_(2^k)]/log J`
`<1/(3072 C log2)`

またはそのpositive-part little-o版です。raw `v` fanや、すでに落とした
rank/Pair/cap bracket、`Dpre,Y,W`を再利用してはいけません。P28、Question 1、
Question 2、novelty、賞金獲得主張はすべて未解決です。

有限側では、全prefixがexact rational `C=32` capを満たす一つのGolomb chainを
512点まで構成し、`130,816`個の差がすべて相異なることを再生確認しました。
ただしcooldownのalternative branchesはglobal exhaustiveではなく、無限延長
定理もありません。P23/P24/P25/P26/P27/P28の反例でもQ1/Q2の解答でもありません。

文献状態は345件、manual選定10件、full read 6件です。検索質問はP23時点で
固定され、その後P24--P27を経て現在はP28方向へfrontierが更新されましたが、監査した
fixed-branch・birth-delay・compatibility条件は変わりません。監査範囲では
P28に必要なexact cancellation/absorption定理は見つかりませんでしたが、これは定理不存在やnoveltyの
主張ではありません。

## Wave 18 の現在地

Wave 18はP22を二つの意味で前進させました。まず高さ`h=5/2`で、exact local
coefficient rowsとWave 17のsorted-rank slackから

`Theta_n^(exc,h)<=H_n^loc+J_n^(h)`

を証明しました。`J_n^(h)`は`d_(n,p)/D_(p,q)>exp(h)/3`のときだけ現れる
明示的descendant-jump functionalです。さらにtarget epoch `n`のsurplusが
source `n/2`のcapped promotionを払い、

`Z_n-R_(2n)=mathfrak P_n-K_n^int-mathcal T_n`
`-Theta_(n/2)^[5/2]-Theta_n^(exc,5/2)+J_n^(5/2)-(U_n+Q_n)`

というexact signed identityを得ました。ここで`mathcal T_n,U_n,Q_n>=0`です。

別のrank-layer分解では、任意の固定future difference `x`に対する全dyadic
sourceのreuseを

`Lambda^(exc,h)(x)<[8C log2/(3exp(h))]log(4x)/x`

まで抑えました。従って残った壁はcoefficient reuseではなくbirth timeです。
現在の仮定からは、`x`のbirth scaleを`x`自身で一様に上から抑えられず、その
birth carrierに既存floor未使用分が十分あるとも証明できません。

Wave 18終了時点の単一主目標P23は

`sum_(k<=J)omega_(k,J)J_(2^k)^(5/2)=o_C(log J)`

または同値なsigned cancellationです。finite Erdős--Turán rulersはone-epoch
local slackの発散を反証し、distant-block constructionはcritical capなしの
terminal-only評価を反証します。P19/P23、Question 1/2、賞金請求は未解決です。

さらにexact q-collapseにより

`J_n^(h)<=sum_p r_(n,p)[log(d_(n,p)/D_(p,n))-(h-log3)]_+`

まで縮約しました。ただし高さ`5/2`のthresholdは`log4`より僅か
`0.0150933...`大きいだけです。alternating scalar modelはFejer sum
`Theta(J)`を与え、terminal cap内のactual finite Golomb familyも
`J_n^(h)>=(3/8-o(1))log log n+O_(C,h)(1)`を実現します。後者は一つの
fixed-onset eventual-`C` branchではないためP23の反例ではありませんが、
one-epoch改善を閉じます。

## Wave 17 の現在地

Wave 17は、Wave 16で残った「同じGothic bulkを既存floorとpromotionに
二重使用していないか」というP21のlocal gateを解きました。まず

`mathfrak B_(2m)>=K_(2m)^int+[log(3/2)/12]Delta_m`
`-2146log(3/2)/(16m^2)`

をsame-atom residualだけで証明しました。次にexact local sorted-rank floorの
surplus `D_n`について

`|D_n-[3/2+(3/4)log3-2log2]|<=18(1+log n)/n`（`n>=16`）

を得ました。従って`n>=2^20`で`D_n>81/128`、`n>=2^22`で
`D_n>3/4`です。一つのstronger floorはeventually `3Delta_m/8`を払うか、
別案として`u-v` promotionの高さ2までのtruncationを全て払えます。この二つは
同じcapacityの別用途であり、加算できません。

Wave 17時点の正確な主目標P22は、残る

`Theta_m^exc=sum_p r_(m,p)(P_(m,p)-2)_+`

を、actual local slack・unused rank surplus・完全なendpoint/descendant renewalを
使ってbounded reuseでsigned repaymentすることです。現在の一般上界は一epoch
`O_C(log log m)`なので、Fejer taperだけでは`o(log J)`になりません。Wave 17は
local capacityを解きました。Wave 18はそのsign/reuse部分を前進させ、現在は
上記P23が主目標です。

## 保存済み Wave 16 の現在地

Wave 16は、`d>=L^2/8`のold differenceについて、互いに交わらない約
`(log L)/(2log 2)`個のfuture blocksを同時に数え、

`rho_infinity(d)-rho_L(d)>d/(128C log 2)`

を証明しました。したがってmacroscopic suffixのpromotion logarithmは
`1/log m`ではなく、`kappa_C=log(1+1/(128C log2))`以上です。legalな
next-shell rebateは各epochで`kappa_C/6`以上、未割当`u-v` resourceは
`kappa_C/3`以上になります。ただし、どちらもpositive resourceであり、
negative carrierなしにfrontierから引くことはできません。

さらにexact renewal expansionから

`Z_m-R_(2m)=mathfrak P_m-mathfrak B_m-mathcal T_m`, `mathcal T_m>=0`

を得ました。これにより、Wave 15でisolatedに見えていたterminal
`mathfrak U_(2^J)=Theta(J)`は真のsigned obstructionではなく、terminal upperは
`O_C(log J)`まで下がります。Fejer taperはharmonic signalを保ったままraw
terminalと1-step weight mismatchをnegligibleにします。

これはWave 16時点の正確な次目標でした。Wave 17は同じnext-bulk
coefficient capacityを`Delta_m`とtriangular floorへ重複なく配分する
local disjoint-premium theoremを証明し、残る標的をP22へ更新しました。

## 保存済み Wave 13--15 の現在地

Wave 13は、仮想的なeventual-`C` integer branch上で`Y_m`と`Z_m`がともに
`1/(1536C log(4m))`以上になるharmonic barrierを証明しました。したがって
P17/P18のall-`C` little-oh主張はQuestion 1と論理的に同値であり、単なる
中間的decay lemmaではありません。signed targetではterminal `R` tailを
必ず残す必要があります。

Wave 14は、長いold difference `d`について

`rho_infinity(d)-rho_L(d)>=d/(64C log d)`

というfuture-rank promotionを証明しました。同じsuffix atomが次epochの
lower shellへ再登場する係数だけを使うと、重複なしで

`A_J>=K_J^star+Phi_(J-1)`

を得ます。Wave 15は、直後blockで実現するmarginal promotion `Delta_m`の
nested reuseを一atomあたり`3/(4m^2)`未満に抑え、full next bulkへ割り当てました。

ただし、この`Delta_m`上界は既存floorと同じbulk capacityを使うため、現状のまま
加算できるpremiumではありません。当時のisolated terminal suffix fan
`Theta(J)`という記述はWave 16のexact renewal potentialで修正済みです。

## 保存済み Wave 12 基礎（当時の「現在」）

Wave 12では、Wave 11のpositive future cut tail `R_m`を1 dyadic stepずらし、
4つの明示的非負sectorの和`Z_m`について

`Y_m=R_m-R_(2m)+Z_m`

を係数ごとに証明しました。従って

`sum Y_m=R_4-R_(2^(J+1))+sum Z_m`。

各fixed pairに対する`Z`係数のdyadic総和は一様有界で、raw tailの
`Theta(log(j/i))` overlapは解消されました。Wave 12当時の主目標P18は、一つの
fixed infinite eventually-critical **integer** Golomb branch上で

`sum_(m in E_J)Z_m=o_C(log J)`

を証明することです。これでP17が従いますが、terminal positive tailがある
ため同値とは主張していません。残る困難は異なるinteger pairs全体のpackingです。

numerical rank、triangular length floor、全interval-containment orderを同時に
最適化しても、Wave 11 floorからの改善は一epochあたり`5`未満です。また
`a_n=n^2+sqrt(2)n`はquadratic real Golomb rulerですが
`Y_m -> (3/2)(log 2-1/2)>0`です。これは非整数なので#1191への反例では
ありませんが、次の証明がinteger unit spacingまたは同値な算術を明示的に使う
必要があることを示します。

以下のWave 11記述は、この最新状態を支える保存済み基礎です。

Wave 11では、隣接gapが互いに異なる正整数であることから、長さ`ell`の
任意interval差に

`D_(p,q)>=binom(ell+1,2)`

を適用しました。exact Abel係数で重み付けすると

`K_m^len=2log m+O(1)`

となり、Wave 10の`7/4` floorが失っていた先頭
`(1/4)sum log m`を完全に回収します。さらに

`T_m-K_m^len=Y_m+G_m^len+S_m`

が各epochでexactに成り立ち、右辺3項はすべて非負です。これにより表示上界は
`O_C(J^2)`から`O_C(J log J)`へ改善しましたが、必要な`o(log J)`では
ありません。

Wave 11当時の単一主目標P17は、一つのfixed infinite eventually-critical branch上で

`G_J^len+S_J>=T_J-K_J^len-epsilon_J`,
`epsilon_J=o(log J)`

を証明すること、すなわち`sum Y_m=o(log J)`を得ることです。lower residualは
exactなfuture cross-ratio tailですが、同一pairのdyadic overlapは
`Theta(log(j/i))`なのでuniform birth chargeは反証済みです。別の
within-length sortのtriangular floorからの増分は一shell
`O(m^(-1/2))`に留まります。別に、2025 finite-diameter theoremは
`log diam>=2log k-O(k^(-1/2))`であり、このorderなのは主項に対する
下位補正です。total-diameter scalarにはcross-length/survival stateがなく、
必要なのはそのcouplingです。

以下のWave 10・Wave 9記述は、この最新状態を支える保存済み基礎です。

### 保存済み Wave 10・Wave 9 基礎（「次」は当時の意味）

Wave 10では、Wave 9が提案したlaminar weighted incomplete-DTS方針を
実際に最大限まで押し進めました。任意重み付きの遺伝的不等式

`sum r beta_r <= sum lambda*d <= sum N_(2m) Gamma_m`

と、対応する`product d >= M!`型のlog-product制約を証明しました。また、
固定gap位置への将来のendpoint-product/inverse-difference負荷はdyadicに
`O(4^(-K))`で減衰するため、残る質量は新しい前線へ移動し続けなければ
ならないことも証明しました。

一方、cross-ratio Abel shellの全negative bulkを全epoch同時に並べ替えても、
最適主項は

`F_E=(7/4) sum_(m in E) log m+O(|E|)`

に留まります。境界を消すには各scaleでもう`(1/4)log m`と二次的な
`log log m`が必要です。さらに既存W9-RLP行は、prefix modulus固定後の
tile LPでは全tile変数の係数が0であり、単純に併置してもoptimumは変わらない
ことを厳密に確認しました。当時のexact obligationはP15でした。当時の有力な
十分条件候補は、actual bulk premiumとpositive-boundary slackを合わせる
**survival-conditioned Abel repayment**、または別のbi-/tri-tree上の
**tensor-box encoding + vanishing box constant**です。両者の同値性・必要性は
未証明です。

30個のWave 10 focused tests、exact primal=dual、9,845,549個のRLP選択、
certificate byte replayで有限部分を監査しています。ただしP15、Question 1、
Question 2は未解決で、賞金請求はまだできません。

Wave 9で正の出生予算は、正規化gap測度
`nu_n=N_n^(-1) sum_(i<n) h_i delta_(i/n)` の位置分散
`V_n=Var_(nu_n)(u)` へ定数因子の損失だけで還元されました：

`(4/49) sum_(k=1)^(J+1)V_(2^k) <= B_H(J)
 <= (36/35) sum_(k=1)^(J+1)V_(2^k)`。

従ってP15の残りは `sum_(k<=J)V_(2^k)=o(log J)` と同値です。しかし
相異なる真の隣接gapだけで `V_n>=n^2/(512N_n)` となるため、局所的に
各分散を小さくする方針では解けません。短rankと小endpoint gapは合計
`O(log log J)`へ除去済みで、残るのはlong-rank・両endpoint-large coreです。

weighted cross-ratioには完全なAbel係数式と、strict-interior minimum/gcdを
同時に使うshifted-factorial境界があります。これは単一状態を強くしますが、
全epoch和ではまだ不足します。文献側ではMa--Yi/Shearerから、任意のepoch
部分集合に同時適用できるhereditary rank-lag inequality W9-RLPを抽出しました。
Wave 9当時の単一目標は、これをtile容量とAbel符号へ結合した
**survival-conditioned laminar weighted non-saturation theorem**です。有限LPや
有限探索だけでは無限枝を証明したことになりません。

以下はこの現在地に至る証明履歴です。

基礎定理は、短いpairの端点不均衡 `delta_N` から、全offsetのsame-block energyの分散を完全復元します。

- `Var E_N = ||delta_N||_{H^{-1}(Z/NZ)}^2`
- ゼロ分散は短pair residue graphがEulerianであることと同値
- diameter regimeでは mandatory split levels から

  `Var E_N >= m(m^2-1)(m^2+11)/(180N)`

- ただし、これを多数のprefix・modulusで結ぶSidon上界がまだありません。

その後、diameter modulusで完全に正のgap-pair展開と、正規化gap測度の
共分散行列更新

`M_(2m) = B M_m B^T + Q_m`, `Q_m >= 0`

を証明しました。最大の `3m/4` 個の相異なる隣接gapを二段階agingすると、
dyadic `M>=16` で

`Var(C_(N_M))/M^4 >= (9M^2-256)/(1,048,576 N_M)`

となります。臨界包絡 `N_M<=2CM^2 log M` の下では、dyadic和が
`(9+o(1)) log J/(2,097,152 C log 2)` 以上です。これは直前の
8-block定数の16倍で、隣接gapの相異性しか使いません。

より古い `m^-3` 汎関数についても、cyclic-arc covariance の正確な
kernelとpair--pair展開、および臨界包絡線下の

`F_J >= (1+o(1)) log(J)/(360 C log(2))`

まで証明済みです。現在の最強汎関数は `m^-4` 重みで、固定interactionの
tailを `4/(15m_s^4)`、粗い絶対損失を一shell `O(1)` まで下げました。
しかし必要な `G_J=o(log J)` signed/structural upper budget は未証明です。
正値性・単調性・無条件raw-budget版には反例があります。したがって
次の主目標は、exact adjoint identityで隔離されたactual birth-shell
innovationを、**一つのglobal critical Sidon sequenceのunbounded history**
で償却する anti-Eulerian lemma です。抽象PSD recursionだけでは
`G_j=1/72`の線形成長例があり、任意の固定深さのlocal critical window
だけでもErdős--Turán族が `Q_00/N -> 1/360` を保ちます。従って整数の
cross-scale contiguous-sum uniquenessを本質的に使う必要があります。

Wave 4では、このlocal obstructionを末尾
`floor(log_2 J)-1=Theta(log log M)`個のdyadic prefixまで強化しました。
また、一つのglobal critical列なら直径profileのdiscrepancyが
`Omega(1/log M)`となり、profile resetが必ず起こることを証明しました。
ただし、各old--new difference帯域の占有率からinnovationを直接支払う
不等式は反例で排除されています。次の本命は、異なるepoch間のcross
differencesを使い、profile resetが無限に独立更新できないことを示す
flat-profile versus profile-reset amortizationです。32点の有限nested
witnessも4遷移での単調減衰を反証しますが、無限列ではありません。

Wave 5では、旧profileの非線形成分がchord除去後に正確に輸送され、深い
packing resetの位置と負符号も固定されることを証明しました。一つの
endpoint-flat runは`O(log log m)`世代しか続きません。しかしdyadic
`C=1`かつ全prefix `O(n^2 log n)`の無限sawtooth gap profileが、resetを
疎にしながら全stepで`Q_00/N>=1/2048`を保ちます。このprofileは4点で
差14が重複する非Sidon例です。従って次の本命は、複数のreset-to-flat
cycleをまたぐ全contiguous-sum一意性を使うarithmetic reset-renewal
exclusionです。有限側では認証済み32点列を64点まで延長し、五遷移で
innovationを`0.0037994`より大きく保ちましたが、無限延長ではありません。

Wave 6では、新生shellとold--new anti-diagonal差を、複数epochにわたる
同一の整数帯域へ正確に注入しました。閾値
`tau_(m,k)=D_m^-+D_m^++k max(mu_m^-,mu_m^+)` に対する積分台帳は
`sum k/tau_(m,k)<=1+log X` を与えますが、endpointではまだ`O(log X)`で、
必要な`o(log J)`には届きません。一般のbirth-lag Hall圧力`Lambda<=1`は
厳密ですが、経験的な`1/(4 sqrt(n))`減衰則は、一つの64点C=1 Golomb
rulerが8→16、16→32、32→64の三連続遷移で厳密に反証しました。
別のheuristic continuationは128点まで達し、8,128差と全127 prefix包絡を
完全監査済みです。どちらも有限証明書であり、無限延長を示しません。

さらにresidue liftにより、一点追加の禁止shadowは高々4剰余類に閉じ込め
られ、増大する有限互換windowでも局所shadow密度からinnovationを支払う
一般則が反証されました。Wave 6時点の単一目標は、一つの無限critical Sidon
列で古い履歴が新しい数値帯域へのcutoff renewalを阻止し、Wave 6の
`O(log)`台帳を`o(log J)`へ自己改善するglobal band-renewal theoremです。

Wave 7では、old--new全rank lagとnewborn内部差を加え、dyadic prefixの
全pairを出生epochごとに一度ずつ分割しました。rank floorを併用すると
`sum_F q_F ell_F/gamma_F^2<=8 sqrt(2)`という一つの無限Golomb履歴上で
総和可能なpotentialが得られます。しかしterminalごとに変わる
Erdős--Turán窓ではadjoint innovationが発散する一方、このpotentialは
`o(1)`なので、固定定数affine支配は反証済みです。

非局所量`surv_C(P)`を、同じ臨界包絡内でprefix `P`を延長できる最大高さ
として定義しました。有限分岐König補題により`surv_C(P)=infinity`と
「同じPが一つの無限critical Golomb列に属する」は同値です。局所候補RHと
HTは厳密反証、epoch-size tax ESTは全8点Golomb rulerまで普遍的に証明され、
64/128点有限標本でも生存しています。ただし128点例ではadjacent-halfだけ
では63の未払いdebtが残ります。Wave 7当時の単一目標は、`surv_C=infinity`を仮定し、
このdebtを未使用non-adjacent差または容量slackで返済させ、actual `Q_m`を
`o(log J)`で支配する定理です。Q2は任意深さの一様有限実現を証明し、König
補題で無限枝を取る経路が副目標です。

Wave 8ではactual newborn-adjacent familyをglobal integer ledgerへ追加し、
各epochで「現在を支払う」か「古いadjacent ancestryを全てclearする」かの
厳密な二者択一を証明しました。一つの固定history上で未払いinternal
familyは高々一つです。またactual `Q_m`を全pairのsigned energyへ完全展開し、
shellの負square atomsが二つのproper boundary fanだけであることを証明。
critical cap下のadjacent endpoint debtと人工boundary rowは総和可能です。

決定的な更新はpair telescopeです。各pairのbirth chargeから全将来の
old-pair負項を引いても少なくとも半分が残り、全体で

`B_H(J)/2 <= sum_(j<=J)<H,Q_j/N_(2m_j)> <= B_H(J)`

となります。従ってsigned cancellationを待つ道は閉じ、Wave 8当時の単一主目標は
一つの無限eventually-critical Golomb branch上でpositive birth budget
`B_H(J)=o(log J)`を証明することです。local `U/T`、latest-shell density、
raw non-adjacent countには厳密反例があります。Hegyvári有限blockも監査し、
無条件spliceはcritical scaleで立方化するためQ2のcompatible towerには
なりません。682点fixtureの全510更新を含む有限検証は有望な反例フィルタ
ですが、無限主張ではありません。

## 検証

ZIP展開後のルートで次を実行します。

```bash
python -m venv /tmp/erdos1191-pytest-venv
/tmp/erdos1191-pytest-venv/bin/python -m pip install -r core_workspace/endpoint_variance/requirements-test.txt
ERDOS1191_PYTHON=/tmp/erdos1191-pytest-venv/bin/python ./integrity/run_all_checks.sh
```

Wave 19の7組をまとめたfocused suiteは73 testsと11,164 subtests、全pytestは
401 testsと78,844 subtestsを通過しました。7つのdated JSON certificateは全て
byte replay一致、対応する14個のgenerator/test Python fileはRuff check/formatを
通過しています。release runner、自己除外manifest、独立展開後の同一完全
runnerの結果は`integrity/WAVE19_TEST_VERIFICATION_2026-08-29.json`に固定します。

Wave 18時点の履歴値は全pytest 328 tests / 67,680 subtests、focused Wave 17--18
22 tests / 2,237 subtestsです。これは
`integrity/WAVE18_TEST_VERIFICATION_2026-08-29.json`に保存されています。
いずれも有限検証であり、#1191の漸近解決ではありません。

## 整理上の注意

- 2つ目の添付ZIPに入っていた28ファイルは、1つ目のZIP内 `core_workspace/endpoint_variance/` と全てhash一致でした。そのため重複コピーは含めていません。
- 元のendpoint内部 `SHA256SUMS` は自己自身を検証対象に含めていたため、1件だけ必ず不一致になります。元記録は監査用に保存し、新パッケージでは自己項目を持たないmanifestを生成しています。
- 旧ledgerが参照する `computation/crossblock.py` 等は今回の添付に含まれていません。未添付の計算を再現済みと扱わないでください。
- mandatory-level boundの等号例 `A={0,1,...,m-1}` は、`m>=3` ではSidonではありません。一般有限集合としてのsharpnessであり、Sidon classでのsharpnessは別問題です。

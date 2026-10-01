# Erdős Problem #1191 次セッション用引き継ぎ

このZIPは、2026年8月29日時点の endpoint-variance / rank-variance /
triangular Abel repayment / positive cut-renewal 継続研究を、重複・キャッシュ・
壊れた内部manifestを除いて整理したものです。

## 新しいセッションでの使い方

1. ZIPを添付する。
2. `NEW_SESSION_LAUNCH_MESSAGE.txt` の全文を貼り付ける。
3. 研究モデルには、最初に `00_START_HERE_PROMPT.txt` を読むよう指示する。
4. ZIP内の `core_workspace/` を現在の正準研究状態として継続させる。

## 最初に読む順番

1. `00_START_HERE_PROMPT.txt`
2. `HANDOFF_MANIFEST.md`
3. `core_workspace/1191_MASTER_STATUS.md`
4. `core_workspace/CONTINUATION_2026-08-29_WAVE12_CUT_RENEWAL_INTEGER_PACKING.md`
5. `core_workspace/endpoint_variance/WAVE12_SIGNED_OFFDIAGONAL_SURVIVAL_ANALYSIS_2026-08-29.md`
6. `core_workspace/endpoint_variance/WAVE12_CUT_RENEWAL_PROBE_2026-08-29.md`
7. `core_workspace/endpoint_variance/wave12_cut_renewal_certificate_2026-08-29.json`
8. `core_workspace/research_sources/WAVE12_SIGNED_OFFDIAGONAL_LITERATURE_DELTA_2026-08-29.md`
9. `core_workspace/research_sources/wave12_literature_state/search_log.json`
10. `core_workspace/CONTINUATION_2026-08-29_WAVE11_TRIANGULAR_ABEL_REPAYMENT.md`
11. `core_workspace/endpoint_variance/WAVE11_SURVIVAL_ABEL_REPAYMENT_ANALYSIS_2026-08-29.md`
12. `core_workspace/endpoint_variance/WAVE11_ABEL_REPAYMENT_PROBE_2026-08-29.md`
13. `core_workspace/endpoint_variance/wave11_abel_repayment_certificate_2026-08-29.json`
14. `core_workspace/research_sources/WAVE11_SURVIVAL_ABEL_LITERATURE_DELTA_2026-08-29.md`
15. `core_workspace/CONTINUATION_2026-08-29_WAVE10_LAMINAR_LOG_PRODUCT_NO_GO.md`
16. `core_workspace/proof_obligations.md`
17. `core_workspace/approach_registry.md`
18. `core_workspace/counterexamples.md`
19. `core_workspace/research_log.md`
20. `NEXT_LEMMA_TARGETS_ANTI_EULERIAN.md`
21. Wave 0--11の証明・監査・反例文書（履歴と導出確認用）

旧Wave 0--11の endpoint theorem、multiscale kernel、有限Golomb最適化も
正準履歴として残っていますが、古い要約と矛盾する場合は上記Wave 12文書を
現在状態として扱います。

## 重要な現在地

Wave 12では、Wave 11のpositive future cut tail `R_m`を1 dyadic stepずらし、
4つの明示的非負sectorの和`Z_m`について

`Y_m=R_m-R_(2m)+Z_m`

を係数ごとに証明しました。従って

`sum Y_m=R_4-R_(2^(J+1))+sum Z_m`。

各fixed pairに対する`Z`係数のdyadic総和は一様有界で、raw tailの
`Theta(log(j/i))` overlapは解消されました。現在の主目標P18は、一つの
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

現在の単一主目標P17は、一つのfixed infinite eventually-critical branch上で

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

最終再実行では275 testsと54 subtestsが通り、294項目の自己除外manifest、
Wave 12までの全証明書のbyte一致、独立展開後の同一完全ランナーも通ります。
正確なscopeとコマンドは `HANDOFF_MANIFEST.md` と
`integrity/WAVE12_TEST_VERIFICATION_2026-08-29.json` に固定しています。
いずれも有限検証であり、#1191の漸近解決ではありません。

## 整理上の注意

- 2つ目の添付ZIPに入っていた28ファイルは、1つ目のZIP内 `core_workspace/endpoint_variance/` と全てhash一致でした。そのため重複コピーは含めていません。
- 元のendpoint内部 `SHA256SUMS` は自己自身を検証対象に含めていたため、1件だけ必ず不一致になります。元記録は監査用に保存し、新パッケージでは自己項目を持たないmanifestを生成しています。
- 旧ledgerが参照する `computation/crossblock.py` 等は今回の添付に含まれていません。未添付の計算を再現済みと扱わないでください。
- mandatory-level boundの等号例 `A={0,1,...,m-1}` は、`m>=3` ではSidonではありません。一般有限集合としてのsharpnessであり、Sidon classでのsharpnessは別問題です。

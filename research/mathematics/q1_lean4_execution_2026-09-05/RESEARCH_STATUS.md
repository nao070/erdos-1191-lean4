# Erdős 1191 Q1 — 実行記録（未解決）

この作業は **原 Q1 の完全証明・完全反証に到達していない**。現在の Lean 検証には、原定式化と整数定式化の同値、反証に必要な条件の同値、入力条件の非空性、direct Haar 行列の代数補題、正差ラベルの共通予算、実 interval demand を伴う有限 physical envelope、および実際の一次モーメントから導いた追加需要が含まれる。`Q1` は透明な命題として定義されているが、その証明項は存在しない。本ファイルは成功判定でも、外部中断を装う報告でもない。

## 2026-09-06 03:20 JST の状態確認

**原 Q1 の完全証明・完全反証、最終 Lean theorem は未達。Goal サービスの実状態は paused。**
親が今回2回取得した実状態は同じ一時停止表示だった。変更主体・理由は未確認で、
数学の困難を理由に blocked にしたものではない。親は `update_goal` を呼んでおらず、
モデル・推論設定も変更していない。確認記録は `evidence/goal12_goal_state_observation.json`。
一時停止を受け、新しい研究・形式化の委任は行わず、届いた成果と再開地点だけを保存した。

前回の384ファイルは、保存済み snapshot と全て byte identity が一致した。
Lean の検証範囲は引き続き補助138宣言・8個の別々の監査で、今回新たな Lean 実行はない。
原 Q1 の証明項、完成 release の clean build、最終定理の公理監査は存在しない。

実行中だった担当から `research/future_covariance_rank_localization.md` が届いた。
これは相関量 `sum sqrt(P_b)/b` を六つの端点が異なる制限された場合へ絞る解析案。
親は保存ファイルと報告 hash の一致を確認したが、全文の独立した数学監査は未了で、
Lean 未検証。前回までのレビュー済み結果へ昇格させていない。
残る主要義務は、その制限された相関量を一つの実際の全履歴で評価することと、
形式側では ordered triple fiber と multiset/aut 重みの同一視である。

保存記録は `evidence/goal12_pause_checkpoint.json`。これは未完了の引継ぎであり、
数学的な不可能性・Q1 の解決・背後での自動継続を主張しない。

## 2026-09-06 00:07 JST の履歴

**原 Q1 の完全証明・完全反証、最終 Lean theorem は未達。Goal は active。**
日付が変わっても同じ objective を維持している。親は `update_goal` を呼ばず、
指定モデル・推論設定を変更していない。実状態は
`evidence/goal11_goal_state_observation.json` に保存した。

指定 ZIP と MASTER、C143 V2 bank、最新の bound follow-up は以前の実ファイルと一致。
34件の限定 metadata inventory も一致する。同じ巨大 pricing replay は繰り返さず、
C139 台帳を現在地にしていない。`evidence/goal11_primary_byte_identity.json` に記録した。

今回、実際の Sidon 集合の順序付き三項和を有限集合として定義し、第一端点を固定すると
残りは高々2順序であることから `orderedCard <= 2|K|` と実数の `orderedCard/6 <= |K|/3`
を Lean で証明した。反復端点・空集合も含む。新しい **6宣言**の対象 build、全名の公理監査、
import 環境の Lean checker はそれぞれ一回、実 exit 0。親も24/32件の binding、
全出力・生成物・公理と旧335ファイルの一致を確認した。
`research/sidon_triple_fiber_formal_scope.md` と `evidence/goal11_sidon_parent_binding.json` が根拠。
計 **138宣言、8つの別々の保存済み監査**で、一括138監査ではない。
weighted multiset/aut との同一視、全 orbit・energy・source、原 Q1 と完成 release は未検証。

解析では、端点の剰余頻度とモーメント、実際の穴を除いた support の下界を導出した。
`n <= q <= n log(2n)` でも、6と互いに素な modulus 群全体には格子拡大の損失が残る。
primitive 履歴にも残るが、全整数 modulus を適応的に選ぶ場合は否定していない。
`research/growing_residue_cap_comparison.md` に正確な範囲を記録した。

幾何学的な不足量 G から、階数1の非負 PSD source Gamma を直接構成した。
総 trace <=1-zeta(2)/2、将来 tail <1/4 を保ち、費用を Gcal/8 と有限定数で評価する。
以前の Theta からの需要移行では、元係数が0の対にも新係数が出る一般配分の証明不足を
親が見つけ、対ごとの使用量と誤差の support を明示して修正した。独立レビューでも修正版を確認。
PSD の差や元の affine LP との同値は主張していない。長い将来区間からの実需要も非可和だが、
旧残差を自動的に減らすわけではない。`research/coherent_defect_source.md` に記録した。

Fourier 経路では、fresh same-sign star の将来寄与が0になること、反復項と quartic diagonal
の費用が有限であることを導いた。ただし順位による差分和には元の量を保つ commutator が残る。
問題は、相関した実量 `sum sqrt(P_b)/b` の評価まで絞られた。実際の正整数 Sidon 族により、
重みを付ける前の `O(T^3 H^2)` 上界は否定できるが、無限の fixed-cap 反例ではない。
`research/causal_fourier_rank_commutator.md` に式・定数・有限族の範囲がある。

3本の新解析は独立レビュー済み。親の再導出と一般転送の修正記録は
`research/goal11_parent_review.md`、最終版の結び付けは `evidence/goal11_reviewed_research.json`。
次は全 modulus の適応的比較、Gamma と Psi の実際の共同配分、または相関した P_b の全履歴評価を
進める。これらの補助結果を completion とせず、原 Q1 と最終 Lean 検証へ継続する。

## 2026-09-05 23:25 JST の履歴


**原 Q1 の完全証明・完全反証、最終 Lean theorem は未達。Goal は active。**
親は `update_goal` を呼んでいない。指定モデル・推論設定を変更していない。
実状態は `evidence/goal10_goal_state_observation.json` に保存した。

指定 ZIP と MASTER、Downloads の C143 V2 bank、最新の bound follow-up の
内容は引き続き一致する。34件の限定した metadata inventory に新しい置換入力はない。
同一 bank の90,600,510件 pricing replay は再実行せず、C139 台帳も現在地にしていない。
根拠は `evidence/goal10_primary_byte_identity.json`。

実際の Sidon 端点から far pair の一意性を導き、有限衝突集合から近い3座標への
単射と `card <= |K|^3` を形式化した。新しい **7宣言**の対象 build・全名の公理監査・
import 環境の Lean checker は実 exit 0。親も実ソース、23/31件の実行時 binding、
公理と全出力、生成物、旧281ファイルの一致を独立に読み戻した。
`evidence/goal10_sidon_parent_binding.json` と
`research/sidon_collision_determination_formal_scope.md` に範囲を記録した。
補助範囲は **計132宣言、7つの別々の保存済み監査**で、一括132宣言監査ではない。
全 orbit・geometry・energy・source の統合、原 Q1、完成 release は未検証のまま。

解析では、固定した投影の最適配分にも、格子拡大で一様な損失が残ると証明した。
1点を加えて gcd を1にしても残り、固定した有限個の modulus を使っても回避できない。
一方、同じ二つの shadow を剰余類ごとに投影する改善を構成した。無制限に細分化すると
需要と実容量が一致するだけの恒等式になり、そのゼロ残差は Q1 を閉じない。
これは `research/eligible_capacity_packing_closure.md` にある。

三項和の実 fiber から、新しい非負 PSD source Theta を構成した。総 trace <=5/36、
有限制限の将来 tail <=1/18 を保ち、既存の geometry defect で費用を評価できる。
同一成分を実際の長い将来区間へ一度ずつ配分し、Hardy 評価から非可和な実需要を得た。
ただし追加後の残差は旧残差と新残差の和であり、元の未制御量を自動的には減らさない。
`research/triple_potential_productive_source.md` に式と固定 cap・有限 horizon を残した。
二つの自然な PSD 残余候補は、実際の正整数 Sidon 集合 {1,2,4,11,15} で否定できる。
他の full-defect 表現は否定していない。詳細は `research/triple_source_remainder_analysis.md`。

別経路では、実際の順序を保つ Fourier 係数の恒等式として利用可能量を表した。
通常の最大値定理をそのまま差分の追加順へ適用することはできず、現状の上界は調和和。
`research/causal_fourier_coefficient_route.md` に正確な式と一次文献の適用範囲を記録した。
以上4本の新解析は独立レビュー済みで、親の再導出は `research/goal10_parent_review.md`。
版の結び付けは `evidence/goal10_reviewed_research.json`。

次は実容量の一様上界、制限した剰余類情報による非自明な比較、予算を複製しない
full-defect 表現、または実順序の Fourier 評価を進める。これらの補助結果と検証を
completion と扱わず、原 Q1 と最終 Lean 検証という同じ条件の下で継続する。

## 2026-09-05 22:20 JST の履歴


**原 Q1 の完全証明・完全反証、最終 Lean theorem は未達。Goal は active。**
前回の blocked 表示は今回の継続で再開され、実ツールで active を確認した。
親は `update_goal` を呼んでいない。数学上の障害を Goal の blocked 判定や completion
として扱っていない。根拠は `evidence/goal9_goal_state_observation.json`。

指定モデル・推論設定は変更していない。指定パック、MASTER、Downloads の C143 V2
bank と最新 follow-up の byte identity を確認した。以前と同じ C143 の巨大な pricing
replay は再実行しておらず、C139 台帳を現在地にしていない。
一次資料の記録は `evidence/goal9_primary_byte_identity.json`。

今回、実際の Sidon 条件から triple multisets の共通要素消去・台の非交差を導き、
実際の signed endpoint witnesses から最新二端点の反対側配置、厳密増加列の順位と
値による cutoff の同値を形式化した。新しい3モジュールの **22宣言**について、
対象 build・全名を明記した公理監査・import 環境の Lean checker がすべて実 exit 0。
根拠は `evidence/goal9_sidon_parent_binding.json` と
`evidence/goal9_ranked_parent_binding.json`。後処理の Python 読み戻しで保存件数を
419 と誤記した失敗は記録し、219 に直して読み戻した。Lean の失敗・再実行ではない。

検証済みの補助範囲は、従来103宣言と今回22宣言の **計125宣言**。6つの別々の
保存済み範囲であり、125宣言の一括監査ではない。全 multiset orbit の集計、
実 stage energy の恒等式、新しい全履歴評価、原 Q1 はまだ Lean で証明されていない。
旧 aggregate は変更していない。完成 release の clean build と最終 Q1 公理監査も未達。

解析では、将来の実ブロックに支払える対の正確な条件 `b<i<r` を取り出し、
その利用可能量を `(1+lambda)/8 * sum u_r DeltaY_r` で評価した。PSD 行列から
成分を削除する主張を使わず、同じ非負の物理予算に対する上界として証明した。
実際の span・穴・投影残差・価格差を残した完全な恒等式と、成分ごとの有限配分
最適値 Pi を構成した。`research/signed_output_energy_closure.md` にある。

さらに、全 triple fiber を使って、上のエネルギー上界と利用可能量の差そのものが
一つの固定 cap の下で発散すると証明した。最新端点が重複する群も含む。
したがって、エネルギー上界と需要の差を有界にする候補は使えない。
利用可能量だけから需要を引いた、より小さい残差については未解決である。
この後続結果は `research/signed_eligible_defect_frequency.md` に記録した。
元ノートの第二の有界差条件を否定した結果であり、原 Q1 の反証ではない。

他に、出力端点の順位差が短い対の総容量の可和性、source と output の分離による
厳密な不足量、小さい相対不足が4点集中と全6端点の相異を強制することを証明した。
その集中配置の衝突数を実 Sidon 性から数え、特定の対数閾値以下の weighted energy
を可和な費用として除去できた。5本の新解析ノートは全文の独立レビューと親の再導出を
通過した。親の検査は `research/goal9_parent_review.md`、全版の結び付けは
`evidence/goal9_reviewed_research.json`。

次の中心課題は、実際の利用可能量と Pi の差に残る未配分対・投影残差を評価し、
同じ固定 cap と原 Q1 の矛盾へつなげること。単なる有界差の証明だけで Q1 が閉じる
とも主張していない。これらの補助結果・検証・記録を completion とせず継続する。

## 2026-09-05 20:25 JST の履歴（今回の再開前）

**原 Q1 の完全証明・完全反証、最終 Lean theorem は引き続き未達。**
最終の `get_goal` を2回確認したところ、Goal の実状態は `blocked` だった。
このターンの親エージェントは `update_goal` を呼び出しておらず、原因・変更主体は未確認。
数学的な困難を理由に blocked と判定したものではない。自動継続にはユーザー側の
Goal 再開操作が必要で、現在のツールには active へ戻す操作がない。
根拠は `evidence/goal8_goal_state_observation.json`。以前の active 表記は、この最終確認で
訂正する。解析・Lean の検証結果と未解決判定は変更しない。

指定した GPT-6 Astra Ultra と推論設定は変更していない。指定パック、
`MASTER_PROMPT.md`、Downloads の C143 V2 bank の byte hash を再確認し、
最新 follow-up も実ファイルから確認した。C139 台帳を現在地としていない。
根拠は `evidence/goal8_primary_byte_identity.json`。

今回の主要な非形式の結果は、重複端点も正確に数えた
`research/signed_multiset_born_retirement.md` の段階別不等式
`R_j<=2B_j` である。退役 R は **出力時刻**、Born B は source 時刻で重み付けする。
全 labeled matching と automorphism の数え上げ、同じ差が二度現れる場合、
Born のみの残余を保持し、従来の反復端点の誤差を取り除いた。全文の独立レビューと
親の独立再導出を通過した。source 時刻へ退役の重みを移した不等式は別の主張であり、
実際の6点 Sidon 集合で反例がある。

この不等式から `E_N<=N Z_N+6B_(<=N)` が得られる。
`research/signed_born_quantitative_gain.md` と親の強化版の計算により、一つの固定 cap
の下で、永久に固定した source の重み付き Born 節約は発散する。新しい signed Abel
対角費用の上界は `2 zeta(2)-1`。ただし、この発散は同じ物理ラベル予算に残る
未使用分・幅・重なりと実需要の差を抑える証明ではない。

Lean では新しい `Q1/SignedCollision.lean` の **16宣言（2定義・14定理）**を実際に
検証した。対象モジュール build、公理監査、import 環境での `leanchecker` は全て exit 0。
公理は `propext`、`Classical.choice`、`Quot.sound` の範囲内。親も現在のソース・
実行前後記録・完全出力・生成物のハッシュを読み戻して確認した。
根拠は `evidence/goal8_signed_collision_parent_binding.json`。

さらに `Q1/SignedAbsoluteCollision.lean` の **5宣言（1定義・4定理）**も対象 build、
公理監査、import 環境での `leanchecker` を通過した。六つの実数交差積の絶対値を
直接評価する証明で、求める不等式を仮定していない。親の読み戻し記録は
`evidence/goal8_signed_absolute_collision_parent_binding.json`、独立レビューは
`research/signed_absolute_collision_review.md` にある。

これらは分散と衝突寄与の **代数部分**を形式化したもので、Sidon の全 multiset
partition と実畳み込みの恒等式は、後段の定理では明示した仮定として残る。
原 Q1 を仮定付きで解決したとは扱わない。従来の82宣言と新しい16宣言・5宣言は重複せず、
別々の保存済み検証範囲として合計103宣言。103宣言をまとめた再監査は未実行であり、
旧 aggregate `Q1.lean` とその監査ドライバも変更していない。
完成 release の全依存 clean 検証・最終 Q1 公理監査は未達。

`research/signed_output_clock_source.md` は、全重複を含めて
`Ret_abs_j<=2B_j` と `Born_abs_j<=3B_j` を証明する。これを使い、出力時刻の重みを
保つ一つの非負 PSD source を構成し、その費用を従来の Born 節約から賄えることを
導いた。実際の good half-block には逆対数規模の追加需要を支払える。
終端より後に現れる出力の費用、全 trace、行列質量、未使用成分を残した全文を親も
独立に確認した。ただし、得られたのは基準容量と需要の差の **下界**であり、Q1 に
必要な対向する上界ではない。

`research/signed_clock_commutator.md` は、任意の `gamma>1/2` に対して
`0<r-b<=b/(log b)^gamma` の配置で、出生・退役価格の交換誤差の絶対和が有限になる
ことを証明した。compatible 価格では cap 不要、直接の価格では一つの固定 cap を
使う。さらに誤差の正味の和を、実際の需要と重ならない終端の未使用容量へ対応させた。
独立レビュー済み。遠い時刻領域の一様上界は未達。

`research/signed_energy_two_sided.md` は、さらに下側の不等式
`-B_j/4<=R_j` を証明した。これにより、生の線形重みでの `E_N` は狭義に増加し、
`E_N-N Z_N` も単調増加する。重み付き Born と、対角を引いた Abel エネルギーを
上下から定数倍で比較できる。全文の独立レビュー済みで、この段階別定理は未 Lean。
従来の quantitative ノートにあった「E_n は単調とは限らない」という文は誤りだったため、
「その証明には単調性を要しない」へ訂正した。以前の式・定数・証明の結論は変更していない。

他の全文レビュー済みの結果は、永久 source の正確な質量・trace・実需要支払い、
半径切断で失う寄与を保持した threshold source、共通最大値の無制限容量が発散する
下界、定数と一次モーメントを同時に射影した需要である。
`research/goal8_parent_review.md` が親の監査と強化された定数を記録する。
二つの新しい固定例の厳密実行も成功したが、有限例として区別し、巨大な C143 pricing
を変更なく再実行したとは報告していない。
現行の解析ソース・レビュー・固定実行・Lean 検証・一次資料照合は
`evidence/goal8_reviewed_research.json` で版を結び付ける。

継続中の中心課題は、出生時刻と退役時刻の差による寄与を評価し、出力時刻を保つ
実需要と一つの物理予算を結びつけて、原 Q1 に必要な全段階の収支を閉じること。
これらの補助結果・検証・研究記録を completion としていない。

## 2026-09-05 18:18 JST の研究記録

**原 Q1 の完全証明・完全反証と、最終 Lean theorem は未達。Goal は active。**
指定モデル・推論設定を変更せず、C143 V2 と最新 follow-up を一次資料として維持した。
Lean の検証済み範囲は引き続き **82 宣言（定義を含む）**であり、今回の数学を
新しい Lean 宣言として数えていない。

今回は、正負対称な差分集合 `Fhat=F union(-F)` を使う経路で、一つの符号問題を
解決した。`signed_bank_born_positivity.md` は、固定した単調な奇関数を重みにすると、
**同時出生の source pair も含む Born 全和が、任意の非負出生時刻重みで非負**となる
ことを証明する。Schur 関係 `x+y=z` の全 source pair、同率の出生時刻、`x=y` を
漏れなく分けた証明で、独立監査を通過した。

この集合の将来需要では支持区間が `T=L+2H`、穴を除いた容量が `D=T-m` となる。
既存の good epoch では、符号付き一様重みと比較した個別の逆対数規模の改善が得られる。
一つの物理的な最大値にまとめた総予算の改善は、まだ証明していない。また、この集合の
同時出生対は後で退役し得るので、以前の正差分集合の Abel 対角公式を移植していない。

`signed_bank_envelope_geometry.md` は、その比較先も検査した。単純な符号関数を
係数1で使うと、正規化した物理核は元の正差分の一様核に厳密に一致する。指定の
全区間一次モーメント需要も `N>=8` では元の需要以下と証明した。この選択だけを
新しい Q1 証明と扱っていない。線形奇関数については物理幅 `[H,2H]` で残余核が
非正だが、実際の最大値がその幅だけで達成されるという定理はない。これも監査済み。

他の継続結果は以下の通り。

- `physical_allocation_shadow_slack.md`：実際の future block への配分では
  `rho^B-d=(E_z-LB)/(2q^2)>=0` が厳密に成り立ち、双対の moment 罰則はゼロ。
  基準の局所 Cauchy 余裕は残る。親が全式と正値性・退化条件を独立に確認した。
- `scalar_moment_physical_cone.md`：符号を選ぶ scalar と追加 moment を
  `t^2<=s<=ell` の同じ非負 PSD 行列族に統合し、一つの物理配分に対する双対と
  実 shadow の平方分解を導いた。独立監査済みで、全余裕を消す定理は未証明。
- `schur_clock_energy.md`：前回の core を有限費用で Schur の二つの対が揃う形に
  修正し、和を平方と実際の出生平均の補正に分けた。補正の現在の上界は
  `O(log T)` で必要な規模に届かない。全ての削除の費用も独立監査した。
- `completed_fiber_mean_route.md`：全 fiber 平均補正を平方と明示した端点項に
  再整理した。端点項の現在の上界は `52R^2` で、必要な全体の三次評価は未達。
  固定した一つの complete fiber の恒等式チェックは exit 0。実行前後ハッシュ・
  時刻・完全出力を記録し、親が読み戻した。一般の符号定理の代用にはしていない。

現行ソース、独立レビュー、固定一例の実行記録、Lean ソースの変更有無は
`evidence/goal7_reviewed_research.json` に対応づける。新しい中心課題は、非負 Born
定理を使える符号付き source の **同じ物理予算**と実需要を構成・比較すること。
既存 source へ戻るだけの選択、半径切断で失う対、支持幅・対角・重なりを全て保つ。
原 Q1 と最終 Lean 検証までの未達部分を、補助結果で置き換えていない。

## 2026-09-05 17:32 JST の研究記録

**原 Q1 は未解決。完全証明・完全反証・最終 Lean theorem は得られていない。**
Goal は active のままで、モデル・推論設定は変更していない。
最新の一次資料は引き続き Downloads の C143 V2 run と 2026-09-05 follow-up。
C139 を現在地に戻していない。

Lean は前節の **82 件の監査済み宣言**が現在の検証範囲である。この継続では
Lean ソースを変更せず、成功済み build・checker・巨大な有限 pricing を再実行して
いない。以下の新しい数学は非形式の証明と独立レビューであり、82 件へ追加した
Lean 宣言ではない。

- `prefix_scalar_gain_dichotomy.md`：古い実 prefix だけで scalar の符号と大きさを
  選び、一般の raw 歴史比較で `B^2/[2(q^2+RNq)]` の改善を得た。正値性の適用は
  `R>=1`、実際の次 block `m=N`、十分大きい extended good epochs に限定した。
  その条件が十分な頻度で起きることも、共有予算を超えることも未証明。
- `completed_fiber_gram_route.md`：同じ三点和の全 fiber を非負 Gram 項、循環項、
  平均補正に分け、全対角・反復点誤差を `17N^3` 以下にまとめた。二つの指定した
  complete fiber で恒等式の有理数検算が exit 0。今回は実行前後の source hash、
  時刻、stdout/stderr を実測記録している。一般の残余項の符号評価ではない。
  `completed_fiber_skew_reindex.md` は循環項の端点対応を明示したが、三次の下界は
  得ていない。主分解は独立監査、追加の再整理は親の独立再導出を通過した。
- `retirement_stage_injection.md`：退役とその注入先が同じ時刻・価格を持つことを
  証明し、automatic・固定点・遠い退役の注入差を有限費用にまとめた。残る近い
  注入差と未対応の出生寄与には、なお符号の評価が必要。
- `near_retirement_incidence.md` と `clock_core_localization.md`：出生時刻が近すぎる
  配置、古すぎる source/output、小さい出力差、端点重複の寄与を絶対可算和として
  除ける。Born 側と退役側の両方を実際の三つの時計で限定した。source 時刻と退役
  時刻の重みを交換していない。二本とも全式の独立監査を通過した。
  `three_clock_separation.md` はさらに、三つの出生時刻のどの二つが等しいか近い
  場合も、一様に有限の総費用として除いた。数値ラベルの反復 `x+x=2x` を別に
  数え、実際の最新出生時刻の価格を保った。親による独立再導出を通過した。
  `near_retirement_packing_limits.md` は実 star の packing と全 source dyad を保つ
  が、現在の評価は必要な逆対数の規模に届かない。その限界も親が確認した。
- `physical_envelope_allocation_dual.md`：複数 row の moment 改善を、一つの物理ラベル
  配分の有限 LP 双対として正確に記述した。最大値の同率 row、配分損失、実 shadow の
  余裕を保持し、実 future block による双対 witness も構成した。独立監査済み。
  この witness を固定 cap の仮定から排除する漸近定理は未証明。

各レビュー、現行 source hash、有限二例の実行記録、および形式検証の変更有無は
`evidence/goal6_reviewed_research.json` に束縛する。これは補助研究の記録であり、
完成した証明 release ではない。次の中心課題は、残る六端点の符号付き寄与を
必要な規模で評価し、それを同じ物理的予算の全余裕と結びつけること。

## 2026-09-05 16:40 JST の検証記録

Lean の現在地は **82 件の監査済み宣言（定義を含む）**。新しい
`Q1/MomentDemand.lean` は313行、28宣言である。保存された実行では
`lake build` が3089 jobsを通過し、明示的な公理監査と新モジュールの
`leanchecker` も exit 0。別担当が現在の14ソース・設定ファイル、ログ、
10個の `.olean`、検査器のハッシュを再照合した。公理は
`propext`、`Classical.choice`、`Quot.sound` の範囲内。
根拠は `lean/evidence/verification.json` と
`evidence/goal5_moment_parent_binding.json` にある。

新しい検査器実行は import 環境での当該モジュール再検査であり、現在の全依存を
空の環境から再検査した結果ではない。最終 Q1 宣言と完成 release の clean build
は未達。以前の日付の節にある54宣言は、その時点の履歴として残している。

数学の継続で確認した内容は次の通り。

- `future_moment_demand.md`：将来の実 block と中心化差ベクトルの一次モーメントから
  追加エネルギー `LB` を導いた。同じ全行列の raw demand は厳密に `lambda*LB/2`
  増える。対角費用を保持し、独立した予算を追加しない。その有限 container 版から
  複数 block の共有最大値までが今回の Lean 形式化範囲。穴を除いた最適分散と
  区間の三次閉形式は非形式のまま。
- `coherent_birth_linear_envelope.md`：二段先の幅を抑えられる good epoch でも
  逆対数の和が発散する。個別改善と一つの最大値の差には、基準の余裕、rowの重なり、
  spanの符号付き補正が残ることを厳密に記述した。これらを小さいと仮定していない。
- `birth_linear_born_term.md`：一定の終端 cap と分散を持つ実 Sidon 集合の有限族で、
  単調 plus scalar の歴史的な mass-only 比較が負になることを証明した。全履歴で
  共通の onset と good shape は不保持。この族は Q1 の反例でも、新moment需要を
  含む比較の反例でもない。
- `birth_linear_total_causal_sign.md`：全 causal quadratic 総和を、automatic な
  column 平方、全六端点三点和 fiber、絶対値 `12N^3` 以下の反復点補正に分解した。
  二つの固定例で direct enumeration と全fiberの集計が有理数で一致した。
  実行時のソース前後ハッシュは未記録であり、事後記録はその限界を明記している。
  実際の三点和等式を破る自由な gap vector は反例として採用していない。
- `causal_birth_energy_telescoping.md`：永久に固定した係数 `g` に対して
  `w_n=1/(q_n^2 H_n^2)` と置くと、対角費用の全和は `8*zeta(2)-10` 以下、
  終端エネルギーは4以下。固定 cap とgood epochから、非負の Abel 内部和が
  発散することを証明した。出生と退役を別の時刻で価格付けする恒等式を保った。
  同じ改善を実現する一つの PSD 行列も構成したが、その質量は `4 log N+O(1)`。
  有限 trace を有限の共有予算と取り違えていない。
- `late_retirement_tail.md`：任意の固定 `alpha>1/4` に対し、退役 rank が
  `r>=b(log b)^alpha` である pair の **退役時刻の重み**の絶対和は一様に有限。
  これは独立レビューを通過した。従って未評価の発散規模は近い出生・退役に
  限定できるが、その近い部分、出生時刻との交換項、物理的な余裕は未評価。
- `endpoint_batch_entropy_obstruction.md`：独立差ラベルモデルでは大きな Sidon
  出生 batch がほとんど確実に存在しないことを証明した。実際の相関した差集合へ
  移す定理はなく、確率的モデルの排除を原Q1へ昇格していない。

現在の全ソース対応は `evidence/goal5_reviewed_research.json`。指定パック内の
`MASTER_PROMPT.md` と作業コピー、および C143 V2 bank の byte hash が一致する
ことも再確認した（`evidence/goal5_primary_byte_recheck.json`）。過去の巨大な有限
pricing計算を再実行したとは報告しない。

次に必要なのは、全fiberの符号付き総和か近い出生・退役の項を、同じ物理的予算の
余裕と合わせて必要な規模で抑える証明である。補助定理の検証を完了条件にせず、
原 Q1 と最終 Lean 検証を目的とする Goal は active のまま維持する。

## 起点と保存方針

指定された Downloads の `ERDOS1191_Q1_LEAN4_CODEX_PACK.zip` をこのディレクトリへ展開し、`MASTER_PROMPT.md` と対象仕様を読み、最新 C143 V2 と 2026-09-05 follow-up を起点として実行した。元の Downloads run、canonical project、および古い台帳は変更していない。親のモデル・推論設定は変更していない。3 並列担当は明示的に `gpt-6-astra`、`ultra` を指定した。

現 bank の確認値：

- bytes: `144369995`
- SHA-256: `d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4`
- producer の実 canonicalization による payload SHA-256: `3961c6caa68c9d5dfbfbc0fdd2e433a1cf310618584ef617a892ce9b79a6725c`
- checkpoint と bank の対象集合一致：960 parents、1,890 children、961 endpoints、未処理 queue は空。

今回実行した内容は `evidence/current_input_identity.json` にある。90,600,510 checks の full-pricing replay は、今回同一性を確認した入力・source に結び付いた既存の exit 0 記録を再利用した。今回その 90 million replay を再実行したとは主張しない。bank の照合、Python replay、Lean の証明は異なる検証境界である。

## 現在の依存関係

| ノード | 実際の状態 | 根拠・残る範囲 |
|---|---|---|
| 正の整数、無限性、反復和を含む Sidon、実 cutoff の liminf | Lean に透明な定義を固定 | `lean/Q1/Target.lean`。liminf は EReal で取り、実数の条件付き完備性による意味変更を避けた |
| 原 liminf ⇔ 整数 squared ε/M 条件 | Lean 検証済み | `original_iff_integerSquared`。floor、sqrt、ε/2 の損失を含む |
| 原 Q1 の否定 ⇔ 実際の無限 Sidon 集合の eventual positive lower bound | Lean 検証済み | `not_q1_iff`。その集合の存在を証明したものではない |
| admissible input の存在 | Lean 検証済み | `{3^n}` を使う `admissible_exists`。Q1 の普遍結論とは別 |
| Sidon の和定義 ⇔ 正差の端点一意性 | Lean 検証済み | `sidon_iff_positiveDifferenceUnique`。反復和も含む元定義から証明 |
| 実際の有限 pair 集合に対する任意非負重みの差ラベル予算 | Lean 検証済み | `weighted_positivePairs_le_labels`。同じ pair の窓をまたぐ重複使用は別途排除が必要 |
| C143 固定 history の全位相・weight-rectangle 結果 | 現データに束縛された外部計算証拠 | `research/c143_local_theorem.md`。全 history / 全 rank の定理ではない |
| direct 行列の任意 rank の moment 展開 | Lean 検証済み | `direct_point_quadratic_moments` |
| 2 jump / 3 jump の代数評価 | Lean 検証済み | `lean/Q1/HaarShape.lean`。実 Haar 状態の幾何分類は Lean 化していない |
| 実 Haar 状態の分類、負部分の一様可和補正、積分公式 | 非形式の手証明・独立レビュー済み | `research/c143_lift.md` と `research/moment_independent_review.md`。積分の Lean 証明はない |
| 補正後の任意ベクトル PSD | **偽** | `e=3, q=(3,2,1,0)`。path 補正後 `−1/18` は Lean 検証済み |
| cap を使わず、Sidon 性と補正可和性だけから全塔上限を得る推論 | **偽** | 独立レビューの実無限 Sidon 構成。critical cap を満たさず、Q1 の反例ではない |
| critical cap と全 prefix の対数階乗下界だけから全塔上限を得る推論 | **偽** | `research/log_energy_route.md` の固定 onset 非 Sidon モデル。`research/log_energy_review.md` が係数・特異な極限・量化を独立に確認 |
| fixed onset critical cap と差の一意性を同時に使う、対向する全塔積分上限 | **未証明** | 正の carrier の存在だけでは上限を得られない |
| 同一の旧差集合に対する複数 future block の累積予算 | 核心の (9), (13) は Lean 検証済み | `shadow_interval_capacity`、`shared_interval_demand_budget`。全区間が同じ実 Sidon history に属する条件、対角項、区間長を保持。旧三角形の (15) は非形式のまま |
| 合同類の entropy deficit から零を導く定量的十分条件 | 非形式の証明・相互レビュー済み | `research/residue_route.md`。十分な deficit を全履歴から強制する部分は未証明 |
| 単一 prefix または開始 rank が動く有限履歴だけから十分な deficit を強制する推論 | **偽** | Bose–Chowla 集合の実 Sidon prefixes。互換 dyadic depth が発散しても fixed-onset 全履歴の反例にはならない |
| 増大する旧 prefix の kernel を一つの物理差へ束ねた最大値上界 | Lean 検証済み | `growing_prefix_interval_envelope`。実 interval demand、旧使用 mask、span mask、有限 max を全て定義通り扱う |
| 同じ物理差 source の used/unused/cross/slack 分解 | Lean 検証済み | `actual_blocks_envelope_accounting`。有限 support との intersection を明示 |
| 実際の中心化一次モーメントによる追加需要と、一つの共有最大値 | Lean 検証済み | `shared_momentDemand_envelope`。全行列と対角費用を保持し、LB支払を仮定しない。全履歴の正のgapは未証明 |
| 原 Q1 の完全証明または完全反証 | **未達** | `Q1` または `¬Q1` を証明する最終 Lean 宣言はない |

## 今回得た全 rank の橋渡し

整数に限らず任意の実数 ruler `b_0<…<b_e`、`e≥3` に対して、raw Haar 状態を

`q_i(x,T)=1_[b_i,b_i+T)(x)−1_[b_i+T,b_i+2T)(x)`

とする。C143 と同じ direct matrix を `M_e=DᵀB_eD` とし、`B_ij=−(i−j)²/(8e²)` for `|i−j|≥2`、それ以外を 0 とする。

任意の実ベクトルについて、`δ_i=q_i−q_(i+1)`、`s_j=Σ i^jδ_i` と置くと

`4e² qᵀM_eq = s_1²−s_0s_2+Σ δ_iδ_(i+1)`。

この代数恒等式は Lean が検証した。実 Haar 状態は rank 順に `0,−1,+1,0` の連続ブロックをなす。その分類により

`P_e(x,T)=qᵀM_eq + e^−2 Σ_(r=1)^(e−2)1_{q_r=−1,q_(r+1)=+1} ≥0`。

各隣接 pair の反対符号の重なりを全 `x,T` で積分すると、gap の長さに依存せず厳密に `2 log 2` となる。従って

`∫∫ P_e dx dT/T² = 2W_e + 2 log 2 (e−2)/e²`。

この補正は全 dyadic rank で一様可和であり、critical cap も整数の最小 gap も不要である。ただしこれは状態に依存する非線形補正であり、任意 PSD 行列の source/owner 規則をそのまま使う根拠にはならない。全 rank の分類と積分公式は現状では非形式の証明である。

別の全距離 moment 行列 `Mtilde` も実状態で非負になるが、下限 cutoff を外すと内部単独 mark の寄与が `T→0` で対数発散する。したがってその積分公式には必ず `T≥1/2` が付く。この注意は上の transition carrier には不要である。

## Lean 検証の再現と範囲

`lean/README.md`、`lean/FORMULATION_BRIDGE.md` と `lean/evidence/verification.json` が正確な再現資料である。Lean 4.33.0 と mathlib commit `db584cd6d46c92f209a44c0f1c829460d327499d` を固定した。

現在記録済みの default build は Target、Equivalence、Nonvacuity、DirectMoment、HaarShape、DifferenceLabels、SharedDifferenceBudget、PhysicalLabelEnvelope、AxiomAudit を実際に含む。ビルド、公理監査、各 kernel check は実行ログと exit code を保存している。54 の監査対象宣言の依存公理は `propext`、`Classical.choice`、`Quot.sound` のみである。

`leanchecker --fresh Q1` は DirectMoment/HaarShape 追加前の snapshot に対して実行し、追加分はそれぞれ `--fresh Q1.DirectMoment` と `--fresh Q1.HaarShape` で全依存を検証した。これらを最新 Q1 に対する一本の clean release 検証と呼ばない。独立実装の checker と完成 release ZIP からの clean rebuild は未実施であり、Q1 の最終宣言もない。

DifferenceLabels に対しては `lake env leanchecker Q1.DifferenceLabels` が exit 0 で終了した。これは imported environment を使う module replay であり、`--fresh` ではない。対応する source hashes とログは `lean/evidence/verification.json` に保存した。

SharedDifferenceBudget に対しても `lake build`、37 宣言の明示公理監査、`lake env leanchecker Q1.SharedDifferenceBudget` が exit 0。親も最終宣言の全仮定・結論、保存ログ、source SHA-256 `ef08da0b99b7251b26321c6d7ffe36fe10e8d447c662602d1c016e3ad70d5257` を確認した。この replay も既存 imports 上の検証である。区間定理の `H` は有限集合 `F` 全体の上界であり、非零重みだけの support 上界に読み替えるなら `F` の取り方を合わせる必要がある。

その後 PhysicalLabelEnvelope を含む build、54 宣言の明示監査、`lake env leanchecker Q1.PhysicalLabelEnvelope` も exit 0。親は module 本文の全宣言と証明、保存 build log、13 source/config の全 SHA-256 一致を独立に確認した。新 module の SHA-256 は `f831816b0eb28e9d7270cbce45c6f8c9ef5c1a82f78355600c92d99611fe03cd`。この replay も imports-based であり、全 release の clean rebuild と呼ばない。有限の対角項付き需要を既に証明した定理から導くため、需要支払いを隠れた仮定に置き換えていない。

## Goal 継続中の追加研究

原 Q1 の証明・反証と最終 Lean clean build、公理監査を completion 条件とする Goal は active のままである。以下は数学的進展であり completion ではない。元の ZIP は初回 snapshot のため、これらの追加内容を含む最新 release と扱わない。

`research/growing_label_budget.md` は関係の初出、将来の第一端点、第二端点を区別した保存則を示す。各関係が可和な charge を持っていても、全関係の charge の和は有限とは限らない。さらに、実際に将来の差として全て使われる無限 Sidon 例でも総 charge が発散する。この例は critical cap を満たさない。任意の非負旧差重みについても、記載した粗い cap 下界と raw pair budget だけの機構では矛盾を得られない。

新しい選択問題は同ファイル (26)–(29) にある。各 shell の kernel をまず同じ整数差 `t` にまとめ、shell 間では和でなく最大値を取ることで、実際の差ラベルを一度だけ課金する上界を得る。全 old/cross/unused 項と envelope の余剰も同じ source で計上する。一つの固定 `C,n_0` を満たす全履歴から、この上界より必要量が大きくなることは未証明であり、次の中心課題である。

`research/nested_fourier_route.md` は全 prefix の厳密な四次モーメント、共分散、および対数重み付き二次量の almost-everywhere 極限を証明し、独立レビューを受けた。その極限は critical cap と矛盾せず、旧差多項式を使う混合積分は上の共通予算と一致する。これを別の全塔上界や Q1 の証明に読み替えない。

`research/persistent_inverse_route.md` は永久的な禁止集合 `a_p+ΔP_p`、一つの候補整数の全証人がなす Schur forest、fixed cap を使う証人の活動期間、最初の証人を保持した再利用量を証明した。親は forest の対角項、計数・条件付き entropy、packing の必要条件と実無限の span-free 反例を確認した。shadow の entropy から集合 A の合同類 entropy への移送や、異なる候補整数の森を結合した損失は未証明である。

2026-09-05 09:08 JST までに、以下の非形式の数学的結果を保存・相互レビューした。これらを Lean 検証済みの54宣言へ加えてはいない。

- `research/envelope_selection_route.md` §§1–12：任意の productive weight の旧 mask 損失、PSD 生存 mask の実 Sidon 反例、対角修復費用、単一 kernel の全時間係数最適化、localized carrier の past/future 定数の相補関係を証明した。
- `research/fixed_width_bank_density.md`：親が全証明を執筆し、global 担当が独立レビューした。同じ fixed-onset cap から、`p=floor(D^theta)`、`theta` が `(1/2,1)` の compact 区間を動く場合に、`F_p(D)=Delta P_p cap [1,D]` が一定割合の短差を持ち、その Schur count が `Omega(D^2)` となることを一様に導出した。
- `research/nested_small_difference_bank.md` と `research/envelope_selection_route.md` §§13–14：実 endpoint による差の出生を保持した厳密な相関・retirement 保存則を証明した。単位 current bank の歴史全体の最大値は `C=binom(q,2)-T/2-Z/2`。fixed cap による損失の少なくとも半分が実際の最大値にも残る。cap なしでは半分が漸近最良となる実 Sidon 履歴も構成した。
- `research/matrix_transport_route.md` と `research/centered_spectral_gain.md`：affine の `log(p)^(-5)` 保証を、量子幅と Fourier 局在により `1/log(p)` へ改善した。全 old bank に対し、四つの非負 scalar carrier の一つが全 near-shell range で対角費用込みの単独 row 改善を達成する。親は全文・全定数を独立に確認した。dyadic 下限級数は発散するが、同じ物理 source 上の全履歴への累積移送を証明したものではない。
- 上の二 carrier の実34点 Sidon 例を、各再現 script が全て整数・Fraction で検証し exit 0。親は source と log の SHA-256 が保存 provenance と一致することを確認した。数値例から漸近定理を推論してはいない。
- `research/compatible_construction_route.md`：compatible field tower による実無限整数 Sidon 構成について、途中高さの厳密計数で critical cap の失敗を証明した。圧縮された7進版は `9+19=14+14` で Sidon 性そのものが失敗する。別構成全ての不可能性や Q1 反証とはしない。
- `research/short_three_sum_flux.md`：Bose–Chowla の切断平均から、ほぼ全ての短差と `Omega(D^2)` の非自明 birth flux を持つ実有限例を証明した。その moving onset は必要な全 past range を覆わず、さらに次の同数点を固定 terminal critical cap 内へ延長できない。Fejer 重み付きの bank Fourier 正性も厳密に導出した。
- `research/cohort_fourier_constraints.md`：親が rank cut を跨ぐ全 short edge の総量 `<=sqrt(2)D^(3/2)` を証明し、適切な境界を選ぶことで各 birth cohort の Fourier 正性を極限へ移した。rank marginal の continuity 点を使い、少量の rank 移動から少量の label 変更を無断で推論しない。global 担当が全文を独立レビューした。

`research/birth_profile_relaxation.md` も全文レビューした。明示的な非零 density profile が、現在の fixed-width の主要な birth flux・historical envelope・cohort Fourier 正性を同時に満たす。これは実 endpoint を構成したものではない。そのため、これらの制約だけを再び並べても Q1 の閉鎖にはならない。

上記の独立作業は、その後に保存された本文と証明を読んでレビューした。
担当設定は全て GPT-6 Astra Ultra のままである。現在の数学的義務は、下記の
固定係数を持つ線形 carrier と、その実 endpoint による退役輸送である。
変更のない C143 full replay や54宣言の検証は再実行していない。

## 2026-09-05 10:18 JST の継続研究

以下は新しく証明・相互レビューした非形式の結果である。Q1 の最終定理や
Lean 検証済み宣言へ追加したものではない。Goal は active、Q1 は未解決。

- `research/birth_centered_fourier_carrier.md` と
  `research/birth_centered_transport.md`：各実出生 class の和をゼロに保つ
  Fourier carrier を構成し、全 prefix の質量誤差を除去した。終端の
  `Omega(q^2/log p)` 利得に加え、因果的 cross energy にも同じ規模の
  正の周波数帯があることを証明した。外側の周波数積分は符号付きで残る。
  明示 sinc-squared 位相平均でも終端下界は保持できる。
- 同 transport ノート：equal-three-sum の異なる三点表現は matching をなす。
  six-distinct 成分の完全分解と反復添字の `O(p^3)` 誤差を証明した。
  選ばれた位相の厳密な仮説下でも個別 fibre は負になり得る実16点例を示した。
  個別の符号から全体の符号は推論しない。
- 同 transport ノート §§11–12：二周波数の対称性から、段階ごとに適合させた
  位相重みでは cross energy が Hilbert–Schmidt ノルムの二乗となる恒等式を
  得た。しかし Sidon 部分集合の多項式位相重みとその確率混合には
  `|X|<=q^(3/2)/2`、`E<=2pq` の上界があり、正規化後に必要な規模を失う。
- `research/weighted_birth_envelope.md`：固定した非負 scalar 分解は、各物理差の
  最後の eligible 時刻を共有するため、歴史全体の最大値と正確に交換できる。
  capacity だけの改善と capacity-minus-demand の改善は対角費用の分だけ異なる。
- `research/born_dead_spectral_route.md`：全32点に強い有限 prefix cap を持つ実
  Sidon history で、119個の正の主小行列式を厳密検証した。終端 gap が正でも
  historical gap が負となり、当該16点時点では全ての centered PSD 方向が
  historical gap 改善に失敗する。十分大きい rank の漸近定理の反例とはしない。
- `research/birth_centered_retirement_operator.md`：明示的な実整数 Sidon 集合族で
  `diam P<=41N^2` かつ `lambda_max(C Rret C)>=N^2/2^37` を解析的に証明した。
  よって任意の有限 Sidon 集合に対する小さい retirement operator 上界は偽。
  この族は全初期 rank を通じた一つの fixed-onset cap を満たさない。
- `research/coherent_birth_field.md`：一つの整数 birth rank を全幅で共有する
  抽象モデルを構成し、出生時刻の tie を含めて主な密度・Schur・Fourier 条件を
  満たすことを証明した。全差の個数と endpoint incidence は満たさず、Sidon
  集合ではない。これを反証として昇格しない。
- `research/recursive_difference_tower.md` と
  `research/two_sided_sidon_folding.md`：全出生 bank が旧差集合を正確に再現する
  recurrence は、既知の再構成定理を使うと7点以降で入れ子の整数 ruler に戻る。
  両方向への延長を正整数 Sidon 集合へ写す folding と、厳密な直径増分も証明。
  再構成は実読した Ranieri et al. の Theorem 1 に依存し、2007年原著全文は
  未取得、当該定理は未 Lean。critical-cap recurrence 自体は未構成。
- `research/cooperative_smoothing_transport.md`：一次論文の協調 coverage を共有の
  差ラベル予算へ接続した。coverage の改善と cross energy の結合不等式が必要。
  出力を平滑化して正の周波数帯だけを残す操作は物理的係数を変えるため、
  その費用を消去できない。

今回の主要な新しい全履歴の橋渡しは、次の二つである。

1. `research/dyadic_good_epochs.md`：`h(n)=a_n-a_1` とする。一つの固定 cap と
   正差一意性から、`p=2^k` について `h(p)>=2h(p/2)` かつ
   `h(2p)<=8h(p)` を満たす good epoch の間隔は `O(log k)`。
   さらに `sum_(good k<=K)1/k >= (1/4)log log K-O(1)` を証明した。
2. `research/birth_linear_good_epoch.md`：終端 `N=2p`、`H=h(N)` に対して
   `z_(a_j-a_i)=(mean(a_1,...,a_(j-1))-a_i)/H` と置く。この係数は各出生 class
   で中心化され、正規化前の値は履歴を延ばしても変わらない。good epoch では
   `S=sum z^2>=q/8192`。厳密な一次モーメント `mu_1=HS` と整数区間の
   Cauchy 不等式から `E>=3N^2 S^2/(2H)` を得た。従って個別 row の正規化
   利得は `3/(2^31 C log(2N))-(R_0+1)/(8(N-1))` 以上。
   good epoch 上のこれらの下界の和は発散する。

親も両証明を全文読解して定数・端点・固定 onset・反復和を確認した。
原 Q1 に必要なのは、個別 row 下界の発散を、同じ物理 source を一度だけ使う
全履歴の収支へ移す証明である。その加算を仮定として導入してはいない。

`research/retirement_shadow_threshold.md` は、その線形 carrier の各畳み込み位置で
実際の退役 graph を完全に記述した。端点交換が involution をなし、対応する
graph は threshold graph となる。線形係数の交換差は prefix 平均の差である。
符号付きの部分和、固定点、unpaired 項を残した恒等式を得て、独立担当も支持した。
これらの恒等式を使った必要な全履歴上界は未証明である。

`research/retirement_shadow_review.md` も親が全文確認した。orbit 二乗和と固定点の
補正は `O(N^3)` に収まり、主な未評価量は unpaired 成分と符号付き部分和の結合に
絞られた。さらに `u_t=1+t z`、`0<=t<=1` について、退役 pair から born pair への
大域的な単射と重みの非減少性を証明した。この scalar carrier 自身の使用済み
mask は少なくとも半分が歴史予算へ残る。ただし基準 `J` に対する gap 改善は
厳密に `t B_lin+t^2(X_z-mS/2)` であり、`B_lin` の符号を仮定していない。
二つの scalar sign を平均するとこの単射の単調性を両方へ適用できなくなる。
この線形項と結合補正を扱うことが、次の具体的な数学的義務である。

Lean は引き続き54宣言の保存済み検証が現在地であり、この節の非形式の結果を
Lean が検証したとは報告しない。原 Q1 の最終宣言、完成 release の clean build、
最終公理監査という completion gate は満たされていない。

## 研究ソースと次の数学的義務

Exa は実インターフェースに `additionalQueries` がなかったため、意味を変えた query を別呼び出しで実行した。成功した 2 呼び出しはいずれも `numResults=100` を要求し、返却された title entries は各 100 件だった。失敗した追加 query は成功数へ入れていない。取得内容は `evidence/exa_search_*.json` に保存した。

O'Bryant I の [arXiv:2606.28651v3](https://arxiv.org/html/2606.28651v3)、Táfula の [arXiv:2607.20753v1](https://arxiv.org/html/2607.20753v1) の一次本文を調べた。確認した定理の正の定数上界や発散する比を仮定した結論は、原 Q1 のゼロ liminf を与えない。全世界の最新結果の不存在を証明した、という主張ではない。

次の義務は、固定した `C,m_0` から始まる全 finite capped Sidon tower を対象に、同じ物理 source で全 rank の正の carrier を支払う対向不等式を導くことである。`a_m≤Cm²log(2m)` は補正の可和性以外に本質的に使う必要がある。正差の一意性を単調差 kernel の平均へ落とすだけでは足りないことは `research/global_route.md` が示している。この未証明の義務を仮定に加えて Q1 を Lean で証明することは行っていない。

追加で、正差の対数和 `L_n=Σ_(i<j<n)log(a_j−a_i)` と `E_n=L_n/n²−log n` を使う全 old/new/cross 分割を計算した。`research/log_energy_route.md` の恒等式は Wave 項を対向する符号で含むが、これも Q1 を閉じない。差の一意性を全 prefix の `L_n≥log((n(n−1)/2)!)` だけへ置き換えると、固定 onset の critical cap とその下界を両方満たしながら `W_n` が正の定数へ収束する非 Sidon 整数モデルが存在する。モデルは各 3 点 block に明示的な等差数列を持たせており、smooth sequence の Sidon 性を未証明のまま断定するものではない。したがって追加の算術評価は、同じ全体 Sidon history の実際の差ラベルを保持する必要がある。

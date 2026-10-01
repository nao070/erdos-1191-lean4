# エグゼクティブ監査

## 総合判定

提示された批判の中心は **概ね妥当**です。ただし、「16時間がすべて無価値」「テストは何も保証しない」「Lean が無いから全チェーンの正しさはほぼゼロ」とまで言うと過剰です。

最も正確な要約は次です。

> 主ボトルネックの説明は Wave 13 で循環していたと判明した。一方、循環を発見した証明、有限反例、恒等式、手法 no-go、局所 promotion/rebate は独立の研究資産として残る。主線は止めて再設計すべきだが、成果物全体を破棄すべきではない。

## 1. 批判が正しい点

### 1.1 P17/P18 の位置づけは修正必須

Wave 13 は、eventual critical cap

`a_n <= C n^2 log(2n)`

を満たす無限 Golomb branch が仮に存在すれば、`Y_m` と `Z_m` に各 dyadic epoch で `Omega_C(1/log m)` の正の下界が生じるため、

`sum Y_m = o(log J)` および `sum Z_m = o(log J)`

は成立できない、としています。Question 1 が真なら branch class が空になるため、これらの universal statement は空虚に真です。逆向きは harmonic lower bound による矛盾です。よって universal P17/P18 は Question 1 と同値です。

これは「本丸を小さな補題へ落とした」ことではありません。**本丸を別の言葉で正確に再表現した**ものです。

### 1.2 最新の入口文書が古い

`00_START_HERE_PROMPT.txt` と `HANDOFF_MANIFEST.md` は Wave 12 / P18 を次の十分条件として扱います。一方 `1191_MASTER_STATUS.md` と `proof_obligations.md` には Wave 13 の同値性再分類が追記されています。次の Codex がトップレベルだけ読むと、既に撤回された主線を再開します。

### 1.3 「275 tests 合格」の適用範囲がずれている

275 tests / 54 subtests と ZIP 展開後の完全再検査は、Wave 12 の封印点についての記録です。現在の作業木には Wave 13–15 が追加され、マニフェストにないファイルと checksum mismatch が存在します。したがって、その数値を Wave 13–15 の全主張へ拡張してはいけません。

### 1.4 Wave 15 は証拠階層が一段低い

Wave 15 本文は adjacent-epoch allocation と horizon obstruction を主張し、有限校正表を掲載しています。しかし、本文が言及する deterministic Wave 15 probe、test、certificate は ZIP 内にありません。本文の数式は方向として整合的に見えますが、Wave 13/14 と同じ executable evidence を持ちません。

### 1.5 インフラ費用は増加しすぎている

全過去 Wave の certificate を毎回再生成する設計は、探索中の高速反証・定理発見より release engineering を優先します。再現性は必要ですが、探索中の fast tier と、節目だけの full release tier を分けるべきです。

## 2. 批判を修正すべき点

### 2.1 「16時間、円を描いただけ」は半分だけ正しい

主線については正しいです。しかし次は実成果です。

- P17/P18 の同値性と量化の明示
- new-birth harmonic floor
- terminal renewal tail を捨てられないこと
- Wave 14 の rank promotion と legal rebate
- Wave 15 の adjacent-epoch reuse の候補証明と horizon obstruction
- 複数の universal candidate を有限反例で棄却
- 二重課金・同一 pair の定数多重割当の障害

したがって「主線の進捗は循環」「副産物は有用」と分けるのが正確です。

### 2.2 `O_C(J log J)` と `o(log J)` の差を「実値で J 倍」と断定しない

これは **現在証明できる上界の次数差**です。比として概ね `J` の隔たりですが、実際の残差が常に `J` 倍大きいと測定したわけではありません。「必要な次数改善が一段ではなく大幅」と表現してください。

### 2.3 テストは「中身を一切保証しない」わけではない

テストと certificate は次を保証できます。

- 有限恒等式の独立再計算
- 列挙範囲での反例・最小例
- exact rational arithmetic の一致
- 既知の符号・添字・係数の回帰防止
- serialization / hash /再現性

保証できないのは、自然言語証明の全量化、有限から無限への推論、文献上の新規性、未テストの補題、自己生成 oracle の独立性です。

### 2.4 Lean は重要だが、欠けた大域定理を作り出さない

Lean 化の優先順位は高いです。ただし全 12 Wave を丸ごと形式化すると、再びインフラが主役になります。まず、結論を支える小さな proof kernel のみを形式化します。

1. Question 1 と eventual critical cap 非存在の同値性
2. Sidon/Golomb と contiguous difference uniqueness
3. Abel/telescope の正確な有限恒等式
4. Wave 11 の三角床・係数分解
5. Wave 13 の harmonic lower bound と P17/P18 同値性

これで「何が確立済みで、どこから完全に open か」が固定できます。

### 2.5 6.5% をこの証明チェーンの確率へ直接掛けない

Aletheia の大規模評価は、LLM が問題の意図をすり替える危険の強い証拠です。しかし、別モデル・別 scaffold・別問題群の集計値です。Wave 1–15 の各補題の独立正答確率として使うことはできません。

### 2.6 「完全証明確率 1% 未満」は測定値ではない

現行ループのまま短時間で完全証明へ到達する見込みが低い、という方向判断は妥当です。ただし厳密な 1% は校正できません。本パックでは確率ではなく、証拠ゲートと停止条件で管理します。

### 2.7 OpenAI の `$2000` 例の読み方

OpenAI の 2026-08-01 公開文は、**10件全体**の solution-finding token cost が Sol API rates で roughly `$2000` と述べています。1問ごとに `$2000` 未満という意味でも、研究開発・人間監査・形式化を含む総費用という意味でもありません。

### 2.8 公開先についての断定を避ける

`erdosproblems.com` に no-go を共有する提案は良いですが、Bloom、Tao、van Doorn が当該コメントを必ず読むという証拠はありません。投稿前に人間数学者の独立監査と新規性確認を入れます。

## 3. 現在の方向性はこのままでよいか

**いいえ。Wave 16 を同じ方式で開始するのは推奨しません。**

ただし、以下は維持します。

- Wave 12 の封印 checkpoint
- Wave 13 の同値性・harmonic obstruction
- Wave 14 の promotion/rebate
- Wave 15 の局所候補を「未独立検証」として保存
- no-go ledger と有限反例

変更点は次です。

1. Wave 番号を一旦凍結
2. 最新作業木を `UNSEALED` と明記
3. claim-evidence registry を作る
4. 小さな Lean kernel を先に作る
5. P17/P18 を「次の補題」から外す
6. terminal potential / disjoint premium / 新しい energy-entropy-martingale / Q2 construction を独立ルートとして競わせる
7. 2回連続で次数改善も proof obligation closure もなければ、そのルートを停止

## 4. 最終評価

- 批判の中心: 妥当
- 「全成果が無価値」: 不当
- 現行 Wave ループ継続: 不適切
- 研究資産保存: 必須
- Lean proof kernel: 次の優先事項
- 完全証明への次手: 残差の別記法ではなく、terminal horizon を閉じる新しい大域機構、または全く別の証明アーキテクチャ

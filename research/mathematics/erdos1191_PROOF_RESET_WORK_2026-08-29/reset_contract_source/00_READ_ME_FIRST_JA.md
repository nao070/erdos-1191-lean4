# Erdős Problem #1191 — Codex 完全証明リセットパック

作成日: 2026-08-29 (Asia/Tokyo)

## 目的

このパックは、既存の `mathematics.zip` を捨てずに、しかし未封印の Wave 13–15 を「すでに検証済み」と誤認せず、Codex の研究を **完全証明または完全反証**へ戻すための監査・開始契約です。

## Codex へ渡すもの

1. 元の `mathematics.zip`
2. このリセットパックの ZIP
3. `02_CODEX_MASTER_PROMPT_EN.txt` の全文（英語版を推奨）

日本語で開始したい場合は `03_CODEX_MASTER_PROMPT_JA.txt` を使用してください。

## 最重要判断

- Wave 13 の「P17/P18 は Question 1 と同値」という再分類は、量化を含めて妥当な可能性が高く、主線の修正として採用すべきです。
- したがって P17/P18 を「本丸より前の小さな補題」として続ける設計は停止します。
- Wave 13/14 の有限恒等式・下界・局所 promotion/rebate は保存します。
- Wave 15 は本文しかなく、本文が言及する probe/test/certificate が同梱されていません。独立検証までは `HUMAN_PROOF_PENDING_AUDIT` とします。
- 現在の作業木は Wave 12 の封印後に変更されており、最新マニフェスト検証に失敗します。これを「数学が偽」とは解釈しませんが、「再現可能な最新リリース」とも呼べません。

## 読む順番

1. `01_EXECUTIVE_AUDIT_JA.md`
2. `14_DECISION_AND_NEXT_ACTION.md`
3. `02_CODEX_MASTER_PROMPT_EN.txt`
4. `04_PROOF_OBLIGATION_DAG.md`
5. `06_FAILURE_MODES_AND_STOP_RULES.md`
6. `07_LEAN_PROOF_KERNEL_PLAN.md`
7. `10_PACKAGE_INTEGRITY_AUDIT.md`
8. `08_LITERATURE_AUDIT.md`
9. `12_VERIFICATION_PROTOCOL.md`

## このパックが保証しないこと

- Erdős #1191 の解決
- Wave 1–15 の全数学の正しさ
- 未実行の全 pytest / 全 certificate 再生成
- 文献検索の完全性
- 賞金請求可能性

このパックが行うのは、現状の証拠レベルを分離し、循環・二重課金・有限から無限への飛躍・封印範囲の誤表示を防ぐことです。

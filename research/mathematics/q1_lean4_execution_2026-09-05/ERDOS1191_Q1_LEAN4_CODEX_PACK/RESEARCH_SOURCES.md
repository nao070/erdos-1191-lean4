# 出典・検索記録・確認範囲

確認日：2026-09-05（Asia/Tokyo）。検索結果と資料の内容、今回実行した検査、Codexに要求する将来の検証を区別します。

## S1 — Q1の命題

T. F. Bloom, Erdős Problem #1191.
https://www.erdosproblems.com/1191
https://www.erdosproblems.com/history/1191

問題ページの検索取得内容で第1問のliminf・Sidon集合・対数因子を確認しました。通常のページopenはこの環境で403になる場合があり、検索取得とExaの取得を利用しています。ページのOPEN表示はサイトの記録であり、不可能性の証明でも網羅的な文献調査の代わりでもありません。原文献の参照は同ページの [Er80,p.98] と [HaRo66] を起点に、実際に使う定理の本文を取得して確認します。このパックは未取得の原論文を全文確認したとは主張しません。

## S2 — Leanの公理

The Lean Language Reference, Axioms.
https://lean-lang.org/doc/reference/latest/Axioms/

公理依存を検査する `#print axioms` と、通常の数学的基礎である `propext`、`Classical.choice`、`Quot.sound` を確認する起点です。`sorryAx` やコンパイラ信頼を表す仕組みは別に扱います。具体的挙動は固定したLeanバージョンで確認します。

## S3 — Leanの証明検証

The Lean Language Reference, Validating a Lean Proof.
https://lean-lang.org/doc/reference/latest/ValidatingProofs/

命題の意味と証明受理を別々に確認する必要性、依存関係の監査、最終moduleを含むbuild、`lean4checker --fresh`、独立したchallengeとの比較を行う追加検証を参照しました。緑表示やbuild終了コードだけに成功条件を縮めません。追加検証器を未実行なのに実行済みと扱いません。

## S4 — Exa Search API

Exa, Search reference.
https://exa.ai/docs/reference/search

確認した公開仕様では `numResults` の上限は100。`additionalQueries` は1–10件の文字列配列で、deep-search系のtypeで使用します。実行時にもインストール済みインターフェースのschemaを確認します。

今回の接続済みExa検索は、各呼出しに `numResults: 100` を指定して実行しました。ただし公開されたMCP関数schemaは `query` と `numResults` のみで、`additionalQueries` と `type` を引数として渡せませんでした。そのため、Q1の原命題・数学文献・Lean形式化・公式モデルガイド・Exa仕様を追加の独立検索へ展開しました。**文字通りの `additionalQueries` 引数をMCPへ送信したとは主張しません。100件が実際に返ったとも主張しません。**

`SEARCH_PLAN.json` に、対応するAPIで直接送信できるbodyと、MCP用の展開形式を同梱しています。これは次回の再現・追加探索用計画であり、JSONに列挙したすべてのクエリを今回そのまま実行したことを表す監査ログではありません。接続済み検索結果の完全な生ログはこのZIPには含みません。

## S5 — OpenAI公式モデルガイド

OpenAI Developers, Model guidance.
https://developers.openai.com/api/docs/guides/latest-model

公式モデルガイドとユーザー提供のコピーを照合しましたが、この取得から「CodexのUltra表示と特定のAPIモデルID・推論パラメータが同一である」とは確定していません。ユーザー選択モデルを維持し、未確認設定を発明しない設計です。モデルの強さやプロンプトだけで、数学的解決または無期限の実行を保証しません。

## 採用しなかった根拠

検索要約だけの新定理、書誌情報・本文を照合していない新しいarXiv番号、非公式の「解決済み」表示は数学の前提に採用していません。C143についても、ユーザーの報告やJSONの成功表示だけをLeanの証明に置き換えていません。

## 添付資料

入力の4本のPDFとモデルガイドは `references/` に原内容を同梱。保存replay JSONは `inputs/`。各ファイルの同一性は `MANIFEST.json` に記録します。方法上の要点は `ATTACHMENT_METHOD_NOTES.md` に限定して記しています。

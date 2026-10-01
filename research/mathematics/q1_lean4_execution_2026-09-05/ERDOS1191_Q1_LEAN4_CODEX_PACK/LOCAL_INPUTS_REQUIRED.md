# Mac側で読む一次資料

このパックには以下のローカル実体は含まれていません。CodexがユーザーのMacの同じ作業環境で動く場合は、そこで直接読みます。存在を確認できなかったファイルを「読んだ」「検証した」と記録しません。

## 研究プロジェクト

```text
/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29
```

## C143 V2 run

```text
/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/runs/pilot_s32_n16_r1
```

読むもの：`C143_BANK.json`、parent/endpoint checkpoint、results、state、生成設定、ソース同定情報、runに関連する検証ログ。runディレクトリ全体を保持するのが最も確実です。

## 新しいfollow-up

```text
evidence/q1_c143_followup_2026-09-05/C143_TO_Q1_REPORT.md
evidence/q1_c143_followup_2026-09-05/c143_full_pricing_replay.py
evidence/q1_c143_followup_2026-09-05/c143_full_pricing_replay.full.json
evidence/q1_c143_followup_2026-09-05/c143_weight_extension.py
evidence/q1_c143_followup_2026-09-05/c143_terminal_audit.py
evidence/q1_c143_followup_2026-09-05/c143_cutoff_audit.py
```

上記はプロジェクトルートからの相対パスです。アップロードされた保存JSONにもreplayのargvが入っています。実際のファイル名や場所が異なる場合は、安全な読み取り検索で解決します。

`WAVE13_P18_HARMONIC_OBSTRUCTION_2026-08-29.md` と、Q1・C058・C116・Fejér重み・global ledgerの定義や依存定理も探して読んでください。これらの主張は、要約文ではなく数学的定義と証明から確認します。

## 別マシンへ移す場合

C143 V2のパッケージとrun、研究プロジェクトの必要なソース・報告・依存資料、既存Lean設定とロックファイル、未コミットの研究変更を移します。認証情報、無関係な個人ファイル、不要な巨大キャッシュは含めません。欠落した依存資料があるときは、どの命題がそれに依存するかを明記します。

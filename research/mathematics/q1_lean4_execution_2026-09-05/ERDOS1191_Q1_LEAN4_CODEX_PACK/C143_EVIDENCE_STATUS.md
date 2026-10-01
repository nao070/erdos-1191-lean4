# C143の証拠を混同しないための現在地

作成日：2026-09-05（Asia/Tokyo）。この環境で確認したのはアップロードされた保存報告です。Mac上の138MBバンク、replay本体、チェックポイント全体は未取得です。

## A. 添付された保存報告

元ファイル：`貼り付けられたテキスト（1 点）(20260904-205211).txt`

パック内：`inputs/c143_full_pricing_replay.full.json`

サイズ：**84,375 bytes**。SHA-256：

    91b4e49d372dbabf31bc3e417cb3af118123b3443603353dc486b1a965f7b052

JSONは、元ファイルをバイト単位でそのままコピーしています。記録されたstatus、exit_code、件数、時間、ハッシュは報告の内容であり、このパック作成時に同じ計算を再実行した結果ではありません。特に「90,600,510件の全チェックを今回再実行した」とは主張しません。

報告に入っている集計：

```json
{
  "argv": [
    "/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/c143_full_pricing_replay.py",
    "--mode",
    "full",
    "--output",
    "/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29/evidence/q1_c143_followup_2026-09-05/c143_full_pricing_replay.full.json"
  ],
  "bank": "/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2/runs/pilot_s32_n16_r1/C143_BANK.json",
  "bank_bytes": 144369995,
  "bank_sha256": "d680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4",
  "children_checked": 1890,
  "elapsed_seconds": 213.41266037499918,
  "endpoints_checked": 961,
  "exit_code": 0,
  "full_root_endpoint_checks": 90600510,
  "min_pointwise_child_margin": "18976473121/3065610240",
  "mode": "full",
  "numpy": "2.4.6",
  "primary": {
    "checkpoint_status_counts": {
      "checkpoint": {
        "CERTIFIED_FULL": 1147,
        "CERTIFIED_SUBINTERVAL": 743
      },
      "checkpoint_endpoints": {
        "FULLROOT_ENDPOINT_CERTIFIED": 961
      }
    },
    "package_hashes_verified": 79,
    "saved_oracle_files_present": [],
    "saved_source_hashes_verified": 28
  },
  "python": "3.13.13 | packaged by conda-forge | (main, Apr  8 2026, 02:29:07) [Clang 19.1.7 ]",
  "scope": {
    "C058_proved": false,
    "Q1_resolved": false,
    "Q2_resolved": false,
    "finite_target_fixture_only": true,
    "history_independent_eta_proved": false,
    "nonanticipating_global_ledger_proved": false,
    "single_phase_global_witness_proved": false,
    "uniform_over_all_C116_histories": false
  },
  "started_utc": "2026-09-04T20:38:14Z",
  "status": "C143_INDEPENDENT_EXACT_FULL_PRICING_OK"
}
```

巨大な有理数2本は原JSONに保存しています。補助スクリプトはそれを浮動小数点に置き換えず、有理数として比較します。

## B. このパックの補助検査で確認する範囲

`aggregate_lower < aggregate_upper`、両方が厳密に `0.04694333` と `0.04694335` の間にあること、記録件数・終了状態・有限fixtureスコープが整合することを確認します。原データから積分を再導出する検証ではありません。ファイルのハッシュは同一性の確認であり、内容の数学的正しさを保証しません。

## C. ユーザーの引き継ぎにあるが、ここではソース再検証していないこと

960 parent、完了キュー、basis/resume修正、全位相coverage、主双対実行可能性、ρ∈[97/100,1]への重み拡張、旧terminalの積分が約−0.00701784であること、14行の台帳、cutoff補正、固定サイズ窓でO(1)しか回収できないという方法限定の障害。いずれもCodexが実ファイルから仮定と証明を読み直して使用する対象です。

保存報告には `scope.Q1_resolved` がfalseと記録されています。これを真へ変更しても証明にはなりません。証明を作り、証明を検証する必要があります。

## D. Q1への距離を定義する

有限pilotの厳密計算と、任意の無限Sidon集合を扱う大域定理は異なります。最小marginが正であることから、任意の履歴・rankに一様な利得が得られるとは自動的に従いません。必要な全境界項と長距離相互作用を扱う定理を証明するか、別の方法で原Q1を直接解決します。

この区別は研究を諦める理由ではありません。次に証明すべき内容を曖昧にしないためのものです。

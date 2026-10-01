# Erdős #1191 Harness Pack — 日本語案内

## これは何か
原 Erdős Problem #1191 Q1 の意味と完了条件を固定したまま、Astra/Codexによる長期の「数学発見 → 反証 → exact check → Lean → 最終監査」を安定化するproject-local harnessです。

**これはQ1の証明ではありません。** 4つのcustom research Skillsはまだuser Codex上でbehavioral A/B testをしていないため、初期状態はCOLD candidateです。

## まず読む
1. `DESIGN_JA.md` — 全体設計と論文由来の境界。
2. `AGENTS.md` — Codexへ常時与えるプロジェクト契約。
3. `TOOL_ROUTER_POLICY.md` — 8 MCP / 85 toolsのrouting。
4. `SOURCE_MAP.md` — どの原論文の何を採用・変更したか。
5. `DEPLOYMENT.md` — 安全な導入順。

## Skills
通常研究:
- `critical-path-proof-research`
- `open-math-falsifier`
- `math-evidence-promotion`
- `math-literature-gap-search`

Meta-only:
- `harness-evolution` — implicit invocation disabled。

## Codex配置
現行Codexはrepo-local skillsを `$REPO_ROOT/.agents/skills/` から読みます。4 regular Skillsとmeta Skillをそこへ置き、`/skills`でdiscoveryを確認します。

既存のroot `AGENTS.md` を上書きせずdiff mergeしてください。`MASTER_PROMPT.md`、`research/PROBLEM_CONTRACT.md`、literal Lean targetが上位です。

## 検証状態
- Static pack validator: local RED→GREEN test済み。
- JSON/YAML/manifest integrity: pack作成時に再検査。
- Behavioral pressure tests: **未実行**。
- User Codexの85 tool routing: **未実行**。
- Q1 / frozen theorem: **このpackでは未証明**。

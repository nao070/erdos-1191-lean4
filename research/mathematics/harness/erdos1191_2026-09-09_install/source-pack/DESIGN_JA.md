# Erdős Problem #1191 — Research Harness 完成設計

日付: 2026-09-09
対象: Codex + Astra Ultra で原 Erdős Problem #1191 Q1 を完全証明または完全反証し、最終 Lean 4 clean build と公理監査まで到達する長期研究環境。

## 1. 設計原則

このpackは「万能数学agent」を作らない。役割は次の三層に分離する。

1. **Truth / Governance** — 原Q1、否定、量化、Lean target、completion gate、最終Verifierを固定する。
2. **Research / Verification** — critical-path theoremを研究し、反証、exact computation、文献、Leanを必要時だけ使う。
3. **Harness Evolution** — 数学とは別のouter loopとして、繰り返し観測された運用失敗だけを最小差分で改善する。

原Q1を解く主体はLayer 2であり、Layer 3の改善それ自体は数学的進捗ではない。

## 2. 元論文からほぼそのまま採用したもの

### LeanMarathon (arXiv:2606.05400)
- durable system of record;
- target-fidelity reviewをproof dischargeより先に置く;
- contract-scoped roles;
- bounded edit scope;
- dynamic dependency DAG;
- self-assessmentではなくexternal/deterministic verification;
- local, recoverable transactions.

**変更点:** LeanMarathonは既存の自然言語proofをLean化するsystemである。一方#1191はproof discovery自体が未完なので、単一Lean blueprintを唯一の研究状態にせず、`PROBLEM_CONTRACT` / `NEXT_THEOREM_CONTRACT` / attempts / evidence / Lean ledgerを共同system of recordとする。

### Meta-Harness (arXiv:2603.28052)
- candidate source、scores/status、raw execution tracesをfilesystemに永続化;
- summaryだけでraw historyを置換しない;
- optimizerは必要なtraceだけ選択して読む;
- expensive evaluationの前にcheap validation;
- proposerとevaluatorを分離。

**変更点:** open mathには信頼できる単一scalar rewardが無いため、Q1のtruth criterionをoptimizerのrewardにしない。Meta-Harnessは運用harnessの改善だけに限定する。

### Self-Harness (arXiv:2606.09498)
- Weakness Mining → Harness Proposal → Proposal Validation;
- isolated anecdoteではなくverifier-grounded failure cluster;
- diverse but minimal proposals;
- 同じmodel/evaluator/budgetで比較;
- regression testingを通った候補だけpromote;
- rejected changesもlineageへ保存。

**強化点:** protected passing casesの一つでも壊した変更はnet scoreが上がっても拒否する。open-mathではbenchmark平均よりfalse completion防止を優先する。

### Agentic Harness Engineering (arXiv:2604.25850)
- component / experience / decision observability;
- file-level rollbackable mutable surfaces;
- editごとの evidence → diagnosis → change → predicted fixes/regressions → observed verdict;
- verifier/model configをmutable workspace外へ置く。

**強化点:** AHE自身がregression predictionの弱さを報告しているため、予測を信用せずprotected regression gateをhard vetoにする。

### Numina-Lean-Agent (arXiv:2601.14027)
- general coding agent + specialized Lean tools;
- LSP goal/diagnostic feedback;
- theorem retrieval;
- compiler feedbackに応じたrecursive decomposition;
- hard subgoalだけisolated contextへ切る。

**変更点:** user環境に既に`lean-lsp`と`lean-explore`があるため、同等MCPを追加しない。

### ProofCouncil (arXiv:2607.09474)
- proof authorとcriticを分離;
- stateful reviewだけでなくfresh criticを使用;
- compute workerは具体的にcheckableなclaimへ使う;
- easier interpretationを解いてしまう問題をfirst-class failureとして扱う。

**強化点:** LLM criticのacceptは最終権限ではない。exact evidence / Lean / literal Q1 contractが上位。

### Adaptive tool shortlist (arXiv:2605.24660)
- installed registryとper-query shortlistを分離;
- query difficulty / scorer qualityでdepthを変える;
- correct tool presented / selected / execution succeededを分離して測定。

**変更点:** 論文のK値を一般最適値としない。5–12 schemasは初期運用域、20はsoft ceilingに過ぎない。実Codexがper-tool filteringを提供しない場合はMCP server単位のphase routingへfallbackする。

## 3. #1191固有の4 Skills

すべて初期状態は `COLD`。

1. `critical-path-proof-research` — frozen current theoremを一つずつ研究し、attempt fingerprintsとraw evidenceを残す。
2. `open-math-falsifier` — route-changing claimをfresh/minimal contextで壊す。claimを書き換えない。
3. `math-evidence-promotion` — finite / informal / Lean / target-connectedを混同しないpromotion gate。
4. `math-literature-gap-search` — general surveyではなくnamed logical gapから検索し、primary-source applicabilityを監査する。

通常のLean proof engineeringには上記を増殖させず、version-compatibleならLean FRO公式`lean-proof`を上流から使う。

## 4. Harness Evolution Skill

`harness-evolution`はmeta-onlyで、`agents/openai.yaml`によりimplicit invocationを無効化する。

発火条件:
- ユーザーが明示的に依頼した場合、または
- 複数traceで同一のrouting/context/verification/recovery/delegation/Skill failureが再現された場合。

発火しない条件:
- 一つの数学lemmaが偽だった;
- proofが難しい;
- Astraがまだ解けていない;
- 文献検索で結果がない。

変更可能:
- tool routing;
- project-local Skill text;
- role prompt;
- context selection;
- failure taxonomy;
- non-truth bookkeeping.

変更禁止:
- original Q1 / exact negation;
- theorem semantics / quantifier order;
- literal Lean target;
- completion gate;
- final verifier / axiom policy;
- protected evaluations;
- permissions / resource authority.

## 5. Tool router

Registryはuser-reported **8 MCP / 85 tools**を保存する。

通常はrole/phaseごとに必要最小限を露出する。

- research-state recovery: `context-mode`
- informal proof discovery: 原則toolsなし。named gapのみliteratureへescalate
- literature: `zbmath` or `exa` → `arxiv` → 必要なら`semantic-scholar`
- Lean theorem retrieval: `lean-explore`
- Lean project state/editing: `lean-lsp`
- exact finite work: local integer/rational computation; actual integer sequenceが現れた時だけ`mcp-oeis`
- final judge: minimal local verification only、web/writeなし

hostがdynamic/deferred schema loadingを持つ場合の初期目標は5–12 schemas。20はsoft ceiling。実装非対応ならserver phase routingにする。

## 6. Evidence promotion

このpackのcustom Skills自体にも数学claimと同じ規律を適用する。

```text
COLD -> WARM -> HOT
```

- COLD: installed candidate; default behaviorを変えない。
- WARM: target pressure testsを改善したが、まだdefault activationしない。
- HOT: baseline/candidate/protected regressionを保存し、再現できる改善が確認された場合のみ。

behavioral testsをuser Codexで走らせる前にHOTと呼ばない。

## 7. 現在の#1191への接続

このpackはactive theoremをhard-codeして永久化しない。2026-09-09時点ではU4-F / `Q1191-U4F-CORE-UNIFORM-01`がactive checkpointであるが、`research/NEXT_THEOREM_CONTRACT.md`が常に優先する。

master completionは変わらない:

- literal `Erdos1191Q1.Q1` またはliteral negationのcomplete proof;
- final pinned Lean developmentのfresh clean build;
- target/type identity;
- transitive axiom / escape audit;
- independent verification tied to source hashes.

それ以外はcheckpointまたはsupporting evidenceであり、Goal completionではない。

## 8. 導入順

1. 現在の研究sourceをsnapshot/hashで保全。
2. root `AGENTS.md`, router policy, source mapをdiff導入。
3. 4 regular Skillsを`$REPO_ROOT/.agents/skills/`へCOLD導入。
4. official `lean-proof`が必要ならupstreamから別途導入しrevisionを記録。
5. `/skills`でdiscoveryを確認。
6. `/mcp verbose`等で実server/tool surfaceを確認。
7. pressure testsをbaseline/candidateで実行。
8. 合格したSkillだけWARM/HOTへ昇格。
9. `harness-evolution`は明示invokeのみ。
10. master `/goal`を維持し、`NEXT_THEOREM_CONTRACT`の数学研究へ戻る。

## 9. このpackが意図的に実装していないもの

- MCTS over proof routes;
- 自動model-weight training;
- evaluator/judge evolution;
- 全MCPの常時activation;
- 既存85 toolsと重複する検索/Lean MCP追加;
- U4-E/U4-R/U4-Gの同時常駐探索;
- 自動Q1 statement repair;
- LLM confidenceだけによるproof promotion。

これらは現在のcritical pathに対して費用とfailure surfaceを増やすため、具体的な再現failureが出るまでYAGNIとする。

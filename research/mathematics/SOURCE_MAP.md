# Source Map and Adaptation Ledger

This file distinguishes mechanisms copied closely from primary work from project-specific adaptations. None of the cited benchmark results is evidence that Erdős #1191 is solved or that the same quantitative gain will transfer.

## LeanMarathon — arXiv:2606.05400
URL: https://arxiv.org/abs/2606.05400
Repository: https://github.com/YuanheZ/LeanMarathon

**Adopt closely**
- durable blueprint/proof-DAG as system of record;
- separate target-fidelity review before large proof discharge;
- contract-scoped roles with bounded edit authority;
- dynamic-leaf decomposition rather than one monolithic context;
- external/deterministic verification rather than self-assessment;
- persistent on-disk state for recovery.

**Adapt for #1191**
LeanMarathon autoformalizes an existing source proof. #1191 still requires mathematical discovery. Therefore our system of record is a small family of authoritative contracts/ledgers rather than one Lean blueprint, and the Math Lead may create new informal claims before they become Lean nodes.

## Meta-Harness — arXiv:2603.28052
URL: https://arxiv.org/abs/2603.28052
Project: https://yoonholee.com/meta-harness/
Repository: https://github.com/stanford-iris-lab/meta-harness

**Adopt closely**
- keep source, scores/status, and raw execution traces on disk;
- allow selective retrieval over full history instead of replacing history with summaries;
- use cheap interface/static validation before expensive evaluation;
- evaluation is external to the proposer.

**Do not copy literally**
Meta-Harness performs code-space search against benchmark reward. The #1191 evolver is not allowed unrestricted rewrites or to optimize the mathematical truth criterion.

## Self-Harness — arXiv:2606.09498
URL: https://arxiv.org/abs/2606.09498

**Adopt closely**
- Weakness Mining -> Harness Proposal -> Proposal Validation;
- cluster verifier-grounded failures rather than anecdotes;
- generate diverse but minimal candidate edits tied to one mechanism;
- hold the base model/evaluator fixed during comparison;
- promote only after non-regressive held-in/held-out testing;
- retain rejected changes in the lineage.

**Adapt for #1191**
There is no reliable scalar “open-problem solve rate” for one unsolved theorem. We apply the loop only to operational process regressions and frozen pressure tests, never to redefine mathematical correctness.

## Agentic Harness Engineering — arXiv:2604.25850
URL: https://arxiv.org/abs/2604.25850
Repository: https://github.com/china-qijizhifeng/agentic-harness-engineering

**Adopt closely**
- component / experience / decision observability;
- file-level mutable surfaces and rollback;
- every edit names failure evidence, inferred root cause, targeted fix, predicted fixes, and predicted regressions;
- model/evaluator/verifier infrastructure remains outside the mutable workspace.

**Strengthen for #1191**
AHE reports weak regression foresight. Our promotion gate therefore gives protected non-regression tests veto power rather than trusting predicted regressions.

## Numina-Lean-Agent — arXiv:2601.14027
URL: https://arxiv.org/abs/2601.14027
Repository: https://github.com/project-numina/numina-lean-agent

**Adopt closely**
- general coding agent + specialized Lean interaction/retrieval tools;
- LSP goal/diagnostic feedback instead of guessing proof state;
- theorem retrieval to reduce hallucinated Lean names;
- recursive blueprint refinement in response to compiler/proof-state feedback.

**Adapt for #1191**
We reuse the already-installed `lean-lsp` and `lean-explore`; we do not add a duplicate Lean MCP merely to mirror Numina's stack.

## ProofCouncil — arXiv:2607.09474
URL: https://arxiv.org/abs/2607.09474
Repository: https://github.com/eth-sri/proof-council

**Adopt closely**
- separate proof author and critic;
- use fresh critic context to reduce path dependence before accepting an important claim;
- invoke compute help on concrete checkable subclaims;
- treat problem interpretation as a first-class failure mode.

**Strengthen for #1191**
A fresh LLM critic is not final authority. Lean/exact evidence and the immutable Q1 contract remain the acceptance boundary.

## Tool shortlist depth — arXiv:2605.24660
URL: https://arxiv.org/abs/2605.24660

**Adopt carefully**
- adapt shortlist depth to query difficulty and retrieval quality;
- separate “correct tool was presented” from “model selected it” and “execution succeeded”;
- shorter candidate lists can improve downstream selection by reducing distractors.

**Do not overgeneralize**
The reported average around seven tools on one BFCL setup is not a universal optimum. `TOOL_ROUTER_POLICY.md` uses 5–12 only as an initial operating region and treats 20 as a soft ceiling where the host can actually filter schemas.

## OpenAI Codex — AGENTS.md and Skills
AGENTS.md: https://developers.openai.com/codex/guides/agents-md
Skills: https://developers.openai.com/codex/skills

**Adopt closely**
- root/project `AGENTS.md` as persistent project instructions, while respecting closer overrides;
- repository-local Skills under `$REPO_ROOT/.agents/skills`;
- progressive disclosure: Skill name/description first, full `SKILL.md` only on activation;
- one focused job per Skill, explicit inputs/outputs, trigger testing;
- `agents/openai.yaml` policy metadata for explicit-only invocation of the meta Skill.

**Adapt for #1191**
Keep the high-frequency project instruction surface short enough to avoid crowding the model. Store detailed paper provenance and validation material in separate files referenced by `AGENTS.md`, rather than copying them into every session prompt.

## Lean FRO Agent Skills
URL: https://github.com/leanprover/skills

**Adopt**
Use upstream `lean-proof` when installed/version-compatible. Follow its validation philosophy: a Skill should earn its place in tests and be removable when the base agent no longer benefits.

## Local authoritative evidence
The generated harness was grounded against the supplied local copies of:

- `PROBLEM_CONTRACT.md`
- `STATE.md`
- `UNRESOLVED_CORE.md`
- `LEAN_CLAIM_LEDGER.md`
- `Target.lean`

The generated pack does not claim to have executed the user's full research repository or current Codex runtime.

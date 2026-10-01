# Deployment into the #1191 Codex project

## Phase 0 — preserve current research state
Do not run `git add .`, `git clean`, hard reset, or a repo-wide rewrite merely to install this pack. The 2026-09-09 checkpoint reported an unborn Git branch and 2,373 untracked files. First use the project's existing snapshot/hash practice or make an explicit recoverable snapshot of the files you will change.

## Phase 1 — install policy files
Copy to the project root:

- `AGENTS.md`
- `TOOL_ROUTER_POLICY.md`
- `SOURCE_MAP.md` (optional but recommended)

Do not overwrite a newer project `AGENTS.md` blindly. Diff and merge project-specific instructions; `MASTER_PROMPT.md` and `research/PROBLEM_CONTRACT.md` remain authoritative.

## Phase 2 — install regular Skills as COLD candidates
Copy the four regular skill directories into `$REPO_ROOT/.agents/skills/`. Current Codex documentation scans `.agents/skills` from the working directory up to the repository root. After copying, run `/skills` (or mention a Skill with `$`) to confirm discovery. Do not copy a second Lean-LSP server or duplicate the official `lean-proof` Skill under a different name.

Run `evals/PRESSURE_TESTS.yaml` as an A/B suite:
1. baseline without the candidate Skill;
2. same case with candidate Skill available/explicitly invoked;
3. protected controls and already-passing cases.

Preserve raw transcripts. Promote a Skill to default/HOT only when it fixes its intended failure without protected regression.

## Phase 3 — tool routing
Use `/mcp verbose` or the runtime's equivalent to confirm the actual available server/tool names. If per-tool deferred loading exists, configure adaptive shortlists. If not, phase tools by MCP server as specified in `TOOL_ROUTER_POLICY.md`; do not pretend unsupported filtering exists.

## Phase 4 — Lean upstream Skill
If not already installed, consider the official Lean FRO `lean-proof` Skill from https://github.com/leanprover/skills. Pin/record the source revision used. Do not vendor a copied version into this pack.

## Phase 5 — Harness Evolution stays dormant
Install `harness-evolution` under `$REPO_ROOT/.agents/skills/`, preserving its `agents/openai.yaml`. Its `allow_implicit_invocation: false` setting keeps the meta-workflow explicit-only. Invoke it only on explicit request or repeated operational failure evidence. Its default is proposal-only; it does not edit Q1 contracts, verifier policy, or protected tests.

## Phase 6 — start mathematics
Keep the existing master `/goal`. Read `research/NEXT_THEOREM_CONTRACT.md` and continue `Q1191-U4F-CORE-UNIFORM-01` proof/refutation work. Do not rerun environment design as a substitute for mathematics.

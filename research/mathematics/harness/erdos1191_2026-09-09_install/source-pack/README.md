# Erdős #1191 Research Harness Pack

Purpose: a project-local control layer for continuing the actual proof/refutation campaign without changing the frozen mathematical target.

## Files

- `DESIGN_JA.md` — Japanese architecture rationale and paper-to-project adaptation notes.
- `README_JA.md` — Japanese quick guide.

- `AGENTS.md` — project authority, roles, evidence semantics, completion gate.
- `TOOL_ROUTER_POLICY.md` — role/phase adaptive use of the reported 8 MCP / 85 tools.
- `skills/critical-path-proof-research/SKILL.md`
- `skills/open-math-falsifier/SKILL.md`
- `skills/math-evidence-promotion/SKILL.md`
- `skills/math-literature-gap-search/SKILL.md`
- `skills/harness-evolution/SKILL.md` — meta-only outer loop.
- `SOURCE_MAP.md` — primary-paper provenance and adaptations.
- `evals/PRESSURE_TESTS.yaml` — behavioral tests specified before the Skills.
- `DEPLOYMENT.md` — safe installation/evaluation order.
- `INSTALL_PROMPT.txt` — conservative install prompt for the existing Codex project.

## Important scope

This pack is a harness design, not a proof of Q1. It was statically validated against the local checkpoint files supplied to ChatGPT, but the behavioral pressure tests have **not** been run in the user's Codex environment. Do not label a new Skill/evolution mechanism validated until its baseline/candidate/regression traces are saved.

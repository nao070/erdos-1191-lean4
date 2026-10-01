# Installation report — 2026-09-09

Files changed

- Added root AGENTS.md, TOOL_ROUTER_POLICY.md, SOURCE_MAP.md and tool-router-policy.yaml.
- Added11 files across the five named .agents/skills directories. Four description scalars were quoted after native YAML parsing exposed #1191 truncation; all Skill bodies remain unchanged. Four regular explicit-invocation guard YAMLs were added. Harness-evolution SKILL/YAML/reference are byte-identical to the pack.
- Preserved seven existing empty1191-* Skill directories. Master goal, mathematical contracts/sources, literal Lean target, toolchain, verifier policy and MCP configuration were not changed by installation.490 preservation fingerprints match.
- Diff/merge plan, exact pack-to-install diff, original source pack, source hashes, static logs, native API records and manifests are in this directory.

Skills discovered

Native Codex Desktop0.151.0 skills/list(cwds=[repo],forceReload=true) found all five at repo scope, enabled for explicit use, with complete descriptions and zero errors:

- critical-path-proof-research — COLD
- open-math-falsifier — COLD
- math-evidence-promotion — COLD
- math-literature-gap-search — COLD
- harness-evolution — DORMANT_EXPLICIT_ONLY / PROPOSE_ONLY

All five metadata files set allow_implicit_invocation:false. The meta YAML is unchanged. Native discovery parses their interfaces; it does not expose the implicit-policy field. No behavioral pressure or implicit-trigger test was run, and none of the four research Skills is called validated or HOT.

Actual MCP/tool inventory

The configured registry still has eight enabled research servers. Native mcpServerStatus/list(detail=toolsAndAuthOnly) reports:

| Dedicated server | Tools |
|---|---:|
| lean-lsp |23|
| arxiv |19|
| semantic-scholar |14|
| context-mode |11|
| lean-explore |8|
| zbmath |5|
| mcp-oeis |3|
| exa |0|

The dedicated seven nonempty research servers total83 tools. Existing Exa Apps exposes web_search_exa and web_fetch_exa, so the two Exa capabilities are available through that separate surface. Do not call the dedicated Exa server a verified2-tool server.

Native codex_apps reports574 tools and the native total is657 entries. The current conversation’s separately exposed MCP registry has677 entries across its namespaces. These are distinct surfaces, not interchangeable totals. Complete names and scopes are recorded in RUNTIME_INVENTORY.json. Pre/post-install MCP names and configuration match; no server was installed, removed or reconfigured. Per-tool dynamic/adaptive schema filtering is NOT_CONFIRMED and was not configured.

Validation commands/results

- python3 scripts/validate_pack.py — PASS in original and adapted isolated pack; PASS again after metadata correction.
- python3 run_supplied_tests.py — executes the four unchanged test_* functions from tests/test_validate_pack.py;4/4 PASS for original and adapted pack, including corrected metadata candidate.
- Original SHA256SUMS.txt —23/23 entries match.
- Native app-server initialize + skills/list + mcpServerStatus/list — PASS. Final skills-only forceReload confirms all complete descriptions.
- Installed15-file hash check,490 preservation fingerprints,7 legacy directories, meta byte-identity and independent readback — PASS.
- Native discovery probes submitted no model turns. No mathematical pre-flight/proof research, dependency/toolchain upgrade or behavioral Skill test was run during installation.

Unresolved installation issues

- Standalone Exa returns0 tools; the existing Apps fallback supplies2. Its cause was not diagnosed and auth/configuration was not changed.
- Per-tool dynamic filtering is unconfirmed.
- Baseline/candidate/protected behavioral traces are absent by design; all four research Skills stay COLD.
- python3 has no pytest module. The supplied tests were executed unchanged directly instead; no package installation was performed.
- The desktop default control socket was absent, so discovery used a bounded native stdio app-server of the installed build, not an assumed live desktop UI refresh. All probe processes terminated after read-only API calls.

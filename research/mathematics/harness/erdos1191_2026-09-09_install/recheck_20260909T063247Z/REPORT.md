# Installation verification report

## Files changed

The requested pack was already installed. No installed file required a change.
The root AGENTS.md, TOOL_ROUTER_POLICY.md, SOURCE_MAP.md and tool-router-policy.yaml
and the 11 files across the five named project-local Skill directories were preserved.
The existing PACK_TO_INSTALL.diff and project-specific merge remain intact.

Only this verification directory was added; FILES.json records its files and hashes.
The new DIFF_MERGE_PLAN.md specifies an empty installed-file diff.
All 24 before/after boundary hashes match, including the installed files,
master prompt, contracts, literal target, current mathematical working sources,
toolchain and MCP configuration. The existing master goal was read twice and
remains active with the same objective. No mathematical pre-flight or proof
research was run during this installation verification.

## Skills discovered

Native Codex Desktop 0.151.0 skills/list(cwds=[repo], forceReload=true) returned
all five at repo scope, enabled, with complete descriptions and zero errors:

- critical-path-proof-research — COLD
- open-math-falsifier — COLD
- math-evidence-promotion — COLD
- math-literature-gap-search — COLD
- harness-evolution — DORMANT_EXPLICIT_ONLY / PROPOSE_ONLY

All five source metadata files set allow_implicit_invocation:false.
The supplied harness-evolution agents/openai.yaml remains byte-identical.
Native discovery does not return that policy field; implicit-trigger behavior
was not tested. The four research Skills have not been behaviorally validated.

## Actual MCP/tool inventory

Native mcpServerStatus/list(detail=toolsAndAuthOnly), with every page consumed:

| Dedicated research server | Tools |
|---|---:|
| lean-lsp | 23 |
| arxiv | 19 |
| semantic-scholar | 14 |
| context-mode | 11 |
| lean-explore | 8 |
| zbmath | 5 |
| mcp-oeis | 3 |
| exa | 0 |

Seven nonempty dedicated research servers supply 83 tools. Native codex_apps
supplies 574, including exa.web_search_exa and exa.web_fetch_exa, for 657 native
entries in total. Zero-tool entries and all returned names are saved in
runtime_native_host.json. The separately exposed conversation surface has
677 MCP entries plus 14 non-MCP tools; all names are saved in
CONVERSATION_TOOL_INVENTORY.json. These surfaces do not demonstrate dynamic
per-tool filtering. No MCP was installed or reconfigured.

## Validation commands/results

- `python3 run_static.py`: creates disposable original and installed-overlay
  copies and runs the unchanged `python3 scripts/validate_pack.py`; both PASS.
- The same runner executes all four unchanged test functions from
  `tests/test_validate_pack.py` through `../run_supplied_tests.py`;
  4/4 PASS in each copy. All four subprocesses exited 0.
- `python3 ../runtime_probe.py runtime_native.json stdio`: sandboxed probe
  could not initialize the Codex SQLite state and returned PROBE_UNRESOLVED.
- `python3 ../runtime_probe.py runtime_native_host.json stdio`: the approved
  host-access probe completed initialize, skills/list and mcpServerStatus/list;
  PASS. It submitted no model turn and its owned process was terminated.
- Independent read-only comparison: 24 ZIP files match source-pack byte for
  byte; the live root/Skill diff exactly matches PACK_TO_INSTALL.diff;
  four regular Skill bodies remain unchanged; meta files are byte-identical;
  seven legacy empty Skill directories remain intact.
- Before/after preservation: 24/24 hashes match.

Static checks and discovery do not validate research behavior.
Baseline/candidate/protected behavioral pressure tests remain NOT_RUN.

## Unresolved installation issues

- Dedicated Exa returns zero tools and authStatus=notLoggedIn; Apps exposes
  the two Exa capabilities. Authentication was not changed.
- Per-tool dynamic/adaptive schema filtering remains NOT_CONFIRMED.
- Behavioral pressure traces are absent; the four research Skills remain COLD.
- Discovery used the installed build's native stdio app-server, not a claimed
  refresh of the running desktop UI. Standard sandbox access could not
  initialize its SQLite state; the bounded approved host probe succeeded.

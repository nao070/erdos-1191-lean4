# Installation readback report

## Files changed

The pack was already installed; no installed file needed a further change.
Existing root AGENTS.md, TOOL_ROUTER_POLICY.md, SOURCE_MAP.md and
tool-router-policy.yaml, plus 11 files in the five project-local Skill
directories, were preserved. The existing merge plan and pack-to-install diff
remain intact. Only this readback directory was added; FILES.json lists its
files and hashes.

Twenty-four before/after boundary hashes match, including the installed
instructions/Skills, master prompt, both mathematical contracts, literal Lean
target, current mathematical working sources, toolchain and MCP configuration.
The master goal remains active with the same objective. No goal mutation,
mathematical pre-flight, proof research, MCP installation or reconfiguration
was performed in this installation readback.

## Skills discovered

Native Codex Desktop 0.151.0 skills/list with this repository cwd and
forceReload=true detected all five at repo scope, enabled, with complete
descriptions and no discovery errors:

- critical-path-proof-research — COLD
- open-math-falsifier — COLD
- math-evidence-promotion — COLD
- math-literature-gap-search — COLD
- harness-evolution — DORMANT_EXPLICIT_ONLY / PROPOSE_ONLY

All five have allow_implicit_invocation:false in source metadata. The supplied
harness-evolution YAML is byte-identical. Native skills/list parses interfaces
but does not return the implicit-policy field. No behavioral trigger test was
run; the four custom research Skills have not been behaviorally validated.

## Actual MCP/tool inventory

Native mcpServerStatus/list(detail=toolsAndAuthOnly), with all pages consumed:

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

The seven nonempty dedicated research servers total 83 tools. Native codex_apps
has 574 entries, including exa.web_search_exa and exa.web_fetch_exa; the native
total is 657. Other zero-tool server entries and every returned tool name are
preserved in runtime_native.json. The current conversation exposes a separate
677-entry MCP inventory in CONVERSATION_MCP_INVENTORY.json. These distinct
surfaces do not establish per-tool dynamic/adaptive schema filtering.

## Validation commands/results

- `python3 run_static.py` creates isolated original and installed-overlay pack
  copies and runs `python3 scripts/validate_pack.py`: both PASS, exit 0.
- The same runner executes the four unchanged functions in
  `tests/test_validate_pack.py` through the existing `run_supplied_tests.py`:
  4/4 PASS in each copy, exit 0. No dependency installation was required.
- `python3 ../runtime_probe.py runtime_native.json stdio` calls initialize,
  skills/list and mcpServerStatus/list: PASS. It submitted no model turn and
  terminated its owned process after collecting the responses.
- Independent readback: ZIP/source-pack byte identity for 24 files, all 65
  registered hashes including 15 installed files, exact saved diff, seven
  preserved legacy empty directories, and meta YAML identity: PASS.

Static and discovery results do not validate research behavior. Baseline,
candidate and protected behavioral pressure tests remain NOT_RUN.

## Unresolved installation issues

- The default desktop control socket is absent. Discovery used a bounded
  native stdio app-server of the installed build, not a claimed live UI refresh.
- Sandboxed stdio could not initialize Codex SQLite state. The authorized native
  probe succeeded with normal host-state access; no configuration was changed.
- Dedicated Exa reports zero tools and authStatus=notLoggedIn. Existing Apps
  supplies its two capabilities; authentication was not altered.
- Per-tool dynamic filtering remains NOT_CONFIRMED.
- Behavioral pressure traces are absent; all four research Skills remain COLD.

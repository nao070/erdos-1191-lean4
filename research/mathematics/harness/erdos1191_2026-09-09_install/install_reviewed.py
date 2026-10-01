from pathlib import Path
import json,hashlib,shutil
R=Path('/Users/USER/Documents/ChatGPT/mathematics');C=Path('/private/tmp/erdos1191-harness-install-20260909/candidate');H=R/'harness/erdos1191_2026-09-09_install'
regular=['critical-path-proof-research','open-math-falsifier','math-evidence-promotion','math-literature-gap-search'];names=regular+['harness-evolution'];pairs=[(C/n,R/n) for n in ['AGENTS.md','TOOL_ROUTER_POLICY.md','SOURCE_MAP.md','tool-router-policy.yaml']]
for n in names:
 for p in sorted((C/'skills'/n).rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:pairs.append((p,R/'.agents/skills'/n/p.relative_to(C/'skills'/n)))
assert len(pairs)==15
protected=json.loads((H/'PROTECTED_BEFORE.json').read_text())['files']
def verify_protected():
 for path,h in protected.items():
  p=Path(path) if Path(path).is_absolute() else R/path
  assert hashlib.sha256(p.read_bytes()).hexdigest()==h, 'protected source changed: '+str(p)
verify_protected()
old=list((R/'.agents/skills').iterdir());assert len(old)==7 and all(p.name.startswith('1191-') and p.is_dir() and not list(p.iterdir()) for p in old)
for n in names:assert not (R/'.agents/skills'/n).exists()
for src,dst in pairs:
 assert not dst.exists(), 'target unexpectedly exists: '+str(dst)
 assert dst.parent==R or R/'.agents/skills' in dst.parents
for n in names:
 assert (C/'skills'/n/'SKILL.md').read_bytes()==(H/'source-pack/skills'/n/'SKILL.md').read_bytes()
assert (C/'skills/harness-evolution/agents/openai.yaml').read_bytes()==(H/'source-pack/skills/harness-evolution/agents/openai.yaml').read_bytes()
entries=[]
for src,dst in pairs:
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst);entries.append({'path':str(dst.relative_to(R)),'previous_state':'ABSENT','source':str(src),'sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
verify_protected();assert all(p.is_dir() and not list(p.iterdir()) for p in old)
(H/'INSTALL_MANIFEST.json').write_text(json.dumps({'status':'FILES_INSTALLED_AWAITING_DISCOVERY','files':entries,'existing_empty_skill_directories_preserved':[p.name for p in old],'protected_file_hashes_unchanged':len(protected),'master_goal_changed':False,'mcp_config_changed':False,'behavioral_tests':'NOT_RUN','research_skills_status':'COLD'},indent=2)+'\n')
print(json.dumps({'installed_files':len(entries),'skill_directories':names,'existing_skill_directories_preserved':7,'protected_hashes_unchanged':len(protected)}))

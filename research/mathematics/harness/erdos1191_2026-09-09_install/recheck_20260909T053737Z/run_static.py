"""Run unchanged pack checks in disposable copies, without a model turn."""
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

OUT = Path(__file__).resolve().parent
INSTALL = OUT.parent
REPO = INSTALL.parent.parent
SOURCE = INSTALL / 'source-pack'
SKILLS = [p.name for p in sorted((SOURCE / 'skills').iterdir()) if p.is_dir()]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

results = []
env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
with tempfile.TemporaryDirectory(prefix='erdos1191-harness-recheck-') as temporary:
    for label in ['original', 'installed_overlay']:
        candidate = Path(temporary) / label
        shutil.copytree(SOURCE, candidate)
        if label == 'installed_overlay':
            for name in ['AGENTS.md', 'TOOL_ROUTER_POLICY.md', 'SOURCE_MAP.md', 'tool-router-policy.yaml']:
                shutil.copy2(REPO / name, candidate / name)
            for name in SKILLS:
                shutil.copytree(REPO / '.agents/skills' / name, candidate / 'skills' / name, dirs_exist_ok=True)
        for check, args in [
            ('validator', [sys.executable, 'scripts/validate_pack.py']),
            ('supplied_tests', [sys.executable, str(INSTALL / 'run_supplied_tests.py')]),
        ]:
            process = subprocess.run(args, cwd=candidate, env=env, capture_output=True, text=True, timeout=30)
            log = OUT / f'{label}_{check}.log'
            log.write_text(process.stdout + process.stderr)
            results.append(dict(case=label, check=check, command=args, isolated_cwd=str(candidate),
                                exit_code=process.returncode, log=log.name, log_sha256=sha(log)))
    result = dict(results=results,
                  status='PASS' if all(x['exit_code'] == 0 for x in results) else 'FAIL',
                  behavioral_pressure_tests='NOT_RUN', research_skills_status='COLD',
                  supplied_validator_sha256=sha(SOURCE / 'scripts/validate_pack.py'),
                  supplied_tests_sha256=sha(SOURCE / 'tests/test_validate_pack.py'))
    (OUT / 'STATIC_VALIDATION.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    if result['status'] != 'PASS':
        sys.exit(1)

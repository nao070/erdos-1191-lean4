from pathlib import Path
import datetime
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[1]
LEAN = BASE / 'lean'
PREFIX = 'sidon_collision_determination_'

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(path):
    return json.loads(Path(path).read_text())

prior_path = BASE / 'evidence/goal9_reviewed_research.json'
prior = read(prior_path)
assert digest(prior_path) == '054629d4e4862fc4f62edc7883d9b8d8e8754c18972d6c6c738b9e5f3386d43d'
assert len(prior['files']) == 281
for rel, expected in prior['files'].items():
    assert digest(BASE / rel) == expected, rel

result = read(LEAN / 'evidence' / (PREFIX + 'result.json'))
names = result['declarations']
assert result['status'] == 'PASS' and len(names) == len(set(names)) == 7
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
source = LEAN / 'Q1/SidonCollisionDetermination.lean'
local_names = re.findall(r'^(?:theorem|noncomputable def)\s+(\w+)', source.read_text(), re.M)
assert names == ['Erdos1191Q1.SidonCollisionDetermination.' + name for name in local_names]
assert digest(source) == '7b21c6150011439e3f01c7c4ba172002094d21a9298eba7f33ce649f5ea9db64'

runs = {}
for tag in ['build', 'axioms', 'checker']:
    path = LEAN / 'evidence' / (PREFIX + tag + '.run.json')
    run = read(path)
    assert run['observed_returncode'] == 0
    before_key = 'source_and_artifact_sha256_before' if tag == 'checker' else 'source_sha256_before'
    after_key = before_key.replace('_before', '_after')
    assert run[before_key] == run[after_key]
    assert len(run[before_key]) == (31 if tag == 'checker' else 23)
    for rel, expected in run[before_key].items():
        assert digest(LEAN / rel) == expected, (tag, rel)
    assert run['prior_frozen_sha256_before'] == run['prior_frozen_sha256_after'] == prior['files']
    assert run['prior_frozen_unchanged_gate_passed']
    assert run['prior_frozen_file_count'] == 281
    for channel in ['stdout', 'stderr']:
        output_path = Path(run[channel + '_path'])
        assert digest(output_path) == run[channel + '_sha256']
        assert output_path.read_text() == run['complete_' + channel]
    if tag == 'axioms':
        found = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", run['complete_stdout'], re.S)
        assert [name for name, _ in found] == names
        for name, raw_axioms in found:
            axioms = [item.strip() for item in raw_axioms.split(',') if item.strip()]
            assert set(axioms) <= allowed
            assert axioms == result['axioms_by_declaration'][name]
        driver = (LEAN / 'evidence' / (PREFIX + 'axioms.lean')).read_text()
        assert re.findall(r'^#print axioms (\S+)', driver, re.M) == names
    if tag == 'checker':
        assert run['mode'] == 'from_imports'
        assert digest(run['checker_executable']) == run['checker_executable_sha256_before'] == run['checker_executable_sha256_after']
    runs[tag] = {
        'record': str(path.relative_to(BASE)), 'sha256': digest(path),
        'argv': run['argv'], 'observed_returncode': run['observed_returncode'],
        'started_utc': run['started_utc'], 'finished_utc': run['finished_utc'],
        'source_or_artifact_snapshot_count': len(run[before_key]),
        'prior_preserved_files_before_after_and_current': 281,
        'saved_output_bytes_and_embedded_outputs_match': True,
    }

saved_readback_path = LEAN / 'evidence' / (PREFIX + 'readback.json')
saved_readback = read(saved_readback_path)
assert saved_readback['status'] == 'PASS'
for rel, expected in saved_readback['evidence_sha256'].items():
    assert digest(LEAN / rel) == expected, rel
for rel, expected in result['compiled_artifact_sha256'].items():
    assert digest(LEAN / rel) == expected, rel

record = {
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'PASS',
    'scope': 'Parent semantic review and independent current-byte/explicit-name readback; no substantive Lean rerun.',
    'source': str(source.relative_to(BASE)), 'source_sha256': digest(source),
    'declaration_count': 7, 'declarations': names,
    'axioms_by_declaration': result['axioms_by_declaration'],
    'runs': runs,
    'prior_snapshot_sha256': digest(prior_path),
    'prior_current_files_unchanged_count': 281,
    'saved_agent_readback': str(saved_readback_path.relative_to(BASE)),
    'saved_agent_readback_sha256': digest(saved_readback_path),
    'formal_scope': 'One actual finite tuple-record definition and six theorems: nonzero far gap, actual far-pair uniqueness, exact membership, disjoint multisets, near-coordinate injection, cardinality at most K.card cubed.',
    'semantic_limits': [
        'Sidonicity and actual membership/order/sum conditions are premises; uniqueness and cardinality are derived, not assumed.',
        'The definition permits repeated old slots within a triple and includes exactly the stated finite records.',
        'No sharp binomial quotient count, geometric cluster theorem, full orbit partition, Gram energy or Q1 is supplied.',
        'Checker uses the existing imported environment and Lean kernel; no complete dependency replay or independent external kernel.',
    ],
    'combined_distinct_supporting_scope': 132,
    'separate_saved_audit_scopes': 7,
    'combined_132_audit_executed': False,
    'unchanged_aggregate_imports_new_module': False,
    'final_q1_verified': False,
    'runner_sha256': digest(__file__),
}
out = BASE / 'evidence/goal10_sidon_parent_binding.json'
out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'record': str(out), 'sha256': digest(out), 'declarations': 7, 'prior_unchanged': 281}))

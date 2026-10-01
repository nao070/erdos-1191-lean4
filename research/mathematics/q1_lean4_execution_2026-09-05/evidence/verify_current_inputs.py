"""Read-only identity binding; deliberately does not rerun the full pricing oracle."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(0)
PROJECT = Path('/Users/USER/Documents/ChatGPT/mathematics/erdos1191_PROOF_RESET_WORK_2026-08-29')
FOLLOW = PROJECT / 'evidence/q1_c143_followup_2026-09-05'
SRC = Path('/Users/USER/Downloads/C143_S32_S41_FULLROOT_EXACT_PHASE_2026-09-04_V2')
BANK = SRC / 'runs/pilot_s32_n16_r1/C143_BANK.json'
OUT = Path(__file__).with_name('current_input_identity.json')

def sha(data):
    return hashlib.sha256(data).hexdigest()

raw = BANK.read_bytes()
bank = json.loads(raw)
assert len(raw) == 144369995
assert sha(raw) == 'd680963e785b7c93c334bb4b84597200bb63b543932b63bf0292604accaae2f4'
# Exact producer encoding: c143/bank.py:18-19, 113; exclude only integrity.
payload_hash = sha(json.dumps({k: v for k, v in bank.items() if k != 'integrity'},
                             sort_keys=True, separators=(',', ':'),
                             ensure_ascii=False).encode())
assert payload_hash == bank['integrity']['canonical_payload_sha256']
assert payload_hash == '3961c6caa68c9d5dfbfbc0fdd2e433a1cf310618584ef617a892ce9b79a6725c'
provenance = json.loads((FOLLOW / 'c143_full_pricing_replay.provenance.json').read_text())
for name, digest in provenance['files_sha256'].items():
    assert sha((FOLLOW / name).read_bytes()) == digest, name
saved = json.loads((FOLLOW / 'c143_full_pricing_replay.full.json').read_text())
assert saved['bank_sha256'] == sha(raw) and saved['exit_code'] == 0
assert saved['full_root_endpoint_checks'] == 90600510
assert provenance['full_process_exit_code_observed'] == 0
assert saved['scope']['Q1_resolved'] is False
spec = importlib.util.spec_from_file_location('saved_c143_replay', FOLLOW / 'c143_full_pricing_replay.py')
replay = importlib.util.module_from_spec(spec)
spec.loader.exec_module(replay)
primary = replay.audit_primary(bank)
assert saved['primary'] == primary
out = {
    'status': 'CURRENT_INPUT_IDENTITIES_MATCH',
    'bank': str(BANK), 'bank_bytes': len(raw), 'bank_sha256': sha(raw),
    'payload_sha256': payload_hash,
    'checked_now': ['byte hash', 'producer-canonical payload hash',
                    '12 replay provenance hashes', '28 run source hashes',
                    '79 package hashes', 'run config identity',
                    'exact checkpoint/bank child and endpoint identity', 'empty queues'],
    'primary': primary,
    'reused_saved_replay': {'file': str(FOLLOW / 'c143_full_pricing_replay.full.json'),
                          'status': saved['status'], 'checks': 90600510, 'exit_code': 0},
    'full_pricing_rerun_this_execution': False,
    'lean_proof_of_bank_or_Q1': False,
}
OUT.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))

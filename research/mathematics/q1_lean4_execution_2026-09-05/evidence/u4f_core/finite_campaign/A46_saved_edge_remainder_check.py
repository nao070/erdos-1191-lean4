#!/usr/bin/env python3
"""Reclassify only the two saved A44/A45 remainder edges at one prescribed cell."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from reference_evaluator import log_bounds
from independent_checker import log_fixed, SCALE

HERE = Path(__file__).resolve().parent
src = HERE / 'A44_SHARED_TERMINAL_REMAINDER_EXACT.json'
previous = json.loads(src.read_text())
assert previous['status'] == 'PASS_EXACT_SAVED_EDGE_SUBCLASS'
assert previous['remaining_count'] == 2
data_path = HERE / previous['input']
data = json.loads(data_path.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(data_path) == previous['source_sha256'][data_path.name]
lo, hi = log_bounds(25)
il, iu = log_fixed(25)
ilo, ihi = F(il, SCALE), F(iu, SCALE)

def floor_threshold(lo, hi):
    left, right = 0, 626
    while right-left > 1:
        mid = (left+right)//2
        if mid**2 * hi**5 <= 625**2:
            left = mid
        elif mid**2 * lo**5 > 625**2:
            right = mid
        else:
            raise ArithmeticError('UNKNOWN threshold comparison')
    assert left**2 * hi**5 <= 625**2 < (left+1)**2 * lo**5
    return left

J = floor_threshold(lo, hi)
assert J == floor_threshold(ilo, ihi)
rows = []
for edge in previous['remaining_edges']:
    record = edge['original_record']
    ranks = sorted(record[2:6])
    points = [data['a'][r-1] for r in ranks]
    gaps = [points[j+1]-points[j] for j in range(3)]
    rows.append({'original_bank_index': edge['original_bank_index'],
                 'record': record, 'y': edge['y'], 'r': edge['r'],
                 'e': edge['e'], 'de': edge['de'], 'old_quad_ranks': ranks,
                 'adjacent_old_gaps': gaps, 'output_t': record[10],
                 'all_three_old_gaps_gt_J': all(g > J for g in gaps),
                 'output_t_gt_J': record[10] > J,
                 'survives_A46': all(g > J for g in gaps) and record[10] > J})
out = {'date': '2026-09-09', 'attempt': 'A46_SAVED_EDGE_SUBCLASS',
       'status': 'PASS_EXACT_TWO_SAVED_EDGES_ONLY',
       'input': previous['input'], 'C_exact': '1', 'm0': 2,
       'M': 96, 'T': 96, 'b': 25, 'k': 48, 'q_exact': '5/2',
       'J': J, 'threshold_proof': {
           'statement': 'J^2*(log25)^5 <= 625^2 < (J+1)^2*(log25)^5',
           'left_upper': str(J**2*hi**5), 'middle': 625**2,
           'right_lower': str((J+1)**2*lo**5)},
       'reference_log_interval': [str(lo), str(hi)],
       'independent_log_interval': [str(ilo), str(ihi)],
       'saved_edges_considered': 2, 'new_endpoint_candidates_examined': 0,
       'rows': rows, 'remaining_count': sum(r['survives_A46'] for r in rows),
       'remaining_indices': [r['original_bank_index'] for r in rows if r['survives_A46']],
       'unknown_comparisons': [],
       'genuine_component_price_exact': previous['genuine_component_price_exact'],
       'source_sha256': {p.name: sha(p) for p in (src, data_path, Path(__file__),
                            HERE/'reference_evaluator.py', HERE/'independent_checker.py')},
       'scope': 'Only subclassify the two saved A44/A45 remainder edges; no new history, cell, terminal, endpoint candidate, graph, or profile scan. A single survivor does not prove matching in a general remainder.'}
(HERE/'A46_SHARED_TERMINAL_REMAINDER_EXACT.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'status': out['status'], 'J': J, 'rows': rows,
                  'remaining_count': out['remaining_count']}, indent=2))

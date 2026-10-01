#!/usr/bin/env python3
"""A26: only the eight A24 rows and their seven B-pairs in one existing bank."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from independent_checker import SCALE, log_fixed, output_condition, rank_conditions

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


stem = 'C1_m02_dense_variant1_M96'
dp = HERE / (stem + '.json')
rp = HERE / (stem + '_records.json')
cp = HERE / (stem + '_independent_check.json')
wp = HERE / 'cut_shift_b24_compact_counterexamples.json'
ap = HERE / 'cut_shift_b24_component48_exact.json'
data = json.loads(dp.read_text())
cert = json.loads(cp.read_text())
previous = next(x for x in json.loads(ap.read_text()) if x['input'] == stem)
for path in (dp, rp, cp, HERE / 'independent_checker.py'):
    assert digest(path) == previous['source_sha256'][path.name]
assert cert['status'] == 'PASS' and cert['input_sha256'] == digest(dp)
assert data['C_exact'] == '1' and data['m0'] == 2
assert data['M'] == data['T'] == 96
witness = json.loads(wp.read_text())['weighted_counterexample_despite_count_decrease']
assert witness['input'] == stem
a = [None] + data['a']
k = 48
assert witness['actual_prefix_through_component48'] == a[1:k+1]
price = (F(1, k*k*(k-1)**2) - F(1, k*k*(k+1)**2)) / (a[k]-a[1])**2
assert price == F(1, 1148518878296832)

mu = Counter()
pair_at_B = {}
eight_rows = []
for sign, kind in ((1, 'birth'), (-1, 'retirement')):
    for rec in witness['complete_' + kind + '_records']:
        p, q, s, c = rec['quad']
        B, H = a[s]-a[q], a[c]-a[p]
        assert B == rec['B'] and H == rec['Hquad']
        assert B*H == rec['BH_product']
        assert pair_at_B.setdefault(B, (q, s)) == (q, s)
        mu[B] += sign*H
        eight_rows.append(dict(rec, boundary=kind, signed_H=sign*H))
assert len(eight_rows) == 8 and len(pair_at_B) == 7
support = sorted(mu)
assert sum(B*v for B, v in mu.items()) == witness['raw_BH_change'] == 424373
threshold_intervals = []
lo = 1
for B in support:
    tail = sum(v for gap, v in mu.items() if gap >= B)
    threshold_intervals.append({'s_first': lo, 's_last': B, 'length': B-lo+1,
                                'tail_signed_H': tail, 'interval_sum': (B-lo+1)*tail})
    lo = B+1
layer_sum = sum(x['interval_sum'] for x in threshold_intervals)
assert layer_sum == 424373

# Independently recover the unique actual endpoint pair of each selected B.
for B, pair in pair_at_B.items():
    found = [(q, s) for q in range(1, k) for s in range(q+1, k+1)
             if a[s]-a[q] == B]
    assert found == [pair]

traces = defaultdict(list)
rows = json.loads(rp.read_text())['records']
assert len(rows) == data['core_records']
for index, row in enumerate(rows):
    dd, ee, pd, qd, pe, qe, c, older, i, r, tt = row
    if r > k:
        continue
    p, q, s, cc = sorted((pd, qd, pe, qe))
    B = a[s]-a[q]
    if B not in pair_at_B:
        continue
    assert pair_at_B[B] == (q, s) and cc == c
    matching = {tuple(sorted((pd, qd))), tuple(sorted((pe, qe)))}
    if matching == {(p, q), (s, c)}:
        continue  # Type 1 is AC only; do not turn it into another BH use.
    typ = 2 if matching == {(p, s), (q, c)} else 3
    assert matching == ({(p, s), (q, c)} if typ == 2 else {(q, s), (p, c)})
    assert older == s and len({pd, qd, pe, qe, i, r}) == 6
    assert a[qd]-a[pd] == dd and a[qe]-a[pe] == ee
    assert dd-ee == a[r]-a[i] == tt
    assert rank_conditions(c, older, i, r) and output_condition(c, tt)
    A, Cgap, H = a[q]-a[p], a[c]-a[s], a[c]-a[p]
    assert dd*ee == (A*Cgap+B*H if typ == 2 else B*H)
    omega = sum((F(1, cut) for cut in range(c+1, i)), F(0))
    lower, upper = log_fixed(c)
    minimum = min(A, B, Cgap)
    if minimum*lower**3 > c*c*SCALE**3:
        large = True
    elif minimum*upper**3 <= c*c*SCALE**3:
        large = False
    else:
        raise AssertionError('UNKNOWN large-gap comparison')
    traces[B].append({'bank_index_zero_based': index, 'original_record': row,
                     'quad': [p, q, s, c], 'type': typ, 'i': i, 'r': r,
                     'A': A, 'B': B, 'Cgap': Cgap, 'Hquad': H,
                     'BH_product': B*H, 'all_large_old_gaps': large,
                     'cut_first': c+1, 'cut_last': i-1,
                     'harmonic_coverage_exact': str(omega),
                     'once_per_record_BH_harmonic_exact': str(B*H*omega),
                     'priced_once_per_record_BH_harmonic_exact': str(price*B*H*omega)})

reports = []
for B in sorted(pair_at_B):
    bank = traces[B]
    assert bank
    assert len({tuple(x['original_record']) for x in bank}) == len(bank)
    for wr in (x for x in eight_rows if x['B'] == B):
        assert any(x['original_record'] == wr['original_record'] for x in bank)
    groups = {}
    for label, selected in [('all_original_BH', bank),
                            ('all_large_old_gap_BH', [x for x in bank if x['all_large_old_gaps']])]:
        cut_profiles = []
        for cut in range(2, k):
            active = [x for x in selected if x['cut_first'] <= cut <= x['cut_last']]
            if active:
                cut_profiles.append({'cut': cut, 'record_count': len(active),
                                     'sum_Hquad': sum(x['Hquad'] for x in active),
                                     'BH_product_sum': sum(x['BH_product'] for x in active)})
        cov = sum((F(x['harmonic_coverage_exact']) for x in selected), F(0))
        hcov = sum((x['Hquad']*F(x['harmonic_coverage_exact']) for x in selected), F(0))
        bhcov = sum((F(x['once_per_record_BH_harmonic_exact']) for x in selected), F(0))
        assert bhcov == B*hcov
        assert cov == sum((F(x['record_count'], x['cut']) for x in cut_profiles), F(0))
        assert bhcov == sum((F(x['BH_product_sum'], x['cut']) for x in cut_profiles), F(0))
        multiple = next((x for x in cut_profiles if x['record_count'] >= 2), None)
        first_two = [] if multiple is None else [x for x in selected
                    if x['cut_first'] <= multiple['cut'] <= x['cut_last']][:2]
        groups[label] = {'record_count': len(selected),
                        'type_counts': dict(sorted(Counter(x['type'] for x in selected).items())),
                        'distinct_quadruples': len({tuple(x['quad']) for x in selected}),
                        'birth_c_multiplicity': dict(sorted(Counter(x['quad'][3] for x in selected).items())),
                        'output_i_r_multiplicity': dict(sorted(Counter(str((x['i'], x['r'])) for x in selected).items())),
                        'all_cut_multiplicities_and_BH_mass': cut_profiles,
                        'max_simultaneous_count': max((x['record_count'] for x in cut_profiles), default=0),
                        'earliest_multiple_cut': multiple,
                        'two_simultaneous_record_witnesses': first_two,
                        'total_once_per_record_harmonic_coverage_exact': str(cov),
                        'total_Hquad_harmonic_coverage_exact': str(hcov),
                        'total_BH_harmonic_coverage_exact': str(bhcov),
                        'total_genuinely_priced_BH_harmonic_coverage_exact': str(price*bhcov),
                        'recordwise_equals_cutwise_harmonic_identity': 'PASS'}
    q, s = pair_at_B[B]
    reports.append({'B': B, 'unique_middle_pair_ranks': [q, s],
                    'unique_middle_pair_values': [a[q], a[s]],
                    'groups': groups, 'all_traced_original_BH_records': bank})

out = {'date': '2026-09-09', 'attempt': 'A26', 'input': stem,
       'C_exact': '1', 'm0': 2, 'M': 96, 'T': 96, 'component_k': k,
       'genuine_component_price_exact': str(price),
       'eight_record_boundary_scope': {'cut_before': 24, 'cut_after': 25, 'l': 6,
                                      'selection': 'all large old gaps'},
       'mu_signed_H_by_integer_B': dict(sorted(mu.items())),
       'signed_mu_total': sum(mu.values()),
       'first_moment_sum_B_mu': 424373,
       'exact_integer_threshold_intervals': threshold_intervals,
       'tail_after_max_B': 0,
       'threshold_layer_sum': layer_sum,
       'genuinely_priced_first_moment_exact': str(price*layer_sum),
       'eight_original_boundary_records': eight_rows,
       'middle_pair_traces': reports,
       'source_sha256': {str(x.relative_to(HERE)): digest(x) for x in
                        [dp, rp, cp, wp, ap, HERE/'independent_checker.py', Path(__file__)]},
       'frozen_source_sha256': data['source_sha256'],
       'strict_gate_recheck': 'PASS_UNKNOWN0 for all traced records',
       'scope': 'Only the eight A24 variant rows and their seven actual middle pairs in the existing original M96 BH bank, with upper output r<=48 and one fixed component price. No new history, new general campaign, full-horizon profile recomputation, or global theorem claim.'}
dest = HERE/'integer_middle_gap_signed_measure_existing_exact.json'
dest.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'mu': out['mu_signed_H_by_integer_B'],
                  'threshold_intervals': threshold_intervals,
                  'first_moment': layer_sum,
                  'trace_summary': [{'B': r['B'], 'pair': r['unique_middle_pair_ranks'],
                                     **{g: {key: v[key] for key in ['record_count', 'type_counts',
                                         'max_simultaneous_count', 'earliest_multiple_cut',
                                         'total_BH_harmonic_coverage_exact']} for g,v in r['groups'].items()}}
                                    for r in reports]}, indent=2))

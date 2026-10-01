#!/usr/bin/env python3
"""Nine prescribed cells only; no full profile or history generation."""
import sys
sys.dont_write_bytecode = True
import hashlib
import importlib.util
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def helper(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + '.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    ref = helper('reference_evaluator')
    ind = helper('independent_checker')
    history = json.loads((HERE / 'C1_m02_dense_variant1_M96.json').read_text())
    prior = json.loads((HERE / 'A78_INDEPENDENT_CHECK.json').read_text())
    original = json.loads((HERE / 'A78_COMMON_FIBER_KERNEL.json').read_text())
    for name, digest in prior['source_sha256'].items():
        if name in ['A78_COMMON_FIBER_KERNEL.json', 'C1_m02_dense_variant1_M96.json',
                    'reference_evaluator.py', 'independent_checker.py']:
            assert sha(HERE / name) == digest
    a = [None] + history['a']
    assert (history['C_exact'], history['m0'], history['M'], history['T']) == ('1', 2, 96, 96)
    assert history['cap_all_ranks_certified'] and history['unknown_core_comparisons'] == 0
    # Read-only fixed-input arithmetic checks; never call the full evaluators.
    all_diff = {}
    for y in range(2, 97):
        for x in range(1, y):
            d = a[y] - a[x]
            assert d > 0 and d not in all_diff
            all_diff[d] = (x, y)
    for cert in history['cap_certificates']:
        n = cert['n']
        assert cert['status'] == 'PASS'
        assert a[n] - a[1] <= n*n*Fraction(cert['log_lower'])

    gate_cache = {}

    def strict(row):
        row = tuple(row)
        if row in gate_cache:
            return gate_cache[row]
        d, e, x, y, w, z, c, s, i, r, t = row
        assert len({x, y, w, z, i, r}) == 6
        rank = ref.rank_core(c, s, i, r)
        phys = ref.physical_core(c, t)
        status = 'FAIL' if False in (rank, phys) else 'UNKNOWN' if None in (rank, phys) else 'PASS'
        try:
            independent = ind.rank_conditions(c, s, i, r) and ind.output_condition(c, t)
            istatus = 'PASS' if independent else 'FAIL'
        except ArithmeticError:
            istatus = 'UNKNOWN'
        assert status == istatus, ('log methods disagree', row)
        gate_cache[row] = status
        return status

    def source_rows(quad, t, out):
        p, q, s, c = quad
        result = []
        for (x, y), (w, z) in [((p, q), (s, c)), ((p, s), (q, c)), ((p, c), (q, s))]:
            d, e = a[y]-a[x], a[z]-a[w]
            if d < e:
                d, e, x, y, w, z = e, d, w, z, x, y
            if d-e == t:
                i, r = out
                result.append((d, e, x, y, w, z, max(y, z), min(y, z), i, r, t))
        return sorted(result)

    def cell(b, k):
        n, m = b-1, k-b
        old = list(itertools.combinations(range(1, b), 2))
        future = {a[r]-a[i]: (i, r) for i in range(b+1, k) for r in range(i+1, k+1)}
        assert len(future) == m*(m-1)//2
        edges = []
        rows_by_edge = {}
        for u, v in itertools.combinations(old, 2):
            t = abs(a[u[0]]+a[u[1]]-a[v[0]]-a[v[1]])
            if t not in future:
                continue
            assert len(set(u+v)) == 4
            l, j = a[u[1]]-a[u[0]], a[v[1]]-a[v[0]]
            numerator = max((l+j)**2-t*t, 0) + max((l-j)**2-t*t, 0)
            assert numerator % 4 == 0
            kernel = numerator//4
            overlap = max(u[0], v[0]) < min(u[1], v[1])
            assert (kernel > 0) == overlap
            if not kernel:
                continue
            out = future[t]
            records = source_rows(sorted(u+v), t, out)
            assert sum(row[0]*row[1] for row in records) == kernel
            assert len(records) in (1, 2)
            for row in records:
                assert row not in rows_by_edge
                rows_by_edge[row] = (u, v)
            edge = {'U': list(u), 'V': list(v), 'L_U': l, 'L_V': j,
                    's_U': a[u[0]]+a[u[1]], 's_V': a[v[0]]+a[v[1]],
                    'output': list(out), 't': t, 'K': kernel,
                    'records': [list(row) for row in records],
                    'strict_status': [strict(row) for row in records]}
            edges.append(edge)
        # Independent direction: old quadruple / source-matching / output lookup.
        direct = {}
        for quad in itertools.combinations(range(1, b), 4):
            p, q, s, c = quad
            for first, second in [((p, q), (s, c)), ((p, s), (q, c)), ((p, c), (q, s))]:
                x, y = first; w, z = second
                d, e = a[y]-a[x], a[z]-a[w]
                if d < e:
                    d, e, x, y, w, z = e, d, w, z, x, y
                t = d-e
                if t not in future:
                    continue
                i, r = future[t]
                row = (d,e,x,y,w,z,max(y,z),min(y,z),i,r,t)
                u, v = sorted((tuple(sorted((y,w))), tuple(sorted((x,z)))))
                assert row not in direct
                direct[row] = (u,v)
        assert direct == rows_by_edge
        deg = Counter(); coredeg = Counter(); D2 = 0; core_D2 = 0
        for edge in edges:
            u, v = tuple(edge['U']), tuple(edge['V'])
            deg[u] += 1; deg[v] += 1
            D2 += edge['L_U']**2+edge['L_V']**2
            if 'PASS' in edge['strict_status']:
                coredeg[u] += 1; coredeg[v] += 1
                core_D2 += edge['L_U']**2+edge['L_V']**2
            assert 2*edge['K'] <= edge['L_U']**2+edge['L_V']**2
        vertices = [{'U':list(u), 'L':a[u[1]]-a[u[0]], 's':a[u[0]]+a[u[1]],
                     'degree':deg[u], 'strict_core_edge_degree':coredeg[u]} for u in old]
        assert D2 == sum(v['L']**2*v['degree'] for v in vertices)
        maximum = max(deg.values(), default=0)
        witnesses = {}
        for name, bound in [('n',n),('m',m),('2m',2*m)]:
            violating = [u for u in old if deg[u] > bound]
            if violating:
                u = violating[0]
                incident = [idx for idx,e in enumerate(edges) if list(u) in (e['U'], e['V'])]
                witnesses[name] = {'bound':bound, 'vertex':list(u), 'degree':deg[u],
                                   'incident_edge_indices':incident, 'violating_vertex_count':len(violating)}
            else:
                witnesses[name] = {'bound':bound, 'status':'NO_COUNTEREXAMPLE_IN_THIS_CELL'}
        status_counts = Counter(strict(row) for row in rows_by_edge)
        Q = sum(row[0]*row[1] for row in rows_by_edge)
        Qcore = sum(row[0]*row[1] for row in rows_by_edge if strict(row) == 'PASS')
        lam = Fraction(4, k*(k*k-1)**2*(a[k]-a[1])**2)
        summary = {'b':b,'k':k,'n':n,'m':m,'vertices':len(old),'edges':len(edges),
                   'source_records':len(rows_by_edge),'kernel_Q':Q,'weighted_diagonal_D_exact':str(Fraction(D2,2)),
                   'Q_over_D_exact':str(Fraction(2*Q,D2)), 'degree_histogram':dict(sorted(Counter(deg[u] for u in old).items())),
                   'maximum_degree':maximum,'max_degree_vertices':[list(u) for u in old if deg[u]==maximum],
                   'degree_candidates':witnesses,'strict_status_counts':dict(status_counts),
                   'strict_core_Q':Qcore,'strict_core_edges':sum('PASS' in e['strict_status'] for e in edges),
                   'strict_core_maximum_edge_degree':max(coredeg.values(),default=0),
                   'strict_core_diagonal_D_exact':str(Fraction(core_D2,2)),
                   'genuine_lambda_k_exact':str(lam),'component_unfiltered_exact':str(lam*Q),
                   'component_strict_core_exact':str(lam*Qcore)}
        return {'summary':summary,'vertices':vertices,'edges':edges}, rows_by_edge

    cells = []; row_maps = {}
    for b in (24,25,26):
        for k in (47,48,49):
            result, rows = cell(b,k)
            cells.append(result); row_maps[(b,k)] = rows
            print(json.dumps(result['summary']), flush=True)

    baseline = next(x for x in cells if (x['summary']['b'],x['summary']['k'])==(25,48))
    old_pairs = {}
    for pair in original['results'][0]['pairs']:
        if pair['kernel'] <= 0:
            continue
        vertices = sorted(tuple(t[:2]) for t in pair['triples'])
        outputs = sorted(t[2]+25 for t in pair['triples'])
        key = tuple(vertices)+tuple(outputs)
        assert key not in old_pairs
        old_pairs[key] = (pair['kernel'], sorted(pair['original_source_products']))
    new_pairs = { (tuple(e['U']),tuple(e['V']),*e['output']):
                 (e['K'], sorted(r[0]*r[1] for r in e['records'])) for e in baseline['edges'] }
    assert new_pairs == old_pairs
    assert baseline['summary']['kernel_Q'] == 257942228
    assert baseline['summary']['source_records'] == 3993

    comparisons = []
    by_cell = {(x['summary']['b'],x['summary']['k']):x for x in cells}
    def edge_map(key):
        return {(tuple(e['U']),tuple(e['V'])):e for e in by_cell[key]['edges']}
    for axis in ('cut','component'):
        transitions = [((b,k),(b+1,k)) for b in (24,25) for k in (47,48,49)] if axis=='cut' else [((b,k),(b,k+1)) for b in (24,25,26) for k in (47,48)]
        for left,right in transitions:
            before, after = edge_map(left), edge_map(right)
            added, removed = sorted(after.keys()-before.keys()), sorted(before.keys()-after.keys())
            for key in before.keys() & after.keys():
                assert before[key] == after[key]
            if axis=='cut':
                b,k = left
                assert all(b in u+v for u,v in added)
                assert all(before[key]['output'][0] == b+1 for key in removed)
            else:
                b,k = left
                assert not removed
                assert all(after[key]['output'][1] == k+1 for key in added)
            comparisons.append({'axis':axis,'from':left,'to':right,
                'added_edges':len(added),'removed_edges':len(removed),
                'added_K':sum(after[key]['K'] for key in added),
                'removed_K':sum(before[key]['K'] for key in removed),
                'delta_Q':by_cell[right]['summary']['kernel_Q']-by_cell[left]['summary']['kernel_Q'],
                'added_edge_keys':added,'removed_edge_keys':removed})
            assert comparisons[-1]['delta_Q'] == comparisons[-1]['added_K']-comparisons[-1]['removed_K']
    sources = ['C1_m02_dense_variant1_M96.json','A78_COMMON_FIBER_KERNEL.json','A78_INDEPENDENT_CHECK.json',
               'reference_evaluator.py','independent_checker.py',Path(__file__).name]
    result = {'attempt':'A80','status':'PASS_BOUNDED_INDEPENDENT_GRAPH_RECONSTRUCTION',
        'campaign':{'C_exact':'1','m0':2,'M':96,'T':96},
        'source_sha256':{name:sha(HERE/name) for name in sources},
        'scope':['Only b in {24,25,26} and k in {47,48,49}; fixed existing actual history.',
                 'Main graph is unfiltered original positive-source incidence, not strict core or current residual.',
                 'Each graph edge is counted once; nested edges retain two distinct source records.',
                 'Strict core flags use both existing rational interval methods; no later residual selector applied.',
                 'No full profile, whole-horizon sum, new history, optimized bound, or uniform-K conclusion.'],
        'baseline_A78_positive_edges_exactly_matched':True,
        'history_positive_difference_uniqueness_checked':True,
        'saved_all_rank_cap_certificates_readback':True,
        'unique_bounded_source_records_checked_by_both_log_methods':len(gate_cache),
        'unknown_records':sum(x=='UNKNOWN' for x in gate_cache.values()),
        'cells':cells,'adjacent_comparisons':comparisons}
    out = HERE/'A80_OLD_PAIR_GRAPH_EXACT.json'
    out.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':'))+'\n')
    print('SAVED',str(out),sha(out),flush=True)


if __name__ == '__main__':
    main()

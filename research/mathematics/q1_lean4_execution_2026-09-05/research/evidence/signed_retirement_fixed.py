#!/usr/bin/env python3
"""One exact inspection of signed linear retirement on four fixed Sidon histories.

This tests a proposed stage-sign route, not original Q1. No parameter sweep.
"""
from collections import defaultdict
from itertools import combinations

FIXTURES = (
    (0, 1, 3),
    (0, 1, 4, 6),
    (0, 1, 10, 13, 17, 39),
    (1, 3, 4, 12, 25, 29, 44, 71, 89, 123, 167, 197, 204, 259,
     273, 279, 362, 410, 420, 483, 519, 700, 705, 800, 854, 887,
     971, 1032, 1259, 1297, 1421, 1518),
)


def inspect(points):
    sums = [points[i] + points[j] for i in range(len(points))
            for j in range(i, len(points))]
    assert len(set(sums)) == len(sums)
    bank = {}
    for j, a in enumerate(points, 1):
        for b in points[:j-1]:
            d = a-b
            assert d > 0 and d not in bank
            bank[d] = bank[-d] = j
    retired, born, counts = defaultdict(int), defaultdict(int), defaultdict(int)
    examples = defaultdict(list)
    for d, e in combinations(sorted(bank), 2):
        t = e-d
        if t not in bank:
            continue
        b, r = max(bank[d], bank[e]), bank[t]
        if r > b:
            retired[r] += d*e
            counts[r] += 1
            if len(examples[r]) < 6:
                examples[r].append((d, e, t, b, d*e))
        else:
            born[b] += d*e
    assert all(v >= 0 for v in born.values())
    square = sum(d*d for d in bank)
    shadow = defaultdict(int)
    for a in points:
        for d in bank:
            shadow[a+d] += d
    energy = sum(v*v for v in shadow.values())
    assert energy == len(points)*square+2*sum(born.values())+2*sum(retired.values())
    print(f'N={len(points)}; points={points}; repeated-sum Sidon: PASS')
    print(f'full_born_by_source_stage={dict(sorted(born.items()))}')
    print(f'full_retired_by_output_stage={dict(sorted(retired.items()))}')
    positives = [r for r in sorted(retired) if retired[r] > 0]
    print(f'positive_retirement_stages={positives}')
    for r in positives[:1]:
        print(f'first_positive_stage={r}; exact_total={retired[r]}; '
              f'pair_count={counts[r]}; first_six_pairs={examples[r]}')
    print(f'full_convolution_identity: PASS; E={energy}; S={square}; '
          f'Born={sum(born.values())}; Retired={sum(retired.values())}')


if __name__ == '__main__':
    for fixture in FIXTURES:
        inspect(fixture)
    print('Four fixed exact checks only; no infinite-counterexample or asymptotic claim.')

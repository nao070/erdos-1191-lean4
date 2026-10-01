from itertools import combinations
from pathlib import Path
import hashlib, json

from endpoint_variance import (
    crossing_loads,
    diameter_regime_profile,
    diameter_regime_variance,
    endpoint_imbalance,
    rank_imbalance_square_sum,
    variance,
)

checks=0
for universe_size in range(0,10):
    universe=range(universe_size)
    for size in range(universe_size+1):
        for points in combinations(universe,size):
            diameter=points[-1]-points[0] if points else 0
            for modulus in range(max(2,diameter+1),max(2,diameter+1)+5):
                profile=diameter_regime_profile(points,modulus)
                assert profile.outside_gap + sum(profile.internal_gaps)==modulus
                assert diameter_regime_variance(points,modulus)==variance(crossing_loads(points,modulus))
                assert sum(x*x for x in endpoint_imbalance(points,modulus))==rank_imbalance_square_sum(size)
                checks+=3
payload={
    'theorem':'complete-prefix diameter-regime gap moments and cubic imbalance',
    'exact_checks':checks,
    'cubic_formula':'m(m^2-1)/3',
    'variance_lower_bound':'m(m^2-1)/(12N)',
}
canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['sha256']=hashlib.sha256(canonical).hexdigest()
Path('diameter_certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))

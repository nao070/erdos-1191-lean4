from itertools import combinations
from pathlib import Path
import hashlib, json
from endpoint_variance import crossing_loads, diameter_required_levels_lower_bound, variance
checks=0
for universe_size in range(0,12):
    for size in range(universe_size+1):
        for points in combinations(range(universe_size),size):
            diameter=points[-1]-points[0] if points else 0
            for modulus in range(max(2,diameter+1),max(2,diameter+1)+4):
                assert variance(crossing_loads(points,modulus)) >= diameter_required_levels_lower_bound(size,modulus)
                checks += 1
payload={
 'theorem':'sharp mandatory split-level variance bound in diameter regime',
 'exact_checks':checks,
 'bound':'m(m^2-1)(m^2+11)/(180N)',
 'sharp_family':'A={0,1,...,m-1}, N=m',
}
canonical=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['sha256']=hashlib.sha256(canonical).hexdigest()
Path('required_levels_certificate.json').write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps(payload,indent=2))

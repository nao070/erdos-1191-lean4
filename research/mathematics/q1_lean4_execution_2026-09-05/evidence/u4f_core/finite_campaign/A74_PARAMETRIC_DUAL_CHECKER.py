#!/usr/bin/env python3
"""Independent A74 certificate checker; standard library, no optimizer/imported reference.

Reads only the two existing source cells and their saved certificates/record subsets.
Reconstructs arbitrary-weight matrices, checks complete assignment duals and affine
lower supports, and writes only A74_PARAMETRIC_DUAL_CHECK.json beside this script.
"""
from bisect import bisect_left
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent
SOURCES = {}
INPUTS = {
    "A70_FEASIBLE_MATCHING_EXACT.json": {
        "history": "C1_m02_dense_variant1_M96.json",
        "c": 24, "b": 25, "k": 48, "C": 1, "M": 96,
        "old_check": "A70_FEASIBLE_MATCHING_CHECK.json",
    },
    "A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json": {
        "history": "C2pow67_m02_prescribed_allowance_M50.json",
        "c": 24, "b": 25, "k": 50, "C": 2**67, "M": 50,
        "old_check": "A72_SOURCE_ALLOWANCE_CHECK.json",
    },
}


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def integer(value):
    require(type(value) is int, "certificate integer required")
    return value


def bind(name, expected=None):
    require(Path(name).name == name, "source must be a local filename")
    data = (ROOT / name).read_bytes()
    digest = sha256(data).hexdigest()
    if expected is not None:
        require(digest == expected, "source hash mismatch: " + name)
    require(name not in SOURCES or SOURCES[name] == digest, "source changed during check")
    SOURCES[name] = digest
    return data


def read(name, expected=None):
    return json.loads(bind(name, expected))


def declared_sources(data):
    for name, digest in data.get("source_sha256", {}).items():
        bind(name, digest)


def build_cell(name, expected):
    config = INPUTS[name]
    source = read(name, expected)
    declared_sources(source)
    history = read(config["history"])
    prior_check = read(config["old_check"])
    require(prior_check["status"].startswith("PASS"), "existing certification did not pass")
    a = [integer(x) for x in history["a"]]
    require(len(a) == config["M"] == history["M"] == history["T"], "history horizon mismatch")
    require(Fraction(history["C_exact"]) == config["C"] and history["m0"] == 2,
            "fixed campaign mismatch")
    require(history["cap_all_ranks_certified"] is True, "missing existing all-rank cap certificate")
    require(history["unknown_core_comparisons"] == 0, "existing core comparison is UNKNOWN")
    c, b, k = config["c"], config["b"], config["k"]
    old, future, ac = a[:c-1], a[b:k], a[c-1]
    require(old == source["old_values"] and future == source["future_values"], "cell values mismatch")
    require(ac-a[0] == source["H_c"], "actual source diameter mismatch")
    require(all(a[i] < a[i+1] for i in range(len(a)-1)), "non-increasing actual input")
    n, m = len(old), len(future)
    # Actual source budget: every physical (w,z,x) at most once.
    Bsource = 0
    fresh = {}
    for z in range(1, n+1):
        for w in range(1, z):
            g = old[z-1]-old[w-1]
            labels = sorted(ac-old[x-1] for x in range(1, n+1) if x not in (w, z))
            fresh[w, z] = labels
            Bsource += sum(g*max(h-g, 0) for h in labels)
    # Each entry is None or (gt, g(hmin-g), hmin), before theta scaling.
    matrices = {}
    for z in range(1, n+1):
        for q in range(1, m+1):
            matrix = []
            for w in range(1, z):
                row = []
                g = old[z-1]-old[w-1]
                labels = fresh[w, z]
                for j in range(1, q):
                    t = future[q-1]-future[j-1]
                    pos = bisect_left(labels, g+t)
                    row.append(None if pos == len(labels) else
                               (g*t, g*(labels[pos]-g), labels[pos]))
                matrix.append(row)
            matrices[z, q] = matrix
    if name.startswith("A70"):
        bank = read("A65_SPARSE_FIBER_FOLLOWUP_EXACT.json")
        declared_sources(bank)
        require(bank["UNKNOWN"] == 0, "A65 UNKNOWN")
        records = [r["record"] for r in bank["records"] if r["category"] != "paid_sparse_support"]
        require(len(records) == 125, "wrong bounded A65 record subset")
    else:
        record_bank = read("C2pow67_m02_prescribed_allowance_M50_records.json")
        records = record_bank["records"]
        require(records == [source["selected_record"]] and history["core_records"] == 1,
                "A72 must have its certified single original record")
    actual_nodes = defaultdict(list)
    seen_records, seen_sources = set(), set()
    beta, original_mass = 0, 0
    for row in records:
        require(len(row) == 11, "wrong physical record schema")
        d, e, x, y, w, z, birth, s, i, r, t = map(integer, row)
        require(tuple(row) not in seen_records, "physical record counted twice")
        seen_records.add(tuple(row))
        require(1 <= x < y <= c and 1 <= w < z <= c and birth == max(y,z) == c,
                "source index mismatch")
        require(s == min(y,z) and len({x,y,w,z,i,r}) == 6 and c < b < i < r <= k,
                "actual original endpoint/cut scope mismatch")
        require(a[y-1]-a[x-1] == d > e == a[z-1]-a[w-1] > 0,
                "actual source differences mismatch")
        require(a[r-1]-a[i-1] == t == d-e > 0, "actual output difference mismatch")
        original_mass += d*e
        if y != c:
            # The smaller fresh orientation contributes no positive g*t charge.
            require(z == c, "exactly one fresh source required")
            continue
        node = z, r-b
        left = w, i-b
        require((w,z,x) not in seen_sources, "source budget reused across nodes")
        seen_sources.add((w,z,x))
        entry = matrices[node][w-1][i-b-1]
        require(entry is not None and entry[2] == d and entry[0] == e*t == entry[1],
                "actual hmin must equal fresh h=g+t")
        actual_nodes[node].append((left[0], left[1], entry[0]))
        beta += e*t
    for edges in actual_nodes.values():
        require(len({e[0] for e in edges}) == len(edges) == len({e[1] for e in edges}),
                "actual right-node edges are not a matching")
    require(beta <= Bsource, "actual physical source charge exceeds its bank")
    if name.startswith("A70"):
        require(beta == 8716524 == source["actual_Beta"] == prior_check["actual_Beta"],
                "A70 independently reconstructed Beta mismatch")
    else:
        require(beta == 127605887595579202812083736393554006016, "A72 Beta mismatch")
    return {"name":name,"source":source,"history":history,"config":config,"old":old,
            "future":future,"ac":ac,"n":n,"m":m,"B":Bsource,"matrices":matrices,
            "actual_nodes":actual_nodes,"beta":beta,"original_mass":original_mass,
            "actual_record_count":len(records),"positive_record_count":len(seen_sources)}


def entry_at(cell, z, q, w, j):
    require(1 <= z <= cell["n"] and 1 <= q <= cell["m"], "node outside source input")
    require(1 <= w < z and 1 <= j < q, "left coordinate outside node")
    return cell["matrices"][z,q][w-1][j-1]


def verify_duals(cell, nodes, theta):
    p, denominator = theta.numerator, theta.denominator
    require(0 <= p <= denominator, "theta outside [0,1]")
    require(len(nodes) == cell["n"]*cell["m"], "wrong number of dual nodes")
    covered, node_results = set(), []
    total, comparisons, selected_positive = 0, 0, 0
    for node in nodes:
        z, q = integer(node["z"]), integer(node["q"])
        require((z,q) in cell["matrices"] and (z,q) not in covered, "duplicate or invalid node")
        covered.add((z,q))
        N = max(z-1,q-1)
        left = list(map(integer,node["dual_left"]))
        right = list(map(integer,node["dual_right"]))
        assignment = list(map(integer,node["assignment"]))
        require(len(left) == len(right) == len(assignment) == N, "dual matrix dimension mismatch")
        require(sorted(assignment) == list(range(N)), "assignment is not a permutation")
        weights = [[0]*N for _ in range(N)]
        for w in range(1,z):
            for j in range(1,q):
                e = entry_at(cell,z,q,w,j)
                if e is not None:
                    weights[w-1][j-1] = max(denominator*e[0]-p*e[1],0)
        for w in range(N):
            for j in range(N):
                require(left[w]+right[j] >= weights[w][j], "assignment dual inequality failed")
                comparisons += 1
        assignment_value = sum(weights[w][assignment[w]] for w in range(N))
        value = integer(node["value_scaled"])
        require(value >= 0 and assignment_value == value == sum(left)+sum(right),
                "primal-dual objective mismatch")
        selected_positive += sum(weights[w][assignment[w]] > 0 for w in range(N))
        actual = sum((denominator-p)*e[2] for e in cell["actual_nodes"].get((z,q),[]))
        require(actual <= value, "actual residual node charge exceeds certified matching")
        total += value
        node_results.append({"z":z,"q":q,"value_scaled":value,
                             "actual_residual_scaled":actual,"gap":value-actual})
    bound = Fraction(p*cell["B"]+total,denominator)
    require(Fraction(cell["beta"]) <= bound, "actual Beta exceeds Dtheta")
    return {"theta_exact":str(theta),"bound_exact":str(bound),"matching_sum_scaled":total,
            "nodes":len(nodes),"dual_inequalities_checked":comparisons,
            "positive_assignment_edges":selected_positive,"all_primal_dual_gaps_zero":True,
            "all_actual_node_residuals_bounded":True,"node_results":node_results}


def verify_support(cell, support, theta, optimum):
    A = cost = 0
    used_w, used_j = defaultdict(set), defaultdict(set)
    seen = set()
    for edge in support["positive_edges"]:
        require(len(edge) == 4, "support edge schema mismatch")
        z,q,w,j = map(integer,edge)
        require((z,q,w,j) not in seen, "support edge repeated")
        seen.add((z,q,w,j))
        require(w not in used_w[z,q] and j not in used_j[z,q], "support is not a partial matching")
        used_w[z,q].add(w);used_j[z,q].add(j)
        e = entry_at(cell,z,q,w,j)
        require(e is not None, "support edge has no allowed fresh hmin")
        A += e[0];cost += e[1]
    slope = cell["B"]-cost
    require(A == integer(support["intercept"]) and slope == integer(support["slope"]),
            "support affine coefficients mismatch")
    value = A+theta*slope
    require(value <= optimum, "feasible affine lower support exceeds optimum")
    return {"intercept":A,"slope":slope,"edges":len(seen),"value_at_theta_exact":str(value),
            "active":value == optimum,"cost_sum":cost}


def main():
    certificate = read("A74_PARAMETRIC_DUAL_EXACT.json")
    declared_sources(certificate)
    require(len(certificate["results"]) == 2, "only the two prescribed cells are allowed")
    require({r["input"] for r in certificate["results"]} == set(INPUTS), "unexpected source cells")
    cells, results = {}, []
    for item in certificate["results"]:
        name = item["input"]
        cell = build_cell(name,item["input_sha256"])
        cells[name] = cell
        require(cell["B"] == integer(item["B_source_positive"]), "source bank mismatch")
        theta = Fraction(item["optimum_theta_exact"])
        optimum = Fraction(item["minimum_D_exact"])
        dual = verify_duals(cell,item["upper_node_duals"],theta)
        require(Fraction(dual["bound_exact"]) == optimum, "claimed optimum differs from dual bound")
        supports = [verify_support(cell,s,theta,optimum) for s in item["lower_supports"]]
        active = [s["slope"] for s in supports if s["active"]]
        if theta == 0:
            optimal = any(s >= 0 for s in active)
            reason = "active lower support with nonnegative slope at theta=0"
        elif theta == 1:
            optimal = any(s <= 0 for s in active)
            reason = "active lower support with nonpositive slope at theta=1"
        else:
            optimal = 0 in active or (any(s < 0 for s in active) and any(s > 0 for s in active))
            reason = "active zero-slope or opposite-sign affine lower supports at interior theta"
        require(optimal, "no valid global minimum certificate")
        require(Fraction(item["endpoint_1_exact"]) == cell["B"], "theta=1 source-bank endpoint mismatch")
        require(optimum <= min(Fraction(item["endpoint_0_exact"]),Fraction(item["endpoint_1_exact"])),
                "minimum exceeds an endpoint")
        results.append({"input":name,"campaign":cell["config"],"B_source_positive":cell["B"],
                        "actual_record_count":cell["actual_record_count"],
                        "positive_record_count":cell["positive_record_count"],"actual_Beta":cell["beta"],
                        "actual_original_product_mass":cell["original_mass"],
                        "optimum_theta_exact":str(theta),"minimum_D_exact":str(optimum),
                        "minimum_minus_actual_Beta_exact":str(optimum-cell["beta"]),
                        "global_minimum_certified":True,"global_minimum_reason":reason,
                        "lower_supports":supports,"upper_certificate":dual})
    # Also certify the already saved 0,1/2,1 matrices, independently of the
    # optimizer trace. This binds both endpoint fields used above.
    basic = read("A74_SOURCE_DUAL_EXACT.json")
    declared_sources(basic)
    require(len(basic["cases"]) == 2 and {r["input"] for r in basic["cases"]} == set(INPUTS),
            "basic certificate must contain exactly the same two cells")
    for basic_item in basic["cases"]:
        name = basic_item["input"]
        cell = cells[name]
        bind(name,basic_item["input_sha256"])
        require(basic_item["old_values"] == cell["old"] and basic_item["future_values"] == cell["future"]
                and basic_item["ac"] == cell["ac"], "basic cell reconstruction mismatch")
        require(basic_item["B_source_positive"] == cell["B"] and basic_item["actual_Beta"] == cell["beta"],
                "basic source or actual mass mismatch")
        require(len(basic_item["cases"]) == 3, "three specified theta values required")
        checked = {}
        for item in basic_item["cases"]:
            theta = Fraction(item["theta"])
            require(theta in {Fraction(0),Fraction(1,2),Fraction(1)} and theta not in checked,
                    "unexpected or duplicate basic theta")
            require(integer(item["numerator"]) == theta.numerator
                    and integer(item["denominator"]) == theta.denominator, "theta scale mismatch")
            dual = verify_duals(cell,item["nodes"],theta)
            require(dual["matching_sum_scaled"] == integer(item["matching_sum_scaled"])
                    and Fraction(dual["bound_exact"]) == Fraction(item["bound_exact"]),
                    "basic matching value mismatch")
            checked[theta] = dual
        parametric = next(r for r in certificate["results"] if r["input"] == name)
        require(Fraction(parametric["endpoint_0_exact"]) == Fraction(checked[Fraction(0)]["bound_exact"]),
                "parametric theta=0 endpoint is not certified")
        require(Fraction(parametric["endpoint_1_exact"]) == Fraction(checked[Fraction(1)]["bound_exact"]),
                "parametric theta=1 endpoint is not certified")
        minimum_tested = min(Fraction(d["bound_exact"]) for d in checked.values())
        require(Fraction(basic_item["minimum_tested_bound_exact"]) == minimum_tested,
                "minimum of three basic values mismatch")
        result = next(r for r in results if r["input"] == name)
        result["basic_three_theta_certificates"] = [checked[t] for t in sorted(checked)]
    bind("A74_SOURCE_DUAL_REVIEW.md")
    bind(Path(__file__).name)
    output = {
        "attempt":"A74","status":"PASS_INDEPENDENT_GLOBAL_PARAMETRIC_MINIMUM_CERTIFICATE",
        "scope":"Only the two existing source cells. No reference import, optimizer, history generation, "
                "record enumeration, strict-gate re-evaluation, profile computation, or Lean build.",
        "source_sha256":SOURCES,"results":results,"unknown_comparisons":0,
        "formal_check":"Finite exact integer/rational arithmetic. Hand theorem A74 supplies Beta<=Dtheta. "
                       "Actual original gate/cap and residual memberships are reused from bound existing evidence.",
        "scope_limits":["The optimizer trace and oracle count are runtime metadata, not needed for this certificate.",
                        "Global means every theta in [0,1] for each of these two fixed cells only.",
                        "Absent auxiliary matching edges are not priced as original records.",
                        "No all-cut/full-profile bound, uniform norm theorem, frozen U4F result, or Q1 conclusion."]}
    destination = ROOT / "A74_PARAMETRIC_DUAL_CHECK.json"
    destination.write_text(json.dumps(output,indent=2,ensure_ascii=False)+"\n")
    print(output["status"])
    for result in results:
        print(result["input"],"theta",result["optimum_theta_exact"],"minimum",result["minimum_D_exact"],
              "actual_Beta",result["actual_Beta"])
    print("output_sha256",sha256(destination.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()

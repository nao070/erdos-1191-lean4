#!/usr/bin/env python3
"""Independent exact A76 checker. Standard library only; no reference imports.

Checks the two saved actual cells at theta=0,1/2,1. The A65 input is the
already-certified 125-row residual subset, not a re-enumeration of all core.
Writes only A76_FULL_MASS_CHECK.json beside this checker.
"""
from bisect import bisect_left
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


F = Path(__file__).resolve().parent
SOURCES = {}
CONFIG = {
    "A70_FEASIBLE_MATCHING_EXACT.json": {
        "history": "C1_m02_dense_variant1_M96.json", "c": 24, "b": 25, "k": 48,
        "M": 96, "C": 1, "record_source": "A65_SPARSE_FIBER_FOLLOWUP_EXACT.json",
        "record_count": 125, "prior_check": "A70_FEASIBLE_MATCHING_CHECK.json",
    },
    "A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json": {
        "history": "C2pow67_m02_prescribed_allowance_M50.json", "c": 24, "b": 25, "k": 50,
        "M": 50, "C": 2**67, "record_source": "C2pow67_m02_prescribed_allowance_M50_records.json",
        "record_count": 1, "prior_check": "A72_SOURCE_ALLOWANCE_CHECK.json",
    },
}


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def integer(value):
    require(type(value) is int, "integer certificate field required")
    return value


def bind(name, expected=None):
    require(Path(name).name == name, "local source filename required")
    data = (F/name).read_bytes()
    digest = sha256(data).hexdigest()
    require(expected is None or expected == digest, "source hash mismatch: "+name)
    require(name not in SOURCES or SOURCES[name] == digest, "source changed during check")
    SOURCES[name] = digest
    return data


def read(name, expected=None):
    return json.loads(bind(name,expected))


def check_declared(data):
    for name,digest in data.get("source_sha256",{}).items():
        bind(name,digest)


def reconstruct(item):
    name = item["input"]
    config = CONFIG[name]
    source = read(name,item["input_sha256"])
    check_declared(source)
    history = read(config["history"])
    prior = read(config["prior_check"])
    require(prior["status"].startswith("PASS"), "existing input certification did not pass")
    a = list(map(integer,history["a"]))
    c,b,k,M = config["c"],config["b"],config["k"],config["M"]
    require(history["M"] == history["T"] == len(a) == M
            and Fraction(history["C_exact"]) == config["C"] and history["m0"] == 2,
            "fixed campaign mismatch")
    require(history["cap_all_ranks_certified"] is True and history["unknown_core_comparisons"] == 0,
            "missing bound cap/core certification")
    require(all(a[j] < a[j+1] for j in range(M-1)), "actual history is not increasing")
    # Literal Sidon and unique output lookup are checked directly on the given
    # integers; this creates no new history or core-record enumeration.
    differences = {}
    for r in range(2,M+1):
        for i in range(1,r):
            t = a[r-1]-a[i-1]
            require(t not in differences, "duplicate actual positive difference")
            differences[t] = (i,r)
    old,future,ac = a[:c-1],a[b:k],a[c-1]
    n,m = len(old),len(future)
    require(old == source["old_values"] and future == source["future_values"]
            and ac-a[0] == source["H_c"], "source cell values mismatch")
    mixed_sums = [x+y for x in old for y in future]
    require(len(set(mixed_sums)) == n*m, "actual old/future two-sums are not unique")

    fresh_by_source = {}
    bank_terms = []
    S_total = 0
    U = sum(old[z-1]-old[w-1] for z in range(1,n+1) for w in range(1,z))
    G = sum(ac-x for x in old)
    excluded = 0
    for z in range(1,n+1):
        for w in range(1,z):
            g = old[z-1]-old[w-1]
            fresh = sorted(ac-old[x-1] for x in range(1,n+1) if x not in (w,z))
            fresh_by_source[w,z] = fresh
            Sg = g*sum(fresh)
            excluded += g*((ac-old[w-1])+(ac-old[z-1]))
            S_total += Sg
            bank_terms.append({"w":w,"z":z,"g":g,"S_g":Sg})
    require(S_total == U*G-excluded == integer(item["six_distinct_source_bank"]),
            "full source bank mismatch")

    # All m columns are present; column j=q has zero weight, rather than being
    # compressed or confused with a dummy. Entries store (g*y,g*hmin,hmin,y).
    entries = {}
    for z in range(1,n+1):
        for q in range(1,m+1):
            matrix = []
            for w in range(1,z):
                row = []
                g = old[z-1]-old[w-1]
                fresh = fresh_by_source[w,z]
                for j in range(1,m+1):
                    y = g+future[q-1]-future[j-1]
                    pos = bisect_left(fresh,y) if j != q and y > 0 else len(fresh)
                    row.append(None if pos == len(fresh) else (g*y,g*fresh[pos],fresh[pos],y))
                matrix.append(row)
            entries[z,q] = matrix

    require(item["record_source"] == config["record_source"], "unexpected record bank")
    record_source = read(item["record_source"],item["record_source_sha256"])
    if name.startswith("A70"):
        check_declared(record_source)
        require(record_source["UNKNOWN"] == 0, "saved selector contains UNKNOWN")
        records = [r["record"] for r in record_source["records"] if r["category"] != "paid_sparse_support"]
        record_scope = "The 125 certified A65-unpaid residual rows; not all original core records of the history."
    else:
        records = record_source["records"]
        require(records == [source["selected_record"]] and history["core_records"] == 1,
                "wrong existing A72 one-record bank")
        record_scope = "The sole original strict-core record of the certified M50 history."
    require(len(records) == config["record_count"] == item["original_record_count"], "record count mismatch")
    actual_nodes = defaultdict(list)
    seen_rows,seen_sources = set(),set()
    orientation_counts = {"fresh_larger":0,"fresh_smaller":0}
    orientation_mass = {"fresh_larger":0,"fresh_smaller":0}
    actual_rows = []
    for index,row in enumerate(records):
        require(len(row) == 11, "wrong original record schema")
        d,e,xd,yd,xe,ye,birth,s,i,r,t = map(integer,row)
        require(tuple(row) not in seen_rows, "physical record counted twice")
        seen_rows.add(tuple(row))
        require(1 <= xd < yd <= c and 1 <= xe < ye <= c and max(yd,ye) == birth == c
                and min(yd,ye) == s and c < b < i < r <= min(k,history["T"])
                and len({xd,yd,xe,ye,i,r}) == 6, "original source/cut endpoint scope mismatch")
        require(d == a[yd-1]-a[xd-1] > e == a[ye-1]-a[xe-1] > 0
                and t == d-e == a[r-1]-a[i-1] > 0, "original integer record arithmetic mismatch")
        if yd == c:
            x,w,z,h,g = xd,xe,ye,d,e
            q,j,orientation = r-b,i-b,"fresh_larger"
        else:
            require(ye == c, "no fresh source")
            x,w,z,h,g = xe,xd,yd,e,d
            q,j,orientation = i-b,r-b,"fresh_smaller"
        require(1 <= w < z < c and 1 <= x < c and x not in (w,z)
                and 1 <= q <= m and 1 <= j <= m and j != q,
                "common mixed-node coordinates out of domain")
        require((j < q) == (h > g) and abs(h-g) == t and differences[t] == (i,r)
                and differences[g] == (w,z) and differences[h] == (x,c),
                "source orientation or unique endpoint recovery mismatch")
        require((w,z,x) not in seen_sources, "physical source reused across orientations/nodes")
        seen_sources.add((w,z,x))
        require(old[w-1]+future[j-1] == old[z-1]+future[q-1]+old[x-1]-ac,
                "common mixed-sum identity failed")
        ent = entries[z,q][w-1][j-1]
        require(ent is not None and ent[2] == ent[3] == h and ent[0] == ent[1] == g*h == d*e,
                "actual hmin/full product identity failed")
        actual_nodes[z,q].append((w,j,x,g*h))
        orientation_counts[orientation] += 1
        orientation_mass[orientation] += g*h
        actual_rows.append({"record_index":index,"record":row,"w":w,"z":z,"fresh_x":x,
                            "q":q,"j":j,"g":g,"h":h,"orientation":orientation,"product":g*h})
    node_products = {}
    for node,edges in actual_nodes.items():
        require(len(edges) == len({e[0] for e in edges}) == len({e[1] for e in edges})
                == len({e[2] for e in edges}), "actual node row/column/fresh projection is not injective")
        node_products[f"{node[0]},{node[1]}"] = sum(e[3] for e in edges)
    Q = sum(node_products.values())
    require(node_products == item["node_actual_products"] and Q == item["full_actual_product"]
            == sum(orientation_mass.values()) <= S_total, "actual Q or node totals mismatch")
    alpha = lambda r:Fraction(1,r*r*(r-1)*(r-1))
    coefficient = (alpha(k)-alpha(k+1))/(a[k-1]-a[0])**2
    return {"name":name,"config":config,"n":n,"m":m,"source_bank":S_total,"source_terms":bank_terms,
            "source_bank_crosscheck":{"U":U,"G":G,"excluded_endpoint_products":excluded},
            "entries":entries,"actual_nodes":actual_nodes,"actual_rows":actual_rows,"Q":Q,
            "record_scope":record_scope,"orientation_counts":orientation_counts,
            "orientation_mass":orientation_mass,"positive_differences_checked":len(differences),
            "mixed_sum_vertices_checked":len(mixed_sums),"lambda":coefficient}


def check_theta(cell,case):
    theta = Fraction(case["theta_exact"])
    require(theta in (Fraction(0),Fraction(1,2),Fraction(1)), "theta outside prescribed set")
    p,den = theta.numerator,theta.denominator
    require(integer(case["numerator"]) == p and integer(case["denominator"]) == den,
            "rational scaling mismatch")
    n,m = cell["n"],cell["m"]
    require(len(case["nodes"]) == n*m, "wrong number of node certificates")
    seen,results = set(),[]
    total = inequalities = positive_assignments = 0
    for node in case["nodes"]:
        z,q = integer(node["z"]),integer(node["q"])
        require(1 <= z <= n and 1 <= q <= m and (z,q) not in seen, "duplicate/invalid node")
        seen.add((z,q))
        N = max(z-1,m)
        left,right = list(map(integer,node["dual_left"])),list(map(integer,node["dual_right"]))
        assignment = list(map(integer,node["assignment"]))
        require(len(left) == len(right) == len(assignment) == N
                and sorted(assignment) == list(range(N)), "invalid padded assignment or dual dimension")
        W = [[0]*N for _ in range(N)]
        for w in range(1,z):
            for j in range(1,m+1):
                ent = cell["entries"][z,q][w-1][j-1]
                if ent is not None:
                    W[w-1][j-1] = max(den*ent[0]-p*ent[1],0)
        require(all(W[w][q-1] == 0 for w in range(N)), "same-future column must be forbidden")
        for w in range(N):
            for j in range(N):
                require(left[w]+right[j] >= W[w][j], "integer assignment dual inequality failed")
                inequalities += 1
        primal = sum(W[w][assignment[w]] for w in range(N))
        value = integer(node["value_scaled"])
        require(value >= 0 and primal == value == sum(left)+sum(right), "nonzero primal-dual gap")
        positive_assignments += sum(W[w][assignment[w]] > 0 for w in range(N))
        actual = cell["actual_nodes"].get((z,q),[])
        actual_value = 0
        for w,j,x,product in actual:
            require(W[w-1][j-1] == (den-p)*product, "actual residual must equal (1-theta)gh")
            actual_value += W[w-1][j-1]
        require(actual_value <= value, "actual node mass exceeds matching optimum")
        total += value
        results.append({"z":z,"q":q,"matching_value_scaled":value,
                        "actual_residual_scaled":actual_value,"primal_dual_gap":0})
    bound = Fraction(p*cell["source_bank"]+total,den)
    require(total == integer(case["matching_sum_scaled"]) and bound == Fraction(case["bound_exact"]),
            "full source-plus-matching bound mismatch")
    require(cell["Q"] <= bound, "actual full product exceeds allowance")
    if theta == 1:
        require(total == 0 and bound == cell["source_bank"], "theta=1 endpoint identity failed")
    return {"theta_exact":str(theta),"bound_exact":str(bound),"matching_sum_scaled":total,
            "source_cost_exact":str(theta*cell["source_bank"]),
            "bound_minus_actual_Q_exact":str(bound-cell["Q"]),
            "nodes":n*m,"dual_inequalities_checked":inequalities,
            "positive_assignment_edges":positive_assignments,"all_primal_dual_gaps_zero":True,
            "all_actual_node_residuals_bounded":True,"node_results":results,
            "genuine_component_allowance_exact":str(cell["lambda"]*bound)}


def main():
    cert = read("A76_FULL_MASS_EXACT.json")
    check_declared(cert)
    require(len(cert["results"]) == 2 and {r["input"] for r in cert["results"]} == set(CONFIG),
            "only the two saved inputs are in scope")
    results = []
    for item in cert["results"]:
        cell = reconstruct(item)
        require(len(item["cases"]) == 3 and {Fraction(c["theta_exact"]) for c in item["cases"]}
                == {Fraction(0),Fraction(1,2),Fraction(1)}, "wrong three-theta certificate set")
        checks = [check_theta(cell,c) for c in item["cases"]]
        minimum = min(Fraction(c["bound_exact"]) for c in checks)
        require(minimum == Fraction(item["minimum_tested_bound_exact"]), "three-point minimum mismatch")
        results.append({"input":cell["name"],"campaign":cell["config"],"record_scope":cell["record_scope"],
                        "original_record_count":len(cell["actual_rows"]),"actual_Q":cell["Q"],
                        "orientation_counts":cell["orientation_counts"],"orientation_product_mass":cell["orientation_mass"],
                        "physical_sources_unique_across_all_nodes_and_orientations":True,
                        "all_original_source_output_endpoint_arithmetic_passed":True,
                        "all_actual_node_row_column_and_fresh_projections_injective":True,
                        "actual_records":cell["actual_rows"],"six_distinct_source_bank":cell["source_bank"],
                        "source_bank_terms":cell["source_terms"],"source_bank_crosscheck":cell["source_bank_crosscheck"],
                        "positive_differences_checked":cell["positive_differences_checked"],
                        "mixed_sum_vertices_checked":cell["mixed_sum_vertices_checked"],
                        "lambda_k_exact":str(cell["lambda"]),
                        "actual_genuine_component_mass_exact":str(cell["lambda"]*cell["Q"]),
                        "cases":checks,"minimum_of_three_tested_bounds_exact":str(minimum),
                        "all_theta_optimality_claimed":False})
    bind("A76_FULL_MASS_REVIEW.md")
    bind(Path(__file__).name)
    output = {"attempt":"A76","status":"PASS_INDEPENDENT_TWO_ORIENTATION_FULL_MASS_CERTIFICATES",
              "scope":"Two saved cells, theta 0,1/2,1 only. Actual source/output arithmetic and all "
                      "assignment matrices independently reconstructed; no reference import or optimizer.",
              "results":results,"source_sha256":SOURCES,"unknown_comparisons":0,
              "limits":["The C1 input is the 125 A65-unpaid residual rows, not an all-core enumeration.",
                        "Original strict-gate/residual/cap certifications are reused from hash-bound artifacts.",
                        "No new history, full-profile scan, A72 profile-generator run, or Lean build.",
                        "Only a minimum among three theta values; no all-theta or vector-penalty optimality claim.",
                        "Auxiliary matching edges need not be original records and receive no original output price.",
                        "No all-history/cut/component uniform norm or frozen U4F/Q1 conclusion."]}
    destination = F/"A76_FULL_MASS_CHECK.json"
    destination.write_text(json.dumps(output,indent=2,ensure_ascii=False)+"\n")
    print(output["status"])
    for r in results:
        print(r["input"],"actual_Q",r["actual_Q"],"orientations",r["orientation_counts"],
              "source_bank",r["six_distinct_source_bank"])
        print("three_bounds",[c["bound_exact"] for c in r["cases"]])
    print("output_sha256",sha256(destination.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()

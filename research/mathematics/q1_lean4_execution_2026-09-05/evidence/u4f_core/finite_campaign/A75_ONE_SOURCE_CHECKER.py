#!/usr/bin/env python3
"""Independent one-source penalty check; no reference imports or optimization."""
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json


F = Path(__file__).resolve().parent
SOURCES = {}


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def integer(x):
    require(type(x) is int, "integer certificate value required")
    return x


def bind(name, expected=None):
    require(Path(name).name == name, "local source filename required")
    data = (F/name).read_bytes()
    digest = sha256(data).hexdigest()
    require(expected is None or expected == digest, "hash mismatch: "+name)
    require(name not in SOURCES or SOURCES[name] == digest, "source changed during check")
    SOURCES[name] = digest
    return data


def read(name, expected=None):
    return json.loads(bind(name,expected))


def main():
    cert = read("A75_ONE_SOURCE_PENALTY_EXACT.json")
    for name, digest in cert["source_sha256"].items():
        bind(name,digest)
    source = read("A70_FEASIBLE_MATCHING_EXACT.json")
    for name, digest in source["source_sha256"].items():
        bind(name,digest)
    history = read("C1_m02_dense_variant1_M96.json")
    a = history["a"]
    require(history["M"] == history["T"] == len(a) == 96
            and Fraction(history["C_exact"]) == 1 and history["m0"] == 2,
            "fixed C1,m02,M=T96 history changed")
    c,b,k = 24,25,48
    old,future,ac = a[:c-1],a[b:k],a[c-1]
    require(old == source["old_values"] and future == source["future_values"]
            and ac-a[0] == source["H_c"] == 713, "cell reconstruction mismatch")
    selected_w,selected_z = map(integer,cert["physical_old_pair"])
    require((selected_w,selected_z) == (1,16), "only the prescribed source is authorized")
    g_selected = old[selected_z-1]-old[selected_w-1]
    require(g_selected == cert["g"] == 283, "selected old difference mismatch")
    theta = Fraction(cert["theta_exact"])
    require(theta == Fraction(1,1000) and cert["numerator"] == 1 and cert["denominator"] == 1000,
            "wrong prescribed penalty")
    denominator = 1000
    terms = [{"x":x,"h":ac-old[x-1],"positive_source_cost":g_selected*max(ac-old[x-1]-g_selected,0)}
             for x in range(1,len(old)+1) if x not in (selected_w,selected_z)]
    Bselected = sum(t["positive_source_cost"] for t in terms)
    require(Bselected == integer(cert["B_selected_source"]) == 1463959, "source cost mismatch")

    # Read back the independently checked A74 theta-zero certificate, rather
    # than rerunning its unchanged 506 node matrices or its optimizer.
    baseline = read("A74_PARAMETRIC_DUAL_EXACT.json")
    checked = read("A74_PARAMETRIC_DUAL_CHECK.json")
    require(checked["status"] == "PASS_INDEPENDENT_GLOBAL_PARAMETRIC_MINIMUM_CERTIFICATE",
            "missing independent A74 success")
    for name,digest in checked["source_sha256"].items():
        bind(name,digest)
    baseline_item = next(r for r in baseline["results"] if r["input"] == "A70_FEASIBLE_MATCHING_EXACT.json")
    checked_item = next(r for r in checked["results"] if r["input"] == "A70_FEASIBLE_MATCHING_EXACT.json")
    require(Fraction(baseline_item["optimum_theta_exact"]) == 0
            and checked_item["global_minimum_certified"] is True
            and Fraction(checked_item["optimum_theta_exact"]) == 0,
            "wrong scalar baseline")
    baseline_nodes = {(n["z"],n["q"]):n["value_scaled"] for n in baseline_item["upper_node_duals"]}
    checked_nodes = {(n["z"],n["q"]):n["value_scaled"]
                     for n in checked_item["upper_certificate"]["node_results"]}
    require(len(baseline_nodes) == len(baseline_item["upper_node_duals"]) == 529
            and baseline_nodes == checked_nodes, "node values differ from independently checked A74")
    previous = sum(baseline_nodes.values())
    require(previous == Fraction(cert["previous_scalar_optimum_exact"])
            == Fraction(checked_item["minimum_D_exact"]) == 80331512, "scalar optimum mismatch")
    unchanged_nodes = {key:value for key,value in baseline_nodes.items() if key[0] != selected_z}
    require(len(unchanged_nodes) == 506, "wrong unchanged node count")
    unchanged = sum(unchanged_nodes.values())
    old_changed = previous-unchanged
    require(unchanged == Fraction(cert["unchanged_node_sum_exact"])
            and old_changed == cert["old_changed_node_sum"], "baseline split mismatch")

    new_values, node_results = {}, []
    comparisons = 0
    require(len(cert["nodes"]) == 23, "only 23 changed nodes required")
    for node in cert["nodes"]:
        z,q = integer(node["z"]),integer(node["q"])
        require(z == selected_z and 1 <= q <= len(future) and q not in new_values,
                "invalid or duplicate changed node")
        N = max(z-1,q-1)
        left = list(map(integer,node["dual_left"]))
        right = list(map(integer,node["dual_right"]))
        assignment = list(map(integer,node["assignment"]))
        require(len(left) == len(right) == len(assignment) == N
                and sorted(assignment) == list(range(N)), "invalid assignment/dual dimensions")
        W = [[0]*N for _ in range(N)]
        for w in range(1,z):
            g = old[z-1]-old[w-1]
            fresh = [ac-old[x-1] for x in range(1,len(old)+1) if x not in (w,z)]
            for j in range(1,q):
                t = future[q-1]-future[j-1]
                candidates = [h for h in fresh if h >= g+t]
                if candidates:
                    hmin = min(candidates)
                    penalty = g*(hmin-g) if w == selected_w else 0
                    W[w-1][j-1] = max(denominator*g*t-penalty,0)
        for w in range(N):
            for j in range(N):
                require(left[w]+right[j] >= W[w][j], "changed-node dual inequality failed")
                comparisons += 1
        value = integer(node["value_scaled"])
        primal = sum(W[w][assignment[w]] for w in range(N))
        require(value >= 0 and value == primal == sum(left)+sum(right), "changed-node primal-dual gap")
        new_values[q] = value
        node_results.append({"z":z,"q":q,"old_value":baseline_nodes[z,q],"new_value_scaled":value,
                             "matrix_size":N,"dual_inequalities":N*N,"primal_dual_gap":0})
    changed_total = sum(new_values.values())
    require(changed_total == cert["new_changed_node_sum_scaled"], "new node sum mismatch")
    new_bound = unchanged+Fraction(Bselected+changed_total,denominator)
    gain = previous-new_bound
    require(new_bound == Fraction(cert["new_bound_exact"]) == Fraction(80330799689,1000),
            "new source-dependent bound mismatch")
    require(gain == Fraction(cert["gain_exact"]) == Fraction(712311,1000) > 0
            and cert["strict_improvement"] is True, "strict gain not certified")

    # Direct arithmetic on the same 125 previously certified A65-unpaid rows.
    bank = read("A65_SPARSE_FIBER_FOLLOWUP_EXACT.json")
    rows = [r["record"] for r in bank["records"] if r["category"] != "paid_sparse_support"]
    require(len(rows) == 125 and bank["UNKNOWN"] == 0, "wrong existing actual subset")
    actual_nodes = defaultdict(list)
    seen_sources,seen_rows = set(),set()
    beta = selected_actual = 0
    for row in rows:
        d,e,x,y,w,z,birth,s,i,r,t = map(integer,row)
        require(tuple(row) not in seen_rows, "duplicate physical actual row")
        seen_rows.add(tuple(row))
        require(birth == c == max(y,z) and min(y,z) == s and c < b < i < r <= k
                and len({x,y,w,z,i,r}) == 6, "actual cut/endpoint scope mismatch")
        require(d == a[y-1]-a[x-1] > e == a[z-1]-a[w-1] > 0
                and d-e == t == a[r-1]-a[i-1] > 0, "actual record arithmetic mismatch")
        if y != c:
            continue
        require((w,z,x) not in seen_sources, "physical source reused")
        seen_sources.add((w,z,x))
        charge = e*t
        penalty = charge if (w,z) == (selected_w,selected_z) else 0
        selected_actual += penalty
        beta += charge
        actual_nodes[z,r-b].append((w,i-b,denominator*charge-penalty))
    actual_node_results = []
    for (z,q),edges in actual_nodes.items():
        require(len(edges) == len({e[0] for e in edges}) == len({e[1] for e in edges}),
                "actual positive right-node edges are not a matching")
        used = sum(e[2] for e in edges)
        allowance = new_values[q] if z == selected_z else denominator*baseline_nodes[z,q]
        require(used <= allowance, "actual residual exceeds a node optimum")
        actual_node_results.append({"z":z,"q":q,"actual_residual_scaled":used,
                                    "allowance_scaled":allowance})
    require(selected_actual <= Bselected and beta == cert["actual_Beta"] == checked_item["actual_Beta"]
            == 8716524 and beta <= new_bound, "actual positive source-charge check failed")
    bind("A74_SOURCE_DUAL_REVIEW.md")
    bind(Path(__file__).name)
    result = {
        "attempt":"A75","status":"PASS_INDEPENDENT_ONE_SOURCE_STRICT_IMPROVEMENT",
        "scope":"One prescribed source on the existing C1,m02,M=T96,c24,b25,k48 cell. "
                "23 changed nodes checked directly; 506 unchanged nodes reused from hash-bound independent A74 proof.",
        "physical_old_pair":[selected_w,selected_z],"g":g_selected,"theta_exact":str(theta),
        "B_selected_source":Bselected,"source_terms":terms,
        "unchanged_nodes_reused":len(unchanged_nodes),"unchanged_node_sum":unchanged,
        "old_changed_node_sum":old_changed,"new_changed_node_sum_scaled":changed_total,
        "changed_nodes":node_results,"dual_inequalities_checked":comparisons,
        "all_changed_primal_dual_gaps_zero":True,
        "previous_all_scalar_theta_minimum_exact":str(Fraction(previous)),
        "new_bound_exact":str(new_bound),"strict_gain_exact":str(gain),
        "actual_record_count":len(rows),"actual_positive_record_count":len(seen_sources),
        "actual_Beta":beta,"actual_selected_source_charge":selected_actual,
        "actual_node_results":actual_node_results,"all_actual_node_residuals_bounded":True,
        "unknown_comparisons":0,"source_sha256":SOURCES,
        "limits":["No claim of optimization over all source-dependent theta values.",
                  "Original strict/cap/residual memberships are reused, not re-enumerated.",
                  "No new history, profile, reference import, optimizer, or Lean build.",
                  "Auxiliary absent matching edges are not assigned original prices.",
                  "No full Q bound, uniform norm closure, frozen U4F result, or Q1 conclusion."]}
    destination = F/"A75_ONE_SOURCE_CHECK.json"
    destination.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
    print(result["status"])
    print("bound",new_bound,"strict_gain",gain,"actual_Beta",beta,"selected_actual",selected_actual)
    print("dual_inequalities",comparisons)
    print("output_sha256",sha256(destination.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()

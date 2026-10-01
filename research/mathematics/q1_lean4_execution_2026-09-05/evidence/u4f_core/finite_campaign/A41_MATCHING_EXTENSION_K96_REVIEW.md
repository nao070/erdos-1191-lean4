# A41 bounded matching check at the one additional horizon

Date: 2026-09-09. Status: PASS exact finite check; no strict two-edge
chain was found. This is not a general matching proof.

After preserving the initial b25,k=v48 two-shift evidence, the parent
authorized exactly one further cell: the same certified C=1,m0=2
variant M=T=96, b=25, e=48=a_9-a_6, and k=v=96. No other shift,
cut, horizon or history was added.

The existing graph/strict-gate/independent-helper comparison code was
reused in A41_matching_extension_b25_k96.py. The original saved M96
record bank was queried only for this shift, cut and component; no
new full-core bank or profile was generated. All strict graph records
agree exactly with those original rows, and all-large selection was
independently checked. UNKNOWN comparisons: zero.

The exact values are:

- 24 old points, 71 future points, 1704 distinct mixed vertices.
- Same-future forced edges: 71.
- Future-decreasing edges: 47; future-increasing edges: 65.
- Future-decreasing edges excluding the two fixed old source rows: 43.
- Strict original core edges: 31; all-large strict edges: 23.
- Strict sum de: 513936; all-large sum de: 358752.
- Genuine component coefficient: 1/1259618724663197400.

The strict graph has 31 maximal nontrivial paths, all of edge length1.
The all-large subgraph has 23 such paths, also all of length1. Their
maximum in/out degrees are1 and maximum total degree is1. Thus there
is no minimal strict two-edge chain or pair of chain records to save.
The full exact JSON still preserves every mixed vertex, graph edge,
original strict record/index and maximal path.

The same e48 path-length upper bound is14, so it does not explain
this matching observation by forcing length at most1. General matching
remains unproved and unrefuted by the prescribed finite checks.
No additional cell or shift was examined after this result.

The component coefficient is the actual terminal kappa_96/H_96^2;
alpha_97 was not replaced by zero. This finite graph test says nothing
by itself about uniform CoreUniform or Q1. The extension's source and
evidence hashes are in A41_A43_followup_review_manifest.json.

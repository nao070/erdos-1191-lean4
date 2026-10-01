# A41 independent review: two actual shifts and strict-core paths

Date: 2026-09-09. Status: PASS for the prescribed finite comparison
and the path statements below. The matching candidate has no
counterexample in this one cell; no general matching theorem is
inferred from that absence.

## Exactly one cell and two shifts

Use only the existing certified C=1,m0=2 variant M=T=96, cut b=25,
and component/output horizon k=v=48. There are n=24 old points
(ranks 1..24), m=23 future points (ranks 26..48), and exactly
nm=552 distinct actual mixed vertices U=a_r-a_y. The old shifts are

    e=48=a_9-a_6=67-19,
    e=422=a_20-a_6=441-19.

Construct every edge U->U+e in this finite vertex set. Write the
endpoint representations as U=(y,r), U+e=(x,i). The same-future
case i=r has (x,y)=(w,z), the unique old pair representing e, so
there are exactly m=23 forced edges for each shift. A strict original
core edge has i<r and d=a_y-a_x=e+(a_r-a_i)>e, hence x<y.

| shift | same future | future decreases | future increases | decreasing, source-disjoint | strict core | all-large core |
|---:|---:|---:|---:|---:|---:|---:|
|48|23|28|43|27|23|17|
|422|23|3|58|3|3|2|

Source-disjoint means that x,y,w,z are four distinct old ranks;
the distinct future ranks then give the six endpoints. Every
strict edge was checked with the original reference rank/physical
gates and the independent strict helpers. The all-large test uses
all three adjacent old physical gaps and the same strict threshold
c_birth^2/(log c_birth)^3. There were zero UNKNOWN comparisons.

The resulting original record rows agree exactly with the existing
A29 source-indexed record pool for these two shifts and this cell.
Each of those indices was then read directly from the original
M96 bank and matched. No other cell or shift, and no full profile,
was enumerated.

| shift | strict sum de | all-large sum de | priced strict sum | priced all-large sum |
|---:|---:|---:|:---|:---|
|48|358752|248784|3737/11963738315592|5183/23927476631184|
|422|789140|548178|197285/287129719574208|91363/191419813049472|

Both use the same genuine kappa_48/H_48^2=1/1148518878296832.
No component coefficient, terminal alpha or cut interval was changed.

## Path distributions and scope of the matching test

Path length below means number of edges in a maximal nontrivial
directed path. The full shift graph, before original core conditions,
has these distributions:

    e48: 65 paths of length1, 13 of length2, 1 of length3;
    e422: 59 paths of length1, 11 of length2, 1 of length3.

Its maximum in/out degrees are each1, with maximum total degree2.
In contrast the strict graph has 23 paths of length1 for e48 and
3 paths of length1 for e422. The all-large subgraph has respectively
17 and2 paths, also all of length1. Their maximum total degree is1.
Thus both tested strict graphs are matchings, and neither has a
minimal two-edge strict chain to report. Raw shift paths are not
counterexamples to the strict-core matching candidate.

The evidence includes every vertex, edge, original row/index and
maximal path. Its isolated-vertex counts use all552 mixed vertices
as the common ambient set, including the rows excluded by the
smaller source endpoints. These are not claims that all ambient
vertices are eligible strict endpoints.

## General strict path law, independently checked

Fix any one actual old difference e=a_z-a_w>0 at one cut b. All
mixed labels are unique, so the graph U->U+e has in/out degree at
most1. A directed cycle is impossible since its labels increase
strictly. Any strict-core subgraph is therefore a family of directed
paths. Each strict edge (y,r)->(x,i) has x<y and i<r; both endpoint
ranks decrease along a path. Six-endpoint distinctness excludes old
rows w and z from every strict vertex, leaving at most (n-2)m
possible vertices.

For a nontrivial path of length L, let D_path and F_path be the
physical spans between its first and last old and future endpoints.
Telescoping the actual edge identities gives

    sum_edges d=D_path=L e+F_path<=H_{b-1}.

Each strict output t is an integer at least
ell_b=floor(b^2/(log b)^5)+1, by the unchanged original core bound
used in A28. Both rank paths have no repeated endpoint, so

    L<=min(n-3, m-1, floor(H_{b-1}/(e+ell_b))).    (1)

This applies to nontrivial paths; if too few endpoints exist, there
are no edges. An upper bound in (1) at most1 is a sufficient matching
condition. A value greater than1 merely leaves longer paths possible
under this bound; it neither proves their existence nor disproves
matching by some stronger argument.

Here H24=713 and ell25=2. Thus e422 has length bound1, which explains
the matching result structurally. For e48 the bound is14, so its
observed matching is only evidence for this one cell.

## Future addition extends existing paths at their beginning

Keep b and e fixed and increase v by one. The original strict gates
of existing endpoint records do not depend on v, so no old strict
edge disappears or changes status. Any new strict edge must use
r=v+1 as its larger output endpoint; i<r belongs to the old future
set. Therefore its tail is a new vertex (y,v+1) and its head is an
old vertex (x,i).

The new tail has no incoming strict edge, since such an edge would
need a still larger future endpoint. Its target also had no incoming
strict edge before the addition: an old incoming tail would have
the same numeric label U=V-e as this new tail, contradicting actual
mixed-label uniqueness. New edges have distinct targets and tails,
and no new edge links two new-future vertices.

Thus each new edge either extends an existing path at its beginning
or creates a path by entering a previously isolated old vertex. It
does not merge two old nontrivial paths. The terminal old/future
endpoint pair of a path remains fixed after that path is created.
No strict condition is dropped in this argument.

These facts do not bound the number of paths or their total original
weighted norm. In particular paying each path by H_{b-1} without
controlling how many paths occur does not finish the global estimate.
The two finite shifts were not expanded into a new campaign.

## Evidence binding

A41_two_shift_graph_b25_k48.py is the single bounded calculation;
A41_two_shift_graph_b25_k48_exact.json contains the complete exact
result and source hashes. Reference versus independent strict gates,
the original indexed rows, source exclusion and all-large selection
were all checked. The companion A41_A42_review_manifest.json binds
this evidence and the present hand proof. No new Lean build was run.

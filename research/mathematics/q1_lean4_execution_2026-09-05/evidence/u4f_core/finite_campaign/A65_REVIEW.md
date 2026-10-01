# A65 bounded sparse-fiber follow-up: independent read-only review

Date: 2026-09-09. Status: PASS.

Scope is exactly the 126 independently certified A62 survivors in the
existing C=1,m0=2,M=T=96 history at b25,k48. All survivors have c24;
the prescribed c23 domain was already empty after A53. I inspected the
new script and saved evidence, verified every bound source hash, and
checked the saved mass arithmetic and old-component edge sets. I did not
generate a history, rerun an original record/profile scan, or rewrite
the root's script/evidence.

The script correctly constructs F3 in two ways: all increasing triples
of old ranks, and increasing pairs followed by an actual old-value
lookup whose recovered rank is larger than the pair. Both enumerate
exactly the unordered THREE-DISTINCT-point subsets with sum
3(a_c-g), including triples that do not generate any core record.
The support-disjointness assertion agrees with A62's Sidon proof.

For p=5/2, q <= c/(log c)^(5/2) is equivalent to
q^2*(log c)^5 <= c^2, since all terms are nonnegative. The script's
upper/lower rational logarithm comparisons correctly handle the
non-strict sparse inequality and its strict complement. It compares
both existing interval methods and raises UNKNOWN rather than assigning
an unresolved comparison. The saved UNKNOWN count is zero.

| Classification | Records | Sum of actual products |
| --- | ---: | ---: |
| Paid sparse support | 1 | 205,860 |
| Unpaid rich support | 3 | 676,152 |
| Unpaid outside support | 122 | 21,245,887 |

The sums total the original selected-cell product mass 22,127,899.
Each saved component price is exactly the corresponding sum multiplied
by lambda48=1/1,148,518,878,296,832. These totals are component48 masses,
not sums of the original full u_r^[96] prices. Membership in the new
A64 class is static and can nevertheless pay the whole original record
by that hand theorem; no missing record receives a price here.

The paid record is bank index 12292,
[705,292,4,24,17,22,24,22,39,42,413]. Its old g=292 has the single
triple of ranks (4,22,23), with point values 9,604,653 summing to
1266=3*(714-292). Its fresh lower rank 4 belongs to this sparse support.
The three supported but rich records are indices 7985,8105,9864 at
g=537,539,400; each respective fiber has q=2.

The saved field old_components_with_at_least_two_unpaid_edges is
properly named. In general, retaining two edges of an old component
does not prove that the retained edges remain connected. In this data,
the stronger all_edges_still_unpaid flag is true for all seven old
components of length at least two, and I directly checked their edge
sets against A62. Those components at g=163,214,227,284,292,318,334
therefore survive intact. The single paid edge is in a different,
one-edge component, including at g=292. No connectivity conclusion
after a partial component deletion is used.

This is only a finite classification of the prescribed records. It
does not prove a frequency estimate for rich centers or resolve the
remaining core norm or Q1. No new Lean verification is claimed.

Source bindings checked in this review:

- A65_sparse_fiber_followup.py:
  9e4cdd4990d203c83c2a8981854dc4943789b893acd7af28e30e8c7d6a60b556
- A65_SPARSE_FIBER_FOLLOWUP_EXACT.json:
  0fca7f0a59c48f0694afca5b720aa4c4946ad2db2c3f853f69dd26c3917ca6e9
- A62_CELL_MANIFEST.json:
  a28068a76ed54d0bacec78b13e25df8e73efbf6a5aaefe1db58e230f5d70cd38

Every source_sha256 entry in the A65 evidence matched its current file.
The task is complete; no process remains running.

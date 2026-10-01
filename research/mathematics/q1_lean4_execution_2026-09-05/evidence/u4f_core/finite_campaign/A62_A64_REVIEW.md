# Independent review of A62–A64

Date: 2026-09-09. Status: PASS after one wording correction.
Scope: the three new hand-proof sections and the one prescribed C2,m0=2,
M=T=19 certificate. The separate C1,b25,k48,c23/24 finite task is recorded
in A62_CELL_MANIFEST.json and is not merged into the C2 campaign.

## A62: actual cycle source means and triangle injection

The identities follow from the reviewed A59 signed boundary law. For an
actual cycle the signed output sum is zero, so summing
a_x=K-sigma*t and gh=g^2+sigma*g*t gives sum a_x=L*K and
sum gh=L*g^2. The fresh lower endpoints are distinct actual old ranks.

At the middle future vertex of a triangle, opposite-color incoming and
outgoing edges are forbidden. Therefore the two consecutive edges have
one common color and the closing edge has the other. Their three fresh
old values have the displayed forms and sum to 3K.

If two actual three-distinct-point subsets with sum 3K share a point,
cancel it. Sidon uniqueness of the remaining unordered two-sums makes
the two triples identical. Thus distinct triples have disjoint supports
and 3q <= c-1. The three fresh lower values determine |K-a_x|; actual
positive-difference uniqueness then determines each physical output
pair. Hence two actual triangles cannot map to the same triple.
The c-3 source bound excludes the two endpoints of the fixed old source;
the future-vertex bound uses disjoint triangle components in a degree-two
graph. Consequently all three bounds on tau, and the exact triangle mass
3g^2*tau, are valid.

The exact priced formula is the sum over k of lambda_k times the actual
triangle mass in G_(c,g;b,k). Upper output ranks can differ between the
three edges. A common u_r is not an exact triangle price. In particular,
an edge can appear as part of a path before the last edge closes a cycle.
The source triple condition alone does not assert output realization or
core eligibility.

## A63: read-only reproduction of the prescribed triangle certificate

I inspected A63_triangle_certificate.py and ran it with Path.write_text
intercepted only to compare against the existing saved artifacts. No
existing output was rewritten. The first strict byte comparison stopped
because elapsed_seconds changed; inspection isolated that sole difference.
The completed replay compared every mathematical JSON field exactly while
allowing that observed runtime field to differ. The records, independent
checker result, and triangle certificate were byte-identical to the saved
files. The completed replay exited 0.

Both existing evaluators passed the one actual history: 59 original core
records, unique positive differences and repeated two-sums, every rank's
C=2,m0=2 cap, genuine prices, exact profile and dyadic I values. The
specified fixed(c11,g200;b12,k19) original cell consists of exactly the
three saved records. Their products 44,000, 49,200 and 26,800 sum to
120,000=3*200^2. They form triangle 17–18–19 with colors +,+,-.
The old fresh values 379,353,465 sum to 1197=3*399. The corresponding
mirror values 419,445,333 are absent from the old prefix.

Every original strict gate and every displayed A46.6/A53/A54/A57 flag is
certified by both rational logarithm implementations. UNKNOWN is zero.
The saved full u18 and u19 retain alpha20; the selected component19
prices are separate. Passing component19 does not assert that all earlier
components pass its displayed remainder selector.

This actual triangle refutes universal forest and bipartite candidates
with those displayed conditions. It does not refute an eventual theorem
with a separately proved threshold or claim survival of unspecified
already-paid initial ranges. This one fixed-cap finite history provides
no unbounded family or counterexample to CoreUniform/Q1. The printed N
and cap utilization are Decimal presentations, not certified enclosures.

## A64: uniform full-price sparse three-sum-support class

For a fixed actual old g, each fresh lower x supports at most one physical
output, since its positive difference |a_c-a_x-g| has a unique actual
output pair. A source triple contributes at most 3g^2: all three fresh
values are positive and sum to 3g. It is legitimate to enlarge the sum
to these three nonnegative products even when some do not generate core
records; no such missing record is assigned a genuine price.

Triple disjointness gives the product bound 3q(c,g)g^2. Restricting to
q <= c/(log c)^p, then enlarging only the nonnegative physical g bank,
and using u_r <= u_(c+2) gives

    E_c <= 3c S_(c-1) u_(c+2)/(log c)^p
        <= 3(c-1)^2/[4c^3(log c)^p]
        <= 3/[4c(log c)^p].

The bound uses the actual old variance estimate and the original
u_(c+2) <= 1/(c^4 H_c^2). A nonempty selected birth ensures that rank
c+2 exists. Empty births have zero mass. No cap or extension is assumed.

For a dyadic birth block ell >= 2, its total full-price mass is at most
3/[4(ell log 2)^p]. Original strict r<c log c places its covered cuts
strictly between 2^ell and 2^(ell+1)(ell+1)log 2. Their harmonic sum is
AT MOST W_ell=log[2(ell+1)log 2]. I requested this correction to the
initial wording that said the sum was equal to W_ell; root accepted it.
No numerical bound changes.

Each original record is priced once and contributes on its physical cut
interval. Thus I_ell <= E_ell W_ell, and weighted Cauchy gives
N_ell <= W_ell sqrt(E_ell). Summing with square-root subadditivity yields

    N_sparse <= sqrt(3)/(2(log 2)^(p/2))
                * sum_(ell>=2) W_ell / ell^(p/2).

This converges for p>2 and is uniform in the original finite horizons.
It includes the k>T genuine tail and the nonreset alpha_(M+1). This is
a full-record subclass estimate, not merely a total-mass bound. After
deletion an actual remaining triangle must have a rich source center
q>c/(log c)^(5/2). Other records and larger cycles are not thereby paid.
No estimate on all rich centers, remaining paths, or the whole core norm
has been established.

## Formal and execution scope

This review adds no Lean theorem, build, or toolchain change. A62 and A64
are hand proofs; the A63 result is exact finite computation with the
existing independent checker. The current core-uniform estimate and Q1
remain unresolved. Source, section, evidence and checker hashes are bound
in A62_A64_review_manifest.json. No task process remains running.

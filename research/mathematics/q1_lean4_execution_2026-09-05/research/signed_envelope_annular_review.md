# Independent review: the unspanned signed annular envelope

Reviewer: /root/causal_telescoping, GPT-6 Astra Ultra.
Review completed 2026-09-05, final binding checked at
2026-09-05 09:54:13 UTC.

**Verdict: mathematical PASS in the stated scope.** No material
correction was needed. The author applied one requested precision
about keeping the prescribed Q_j^2 normalization fixed.

Reviewed source:
research/signed_envelope_annular_lower_bound.md

Final reviewed SHA256:
b814d6e00292e26c66fd92d26d31d3cda5c5d1d272abbdc6429c428dc5bde5fb

The full source was first read at hash
96187c49a69b241cc16baead79ab60fd5d2f5c875563822696e808f879fb7ab8.
After the author changed the normalization sentence, the amended
paragraph and its surrounding scope were read and the final source
hash was measured. This records a follow-up binding, not a claim
that the initial read already saw the amended text.

The existing good-index input was read directly from
research/coherent_birth_linear_envelope.md, section 1; its observed
SHA256 was
0b9327dbed49d7086238954e9cb5d120b6864cb59bbb2597c8d6c2763bf35d00.
No prior finite numerical test was repeated, no new test was run,
and no Lean verification is claimed.

## 1. Signed source-pair counting

For the ordered Schur count A, summing D(t) over t in F counts
ordered pairs (d,t) whose positive sum is in F. Summing S(t)
over t in F counts the same ordered solutions. Therefore the
used signed correlation is exactly 2A+A=3A.

The kth smallest output z admits at most k-1 first summands,
so A<=q(q-1)/2. This counts x=y once, as required for the sole
opposite-sign pair {-x,x}. Subtracting from binom(2q,2) gives
(q^2+q)/2, and division by Q^2 gives exactly
1/8+1/(4Q). Equation (1) is correct.

The interval F={1,...,q} does attain the ordered-Schur upper
bound as a statement about arbitrary positive sets. The note
correctly makes no arbitrary-rank Sidon-realization claim for it.
The general bounded-feature lower and upper entry bounds are
valid without oddness or PSD. At a positive output there are
at most Q correlation pairs, which is sufficient for b/Q.

## 2. The linear lambda=1 endpoint

The split at H/2 is valid even when H is odd. Only the h^2
opposite-sign high/high pairs can have weight less than 1/2.
They are counted as ordered positive magnitudes, giving exactly
h^2 signed unordered pairs, including repeated magnitudes.

For h<=7q/10, one half of the remaining unused unit count is
at least q^2/200. For h>7q/10, the two same-sign high groups
have h(h-1) pairs and all outputs are strictly below H/2.
There are at most l possible old output labels in this range.
For one such positive output and one sign, translation on h
distinct real labels has at most h-1 realizations: its directed
graph consists of nontrivial increasing chains. Thus the used
count at those outputs is at most 2l(h-1).

The remainder is (h-1)(3h-2q). With q>=2 the high case implies
h>=2, and this exceeds 7q^2/200. Division by 4q^2 proves
the 1/800 constant. The fixed current-unused functional is affine
in lambda, so its bounds at 0 and 1 imply the same bound on
the full interval [0,1]. The q=1 exception is correctly stated;
actual ranks at least three avoid it.

## 3. Integer cutoff and annular overlap

There are floor(alpha Q_j)<=alpha Q_j positive integers satisfying
t<=alpha Q_j. The pointwise b/Q_j bound therefore discards at
most alpha b=c/2 mass, leaving at least c/2.

The support enlargement is valid because Q_j>=N_j^2/2 and
log(2N_j)=(j+1)log 2. For a fixed t in an enlarged annulus,
the exponent is bounded below by

~~~
log_4(t/[2C(J+1)log 2])
~~~

and strictly above by log_4(2t/alpha). The possible interval has
length at most log_4 R_J when nonempty. The chosen
2+ceil(log_4 R_J) bound is conservative for integer endpoints
and strict inequalities. The max(1,...) convention also covers
the case where the raw support-ratio bound is below one.

The pointwise inequality sums only the at most B_J active tails
at one physical label. Summing it proves equation (6) for the
literal single maximum, with no replicated row capacity.
Ties do not affect the argument.

## 4. Constants and the shifted good indices

For the linear rows, c=1/800 and b=2 give alpha=1/3200.
The support ratio is 12800C(J+1)log 2, and the resulting
capacity coefficient is 1/(1600B_J). Equation (7) is correct.
The constants are uniform for every choice lambda_j in [0,1].

The previous good-index lemma gives at least floor(M/L_M)
good k in [M,2M-1], with the exact L_M shown in (8).
The corresponding old rank is 2^(k+1), so the new exponent is
j=k+1 and ranges in [M+1,2M]. Choosing J=2M is correct,
including the rightmost endpoint. For fixed constants and a
fixed onset, both L_M and B_(2M) are O(log M). This proves
the stated Omega(M/(log M)^2) lower bound. A positive proportion
of good indices was not assumed.

## 5. Scope

The theorem concerns the prescribed Q_j^2-normalized, unspanned
current-unused kernels. The amended normalization paragraph
correctly avoids excluding arbitrary rescaling of both the full
kernel and its demand.

An actual future-span mask may remove the annular mass; the note
does not claim otherwise. A divergent capacity alone also gives
no sign or divergence for capacity minus actual demand. Neither
the signed Born theorem nor this packing argument supplies that
remaining estimate. The source states these boundaries explicitly.
The result is a proved supporting obstruction to a bounded
unspanned envelope shortcut, not a proof or disproof of original Q1.

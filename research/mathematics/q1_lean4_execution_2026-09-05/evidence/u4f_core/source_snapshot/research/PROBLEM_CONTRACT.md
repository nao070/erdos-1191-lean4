# Erdős Problem #1191 Q1 — Problem Contract

Checkpoint date: 2026-09-09 (Asia/Tokyo)  
Research status: **OPEN / ACTIVE; this file is a statement contract, not a proof.**

## 1. Authoritative statement

Primary current source: [Erdős Problems #1191](https://www.erdosproblems.com/1191), checked on 2026-09-09. The site states Q1 as open. Local frozen sources are
`q1_lean4_execution_2026-09-05/ERDOS1191_Q1_LEAN4_CODEX_PACK/TARGET_SPEC.md`
and `q1_lean4_execution_2026-09-05/lean/Q1/Target.lean`.

Let \(A\subseteq\mathbb N_{>0}\) be infinite and put

\[
C_A(x):=\lvert A\cap[1,x]\rvert
=\#\{a\in A:1\le a\le x\},\qquad x\in\mathbb R.
\]

The logarithm is natural. Original Q1 asks whether

\[
\boxed{\quad
\forall A\subseteq\mathbb N_{>0}\;\bigl(A\text{ infinite and Sidon}\bigr)
\Longrightarrow
\liminf_{x\to\infty}C_A(x)\sqrt{\frac{\log x}{x}}=0.
\quad}
\]

The real-cutoff count is inclusive. In the Lean target it is implemented by the
nonnegative natural floor and the lower limit is taken in `EReal`, so an infinite
lower limit cannot be turned into zero by a conditionally-complete-real convention.

## 2. Sidon convention

Throughout this checkpoint, `Sidon A` means unique unordered two-summand sums,
including repeated summands:

\[
\forall a,b,c,d\in A,\quad
a+b=c+d\Longrightarrow
(a=c\land b=d)\ \lor\ (a=d\land b=c).
\]

Equivalently, for positive ordered endpoint pairs,

\[
a<b,\ c<d,\quad b-a=d-c\Longrightarrow(a,b)=(c,d).
\]

The equivalence of these two definitions is Lean-verified as
`Erdos1191Q1.sidon_iff_positiveDifferenceUnique`. A definition that excludes
`a=a`, allows zero without a positivity bridge, or gives only uniqueness for
distinct summands is not silently interchangeable with this contract.

## 3. Integer and real formulations

For one set \(A\), the integer squared formulation is

\[
\forall\varepsilon>0\ \forall M\in\mathbb N\ \exists N\in\mathbb N:\quad
N\ge\max(M,2),\qquad C_A(N)^2\log N<\varepsilon N.
\tag{I}
\]

`Erdos1191Q1.original_iff_integerSquared` proves, for every set of natural
numbers and without a Sidon assumption, that the original real-cutoff lower-limit
condition is equivalent to (I). The proof includes:

- the floor identity for the inclusive count;
- nonnegativity and the square-root/square transition for \(x\ge2\);
- the `epsilon/2` loss when replacing a real cutoff by its floor;
- the converse passage from integer cutoffs to arbitrary real lower bounds.

Consequently the universal statements `Q1` and `Q1Integer` are Lean-verified to
be equivalent. The integer formulation is a verified reformulation, not a weaker
replacement.

## 4. Exact negation

The exact negation of Q1 is

\[
\boxed{\quad
\exists A\subseteq\mathbb N_{>0}\;\exists\varepsilon>0\;\exists M\ge2:
\ A\text{ is infinite and Sidon, and }
\forall N\ge M,\quad
\varepsilon N\le C_A(N)^2\log N.
\quad}
\]

This is Lean-verified by `Erdos1191Q1.not_q1_iff`. The real-cutoff negation for
one set is likewise equivalent to `EventualLowerBound` by `not_original_iff`.
A lower bound on only a subsequence, a limsup statement, or a finite family of
long prefixes is not this negation.

## 5. Completion contract

### Complete affirmative proof

A complete proof must establish the displayed universal Q1 statement for every
positive infinite Sidon set. If the integer or finite-tree form is used, every
equivalence, uniform constant, boundary/cutoff term, and limiting step must be
proved. For the requested formal completion, Lean must contain a theorem of the
literal `Erdos1191Q1.Q1` proposition, with no target-equivalent premise, `sorry`,
`admit`, custom axiom, unchecked oracle, or semantic substitution; the final
dependency/axiom audit and clean pinned build must pass.

### Complete negative proof

A complete refutation must construct, or prove the existence of, one actual
positive infinite Sidon set and fixed \(\varepsilon>0,M\ge2\) satisfying the
eventual lower bound for every \(N\ge M\). For the requested formal completion,
Lean must prove the literal `¬ Erdos1191Q1.Q1` (equivalently the witness statement
in `not_q1_iff`) under the same trust and build conditions.

## 6. Non-resolution guardrails

None of the following resolves Q1 by itself:

- a positive constant upper bound for the liminf;
- a finite upper bound, a finite-rank lemma, or a fixed-history certificate;
- C143/C139/C140 phase or optimization results for named fixtures;
- a numerical experiment, bounded search, solver optimum, or exact finite replay;
- a theorem about selected histories, moving onsets, almost every construction,
  or only a subsequence of cutoffs;
- an auxiliary Lean theorem whose conclusion is not `Q1` or `¬Q1`;
- an obstruction or counterexample to one proof route;
- assuming an all-history capacity/transport theorem that is itself the missing
  global implication.

Every future claim must keep the labels **Lean-verified**, **mathematically
proved but not Lean-verified**, **finite computational evidence**, **provisional**,
and **rejected** separate.

# Independent review of the signed retirement boundary example

2026-09-05. Reviewer: `/root/moment_evidence_audit`, GPT-6 Astra Ultra.

Result: no mathematical defect identified in the capacity distinction, the complete eight-pair example, the normalization, or the stated quantifier boundary. The complete note, fixed checker source, stdout, stderr, and instrumented run record were read. Current source/log bytes were checked against the saved hashes and complete log strings. The checker itself was not rerun. The supporting full signed-bank definitions and capacity identity in `signed_bank_born_positivity.md` were also read.

## Full capacity versus capacity on actual used outputs

For a fixed nonnegative matrix on the terminal old signed bank, an output born at rank r accumulates exactly the available source pairs with later source birth strictly below r before its old-output mask switches off. If the output is absent from the final history, its available pairs remain in the full historical capacity. Thus the full capacity contains retired plus still-unused-output pairs, while restricting to outputs actually present by the specified final horizon retains only the retired pairs.

For a centered signed residual, the total strict-upper-triangle sum is `-S/2`. If Born, retired, and unused denote its three literal pair parts, then

```
retired+unused=-Born-S/2.
```

Deleting the unused outputs changes this identity; it does not justify replacing retired alone by `-Born-S/2`. This establishes the source's distinction. The pair-lifetime maximum argument applies to each full nonnegative matrix before differences are taken; a signed residual is not separately maximized as a nonnegative capacity.

Here Born is the **full signed-bank** definition, including equal source births. Signed same-birth pairs can retire later, so neither the older positive-bank mixed-Born convention nor its diagonal/Abel formula is imported. The direct finite convolution expansion in the source includes all used signed pairs and remains valid.

## The actual example and all eight products

The set `{0,1,10,13,17}` has ten distinct positive differences `1,3,4,7,9,10,12,13,16,17`. This proves its Sidon property including repeated sums. The old bank is exactly `F_4={1,3,9,10,12,13}` and the output star is `G_5={4,7,16,17}`.

The signed pairs can also be exhaustively checked as same-sign old differences and opposite-sign old sums:

| Output | Same-sign contribution | Opposite-sign contribution | Total |
|---|---:|---:|---:|
| 4 | `2*9*13=234` | `-2*1*3=-6` | 228 |
| 7 | `2*3*10=60` | 0 | 60 |
| 16 | 0 | `-2*3*13=-78` | -78 |
| 17 | 0 | 0 | 0 |

These are exactly the eight unordered pairs listed in the source. Every pair has a label of absolute value 3 or 13, actually born at rank four; its other label is old by that rank. Each output is actually born at five. Therefore all have common later source birth four and common retirement birth five.

There are no retirement pairs at the earlier stages. At rank three the old signed bank is `{−1,1}`, whose possible output 2 is absent from the new star `{9,10}`. At rank four the old positive magnitudes are `{1,9,10}`; neither their within-bank differences nor their opposite-sign sums produce any new output in `{3,12,13}`. The stage-two old bank is empty. Thus the full retirement through five is exactly

```
228+60-78=210>0.
```

The feature here is the permanent raw signed linear function `g(d)=d`. It is not the earlier positive-bank coefficient `d-h_(tau(d))`. A common positive source-stage price or retirement-stage price scales all eight products by the same positive number and preserves the sign. This statement concerns those common stage prices; it makes no assertion about separately adjustable positive weights on individual pairs.

For the normalized residual `phi(d)=d/H_4`, with `H_4=13` and signed bank size `Q_4=12`, division by `H_4^2 Q_4^2` gives

```
210/(169*144)=35/4056>0.
```

If the residual is later multiplied by a matrix parameter lambda, that parameter multiplies this value as well. The displayed normalization itself contains no implicit lambda.

For the odd minimum kernel, the output-four pairs give `2*9-2*1=16`; output seven gives `2*3=6`; output sixteen gives `-2*3=-6`. Its total is therefore 16. The sign outer product instead gives `2-2=0`, then 2, then -2, for total zero. These are direct evaluations of the same eight pairs, not additional executions of the checker.

## What the saved fixed execution establishes

The current checker uses integer arithmetic and four explicitly written tuples of ranks 3, 4, 6, and 32. It checks every unordered two-sum including repeated summands, constructs the positive and negative birth map from the actual endpoints, enumerates every unordered signed source pair, and classifies a used pair by `r>b` versus `r<=b`. It retains full same-birth source pairs. Its separate shadow convolution verifies

```
E=N*S+2*Born+2*Retired.
```

The script additionally asserts nonnegative full Born totals in these fixed examples; this is finite corroboration, not its proof of a universal Born theorem. Its assertions do not assume a sign for retirement.

The rank-six tuple contains the displayed five-point prefix. Its saved output reports the positive stage-five total 210, count eight, and the first six pairs. Adding the sixth point cannot change a retirement at stage five: such a pair's sources were all already present before five. The same output has no earlier retirement entries and records the later negative stage-six total separately. The rank-32 output reports positive stage sixteen `927108` with 742 pairs. Those additional numbers are reported finite outputs, not extrapolated all-rank signs.

The saved run record identifies the invocation as `/opt/homebrew/opt/python@3.14/bin/python3.14` with the absolute checker path and the stated workspace as cwd. It records start `2026-09-05T09:48:19.023204+00:00`, finish `2026-09-05T09:48:19.096001+00:00`, observed return code zero, and a performed and passed unchanged-source gate. Both recorded source hashes are the same and match the current file. This review's read-only byte comparisons also confirmed that both saved stdout/stderr hashes and their complete strings match the current log files exactly: 2413 stdout bytes and zero stderr bytes.

The exit and timing evidence are the saved instrumented run observations. The present review is a source-and-log binding check plus independent arithmetic, not another execution. The record identifies an interpreter path but does not contain an interpreter binary hash or a complete environment lock; no stronger historical runtime binding is asserted.

## Quantifier boundary

The actual five-point example disproves a universal claim that every full signed retirement stage is nonpositive for raw linear g, and likewise gives a positive minimum-kernel retirement. It also disproves fixing that universal stage sign by a common positive price on the stage. The sign feature is explicitly distinguished because it gives zero here.

The example does not supply an infinite capped history, defeat an estimate allowing a finite initial or repeated-endpoint error, or exclude cancellation enforced by stronger all-history hypotheses. No conclusion about the sign or required scale of an asymptotic core follows from this finite positive stage. The note retains these limitations. No source correction was requested; original Q1 remains unresolved.

Reviewed source SHA-256: `073293082a82874b5e7b03a4f87e321bb827f09430f60274c3317ee8918f1733`.

Bound evidence SHA-256 values:

- Checker: `6b2a2180357c0267442e1ecf0b0b29aafe5785ee3767a0dbcb5167bc029e63ab`.
- Stdout: `56d5b52d9092d507a0fcbd96207eac0f143826a1ad94070dfee5f06b8a528589`.
- Empty stderr: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- Instrumented run record: `51e98df780888ec2f63eb1355f91e100b71a5fa5f02a73d55c531c7a9b89f037`.

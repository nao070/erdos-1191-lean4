# A72: independent fixed-cap source-allowance counterexample

Date: 2026-09-09. Status: PASS.

This separate campaign fixes C=2^67, m0=2, M=T=k=50, c=24, b=25.
It does not reuse C=1 as a claim about this new history. The independent
checker reconstructs the one prescribed 50-point sequence from L=2^60,
the supplied coarse B values, and the explicit perturbation formula.
It imports only the existing independent fixed-point logarithm helper,
not the root's reference implementation.

## Actual sequence, Sidon condition, and cap

The sequence starts at 1 and is strictly increasing. Direct independent
integer checks give all 1225 positive differences distinct and all
1275 unordered two-sums, including repeated summands, distinct.

There is also a short independent explanation of this construction's
Sidon property. The exceptional perturbation p42 has precisely the nine
one-bits at positions 4..7,20..23,40. Its longest run of consecutive
one-bits has length four. Adding one power of two leaves at least six
one-bits; 2*p42 has nine. Neither can equal a sum of two ordinary powers
of two, which has at most two one-bits. Comparisons with p42 on both
sides cancel it, and ordinary powers already have unique unordered
two-sums. Thus the perturbation set itself is Sidon. All perturbation
two-sums are smaller than L. Equality of two sums of the actual a_j
therefore forces equality of the perturbation sums, and then equality
of their unordered endpoint pairs.

Each of the 49 required cap inequalities was independently certified
using a rational lower bound for log(2n). The same C is used throughout.
The simpler global check also passes: H50<512L=4C, while n>=2 and
log(2n)>=log4>1 imply C*n^2*log(2n)>4C. No extension or refitting of
C or m0 is used.

## One preserved physical record

The defining perturbation preserves the specified relation

    a24+a8+a40 = a4+a20+a42.

This statement asserts that specified equality, not a new classification
of every possible three-sum collision. It yields the saved physical row

    [23058430092153716720,13835058055283212032,
     4,24,8,20,24,20,40,42,9223372036870504688].

All six endpoints are distinct. The checker independently confirms all
five original strict log conditions, every displayed A46/A53/A54/A57
residual condition, the absence of the old mirror, and the empty actual
F3 at this source center. Every strict comparison is resolved; UNKNOWN=0.
The actual old F3 is the only three-sum fiber enumerated by this checker.

The existing source-bound independent output-oriented checker certifies
that the complete original core contains exactly this one record. Its
saved PASS and source hashes were checked. I did not rerun that full
core enumeration or the original evaluator. Independently summing the
genuine components 42..50 recovers the saved full u42, all profile
coefficients on cuts 25..39, all exact dyadic I values, and the once-per-
record harmonic coverage. The nonzero alpha51 subtraction is retained.

The terminal coefficient is

    lambda50 = 1/25527428477350911764427016026213912381273457594050.

The original full u42 and the single component50 price are kept separate.
Approximate N and cap-use displays are not certified enclosures here.

## Feasible matching lower certificate

For all 575 actual right nodes, the checker validates every listed
matching edge's actual old/future coordinates, positive gap values,
g+t<=H_c, and unit capacities. It independently sums every integer
weight and every node. No optimality, greedy implementation, or dual
certificate is needed for the following strict comparison:

    Phi_H >= 2498101079407809411484738706689307741019104
          > 2061544892416596415016373271045970178605160 = UG.

The certified positive margin is

    436556186991212996468365435643337562413944.

The lower bound divided by UG is exactly
312262634925976176435592338336163467627388 /
257693111552074551877046658880746272325645.
The near-birth and near-span conditions are independently certified at
this same actual cell, and the specified original strict record survives
the displayed conditions.

These auxiliary matching pairs are not asserted to be original core
records and receive no genuine record prices. A feasible matching lower
bound on the allowance suffices to refute the universal coefficient-one
comparison Phi_H<=UG. It does not refute a C=1-only restriction, an
eventual statement with a separately proved threshold, arbitrary constant
multiples, or the valid A70 upper-bound theorem. It gives no unbounded
family, actual profile growth, or counterexample to CoreUniform/Q1.

## Source and execution bindings

The checker exited 0. All root source and evidence bytes remained
unchanged during the check. No extra history, profile campaign, Lean
build, Skill invocation, or process was started or left running.

- A72_SOURCE_ALLOWANCE_COUNTEREXAMPLE.json:
  5c43800cf7470ce5ce5fdb7b4974c4d68c0b4564c79a83d5fbab632d4ca4f87a
- A72_SOURCE_ALLOWANCE_CHECKER.py:
  18d342324a03d99601bc845122fce6af0d7952a3695805ac399ff0308cdefe7b
- A72_SOURCE_ALLOWANCE_CHECK.json:
  f3d64eea70c6f90935c1cb55ca110f165698995af929ada146e92538b7d93b07
- C2pow67_m02_prescribed_allowance_M50.json:
  5a1374e9c7c37dcfa38893db1a295ce981d79ee5a7a71e28518d1443884902b0
- C2pow67_m02_prescribed_allowance_M50_independent_check.json:
  d2de9431c5b0526d23ccf618c1015eac7b5e5c1cdfad98af3bacc88758d8ff60

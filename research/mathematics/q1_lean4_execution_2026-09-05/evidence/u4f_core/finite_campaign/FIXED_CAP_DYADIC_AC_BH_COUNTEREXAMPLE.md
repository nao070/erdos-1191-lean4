# Fixed-cap finite counterexample to the constant-one AC/BH comparisons

2026-09-09. Exact finite certification, independently checked; not a
counterexample to Q1191-U4F-CORE-UNIFORM-01 or Q1.

The preceding existing-prefix check tested 900 actual dyadic block/horizon
pairs from the two saved C=1, m0=2 histories, through M=T=96, and found no
dyadic violation. That finite absence is not a theorem. This subsequent
campaign fixed C=1000000, m0=2, M=T=12, the six anchors, the seed and the
1000-trial ceiling BEFORE testing a padding. Its first trial succeeded:

    a = (1,14512,30001,30629,31694,32001,
         63361,67001,71675,84375,100001,105001).

All 66 positive differences are distinct. Among disjoint pairs of
three-element endpoint sets, the only repeated sum is

    a_12+a_6+a_3 = a_11+a_8+a_1 = 167003.

The existing exact evaluator and a separate output-centric checker both
certify every intermediate-rank cap, every strict core comparison, and
exactly TWO core records. No logarithmic comparison is UNKNOWN. Repeated
two-sum Sidon, including doubled endpoints, is checked independently.

The old quadruple is (p,q,s,c)=(1,3,6,8), with actual point values
(1,30001,32001,67001), gaps (A,B,Cgap)=(30000,2000,35000), Hquad=67000.
Every gap is strictly larger than 8^2/log(8)^3 (the saved fixed-point
interval certifies this); hence this lies in the unchanged all-large-gap
subclass. The two matchings have labels

    {30000,35000}, product AC=1050000000, older birth 3;
    {32000,37000}, product AC+BH=1184000000, older birth 6.

Here BH=134000000. Both share the actual output
(i,r)=(11,12), t=5000, and the exact covered cuts {9,10}. Every record has
six distinct endpoints. The genuine price is

    u_12^[12] = (alpha_12-alpha_13)/H_12^2
              = 1/676350675000000,

with H_12=105000. The terminal alpha_13 was retained. There are no other
core records and no plus record at another output; thus no ignored mass
can repair the proposed aggregate comparison in this example.

At b=9 and b=10 the entire channels, not just one witness row, are

    Q_AC = 2AC*u_12 = 4/1288287,
    Q_BH = BH*u_12 = 134/676350675,
    Q_AC-Q_BH = 1966/676350675 > 0,
    Q_AC/Q_BH = 1050/67 > 15.

All other cuts have zero profile. On the actual dyadic block
8<=b<min(16,12)=12, the record coverage is 1/9+1/10=19/90. Consequently

    I_AC = 38/57972915,
    I_BH = 1273/30435780375,
    I_AC-I_BH = 18677/30435780375 > 0.

The actual block square-root harmonic sums are, approximately,

    AC:   0.0003719930063286877657122928872545672704221328632743,
    BH:   0.00009396746844747968221023816468632123335605758000727,
    full: 0.0003836778360602593183772063138645852568552169154409.

They are (19/90) times the square root of their respective constant
profile values, not square roots of I. Exact rational enclosing intervals
were additionally certified using integer square roots at scale 10^40;
see the `components` object in the saved result. The ordinary evaluator's
Decimal presentation is explicitly separate from these enclosures.

## Reproducibility and logical boundary

- `targeted_fixed_C12.py`: bounded deterministic padding procedure,
  existing evaluator and independent-checker calls, and exact decomposition.
- `C1000000_m02_M12_target/campaign_fixed_before_trials.json`: fixed inputs.
- `C1000000_m02_M12_target/C1000000_m02_M12_target.json`: canonical result,
  rational cap/log certificates, original source hashes, profile and I.
- Its `_records.json` and `_independent_check.json`: both records and PASS.
- `C1000000_m02_M12_target/bounded_search_result.json`: exact channel
  comparison, gap certification, sqrt enclosures, and trial count one.

This rejects both universal constant-one candidates Q_AC<=Q_BH and
I_AC<=I_BH even under an actual fixed finite cap. It does not reject a
different-constant comparison, an eventual estimate with additional
hypotheses, or the existence of K(C,m0). It gives no unbounded history
family at this fixed C. No Lean verification is claimed for this witness.

Next nonduplicate action: retain this counterexample when reviewing the
cap-sensitive nonlinear comparison A15, rather than assuming an AC/BH
linear domination without its missing hypotheses.

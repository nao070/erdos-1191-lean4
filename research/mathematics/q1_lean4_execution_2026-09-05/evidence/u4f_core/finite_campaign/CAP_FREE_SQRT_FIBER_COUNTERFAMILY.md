# An actual Sidon family defeating cap-independent square-root fiber bounds

2026-09-09. Independent mathematical review of the main researcher's
proposed generic rational construction. Verdict: sound. This is an actual
Sidon family, unlike the scalar no-go, but it does **not** retain a common
diameter cap. It is not a counterexample to Q1191-U4F-CORE-UNIFORM-01
or original Q1. No new finite campaign or Lean verification is involved.

## Parameters and point forms

For any integer m>=16 take independent real parameters in the open box

```
J in (1,1.1),       T in (3,3.1),      U in (1,1.1),
I in (20,20.1),
P_j in (2,2.1),     Q_j in (10,10.1),
Z_j in (15,15.1),   Y_j in (20.3,20.4),  1<=j<=m.
```

The 5m+5 point forms, listed by their separated value ranges, are

```
J;
P_j;
J+T+U;
Q_j;
C_j=J+T+Q_j-P_j;
Z_j;
I;
Y_j;
I+U;
I+T.
```

The C_j lie in (11.9,12.3), between the Q and Z groups. All other
displayed groups are also disjoint and in the stated order. Avoiding
point coincidences inside each group fixes distinct ranks there.

## Symbolic Sidon verification

Every unordered pair of point forms, including repeated points, has a
distinct formal linear sum. Here is a classification that proves this
for every m, without finite symbolic extrapolation.

Private Z_j and Y_j coordinates immediately identify any point bearing
one of those coordinates. For a fixed j, the private (P_j,Q_j)
signatures of P_j,Q_j,C_j are respectively

```
(1,0), (0,1), (-1,1).
```

With two different private indices the two signatures identify the two
points separately. With one private index, the only ambiguous signature
between two private points and one private point plus a fixed form is

```
signature(P_j+C_j) = signature(Q_j).
```

At the level of complete forms, P_j+C_j=Q_j+(J+T). Equality with
Q_j+F would require the fixed point form F=J+T, which is absent.
The other same-index double signatures are (2,0),(1,1),(0,2),(-1,2),
and (-2,2), all distinct. A single private point paired with two
different fixed choices cannot give equal full forms.

It remains to check the five fixed forms

```
J, B=J+T+U, I, D=I+U, E=I+T.
```

Their 15 unordered two-sums split by their coefficients of J and I:

| J/I coefficients | Two-sums' distinct T/U coefficient pairs |
|---|---|
| (2,0): J+J,J+B,B+B | (0,0),(1,1),(2,2) |
| (1,1): J+I,J+D,J+E,B+I,B+D,B+E | (0,0),(0,1),(1,0),(1,1),(1,2),(2,1) |
| (0,2): I+I,I+D,I+E,D+D,D+E,E+E | (0,0),(0,1),(1,0),(0,2),(1,1),(2,0) |

All are distinct, completing formal two-sum uniqueness.

An equality of distinct numerical two-sums therefore describes a proper
rational hyperplane in parameter space. There are only finitely many.
Their union cannot cover the nonempty open parameter box; its complement
contains a nonempty open set and hence a rational point. Choose such
rational parameters. This also avoids individual point coincidences.
The resulting finite point set has repeated-sum Sidon uniqueness.

Choose an integer scale D clearing all chosen denominators and satisfying
D>=(3m+2)^2. Scale every point by D and translate the minimum to 1.
The resulting actual positive integers remain Sidon, with the same ranks.
All difference identities below scale by D and survive the translation.

## The common oriented collision and its m fibers

The ranks of the distinguished points are

```
jplus=1                    (point J),
jminus=m+2                 (point J+T+U),
c_j in [2m+3,3m+2]         (point C_j),
i=4m+3                     (point I),
rminus=5m+4                (point I+U),
rplus=5m+5                 (point I+T).
```

The older label for C_j is e_j=D(Q_j-P_j)>7D. Its upper source birth
s_j is the rank of Q_j, in [m+3,2m+2]. The new differences are

```
d_plus,j = D(C_j-J) = e_j+DT,
d_minus,j = D(C_j-(J+T+U)) = e_j-DU.
```

They are positive and lie on opposite sides of e_j. Their actual outputs
are DT=a_rplus-a_i and DU=a_rminus-a_i. Each record has six distinct
endpoint indices by the separated rank groups. All m rows share the
same oriented repeated collision with A=D(J+T), up to translation of
point coordinates, while their actual older difference labels differ.

## Every specified record is strict core

For m>=16, c>=35 gives log c>3, and r>=84 gives log r>4. Thus

```
s >= m+3 > c/(log c)^2,
i-c >= m+1 > c/(log c)^2,
rminus-i = m+1 > rminus/(log rminus)^3,
rplus-i = m+2 > rplus/(log rplus)^3,
rplus=5m+5 < 3(2m+3) < c log c.
```

Both physical outputs exceed D. Since c<=(3m+2) and D>=(3m+2)^2,

```
c^2/(log c)^3 < (3m+2)^2/27 <= D/27 < DU < DT.
```

The actual integer endpoints supply positive labels, unique outputs,
six-distinctness, and Sidon packing automatically. No synthetic label
copies or missing endpoint equations are used in this construction.
Take M=T=5m+5 for its actual finite core.

## What the family refutes, and what it does not

The largest point before I belongs to the Z group. Hence

```
H_(i-1) < 15D,
sum_(the m constructed c rows) e_c > 7mD,
sum_c e_c / H_(i-1) > (7/15)m.
```

Any additional actual rows only increase the full fiber sum. Since
jminus=m+2, this ratio divided by sqrt(jminus) tends to infinity.
Thus no absolute constant B can make

```
sum_c e_c <= B H_(i-1) sqrt(jminus)
```

hold over all actual Sidon histories without a common fixed cap. The
constant-one claim already fails for each m>=16 in this family.

The early diameter explicitly explains the boundary:

```
H_2 > 0.9D >= 0.9(3m+2)^2.
```

A cap with m0=2 would therefore need
C>0.9D/[4 log4], which tends to infinity with m. Changing C at each
member is not a common-cap campaign and cannot refute the frozen theorem.
The construction also does not prove that these finite sets extend to an
infinite Sidon history satisfying one cap. It only eliminates a shortcut
whose proposed fiber bound has no dependence on the cap.

The existence argument is an exact mathematical family proof; no specific
integer coordinates or finite numerical certificate are claimed here.
Its formalization in Lean remains undone. The next full-core attack must
retain fixed-cap dependence if it uses a square-root fiber saving.

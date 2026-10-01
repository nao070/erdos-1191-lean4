# C139 final verification — 2026-09-01

Status: EXACT_MAXIMAL_CONNECTED_FIXED_Y_PHASE_CHAMBER_C058_OPEN.

C139 canonically extends the C138 fixed witness from one phase to the
maximal connected closed owner-feasible chamber containing t0=17745/32:

    [4425/8, 555].

The scope is exactly one frozen C132 32-mark fixture, the same 100 channels,
and the same 57-root rank-51 graph Y as C138. It is not a complete phase bank.

Exact owner audit:

- generic open chamber: 150 events, 149 cells, 1,192 weighted rows,
  884 tight and 308 strict;
- lower endpoint 4425/8: 148 events, 147 cells, 1,176 rows, all nonnegative;
- upper endpoint 555: 147 events, 146 cells, 1,168 rows, all nonnegative;
- pre8/rank-7 ownership is nonnegative throughout and integrates to 6489/256;
- the minimum positive slack and capacity are both 5/65536.

The objective is affine on the whole chamber:

    D(t) = -(99/512)t + 765573/4096,
    P(t) = (36082193/435322880)t + 1599473659439/16716398592,
    2D(t)-P(t)
      = -(204429713/435322880)t + 4649365900753/16716398592.

The margin decreases with t but remains positive at the upper endpoint:

    2D(555)-P(555) = 292559857297/16716398592 > 0.

Maximality is exact for this fixed Y. The immediately adjacent open chambers
fail:

- left chamber (553,4425/8), owner (16,8), slack -549/131072;
- right chamber (555,557), owner (16,1), slack -15/8192.

The responsible cells collapse exactly at the two feasible endpoints, so the
closed endpoint convention does not hide a negative retained row.

The same-atom fourteen-row ledger is replayed over its finer internal
partition [4425/8,554), [554,1664/3), [1664/3,555]. All fourteen formal rows
are retained on every piece and collapsed boundary. The five nonzero affine
rows sum coefficientwise to D(t); the four A8 rows, three later A16 rows, and
both terminal rows are identically zero on this frozen fixture. Full M16 is
rebuilt in every epoch-16 demand; all 63 cross-half sources remain present.

Fresh canonical commands and outputs:

    python3 -B route_probes/ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_certificate.py
    C139_EXACT_PHASE_CHAMBER_OK closed=[4425/8,555] reference=17745/32
    roots=57 rank=51 minimum_margin=292559857297/16716398592
    adjacent_slacks=-549/131072,-15/8192 formal_rows=14
    terminals_retained C058_open

    python3 -B route_probes/ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_independent_oracle.py
    INDEPENDENT_C139_OK closed=[4425/8,555] roots=57 rank=51
    adjacent_slacks=-549/131072,-15/8192 affine_D_P_margin=exact
    formal_rows=14 full_M16 pre8_nonnegative C058_open

    python3 -B -m unittest -v route_probes/ROUTE_C_C139_FIXED_Y_PHASE_CHAMBER_test.py
    Ran 13 tests in 22.061s
    OK

Canonical SHA-256 values:

    report       3384782da305e45313b5e2379bc9d92556cc167da579ae884ac68ff2c2340d8f
    verifier     913fe2dc8fd9a07a79108a53d6b9850703e04292e83e14d456190687b032e914
    certificate  d30e5ab17b184536c3a9e34737a11e77d58661aaf485fd217819b2a40498d651
    payload      be2d4cd75229baaf3564546f06151982f7f0ee99e6dacf158af36136a6b2f0e4
    oracle       faf2752299c25c12787391076951bd27d918785ae2fa26d91ac1c932a788f5de
    test         da63e177a939baa99ecf038c1e1b86c654519a4b86e9a2aba5b5ae110b346888

Scope boundary: C139 proves only this fixed-fixture, fixed-Y maximal connected
closed chamber. It proves no feasibility outside the chamber, no complete
factor-two phase bank, no nonanticipating phase-selection rule, no nonzero
history or terminal case, no arbitrary rank/history, no global C103 ledger,
and no C058, Q1, Q2, publication, or prize conclusion. Global status remains
UNRESOLVED_AT_HARD_LIMIT.

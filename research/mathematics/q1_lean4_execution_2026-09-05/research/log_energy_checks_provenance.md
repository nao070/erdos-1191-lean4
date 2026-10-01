# Log-energy checks: source saved after execution

These two sources preserve the exact Python bodies already run inline during
the 2026-09-05 `c143_mathematics` agent turn. They were saved afterward at the
parent agent's request. Saving them did not execute new checks. The result
transcripts below copy retained tool outputs, rather than claiming a new
filesystem-log capture or a rerun.

## Exact coefficient check

Source: `verify_log_energy_coefficients.py`.
Original executable: `python3`.
Original tool result chunk: `06274e`.
Observed exit code: `0`.
Observed wall time: `0.000004875` seconds, as reported by the tool.

```
exact_W_newhalf_log_coefficient_identity_ranks_3_through_32_PASS
```

The source imports `point_matrix` from the primary C143 package read-only.
It checks rational/integer coefficients exactly and evaluates no logarithms.

## Floating smooth-ruler sanity check

Source: `log_energy_smooth_sanity.py`.
Original executable: `/Users/USER/miniforge3/bin/python`.
Original tool result chunk: `b1bc04`.
Observed exit code: `0`.
Observed wall time: `0.112288459` seconds, as reported by the tool.

```
{'n': 128, 'old_constant_error': np.float64(-0.05625541084499619), 'new_constant_error': np.float64(0.06046446770517033), 'cross_constant_error': np.float64(0.09965905095426941), 'W': np.float64(0.11972553606559008), 'W_limit': 0.12263159084947928, 'split_error': np.float64(2.9103830456733704e-11), 'factorial_floor_slack_per_n2': np.float64(0.8080167157331104)}
{'n': 512, 'old_constant_error': np.float64(-0.03136337533402278), 'new_constant_error': np.float64(0.0595813716715371), 'cross_constant_error': np.float64(0.08105828504051504), 'W': np.float64(0.12158657790852584), 'W_limit': 0.12263159084947928, 'split_error': np.float64(1.862645149230957e-09), 'factorial_floor_slack_per_n2': np.float64(0.9351936188347638)}
{'n': 2048, 'old_constant_error': np.float64(-0.021382495147809766), 'new_constant_error': np.float64(0.05338086138391773), 'cross_constant_error': np.float64(0.06753058640700438), 'W': np.float64(0.12209774998536156), 'W_limit': 0.12263159084947928, 'split_error': np.float64(-2.2351741790771484e-07), 'factorial_floor_slack_per_n2': np.float64(1.037581171034521)}
```

All quantities in this second transcript are floating diagnostics. In
particular the last digits of `W_limit` are cancellation/rounding artifacts;
the mathematical note reports the exact expression and only `0.12263159`
as a decimal. The numerical split residuals are not exact zero checks.

Reproduction commands:

```
python3 /Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/research/verify_log_energy_coefficients.py
/Users/USER/miniforge3/bin/python /Users/USER/Documents/ChatGPT/mathematics/q1_lean4_execution_2026-09-05/research/log_energy_smooth_sanity.py
```

Neither script is a Lean verification, proof of an asymptotic limit, or proof
of Q1. The universal mathematical arguments are in `log_energy_route.md`.

# Figures — Bayesian Tool Use paper

## Files

| Figure | File | Source dimensions | Renders in paper as | LaTeX env |
|--------|------|-------------------|---------------------|-----------|
| 1 — Three-route framework | `fig1_framework.pdf` | 10.0 × 2.2″ | 6.85 × 1.51″ | `figure*` |
| 2 — Prompt templates | `fig2_prompts.pdf` | 11.0 × 2.6″ | 6.85 × 1.62″ | `figure*` |
| 3 — Main accuracy + paired contrasts | `fig3_main.pdf` | 10.0 × 2.5″ | 6.85 × 1.71″ | `figure*` |
| 4 — Per-task accuracy + GLMM | `fig4_per_task.pdf` | 10.0 × 2.9″ | 6.85 × 1.99″ | `figure*` |
| 5 — Translation additivity | `fig5_additivity.pdf` | 5.0 × 2.7″ | 3.35 × 1.81″ | `figure` |
| 6 — Recovery vs difficulty | `fig6_recovery.pdf` | 5.0 × 2.8″ | 3.35 × 1.88″ | `figure` |

PNG previews are included alongside each PDF for quick inspection.

## LaTeX usage

```latex
\begin{figure*}[t]
  \centering
  \includegraphics[width=\linewidth]{fig1_framework.pdf}
  \caption{...}
  \label{fig:framework}
\end{figure*}
```

For single-column figures (5, 6) use `figure` and `\linewidth`.

## Style consistency

All figures share `source/style.py`, which defines:

- **Route palette** (Wong colorblind-safe):
  - Route 1 / NL: `#0072B2` (blue)
  - Route 2 / Sim: `#E69F00` (orange)
  - Route 3 / Code+Exec: `#009E73` (green)
- **Auxiliary colors**: gray scale + `#D55E00` red for warnings/chance lines
- **Typography**: sans-serif (Helvetica/Arial fallback), 8–9 pt body
- **`pdf.fonttype: 42`**: text remains editable in vector editors

## Source

`source/` contains the Python script for each figure plus `style.py`.
Each figure is independently runnable:

```
python source/fig4_per_task.py
```

Fig 4 also requires `extracted_fig4_full.json` (data extracted from the
original paper PNG by pixel detection) — request separately if needed.

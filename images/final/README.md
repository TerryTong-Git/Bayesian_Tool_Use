# Figures - Bayesian Tool Use paper

Current PDF assets were replaced from `/Users/terrytong/Downloads/files (3).zip`
on 2026-05-28. The paper references the PDFs below from `images/final/`; PNG
files are regenerated previews for inspection only.

## Files

| Figure | File | Source size | Paper include | LaTeX env |
|--------|------|-------------|---------------|-----------|
| 1 - Three-route framework | `fig1_framework.pdf` | 8.50 x 2.90 in | `width=\linewidth` | `figure` |
| 2 - Prompt templates | `fig2_prompts.pdf` | 8.56 x 2.04 in | `width=\textwidth` | `figure*` |
| 3 - Main accuracy + paired contrasts | `fig3_main.pdf` | 10.94 x 3.04 in | `width=\textwidth` | `figure*` |
| 4 - Per-task accuracy + GLMM | `fig4_per_task.pdf` | 12.73 x 4.16 in | `width=\textwidth` | `figure*` |
| 5 - Translation additivity | `fig5_additivity.pdf` | 4.39 x 2.91 in | `width=\linewidth` | `figure` |
| 6 - Recovery vs difficulty | `fig6_recovery.pdf` | 5.94 x 3.86 in | `width=\linewidth` | `figure` |

PNG previews are included alongside each PDF for quick inspection.

## LaTeX usage

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{images/final/fig1_framework.pdf}
  \caption{...}
  \label{fig:three_routes}
\end{figure}
```

Full-width figures (2-4) use `figure*` and `\textwidth`; single-column figures
(1, 5, 6) use `figure` and `\linewidth`.

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

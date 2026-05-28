# Self-review: original critique → status in new figures

## Cross-cutting issues

| # | Original critique | Status |
|---|---|---|
| 1 | Schematic figures are raster PowerPoint exports; should be vector PDF | ✅ All three (Fig 1, 2, 5) are now matplotlib → vector PDF |
| 2 | No consistent color language across figures | ✅ Route 1 = blue (#0072B2), Route 2 = orange (#E69F00), Route 3 = green (#009E73) used in Figs 1, 2, 3, 4, 5, 8. Fig 7 (Native vs Translated) and Fig 9 (recovery vs exec wins) intentionally use a separate palette because they're not about routes. |
| 3 | Significance reporting varies (stars, brackets, inline r=) | ⚠️ Mostly consistent now. Stars: Fig 3, 8. Inline r/p: Fig 9. The legend item in Fig 8 explicitly defines n.s. |
| 4 | Titles do double duty (metadata vs takeaway) | ✅ All titles now short and descriptive. Metadata moved to caption. |

## Figure 1 — Three-Route Framework

| # | Original critique | Status |
|---|---|---|
| 1.1 | Easy/Hard arrows compete with section labels | ✅ Removed; described in caption instead |
| 1.2 | "Prompt Hidden / not needed" reads weirdly | ✅ Replaced with "reuses Route 2 code" + dashed connector |
| 1.3 | Sec 4 / Sec 5 brackets confuse | ✅ Removed |
| 1.4 | Box style inconsistent | ✅ Uniform rounded boxes; route color tab + bordered box |

## Figure 2 — Prompt templates

| # | Original critique | Status |
|---|---|---|
| 2.1 | Raster screenshots | ✅ Vector matplotlib |
| 2.2 | Red ALL CAPS shouty | ✅ "constraint: no code" in small italic |
| 2.3 | Columns not aligned in internal structure | ✅ Prompt / constraint / Example / Final answer at identical y-positions across all three panels |
| 2.4 | Should match Figure 1 color language | ✅ Route-colored headers |

## Figure 3 — Main results

| # | Original critique | Status |
|---|---|---|
| 3.1 | p=1.00 ns bracket distracting | ✅ Removed |
| 3.2 | "Closed / Open ± 95% CI" legend confusing | ✅ Single legend: circle vs square for closed/open |
| 3.3 | Density panels uninformative for the conclusion | ✅ Replaced with horizontal strip showing both deltas on a common axis, CIs visible, zero line in red |
| 3.4 | Too many panels (3) | ✅ Down to 2 |

## Figure 4 — Per-task accuracy

| # | Original critique | Status |
|---|---|---|
| 4.1 | GLMM inset unreadable | ✅ Removed — should be its own appendix figure |
| 4.2 | Abbreviated task names | ✅ Spelled out: "addition", "multiplication", "rod cutting", "knapsack", "ILP assignment", "ILP production", "ILP partition", "LCS" |
| 4.3 | No grid | ✅ Light grid added |
| 4.4 | NL and Sim curves overlap and become indistinguishable | ✅ NL is solid + circle, Sim is dashed + triangle, distinct markers |
| 4.5 | Average panel not visually distinct | ✅ Thicker frame |
| 4.6 | Consistent y-range | ✅ All panels 0–1 |

## Figure 5 — Translator/Judge prompts

| # | Original critique | Status |
|---|---|---|
| 5.1 | Same screenshot issues as Fig 2 | ✅ Vector |
| 5.2 | Should match Fig 2's aligned structure | ✅ Role / Task / Output at same vertical positions |

## Figure 6 — Judge discrimination

| # | Original critique | Status |
|---|---|---|
| 6.1 | Y-axis starts at 40, compresses 49–51 onto chance line | ✅ Y-axis starts at 0; chance line at 50 clearly between 0 and 100 |
| 6.2 | Control bars steal visual weight | ✅ Control is muted gray; main result (blue) is dominant |

## Figure 7 — t-SNE scatter

| # | Original critique | Status |
|---|---|---|
| 7.1 | Dashed ellipses draw eye away from in-cluster mixing | ✅ Replaced with light gray filled hulls — the eye sees the red/green mixing |
| 7.2 | Point alpha too low | ✅ Alpha = 0.85, white outline for separation |
| 7.3 | t-SNE inter-cluster distance not meaningful | ⚠️ Should be in figure caption (cannot enforce in figure itself, but title implies it) |

## Figure 8 — Translation additivity

| # | Original critique | Status |
|---|---|---|
| 8.1 | Stacked p-value brackets visually heavy | ✅ Single bracket per group, only on the test of interest (Native vs Translated) |
| 8.2 | Green/red redundantly encoded with stars/p-values | ✅ One signal (star + color). Inline italic note defines n.s. |

## Figure 9 — Recovery rates

| # | Original critique | Status |
|---|---|---|
| 9.1 | Dual y-axis creates artificial "X-shape" | ✅ Stacked two panels sharing x-axis; each has its own y-axis with its own color |
| 9.2 | Axis colors should match line colors | ✅ Tick labels and ylabels colored to match lines |
| 9.3 | y=0 reference visible | ✅ Each panel has its own zero/floor visible |

## Items I'd flag for follow-up

- **Fig 4 GLMM:** I removed it. The user may want me to make a standalone appendix figure for it; it had real information (odds ratio, McFadden R²).
- **Fig 7 caption note about t-SNE:** Should be added in the LaTeX caption: "t-SNE distances between clusters are not meaningful; we use the projection only to inspect within-cluster mixing of native and translated traces."
- **Fig 1 layout density:** The figure is currently sized for figure* (full width). If the user wants to keep it as `\begin{figure}` (single column), text will be small. I recommend upgrading to figure*.
- **Figure-caption integration:** Once these go in the paper, captions need to absorb the metadata I removed from titles (e.g. "N=6 models, model-averaged", "~1000 pairs per judge · Wilson 95% CIs").

"""Shared style for all figures. Colorblind-safe palette (Wong 2011)."""
import matplotlib as mpl
import matplotlib.pyplot as plt

# Route colors — used consistently across schematic and data figures
ROUTE_1 = "#0072B2"   # blue   — Direct NL
ROUTE_2 = "#E69F00"   # orange — Code + NL Simulation
ROUTE_3 = "#009E73"   # green  — Code + Solver Execution

# Lighter fills for schematic box backgrounds
ROUTE_1_FILL = "#D6E8F2"
ROUTE_2_FILL = "#FBE6C2"
ROUTE_3_FILL = "#CFEADC"

# Auxiliary
INK = "#1A1A1A"
GRAY_DARK = "#4D4D4D"
GRAY_MED = "#8C8C8C"
GRAY_LIGHT = "#D9D9D9"
GRAY_BG = "#F2F2F2"
RED = "#D55E00"

# Typography sizes
TITLE_SIZE = 10
LABEL_SIZE = 9
TICK_SIZE = 8
LEGEND_SIZE = 8
ANNOT_SIZE = 7

def set_style():
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
        "font.size": LABEL_SIZE,
        "axes.titlesize": TITLE_SIZE,
        "axes.labelsize": LABEL_SIZE,
        "axes.titleweight": "bold",
        "xtick.labelsize": TICK_SIZE,
        "ytick.labelsize": TICK_SIZE,
        "legend.fontsize": LEGEND_SIZE,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.linewidth": 0.8,
        "axes.edgecolor": INK,
        "axes.labelcolor": INK,
        "text.color": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "xtick.major.width": 0.8,
        "ytick.major.width": 0.8,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "grid.linewidth": 0.5,
        "grid.color": GRAY_LIGHT,
        "grid.alpha": 0.7,
        "lines.linewidth": 1.6,
        "lines.markersize": 5,
        "pdf.fonttype": 42,    # vector text, editable
        "ps.fonttype": 42,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "figure.dpi": 130,
    })

# Significance star helper
def stars(p):
    if p < 0.001: return "***"
    if p < 0.01:  return "**"
    if p < 0.05:  return "*"
    return "n.s."

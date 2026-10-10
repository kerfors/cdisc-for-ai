# Draws docs/images/cdisc_for_ai_design_to_data.png (the picture on the Pages front page and in README.md).
# Run: python3 cdisc_for_ai_design_to_data.py   (needs matplotlib and numpy)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"]="DejaVu Sans"
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

W, H, S = 1200, 805, 115          # S = extra height added below the top row
fig = plt.figure(figsize=(W/100, H/100), dpi=100)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")

BLUE, BLUE_F = "#3d6a8f", "#e6edf3"
ORANGE, ORANGE_F = "#cc7a3f", "#f9e8dc"
GREEN, GREEN_F = "#527f33", "#eaf4e6"
GREY, DARK = "#999999", "#222222"

def box(x, y, w, h, fc, ec, lw=1.5, ls="-", r=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, ls=ls))
def arrow(p, q, color=GREY, lw=2.5, ls="-", rad=0.0, ms=16):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=ms, color=color,
                                 lw=lw, ls=ls, connectionstyle=f"arc3,rad={rad}",
                                 shrinkA=0, shrinkB=0))

ax.text(50, 45, "From study design to data, linked and queried", fontsize=24, fontweight="bold", color=DARK, va="center")
ax.text(50, 90, "cdisc-for-ai explores how the standards behave. Reference files in Excel today; RDF/OWL is where we are heading.",
        fontsize=13, color="#666666", va="center")

# headings and brackets
ax.text(278, 145, "Study design (USDM)  \u2014  later, separate step", fontsize=12.5, fontweight="bold", color=BLUE, ha="center", va="center")
ax.plot([50, 50, 507, 507], [185, 166, 166, 185], color=BLUE, lw=1.5, ls=(0, (4, 2.5)))
ax.text(920, 145, "Data standards  \u2014  explored today", fontsize=12.5, fontweight="bold", color=GREEN, ha="center", va="center")
ax.plot([692, 692, 1149, 1149], [178, 166, 166, 178], color=GREEN, lw=1.8)

PLUM = "#a23b72"
y0, bw, bh = 185, 136, 85
row = [(50, "Objectives", 0), (211, "Endpoints &\nestimands", 0), (371, "Activities", 0),
       (692, "Biomedical\nConcepts", 1), (853, "Dataset\nSpecializ-\nations", 1), (1013, "SDTM +\nterminology", 1)]
for x, lab, g in row:
    if g: box(x, y0, bw, bh, GREEN_F, GREEN)
    else: box(x, y0, bw, bh, BLUE_F, BLUE, ls=(0, (4, 2.5)))
    ax.text(x + bw/2, y0 + bh/2, lab, fontsize=11.5, fontweight="bold", color=DARK, ha="center", va="center", linespacing=0.95)
ym = y0 + bh/2
for x0, x1 in [(186, 211), (347, 371), (507, 692), (828, 853), (989, 1013)]:
    arrow((x0 + 4, ym), (x1 - 3, ym))

# third corner of the triangle: Procedures (a USDM class), below the gap
px, py = 532, 338
box(px, py, bw, bh, BLUE_F, BLUE, lw=3)
ax.text(px + bw/2, py + bh/2, "Procedures", fontsize=11.5, fontweight="bold", color=DARK, ha="center", va="center")
ax.text(px - 14, py + bh/2, "often forgotten: drives\npatient burden and cost", fontsize=9.5, fontstyle="italic",
        color="#555555", ha="right", va="center", linespacing=1.15)
yb = y0 + bh
arrow((462, yb + 4), (556, py - 4))                                          # Activities -> Procedures (USDM)
arrow((px + bw + 4, py + 40), (792, yb + 5), color=GREEN, lw=1.8, rad=0.3, ms=13)   # the procedure itself as a concept
import numpy as np
P0, P2 = np.array([618.0, py - 4]), np.array([716.0, yb + 6])                 # read from: not stated
d = (P2 - P0)/np.linalg.norm(P2 - P0); n = np.array([-d[1], d[0]]); L = np.linalg.norm(P2 - P0)
for t0, t1 in [(0, 0.42), (0.58, 0.86)]:
    q0, q1 = P0 + d*L*t0, P0 + d*L*t1; ax.plot([q0[0], q1[0]], [q0[1], q1[1]], color=PLUM, lw=2.4, solid_capstyle="butt")
for t in (0.42, 0.58):
    p = P0 + d*L*t; v = 7*(n + 0.45*d); ax.plot([p[0]-v[0], p[0]+v[0]], [p[1]-v[1], p[1]+v[1]], color=PLUM, lw=2.2)
arrow(tuple(P0 + d*L*0.8), tuple(P2), color=PLUM, lw=2.4, ms=14)

# legend for the three kinds of link
lx, ly = 742, py + 22
ax.plot([lx, lx + 40], [ly, ly], color=GREY, lw=2.5)
ax.text(lx + 50, ly, "in USDM an activity points to both", fontsize=9.5, fontstyle="italic", color="#666666", va="center")
ax.plot([lx, lx + 40], [ly + 24, ly + 24], color=GREEN, lw=1.8)
ax.text(lx + 50, ly + 24, "the procedure itself as a concept (SDTM PR, a few BCs)", fontsize=9.5, fontstyle="italic", color=GREEN, va="center")
ax.plot([lx, lx + 14], [ly + 48, ly + 48], color=PLUM, lw=2.4); ax.plot([lx + 26, lx + 40], [ly + 48, ly + 48], color=PLUM, lw=2.4)
for xx in (lx + 14, lx + 26): ax.plot([xx - 3, xx + 3], [ly + 54, ly + 42], color=PLUM, lw=2.2)
ax.text(lx + 50, ly + 48, "what is read from a procedure: not stated today", fontsize=9.5, fontweight="bold",
        fontstyle="italic", color=PLUM, va="center")

# lower panels (shifted down by S)
def panel(x, title, head, body_fc, ec, ls="-"):
    y = 345 + S
    box(x, y, 330, 225, body_fc, ec, ls=ls, r=10)
    ax.add_patch(FancyBboxPatch((x, y), 330, 60, boxstyle="round,pad=0,rounding_size=10", fc=head, ec=head, lw=0))
    ax.add_patch(Rectangle((x, y + 30), 330, 30, fc=head, ec=head, lw=0))
    box(x, y, 330, 225, "none", ec, ls=ls, r=10)
    ax.text(x + 165, y + 30, title, fontsize=15, fontweight="bold", color="white", ha="center", va="center")
panel(50, "CDISC publishes", "#808080", "#f2f2f2", "#808080")
panel(435, "cdisc-for-ai", ORANGE, ORANGE_F, ORANGE)
TEAL, TEAL_F = "#2b7a78", "#e4f1f0"
panel(820, "Heading for RDF/OWL", TEAL, TEAL_F, TEAL, ls=(0, (4, 2.5)))

def lines(x, y, head, hc, items, dy):
    ax.text(x, y + S, head, fontsize=11.5, fontstyle="italic", color=hc, va="center")
    for k, t in enumerate(items):
        ax.text(x, y + S + dy[k], t, fontsize=10.5, color=DARK, va="center")
lines(70, 433, "read as documents and files", "#808080",
      ["•  USDM, SDTM / SDTMIG", "•  COSMoS BCs + Dataset Specializations", "•  SDTM Controlled Terminology, NCIt"], [38, 73, 107])
lines(455, 432, "measure and record  —  published today", ORANGE,
      ["•  how the published content behaves,", "    measured at each release", "•  reference files in Excel", "•  gaps and findings fed back to CDISC"], [29, 55, 81, 108])
lines(840, 432, "linked and queried", TEAL,
      ["•  design and data in one graph,", "    related to established ontologies", "•  usdm-rdf: USDM v4, OWL + SHACL", "    (draft)",
       "•  cosmos-rdf: COSMoS as published", "    (early work)"], [25, 45, 65, 85, 104, 123])

arrow((383, 457 + S), (430, 457 + S))
arrow((768, 457 + S), (815, 457 + S), ls=(0, (4, 2.5)))
arrow((596, 572 + S), (222, 573 + S), color=ORANGE, lw=1.6, ls=(0, (4, 2.5)), rad=-0.17, ms=13)
ax.text(407, 646 + S, "findings back to the standards", fontsize=11, color=ORANGE, ha="center", va="center")
ax.text(1150, 646 + S, "github.com/kerfors/cdisc-for-ai", fontsize=11, color="#666666", ha="right", va="center")

import os
fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cdisc_for_ai_design_to_data.png"), dpi=100, facecolor="white")

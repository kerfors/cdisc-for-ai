# Draws docs/images/cdisc_for_ai_design_to_data.png (the picture on the Pages front page and in README.md).
# Run: python3 cdisc_for_ai_design_to_data.py   (needs matplotlib)

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "DejaVu Sans"
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

W, H = 1200, 780
fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)
ax.axis("off")
fig.patch.set_facecolor("white")

DARK = "#222222"
GREY = "#666666"
BLUE, BLUE_BG = "#3d6a8f", "#e6edf3"
ORANGE, ORANGE_BG = "#cc7a3f", "#f9e8dc"
GREEN, GREEN_BG = "#527f33", "#eaf4e6"
TEAL, TEAL_BG = "#2b7a78", "#e4f1f0"
LGREY, LGREY_BG = "#808080", "#f2f2f2"
PLUM = "#a23b72"
ARROW = "#999999"


def box(x, y, w, h, fc, ec, lw=1.6, ls="-", r=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, ls=ls))


def arrow(x1, y1, x2, y2, color=ARROW, ls="-", lw=2.2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=16,
                                 color=color, lw=lw, ls=ls))


# Title and subtitle
ax.text(50, 45, "From study design to data, linked and queried", fontsize=24, weight="bold",
        color=DARK, va="center")
ax.text(50, 90, "cdisc-for-ai explores how the standards behave. Reference files in Excel today; "
        "RDF/OWL is where we are heading.", fontsize=13, color=GREY, va="center")

# Top row
ax.text(315, 145, "Study design (USDM)  —  later, separate step", fontsize=12.5, weight="bold",
        color=BLUE, ha="center", va="center")
ax.plot([50, 50, 580, 580], [185, 166, 166, 185], color=BLUE, lw=1.6, ls=(0, (4, 2)))
ax.text(885, 145, "Data standards  —  explored today", fontsize=12.5, weight="bold",
        color=GREEN, ha="center", va="center")
ax.plot([620, 620, 1150, 1150], [178, 166, 166, 178], color=GREEN, lw=1.8)

steps = [
    ("Objectives", BLUE_BG, BLUE, "--", 1.6),
    ("Endpoints &\nestimands", BLUE_BG, BLUE, "--", 1.6),
    ("Activities", BLUE_BG, BLUE, "--", 1.6),
    ("Biomedical\nConcepts", GREEN_BG, GREEN, "-", 1.6),
    ("Dataset\nSpecializations", GREEN_BG, GREEN, "-", 1.6),
    ("SDTM +\nterminology", GREEN_BG, GREEN, "-", 1.6),
]
x0, bw, gap, by, bh = 50, 150, 40, 185, 85
for i, (label, fc, ec, ls, lw) in enumerate(steps):
    x = x0 + i * (bw + gap)
    box(x, by, bw, bh, fc, ec, lw=lw, ls=ls, r=12)
    ax.text(x + bw / 2, by + bh / 2, label, fontsize=11.5, weight="bold", color=DARK,
            ha="center", va="center", linespacing=1.0)
    if i < len(steps) - 1:
        arrow(x + bw + 3, by + bh / 2, x + bw + gap - 3, by + bh / 2, lw=1.6)

# Observable: implicit in BC + DSS, read out by cdisc-for-ai
ax.plot([620, 620, 960, 960], [282, 290, 290, 282], color=ORANGE, lw=1.6)
ax.text(790, 306, "observable  —  implicit; read out by cdisc-for-ai", fontsize=10.5,
        weight="bold", style="italic", color=ORANGE, ha="center", va="center")

# Procedures: a second axis, not a step in the chain (USDM: an activity points to both)
box(415, 315, 180, 60, BLUE_BG, BLUE, lw=1.6, ls="--", r=12)
ax.text(505, 345, "Procedures\n(clinical practice)", fontsize=11, weight="bold", color=DARK,
        ha="center", va="center", linespacing=1.0)
arrow(505, 272, 505, 313, lw=1.6)
ax.text(505, 393, "how it is done: not standardised by CDISC", fontsize=10, style="italic",
        color=BLUE, ha="center", va="center")
ax.text(505, 410, "what is read from it: not stated today", fontsize=10, weight="bold",
        style="italic", color=PLUM, ha="center", va="center")
ax.text(505, 427, "one OGTT, many observables", fontsize=10, style="italic", color=BLUE,
        ha="center", va="center")
ax.plot([597, 1075], [345, 345], color=ORANGE, lw=1.6, ls=(0, (4, 3)))
arrow(1075, 345, 1075, 272, color=ORANGE, ls=(0, (4, 3)), lw=1.6)
ax.text(830, 362, "traces in SDTM qualifiers (--FAST, --POS, --TPT)", fontsize=10,
        style="italic", color=ORANGE, ha="center", va="center")

# Bottom row: three panels
py, ph, pw, hh = 450, 225, 330, 60


def panel(x, title, hdr, bg, ec, sub, subcol, bullets, ls="-", step=34, first=577, fs=10.5):
    box(x, py, pw, ph, bg, ec, lw=1.4, ls=ls, r=10)
    ax.add_patch(FancyBboxPatch((x, py), pw, hh, boxstyle="round,pad=0,rounding_size=10",
                                fc=hdr, ec=hdr, lw=0))
    ax.add_patch(plt.Rectangle((x, py + hh - 12), pw, 12, fc=hdr, ec=hdr, lw=0))
    ax.text(x + pw / 2, py + hh / 2, title, fontsize=15, weight="bold", color="white",
            ha="center", va="center")
    ax.text(x + 20, py + 88, sub, fontsize=10.5, style="italic", color=subcol, va="center")
    for j, b in enumerate(bullets):
        if b.startswith("~"):
            ax.text(x + 20, first + j * step, "    " + b[1:], fontsize=fs, color=DARK, va="center")
        else:
            ax.text(x + 20, first + j * step, "•  " + b, fontsize=fs, color=DARK, va="center")


panel(50, "CDISC publishes", LGREY, LGREY_BG, LGREY, "read as documents and files", LGREY,
      ["USDM, SDTM / SDTMIG", "COSMoS BCs + Dataset Specializations",
       "SDTM Controlled Terminology, NCIt"])
panel(435, "cdisc-for-ai", ORANGE, ORANGE_BG, ORANGE, "measure and record  —  published today", ORANGE,
      ["what identifies an observable,", "~read from what is published",
       "reference files in Excel,", "~measured at each release",
       "gaps and findings fed back to CDISC"], step=23, first=567)
panel(820, "Heading for RDF/OWL", TEAL, TEAL_BG, TEAL, "linked and queried", TEAL,
      ["design and data in one graph,", "~related to established ontologies",
       "usdm-rdf: USDM v4, OWL + SHACL", "~(draft)",
       "cosmos-rdf: COSMoS as published", "~(early work)"], ls="--", step=19.5, first=563)

arrow(381, 562, 433, 562, lw=2.4)
arrow(766, 562, 818, 562, ls="--", lw=2.4)

# Feedback loop
ax.add_patch(FancyArrowPatch((598, 676), (218, 676), connectionstyle="arc3,rad=-0.22",
                             arrowstyle="-|>", mutation_scale=16, color=ORANGE, lw=1.6,
                             ls=(0, (4, 3))))
ax.text(408, 751, "findings back to the standards", fontsize=11, color=ORANGE, ha="center",
        va="center")
ax.text(1150, 751, "github.com/kerfors/cdisc-for-ai", fontsize=11, color=GREY, ha="right",
        va="center")

fig.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cdisc_for_ai_design_to_data.png"),
            dpi=100, facecolor="white")

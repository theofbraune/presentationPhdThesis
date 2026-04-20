# style.py
from manim import *

# ---- LaTeX template ----
CUSTOM_TEMPLATE = TexTemplate(

preamble=r"""
\usepackage[T1]{fontenc}
\let\Bbbk\relax
\usepackage[cmintegrals,cmbraces]{newtxmath}
\usepackage{ebgaramond}
\usepackage{amsmath}
\usepackage{bm}
\newcommand{\R}{\mathbb{R}}
\newcommand{\nab}{\nabla}
\newcommand{\dnab}{d^{\nabla}}
\newcommand{\Onab}{\Omega^{\nabla}}
\usepackage{ulem}
\usepackage{xcolor}
"""

)

Tex.set_default(tex_template=CUSTOM_TEMPLATE)
MathTex.set_default(tex_template=CUSTOM_TEMPLATE)

# ---- shared colors, sizes, etc. ----
TITLE_SIZE = 32
BODY_SIZE = 24
ACCENT_COLOR = YELLOW

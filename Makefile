# Makefile for DECPresentationManim
# Run from the repo root.

# Make sure Python can find the `utils` and `slides` packages
export PYTHONPATH := .
export PYTHONPYCACHEPREFIX := ./build/pycache
export MANIM_SLIDES_FOLDER := ./build/slides_data
export MANIM_SLIDES_VIDEOS_FOLDER := ./build/slides_data/files
# --- defaults (can be overridden on the command line) ---
FILE   ?= render.py
CLASS  ?= FullPresentation
OUTPUT ?= presentation.html

# =============================================================
# Build a single slide / scene
# Usage:
#   make slide FILE=slides/introThesis.py
#   make slide FILE=slides/introThesis.py CLASS=IntroThesis
# =============================================================
.PHONY: slide
slide:
	manim -p $(FILE)

# =============================================================
# Build the full presentation HTML
# Usage:
#   make present
#   make present CLASS=FullPresentation OUTPUT=presentation.html
#   make present FILE=render.py CLASS=FullPresentation OUTPUT=thesis.html
# =============================================================
.PHONY: present
present:
	manim $(FILE) $(CLASS)
	manim-slides convert $(CLASS) $(OUTPUT)

# =============================================================
# Render full presentation only (no HTML conversion)
# =============================================================
.PHONY: render
render:
	manim $(FILE)

# =============================================================
# Convert an already-rendered presentation to HTML
# Usage:
#   make html CLASS=FullPresentation OUTPUT=presentation.html
# =============================================================
.PHONY: html
html:
	manim-slides convert $(CLASS) $(OUTPUT)

# =============================================================
# Clean generated media
# =============================================================
.PHONY: clean
clean:
	rm -rf media/ slides/__pycache__ utils/__pycache__ __pycache__
	rm -f *.html
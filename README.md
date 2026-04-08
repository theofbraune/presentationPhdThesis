# Geometry Driven Discretization of Differential Operators


This repository contains the **Manim + Manim-Slides** source files for my the presentation:

**"Geometry Driven Discretization of Differential Operators"**


This is a bit a personal playground to work with manim and an individual workflow. I hope it can be helpful.


## Repository structure
    PresentationManim/
    ├── Makefile           # build commands (see below)
    ├── manim.cfg          # Manim output configuration
    ├── render.py          # top-level entry point — lists all scenes
    ├── slides/            # one Python file per slide / scene
    ├── utils/             # shared helpers
    │   ├── preamble.py    # custom LaTeX preamble (fonts, macros)
    │   └── videoUtils.py  # wrapper for embedding video frame sequences
    ├── figures/           # static images used in the slides
    └── build/             # all generated output (gitignored)



All generated content — rendered videos, LaTeX intermediate files,
`manim-slides` JSON manifests, Python bytecode, the final HTML
presentation — lives under `build/` and is excluded from git via a
single line in `.gitignore`.

## Setup

This project uses **Manim** + **manim-slides**. I highly recommend
creating a dedicated virtual environment:
```bash
conda create -n manimEnv python=3.12
conda activate manimEnv
pip install manim manim-slides
```

A working LaTeX installation is also required (TeX Live or MacTeX).
The custom preamble in `utils/preamble.py` uses EB Garamond and
`newtxmath`, because I like the design, but it is easily modifyable, depending on what is available in your TeX
distribution.

## Building

All build commands go through the `Makefile`. Run them from the
**repository root** (not from inside `slides/`).

### Render a single slide with preview
```bash
make slide FILE=slides/intro.py
```

This compiles the scene defined in `slides/intro.py` and opens a
preview window. This runs the commanf
```bash
manim -p slides/intro.py
```

### Build the full presentation
```bash
make present
```

This renders every scene listed in `render.py` and converts the
result into a static HTML slideshow at `build/presentation.html`. Think about it like a `main.cpp` that depends on many other `.cpp` files. Compiling `main.c/render.py` builds all linked `.c` files (or manim slides) with it, but they can all be build/tested individually. 

I like this `C/C++` workflow to have temp and build files in a seperate build folder away from the work tree. For all manim related files, this works well with the config file, for the manim-slide related files somehow not, like that the `.json` files and the folder `files` are still in the main work tree, but they are gitignored.

You can override the output filename:
```bash
make present OUTPUT=build/thesisDefense.html
```

Or use a different top-level file (for example `renderTest.py`,
which lists only a subset of scenes for quick iteration):
```bash
make present FILE=renderTest.py CLASS=FullPresentationTest OUTPUT=build/test.html
```

### Render only, without converting to HTML
```bash
make render
```

### Convert an already-rendered presentation to HTML
```bash
make html OUTPUT=build/presentation.html
```

### Clean up generated files
```bash
make clean
```

This wipes the entire `build/` folder.

## How the build is organized

Two configuration files keep the source tree clean and funnel
everything generated into `build/`:

- **`manim.cfg`** redirects Manim's `media_dir`, `tex_dir`, and
  `log_dir` under `build/media/` and `build/logs/`.
- **The `Makefile`** sets `PYTHONPATH=.` (so that `from utils import
  preamble` works from any slide file) and `PYTHONPYCACHEPREFIX` (so
  that `__pycache__/` folders are kept out of the source tree).

The result: `slides/`, `utils/`, and `figures/` stay clean, and
everything generated lives under `build/`.

## Adding a new slide

1. Create a new file in `slides/`, e.g. `slides/myNewSlide.py`.
2. Inside, import the preamble and define a `Slide` (or `ThreeDSlide`)
   subclass:
```python
   from manim import *
   from manim_slides import Slide
   from utils import preamble

   class MyNewSlide(Slide):
       def construct(self):
           title = Tex("My new slide", font_size=40).to_corner(UL)
           self.play(FadeIn(title))
           self.next_slide()
           # ...
```

3. Test it in isolation:
```bash
   make slide FILE=slides/myNewSlide.py 
```

4. Once it works, add the import and class name to `render.py` in the
   position where it should appear in the final talk.

## Embedding video frame sequences

For animations rendered outside Manim (e.g. Houdini exports), use the
`play_video_loop` helper in `utils/videoUtils.py`. It loads a folder
of frame images and plays them as a looping segment inside a slide,
with optional fade in/out and uniform sizing:
```python
from utils.videoUtils import play_video_loop

class VideoDemo(Slide):
    def construct(self):
        play_video_loop(
            self,
            frame_dir="figures/myKeyFrames",
            position=ORIGIN,
            height=4.0,
            fps=24,
            fade_in_time=0.5,
            fade_out_time=0.5,
        )
        self.next_slide()
```

The wrapper marks the playback region as a `manim-slides` loop, so
the animation runs continuously until the user advances to the next
slide.
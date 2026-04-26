from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slideSummary(Slide):
    def construct(self):

        title = Tex(r"Summary", font_size=30).to_corner(UL)
        self.add(title)
        self.next_slide()

        BULLET_X = -6.0
        START_Y  =  2.3
        SPACING  =  1.05

        def bullet(text, y, color=WHITE, font_size=23):
            dot  = Tex(r"$\bullet$", font_size=font_size, color=color
                       ).move_to(np.array([BULLET_X + 0.15, y, 0]))
            body = Tex(text, font_size=font_size, color=color
                       ).next_to(dot, RIGHT, buff=0.25).align_to(dot, UP)
            body.set_max_width(11.5)
            return VGroup(dot, body)

        bullets = [
            
            bullet(
                r"Parallel-propagated frame (PPF): canonical frame field "
                r"in which $\omega = \mathcal{O}(h)$ "
                r"$\Rightarrow$ convergent discrete $d^\nabla$.",
                START_Y ,
            ),
            bullet(
                r"Alternation operator $\mathrm{Alt}^\nabla$: "
                r"symmetrizes over corners, gains one order of accuracy "
                r"$\mathcal{O}(h^{\ell+2}) \to \mathcal{O}(h^{\ell+3})$.",
                START_Y -   SPACING,
                color=YELLOW,
            ),
            bullet(
                r"Algebraic Bianchi identity $d^\nabla d^\nabla\alpha = \Omega^\nabla\wedge\alpha$ "
                r"holds \textit{exactly} at the discrete level.",
                START_Y - 2 * SPACING,
                color=YELLOW,
            ),
            bullet(
                r"Results hold for simplicial complexes "
                r"and most results extend to general cell complexes.",
                START_Y - 3 * SPACING,
            ),
            bullet(
                r"Framework covers vector-valued and endomorphism-valued forms; "
                r"convergence and combinatorial results hold in full generality.",
                START_Y - 4 * SPACING,
            ),
        ]

        for b in bullets:
            self.play(FadeIn(b))
            self.next_slide()

        # separator before outlook teaser
        sep = Line(LEFT * 6.5, RIGHT * 6.5, color=GRAY, stroke_width=1.0
                   ).move_to(DOWN * 2.8)
        teaser = Tex(
            r"What comes next?",
            font_size=26, color=YELLOW,
        ).next_to(sep, DOWN, buff=0.3)

        self.play(Create(sep), FadeIn(teaser))
        self.wait()
        self.next_slide()
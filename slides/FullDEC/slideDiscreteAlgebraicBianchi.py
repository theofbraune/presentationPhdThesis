from manim import *
from manim_slides import Slide, ThreeDSlide
import utils.preamble as preamble
import numpy as np





class slideDiscreteAlgebraicBianchiFixed(Slide):
    def construct(self):

        title = Tex(
            r"Discrete Algebraic Bianchi Identity",
            font_size=30,
        ).to_corner(UL)
        self.add(title)
        self.next_slide()

        # =====================================================================
        # BEAT 1 — combinatorial result
        # =====================================================================
        text1 = Tex(
            r"Applying $d^\nabla$ twice to a bundle-valued form $\alpha$:",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(text1))

        bianchi_discrete = MathTex(
            r"d^\nabla d^\nabla \alpha(\sigma, v_0)",
            r"\;=\;",
            r"\Omega^\nabla \wedge \alpha(\sigma, v_0)",
            font_size=32,
        ).next_to(text1, DOWN, aligned_edge=LEFT, buff=0.3)
        box_bianchi = SurroundingRectangle(
            bianchi_discrete, color=YELLOW, buff=0.2,
        )
        self.play(FadeIn(bianchi_discrete))
        self.play(Create(box_bianchi))
        self.next_slide()

        text2 = Tex(
            r"This holds \textbf{exactly} at the discrete level — "
            r"not just approximately.",
            font_size=24, color=YELLOW,
        ).next_to(bianchi_discrete, DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(FadeIn(text2))
        self.next_slide()
        imageMathematica = ImageMobject("figures/odd_and_even_permutations.jpg")
        imageMathematica.height = 4.0
        imageMathematica.move_to(ORIGIN+DOWN)
        self.play(FadeIn(imageMathematica))
        self.wait()
        self.next_slide()
        self.play(FadeOut(imageMathematica))


        # =====================================================================
        # BEAT 2 — convergence of the error
        # =====================================================================
        text3 = Tex(
            r"Moreover, the error $\|d^\nabla d^\nabla\alpha - \Omega^\nabla\wedge\alpha\|$ "
            r"now decays under refinement:",
            font_size=24,
        ).next_to(text2, DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(FadeIn(text3))
        self.next_slide()

        imgConv = ImageMobject("figures/bianchiVectorValuedConv.png")
        imgConv.height = 2.8
        imgConv.move_to(DOWN * 7)
        self.add(imgConv)
        self.play(
            imgConv.animate.next_to(text3, DOWN, buff=0.3),
            run_time=0.8, rate_func=smooth,
        )
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 3 — punchline
        # =====================================================================
        self.play(
            FadeOut(text1), FadeOut(bianchi_discrete), FadeOut(box_bianchi),
            FadeOut(text2), FadeOut(text3), FadeOut(imgConv),
        )
        self.next_slide()

        punchline = Tex(
            r"The discrete theory is \textit{structure-preserving}: "
            r"algebraic Bianchi holds exactly, "
            r"and convergence to the smooth theory is guaranteed.",
            font_size=26, color=YELLOW,
        ).move_to(ORIGIN).set_max_width(9.0)
        self.play(FadeIn(punchline))
        self.wait()
        self.next_slide()


        # now two applications od d nabla dnabla alpha. 
        # combinatorially leads to a curvature wedge product term

        # But now, we can see that the error of the bianchi identitites does decay under refinement

        # This is a key property :) 

        # now wrap this up. Say that we have a discrete bundle valued exterior calculus, 

        # means we have a calculus that satisfies the algebraic bianchi identities combinatorially in an exact sense 

        # further we have shown that it converges under refinement. 

        # Here, what I presented is for simplicial complexes, but we demonstrated taht the ideas can be extended to more general cell complexes. 

        # I talked about vector valued forms and "endomorphism valued forms" only in the context of curvature, but the convergence results and combinatorial results hold true for more general bundle valued forms.



        # --> What comes next? 

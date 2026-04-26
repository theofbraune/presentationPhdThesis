from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slideAlgebraicBianchiIssue(Slide):
    def construct(self):

        title = Tex(
            r"The Algebraic Bianchi Identity",
            font_size=30,
        ).to_corner(UL)
        self.add(title)
        self.next_slide()

        # =====================================================================
        # BEAT 1 — recall smooth algebraic Bianchi + flat plot
        # =====================================================================
        text_recall = Tex(
            r"Recall the \textit{algebraic Bianchi identity}:",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(text_recall))

        bianchi_smooth = MathTex(
            r"d^\nabla d^\nabla \alpha \;=\; \Omega^\nabla \wedge \alpha",
            font_size=34,
        ).next_to(text_recall, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(bianchi_smooth))
        self.next_slide()

        text_question = Tex(
            r"Does $\mathfrak{d}^\nabla\mathfrak{d}^\nabla\alpha "
            r"\approx \Omega^\nabla \wedge \alpha$ hold discretely?",
            font_size=24,
        ).next_to(bianchi_smooth, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(text_question))
        self.next_slide()

        imgFlat = ImageMobject("figures/bianchiVectorValued.png")
        imgFlat.height = 3.0
        imgFlat.next_to(text_question, DOWN, aligned_edge=LEFT, buff=0.3)
        caption_flat = Tex(
            r"Error does not decay under refinement.",
            font_size=20, color=RED,
        ).next_to(imgFlat, DOWN, aligned_edge=LEFT, buff=0.12)

        self.play(FadeIn(imgFlat))
        self.play(FadeIn(caption_flat))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 2 — clear, two-column diagnosis
        # =====================================================================
        self.play(
            FadeOut(text_recall), FadeOut(bianchi_smooth),
            FadeOut(text_question), FadeOut(imgFlat), FadeOut(caption_flat),
        )
        self.next_slide()

        divider = Line(
            start=UP * 3.2, 
            end=DOWN * 1.8, 
            color=GRAY, 
            stroke_width=1.0
        )
        self.play(Create(divider))

        # ── LEFT: combinatorial ───────────────────────────────────────────────
        left_title = Tex(
            r"\textbf{Combinatorial issue}",
            font_size=23, color=ORANGE,
        ).move_to(LEFT * 5.8 + UP * 2.9)
        self.play(FadeIn(left_title))

        text_l1 = Tex(r"We have:", font_size=21,
                      ).next_to(left_title, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        mathTexCurv = MathTex(
            r"\mathfrak{d}^\nabla\mathfrak{d}^\nabla\alpha"
            r"([v_0,v_1,v_2,v_3],v_0) =",
            r"\Omega^\nabla([v_0,v_1,v_2],v_0,v_2)\,\alpha([v_2,v_3],v_2)",
            font_size=20,
        ).next_to(text_l1, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(text_l1), FadeIn(mathTexCurv))
        self.next_slide()

        textSided = Tex(
            r"Sided towards $v_0$ — only \textit{one} stencil.",
            font_size=21, color=ORANGE,
        ).next_to(mathTexCurv, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(textSided))
        self.next_slide()

        textv2 = Tex(
            r"Compare to smooth $\Omega^\nabla \wedge \alpha$:",
            font_size=21,
        ).next_to(textSided, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        formula_smooth = MathTex(
            r"(\Omega^\nabla \wedge \alpha)(\sigma) = "
            r"\frac{1}{3!}\sum_{\pi\in S_3}"
            r"\Omega^\nabla(\sigma_\pi)\,\alpha(\sigma_\pi)",
            font_size=19,
        ).next_to(textv2, DOWN, aligned_edge=LEFT, buff=0.15).set_max_width(5.6)
        self.play(FadeIn(textv2), FadeIn(formula_smooth))
        self.next_slide()

        text_l2 = Tex(
            r"$\Rightarrow$ One stencil vs. \textit{all} stencils.",
            font_size=21, color=ORANGE,
        ).next_to(formula_smooth, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(text_l2))
        self.next_slide()

        # ── RIGHT: analytic ───────────────────────────────────────────────────
        right_title = Tex(
            r"\textbf{Analytic issue}",
            font_size=23, color=BLUE_C,
        ).move_to(RIGHT * 1.3 + UP * 2.9)
        self.play(FadeIn(right_title))

        text_r1 = Tex(
            r"$\mathfrak{d}^\nabla$ at corner $v_0$: "
            r"converges at $\mathcal{O}(h^{\ell+2})$.",
            font_size=21,
        ).next_to(right_title, 2*DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.6)
        self.play(FadeIn(text_r1))
        self.next_slide()

        text_r2 = Tex(
            r"Reproducing $\Omega^\nabla \wedge \alpha$ requires "
            r"$\mathcal{O}(h^{\ell+3})$.",
            font_size=21,
        ).next_to(text_r1, DOWN, aligned_edge=LEFT, buff=0.25).set_max_width(5.6)
        self.play(FadeIn(text_r2))
        self.next_slide()

        text_r3 = Tex(
            r"$\Rightarrow$ One order too low.",
            font_size=21, color=BLUE_C,
        ).next_to(text_r2, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(text_r3))
        self.wait()
        self.next_slide()


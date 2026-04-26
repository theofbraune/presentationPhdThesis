from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slideAlgebraicBianchiFix(Slide):
    def construct(self):

        title = Tex(
            r"Discrete Covariant Exterior Derivative",
            font_size=30,
        ).to_corner(UL)
        self.add(title)
        self.next_slide()

        # ── divider ───────────────────────────────────────────────────────────
        divider = Line(UP * 3.2, DOWN * 1.0, color=GRAY, stroke_width=1.0
                       ).move_to(ORIGIN)
        self.play(Create(divider))

        # =====================================================================
        # LEFT: combinatorial fix
        # =====================================================================
        left_title = Tex(
            r"\textbf{Combinatorial fix}",
            font_size=23, color=ORANGE,
        ).move_to(LEFT * 5.8 + UP * 2.9)
        self.play(FadeIn(left_title))
        self.next_slide()

        text_l1 = Tex(
            r"Average $\mathfrak{d}^\nabla$ over all corners "
            r"$\Rightarrow$ all stencils contribute.",
            font_size=21,
        ).next_to(left_title, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.6)
        self.play(FadeIn(text_l1))
        self.next_slide()

        dnabla_def = MathTex(
            r"d^\nabla\alpha(\sigma, v_0) :=",
            r"\mathrm{Alt}^\nabla\!\left(\mathfrak{d}^\nabla\alpha\right)(\sigma, v_0)",
            font_size=21,
        ).next_to(text_l1, DOWN, aligned_edge=LEFT, buff=0.25).set_max_width(5.6)
        box_def = SurroundingRectangle(dnabla_def, color=ORANGE, buff=0.12)
        self.play(FadeIn(dnabla_def), Create(box_def))
        self.next_slide()

        text_l2 = Tex(
            r"Explicitly: symmetrize over all $(\ell+2)!$ permutations "
            r"of the vertices, transport each estimate to $v_0$.",
            font_size=20,
        ).next_to(dnabla_def, DOWN, aligned_edge=LEFT, buff=0.25).set_max_width(5.6)
        self.play(FadeIn(text_l2))
        self.next_slide()

        text_l3 = Tex(
            r"$\Rightarrow$ All stencils contribute equally.",
            font_size=21, color=ORANGE,
        ).next_to(text_l2, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(text_l3))
        self.next_slide()

        # =====================================================================
        # RIGHT: analytic fix
        # =====================================================================
        right_title = Tex(
            r"\textbf{Analytic fix}",
            font_size=23, color=BLUE_C,
        ).move_to(RIGHT * 1.3 + UP * 2.9)
        self.play(FadeIn(right_title))
        self.next_slide()

        text_r1 = Tex(
            r"Vertex-based PPF at $v_0$:",
            font_size=21,
        ).next_to(right_title, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.6)
        self.play(FadeIn(text_r1))

        formula_vertex = MathTex(
            r"\int_c \mathcal{R}^{\nabla,v_0} d^\nabla\alpha",
            r"=",
            r"\int_{\partial c} \mathcal{R}^{\nabla,v_0}\alpha",
            r"+ \mathcal{O}(h^{\ell+2})",
            font_size=20,
        ).next_to(text_r1, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(formula_vertex))
        self.next_slide()

        arrow_down = Tex(
            r"$\Downarrow$ center-of-mass PPF instead:",
            font_size=20, color=BLUE_C,
        ).next_to(formula_vertex, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(arrow_down))

        formula_center = MathTex(
            r"\mathcal{R}_{v_0,c_\sigma}"
            r"\int_c \mathcal{R}^{\nabla,c_\sigma} d^\nabla\alpha",
            r"=",
            r"R_{v_0,c_\sigma}\int_{\partial c} \mathcal{R}^{\nabla,c_\sigma}\alpha",
            r"+ \mathcal{O}(h^{\ell+3})",
            font_size=20,
        ).next_to(arrow_down, DOWN, aligned_edge=LEFT, buff=0.15).set_max_width(5.6)
        box_center = SurroundingRectangle(formula_center[3], color=BLUE_C, buff=0.10)
        self.play(FadeIn(formula_center), Create(box_center))
        self.next_slide()

        text_r3 = Tex(
            r"$\Rightarrow$ One extra order of accuracy.",
            font_size=21, color=BLUE_C,
        ).next_to(formula_center, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.6)
        self.play(FadeIn(text_r3))
        self.next_slide()

        # =====================================================================
        # BEAT 3 — unified conclusion bar
        # =====================================================================
        fix_line = Line(
            LEFT * 6.8, RIGHT * 6.8, color=GRAY, stroke_width=1.0,
        ).move_to(DOWN * 1.8)
        self.play(Create(fix_line))

        fix_label = Tex(
            r"Both fixes are two sides of the same coin: "
            r"$\mathrm{Alt}^\nabla$ \textbf{=} center-of-mass PPF evaluation.",
            font_size=27, color=YELLOW,
        ).next_to(fix_line, DOWN, buff=0.2).set_max_width(10.0)
        fix_label.shift(DOWN * 0.5)
        self.play(FadeIn(fix_label))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 4 — clear everything, show theorem screenshot
        # =====================================================================
        self.play(
            FadeOut(left_title), FadeOut(text_l1), FadeOut(dnabla_def),
            FadeOut(box_def), FadeOut(text_l2), FadeOut(text_l3),
            FadeOut(right_title), FadeOut(text_r1), FadeOut(formula_vertex),
            FadeOut(arrow_down), FadeOut(formula_center), FadeOut(box_center),
            FadeOut(text_r3),
            FadeOut(divider), FadeOut(fix_line), FadeOut(fix_label),
        )
        self.next_slide()
        

        imgConvProof = ImageMobject("figures/theoremDNabla.png")
        imgConvProof.height = 5.0
        imgConvProof.move_to(DOWN * 7)
        self.add(imgConvProof)
        self.play(
            imgConvProof.animate.move_to(ORIGIN + UP * 0.3),
            run_time=1.0, rate_func=smooth,
        )
        self.wait()
        self.next_slide()


        imgConv = ImageMobject("figures/convergenceTorsionComplete.png")
        imgConv.height = 5.0
        imgConv.move_to(DOWN * 7)
        self.add(imgConv)
        self.play(
            imgConvProof.animate.move_to(ORIGIN+10*UP),
            imgConv.animate.move_to(ORIGIN + UP * 0.3),
            run_time=1.0, rate_func=smooth,
        )

        # conv_caption = Tex(
        #     r"$\mathfrak{d}^\nabla$: $\mathcal{O}(h^{\ell+2})$ \quad "
        #     r"$d^\nabla$ (vertex PPF): $\mathcal{O}(h^{\ell+2})$ \quad "
        #     r"$d^\nabla$ (center PPF): $\mathcal{O}(h^{\ell+3})$",
        #     font_size=19, color=YELLOW,
        # # ).next_to(imgConv, DOWN, buff=0.15)
        # self.play(FadeIn(conv_caption))
        # self.wait()
        # self.next_slide()
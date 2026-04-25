from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


def fiber_square(pos, size=0.25, angle=0.0):
    sq = Square(side_length=size, color=WHITE, stroke_width=2).move_to(pos)
    sq.rotate(angle, about_point=pos)
    return sq

def integrateConnectionOneForm(posStart, posEnd):
    xStart, yStart = posStart[0], posStart[1]
    xEnd,   yEnd   = posEnd[0],   posEnd[1]
    deltaX = xEnd - xStart
    deltaY = yEnd - yStart
    xMid   = 0.5 * (xStart + xEnd)
    yMid   = 0.5 * (yStart + yEnd)
    return (2*yMid + 1) * deltaX + (xMid + 2) * deltaY


class slideFrakDfixed(Slide):
    def construct(self):
        title_text = Tex(
            "From Smooth To Discrete Forms", font_size=30
        ).to_corner(UL)
        self.add(title_text)

        textIntegralOfdNabla = Tex(
            r"Given a 2-cell $c = [v_0,v_1,v_2]$, "
            r"approximate $\int_c d^\nabla\theta$ in the PPF at $v_0$:",
            font_size=25,
        ).next_to(title_text, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textIntegralOfdNabla))

        # ── visual: center + 2 rays + fibers ─────────────────────────────────
        center = RIGHT*4 + DOWN

        ray0    = Line(center, center + 2*np.array([np.cos(0),           np.sin(0),           0]), color=DARK_BLUE)
        ray2    = Line(center, center + 2*np.array([np.cos(2*2*PI/9),    np.sin(2*2*PI/9),    0]), color=DARK_BLUE)
        lastLine = Line(ray0.get_end(), ray2.get_end(), color=DARK_BLUE)

        fiber0 = fiber_square(center,         size=0.6); fiber0.set_fill(DARK_BLUE, 0.9)
        fiber1 = fiber_square(ray0.get_end(), size=0.6); fiber1.set_fill(DARK_BLUE, 0.9)
        fiber2 = fiber_square(ray2.get_end(), size=0.6); fiber2.set_fill(DARK_BLUE, 0.9)

        baseVec    = Arrow(center, center + 0.2*UP,    buff=0, color=YELLOW, stroke_width=36)
        baseVecRot = Arrow(center, center + 0.2*RIGHT, buff=0, color=YELLOW, stroke_width=36)

        end0 = ray0.get_end();  rot0 = integrateConnectionOneForm(center, end0)
        end2 = ray2.get_end();  rot2 = integrateConnectionOneForm(center, end2)

        vec0 = baseVec.copy().move_to(end0 + 0.1*UP);    vec0.rotate(rot0,    about_point=end0)
        vec2 = baseVec.copy().move_to(end2 + 0.1*UP);    vec2.rotate(rot2,    about_point=end2)
        rot0b = baseVecRot.copy().move_to(end0 + 0.1*RIGHT); rot0b.rotate(rot0, about_point=end0)
        rot2b = baseVecRot.copy().move_to(end2 + 0.1*RIGHT); rot2b.rotate(rot2, about_point=end2)

        label_v0 = Tex(r"$v_0$", font_size=24).next_to(fiber0, LEFT+0.3*UP)
        label_v1 = Tex(r"$v_1$", font_size=24).next_to(fiber1, LEFT+0.3*UP)
        label_v2 = Tex(r"$v_2$", font_size=24).next_to(fiber2, LEFT+0.3*UP)

        self.add(ray0, ray2, lastLine,
                 fiber0, fiber1, fiber2,
                 baseVec, baseVecRot,
                 vec0, vec2, rot0b, rot2b,
                 label_v0, label_v1, label_v2)
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 1 — expand d^∇ = d + ω∧, highlight ω∧θ
        # =====================================================================
        integralBoundary = MathTex(
            r"\int_{c} \mathcal{R}^{\nabla, v_0} d^\nabla\theta",
            r"= \int_{c} \mathcal{R}^{\nabla, v_0} d\theta",
            r"+ \int_{c} \mathcal{R}^{\nabla, v_0} \omega\wedge\theta",
            font_size=25,
        ).next_to(textIntegralOfdNabla, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(integralBoundary))
        self.wait()
        self.next_slide()

        box_omega = SurroundingRectangle(
            integralBoundary[2], color=YELLOW, buff=0.1, corner_radius=0.1,
        )
        self.play(Create(box_omega))

        textSmall = Tex(
            r"In the PPF: $\omega = \mathcal{O}(h)$ $\Rightarrow$ this term is $\mathcal{O}(h^3)$",
            font_size=22, color=YELLOW,
        ).next_to(box_omega, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textSmall))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 2 — apply Stokes to the d term, expand boundary
        # =====================================================================
        self.play(FadeOut(box_omega), FadeOut(textSmall))

        integralStokes = MathTex(
            r"= \int_{\partial c} \mathcal{R}^{\nabla, v_0}\theta",
            r"+ \mathcal{O}(h^3)",
            font_size=25,
        ).next_to(integralBoundary, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(integralStokes))
        self.wait()
        self.next_slide()

        integralExpanded = MathTex(
            r"= \boldsymbol{\theta}([v_0,v_1],v_0)"
            r"- \boldsymbol{\theta}([v_0,v_2],v_0)"
            r"+ \mathcal{R}_{v_0,v_1}\,\boldsymbol{\theta}([v_1,v_2],v_1)"
            r"+ \mathcal{O}(h^3)",
            font_size=24,
        ).next_to(integralStokes, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(integralExpanded))

        textCurv = Tex(
            r"(last edge transported to $v_0$ via $\mathcal{R}_{v_0,v_1}$,"
            r" remainder is curvature — $\mathcal{O}(h^3)$)",
            font_size=20, color=GRAY,
        ).next_to(integralExpanded, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textCurv))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 3 — conclusion: this is exactly frak{d}^∇ + O(h³)
        # =====================================================================
        self.remove(*self.mobjects)
        self.add(title_text)

        texConclusion = MathTex(
            r"(d^\nabla\theta)(c, v_0)"
            r"\;=\; \mathfrak{d}^{\nabla}\theta([v_0,v_1,v_2],v_0)"
            r"\;+\; \mathcal{O}(h^3)",
            font_size=35,
        ).move_to(ORIGIN)
        box_conc = SurroundingRectangle(texConclusion, color=YELLOW, buff=0.2)
        self.play(Write(texConclusion, run_time=1.5))
        self.play(Create(box_conc))
        self.wait()
        self.next_slide()

        # fix image size and position it just below the screen
        imageConv = ImageMobject("figures/convergenceTorsion.png")
        imageConv.height = 5                          # fix height in scene units
        imageConv.move_to(ORIGIN + DOWN * 6)            # start off-screen below

        # move formula + box up, slide image in from below simultaneously
        formula_group = VGroup(texConclusion, box_conc)
        self.add(imageConv)
        self.play(
            formula_group.animate.move_to(UP * 2.0),
            imageConv.animate.move_to(DOWN * 1.2),
            run_time=1.0,
            rate_func=smooth,
        )
        self.wait()
        self.next_slide()
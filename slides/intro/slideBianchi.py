from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np


class slideBianchi(Slide):
    def construct(self):

        # ================================================================
        # TITLE
        # ================================================================
        title = Tex("Curvature and the Bianchi Identity", font_size=32).to_corner(UL)
        self.play(FadeIn(title))
        self.wait()
        self.next_slide()


        # ================================================================
        # INTRO: WHAT CURVATURE MEANS
        # ================================================================
        intro = Tex(
            r"Curvature measures the infinitesimal failure of parallel transport to commute.",
            font_size=26
        ).next_to(title, 2*DOWN, aligned_edge=LEFT)
        self.play(FadeIn(intro))
        self.wait()
        self.next_slide()


        # ================================================================
        # STENCIL GEOMETRY (your exact parallelogram)
        # ================================================================
        eps = 2.4
        center = RIGHT*2. + UP*0.1
        p = center + 0.5*(LEFT + DOWN)
        q = p + eps*RIGHT
        r = p + 0.9*eps*UP + 0.5*eps*RIGHT
        s = q + 0.9*eps*UP + 0.5*eps*RIGHT

        dots = VGroup(Dot(p), Dot(q), Dot(r), Dot(s))
        # labels = VGroup(
        #     MathTex("p").scale(0.7).next_to(p, DOWN),
        #     MathTex("p+\\varepsilon X").scale(0.7).next_to(q, DOWN),
        #     MathTex("p+\\varepsilon Y").scale(0.7).next_to(r, LEFT),
        #     MathTex("p+\\varepsilon (X+Y)").scale(0.7).next_to(s, RIGHT)
        # )

        stencil = Polygon(p, q, s, r, color=WHITE, stroke_width=2)

        self.play(Create(stencil), FadeIn(dots))
        self.wait()
        self.next_slide()


        # ================================================================
        # VECTOR AT p — start of parallel transport
        # ================================================================
        vec_p = Arrow(p, p + 0.5*RIGHT, color=YELLOW, buff=0)
        self.play(GrowArrow(vec_p))
        self.wait()
        self.next_slide()


        # ================================================================
        # PATH 1: p -> q -> s (upper path)
        # ================================================================
        vec_q = vec_p.copy().move_to(q+0.25*RIGHT)
        vec_q.rotate(-0.25, about_point=q)
        self.play(Transform(vec_p, vec_q))
        self.wait()

        vec_s1 = vec_q.copy().move_to(s+0.25*RIGHT+0.1*DOWN)
        # vec_s1.rotate(-0.0, about_point=s)
        self.play(Transform(vec_p, vec_s1))
        self.wait()
        self.next_slide()


        # ================================================================
        # PATH 2: p -> r -> s (lower path)
        # ================================================================
        vec_p2 = Arrow(p, p + 0.5*RIGHT, color=GREEN, buff=0)
        self.play(GrowArrow(vec_p2))

        vec_r = vec_p2.copy().move_to(r+0.25*RIGHT)
        vec_r.rotate(-0.00, about_point=r)
        self.play(Transform(vec_p2, vec_r))
        self.wait()

        vec_s2 = vec_r.copy().move_to(s+0.25*RIGHT)
        vec_s2.rotate(0.35, about_point=s)
        self.play(Transform(vec_p2, vec_s2))
        self.wait()
        self.next_slide()


        # ================================================================
        # MISMATCH = CURVATURE
        # ================================================================
        # mismatch = CurvedArrow(vec_s2.get_end(), vec_s1.get_end(), color=YELLOW)
        mismatch_label = Tex("Curvature: Infinitesimal mismatch", color=YELLOW, font_size = 25).next_to(stencil, UP)

        # self.play(Create(mismatch), FadeIn(mismatch_label))
        self.play(FadeIn(mismatch_label))
        self.wait()
        self.next_slide()


        # ================================================================
        # CLEAN UP STENCIL FOR FORMULAS
        # ================================================================
        self.play(
            FadeOut(stencil), FadeOut(dots),
            FadeOut(vec_p), FadeOut(vec_p2),
            FadeOut(vec_r), FadeOut(vec_q),
            FadeOut(vec_s1), FadeOut(vec_s2),
             FadeOut(mismatch_label)
        )
        self.wait()
        self.next_slide()
        # ================================================================
        # Curvatue as derivatice of omega 
        # ================================================================
        textCurvature = Tex(
            "Curvature: Exterior covariant derivative of the connection 1-form $\\omega$: $$\Omega^{\\nabla} = d\\omega + \\omega\wedge\\omega$$",
            font_size=26
        ).next_to(intro, 2*DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textCurvature))
        self.wait()
        self.next_slide()

        # ================================================================
        # GENERAL k-FORM FORMULA
        # ================================================================
        eq_general = Tex(
            "It holds: $d^{\\nabla} d^{\\nabla}\\alpha = \Omega^{\\nabla} \wedge \\alpha, $ the algebraic Bianchi identity.",
            font_size=25
        ).next_to(textCurvature, 2*DOWN, aligned_edge=LEFT)

        # self.play(Write(eq_general))
        # self.wait()
        # self.next_slide()
        # textAlgebraicBianchi = Tex(
        #     "This is called the algebraic Bianchi identity.",
        #     font_size=26
        # ).next_to(eq_general, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(eq_general))
        self.wait()
        self.next_slide()
        textDifferentialBianchi = Tex(
            "Further, the differential Bianchi identity: $d^{\\nabla} \\Omega^{\\nabla} = 0$",
            font_size=26
        ).next_to(eq_general, 2*DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textDifferentialBianchi))
        self.wait()
        self.next_slide()
        # now show the 2 equations
        
        # =============================================================
        # CENTERPIECE EQUATIONS — STRUCTURE-GIVING
        # =============================================================
        # remove all previos elements 
        self.remove(*self.mobjects)
        eq1 = Tex(
            "$$d^{\\nabla}  d^{\\nabla}\,\\alpha = \\Omega^{\\nabla}\wedge \\alpha$$",
            font_size=40
        ).move_to(UP*0.5)

        eq2 = Tex(
            "$$d^{\\nabla}\\Omega^{\\nabla} = 0$$",
            font_size=40
        ).next_to(eq1, DOWN, buff=0.8)

        # subtle entrance animation
        self.play(Write(eq1, run_time=2), Write(eq2, run_time=2))
        self.wait(0.5)
        self.next_slide()

        # =============================================================
        # OPTIONAL: add small glow/highlight
        # =============================================================
        highlight1 = SurroundingRectangle(eq1, color=YELLOW, buff=0.2)
        highlight2 = SurroundingRectangle(eq2, color=YELLOW, buff=0.2)

        self.play(Create(highlight1), Create(highlight2))
        self.wait()
        self.next_slide()

        # =============================================================
        # FINAL STATEMENT: structure-giving equations
        # =============================================================
        final_text = Tex(
            r" Bianchi Identities: {Structure-giving equations} ",
            font_size=28
        ).next_to(eq2, DOWN, buff=1.2)

        self.play(FadeIn(final_text, shift=UP))
        self.wait()
        self.next_slide()
        


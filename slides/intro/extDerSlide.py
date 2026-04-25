from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np


def make_rotated_frame_square(center_point, angle=0, size=0.6, color=WHITE):
    sq = Square(
        side_length=size,
        stroke_color=color,
        fill_color=color,
        fill_opacity=0.4,
    ).move_to(center_point)
    sq.rotate(angle, about_point=center_point)
    e1 = Arrow(center_point, center_point + 0.3 * RIGHT,
               buff=0, stroke_width=3, color=BLACK)
    e2 = Arrow(center_point, center_point + 0.3 * UP,
               buff=0, stroke_width=3, color=BLACK)
    e1.rotate(angle, about_point=center_point)
    e2.rotate(angle, about_point=center_point)
    return VGroup(sq, e1, e2)


class ExteriorDerivativeSlides(Slide):
    def construct(self):
        title = Tex(
            r"From $d$ to $d^{\nabla}$",
            font_size=32,
        ).to_corner(UL)
        self.add(title)
        self.next_slide()

        # =====================================================================
        # BEAT 1 — scalar d, one sentence + formula
        # =====================================================================
        caption_scalar = Tex(
            r"For scalar-valued forms, $d\alpha$ measures \textit{circulation} around an infinitesimal loop:",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(caption_scalar))
        self.wait()
        self.next_slide()
        # ----- parallelogram geometry -----
        eps    = 2.0
        center = RIGHT * 4.5 + DOWN * 0.5
        p = center + 0.6 * (LEFT + DOWN)
        q = p + eps * RIGHT
        r = p + eps * UP
        s = p + eps * RIGHT + eps * UP

        dots = VGroup(Dot(p), Dot(q), Dot(r), Dot(s))
        label_p = MathTex("p", font_size=22).next_to(p, DL, buff=0.1)

        a_pq = Arrow(p, q, buff=0.1, color=RED,  stroke_width=4)   # X at p
        a_pr = Arrow(p, r, buff=0.1, color=BLUE, stroke_width=4)   # Y at p
        a_qs = Arrow(q, s, buff=0.1, color=BLUE, stroke_width=4)   # Y at p+εX
        a_rs = Arrow(r, s, buff=0.1, color=RED,  stroke_width=4)   # X at p+εY
        boundary = VGroup(a_pq, a_pr, a_qs, a_rs)

        # ----- edge labels -----
        lbl_X       = MathTex("X",          font_size=24, color=RED ).next_to(a_pq, DOWN, buff=0.1)
        lbl_Y       = MathTex("Y",          font_size=24, color=BLUE).next_to(a_pr, LEFT, buff=0.1)
        lbl_alphaY  = MathTex(r"\alpha[Y]", font_size=22, color=BLUE).next_to(a_qs, RIGHT, buff=0.1)
        lbl_alphaX  = MathTex(r"\alpha[X]", font_size=22, color=RED ).next_to(a_rs, UP,    buff=0.1)
        edge_labels = VGroup(lbl_X, lbl_Y, lbl_alphaY, lbl_alphaX)

        # ----- BEAT 1 — scalar circulation -----
        # caption1 = Tex(
        #     r"$d\alpha$ = circulation around an infinitesimal loop",
        #     font_size=24,
        # ).to_corner(UL).shift(DOWN * 0.9 + RIGHT * 0.1)

        # self.play(FadeIn(caption1))
        self.play(FadeIn(dots), FadeIn(label_p))
        self.play(GrowArrow(a_pq), GrowArrow(a_pr),
                  GrowArrow(a_qs), GrowArrow(a_rs))
        self.play(FadeIn(edge_labels))
        self.next_slide()
        

        formula_scalar = MathTex(
            r"d\alpha(X,Y) \;=\; d_X\,\alpha[Y] \;-\; d_Y\,\alpha[X]",
            font_size=30,
        ).next_to(caption_scalar, DOWN, buff=0.4).align_to(caption_scalar, LEFT)
        box_scalar = SurroundingRectangle(formula_scalar, color=WHITE, buff=0.15)
        self.play(FadeIn(formula_scalar), Create(box_scalar))
        self.next_slide()

        # =====================================================================
        # BEAT 2 — fibers twist → need d^\nabla
        # =====================================================================
        # parallelogram geometry for the frame animation
        

        frame_p = make_rotated_frame_square(p, angle=0.10)
        frame_q = make_rotated_frame_square(q, angle=0.35)
        frame_r = make_rotated_frame_square(r, angle=-0.20)
        frame_s = make_rotated_frame_square(s, angle=0.25)
        frames  = VGroup(frame_p, frame_q, frame_r, frame_s)

        textVectorial = Tex(
            r"For \textit{vector-valued} forms, fibers twist along the loop "
            r"— we must account for the frame rotation:",
            font_size=24,
        ).next_to(formula_scalar, DOWN, buff=0.5).align_to(formula_scalar, LEFT)

        self.play(
            FadeIn(textVectorial),
            FadeIn(frames),
            frame_p.animate.rotate(0.20, about_point=p),
            frame_q.animate.rotate(-0.15, about_point=q),
            frame_r.animate.rotate(0.18, about_point=r),
            frame_s.animate.rotate(-0.22, about_point=s),
            run_time=1.6,
        )
        self.next_slide()

        # =====================================================================
        # BEAT 3 — d^\nabla = d + ω∧, replace d with ∇
        # =====================================================================
        formula_covariant = MathTex(
            r"d^{\nabla}\alpha(X,Y) \;=\; \nabla_X\,\alpha[Y] \;-\; \nabla_Y\,\alpha[X]",
            font_size=30,
        ).next_to(textVectorial, DOWN, buff=0.4).align_to(textVectorial, LEFT)
        box_cov = SurroundingRectangle(formula_covariant, color=YELLOW, buff=0.15)

        self.play(FadeIn(formula_covariant), Create(box_cov))
        self.next_slide()

        # explicitly show d^\nabla = d + ω∧
        formula_expand = MathTex(
            r"d^{\nabla}\alpha \;=\; d\alpha \;+\; \omega \wedge \alpha",
            font_size=28,
        ).next_to(formula_covariant, DOWN, buff=0.3).align_to(formula_covariant, LEFT)
        expand_caption = Tex(
            r"$d$ acts on coordinates, $\omega\wedge$ acts on the frame.",
            font_size=22, color=YELLOW,
        ).next_to(formula_expand, DOWN, buff=0.2).align_to(formula_expand, LEFT)

        self.play(FadeIn(formula_expand))
        self.play(FadeIn(expand_caption))
        self.next_slide()
        textBianchi = Tex(r"Further the \textit{Bianchi identities} hold for $d^{\nabla}$: ", font_size=24).next_to(expand_caption, DOWN, buff=0.6).align_to(textVectorial, LEFT)

        bianchi = MathTex(
            r"d^{\nabla}\Omega^{\nabla} \;=\; 0",
            r"\qquad",
            r"d^{\nabla}d^{\nabla} \alpha \;=\; \Omega^{\nabla} \wedge \alpha",
            font_size=28,
        ).next_to(textBianchi, DOWN, buff=0.6).align_to(textVectorial, LEFT)
        self.play(FadeIn(textBianchi), FadeIn(bianchi))
        self.wait()
        self.next_slide()


        # =====================================================================
        # BEAT 4 — Bianchi identities: clear stage, move to center
        # =====================================================================
        self.play(
            FadeOut(caption_scalar), FadeOut(formula_scalar), FadeOut(box_scalar),
            FadeOut(textVectorial), FadeOut(frames),
            FadeOut(formula_covariant), FadeOut(box_cov),
            FadeOut(formula_expand), FadeOut(expand_caption),
            FadeOut(dots), FadeOut(label_p),
            FadeOut(a_pq), FadeOut(a_pr),
            FadeOut(a_qs), FadeOut(a_rs),
            FadeOut(edge_labels), FadeOut(textBianchi)
            )
        self.wait()
        self.next_slide()
        self.play(
            bianchi.animate.scale(1.8).move_to(ORIGIN),
            run_time=1.2,
        )

        # bianchi = MathTex(
        #     r"d^{\nabla}\Omega^{\nabla} \;=\; 0",
        #     r"\qquad",
        #     r"d^{\nabla}d^{\nabla} \alpha \;=\; \Omega^{\nabla} \wedge \alpha",
        #     font_size=40,
        # ).move_to(ORIGIN)
        box_focus = SurroundingRectangle(bianchi, color=YELLOW, buff=0.3)

        # self.play( run_time=1.5)
        self.play(Create(box_focus))

        caption_focus = Tex(
            r"\textit{Structure-giving equations.}",
            font_size=30, color=YELLOW,
        ).next_to(bianchi, DOWN, buff=0.6)
        self.play(Write(caption_focus))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 5 — Bianchi right, Stokes left, analogy
        # =====================================================================
        bianchi_group = VGroup(bianchi, box_focus)

        self.play(
            bianchi_group.animate.scale(0.8).to_edge(RIGHT, buff=0.6),
            FadeOut(caption_focus),
            run_time=1.2,
        )

        stokes_formula = MathTex(
            r"\int_{\partial U} \alpha \;=\; \int_{U} d\alpha",
            font_size=35,
        ).to_edge(LEFT, buff=0.8)
        box_stokes = SurroundingRectangle(stokes_formula, color=BLUE, buff=0.3)

        self.play(FadeIn(stokes_formula), Create(box_stokes))
        self.next_slide()

        stokes_label = Tex(
            r"DEC needs Stokes to hold\\by construction.",
            font_size=22, color=BLUE,
        ).next_to(box_stokes, DOWN, buff=0.4)

        bianchi_label = Tex(
            r"Bundle-valued DEC needs\\Bianchi to hold by construction.",
            font_size=22, color=YELLOW,
        ).next_to(bianchi_group, DOWN, buff=0.4)

        self.play(FadeIn(stokes_label))
        self.next_slide()
        self.play(FadeIn(bianchi_label))
        self.wait()
        self.next_slide()
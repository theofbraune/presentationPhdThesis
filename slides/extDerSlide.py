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

        # ----- parallelogram geometry -----
        eps = 2.0
        center = RIGHT * 1.8 + DOWN * 0.3
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

        # ----- edge labels: X, Y on the bottom-left arrows; α[X], α[Y] on top-right -----
        lbl_X       = MathTex("X",       font_size=24, color=RED ).next_to(a_pq, DOWN, buff=0.1)
        lbl_Y       = MathTex("Y",       font_size=24, color=BLUE).next_to(a_pr, LEFT, buff=0.1)
        lbl_alphaY  = MathTex(r"\alpha[Y]", font_size=22, color=BLUE).next_to(a_qs, RIGHT, buff=0.1)
        lbl_alphaX  = MathTex(r"\alpha[X]", font_size=22, color=RED ).next_to(a_rs, UP,    buff=0.1)
        edge_labels = VGroup(lbl_X, lbl_Y, lbl_alphaY, lbl_alphaX)

        # ----- BEAT 1 — scalar circulation -----
        caption1 = Tex(
            r"$d\alpha$ = circulation around an infinitesimal loop",
            font_size=24,
        ).to_corner(UL).shift(DOWN * 0.9 + RIGHT * 0.1)

        self.play(FadeIn(caption1))
        self.play(FadeIn(dots), FadeIn(label_p))
        self.play(GrowArrow(a_pq), GrowArrow(a_pr),
                  GrowArrow(a_qs), GrowArrow(a_rs))
        self.play(FadeIn(edge_labels))
        self.next_slide()

        # ----- BEAT 2 — scalar formula -----
        formula_scalar = MathTex(
            r"d\alpha(X,Y) \;=\; d_X\,\alpha[Y] \;-\; d_Y\,\alpha[X]",
            font_size=30,
        ).next_to(caption1, DOWN, buff=0.6).align_to(caption1, LEFT)
        box = SurroundingRectangle(formula_scalar, color=WHITE, buff=0.15)

        self.play(FadeIn(formula_scalar), Create(box))
        self.next_slide()

        # ----- BEAT 3 — fibers rotate -----
        frame_p = make_rotated_frame_square(p, angle=0.10)
        frame_q = make_rotated_frame_square(q, angle=0.35)
        frame_r = make_rotated_frame_square(r, angle=-0.20)
        frame_s = make_rotated_frame_square(s, angle=0.25)
        frames = VGroup(frame_p, frame_q, frame_r, frame_s)

        self.play(FadeIn(frames))
        self.play(
            frame_p.animate.rotate(0.20, about_point=p),
            frame_q.animate.rotate(-0.15, about_point=q),
            frame_r.animate.rotate(0.18, about_point=r),
            frame_s.animate.rotate(-0.22, about_point=s),
            run_time=1.6,
        )
        self.next_slide()

        textVectorial = Tex(r"For vector-valued forms, replace $d$ with $\nabla$.", font_size=24, color=YELLOW).next_to(formula_scalar, DOWN, buff=0.6).align_to(formula_scalar, LEFT)
        self.play(FadeIn(textVectorial))
        self.wait()
        self.next_slide()

        # ----- BEAT 4 — the fix: d → ∇ -----
        formula_covariant = MathTex(
            r"d^{\nabla}\alpha(X,Y) \;=\; \nabla_X\,\alpha[Y] \;-\; \nabla_Y\,\alpha[X]",
            font_size=30,
        ).move_to(formula_scalar)
        box_yellow = SurroundingRectangle(formula_covariant, color=YELLOW, buff=0.15)

        self.play(
            Transform(formula_scalar, formula_covariant),
            Transform(box, box_yellow),
        )
        self.wait(0.5)
        self.next_slide()

        # ----- BEAT 5 — Bianchi identities -----
        bianchi = MathTex(
            r"d^{\nabla}\Omega^{\nabla} \;=\; 0",
            r"\qquad",
            r"d^{\nabla}d^{\nabla} \alpha \;=\; \Omega^{\nabla} \wedge \alpha",
            font_size=28,
        ).next_to(textVectorial, DOWN, buff=0.6).align_to(textVectorial, LEFT)

        bianchi_caption = Tex(
            r"\textit{Bianchi identities} — Structure-giving equations.",
            font_size=24,
        ).next_to(bianchi, DOWN, buff=0.25).align_to(formula_scalar, LEFT)

        self.play(FadeIn(bianchi))
        self.play(FadeIn(bianchi_caption))
        self.wait()
        self.next_slide()
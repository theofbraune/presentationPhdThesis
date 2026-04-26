from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slideFutureWork2(Slide):
    def construct(self):

        title = Tex(r"Future Work", font_size=30).to_corner(UL)
        self.add(title)
        self.next_slide()

        TEXT_WIDTH      = 6.5
        TEXT_WIDTH_SUB  = 6.0
        MAIN_BUFF       = 0.45
        SUB_BUFF        = 0.20
        TOPIC_BUFF      = 0.50

        def main_bullet(text, anchor, font_size=22, color=WHITE):
            dot  = Tex(r"$\bullet$", font_size=font_size, color=color)
            body = Tex(text, font_size=font_size, color=color
                       ).next_to(dot, RIGHT, buff=0.2)
            body.set_max_width(TEXT_WIDTH)
            grp  = VGroup(dot, body).arrange(RIGHT, buff=0.2)
            grp.next_to(anchor, DOWN, aligned_edge=LEFT, buff=MAIN_BUFF)
            grp.to_edge(LEFT, buff=0.4)
            return grp

        def sub_bullet(text, anchor, font_size=21, color=GRAY):
            dot  = Tex(r"$\circ$", font_size=font_size, color=color)
            body = Tex(text, font_size=font_size, color=color
                       ).next_to(dot, RIGHT, buff=0.2)
            body.set_max_width(TEXT_WIDTH_SUB)
            grp  = VGroup(dot, body).arrange(RIGHT, buff=0.2)
            grp.next_to(anchor, DOWN, aligned_edge=LEFT, buff=SUB_BUFF)
            grp.shift(RIGHT * 0.5)
            return grp

        # ── images — right column ─────────────────────────────────────────────
        # img3 = ImageMobject("figures/sphere.png")
        # img3.height = 3.0
        # img3.move_to(RIGHT * 3.8 + UP * 1.5)

        # img4 = ImageMobject("figures/parabolasCheck.png")
        # img4.height = 3.0
        # img4.move_to(RIGHT * 3.8 + DOWN * 1.5)

        # =====================================================================
        # TOPIC 1 — Discrete Hodge Star
        # =====================================================================
        b4 = main_bullet(
            r"\textbf{Discrete Hodge Star for Bundle-Valued Forms}",
            title,
        )
        self.play(FadeIn(b4))
        self.next_slide()

        b4_s1 = sub_bullet(
            r"The operators here are metric-free — "
            r"in scalar DEC the metric enters via the Hodge star.",
            b4,
        )
        self.play(FadeIn(b4_s1))
        self.next_slide()

        b4_s2 = sub_bullet(
            r"In DEC, the \textit{Galerkin} Hodge star from FEM "
            r"is often more accurate than the geometric one.",
            b4_s1,
        )
        self.play(FadeIn(b4_s2))
        self.next_slide()

        b4_s3 = sub_bullet(
            r"Recent FEM spaces for bundle-valued forms [Christiansen \& Hu] "
            r"cover flat bundles — can this be a possible direction for a bundle-valued Hodge star?",
            b4_s2,
        )
        self.play(FadeIn(b4_s3))
        # self.play(FadeIn(img3))
        self.next_slide()

        # =====================================================================
        # TOPIC 2 — General Relativity
        # =====================================================================
        b5 = main_bullet(
            r"\textbf{General Relativity and the Einstein Equations}",
            b4_s3,
        )
        # extra gap between topics
        b5.shift(DOWN * TOPIC_BUFF)
        self.play(FadeIn(b5))
        self.next_slide()

        b5_s1 = sub_bullet(
            r"The contracted Bianchi identity implies the Einstein tensor "
            r"is divergence-free — a direct consequence of the smooth "
            r"Bianchi identities.",
            b5,
        )
        self.play(FadeIn(b5_s1))
        self.next_slide()

        b5_s2 = sub_bullet(
            r"We have a discrete Bianchi identity — can this structural "
            r"property extend to discrete Einstein equations?",
            b5_s1,
        )
        self.play(FadeIn(b5_s2))
        # self.play(FadeOut(img3), FadeIn(img4))
        self.wait()
        self.next_slide()
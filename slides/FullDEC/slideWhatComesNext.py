from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slideFutureWork(Slide):
    def construct(self):

        title = Tex(r"What comes next?", font_size=30).to_corner(UL)
        self.add(title)
        self.next_slide()

        TEXT_WIDTH      = 6.5
        TEXT_WIDTH_SUB  = 6.0
        MAIN_BUFF       = 0.40
        SUB_BUFF        = 0.18
        TOPIC_BUFF      = 0.40

        def main_bullet(text, anchor, font_size=22, color=WHITE):
            dot  = Tex(r"$\bullet$", font_size=font_size, color=color)
            body = Tex(text, font_size=font_size, color=color)
            body.set_max_width(TEXT_WIDTH)
            grp  = VGroup(dot, body).arrange(RIGHT, buff=0.25)
            grp.next_to(anchor, DOWN, aligned_edge=LEFT, buff=MAIN_BUFF)
            grp.to_edge(LEFT, buff=0.4)
            return grp

        def sub_bullet(text, anchor, font_size=21, color=GRAY):
            dot  = Tex(r"$\circ$", font_size=font_size, color=color)
            body = Tex(text, font_size=font_size, color=color)
            body.set_max_width(TEXT_WIDTH_SUB)
            grp  = VGroup(dot, body).arrange(RIGHT, buff=0.25)
            grp.next_to(anchor, DOWN, aligned_edge=LEFT, buff=SUB_BUFF)
            grp.shift(RIGHT * 0.5)
            return grp

        # ── images — right column (uncomment when ready) ─────────────────────
        # img1 = ImageMobject("figures/elasticity.png")
        # img1.height = 2.0
        # img1.move_to(RIGHT * 3.8 + UP * 2.0)

        # img2 = ImageMobject("figures/hexmesh.png")
        # img2.height = 2.0
        # img2.move_to(RIGHT * 3.8 + UP * 0.0)

        # img3 = ImageMobject("figures/relativity.png")
        # img3.height = 2.0
        # img3.move_to(RIGHT * 3.8 + DOWN * 2.0)

        # =====================================================================
        # TOPIC 1 — Elasticity
        # =====================================================================
        b1 = main_bullet(
            r"\textbf{Elasticity}",
            title,
        )
        self.play(FadeIn(b1))
        self.next_slide()

        b1_s1 = sub_bullet(
            r"Stress is naturally a covector-valued 2-form — "
            r"momentum balance becomes a discrete Stokes-type theorem.",
            b1,
        )
        self.play(FadeIn(b1_s1))
        self.next_slide()

        b1_s2 = sub_bullet(
            r"Can we turn the intrinsic geometric formulation "
            r"into a practical discrete algorithm?",
            b1_s1,
        )
        self.play(FadeIn(b1_s2))
        # self.play(FadeIn(img1))
        self.next_slide()

        # =====================================================================
        # TOPIC 2 — Torsion in 3D and Hex Meshing
        # =====================================================================
        b2 = main_bullet(
            r"\textbf{Torsion in 3D and Hex Meshing}",
            b1_s2,
        )
        b2.shift(DOWN * TOPIC_BUFF)
        self.play(FadeIn(b2))
        self.next_slide()

        b2_s1 = sub_bullet(
            r"In 2D, torsion introduces a controlled twist in the frame field.",
            b2,
        )
        self.play(FadeIn(b2_s1))
        self.next_slide()

        b2_s2 = sub_bullet(
            r"Can torsion control help design better frame fields "
            r"and improve robustness of hex meshing pipelines in 3D?",
            b2_s1,
        )
        self.play(FadeIn(b2_s2))
        # self.play(FadeIn(img2))
        self.next_slide()

        # =====================================================================
        # TOPIC 3 — General Relativity
        # =====================================================================
        b3 = main_bullet(
            r"\textbf{General Relativity}",
            b2_s2,
        )
        b3.shift(DOWN * TOPIC_BUFF)
        self.play(FadeIn(b3))
        self.next_slide()

        b3_s1 = sub_bullet(
            r"The contracted Bianchi identity implies the Einstein tensor "
            r"is divergence-free $\Rightarrow$ Energy-momentum conservation.",
            b3,
        )
        self.play(FadeIn(b3_s1))
        self.next_slide()

        b3_s2 = sub_bullet(
            r"We have a discrete Bianchi identity — "
            r"can this extend to discrete Einstein equations?",
            b3_s1,
        )
        self.play(FadeIn(b3_s2))
        # self.play(FadeIn(img3))
        self.wait()
        self.next_slide()
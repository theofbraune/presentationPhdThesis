from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np

from utils.videoLoop import play_video_loop


class slideDiscreteLeviCivita(Slide):
    def construct(self):

        title = Tex(
            r"Discrete Levi-Civita Connection",
            font_size=30,
        ).to_corner(UL)
        self.play(FadeIn(title))
        self.wait()
        self.next_slide()

        textLCPolyhedral = Tex(
            r"On polyhedral surfaces: discrete connection, one scalar per dual edge",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        imageBunny = ImageMobject("figures/sphere.png").to_corner(DR).shift(
            LEFT * 0.5 + UP * 0.5).scale(0.25)
        self.play(FadeIn(textLCPolyhedral), FadeIn(imageBunny))
        self.wait()
        self.next_slide()

        textLCPolyhedral2 = Tex(
            r"On polyhedral surfaces, the Levi-Civita connection is "
            r"the \textit{hinge-connection}",
            font_size=24,
        ).next_to(textLCPolyhedral, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textLCPolyhedral2), FadeOut(imageBunny))
        self.wait()
        self.next_slide()
        imageFirst = ImageMobject("figures/renderHinge/outCropped/output_0001.png")
        imageFirst.height = 3.5
        imageFirst.position = ORIGIN
        self.play(FadeIn(imageFirst))
        self.wait()
        self.next_slide()


        # --- hinge video ---
        self.remove(imageFirst)
        my_video = play_video_loop(
            self,
            frame_dir="figures/renderHinge/outCropped/",
            position=ORIGIN,
            height=3.5,
            fps=20,
            fade_in_time=0.5,
            fade_out_time=0.5,
            persist=True,
        )
        self.wait()

        imagePolyhedral = ImageMobject("figures/CAD_model.png").next_to(
            textLCPolyhedral2, DOWN, aligned_edge=LEFT, buff=0.4).scale(0.5)
        self.play(FadeIn(imagePolyhedral), FadeOut(my_video))

        imageSphere = ImageMobject("figures/sphere.png").next_to(
            textLCPolyhedral2, DOWN, aligned_edge=LEFT, buff=0.4
        ).scale(0.3).shift(2 * UP)
        imageBunny = ImageMobject("figures/bunnyPolyhedral.png").next_to(
            imageSphere, RIGHT, buff=0.4
        ).scale(0.3).shift(2 * UP)

        self.next_slide()
        self.play(FadeOut(imagePolyhedral), FadeIn(imageSphere), FadeIn(imageBunny))
        self.wait()
        self.next_slide()
        self.play(FadeOut(imageSphere), FadeOut(imageBunny))

        # =====================================================================
        # STRIKETHROUGH "polyhedral" — red highlight + red line drawn over it
        # =====================================================================
        textLCPolyhedralConv = Tex(
            r"On \textcolor{red}{polyhedral} surfaces: "
            r"discrete connection, one scalar per dual edge",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)

        textLCPolyhedral2Conv = Tex(
            r"On \textcolor{red}{polyhedral} surfaces, "
            r"the Levi-Civita connection is the \textit{hinge-connection}",
            font_size=24,
        ).next_to(textLCPolyhedral, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(
            Transform(textLCPolyhedral,  textLCPolyhedralConv),
            Transform(textLCPolyhedral2, textLCPolyhedral2Conv),
        )
        self.next_slide()

        # draw red strikethrough lines over "polyhedral" in both texts
        # tune word_start_frac / word_end_frac by eye
        def make_strike(tex_obj, start_frac=0.04, end_frac=0.27,
                        color=RED, stroke_width=5):
            w      = tex_obj.width
            left_x = tex_obj.get_left()[0] + start_frac * w
            rght_x = tex_obj.get_left()[0] + end_frac   * w
            mid_y  = tex_obj.get_center()[1]
            return Line(
                np.array([left_x, mid_y, 0]),
                np.array([rght_x, mid_y, 0]),
                color=color, stroke_width=stroke_width,
            )

        strike1 = make_strike(textLCPolyhedralConv,  start_frac=0.04, end_frac=0.27)
        strike2 = make_strike(textLCPolyhedral2Conv, start_frac=0.04, end_frac=0.27)
        self.play(Create(strike1), Create(strike2))
        self.wait()
        self.next_slide()

        # =====================================================================
        # SMOOTH SURFACE TEXT
        # =====================================================================
        textApproxSmooth = Tex(
            r"Instead, treat the polyhedral surface as an approximation "
            r"of a smooth surface",
            font_size=24,
        ).next_to(textLCPolyhedral2Conv, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textApproxSmooth))
        self.wait()

        textGaussianCurvature = Tex(
            r"Based on the Gaussian curvature, derive a "
            r"closed-form Levi-Civita expression",
            font_size=24,
        ).next_to(textApproxSmooth, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textGaussianCurvature))
        self.wait()
        self.next_slide()

        # =====================================================================
        # CONE DIAGRAM: triangulated → smooth + formula
        # =====================================================================
        cone_tri = ImageMobject("figures/conical.png")
        cone_tri.height = 2.0
        cone_tri.next_to(textGaussianCurvature, DOWN, aligned_edge=LEFT, buff=0.4)

        label_tri = Tex(r"polyhedral", font_size=19, color=GRAY
                        ).next_to(cone_tri, DOWN, buff=0.12)

        arrow_cone = Arrow(
            LEFT * 0.2, RIGHT * 0.2,
            buff=0, color=WHITE, stroke_width=3,
            max_tip_length_to_length_ratio=0.35,
        ).next_to(cone_tri, RIGHT, buff=0.3).shift(UP * 0.05)

        cone_smooth = ImageMobject("figures/constant_curvature.png")
        cone_smooth.height = 2.0
        cone_smooth.next_to(arrow_cone, RIGHT, buff=0.3)

        label_smooth = Tex(r"constant curvature", font_size=19, color=GRAY
                           ).next_to(cone_smooth, DOWN, buff=0.12)

        formula_lc = MathTex(
            r"\nabla^{\mathrm{LC}} = \frac{1}{2} \kappa r^2 d\varphi",
            font_size=30,
        ).next_to(cone_smooth, RIGHT, buff=0.4).shift(UP * 0.1)

        formula_caption = Tex(
            r"Closed-form LC from Gaussian curvature $K_i$",
            font_size=22, color=YELLOW,
        ).next_to(formula_lc, DOWN, buff=0.15).align_to(formula_lc, LEFT)

        self.play(FadeIn(cone_tri), FadeIn(label_tri))
        self.next_slide()
        self.play(GrowArrow(arrow_cone))
        self.play(FadeIn(cone_smooth), FadeIn(label_smooth))
        self.next_slide()
        self.play(FadeIn(formula_lc))
        self.play(FadeIn(formula_caption))
        self.wait()
        self.next_slide()

        
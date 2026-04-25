from manim import *
from manim_slides import Slide, ThreeDSlide
import utils.preamble as preamble
import numpy as np


class slideDiscreteBundleValuedForm(Slide):
    def construct(self):

        title = Tex(
            r"Discrete Bundle-Valued Differential Forms",
            font_size=30,
        ).to_corner(UL)
        self.add(title)

        LEFT_EDGE   = -6.5   # left anchor x
        TEXT_WIDTH  = 5.5    # max width of text column
        IMG_X       = 2.8    # center x of image column

        heightImage = 4
        position = ORIGIN + 2.5*RIGHT + UP * 0.5

        def left_tex(text, font_size=23):
            t = Tex(text, font_size=font_size)
            t.set_max_width(TEXT_WIDTH)
            return t

        imageBase = ImageMobject("figures/discreteFormsAndCurvature/oneSimplexSetup.png" )
        imageBase.set_height(heightImage)
        imageBase.move_to(position)
        self.add(imageBase)

        # =====================================================================
        # BEAT 1 — scalar vs bundle-valued, arrow layout
        # =====================================================================

        label_scalar = Tex(r"\textit{Discrete scalar $k$-form:}", font_size=23,
                           color=WHITE)
        arrow_scalar = Tex(r"$\rightarrow$", font_size=23)
        val_scalar   = Tex(r"one scalar per oriented $k$-cell",
                           font_size=23, color=YELLOW)

        label_bundle = Tex(r"\textit{Discrete bundle-valued $k$-form:}",
                           font_size=23, color=WHITE)
        
        arrow_bundle = Tex(r"$\rightarrow$", font_size=23)
        val_bundle   = Tex(r"one vector per oriented $k$-cell \textbf{and} fiber"
                           r"\quad $\alpha(\sigma, v_i)$",
                           font_size=23, color=YELLOW)

        # position row 1
        label_scalar.next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        arrow_scalar.next_to(label_scalar, DOWN, aligned_edge=LEFT, buff=0.15)
        val_scalar.next_to(arrow_scalar,   RIGHT, buff=0.15).align_to(
            arrow_scalar, UP)

        # position row 2
        label_bundle.next_to(arrow_scalar, 1.5*DOWN, aligned_edge=LEFT, buff=0.4)
        arrow_bundle.next_to(label_bundle, DOWN, aligned_edge=LEFT, buff=0.15)
        val_bundle.next_to(arrow_bundle,   RIGHT, buff=0.15).align_to(
            arrow_bundle, UP)

        # constrain everything to left column
        for mob in [label_scalar, arrow_scalar, val_scalar,
                    label_bundle, arrow_bundle, val_bundle]:
            mob.set_max_width(TEXT_WIDTH)

        self.play(FadeIn(label_scalar), FadeIn(arrow_scalar), FadeIn(val_scalar))
        self.next_slide()
        self.play(FadeIn(label_bundle))
        imagebundleVal1 = ImageMobject("figures/discreteFormsAndCurvature/discreteKform/discreteKform1.png" )
        imagebundleVal1.set_height(heightImage)
        imagebundleVal1.move_to(position)
        self.wait()
        self.next_slide()

        self.play(Transform(imageBase, imagebundleVal1), run_time=1.0)
        imagebunfleVal2 = ImageMobject("figures/discreteFormsAndCurvature/discreteKform/discreteKform2.png" )
        imagebunfleVal2.set_height(heightImage)
        imagebunfleVal2.move_to(position)
        self.wait()
        self.next_slide()
        self.play(Transform(imageBase, imagebunfleVal2), run_time=1.0)
        
        imagebundleVal3 = ImageMobject("figures/discreteFormsAndCurvature/discreteKform/discreteKform3.png" )
        imagebundleVal3.set_height(heightImage)
        imagebundleVal3.move_to(position)
        
        self.wait()
        self.next_slide()
        self.play(Transform(imageBase, imagebundleVal3), run_time=1.0)

        imagebundleVal4 = ImageMobject("figures/discreteFormsAndCurvature/discreteKform/discreteKform4.png" )
        imagebundleVal4.set_height(heightImage)
        imagebundleVal4.move_to(position)
        self.wait()
        self.next_slide()

        self.play(Transform(imageBase, imagebundleVal4), run_time=1.0)

        imagebundleVal5 = ImageMobject("figures/discreteFormsAndCurvature/discreteKform/discreteKform5.png" )
        imagebundleVal5.set_height(heightImage)
        imagebundleVal5.set
        imagebundleVal5.move_to(position)
        self.wait()
        self.next_slide()

        self.play(Transform(imageBase, imagebundleVal5), run_time=1.0)
        self.wait()
        self.next_slide()

        self.play(FadeIn(arrow_bundle), FadeIn(val_bundle))
        self.next_slide()

        # # image on the right
        # imgForms = ImageMobject("figures/two_forms_bundle_valued.png")
        # imgForms.height = 3.2
        # imgForms.move_to(np.array([IMG_X, 0.5, 0]))
        # self.play(FadeIn(imgForms))
        # self.next_slide()

        # # =====================================================================
        # # BEAT 2 — discrete curvature
        # # =====================================================================

        label_Curv = Tex(r"\textit{Smooth Curvature 2-form:}",
                           font_size=23, color=WHITE)
        
        arrow_Curv = Tex(r"$\rightarrow$", font_size=23)
        val_Curv   = Tex(r"Endomorphism-valued 2-form measuring path-dependence\\ of parallel transport.",
                           font_size=23, color=YELLOW)
        
        label_Curv.next_to(arrow_bundle, 1.5*DOWN, aligned_edge=LEFT, buff=0.4)
        arrow_Curv.next_to(label_Curv, DOWN, aligned_edge=LEFT, buff=0.15)
        val_Curv.next_to(arrow_Curv,   RIGHT, buff=0.15).align_to(arrow_Curv, UP)

        self.play(FadeIn(label_Curv), FadeIn(arrow_Curv), FadeIn(val_Curv))
        self.next_slide()

        label_discreteCurv = Tex(
            r"\textit{Discrete curvature:}",
            font_size=23,
            color=WHITE,
        ).next_to(arrow_Curv, 1.5*DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(label_discreteCurv))
        imageDiscreteCurv1 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature1.png" )
        self.next_slide()
        imageDiscreteCurv1.set_height(heightImage)
        imageDiscreteCurv1.move_to(position)
        self.play(FadeIn(imageDiscreteCurv1), run_time=1.0)
        self.next_slide()
        imageDiscreteCurv2 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature2.png" )
        imageDiscreteCurv2.set_height(heightImage)
        imageDiscreteCurv2.move_to(position)
        self.play(Transform(imageDiscreteCurv1, imageDiscreteCurv2), run_time=1.0)
        self.next_slide()   

        imageDiscreteCurv3 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature3.png" )
        imageDiscreteCurv3.set_height(heightImage)
        imageDiscreteCurv3.move_to(position)
        self.play(Transform(imageDiscreteCurv1, imageDiscreteCurv3), run_time=1.0)
        self.next_slide()

        imageDiscreteCurv4 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature4.png" )
        imageDiscreteCurv4.set_height(heightImage)
        imageDiscreteCurv4.move_to(position)
        self.play(Transform(imageDiscreteCurv1, imageDiscreteCurv4), run_time=1.0)
        self.next_slide()

        imageDiscreteCurv5 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature5.png" )
        imageDiscreteCurv5.set_height(heightImage)
        imageDiscreteCurv5.move_to(position)
        self.play(Transform(imageDiscreteCurv1, imageDiscreteCurv5), run_time=1.0)
        self.next_slide()

        imageDiscreteCurv6 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature6.png" )
        imageDiscreteCurv6.set_height(heightImage)
        imageDiscreteCurv6.move_to(position)
        self.play(Transform(imageDiscreteCurv1, imageDiscreteCurv6), run_time=1.0)
        self.next_slide()

        imageDiscreteCurv7 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature7.png" )
        imageDiscreteCurv7.set_height(heightImage)
        imageDiscreteCurv7.move_to(position)
        self.play(Transform(imageDiscreteCurv1, imageDiscreteCurv7), run_time=1.0)
        self.next_slide()

        imageDiscreteCurv8 = ImageMobject("figures/discreteFormsAndCurvature/discreteCurv/discreteCurvature8.png" )
        imageDiscreteCurv8.set_height(heightImage)
        imageDiscreteCurv8.move_to(position)
        self.play(Transform(imageDiscreteCurv1, imageDiscreteCurv8), run_time=1.0)
        self.next_slide()

        arrow_discreteCurv = Tex(r"$\rightarrow$", font_size=23).next_to(label_discreteCurv, DOWN, aligned_edge=LEFT, buff=0.15)
        val_discreteCurv = Tex(r"Given evaluation $v_0$ and cut $v_2$ fibers, measure discrete path-dependance ", font_size=23, color=YELLOW)
        val_discreteCurv.next_to(arrow_discreteCurv,   RIGHT, buff=0.15).align_to(
            arrow_discreteCurv, UP)
        self.play(FadeIn(arrow_discreteCurv), FadeIn(val_discreteCurv))
        self.next_slide()


        # textCurv2 = left_tex(
        #     r"Discrete curvature: given a 2-cell $\sigma = [v_0,v_1,v_2]$, "
        #     r"evaluation fiber $v_0$, cut fiber $v_2$:"
        # ).next_to(textCurv, DOWN, aligned_edge=LEFT, buff=0.3)
        # curv_formula = MathTex(
        #     r"\Omega^\nabla([v_0,v_1,v_2],\, v_0,\, v_2) "
        #     r"\;=\; R_{v_0 v_1} R_{v_1 v_2} - R_{v_0 v_2}",
        #     font_size=24,
        # ).next_to(textCurv2, DOWN, aligned_edge=LEFT, buff=0.2)
        # curv_formula.set_max_width(TEXT_WIDTH)

        # self.play(FadeIn(textCurv2), FadeIn(curv_formula))
        # self.next_slide()

        textAbusive = left_tex(
            r"\textit{Note:} a continuous endomorphism-valued form, "
            r"but discrete — a homomorphism between fibers."
        ).next_to(arrow_discreteCurv, 1.5*DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textAbusive))
        self.wait()
        self.next_slide()
from manim import *
from manim_slides import Slide
import utils.preamble as preamble
from utils.videoLoop import *


class BundleValuedFormsIntro(Slide):
    def construct(self):

        title = Tex(r"Bundle-Valued Differential Forms", font_size=32).to_corner(UL)
        self.play(FadeIn(title))
        self.next_slide()

        textElasticBody = Tex(r" Consider the following elastic body:", font_size=24).next_to(title, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(FadeIn(textElasticBody))
        self.next_slide()
        height = 6.0
        position = 3 * RIGHT
        firstVideoSeq = play_video_loop_with_custom_range(
            self,
            frame_dir = "figures/visualizeStress/",
            position = position,
            height = height,
            fps = 20,
            fade_in_time = 0.5,
            fade_out_time = 0.5,
            persist = True,
            max_frames=48
        )
        self.wait()
        self.next_slide()
        self.remove(firstVideoSeq)
        secondVideoSeq = play_video_loop_with_custom_range(
            self,
            frame_dir = "figures/visualizeStress/",
            position = position,
            height = height,
            fps = 20,
            fade_in_time = 0.5,
            fade_out_time = 0.5,
            persist = True,
            start_frame = 48,
            max_frames=24
        )
        self.wait()
        self.next_slide()

        textForceOnStencil = Tex(r"What is the force attacking on the stencil?", font_size=24).next_to(textElasticBody, DOWN, buff=0.5, aligned_edge=LEFT)
        imageStencil = ImageMobject("figures/illustrateStress/stencilCropped.png")
        imageStencil.height = height 
        imageStencil.move_to(position)
        self.play(FadeIn(textForceOnStencil), FadeIn(imageStencil))
        self.next_slide()
        self.wait()
        imageStencilWithForce = ImageMobject("figures/illustrateStress/stencilWithStressCropped.png")
        imageStencilWithForce.height = height
        imageStencilWithForce.move_to(position)
        self.play(Transform(imageStencil, imageStencilWithForce), run_time=1.0)
        self.next_slide()
        self.wait()
        imageDifferentStencil = ImageMobject("figures/illustrateStress/stencilFlatCropped.png")
        imageDifferentStencil.height = height
        imageDifferentStencil.move_to(position)
        self.play(Transform(imageStencil, imageDifferentStencil), run_time=1.0)
        self.next_slide()
        self.wait()
        imageStencilWithTraction = ImageMobject("figures/illustrateStress/stencilFlatAnnotatedCropped.png")
        imageStencilWithTraction.height = height
        imageStencilWithTraction.move_to(position)
        self.play(FadeOut(imageStencil), FadeIn(imageStencilWithTraction), run_time=1.0)
        self.next_slide()
        self.wait()
        textStressTensor = Tex(
            r"The \textit{stress tensor} $\sigma$ maps surface normals "
            r"to traction forces.",
            font_size=24,
        ).next_to(textForceOnStencil, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(FadeIn(textStressTensor))
        textStressTensor2 = Tex("$\quad\Rightarrow$ It returns a vector per surface element.",
            font_size=24,
        ).next_to(textStressTensor, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(FadeIn(textStressTensor2))
        self.next_slide()
        self.wait()

        textStressBundleValued = Tex(r"Stress can be viewed as a vector-valued 2-form [Kanso et al. 2007]", font_size=24).next_to(textStressTensor2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(FadeIn(textStressBundleValued))
        self.next_slide()
        self.wait()
        
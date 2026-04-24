from manim import *
from manim_slides import Slide
import utils.preamble as preamble
from utils.videoLoop import *


class BundleValuedFormsIntro2(Slide):
    def construct(self):

        title = Tex(r"Bundle-Valued Differential Forms", font_size=32).to_corner(UL)
        self.play(FadeIn(title))
        self.next_slide()
        height = 5.0
        position1 =  LEFT

        position2 = RIGHT

        imageFlux  = ImageMobject("figures/illustrateStress/fluxScalarValued.png").shift(LEFT)
        imageFlux.height = height
        # imageFlux.move_to(position1)
        # self.play(FadeIn(imageFlux))

        # self.wait()
        # self.next_slide()

        imageStress = ImageMobject("figures/illustrateStress/stressVectorValued2Form.png")
        imageStress.height = height
        group = Group(imageFlux, imageStress).arrange(RIGHT, buff=1.0).move_to(ORIGIN)
        # imageStress.move_to(position2)
        self.play(FadeIn(imageFlux), FadeIn(imageStress))
        
        # self.next_slide()
        # self.wait()
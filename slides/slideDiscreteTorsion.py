from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np

from utils.videoLoop import play_video_loop


class slideDiscreteLeviCivita2(Slide):
    def construct(self):
        title = Tex(r"Discrete Torsion of Connections", font_size=30).to_corner(UL)
        self.add(title)
        self.next_slide()
        textSmooth = Tex(r" Smooth setting: After fixing the Levi-Civita connection, any metric connection differs by a scalar valued 1-form $\alpha$ ", font_size=24).next_to(title, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textSmooth))
        self.wait()
        self.next_slide()
        textDiscrete = Tex(r" Smooth Torsion : $\Theta^\nabla = -\alpha ^\sharp d\mathrm{vol}$", font_size=24).next_to(textSmooth, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textDiscrete))
        self.wait()
        self.next_slide()
        textDiscrete2 = Tex(r" Discrete Torsion of $\nabla = \nabla^{\mathrm{LC}} + J\alpha$ $\rightarrow $\Theta^\nabla =  -\alpha$ ", font_size=24).next_to(textDiscrete, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        surroundingBox = SurroundingRectangle(textDiscrete2, color=YELLOW, buff=0.1)
        self.play(FadeIn(textDiscrete2), Create(surroundingBox))
        self.wait()
        self.next_slide()
        textDiscreteIdentification = Tex(r" We use the identification between discrete 1-forms and vector fields on surfaces ", font_size=24).next_to(textDiscrete2, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textDiscreteIdentification))
        self.wait()
        self.next_slide()
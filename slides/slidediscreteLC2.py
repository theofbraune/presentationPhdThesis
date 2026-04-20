from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np

from utils.videoLoop import play_video_loop


class slideDiscreteLeviCivita2(Slide):
    def construct(self):

        title = Tex(
            r"Discrete Levi-Civita Connection",
            font_size=30,
        ).to_corner(UL)
        self.play(FadeIn(title))
        # self.wait()
        self.next_slide()

        
        textDiscreteExpr = Tex(r"Fit a discrete expression against analytic formula", font_size=24).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textDiscreteExpr))
        self.wait()
        self.next_slide()
        textDiscreteExpr2 = Tex(r"Closed form formula that distributes rotation angles ", font_size=24).next_to(textDiscreteExpr, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        # put the diamond right in the middle of the second column
        imageDiamond = ImageMobject("figures/edge_diamond.png").next_to(textDiscreteExpr2, RIGHT, aligned_edge=RIGHT, buff=0.4).shift(2*RIGHT+DOWN*0.5)
        formulaLC = Tex(r"$\alpha^{\mathrm{LC}}_{ij} = \eta_{ij} + \frac{1}{\lozenge_{ij}}\left(K_i A_{\ast ij}\left(\frac{A_{\ast ij}}{A_i} - \frac{\varphi_{\ast ij}}{\Phi_i} \right) - K_j A_{\ast ji}\left( \frac{A_{\ast ji}}{A_j} - \frac{\varphi_{\ast ji}}{\Phi_j} \right) \right)$", font_size=24)
        formulaLC.next_to(imageDiamond, DOWN, buff=0.4)
        self.play(FadeIn(textDiscreteExpr2), FadeIn(imageDiamond), FadeIn(formulaLC))
        self.wait()
        self.next_slide()
        textLowerError = Tex(r" Consistently lower error on 500 examples than the hinge connection ", font_size=24).next_to(textDiscreteExpr2, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        imageConvergence = (
            ImageMobject("figures/convergencePlot.png")
            .scale(0.5)
            .next_to(textLowerError, DOWN, aligned_edge=RIGHT, buff=0.3)
            .to_edge(RIGHT, buff=0.5).shift(2*UP)
        )
        # imageConvergence = ImageMobject("figures/convergencePlot.png").next_to(textLowerError, RIGHT, buff=0.4).scale(0.5).shift(LEFT)
        imageParabola = ImageMobject("figures/parabola1.png").next_to(textLowerError, 4*DOWN, buff=0.4).scale(1.5).shift(LEFT)
        imageParabola2 = ImageMobject("figures/parabola2.png").next_to(imageParabola, RIGHT, buff=0.4).scale(1.5)
        self.play(FadeIn(textLowerError), FadeIn(imageConvergence), FadeOut(formulaLC), FadeOut(imageDiamond), FadeIn(imageParabola), FadeIn(imageParabola2))
        self.wait()
        self.next_slide()

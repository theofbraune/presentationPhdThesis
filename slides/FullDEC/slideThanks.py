from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *

class slideThanks(Slide):
    def construct(self):
        # --- Title ---
        textThanks = Tex("Thank you for your attention!", font_size=60).to_edge(UP, buff=1.0)
        
        self.play(Write(textThanks))
        self.wait()
        self.next_slide()

        # --- Collaborators Heading ---
        textThanksCol = Tex("A big thanks to my collaborators:", font_size=30)
        textThanksCol.next_to(textThanks, DOWN, buff=0.8)
        
        self.play(FadeIn(textThanksCol))
        self.wait()
        self.next_slide()

        # --- Images Setup ---
        IMG_HEIGHT = 2. # Increased slightly since there's no text below now

        # Create the Mobjects and set heights
        img_yiying = ImageMobject("figures/colaborators/yiyingTong.jpeg")
        img_yiying.set_height(IMG_HEIGHT)
        img_mark = ImageMobject("figures/colaborators/markGillespie.png")
        img_mark.set_height(IMG_HEIGHT)
        img_francois = ImageMobject("figures/colaborators/francoisGayBalmaz.jpg")
        img_francois.set_height(IMG_HEIGHT)
        img_mathieu = ImageMobject("figures/colaborators/mathieuDesbrun.jpg")
        img_mathieu.set_height(IMG_HEIGHT)

        # Pack into a Group to handle spacing automatically
        # Order: Yiying, Mark, Francois, Mathieu (or whichever order you prefer)
        colabs_group = Group(img_yiying, img_mark, img_francois, img_mathieu)
        
        # Arrange them in a line with 0.7 units of space between them
        colabs_group.arrange(RIGHT, buff=0.7).shift(DOWN * 0.5)

        # --- Animation ---
        # Staggered entry for a nicer visual flow
        self.play(
            LaggedStart(
                *[FadeIn(img) for img in colabs_group],
                lag_ratio=0.2,
                run_time=1.5
            )
        )
        
        self.wait()
        self.next_slide()
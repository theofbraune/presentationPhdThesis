from manim import *
from manim_slides import Slide
import utils.preamble as preamble

class Intro(Slide):
    def construct(self):
        
        
        title = Tex(r"Geometry Driven Discretization \\ of Differential Operators", color=WHITE).scale(1.5)
        title.to_edge(UP)  # Position the text at the top of the frame

        subtitle = Tex(r"Theo Braune", color=WHITE).next_to(title, 1.5*DOWN)
        subtitle.scale(0.8)

        subtitle_authors = Tex(r" Supervised by Mathieu Desbrun",font_size = 20).next_to(subtitle,DOWN)
        background_image = ImageMobject("figures/connection_2.png").next_to(subtitle_authors, DOWN).scale(0.8)
        # background_image.set_height(FRAME_HEIGHT)  # Set the height of the image to fill the frame
        # background_image.set_width(FRAME_WIDTH)  # Set the width of the image to fill the frame
        self.add(background_image)

        geomerix = ImageMobject("figures/geomerix.png").scale(0.5).to_corner(DL)
        inria = ImageMobject("figures/inr_logo_rouge.png").scale(0.5).next_to(geomerix,3*RIGHT)
        LIX = ImageMobject("figures/logo-lix.png").scale(0.5).to_corner(DR)
        polytechnique = ImageMobject("figures/POLYTECHNIQUE-IP_PARIS_small.png").scale(0.5).next_to(LIX,3*LEFT)

        self.add(title, subtitle, subtitle_authors,geomerix,inria,LIX,polytechnique)
        self.wait()
        
        self.next_slide()
        
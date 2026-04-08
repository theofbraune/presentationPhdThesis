from manim import *
from manim_slides import Slide
from utils import preamble

class GoalSlide(Slide):
    def construct(self):

        title = Tex("Goal", font_size=60).to_corner(UL)
        self.play(FadeIn(title))
        self.wait()
        self.next_slide()

        # --- Main goal text ---
        goal = Tex(
            r"Develop a \textit{structure-preserving} discretization \\"
            r"of Cartan's \textit{bundle-valued exterior calculus}.",
            font_size=40
        )
        goal.move_to(DOWN * 3)
        self.play(goal.animate.move_to(ORIGIN), run_time=1.8, rate_func=smooth)
        self.wait()
        self.next_slide()

        self.remove(title, goal)
        title_text = Text("The Plan", font_size=48).to_corner(UL)
        self.play(FadeIn(title_text))

        # ---- layout parameters ----
        IMG_HEIGHT = 1.5            # uniform height for all figures
        RIGHT_PADDING = 0.8         # distance from the right edge of the frame
        BULLET_SPACING = 1.8        # vertical gap between bullet points
        BULLET_START_Y = 1.1       # y-coordinate of the first bullet (tweak to taste)

        bullet_points = [
            " - Review of Continuous Exterior Calculus",
            " - Case Study: Discrete Torsion of Connection Forms on Simplicial Meshes",
            " - Beyond DEC: A Discrete Exterior Calculus of Bundle Valued Forms",
        ]
        image_paths = [
            "figures/connection_2.png",
            "figures/bunnyFig.png",
            "figures/retraction.png",
        ]

        bullet_point_texts = []
        bullet_point_figs = []

        for i, (point, path) in enumerate(zip(bullet_points, image_paths)):
            # --- bullet text: aligned to the left edge, spaced by BULLET_SPACING ---
            txt = Tex(point, font_size=30)
            txt.to_edge(LEFT, buff=0.8)
            txt.set_y(BULLET_START_Y - i * BULLET_SPACING)
            bullet_point_texts.append(txt)

            # --- image: uniform height, aligned to the right edge ---
            img = ImageMobject(path)
            img.height = IMG_HEIGHT        # rescales uniformly, preserving aspect
            img.to_edge(RIGHT, buff=RIGHT_PADDING)
            img.set_y(txt.get_y())         # vertically centered on its bullet
            bullet_point_figs.append(img)

        # Reveal bullets one by one
        for text, img in zip(bullet_point_texts, bullet_point_figs):
            self.next_slide()
            self.play(FadeIn(text), FadeIn(img))

        self.next_slide()
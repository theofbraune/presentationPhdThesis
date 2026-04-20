from manim import *
from manim_slides import Slide
import utils.preamble as preamble


class TorsionCover(Slide):
    def construct(self):

        # ----- title -----
        title = Tex(
            r"Case Study: Discrete Torsion of Connection Forms On Simplicial Meshes",
            font_size=32,
        ).to_edge(UP, buff=0.4)
        citation = Tex(
            r"\small Braune, Gillespie, Tong, Desbrun — \textit{ACM Trans. Graph.} 2025",
            font_size=18, color=GRAY,
        ).next_to(title, DOWN, buff=0.1)

        self.play(FadeIn(title), FadeIn(citation))
        self.next_slide()

        # ----- paper screenshot slides in from the left -----
        paper = ImageMobject("figures/torsionTeaser.png")
        paper.height = 4.5
        paper.to_edge(LEFT, buff=0.3).set_y(-0.3)  # final resting position

        # start off-screen to the left
        paper.shift(LEFT * 10)
        self.play(paper.animate.shift(RIGHT * 10), run_time=0.9, rate_func=smooth)
        self.next_slide()

        # ----- three result figures slide in from the right -----
        fig_paths = [
            "figures/bunnyFigChop.png",
            # "figures/connection_2.png",
            "figures/diloTorsion.png",
        ]
        # fig_captions = [
        #     r"Torsion on the bunny",
        #     r"Levi-Civita connection",
        #     r"Minimal-torsion frames",
        # ]

        FIG_HEIGHT = 1.8
        FIG_X = 2.8   # horizontal center of the figure column (right half)
        FIG_Y_POSITIONS = [1.5,  -2.1]  # three vertical slots

        figs = []
        for path, y in zip(fig_paths, FIG_Y_POSITIONS):
            img = ImageMobject(path)
            img.height = FIG_HEIGHT
            img.set_x(FIG_X).set_y(y)

            figs.append(img)

            # cap.next_to(img, DOWN, buff=0.1)

            # figs.append(img)
            # caps.append(cap)

        for img in figs:
            # start off-screen to the right
            img.shift(RIGHT * 10)
            self.play(
                img.animate.shift(LEFT * 10),
                run_time=0.6, rate_func=smooth,
            )
            self.next_slide()

        self.wait()
        self.next_slide()
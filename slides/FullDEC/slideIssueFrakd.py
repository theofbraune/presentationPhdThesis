from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slideIssueFrakD(Slide):
    def construct(self):
        title_text = Tex(
            "From Smooth To Discrete Forms", font_size=30
        ).to_corner(UL)
        self.add(title_text)
        self.next_slide()

        # =====================================================================
        # BEAT 1 — setup: solder form + torsion, one beat
        # =====================================================================
        textIntro = Tex(
            r"Take the solder form $\theta \in \Omega^1(M, TM)$, "
            r"$\theta(X) = X$. "
            r"Its torsion under connection $\omega$ is:"
            r"$$d^\nabla\theta \;=\; d\theta + \omega \wedge \theta$$",
            font_size=24,
        ).next_to(title_text, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textIntro))
        self.next_slide()

        textDiscrete = Tex(
            r"Integrate over cells of a simplicial complex "
            r"$\Rightarrow$ discrete bundle-valued forms. "
            r"Apply $\mathfrak{d}^\nabla$ from before.",
            font_size=24,
        ).next_to(textIntro, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textDiscrete))
        self.next_slide()

        # =====================================================================
        # BEAT 2 — convergence plot that doesn't decay
        # =====================================================================
        imgConv = ImageMobject("figures/notConvergenceTorsion.png")
        imgConv.height = 3.2
        imgConv.next_to(textDiscrete, DOWN, aligned_edge=LEFT, buff=0.3)

        conv_caption = Tex(
            r"Error under mesh refinement — \textit{no convergence}.",
            font_size=21, color=RED,
        ).next_to(imgConv, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(FadeIn(imgConv))
        self.play(FadeIn(conv_caption))
        self.next_slide()

        # =====================================================================
        # BEAT 3 — why?
        # =====================================================================
        textWhy = Tex(
            r"Why?", font_size=36, color=YELLOW,
        ).next_to(conv_caption, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textWhy))
        self.wait()
        self.next_slide()

        # =====================================================================
        # CLEAR — transition to formula analysis
        # =====================================================================
        self.play(
            FadeOut(textIntro), FadeOut(textDiscrete),
            FadeOut(imgConv), FadeOut(conv_caption),
            FadeOut(textWhy),
        )
        self.next_slide()

        # =====================================================================
        # rest of the slide unchanged from here ...
        # =====================================================================
        textIntegralOfdNabla = Tex(
            r"Given a 2-cell $c$ with vertex $v_0$, "
            r"we try to approximate $\int_c d^\nabla\theta$:",
            font_size=25,
        ).next_to(title_text, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textIntegralOfdNabla))
        self.wait()
        self.next_slide()

        textFormula = MathTex(
            r"\mathfrak{d}^{\nabla}\theta([v_0,v_1,v_2],v_0) = "
            r"\mathcal{R}_{0,1}\,\theta([v_1,v_2],v_1) "
            r"-\theta([v_0,v_2],v_0) +\theta([v_0,v_1],v_0)",
            font_size=25,
        ).next_to(textIntegralOfdNabla, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textFormula))
        self.wait()
        self.next_slide()

        textFormula2 = MathTex(
            r"\mathfrak{d}^{\nabla}\theta([v_0,v_1,v_2],v_0) = "
            r"\mathcal{R}_{0,1}\,\theta([v_1,v_2],v_1) "
            r"-\theta([v_0,v_2],v_0) +\theta([v_0,v_1],v_0) "
            r"\approx \int_{c} d^{\nabla}\theta = \int_{c} d\theta",
            font_size=25,
        ).next_to(textIntegralOfdNabla, DOWN, aligned_edge=LEFT)
        textLastOmegaWedge = MathTex(
            r"+\int_{c} \omega \wedge \theta",
            font_size=25,
        ).next_to(textFormula2, RIGHT)

        self.play(FadeOut(textFormula), FadeIn(textFormula2, textLastOmegaWedge))
        self.wait()
        self.next_slide()

        highlight_box = SurroundingRectangle(
            textLastOmegaWedge, color=YELLOW, buff=0.1, corner_radius=0.1,
        )
        self.play(Create(highlight_box))
        self.wait()
        self.next_slide()

        explanation = Tex(
            r"Not a boundary integral!",
            font_size=24,
        ).next_to(textLastOmegaWedge, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(explanation))
        self.wait()
        self.next_slide()

        textIdeaPPF = Tex(
            r"The expression for $\omega$ depends on the choice of frame field.",
            font_size=25,
        ).next_to(textFormula2, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textIdeaPPF))
        self.wait()
        self.next_slide()

        textPPF = Tex(
            r"Idea: choose a frame field such that "
            r"$\omega \in \mathcal{O}(h)$ — then the term is small enough "
            r"and we get convergence.",
            font_size=25,
        ).next_to(textIdeaPPF, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(textPPF))
        self.wait()
        self.next_slide()
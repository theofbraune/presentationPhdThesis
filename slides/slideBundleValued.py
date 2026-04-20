from manim import *
from manim_slides import Slide
import utils.preamble as preamble


class BundleValuedFormsIntro(Slide):
    def construct(self):

        title = Tex(r"Bundle-Valued Differential Forms", font_size=32).to_corner(UL)
        self.play(FadeIn(title))
        self.next_slide()

        # =====================================================================
        # BEAT 1 — recall scalar forms
        # =====================================================================
        recall = Tex(
            r"Recall: a scalar $k$-form $\alpha \in \Omega^k(M)$ "
            r"measures oriented $k$-dimensional content — it returns a \textit{number}.",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(recall))
        self.next_slide()

        # =====================================================================
        # BEAT 2 — the generalisation: return a vector instead
        # =====================================================================
        generalise = Tex(
            r"What if, instead of a number, we want to return a \textit{vector} "
            r"in a fiber $E_p$?",
            font_size=24,
        ).next_to(recall, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(generalise))
        self.next_slide()

        # =====================================================================
        # BEAT 3 — bullet points
        # =====================================================================
        BULLET_X    = -5.8          # left edge
        START_Y     =  0.6          # y of first bullet
        SPACING     =  1.05         # vertical gap between bullets

        def bullet(text, y, font_size=23):
            dot = Tex(r"$\bullet$", font_size=font_size).move_to(
                np.array([BULLET_X + 0.1, y, 0])
            ).align_to(np.array([BULLET_X, y, 0]), LEFT)
            body = Tex(text, font_size=font_size).next_to(
                dot, RIGHT, buff=0.25
            ).align_to(dot, UP)
            return VGroup(dot, body)

        b1 = bullet(
            r"A \textit{bundle-valued $k$-form} $\alpha \in \Omega^k(M, E)$ "
            r"eats $k$ tangent vectors and returns an element of the fiber $E_p$.",
            START_Y,
        )
        b2 = bullet(
            r"Formally: $\Omega^k(M, E) \;=\; \Omega^k(M) \otimes E$ "
            r"— tensor the usual $k$-forms with the bundle.",
            START_Y - SPACING,
        )
        b3 = bullet(
            r"Intuition: the same measurement idea as before, "
            r"but the \textit{result is a vector}, not a scalar.",
            START_Y - 2 * SPACING,
        )
        # b4 = bullet(
        #     r"Examples: the \textit{torsion} $\Theta^\nabla \in \Omega^2(M, TM)$, "
        #     r"the \textit{curvature} $\Omega^\nabla \in \Omega^2(M, \mathrm{End}(E))$.",
        #     START_Y - 3 * SPACING,
        # )

        for b in [b1, b2, b3]:
            self.play(FadeIn(b))
            self.next_slide()

        # # =====================================================================
        # # BEAT 4 — side-by-side visual comparison
        # # =====================================================================
        # scalar_img = ImageMobject("figures/two_forms_scalar_valued.png").scale(0.85)
        # bundle_img = ImageMobject("figures/two_forms_bundle_valued.png").scale(0.85)
        # scalar_img.shift(LEFT * 3 + DOWN * 1.2)
        # bundle_img.shift(RIGHT * 1.5 + DOWN * 1.2)

        # scalar_label = Tex(
        #     r"scalar 2-form: returns a \textit{number}",
        #     font_size=22,
        # ).next_to(scalar_img, UP, buff=0.15)
        # bundle_label = Tex(
        #     r"bundle-valued 2-form: returns a \textit{vector}",
        #     font_size=22,
        # ).next_to(bundle_img, UP, buff=0.15)

        # self.play(
        #     FadeOut(recall), FadeOut(generalise),
        #     FadeOut(b1), FadeOut(b2), FadeOut(b3), FadeOut(b4),
        # )
        # self.play(FadeIn(scalar_img), FadeIn(scalar_label))
        # self.next_slide()
        # self.play(FadeIn(bundle_img), FadeIn(bundle_label))
        # self.next_slide()

        # # =====================================================================
        # # BEAT 5 — punchline: to differentiate them we need d^\nabla
        # # =====================================================================
        # punchline = Tex(
        #     r"To differentiate bundle-valued forms we need the "
        #     r"\textit{covariant exterior derivative} $d^{\nabla} = d + \omega \wedge$.",
        #     font_size=24, color=YELLOW,
        # ).to_edge(DOWN, buff=0.6)
        # self.play(FadeIn(punchline))
        # self.wait()
        # self.next_slide()
from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np


class slideTorsionIntro(Slide):
    def construct(self):

        # ================================================================
        # TITLE
        # ================================================================
        title = Tex(
            r"Torsion: An Example of the Covariant Exterior Derivative",
            font_size=30,
        ).to_corner(UL)
        self.play(FadeIn(title))
        self.wait()
        self.next_slide()

        # ================================================================
        # BEAT 1 — TORSION AS d^nabla OF THE SOLDER FORM
        # ================================================================
        intro = Tex(
            r"For $E = TM$, the solder form $\theta \in \Omega^1(M, TM)$ "
            r"maps each tangent vector to itself.",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(intro))
        solderTex = MathTex(r"\theta[X] = X", font_size=34).next_to(intro, DOWN+RIGHT, buff=0.3)
        self.play(FadeIn(solderTex))
        self.wait()
        self.next_slide()
        self.remove(solderTex)
        self.next_slide()

        torsion_def = Tex(
            r"Natural example of $d^\nabla$:  \textit{Torsion 2-form}:",
            font_size=24,
        ).next_to(intro, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(torsion_def))
        self.next_slide()

        torsion_formula = MathTex(
            r"\Theta^\nabla \;=\; d^\nabla\theta \;=\; d\theta + \omega \wedge \theta",
            font_size=34,
        ).next_to(torsion_def, DOWN, aligned_edge=LEFT, buff=0.3)
        torsion_formula_box = SurroundingRectangle(torsion_formula, color=BLUE_C, buff=0.15)
        self.play(FadeIn(torsion_formula))
        self.play(Create(torsion_formula_box))
        self.wait(0.5)
        self.next_slide()

        # ================================================================
        # BEAT 2 — LEVI-CIVITA: THE CANONICAL REFERENCE
        # ================================================================
        lc_title = Tex(r"Connections \& curvature", font_size=30).to_corner(UL)
        new_title = Tex(
            r"The Levi-Civita connection: a canonical reference",
            font_size=30,
        ).to_corner(UL)
        self.play(
            FadeOut(intro),
            FadeOut(torsion_def),
            FadeOut(torsion_formula),
            FadeOut(torsion_formula_box),
            Transform(title, new_title),
        )
        self.next_slide()

        lcTeaserText = Tex(r"For any choice of torsion, there is a unique metric preserving connection realizing it.", font_size=24).next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(lcTeaserText))
        self.wait()
        self.next_slide()
        # First part appears immediately
        lcTeaserText2 = Tex(
            r"Zero torsion $\Rightarrow$ the \textit{Levi-Civita connection} $\nabla^{\mathrm{LC}}$: the unique torsion-free metric connection.",
        font_size=24
        ).next_to(lcTeaserText, DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(FadeIn(lcTeaserText2))
        self.wait()
        self.next_slide()  # ← key press here

          
        # lc_img = ImageMobject("figures/levi_civita.png")   # swap for your wikipedia screenshot
        # lc_img.scale(0.75).to_edge(RIGHT).shift(DOWN * 0.5)
        # self.play(FadeIn(lc_img))
        # self.next_slide()
        # torsion_meaning = Tex(
        #     r"$\Theta^\nabla = 0 \;\Leftrightarrow\; \nabla = \nabla^{\mathrm{LC}}$: "
        #     r"torsion measures the \textit{deviation} from the Levi-Civita connection.",
        #     font_size=24,
        # ).next_to(lc_name, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.play(FadeIn(torsion_meaning))
        # self.wait()
        # self.next_slide()

        # ================================================================
        # BEAT 4 — AFFINE SPACE OF CONNECTIONS
        # ================================================================
       
        # self.next_slide()

        affine_text = Tex(
            r"Metric connections on a surfaces: \textit{affine space}: ",
            font_size=24,
        ).next_to(lcTeaserText2, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(affine_text))
        self.next_slide()
        affineTransform = Tex("Given a reference connection, ALL connections differ by a 1-form", font_size=24).next_to(affine_text, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(affineTransform))
        self.next_slide()

        # affine_formula = MathTex(
        #     r"\nabla \;=\; \nabla^{\mathrm{LC}} + J\alpha, \qquad \alpha \in \Omega^1(M)",
        #     font_size=28,
        # ).next_to(affineTransform, DOWN, aligned_edge=LEFT, buff=0.4)
        affine_formula = MathTex(r"\omega^{\nabla} = \omega^{\nabla^{\mathrm{LC}}} + \begin{pmatrix}0 & -\alpha\\ \alpha& 0\end{pmatrix}, \qquad \alpha \in \Omega^1(M)", font_size=28).next_to(affineTransform, DOWN, aligned_edge=LEFT, buff=0.4)
        affine_box = SurroundingRectangle(affine_formula, color=BLUE_C, buff=0.15)
        self.play(FadeIn(affine_formula), Create(affine_box))
        self.next_slide()

        text = Tex(r"Lets compute the torsion of $\nabla$ in terms of $\alpha$.", font_size=24).next_to(affine_formula, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(text))
        self.next_slide()
        titleTorsion = Tex(r" Torsion of $\nabla = \nabla^{\mathrm{LC}} + J\alpha$", font_size=30).to_corner(UL)
        self.play(
            FadeOut(lcTeaserText),
            FadeOut(lcTeaserText2),
            FadeOut(affine_text),
            FadeOut(affineTransform),
            FadeOut(affine_formula),
            FadeOut(affine_box),
            FadeOut(text),
            Transform(title, titleTorsion),
        )
        self.next_slide()
        text2 = Tex(r"It holds: ", font_size=24).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        formula = MathTex(r"\Theta^\nabla \;=\; d\theta + \omega^\nabla \wedge \theta ", font_size=34).next_to(text2, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(text2), FadeIn(formula))
        self.next_slide()
        # ── step 1: show the initial expansion ──────────────────────────────
        f_zero = MathTex(
            r"d\theta + \omega^{\mathrm{LC}} \wedge \theta",
            font_size=34,
        ).next_to(formula, DOWN, aligned_edge=LEFT, buff=0.3)

        f_plus = MathTex(
            r"+ J\alpha \wedge \theta",
            font_size=34,
        ).next_to(f_zero, RIGHT, buff=0.2)

        eq_sign = MathTex(r"=", font_size=34).next_to(formula, 1.1 * DOWN, aligned_edge=LEFT, buff=0.3)
        # reposition: eq = f_zero f_plus in a row
        eq_sign.next_to(formula, 1.1 * DOWN, aligned_edge=LEFT, buff=0.3)
        f_zero.next_to(eq_sign, RIGHT, buff=0.2)
        f_plus.next_to(f_zero, RIGHT, buff=0.2)

        self.play(FadeIn(eq_sign), FadeIn(f_zero), FadeIn(f_plus))
        self.next_slide()

        # ── step 2: strike through the zero part ────────────────────────────
        strike = Line(
            f_zero.get_left()  + DOWN * 0.05,
            f_zero.get_right() + DOWN * 0.05,
            color=RED, stroke_width=4,
        )
        label_zero = MathTex(r"=\,0", font_size=20, color=RED
                             ).next_to(f_zero, DOWN, buff=0.1)
        self.play(Create(strike), FadeIn(label_zero))
        self.next_slide()

        # ── step 3: expand Jα as matrix, append to the right ────────────────
        f_matrix = MathTex(
            r"= \begin{pmatrix}0 & -\alpha \\ \alpha & 0\end{pmatrix}"
            r"\wedge \theta",
            font_size=34,
        ).next_to(f_plus, RIGHT, buff=0.2)
        self.play(Write(f_matrix))
        self.next_slide()
        f_matrix2 = MathTex(
            r"= \begin{pmatrix}0 & -\alpha \\ \alpha & 0\end{pmatrix}"
            r"\wedge \begin{pmatrix}dx \\ dy\end{pmatrix}",
            font_size=34,
        ).next_to(f_plus, RIGHT, buff=0.2)
        self.play(TransformMatchingTex(f_matrix, f_matrix2))
        self.next_slide()

        # ── step 4: append the first result column vector ────────────────────
        f_result1 = MathTex(
            r"= \begin{pmatrix}-\alpha\wedge dy \\ \alpha\wedge dx\end{pmatrix}",
            font_size=34,
        ).next_to(f_matrix2, RIGHT, buff=0.2)
        self.play(Write(f_result1))
        self.next_slide()

        # ── step 5: append the expanded wedge products ───────────────────────
        f_result2 = MathTex(
            r"= \begin{pmatrix}-\alpha_x\,dx\wedge dy \\ "
            r"\alpha_y\,dy\wedge dx\end{pmatrix}",
            font_size=34,
        ).next_to(f_result1, RIGHT, buff=0.2)
        self.play(Write(f_result2))
        self.next_slide()

        # ── step 6: final result below ───────────────────────────────────────
        formula5 = MathTex(
            r"= -\alpha^\sharp\, d\mathrm{vol}",
            font_size=34, color=YELLOW,
        ).next_to(eq_sign, 1.5*DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(formula5))
        self.next_slide()

        textWell = Tex(
            r"Well suited for discretization!",
            font_size=40, color=YELLOW,
        ).next_to(formula5, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textWell))
        self.next_slide()

        # # ================================================================
        # # BEAT 5 — TORSION IS EXACTLY alpha^sharp WEDGE VOLUME FORM
        # # ================================================================
        # torsion_calc_title = Tex(
        #     r"Torsion of $\nabla = \nabla^{\mathrm{LC}} + J\alpha$",
        #     font_size=30,
        # ).to_corner(UL)
        # self.play(
        #     FadeOut(affine_text),
        #     FadeOut(affine_formula),
        #     FadeOut(affine_box),
        #     FadeOut(affine_caption),
        #     Transform(title, torsion_calc_title),
        # )
        # self.next_slide()

        # calc_intro = Tex(
        #     r"Let us compute the torsion of $\nabla = \nabla^{\mathrm{LC}} + J\alpha$. "
        #     r"Since $\nabla^{\mathrm{LC}}$ is torsion-free ($d^{\nabla^{\mathrm{LC}}}\theta = 0$):",
        #     font_size=24,
        # ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        # self.play(FadeIn(calc_intro))
        # self.next_slide()

        # # step 1
        # calc_step1 = MathTex(
        #     r"\Theta^\nabla \;=\; d^\nabla\theta \;=\; d\theta + \omega \wedge \theta",
        #     font_size=26,
        # ).next_to(calc_intro, DOWN, aligned_edge=LEFT, buff=0.4)
        # self.play(FadeIn(calc_step1))
        # self.next_slide()

        # # step 2: substitute omega = omega_LC + Jalpha
        # calc_step2 = MathTex(
        #     r"\;=\; \underbrace{d\theta + \omega^{\mathrm{LC}} \wedge \theta}_{=\,0} "
        #     r"\;+\; J\alpha \wedge \theta",
        #     font_size=26,
        # ).next_to(calc_step1, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.play(FadeIn(calc_step2))
        # self.next_slide()

        # # step 3: simplify J alpha wedge theta
        # calc_step3 = MathTex(
        #     r"\;=\; J\alpha \wedge \theta \;=\; -\alpha^\sharp \, dA",
        #     font_size=26,
        # ).next_to(calc_step2, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.play(FadeIn(calc_step3))
        # self.next_slide()

        # # box the final result
        # result = MathTex(
        #     r"\Theta^\nabla \;=\; -\alpha^\sharp \, dA",
        #     font_size=34,
        # ).next_to(calc_step3, DOWN, aligned_edge=LEFT, buff=0.4)
        # result_box = SurroundingRectangle(result, color=YELLOW, buff=0.2)
        # self.play(FadeIn(result), Create(result_box))
        # self.next_slide()

        # result_caption = Tex(
        #     r"Torsion is entirely encoded in $\alpha$ — the deviation from $\nabla^{\mathrm{LC}}$.",
        #     font_size=23,
        #     color=YELLOW,
        # ).next_to(result, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.play(FadeIn(result_caption))
        # self.wait()
        # self.next_slide()
from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slideDiscreteFrakd(Slide):
    def construct(self):

        title_text = Tex(
            r"Discrete Covariant Exterior Derivative",
            font_size=30,
        ).to_corner(UL)
        self.add(title_text)
        self.wait(1)
        self.next_slide()

        # =====================================================================
        # BEAT 1 — scalar DEC: half-edge arrows + numbers merge to center
        # =====================================================================
        text_b1 = Tex(
            r"Recall: scalar $d\alpha(\sigma)$ = signed sum over $\partial\sigma$.",
            font_size=23,
        ).next_to(title_text, DOWN, aligned_edge=LEFT, buff=0.4).set_max_width(5.0)
        self.play(FadeIn(text_b1))

        # triangle on the RIGHT half of the screen
        v0 = np.array([-0.6, -1.1, 0]) + RIGHT * 4.5+UP
        v1 = np.array([ 1.6, -1.1, 0]) + RIGHT * 4.5+UP
        v2 = np.array([ 0.5,  1.0, 0]) + RIGHT * 4.5+UP
        center = (v0 + v1 + v2) / 3

        tri = Polygon(v0, v1, v2,
                      fill_color=BLUE_E, fill_opacity=0.20,
                      stroke_color=WHITE, stroke_width=2)
        self.play(FadeIn(tri))

        dot0 = Dot(v0, color=WHITE, radius=0.07)
        dot1 = Dot(v1, color=WHITE, radius=0.07)
        dot2 = Dot(v2, color=WHITE, radius=0.07)
        lbl0 = Tex(r"$v_0$", font_size=21).next_to(v0, DL, buff=0.22)
        lbl1 = Tex(r"$v_1$", font_size=21).next_to(v1, DR, buff=0.22)
        lbl2 = Tex(r"$v_2$", font_size=21).next_to(v2, UP,  buff=0.22)
        self.play(FadeIn(dot0), FadeIn(dot1), FadeIn(dot2))
        self.play(FadeIn(lbl0), FadeIn(lbl1), FadeIn(lbl2))
        self.next_slide()

        # half-edge arrows
        INSET = 0.18
        def inset_arrow(start, end, color=RED):
            d = end - start
            d_norm = d / np.linalg.norm(d)
            return Arrow(
                start + INSET * d_norm,
                end   - INSET * d_norm,
                buff=0, color=color,
                tip_length=0.18, stroke_width=3,
                max_tip_length_to_length_ratio=0.25,
            ).set_opacity(0.0)

        arrow_01 = inset_arrow(v0, v1)
        arrow_12 = inset_arrow(v1, v2)
        arrow_20 = inset_arrow(v2, v0)
        boundary_arrows = VGroup(arrow_01, arrow_12, arrow_20)
        self.add(boundary_arrows)

        for arr in [arrow_01, arrow_12, arrow_20]:
            self.play(arr.animate.set_opacity(1.0), run_time=0.2)
        self.next_slide()

        # scalar values on edges
        def edge_label(text, arrow, color=WHITE, nudge_scale=0.35):
            mid = arrow.get_center()
            outward = mid - center
            outward = outward / (np.linalg.norm(outward) + 1e-6) * nudge_scale
            return MathTex(text, font_size=26, color=color).move_to(mid + outward)

        lbl_e01 = edge_label(r"+2", arrow_01, color=YELLOW)
        lbl_e12 = edge_label(r"-1", arrow_12, color=YELLOW)
        lbl_e20 = edge_label(r"+3", arrow_20, color=YELLOW)
        edge_labels = VGroup(lbl_e01, lbl_e12, lbl_e20)

        self.play(LaggedStart(*[FadeIn(l) for l in edge_labels], lag_ratio=0.2))
        self.next_slide()

        # numbers fly to center
        face_sum = MathTex(r"2-1+3 = +4", font_size=20, color=YELLOW
                           ).move_to(center)
        self.play(*[lbl.animate.move_to(center) for lbl in edge_labels],
                  run_time=0.9)
        self.remove(*edge_labels)
        self.add(face_sum)
        self.next_slide()

        scalar_formula = MathTex(
            r"d\alpha(\sigma) \;=\; \sum_{i=0}^{2} (-1)^i\, \alpha(\sigma_i)",
            font_size=22,
        ).next_to(text_b1, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.0)
        self.play(FadeIn(scalar_formula))
        self.next_slide()

        # =====================================================================
        # BEAT 2 — add fiber squares over vertices
        # =====================================================================
        text_b2 = Tex(
            r"Now $\alpha$ is \textit{vector-valued}: "
            r"values live in fibers $E_{v_i}$ over each vertex.",
            font_size=22,
        ).next_to(scalar_formula, DOWN, aligned_edge=LEFT, buff=0.25
                  ).set_max_width(5.0)
        self.play(FadeIn(text_b2))
        self.play(FadeOut(face_sum))

        # fiber squares: offset outward from triangle center
        def fiber_sq(vertex_pos, color="#FFD166", size=0.30, opacity=0.75):
            outward = vertex_pos - center
            outward = outward / np.linalg.norm(outward) * 0.45
            return Square(
                side_length=size,
                fill_color=color, fill_opacity=opacity,
                stroke_color=WHITE, stroke_width=1.5,
            ).move_to(vertex_pos)

        fsq0 = fiber_sq(v0)
        fsq1 = fiber_sq(v1)
        fsq2 = fiber_sq(v2)
        fibers = VGroup(fsq0, fsq1, fsq2)
        self.play(LaggedStart(*[FadeIn(f) for f in fibers], lag_ratio=0.2))
        self.next_slide()

        # vector labels on edges
        def vec_label(text, arrow, color=WHITE, nudge_scale=0.38, font_size=20):
            mid = arrow.get_center()
            outward = mid - center
            outward = outward / (np.linalg.norm(outward) + 1e-6) * nudge_scale
            return MathTex(text, font_size=font_size, color=color
                           ).move_to(mid + outward)

        vlbl_01 = vec_label(r"\alpha(\sigma_2)", arrow_01, color=ORANGE)
        vlbl_12 = vec_label(r"\alpha(\sigma_0)", arrow_12, color=GREEN)
        vlbl_20 = vec_label(r"\alpha(\sigma_1)", arrow_20, color=TEAL)
        self.play(LaggedStart(
            *[FadeIn(l) for l in [vlbl_01, vlbl_12, vlbl_20]], lag_ratio=0.2
        ))
        self.next_slide()

        # =====================================================================
        # BEAT 3 — problem: different fibers
        # =====================================================================
        text_b3 = Tex(
            r"\textcolor{red}{Problem:} these vectors live in "
            r"\textit{different} fibers — cannot sum directly.",
            font_size=22,
        ).next_to(text_b2, DOWN, aligned_edge=LEFT, buff=0.25).set_max_width(5.0)
        self.play(FadeIn(text_b3))

        fsq1_bad = fiber_sq(v1, color=RED, opacity=0.55)
        fsq2_bad = fiber_sq(v2, color=RED, opacity=0.55)
        self.play(FadeIn(fsq1_bad), FadeIn(fsq2_bad))
        self.next_slide()
        self.play(FadeOut(fsq1_bad), FadeOut(fsq2_bad))

        # =====================================================================
        # BEAT 4 — fix: transport arcs, then merge into fsq0
        # =====================================================================
        text_b4 = Tex(
            r"\textcolor{yellow}{Fix:} transport everything to $E_{v_0}$ "
            r"via $\mathcal{R}_{ij}$, then sum.",
            font_size=22,
        ).next_to(text_b3, DOWN, aligned_edge=LEFT, buff=0.25).set_max_width(5.0)
        self.play(FadeIn(text_b4))
        self.next_slide()

        

        self.remove(vlbl_01)
        self.next_slide()

        # =====================================================================
        # BEAT 5 — formulas on left, triangle stays on right
        # =====================================================================
        self.play(
            FadeOut(text_b1), FadeOut(text_b2),
            FadeOut(text_b3), FadeOut(text_b4),
            FadeOut(scalar_formula),
            FadeOut(vlbl_12), FadeOut(vlbl_20),
        )
        self.next_slide()

        # ── α formula on left ─────────────────────────────────────────────────
        text_alpha_intro = Tex(
            r"For a bundle-valued $\ell$-form $\alpha$:",
            font_size=22,
        ).next_to(title_text, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(text_alpha_intro))

        formula_alpha = MathTex(
            r"\mathfrak{d}^\nabla\alpha(\sigma, v_0) =",
            r"\textcolor{orange}{\mathcal{R}_{01}\,\alpha(\sigma_0, v_1)}",
            r"+ \sum_{i=1}^{\ell+1} (-1)^i\,\alpha(\sigma_i, v_0)",
            font_size=26,
        ).next_to(text_alpha_intro, 1.5 * DOWN, aligned_edge=LEFT, buff=0.25
                  ).set_max_width(5.8)

        box_t = SurroundingRectangle(formula_alpha[1], color=ORANGE, buff=0.07)
        box_s = SurroundingRectangle(formula_alpha[2], color=WHITE,  buff=0.07)
        note_t = Tex(r"transport to $v_0$", font_size=17, color=ORANGE
                     ).next_to(box_t, DOWN, buff=0.10)
        note_s = Tex(r"scalar-DEC sum", font_size=17, color=GRAY
                     ).next_to(box_s, DOWN, buff=0.10)

        self.play(FadeIn(formula_alpha))
        self.next_slide()
        self.play(Create(box_t), FadeIn(note_t))
        self.next_slide()
        self.play(Create(box_s), FadeIn(note_s))
        self.next_slide()

        # ── β formula below ───────────────────────────────────────────────────
        text_beta_intro = Tex(
            r"For an endomorphism-valued $\ell$-form $\beta$ "
            r"($\mathcal{R}_{ij}$ on both sides):",
            font_size=26,
        ).next_to(formula_alpha, 4 * DOWN, aligned_edge=LEFT, buff=0.45).set_max_width(5.8)
        self.play(FadeIn(text_beta_intro))

        formula_beta = MathTex(
            r"\mathfrak{d}^\nabla\beta(\sigma, v_0, v_{\ell+1}) =",
            r"\textcolor{orange}{\mathcal{R}_{01}\,\beta(\sigma_0, v_1, v_{\ell+1})}",
            r"+ \sum_{i=1}^{\ell} (-1)^i\,\beta(\sigma_i, v_0, v_{\ell+1})",
            r"\textcolor{orange}{+ (-1)^{\ell+1}\,\beta(\sigma_{\ell+1}, v_0, v_\ell)\,\mathcal{R}_{\ell,\ell+1}}",
            font_size=26,
        ).next_to(text_beta_intro, DOWN, aligned_edge=LEFT, buff=0.2
                  ).set_max_width(5.8)

        box_bt1 = SurroundingRectangle(formula_beta[1], color=ORANGE, buff=0.06)
        box_bt2 = SurroundingRectangle(formula_beta[3], color=ORANGE, buff=0.06)

        self.play(FadeIn(formula_beta))
        self.next_slide()
        self.play(Create(box_bt1), Create(box_bt2))
        self.next_slide()

        caption = Tex(
            r"Same combinatorics as scalar DEC — "
            r"transport terms to a common fiber.",
            font_size=21, color=YELLOW,
        ).next_to(formula_beta, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.8)
        self.play(FadeIn(caption))
        self.next_slide()

        # =====================================================================
        # BEAT 6 — Bianchi + hook
        # =====================================================================
        self.play(
            FadeOut(text_alpha_intro), FadeOut(formula_alpha),
            FadeOut(box_t), FadeOut(note_t),
            FadeOut(box_s), FadeOut(note_s),
            FadeOut(text_beta_intro), FadeOut(formula_beta),
            FadeOut(box_bt1), FadeOut(box_bt2),
            FadeOut(caption),
            FadeOut(tri),
            FadeOut(dot0), FadeOut(dot1), FadeOut(dot2),
            FadeOut(lbl0), FadeOut(lbl1), FadeOut(lbl2),
            FadeOut(boundary_arrows), FadeOut(fibers),
        )
        self.next_slide()

        bianchi_intro = Tex(
            r"The \textit{differential Bianchi identity} holds "
            r"\textbf{exactly} at the discrete level:",
            font_size=24,
        ).next_to(title_text, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(bianchi_intro))

        bianchi = MathTex(
            r"\mathfrak{d}^\nabla \Omega^\nabla \;=\; 0",
            font_size=54,
        ).move_to(ORIGIN + DOWN * 0.2)
        bianchi_box = SurroundingRectangle(bianchi, color=YELLOW, buff=0.3)

        self.play(Write(bianchi, run_time=1.5))
        self.play(Create(bianchi_box))
        self.next_slide()

        self.play(
            FadeOut(bianchi_intro),
            bianchi.animate.shift(UP * 0.5).scale(0.85),
            bianchi_box.animate.shift(UP * 0.5).scale(0.85),
        )

        done_text = Tex(r"Are we done?", font_size=40).move_to(DOWN * 0.5)
        not_quite = Tex(r"Not quite\ldots", font_size=40, color=RED
                        ).next_to(done_text, DOWN, buff=0.4)

        self.play(FadeIn(done_text))
        self.next_slide()
        self.play(FadeIn(not_quite))
        self.wait()
        self.next_slide()
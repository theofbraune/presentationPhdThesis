from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np
from utils.videoLoop import play_video_loop


class slideControllingTorsionCurvature(Slide):
    def construct(self):

        title = Tex(
            r"Controlling Discrete Torsion and Curvature",
            font_size=30,
        ).to_corner(UL)
        self.add(title)
        self.wait(1)
        self.next_slide()

        # =====================================================================
        # BEAT 1 — Hodge decomposition controls the connection
        # =====================================================================
        textHodge = Tex(
            r"Suppose we search for a connection with $\text{target torsion} = \alpha$",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textHodge))
        self.next_slide()

        hodge_formula = Tex(
            r"Apply Hodge-Decomposition $\alpha \;=\; df + \delta g +h$ ",
            font_size=24,
        ).next_to(textHodge, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(hodge_formula))
        self.next_slide()

        textCurvControls = Tex(
            r"Most applications in graphics only control curvature. $\rightarrow$  Only fix the $\delta$ and \textit{harmonic} part -- $d$ part is left free.",
            font_size=24,
        ).next_to(hodge_formula, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textCurvControls))
        self.next_slide()

        # self.play(
        #     FadeOut(textHodge),
        #     FadeOut(hodge_formula),
        #     FadeOut(textCurvControls),
        # )
        # self.next_slide()
        textExample = Tex(r"Example: Trivial Connections [Crane et al. 2010] with Torsion Control", font_size = 24).next_to(textCurvControls, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textExample))
        self.next_slide()

        """
        # =====================================================================
        # BEAT 2 — local parallel transport: annotated last frame
        # show the Houdini frame with vectors being advected locally,
        # then fade in the annotated version with the dual loop
        # =====================================================================
        textAdvect = Tex(
            r"Parallel transport moves vectors along edges "
            r"via the connection $\alpha$.",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textAdvect))
        self.next_slide()

        # --- Houdini video: local advection of a few triangles ---
        # PLACEHOLDER: replace with your actual frame directory
        local_video = play_video_loop(
            self,
            frame_dir="figures/renderAdvectionLocal/",
            position=RIGHT * 1.5 + DOWN * 0.5,
            height=3.5,
            fps=20,
            fade_in_time=0.5,
            fade_out_time=0.0,
            persist=True,
        )
        self.next_slide()

        # fade out video, fade in annotated last frame
        annotated_frame = ImageMobject("figures/advection_annotated.png")
        annotated_frame.height = 3.5
        annotated_frame.move_to(RIGHT * 1.5 + DOWN * 0.5)
        self.play(FadeOut(local_video), FadeIn(annotated_frame))

        textAngleDefect = Tex(
            r"The curvature $\Omega^\nabla$ around a dual loop "
            r"= the \textit{angle defect} at the enclosed vertex.",
            font_size=24,
        ).next_to(textAdvect, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textAngleDefect))
        self.next_slide()

        self.play(FadeOut(annotated_frame), FadeOut(textAngleDefect))
        self.next_slide()

        # =====================================================================
        # BEAT 3 — trivial connection: curvature at cone singularities only
        # =====================================================================
        textTrivial = Tex(
            r"A \textit{trivial connection} concentrates curvature "
            r"at prescribed singularities — parallel transport is "
            r"path-independent everywhere else.",
            font_size=24,
        ).next_to(textAdvect, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textTrivial))
        self.next_slide()

        textGlobal = Tex(
            r"$\Rightarrow$ If singularities are chosen consistently, "
            r"we obtain a \textit{globally consistent} vector field.",
            font_size=24, color=YELLOW,
        ).next_to(textTrivial, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textGlobal))
        self.next_slide()

        self.play(FadeOut(textTrivial), FadeOut(textGlobal), FadeOut(textAdvect))
        self.next_slide()

        # =====================================================================
        # BEAT 4 — global field animation (zooms out from local to full mesh)
        # =====================================================================
        textGlobalAnim = Tex(
            r"Trivial connection $\Rightarrow$ globally consistent direction field:",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textGlobalAnim))

        # --- Houdini video: zoom out to show full parallel-transported field ---
        # PLACEHOLDER: replace with your actual frame directory
        global_video = play_video_loop(
            self,
            frame_dir="figures/renderAdvectionGlobal/",
            position=RIGHT * 1.0 + DOWN * 0.8,
            height=4.0,
            fps=20,
            fade_in_time=0.5,
            fade_out_time=0.5,
            persist=True,
        )
        self.next_slide()

        self.play(FadeOut(global_video), FadeOut(textGlobalAnim))
        self.next_slide()

        # =====================================================================
        # BEAT 5 — adding a torsion potential d𝜙
        # =====================================================================
        textTorsionFree = Tex(
            r"The trivial connection has zero torsion gradient: $d\phi = 0$.",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textTorsionFree))
        self.next_slide()

        textAddPhi = Tex(
            r"Adding $d\phi$ to the connection does \textit{not} change curvature "
            r"(since $d(d\phi) = 0$), but twists the field.",
            font_size=24,
        ).next_to(textTorsionFree, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textAddPhi))

        dphi_formula = MathTex(
            r"\alpha \;\mapsto\; \alpha + d\phi "
            r"\quad\Rightarrow\quad "
            r"\Omega^\nabla \text{ unchanged},\quad "
            r"\Theta^\nabla \text{ changes}",
            font_size=26,
        ).next_to(textAddPhi, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(dphi_formula))
        self.next_slide()

        self.play(
            FadeOut(textTorsionFree),
            FadeOut(textAddPhi),
            FadeOut(dphi_formula),
        )
        self.next_slide()

        # =====================================================================
        # BEAT 6 — side-by-side comparison: zero torsion vs prescribed torsion
        # =====================================================================
        textCompare = Tex(
            r"Effect of adding a torsion potential $\phi$:",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textCompare))

        # left: minimal torsion field
        img_minimal = ImageMobject("figures/torsion_minimal.png")
        img_minimal.height = 3.0
        img_minimal.shift(LEFT * 3.0 + DOWN * 1.0)

        label_minimal = Tex(
            r"$d\phi = 0$\\minimal torsion",
            font_size=20, color=GRAY,
        ).next_to(img_minimal, DOWN, buff=0.15)

        # right: prescribed torsion field
        img_prescribed = ImageMobject("figures/torsion_prescribed.png")
        img_prescribed.height = 3.0
        img_prescribed.shift(RIGHT * 1.5 + DOWN * 1.0)

        label_prescribed = Tex(
            r"$d\phi \neq 0$\\prescribed torsion",
            font_size=20, color=YELLOW,
        ).next_to(img_prescribed, DOWN, buff=0.15)

        self.play(FadeIn(img_minimal), FadeIn(label_minimal))
        self.next_slide()
        self.play(FadeIn(img_prescribed), FadeIn(label_prescribed))
        self.next_slide()

        # =====================================================================
        # BEAT 7 — further applications
        # =====================================================================
        self.play(
            FadeOut(img_minimal), FadeOut(label_minimal),
            FadeOut(img_prescribed), FadeOut(label_prescribed),
            FadeOut(textCompare),
        )
        self.next_slide()

        textApps = Tex(
            r"Same framework applies to:",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textApps))

        BULLET_X = -5.8
        START_Y  =  1.0
        SPACING  =  1.1

        def bullet(text, y, font_size=23):
            dot  = Tex(r"$\bullet$", font_size=font_size
                       ).move_to(np.array([BULLET_X + 0.1, y, 0]))
            body = Tex(text, font_size=font_size
                       ).next_to(dot, RIGHT, buff=0.25).align_to(dot, UP)
            return VGroup(dot, body)

        b1 = bullet(
            r"Stripe patterns — torsion controls stripe twist",
            START_Y,
        )
        b2 = bullet(
            r"Vector heat method / connection Laplacian — "
            r"torsion introduces a twist into logarithmic maps",
            START_Y - SPACING,
        )
        b3 = bullet(
            r"$N$-vector field design — full independent control "
            r"of curvature and torsion",
            START_Y - 2 * SPACING,
        )

        for b in [b1, b2, b3]:
            self.play(FadeIn(b))
            self.next_slide()

        self.wait(1)
        self.next_slide()
        """
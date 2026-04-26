# from email.mime import image
# from manim import *
# from manim_slides import Slide
# import utils.preamble as preamble
# import numpy as np
# from utils.videoLoop import play_video_loop


# class slideControllingTorsionCurvatureCont2(Slide):
#     def construct(self):

#         title = Tex(
#             r"Controlling Discrete Torsion and Curvature",
#             font_size=30,
#         ).to_corner(UL)
#         self.add(title)
        

#         # =====================================================================
#         # BEAT 1 — Hodge decomposition controls the connection
#         # =====================================================================
#         textHodge = Tex(
#             r"Suppose we search for a connection with $\text{target torsion} = \alpha$",
#             font_size=24,
#         ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
#         self.add(textHodge)
#         hodge_formula = Tex(
#             r"Apply Hodge-Decomposition:\quad $\alpha \;=\; df + \delta g +h$ ",
#             font_size=24,
#         ).next_to(textHodge, DOWN, aligned_edge=LEFT, buff=0.3)
#         self.add(hodge_formula)

#         textCurvControls = Tex(
#             r"Most applications in graphics only control curvature. $\rightarrow$  Only fix the $\delta$ and \textit{harmonic} part -- $d$ part is left free.",
#             font_size=24,
#         ).next_to(hodge_formula, DOWN, aligned_edge=LEFT, buff=0.3)
#         self.add(textCurvControls)

#         # self.play(
#         #     FadeOut(textHodge),
#         #     FadeOut(hodge_formula),
#         #     FadeOut(textCurvControls),
#         # )
#         # self.next_slide()
#         self.add(textExample)
#         # include the picture of the spot with sing 
#         textGloballyOptimalField = Tex(r"Example: Connection Laplacian with Torsion Control", font_size = 24).next_to(textCurvControls, DOWN, aligned_edge=LEFT, buff=0.3)
#         self.play(Transform(textExample, textGloballyOptimalField))
#         self.wait()
#         self.next_slide()
#         imageDilo = ImageMobject("figures/globallyOptFieldLC.png").next_to(textGloballyOptimalField, DOWN, aligned_edge=LEFT, buff=0.3)
#         imageDilo.height = 3.0
#         textGlobally = Tex(r"Globally Optimal Fields [Knöppel et al. 2015]", font_size = 20, color=YELLOW).next_to(imageDilo, DOWN, aligned_edge=LEFT, buff=0.15)
#         self.play(FadeIn(imageDilo), FadeIn(textGlobally))
#         imageAddedTorsion = ImageMobject("figures/globallyOptFieldTorsion.png").next_to(imageDilo, RIGHT, aligned_edge=UP, buff=0.5)
#         imageAddedTorsion.height = 3.0
#         textAddedTorsion = Tex(r"Added Exact Torsion Component", font_size = 20, color=YELLOW).next_to(imageAddedTorsion, DOWN, aligned_edge=LEFT, buff=0.15)
#         self.play(FadeIn(imageAddedTorsion), FadeIn(textAddedTorsion))
#         self.next_slide()
from manim import *
from manim_slides import Slide
import utils.preamble as preamble
import numpy as np
from utils.videoLoop import play_video_loop


class slideControllingTorsionCurvatureCont2(Slide):
    def construct(self):

        title = Tex(
            r"Controlling Discrete Torsion and Curvature",
            font_size=30,
        ).to_corner(UL)
        self.add(title)
        # self.play(FadeIn(title))
        # self.next_slide()

        # =====================================================================
        # BEAT 1 — Hodge decomposition
        # =====================================================================
        textHodge = Tex(
            r"Suppose we search for a connection with "
            r"$\text{target torsion} = \alpha$",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        # self.play(FadeIn(textHodge))
        # self.next_slide()
        self.add(textHodge)

        hodge_formula = Tex(
            r"Apply Hodge decomposition: "
            r"$\quad \alpha \;=\; df + \delta g + h$",
            font_size=24,
        ).next_to(textHodge, DOWN, aligned_edge=LEFT, buff=0.3)
        self.add(hodge_formula)

        textCurvControls = Tex(
            r"Most applications in graphics only control curvature. "
            r"$\rightarrow$ Only fix the $\delta$ and harmonic part "
            r"--- $d$ part is left free.",
            font_size=24,
        ).next_to(hodge_formula, DOWN, aligned_edge=LEFT, buff=0.3)
        self.add(textCurvControls)

        # =====================================================================
        # BEAT 2 — example title
        # =====================================================================
        textExample = Tex(r"Example: Trivial Connections [Crane et al. 2010] with Torsion Control", font_size = 24).next_to(textCurvControls, DOWN, aligned_edge=LEFT, buff=0.3)
        self.add(textExample)
        textExample2 = Tex(
            r"Example: Connection Laplacian with Torsion Control",
            font_size=24,
        ).next_to(textCurvControls, DOWN, aligned_edge=LEFT, buff=0.3)
        self.wait()
        self.play(Transform(textExample, textExample2))
        self.next_slide()

        # =====================================================================
        # BEAT 3 — left image: LC field
        # =====================================================================
        imageDilo = ImageMobject("figures/globallyOptFieldLC.png")
        imageDilo.height = 2.0
        imageDilo.next_to(textExample, DOWN, aligned_edge=LEFT, buff=0.3)

        textGlobally = Tex(
            r"Globally Optimal Fields [Knöppel et al. 2015]",
            font_size=20, color=YELLOW,
        ).next_to(imageDilo, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(FadeIn(imageDilo), FadeIn(textGlobally))
        self.next_slide()

        # =====================================================================
        # BEAT 4 — right image: with added torsion
        # =====================================================================
        imageAddedTorsion = ImageMobject("figures/globallyOptFieldTorsion.png")
        imageAddedTorsion.height = 2.0
        imageAddedTorsion.next_to(imageDilo, RIGHT, aligned_edge=UP, buff=0.5)

        textAddedTorsion = Tex(
            r"Added Exact Torsion Component",
            font_size=20, color=YELLOW,
        ).next_to(imageAddedTorsion, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(FadeIn(imageAddedTorsion), FadeIn(textAddedTorsion))
        self.next_slide()

        # =====================================================================
        # CLEAR
        # =====================================================================
        self.play(
            
            FadeOut(imageDilo), 
            FadeOut(imageAddedTorsion), FadeOut(textAddedTorsion),
            FadeOut(textGlobally)
        )
        self.next_slide()
        imgBunny = ImageMobject("figures/bunnyFigTriple.png")
        imgBunny.height = 3.0
        imgBunny.next_to(textExample, DOWN, aligned_edge=LEFT, buff=0.3)
        self.add(imgBunny)
        textLap = Tex(r"Log map via Torsion free Connection Laplacian [Sharp et al. 2019] vs with added Exact Torsion", font_size=20, color=YELLOW).next_to(imgBunny, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textLap))
        self.next_slide()

        self.remove(*self.mobjects)
        textTitle = Tex(r"Conclusion", font_size=30).to_corner(UL)
        self.add(textTitle)
        textConclusion = Tex(r"$\bullet$Elegant structure preserving discretization of torsion of connections on surfaces", font_size=24).next_to(textTitle, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textConclusion))
        self.next_slide()
        textNext = Tex(r"$\bullet$Enriches the design space for methods that control curvature in geometry processing ",font_size=24).next_to(textConclusion, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textNext))
        self.next_slide()
        textHowever = Tex(r"$\bullet$However, heavily dependent on the fact that we consider the torsion form on the tangent bundle of a surface  ", font_size=24).next_to(textNext, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textHowever))
        self.next_slide()
        textNoGeneralization = Tex(r"$\bullet$How can we generalize the structure preserving discretization of arbitrary bundle valued forms on arbitrary manifolds?", font_size=24).next_to(textHowever, 2* DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(FadeIn(textNoGeneralization))
        self.next_slide()
        # videoDistorted = play_video_loop(
        #     self,
        #     frame_dir="figures/render_cow_torsion/croppedOut/",




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
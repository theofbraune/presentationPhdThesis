from manim import *
from manim_slides import Slide
import utils.preamble as preamble


class slide7(Slide):
    # historical context + applications + the gap
    def construct(self):
        title_text = Tex(
            "Discrete Exterior Calculus", font_size=30
        ).to_corner(UL)
        self.play(FadeIn(title_text))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 1 — CARTAN. Plant the seed: original theory was rich.
        # =====================================================================
        cartan_img = ImageMobject("figures/Elie_Cartan.jpg").scale(0.7)
        cartan_img.to_edge(RIGHT).shift(UP * 0.3)

        cartan_text = Tex(
            r"\textbf{Élie Cartan, 1920s:} differential forms, vector bundles, "
            r"connections, curvature.",
            font_size=24,
        ).next_to(title_text, 2 * DOWN, aligned_edge=LEFT)
        # cartan_text.set_width(7)  # keep it on the left so the photo has room

        self.play(FadeIn(cartan_text), FadeIn(cartan_img))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 2 — HIRANI ET AL. Note the deliberate phrasing.
        # =====================================================================
        hirani_text = Tex(
            r"\textbf{Hirani, Marsden, Desbrun, Stern, Leok (2003):} "
            r"a discrete calculus for the \textit{scalar} part of this theory.",
            font_size=24,
        ).next_to(cartan_text, 2 * DOWN, aligned_edge=LEFT)
        # hirani_text.set_width(7)

        self.play(FadeIn(hirani_text))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 3 — APPLICATIONS, 2x2 GRID
        # Four applications, each with a citation underneath.
        # The grid sits in the lower portion of the slide.
        # =====================================================================
        # Cartan slides off to make room for the gallery
        # self.play(
            # cartan_img.animate.scale(0.5).to_corner(UR).shift(DOWN * 0.5),
        # )

        gallery_text = Tex(
            r"Today, DEC is ubiquitous in geometry processing and simulation:",
            font_size=22,
        ).next_to(hirani_text, 2 * DOWN, aligned_edge=LEFT)
        self.play(FadeIn(gallery_text))
        self.wait()

        
        # Build the 2x2 grid programmatically
        figs_info = [
            ("figures/decApplications/fluidSim.png",                "[Nabizadeh et al. 2022]"),
            ("figures/decApplications/discrete_electromagnetics.png","[Stern et al. 2007]"),
            ("figures/decApplications/trivial_connections.png",     "[Crane et al. 2010]"),
            ("figures/decApplications/hodgeDecomp.png",              "[Zhao et al. 2021]"),
        ]

        IMG_HEIGHT = 1.4
        H_GAP = 0.6
        V_GAP = 0.5

        gallery_items = []  # list of Group(image, caption) so we can position together
        for path, citation in figs_info:
            img = ImageMobject(path)
            img.height = IMG_HEIGHT
            cap = Tex(citation, font_size=16).next_to(img, DOWN, buff=0.1)
            gallery_items.append((img, cap))

        # Lay out in 2x2: top row, bottom row
        # Reference position: under gallery_text, slightly left of center
        anchor = gallery_text.get_corner(DL) + DOWN * 0.6 + RIGHT * 1.0

        # top-left, top-right, bottom-left, bottom-right
        positions = [
            anchor + RIGHT * 0,
            anchor + RIGHT * (IMG_HEIGHT * 1.6 + H_GAP),
            anchor + DOWN  * (IMG_HEIGHT + V_GAP) + RIGHT * 0,
            anchor + DOWN  * (IMG_HEIGHT + V_GAP) + RIGHT * (IMG_HEIGHT * 1.6 + H_GAP),
        ]

        for (img, cap), pos in zip(gallery_items, positions):
            img.move_to(pos, aligned_edge=UL)
            cap.next_to(img, DOWN, buff=0.1)

        # Reveal the four figures one by one
        for img, cap in gallery_items:
            self.play(FadeIn(img), FadeIn(cap), run_time=0.5)
            self.next_slide()

        
        # =====================================================================
        # BEAT 4 — THE PIVOT. The punchline of the slide.
        # =====================================================================
        # Bring Cartan back to visual prominence
        self.play(cartan_img.animate.scale(1.4).to_edge(RIGHT).shift(DOWN * 0.5))

        # Fade the gallery to half opacity so the punchline stands out
        for img, cap in gallery_items:
            self.play(
                img.animate.set_opacity(0.05),
                cap.animate.set_opacity(0.05),
                run_time=0.15,
            )

        self.play(FadeOut(gallery_text))
        # The gap statement, in the same area as the original Cartan beat
        gap_text = Tex(
            r"But Cartan also developed a \textit{bundle-valued} exterior calculus.",
            font_size=26,
            color=YELLOW,
        ).next_to(hirani_text, 2 * DOWN, aligned_edge=LEFT)
        # gap_text.set_width(8)

        gap_text2 = Tex(
            r"It is \textbf{still missing} from DEC.",
            font_size=28,
            color=YELLOW,
        ).next_to(gap_text, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(gap_text))
        self.wait()
        self.next_slide()
        self.play(FadeIn(gap_text2))
        self.wait()
        self.next_slide()
        
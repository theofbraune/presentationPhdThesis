from manim import *
from manim_slides import Slide
import utils.preamble as preamble


class slide6(Slide):
    # discrete exterior derivative + Stokes
    def construct(self):

        # =====================================================================
        # TITLE + QUESTION
        # =====================================================================
        title_text = Tex(
            "Exterior Derivative and Stokes' Theorem", font_size=30
        ).to_corner(UL)
        self.add(title_text)
        self.wait()
        self.next_slide()

        text_question = Tex(
            r"How do we extend $d$ to discrete forms?",
            font_size=25,
        ).next_to(title_text, 2 * DOWN, aligned_edge=LEFT)
        self.play(FadeIn(text_question))
        self.wait()
        self.next_slide()

        # =====================================================================
        # STOKES AS THE DEFINING PROPERTY
        # Instead of writing out the coordinate formula for d, we lead with
        # Stokes — d is the operator that makes this hold.
        # =====================================================================
        stokes_def = MathTex(
            r"\int_{\partial c}\alpha \;=\; \int_{c} d\alpha",
            font_size=42,
        ).move_to(ORIGIN + UP * 0.5)

        stokes_caption = Tex(
            r"This is the \textit{defining property} of $d$.",
            font_size=24,
        ).next_to(stokes_def, DOWN, buff=0.5)

        self.play(FadeIn(stokes_def))
        self.wait(0.4)
        self.play(FadeIn(stokes_caption))
        self.wait()
        self.next_slide()

        # Move Stokes up to the top-left so it stays visible as a reference
        stokes_def_small = MathTex(
            r"\int_{\partial c}\alpha = \int_{c} d\alpha",
            font_size=26,
        ).next_to(text_question, 1.5 * DOWN, aligned_edge=LEFT)
        self.play(
            FadeOut(stokes_caption),
            Transform(stokes_def, stokes_def_small),
        )
        self.wait()
        self.next_slide()

        # =====================================================================
        # MESH GEOMETRY (your existing setup, unchanged)
        # =====================================================================
        p0 = [-0.2, -0.9, 0.]
        p1 = [0.35, -0.4, 0.]
        p2 = [0.5, 0.25, 0.]
        p3 = [0.0, 0.75, 0.]
        p4 = [-0.65, 0.25, 0.]

        p5 = [-1.5, -1.5, 0.]
        p6 = [-0.5, -1.5, 0.]
        p7 = [0.5, -1.5, 0.]
        p8 = [1.5, -1.5, 0.]

        p9 = [1.5, -0.5, 0.]
        p10 = [1.5, 0.5, 0.]
        p11 = [1.5, 1.5, 0.]

        p12 = [0.5, 1.5, 0.]
        p13 = [-0.5, 1.5, 0.]
        p14 = [-1.5, 1.5, 0.]
        p15 = [-1.5, 0.5, 0.]
        p16 = [-1.5, -0.5, 0.]

        points = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

        f0 = [0, 1, 2, 3, 4]
        f1 = [0, 6, 7, 9]
        f2 = [7, 8, 9]
        f3 = [0, 9, 1]
        f4 = [2, 1, 9, 10]
        f5 = [2, 10, 11, 12]
        f6 = [3, 2, 12, 13]
        f7 = [3, 13, 14, 15, 4]
        f8 = [15, 16, 4]
        f9 = [16, 0, 4]
        f10 = [5, 6, 0, 16]
        faces = [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10]

        polygons = VGroup()
        faces_for_cell = []
        for j, face_indices in enumerate(faces):
            polygon_points = [points[i] for i in face_indices]
            polygon = Polygon(*polygon_points, color=BLUE, fill_opacity=0.1)
            polygons.add(polygon)
            if j == 0 or j == 9:
                faces_for_cell.append(polygon)

        # boundary arrows of f0 (the central pentagon)
        fleche0 = Arrow(p0, p1, buff=0.6, color=RED, tip_length=0.1).shift([0, 0.1, 0]).set_opacity(0.).scale(0.8)
        fleche1 = Arrow(p1, p2, buff=0.6, color=RED, tip_length=0.1).shift([-0.1, 0., 0]).set_opacity(0.).scale(0.8)
        fleche2 = Arrow(p2, p3, buff=0.6, color=RED, tip_length=0.1).shift([0, -0.1, 0]).set_opacity(0.).scale(0.8)
        fleche3 = Arrow(p3, p4, buff=0.6, color=RED, tip_length=0.1).shift([0, -0.1, 0]).set_opacity(0.).scale(0.8)
        fleche4 = Arrow(p4, p0, color=RED, tip_length=0.1).shift([0.1, 0.0, 0]).set_opacity(0.)
        polygons.add(fleche0, fleche1, fleche2, fleche3, fleche4)
        face1 = [fleche0, fleche1, fleche2, fleche3, fleche4]

        # boundary arrows of f9 (the adjacent triangle)
        fleche5 = Arrow(p16, p0, color=RED, tip_length=0.1).shift([0, 0.1, 0]).set_opacity(0.)
        fleche6 = Arrow(p0, p4, color=RED, tip_length=0.1).shift([-0.1, 0., 0]).set_opacity(0.)
        fleche7 = Arrow(p4, p16, color=RED, tip_length=0.1).shift([0, -0.1, 0]).set_opacity(0.)
        polygons.add(fleche5, fleche6, fleche7)
        face2 = [fleche5, fleche6, fleche7]

        shared_edges = [fleche4, fleche6]

        polygons.scale(2)
        polygons.to_edge(RIGHT)

        self.play(FadeIn(polygons))
        self.wait()
        self.next_slide()

        # =====================================================================
        # ANIMATION 1 — DISCRETE d ON A SINGLE FACE
        # Boundary edges carry numbers; they collapse into a single number
        # on the face. This is the slide5 animation, one dimension up.
        # =====================================================================
        # Highlight the central face only
        central_face = faces_for_cell[0]
        self.play(central_face.animate.set_fill(BLUE, opacity=0.3))

        # Reveal the boundary arrows of the central face
        for fleche in face1:
            self.play(fleche.animate.set_opacity(1.0), run_time=0.15)

        # Number labels on each boundary edge — placeholder values
        edge_values = ["+2", "-1", "+3", "0", "-1"]
        edge_arrows = face1
        edge_labels = VGroup()
        for arrow, val in zip(edge_arrows, edge_values):
            mid = arrow.get_center()
            label = MathTex(val, font_size=24).move_to(mid)
            # nudge slightly outward from the face center
            face_center = central_face.get_center()
            outward = (mid - face_center)
            outward = outward / (np.linalg.norm(outward) + 1e-6) * 0.4
            label.shift(outward)
            edge_labels.add(label)

        self.play(FadeIn(edge_labels))
        self.wait(0.3)
        self.next_slide()

        # The signed sum: collapse all labels into a single number on the face
        face_value = MathTex(r"+3", font_size=32).move_to(central_face.get_center())

        self.play(
            *[Transform(lbl, face_value.copy()) for lbl in edge_labels],
            run_time=0.9,
        )
        self.remove(*edge_labels)
        self.add(face_value)
        self.wait(0.3)
        self.next_slide()

        # =====================================================================
        # BULLET 1 — recap as a formula
        # =====================================================================
        bullet_d = MathTex(
            r"\langle d\alpha,\, c\rangle \;=\; \sum_{c'\in\partial c} \mathrm{sgn}(c')\, \langle\alpha,\, c'\rangle",
            font_size=28,
        ).next_to(stokes_def, 2 * DOWN, aligned_edge=LEFT)

        bullet_d_text = Tex(
            r"\textbf{Discrete } $d$\textbf{:} signed sum on the boundary.",
            font_size=24,
        ).next_to(bullet_d, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(bullet_d))
        self.wait(0.3)
        self.play(FadeIn(bullet_d_text))
        self.wait()
        self.next_slide()

        # =====================================================================
        # ANIMATION 2 — GLUE THE SECOND FACE, SHARED EDGES CANCEL
        # =====================================================================
        # Fade out the face value to make room for the next beat
        self.play(FadeOut(face_value))

        # Highlight the second face and reveal its boundary
        second_face = faces_for_cell[1]
        self.play(second_face.animate.set_fill(BLUE, opacity=0.3))
        for fleche in face2:
            self.play(fleche.animate.set_opacity(1.0), run_time=0.15)
        self.wait(0.3)
        self.next_slide()

        # Now show the cancellation: the shared edges fade out
        bullet_cancel = Tex(
            r"\textbf{Shared edges cancel} when faces are glued.",
            font_size=24,
        ).next_to(bullet_d_text, 1.5 * DOWN, aligned_edge=LEFT)

        self.play(FadeIn(bullet_cancel))
        self.wait(0.3)
        self.play(*[fleche.animate.set_opacity(0.0) for fleche in shared_edges])
        self.wait()
        self.next_slide()

        # =====================================================================
        # SYNTHESIS — STOKES IS A CONSEQUENCE, NOT AN ASSUMPTION
        # =====================================================================
        bullet_stokes = Tex(
            r"$\Rightarrow$ Stokes' theorem holds \textit{by construction}.",
            font_size=26,
        ).next_to(bullet_cancel, 1.5 * DOWN, aligned_edge=LEFT)

        self.play(FadeIn(bullet_stokes))
        self.wait()
        self.next_slide()

        # =====================================================================
        # CLIMAX — clear the left column, big Stokes formula, headline
        # =====================================================================
        self.play(
            FadeOut(text_question),
            FadeOut(stokes_def),
            FadeOut(bullet_d),
            FadeOut(bullet_d_text),
            FadeOut(bullet_cancel),
            FadeOut(bullet_stokes),
        )

        big_stokes = MathTex(
            r"\int_{\partial U}\alpha \;=\; \int_{U} d\alpha",
            font_size=60,
        ).move_to(LEFT * 3 + UP * 0.5)
        self.play(FadeIn(big_stokes))
        self.wait()
        self.next_slide()

        structurePreserving = Tex(
            r"\textbf{Structure-preserving discretization!}",
            font_size=36,
        ).next_to(big_stokes, DOWN, buff=0.8)
        self.play(FadeIn(structurePreserving))
        self.wait()
        self.next_slide()
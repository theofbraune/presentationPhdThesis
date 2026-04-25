from manim import *
from manim_slides import Slide
import utils.preamble as preamble


class slide5(Slide):
    #differential forms and DEC
    def construct(self):
        title_text = Tex("Differential k-Forms and Discrete Differential Forms",font_size=30).to_corner(UL)
        self.play(FadeIn(title_text))
        self.wait()
        self.next_slide()
        imageGerman = ImageMobject("figures/differentialFormGerman.png").scale(0.7).next_to(title_text,2*DOWN,aligned_edge=LEFT)
        self.play(FadeIn(imageGerman))
        imageComputerGuy = ImageMobject("figures/computer-guy.jpg").scale(0.7).to_edge(RIGHT).shift(DOWN)
        self.play(FadeIn(imageComputerGuy))
        self.wait()
        self.next_slide()
        imageEnglish = ImageMobject("figures/differentialFormEnglish.png").scale(0.7).next_to(title_text,2*DOWN,aligned_edge=LEFT)
        self.play(FadeOut(imageComputerGuy), FadeOut(imageGerman), FadeIn(imageEnglish))
        self.wait()
        self.next_slide()

        imageEnglishCropped = ImageMobject("figures/differentialFormEnglishAnnotated.png").scale(0.7).next_to(title_text,2*DOWN,aligned_edge=LEFT)

        self.play(FadeOut(imageEnglish), FadeIn(imageEnglishCropped))
        self.wait()
        self.next_slide()
        self.play(FadeOut(imageEnglishCropped))
        self.wait()
        self.next_slide()
        description_text = MathTex(r"\bullet \text{ Differential } k\text{-form:  Integrand on a }k\text{-dimensional oriented chain.}", font_size=25).to_edge(LEFT).shift(DOWN)
        description_text.to_corner(UL).shift(DOWN)
        self.wait()
        self.next_slide()
        self.play(FadeIn(description_text))
        # other_interpretation = Tex(" Other interpretation: \" A differential k-form is an object to be integrated over an oriented k-dimensional manifold\" [Crane et al. 2013] ",font_size=25)
        # other_interpretation.next_to(description_text,2*DOWN,aligned_edge=LEFT)
        # self.wait()
        # self.next_slide()
        # self.play(FadeIn(other_interpretation))
        # self.wait()
        # self.next_slide()
        text_discrete = Tex(r"$\bullet$ Advantage: Easily adaptable to discrete manifolds.",font_size=25).next_to(description_text,2*DOWN,aligned_edge=LEFT)
        self.play(FadeIn(text_discrete))
        self.wait()
        self.next_slide()

        
        p0 = [-0.2,-0.9,0.]
        p1 = [0.35,-0.4,0.] 
        p2 = [0.5,0.25,0.]
        p3 = [0.0,0.75,0.]
        p4 = [-0.65,0.25,0.]
        
        p5 = [-1.5,-1.5,0.]
        p6 = [-0.5,-1.5,0.]
        p7 = [0.5,-1.5,0.]
        p8 = [1.5,-1.5,0.]

        p9 = [1.5,-0.5,0.]
        p10 = [1.5,0.5,0.]
        p11 = [1.5,1.5,0.]

        p12 = [0.5,1.5,0.]
        p13 = [-0.5,1.5,0.]
        p14 = [-1.5,1.5,0.]
        p15 = [-1.5,0.5,0.]
        p16 = [-1.5,-0.5,0.]
        
        points = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16]
        # points = [np.resize(np.array(p),[3,1]) for p in points]
        f0 = [0,1,2,3,4]
        f1 = [0,6,7,9]
        f2 = [7,8,9]
        f3 = [0,9,1]
        f4 = [2,1,9,10]
        f5 = [2,10,11,12]
        f6 = [3,2,12,13]
        f7 = [3,13,14,15,4]
        f8 = [15,16,4]
        f9 = [16,0,4]
        f10 = [5,6,0,16]

        # faces = [
        #     [0,1,2], [0,6,7], [7,8,9], [0,9,1], [2,1,9], [2,10,11], [3,2,12], [3,13,14],
        #     [15,16,4], [16,0,4], [5,0,16], [0,2,3], [0,3,4], [0,7,9], [2,9,10], [2,11,12],
        #     [3,12,13], [3,14,15], [3,15,4], [5,0,16]
        # ]
        faces = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]

        # Create polygons for each face
        polygons = VGroup()
        for face_indices in faces:
            polygon_points = [points[i] for i in face_indices]
            polygon = Polygon(*polygon_points, color=BLUE, fill_opacity=0.1)
            polygons.add(polygon)

        fleche0 = Arrow(p4,p3,buff=0.7,color=RED,tip_length=0.1).shift([0,0.1,0]).set_opacity(0.)
        fleche1 = Arrow(p3,p4,buff=0.7,color=RED,tip_length=0.1).shift([0,-0.1,0]).set_opacity(0.)
        polygons.add(fleche0,fleche1)    

        
        polygons.scale(2)
        polygons.to_edge(RIGHT)
        # Add polygons to the scene
        # self.add(polygons)

        self.wait()  # Wait for a moment to display the scene
        self.next_slide()
        # text_discrete_diff_form = Tex(" Given a simplicial complex $\mathcal{C}$, a discrete differential k-form\\\ $\\alpha$ assign to every (oriented) k-simplex a scalar",font_size=25).next_to(text_discrete,2*DOWN,aligned_edge=LEFT)
        self.play(FadeIn(polygons))
        self.wait()
        self.next_slide()
        # textDiscreteForm = Tex(" - Discrete Differential k-form: One scalar per oriented k-simplex. ",font_size=25).next_to(text_discrete,2*DOWN,aligned_edge=LEFT)
        form_1 = MathTex("\\langle \\alpha,e\\rangle = 2").next_to(fleche1.get_center(),0.01*RIGHT+0.1*DOWN).scale(0.5)
        form_2 = MathTex("\\langle \\alpha,-e\\rangle = -2").next_to(fleche0.get_center(),0.01*LEFT+0.1*UP).scale(0.5)
        # ----------------------------------------------------------
        # SMOOTH → DISCRETE: integrate a field along an edge
        # ----------------------------------------------------------
        # Pick the edge we want to discretize (the one fleche1 already
        # highlights). Use its actual endpoints in screen coordinates.
        edge_start = fleche1.get_start()
        edge_end   = fleche1.get_end()
        edge_vec   = edge_end - edge_start
        edge_dir   = edge_vec / np.linalg.norm(edge_vec)

        # Sample points along the edge
        n_samples = 6
        sample_points = [
            edge_start + (i + 0.5) / n_samples * edge_vec
            for i in range(n_samples)
        ]

        # A smooth "field" along the edge — short arrows tangent to it,
        # with varying lengths to suggest a non-constant 1-form being sampled.
        # (Tangent because we're integrating ⟨α, ė⟩; only the tangential
        # component matters.)
        sample_lengths = [0.15, 0.22, 0.28, 0.30, 0.26, 0.15]  # arbitrary profile
        field_arrows = VGroup()
        for p, L in zip(sample_points, sample_lengths):
            a = Arrow(
                p - 0.5 * L * edge_dir,
                p + 0.5 * L * edge_dir,
                buff=0,
                stroke_width=2.5,
                color=GREEN,
                tip_length=0.08,
            )
            field_arrows.add(a)

        # Step 1: show the smooth field as a row of little arrows along the edge
        self.play(FadeIn(field_arrows, run_time=2.5))
        self.wait(0.4)

        # Step 2: show the integral symbol next to the edge briefly
        integral_label = MathTex(
            r"\int_{e} \alpha", font_size=28
        ).next_to(fleche1.get_center(), RIGHT+DOWN, buff=0.15)
        self.play(FadeIn(integral_label))
        self.wait()
        self.next_slide()

        
        # Step 3: collapse the arrows into the single discrete value
        # (we transform them all into the number that will sit on the edge)
        arr = Arrow(edge_start,edge_end,buff=0.7,color=RED,tip_length=0.1)
        arr.scale(2)
        arr.to_edge(RIGHT)
        self.play(
            *[
                Transform(a, form_1.copy())
                for a in field_arrows
            ],
            FadeOut(integral_label),
            fleche1.animate.set_opacity(1.0),
            run_time=1.0,
        )
        # Clean up the duplicates and reveal the real form_1
        self.remove(*field_arrows)

        #fleche1.set_opacity(1.0)
        self.add(form_1)
        self.wait()
        self.next_slide()

        self.next_slide()
        bullet_integration = Tex(
            r"$\bullet$ Integrating against finitely many cells $\to$ finitely many values.",
            font_size=25,
        ).next_to(text_discrete, 2*DOWN, aligned_edge=LEFT)
        self.play(FadeIn(bullet_integration))
        self.wait()

        # ----------------------------------------------------------
        # Animation 2: orientation flip
        # Same field, opposite tangent direction, collapses into form_2
        # ----------------------------------------------------------
        self.next_slide()

        edge_start = fleche0.get_end()
        edge_end   = fleche0.get_start()
        edge_vec   = edge_end - edge_start
        edge_dir   = edge_vec / np.linalg.norm(edge_vec)

        # Sample points along the edge
        n_samples = 6
        sample_points = [
            edge_start + (i + 0.5) / n_samples * edge_vec
            for i in range(n_samples)
        ]


        # Reuse the same sample points but flip the arrow direction
        field_arrows_flipped = VGroup()
        for p, L in zip(sample_points, sample_lengths):
            a = Arrow(
                p + 0.5 * L * edge_dir,   # start and end swapped
                p - 0.5 * L * edge_dir,
                buff=0, stroke_width=2.5, color=GREEN, tip_length=0.08,
            )
            field_arrows_flipped.add(a)

        self.play(FadeIn(field_arrows_flipped, run_time=0.5))
        self.wait(0.3)
        self.next_slide()

        integral_label_neg = MathTex(r"\int_{-e} \alpha", font_size=28).next_to(fleche0.get_center(), 0.1*UP+LEFT, buff=0.15)
        self.play(FadeIn(integral_label_neg))
        self.wait(0.3)
        self.next_slide()

        self.play(
            *[Transform(a, form_2.copy()) for a in field_arrows_flipped],
            FadeOut(integral_label_neg),
            fleche0.animate.set_opacity(1.0),
            run_time=0.9,
        )
        self.remove(*field_arrows_flipped)
        self.add(form_2)
        self.wait(0.3)


        # ----------------------------------------------------------
        # BULLET 2: orientation flip → sign flip
        # ----------------------------------------------------------
        self.next_slide()
        bullet_orientation = Tex(
            r"$\bullet$ Reversing the orientation flips the sign.",
            font_size=25,
        ).next_to(bullet_integration, 2*DOWN, aligned_edge=LEFT)
        self.play(FadeIn(bullet_orientation))
        self.wait()

        # ----------------------------------------------------------
        # BULLET 3: the definition, as a summary of what was demonstrated
        # ----------------------------------------------------------
        self.next_slide()
        bullet_definition = Tex(
            r"$\bullet$ \textbf{Discrete $k$-form:} one scalar per oriented $k$-cell.",
            font_size=25,
        ).next_to(bullet_orientation, 2*DOWN, aligned_edge=LEFT)
        self.play(FadeIn(bullet_definition))
        self.wait()
        self.next_slide()
        """

        self.play(FadeIn(textDiscreteForm,form_1))
        
        self.wait()
        self.next_slide()
        text_reversing = Tex(" - Reversing the orientation yields a sign flip.",font_size=25).next_to(textDiscreteForm,2*DOWN,aligned_edge=LEFT)
        form_2 = MathTex("\\langle \\alpha,-e\\rangle = -2").next_to(fleche0.get_center(),0.3*LEFT).scale(0.5)
        

        fleche0.set_opacity(1.)
        self.play(FadeIn(form_2,text_reversing))
        self.wait(2)
        self.next_slide()
        self.play(FadeOut(form_1,form_2))
        textDiscretization = Tex("- Integration: turn smooth forms into discrete forms", font_size = 25).next_to(text_reversing,2*DOWN,aligned_edge=LEFT)
        self.play(FadeIn(textDiscretization))
        self.wait()
        self.next_slide()
        """
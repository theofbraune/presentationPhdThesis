from manim import *
from manim_slides import Slide
import utils.preamble as preamble


class slide8(Slide):
    def construct(self):
        # =====================================================================
        # The title evolves across the three beats
        # =====================================================================
        title = Tex("Vector bundles", font_size=30).to_corner(UL)
        self.play(FadeIn(title))
        self.next_slide()

        # =====================================================================
        # BEAT 1 — VECTOR BUNDLES
        # =====================================================================
        bundle_img = ImageMobject("figures/example_bundle.png").scale(0.9)
        bundle_img.to_edge(RIGHT).shift(DOWN * 0.3)
        self.play(FadeIn(bundle_img))

        bundle_caption = Tex(
            r"A vector space (the \textit{fiber} $E_p$) attached to each point of $M$.",
            font_size=24,
        ).next_to(title, 2*DOWN, aligned_edge=LEFT, buff=0.6)
        # bundle_caption.set_width(7)
        self.play(FadeIn(bundle_caption))
        self.next_slide()

        section_caption = Tex(
            r"A \textit{section} $\psi$ chooses one $\psi(p)\in E_p$ per point.",
            font_size=22,
        ).next_to(bundle_caption, 2*DOWN, aligned_edge=LEFT, buff=0.4)
        # section_caption.set_width(7)
        self.play(FadeIn(section_caption))
        self.wait(0.5)
        self.next_slide()

        # =====================================================================
        # CLEAR — transition to BEAT 2
        # =====================================================================
        new_title = Tex(r"Connections \& parallel transport", font_size=30).to_corner(UL)
        self.play(
            FadeOut(bundle_caption),
            FadeOut(section_caption),
            FadeOut(bundle_img),
            Transform(title, new_title),
        )
        self.next_slide()

        # =====================================================================
        # BEAT 2 — CONNECTIONS & PARALLEL TRANSPORT (enriched)
        # =====================================================================

        # ---- 2a: the question — how do we compare vectors in different fibers?
        compare_img = ImageMobject("figures/connections/two_connections_compare.png")
        compare_img.scale(0.75).to_edge(RIGHT).shift(DOWN * 0.2)
        self.play(FadeIn(compare_img))

        question = Tex(
            r"How do we compare vectors in different fibers?",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(FadeIn(question))
        self.next_slide()

        # ---- 2b: the answer — a connection
        # todo add here the animation from sigg
        answer = Tex(
            r"A \textit{connection} $\nabla$ specifies how to slide vectors between fibers along a curve.",
            font_size=24,
        ).next_to(question, DOWN, aligned_edge=LEFT, buff=0.4)
        answer.set_width(6.5)
        self.play(FadeIn(answer))
        self.next_slide()

        # ---- 2c: parallel transport — the vector follows the twist of the bundle
        pt_setup = ImageMobject("figures/connections/parallel_transport_setupy.png")
        pt_setup.scale(0.85).to_edge(RIGHT).shift(DOWN * 0.2)
        self.play(FadeOut(compare_img), FadeIn(pt_setup))
        self.next_slide()

        pt_done = ImageMobject("figures/connections/parallel_transport_finishedy.png")
        pt_done.scale(0.85).to_edge(RIGHT).shift(DOWN * 0.2)

        # twist_caption = Tex(
        #     r"The vector \textit{follows the twist} of the bundle.",
        #     font_size=20,
        #     color=YELLOW,
        # ).next_to(answer, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(FadeOut(pt_setup), FadeIn(pt_done)) 
        #.  FadeIn(twist_caption))
        self.next_slide()

        # ---- 2d: covariant derivative — formula evolves from naive attempt to definition
        cov1 = ImageMobject("figures/connections/covariant_derivative_setup.png")
        cov1.scale(0.75).to_edge(RIGHT).shift(DOWN * 0.2)

        cov_question = Tex(
            r"How do we differentiate a section?",
            font_size=22,
        ).next_to(answer, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(
            FadeOut(pt_done),
            FadeIn(cov1),
            FadeIn(cov_question),
        )
        self.next_slide()

        # Step 1: the naive difference quotient — values live in different fibers, doesn't make sense
        formula_step1 = MathTex(
            r"\frac{\psi_{\gamma(t+h)} \;-\; \psi_{\gamma(t)}}{h} \;\;?",
            font_size=26,
        ).next_to(cov_question, DOWN, aligned_edge=LEFT, buff=0.4)

        naive_caption = Tex(
            r"\small (but $\psi_{\gamma(t+h)}$ and $\psi_{\gamma(t)}$ live in \textit{different} fibers)",
            font_size=22,
            color=GRAY,
        ).next_to(formula_step1, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(FadeIn(formula_step1))
        self.play(FadeIn(naive_caption))
        self.next_slide()

        # Step 2: the fix — parallel-transport ψ at t+h back to t, image gains the transport arrow
        cov2 = ImageMobject("figures/connections/covariant_derivative_with_parallel_transport.png")
        cov2.scale(0.75).to_edge(RIGHT).shift(DOWN * 0.2)

        formula_step2 = MathTex(
            r"\frac{\mathcal{R}_{\gamma(t),\gamma(t+h)}\,\psi_{\gamma(t+h)} \;-\; \psi_{\gamma(t)}}{h}",
            font_size=26,
        ).next_to(cov_question, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(
            FadeOut(cov1),
            FadeIn(cov2),
            FadeOut(naive_caption),
            Transform(formula_step1, formula_step2),
        )
        self.next_slide()

        # Step 3: take the limit, name it ∇_X ψ
        formula_step3 = MathTex(
            r"\nabla_X\psi \;:=\; \lim_{h\to 0}"
            r"\frac{\mathcal{R}_{\gamma(t),\gamma(t+h)}\,\psi_{\gamma(t+h)} \;-\; \psi_{\gamma(t)}}{h}",
            font_size=22,
        ).next_to(cov_question, DOWN, aligned_edge=LEFT, buff=0.4)

        self.play(Transform(formula_step1, formula_step3))
        self.wait(0.5)
        self.next_slide()


       
        # ---- 2e: coordinate form, name ω
        # The image swaps from "parallel transport" to "frame field" because
        # the coordinate form depends on a choice of frame.
        frame_pic = ImageMobject("figures/connections/covariant_derivative_frame_aftery.png")
        frame_pic.scale(0.75).to_edge(RIGHT).shift(DOWN * 0.2)

        in_a_frame = Tex(
            r"In a local frame:",
            font_size=22,
        ).next_to(formula_step1, DOWN, aligned_edge=LEFT, buff=0.4)

        coord_form = MathTex(
            r"\nabla_X\psi \;=\; d_X\psi \;+\; \omega(X)\,\psi",
            font_size=26,
        ).next_to(in_a_frame, DOWN, aligned_edge=LEFT, buff=0.2)

        omega_label = Tex(
            r"$\omega$: the \textit{connection 1-form}",
            font_size=20,
            color=YELLOW,
        ).next_to(coord_form, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(
            FadeOut(cov2),
            FadeIn(frame_pic),
            FadeIn(in_a_frame),
        )
        self.play(FadeIn(coord_form))
        self.play(FadeIn(omega_label))
        self.wait(0.5)
        self.next_slide()
       
        # let the elements disappear 
        titleBundleValued = Tex(r"Bundle valued forms", font_size=30).to_corner(UL)
        self.play(

            FadeOut(frame_pic),
            FadeOut(in_a_frame),
            FadeOut(coord_form),
            FadeOut(omega_label),
            FadeOut(formula_step1),
            FadeOut(cov_question),
            FadeOut(question),
            FadeOut(answer),
            FadeOut(cov1),
            FadeOut(cov2),
            FadeOut(new_title),
            FadeOut(title),
            FadeIn(titleBundleValued)
        )


        self.wait()
        self.next_slide()
        # =====================================================================
        # BEAT 3 — BUNDLE-VALUED FORMS (side-by-side)
        # =====================================================================
        textFormally = Tex(r" Formally, bundle-valued $k$-forms are $\Omega^k(M,E) = \Omega^k(M) \otimes E$.", font_size=22).next_to(titleBundleValued, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textFormally))
        self.next_slide()


        scalar_img = ImageMobject("figures/two_forms_scalar_valued.png").scale(0.85)
        scalar_img.shift(LEFT * 3 + 1.5 * DOWN * 0.3)

        bundle_form_img = ImageMobject("figures/two_forms_bundle_valued.png").scale(0.85)
        bundle_form_img.shift(RIGHT * 3 + 1.5 * DOWN * 0.3)

        scalar_label = Tex(
            r"scalar 2-form: returns a \textit{number}",
            font_size=22,
        ).next_to(scalar_img, UP, buff=0.2)
        bundle_form_label = Tex(
            r"bundle-valued 2-form: returns a \textit{vector}",
            font_size=22,
        ).next_to(bundle_form_img, UP, buff=0.2)

        self.play(FadeIn(scalar_img), FadeIn(scalar_label))
        self.next_slide()
        self.play(FadeIn(bundle_form_img), FadeIn(bundle_form_label))
        self.next_slide()

        transition = Tex(
            r"To differentiate them we need the covariant exterior derivative $d^{\nabla}$.",
            font_size=24,
        ).to_edge(DOWN, buff=0.6)
        self.play(FadeIn(transition))
        self.wait()
        self.next_slide()
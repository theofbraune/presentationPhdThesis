from manim import *
from manim_slides import Slide, ThreeDSlide
import numpy as np
from utils.preamble import *
from utils.videoLoop import *


# ─────────────────────────────────────────────────────────────────────────────
# Surface helpers
# ─────────────────────────────────────────────────────────────────────────────
SURF_SCALE = 0.65
SURF_SHIFT  =  2.*DOWN 

def surf_z(u, v):
    return 1.5 * np.sin(0.45 * u) + 0.9 * np.cos(0.5 * v)

def surf_point(u, v):
    return SURF_SCALE * np.array([u, v, surf_z(u, v)]) + np.array([*SURF_SHIFT[:2], 0])

def surf_normal(u, v):
    dz_du = 1.5 * 0.45 * np.cos(0.45 * u)
    dz_dv = -0.9 * 0.5 * np.sin(0.5 * v)
    tu = SURF_SCALE * np.array([1, 0, dz_du])
    tv = SURF_SCALE * np.array([0, 1, dz_dv])
    n  = np.cross(tu, tv)
    return n / np.linalg.norm(n)

def make_fiber_square(base_pt, normal, size=0.35, color="#FFD166",
                      edge_color="#FFFFFF", opacity=0.85):
    normal = normal / np.linalg.norm(normal)
    ref = UP if abs(np.dot(normal, UP)) < 0.85 else RIGHT
    t1  = np.cross(normal, ref);  t1 = t1 / np.linalg.norm(t1)
    t2  = np.cross(normal, t1);   t2 = t2 / np.linalg.norm(t2)
    offset = 0.15 * normal
    c  = base_pt + offset
    s  = size / 2
    corners = [c + s*t1 + s*t2, c - s*t1 + s*t2,
               c - s*t1 - s*t2, c + s*t1 - s*t2]
    face  = Polygon(*corners, fill_color=color, fill_opacity=opacity,
                    stroke_color=edge_color, stroke_width=2.0)
    stalk = Line(base_pt, c, color=edge_color,
                 stroke_width=1.2, stroke_opacity=0.6)
    return VGroup(stalk, face)

def make_fiber_arrow(base, tip, t1, t2, color="#000000",
                     shaft_width=2.5, tip_size=0.06):
    direction = tip - base
    length = np.linalg.norm(direction)
    if length < 1e-6:
        return VGroup()
    unit      = direction / length
    shaft_end = base + (length - tip_size * 1.2) * unit
    shaft = Line(base, shaft_end, color=color, stroke_width=shaft_width)
    v_comp = np.dot(t1, unit) * t2 - np.dot(t2, unit) * t1
    if np.linalg.norm(v_comp) > 1e-6:
        v_comp = v_comp / np.linalg.norm(v_comp)
    else:
        v_comp = t1
    head = Polygon(tip,
                   shaft_end + tip_size * 0.55 * v_comp,
                   shaft_end - tip_size * 0.55 * v_comp,
                   fill_color=color, fill_opacity=1.0,
                   stroke_color=color, stroke_width=0)
    return VGroup(shaft, head)


# ─────────────────────────────────────────────────────────────────────────────
# Curve: longer, more interesting path across the surface
# ─────────────────────────────────────────────────────────────────────────────
U0, V0 = -3.5, -2.5

def curve_uv(t):
    u = U0 + t * 7.0
    v = V0 + t * 5.0 + 1.2 * np.sin(2.5 * t)
    return u, v

def curve_pt(t):
    u, v = curve_uv(t)
    return surf_point(u, v)

def curve_normal(t):
    u, v = curve_uv(t)
    return surf_normal(u, v)

def curve_frame(t):
    u, v = curve_uv(t)
    n    = surf_normal(u, v);  n = n / np.linalg.norm(n)
    ref  = UP if abs(np.dot(n, UP)) < 0.85 else RIGHT
    t1   = np.cross(n, ref);   t1 = t1 / np.linalg.norm(t1)
    t2   = np.cross(n, t1);    t2 = t2 / np.linalg.norm(t2)
    return t1, t2

from manim import *
from manim_slides import Slide
import numpy as np
from utils.preamble import *


class slidePPF(Slide):
    def construct(self):

        title = Tex(
            r"The Parallel-Propagated Frame",
            font_size=30,
        ).to_corner(UL)
        self.add(title)
        self.next_slide()

        # =====================================================================
        # BEAT 1 — key insight: ω = 0 at the source point
        # =====================================================================
        text1 = Tex(
            r"The $\omega \wedge \alpha$ term depends on the choice of frame.",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(text1))
        self.next_slide()
        
        HEIGHTIm = 4.5
        POS = ORIGIN + 3**RIGHT
        
        videoParallelTransport = play_video_loop(
            self,
            frame_dir="figures/renderParallelTransport/croppedOut/",
            position=POS,   # <-- sit exactly over imageWithConn
            height=HEIGHTIm,           # <-- match exact height
            fps=3,
            fade_in_time=0.5,
            fade_out_time=0.0,
            persist=True,
        )

        
        text2 = Tex(
            r"Fix a source point $p_0$. "
            r"Parallel-transport the frame at $p_0$ to nearby points.",
            font_size=24,
        ).next_to(text1, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(text2))
        self.wait(2)
        self.next_slide()

        videoParallelTransport2 = play_video_loop(
            self,
            frame_dir="figures/renderTransportFrame/croppedOut/",
            position=POS,   # <-- sit exactly over imageWithConn
            height=HEIGHTIm,           # <-- match exact height
            fps=3,
            fade_in_time=0.5,
            fade_out_time=0.0,
            persist=True,
        )
        self.remove(videoParallelTransport)  # <-- remove the first video
        self.wait()
        self.next_slide()
        imageParallelTransport = ImageMobject("figures/discreteFormsAndCurvature/parallelTransportPPF.png")
        imageParallelTransport.height = HEIGHTIm
        imageParallelTransport.move_to(POS)
        self.play(FadeIn(imageParallelTransport))
        self.remove(videoParallelTransport2)  # <-- remove the second video
        self.wait()
        self.next_slide()
        imageParallelTransport2 = ImageMobject("figures/discreteFormsAndCurvature/parallelTransportPPF2.png")
        imageParallelTransport2.height = HEIGHTIm
        imageParallelTransport2.move_to(POS)
        # self.play(Transform(imageParallelTransport, imageParallelTransport2), run_time=1.0)
        self.play(FadeOut(imageParallelTransport), FadeIn(imageParallelTransport2), run_time=1.0)
        self.next_slide()   

        imageParallelTransport3 = ImageMobject("figures/discreteFormsAndCurvature/parallelTransportPPF3.png")
        imageParallelTransport3.height = HEIGHTIm
        imageParallelTransport3.move_to(POS)
        # self.play(Transform(imageParallelTransport, imageParallelTransport3), run_time=1.0)
        self.play(FadeOut(imageParallelTransport2), FadeIn(imageParallelTransport3), run_time=1.0)
        self.next_slide()   

        imageParallelTransport4 = ImageMobject("figures/discreteFormsAndCurvature/parallelTransportPPF4.png")
        imageParallelTransport4.height = HEIGHTIm
        imageParallelTransport4.move_to(POS)
        # self.play(Transform(imageParallelTransport, imageParallelTransport4), run_time=1.0)
        self.play(FadeOut(imageParallelTransport3), FadeIn(imageParallelTransport4), run_time=1.0)
        self.next_slide()

        self.wait()

        text3 = Tex(
            r"Along $\gamma$: $R = \mathrm{Id}$",
            font_size=24,
        ).next_to(text2, DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(FadeIn(text3))
        self.wait()
        self.next_slide()

        arrow_down = Tex(r"$\Downarrow$", font_size=28
                         ).next_to(text3,  DOWN, aligned_edge=LEFT, buff=0.15)
        self.play(FadeIn(arrow_down))

        omega_zero = MathTex(
            r"\omega(p_0) \;=\; \log(\mathrm{Id}) \;=\; 0",
            font_size=30, color=YELLOW,
        ).next_to(arrow_down, 2*DOWN, aligned_edge=LEFT, buff=0.15)
        box_omega = SurroundingRectangle(omega_zero, color=YELLOW, buff=0.15)
        self.play(FadeIn(omega_zero), Create(box_omega))
        self.next_slide()

        text4 = Tex(
            r"By continuity: $\omega = \mathcal{O}(h)$.",
            font_size=24, color=YELLOW,
        ).next_to(omega_zero, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(text4))
        self.wait()
        self.next_slide()

        # =====================================================================
        # BEAT 2 — retraction: what the PPF looks like geometrically
        # =====================================================================
        self.play(
            FadeOut(text1), FadeOut(text2), FadeOut(text3),
            FadeOut(arrow_down), FadeOut(omega_zero),
            FadeOut(box_omega), FadeOut(text4),
            FadeOut(imageParallelTransport4)
        )
        self.next_slide()

        text_retract = Tex(
            r"Given a simplicial region $\sigma$, pick a source $p_0$. ",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4).set_max_width(5.5)
        text_retract2 = Tex(
            r"For every $p \in \sigma$, draw the retraction path "
            r"$\gamma_p \colon p \to p_0$.", font_size=24,
        ).next_to(text_retract, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.5)
        self.play(FadeIn(text_retract))
        self.next_slide()
        self.play(FadeIn(text_retract2))

        img_retraction = ImageMobject("figures/retraction.png")
        img_retraction.height = 4.2
        img_retraction.to_edge(RIGHT, buff=0.4).shift(DOWN * 0.4)
        self.play(FadeIn(img_retraction))
        self.next_slide()

        text_transport = Tex(
            r"Parallel-transport the frame at $p_0$ "
            r"along each path $\gamma_p$.",
            font_size=24,
        ).next_to(text_retract2, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.5)
        self.play(FadeIn(text_transport))
        self.next_slide()

        text_name = Tex(
            r"This is the \textbf{parallel-propagated frame} (PPF).",
            font_size=24, color=YELLOW,
        ).next_to(text_transport, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.5)
        self.play(FadeIn(text_name))
        self.next_slide()

        # =====================================================================
        # BEAT 3 — two choices of source point
        # =====================================================================
        text_vertex = Tex(
            r"$\bullet$ Source = vertex $v_0$: "
            r"retraction paths go to $v_0$.",
            font_size=22,
        ).next_to(text_name, DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.5)
        self.play(FadeIn(text_vertex))
        self.next_slide()

        text_bary = Tex(
            r"$\bullet$ Source = barycenter $c_\sigma$: "
            r"retraction paths go to $c_\sigma$.",
            font_size=22,
        ).next_to(text_vertex, DOWN, aligned_edge=LEFT, buff=0.2).set_max_width(5.5)
        self.play(FadeIn(text_bary))
        self.next_slide()
        text_important = Tex(r" The PPF yields a \textit{canonical}, \textit{geometric} choice of frame for discretization.", font_size=30, color=YELLOW).next_to(text_bary, 5*DOWN, aligned_edge=LEFT, buff=0.3).set_max_width(5.5)
        surrRect = SurroundingRectangle(text_important, color=YELLOW, buff=0.15)
        self.play(FadeIn(text_important), Create(surrRect))
        self.wait()
        self.next_slide()
        

        
    
from manim import *
from manim_slides import Slide, ThreeDSlide
import utils.preamble as preamble
import numpy as np


# ─────────────────────────────────────────────────────────────────────────────
# Surface helpers — must match slide8.py exactly
# ─────────────────────────────────────────────────────────────────────────────
SURF_SCALE = 0.38
SURF_SHIFT  = -RIGHT * 1.5 + DOWN * 3.5

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
    offset  = 0.15 * normal
    c       = base_pt + offset
    s       = size / 2
    corners = [
        c + s*t1 + s*t2,
        c - s*t1 + s*t2,
        c - s*t1 - s*t2,
        c + s*t1 - s*t2,
    ]
    face = Polygon(
        *corners,
        fill_color=color,
        fill_opacity=opacity,
        stroke_color=edge_color,
        stroke_width=2.0,
    )
    stalk = Line(
        base_pt, c,
        color=edge_color,
        stroke_width=1.2,
        stroke_opacity=0.6,
    )
    return VGroup(stalk, face)

def make_fiber_arrow(base, tip, t1, t2, color="#000000",
                     shaft_width=2.5, tip_size=0.06):
    direction = tip - base
    length    = np.linalg.norm(direction)
    if length < 1e-6:
        return VGroup()
    unit      = direction / length
    shaft_end = base + (length - tip_size * 1.2) * unit
    shaft = Line(base, shaft_end, color=color, stroke_width=shaft_width)
    v_comp_plane = np.dot(t1, unit) * t2 - np.dot(t2, unit) * t1
    if np.linalg.norm(v_comp_plane) > 1e-6:
        v_comp_plane = v_comp_plane / np.linalg.norm(v_comp_plane)
    else:
        v_comp_plane = t1
    apex  = tip
    left  = shaft_end + tip_size * 0.55 * v_comp_plane
    right = shaft_end - tip_size * 0.55 * v_comp_plane
    head = Polygon(
        apex, left, right,
        fill_color=color,
        fill_opacity=1.0,
        stroke_color=color,
        stroke_width=0,
    )
    return VGroup(shaft, head)

def make_frame(center, angle=0.0, scale=0.45, color1=YELLOW, color2=BLUE):
    e1 = np.array([np.cos(angle), np.sin(angle), 0])
    e2 = np.array([-np.sin(angle), np.cos(angle), 0])
    a1 = Arrow(center, center + scale*e1, buff=0, color=color1,
               stroke_width=3, max_tip_length_to_length_ratio=0.25)
    a2 = Arrow(center, center + scale*e2, buff=0, color=color2,
               stroke_width=3, max_tip_length_to_length_ratio=0.25)
    return VGroup(a1, a2)

def gamma_uv(t):
    u = -3.5 + 7.0 * t
    v = -3.5 + 7.0 * t
    return u, v

def gamma(t):
    u, v = gamma_uv(t)
    return surf_point(u, v)

def gamma_normal(t):
    u, v = gamma_uv(t)
    return surf_normal(u, v)


class slide8b(ThreeDSlide):
    def construct(self):

        # =====================================================================
        # CAMERA — must match slide8 exactly
        # =====================================================================
        self.set_camera_orientation(
            phi=55 * DEGREES,
            theta=160 * DEGREES,
            zoom=1.05,
        )

        # =====================================================================
        # SURFACE
        # =====================================================================
        surface = Surface(
            lambda u, v: surf_point(u, v),
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=(20, 20),
            fill_color="#1B4D5C",
            fill_opacity=0.85,
            stroke_color="#2A7A8C",
            stroke_width=0.8,
            stroke_opacity=0.7,
        )
        self.add(surface)

        label_M = Tex(r"$\mathcal{M}$", font_size=35)
        label_M.move_to(surf_point(4.5, -4.5) + UP * 4.0 + RIGHT * 1.0)
        self.add_fixed_orientation_mobjects(label_M)
        self.add(label_M)

        # =====================================================================
        # CURVE + DOTS + LABEL
        # =====================================================================
        N_CURVE      = 60
        curve_points = [gamma(t) for t in np.linspace(0, 1, N_CURVE)]
        curve = VMobject(color=WHITE, stroke_width=3)
        curve.set_points_smoothly(curve_points)
        self.add(curve)

        dot_start = Dot3D(gamma(0.0), radius=0.08, color=GREEN)
        dot_end   = Dot3D(gamma(1.0), radius=0.08, color=RED)
        self.add(dot_start, dot_end)

        u_mid, v_mid = gamma_uv(0.5)
        n_mid        = surf_normal(u_mid, v_mid)
        label_gamma  = Tex(r"$\gamma$", font_size=35, color=BLACK)
        label_gamma.move_to(gamma(0.5) + 0.6 * n_mid + np.array([0.2, 0.0, 0.0]))
        self.add_fixed_orientation_mobjects(label_gamma)
        self.add(label_gamma)

        # =====================================================================
        # FIBERS ALONG THE CURVE
        # =====================================================================
        N_bundle    = 10
        fibersCurve = VGroup()
        for t in np.linspace(0, 1, N_bundle):
            u, v = gamma_uv(t)
            pt   = surf_point(u, v)
            n    = surf_normal(u, v)
            fibersCurve.add(make_fiber_square(pt, n, size=0.28,
                                              color="#FFD166", opacity=0.65))
        self.add(fibersCurve)

        # =====================================================================
        # MOVING ARROW AT FINAL POSITION (t=1)
        # =====================================================================
        ARROW_LENGTH = 0.22
        ARROW_COLOR  = BLACK
        total_angle  = 1.1

        u_f, v_f = gamma_uv(1.0)
        n_f      = surf_normal(u_f, v_f);  n_f = n_f / np.linalg.norm(n_f)
        ref_f    = UP if abs(np.dot(n_f, UP)) < 0.85 else RIGHT
        t1_f     = np.cross(n_f, ref_f);   t1_f = t1_f / np.linalg.norm(t1_f)
        t2_f     = np.cross(n_f, t1_f);    t2_f = t2_f / np.linalg.norm(t2_f)

        angle_final = total_angle * (1.0 ** 1.5)
        dir_final   = np.cos(angle_final) * t1_f + np.sin(angle_final) * t2_f
        base_final  = surf_point(u_f, v_f) + 0.15 * n_f
        tip_final   = base_final + ARROW_LENGTH * dir_final

        moving_arrow = make_fiber_arrow(
            base_final, tip_final, t1_f, t2_f,
            color=ARROW_COLOR, shaft_width=3.0, tip_size=0.08,
        )
        self.add(moving_arrow)

        # =====================================================================
        # TRANSPORT LABEL AT FINAL POSITION
        # =====================================================================
        transport_label = MathTex(
            r"\mathcal{R}^\nabla_{\gamma,t}v \in E_{\gamma(t)}",
            font_size=22, color=WHITE,
        )
        transport_label.move_to(base_final + 0.5 * n_f)
        self.add_fixed_orientation_mobjects(transport_label)
        self.add(transport_label)

        # =====================================================================
        # TRAIL ARROWS — same logic as slide8, precomputed
        # =====================================================================
        fiber_ts    = np.linspace(0, 1, N_bundle)
        fiber_bases = []
        fiber_frames_list = []
        for t_f in fiber_ts:
            u_ff, v_ff = gamma_uv(t_f)
            pt_ff  = surf_point(u_ff, v_ff)
            n_ff   = surf_normal(u_ff, v_ff);  n_ff = n_ff / np.linalg.norm(n_ff)
            ref_ff = UP if abs(np.dot(n_ff, UP)) < 0.85 else RIGHT
            t1_ff  = np.cross(n_ff, ref_ff);   t1_ff = t1_ff / np.linalg.norm(t1_ff)
            t2_ff  = np.cross(n_ff, t1_ff);    t2_ff = t2_ff / np.linalg.norm(t2_ff)
            fiber_bases.append(pt_ff + 0.15 * n_ff)
            fiber_frames_list.append((n_ff, t1_ff, t2_ff))

        N_STEPS = 50
        visited_arrows       = VGroup()
        placed_fiber_indices = set()

        for i, t in enumerate(np.linspace(0, 1, N_STEPS)):
            u_t, v_t  = gamma_uv(t)
            pt_t      = surf_point(u_t, v_t)
            n_t       = surf_normal(u_t, v_t);  n_t = n_t / np.linalg.norm(n_t)
            ref_t     = UP if abs(np.dot(n_t, UP)) < 0.85 else RIGHT
            t1_t      = np.cross(n_t, ref_t);   t1_t = t1_t / np.linalg.norm(t1_t)
            t2_t      = np.cross(n_t, t1_t);    t2_t = t2_t / np.linalg.norm(t2_t)
            angle_t   = total_angle * (t ** 1.5)
            direction = np.cos(angle_t) * t1_t + np.sin(angle_t) * t2_t
            base_t    = pt_t + 0.15 * n_t

            dists       = [np.linalg.norm(base_t - fb) for fb in fiber_bases]
            nearest_idx = int(np.argmin(dists))

            if nearest_idx not in placed_fiber_indices and dists[nearest_idx] < 0.25:
                placed_fiber_indices.add(nearest_idx)
                _, t1_fi, t2_fi = fiber_frames_list[nearest_idx]
                trail_base = fiber_bases[nearest_idx]
                trail_tip  = trail_base + ARROW_LENGTH * direction
                trail = make_fiber_arrow(
                    trail_base, trail_tip, t1_fi, t2_fi,
                    color=ARROW_COLOR, shaft_width=1.5, tip_size=0.06,
                )
                trail.set_opacity(0.45)
                visited_arrows.add(trail)

        self.add(visited_arrows)

        # =====================================================================
        # FIXED-IN-FRAME TEXT from slide8
        # =====================================================================
        title = Tex("Vector Bundles and Connections", font_size=30).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        self.add(title)

        textConn2 = Tex(
            r"A connection assigns "
            r"$\mathcal{R}^\nabla_{\gamma,t} \colon "
            r"E_{\gamma(0)} \to E_{\gamma(t)}$ to each curve $\gamma$.",
            font_size=24,
        ).next_to(title, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(textConn2)
        self.add(textConn2)

        self.wait(1)
        self.next_slide()

        # =====================================================================
        # CONNECTION 1-FORM: rotating frames in each fiber
        # =====================================================================
        textConnOneForm = Tex(
            r"Connection one-form $\omega$: infinitesimal change of the rotation",
            font_size=24,
        ).next_to(textConn2, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(textConnOneForm)
        self.play(FadeIn(textConnOneForm))

        fiber_frames_3d = VGroup()
        for idx, t in enumerate(np.linspace(0, 1, N_bundle)):
            u, v  = gamma_uv(t)
            pt    = surf_point(u, v)
            n     = surf_normal(u, v);  n = n / np.linalg.norm(n)
            ref   = UP if abs(np.dot(n, UP)) < 0.85 else RIGHT
            t1    = -np.cross(n, ref);   t1 = t1 / np.linalg.norm(t1)
            t2    = -np.cross(n, t1);    t2 = t2 / np.linalg.norm(t2)
            frame_angle = total_angle * (t ** 1.5)
            e1 = np.cos(frame_angle) * t1 + np.sin(frame_angle) * t2
            e2 = -np.sin(frame_angle) * t1 + np.cos(frame_angle) * t2
            base  = pt + 0.15 * n
            scale = 0.18
            a1 = make_fiber_arrow(base, base + scale * e1, t1, t2,
                                  color=BLACK, shaft_width=2.0, tip_size=0.06)
            a2 = make_fiber_arrow(base, base + scale * e2, t1, t2,
                                  color=BLACK, shaft_width=2.0, tip_size=0.06)
            fiber_frames_3d.add(VGroup(a1, a2))

        self.play(
            LaggedStart(*[FadeIn(f) for f in fiber_frames_3d], lag_ratio=0.1),
            run_time=1.5,
        )
        self.next_slide()

        # =====================================================================
        # ω = αJ
        # =====================================================================
        textSkew = Tex(
            r"On a surface, $\omega$ is skew-symmetric — one scalar 1-form $\alpha$:",
            font_size=24,
        ).next_to(textConnOneForm, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(textSkew)
        self.play(FadeIn(textSkew))

        omega_formula = MathTex(
            r"\mathcal{R}^\nabla_{\gamma,t} = P\,\mathrm{exp}\!\left(\int_{\gamma}\omega\right),\quad \omega(X) = \alpha(X)\,J,\quad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}",
            font_size=24,
        ).next_to(textSkew, DOWN, aligned_edge=LEFT, buff=0.25)
        self.add_fixed_in_frame_mobjects(omega_formula)
        self.play(FadeIn(omega_formula))
        self.next_slide()

        # =====================================================================
        # CURVATURE TEASER
        # =====================================================================
        textCurv = Tex(
            r"The \textit{curvature} $\Omega^\nabla$ measures how much "
            r"$\mathcal{R}^\nabla_{\gamma,t}$ depends on the path:",
            font_size=24,
        ).next_to(omega_formula, DOWN, aligned_edge=LEFT, buff=0.35)
        self.add_fixed_in_frame_mobjects(textCurv)
        self.play(FadeIn(textCurv))

        curv_formula = MathTex(
            r"\Omega^\nabla \;=\; d\omega + \omega \wedge \omega",
            font_size=28,
        ).next_to(textCurv, DOWN, aligned_edge=LEFT, buff=0.2)
        curv_box = SurroundingRectangle(curv_formula, color=BLUE_C, buff=0.15)
        self.add_fixed_in_frame_mobjects(curv_box)
        self.add_fixed_in_frame_mobjects(curv_formula)
        self.play(FadeIn(curv_formula))
        self.play(Create(curv_box))
        self.next_slide()


        self.play(
            FadeOut(textCurv), FadeOut(curv_formula),
            FadeOut(curv_box)
        )
        self.next_slide()

        # =====================================================================
        # COVARIANT DERIVATIVE: ∇ = d + ω
        # =====================================================================
        textCovDeriv = Tex(
            r"The covariant derivative of a section $\psi$ in direction $X$:",
            font_size=24,
        ).next_to(omega_formula, DOWN, aligned_edge=LEFT, buff=0.35)
        self.add_fixed_in_frame_mobjects(textCovDeriv)
        self.play(FadeIn(textCovDeriv))

        nabla_formula = MathTex(
            r"\nabla_X \psi \;=\;\underbrace{d_X \psi}_{\text{acts on coordinates}}\;+\; \underbrace{\omega(X)\,\psi}_{\text{acts on the frame}}",
            font_size=26,
        ).next_to(textCovDeriv, DOWN, aligned_edge=LEFT, buff=0.25)
        nabla_box = SurroundingRectangle(nabla_formula, color=YELLOW, buff=0.15)
        self.add_fixed_in_frame_mobjects(nabla_formula)
        self.add_fixed_in_frame_mobjects(nabla_box)
        self.play(FadeIn(nabla_formula))
        self.play(Create(nabla_box))
        self.wait(1)
        self.next_slide()

        # =====================================================================
        # CLEAR
        # =====================================================================
        self.play(
            FadeOut(textConnOneForm), FadeOut(textSkew),
            FadeOut(omega_formula), FadeOut(textCovDeriv),
            FadeOut(nabla_formula), FadeOut(nabla_box),
            FadeOut(fiber_frames_3d),
            FadeOut(moving_arrow), FadeOut(transport_label),
            FadeOut(visited_arrows), FadeOut(fibersCurve),
            FadeOut(curve), FadeOut(dot_start), FadeOut(dot_end),
            FadeOut(label_gamma), FadeOut(surface), FadeOut(label_M),
            FadeOut(textConn2), FadeOut(title),
        )
        self.next_slide()
        
        self.move_camera(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            zoom=1.0,
            run_time=0.5,
        )
        self.set_camera_orientation(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
        )
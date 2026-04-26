from manim import *
from manim_slides import Slide, ThreeDSlide
import utils.preamble as preamble
import numpy as np


# ─────────────────────────────────────────────────────────────────────────────
# Surface helpers
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


# ─────────────────────────────────────────────────────────────────────────────
# Curve γ helpers — defined at module level so gamma() and gamma_normal()
# are available everywhere without redefinition
# ─────────────────────────────────────────────────────────────────────────────
def gamma_uv(t):
    """Returns (u, v) parameter values along the curve."""
    u = -3.5 + 7.0 * t
    v = -3.5 + 7.0 * t
    return u, v

def gamma(t):
    u, v = gamma_uv(t)
    return surf_point(u, v)

def gamma_normal(t):
    u, v = gamma_uv(t)
    return surf_normal(u, v)


class slide8(ThreeDSlide):
    def construct(self):

        # =====================================================================
        # TITLE
        # =====================================================================
        title = Tex("Vector Bundles and Connections", font_size=30).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title))
        self.next_slide()
        bundle_caption = Tex(
            r"$\bullet$ A vector space (the \textit{fiber} $E_p$) "
            r"attached to each point of $\mathcal{M}$.",
            font_size=24,
        ).next_to(title, 2*DOWN, aligned_edge=LEFT, buff=0.5)
        self.add_fixed_in_frame_mobjects(bundle_caption)
        self.play(FadeIn(bundle_caption))
        self.next_slide()

        # =====================================================================
        # BEAT 1 — VECTOR BUNDLES  (3-D scene)
        # =====================================================================
        self.set_camera_orientation(
            phi=55 * DEGREES,
            theta=160 * DEGREES,
            zoom=1.05,
        )

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
        self.play(FadeIn(label_M))

        # =====================================================================
        # STEP 2 — fiber squares
        # =====================================================================
        grid_us = np.linspace(-4.0, 4.0, 10)
        grid_vs = np.linspace(-4.0, 4.0, 10)

        fiber_group = VGroup()
        for u in grid_us:
            for v in grid_vs:
                pt = surf_point(u, v)
                n  = surf_normal(u, v)
                fiber_group.add(make_fiber_square(pt, n, size=0.30))

        self.play(
            LaggedStart(*[FadeIn(f) for f in fiber_group], lag_ratio=0.05),
            run_time=2.0,
        )

        

        # =====================================================================
        # STEP 3 — section as arrows in the fiber planes
        # =====================================================================
        section_caption = Tex(
            r"$\bullet$A \textit{section} $\psi$ chooses one vector "
            r"$\psi(p)\in E_p$ per point.",
            font_size=24,
        ).next_to(bundle_caption, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(section_caption)
        self.play(FadeIn(section_caption))

        section_arrows = VGroup()
        for u in grid_us:
            for v in grid_vs:
                pt     = surf_point(u, v)
                normal = surf_normal(u, v)
                normal = normal / np.linalg.norm(normal)
                ref = UP if abs(np.dot(normal, UP)) < 0.85 else RIGHT
                t1  = np.cross(normal, ref);  t1 = t1 / np.linalg.norm(t1)
                t2  = np.cross(normal, t1);   t2 = t2 / np.linalg.norm(t2)
                angle     = 0.0 * u + 0.2 * v
                length    = 0.15
                direction = np.cos(angle) * t1 + np.sin(angle) * t2
                base = pt + 0.15 * normal
                tip  = base + length * direction
                section_arrows.add(
                    make_fiber_arrow(base, tip, t1, t2,
                                     color="#000000",
                                     shaft_width=2.0,
                                     tip_size=0.07)
                )

        self.play(
            LaggedStart(*[FadeIn(a) for a in section_arrows], lag_ratio=0.03),
            run_time=1.5,
        )
        self.wait(0.3)
        self.next_slide()

        # =====================================================================
        # CONNECTION INTRO TEXT
        # =====================================================================
        textConnection = Tex(
            r"$\bullet$ To compare vectors in different fibers, "
            r"we need a \textit{connection} $\nabla$.",
            font_size=24,
        ).next_to(section_caption, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(textConnection)
        self.play(FadeIn(textConnection))
        self.wait()
        self.next_slide()

        textConn2 = Tex(
            r"$\bullet$ A connection assigns "
            r"$\mathcal{R}^\nabla_{\gamma,t} \colon "
            r"E_{\gamma(0)} \to E_{\gamma(t)}$ to each curve $\gamma$.",
            font_size=24,
        ).next_to(textConnection, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(textConn2)
        self.play(FadeIn(textConn2))
        self.next_slide()

        # =====================================================================
        # PARALLEL TRANSPORT ANIMATION
        # =====================================================================

        # step 1: clear section arrows + text, keep surface
        self.play(
            FadeOut(section_arrows),
            # FadeOut(section_caption),
            # FadeOut(bundle_caption),
            # FadeOut(textConnection),
            # FadeOut(textConn2),
        )
        self.next_slide()

        # step 2: clear all fibers — show clean surface only
        self.play(FadeOut(fiber_group))

        # step 3: draw curve γ on the surface
        N_CURVE      = 60
        t_vals_curve = np.linspace(0, 1, N_CURVE)
        curve_points = [gamma(t) for t in t_vals_curve]
        curve = VMobject(color=WHITE, stroke_width=3)
        curve.set_points_smoothly(curve_points)

        # labels lifted along the surface normal — guaranteed above the surface
        LIFT = 0.55

        u_start, v_start = gamma_uv(0.0)
        u_end,   v_end   = gamma_uv(1.0)
        n_start = surf_normal(u_start, v_start)
        n_end   = surf_normal(u_end,   v_end)

        dot_start = Dot3D(gamma(0.0), radius=0.08, color=GREEN)
        dot_end   = Dot3D(gamma(1.0), radius=0.08, color=RED)

        

        self.play(Create(curve), run_time=1.2)
        self.play(FadeIn(dot_start))
        self.play(FadeIn(dot_end))
        u_mid, v_mid = gamma_uv(0.5)
        n_mid        = surf_normal(u_mid, v_mid)
        label_gamma  = Tex(r"$\gamma$", font_size=35, color=BLACK)
        label_gamma.move_to(gamma(0.5) + 0.6 * n_mid + np.array([0.2, 0.0, 0.0]))
        self.add_fixed_orientation_mobjects(label_gamma)
        self.play(FadeIn(label_gamma))
        self.next_slide()

        # step 4: show fibers only along the curve — correct u,v parametrization
        N_bundle   = 10
        fibersCurve = VGroup()
        for t in np.linspace(0, 1, N_bundle):
            u, v = gamma_uv(t)
            pt   = surf_point(u, v)
            n    = surf_normal(u, v)
            fibersCurve.add(make_fiber_square(pt, n, size=0.28,
                                              color="#FFD166", opacity=0.65))
        self.play(
            LaggedStart(*[FadeIn(f) for f in fibersCurve], lag_ratio=0.08),
            run_time=1.2,
        )
        self.next_slide()

        # step 5: initial vector in the fiber at γ(0)
        t0      = 0.0
        pt_t0   = gamma(t0)
        n_t0    = gamma_normal(t0)
        n_t0    = n_t0 / np.linalg.norm(n_t0)
        ref_t0  = UP if abs(np.dot(n_t0, UP)) < 0.85 else RIGHT
        t1_0    = np.cross(n_t0, ref_t0);  t1_0 = t1_0 / np.linalg.norm(t1_0)
        t2_0    = np.cross(n_t0, t1_0);   t2_0 = t2_0 / np.linalg.norm(t2_0)

        ARROW_LENGTH = 0.22
        ARROW_COLOR  = BLACK

        base_0 = pt_t0 + 0.15 * n_t0
        tip_0  = base_0 + ARROW_LENGTH * t1_0    # starts pointing along t1

        moving_arrow = make_fiber_arrow(
            base_0, tip_0, t1_0, t2_0,
            color=ARROW_COLOR, shaft_width=3.0, tip_size=0.08,
        )
        self.play(FadeIn(moving_arrow))
        self.next_slide()

        # step 6: transport label that travels with the arrow
        transport_label = MathTex(
            r"\mathcal{R}^\nabla_{\gamma,t}v \in E_{\gamma(t)}",
            font_size=22, color=BLACK,
        )
        transport_label.move_to(base_0 + 0.5 * n_t0)
        self.add_fixed_orientation_mobjects(transport_label)
        self.play(FadeIn(transport_label))
        self.next_slide()

        # precompute fiber centers along the curve so trails snap to them
        fiber_ts     = np.linspace(0, 1, N_bundle)
        fiber_bases  = []
        fiber_frames = []
        for t_f in fiber_ts:
            u_f, v_f = gamma_uv(t_f)
            pt_f  = surf_point(u_f, v_f)
            n_f   = surf_normal(u_f, v_f);  n_f = n_f / np.linalg.norm(n_f)
            ref_f = UP if abs(np.dot(n_f, UP)) < 0.85 else RIGHT
            t1_f  = np.cross(n_f, ref_f);  t1_f = t1_f / np.linalg.norm(t1_f)
            t2_f  = np.cross(n_f, t1_f);   t2_f = t2_f / np.linalg.norm(t2_f)
            fiber_bases.append(pt_f + 0.15 * n_f)
            fiber_frames.append((n_f, t1_f, t2_f))

        # =====================================================================
        # TRANSPORT ANIMATION — single continuous animation instead of 50 clips
        # =====================================================================
        N_STEPS     = 50
        total_angle = 1.1
        visited_arrows = VGroup()

        # precompute all frames
        all_arrows = []
        all_bases  = []
        for t in np.linspace(0, 1, N_STEPS):
            u_t, v_t = gamma_uv(t)
            pt_t  = surf_point(u_t, v_t)
            n_t   = surf_normal(u_t, v_t);  n_t = n_t / np.linalg.norm(n_t)
            ref_t = UP if abs(np.dot(n_t, UP)) < 0.85 else RIGHT
            t1_t  = np.cross(n_t, ref_t);  t1_t = t1_t / np.linalg.norm(t1_t)
            t2_t  = np.cross(n_t, t1_t);   t2_t = t2_t / np.linalg.norm(t2_t)

            angle_t   = total_angle * (t ** 1.5)
            direction = np.cos(angle_t) * t1_t + np.sin(angle_t) * t2_t

            base_t = pt_t + 0.15 * n_t
            tip_t  = base_t + ARROW_LENGTH * direction

            all_arrows.append(make_fiber_arrow(
                base_t, tip_t, t1_t, t2_t,
                color=ARROW_COLOR, shaft_width=3.0, tip_size=0.08,
            ))
            all_bases.append((base_t, n_t))

        # place trail arrows at fiber centers
        placed_fiber_indices = set()
        for i, t in enumerate(np.linspace(0, 1, N_STEPS)):
            base_t = all_bases[i][0]
            dists = [np.linalg.norm(base_t - fb) for fb in fiber_bases]
            nearest_idx = int(np.argmin(dists))
            if nearest_idx not in placed_fiber_indices and dists[nearest_idx] < 0.25:
                placed_fiber_indices.add(nearest_idx)
                n_f, t1_f, t2_f = fiber_frames[nearest_idx]
                trail_base = fiber_bases[nearest_idx]
                direction_i = (all_arrows[i][1].get_vertices()[0]
                               - fiber_bases[nearest_idx])  # reuse direction
                # recompute direction cleanly
                t    = np.linspace(0, 1, N_STEPS)[i]
                u_t, v_t = gamma_uv(t)
                n_t  = surf_normal(u_t, v_t); n_t = n_t / np.linalg.norm(n_t)
                ref_t = UP if abs(np.dot(n_t, UP)) < 0.85 else RIGHT
                t1_t  = np.cross(n_t, ref_t);  t1_t = t1_t / np.linalg.norm(t1_t)
                t2_t  = np.cross(n_t, t1_t);   t2_t = t2_t / np.linalg.norm(t2_t)
                angle_t   = total_angle * (t ** 1.5)
                direction = np.cos(angle_t) * t1_t + np.sin(angle_t) * t2_t
                trail_tip  = trail_base + ARROW_LENGTH * direction
                trail = make_fiber_arrow(
                    trail_base, trail_tip, t1_f, t2_f,
                    color=ARROW_COLOR, shaft_width=1.5, tip_size=0.06,
                )
                trail.set_opacity(0.45)
                visited_arrows.add(trail)

        # single animation — one clip instead of 50
        def update_arrow(mob, alpha):
            idx = min(int(alpha * (N_STEPS - 1)), N_STEPS - 1)
            mob.become(all_arrows[idx])
            base_t, n_t = all_bases[idx]
            transport_label.move_to(base_t + 0.5 * n_t)
            # reveal trail arrows up to current position
            for j, trail in enumerate(visited_arrows):
                trail_t = list(placed_fiber_indices)[j] / N_bundle
                trail.set_opacity(0.45 if alpha >= trail_t else 0.0)

        self.play(
            UpdateFromAlphaFunc(moving_arrow, update_arrow),
            run_time=3.0,
            rate_func=linear,
        )
        self.add(visited_arrows)

        transport_label.set_color(WHITE)
        self.wait(1)
        self.next_slide()
        
       
        # now zoom in to the manifold and 2 nearby points, say that there, the infinitesimal change is what we call covariant derivative
        # self.next_slide()
        # # step 8: final caption
        # mapping_caption = Tex(
        #     r"The connection transports $\psi(\gamma(0))$ "
        #     r"to $E_{\gamma(t)}$ along $\gamma$.",
        #     font_size=22,
        # ).next_to(title, 2*DOWN, aligned_edge=LEFT, buff=0.5)
        # self.add_fixed_in_frame_mobjects(mapping_caption)
        # self.play(FadeIn(mapping_caption))
        # self.next_slide()

        # # =====================================================================
        # # CLEAR — transition to next beat
        # # =====================================================================
        # self.play(
        #     FadeOut(moving_arrow), FadeOut(transport_label),
        #     FadeOut(mapping_caption),
        #     FadeOut(curve), FadeOut(dot_start), FadeOut(dot_end),
        #     FadeOut(fibersCurve),
        #     FadeOut(surface), FadeOut(label_M),
        # )
        # self.next_slide()

        # # =====================================================================
        # # BEAT 2 — CONNECTIONS & COVARIANT DERIVATIVE  (2-D, flat camera)
        # # =====================================================================
        # self.move_camera(phi=0*DEGREES, theta=-90*DEGREES, zoom=1.0, run_time=1.2)

        # new_title = Tex(r"Connections \& parallel transport",
        #                 font_size=30).to_corner(UL)
        # self.add_fixed_in_frame_mobjects(new_title)
        # self.play(Transform(title, new_title))
        # self.next_slide()

        # question = Tex(
        #     r"How do we compare vectors in different fibers?",
        #     font_size=24,
        # ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        # self.add_fixed_in_frame_mobjects(question)
        # self.play(FadeIn(question))
        # self.next_slide()

        # answer = Tex(
        #     r"A \textit{connection} $\nabla$ specifies how to \textit{slide} "
        #     r"vectors between fibers along a curve.",
        #     font_size=24,
        # ).next_to(question, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.add_fixed_in_frame_mobjects(answer)
        # self.play(FadeIn(answer))
        # self.next_slide()

        # cov_intro = Tex(
        #     r"Infinitesimally: the \textit{covariant derivative} $\nabla_X \psi$ "
        #     r"measures how a section changes in direction $X$.",
        #     font_size=24,
        # ).next_to(answer, DOWN, aligned_edge=LEFT, buff=0.35)
        # self.add_fixed_in_frame_mobjects(cov_intro)
        # self.play(FadeIn(cov_intro))
        # self.next_slide()

        # frame_intro = Tex(r"In a local frame:", font_size=24
        #                   ).next_to(cov_intro, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.add_fixed_in_frame_mobjects(frame_intro)
        # self.play(FadeIn(frame_intro))

        # frame_formula = MathTex(
        #     r"\nabla_X \psi \;=\; "
        #     r"\underbrace{d_X \psi}_{\text{change in components}}"
        #     r"\;+\; \underbrace{\omega(X)\,\psi}_{\text{frame rotation}}",
        #     font_size=26,
        # ).next_to(frame_intro, DOWN, aligned_edge=LEFT, buff=0.25)
        # self.add_fixed_in_frame_mobjects(frame_formula)
        # self.play(FadeIn(frame_formula))
        # self.next_slide()

        # omega_lie = Tex(
        #     r"$\omega(X)$ is a Lie algebra element: an infinitesimal rotation matrix.",
        #     font_size=22,
        # ).next_to(frame_formula, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.add_fixed_in_frame_mobjects(omega_lie)
        # self.play(FadeIn(omega_lie))
        # self.next_slide()

        # omega_label = Tex(
        #     r"We call $\omega \in \Omega^1(M,\,\mathfrak{gl}(E))$ "
        #     r"the \textit{connection 1-form}.",
        #     font_size=22, color=YELLOW,
        # ).next_to(omega_lie, DOWN, aligned_edge=LEFT, buff=0.2)
        # self.add_fixed_in_frame_mobjects(omega_label)
        # self.play(FadeIn(omega_label))
        # self.next_slide()

        # # =====================================================================
        # # BEAT 2d — METRIC CONNECTIONS: ω SKEW-SYMMETRIC, ONE COMPONENT
        # # =====================================================================
        # self.play(
        #     FadeOut(question), FadeOut(answer),
        #     FadeOut(cov_intro), FadeOut(frame_intro),
        # )
        # self.next_slide()

        # omega_general = MathTex(
        #     r"\omega(X) \;=\; "
        #     r"\begin{pmatrix} \omega^1{}_1(X) & \omega^1{}_2(X) \\"
        #     r"\omega^2{}_1(X) & \omega^2{}_2(X) \end{pmatrix}",
        #     font_size=24,
        # ).next_to(frame_formula, DOWN, aligned_edge=LEFT, buff=0.4)
        # self.add_fixed_in_frame_mobjects(omega_general)
        # self.play(FadeOut(omega_lie), FadeOut(omega_label), FadeIn(omega_general))
        # self.next_slide()

        # metric_note = Tex(
        #     r"We focus on \textit{metric-compatible} connections: "
        #     r"parallel transport preserves lengths "
        #     r"$\;\Rightarrow\;$ $\omega$ is \textit{skew-symmetric}.",
        #     font_size=22,
        # ).next_to(omega_general, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.add_fixed_in_frame_mobjects(metric_note)
        # self.play(FadeIn(metric_note))
        # self.next_slide()

        # omega_skew = MathTex(
        #     r"\omega(X) \;=\; "
        #     r"\begin{pmatrix} 0 & -\alpha(X) \\ \alpha(X) & 0 \end{pmatrix}"
        #     r"\;=\; J\alpha(X)",
        #     font_size=24,
        # ).next_to(frame_formula, DOWN, aligned_edge=LEFT, buff=0.4)
        # self.add_fixed_in_frame_mobjects(omega_skew)
        # self.play(Transform(omega_general, omega_skew))
        # self.next_slide()

        # surface_note = Tex(
        #     r"On a surface: \textit{one scalar 1-form} $\alpha \in \Omega^1(M)$ "
        #     r"encodes the entire metric connection.",
        #     font_size=22, color=YELLOW,
        # ).next_to(omega_skew, DOWN, aligned_edge=LEFT, buff=0.3)
        # self.add_fixed_in_frame_mobjects(surface_note)
        # self.play(FadeIn(surface_note))
        # self.next_slide()

        # # 2-D frame field placeholder
        # surf_center = RIGHT * 3.5 + DOWN * 0.4
        # surf_pts = [
        #     np.array([surf_center[0] + (i-2)*0.85,
        #               surf_center[1] + (j-1)*0.85, 0])
        #     for i in range(4) for j in range(3)
        # ]
        # surf_frames = VGroup(*[
        #     make_frame(pt, angle=0.12*k, scale=0.32)
        #     for k, pt in enumerate(surf_pts)
        # ])
        # surf_dots   = VGroup(*[Dot(pt, radius=0.04, color=GRAY) for pt in surf_pts])
        # alpha_label = Tex(
        #     r"$\alpha$: one rotation angle per tangent direction",
        #     font_size=18, color=YELLOW,
        # ).next_to(surf_frames, DOWN, buff=0.15)

        # self.play(FadeIn(surf_dots))
        # self.play(LaggedStart(*[FadeIn(f) for f in surf_frames], lag_ratio=0.04))
        # self.play(FadeIn(alpha_label))
        # self.next_slide()

        # # =====================================================================
        # # BEAT 2e — CURVATURE
        # # =====================================================================
        # curv_title = Tex(r"Connections \& curvature", font_size=30).to_corner(UL)
        # self.add_fixed_in_frame_mobjects(curv_title)
        # self.play(
        #     FadeOut(frame_formula), FadeOut(omega_general),
        #     FadeOut(metric_note), FadeOut(surface_note),
        #     FadeOut(surf_dots), FadeOut(surf_frames), FadeOut(alpha_label),
        #     Transform(title, curv_title),
        # )
        # self.next_slide()

        # curv_question = Tex(
        #     r"What if $\mathcal{R}_\gamma$ depends on the path, not just the endpoints?",
        #     font_size=24,
        # ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.5)
        # self.add_fixed_in_frame_mobjects(curv_question)
        # self.play(FadeIn(curv_question))
        # self.next_slide()

        # loop_center = RIGHT * 2.5 + DOWN * 0.5
        # loop = Circle(radius=1.1, color=WHITE, stroke_width=2).move_to(loop_center)
        # loop_frames = VGroup(*[
        #     make_frame(
        #         loop_center + 1.1*np.array([np.cos(k*2*PI/8),
        #                                     np.sin(k*2*PI/8), 0]),
        #         angle=0.55*k*2*PI/8, scale=0.3,
        #     ) for k in range(8)
        # ])
        # frame_start = make_frame(loop_center+RIGHT*1.1, angle=0.0,
        #                          scale=0.38, color1=GREEN, color2=BLUE)
        # frame_end   = make_frame(loop_center+RIGHT*1.1, angle=0.55*2*PI,
        #                          scale=0.38, color1=RED,   color2=ORANGE)
        # holonomy_label = Tex(
        #     r"\textit{holonomy}: frame returns rotated",
        #     font_size=20, color=YELLOW,
        # ).next_to(loop, DOWN, buff=0.2)

        # self.play(Create(loop))
        # self.play(LaggedStart(*[FadeIn(f) for f in loop_frames], lag_ratio=0.1))
        # self.play(FadeIn(frame_start), FadeIn(frame_end), FadeIn(holonomy_label))
        # self.next_slide()

        # holonomy_caption = Tex(
        #     r"Parallel-transporting a vector around a loop returns it \textit{rotated}.",
        #     font_size=22,
        # ).next_to(curv_question, DOWN, aligned_edge=LEFT, buff=0.4)
        # self.add_fixed_in_frame_mobjects(holonomy_caption)
        # self.play(FadeIn(holonomy_caption))
        # self.next_slide()

        # curvature_formula = MathTex(
        #     r"\Omega^\nabla \;=\; d\omega + \omega \wedge \omega", font_size=28,
        # ).next_to(holonomy_caption, DOWN, aligned_edge=LEFT, buff=0.4)
        # curvature_caption = Tex(
        #     r"$\Omega^\nabla$ is the \textit{curvature 2-form}: "
        #     r"measures infinitesimal holonomy.",
        #     font_size=22, color=YELLOW,
        # ).next_to(curvature_formula, DOWN, aligned_edge=LEFT, buff=0.2)
        # self.add_fixed_in_frame_mobjects(curvature_formula, curvature_caption)
        # self.play(FadeIn(curvature_formula), FadeIn(curvature_caption))
        # self.next_slide()

        # # =====================================================================
        # # CLEAR — transition to BEAT 3
        # # =====================================================================
        # titleBundleValued = Tex(r"Bundle valued forms", font_size=30).to_corner(UL)
        # self.add_fixed_in_frame_mobjects(titleBundleValued)
        # self.play(
        #     FadeOut(curv_question), FadeOut(holonomy_caption),
        #     FadeOut(curvature_formula), FadeOut(curvature_caption),
        #     FadeOut(loop), FadeOut(loop_frames),
        #     FadeOut(frame_start), FadeOut(frame_end), FadeOut(holonomy_label),
        #     FadeOut(title),
        #     FadeIn(titleBundleValued),
        # )
        # self.wait()
        # self.next_slide()

        # # =====================================================================
        # # BEAT 3 — BUNDLE-VALUED FORMS
        # # =====================================================================
        # textFormally = Tex(
        #     r"Formally, bundle-valued $k$-forms are "
        #     r"$\Omega^k(M,E) = \Omega^k(M) \otimes E$.",
        #     font_size=24,
        # ).next_to(titleBundleValued, DOWN, aligned_edge=LEFT, buff=0.4)
        # self.add_fixed_in_frame_mobjects(textFormally)
        # self.play(FadeIn(textFormally))
        # self.next_slide()

        # scalar_img      = ImageMobject("figures/two_forms_scalar_valued.png").scale(0.85)
        # bundle_form_img = ImageMobject("figures/two_forms_bundle_valued.png").scale(0.85)
        # scalar_img.shift(LEFT * 3 + DOWN * 0.5)
        # bundle_form_img.shift(RIGHT * 1.5 + DOWN * 0.5)

        # scalar_label      = Tex(r"scalar 2-form: returns a \textit{number}",
        #                         font_size=24).next_to(scalar_img,      UP, buff=0.2)
        # bundle_form_label = Tex(r"bundle-valued 2-form: returns a \textit{vector}",
        #                         font_size=24).next_to(bundle_form_img, UP, buff=0.2)

        # self.play(FadeIn(scalar_img), FadeIn(scalar_label))
        # self.next_slide()
        # self.play(FadeIn(bundle_form_img), FadeIn(bundle_form_label))
        # self.next_slide()

        # transition = Tex(
        #     r"To differentiate them we need the "
        #     r"covariant exterior derivative $d^{\nabla}$.",
        #     font_size=24,
        # ).to_corner(DL).shift(UP * 0.3 + RIGHT * 0.3)
        # self.add_fixed_in_frame_mobjects(transition)
        # self.play(FadeIn(transition))
        # self.wait()
        # self.next_slide()
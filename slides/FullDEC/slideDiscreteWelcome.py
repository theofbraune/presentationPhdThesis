from manim import *
from manim_slides import Slide, ThreeDSlide
import utils.preamble as preamble
import numpy as np
from utils.videoLoop import *


# ─────────────────────────────────────────────────────────────────────────────
# Surface helpers
# ─────────────────────────────────────────────────────────────────────────────
SURF_SCALE = 0.38
# SURF_SHIFT  = RIGHT * 2.5 + DOWN * 0.5   # right side of screen
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
    offset = 0.15 * normal
    c = base_pt + offset
    s = size / 2
    corners = [
        c + s*t1 + s*t2, c - s*t1 + s*t2,
        c - s*t1 - s*t2, c + s*t1 - s*t2,
    ]
    face = Polygon(*corners, fill_color=color, fill_opacity=opacity,
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
    unit = direction / length
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


class slideDiscreteBundle(Slide):
    def construct(self):
        title = Tex(r"Discrete Vector Bundles", font_size=30).to_corner(UL)
        self.play(FadeIn(title))
        self.next_slide()

        # self.set_camera_orientation(phi=55*DEGREES, theta=160*DEGREES, zoom=1.05)

        # =====================================================================
        # BEAT 1 — smooth surface + continuous fiber bundle
        # =====================================================================
        textMesh = Tex(
            r"Recall: Smooth vector bundle $E \to \mathcal{M}$.",
            font_size=24,
        ).next_to(title, DOWN, aligned_edge=LEFT, buff=0.4)
        self.play(FadeIn(textMesh))

        heightImage = 3.5
        position = ORIGIN + 2.5*RIGHT + UP * 0.5
        imageBaseManifold = ImageMobject("figures/discreteFormsAndCurvature/baseManifold.png" )
        imageBaseManifold.set_height(heightImage)
        imageBaseManifold.move_to(position)
        self.play(FadeIn(imageBaseManifold), run_time=1.0)
        self.wait()
        self.next_slide()
        position = imageBaseManifold.get_center()
        imageBundleSmooth = ImageMobject("figures/discreteFormsAndCurvature/baseManifoldWithBundle.png")
        imageBundleSmooth.set_height(heightImage)
        imageBundleSmooth.move_to(position)
        self.play(Transform(imageBaseManifold, imageBundleSmooth), run_time=1.0)

        # =====================================================================
        # BEAT 2 — fade out bundle, tessellate into triangles
        # =====================================================================
        textDiscrete = Tex(
            r"Approximate $\mathcal{M}$ by a simplicial mesh $M$.",
            font_size=24,
        ).next_to(textMesh, 2*DOWN, aligned_edge=LEFT, buff=0.35)
        self.play(FadeIn(textDiscrete))
        imageDiscreteManifold = ImageMobject("figures/discreteFormsAndCurvature/DiscreteManifoldWithBundle.png")
        imageDiscreteManifold.set_height(heightImage)
        imageDiscreteManifold.move_to(position)
        textFiber = Tex(
            r" \textit{Discrete vector bundle}: "
            r"one fiber $E_v \cong \mathbb{R}^r$ per vertex $v$.",
            font_size=24,
        ).next_to(textDiscrete, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textFiber), Transform(imageBaseManifold, imageDiscreteManifold), run_time=1.0)
        self.wait()
        self.next_slide()
        # now zoom in on on the triangle
        firstVideoSeq = play_video_loop(
            self,
            frame_dir = "figures/discreteFormsAndCurvature/render_par/croppedOut/",
            position = position,
            height = heightImage,
            fps = 20,
            fade_in_time = 0.5,
            fade_out_time = 0.5,
            persist = True        
        )
        self.remove(imageBaseManifold)
        self.remove(imageDiscreteManifold)
        imageCover = ImageMobject("figures/discreteFormsAndCurvature/DiscreteManifoldWithBundleZoom.png")
        imageCover.set_height(heightImage)
        imageCover.move_to(position)
        self.add(imageCover)
        self.remove(firstVideoSeq)
        textDiscreteConn = Tex(
            r" \textit{Discrete connection}: "
            r"parallel transport $R_{v_0,v_1}$ per edge $(v_0,v_1)$ ", font_size = 24
        ).next_to(textFiber, 2*DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(FadeIn(textDiscreteConn), run_time=0.8)
        self.wait()
        imageConnFirst = ImageMobject("figures/discreteFormsAndCurvature/discreteConn/discreteConn1.png")
        imageConnFirst.set_height(heightImage)
        imageConnFirst.move_to(position)
        # self.play(Transform(imageCover, imageConnFirst), run_time=0.4)
        self.play(FadeOut(imageCover), FadeIn(imageConnFirst), run_time=0.4)
        self.wait()
        self.next_slide()
        imageConnSecond = ImageMobject("figures/discreteFormsAndCurvature/discreteConn/discreteConn2.png")
        imageConnSecond.set_height(heightImage)
        imageConnSecond.move_to(position)
        # self.play(Transform(imageCover, imageConnSecond), run_time=0.4)
        self.play(Transform(imageConnFirst, imageConnSecond), run_time=0.4)
        self.wait()
        self.next_slide()
        imageConnThird = ImageMobject("figures/discreteFormsAndCurvature/discreteConn/discreteConn3.png")
        imageConnThird.set_height(heightImage)
        imageConnThird.move_to(position)
        # self.play(Transform(imageCover, imageConnThird), run_time=0.4)
        self.play(Transform(imageConnSecond, imageConnThird), run_time=0.4)
        self.wait()
        self.next_slide()
        imageConnFourth = ImageMobject("figures/discreteFormsAndCurvature/discreteConn/discreteConn4.png")
        imageConnFourth.set_height(heightImage)
        imageConnFourth.move_to(position)
        # self.play(Transform(imageCover, imageConnFourth), run_time=0.4)
        self.play(Transform(imageConnThird, imageConnFourth), run_time=0.4)
        self.wait()
        self.next_slide()

        # fade out the smooth fibers
        # self.play(
        #     FadeOut(fiber_group_smooth),
        #     FadeIn(textDiscrete),
        #     run_time=0.8,
        # )

        # coarse surface — low resolution, will become the mesh
        # surface_coarse = Surface(
        #     lambda u, v: surf_point(u, v),
        #     u_range=[-5, 5], v_range=[-5, 5],
        #     resolution=(5, 5),
        #     fill_color="#1B4D5C", fill_opacity=0.85,
        #     stroke_color="#000000", stroke_width=0.0,
        # )

        

        """
        # build triangulated mesh edges explicitly
        # sample a coarse grid and triangulate each quad into 2 triangles
        N_MESH = 6
        us_mesh = np.linspace(-5, 5, N_MESH)
        vs_mesh = np.linspace(-5, 5, N_MESH)

        mesh_edges = VGroup()
        mesh_vertices = []
        for i, u in enumerate(us_mesh):
            for j, v in enumerate(vs_mesh):
                mesh_vertices.append((i, j, surf_point(u, v)))

        def get_pt(i, j):
            u = us_mesh[i]
            v = vs_mesh[j]
            return surf_point(u, v)

        for i in range(N_MESH - 1):
            for j in range(N_MESH - 1):
                p00 = get_pt(i,   j)
                p10 = get_pt(i+1, j)
                p01 = get_pt(i,   j+1)
                p11 = get_pt(i+1, j+1)
                # lower triangle: p00 - p10 - p11
                mesh_edges.add(Line(p00, p10, color=ORANGE, stroke_width=5))
                mesh_edges.add(Line(p10, p11, color=ORANGE, stroke_width=5))
                mesh_edges.add(Line(p11, p00, color=ORANGE, stroke_width=5))
                # upper triangle: p00 - p01 - p11
                mesh_edges.add(Line(p00, p01, color=ORANGE, stroke_width=5))
                mesh_edges.add(Line(p01, p11, color=ORANGE, stroke_width=5))
                # diagonal already drawn as p11-p00 above

        # swap smooth surface for coarse, draw thick black edges
        # self.play(
        #     Transform(surface_smooth, surface_coarse),
        #     run_time=0.8,
        # )
        self.play(
            LaggedStart(*[Create(e) for e in mesh_edges], lag_ratio=0.01),
            run_time=1.5,
        )
        self.next_slide()

        # =====================================================================
        # BEAT 3 — one fiber per vertex
        # =====================================================================
        textFiber = Tex(
            r"$\bullet$ \textit{Discrete vector bundle}: "
            r"one fiber $E_v \cong \mathbb{R}^r$ per vertex $v$.",
            font_size=24,
        ).next_to(textDiscrete, DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(textFiber)
        self.play(FadeIn(textFiber))

        # fiber squares only at mesh vertices
        fiber_group_discrete = VGroup()
        vertex_dots = VGroup()
        for i, u in enumerate(us_mesh):
            for j, v in enumerate(vs_mesh):
                pt = surf_point(u, v)
                n  = surf_normal(u, v)
                fiber_group_discrete.add(
                    make_fiber_square(pt, n, size=0.28,
                                      color="#FFD166", opacity=0.80)
                )
                vertex_dots.add(Dot3D(pt, radius=0.05, color=WHITE))

        self.play(FadeIn(vertex_dots), run_time=0.5)
        self.play(
            LaggedStart(*[FadeIn(f) for f in fiber_group_discrete], lag_ratio=0.03),
            run_time=1.5,
        )
        self.next_slide()

        # =====================================================================
        # BEAT 4 — one parallel transport per edge
        # =====================================================================
        textConn = Tex(
            r"$\bullet$ \textit{Discrete connection}: "
            r"one parallel transport map $R_{ij}$ per edge $e_{ij}$.",
            font_size=24,
        ).next_to(textFiber, DOWN, aligned_edge=LEFT, buff=0.3)
        self.add_fixed_in_frame_mobjects(textConn)
        self.play(FadeIn(textConn))

        # highlight a few edges with colored transport arrows between fibers
        edge_transport = VGroup()
        highlight_edges = [
            (2, 2, 3, 2),
            (2, 2, 2, 3),
            (3, 3, 4, 3),
        ]
        for i0, j0, i1, j1 in highlight_edges:
            u0_e, v0_e = us_mesh[i0], vs_mesh[j0]
            u1_e, v1_e = us_mesh[i1], vs_mesh[j1]
            p0_e = surf_point(u0_e, v0_e)
            p1_e = surf_point(u1_e, v1_e)
            n0_e = surf_normal(u0_e, v0_e); n0_e = n0_e / np.linalg.norm(n0_e)
            n1_e = surf_normal(u1_e, v1_e); n1_e = n1_e / np.linalg.norm(n1_e)

            # curved arrow from fiber at v0 to fiber at v1
            mid = 0.5 * (p0_e + p1_e) + 0.3 * surf_normal(
                (u0_e + u1_e) / 2, (v0_e + v1_e) / 2)
            arc = CurvedArrow(
                p0_e + 0.2 * n0_e,
                p1_e + 0.2 * n1_e,
                color=ORANGE, stroke_width=3,
                angle=TAU / 6,
            )
            edge_transport.add(arc)

        # label one edge
        R_label = MathTex(r"R_{ij}", font_size=22, color=ORANGE)
        mid_edge = 0.5 * (surf_point(us_mesh[2], vs_mesh[2]) +
                          surf_point(us_mesh[3], vs_mesh[2]))
        R_label.move_to(mid_edge + 0.5 * surf_normal(
            (us_mesh[2]+us_mesh[3])/2, vs_mesh[2]))
        self.add_fixed_orientation_mobjects(R_label)

        self.play(
            LaggedStart(*[Create(e) for e in edge_transport], lag_ratio=0.2),
            FadeIn(R_label),
            run_time=1.2,
        )
        self.next_slide()
        """

       




# next, how to differentiate discrete bundle valued forms.
# show how, say almost like in DEC, show that this was presented by Hirani. Explain that it has the advantage, that the differential bianchi, just exactly zero

# just say roughly what was the idea to check it, with the solder form. Integrate it per edge, plug it into the formula, evaluate against the smooth expression
# then show the convergence plot, nope.....


# Explain the issue: Look at the smooth setting, there is d term and something that is not d, omega wedge term 

# this term is there.... Scary. You cannot get rid of it, but can we make it at least small? Turns out yess. 

# This expression, super dependant of the frame -> put it a bit under the rug 

# now consider the following: 

# Imagine you take a simplex, that you can embed in a smooth manifold. Now pick one point in the embedded domain, do a retraction on this point. For all points on the boundary, trace the retraction paths. Visualize that! 
# then from this source point, take the retraction paths and sample fibers over the paths. 

# Then, next show the key insight. Take a frame at the origin, parallel transport it along the paths. 
 
# Now, imagine you parallel transport a vector along the ray. Express it in this coordinate system... maybe even write on the screen coordinates, later, it is exactly the same. 
# R = Identity, omega = log(Identity) = 0.... The ground rule of calculus, something is zero at a point, then it is small around it. 

# This frame -> parallel propagated frame.

# If we integrate the forms in this frame, then the omega term is small, and we get convergence. -> show the convergence plot and the screenshot from the theorem in the paper. 

# Are we done? Nope... Lets look at the algebraic bianchi identity. Apply it twice. Show that for the smooth formula, there are 3 terms, but we have only one. Also show the convergence plot for the bianchi identity.... not decaying.

# Idea: problem is, it is biased towards one corner, lets try to leverage this -> hit it with a symmetry operation.-> Alternation operator. 

# Now, we could show that indeed, if you compare this to the smooth formula, we get a faster convergence. -> Also possible for endomorphism valued forms.
# explain, that this formula is up to one order higher the same as a "center based PPF". (See how much time we have, if there is enough time, would be nice to give an analogy with quadrature.)


# this is the key result-> with this result in place we could indeed show that also 2 applications of the discrete exterior covariant exterior converge under refinement, meaning the discrete exterior calculus of bundle valued forms is structure preserving :) 

# Note, we could show that this can be extended to the cellular forms. Key idea-> convert corner based evaluations to center of mass based evaluations... means the symmetrization needs to be weigted based on the generalized barycentric coordinates of the center of mass. 
# Works as well for endomorphism valued forms. 

# Conclusion: We present here a general framework for discrete bundle valued exterior calculus . 
# We show that the discretization is structure preserving.
# It is a ready to use framework for applications that are based on discrete bundle valued exterior calculus, such as nonlinear elasticity, gauge theories, compressible fluids, general relativity, ... and many more. 
# 
#  i.e the point that is the average of all points in the cell. Then, do a corner based evaluation
# Further, we still have the combinatorial properties right, discretely we have the same algebraic bianchi identity, now a combi

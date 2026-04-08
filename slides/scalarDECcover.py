
from manim import *
from manim_slides import Slide
import utils.preamble as preamble


class ScalarDEC_cover(Slide):
    def construct(self):
        title = Tex("Scalar Valued (Discrete) Exterior Calculus", color=WHITE).scale(1.5)
        title.to_edge(UP)  # Position the text at the top of the frame
        self.add(title)
        
        self.wait()
        self.next_slide()


        formula_stokes = MathTex(r"\int_{M} d\alpha = \int_{\partial M}\alpha").to_edge(LEFT).scale(0.8)

        background_image = ImageMobject("figures/Elie_Cartan.jpg").to_edge(RIGHT)

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
        faces_for_cell = []
        shared_edges = []
        for j in range(len(faces)):
            face_indices = faces[j]
            polygon_points = [points[i] for i in face_indices]
            polygon = Polygon(*polygon_points, color=BLUE, fill_opacity=0.1)
            polygons.add(polygon)
            if(j==0 or j==9):
                faces_for_cell.append(polygon)

        fleche0 = Arrow(p0,p1,buff=0.6,color=RED,tip_length=0.1).shift([0,0.1,0]).set_opacity(1.).scale(0.8)
        fleche1 = Arrow(p1,p2,buff=0.6,color=RED,tip_length=0.1).shift([-0.1,0.,0]).set_opacity(1.).scale(0.8)
        fleche2 = Arrow(p2,p3,buff=0.6,color=RED,tip_length=0.1).shift([0,-0.1,0]).set_opacity(1.).scale(0.8)
        fleche3 = Arrow(p3,p4,buff=0.6,color=RED,tip_length=0.1).shift([0,-0.1,0]).set_opacity(1.).scale(0.8)
        fleche4 = Arrow(p4,p0,color=RED,tip_length=0.1).shift([0.1,0.0,0]).set_opacity(0.8)

        polygons.add(fleche0,fleche1,fleche2,fleche3,fleche4)   


        fleche5 = Arrow(p16,p0,color=RED,tip_length=0.1).shift([0,0.1,0]).set_opacity(0.8)
        fleche6 = Arrow(p0,p4,color=RED,tip_length=0.1).shift([-0.1,0.,0]).set_opacity(0.8)
        fleche7 = Arrow(p4,p16,color=RED,tip_length=0.1).shift([0,-0.1,0]).set_opacity(0.8)
        
        polygons.add(fleche5,fleche6,fleche7)
        
        polygons.scale(1.5)
        # polygons.to_edge(RIGHT)
        for fc in faces_for_cell:
            fc.set_opacity(0.4)

        self.add(background_image,formula_stokes,polygons)
        # self.play(FadeIn())
        self.wait()
        self.next_slide()
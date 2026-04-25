
from manim import *
from manim_slides import Slide, ThreeDSlide


class slideTeaserBundle(ThreeDSlide):
    #bundle valued forms and stress 
    def construct(self):

        title_text = Tex("Vector Valued Forms",font_size=30).to_corner(UL)
        self.play(FadeIn(title_text))
        self.wait()
        self.next_slide()
        text_intro = Tex(" \\text{DEC describes \\textit{scalar} valued differential forms discretely  in a structure preserving way.}", font_size=25).to_corner(UL).shift(DOWN)
        self.play(FadeIn(text_intro))

        self.wait()
        self.next_slide()
        text_vector  = Tex(" Cartans original work also deals with \\textit{vector valued differential forms}.",font_size=25).next_to(text_intro,1.2*DOWN,aligned_edge=LEFT)
        self.play(FadeIn(text_vector))
        self.wait()
        self.next_slide()
        
        text_elastic = Tex(" \\text{Lets take a look at vector valued forms. Consider the following elastic body:}", font_size=25).next_to(title_text,1.5*DOWN,aligned_edge=LEFT)
        # video = VideoMobject("figures/bundle_valued_stress/elastic_body.mp4").scale(0.7).to_edge(DOWN)
        
        #self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES) # 3D view        
        self.play(FadeOut(text_intro,text_vector),FadeIn(text_elastic))
        self.wait()
        self.next_slide()


        # Constants for geometry and drawing adjustment
        stretched_width = 3.0
        stretched_height = 1.6
        stretched_depth = 1.6
        half_x_length = stretched_width / 2.0 # 1.5
        
        epsilon = 0.005 
        initial_vector_length = 1.0 

        self.play(FadeOut(text_elastic,title_text))

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        axes_3d = ThreeDAxes(
            # unit_size=1 in Z axis
            z_range=(-3,3,1),
            z_length=3.5,
        )
        self.add_fixed_in_frame_mobjects(title_text)
        
        # --- MODIFIED: Use Cube and scale to achieve Cuboid shape ---
        
        # 1. Full Body (3.0 x 1.6 x 1.6) - Used for the Transform source
        # Start with a 1x1x1 cube and scale it to the required dimensions
        full_body = Cube(
            side_length=1,
            fill_opacity=0.3, color=BLUE, 
            stroke_color=BLACK, stroke_width=3
        ).scale((stretched_width, stretched_height, stretched_depth)) 

        initial_body = Cube(
            side_length=1,
            fill_opacity=0.3, color=BLUE, 
            stroke_color=BLACK, stroke_width=3
        ).scale((half_x_length, stretched_height, stretched_depth)) 
        
        # 4. First Half of the Body (1.5 x 1.6 x 1.6) - The target of the transform
        first_half = Cube(
            side_length=1,
            fill_opacity=0.5, color=BLUE, 
            stroke_color=BLACK, stroke_width=3
        ).scale((half_x_length, stretched_height, stretched_depth))
        
        # Shift it to the left side (center of the half is at -0.75)
        first_half.shift(-half_x_length / 2 * RIGHT)
        # --- MODIFIED END ---
        
        # 2. Cutting Plane Setup (Uses the height/depth of the cuboid)
        cut_plane = Square(
            side_length=stretched_height, 
            fill_opacity=1.0, color=RED, stroke_color=RED,
        ).set_depth(0).rotate(90 * DEGREES, axis=Y_AXIS).shift(epsilon * RIGHT) 



        textElasticForce = Tex(" What is the force acting on the surface piece?", font_size=25).next_to(title_text,DOWN,aligned_edge=LEFT)


        self.add(initial_body, axes_3d)
        self.wait(0.5)
        self.play(Transform(initial_body, full_body, run_time=3.0))
        # self.add(full_body, axes_3d)
        self.wait(0.5)
        
        # 3. Animate the Cut and Initial Vector (Slide 1)
        self.next_slide()
        self.play(
            Transform(full_body, first_half, run_time=0.5)
        )
        
        self.play(FadeIn(cut_plane))
        self.wait(0.5)
        self.next_slide()

        self.add_fixed_in_frame_mobjects(textElasticForce)
        self.next_slide()
        self.wait(0.5)



        # textTraction = Tex(" What is the force acting on this surface piece?", font_size=25).next_to(elastic_body,DOWN,aligned_edge=LEFT)

        # Define the single traction vector
        center_of_plane = cut_plane.get_center()
        initial_vector_length = 1.0
        
        traction_vector = Arrow(
            start=center_of_plane, 
            end=center_of_plane + initial_vector_length * RIGHT,
            color=BLACK, stroke_width=5, buff=0
        )
        self.play(FadeIn(traction_vector))
        self.wait()
        
        self.wait()

        # --- SLIDE 2: Rotate 45 degrees, Vector is Half Size ---
        self.next_slide()
        
        rotation_anchor = center_of_plane
        new_vector_length = initial_vector_length / 2.0
        
        self.play(
            cut_plane.animate.rotate(45 * DEGREES, axis=UP, about_point=rotation_anchor),
            run_time=1.5
        )
        self.wait(0.5)

        new_end_point = rotation_anchor + new_vector_length * RIGHT
        
        self.play(
            traction_vector.animate.put_start_and_end_on(
                start=rotation_anchor, 
                end=new_end_point
            ),
            run_time=1.0
        )
        self.wait()

        # --- SLIDE 3: Rotate another 45 degrees (Total 90), Vector Disappears ---
        self.next_slide()
        
        self.play(
            cut_plane.animate.rotate(45 * DEGREES, axis=UP, about_point=rotation_anchor),
            run_time=1.5
        )
        self.wait(0.5)

        # final_end_point = rotation_anchor 

        self.play(
            FadeOut(traction_vector),
            run_time=0.2
        )
        self.wait()

        # Final cleanup
        self.next_slide()
        text_stress_tensor = Tex("\\text{In continuum mechanics this object called the \\textit{stress tensor}.}",font_size=25).next_to(textElasticForce,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(text_stress_tensor)
        self.wait(0.5)
        self.next_slide()
        text_stress_tensor_forms = Tex("\\text{Stress can be introduced as a \\textit{vector valued} differential 2-form. [Kanso et al. 2007]}",font_size=25).next_to(text_stress_tensor,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(text_stress_tensor_forms)
        
        # self.reset_camera_orientation()
        self.wait(0.5)
        self.set_camera_orientation(phi=0, theta=-90*DEGREES)
        self.next_slide()

        """
        # self.play(
        #     FadeOut( cut_plane, full_body)
        # )
        # self.wait()
        # self.play(FadeOut(axes_3d,traction_vector,cut_plane,full_body,initial_body,first_half))
        # self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        

        # 
        # self.play(FadeOut(text_intro,text_vector),FadeIn(text_elastic))
        # self.wait()
        # self.next_slide()
        # elastic_body = ImageMobject("figures/bundle_valued_stress/cube_small.png")
        # elastic_body.to_edge(LEFT)
        # fleche = MathTex("\\longrightarrow").next_to(elastic_body,RIGHT)

        # deformed_body = ImageMobject("figures/bundle_valued_stress/cube_stretching.png").next_to(fleche,RIGHT)

        # self.play(FadeIn(elastic_body,fleche,deformed_body))
        # self.wait()
        # self.next_slide()
        # test_surface =  ImageMobject("figures/bundle_valued_stress/cube_cut_horizontal.png").next_to(fleche,RIGHT)

        # self.play(FadeOut(deformed_body),FadeIn(test_surface))
        # self.wait()
        # self.next_slide()
        # description_force = Tex("\\text{What is the force attacking on this surface piece?}",font_size=25).next_to(elastic_body,DOWN,aligned_edge=LEFT)
        # self.play(FadeIn(description_force))
        # self.wait()
        # self.next_slide()

        # form_horizontal = ImageMobject("figures/bundle_valued_stress/cube_cut_horizontal_stress.png").next_to(fleche,RIGHT)
        # self.play(FadeOut(test_surface),FadeIn(form_horizontal))
        # self.wait()
        # self.next_slide()
        # form_vertical = ImageMobject("figures/bundle_valued_stress/cube_cut_vertical_stress.png").next_to(fleche,RIGHT)
        # self.play(FadeOut(form_horizontal),FadeIn(form_vertical))
        # self.wait()
        # self.next_slide()
        

        # deformed_body = ImageMobject("figures/bundle_valued_stress/cube_deformed.png").next_to(fleche,RIGHT)

        # self.play(FadeOut( form_vertical),FadeIn(deformed_body))
        # self.wait()
        # self.next_slide()
        # test_surface =  ImageMobject("figures/bundle_valued_stress/cube_bending_surface.png").next_to(fleche,RIGHT)

        # self.play(FadeOut(deformed_body),FadeIn(test_surface))
        # self.wait()
        # self.next_slide()

        # form_horizontal = ImageMobject("figures/bundle_valued_stress/cube_bending_surface_stress.png").next_to(fleche,RIGHT)
        # self.play(FadeOut(test_surface),FadeIn(form_horizontal))
        # self.wait()
        # self.next_slide()
        # 
        # self.play(FadeIn(title_text))
        # text_stress_tensor = Tex("\\text{In continuum mechanics this object called the \\textit{stress tensor}.}",font_size=25).next_to(title_text,3*DOWN,aligned_edge=LEFT)
        # self.play(FadeIn(text_stress_tensor))
        # self.wait()
        # self.next_slide()
        # text_stress_tensor_forms = Tex("\\text{Stress can be introduced as a \\textit{vector valued} differential 2-form. [Kanso et al. 2007]}",font_size=25).next_to(text_stress_tensor,DOWN,aligned_edge=LEFT)

        # self.play(FadeIn(text_stress_tensor_forms))
        # self.wait()
        """ 
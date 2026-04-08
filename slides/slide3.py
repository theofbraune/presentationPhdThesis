
from manim import *
from manim_slides import Slide


  
class slide3(Slide):
    def construct(self):
        func = lambda pos: np.sin(0.5*pos[1]) * RIGHT + 0.25*(np.cos(pos[0]) + pos[1]-2) * UP

        # func = lambda pos: (2*pos[1]**2 - (.5*pos[0]))*UP + (2.5*(pos[1]) - (pos[0]))*RIGHT 
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        

        # func = VectorField.scale_func(func, 0.5)
        # self.play(vector_field.animate.become(ArrowVectorField(func)))
        self.wait()

        title_text = Tex("Differential 1-Forms",font_size=30).to_corner(UL)
        text_domain = Rectangle(color=BLACK,height=7,width=7, fill_opacity = 0.85)
        text_domain.next_to(title_text, DOWN).align_to(title_text, LEFT)
        
        

        # Add text domain and title to the scene
        self.add(text_domain, title_text)
        self.next_slide()
        text_vf=Tex(
            'Consider the differential form', font_size=30
        ).next_to(text_domain,UP).shift(0.8*DOWN).scale(0.8)

        formula_form = MathTex('F^\\flat(x,y) = \mathrm{sin}(0.5 x)\ dx +  0.25(\mathrm{cos}(x) + y-2)\ dy ').next_to(text_vf,0.7*DOWN).scale(0.5)

        self.add(text_vf,formula_form)
        self.wait(1)
        self.next_slide()
        description = Tex("The differential form itself can be paired with a curve.",font_size=30).next_to(formula_form,0.7*DOWN).scale(0.8)
        formula_pairing = MathTex('\\langle F^\\flat,\gamma \\rangle = \int_{\gamma} F^\\flat').next_to(description,0.7*DOWN).scale(0.5)
        self.wait()
        
        self.add(description)
        self.play(FadeIn(formula_pairing))

        self.wait()
        self.next_slide()

        # now add the same curve as before. Show that the orientation reversed flips the sign.

        self.next_slide()

        curve = ParametricFunction(lambda t: np.array([6*np.cos(t), 3.5*np.sin(t),  0]), t_range=[-1, 1], color=RED, stroke_width=0.8)
        derivative = lambda t: np.array([ -6*np.sin(t), 3.5*np.cos(t),  0])

        # Add the curve to the scene
        self.add(curve)

        vector_field.set_opacity(0.3)
        self.next_slide()

        # Sample points along the curve
        num_points = 10  # Adjust the number of points as needed
        points = VGroup()
        
        tangent_vectors = VGroup()
        tangent_vectors_shift = VGroup()
        tangent_vectors_flipped_shift = VGroup()
        vf = VGroup()
        vf_shift = VGroup()

        langle_rangle_komma = []

        for t in np.linspace(-1, 1, num_points):

            point = curve.get_point_from_function(t)
            
            dot = Dot(point, color=BLUE)
            dot.radius *=0.2
            points.add(dot)

            tangent = derivative(t)
            tangent/=2*np.linalg.norm(tangent)

            tangent_vector = Arrow(point, point + tangent, color = BLUE,stroke_width=3,buff=0.)
            tangent_vectors.add(tangent_vector)

            komma = MathTex(r",").next_to(point ,0.1*LEFT).set_opacity(0.0)
            self.add(komma)
            

            tangent_vector_shift = Arrow(point - [0.2,0.,0.], point - [0.2,0.,0.] + tangent, color = BLUE,stroke_width=3,buff=0.)
            tangent_vectors_shift.add(tangent_vector_shift)
            tangent_vector_flipped_shift = Arrow(point - [0.2,0.,0.], point - [0.2,0.,0.] - tangent, color = BLUE,stroke_width=3,buff=0.)
            tangent_vectors_flipped_shift.add(tangent_vector_flipped_shift)

            vfield_val = func(point)
            vfield_val/=2*np.linalg.norm(vfield_val)

            vfield = Arrow(point, point + vfield_val, color = GREEN,stroke_width=3,buff=0.)
            vfield_shift = Arrow(point + [0.1,0.,0.], point+ [0.1,0.,0.] + vfield_val, color = GREEN,stroke_width=3,buff=0.)

            vf.add(vfield)
            vf_shift.add(vfield_shift)

            langle = MathTex(r"\langle\ ").next_to(tangent_vector_shift.get_start()-[0.1,0,0],LEFT).set_opacity(0.0)
            rangle = MathTex(r"\rangle\ ").next_to([vfield_shift.get_end()[0]+0.1,vfield_shift.get_start()[1],0],RIGHT).set_opacity(0.0)
            self.add(langle)
            self.add(rangle)
            langle_rangle_komma.append(komma)
            langle_rangle_komma.append(langle)
            langle_rangle_komma.append(rangle)
            
            
        self.play(FadeIn(vf,tangent_vectors))
        self.next_slide()
        self.play(Transform(vf,vf_shift),Transform(tangent_vectors,tangent_vectors_shift))
        for obj in langle_rangle_komma:
            obj.set_opacity(1.)

        self.next_slide()
        d1 = Dot().set_color(ORANGE)
        self.wait()
        self.next_slide()
        self.play(MoveAlongPath(d1, curve), rate_func=linear)
        self.next_slide()
        self.remove(d1)
        self.wait()
        self.next_slide()

        self.next_slide()
        self.wait()
        self.play(Transform(tangent_vectors,tangent_vectors_flipped_shift))
        self.remove(tangent_vectors_shift)
        self.wait()
        self.next_slide()

        curve_rev = ParametricFunction(lambda t: np.array([6*np.cos(-t), 3.5*np.sin(-t),  0]), t_range=[-1, 1], color=RED, stroke_width=0.8)
        self.next_slide()
        d1 = Dot().set_color(ORANGE)
        self.next_slide()
        self.play(MoveAlongPath(d1, curve_rev), rate_func=linear)
        self.next_slide()
        self.remove(d1)
        self.wait()
        self.next_slide()

        description_work = Tex("Reversing the orientation of the curve yields:",font_size=30).next_to(formula_pairing,0.7*DOWN).scale(0.8)
        formula_pairing_flip = MathTex('\\langle F^\\flat,-\gamma \\rangle = - \\langle F^\\flat,\gamma \\rangle').next_to(description_work,0.7*DOWN).scale(0.5)
        self.play(FadeIn(description_work,formula_pairing_flip))

        self.wait()
        self.next_slide()
        description_work_concat = Tex("Concatenation of curve yields:",font_size=30).next_to(formula_pairing_flip,0.7*DOWN).scale(0.8)
        self.play(FadeIn(description_work_concat))

        self.remove(curve,vf,tangent_vectors_shift,tangent_vectors_flipped_shift,tangent_vectors)
        for obj in langle_rangle_komma:
            obj.set_opacity(0.)

        curve1 = ParametricFunction(lambda t: np.array([6*np.cos(t), 3.5*np.sin(t),  0]), t_range=[-1, 0], color=RED, stroke_width=1.2) 
        derivative1 = lambda t: np.array([-6*np.sin(t), 3.5*np.cos(t),  0])

        curve2 = ParametricFunction(lambda t: np.array([6*np.cos(0), 3.5*np.sin(0),  0])*(1-t) + np.array([4, 3.5,  0])*t , t_range=[0, 1], color=BLUE, stroke_width=1.2)
        derivative2 = lambda t: np.array([6*np.cos(0), 3.5*np.sin(0),  0])*(-1) + np.array([4, 3.5,  0])

        self.add(curve1,curve2)
        label_curve1 = MathTex('\gamma_1').next_to(curve1.get_center(),5.5*RIGHT).scale(1.)
        label_curve2 = MathTex('\gamma_2').next_to(curve2.get_center(),4.5*RIGHT).scale(1.)
        self.play(FadeIn(label_curve1,label_curve2))
        self.wait()
        self.next_slide()
        formula_pairing_concat = MathTex('\\langle F^\\flat,\gamma_1 + \gamma_2 \\rangle = \\langle F^\\flat,\gamma_1 \\rangle + \\langle F^\\flat,\gamma_2 \\rangle').next_to(description_work_concat,0.7*DOWN).scale(0.5)
        self.play(FadeIn(formula_pairing_concat))
        self.wait()
        self.next_slide()

        #add the tangent vectors
        t_range0 = np.linspace(-1,-0.2,4)
        t_range1 = np.linspace(0,1,5)
        tangent_vectors = VGroup()
        tangent_vectors_shift = VGroup()
        tangent_vectors_flipped_shift = VGroup()
        vf = VGroup()
        vf_shift = VGroup()

        langle_rangle_komma = []

        for t in t_range0:
        
            point = curve1.get_point_from_function(t)
            
            dot = Dot(point, color=BLUE)
            dot.radius *=0.2
            points.add(dot)

            tangent = derivative1(t)
            tangent/=2*np.linalg.norm(tangent)

            tangent_vector = Arrow(point, point + tangent, color = BLUE,stroke_width=3,buff=0.)
            tangent_vectors.add(tangent_vector)

            komma = MathTex(r",").next_to(point ,0.1*LEFT).set_opacity(0.0)
            self.add(komma)
            

            tangent_vector_shift = Arrow(point - [0.2,0.,0.], point - [0.2,0.,0.] + tangent, color = BLUE,stroke_width=5,buff=0.)
            tangent_vectors_shift.add(tangent_vector_shift)
            tangent_vector_flipped_shift = Arrow(point - [0.2,0.,0.], point - [0.2,0.,0.] - tangent, color = BLUE,stroke_width=3,buff=0.)
            tangent_vectors_flipped_shift.add(tangent_vector_flipped_shift)

            vfield_val = func(point)
            vfield_val/=2*np.linalg.norm(vfield_val)

            vfield = Arrow(point, point + vfield_val, color = GREEN,stroke_width=3,buff=0.)
            vfield_shift = Arrow(point + [0.1,0.,0.], point+ [0.1,0.,0.] + vfield_val, color = GREEN,stroke_width=3,buff=0.)

            vf.add(vfield)
            vf_shift.add(vfield_shift)

            langle = MathTex(r"\langle\ ").next_to(tangent_vector_shift.get_start()-[0.1,0,0],LEFT).set_opacity(0.0)
            rangle = MathTex(r"\rangle\ ").next_to([vfield_shift.get_end()[0]+0.2,vfield_shift.get_start()[1],0],RIGHT).set_opacity(0.0)
            self.add(langle)
            self.add(rangle)
            langle_rangle_komma.append(komma)
            langle_rangle_komma.append(langle)
            langle_rangle_komma.append(rangle)

        for t in t_range1:
        
            point = curve2.get_point_from_function(t)
            
            dot = Dot(point, color=BLUE)
            dot.radius *=0.2
            points.add(dot)

            tangent = derivative2(t)
            tangent/=2*np.linalg.norm(tangent)

            tangent_vector = Arrow(point, point + tangent, color = BLUE,stroke_width=5,buff=0.)
            tangent_vectors.add(tangent_vector)

            komma = MathTex(r",").next_to(point ,0.1*LEFT).set_opacity(0.0)
            self.add(komma)
            

            tangent_vector_shift = Arrow(point - [0.2,0.,0.], point - [0.2,0.,0.] + tangent, color = BLUE,stroke_width=5,buff=0.)
            tangent_vectors_shift.add(tangent_vector_shift)
            tangent_vector_flipped_shift = Arrow(point - [0.2,0.,0.], point - [0.2,0.,0.] - tangent, color = BLUE,stroke_width=3,buff=0.)
            tangent_vectors_flipped_shift.add(tangent_vector_flipped_shift)

            vfield_val = func(point)
            vfield_val/=2*np.linalg.norm(vfield_val)

            vfield = Arrow(point, point + vfield_val, color = GREEN,stroke_width=3,buff=0.)
            vfield_shift = Arrow(point + [0.1,0.,0.], point+ [0.1,0.,0.] + vfield_val, color = GREEN,stroke_width=3,buff=0.)

            vf.add(vfield)
            vf_shift.add(vfield_shift)

            langle = MathTex(r"\langle\ ").next_to(tangent_vector_shift.get_start()-[0.1,0,0],LEFT).set_opacity(0.0)
            rangle = MathTex(r"\rangle\ ").next_to([vfield_shift.get_end()[0]+0.05,vfield_shift.get_start()[1],0],RIGHT).set_opacity(0.0)
            self.add(langle)
            self.add(rangle)
            langle_rangle_komma.append(komma)
            langle_rangle_komma.append(langle)
            langle_rangle_komma.append(rangle)

        self.wait()
        self.next_slide()
        self.play(FadeIn(tangent_vectors_shift,vf_shift))
        for obj in langle_rangle_komma:
            obj.set_opacity(1.0)


        d1 = Dot().set_color(ORANGE)
        self.next_slide()
        self.play(MoveAlongPath(d1, curve1), rate_func=linear)
        self.wait(0.5)
        self.next_slide()
        self.play(MoveAlongPath(d1, curve2), rate_func=linear)
        self.wait()
        self.next_slide()
        description_dual_space = Tex("The space of 1-forms can be seen as the \" dual space \" to curves ",font_size=30).next_to(formula_pairing_concat,0.7*DOWN).scale(0.8)
        self.play(FadeIn(description_dual_space),FadeOut(tangent_vectors_shift))

from manim import *
from manim_slides import Slide
import utils.preamble as preamble

class ScalarValuedDEC(Slide):
    def construct(self):
        

        func = lambda pos: np.sin(0.5*pos[1]) * RIGHT + 0.25*(np.cos(pos[0]) + pos[1]-2) * UP

        # func = lambda pos: (2*pos[1]**2 - (.5*pos[0]))*UP + (2.5*(pos[1]) - (pos[0]))*RIGHT 
        vector_field = ArrowVectorField(func)
        self.add(vector_field)
        self.wait()

        # func = VectorField.scale_func(func, 0.5)
        # self.play(vector_field.animate.become(ArrowVectorField(func)))
        # self.wait()

        title_text = Tex("Work in a force field along a path",font_size=30).to_corner(UL)
        text_domain = Rectangle(color=BLACK,height=7,width=7, fill_opacity = 0.85)
        text_domain.next_to(title_text, DOWN).align_to(title_text, LEFT)
        self.next_slide()
        

        # Add text domain and title to the scene
        self.add(text_domain, title_text)
        self.play(FadeIn(text_domain, title_text))

        text_vf=Tex(
            'Consider the vector field', font_size=30
        ).next_to(text_domain,UP).shift(0.8*DOWN).scale(0.8)

        formula_vf = MathTex(r"F(x,y) =\begin{pmatrix} \mathrm{sin}(0.5 x) \\ 0.25(\mathrm{cos}(x) + y-2)  \end{pmatrix}").next_to(text_vf,0.7*DOWN).scale(0.5)

        self.add(text_vf,formula_vf)
        self.next_slide()
        self.wait()


        text_curve=Tex(
            'Given a curve $\gamma$, the work along the path can be computed as', font_size=30
        ).next_to(formula_vf,0.8*DOWN).scale(0.8)

        self.add(text_curve)
        formula_work = MathTex('W(\gamma) = \int_{[0,1]}\langle F(\gamma(t)),\dot{\gamma}(t)\\rangle dt').next_to(text_curve,DOWN).scale(0.5)
        self.play(FadeIn(text_curve,formula_work))
        self.next_slide()

        # Add the curve to the scene
        # curve = ParametricFunction(lambda t: np.array([1.3*np.sin(1.25*t)+2, 2.5*1.3*0.6*np.cos(t)-1, 0] ) , t_range=[-1., 0.], color=RED, stroke_width=2)
        # curve = ParametricFunction(lambda t: np.array([np.sin(t)+2, np.cos(t)-1, 0] ) , t_range=[-1., 0.], color=RED, stroke_width=2)

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
            
            
        self.play(FadeIn(vf))
        self.next_slide()
        
        self.wait()
        

        # Add the points to the scene
        self.play(FadeIn(tangent_vectors))
        self.next_slide()
        
        
        self.play(Transform(tangent_vectors,tangent_vectors_shift),Transform(vf,vf_shift))
        self.next_slide()
        for obj in langle_rangle_komma:
            obj.set_opacity(1.)
        
        self.next_slide()
        d1 = Dot().set_color(ORANGE)
        self.next_slide()
        self.play(MoveAlongPath(d1, curve), rate_func=linear)
        self.next_slide()
        self.remove(d1)
        self.wait()
        self.next_slide()
        text_work=Tex(
            'For this particular curve it holds $W(\gamma) = -6.87958..$', font_size=30
        ).next_to(formula_work,0.8*DOWN).scale(0.8)
        self.next_slide()
        self.play(FadeIn(text_work))
        self.next_slide()
        self.play(FadeOut(text_work))
        self.wait()
        self.next_slide()       

        self.wait(2)  # Wait for a moment to display the scene
        text_field = Tex('Instead of considering the vector field...  ').next_to(formula_work,0.5*DOWN).scale(0.5)
        text_form = Tex('Consider instead the covector field  ').next_to(formula_work,0.5*DOWN).scale(0.5)
        formula_field = MathTex(r"F(x,y) = \mathrm{sin}(0.5 x)\ e_x +  0.25(\mathrm{cos}(x) + y-2)\ e_y ").next_to(text_field,0.5*DOWN).scale(0.5)
        self.next_slide()
        self.play(FadeIn(formula_field,text_field))
        formula_form = MathTex(r"F^{\flat}(x,y) = \mathrm{sin}(0.5 x)\ de_x +  0.25(\mathrm{cos}(x) + y-2)\ de_y ").next_to(text_field,0.5*DOWN).scale(0.5)
        self.wait()
        self.next_slide()
        self.play(Transform(formula_field,formula_form),Transform(text_field,text_form),FadeOut(tangent_vectors))
        formula_form2 = MathTex(r"F^{\flat}(x,y) = \mathrm{sin}(0.5 x)\ dx +  0.25(\mathrm{cos}(x) + y-2)\ dy").next_to(text_field,0.5*DOWN).scale(0.5)
        self.wait()
        self.next_slide()
        self.play(Transform(formula_field,formula_form2))
        self.wait()
        self.next_slide()
        text_form_below = Tex('The object $F^\\flat$ is an example for a \\textit{differential (1)-form}.  ').next_to(formula_form,0.5*DOWN).scale(0.5)
        self.play(FadeIn(text_form_below))
        

        self.wait()
   

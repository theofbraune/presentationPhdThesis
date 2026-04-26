
from manim import *
from manim_slides import Slide
from utils.preamble import *


class slide4(Slide):
    #differential 2-forms
    def construct(self):
        title_text = Tex("Differential 2-Forms",font_size=30).to_corner(UL).shift(RIGHT)
        description_text = Tex("Flux through an oriented surface piece", font_size=20).next_to(title_text,DOWN)
        self.next_slide()

        # Add text domain and title to the scene
        self.play(FadeIn(title_text,description_text))
        video_image = ImageMobject("figures/smoke/smokeSmall/smoke_two_form_normal.png")
        video_image_flipped = ImageMobject("figures/smoke/smokeSmall/smoke_two_form_normal_flipped.png")
        
        # Scale the image if needed
        video_image.scale(1.1)  # Adjust scale as needed

        # Position the image on the left-hand side
        video_image.to_edge(LEFT).shift(DOWN)
        # Scale the image if needed
        video_image_flipped.scale(1.1)  # Adjust scale as needed

        # Position the image on the left-hand side
        video_image_flipped.to_edge(LEFT).shift(DOWN)

        # Add the image to the scene
        self.add(video_image)
        
        self.wait(1)  # Wait for a moment to display the scene
        self.next_slide()
        equal = MathTex(' =\quad').next_to(video_image,0.5*RIGHT)
        minus = MathTex('-').next_to(equal,0.25*RIGHT)
        langle = MathTex('\quad\\bigg\langle').next_to(minus,1.5*RIGHT)
        # langle_minus = MathTex('\quad - \\bigg\langle').next_to(equal,1.5*RIGHT)
        
        two_form_image = ImageMobject("figures/smoke/two_form.png").next_to(langle,RIGHT).scale(0.9).shift(DOWN*0.2)
        komma = Tex(",").next_to(two_form_image,0.5*RIGHT)
   
        segment_image = ImageMobject("figures/smoke/segment_normal.png").next_to(komma,RIGHT)
        rangle = MathTex("\\bigg\\rangle").next_to(segment_image,RIGHT)

        self.next_slide()
        self.play(FadeIn(equal,langle,two_form_image,komma,segment_image,rangle))
        
        text_pairing = Tex("The velocity field can be paired with an oriented surface piece to obtain the flux through it.  ",font_size=20).next_to(komma,15*UP)
        self.play(FadeIn(text_pairing))
        # here change the surface a few times
        self.wait()
        self.next_slide()
        
        two_form_perp = ImageMobject("figures/smoke/smoke_two_form_perp.png")
        # Scale the image if needed
        two_form_perp.scale(0.9)  # Adjust scale as needed
        # Position the image on the left-hand side
        two_form_perp.to_edge(LEFT).shift(1.5*DOWN+0.2*LEFT)

        segment_image_perp = ImageMobject("figures/smoke/90_deg_two_form_perp.png").next_to(komma,RIGHT)

        self.play(FadeIn(two_form_perp,segment_image_perp),FadeOut(video_image,segment_image))

   
        self.wait()
        self.next_slide()
        
        self.play(FadeOut(two_form_perp,segment_image_perp),FadeIn(video_image, segment_image))
        self.wait()
        self.next_slide()
        
        
        minus = MathTex("-").next_to(equal,0.25*RIGHT)
        text_flipping = Tex("Flipping the orientation of the surface yields a sign flip.  ",font_size=20).next_to(text_pairing,2*DOWN)

        segment_image_flipped = ImageMobject("figures/smoke/normal_flipped.png").next_to(komma,RIGHT)

        self.wait()
        self.next_slide()
        # langle.set_opacity(0.)
        self.play(FadeIn(text_flipping,video_image_flipped,minus),FadeOut(video_image))
        
        self.wait()
        self.next_slide()
        # langle_minus.set_opacity(0.)
        langle.set_opacity(1.)
        description_text_form = Tex(" A differential 2-form can be seen as a dual object to oriented surfaces.",font_size=20).next_to(text_pairing,2*DOWN)
        self.play(FadeOut(video_image_flipped,equal, minus, segment_image))
        self.play(Transform(langle,langle.shift(3*LEFT)),Transform(two_form_image,two_form_image.shift(3*LEFT)), Transform(komma,komma.shift(3*LEFT)),Transform(rangle,rangle.shift(3*LEFT)))
        self.play(Transform(text_flipping,description_text_form))
        self.wait()
        self.next_slide()
        

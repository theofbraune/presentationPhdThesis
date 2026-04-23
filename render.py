

from manim import * # Add this line to ensure all Manim functions are available
from manim_slides import Slide, ThreeDSlide
# Import all your scene classes (assuming these imports are correct)
# from cemetary.presentation import slide11
from slides.introThesis import Intro
from slides.slideGoal import GoalSlide
from slides.scalarDECcover import ScalarDEC_cover
from slides.scalarValuedDEC import ScalarValuedDEC
from slides.slide3 import slide3
from slides.slide4 import slide4
from slides.slide5 import slide5
from slides.slide6 import slide6
# from slides.stokes import stokes 
from slides.slide7 import slide7
from slides.slide8 import slide8
from slides.slide8b import slide8b
from slides.slideBundleValued import BundleValuedFormsIntro
from slides.extDerSlide import ExteriorDerivativeSlides
from slides.slideTorsionIntro import TorsionCover
from slides.slideTorsionSmooth import slideTorsionIntro
from slides.slideDiscreteLC import slideDiscreteLeviCivita
from slides.slidediscreteLC2 import slideDiscreteLeviCivita2
from slides.slideDiscreteTorsion import slideDiscreteTorsion
from slides.slideControlTorsion import slideControllingTorsionCurvature
from slides.slideControlTorsionCont import slideControllingTorsionCurvatureCont
from slides.slideControlTorsionCont2 import slideControllingTorsionCurvatureCont2
from slides.slideFullDECCover import FullDECCover

"""
# from slides.slideDiscreteTorsion3 import slideDiscreteTorsion3

# from slides.teaserBundleValued import teaser_bundle_valued
# from slides.slide9 import slide9
# from slides.slide_connection import slide_connection
# from slides.slide10 import slide10
# from slides.slide11 import ExteriorDerivativeSlides
# from slides.slide12 import slide12
# from slides.TransitionBundleValued import TransitionBundleValued
# from slides.slide13 import slide13
# from slides.slide14 import slide14
# from slides.slide15 import slide15
# from slides.slide16 import slide16
# from slides.slideDiscretization import slide16AndAHalf
# from slides.slideDiscretization2 import slide16AndThreeQuarter
# from slides.slide17 import slide17
# from slides.slide18 import slide18
# from slides.slideSummary import SummarySlide
# from slides.slide19 import slide19
# from slides.slide20 import slide20
# ... (all other imports)
"""
# Define the master presentation class. 
class FullPresentation(ThreeDSlide): 
    
    # List all scene classes in the exact desired order
    SCENES = [
        Intro,
        GoalSlide,
        ScalarDEC_cover,
        ScalarValuedDEC,
        slide4,
        slide5,
        slide6,
        slide7,
        slide8,
        slide8b,
        BundleValuedFormsIntro,
        ExteriorDerivativeSlides,
        TorsionCover,
        slideTorsionIntro,
        slideDiscreteLeviCivita,
        slideDiscreteLeviCivita2,
        slideDiscreteTorsion,
        slideControllingTorsionCurvature,
        slideControllingTorsionCurvatureCont,
        slideControllingTorsionCurvatureCont2,
        FullDECCover,
        # slide12,
        # TransitionBundleValued,
        # slide13,
        # slide14,
        # slide15,
        # slide16,
        # slide16AndAHalf,
        # slide16AndThreeQuarter,
        # slide17,
        # slide18,
        # SummarySlide,
        # slide19,
        # slide20,

        # ... all other classes in order ...
    ]
    
    def construct(self):
        # Use a list of classes to manually execute them sequentially
        for SceneClass in self.SCENES:
            # 1. Run the next scene's construct method
            SceneClass.construct(self)
            
            # 2. CRITICAL CLEANUP: Remove all Mobjects (visual objects) from the scene
            # This ensures the next scene starts on a blank slate.
            # We use self.remove(*self.mobjects) instead of self.clear() to avoid 
            # clearing the entire scene prematurely in case of background persistence.
            self.remove(*self.mobjects)
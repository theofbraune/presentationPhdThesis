

from manim import * # Add this line to ensure all Manim functions are available
from manim_slides import Slide, ThreeDSlide
# Import all your scene classes (assuming these imports are correct)
# from cemetary.presentation import slide11
from slides.intro.introThesis import Intro
from slides.intro.slideBundleVal2 import BundleValuedFormsIntro2
from slides.intro.slideGoal import GoalSlide
from slides.intro.scalarDECcover import ScalarDEC_cover
from slides.intro.scalarValuedDEC import ScalarValuedDEC
from slides.intro.slide3 import slide3
from slides.intro.slide4 import slide4
from slides.intro.slide5 import slide5
from slides.intro.slide6 import slide6
# from slides.stokes import stokes 
from slides.intro.slide7 import slide7
from slides.intro.slide8 import slide8
from slides.intro.slide8b import slide8b
from slides.intro.slideBundleValued import BundleValuedFormsIntro
from slides.intro.slideBundleVal2 import BundleValuedFormsIntro2
from slides.intro.extDerSlide import ExteriorDerivativeSlides

# for the discrete torsion part 
from slides.discreteTorsion.slideTorsionIntro import TorsionCover
from slides.discreteTorsion.slideTorsionSmooth import slideTorsionIntro
from slides.discreteTorsion.slideDiscreteLC import slideDiscreteLeviCivita
from slides.discreteTorsion.slidediscreteLC2 import slideDiscreteLeviCivita2
from slides.discreteTorsion.slideDiscreteTorsion import slideDiscreteTorsion
from slides.discreteTorsion.slideControlTorsion import slideControllingTorsionCurvature
from slides.discreteTorsion.slideControlTorsionCont import slideControllingTorsionCurvatureCont
from slides.discreteTorsion.slideControlTorsionCont2 import slideControllingTorsionCurvatureCont2

# for the full DEC part 
from slides.FullDEC.slideFullDECCover import FullDECCover
from slides.FullDEC.slideDiscreteWelcome import slideDiscreteBundle
from slides.FullDEC.slideDiscreteBundleValuedForms import slideDiscreteBundleValuedForm
from slides.FullDEC.slideDiscreteFrakd import slideDiscreteFrakd
from slides.FullDEC.slideIssueFrakd import slideIssueFrakD
from slides.FullDEC.slidePPF import slidePPF
from slides.FullDEC.slideFrakDfirstStep import slideFrakDfixed
from slides.FullDEC.slideAlgebraicBianchi import slideAlgebraicBianchiIssue
from slides.FullDEC.slidedNabla import slideAlgebraicBianchiFix
from slides.FullDEC.slideDiscreteAlgebraicBianchi import slideDiscreteAlgebraicBianchiFixed
from slides.FullDEC.slideWrapUpAndSummary import slideSummary
from slides.FullDEC.slideWhatComesNext import slideFutureWork
from slides.FullDEC.slideThanks import slideThanks



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
        BundleValuedFormsIntro,
        BundleValuedFormsIntro2,
        slide8,
        slide8b,
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
        slideDiscreteBundle,
        slideDiscreteBundleValuedForm,
        slideDiscreteFrakd,
        slideIssueFrakD,
        slidePPF,
        slideFrakDfixed,
        slideAlgebraicBianchiIssue,
        slideAlgebraicBianchiFix,
        slideDiscreteAlgebraicBianchiFixed,
        slideSummary,
        slideFutureWork,
        slideThanks
        

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

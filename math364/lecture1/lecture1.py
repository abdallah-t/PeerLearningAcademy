from manim import *

LOGO_YELLOW = "#fed966"
LOGO_GREEN = "#a8d18d"
LOGO_RED = "#f08362"
ARABIC_FONT = "Vazirmatn"
ENGLISH_FONT = "CMU Serif"
class angles(Scene):
    def construct(self):
        full_rotation = [r"400^{\text{g}}", r"2\pi^{\text{r}}", r"360^{\circ}"]
        angles = Text("الزوايا", font=ARABIC_FONT, font_size=70)
        self.play(Write(angles, reverse=True))
        self.add(angles)
        self.wait()
        self.play(angles.animate.to_edge(UR).scale(0.8))
        self.wait()
        degrees = Text("درجات", font=ARABIC_FONT, font_size=70, color=LOGO_YELLOW).move_to([7, 2.5, 0], aligned_edge=RIGHT)
        radians = Text("راديان", font=ARABIC_FONT, font_size=70, color=LOGO_GREEN).move_to([7, 2.5, 0], aligned_edge=RIGHT)
        grads = Text("جراد", font=ARABIC_FONT, font_size=70, color=LOGO_GREEN).move_to([7, 2.5, 0], aligned_edge=RIGHT)
        angle_group = VGroup(grads, radians, degrees)
        self.play(FadeIn(angle_group), angle_group.animate.arrange(RIGHT, buff=2), run_time=2)
        self.add(angle_group)
        self.wait()
        rotations = VGroup()
        for i in reversed(range(len(angle_group))):
            angle = angle_group[i].copy()
            rotation = MathTex(full_rotation[i]).next_to(angle, ORIGIN)
            self.play(FadeIn(rotation), rotation.animate.next_to(angle, DOWN))
            self.wait()
            self.add(rotation)
            rotations.add(rotation)
        
        self.wait()
        self.play(FadeOut(rotations))
        self.wait()
        self.play(FadeOut(grads))
        angle_group.remove(grads)
        self.play(angle_group.animate.move_to(ORIGIN))
        self.wait()
        self.play(angle_group[1].animate.move_to(ORIGIN).to_edge(UP), FadeOut(angle_group[0]).scale(0.8), run_time=2)
        self.wait()
        angle_definition = MathTex(r"")

        
        

        self.wait()
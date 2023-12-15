from manim import *

LOGO_YELLOW = "#fed966"
LOGO_GREEN = "#a8d18d"
LOGO_RED = "#f08362"
ARABIC_FONT = "Vazirmatn"
ENGLISH_FONT = "CMU Serif"
class angles(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amssymb}")

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
        angle_group[1].save_state()
        self.wait()
        self.play(angle_group[1].animate.move_to(ORIGIN).to_edge(UP).scale(0.8), FadeOut(angle_group[0]), run_time=2)
        self.wait()
        degree_definition = MathTex(r"1", r"\text{ deg}", r":=", r"\dfrac{1}{360}", r"\text{ Rotations}", tex_template=myTemplate).scale(1.5)
        self.play(Write(degree_definition))
        self.wait()
        self.play(Indicate(degree_definition[1], scale_factor=1.5, color=LOGO_YELLOW))
        self.wait()
        self.play(Indicate(degree_definition[2], scale_factor=1.5, color=LOGO_YELLOW))
        self.wait()
        self.play(Indicate(degree_definition[4], scale_factor=1.5, color=LOGO_YELLOW))
        self.wait()
        box = SurroundingRectangle(degree_definition[3][2:5])
        self.play(Create(box))
        self.wait()
        why_360 = Text("why 360?", font=ENGLISH_FONT, font_size=30, color=LOGO_RED).next_to(box, DOWN)
        self.play(Write(why_360))
        self.add(why_360)
        self.wait()
        self.play(FadeOut(why_360, box, degree_definition))
        self.wait()
        self.play(angle_group[1].animate.restore(), FadeIn(angle_group[0]), run_time=2)
        self.wait()
        self.play(angle_group[0].animate.move_to(ORIGIN).to_edge(UP).scale(0.8), FadeOut(angle_group[1]), run_time=2)
        self.wait

        what_is_radian = MarkupText(f'<span font_family="{ARABIC_FONT}" foreground="{LOGO_YELLOW}">ما هو الراديان؟</span>')
        self.play(Write(what_is_radian, reverse=True))
        self.add(what_is_radian)
        self.wait()
        self.play(what_is_radian.animate.next_to(angles, DOWN, aligned_edge=RIGHT))
        self.wait()
        

        #circle animation
        circle = Circle(radius=2, color=WHITE,).shift(DOWN)
        radius_1 = Line(circle.get_center(), circle.point_at_angle(2 * PI), color=LOGO_RED, stroke_width=7)
        radius_1_label = MathTex("r").next_to(radius_1, RIGHT).move_to(radius_1)
        self.play(Create(circle), Create(radius_1))
        self.wait()
        self.play(FadeIn(radius_1_label), radius_1_label.animate.next_to(radius_1, DOWN))
        self.wait()
        normal = radius_1.copy()
        self.play(normal.animate.rotate(-1 * PI / 2, about_point=circle.get_right()))
        self.wait()
        normal_label = MathTex("r").move_to(normal)
        self.play(FadeIn(normal_label), normal_label.animate.next_to(normal, RIGHT))
        self.wait()
        arc = ArcBetweenPoints(circle.point_at_angle(1), circle.point_at_angle(2 * PI), radius=-2, color=LOGO_GREEN, stroke_width=7)
        
        self.play(Transform(normal, arc), normal_label.animate.move_to(arc.get_center() + 0.5 * (RIGHT * np.cos(0.5) + UP * np.sin(0.5))))
        self.wait()
        radius_2 = Line(circle.get_center(), circle.point_at_angle(1), color=LOGO_RED, stroke_width=7)
        radius_2_label = MathTex("r").move_to(radius_2)
        self.play(Create(radius_2))
        self.wait()
        self.play(FadeIn(radius_2_label), radius_2_label.animate.move_to(radius_2.get_center() + 0.3 * (RIGHT * np.cos(PI - 1) + UP * np.sin(PI - 1))))
        self.wait()
        angle_between_radii = Angle(radius_1, radius_2, radius=0.5)
        self.play(Create(angle_between_radii))
        self.wait()
        theta = MathTex(r"\theta").move_to(angle_between_radii).scale(0.8)
        self.play(FadeIn(theta), theta.animate.move_to(angle_between_radii.get_center() + 0.4 * (RIGHT * np.cos(0.5) + UP * np.sin(0.5))))
        self.wait()

        theta.save_state()
        self.play(theta.animate.shift(3 * RIGHT).scale(2).set_color(LOGO_YELLOW), run_time=2)
        self.wait()
        is_equal_to_1_rad = MathTex(r"= 1 \text{ rad}").next_to(theta, RIGHT)
        self.play(Write(is_equal_to_1_rad))
        self.wait()
        self.play(theta.animate.restore(), FadeOut(is_equal_to_1_rad))
        self.wait()
        one_rad = MathTex(r"1 ^{r}", font_size=30).move_to(angle_between_radii.get_center() + 0.4 * (RIGHT * np.cos(0.5) + UP * np.sin(0.5)))
        self.play(Transform(theta, one_rad))




        sector = VGroup(arc, radius_1, radius_2, angle_between_radii)
        
        sectors = VGroup()
        temp_thetas = VGroup()
        temp_thetas.add(theta)
        last = sector.copy()
        self.play(FadeOut(radius_2_label, normal_label, radius_1_label))
        self.wait()
        for i in range(5):
            sectors.add(last)
            self.play(Rotate(last, 1, about_point=circle.get_center()))
            temp_theta = theta.copy()
            self.play(temp_theta.animate.move_to(last[3].get_center() + 0.4 * (RIGHT * np.cos(1.5 + i) + UP * np.sin(1.5 + i))))
            last = last.copy()
            temp_thetas.add(temp_theta)


        
        little_angle = Angle(sectors[4][2],radius_1, radius=0.5)
        self.play(Create(little_angle))
        self.wait()
        little_theta = MathTex(r"{0.28\cdots}^{r}", font_size=20).move_to(little_angle)
        self.play(little_theta.animate.move_to(little_angle.get_center() + 0.8 * (RIGHT * np.cos(3 + PI) + UP * np.sin(PI + 3))))
        temp_thetas.add(little_theta)
        self.wait()
        # group all angles 
        thetas_to_point = AnimationGroup(*[temp_thetas[i].animate.move_to(circle.get_center() + 3 * RIGHT, aligned_edge=LEFT) for i in range(len(temp_thetas))], lag_ratio=0.15)
        self.play(thetas_to_point)
        two_pi_dec = MathTex(r"6.28\cdots^{r}").move_to(temp_thetas[0], aligned_edge=LEFT).scale(0.8)
        two_pi = MathTex(r"2\pi^{r}").move_to(temp_thetas[0], aligned_edge=LEFT).scale(0.8)
        self.play(thetas_to_point)
        self.play(Transform(temp_thetas, two_pi_dec))
        self.wait()
        self.play(Transform(temp_thetas, two_pi))
        self.wait()

        
        self.play(FadeOut(*self.mobjects))
        

        

        self.wait()

class TransformingBetweenAngles(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amssymb}")
        myTemplate.add_to_preamble(r"\usepackage{cancel}")
        arabic_template = TexTemplate()
        arabic_template.add_to_preamble(r"% !TEX program = xelatex")
        arabic_template.add_to_preamble(r"\usepackage[margin=0.75in]{geometry} % Load geometry before bidi")
        arabic_template.add_to_preamble(r"\usepackage{polyglossia}")
        arabic_template.add_to_preamble(r"\setmainlanguage{arabic}")
        arabic_template.add_to_preamble(r"\setotherlanguage{english}")
        arabic_template.add_to_preamble(r"\usepackage{fontspec}")
        arabic_template.add_to_preamble(r"\newfontfamily\arabicfont[Script=Arabic, Scale=1.1]{Times New Roman}")

        how_to_convert_text = "كيف نحول بين الزوايا؟"
        how_to_convert = MarkupText(f'<span font_family="{ARABIC_FONT}" foreground="{WHITE}">{how_to_convert_text}</span>').scale(1.2)
        self.play(Write(how_to_convert, reverse=True))
        self.add(how_to_convert)
        self.play(how_to_convert.animate.to_edge(UP).scale(0.8).set_color(LOGO_YELLOW))
        self.wait()
        
        # initial equations
        full_rotation_deg = MathTex(r"1 \text{ Rotation}", r"=", r"360 \text{ deg}", tex_template=myTemplate)
        full_rotation_rad = MathTex(r"1 \text{ Rotation}", r"=", r"2\pi \text{ rad}", tex_template=myTemplate)
        equations = VGroup(full_rotation_deg, full_rotation_rad).arrange(DOWN, buff=1, aligned_edge=LEFT).move_to(ORIGIN)
        self.play(Write(full_rotation_deg))
        self.wait()
        self.play(Write(full_rotation_rad))
        self.wait()
        
        # manipulate the equations
        steps =VGroup(MathTex(r"360", r"\text{ deg}", r"=", r"2\pi", r"\text{ rad}", tex_template=myTemplate),
                      MathTex(r"\dfrac{360}{2}", r"\text{ deg}", r"=", r"\dfrac{2\pi}{2}", r"\text{ rad}", tex_template=myTemplate),
                      MathTex(r"\dfrac{360}{2}", r"\text{ deg}", r"=", r"\dfrac{\cancel{2}\pi}{\cancel{2}}", r"\text{ rad}", tex_template=myTemplate),
                      MathTex(r"180", r"\text{ deg}", r"=", r"\pi", r"\text{ rad}", tex_template=myTemplate),
                      MathTex(r"\dfrac{180 \text{ deg}}{\pi \text{ rad}}", r"=", r"1", tex_template=myTemplate),
                      MathTex(r"\dfrac{\pi \text{ rad}}{180 \text{ deg}}", r"=", r"1", tex_template=myTemplate),

        )
        self.play(TransformMatchingTex(equations, steps[0]))
        for i in range(len(steps) - 2):
            self.play(TransformMatchingTex(steps[i], steps[i + 1], transform_mismatches=True))
            self.wait()
        
        steps[5].next_to(steps[4], RIGHT, buff=1)
        final_equations = VGroup(steps[4], steps[5])
        self.play(TransformFromCopy(steps[4], steps[5]))
        self.wait()
        self.play(final_equations.animate.arrange(RIGHT, buff=1).move_to(ORIGIN))
        self.wait()
        
        self.play(final_equations.animate.scale(0.8).to_edge(DR))
        # example 1
        question_0_text = "مثال 1: حول 45 درجة إلى راديان"
        question_0 = MarkupText(f'<span font_family="{ARABIC_FONT}" foreground="{WHITE}">{question_0_text}</span>')
        self.play(Write(question_0, reverse=True))
        self.add(question_0)
        self.wait()
        self.play(question_0.animate.scale(0.7).set_color(LOGO_GREEN).next_to(how_to_convert, DOWN).to_edge(RIGHT))
        self.wait()
        
        deg_to_rad_example_1 =VGroup(MathTex(r"45", r"\text{ deg}", tex_template=myTemplate),
                                     MathTex(r"45", r"\text{ deg}", r"\cdot", r"1", tex_template=myTemplate),
                                     MathTex(r"45", r"\text{ deg}", r"\cdot", r"\dfrac{\pi \text{ rad}}{180 \text{ deg}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{45 \text{ deg}}{1}", r"\cdot", r"\dfrac{\pi \text{ rad}}{180 \text{ deg}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{45 \text{ deg} \cdot \pi \text{ rad}}{180 \text{ deg}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{45 \text{ \cancel{deg}} \cdot \pi \text{ rad}}{180 \text{ \cancel{deg}}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{45 \cdot \pi \text{ rad}}{180}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{45 \cdot \pi}{180}}", r"\text{ rad}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{\pi}{4}}", r"\text{ rad}", tex_template=myTemplate),
                                     
        )


        self.play(Write(deg_to_rad_example_1[0]))
        for i in range(len(deg_to_rad_example_1) - 1):
            self.play(TransformMatchingShapes(deg_to_rad_example_1[i], deg_to_rad_example_1[i + 1], transform_mismatches=False))
            self.wait()
        
        self.play(FadeOut(deg_to_rad_example_1[-1]))
        self.wait()
        self.play(FadeOut(question_0))
        
        # example 2
        question_1_text = r"مثال 2: حول \pi راديان إلى درجات"
        question_1 = Tex(question_1_text, tex_template=TexFontTemplates.)
        self.play(Write(question_1, reverse=True))
        self.add(question_1)
        self.wait()
        self.play(question_1.animate.scale(0.7).set_color(LOGO_GREEN).next_to(how_to_convert, DOWN).to_edge(RIGHT))
        self.wait()

        rad_to_deg_example_1 =VGroup(MathTex(r"\pi", r"\text{ rad}", tex_template=myTemplate),
                                     MathTex(r"\pi", r"\text{ rad}", r"\cdot", r"1", tex_template=myTemplate),
                                     MathTex(r"\pi", r"\text{ rad}", r"\cdot", r"\dfrac{180 \text{ deg}}{\pi \text{ rad}}", tex_template=myTemplate, arg_separator=""),
                                     MathTex(r"\dfrac{\pi \text{ rad}}{1}", r"\cdot", r"\dfrac{180 \text{ deg}}{\pi \text{ rad}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{\pi \text{ rad} \cdot 180 \text{ deg}}{\pi \text{ rad}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{\pi \text{ \cancel{rad}} \cdot 180 \text{ deg}}{\pi \text{ \cancel{rad}}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{\pi \cdot 180 \text{ deg}}{\pi}}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{\pi \cdot 180}{\pi}}", r"\text{ deg}", tex_template=myTemplate),
                                     MathTex(r"\dfrac{180}{1}}", r"\text{ deg}", tex_template=myTemplate),
                                     MathTex(r"180", r"\text{ deg}", tex_template=myTemplate),

        )
        
        self.play(Write(rad_to_deg_example_1[0]))
        for i in range(len(rad_to_deg_example_1) - 1):
            self.play(TransformMatchingShapes(rad_to_deg_example_1[i], rad_to_deg_example_1[i + 1], transform_mismatches=False))
            self.wait()
        
        self.play(FadeOut(rad_to_deg_example_1[-1]))
        



        
        self.wait()

        self.wait()
        
        


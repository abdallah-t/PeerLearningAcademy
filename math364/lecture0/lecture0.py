from manim import *

LOGO_YELLOW = "#fed966"
LOGO_GREEN = "#a8d18d"
LOGO_RED = "#f08362"
ARABIC_FONT = "Rubik"
ENGLISH_FONT = "CMU Serif"

class Introduction(Scene):
    def construct(self):
        math364 = Text("Math364", font=ENGLISH_FONT, font_size=70)
        abdallah = Text("عبدالله طنطاوي", font=ARABIC_FONT, font_size=70, color=LOGO_GREEN)
        self.play(Write(math364))
        self.wait(2)
        self.play(math364.animate.shift(3 * UP).scale(0.6))
        self.wait()
        self.play(Write(abdallah, reverse=True))
        self.add(abdallah)
        self.wait(2)
        self.play(Unwrite(math364))
        self.play(Unwrite(abdallah))
        self.wait(2)


class CourseContent(Scene):
    def construct(self):
        what_will_you_learn = Text("ماذا ستتعلم؟", font=ARABIC_FONT, font_size=70,)
        point1 = Dot([6, 1, 0])
        content = Text("المحتوى الدراسي", font=ARABIC_FONT, font_size=40, color=LOGO_YELLOW)
        content.next_to(point1, LEFT)

        point2 = Dot([6, -0.5 , 0])
        calculator_tips = Text("نصائح لاستخدام الآلة الحاسبة", font=ARABIC_FONT, font_size=40, color=LOGO_GREEN)
        calculator_tips.next_to(point2, LEFT)

        
        point3 = Dot([6, -2, 0])
        exam_tips = Text("نصائح لأداء الامتحانات", font=ARABIC_FONT, font_size=40, color=LOGO_RED)
        exam_tips.next_to(point3, LEFT)
        
        self.play(Write(what_will_you_learn, reverse=True))
        self.add(what_will_you_learn)
        self.wait()
        self.play(what_will_you_learn.animate.move_to([7, 2.5, 0], aligned_edge=RIGHT).scale(0.8))
        self.wait()

        self.play(FadeIn(point1))       
        self.play(Write(content, reverse=True))
        self.add(content)
        self.wait()

        self.play(FadeIn(point2))
        self.play(Write(calculator_tips, reverse=True))
        self.add(calculator_tips)
        self.wait()

        self.play(FadeIn(point3))
        self.play(Write(exam_tips, reverse=True))
        self.add(exam_tips)
        self.wait()

        self.wait(2)
        self.play(FadeOut(point1), FadeOut(point2), FadeOut(point3))
        self.play(Unwrite(content), Unwrite(calculator_tips), Unwrite(exam_tips))
        self.play(Unwrite(what_will_you_learn))
        self.wait()

class SpecialCourse(Scene):
    def construct(self):
        special_thing = Text("ما المميز؟", font=ARABIC_FONT, font_size=70,)
        self.play(Write(special_thing, reverse=True))
        self.add(special_thing)
        self.wait()
        self.play(special_thing.animate.move_to([7, 2.5, 0], aligned_edge=RIGHT).scale(0.8))
        self.wait()

        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.play(FadeIn(line1), FadeIn(line_moving), FadeIn(a), FadeIn(tex))
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )

        self.play(theta_tracker.animate.set_value(40))
        self.play(theta_tracker.animate.increment_value(140))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(350))
        self.play(FadeOut(line1), FadeOut(line_moving), FadeOut(a), FadeOut(tex))
        self.wait()

        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

        student1 = SVGMobject("../../assets/images/student.svg").set_color(WHITE)
        student2 = SVGMobject("../../assets/images/student.svg").set_color(WHITE)
        students = VGroup(student1, student2)
        self.play(Write(student1))
        self.play(student1.animate.shift(2* LEFT))
        self.play(Write(student2))
        self.play(students.animate.move_to([0, 0, 0]))
        self.wait()
        self.play(Unwrite(students))
        self.wait(2)
        
        youtube = SVGMobject("../../assets/images/youtube.svg", stroke_color=WHITE, stroke_width=5)
        self.play(Write(youtube))
        self.wait()
        



    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)
        self.play(FadeOut(*self.mobjects[1:]))
        

            
class Requirements(Scene):
    def construct(self):
        requirements = Text("متطلبات الكورس", font=ARABIC_FONT, font_size=70,)
        self.play(Write(requirements, reverse=True))
        self.add(requirements)
        self.wait()
        self.play(requirements.animate.move_to([7, 2.5, 0], aligned_edge=RIGHT).scale(0.8))
        self.wait()
        calculator = Text("آلة حاسبة", font=ARABIC_FONT, font_size=40, color=LOGO_GREEN)
        point1 = Dot([6, 1, 0])
        calculator.next_to(point1, LEFT)
        self.play(FadeIn(point1))
        self.play(Write(calculator, reverse=True))
        self.add(calculator)
        calculator_image = SVGMobject("../../assets/images/calculator.svg", stroke_color=LOGO_GREEN, stroke_width=5).scale(0.5)
        calculator_image.next_to(calculator, LEFT)
        self.play(Write(calculator_image))

        pen_and_paper = Text("ورقة وقلم", font=ARABIC_FONT, font_size=40, color=LOGO_RED)
        point2 = Dot([6, -0.5 , 0])
        pen_and_paper.next_to(point2, LEFT)
        self.play(FadeIn(point2))
        self.play(Write(pen_and_paper, reverse=True))
        self.add(pen_and_paper)
        pen_and_paper_image = SVGMobject("../../assets/images/pen_and_paper.svg", stroke_color=LOGO_RED, stroke_width=5).scale(0.5)
        pen_and_paper_image.next_to(pen_and_paper, LEFT)
        self.play(Write(pen_and_paper_image))


        self.wait()

        self.play(FadeOut(point1), FadeOut(point2))
        self.play(Unwrite(calculator), Unwrite(pen_and_paper))
        self.play(Unwrite(calculator_image), Unwrite(pen_and_paper_image))
        



        self.wait(2)
        self.play(Unwrite(requirements))
        self.wait()
        

class Content(Scene):
    def construct(self):
        
        content = Text("المحتوى الدراسي", font=ARABIC_FONT, font_size=70,)
        self.play(Write(content, reverse=True))
        self.add(content)
        self.wait()
        self.play(content.animate.move_to([7, 2.5, 0], aligned_edge=RIGHT).scale(0.8))
        self.wait()

        trigonometry = Text("علم المثلثات", font=ARABIC_FONT, font_size=40, color=LOGO_YELLOW)
        point1 = Dot([6, 1, 0])
        trigonometry.next_to(point1, LEFT)
        self.play(FadeIn(point1))
        self.play(Write(trigonometry, reverse=True))
        self.add(trigonometry)
        trigonometry_image = SVGMobject("../../assets/images/trigonometry.svg", stroke_color=LOGO_YELLOW, stroke_width=5).scale(0.5)
        trigonometry_image.next_to(trigonometry, LEFT)
        self.play(Write(trigonometry_image))
        self.wait()

        functions = Text("تحليل الدوال", font=ARABIC_FONT, font_size=40, color=LOGO_GREEN)
        point2 = Dot([6, -0.5 , 0])
        functions.next_to(point2, LEFT)
        self.play(FadeIn(point2))
        self.play(Write(functions, reverse=True))
        self.add(functions)
        functions_image = SVGMobject("../../assets/images/functions.svg", stroke_color=LOGO_GREEN, stroke_width=5).scale(0.5)
        functions_image.next_to(functions, LEFT)
        self.play(Write(functions_image))
        self.wait()

        limits_and_derivatives = Text("الاشتقاق والنهايات", font=ARABIC_FONT, font_size=40, color=LOGO_RED)
        point3 = Dot([6, -2 , 0])
        limits_and_derivatives.next_to(point3, LEFT)
        self.play(FadeIn(point3))
        self.play(Write(limits_and_derivatives, reverse=True))
        self.add(limits_and_derivatives)
        limits_and_derivatives_tex = MathTex(r"\frac{dy}{dx}\left(\lim_{x \to 0} \frac{\sin x}{x}\right)").set_color(LOGO_RED)
        limits_and_derivatives_tex.next_to(limits_and_derivatives, LEFT)
        self.play(Write(limits_and_derivatives_tex))
        self.wait()

        self.play(FadeOut(point1), FadeOut(point2), FadeOut(point3))
        self.play(Unwrite(trigonometry), Unwrite(functions), Unwrite(limits_and_derivatives))
        self.play(Unwrite(trigonometry_image), Unwrite(functions_image), Unwrite(limits_and_derivatives_tex))
        self.play(Unwrite(content))

        self.wait()
        

class CourseTips(Scene):
    def construct(self):
        course_tips = Text("نصائح الكورس", font=ARABIC_FONT, font_size=70,)
        self.play(Write(course_tips, reverse=True))
        self.add(course_tips)
        self.wait()
        self.play(course_tips.animate.move_to([7, 2.5, 0], aligned_edge=RIGHT).scale(0.8))
        self.wait()

        tip1 = Text("وقف وحل!", font=ARABIC_FONT, font_size=40, color=LOGO_YELLOW)
        point1 = Dot([6, 1, 0])
        tip1.next_to(point1, LEFT)
        self.play(FadeIn(point1))
        self.play(Write(tip1, reverse=True))
        self.add(tip1)
        tip1_image = SVGMobject("../../assets/images/stop.svg", stroke_color=LOGO_YELLOW, stroke_width=4).scale(0.5)
        tip1_image.next_to(tip1, LEFT)
        self.play(Write(tip1_image))
        self.wait()

        tip2 = Text("احرص على حل التمارين", font=ARABIC_FONT, font_size=40, color=LOGO_GREEN)
        point2 = Dot([6, -0.5 , 0])
        tip2.next_to(point2, LEFT)
        self.play(FadeIn(point2))
        self.play(Write(tip2, reverse=True))
        self.add(tip2)
        tip2_image = SVGMobject("../../assets/images/exercise.svg", stroke_color=LOGO_GREEN, stroke_width=5).scale(0.5)
        tip2_image.next_to(tip2, LEFT)
        self.play(Write(tip2_image))
        
        self.wait()

        tip3 = Text("اسأل ما تريد!", font=ARABIC_FONT, font_size=40, color=LOGO_RED)
        point3 = Dot([6, -2 , 0])
        tip3.next_to(point3, LEFT)
        self.play(FadeIn(point3))
        self.play(Write(tip3, reverse=True))
        self.add(tip3)
        tip3_image = SVGMobject("../../assets/images/question.svg", stroke_color=LOGO_RED, stroke_width=5).scale(0.5)
        tip3_image.next_to(tip3, LEFT)
        self.play(Write(tip3_image))

        self.wait()

        self.play(FadeOut(point1), FadeOut(point2), FadeOut(point3))
        self.play(Unwrite(tip1), Unwrite(tip2), Unwrite(tip3))
        self.play(Unwrite(tip1_image), Unwrite(tip2_image), Unwrite(tip3_image))
        self.play(Unwrite(course_tips))

        self.wait()
from manim import *

color_scheme = {"فريق": "#fed966", "تعليم": "#a8d18d", "الأقران": "#f08362"},
LOGO_YELLOW = "#fed966"
LOGO_GREEN = "#a8d18d"
LOGO_RED = "#f08362"
LOGO_FONT = "Rubik Black"
LOGO_PURPLE = "#022060"
social_media_font = "Space mono"
markup = f'<span font_family="{LOGO_FONT}" foreground="{LOGO_YELLOW}">فريق</span><span font_family="{LOGO_FONT}" foreground="{LOGO_GREEN}"> تعليم</span><span font_family="{LOGO_FONT}" foreground="{LOGO_RED}"> الأقران</span>'

class TumbNail(Scene):
    def construct(self):
        plane = NumberPlane()
        peer_learning_logo = SVGMobject("../../assets/images/logo.svg", stroke_color=LOGO_GREEN, fill_color=LOGO_GREEN)
        font_arabic_logo = MarkupText(text=markup).scale(1.5)
        font_arabic_logo.next_to(peer_learning_logo, LEFT)
        
        logo_group = Group(peer_learning_logo, font_arabic_logo).scale(0.5)
        logo_group.move_to(UR * 3 + RIGHT)
        math364 = Text("ريض 364", font=LOGO_FONT, font_size=43)

        lecture0 = Text("حصة 0: المقدمة", font=LOGO_FONT, font_size=43)
        
        


        self.add(font_arabic_logo, peer_learning_logo, math364, lecture0)
        
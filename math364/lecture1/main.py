from manim import *

color_scheme = {"فريق": "#fed966", "تعليم": "#a8d18d", "الأقران": "#f08362"},
LOGO_YELLOW = "#fed966"
LOGO_GREEN = "#a8d18d"
LOGO_RED = "#f08362"
LOGO_FONT = "Rubik Black"
LOGO_PURPLE = "#022060"
social_media_font = "Space mono"
markup = f'<span font_family="{LOGO_FONT}" foreground="{LOGO_YELLOW}">فريق</span><span font_family="{LOGO_FONT}" foreground="{LOGO_GREEN}"> تعليم</span><span font_family="{LOGO_FONT}" foreground="{LOGO_RED}"> الأقران</span>'
class Logo(Scene):
    def construct(self):
        plane = NumberPlane()
        peer_learning_logo = ImageMobject("../../assets/images/logo.png")
        peer_learning_logo.height = 4
        peer_learning_logo.width = 4
        
        
        font_arabic_logo = MarkupText(text=markup).scale(1.5)
        font_arabic_logo.next_to(peer_learning_logo, LEFT * 0.01)
        #font_english_logo = Text("Peer Learning Team", color=LOGO_PURPLE, font="Sans", font_size=43)
        #font_english_logo.next_to(font_arabic_logo, DOWN)
        


        instagram_logo = ImageMobject("../../assets/images/IGLogo.png")
        instagram_logo.height = 0.6
        instagram_logo.width = 0.6
        instagram_logo.move_to([-6, -2, 0])
        instagram_account = Text("abdallahtantawy",font=social_media_font, font_size=30)
        instagram_account.next_to(instagram_logo, RIGHT)

        github_logo = ImageMobject("../../assets/images/GitHubLogo.png")
        github_logo.height = 0.6
        github_logo.width = 0.6
        github_logo.move_to([-6, -3, 1])
        github_account = Text("abdallah-t",font=social_media_font, font_size=30)
        github_account.next_to(github_logo, RIGHT)
        self.play(FadeIn(peer_learning_logo))
        self.wait(0.5)
        self.play(peer_learning_logo.animate.shift(RIGHT * 4.5))
        font_arabic_logo.next_to(peer_learning_logo, LEFT * 0.01)
        self.play(Write(font_arabic_logo, reverse=True))
        self.add(font_arabic_logo)
        self.play(FadeIn(instagram_logo))
        self.play(Write(instagram_account), run_time=0.5)
        self.play(FadeIn(github_logo))
        self.play(Write(github_account), run_time=0.5)
        self.wait()

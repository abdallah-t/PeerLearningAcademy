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
        peer_learning_logo = SVGMobject("../../assets/images/logo.svg", stroke_color=LOGO_GREEN, fill_color=LOGO_GREEN)
        
        
        font_arabic_logo = MarkupText(text=markup).scale(1.5)
        font_arabic_logo.next_to(peer_learning_logo, LEFT)
        #font_english_logo = Text("Peer Learning Team", color=LOGO_PURPLE, font="Sans", font_size=43)
        #font_english_logo.next_to(font_arabic_logo, DOWN)
        

        peerlearning_instagram = SVGMobject("../../assets/images/IGLogo.svg", stroke_color=WHITE, fill_color=WHITE)
        peerlearning_instagram.height = 0.4
        peerlearning_instagram.width = 0.4
        peerlearning_instagram.move_to([-6, -2.5, 0])
        peerlearning_account = Text("peerlearning.bh",font=social_media_font, font_size=20)
        peerlearning_account.next_to(peerlearning_instagram, RIGHT)

        instagram_logo = SVGMobject("../../assets/images/IGLogo.svg", stroke_color=WHITE, fill_color=WHITE)
        instagram_logo.height = 0.4
        instagram_logo.width = 0.4
        instagram_logo.move_to([3, -2.5, 0])
        instagram_account = Text("abdallahtantawy",font=social_media_font, font_size=20)
        instagram_account.next_to(instagram_logo, RIGHT)

        github_logo = SVGMobject("../../assets/images/GitHubLogo.svg", stroke_color=WHITE, fill_color=WHITE)
        github_logo.height = 0.4
        github_logo.width = 0.4
        github_logo.next_to(instagram_logo, DOWN)
        github_account = Text("abdallah-t",font=social_media_font, font_size=20)
        github_account.next_to(github_logo, RIGHT)

        self.play(Write(peer_learning_logo))
        self.wait(0.5)
        self.play(peer_learning_logo.animate.shift(RIGHT * 4.5))
        font_arabic_logo.next_to(peer_learning_logo, LEFT)
        self.play(Write(font_arabic_logo, reverse=True))
        self.add(font_arabic_logo)
        
        self.play(Write(peerlearning_instagram))
        self.play(Write(peerlearning_account), run_time=0.5)
        self.play(Write(instagram_logo))
        self.play(Write(instagram_account), run_time=0.5)
        self.play(Write(github_logo))
        self.play(Write(github_account), run_time=0.5)
        self.wait()

        self.play(Unwrite(peer_learning_logo), Unwrite(font_arabic_logo), Unwrite(peerlearning_instagram), Unwrite(peerlearning_account), Unwrite(instagram_logo), Unwrite(instagram_account), Unwrite(github_logo), Unwrite(github_account))
        self.wait()


class Outro(Scene):
    def construct(self):
        outro = Text("شكراً لحضوركم", font=LOGO_FONT, font_size=70)
        self.play(Write(outro, reverse=True))
        self.add(outro)
        self.wait(2)
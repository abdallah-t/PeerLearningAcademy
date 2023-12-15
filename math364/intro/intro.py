from manim import *

color_scheme = {"فريق": "#fed966", "تعليم": "#a8d18d", "الأقران": "#f08362"},
LOGO_YELLOW = "#ffd966"
LOGO_GREEN = "#a9d18e"
LOGO_RED = "#f08462"
LOGO_FONT = "Vazirmatn Black"
LOGO_PURPLE = "#002060"
SOCIAL_MEDIA_FONT = "Space mono"
SOCIAL_MEDIA_LOGO_HEIGHT = 0.4
SOCIAL_MEDIA_LOGO_WIDTH = 0.4
class Logo(Scene):
    def construct(self):
        plane = NumberPlane()
        peer_learning_logo = SVGMobject("../../assets/images/svgs/logo_main.svg")
        
        
        markup = f'<span font_family="{LOGO_FONT}" foreground="{LOGO_YELLOW}">فريق</span><span font_family="{LOGO_FONT}" foreground="{LOGO_GREEN}"> تعليم</span><span font_family="{LOGO_FONT}" foreground="{LOGO_RED}"> الأقران</span>'
        font_arabic_logo = MarkupText(text=markup).scale(1.5)
        font_arabic_logo.next_to(peer_learning_logo, LEFT)
        

        instagram_logo_peerlearning = SVGMobject("../../assets/images/svgs/instagram_logo.svg", stroke_color=WHITE, fill_color=WHITE)
        instagram_logo_peerlearning.height = SOCIAL_MEDIA_LOGO_HEIGHT
        instagram_logo_peerlearning.width = SOCIAL_MEDIA_LOGO_WIDTH

        x_logo_peerlearning = SVGMobject("../../assets/images/svgs/x_logo.svg", stroke_color=WHITE, fill_color=WHITE)
        x_logo_peerlearning.height = SOCIAL_MEDIA_LOGO_HEIGHT
        x_logo_peerlearning.width = SOCIAL_MEDIA_LOGO_WIDTH

        youtube_logo_peerlearning = SVGMobject("../../assets/images/svgs/youtube.svg", stroke_color=WHITE, fill_color=WHITE, stroke_width=5)
        youtube_logo_peerlearning.height = SOCIAL_MEDIA_LOGO_HEIGHT
        youtube_logo_peerlearning.width = SOCIAL_MEDIA_LOGO_WIDTH
        
        tiktok_logo_peerlearning = SVGMobject("../../assets/images/svgs/tiktok_logo.svg", stroke_color=WHITE, fill_color=WHITE)
        tiktok_logo_peerlearning.height = SOCIAL_MEDIA_LOGO_HEIGHT
        tiktok_logo_peerlearning.width = SOCIAL_MEDIA_LOGO_WIDTH

        peerlearning_social_media_logos = VGroup(instagram_logo_peerlearning, x_logo_peerlearning, youtube_logo_peerlearning, tiktok_logo_peerlearning).arrange(RIGHT)
        peerlearning_social_media_logos.to_edge(DL, buff=1)

        peerlearning_account_name = Text("peerlearningbh",font=SOCIAL_MEDIA_FONT, font_size=20)
        peerlearning_account_name.next_to(peerlearning_social_media_logos, DOWN)
        peerlearning_social_media_logos.add(peerlearning_account_name)

        instagram_logo_abdallah = instagram_logo_peerlearning.copy()
        abdallah_account_name_instagram = Text("abdallahtantawy",font=SOCIAL_MEDIA_FONT, font_size=20)
        abdallah_account_name_instagram.next_to(instagram_logo_abdallah, RIGHT)

        github_logo_abdallah = SVGMobject("../../assets/images/svgs/github_logo.svg", stroke_color=WHITE, fill_color=WHITE)
        github_logo_abdallah.height = SOCIAL_MEDIA_LOGO_HEIGHT
        github_logo_abdallah.width = SOCIAL_MEDIA_LOGO_WIDTH
        github_logo_abdallah.next_to(instagram_logo_abdallah, DOWN)
        abdallah_github_account = Text("abdallah-t",font=SOCIAL_MEDIA_FONT, font_size=20)
        abdallah_github_account.next_to(github_logo_abdallah, RIGHT)
        
        abdallah_social_media = VGroup(instagram_logo_abdallah, github_logo_abdallah, abdallah_account_name_instagram, abdallah_github_account)
        abdallah_social_media.to_edge(DR, buff=1).align_to(peerlearning_social_media_logos, DOWN)


        self.play(Write(peer_learning_logo))
        self.wait(0.5)
        self.play(peer_learning_logo.animate.shift(RIGHT * 4.5))
        font_arabic_logo.next_to(peer_learning_logo, LEFT)
        self.play(Write(font_arabic_logo, reverse=True))
        self.add(font_arabic_logo)
        
        self.play(Write(peerlearning_social_media_logos))
        self.play(Write(instagram_logo_abdallah))
        self.play(Write(abdallah_account_name_instagram), run_time=0.5)
        self.play(Write(github_logo_abdallah))
        self.play(Write(abdallah_github_account), run_time=0.5)
        self.wait()

        self.play(Unwrite(peer_learning_logo), Unwrite(font_arabic_logo), Unwrite(peerlearning_account_name), Unwrite(instagram_logo_abdallah), Unwrite(peerlearning_social_media_logos), Unwrite(abdallah_social_media))
        self.wait()


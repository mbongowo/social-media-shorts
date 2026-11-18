from manim import *

config.frame_width = 8.0
config.frame_height = 14.22

INK = '#eaf2ef'
ACCENT = '#39d98a'
WARN = '#ff6b6b'
SKY = '#4aa8ff'
SAND = '#e8c268'
BG = '#0b1c17'

config.background_color = BG


def endcard(scene):
    title = Text('Maps, satellites & GeoAI', font_size=34, color=INK)
    title.scale_to_fit_width(config.frame_width * 0.82)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT)
    follow = Text('Follow for more', font_size=30, color=ACCENT)
    group = VGroup(title, line, follow).arrange(DOWN, buff=0.35)
    scene.play(FadeIn(group))
    scene.wait(1.5)


class ZipCodeUnique(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'Your zip code can\nname you.',
            font_size=58, color=INK, line_spacing=1.1
        )
        hook.scale_to_fit_width(config.frame_width * 0.86)
        hook.to_edge(UP, buff=0.9)
        self.add(hook)
        self.wait(1)

        setup = Text(
            'Three facts: zip code, gender,\nbirth date. No name attached.',
            font_size=32, color=INK, line_spacing=1.1
        )
        setup.scale_to_fit_width(config.frame_width * 0.82)
        setup.next_to(hook, DOWN, buff=0.7)
        self.play(FadeIn(setup))
        self.wait(1.5)

        n = 100
        cols = 10
        dots = VGroup()
        for i in range(n):
            d = Dot(radius=0.065, color=SKY)
            r, c = divmod(i, cols)
            d.move_to(RIGHT * (c - (cols - 1) / 2) * 0.62 + UP * (r - (n // cols - 1) / 2) * 0.62)
            dots.add(d)
        dots.scale_to_fit_width(config.frame_width * 0.82)
        dots.move_to(ORIGIN + DOWN * 0.3)

        self.play(FadeOut(setup))
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.01), run_time=1.5)
        self.wait(0.5)

        highlight_count = 87
        order = list(range(n))
        highlight_idx = order[:highlight_count]
        anims = [dots[i].animate.set_color(WARN) for i in highlight_idx]
        self.play(*anims, run_time=1.2)
        self.wait(0.5)

        badge = Text('87.1%', font_size=72, color=WARN)
        badge.scale_to_fit_width(config.frame_width * 0.5)
        badge_label = Text('of Americans, uniquely identified', font_size=26, color=INK)
        badge_label.scale_to_fit_width(config.frame_width * 0.78)
        badge_group = VGroup(badge, badge_label).arrange(DOWN, buff=0.15)
        badge_group.next_to(dots, DOWN, buff=0.55)
        self.play(FadeIn(badge_group))
        self.wait(2)

        self.play(FadeOut(dots), FadeOut(badge_group), FadeOut(hook))

        fact = Text(
            '1990 US census data: zip code + gender\n+ birth date alone was enough to name\n216 of 248 million people.',
            font_size=30, color=INK, line_spacing=1.2
        )
        fact.scale_to_fit_width(config.frame_width * 0.84)
        fact.move_to(UP * 2.0)
        self.play(FadeIn(fact))
        self.wait(2.5)

        source = Text('Sweeney, 2002, k-anonymity paper', font_size=22, color=SAND)
        source.scale_to_fit_width(config.frame_width * 0.78)
        source.next_to(fact, DOWN, buff=0.5)
        self.play(FadeIn(source))
        self.wait(1.5)

        self.play(FadeOut(fact), FadeOut(source))

        punch = Text(
            'Anonymous data is not\nas anonymous as it looks.',
            font_size=38, color=ACCENT, line_spacing=1.2
        )
        punch.scale_to_fit_width(config.frame_width * 0.84)
        punch.move_to(DOWN * 4.4)
        self.play(FadeIn(punch))
        self.wait(2)
        self.play(FadeOut(punch))

        endcard(self)

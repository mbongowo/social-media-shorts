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
    brand = Text('Maps, satellites & GeoAI', font_size=34, color=INK)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
    follow = Text('Follow for more', font_size=30, color=SAND)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.45)
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(1.4)


class ProjectionScoreCard(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'Scientists gave every\nworld map a distortion score',
            font_size=40,
            color=INK,
            line_spacing=1.15,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        base_y = -1.0
        max_h = 3.6
        merc_h = max_h * (8.296 / 8.296)
        wink_h = max_h * (4.563 / 8.296)

        merc_bar = Rectangle(width=1.7, height=0.02, color=WARN, fill_color=WARN, fill_opacity=1)
        merc_bar.move_to(LEFT * 1.6 + UP * base_y, aligned_edge=DOWN)
        wink_bar = Rectangle(width=1.7, height=0.02, color=ACCENT, fill_color=ACCENT, fill_opacity=1)
        wink_bar.move_to(RIGHT * 1.6 + UP * base_y, aligned_edge=DOWN)

        merc_label = Text('Mercator', font_size=28, color=INK).next_to(merc_bar, DOWN, buff=0.25)
        wink_label = Text('Winkel Tripel', font_size=28, color=INK).next_to(wink_bar, DOWN, buff=0.25)

        merc_score = Text('8.3', font_size=34, color=WARN, weight=BOLD)
        wink_score = Text('4.6', font_size=34, color=ACCENT, weight=BOLD)

        self.play(
            merc_bar.animate.stretch_to_fit_height(merc_h).move_to(LEFT * 1.6 + UP * base_y, aligned_edge=DOWN),
            wink_bar.animate.stretch_to_fit_height(wink_h).move_to(RIGHT * 1.6 + UP * base_y, aligned_edge=DOWN),
            run_time=1.3,
        )
        merc_score.next_to(merc_bar, UP, buff=0.2)
        wink_score.next_to(wink_bar, UP, buff=0.2)
        self.play(FadeIn(merc_label), FadeIn(wink_label), FadeIn(merc_score), FadeIn(wink_score))
        self.wait(0.6)

        lower_note = Text('Lower score = less distortion', font_size=24, color=SAND)
        lower_note.move_to(UP * 4.2)
        self.play(FadeIn(lower_note))
        self.wait(0.8)

        fact = Text(
            'Mercator distorts nearly 2x\nas much as Winkel Tripel',
            font_size=32,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.2)

        self.play(FadeOut(hook), FadeOut(merc_bar), FadeOut(wink_bar), FadeOut(merc_label),
                   FadeOut(wink_label), FadeOut(merc_score), FadeOut(wink_score),
                   FadeOut(lower_note), FadeOut(fact))

        punch = Text(
            'That is why National Geographic\nswitched maps in 1998',
            font_size=34,
            color=ACCENT,
            line_spacing=1.2,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(punch))

        endcard(self)

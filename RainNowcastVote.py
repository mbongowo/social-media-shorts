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


class RainNowcastVote(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            '51 experts graded 3 rain forecasts.\nAn AI won 89% of the time.',
            font_size=36,
            color=INK,
            line_spacing=1.2,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        rings = VGroup(*[
            Circle(radius=r, color=SKY, stroke_width=3, stroke_opacity=0.8 - i * 0.15)
            for i, r in enumerate([0.5, 0.9, 1.3])
        ]).move_to(UP * 3.4)
        dot = Dot(point=rings.get_center(), color=SKY, radius=0.08)
        self.play(*[Create(r) for r in rings], run_time=0.9)
        self.play(FadeIn(dot))

        raindrops = VGroup(*[
            Square(side_length=0.22, color=ACCENT, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0)
            for _ in range(9)
        ]).arrange_in_grid(rows=3, cols=3, buff=0.16).move_to(UP * 1.55)
        self.play(LaggedStart(*[FadeIn(sq, scale=0.6) for sq in raindrops], lag_ratio=0.08), run_time=1.1)
        self.wait(0.4)

        radar_label = Text('same radar data, 3 forecasting methods', font_size=22, color=INK).move_to(UP * 0.35)
        self.play(FadeIn(radar_label, shift=UP * 0.1))
        self.wait(0.8)

        self.play(
            FadeOut(rings), FadeOut(dot), FadeOut(raindrops), FadeOut(radar_label),
        )

        axis = Line(LEFT * 2.6 + DOWN * 0.6, RIGHT * 2.6 + DOWN * 0.6, color=INK, stroke_width=3)

        ai_bar = Rectangle(width=1.3, height=2.6, color=ACCENT, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0)
        ai_bar.next_to(axis.get_left() + RIGHT * 1.4, UP, buff=0, aligned_edge=DOWN)
        ai_label = Text('AI nowcast', font_size=22, color=INK).next_to(ai_bar, DOWN, buff=0.25)
        ai_pct = Text('89%', font_size=30, color=ACCENT, weight=BOLD).next_to(ai_bar, UP, buff=0.2)

        other_bar = Rectangle(width=1.3, height=0.32, color=WARN, fill_color=WARN, fill_opacity=0.9, stroke_width=0)
        other_bar.next_to(axis.get_left() + RIGHT * 3.8, UP, buff=0, aligned_edge=DOWN)
        other_label = Text('2 other methods', font_size=22, color=INK).next_to(other_bar, DOWN, buff=0.25)
        other_pct = Text('11%', font_size=30, color=WARN, weight=BOLD).next_to(other_bar, UP, buff=0.2)

        self.play(Create(axis))
        self.play(GrowFromEdge(ai_bar, DOWN), run_time=0.9)
        self.play(FadeIn(ai_label), FadeIn(ai_pct))
        self.play(GrowFromEdge(other_bar, DOWN), run_time=0.7)
        self.play(FadeIn(other_label), FadeIn(other_pct))
        self.wait(1.2)

        chart = VGroup(axis, ai_bar, ai_label, ai_pct, other_bar, other_label, other_pct)
        self.play(FadeOut(chart))

        fact = Text(
            'Judged blind against 2 rival methods,\nfor the next 90 minutes of rain,\nby Met Office meteorologists',
            font_size=26,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.6)

        self.play(FadeOut(hook), FadeOut(fact))

        punch = Text(
            'It never coded one equation\nof rain physics.\nIt just learned the patterns.',
            font_size=32,
            color=ACCENT,
            line_spacing=1.2,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(punch))

        endcard(self)

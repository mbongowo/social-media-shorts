from manim import *
import numpy as np

config.frame_width = 8.0
config.frame_height = 14.22

INK = '#eaf2ef'
ACCENT = '#39d98a'
WARN = '#ff6b6b'
SKY = '#4aa8ff'
SAND = '#e8c268'
BG = '#0b1c17'


def endcard(scene):
    scene.clear()
    brand = Text('Maps, satellites & GeoAI', color=INK, font_size=40)
    brand.scale_to_fit_width(config.frame_width * 0.85)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=6)
    line.next_to(brand, DOWN, buff=0.4)
    follow = Text('Follow for more', color=ACCENT, font_size=34)
    follow.next_to(line, DOWN, buff=0.4)
    group = VGroup(brand, line, follow).move_to(ORIGIN)
    scene.add(group)
    scene.wait(2)


class ZipfCityLaw(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "One formula predicts\nevery big US city's size",
            color=INK,
            font_size=38,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.3)
        self.add(hook)
        self.wait(1)

        label_rule = Text('Population = size of city #1, divided by rank', color=INK, font_size=22)
        label_rule.scale_to_fit_width(config.frame_width * 0.85)
        label_rule.move_to(UP * 3.5)
        self.play(FadeIn(label_rule), run_time=0.5)

        ranks = [1, 2, 3, 4, 5, 6]
        heights = [3.6 / r for r in ranks]
        bar_w = 0.95
        gap = 0.18
        n = len(ranks)
        total_w = n * bar_w + (n - 1) * gap
        start_x = -total_w / 2 + bar_w / 2

        bars = VGroup()
        labels = VGroup()
        base_y = 1.2
        for i, (r, h) in enumerate(zip(ranks, heights)):
            bar = Rectangle(
                width=bar_w,
                height=h,
                color=ACCENT,
                fill_color=ACCENT,
                fill_opacity=0.85,
                stroke_width=1.5,
            )
            x = start_x + i * (bar_w + gap)
            bar.move_to(np.array([x, base_y - h / 2 + 3.6 / 2, 0]))
            bars.add(bar)
            lab = Text(str(r), color=INK, font_size=20)
            lab.next_to(bar, DOWN, buff=0.15)
            labels.add(lab)

        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.12), run_time=1.4)
        self.play(FadeIn(labels), run_time=0.4)

        curve_pts = [bar.get_top() for bar in bars]
        curve = VMobject(color=SKY, stroke_width=4)
        curve.set_points_smoothly(curve_pts)
        self.play(Create(curve), run_time=0.9)

        rank_axis_label = Text('rank (1 = biggest city)', color=INK, font_size=18)
        rank_axis_label.next_to(bars, DOWN, buff=0.55)
        self.play(FadeIn(rank_axis_label), run_time=0.4)
        self.wait(1.0)

        self.play(
            FadeOut(bars), FadeOut(labels), FadeOut(curve),
            FadeOut(label_rule), FadeOut(rank_axis_label),
            run_time=0.4,
        )

        fact = Text(
            "135 largest US metro areas, 1991\ndata: population vs rank fits this\ncurve at 98.6 percent (R2 = 0.986)",
            color=INK,
            font_size=24,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "No planner drew this.\nCities sort themselves by rank.",
            color=WARN,
            font_size=30,
            line_spacing=1.1,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)
        self.play(FadeOut(fact), run_time=0.4)
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(hook), FadeOut(punch), run_time=0.4)
        endcard(self)

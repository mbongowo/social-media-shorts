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


class GraphCastWin(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "An AI now beats the world's\ntop weather forecast model",
            color=INK,
            font_size=34,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.3)
        self.add(hook)
        self.wait(1)

        label_setup = Text('Same 10 day forecast, graded on 1380 targets', color=INK, font_size=20)
        label_setup.scale_to_fit_width(config.frame_width * 0.85)
        label_setup.move_to(UP * 3.4)
        self.play(FadeIn(label_setup), run_time=0.5)

        cols, rows = 10, 10
        sq = 0.42
        gap = 0.07
        total_w = cols * sq + (cols - 1) * gap
        total_h = rows * sq + (rows - 1) * gap
        start_x = -total_w / 2 + sq / 2
        start_y = total_h / 2 - sq / 2 + 0.6

        squares = VGroup()
        order = [(r, c) for r in range(rows) for c in range(cols)]
        for idx, (r, c) in enumerate(order):
            is_win = idx < 90
            color = ACCENT if is_win else WARN
            s = Square(side_length=sq, color=color, fill_color=color, fill_opacity=0.9, stroke_width=1)
            x = start_x + c * (sq + gap)
            y = start_y - r * (sq + gap)
            s.move_to(np.array([x, y, 0]))
            squares.add(s)

        self.play(LaggedStartMap(FadeIn, squares, lag_ratio=0.01), run_time=1.6)

        legend_win = Text('green = AI more accurate', color=ACCENT, font_size=18)
        legend_lose = Text('red = old model more accurate', color=WARN, font_size=18)
        legend = VGroup(legend_win, legend_lose).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legend.next_to(squares, DOWN, buff=0.5)
        self.play(FadeIn(legend), run_time=0.5)
        self.wait(1.2)

        self.play(FadeOut(squares), FadeOut(legend), FadeOut(label_setup), run_time=0.4)

        fact = Text(
            "GraphCast beat ECMWF's HRES\non 90 percent of 1380 forecast\ntargets across 10 days, 2023",
            color=INK,
            font_size=24,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "No physics equations.\nJust patterns learned from\ndecades of past weather.",
            color=WARN,
            font_size=28,
            line_spacing=1.15,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)
        self.play(FadeOut(fact), run_time=0.4)
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(hook), FadeOut(punch), run_time=0.4)
        endcard(self)

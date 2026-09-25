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


class SnowCloudCheck(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "A satellite decides if it\nsnowed where you live",
            color=INK,
            font_size=38,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.3)
        self.add(hook)
        self.wait(1)

        no_snow_fill = '#173028'
        pattern = [
            1, 0, 0, 1, 0,
            0, 1, 1, 0, 0,
            1, 0, 1, 0, 1,
            0, 0, 1, 0, 0,
            1, 1, 0, 0, 1,
        ]
        wrong_indices = [7, 18]

        cell = 1.15
        gap = 0.12
        squares = VGroup()
        for row in range(5):
            for col in range(5):
                idx = row * 5 + col
                is_snow = pattern[idx] == 1
                sq = Square(
                    side_length=cell,
                    color=INK,
                    stroke_width=1.5,
                    fill_color=(SKY if is_snow else no_snow_fill),
                    fill_opacity=0.9,
                )
                sq.move_to(np.array([
                    (col - 2) * (cell + gap),
                    (2 - row) * (cell + gap) + 0.2,
                    0,
                ]))
                squares.add(sq)

        label_check = Text('A satellite scans a grid of pixels', color=INK, font_size=22)
        label_check.scale_to_fit_width(config.frame_width * 0.82)
        label_check.next_to(squares, UP, buff=0.35)
        self.play(FadeIn(label_check), run_time=0.4)
        self.play(LaggedStart(*[FadeIn(sq) for sq in squares], lag_ratio=0.03), run_time=1.2)
        self.wait(0.5)

        marks = VGroup()
        for idx in wrong_indices:
            box = SurroundingRectangle(squares[idx], color=WARN, stroke_width=4, buff=0.02)
            marks.add(box)
        label_wrong = Text('2 of these 25 calls are wrong', color=WARN, font_size=22)
        label_wrong.scale_to_fit_width(config.frame_width * 0.82)
        label_wrong.next_to(squares, DOWN, buff=0.35)
        self.play(Create(marks), FadeIn(label_wrong), run_time=0.8)
        self.wait(1.3)

        self.play(
            FadeOut(squares), FadeOut(marks), FadeOut(label_check), FadeOut(label_wrong),
            run_time=0.4,
        )

        fact = Text(
            "NASA's MODIS satellite maps snow\ncover worldwide every day. Clear-sky\naccuracy measures about 93 percent",
            color=INK,
            font_size=24,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "The other 7 percent?\nUsually a cloud, not snow.",
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

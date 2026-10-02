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


class FlanneryFix(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "A map circle scaled by\nthe exact math looks too small",
            color=INK,
            font_size=32,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.3)
        self.add(hook)
        self.wait(1)

        label_setup = Text('Two circles. The right one holds 4x the data', color=INK, font_size=19)
        label_setup.scale_to_fit_width(config.frame_width * 0.85)
        label_setup.move_to(UP * 3.4)
        self.play(FadeIn(label_setup), run_time=0.5)

        base_r = 0.45
        math_r = base_r * 2.0
        flannery_r = base_r * (4.0 ** 0.5716)

        small = Circle(radius=base_r, color=SKY, fill_color=SKY, fill_opacity=0.85, stroke_width=1)
        small.move_to(LEFT * 1.8 + UP * 0.9)
        small_label = Text('value = 1', color=INK, font_size=18)
        small_label.next_to(small, DOWN, buff=0.3)

        big = Circle(radius=math_r, color=SAND, fill_color=SAND, fill_opacity=0.85, stroke_width=1)
        big.move_to(RIGHT * 1.3 + UP * 0.9)
        big_val_label = Text('value = 4', color=INK, font_size=18)
        big_val_label.next_to(big, DOWN, buff=0.3)
        big_radius_label = Text('radius, math: 2.0x', color=SAND, font_size=18)
        big_radius_label.next_to(big_val_label, DOWN, buff=0.15)

        self.play(FadeIn(small), FadeIn(small_label), run_time=0.5)
        self.play(FadeIn(big), FadeIn(big_val_label), FadeIn(big_radius_label), run_time=0.6)
        self.wait(1.2)

        big_flannery = Circle(radius=flannery_r, color=ACCENT, fill_color=ACCENT, fill_opacity=0.85, stroke_width=1)
        big_flannery.move_to(big.get_center())
        new_radius_label = Text('radius, Flannery: 2.21x', color=ACCENT, font_size=18)
        new_radius_label.move_to(big_radius_label.get_center())

        self.play(
            Transform(big, big_flannery),
            Transform(big_radius_label, new_radius_label),
            run_time=1.0,
        )
        self.wait(1.3)

        self.play(FadeOut(small), FadeOut(small_label), FadeOut(big),
                  FadeOut(big_val_label), FadeOut(big_radius_label),
                  FadeOut(label_setup), run_time=0.4)

        fact = Text(
            "Flannery, 1971: viewers see big\ncircles as smaller than they are,\nso maps scale radius by value^0.57,\nnot the exact value^0.5",
            color=INK,
            font_size=23,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.8)

        punch = Text(
            "The 'exaggerated' circle\nis the one your eyes\nactually read as true",
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

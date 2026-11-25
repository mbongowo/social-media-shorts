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

config.background_color = BG


def endcard(scene):
    brand = Text('Maps, satellites & GeoAI', font_size=34, color=INK)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
    follow = Text('Follow for more', font_size=30, color=SAND)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.45)
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(1.4)


class MagneticPoleDrift(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'Your compass does not\npoint at a fixed spot',
            font_size=38,
            color=INK,
            line_spacing=1.2,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        center = np.array([0.0, 2.4, 0.0])
        radius = 2.6

        def point_on_circle(deg):
            rad = deg * DEGREES
            return center + radius * np.array([np.cos(rad), np.sin(rad), 0.0])

        pole_circle = Circle(radius=radius, color=INK, stroke_width=2).move_to(center)

        fixed_ring = Circle(radius=0.14, color=SAND, stroke_width=3).move_to(center)
        fixed_dot = Dot(point=center, radius=0.05, color=SAND, fill_opacity=1)
        true_label = Text('True north, fixed', font_size=20, color=SAND)
        true_label.next_to(center, UP, buff=0.35)

        self.play(Create(pole_circle), run_time=0.8)
        self.play(FadeIn(fixed_ring), FadeIn(fixed_dot), FadeIn(true_label))
        self.wait(0.5)

        start = point_on_circle(150)
        end = point_on_circle(40)

        mag_dot = Dot(point=start, radius=0.09, color=WARN, fill_opacity=1)
        mag_label_1999 = Text('1999', font_size=20, color=WARN)
        mag_label_1999.next_to(mag_dot, LEFT, buff=0.2)

        self.play(FadeIn(mag_dot), FadeIn(mag_label_1999))
        self.wait(0.6)

        track = DashedLine(start, end, color=WARN, stroke_width=3, dash_length=0.08)
        self.play(Create(track), run_time=1.0)
        self.play(mag_dot.animate.move_to(end), run_time=1.2)
        mag_label_2019 = Text('2019', font_size=20, color=WARN)
        mag_label_2019.next_to(mag_dot, RIGHT, buff=0.2)
        self.play(FadeIn(mag_label_2019))
        self.wait(0.8)

        self.play(FadeOut(true_label), FadeOut(mag_label_1999))

        fact = Text(
            '1999 to 2019 it moved 1,104 km\ntoward Siberia. 87% traces to\none stretching lobe of core flux\nunder Canada',
            font_size=25,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(2.0)

        self.play(
            FadeOut(hook), FadeOut(fact), FadeOut(pole_circle),
            FadeOut(fixed_ring), FadeOut(fixed_dot),
            FadeOut(mag_dot), FadeOut(mag_label_2019), FadeOut(track),
        )

        punch = Text(
            'Maps hold still.\nThe pole does not.',
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

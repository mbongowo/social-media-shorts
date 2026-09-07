from manim import *
import random

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


class HotspotZTest(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'That red map "hotspot"\nmight just be random',
            font_size=38,
            color=INK,
            line_spacing=1.2,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        random.seed(7)
        dots = VGroup()
        cluster_dots = VGroup()
        for _ in range(50):
            x = random.uniform(-2.9, 2.9)
            y = random.uniform(1.6, 3.6)
            d = Dot(point=[x, y, 0], radius=0.05, color=INK, fill_opacity=0.55)
            dots.add(d)
        for _ in range(9):
            x = random.uniform(-0.7, 0.9)
            y = random.uniform(2.3, 3.1)
            d = Dot(point=[x, y, 0], radius=0.06, color=WARN, fill_opacity=0.9)
            cluster_dots.add(d)

        self.play(FadeIn(dots), run_time=0.8)
        self.wait(0.2)
        ring = Circle(radius=1.05, color=WARN, stroke_width=3).move_to([0.1, 2.7, 0])
        self.play(FadeIn(cluster_dots), Create(ring), run_time=0.8)
        looks_label = Text('looks like a hotspot', font_size=22, color=WARN).next_to(ring, DOWN, buff=0.25)
        self.play(FadeIn(looks_label, shift=UP * 0.1))
        self.wait(1.0)
        self.play(FadeOut(looks_label))

        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 1, 1],
            x_length=5.6,
            y_length=1.8,
            axis_config={'color': INK, 'stroke_width': 2, 'include_tip': False},
        ).move_to(DOWN * 0.6)
        bell = axes.plot(lambda x: 2.5 * (2.71828 ** (-0.5 * x * x)), color=SKY, stroke_width=4)

        cutoff_x = axes.c2p(1.96, 0)[0]
        cutoff_line = DashedLine(
            [cutoff_x, axes.get_bottom()[1], 0],
            [cutoff_x, axes.get_top()[1] + 0.3, 0],
            color=SAND,
            stroke_width=3,
            dash_length=0.1,
        )
        z_label = Text('z = 1.96', font_size=20, color=SAND).next_to(cutoff_line, UP, buff=0.1)

        self.play(
            FadeOut(dots), FadeOut(cluster_dots), FadeOut(ring),
            Create(axes), Create(bell),
            run_time=1.0,
        )
        self.play(Create(cutoff_line), FadeIn(z_label))
        conf_label = Text('under 5% odds: random', font_size=20, color=SAND).next_to(axes, DOWN, buff=0.3)
        self.play(FadeIn(conf_label, shift=UP * 0.1))
        self.wait(1.2)

        fact = Text(
            'Getis-Ord Gi* only calls it\na hotspot past z = 1.96,\nunder 5% odds of pure chance',
            font_size=26,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.6)

        self.play(
            FadeOut(hook), FadeOut(fact),
            FadeOut(axes), FadeOut(bell), FadeOut(cutoff_line),
            FadeOut(z_label), FadeOut(conf_label),
        )

        punch = Text(
            'Red because randomness\ncannot explain it.\nNot because it looks scary.',
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

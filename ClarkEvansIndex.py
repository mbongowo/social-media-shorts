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
    title = Text('Maps, satellites & GeoAI', font_size=40, color=INK)
    line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT)
    follow = Text('Follow for more', font_size=32, color=ACCENT)
    group = VGroup(title, line, follow).arrange(DOWN, buff=0.4)
    scene.add(group)
    scene.wait(2)


class ClarkEvansIndex(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "ONE NUMBER DECIDES IF DOTS\nON A MAP ARE REALLY CLUSTERED",
            font_size=40,
            color=INK,
            line_spacing=1.2,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        setup = Text(
            "Compare each point's nearest neighbor\nto what pure random chance predicts",
            font_size=26,
            color=INK,
            line_spacing=1.2,
        )
        setup.scale_to_fit_width(config.frame_width * 0.85)
        setup.move_to(UP * 2.9)
        self.play(FadeIn(setup))
        self.wait(1)

        axis = NumberLine(
            x_range=[0, 2.4, 0.5],
            length=6.0,
            color=INK,
            include_numbers=False,
        )
        axis.move_to(DOWN * 0.6)
        self.play(Create(axis))
        self.wait(0.3)

        clustered_pt = axis.n2p(0.0)
        random_pt = axis.n2p(1.0)
        max_pt = axis.n2p(2.1491)

        clustered_dots = VGroup(*[
            Dot(point=np.array([dx * 0.1, dy * 0.1, 0]), radius=0.035, color=WARN)
            for dx in range(-2, 3) for dy in range(-2, 3)
        ])
        clustered_dots.move_to(clustered_pt + UP * 1.5)

        rng = np.random.default_rng(7)
        random_dots = VGroup(*[
            Dot(point=np.array([rng.uniform(-0.45, 0.45), rng.uniform(-0.45, 0.45), 0]),
                radius=0.035, color=SAND)
            for _ in range(16)
        ])
        random_dots.move_to(random_pt + UP * 1.5)

        hex_dots = VGroup()
        for row in range(-2, 3):
            for col in range(-2, 3):
                offset = 0.15 if row % 2 == 0 else 0.0
                hex_dots.add(Dot(point=np.array([col * 0.3 + offset, row * 0.26, 0]),
                                  radius=0.035, color=ACCENT))
        hex_dots.move_to(max_pt + UP * 1.5)

        clustered_label = Text("R = 0", font_size=24, color=WARN)
        clustered_label.next_to(clustered_dots, DOWN, buff=0.3)
        random_label = Text("R = 1.0", font_size=24, color=SAND)
        random_label.next_to(random_dots, DOWN, buff=0.3)
        max_label = Text("R = 2.1491", font_size=24, color=ACCENT)
        max_label.next_to(hex_dots, DOWN, buff=0.3)

        self.play(FadeIn(clustered_dots), FadeIn(clustered_label))
        self.wait(0.4)
        self.play(FadeIn(random_dots), FadeIn(random_label))
        self.wait(0.4)
        self.play(FadeIn(hex_dots), FadeIn(max_label))
        self.wait(1)

        ceiling_note = Text("2.1491 is the mathematical ceiling", font_size=24, color=ACCENT)
        ceiling_note.scale_to_fit_width(config.frame_width * 0.85)
        ceiling_note.move_to(DOWN * 3.0)
        self.play(FadeIn(ceiling_note))
        self.wait(1.2)

        self.play(
            FadeOut(setup), FadeOut(axis),
            FadeOut(clustered_dots), FadeOut(random_dots), FadeOut(hex_dots),
            FadeOut(clustered_label), FadeOut(random_label),
            FadeOut(max_label), FadeOut(ceiling_note),
        )

        fact = Text(
            "Clark and Evans, 1954: R is observed spacing\ndivided by the spacing random chance predicts.\nPerfect hexagon spacing tops out at 2.1491,\nthe most spread out points can ever be.",
            font_size=26,
            color=INK,
            line_spacing=1.25,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact))
        self.wait(2.5)

        punch = Text(
            "So before you call a map clustered,\nthe math already set the bar in 1954.",
            font_size=28,
            color=ACCENT,
            line_spacing=1.25,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(DOWN * 4.4)
        self.play(FadeOut(fact), FadeIn(punch))
        self.wait(2)
        self.play(FadeOut(punch), FadeOut(hook))

        endcard(self)

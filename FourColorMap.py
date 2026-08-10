from manim import *

config.frame_width = 8.0
config.frame_height = 14.22

INK = '#eaf2ef'
ACCENT = '#39d98a'
WARN = '#ff6b6b'
SKY = '#4aa8ff'
SAND = '#e8c268'
BG = '#0b1c17'


def endcard(scene):
    brand = Text('Maps, satellites & GeoAI', font_size=30, color=INK)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT)
    follow = Text('Follow for more', font_size=26, color=ACCENT)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.35)
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(0.9)


class FourColorMap(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'No map ever\nneeds a 5th color',
            font_size=54,
            color=INK,
            line_spacing=1.1,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 5.6)
        self.play(FadeIn(hook, shift=DOWN * 0.2))
        self.wait(0.6)

        center = Circle(radius=0.8, color=SAND, fill_opacity=1, stroke_width=2, stroke_color=BG)
        center.move_to(ORIGIN)

        wedge_colors = [ACCENT, WARN, SKY]
        wedges = VGroup()
        outer_r = 2.0
        for i, col in enumerate(wedge_colors):
            sector = AnnularSector(
                inner_radius=1.0,
                outer_radius=outer_r,
                angle=TAU / 3,
                start_angle=i * TAU / 3 + PI / 2,
                arc_center=center.get_center(),
                color=col,
                fill_opacity=1,
                stroke_width=2,
                stroke_color=BG,
            )
            wedges.add(sector)

        self.play(FadeIn(center, scale=0.8))
        self.wait(0.2)
        self.play(LaggedStart(*[FadeIn(w, scale=0.9) for w in wedges], lag_ratio=0.25))
        self.wait(0.3)

        label = Text('4 regions.\nEvery pair touches.', font_size=30, color=INK, line_spacing=1.1)
        label.scale_to_fit_width(config.frame_width * 0.85)
        label.move_to(UP * 3.1)
        self.play(FadeIn(label))
        self.wait(0.8)
        self.play(FadeOut(label))

        fact = Text(
            'Proven in 1976 - the first major\ntheorem checked by computer,\nnot by hand',
            font_size=30,
            color=INK,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.2)

        punch = Text(
            'Four colors.\nInfinite borders.\nZero exceptions.',
            font_size=36,
            color=ACCENT,
            line_spacing=1.15,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)

        self.play(
            FadeOut(hook),
            FadeOut(fact),
            FadeOut(VGroup(center, wedges)),
        )
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.0)
        self.play(FadeOut(punch))

        endcard(self)

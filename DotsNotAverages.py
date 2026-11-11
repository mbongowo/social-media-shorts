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
    title = Text('Maps, satellites & GeoAI', font_size=34, color=INK)
    line = Line(LEFT * 2, RIGHT * 2, color=ACCENT)
    follow = Text('Follow for more', font_size=30, color=ACCENT)
    group = VGroup(title, line, follow).arrange(DOWN, buff=0.4)
    scene.play(FadeIn(group))
    scene.wait(1.2)


class DotsNotAverages(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Your census map is\nguessing where people live.",
            font_size=40, color=INK, line_spacing=1.15
        ).scale_to_fit_width(config.frame_width * 0.85)
        hook.move_to(UP * 5.4)
        self.add(hook)
        self.wait(1)

        county = RoundedRectangle(width=5.0, height=3.6, corner_radius=0.2,
                                   color=INK, stroke_width=3).move_to(UP * 1.2)

        even_dots = VGroup(*[
            Dot(radius=0.07, color=SKY).move_to(
                county.get_center() + np.array([x, y, 0])
            )
            for x in np.linspace(-2.0, 2.0, 6)
            for y in np.linspace(-1.3, 1.3, 5)
        ])

        setup = Text("Areal weighting: spread population\nevenly across the whole polygon",
                      font_size=24, color=INK, line_spacing=1.1
                      ).scale_to_fit_width(config.frame_width * 0.82)
        setup.next_to(county, DOWN, buff=0.35)

        self.play(Create(county), run_time=0.8)
        self.play(FadeIn(setup), run_time=0.6)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in even_dots], lag_ratio=0.02), run_time=1.6)
        self.wait(0.6)

        self.play(FadeOut(setup))
        label1 = Text("Error: 21.2%", font_size=30, color=WARN).next_to(county, DOWN, buff=0.35)
        self.play(FadeIn(label1))
        self.wait(1.0)

        self.play(FadeOut(even_dots), FadeOut(label1))

        real_points = [
            [-1.8, 1.0, 0], [-1.7, 0.85, 0], [-1.65, 1.05, 0],
            [0.25, 0.7, 0], [0.45, 0.85, 0], [0.55, 0.55, 0], [0.35, 0.4, 0],
            [1.6, -0.35, 0], [1.7, -0.2, 0], [1.5, -0.5, 0], [1.75, -0.4, 0],
            [-0.9, -0.85, 0], [-0.7, -1.0, 0],
            [0.1, -1.1, 0],
        ]
        addr_dots = VGroup(*[
            Dot(radius=0.08, color=ACCENT).move_to(county.get_center() + np.array(p))
            for p in real_points
        ])

        setup2 = Text("Dasymetric mapping: place people\nat real address points instead",
                       font_size=24, color=INK, line_spacing=1.1
                       ).scale_to_fit_width(config.frame_width * 0.82)
        setup2.next_to(county, DOWN, buff=0.35)
        self.play(FadeIn(setup2))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in addr_dots], lag_ratio=0.05), run_time=1.4)
        self.wait(0.6)
        self.play(FadeOut(setup2))

        label2 = Text("Error: 4.9%", font_size=30, color=ACCENT).next_to(county, DOWN, buff=0.35)
        self.play(FadeIn(label2))
        self.wait(1.0)

        self.play(FadeOut(county), FadeOut(addr_dots), FadeOut(label2), FadeOut(hook))

        fact = Text(
            "683 Ohio block groups: using\naddress points cut population\nerror from 21.2% to 4.9%\n(Zandbergen, 2011)",
            font_size=30, color=INK, line_spacing=1.15
        ).scale_to_fit_width(config.frame_width * 0.86)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact))
        self.wait(2.0)

        self.play(FadeOut(fact))

        punch = Text(
            "Same census data.\nJust moved the dots\nto where people live.",
            font_size=34, color=SAND, line_spacing=1.2
        ).scale_to_fit_width(config.frame_width * 0.85)
        self.play(FadeIn(punch))
        self.wait(1.6)
        self.play(FadeOut(punch))

        endcard(self)

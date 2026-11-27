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
    title = Text("Maps, satellites & GeoAI", font_size=34, color=INK)
    title.scale_to_fit_width(config.frame_width * 0.82)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT)
    follow = Text("Follow for more", font_size=30, color=ACCENT)
    follow.scale_to_fit_width(config.frame_width * 0.6)
    group = VGroup(title, line, follow).arrange(DOWN, buff=0.4)
    scene.add(group)
    scene.wait(1.4)


class MethaneFromSpace(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "A satellite caught\n1,800 invisible gas leaks.",
            font_size=42,
            color=INK,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.86)
        hook.to_edge(UP, buff=0.9)
        self.add(hook)
        self.wait(1)

        setup = Text(
            "TROPOMI: a spectrometer in orbit\nthat reads gas by its light signature.",
            font_size=28,
            color=SAND,
            line_spacing=1.1,
        )
        setup.scale_to_fit_width(config.frame_width * 0.82)
        setup.next_to(hook, DOWN, buff=0.7)
        self.play(FadeIn(setup))
        self.wait(1.2)
        self.play(FadeOut(setup))

        ground = Rectangle(width=3.0, height=0.5, color=INK, fill_color=INK, fill_opacity=0.25)
        ground.move_to(DOWN * 0.8)
        flare = Triangle(color=WARN, fill_color=WARN, fill_opacity=0.6).scale(0.18)
        flare.next_to(ground, UP, buff=0.0).shift(LEFT * 0.9)

        plume = Polygon(
            [-0.4, 0, 0], [0.4, 0, 0], [1.3, 3.2, 0], [-1.3, 3.2, 0],
            color=WARN, fill_color=WARN, fill_opacity=0.22, stroke_width=0,
        )
        plume.move_to(flare.get_center() + UP * 1.6)

        orbit = DashedLine(LEFT * 3.4, RIGHT * 3.4, color=SKY, stroke_width=2)
        orbit.move_to(UP * 3.6)
        sat = Square(side_length=0.3, color=SKY, fill_color=SKY, fill_opacity=0.9)
        sat.move_to(RIGHT * 1.8 + UP * 3.6)
        beam = DashedLine(flare.get_center(), sat.get_center(), color=SKY, stroke_width=2)

        scene_group = VGroup(ground, flare, plume, orbit, sat, beam)
        self.play(
            FadeIn(ground), FadeIn(flare),
            Create(orbit), FadeIn(sat),
        )
        self.play(GrowFromPoint(plume, flare.get_center()), Create(beam))
        self.wait(1.4)
        self.play(FadeOut(scene_group))

        badge = Text("25+ tonnes/hour, each one", font_size=30, color=ACCENT)
        badge.scale_to_fit_width(config.frame_width * 0.78)
        badge.move_to(ORIGIN)
        self.play(FadeIn(badge))
        self.wait(1.4)
        self.play(FadeOut(badge))

        fact = Text(
            "TROPOMI spotted them from orbit,\n2019 to 2020 (Lauvaux et al., Science 2022).\n"
            "The oil and gas leaks alone equal 8 to 12%\nof the sector's reported methane\nin six top producing nations,\nmissing from official counts.",
            font_size=26,
            color=INK,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.86)
        fact.move_to(DOWN * 3.8)
        self.play(FadeIn(fact))
        self.wait(3.2)
        self.play(FadeOut(fact))

        punch = Text("The leak was invisible.\nSpace saw it anyway.", font_size=36, color=ACCENT, line_spacing=1.1)
        punch.scale_to_fit_width(config.frame_width * 0.82)
        punch.move_to(ORIGIN)
        self.play(FadeIn(punch))
        self.wait(1.6)
        self.play(FadeOut(punch))

        endcard(self)

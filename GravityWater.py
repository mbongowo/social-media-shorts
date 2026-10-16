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
    brand = Text('Maps, satellites & GeoAI', font_size=34, color=INK)
    line = Line(LEFT * 2.6, RIGHT * 2.6, color=ACCENT, stroke_width=5)
    follow = Text('Follow for more', font_size=30, color=ACCENT)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.45)
    scene.play(FadeIn(group))
    scene.wait(1.2)


class GravityWater(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Satellites can weigh\nunderground water from space",
            font_size=46,
            color=INK,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.9)
        hook.to_edge(UP, buff=0.9)

        self.add(hook)
        self.wait(1)

        setup = Text(
            "Two GRACE satellites fly 220 km apart,\ntracking tiny changes in Earth's gravity",
            font_size=28,
            color=SKY,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.85)
        setup.move_to(UP * 3.6)
        self.play(FadeIn(setup))
        self.wait(1.5)

        sat1 = Dot(radius=0.14, color=SAND).move_to(LEFT * 1.3 + UP * 1.9)
        sat2 = Dot(radius=0.14, color=SAND).move_to(RIGHT * 1.3 + UP * 1.9)
        link = DashedLine(sat1.get_center(), sat2.get_center(), color=SAND, stroke_width=3)
        sat_label = Text("measuring the tiny gap\nbetween them", font_size=22, color=SAND, line_spacing=1.1)
        sat_label.next_to(VGroup(sat1, sat2, link), DOWN, buff=0.35)

        ground = Rectangle(width=6.2, height=1.4, color=INK, fill_color=BG, fill_opacity=1, stroke_width=2)
        ground.move_to(DOWN * 0.6)
        water_level = Rectangle(width=6.0, height=0.9, color=SKY, fill_color=SKY, fill_opacity=0.5, stroke_width=0)
        water_level.move_to(ground.get_bottom() + UP * 0.45)

        satellites = VGroup(sat1, sat2, link, sat_label)
        self.play(FadeIn(sat1), FadeIn(sat2), Create(link), FadeIn(sat_label))
        self.play(FadeIn(ground), FadeIn(water_level))
        self.wait(1)

        self.play(FadeOut(setup))

        shrink = water_level.copy().stretch_to_fit_height(0.35, about_edge=DOWN)
        self.play(Transform(water_level, shrink), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(satellites))

        region_label = Text("Rajasthan, Punjab, Haryana, Delhi\n2002 to 2008", font_size=24, color=SAND, line_spacing=1.1)
        region_label.move_to(DOWN * 2.7)
        self.play(FadeIn(region_label))
        self.wait(1)

        fact = Text(
            "That region lost 17.7 cubic km\nof groundwater every year",
            font_size=34,
            color=WARN,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.9)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact))
        self.wait(1.5)

        punch = Text(
            "No pump was ever measured.\nGravity gave it away.",
            font_size=30,
            color=ACCENT,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.85)
        punch.next_to(fact, DOWN, buff=0.4)
        self.play(FadeIn(punch))
        self.wait(2)

        self.play(FadeOut(VGroup(hook, ground, water_level, region_label, fact, punch)))
        endcard(self)

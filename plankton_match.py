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


class PlanktonMatch(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Invisible ocean cells\nmatch every plant on land",
            color=INK,
            font_size=46,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        sat_body = Rectangle(width=0.5, height=0.3, color=SAND, fill_color=SAND, fill_opacity=1)
        sat_panel_l = Rectangle(width=0.5, height=0.15, color=SKY, fill_color=SKY, fill_opacity=1).next_to(sat_body, LEFT, buff=0.05)
        sat_panel_r = Rectangle(width=0.5, height=0.15, color=SKY, fill_color=SKY, fill_opacity=1).next_to(sat_body, RIGHT, buff=0.05)
        satellite = VGroup(sat_body, sat_panel_l, sat_panel_r).move_to(UP * 2.9)
        self.play(FadeIn(satellite), run_time=0.6)

        beam = DashedLine(satellite.get_bottom(), satellite.get_bottom() + DOWN * 1.3, color=SKY, stroke_width=3)
        self.play(Create(beam), run_time=0.6)

        ocean_bar = Rectangle(width=1.4, height=3.4, color=SKY, fill_color=SKY, fill_opacity=0.85)
        land_bar = Rectangle(width=1.4, height=3.95, color=ACCENT, fill_color=ACCENT, fill_opacity=0.85)
        bars = VGroup(ocean_bar, land_bar).arrange(RIGHT, buff=1.0, aligned_edge=DOWN)
        bars.move_to(DOWN * 0.6)

        ocean_label = Text('Ocean\nphytoplankton', color=SKY, font_size=26, line_spacing=1.0).next_to(ocean_bar, DOWN, buff=0.25)
        land_label = Text('Land\nplants', color=ACCENT, font_size=26, line_spacing=1.0).next_to(land_bar, DOWN, buff=0.25)

        ocean_value = Text('48.5', color=INK, font_size=30).next_to(ocean_bar, UP, buff=0.2)
        land_value = Text('56.4', color=INK, font_size=30).next_to(land_bar, UP, buff=0.2)

        self.play(
            GrowFromEdge(ocean_bar, DOWN),
            GrowFromEdge(land_bar, DOWN),
            run_time=1.2,
        )
        self.play(
            FadeIn(ocean_label), FadeIn(land_label),
            FadeIn(ocean_value), FadeIn(land_value),
            run_time=0.6,
        )
        self.wait(0.6)

        unit = Text('billion tonnes of carbon fixed per year', color=INK, font_size=24)
        unit.scale_to_fit_width(config.frame_width * 0.85)
        unit.next_to(bars, DOWN, buff=1.5)
        self.play(FadeIn(unit), run_time=0.5)
        self.wait(1.0)

        self.play(FadeOut(satellite), FadeOut(beam), FadeOut(unit), run_time=0.4)

        fact = Text(
            "Satellites reading ocean color show phytoplankton\nfix almost as much carbon as every plant on land",
            color=INK,
            font_size=28,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.4)

        punch = Text(
            "Half of Earth's plant engine\nruns in cells too small to see",
            color=WARN,
            font_size=32,
            line_spacing=1.1,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)
        self.play(FadeOut(bars), FadeOut(ocean_label), FadeOut(land_label), FadeOut(ocean_value), FadeOut(land_value), FadeOut(fact), run_time=0.4)
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(hook), FadeOut(punch), run_time=0.4)
        endcard(self)

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


class SubPixelFire(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "One satellite pixel covers\na million square metres",
            color=INK,
            font_size=44,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        sat_body = Rectangle(width=0.5, height=0.3, color=SAND, fill_color=SAND, fill_opacity=1)
        sat_panel_l = Rectangle(width=0.5, height=0.15, color=SKY, fill_color=SKY, fill_opacity=1).next_to(sat_body, LEFT, buff=0.05)
        sat_panel_r = Rectangle(width=0.5, height=0.15, color=SKY, fill_color=SKY, fill_opacity=1).next_to(sat_body, RIGHT, buff=0.05)
        satellite = VGroup(sat_body, sat_panel_l, sat_panel_r).move_to(UP * 3.1)
        self.play(FadeIn(satellite), run_time=0.6)

        beam = DashedLine(satellite.get_bottom(), satellite.get_bottom() + DOWN * 1.1, color=SKY, stroke_width=3)
        self.play(Create(beam), run_time=0.6)

        pixel = Square(side_length=3.4, color=INK, stroke_width=3)
        pixel.move_to(UP * 0.3)
        pixel_label = Text('1 pixel: 1 km x 1 km', color=INK, font_size=24).next_to(pixel, UP, buff=0.25)
        self.play(Create(pixel), FadeIn(pixel_label), run_time=0.9)
        self.wait(0.4)

        fire = Square(side_length=0.22, color=WARN, fill_color=WARN, fill_opacity=1)
        fire.move_to(pixel.get_center() + RIGHT * 0.9 + DOWN * 0.7)
        fire_label = Text('1,000 m2 fire', color=WARN, font_size=22).next_to(fire, DOWN, buff=0.3)
        self.play(FadeIn(fire, scale=0.3), FadeIn(fire_label), run_time=0.7)
        self.wait(0.8)

        ratio = Text('1,000x smaller than the pixel', color=SAND, font_size=24)
        ratio.scale_to_fit_width(config.frame_width * 0.82)
        ratio.next_to(pixel, DOWN, buff=1.1)
        self.play(FadeIn(ratio), run_time=0.5)
        self.wait(1.1)

        self.play(
            FadeOut(satellite), FadeOut(beam), FadeOut(ratio),
            run_time=0.4,
        )

        fact = Text(
            "MODIS satellites still catch flaming\nor smoldering fires as small as 1,000 m2,\nbecause the heat overwhelms the pixel",
            color=INK,
            font_size=26,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.9)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.5)

        punch = Text(
            "You do not have to fill the pixel.\nJust burn hot enough to stand out.",
            color=WARN,
            font_size=32,
            line_spacing=1.1,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)
        self.play(
            FadeOut(pixel), FadeOut(pixel_label), FadeOut(fire), FadeOut(fire_label), FadeOut(fact),
            run_time=0.4,
        )
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(hook), FadeOut(punch), run_time=0.4)
        endcard(self)

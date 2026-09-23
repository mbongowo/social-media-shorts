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


class GeoidGap(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Sea level dips 106 meters here,\nwith no hill in sight",
            color=INK,
            font_size=38,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.3)
        self.add(hook)
        self.wait(1)

        panel = Rectangle(
            width=config.frame_width * 0.88,
            height=5.0,
            color=SKY,
            fill_color=SKY,
            fill_opacity=0.06,
            stroke_width=2,
        )
        panel.move_to(UP * 0.4)
        self.play(FadeIn(panel), run_time=0.5)

        ref_y = 1.6
        ref_line = DashedLine(
            LEFT * 3.3 + UP * ref_y,
            RIGHT * 3.3 + UP * ref_y,
            color=INK,
            stroke_width=2,
            dash_length=0.15,
        )
        label_ref = Text('Ellipsoid: the smooth shape maps assume', color=INK, font_size=20)
        label_ref.scale_to_fit_width(config.frame_width * 0.82)
        label_ref.next_to(ref_line, UP, buff=0.2)
        self.play(Create(ref_line), FadeIn(label_ref), run_time=0.8)
        self.wait(0.5)

        depth = 1.8
        sigma = 0.9

        def geoid_y(x):
            dip = depth * np.exp(-((x) ** 2) / (2 * sigma ** 2))
            ripple = 0.05 * np.sin(x * 4.0)
            return ref_y - dip + ripple

        geoid = ParametricFunction(
            lambda t: np.array([t, geoid_y(t), 0]),
            t_range=[-3.3, 3.3, 0.05],
            color=ACCENT,
            stroke_width=4,
        )
        label_geoid = Text('Geoid: true sea level, shaped by gravity', color=ACCENT, font_size=20)
        label_geoid.scale_to_fit_width(config.frame_width * 0.82)
        label_geoid.next_to(panel, DOWN, buff=0.25)
        self.play(Create(geoid), run_time=1.2)
        self.play(FadeIn(label_geoid), run_time=0.4)
        self.wait(0.6)

        bottom_y = geoid_y(0.0)
        gap_arrow = DoubleArrow(
            start=np.array([0.0, ref_y, 0]),
            end=np.array([0.0, bottom_y, 0]),
            color=WARN,
            stroke_width=3,
            buff=0,
            tip_length=0.15,
        )
        gap_label = Text('106 m', color=WARN, font_size=28)
        gap_label.next_to(gap_arrow, RIGHT, buff=0.15)
        self.play(GrowFromCenter(gap_arrow), FadeIn(gap_label), run_time=0.6)
        self.wait(1.4)

        self.play(
            FadeOut(panel), FadeOut(ref_line), FadeOut(label_ref),
            FadeOut(geoid), FadeOut(label_geoid), FadeOut(gap_arrow), FadeOut(gap_label),
            run_time=0.4,
        )

        fact = Text(
            "Earth's gravity is lumpy. South of India\nthe geoid sags 106m below the ellipsoid\nGPS and maps use, over 3 million km2",
            color=INK,
            font_size=24,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "No hill made that dip.\nGravity did.",
            color=WARN,
            font_size=32,
            line_spacing=1.1,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)
        self.play(FadeOut(fact), run_time=0.4)
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(hook), FadeOut(punch), run_time=0.4)
        endcard(self)

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


class PreHarvestAI(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "AI forecasts crop yields\nbefore the harvest, from space",
            color=INK,
            font_size=42,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        field = Rectangle(width=3.2, height=2.0, color=ACCENT, fill_color='#123024', fill_opacity=1)
        field.move_to(UP * 2.4)
        rows = VGroup()
        for i in range(5):
            for j in range(7):
                dot = Dot(radius=0.05, color=ACCENT)
                dot.move_to(field.get_corner(UL) + RIGHT * (0.3 + j * 0.44) + DOWN * (0.3 + i * 0.4))
                rows.add(dot)
        self.play(Create(field), run_time=0.6)
        self.play(FadeIn(rows), run_time=0.7)

        sat_body = Rectangle(width=0.5, height=0.3, color=SAND, fill_color=SAND, fill_opacity=1)
        sat_panel_l = Rectangle(width=0.5, height=0.15, color=SKY, fill_color=SKY, fill_opacity=1).next_to(sat_body, LEFT, buff=0.05)
        sat_panel_r = Rectangle(width=0.5, height=0.15, color=SKY, fill_color=SKY, fill_opacity=1).next_to(sat_body, RIGHT, buff=0.05)
        satellite = VGroup(sat_body, sat_panel_l, sat_panel_r).move_to(field.get_top() + UP * 0.8)
        self.play(FadeIn(satellite), run_time=0.5)

        beam = DashedLine(satellite.get_bottom(), field.get_center(), color=SKY, stroke_width=3)
        self.play(Create(beam), run_time=0.6)
        scan_label = Text('Weekly satellite scans', color=SKY, font_size=22).next_to(field, LEFT, buff=0.3).rotate(PI / 2)
        self.wait(0.6)

        self.play(
            FadeOut(satellite), FadeOut(beam), FadeOut(field), FadeOut(rows),
            run_time=0.4,
        )

        axis_line = Line(LEFT * 2.6 + DOWN * 1.0, RIGHT * 2.6 + DOWN * 1.0, color=INK, stroke_width=3)
        axis_line.move_to(UP * 0.4)
        bar_old = Rectangle(width=0.9, height=2.2, color=SKY, fill_color=SKY, fill_opacity=1)
        bar_old.move_to(axis_line.get_center() + LEFT * 1.3 + UP * 1.1)
        bar_new = Rectangle(width=0.9, height=1.54, color=ACCENT, fill_color=ACCENT, fill_opacity=1)
        bar_new.move_to(axis_line.get_center() + RIGHT * 1.3 + UP * 0.77)
        label_old = Text('Traditional\nsatellite model', color=SKY, font_size=20, line_spacing=1.1).next_to(bar_old, DOWN, buff=0.2)
        label_new = Text('Deep Gaussian\nProcess model', color=ACCENT, font_size=20, line_spacing=1.1).next_to(bar_new, DOWN, buff=0.2)
        err_label = Text('yield error (RMSE)', color=INK, font_size=18).next_to(axis_line, UP, buff=2.6)

        self.play(Create(axis_line), run_time=0.3)
        self.play(GrowFromEdge(bar_old, DOWN), FadeIn(label_old), run_time=0.7)
        self.play(GrowFromEdge(bar_new, DOWN), FadeIn(label_new), run_time=0.7)
        self.play(FadeIn(err_label), run_time=0.4)

        pct = Text('-30% error', color=WARN, font_size=30)
        pct.next_to(bar_new, UP, buff=0.3)
        self.play(FadeIn(pct, scale=0.5), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(axis_line), FadeOut(bar_old), FadeOut(bar_new),
            FadeOut(label_old), FadeOut(label_new), FadeOut(err_label), FadeOut(pct),
            run_time=0.4,
        )

        fact = Text(
            "Stanford's deep model cut US county\nsoybean yield error 30% versus\ntraditional satellite methods (You et al., 2017)",
            color=INK,
            font_size=24,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.9)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "See the harvest coming,\nweeks before it comes in.",
            color=ACCENT,
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

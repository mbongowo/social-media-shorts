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
    bg = Rectangle(width=config.frame_width, height=config.frame_height, color=BG, fill_color=BG, fill_opacity=1)
    title = Text('Maps, satellites & GeoAI', font_size=34, color=INK, weight=BOLD)
    title.scale_to_fit_width(config.frame_width * 0.85)
    line = Line(LEFT * 1.6, RIGHT * 1.6, color=ACCENT, stroke_width=5)
    line.next_to(title, DOWN, buff=0.35)
    follow = Text('Follow for more', font_size=30, color=ACCENT, weight=BOLD)
    follow.next_to(line, DOWN, buff=0.35)
    group = VGroup(title, line, follow)
    scene.add(bg)
    scene.play(FadeIn(group))
    scene.wait(1.5)


class SeaLevelSpeedsUp(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height, color=BG, fill_color=BG, fill_opacity=1)
        self.add(bg)

        hook = VGroup(
            Text('THE OCEAN IS NOT JUST RISING', font_size=46, color=INK, weight=BOLD),
            Text('IT IS SPEEDING UP', font_size=46, color=ACCENT, weight=BOLD),
        ).arrange(DOWN, buff=0.18)
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)

        self.add(hook)
        self.wait(1)

        setup = Text('25 years of radar satellites timed the sea surface', font_size=26, color=INK)
        setup.scale_to_fit_width(config.frame_width * 0.85)
        setup.move_to(UP * 3.2)
        self.play(FadeIn(setup))
        self.wait(1)

        sat_dot = Dot(point=UP * 2.0, radius=0.12, color=SKY)
        sat_label = Text('radar satellite', font_size=20, color=SKY)
        sat_label.next_to(sat_dot, UP, buff=0.15)
        pulse = DashedLine(UP * 1.85, DOWN * 0.3, color=SKY, stroke_width=3)
        ocean = Line(LEFT * 2.6 + DOWN * 0.5, RIGHT * 2.6 + DOWN * 0.5, color=ACCENT, stroke_width=5)
        ocean_label = Text('sea surface', font_size=20, color=ACCENT)
        ocean_label.next_to(ocean, DOWN, buff=0.2)
        echo_label = Text('bounce the echo, time its return', font_size=24, color=INK)
        echo_label.scale_to_fit_width(config.frame_width * 0.82)
        echo_label.move_to(UP * 0.9)

        mech_group = VGroup(sat_dot, sat_label, pulse, ocean, ocean_label, echo_label)
        self.play(FadeIn(sat_dot), FadeIn(sat_label), Create(pulse), run_time=1.2)
        self.play(Create(ocean), FadeIn(ocean_label), FadeIn(echo_label))
        self.wait(1.3)

        self.play(FadeOut(mech_group), FadeOut(setup))

        start = np.array([-2.6, -0.9, 0])
        end_straight = np.array([1.9, 0.9, 0])
        axis_x = Line(start + LEFT * 0.25, end_straight + RIGHT * 0.35 + DOWN * 0.1, color=INK, stroke_width=2)
        axis_x.set_opacity(0.35)
        axis_y = Line(start + DOWN * 0.2, start + UP * 3.2, color=INK, stroke_width=2)
        axis_y.set_opacity(0.35)

        dashed_ref = DashedLine(start, end_straight, color=SAND, stroke_width=4)

        xs = np.linspace(0, 1, 60)
        bend_height = 1.0
        curve_points = []
        for xf in xs:
            xc = start[0] + xf * (end_straight[0] - start[0])
            yc = start[1] + xf * (end_straight[1] - start[1]) + (xf ** 2) * bend_height
            curve_points.append(np.array([xc, yc, 0]))
        curve = VMobject(color=ACCENT, stroke_width=6)
        curve.set_points_smoothly(curve_points)

        y1993 = Text('1993', font_size=22, color=SAND)
        y1993.next_to(start, DOWN, buff=0.2)
        y2018 = Text('2018', font_size=22, color=SAND)
        y2018.next_to(end_straight, DOWN, buff=0.2)

        gap_line = Line(end_straight, curve_points[-1], color=WARN, stroke_width=4)

        swatch1 = DashedLine(LEFT * 0.45, RIGHT * 0.45, color=SAND, stroke_width=5)
        label1 = Text('steady-rate forecast', font_size=24, color=SAND)
        legend_row1 = VGroup(swatch1, label1).arrange(RIGHT, buff=0.25)

        swatch2 = Line(LEFT * 0.45, RIGHT * 0.45, color=ACCENT, stroke_width=6)
        label2 = Text('actual, accelerating', font_size=24, color=ACCENT, weight=BOLD)
        legend_row2 = VGroup(swatch2, label2).arrange(RIGHT, buff=0.25)

        legend = VGroup(legend_row1, legend_row2).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        if legend.width > config.frame_width * 0.78:
            legend.scale_to_fit_width(config.frame_width * 0.78)
        legend.move_to(DOWN * 2.6)

        self.play(Create(axis_x), Create(axis_y))
        self.play(FadeIn(y1993), FadeIn(y2018))
        self.play(Create(dashed_ref), FadeIn(legend_row1))
        self.wait(0.5)
        self.play(Create(curve), FadeIn(legend_row2), run_time=2)
        self.play(FadeIn(gap_line))
        self.wait(1.5)

        graph_group = VGroup(
            axis_x, axis_y, dashed_ref, curve, y1993, y2018, legend, gap_line,
        )

        fact = Text(
            'Satellite radar found the rise speeding up by\nabout 0.084 mm per year, every year, since 1993',
            font_size=25, color=INK, line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact))
        self.wait(2)

        self.play(FadeOut(graph_group))

        punch = Text('Keep that curve going and 2100 could\nbring 65 cm, not a straight line\'s guess', font_size=30,
                      color=ACCENT, weight=BOLD, line_spacing=1.2)
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(UP * 0.3)
        self.play(FadeIn(punch))
        self.wait(2)

        self.play(FadeOut(hook), FadeOut(fact), FadeOut(punch), FadeOut(bg))
        endcard(self)

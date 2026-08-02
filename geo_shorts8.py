from manim import *

config.frame_width = 8.0
config.frame_height = 14.22
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = "#0b1c17"

INK = "#eaf2ef"
ACCENT = "#39d98a"
WARN = "#ff6b6b"
SKY = "#4aa8ff"
SAND = "#e8c268"
BG = "#0b1c17"


def endcard(scene):
    title = Text("Maps, satellites & GeoAI", font_size=32, color=INK, weight=BOLD)
    line = Line(LEFT * 2, RIGHT * 2, color=ACCENT, stroke_width=4)
    sub = Text("Follow for more", font_size=26, color=ACCENT, weight=BOLD)
    group = VGroup(title, line, sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)
    scene.play(FadeIn(group, scale=1.05), run_time=0.8)
    scene.wait(1.3)
    scene.play(FadeOut(group), run_time=0.5)


class SunSyncOrbit(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("Satellites plan their\nphotos to the minute.", font_size=32, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.6)

        sub = Text(
            "So images taken months\napart still match\nin light and shadow.",
            font_size=26, color=SKY, weight=BOLD, line_spacing=1.25,
        ).next_to(hook, DOWN, buff=0.6)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.9)
        self.wait(1.0)
        self.play(FadeOut(sub), run_time=0.4)

        earth = Circle(radius=1.3, color=SKY, fill_color=SKY, fill_opacity=0.25, stroke_width=3).move_to(UP * 0.6)
        orbit = Ellipse(width=3.6, height=3.6 * 2.6, color=ACCENT, stroke_width=2.5).move_to(UP * 0.6).rotate(0.06 * PI)
        sat = Dot(radius=0.11, color=INK).move_to(earth.get_top() + UP * 0.15)
        sun_ray = Arrow(LEFT * 3.4 + UP * 0.6, earth.get_left(), color=SAND, stroke_width=3, buff=0.05)
        sun_label = Text("sunlight", font_size=18, color=SAND).next_to(sun_ray, UP, buff=0.1)

        self.play(FadeIn(earth), run_time=0.6)
        self.play(Create(orbit), run_time=1.0)
        self.play(FadeIn(sat), GrowArrow(sun_ray), Write(sun_label), run_time=0.8)
        self.play(MoveAlongPath(sat, orbit), run_time=1.6, rate_func=linear)
        self.wait(0.6)
        self.play(FadeOut(VGroup(earth, orbit, sat, sun_ray, sun_label)), run_time=0.6)

        fact = Text(
            "Landsat crosses the equator\nnear 10:00 local time on\nevery pass, circling pole\nto pole at about 705 km,\nkeeping the sun angle steady.",
            font_size=24, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text("Same sun angle,\nevery single pass.", font_size=32, color=ACCENT, weight=BOLD, line_spacing=1.25).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class BitDepthSecret(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("Your screen shows 256\nshades of gray.", font_size=32, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.6)
        sub = Text("Satellites record\nthousands more.", font_size=28, color=WARN, weight=BOLD, line_spacing=1.2).next_to(hook, DOWN, buff=0.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.8)
        self.wait(0.9)
        self.play(FadeOut(sub), run_time=0.4)

        coarse = VGroup(*[
            Square(side_length=0.42, stroke_width=0.5, stroke_color=BG,
                   fill_color=interpolate_color(ManimColor(BG), ManimColor(INK), i / 7), fill_opacity=1)
            for i in range(8)
        ]).arrange(RIGHT, buff=0.0).move_to(UP * 1.6)
        coarse_label = Text("8-bit: 256 levels", font_size=20, color=SAND).next_to(coarse, UP, buff=0.25)

        fine = VGroup(*[
            Square(side_length=0.19, stroke_width=0.2, stroke_color=BG,
                   fill_color=interpolate_color(ManimColor(BG), ManimColor(ACCENT), i / 17), fill_opacity=1)
            for i in range(18)
        ]).arrange(RIGHT, buff=0.0).move_to(DOWN * 0.4)
        fine_label = Text("12-bit: 4096 levels", font_size=20, color=ACCENT).next_to(fine, UP, buff=0.25)

        self.play(FadeIn(coarse, shift=UP * 0.2), Write(coarse_label), run_time=1.0)
        self.wait(0.7)
        self.play(FadeIn(fine, shift=UP * 0.2), Write(fine_label), run_time=1.0)
        self.wait(1.1)
        self.play(FadeOut(VGroup(coarse, coarse_label, fine, fine_label)), run_time=0.6)

        fact = Text(
            "Landsat 8 records each\npixel at 12-bit depth,\n4096 brightness levels,\nnot the 256 a normal\nphoto uses.",
            font_size=25, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text("More shades caught\nmeans subtler change seen.", font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.25).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class ClassBreaksLie(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("Same data.\nThree different maps.", font_size=34, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.8)
        self.play(FadeOut(hook), run_time=0.4)

        values = [1, 2, 2, 3, 3, 3, 4, 4, 5, 9]

        def make_row(colors, label_text, label_color):
            row = VGroup(*[
                Square(side_length=0.55, stroke_width=1, stroke_color=BG, fill_color=c, fill_opacity=1)
                for c in colors
            ]).arrange(RIGHT, buff=0.06)
            label = Text(label_text, font_size=19, color=label_color).next_to(row, LEFT, buff=0.3)
            return VGroup(label, row).arrange(RIGHT, buff=0.3)

        equal_colors = [SKY if v <= 5 else WARN for v in values]
        quantile_colors = [SKY if v <= 3 else (SAND if v <= 4 else WARN) for v in values]
        natural_colors = [SKY if v <= 4 else (SAND if v == 5 else WARN) for v in values]

        row1 = make_row(equal_colors, "equal interval", SKY).move_to(UP * 2.6)
        row2 = make_row(quantile_colors, "quantile", SAND).move_to(UP * 1.2)
        row3 = make_row(natural_colors, "natural breaks", ACCENT).move_to(UP * -0.2)

        self.play(FadeIn(row1, shift=UP * 0.2), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(row2, shift=UP * 0.2), run_time=0.8)
        self.wait(0.6)
        self.play(FadeIn(row3, shift=UP * 0.2), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(VGroup(row1, row2, row3)), run_time=0.6)

        fact = Text(
            "Equal interval, quantile,\nand natural breaks slice the\nsame numbers into different\ncolor bins, and the map's\nstory changes with them.",
            font_size=24, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text("The bins are a choice.\nThe data never changed.", font_size=30, color=ACCENT, weight=BOLD, line_spacing=1.25).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class ImageChipping(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("AI can't see the whole\nsatellite image at once.", font_size=30, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.7)
        self.play(FadeOut(hook), run_time=0.4)

        big = Square(side_length=4.2, stroke_color=SKY, stroke_width=3, fill_opacity=0).move_to(UP * 1.0)
        big_label = Text("one huge scene", font_size=20, color=SKY).next_to(big, UP, buff=0.2)
        self.play(Create(big), Write(big_label), run_time=1.0)
        self.wait(0.6)

        grid = VGroup(*[
            Square(side_length=1.0, stroke_color=ACCENT, stroke_width=1.5,
                   fill_color=ACCENT, fill_opacity=0.18)
            for _ in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=0.05).move_to(big.get_center())
        self.play(FadeIn(grid, lag_ratio=0.05), run_time=1.3)
        self.wait(0.6)

        chip = grid[5].copy().set_fill(opacity=0.6).scale(1.15)
        chip_label = Text("one chip: 256 x 256 px", font_size=18, color=ACCENT).next_to(big, DOWN, buff=0.5)
        self.play(Transform(grid[5], chip), Write(chip_label), run_time=0.9)
        self.wait(1.0)
        self.play(FadeOut(VGroup(big, big_label, grid, chip_label)), run_time=0.6)

        fact = Text(
            "Huge scenes get cut into\nsmall tiles, often 256 by\n256 pixels, fed to the model\none chip at a time, then\nstitched back into one map.",
            font_size=23, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text("The model never sees\nthe whole picture at once.", font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.25).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class RareClassTrap(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("A model that finds\nzero floods can still\nscore 98% accuracy.", font_size=30, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.1)
        self.wait(1.0)
        self.play(FadeOut(hook), run_time=0.4)

        grid = VGroup(*[
            Square(side_length=0.5, stroke_width=0.5, stroke_color=BG, fill_color=SKY, fill_opacity=0.5)
            for _ in range(100)
        ]).arrange_in_grid(rows=10, cols=10, buff=0.03).move_to(UP * 1.0)

        flood_indices = [12, 34, 57]
        for i in flood_indices:
            grid[i].set_fill(WARN, opacity=1)

        label_no = Text("no flood (98%)", font_size=18, color=SKY).next_to(grid, UP, buff=0.25)
        label_yes = Text("flood (2%)", font_size=18, color=WARN).next_to(grid, DOWN, buff=0.25)

        self.play(FadeIn(grid, lag_ratio=0.01), run_time=1.3)
        self.play(Write(label_no), Write(label_yes), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(VGroup(grid, label_no, label_yes)), run_time=0.6)

        fact = Text(
            "If flooded pixels are only\n2% of a scene, guessing\n'no flood' everywhere already\nwins on accuracy, while\nmissing every real flood.",
            font_size=24, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text("That's why precision\nand recall matter more.", font_size=30, color=ACCENT, weight=BOLD, line_spacing=1.25).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class QuadtreeIndex(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("Finding the nearest\ncoffee shop shouldn't check\nevery building on Earth.", font_size=27, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.1)
        self.wait(1.0)
        self.play(FadeOut(hook), run_time=0.4)

        outer = Square(side_length=4.4, stroke_color=SKY, stroke_width=2.5).move_to(UP * 1.0)
        self.play(Create(outer), run_time=0.8)
        self.wait(0.4)

        h1 = Line(outer.get_left(), outer.get_right(), stroke_color=ACCENT, stroke_width=2)
        v1 = Line(outer.get_top(), outer.get_bottom(), stroke_color=ACCENT, stroke_width=2)
        self.play(Create(h1), Create(v1), run_time=0.8)
        self.wait(0.3)

        quad_size = 4.4 / 2
        top_right = outer.get_center() + UP * (quad_size / 2) + RIGHT * (quad_size / 2)
        h2 = Line(top_right + LEFT * (quad_size / 2), top_right + RIGHT * (quad_size / 2), stroke_color=SAND, stroke_width=1.5)
        v2 = Line(top_right + UP * (quad_size / 2), top_right + DOWN * (quad_size / 2), stroke_color=SAND, stroke_width=1.5)
        self.play(Create(h2), Create(v2), run_time=0.7)

        dot = Dot(radius=0.08, color=WARN).move_to(top_right + UP * 0.35 + RIGHT * 0.2)
        dot_label = Text("target", font_size=16, color=WARN).next_to(dot, RIGHT, buff=0.15)
        self.play(FadeIn(dot), Write(dot_label), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(VGroup(outer, h1, v1, h2, v2, dot, dot_label)), run_time=0.6)

        fact = Text(
            "Spatial indexes like quadtrees\nand R-trees split space into\nnested boxes, so a search\nskips most of the data\ninstead of scanning it all.",
            font_size=23, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text("Less searching,\nsame right answer.", font_size=31, color=ACCENT, weight=BOLD, line_spacing=1.25).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)

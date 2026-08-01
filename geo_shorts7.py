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


class ResolutionTradeoff(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("Sharp OR fast.\nNever both.", font_size=36, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.6)

        sub = Text(
            "Every satellite trades\nspatial detail for\nhow often it comes back.",
            font_size=27, color=SKY, weight=BOLD, line_spacing=1.25,
        ).next_to(hook, DOWN, buff=0.6)
        self.play(FadeIn(sub, shift=UP * 0.3), run_time=0.9)
        self.wait(1.0)
        self.play(FadeOut(sub), run_time=0.4)

        fine_grid = VGroup(*[
            Square(side_length=0.28, stroke_color=ACCENT, stroke_width=1, fill_color=ACCENT, fill_opacity=0.25)
            for _ in range(36)
        ]).arrange_in_grid(rows=6, cols=6, buff=0.03)
        coarse_grid = VGroup(*[
            Square(side_length=0.85, stroke_color=SAND, stroke_width=1, fill_color=SAND, fill_opacity=0.25)
            for _ in range(4)
        ]).arrange_in_grid(rows=2, cols=2, buff=0.05)

        grids = VGroup(fine_grid, coarse_grid).arrange(DOWN, buff=1.0).move_to(UP * 0.9)
        fine_label = Text("30m detail, every 16 days", font_size=20, color=ACCENT).next_to(fine_grid, UP, buff=0.25)
        coarse_label = Text("1km blur, every 10 minutes", font_size=20, color=SAND).next_to(coarse_grid, DOWN, buff=0.25)

        self.play(FadeIn(fine_grid, shift=UP * 0.2), Write(fine_label), run_time=1.0)
        self.play(FadeIn(coarse_grid, shift=UP * 0.2), Write(coarse_label), run_time=1.0)
        self.wait(1.1)
        self.play(FadeOut(VGroup(grids, fine_label, coarse_label)), run_time=0.5)

        fact = Text(
            "Landsat resolves 30 meters\nbut revisits every 16 days.\nWeather satellites scan the\nwhole planet every 10 minutes\nat about 1km per pixel.",
            font_size=25, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text("Every satellite is a\ntrade you signed up for.", font_size=30, color=ACCENT, weight=BOLD, line_spacing=1.25).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.0)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class AtmosphereBlur(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("Your satellite photo\nhas a photobomber.", font_size=32, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.7)
        self.play(FadeOut(hook), run_time=0.4)

        sun = Circle(radius=0.4, color=SAND, fill_color=SAND, fill_opacity=1).move_to(UP * 5.0 + LEFT * 2.2)
        sat = Square(side_length=0.5, color=INK, fill_color=INK, fill_opacity=1).move_to(UP * 5.0 + RIGHT * 2.2)

        haze = Rectangle(width=6.0, height=1.4, fill_color=SKY, fill_opacity=0.3, stroke_width=0).move_to(UP * 1.8)
        haze_label = Text("atmosphere: gas + haze", font_size=18, color=SKY).next_to(haze, UP, buff=0.15)

        ground = Rectangle(width=6.0, height=0.4, fill_color="#123326", fill_opacity=1, stroke_width=0).move_to(DOWN * 1.2)

        self.play(FadeIn(sun), FadeIn(sat), FadeIn(ground), run_time=0.8)
        self.play(FadeIn(haze), Write(haze_label), run_time=0.8)

        down_arrow = Arrow(sun.get_bottom(), ground.get_top() + LEFT * 1.5, color=SAND, stroke_width=3, buff=0.1)
        up_arrow = Arrow(ground.get_top() + LEFT * 1.5, sat.get_bottom(), color=SKY, stroke_width=3, buff=0.1)
        self.play(GrowArrow(down_arrow), run_time=0.7)
        self.play(GrowArrow(up_arrow), run_time=0.7)
        self.wait(1.0)
        self.play(FadeOut(VGroup(sun, sat, haze, haze_label, ground, down_arrow, up_arrow)), run_time=0.6)

        fact = Text(
            "Sunlight crosses the\natmosphere twice before it\nreaches the sensor, scattered\nand absorbed by gas and haze\nalong the way.",
            font_size=25, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text(
            "Atmospheric correction wipes\nthe sky's fingerprints off\nso the ground shows through.",
            font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.25,
        ).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class CoastlineParadox(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("How long is a\ncoastline?", font_size=36, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.5)
        sub = Text("Trick question.", font_size=30, color=WARN, weight=BOLD).next_to(hook, DOWN, buff=0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.5)

        coarse_pts = [(-2.6, 0), (-1.0, 1.1), (0.6, -0.6), (2.6, 0.8)]
        coarse_line = VMobject(color=SAND, stroke_width=5)
        coarse_line.set_points_as_corners([[x, y, 0] for x, y in coarse_pts])
        coarse_label = Text("big ruler: short path", font_size=20, color=SAND).move_to(UP * 3.0)

        self.play(Write(coarse_label), run_time=0.6)
        self.play(Create(coarse_line), run_time=1.2)
        self.wait(0.9)
        self.play(FadeOut(coarse_line), FadeOut(coarse_label), run_time=0.5)

        import random
        random.seed(7)
        fine_pts = []
        n = 24
        for i in range(n + 1):
            x = -2.6 + 5.2 * i / n
            base_y = 0.3 * (i % 4 - 1.5)
            jitter = 0.35 * ((-1) ** i)
            fine_pts.append((x, base_y + jitter))
        fine_line = VMobject(color=ACCENT, stroke_width=4)
        fine_line.set_points_as_corners([[x, y, 0] for x, y in fine_pts])
        fine_label = Text("small ruler: longer path", font_size=20, color=ACCENT).move_to(UP * 3.0)

        self.play(Write(fine_label), run_time=0.6)
        self.play(Create(fine_line), run_time=1.6)
        self.wait(1.0)
        self.play(FadeOut(fine_line), FadeOut(fine_label), run_time=0.5)

        fact = Text(
            "Measure a coastline with a\nsmaller ruler and it gets\nlonger, every time,\nwith no limit in theory.",
            font_size=26, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text(
            "Zoom in far enough and\nthe coastline never finishes\ndrawing itself.",
            font_size=29, color=ACCENT, weight=BOLD, line_spacing=1.25,
        ).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class DomainShift(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text("This AI aced\nCalifornia.", font_size=34, color=INK, weight=BOLD, line_spacing=1.2)
        hook.move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.5)
        sub = Text("Then it saw Kenya.", font_size=32, color=WARN, weight=BOLD).next_to(hook, DOWN, buff=0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.8)
        self.wait(0.9)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.5)

        region_a = VGroup(*[
            Square(side_length=0.5, stroke_color=ACCENT, stroke_width=1, fill_color=ACCENT, fill_opacity=0.35)
            for _ in range(9)
        ]).arrange_in_grid(rows=3, cols=3, buff=0.06)
        label_a = Text("trained here", font_size=18, color=ACCENT).next_to(region_a, UP, buff=0.2)
        group_a = VGroup(region_a, label_a).move_to(UP * 2.5)

        check = Text("check", font_size=22, color=ACCENT, weight=BOLD).move_to(UP * 2.5 + RIGHT * 2.8)

        self.play(FadeIn(group_a), run_time=0.9)
        self.play(FadeIn(check, scale=1.2), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(check), run_time=0.3)
        self.play(FadeOut(group_a), run_time=0.5)

        region_b = VGroup(*[
            Square(side_length=0.5, stroke_color=SAND, stroke_width=1, fill_color=SAND, fill_opacity=0.35)
            for _ in range(9)
        ]).arrange_in_grid(rows=3, cols=3, buff=0.06)
        label_b = Text("applied here", font_size=18, color=SAND).next_to(region_b, UP, buff=0.2)
        group_b = VGroup(region_b, label_b).move_to(UP * 2.5)

        cross = Cross(scale_factor=0.9, stroke_color=WARN, stroke_width=6).move_to(UP * 2.5 + RIGHT * 2.8)

        self.play(FadeIn(group_b), run_time=0.9)
        self.play(Create(cross), run_time=0.6)
        self.wait(1.0)
        self.play(FadeOut(VGroup(group_b, cross)), run_time=0.6)

        fact = Text(
            "A GeoAI model trained on one\nregion's imagery can lose\nreal accuracy when it sees a\nnew landscape, sensor, or\nseason without adaptation.",
            font_size=24, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text(
            "The map isn't the problem.\nThe training data's\nhometown is.",
            font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.25,
        ).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class VectorRaster(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Every map you've seen\nis secretly one of\ntwo things.",
            font_size=30, color=INK, weight=BOLD, line_spacing=1.2,
        ).move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.1)
        self.wait(0.9)
        self.play(FadeOut(hook), run_time=0.5)

        vec_dots = VGroup(*[Dot(radius=0.06, color=ACCENT) for _ in range(4)])
        vec_pts = [(-1.0, 0.6), (-0.3, 1.0), (0.4, -0.2), (1.0, 0.5)]
        for dot, (x, y) in zip(vec_dots, vec_pts):
            dot.move_to([x, y, 0])
        vec_line = VMobject(color=ACCENT, stroke_width=3)
        vec_line.set_points_as_corners([[x, y, 0] for x, y in vec_pts])
        vec_label = Text("vector\npoints, lines, shapes", font_size=18, color=ACCENT, line_spacing=1.2)
        vec_group = VGroup(vec_line, vec_dots, vec_label.next_to(VGroup(vec_line, vec_dots), DOWN, buff=0.4))
        vec_group.move_to(UP * 2.6 + LEFT * 1.9)

        ras_grid = VGroup(*[
            Square(side_length=0.42, stroke_color=SAND, stroke_width=1,
                   fill_color=SAND, fill_opacity=(0.15 + 0.12 * (i % 4)))
            for i in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=0.02)
        ras_label = Text("raster\ngrid of cell values", font_size=18, color=SAND, line_spacing=1.2).next_to(ras_grid, DOWN, buff=0.4)
        ras_group = VGroup(ras_grid, ras_label).move_to(UP * 2.6 + RIGHT * 1.9)

        self.play(FadeIn(vec_group, shift=UP * 0.2), run_time=1.0)
        self.play(FadeIn(ras_group, shift=UP * 0.2), run_time=1.0)
        self.wait(1.2)
        self.play(FadeOut(vec_group), FadeOut(ras_group), run_time=0.6)

        fact = Text(
            "Vector data stores exact\npoints, lines, and shapes.\nRaster data stores a grid\nof cells, each holding\none value.",
            font_size=25, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text(
            "Roads want vectors.\nTemperature wants raster.",
            font_size=29, color=ACCENT, weight=BOLD, line_spacing=1.25,
        ).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)


class KrigingGuess(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Nobody measured\nthis spot.",
            font_size=34, color=INK, weight=BOLD, line_spacing=1.2,
        ).move_to(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        self.wait(0.5)
        sub = Text("The map still knows.", font_size=30, color=ACCENT, weight=BOLD).next_to(hook, DOWN, buff=0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.8)
        self.wait(0.9)
        self.play(FadeOut(hook), FadeOut(sub), run_time=0.5)

        samples = [
            ((-2.0, 1.4), "18"), ((1.8, 1.6), "22"), ((-1.6, -1.2), "15"), ((2.0, -1.4), "20"),
        ]
        sample_dots = VGroup()
        sample_labels = VGroup()
        for (x, y), val in samples:
            d = Dot(point=[x, y, 0], radius=0.09, color=SKY)
            t = Text(val, font_size=18, color=SKY).next_to(d, UP, buff=0.12)
            sample_dots.add(d)
            sample_labels.add(t)

        query = Dot(point=[0, 0, 0], radius=0.11, color=WARN)
        qmark = Text("?", font_size=26, color=WARN, weight=BOLD).next_to(query, DOWN, buff=0.12)

        group = VGroup(sample_dots, sample_labels, query, qmark).move_to(UP * 2.4)
        self.play(FadeIn(sample_dots), FadeIn(sample_labels), run_time=0.9)
        self.play(FadeIn(query, scale=1.3), Write(qmark), run_time=0.6)
        self.wait(0.5)

        lines = VGroup(*[
            DashedLine(d.get_center(), query.get_center(), color=SAND, stroke_width=2, dash_length=0.08)
            for d in sample_dots
        ])
        self.play(Create(lines), run_time=1.0)
        self.wait(0.6)

        answer = Text("~19", font_size=24, color=ACCENT, weight=BOLD).next_to(query, DOWN, buff=0.35)
        self.play(FadeOut(qmark), Write(answer), run_time=0.7)
        self.wait(1.0)
        self.play(FadeOut(VGroup(sample_dots, sample_labels, query, lines, answer)), run_time=0.6)

        fact = Text(
            "Kriging estimates unknown\nvalues by weighting nearby\nsamples by how correlated\ndistance makes them, a method\nborn in South African gold mines.",
            font_size=22, color=INK, line_spacing=1.3,
        ).move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.3), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(fact), run_time=0.5)

        punch = Text(
            "It's an educated guess\nwith math holding the pen.",
            font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.25,
        ).move_to(ORIGIN)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.1)
        self.play(FadeOut(punch), run_time=0.4)

        endcard(self)

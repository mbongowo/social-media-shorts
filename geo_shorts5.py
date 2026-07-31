"""Batch 4 — GeoAI + geospatial data science shorts (TikTok-first, reused everywhere)."""

from manim import *

config.frame_width = 8.0
config.frame_height = 14.22

INK = "#eaf2ef"
ACCENT = "#39d98a"
WARN = "#ff6b6b"
SKY = "#4aa8ff"
SAND = "#e8c268"
BG = "#0b1c17"


def endcard(scene):
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=3)
    brand = Text("Maps, satellites & GeoAI", font_size=40, color=INK, weight=BOLD)
    sub = Text("Follow for more", font_size=30, color=ACCENT)
    grp = VGroup(brand, line, sub).arrange(DOWN, buff=0.35)
    scene.play(FadeIn(grp, shift=UP * 0.3), run_time=0.8)
    scene.wait(1.6)


class AICRSBug(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("AI can write your\nGIS code.", font_size=56, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        sub = Text("It cant catch this bug.", font_size=34, color=WARN).next_to(hook, DOWN, buff=0.4)
        self.play(FadeIn(sub), run_time=0.6)

        sq1 = Square(1.5, color=ACCENT, fill_color=ACCENT, fill_opacity=0.15).shift(UP * 0.6 + LEFT * 2.0)
        dot1 = Dot(sq1.get_center(), radius=0.12, color=ACCENT)
        lbl1 = Text("EPSG:4326", font_size=26, color=ACCENT).next_to(sq1, UP, buff=0.25)
        sq2 = Square(1.5, color=SKY, fill_color=SKY, fill_opacity=0.15).shift(UP * 0.6 + RIGHT * 2.0)
        dot2 = Dot(sq2.get_center(), radius=0.12, color=SKY)
        lbl2 = Text("EPSG:32632", font_size=26, color=SKY).next_to(sq2, UP, buff=0.25)
        self.play(FadeIn(sq1), FadeIn(dot1), Write(lbl1), FadeIn(sq2), FadeIn(dot2), Write(lbl2), run_time=1.2)

        dash = DashedLine(dot1.get_center(), dot2.get_center(), color=WARN, stroke_width=4, dash_length=0.12)
        same = Text("same place - different grid", font_size=26, color=WARN,
                    line_spacing=1.0).next_to(dash, DOWN, buff=0.5)
        self.play(Create(dash), Write(same), run_time=1.2)
        self.wait(0.4)

        fact = Text("One mismatched coordinate system and\nthe code runs fine - and is silently,\ncompletely wrong.",
                    font_size=30, color=INK, line_spacing=1.1).shift(DOWN * 4.4)
        self.play(Write(fact), run_time=1.5)
        self.wait(0.6)
        self.play(FadeOut(fact), run_time=0.4)
        punch = Text("The tools got faster.\nThe fundamentals got\nmore valuable.", font_size=38,
                     color=ACCENT, weight=BOLD, line_spacing=1.1).shift(DOWN * 4.6)
        self.play(Write(punch), run_time=1.2)
        self.wait(1.1)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class AISAMBuildings(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("AI can count buildings\nfrom space.", font_size=52, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        cols, rows = 4, 3
        buildings = VGroup()
        for r in range(rows):
            for c in range(cols):
                b = Rectangle(width=0.9, height=0.7, color=GREY_C, fill_color=GREY_C, fill_opacity=0.8)
                b.move_to(RIGHT * (c - 1.5) * 1.15 + UP * (1 - r) * 1.0 + UP * 0.3)
                buildings.add(b)
        self.play(LaggedStart(*[FadeIn(b) for b in buildings], lag_ratio=0.06), run_time=1.2)

        self.play(LaggedStart(*[b.animate.set_color(ACCENT).set_fill(ACCENT, opacity=0.85)
                                 for b in buildings], lag_ratio=0.08), run_time=1.6)

        count = Text("25", font_size=64, color=ACCENT, weight=BOLD).shift(DOWN * 2.0)
        count_lbl = Text("buildings counted", font_size=28, color=INK).next_to(count, DOWN, buff=0.2)
        self.play(FadeIn(count, scale=1.4), Write(count_lbl), run_time=1.0)
        self.wait(0.4)

        fact = Text("A pure-numpy stage turns SAM masks into\nreportable numbers: 25 buildings, mean\n26.77 m2, geometry at IoU 1.0.",
                    font_size=28, color=INK, line_spacing=1.1).shift(DOWN * 4.6)
        self.play(FadeOut(count), FadeOut(count_lbl), Write(fact), run_time=1.4)
        self.wait(1.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class STACSearch(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("How do you search\npetabytes of satellite\nimages?", font_size=48, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        import random as _r
        _r.seed(7)
        tiles = VGroup(*[
            Square(0.55, color=SKY, fill_color=SKY, fill_opacity=0.6).move_to(
                RIGHT * _r.uniform(-3.0, 3.0) + UP * _r.uniform(-1.0, 1.6))
            for _ in range(12)
        ])
        self.play(LaggedStart(*[FadeIn(t, scale=0.5) for t in tiles], lag_ratio=0.08), run_time=1.4)

        query = RoundedRectangle(width=4.4, height=0.9, corner_radius=0.15, color=ACCENT,
                                 fill_color=ACCENT, fill_opacity=0.15).shift(UP * 2.6)
        query_lbl = Text("area + date + band", font_size=26, color=ACCENT).move_to(query)
        self.play(FadeIn(query), Write(query_lbl), run_time=0.9)

        row_targets = []
        for i in range(12):
            col = i % 6
            rrow = i // 6
            row_targets.append(RIGHT * (col - 2.5) * 0.85 + DOWN * (0.4 + rrow * 0.8))
        self.play(*[t.animate.move_to(pos).set_color(ACCENT).set_fill(ACCENT, opacity=0.7)
                    for t, pos in zip(tiles, row_targets)], run_time=1.4)
        catalog_lbl = Text("the catalog", font_size=26, color=ACCENT).shift(DOWN * 2.4)
        self.play(Write(catalog_lbl), run_time=0.6)
        self.wait(0.3)

        fact = Text("SpatioTemporal Asset Catalogs turn\nscattered imagery into ONE queryable\nindex. Ask for your area and date -\nget the pixels.",
                    font_size=28, color=INK, line_spacing=1.1).shift(DOWN * 4.6)
        self.play(FadeOut(catalog_lbl), Write(fact), run_time=1.5)
        self.wait(1.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class COGStream(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("You dont have to\ndownload the whole\n50 GB file.", font_size=48, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        raster = Square(4.2, color=GREY_C, fill_color=GREY_C, fill_opacity=0.5).shift(UP * 0.2)
        self.play(FadeIn(raster), run_time=0.8)

        n = 5
        cell = 4.2 / n
        grid_lines = VGroup()
        for i in range(1, n):
            x = raster.get_left()[0] + i * cell
            grid_lines.add(Line([x, raster.get_top()[1], 0], [x, raster.get_bottom()[1], 0],
                                 color=BG, stroke_width=2))
            y = raster.get_bottom()[1] + i * cell
            grid_lines.add(Line([raster.get_left()[0], y, 0], [raster.get_right()[0], y, 0],
                                 color=BG, stroke_width=2))
        self.play(Create(grid_lines), run_time=1.0)

        tile_cells = VGroup()
        for r in range(n):
            for c in range(n):
                x = raster.get_left()[0] + (c + 0.5) * cell
                y = raster.get_bottom()[1] + (r + 0.5) * cell
                t = Square(cell * 0.94, color=GREY_C, fill_color=GREY_C, fill_opacity=0.0,
                          stroke_width=0).move_to([x, y, 0])
                tile_cells.add(t)

        highlight_idx = [6, 7, 12, 17, 18]
        highlights = VGroup(*[tile_cells[i].copy().set_fill(ACCENT, opacity=0.85).set_stroke(ACCENT, 2)
                              for i in highlight_idx])
        self.play(LaggedStart(*[FadeIn(h) for h in highlights], lag_ratio=0.15), run_time=1.2)

        stream_lbl = Text("stream only these", font_size=28, color=ACCENT).shift(DOWN * 2.6)
        self.play(Write(stream_lbl), run_time=0.7)
        self.wait(0.4)

        fact = Text("Cloud-Optimized GeoTIFFs serve tiles\non demand over HTTP. Memory and\nbandwidth stop being the limit on\nhow much you can use.",
                    font_size=28, color=INK, line_spacing=1.1).shift(DOWN * 4.6)
        self.play(FadeOut(stream_lbl), Write(fact), run_time=1.5)
        self.wait(1.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)

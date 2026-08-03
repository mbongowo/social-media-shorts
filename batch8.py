"""Batch 8 — six new geo-education shorts across the four themes."""

from manim import *

config.frame_width = 8.0
config.frame_height = 14.22

INK = "#eaf2ef"
ACCENT = "#39d98a"
WARN = "#ff6b6b"
SKY = "#4aa8ff"
SAND = "#e8c268"
BG = "#0b1c17"


def fit(mobj, w=7.2):
    if mobj.width > w:
        mobj.scale_to_fit_width(w)
    return mobj


def endcard(scene):
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=3)
    brand = Text("Maps, satellites & GeoAI", font_size=40, color=INK, weight=BOLD)
    sub = Text("Follow for more", font_size=30, color=ACCENT)
    grp = VGroup(brand, line, sub).arrange(DOWN, buff=0.35)
    scene.play(FadeIn(grp, shift=UP * 0.3), run_time=0.8)
    scene.wait(1.6)


class TerrainLean(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = fit(Text("This satellite photo\nis quietly lying to you.", font_size=48, color=INK,
                    weight=BOLD, line_spacing=1.1)).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        sat = Dot(UP * 2.6 + RIGHT * 0.2, radius=0.12, color=SKY)
        sat_lbl = Text("sensor", font_size=22, color=SKY).next_to(sat, UP, buff=0.15)
        mountain = Polygon(
            LEFT * 1.6 + DOWN * 0.6, ORIGIN + UP * 1.4, RIGHT * 1.6 + DOWN * 0.6,
            color=SAND, fill_color=SAND, fill_opacity=0.85,
        ).shift(DOWN * 0.6)
        ground = Line(LEFT * 3, RIGHT * 3, color=INK, stroke_width=2).shift(DOWN * 1.2)
        self.play(FadeIn(sat), Write(sat_lbl), Create(mountain), Create(ground), run_time=1.1)

        ray_true = DashedLine(sat.get_center(), mountain.get_top(), color=ACCENT, stroke_width=3)
        base_true = Dot(mountain.get_top()[0] * RIGHT + DOWN * 1.2, radius=0.06, color=ACCENT)
        ray_lean = Line(sat.get_center(), mountain.get_top(), color=WARN, stroke_width=3)
        lean_pt = mountain.get_top() + DOWN * 1.2 - mountain.get_top()
        appears_at = Dot(np.array([mountain.get_top()[0] + 0.9, -1.2, 0]), radius=0.06, color=WARN)
        note = Text("peak's true position", font_size=20, color=ACCENT).next_to(base_true, DOWN, buff=0.5).shift(LEFT*0.9)
        note2 = Text("where it appears\nin the raw image", font_size=20, color=WARN, line_spacing=1.0).next_to(appears_at, DOWN, buff=0.3)

        self.play(Create(ray_true), FadeIn(base_true), run_time=0.8)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(0.3)
        self.play(Create(ray_lean), FadeIn(appears_at), run_time=0.8)
        self.play(FadeIn(note2), run_time=0.5)
        self.wait(0.8)

        fact = fit(Text(
            "Tall terrain leans in raw imagery\nbecause off-nadir viewing angles\nshift high elevations sideways.",
            font_size=28, color=WHITE, line_spacing=1.2,
        )).shift(DOWN * 4.4)
        self.play(*[FadeOut(m) for m in [hook]], run_time=0.4)
        self.play(FadeIn(fact, shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)

        punch = fit(Text(
            "Orthorectification uses elevation\ndata to warp every pixel back\nto its true map position.",
            font_size=30, color=ACCENT, weight=BOLD, line_spacing=1.2,
        )).move_to(fact.get_center())
        self.play(FadeOut(fact), run_time=0.3)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class FalseColorVeg(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = fit(Text("This isn't a photo.\nIt's a plant health scan.", font_size=46, color=INK,
                    weight=BOLD, line_spacing=1.15)).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        leaf = RegularPolygon(n=8, radius=1.4, color=ACCENT, fill_color=ACCENT, fill_opacity=0.85).shift(UP * 1.6)
        leaf_lbl = Text("healthy leaf", font_size=22, color=INK).next_to(leaf, DOWN, buff=0.3)
        self.play(FadeIn(leaf), Write(leaf_lbl), run_time=0.8)

        arrow_nir = Arrow(leaf.get_right(), leaf.get_right() + RIGHT * 1.6, color=WARN, stroke_width=4, buff=0.1)
        nir_lbl = Text("bounces most\nnear-infrared light away", font_size=20, color=WARN, line_spacing=1.0).next_to(arrow_nir, RIGHT, buff=0.15)
        self.play(GrowArrow(arrow_nir), FadeIn(nir_lbl), run_time=0.9)
        self.wait(0.6)
        self.play(FadeOut(arrow_nir), FadeOut(nir_lbl), run_time=0.4)

        rgb_row = VGroup(
            Square(0.5, color=WARN, fill_color=WARN, fill_opacity=0.9),
            Square(0.5, color="#39ff6a", fill_color="#39ff6a", fill_opacity=0.9),
            Square(0.5, color=SKY, fill_color=SKY, fill_opacity=0.9),
        ).arrange(RIGHT, buff=0.2).shift(DOWN * 0.3)
        rgb_lbl = VGroup(
            Text("NIR ->", font_size=18, color=INK),
            Text("R", font_size=18, color=INK),
        ).arrange(RIGHT, buff=0.1).next_to(rgb_row[0], UP, buff=0.15)
        remap = Text("Remap that infrared band\ninto the red display channel", font_size=24, color=INK, line_spacing=1.1).next_to(rgb_row, DOWN, buff=0.4)
        self.play(FadeIn(rgb_row), FadeIn(rgb_lbl), Write(remap), run_time=1.0)
        self.wait(0.8)
        self.play(FadeOut(remap), FadeOut(rgb_lbl), FadeOut(rgb_row), FadeOut(leaf_lbl), run_time=0.5)

        self.play(leaf.animate.set_color(WARN).set_fill(WARN, opacity=0.9), run_time=0.7)
        glow_lbl = Text("healthy vegetation now\nglows bright red", font_size=24, color=WARN, weight=BOLD).next_to(leaf, DOWN, buff=0.3)
        self.play(Write(glow_lbl), run_time=0.8)
        self.wait(0.8)

        self.play(*[FadeOut(m) for m in [hook, leaf, glow_lbl]], run_time=0.4)
        fact = fit(Text(
            "Chlorophyll reflects far more\nnear-infrared light than green,\nso false color exaggerates it.",
            font_size=28, color=WHITE, line_spacing=1.2,
        )).shift(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2), run_time=0.9)
        self.wait(1.1)
        punch = fit(Text(
            "Stressed or dying plants lose\nthat infrared glow long before\nthe leaf looks sick to your eye.",
            font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.2,
        )).move_to(fact.get_center())
        self.play(FadeOut(fact), run_time=0.3)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class GreatCircleLie(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = fit(Text("The straight line on your map\nisn't the shortest path.", font_size=42, color=INK,
                    weight=BOLD, line_spacing=1.15)).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        rect = Rectangle(width=5.2, height=3.2, color=INK, stroke_width=2).shift(UP * 1.6)
        a = Dot(rect.get_left() + UP * 0.9 + RIGHT * 0.3, radius=0.09, color=ACCENT)
        b = Dot(rect.get_right() + DOWN * 0.9 + LEFT * 0.3, radius=0.09, color=ACCENT)
        a_lbl = Text("New York", font_size=20, color=ACCENT).next_to(a, UP, buff=0.15)
        b_lbl = Text("Tokyo", font_size=20, color=ACCENT).next_to(b, DOWN, buff=0.15)
        straight = Line(a.get_center(), b.get_center(), color=WARN, stroke_width=4)
        straight_lbl = Text("rhumb line: straight,\nconstant compass bearing", font_size=18, color=WARN, line_spacing=1.0).next_to(straight, DOWN, buff=0.2).shift(RIGHT*0.4)
        self.play(Create(rect), FadeIn(a), FadeIn(b), Write(a_lbl), Write(b_lbl), run_time=1.0)
        self.play(Create(straight), FadeIn(straight_lbl), run_time=0.9)
        self.wait(0.8)

        curved = ArcBetweenPoints(a.get_center(), b.get_center(), angle=-1.1, color=SKY, stroke_width=4)
        curved_lbl = Text("great circle: curved on the map,\nbut actually shorter", font_size=18, color=SKY, line_spacing=1.0).next_to(rect, DOWN, buff=1.1)
        self.play(Create(curved), FadeIn(curved_lbl), run_time=0.9)
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in [hook]], run_time=0.4)
        fact = fit(Text(
            "On a flat Mercator map, a straight\nline holds one compass heading --\nbut a sphere's shortest path curves.",
            font_size=26, color=WHITE, line_spacing=1.2,
        )).shift(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)

        punch = fit(Text(
            "Pilots and ships fly the curve.\nThe straight line is only\nconvenient, never shortest.",
            font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.2,
        )).move_to(fact.get_center())
        self.play(FadeOut(fact), run_time=0.3)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class ShortcutLearning(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = fit(Text("This AI hit 98% accuracy.\nIt still can't do its job.", font_size=42, color=INK,
                    weight=BOLD, line_spacing=1.15)).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        panel = RoundedRectangle(width=5.0, height=2.6, corner_radius=0.15, color=SAND,
                                  fill_color=SAND, fill_opacity=0.7).shift(UP * 1.8)
        fence = VGroup(*[Line(UP * 0.9, DOWN * 0.9, color=INK, stroke_width=3).shift(RIGHT * x)
                         for x in np.linspace(-2.2, 2.2, 7)]).shift(UP * 1.8 + DOWN * 1.35)
        target_lbl = Text("target: solar farms", font_size=22, color=INK).next_to(panel, UP, buff=0.3)
        self.play(FadeIn(panel), FadeIn(fence), Write(target_lbl), run_time=1.0)
        self.wait(0.4)

        arrow = Arrow(fence.get_bottom(), fence.get_bottom() + DOWN * 0.9, color=WARN, stroke_width=4, buff=0.05)
        real_reason = Text("model actually learned:\nthe perimeter fence pattern", font_size=22, color=WARN, line_spacing=1.05).next_to(arrow, DOWN, buff=0.2)
        self.play(GrowArrow(arrow), Write(real_reason), run_time=1.0)
        self.wait(1.0)

        no_panel = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.1, color=SAND,
                                     fill_color=SAND, fill_opacity=0.0, stroke_opacity=0.0).next_to(real_reason, DOWN, buff=0.5)
        fence2 = VGroup(*[Line(UP * 0.35, DOWN * 0.35, color=INK, stroke_width=3).shift(RIGHT * x)
                          for x in np.linspace(-1.4, 1.4, 5)]).next_to(real_reason, DOWN, buff=0.6)
        wrong_lbl = Text("empty fenced lot -> AI says\n\"solar farm\" anyway", font_size=20, color=WARN, line_spacing=1.0).next_to(fence2, DOWN, buff=0.25)
        self.play(FadeIn(fence2), Write(wrong_lbl), run_time=0.9)
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in [hook]], run_time=0.4)
        fact = fit(Text(
            "Neural networks take the easiest\nsignal correlated with the label --\nnot necessarily the true cause.",
            font_size=26, color=WHITE, line_spacing=1.2,
        )).shift(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)

        punch = fit(Text(
            "Researchers call it shortcut\nlearning. Test on new regions,\nor accuracy numbers can lie.",
            font_size=27, color=ACCENT, weight=BOLD, line_spacing=1.2,
        )).move_to(fact.get_center())
        self.play(FadeOut(fact), run_time=0.3)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class HexGridEdge(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = fit(Text("Why mapmakers are ditching\nsquares for hexagons.", font_size=42, color=INK,
                    weight=BOLD, line_spacing=1.15)).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        sq_grid = VGroup(*[Square(0.7, color=SKY, stroke_width=2).move_to(RIGHT * c * 0.7 + UP * r * 0.7)
                           for r in (-1, 0, 1) for c in (-1, 0, 1)]).shift(UP * 2.2 + LEFT * 2.0)
        center_sq = sq_grid[4]
        orth = [sq_grid[1], sq_grid[3], sq_grid[5], sq_grid[7]]
        diag = [sq_grid[0], sq_grid[2], sq_grid[6], sq_grid[8]]
        sq_lbl = Text("square grid", font_size=20, color=SKY).next_to(sq_grid, DOWN, buff=0.25)
        self.play(Create(sq_grid), Write(sq_lbl), run_time=1.0)

        d1 = Line(center_sq.get_center(), orth[0].get_center(), color=ACCENT, stroke_width=3)
        d2 = Line(center_sq.get_center(), diag[0].get_center(), color=WARN, stroke_width=3)
        self.play(Create(d1), Create(d2), run_time=0.8)
        uneven = Text("neighbor distances\naren't equal", font_size=18, color=WARN, line_spacing=1.0).next_to(sq_lbl, DOWN, buff=0.2)
        self.play(Write(uneven), run_time=0.6)
        self.wait(0.8)

        hexes = VGroup(*[RegularPolygon(n=6, radius=0.42, color=ACCENT, stroke_width=2).move_to(p) for p in [
            RIGHT * 2.0 + UP * 2.2,
            RIGHT * 2.0 + UP * 2.2 + RIGHT * 0.73 + UP * 0.42,
            RIGHT * 2.0 + UP * 2.2 + RIGHT * 0.73 + DOWN * 0.42,
            RIGHT * 2.0 + UP * 2.2 + LEFT * 0.73 + UP * 0.42,
            RIGHT * 2.0 + UP * 2.2 + LEFT * 0.73 + DOWN * 0.42,
            RIGHT * 2.0 + UP * 2.2 + UP * 0.84,
            RIGHT * 2.0 + UP * 2.2 + DOWN * 0.84,
        ]])
        hex_lbl = Text("hex grid", font_size=20, color=ACCENT).next_to(hexes, DOWN, buff=0.25)
        self.play(Create(hexes), Write(hex_lbl), run_time=1.0)
        even_lbl = Text("all 6 neighbors\nequally distant", font_size=18, color=ACCENT, line_spacing=1.0).next_to(hex_lbl, DOWN, buff=0.2)
        self.play(Write(even_lbl), run_time=0.6)
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in [hook]], run_time=0.4)
        fact = fit(Text(
            "In a square grid, a diagonal\nneighbor is farther away than\none straight across.",
            font_size=27, color=WHITE, line_spacing=1.2,
        )).shift(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2), run_time=0.9)
        self.wait(1.1)

        punch = fit(Text(
            "Hexagonal indexes like H3 tile\nEarth so every neighbor is the\nsame distance -- cleaner analytics.",
            font_size=26, color=ACCENT, weight=BOLD, line_spacing=1.2,
        )).move_to(fact.get_center())
        self.play(FadeOut(fact), run_time=0.3)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class GPSSnap(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = fit(Text("Your GPS dot is wrong.\nYour map fixes it for you.", font_size=42, color=INK,
                    weight=BOLD, line_spacing=1.15)).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        road = Line(LEFT * 3, RIGHT * 3, color=SKY, stroke_width=6).shift(UP * 1.6)
        road_lbl = Text("actual road", font_size=20, color=SKY).next_to(road, UP, buff=0.2)
        self.play(Create(road), Write(road_lbl), run_time=0.8)

        raw_pts = VGroup(*[Dot(road.get_center() + RIGHT * x + UP * np.sin(x * 2) * 0.35, radius=0.07, color=WARN)
                           for x in np.linspace(-2.6, 2.6, 7)])
        raw_lbl = Text("raw GPS fixes scatter\noff the road", font_size=20, color=WARN, line_spacing=1.0).next_to(raw_pts, DOWN, buff=0.35)
        self.play(FadeIn(raw_pts), Write(raw_lbl), run_time=1.0)
        self.wait(0.8)
        self.play(FadeOut(raw_lbl), run_time=0.4)

        snapped = VGroup(*[Dot(road.get_center() + RIGHT * x, radius=0.07, color=ACCENT)
                           for x in np.linspace(-2.6, 2.6, 7)])
        arrows = VGroup(*[Arrow(p.get_center(), s.get_center(), color=ACCENT, stroke_width=2, buff=0.02,
                                 max_tip_length_to_length_ratio=0.3)
                          for p, s in zip(raw_pts, snapped)])
        snap_lbl = Text("map matching snaps each point\nonto the most likely road", font_size=20, color=ACCENT, line_spacing=1.0).next_to(road, DOWN, buff=1.1)
        self.play(Create(arrows), FadeIn(snapped), Write(snap_lbl), run_time=1.1)
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in [hook]], run_time=0.4)
        fact = fit(Text(
            "Consumer GPS can be off by\nseveral meters, enough to place\nyou on the wrong street or lane.",
            font_size=27, color=WHITE, line_spacing=1.2,
        )).shift(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2), run_time=0.9)
        self.wait(1.1)

        punch = fit(Text(
            "Map-matching algorithms use the\nroad network's shape to correct\nevery noisy point in real time.",
            font_size=26, color=ACCENT, weight=BOLD, line_spacing=1.2,
        )).move_to(fact.get_center())
        self.play(FadeOut(fact), run_time=0.3)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.2)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)

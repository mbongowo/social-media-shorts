"""Batch 3 — five viral-format global shorts (TikTok-first, reused everywhere)."""

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


class GPSTrilateration(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("GPS doesn't know\nwhere you are.", font_size=56, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)
        sub = Text("Your phone computes it.", font_size=36, color=ACCENT).next_to(hook, DOWN, buff=0.4)
        self.play(FadeIn(sub), run_time=0.6)

        sats = VGroup(*[Dot(p, radius=0.14, color=SKY) for p in
                        [UP * 1.8 + LEFT * 2.4, UP * 2.2 + RIGHT * 2.2, DOWN * 2.6 + RIGHT * 0.2]])
        s_lbl = Text("satellites broadcast one thing:\nthe time, extremely precisely",
                     font_size=30, color=SKY, line_spacing=1.05).shift(DOWN * 4.4)
        self.play(FadeIn(sats), Write(s_lbl), run_time=1.2)

        circles = VGroup(
            Circle(radius=2.6, color=SKY, stroke_width=4).move_to(sats[0]),
            Circle(radius=2.9, color=SKY, stroke_width=4).move_to(sats[1]),
            Circle(radius=2.4, color=SKY, stroke_width=4).move_to(sats[2]),
        )
        for c in circles:
            self.play(Create(c), run_time=0.7)
        you = Dot(UP * 0.0 + RIGHT * 0.0, radius=0.16, color=WARN)
        you_lbl = Text("you", font_size=32, color=WARN, weight=BOLD).next_to(you, RIGHT, buff=0.2)
        self.play(FadeIn(you, scale=2.5), FadeIn(you_lbl), run_time=0.8)
        self.play(FadeOut(s_lbl), run_time=0.3)
        punch = Text("Your phone measures the delays\nand solves for the only point\nthe signals agree on.",
                     font_size=34, color=INK, line_spacing=1.1).shift(DOWN * 4.6)
        self.play(Write(punch), run_time=1.4)
        self.wait(1.0)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class NightLights(Scene):
    def construct(self):
        self.camera.background_color = "#050a0f"
        hook = Text("You can measure an\neconomy from space.", font_size=52, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        coast = VMobject(color=GREY_D, stroke_width=3)
        coast.set_points_smoothly([
            DOWN * 3.2 + LEFT * 3.4, DOWN * 1.6 + LEFT * 2.2, UP * 0.2 + LEFT * 2.8,
            UP * 1.6 + LEFT * 1.0, UP * 1.2 + RIGHT * 1.8, DOWN * 0.8 + RIGHT * 3.2,
        ])
        self.play(Create(coast), run_time=1.0)

        cities = [(UP * 0.8 + LEFT * 0.6, 0.30), (DOWN * 0.6 + RIGHT * 1.2, 0.22),
                  (DOWN * 1.8 + LEFT * 1.4, 0.18), (UP * 0.2 + RIGHT * 2.2, 0.14),
                  (DOWN * 2.4 + RIGHT * 0.2, 0.12), (UP * 1.3 + LEFT * 1.9, 0.10)]
        dots = VGroup(*[Dot(p, radius=r, color=YELLOW, fill_opacity=0.95) for p, r in cities])
        glow = VGroup(*[Dot(p, radius=r * 2.4, color=YELLOW, fill_opacity=0.25) for p, r in cities])
        self.play(LaggedStart(*[FadeIn(VGroup(g, d), scale=0.3) for g, d in zip(glow, dots)],
                              lag_ratio=0.25), run_time=2.0)

        fact = Text("Night-light satellites track growth,\nblackouts, conflict and recovery —\nin places with no official statistics.",
                    font_size=32, color=INK, line_spacing=1.1).shift(DOWN * 4.4)
        self.play(Write(fact), run_time=1.5)
        self.wait(0.6)
        self.play(FadeOut(fact), run_time=0.4)
        punch = Text("Light is data.", font_size=54, color=YELLOW, weight=BOLD).shift(DOWN * 4.6)
        self.play(Write(punch), run_time=0.8)
        self.wait(1.1)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class SaharaAmazon(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("The Sahara Desert\nfeeds the Amazon.", font_size=54, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        sahara = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.2, color=SAND,
                                  fill_color=SAND, fill_opacity=0.9).shift(UP * 0.6 + RIGHT * 2.2)
        sa_lbl = Text("Sahara", font_size=30, color=BG, weight=BOLD).move_to(sahara)
        amazon = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.2, color=ACCENT,
                                  fill_color=ACCENT, fill_opacity=0.9).shift(DOWN * 1.8 + LEFT * 2.2)
        am_lbl = Text("Amazon", font_size=30, color=BG, weight=BOLD).move_to(amazon)
        ocean = Text("Atlantic", font_size=26, color=SKY).shift(UP * -0.6 + RIGHT * 0.1)
        self.play(FadeIn(sahara), FadeIn(sa_lbl), FadeIn(amazon), FadeIn(am_lbl), FadeIn(ocean), run_time=1.0)

        dust = VGroup(*[Dot(radius=0.06, color=SAND) for _ in range(9)])
        path = ArcBetweenPoints(sahara.get_left() + DOWN * 0.2, amazon.get_top() + RIGHT * 0.2, angle=-0.7)
        self.play(Create(path.copy().set_stroke(SAND, 3, opacity=0.5)), run_time=0.8)
        anims = [MoveAlongPath(d, path) for d in dust]
        self.play(LaggedStart(*anims, lag_ratio=0.12), run_time=2.2)

        fact = Text("~27 million tons of dust cross the\nAtlantic every year — carrying the\nphosphorus rainforest soils lack.",
                    font_size=32, color=INK, line_spacing=1.1).shift(DOWN * 4.4)
        self.play(Write(fact), run_time=1.5)
        self.wait(0.6)
        self.play(FadeOut(fact), run_time=0.4)
        punch = Text("Deserts feed rainforests.\nSatellites watched it happen.", font_size=40,
                     color=ACCENT, weight=BOLD, line_spacing=1.1).shift(DOWN * 4.6)
        self.play(Write(punch), run_time=1.1)
        self.wait(1.1)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class RiversMove(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("Rivers don't stay\nwhere you left them.", font_size=52, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        r1 = VMobject(color=SKY, stroke_width=9)
        r1.set_points_smoothly([
            UP * 2.4 + LEFT * 2.8, UP * 1.0 + LEFT * 0.6, UP * 1.8 + RIGHT * 1.4,
            UP * 0.2 + RIGHT * 2.6, DOWN * 1.2 + RIGHT * 0.8, DOWN * 0.6 + LEFT * 1.6,
            DOWN * 2.6 + LEFT * 2.4,
        ])
        yr1 = Text("1990", font_size=30, color=GREY_B).shift(UP * 2.8 + RIGHT * 2.6)
        self.play(Create(r1), FadeIn(yr1), run_time=1.4)

        r2 = VMobject(color=ACCENT, stroke_width=9)
        r2.set_points_smoothly([
            UP * 2.4 + LEFT * 2.8, UP * 0.6 + LEFT * 1.2, UP * 1.4 + RIGHT * 2.0,
            DOWN * 0.4 + RIGHT * 2.2, DOWN * 1.6 + RIGHT * 0.2, DOWN * 1.0 + LEFT * 2.0,
            DOWN * 2.6 + LEFT * 2.4,
        ])
        yr2 = Text("2026", font_size=30, color=ACCENT).next_to(yr1, DOWN, buff=0.2)
        self.play(TransformFromCopy(r1, r2), FadeIn(yr2), run_time=1.8)
        self.play(r1.animate.set_stroke(opacity=0.35), run_time=0.5)

        fact = Text("Meanders crawl meters every year.\nSatellites catch entire bends being\nabandoned into oxbow lakes.",
                    font_size=32, color=INK, line_spacing=1.1).shift(DOWN * 4.4)
        self.play(Write(fact), run_time=1.4)
        self.wait(0.6)
        self.play(FadeOut(fact), run_time=0.4)
        punch = Text("The map is a snapshot.\nThe river keeps moving.", font_size=42,
                     color=ACCENT, weight=BOLD, line_spacing=1.1).shift(DOWN * 4.6)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.1)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)


class PixelTruth(Scene):
    def construct(self):
        self.camera.background_color = BG
        hook = Text("No, satellites can't read\nyour license plate.", font_size=48, color=INK,
                    weight=BOLD, line_spacing=1.1).shift(UP * 4.8)
        self.play(Write(hook), run_time=1.0)

        rows = VGroup(
            VGroup(Square(1.7, color=SKY, fill_color=SKY, fill_opacity=0.5),
                   Text("10 m — Sentinel-2\nsees your whole block", font_size=28, color=INK, line_spacing=1.0)),
            VGroup(Square(1.0, color=ACCENT, fill_color=ACCENT, fill_opacity=0.5),
                   Text("1 m — commercial sats\nsee your car exists", font_size=28, color=INK, line_spacing=1.0)),
            VGroup(Square(0.5, color=WARN, fill_color=WARN, fill_opacity=0.6),
                   Text("30 cm — the very best\nsee its color. That's it.", font_size=28, color=INK, line_spacing=1.0)),
        )
        for row in rows:
            row.arrange(RIGHT, buff=0.5, aligned_edge=UP)
        rows.arrange(DOWN, buff=0.7, aligned_edge=LEFT).shift(UP * 0.2 + LEFT * 0.4)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.4), run_time=0.8)
        self.wait(0.5)

        fact = Text("One pixel = one number.\nSmaller pixels need bigger optics —\nphysics, not budget, sets the limit.",
                    font_size=32, color=INK, line_spacing=1.1).shift(DOWN * 4.2)
        self.play(Write(fact), run_time=1.4)
        self.wait(0.6)
        self.play(FadeOut(fact), run_time=0.4)
        punch = Text("Resolution is physics.\nNot Hollywood.", font_size=44,
                     color=ACCENT, weight=BOLD, line_spacing=1.1).shift(DOWN * 4.4)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.1)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)
        endcard(self)

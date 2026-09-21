from manim import *
import random

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


class GhostFleet(Scene):
    def construct(self):
        self.camera.background_color = BG
        random.seed(11)

        hook = Text(
            "Most fishing boats on Earth\nare invisible to trackers",
            color=INK,
            font_size=40,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.3)
        self.add(hook)
        self.wait(1)

        ocean = Rectangle(
            width=config.frame_width * 0.88,
            height=5.0,
            color=SKY,
            fill_color=SKY,
            fill_opacity=0.08,
            stroke_width=2,
        )
        ocean.move_to(UP * 0.4)
        self.play(FadeIn(ocean), run_time=0.5)

        n = 36
        positions = []
        for _ in range(n):
            x = random.uniform(-ocean.width / 2 + 0.3, ocean.width / 2 - 0.3)
            y = random.uniform(-ocean.height / 2 + 0.3, ocean.height / 2 - 0.3)
            positions.append(ocean.get_center() + RIGHT * x + UP * y)

        tracked_idx = set(random.sample(range(n), 9))
        tracked_dots = VGroup()
        for i in tracked_idx:
            d = Dot(radius=0.11, color=ACCENT, fill_opacity=1)
            d.move_to(positions[i])
            tracked_dots.add(d)

        label_ais = Text('Public AIS tracking', color=ACCENT, font_size=26)
        label_ais.next_to(ocean, UP, buff=0.3)
        self.play(FadeIn(tracked_dots), FadeIn(label_ais), run_time=0.7)
        self.wait(0.9)

        label_sar = Text('Radar satellites scan the same water', color=SAND, font_size=24)
        label_sar.scale_to_fit_width(config.frame_width * 0.85)
        label_sar.next_to(ocean, UP, buff=0.3)
        self.play(FadeOut(label_ais), FadeIn(label_sar), run_time=0.5)

        dark_dots = VGroup()
        for i in range(n):
            if i in tracked_idx:
                continue
            d = Dot(radius=0.11, color=WARN, fill_opacity=1)
            d.move_to(positions[i])
            dark_dots.add(d)
        self.play(FadeIn(dark_dots), run_time=0.9)
        self.wait(1.0)

        self.play(FadeOut(label_sar), run_time=0.3)

        pct = Text('72-76%', color=WARN, font_size=64)
        pct.next_to(ocean, DOWN, buff=0.35)
        sub = Text('of industrial fishing vessels never\nbroadcast their location', color=INK, font_size=24, line_spacing=1.1)
        sub.scale_to_fit_width(config.frame_width * 0.85)
        sub.next_to(pct, DOWN, buff=0.25)
        self.play(FadeIn(pct), FadeIn(sub), run_time=0.6)
        self.wait(1.6)

        self.play(FadeOut(ocean), FadeOut(tracked_dots), FadeOut(dark_dots), FadeOut(pct), FadeOut(sub), run_time=0.4)

        fact = Text(
            "AI scanned 2 million Sentinel-1 radar\nimages (2017-2021) and found most of the\nworld's fishing fleet was never in AIS data",
            color=INK,
            font_size=24,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "The ocean was never empty.\nIt was just not broadcasting.",
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

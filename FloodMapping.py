from manim import *

config.frame_width = 8.0
config.frame_height = 14.22
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = "#0b1c17"

ACCENT = "#39d98a"
DIM = "#7fa89a"
WARN = "#ff6b57"


class FloodMapping(Scene):
    def construct(self):
        self.camera.background_color = "#0b1c17"

        # 1. Hook
        hook1 = Text("Missouri this week:", font_size=38, color=WHITE, weight=BOLD)
        hook2 = Text("160+ rescued from floodwater.", font_size=32, color=WARN, weight=BOLD)
        hook_group = VGroup(hook1, hook2).arrange(DOWN, buff=0.35).move_to(UP * 4.7)
        self.play(Write(hook1), run_time=0.8)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.5)

        claim = Text(
            "Satellites mapped the flood extent\nbefore rescue crews got there.",
            font_size=30, color=ACCENT, weight=BOLD, line_spacing=1.2,
        ).next_to(hook_group, DOWN, buff=0.6)
        self.play(FadeIn(claim, shift=UP * 0.3), run_time=0.9)
        self.wait(0.8)
        self.play(FadeOut(hook_group), FadeOut(claim), run_time=0.5)

        # 2. The problem: optical fails in storms
        title = Text("The problem with floods", font_size=32, color=WHITE, weight=BOLD)
        title.move_to(UP * 5.8)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.6)

        cloud = Text("☁ ☁ ☁", font_size=44, color=DIM).move_to(UP * 3.3)
        optical_label = Text("Optical satellites: blind", font_size=26, color=DIM).next_to(
            cloud, DOWN, buff=0.4
        )
        self.play(FadeIn(cloud, shift=DOWN * 0.2), FadeIn(optical_label), run_time=0.8)
        self.wait(0.9)
        self.play(FadeOut(cloud), FadeOut(optical_label), FadeOut(title), run_time=0.5)

        # 3. The solution: SAR sees through
        radar_title = Text("Radar (SAR) sees through it", font_size=30, color=ACCENT, weight=BOLD)
        radar_title.move_to(UP * 5.3)
        self.play(FadeIn(radar_title, shift=UP * 0.2), run_time=0.7)

        # simple water-vs-land grid
        grid = VGroup()
        np.random.seed(3)
        rows, cols = 8, 5
        for r in range(rows):
            for c in range(cols):
                is_water = (r >= 4 and r <= 6 and 1 <= c <= 3) or (r == 3 and c == 2)
                cell = Square(side_length=0.62, stroke_width=1, stroke_color=DIM,
                               fill_opacity=1,
                               fill_color=(ACCENT if is_water else "#123326"))
                cell.move_to(RIGHT * (c - 2) * 0.64 + DOWN * (r - 3.5) * 0.64)
                grid.add(cell)
        grid.move_to(UP * 1.6)

        self.play(Create(grid), run_time=1.1)
        self.wait(0.3)

        radar_note = Text(
            "Smooth water reflects radar differently\nthan rough land — flood extent\nshows up automatically, day or night.",
            font_size=25, color=WHITE, line_spacing=1.3,
        ).next_to(grid, DOWN, buff=0.55)
        self.play(FadeIn(radar_note, shift=UP * 0.2), run_time=0.9)
        self.wait(1.3)
        self.play(FadeOut(grid), FadeOut(radar_note), FadeOut(radar_title), run_time=0.6)

        # 4. Punchline
        verdict_label = Text("This is happening in near-real time:", font_size=24, color=DIM)
        verdict_label.move_to(UP * 3.2)
        verdict = Text(
            "Sentinel-1 and NISAR image\nthe same flood every 1-6 days.",
            font_size=32, color=ACCENT, weight=BOLD, line_spacing=1.3,
        ).next_to(verdict_label, DOWN, buff=0.5)

        self.play(FadeIn(verdict_label, shift=UP * 0.2), run_time=0.7)
        self.play(Write(verdict), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(verdict_label), FadeOut(verdict), run_time=0.6)

        # 5. End card
        end1 = Text("Maps, satellites & GeoAI", font_size=34, color=WHITE, weight=BOLD)
        end2 = Text("Follow for more", font_size=30, color=ACCENT, weight=BOLD)
        end_group = VGroup(end1, end2).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        self.play(FadeIn(end_group, scale=1.05), run_time=0.8)
        self.wait(1.3)
        self.play(FadeOut(end_group), run_time=0.5)

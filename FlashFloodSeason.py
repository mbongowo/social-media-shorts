from manim import *

config.frame_width = 8.0
config.frame_height = 14.22
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = "#0b1c17"

ACCENT = "#39d98a"
DIM = "#7fa89a"
WARN = "#ff6b57"


class FlashFloodSeason(Scene):
    def construct(self):
        self.camera.background_color = "#0b1c17"

        # 1. Hook
        hook1 = Text("15 flash flood emergencies.", font_size=34, color=WHITE, weight=BOLD)
        hook2 = Text("2 weeks.", font_size=40, color=WARN, weight=BOLD)
        hook_group = VGroup(hook1, hook2).arrange(DOWN, buff=0.3).move_to(UP * 4.7)
        self.play(Write(hook1), run_time=0.8)
        self.play(Write(hook2), run_time=0.6)
        self.wait(0.5)

        claim = Text(
            "Texas Hill Country got hit\nby a 1-in-1000-year storm —\ntwo years running.",
            font_size=28, color=ACCENT, weight=BOLD, line_spacing=1.2,
        ).next_to(hook_group, DOWN, buff=0.6)
        self.play(FadeIn(claim, shift=UP * 0.3), run_time=0.9)
        self.wait(0.9)
        self.play(FadeOut(hook_group), FadeOut(claim), run_time=0.5)

        # 2. What "1000-year" actually means
        title = Text('What "1000-year storm" means', font_size=28, color=WHITE, weight=BOLD)
        title.move_to(UP * 5.8)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.6)

        sub = Text(
            "Not once per millennium.\nA 0.1% chance in any\ngiven year — at that spot.",
            font_size=27, color=WHITE, line_spacing=1.3,
        ).move_to(UP * 3.0)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.9)
        self.wait(1.1)
        self.play(FadeOut(sub), FadeOut(title), run_time=0.5)

        # 3. Rainfall bar comparison
        bar_title = Text("Rainfall rate that week", font_size=27, color=ACCENT, weight=BOLD)
        bar_title.move_to(UP * 5.5)
        self.play(FadeIn(bar_title, shift=UP * 0.2), run_time=0.7)

        base_y = UP * 1.3
        normal_bar = Rectangle(width=1.4, height=0.9, fill_opacity=1, fill_color="#123326",
                                 stroke_color=DIM, stroke_width=1)
        event_bar = Rectangle(width=1.4, height=3.6, fill_opacity=1, fill_color=WARN,
                                stroke_color=WARN, stroke_width=1)
        bars = VGroup(normal_bar, event_bar).arrange(RIGHT, buff=1.0, aligned_edge=DOWN)
        bars.move_to(base_y)

        normal_label = Text("normal storm\n~1 in/day", font_size=18, color=DIM, line_spacing=1.1).next_to(normal_bar, DOWN, buff=0.25)
        event_label = Text("this event\nnear 1 yr of rain\nin days", font_size=18, color=WARN, line_spacing=1.1).next_to(event_bar, DOWN, buff=0.25)

        self.play(GrowFromEdge(normal_bar, DOWN), FadeIn(normal_label), run_time=0.7)
        self.play(GrowFromEdge(event_bar, DOWN), FadeIn(event_label), run_time=1.0)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(bars, normal_label, event_label, bar_title)),
            run_time=0.6,
        )

        # 4. Why it matters — the geospatial angle
        why = Text(
            "A warmer atmosphere holds\nmore moisture, so storms\ndump it faster, in smaller areas.",
            font_size=27, color=WHITE, line_spacing=1.35,
        ).move_to(UP * 2.5)
        self.play(FadeIn(why, shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)
        self.play(FadeOut(why), run_time=0.5)

        # 5. Punchline
        verdict_label = Text("Satellite rainfall estimates", font_size=22, color=DIM)
        verdict_label.move_to(UP * 3.3)
        verdict = Text(
            "now update every 30 minutes —\nwarning before the river rises.",
            font_size=29, color=ACCENT, weight=BOLD, line_spacing=1.3,
        ).next_to(verdict_label, DOWN, buff=0.5)

        self.play(FadeIn(verdict_label, shift=UP * 0.2), run_time=0.7)
        self.play(Write(verdict), run_time=1.2)
        self.wait(1.4)
        self.play(FadeOut(verdict_label), FadeOut(verdict), run_time=0.6)

        # 6. End card
        end1 = Text("Maps, satellites & GeoAI", font_size=34, color=WHITE, weight=BOLD)
        end2 = Text("Follow for more", font_size=30, color=ACCENT, weight=BOLD)
        end_group = VGroup(end1, end2).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        self.play(FadeIn(end_group, scale=1.05), run_time=0.8)
        self.wait(1.3)
        self.play(FadeOut(end_group), run_time=0.5)

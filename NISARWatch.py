from manim import *

config.frame_width = 8.0
config.frame_height = 14.22
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = "#0b1c17"

ACCENT = "#39d98a"
DIM = "#7fa89a"
WARN = "#ff6b57"


class NISARWatch(Scene):
    def construct(self):
        self.camera.background_color = "#0b1c17"

        # 1. Hook
        hook1 = Text("There's a satellite now", font_size=36, color=WHITE, weight=BOLD)
        hook2 = Text("checking the ground you stand on.", font_size=30, color=WHITE, weight=BOLD)
        hook_group = VGroup(hook1, hook2).arrange(DOWN, buff=0.3).move_to(UP * 4.7)
        self.play(Write(hook1), run_time=0.8)
        self.play(Write(hook2), run_time=0.7)
        self.wait(0.5)

        claim = Text(
            "Every few days. Day or night.\nThrough clouds.",
            font_size=30, color=ACCENT, weight=BOLD, line_spacing=1.2,
        ).next_to(hook_group, DOWN, buff=0.6)
        self.play(FadeIn(claim, shift=UP * 0.3), run_time=0.9)
        self.wait(0.8)
        self.play(FadeOut(hook_group), FadeOut(claim), run_time=0.5)

        # 2. What it is
        title = Text("NISAR just went fully live", font_size=30, color=WHITE, weight=BOLD)
        title.move_to(UP * 5.8)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.6)

        sub = Text(
            "NASA + ISRO radar mission.\nTwin radars, 5-10m resolution,\nrevisits the same ground\nevery 1-6 days.",
            font_size=27, color=WHITE, line_spacing=1.3,
        ).move_to(UP * 2.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)
        self.play(FadeOut(sub), FadeOut(title), run_time=0.5)

        # 3. Millimeter-scale ground shift visual
        radar_title = Text("It sees millimeters of ground shift", font_size=27, color=ACCENT, weight=BOLD)
        radar_title.move_to(UP * 5.5)
        self.play(FadeIn(radar_title, shift=UP * 0.2), run_time=0.7)

        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-1.2, 1.2, 1],
            x_length=6.0,
            y_length=3.4,
            axis_config={"color": DIM, "stroke_width": 2, "include_tip": False},
            tips=False,
        ).move_to(UP * 2.0)

        flat_line = axes.plot(lambda x: 0.15 * np.sin(x * 1.3), color=DIM, stroke_width=4)
        shift_curve = axes.plot(
            lambda x: 0.15 * np.sin(x * 1.3) + (0.55 if x > 3 else 0) * min((x - 3), 1) if x > 3 else 0.15 * np.sin(x * 1.3),
            color=WARN, stroke_width=5,
        )

        before_label = Text("stable ground", font_size=20, color=DIM).next_to(axes, DOWN, buff=0.3).shift(LEFT * 1.6)
        after_label = Text("subsidence detected", font_size=20, color=WARN).next_to(before_label, DOWN, buff=0.25).align_to(before_label, LEFT)

        self.play(Create(axes), run_time=0.7)
        self.play(Create(flat_line), FadeIn(before_label), run_time=0.9)
        self.wait(0.2)
        self.play(Create(shift_curve), FadeIn(after_label), run_time=1.0)
        self.wait(0.9)

        self.play(
            FadeOut(VGroup(axes, flat_line, shift_curve, before_label, after_label, radar_title)),
            run_time=0.6,
        )

        # 4. Why it matters
        why = Text(
            "Landslides. Flood extent.\nSinking land near dams and rail.\nCrop stress, season by season.",
            font_size=28, color=WHITE, line_spacing=1.35,
        ).move_to(UP * 2.5)
        self.play(FadeIn(why, shift=UP * 0.2), run_time=0.9)
        self.wait(1.3)
        self.play(FadeOut(why), run_time=0.5)

        # 5. Punchline
        verdict_label = Text("Since February 2026:", font_size=24, color=DIM)
        verdict_label.move_to(UP * 3.2)
        verdict = Text(
            "100,000+ data products\nreleased, free and open.",
            font_size=32, color=ACCENT, weight=BOLD, line_spacing=1.3,
        ).next_to(verdict_label, DOWN, buff=0.5)

        self.play(FadeIn(verdict_label, shift=UP * 0.2), run_time=0.7)
        self.play(Write(verdict), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(verdict_label), FadeOut(verdict), run_time=0.6)

        # 6. End card
        end1 = Text("Maps, satellites & GeoAI", font_size=34, color=WHITE, weight=BOLD)
        end2 = Text("Follow for more", font_size=30, color=ACCENT, weight=BOLD)
        end_group = VGroup(end1, end2).arrange(DOWN, buff=0.4).move_to(ORIGIN)
        self.play(FadeIn(end_group, scale=1.05), run_time=0.8)
        self.wait(1.3)
        self.play(FadeOut(end_group), run_time=0.5)

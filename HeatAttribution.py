from manim import *

config.frame_width = 8.0
config.frame_height = 14.22
config.pixel_width = 1080
config.pixel_height = 1920
config.background_color = "#0b1c17"

ACCENT = "#39d98a"
DIM = "#7fa89a"


class HeatAttribution(Scene):
    def construct(self):
        self.camera.background_color = "#0b1c17"

        # 1. Hook
        hook1 = Text("106°F in New Jersey.", font_size=40, color=WHITE, weight=BOLD)
        hook2 = Text("This week.", font_size=40, color=WHITE, weight=BOLD)
        hook_group = VGroup(hook1, hook2).arrange(DOWN, buff=0.3).move_to(UP * 4.5)
        self.play(Write(hook1), run_time=0.8)
        self.play(Write(hook2), run_time=0.6)
        self.wait(0.4)

        claim = Text(
            "Scientists just proved this doesn't\nhappen without us.",
            font_size=30, color=ACCENT, weight=BOLD, line_spacing=1.2,
        ).next_to(hook_group, DOWN, buff=0.6)
        self.play(FadeIn(claim, shift=UP * 0.3), run_time=0.9)
        self.wait(0.8)
        self.play(FadeOut(hook_group), FadeOut(claim), run_time=0.5)

        # 2. Two temperature distributions
        title = Text("Climate attribution science", font_size=32, color=WHITE, weight=BOLD)
        title.move_to(UP * 5.8)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.6)

        axes = Axes(
            x_range=[-4, 6, 1],
            y_range=[0, 1.1, 1],
            x_length=6.2,
            y_length=3.6,
            axis_config={"color": DIM, "stroke_width": 2, "include_tip": False},
            tips=False,
        ).move_to(UP * 1.7)

        def bell(mu, sigma=1.3):
            return lambda x: np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

        natural_curve = axes.plot(bell(0), color=DIM, stroke_width=5)
        actual_curve = axes.plot(bell(2.2), color=ACCENT, stroke_width=5)

        natural_label = Text("Natural world", font_size=22, color=DIM).next_to(
            axes, DOWN, buff=0.35
        ).shift(LEFT * 1.6)
        actual_label = Text("Actual world (2026)", font_size=22, color=ACCENT).next_to(
            natural_label, DOWN, buff=0.25
        ).align_to(natural_label, LEFT)

        self.play(Create(axes), run_time=0.7)
        self.play(Create(natural_curve), FadeIn(natural_label), run_time=0.9)
        self.wait(0.2)
        self.play(Create(actual_curve), FadeIn(actual_label), run_time=0.9)
        self.wait(0.3)

        # highlight the shifted tail = this heat wave
        tail_x = ValueTracker(3.4)
        marker = always_redraw(
            lambda: DashedLine(
                axes.c2p(tail_x.get_value(), 0),
                axes.c2p(tail_x.get_value(), bell(2.2)(tail_x.get_value())),
                color=WHITE,
                stroke_width=3,
            )
        )
        tag = Text("this heat wave", font_size=20, color=WHITE).next_to(
            axes.c2p(3.4, bell(2.2)(3.4)), UR, buff=0.15
        )
        self.play(Create(marker), FadeIn(tag), run_time=0.7)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(axes, natural_curve, actual_curve, natural_label,
                            actual_label, marker, tag, title)),
            run_time=0.6,
        )

        # 3. Explanation
        explain = Text(
            "Satellite temperature records +\nclimate models calculate how many\ntimes more likely an event is\nwith fossil-fuel warming.",
            font_size=28, color=WHITE, line_spacing=1.3,
        ).move_to(UP * 2.5)
        self.play(FadeIn(explain, shift=UP * 0.2), run_time=0.9)
        self.wait(1.4)
        self.play(FadeOut(explain), run_time=0.5)

        # 4. Punchline
        verdict_label = Text("World Weather Attribution, this week:", font_size=24, color=DIM)
        verdict_label.move_to(UP * 3.2)
        verdict = Text(
            '"Virtually impossible"\nwithout climate change.',
            font_size=36, color=ACCENT, weight=BOLD, line_spacing=1.3,
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

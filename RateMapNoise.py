from manim import *

config.frame_width = 8.0
config.frame_height = 14.22

INK = '#eaf2ef'
ACCENT = '#39d98a'
WARN = '#ff6b6b'
SKY = '#4aa8ff'
SAND = '#e8c268'
BG = '#0b1c17'

config.background_color = BG


def endcard(scene):
    brand = Text('Maps, satellites & GeoAI', font_size=34, color=INK)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT)
    follow = Text('Follow for more', font_size=30, color=ACCENT)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.4)
    scene.play(FadeIn(group))
    scene.wait(1.5)


class RateMapNoise(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "The BEST and the WORST\ncounty cancer rates are\nthe SAME counties",
            font_size=38,
            color=INK,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.9)
        hook.to_edge(UP, buff=0.9)

        self.add(hook)
        self.wait(1)

        setup = Text(
            "US kidney cancer death rates, county by county",
            font_size=24,
            color=SAND,
        ).scale_to_fit_width(config.frame_width * 0.85)
        setup.next_to(hook, DOWN, buff=0.6)
        self.play(FadeIn(setup))
        self.wait(0.5)

        big_dots = VGroup(*[
            Dot(radius=0.22, color="#1f3b33")
            for _ in range(36)
        ]).arrange_in_grid(rows=6, cols=6, buff=0.28)
        big_dots.move_to(ORIGIN + UP * 0.3)

        self.play(FadeIn(big_dots))
        self.wait(0.3)

        tiny_positions = [0, 5, 7, 12, 14, 17, 21, 23, 28, 30, 35, 3, 9, 26, 32]
        high_idx = [0, 12, 21, 30, 9]
        low_idx = [5, 14, 23, 28, 26]

        tiny_labels = VGroup()
        for i in tiny_positions:
            dot = big_dots[i]
            tiny = Dot(radius=0.1, color="#1f3b33").move_to(dot.get_center())
            tiny_labels.add(tiny)

        self.play(
            *[FadeOut(big_dots[i]) for i in tiny_positions],
            *[FadeIn(t) for t in tiny_labels],
        )
        self.wait(0.3)

        caption_small = Text(
            "Small counties: few people, few cases",
            font_size=22,
            color=INK,
        ).scale_to_fit_width(config.frame_width * 0.85)
        caption_small.next_to(big_dots, DOWN, buff=0.5)
        self.play(FadeIn(caption_small))
        self.wait(0.8)

        high_dots = VGroup(*[tiny_labels[tiny_positions.index(i)] for i in high_idx])
        low_dots = VGroup(*[tiny_labels[tiny_positions.index(i)] for i in low_idx])

        self.play(
            *[d.animate.set_color(WARN).scale(1.6) for d in high_dots],
            *[d.animate.set_color(SKY).scale(1.6) for d in low_dots],
        )
        self.wait(0.3)

        legend = VGroup(
            Dot(radius=0.12, color=WARN),
            Text("highest rate", font_size=20, color=WARN),
            Dot(radius=0.12, color=SKY),
            Text("lowest rate", font_size=20, color=SKY),
        ).arrange(RIGHT, buff=0.2)
        legend2 = VGroup(legend[0:2], legend[2:4]).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        legend2.next_to(caption_small, DOWN, buff=0.4)
        self.play(FadeIn(legend2))
        self.wait(1.2)

        self.play(FadeOut(caption_small), FadeOut(legend2), FadeOut(setup))

        fact = Text(
            "Both extremes cluster in the\nsame small, rural counties.\nIt is sampling noise, not risk.",
            font_size=26,
            color=INK,
            line_spacing=1.25,
        ).scale_to_fit_width(config.frame_width * 0.9)
        fact.next_to(big_dots, DOWN, buff=0.7)
        self.play(FadeIn(fact))
        self.wait(2)

        punch = Text(
            "A county of a few thousand people\nneeds just one extra case to swing\nfrom best in the US to worst.",
            font_size=24,
            color=ACCENT,
            line_spacing=1.25,
        ).scale_to_fit_width(config.frame_width * 0.88)
        punch.move_to(fact)

        self.play(FadeOut(fact), FadeIn(punch))
        self.wait(2)

        self.play(
            FadeOut(big_dots), FadeOut(tiny_labels), FadeOut(punch), FadeOut(hook)
        )
        endcard(self)

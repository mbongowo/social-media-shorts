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
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
    follow = Text('Follow for more', font_size=30, color=SAND)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.45)
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(1.4)


class CornBeltGlow(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'The US Corn Belt glows brighter\nthan the Amazon rainforest',
            font_size=38,
            color=INK,
            line_spacing=1.2,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        explainer = Text(
            "Photosynthesis makes a plant glow.\nA satellite can measure it.",
            font_size=24,
            color=INK,
            line_spacing=1.2,
        )
        explainer.scale_to_fit_width(config.frame_width * 0.85)
        explainer.move_to(UP * 2.9)
        self.play(FadeIn(explainer, shift=UP * 0.15))
        self.wait(0.9)
        self.play(FadeOut(explainer))

        baseline_y = -0.8
        amazon_h = 2.0
        corn_h = 2.8

        baseline = Line(LEFT * 2.7 + UP * baseline_y, RIGHT * 2.7 + UP * baseline_y, color=INK, stroke_width=2)

        amazon_bar = Rectangle(width=1.3, height=0.05, fill_color=ACCENT, fill_opacity=0.9, stroke_width=0)
        amazon_bar.move_to(LEFT * 1.7 + UP * baseline_y, aligned_edge=DOWN)

        corn_bar = Rectangle(width=1.3, height=0.05, fill_color=SAND, fill_opacity=0.9, stroke_width=0)
        corn_bar.move_to(RIGHT * 1.7 + UP * baseline_y, aligned_edge=DOWN)

        self.play(Create(baseline))
        self.play(
            amazon_bar.animate.stretch_to_fit_height(amazon_h, about_edge=DOWN),
            corn_bar.animate.stretch_to_fit_height(corn_h, about_edge=DOWN),
            run_time=1.2,
        )

        amazon_label = Text('Amazon', font_size=22, color=INK).next_to(amazon_bar, DOWN, buff=0.2)
        corn_label = Text('US Corn Belt', font_size=22, color=INK).next_to(corn_bar, DOWN, buff=0.2)
        self.play(FadeIn(amazon_label), FadeIn(corn_label))
        self.wait(0.4)

        ref_line = DashedLine(
            LEFT * 2.7 + UP * (baseline_y + amazon_h),
            RIGHT * 2.7 + UP * (baseline_y + amazon_h),
            color=INK,
            stroke_width=2,
            dash_length=0.12,
        )
        self.play(Create(ref_line))

        plus40 = Text('+40%', font_size=30, color=ACCENT, weight=BOLD)
        plus40.move_to(RIGHT * 1.7 + UP * (baseline_y + corn_h + 0.45))
        self.play(FadeIn(plus40, scale=0.7))
        self.wait(1.0)

        fact = Text(
            'GOME-2 satellite data, 2007-2011:\nJuly glow over the Corn Belt topped\nthe Amazon rainforest by about 40%',
            font_size=24,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        scene_group = VGroup(
            baseline, amazon_bar, corn_bar,
            amazon_label, corn_label, ref_line, plus40,
        )
        self.play(FadeOut(hook), FadeOut(fact), FadeOut(scene_group))

        punch = Text(
            'For a few weeks a year,\nfarmland out-glows a rainforest.',
            font_size=32,
            color=ACCENT,
            line_spacing=1.2,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(punch))

        endcard(self)

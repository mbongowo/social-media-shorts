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


class GeoTimeTwin(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'Satellites taught\nthis AI for free',
            font_size=42,
            color=INK,
            line_spacing=1.15,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        pin = Triangle(color=WARN, fill_color=WARN, fill_opacity=1).scale(0.22)
        pin.rotate(PI)
        pin.move_to(UP * 3.9)
        pin_label = Text('same pin', font_size=24, color=SAND).next_to(pin, UP, buff=0.2)

        chip1 = Square(side_length=1.5, color=SKY, fill_color=SKY, fill_opacity=0.25)
        chip1.move_to(LEFT * 1.5 + UP * 2.2)
        chip2 = Square(side_length=1.5, color=SKY, fill_color=SKY, fill_opacity=0.25)
        chip2.move_to(RIGHT * 1.5 + UP * 2.2)
        chip1_label = Text('day 1', font_size=24, color=INK).next_to(chip1, DOWN, buff=0.2)
        chip2_label = Text('day 90', font_size=24, color=INK).next_to(chip2, DOWN, buff=0.2)

        self.play(FadeIn(pin), FadeIn(pin_label))
        self.play(FadeIn(chip1), FadeIn(chip1_label), FadeIn(chip2), FadeIn(chip2_label))

        bracket = Line(chip1.get_right(), chip2.get_left(), color=ACCENT, stroke_width=5)
        pair_label = Text('free training pair', font_size=26, color=ACCENT, weight=BOLD)
        pair_label.next_to(bracket, DOWN, buff=0.15)
        self.play(Create(bracket), FadeIn(pair_label))
        self.wait(0.8)

        self.play(
            FadeOut(pin), FadeOut(pin_label), FadeOut(chip1), FadeOut(chip1_label),
            FadeOut(chip2), FadeOut(chip2_label), FadeOut(bracket), FadeOut(pair_label),
        )

        base_y = -1.6
        max_h = 3.2
        std_h = max_h * 0.72
        geo_h = max_h * 1.0

        std_bar = Rectangle(width=1.7, height=0.02, color=SKY, fill_color=SKY, fill_opacity=1)
        std_bar.move_to(LEFT * 1.6 + UP * base_y, aligned_edge=DOWN)
        geo_bar = Rectangle(width=1.7, height=0.02, color=ACCENT, fill_color=ACCENT, fill_opacity=1)
        geo_bar.move_to(RIGHT * 1.6 + UP * base_y, aligned_edge=DOWN)

        std_label = Text('standard AI', font_size=26, color=INK).next_to(std_bar, DOWN, buff=0.25)
        geo_label = Text('geo-aware AI', font_size=26, color=INK).next_to(geo_bar, DOWN, buff=0.25)

        self.play(
            std_bar.animate.stretch_to_fit_height(std_h).move_to(LEFT * 1.6 + UP * base_y, aligned_edge=DOWN),
            geo_bar.animate.stretch_to_fit_height(geo_h).move_to(RIGHT * 1.6 + UP * base_y, aligned_edge=DOWN),
            run_time=1.3,
        )
        plus8 = Text('+8%', font_size=34, color=ACCENT, weight=BOLD).next_to(geo_bar, UP, buff=0.2)
        self.play(FadeIn(std_label), FadeIn(geo_label), FadeIn(plus8))
        self.wait(0.6)

        fact = Text(
            'No human labeled a single\nphoto, and it still won',
            font_size=32,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.2)

        self.play(
            FadeOut(hook), FadeOut(std_bar), FadeOut(geo_bar), FadeOut(std_label),
            FadeOut(geo_label), FadeOut(plus8), FadeOut(fact),
        )

        punch = Text(
            'The GPS tag was free\ntraining data all along',
            font_size=34,
            color=ACCENT,
            line_spacing=1.2,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(punch))

        endcard(self)

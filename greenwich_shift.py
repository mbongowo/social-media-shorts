from manim import *

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


class GreenwichShift(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Stand on Greenwich's meridian line?\nYour GPS says you are 102 m off.",
            color=INK,
            font_size=38,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 5.1)
        self.add(hook)
        self.wait(1)

        ground = Line(LEFT * 3.2, RIGHT * 3.2, color=INK, stroke_width=2)
        ground.move_to(UP * 0.2)

        old_line = Line(UP * 1.6, DOWN * 0.9, color=SAND, stroke_width=6)
        old_line.move_to(LEFT * 1.9 + UP * 0.35)
        old_label = Text('Brass strip\nlaid in 1884', color=SAND, font_size=20, line_spacing=1.1)
        old_label.next_to(old_line, DOWN, buff=0.3)

        new_line = Line(UP * 1.6, DOWN * 0.9, color=ACCENT, stroke_width=6)
        new_line.move_to(RIGHT * 1.9 + UP * 0.35)
        new_label = Text('0 deg longitude\non GPS today', color=ACCENT, font_size=20, line_spacing=1.1)
        new_label.next_to(new_line, DOWN, buff=0.3)

        self.play(Create(ground), run_time=0.5)
        self.play(Create(old_line), FadeIn(old_label), run_time=0.7)
        self.wait(0.3)
        self.play(Create(new_line), FadeIn(new_label), run_time=0.7)
        self.wait(0.4)

        gap = DoubleArrow(
            old_line.get_center() + UP * 1.3,
            new_line.get_center() + UP * 1.3,
            color=WARN,
            stroke_width=4,
            buff=0,
        )
        gap_label = Text('102 m', color=WARN, font_size=26).next_to(gap, UP, buff=0.15)
        self.play(GrowFromCenter(gap), FadeIn(gap_label), run_time=0.7)
        self.wait(1.3)

        self.play(
            FadeOut(ground), FadeOut(old_line), FadeOut(old_label),
            FadeOut(new_line), FadeOut(new_label), FadeOut(gap), FadeOut(gap_label),
            run_time=0.4,
        )

        fact = Text(
            "Earth's gravity bends old astronomical\nlongitude; modern GPS fixes on the\nplanet's center of mass instead (Malys et al., 2015)",
            color=INK,
            font_size=23,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.9)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "GPS did not move the meridian.\nIt just stopped trusting gravity.",
            color=ACCENT,
            font_size=30,
            line_spacing=1.1,
        )
        punch.scale_to_fit_width(config.frame_width * 0.88)
        punch.move_to(ORIGIN)
        self.play(FadeOut(fact), run_time=0.4)
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(hook), FadeOut(punch), run_time=0.4)
        endcard(self)

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


class LabelPacking(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'Map labels have\nno perfect answer',
            font_size=42,
            color=INK,
            line_spacing=1.15,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        city_pts = [LEFT * 2.0 + UP * 3.0, RIGHT * 1.6 + UP * 3.4, ORIGIN + UP * 2.6]
        dots = VGroup(*[Dot(point=p, color=SAND, radius=0.09) for p in city_pts])
        self.play(FadeIn(dots))

        box1 = Rectangle(width=1.7, height=0.6, color=WARN, fill_color=WARN, fill_opacity=0.35)
        box1.move_to(city_pts[0] + RIGHT * 0.6 + UP * 0.15)
        box2 = Rectangle(width=1.7, height=0.6, color=WARN, fill_color=WARN, fill_opacity=0.35)
        box2.move_to(city_pts[1] + RIGHT * 0.2 + UP * 0.05)
        box3 = Rectangle(width=1.7, height=0.6, color=WARN, fill_color=WARN, fill_opacity=0.35)
        box3.move_to(city_pts[2] + RIGHT * 0.5 + DOWN * 0.05)
        boxes = VGroup(box1, box2, box3)
        clash = Text('overlap', font_size=26, color=WARN, weight=BOLD).move_to(UP * 2.85 + RIGHT * 0.1)

        self.play(FadeIn(boxes))
        self.play(FadeIn(clash, shift=UP * 0.1))
        self.wait(0.6)
        self.play(FadeOut(clash))

        target1 = box1.copy().set_color(ACCENT).set_fill(ACCENT, opacity=0.3).move_to(city_pts[0] + LEFT * 1.0 + UP * 0.6)
        target2 = box2.copy().set_color(ACCENT).set_fill(ACCENT, opacity=0.3).move_to(city_pts[1] + RIGHT * 1.1 + UP * 0.5)
        target3 = box3.copy().set_color(ACCENT).set_fill(ACCENT, opacity=0.3).move_to(city_pts[2] + DOWN * 0.8)

        self.play(
            Transform(box1, target1),
            Transform(box2, target2),
            Transform(box3, target3),
            run_time=1.2,
        )
        fixed = Text('a fix, not the fix', font_size=24, color=ACCENT).move_to(UP * 1.5)
        self.play(FadeIn(fixed, shift=UP * 0.1))
        self.wait(0.8)

        self.play(FadeOut(dots), FadeOut(boxes), FadeOut(fixed))

        fact = Text(
            'Proven NP-hard in 1991.\nBest guarantee: within 2x\nof the optimal fit',
            font_size=30,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.4)

        self.play(FadeOut(hook), FadeOut(fact))

        punch = Text(
            'Every map app you use\nis guessing, not solving',
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

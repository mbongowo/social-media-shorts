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


class LineSimplifyTwins(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'This 1973 trick decides\nwhich map points survive',
            font_size=40,
            color=INK,
            line_spacing=1.2,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        raw_pts = [
            (-2.9, 3.6), (-2.2, 2.9), (-1.5, 3.9), (-0.8, 2.6),
            (-0.1, 3.6), (0.6, 2.5), (1.3, 3.5), (2.0, 2.8), (2.7, 3.4),
        ]
        raw_coords = [np.array([x, y, 0]) for x, y in raw_pts]

        raw_line = VMobject(color=SKY, stroke_width=4)
        raw_line.set_points_as_corners(raw_coords)
        raw_dots = VGroup(*[Dot(p, color=SKY, radius=0.075) for p in raw_coords])

        raw_label = Text('raw digitized line, 9 points', font_size=22, color=INK).move_to(UP * 1.5)

        self.play(Create(raw_line), run_time=1.1)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in raw_dots], lag_ratio=0.08), run_time=0.9)
        self.play(FadeIn(raw_label, shift=UP * 0.1))
        self.wait(0.7)

        keep_idx = [0, 2, 5, 8]
        drop_idx = [i for i in range(len(raw_coords)) if i not in keep_idx]

        drop_marks = VGroup(*[
            Cross(scale_factor=0.12, color=WARN, stroke_width=3).move_to(raw_coords[i])
            for i in drop_idx
        ])
        self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in drop_marks], lag_ratio=0.1), run_time=0.9)
        self.wait(0.5)

        keep_coords = [raw_coords[i] for i in keep_idx]
        simple_line = VMobject(color=ACCENT, stroke_width=6)
        simple_line.set_points_as_corners(keep_coords)
        keep_dots = VGroup(*[Dot(p, color=ACCENT, radius=0.09) for p in keep_coords])

        self.play(
            FadeOut(drop_marks),
            *[FadeOut(raw_dots[i]) for i in drop_idx],
            Transform(raw_line, simple_line),
            run_time=1.0,
        )
        self.play(*[Transform(raw_dots[i], keep_dots[j]) for j, i in enumerate(keep_idx)])
        self.wait(0.3)

        simple_label = Text('same shape, 4 points', font_size=22, color=ACCENT).move_to(UP * 1.5)
        self.play(Transform(raw_label, simple_label))
        self.wait(0.9)

        scene_group = VGroup(raw_line, raw_dots, raw_label)
        self.play(FadeOut(scene_group))

        ramer = VGroup(
            Text('Ramer', font_size=26, color=INK, weight=BOLD),
            Text('Switzerland, 1972', font_size=20, color=SAND),
        ).arrange(DOWN, buff=0.15).move_to(LEFT * 1.9 + UP * 0.8)

        dp = VGroup(
            Text('Douglas and Peucker', font_size=26, color=INK, weight=BOLD),
            Text('Canada, 1973', font_size=20, color=SAND),
        ).arrange(DOWN, buff=0.15).move_to(RIGHT * 1.9 + UP * 0.8)

        equals = Text('=', font_size=40, color=ACCENT, weight=BOLD).move_to(UP * 0.8)

        self.play(FadeIn(ramer, shift=RIGHT * 0.2), FadeIn(dp, shift=LEFT * 0.2))
        self.play(FadeIn(equals, scale=1.3))
        self.wait(1.1)

        self.play(FadeOut(ramer), FadeOut(dp), FadeOut(equals))

        fact = Text(
            'Same fix, invented an ocean apart,\nneither one knowing of the other',
            font_size=26,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.6)

        self.play(FadeOut(hook), FadeOut(fact))

        punch = Text(
            'Every time a map zooms out,\nit is still running their algorithm.',
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

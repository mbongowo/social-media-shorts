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
    brand = Text('Maps, satellites & GeoAI', font_size=30, color=INK)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT)
    follow = Text('Follow for more', font_size=26, color=ACCENT)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.35)
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(0.9)


def neural_net(color=ACCENT):
    layers = [2, 3, 2]
    xs = [-0.7, 0, 0.7]
    cols = VGroup()
    for x, n in zip(xs, layers):
        col = VGroup(*[Dot(radius=0.09, color=color) for _ in range(n)]).arrange(DOWN, buff=0.32)
        col.move_to(RIGHT * x)
        cols.add(col)
    lines = VGroup()
    for a, b in zip(cols[:-1], cols[1:]):
        for d1 in a:
            for d2 in b:
                lines.add(Line(d1.get_center(), d2.get_center(), stroke_width=1, color=color, stroke_opacity=0.5))
    return VGroup(lines, cols)


class PovertyFromSpace(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'An AI guessed local wealth\nfrom a satellite photo alone',
            font_size=42,
            color=INK,
            line_spacing=1.1,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 5.6)
        self.add(hook)
        self.wait(1)

        day = Square(side_length=1.6, color=SAND, fill_color=SAND, fill_opacity=0.85, stroke_width=2, stroke_color=BG)
        day.move_to(LEFT * 1.8 + UP * 2.6)
        day_grid = VGroup(*[
            Line(
                day.get_corner(UL) + RIGHT * i * 0.4,
                day.get_corner(UL) + RIGHT * i * 0.4 + DOWN * 1.6,
                stroke_width=1, color=BG,
            )
            for i in range(1, 4)
        ])

        night = Square(side_length=1.6, color=INK, fill_color=BG, fill_opacity=1, stroke_width=2, stroke_color=INK)
        night.move_to(RIGHT * 1.8 + UP * 2.6)
        lights = VGroup(*[
            Dot(radius=0.07, color=SAND).move_to(night.get_center() + np.array([x, y, 0]))
            for x, y in [(-0.4, 0.3), (0.2, 0.5), (0.5, -0.2), (-0.2, -0.4), (0.1, 0.0)]
        ])

        label_top = Text('two views of one place', font_size=24, color=INK)
        label_top.scale_to_fit_width(config.frame_width * 0.75)
        label_top.next_to(VGroup(day, night), UP, buff=0.35)

        tag_day = Text('daytime photo', font_size=18, color=INK)
        tag_day.next_to(day, DOWN, buff=0.2)
        tag_night = Text('night lights', font_size=18, color=SAND)
        tag_night.next_to(night, DOWN, buff=0.2)

        self.play(FadeIn(label_top))
        self.play(FadeIn(day), FadeIn(day_grid), FadeIn(night), FadeIn(lights))
        self.play(FadeIn(tag_day), FadeIn(tag_night))
        self.wait(0.8)

        net = neural_net(color=ACCENT)
        net.scale(0.9)
        net.move_to(DOWN * 0.4)
        net_label = Text('a neural net links them', font_size=22, color=ACCENT)
        net_label.scale_to_fit_width(config.frame_width * 0.8)
        net_label.next_to(net, DOWN, buff=0.3)

        self.play(
            FadeOut(tag_day), FadeOut(tag_night), FadeOut(label_top),
            day.animate.scale(0.4).move_to(UP * 1.0 + LEFT * 0.9),
            day_grid.animate.scale(0.4).move_to(UP * 1.0 + LEFT * 0.9),
            night.animate.scale(0.4).move_to(UP * 1.0 + RIGHT * 0.9),
            lights.animate.scale(0.4).move_to(UP * 1.0 + RIGHT * 0.9),
        )
        self.play(FadeIn(net), FadeIn(net_label))
        self.wait(0.8)

        meter_box = Rectangle(width=0.5, height=1.6, color=INK, stroke_width=2)
        meter_box.move_to(DOWN * 2.6)
        meter_fill = Rectangle(width=0.5, height=0.1, color=ACCENT, fill_color=ACCENT, fill_opacity=1, stroke_width=0)
        meter_fill.move_to(meter_box.get_bottom() + UP * 0.05)
        meter_label = Text('predicted wealth', font_size=20, color=INK)
        meter_label.next_to(meter_box, DOWN, buff=0.25)

        self.play(FadeIn(meter_box), FadeIn(meter_label))
        self.play(
            meter_fill.animate.stretch_to_fit_height(1.2, about_edge=DOWN).move_to(
                meter_box.get_bottom() + UP * 0.6
            )
        )
        self.wait(0.6)

        self.play(FadeOut(VGroup(day, day_grid, night, lights, net, net_label, meter_box, meter_fill, meter_label)))

        fact = Text(
            'Trained on night lights as a\nwealth clue, the model explained\nup to 75% of local economic\nvariation in five African countries',
            font_size=27,
            color=INK,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.2)

        cite = Text('Jean et al., Science 2016', font_size=18, color=SAND)
        cite.scale_to_fit_width(config.frame_width * 0.8)
        cite.next_to(fact, DOWN, buff=0.3)

        self.play(FadeIn(fact, shift=UP * 0.2))
        self.play(FadeIn(cite))
        self.wait(1.4)

        punch = Text(
            'No survey door\nwas ever knocked.',
            font_size=36,
            color=ACCENT,
            line_spacing=1.15,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)

        self.play(
            FadeOut(hook),
            FadeOut(fact),
            FadeOut(cite),
        )
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.0)
        self.play(FadeOut(punch))

        endcard(self)

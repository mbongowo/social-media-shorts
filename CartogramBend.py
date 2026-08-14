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


class CartogramBend(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'Some maps make a small\ncountry outsize a giant one',
            font_size=44,
            color=INK,
            line_spacing=1.1,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 5.6)
        self.add(hook)
        self.wait(1)

        big = Circle(radius=1.4, color=SAND, fill_color=SAND, fill_opacity=0.9, stroke_width=2, stroke_color=BG)
        small = Circle(radius=0.6, color=SKY, fill_color=SKY, fill_opacity=0.9, stroke_width=2, stroke_color=BG)
        big.move_to(LEFT * 1.8 + UP * 1.8)
        small.move_to(RIGHT * 1.8 + UP * 1.8)

        label_land = Text('sized by land area', font_size=24, color=INK)
        label_land.scale_to_fit_width(config.frame_width * 0.7)
        label_land.next_to(VGroup(big, small), UP, buff=0.35)

        tag_big = Text('more land', font_size=20, color=INK)
        tag_big.next_to(big, DOWN, buff=0.2)
        tag_small = Text('less land', font_size=20, color=INK)
        tag_small.next_to(small, DOWN, buff=0.2)

        self.play(FadeIn(label_land))
        self.play(FadeIn(big, scale=0.8), FadeIn(small, scale=0.8))
        self.play(FadeIn(tag_big), FadeIn(tag_small))
        self.wait(0.6)

        label_pop = Text('sized by population', font_size=24, color=ACCENT)
        label_pop.scale_to_fit_width(config.frame_width * 0.7)
        label_pop.move_to(label_land.get_center())

        tag_big2 = Text('fewer people', font_size=20, color=INK)
        tag_small2 = Text('more people', font_size=20, color=INK)

        self.play(
            big.animate.scale(0.6 / 1.4),
            small.animate.scale(1.7 / 0.6),
            Transform(label_land, label_pop),
        )
        tag_big2.next_to(big, DOWN, buff=0.2)
        tag_small2.next_to(small, DOWN, buff=0.2)
        self.play(
            Transform(tag_big, tag_big2),
            Transform(tag_small, tag_small2),
        )
        self.wait(0.8)

        self.play(FadeOut(VGroup(big, small, tag_big, tag_small, label_land)))

        fact = Text(
            'A 2004 algorithm resizes\nregions by treating population\nlike a gas that spreads out\nevenly, pulling borders along',
            font_size=28,
            color=INK,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.1)

        cite = Text('Gastner and Newman, PNAS 2004', font_size=18, color=SAND)
        cite.scale_to_fit_width(config.frame_width * 0.8)
        cite.next_to(fact, DOWN, buff=0.3)

        self.play(FadeIn(fact, shift=UP * 0.2))
        self.play(FadeIn(cite))
        self.wait(1.4)

        punch = Text(
            'The shape moved.\nThe count did not.',
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

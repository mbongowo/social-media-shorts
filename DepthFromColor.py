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
    follow = Text('Follow for more', font_size=30, color=ACCENT)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.4)
    group.move_to(ORIGIN)
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(1.2)


class DepthFromColor(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = VGroup(
            Text('A satellite can measure', font_size=40, color=INK),
            Text('ocean depth with no sonar.', font_size=40, color=INK),
        ).arrange(DOWN, buff=0.18)
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.4)

        self.add(hook)
        self.wait(1)

        water = Rectangle(
            width=config.frame_width * 0.82, height=5.4,
            fill_color=SKY, fill_opacity=0.35, stroke_color=SKY, stroke_width=2,
        ).move_to(UP * 1.1)

        seafloor = Polygon(
            water.get_corner(DL), water.get_corner(DR),
            water.get_corner(DR) + DOWN * 0.3,
            water.get_corner(DL) + DOWN * 0.9,
            fill_color=SAND, fill_opacity=0.9, stroke_width=0,
        )

        surface_line = Line(water.get_corner(UL), water.get_corner(UR), color=INK, stroke_width=3)

        self.play(FadeIn(water), FadeIn(seafloor), FadeIn(surface_line))
        self.wait(0.3)

        blue_arrow = Arrow(
            start=water.get_top() + LEFT * 1.4 + UP * 0.4,
            end=seafloor.get_center() + LEFT * 1.4 + DOWN * 0.1,
            color=SKY, stroke_width=6, buff=0,
        )
        blue_label = Text('B', font_size=30, color=SKY).next_to(blue_arrow, LEFT, buff=0.15)

        green_arrow = Arrow(
            start=water.get_top() + RIGHT * 1.4 + UP * 0.4,
            end=water.get_center() + RIGHT * 1.4,
            color=ACCENT, stroke_width=6, buff=0,
        )
        green_label = Text('G', font_size=30, color=ACCENT).next_to(green_arrow, RIGHT, buff=0.15)

        self.play(GrowArrow(blue_arrow), FadeIn(blue_label))
        self.play(GrowArrow(green_arrow), FadeIn(green_label))
        self.wait(0.4)

        note = Text('Blue light reaches deeper than green.', font_size=26, color=INK)
        note.scale_to_fit_width(config.frame_width * 0.82)
        note.next_to(seafloor, DOWN, buff=0.5)
        self.play(FadeIn(note, shift=UP * 0.2))
        self.wait(1.0)

        ratio = Text('Blue/Green ratio -> depth', font_size=30, color=ACCENT)
        ratio.scale_to_fit_width(config.frame_width * 0.82)
        ratio.move_to(note.get_center())

        self.play(FadeOut(note), FadeIn(ratio, shift=UP * 0.2))
        self.wait(1.0)

        headline = Text('Past 25 m deep', font_size=46, color=WARN)
        headline.scale_to_fit_width(config.frame_width * 0.75)
        headline.move_to(ratio.get_center())

        self.play(FadeOut(ratio), FadeIn(headline, shift=UP * 0.2))
        self.wait(1.2)

        self.play(
            FadeOut(headline), FadeOut(water), FadeOut(seafloor), FadeOut(surface_line),
            FadeOut(blue_arrow), FadeOut(blue_label), FadeOut(green_arrow), FadeOut(green_label),
        )

        fact = VGroup(
            Text('In clear water, comparing blue', font_size=28, color=INK),
            Text('and green light let a satellite', font_size=28, color=INK),
            Text('read seafloor depth past 25 m,', font_size=28, color=INK),
            Text('matched against lidar truth.', font_size=28, color=INK),
            Text('Stumpf, Holderied and Sinclair,', font_size=22, color=SAND),
            Text('2003, Limnology and Oceanography.', font_size=22, color=SAND),
        ).arrange(DOWN, buff=0.14)
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)

        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(2.2)

        punch = Text("The sea's color is a depth gauge.", font_size=32, color=ACCENT)
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(DOWN * 2.2)

        self.play(FadeOut(fact), FadeIn(punch, shift=UP * 0.2))
        self.wait(1.5)

        self.play(FadeOut(punch), FadeOut(hook))
        endcard(self)

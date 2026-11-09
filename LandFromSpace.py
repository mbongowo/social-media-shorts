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
    title = Text('Maps, satellites & GeoAI', font_size=36, color=INK)
    title.scale_to_fit_width(config.frame_width * 0.85)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
    follow = Text('Follow for more', font_size=30, color=ACCENT)
    group = VGroup(title, line, follow).arrange(DOWN, buff=0.4)
    scene.add(group)
    scene.wait(1.5)


class LandFromSpace(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "It never set foot on\nthe ground. It learned to\nread it anyway.",
            font_size=46,
            color=INK,
            line_spacing=1.2,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.to_edge(UP, buff=0.9)

        self.add(hook)
        self.wait(1)

        setup = Text(
            "27,000 satellite photos.\nTen land types.\nOne neural network.",
            font_size=30,
            color=INK,
            line_spacing=1.25,
        )
        setup.scale_to_fit_width(config.frame_width * 0.82)
        setup.move_to(UP * 1.2)

        self.play(FadeIn(setup))
        self.wait(1.5)
        self.play(FadeOut(setup))

        # Diagram: a grid of colored satellite tiles (crop, forest, water,
        # urban) feeds into a CNN box, which outputs one correctly labeled tile.
        colors = [SAND, ACCENT, SKY, WARN, ACCENT, SAND, SKY, SAND, ACCENT]
        tiles = VGroup(*[
            Square(side_length=0.5, color=c, fill_color=c, fill_opacity=0.9, stroke_width=1)
            for c in colors
        ])
        tiles.arrange_in_grid(rows=3, cols=3, buff=0.08)
        tiles_label = Text("satellite patches", font_size=18, color=INK)
        tiles_label.scale_to_fit_width(2.0)
        tiles_label.next_to(tiles, DOWN, buff=0.15)
        tiles_group = VGroup(tiles, tiles_label)

        arrow1 = Arrow(ORIGIN, RIGHT * 0.9, color=INK, buff=0, stroke_width=3)

        cnn_box = Rectangle(width=1.3, height=0.6, color=SKY, stroke_width=3)
        cnn_label = Text("CNN", font_size=22, color=SKY)
        cnn_label.move_to(cnn_box.get_center())
        cnn_group = VGroup(cnn_box, cnn_label)

        arrow2 = Arrow(ORIGIN, RIGHT * 0.9, color=INK, buff=0, stroke_width=3)

        out_tile = Square(side_length=0.6, color=ACCENT, fill_color=ACCENT, fill_opacity=0.9, stroke_width=2)
        out_label = Text("forest: correct", font_size=18, color=ACCENT)
        out_label.scale_to_fit_width(1.6)
        out_label.next_to(out_tile, DOWN, buff=0.12)
        out_group = VGroup(out_tile, out_label)

        row = VGroup(tiles_group, arrow1, cnn_group, arrow2, out_group).arrange(RIGHT, buff=0.25)
        row.scale_to_fit_width(config.frame_width * 0.88)
        row.move_to(UP * 0.4)

        self.play(FadeIn(row))
        self.wait(2)
        self.play(FadeOut(row))

        number = Text("98.57%", font_size=68, color=ACCENT)
        number.scale_to_fit_width(config.frame_width * 0.7)
        number_sub = Text("accuracy classifying land cover\nfrom Sentinel-2 image patches", font_size=24, color=INK, line_spacing=1.2)
        number_sub.scale_to_fit_width(config.frame_width * 0.8)
        number_group = VGroup(number, number_sub).arrange(DOWN, buff=0.3)
        number_group.move_to(UP * 0.4)

        self.play(FadeIn(number_group))
        self.wait(2)

        fact = Text(
            "Helber, Bischke, Dengel & Borth\nbuilt this benchmark (EuroSAT),\nIEEE JSTARS, 2019.",
            font_size=23,
            color=INK,
            line_spacing=1.25,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.to_edge(DOWN, buff=1.6)

        self.play(FadeOut(number_group))
        self.add(fact)
        self.wait(2.5)

        punch = Text(
            "The ground truth\ncame from orbit.",
            font_size=34,
            color=ACCENT,
            line_spacing=1.2,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)

        self.play(FadeOut(fact), FadeOut(hook))
        self.play(FadeIn(punch))
        self.wait(2)
        self.play(FadeOut(punch))

        endcard(self)

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


def choropleth_grid(colors):
    squares = VGroup()
    for row in range(3):
        for col in range(3):
            sq = Square(side_length=0.78, fill_opacity=1, stroke_color=BG, stroke_width=3)
            sq.set_fill(colors[row * 3 + col])
            sq.move_to(RIGHT * (col - 1) * 0.85 + UP * (1 - row) * 0.85)
            squares.add(sq)
    return squares


class ColorBlindMaps(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            '8 PERCENT OF MEN\nCANNOT READ THIS MAP',
            font_size=40,
            color=INK,
            line_spacing=1.2,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        label1 = Text('a normal choropleth map', font_size=22, color=SAND)
        label1.move_to(UP * 2.6)

        red_green = ['#c0392b', '#e67e22', '#e8c268', '#7fbf6a', '#2e8b3a',
                     '#e67e22', '#e8c268', '#7fbf6a', '#c0392b']
        grid1 = choropleth_grid(red_green)
        grid1.move_to(UP * 0.9)

        self.play(FadeIn(label1), Create(grid1), run_time=1.1)
        self.wait(1.0)

        label2 = Text('how it looks to a colorblind viewer', font_size=20, color=WARN)
        label2.move_to(DOWN * 1.6)

        confused = ['#a68a5a', '#c89a4e', '#e8c268', '#b4a25a', '#8c8248',
                    '#c89a4e', '#e8c268', '#b4a25a', '#a68a5a']
        grid2 = choropleth_grid(confused)
        grid2.move_to(DOWN * 3.3)

        self.play(FadeIn(label2), Create(grid2), run_time=1.1)
        self.wait(1.5)

        self.play(
            FadeOut(label1), FadeOut(grid1),
            FadeOut(label2), FadeOut(grid2),
        )

        fact = Text(
            'About 8% of men of Northern\nEuropean descent have red-green\ncolor blindness.\nNeitz and Neitz, Vision Research, 2011.',
            font_size=24,
            color=INK,
            line_spacing=1.25,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(2.0)

        self.play(FadeOut(hook), FadeOut(fact))

        label3 = Text('the colorblind safe fix', font_size=22, color=ACCENT)
        label3.move_to(UP * 2.0)

        safe = [SKY, '#88c4f8', SAND, '#88c4f8', '#c9c9c9',
                SAND, SKY, '#88c4f8', SAND]
        grid3 = choropleth_grid(safe)
        grid3.move_to(UP * 0.3)

        self.play(FadeIn(label3), Create(grid3), run_time=1.1)
        self.wait(1.2)

        punch = Text(
            'Real maps go blue to orange,\nnot red to green.',
            font_size=32,
            color=ACCENT,
            line_spacing=1.2,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(DOWN * 3.6)
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.6)

        self.play(FadeOut(label3), FadeOut(grid3), FadeOut(punch))

        endcard(self)

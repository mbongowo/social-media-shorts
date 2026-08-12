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


class OnboardCloudFilter(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'This satellite\ndeletes its own photos',
            font_size=50,
            color=INK,
            line_spacing=1.1,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 5.6)
        self.play(FadeIn(hook, shift=DOWN * 0.2))
        self.wait(0.6)

        sat_body = Rectangle(width=0.9, height=0.5, color=INK, fill_color=INK, fill_opacity=1)
        panel_l = Rectangle(width=1.0, height=0.35, color=SKY, fill_color=SKY, fill_opacity=1)
        panel_l.next_to(sat_body, LEFT, buff=0.05)
        panel_r = Rectangle(width=1.0, height=0.35, color=SKY, fill_color=SKY, fill_opacity=1)
        panel_r.next_to(sat_body, RIGHT, buff=0.05)
        satellite = VGroup(sat_body, panel_l, panel_r)
        satellite.move_to(UP * 3.4)
        self.play(FadeIn(satellite, scale=0.8))
        self.wait(0.2)

        earth = Circle(radius=1.7, color=SKY, fill_color=SKY, fill_opacity=0.25, stroke_width=3)
        earth.move_to(DOWN * 1.6)
        self.play(FadeIn(earth, scale=0.9))

        tile_clear = Square(side_length=0.6, color=ACCENT, fill_color=ACCENT, fill_opacity=1, stroke_width=2, stroke_color=BG)
        tile_cloud1 = Square(side_length=0.6, color=INK, fill_color=INK, fill_opacity=1, stroke_width=2, stroke_color=BG)
        tile_cloud2 = Square(side_length=0.6, color=INK, fill_color=INK, fill_opacity=1, stroke_width=2, stroke_color=BG)
        tiles = VGroup(tile_cloud1, tile_clear, tile_cloud2).arrange(RIGHT, buff=0.15)
        tiles.move_to(UP * 1.2)
        self.play(LaggedStart(*[FadeIn(t, shift=DOWN * 0.2) for t in tiles], lag_ratio=0.2))
        self.wait(0.3)

        scan = Text('onboard AI scans each tile', font_size=26, color=SAND)
        scan.scale_to_fit_width(config.frame_width * 0.85)
        scan.next_to(tiles, UP, buff=0.35)
        self.play(FadeIn(scan))
        self.wait(0.4)

        cross1 = Cross(tile_cloud1, stroke_color=WARN, stroke_width=6)
        cross2 = Cross(tile_cloud2, stroke_color=WARN, stroke_width=6)
        check = Text('OK', font_size=22, color=BG, weight=BOLD)
        check.move_to(tile_clear.get_center())
        self.play(Create(cross1), Create(cross2), FadeIn(check))
        self.wait(0.3)

        down_arrow = Arrow(tile_clear.get_bottom(), earth.get_top(), color=ACCENT, buff=0.1, stroke_width=5)
        self.play(GrowArrow(down_arrow))
        self.play(FadeOut(VGroup(tile_cloud1, tile_cloud2, cross1, cross2)))
        self.wait(0.4)

        self.play(
            FadeOut(scan),
            FadeOut(down_arrow),
            FadeOut(VGroup(satellite, earth, tile_clear, check)),
        )

        fact = Text(
            'ESA\'s Phi-sat-1 ran a neural net\nin orbit that threw out cloudy\nimages before they were ever\nsent to the ground',
            font_size=28,
            color=INK,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.6)

        punch = Text(
            'The AI judged your\nphoto before you\never saw it',
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
        )
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.0)
        self.play(FadeOut(punch))

        endcard(self)

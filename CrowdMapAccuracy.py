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


class CrowdMapAccuracy(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'Untrained volunteers mapped\nroads as well as the pros',
            font_size=38,
            color=INK,
            line_spacing=1.15,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        os_label = Text('Ordnance Survey', font_size=24, color=SKY).move_to(UP * 3.1 + LEFT * 0.1)
        os_line = Line(LEFT * 3.0 + UP * 2.4, RIGHT * 3.0 + UP * 2.0, color=SKY, stroke_width=7)
        self.play(FadeIn(os_label))
        self.play(Create(os_line), run_time=0.9)

        osm_label = Text('OpenStreetMap', font_size=24, color=ACCENT).move_to(UP * 1.55 + LEFT * 0.15)
        osm_line = Line(LEFT * 3.0 + UP * 2.28, RIGHT * 3.0 + UP * 1.88, color=ACCENT, stroke_width=7)
        self.play(FadeIn(osm_label))
        self.play(Create(osm_line), run_time=0.9)
        self.wait(0.3)

        gap_arrow = DoubleArrow(
            os_line.get_center() + DOWN * 0.02,
            osm_line.get_center() + UP * 0.02,
            color=SAND,
            stroke_width=4,
            buff=0,
        )
        gap_label = Text('about 6m apart', font_size=24, color=SAND).next_to(gap_arrow, RIGHT, buff=0.3)
        self.play(GrowArrow(gap_arrow))
        self.play(FadeIn(gap_label, shift=UP * 0.1))
        self.wait(1.0)

        self.play(
            FadeOut(os_label), FadeOut(os_line),
            FadeOut(osm_label), FadeOut(osm_line),
            FadeOut(gap_arrow), FadeOut(gap_label),
        )

        bar_bg = Rectangle(width=4.6, height=0.7, color=INK, stroke_width=2).move_to(UP * 2.2)
        bar_fill = Rectangle(width=4.6 * 0.8, height=0.7, color=ACCENT, fill_color=ACCENT, fill_opacity=0.85, stroke_width=0)
        bar_fill.align_to(bar_bg, LEFT).align_to(bar_bg, UP)
        bar_caption = Text('motorway overlap: 80%', font_size=26, color=INK).next_to(bar_bg, DOWN, buff=0.35)

        self.play(Create(bar_bg))
        self.play(GrowFromPoint(bar_fill, bar_fill.get_left()), run_time=0.8)
        self.play(FadeIn(bar_caption, shift=UP * 0.1))
        self.wait(1.2)

        self.play(FadeOut(bar_bg), FadeOut(bar_fill), FadeOut(bar_caption))

        fact = Text(
            'OSM roads landed within\nabout 6m of official surveys,\n80% motorway overlap',
            font_size=28,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.4)

        self.play(FadeOut(hook), FadeOut(fact))

        punch = Text(
            'Thousands of strangers\nmapped for free.\nIt held up anyway',
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

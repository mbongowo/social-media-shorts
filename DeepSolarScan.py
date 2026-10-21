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
    title = Text('Maps, satellites & GeoAI', font_size=34, color=INK)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT)
    follow = Text('Follow for more', font_size=30, color=ACCENT)
    group = VGroup(title, line, follow).arrange(DOWN, buff=0.35)
    scene.add(group)
    scene.wait(1.4)


class DeepSolarScan(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "An AI scanned 1 BILLION\nsatellite tiles for solar panels",
            font_size=44,
            color=INK,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        setup = Text(
            "A CNN labeled each 100ft tile:\npanel, or no panel",
            font_size=28,
            color=INK,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.85)
        setup.move_to(UP * 2.6)
        self.play(FadeIn(setup))
        self.wait(1.2)
        self.play(FadeOut(setup))

        grid_rows, grid_cols = 6, 5
        tiles = VGroup()
        for r in range(grid_rows):
            for c in range(grid_cols):
                sq = Square(side_length=0.62, color=INK, fill_opacity=0.08, stroke_width=1.5)
                sq.move_to(
                    RIGHT * (c - (grid_cols - 1) / 2) * 0.72
                    + DOWN * (r - (grid_rows - 1) / 2) * 0.72
                )
                tiles.add(sq)
        tiles.move_to(UP * 0.5)
        self.play(FadeIn(tiles), run_time=1.0)

        hit_indices = [2, 7, 9, 14, 17, 22, 27]
        hits = VGroup(*[tiles[i] for i in hit_indices])
        self.play(
            *[t.animate.set_fill(ACCENT, opacity=0.85).set_stroke(ACCENT, width=2) for t in hits],
            run_time=1.1,
        )
        self.wait(0.6)

        found = Text(
            "1.47 million solar installations\nfound across the US",
            font_size=32,
            color=ACCENT,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.85)
        found.move_to(DOWN * 4.4)
        self.play(FadeIn(found))
        self.wait(1.6)

        self.play(FadeOut(tiles), FadeOut(found))

        punch = Text(
            "No agency had ever counted\nthem all. A neural net did.",
            font_size=32,
            color=SAND,
            line_spacing=1.2,
        ).scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(DOWN * 1.0)
        self.play(FadeIn(punch))
        self.wait(1.8)

        self.play(FadeOut(hook), FadeOut(punch))
        endcard(self)

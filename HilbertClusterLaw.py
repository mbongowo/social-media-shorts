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


class HilbertClusterLaw(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "A map database does not\ncare how big your search is",
            font_size=46,
            color=INK,
            line_spacing=1.2,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.to_edge(UP, buff=0.9)

        self.add(hook)
        self.wait(1)

        setup = Text(
            "Spatial indexes store map tiles\nalong one long curve, like\nthe Hilbert curve, not a grid.",
            font_size=28,
            color=INK,
            line_spacing=1.25,
        )
        setup.scale_to_fit_width(config.frame_width * 0.84)
        setup.move_to(UP * 1.2)

        self.play(FadeIn(setup))
        self.wait(1.8)
        self.play(FadeOut(setup))

        # Two query shapes of equal area: a compact blob (short edge) and a
        # long thin strip (long edge). Each is tiled into small squares that
        # stand for disk pages read off the curve; squares of the same color
        # that touch are one contiguous "cluster" (one disk read).
        def make_blob(n, color):
            group = VGroup()
            for i in range(n):
                for j in range(n):
                    sq = Square(side_length=0.34, color=color, fill_color=color, fill_opacity=0.75, stroke_width=1)
                    sq.move_to(RIGHT * i * 0.36 + UP * j * 0.36)
                    group.add(sq)
            group.move_to(ORIGIN)
            return group

        def make_strip(n, color):
            group = VGroup()
            for i in range(n):
                sq = Square(side_length=0.34, color=color, fill_color=color, fill_opacity=0.75, stroke_width=1)
                sq.move_to(RIGHT * i * 0.36)
                group.add(sq)
            group.move_to(ORIGIN)
            return group

        blob = make_blob(4, SKY)
        blob_label = Text("compact shape", font_size=22, color=SKY)
        blob_label.next_to(blob, UP, buff=0.25)
        blob_reads = Text("1 disk read", font_size=24, color=ACCENT)
        blob_reads.next_to(blob, DOWN, buff=0.3)
        blob_group = VGroup(blob_label, blob, blob_reads)
        blob_group.move_to(UP * 2.0)

        strip = make_strip(16, SAND)
        strip.scale_to_fit_width(config.frame_width * 0.8)
        strip_label = Text("same area, stretched thin", font_size=22, color=SAND)
        strip_label.next_to(strip, UP, buff=0.25)
        strip_reads = Text("up to 16 disk reads", font_size=24, color=WARN)
        strip_reads.next_to(strip, DOWN, buff=0.3)
        strip_group = VGroup(strip_label, strip, strip_reads)
        strip_group.move_to(DOWN * 0.6)

        self.play(FadeIn(blob_group))
        self.wait(1.3)
        self.play(FadeIn(strip_group))
        self.wait(2)

        number = Text("clusters track the edge,\nnot the area", font_size=40, color=WARN, line_spacing=1.2)
        number.scale_to_fit_width(config.frame_width * 0.82)
        number_sub = Text("same area, same curve, different cost", font_size=22, color=INK)
        number_sub.scale_to_fit_width(config.frame_width * 0.82)
        number_group = VGroup(number, number_sub).arrange(DOWN, buff=0.3)
        number_group.move_to(DOWN * 1.2)

        self.play(FadeOut(blob_group), FadeOut(strip_group))
        self.play(FadeIn(number_group))
        self.wait(2.2)

        fact = Text(
            "Moon, Jagadish, Faloutsos &\nSaltz proved it: on a Hilbert\ncurve, cluster count tracks a\nquery's surface area, not its\nhypervolume. IEEE TKDE, 2001.",
            font_size=22,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.86)
        fact.to_edge(DOWN, buff=1.4)

        self.play(FadeOut(number_group))
        self.add(fact)
        self.wait(3)

        punch = Text(
            "Shape your search like a\nblob, not a spider.",
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

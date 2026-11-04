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


class InSARSink(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Satellites caught a city\nsinking 30 cm a year",
            font_size=50,
            color=INK,
            line_spacing=1.2,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.to_edge(UP, buff=0.9)

        self.add(hook)
        self.wait(1)

        setup = Text(
            "No earthquake. Just two\nradar echoes from orbit,\ncompared years apart.",
            font_size=30,
            color=INK,
            line_spacing=1.25,
        )
        setup.scale_to_fit_width(config.frame_width * 0.82)
        setup.move_to(UP * 1.2)

        self.play(FadeIn(setup))
        self.wait(1.5)
        self.play(FadeOut(setup))

        # Diagram: a satellite sends a radar pulse to the same ground point
        # at two different times. The ground has dropped between passes, so
        # the echo travels a slightly longer path, measured as a phase shift.
        sat = Triangle(color=SKY, fill_color=SKY, fill_opacity=1).scale(0.22)
        sat.move_to(UP * 2.6)
        sat_label = Text("radar satellite", font_size=20, color=SKY)
        sat_label.scale_to_fit_width(2.6)
        sat_label.next_to(sat, UP, buff=0.15)

        ground_early = Line(LEFT * 2.0, RIGHT * 2.0, color=SAND, stroke_width=5)
        ground_early.move_to(DOWN * 0.3)
        label_early = Text("2007", font_size=22, color=SAND)
        label_early.next_to(ground_early, LEFT, buff=0.3)

        ground_late = Line(LEFT * 2.0, RIGHT * 2.0, color=WARN, stroke_width=5)
        ground_late.move_to(DOWN * 1.0)
        label_late = Text("2011", font_size=22, color=WARN)
        label_late.next_to(ground_late, LEFT, buff=0.3)

        path_early = DashedLine(sat.get_bottom(), ground_early.get_center(), color=SAND, stroke_width=3)
        path_late = DashedLine(sat.get_bottom(), ground_late.get_center(), color=WARN, stroke_width=3)

        drop_arrow = Arrow(ground_early.get_right() + RIGHT * 0.3, ground_late.get_right() + RIGHT * 0.3, color=INK, buff=0, stroke_width=3)

        diagram = VGroup(sat, sat_label, ground_early, label_early, ground_late, label_late, path_early, path_late, drop_arrow)
        diagram.move_to(UP * 0.5)

        self.play(FadeIn(diagram))
        self.wait(2)

        number = Text("> 30 cm/yr", font_size=68, color=WARN)
        number.scale_to_fit_width(config.frame_width * 0.65)
        number_sub = Text("sinking rate, parts of Mexico City", font_size=24, color=INK)
        number_sub.scale_to_fit_width(config.frame_width * 0.82)
        number_group = VGroup(number, number_sub).arrange(DOWN, buff=0.25)
        number_group.move_to(DOWN * 1.1)

        self.play(FadeOut(diagram))
        self.play(FadeIn(number_group))
        self.wait(2)

        fact = Text(
            "Chaussard, Wdowinski, Cabral-Cano\n& Amelung measured this with ALOS\nsatellite radar (InSAR), 2007 to 2011.",
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
            "The ground did not shake.\nIt was pumped dry.",
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

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


class WebMercatorGap(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "Google Maps has a\n21 km gap built in",
            font_size=52,
            color=INK,
            line_spacing=1.2,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.to_edge(UP, buff=0.9)

        self.add(hook)
        self.wait(1)

        setup = Text(
            "Your GPS gives an ellipsoid\nlatitude. The map plots it\nwith sphere math instead.",
            font_size=30,
            color=INK,
            line_spacing=1.25,
        )
        setup.scale_to_fit_width(config.frame_width * 0.82)
        setup.move_to(UP * 1.2)

        self.play(FadeIn(setup))
        self.wait(1.5)
        self.play(FadeOut(setup))

        # Diagram: sphere vs ellipsoid cross-section with a latitude line that
        # lands in two different places once each model's Mercator formula
        # projects it to a flat northing position.
        sphere = Circle(radius=1.6, color=SKY, stroke_width=4).move_to(UP * 0.6 + LEFT * 1.7)
        sphere_label = Text("Sphere model\n(what the map uses)", font_size=22, color=SKY, line_spacing=1.15)
        sphere_label.scale_to_fit_width(2.6)
        sphere_label.next_to(sphere, DOWN, buff=0.22)

        ellipse = Ellipse(width=3.0, height=3.36, color=SAND, stroke_width=4).move_to(UP * 0.6 + RIGHT * 1.7)
        ellipse_label = Text("WGS84 ellipsoid\n(what GPS uses)", font_size=22, color=SAND, line_spacing=1.15)
        ellipse_label.scale_to_fit_width(2.6)
        ellipse_label.next_to(ellipse, DOWN, buff=0.22)

        diagram = VGroup(sphere, sphere_label, ellipse, ellipse_label)
        diagram.move_to(UP * 0.9)

        self.play(FadeIn(diagram))
        self.wait(1.5)

        number = Text("~21 km", font_size=72, color=WARN)
        number.scale_to_fit_width(config.frame_width * 0.6)
        number_sub = Text("northing error near 45 deg latitude", font_size=24, color=INK)
        number_sub.scale_to_fit_width(config.frame_width * 0.82)
        number_group = VGroup(number, number_sub).arrange(DOWN, buff=0.25)
        number_group.move_to(DOWN * 1.1)

        self.play(FadeOut(diagram))
        self.play(FadeIn(number_group))
        self.wait(2)

        fact = Text(
            "Battersby, Finn, Usery & Yamamoto\nshowed Web Mercator mixes the two\nmodels, used by Google, Bing, OSM.",
            font_size=24,
            color=INK,
            line_spacing=1.25,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.to_edge(DOWN, buff=1.6)

        self.play(FadeOut(number_group))
        self.add(fact)
        self.wait(2.5)

        punch = Text(
            "Your GPS dot is fine.\nThe grid under it is not.",
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

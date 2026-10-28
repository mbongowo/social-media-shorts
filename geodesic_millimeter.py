from manim import *

config.frame_width = 8.0
config.frame_height = 14.22
config.background_color = "#0b1c17"

INK = '#eaf2ef'
ACCENT = '#39d98a'
WARN = '#ff6b6b'
SKY = '#4aa8ff'
SAND = '#e8c268'
BG = '#0b1c17'


def endcard(scene):
    if scene.mobjects:
        scene.play(FadeOut(*scene.mobjects))
    brand = Text("Maps, satellites & GeoAI", font_size=40, color=INK)
    brand.scale_to_fit_width(config.frame_width * 0.85)
    line = Line(LEFT * 1.6, RIGHT * 1.6, color=ACCENT, stroke_width=6)
    follow = Text("Follow for more", font_size=34, color=ACCENT)
    group = VGroup(brand, line, follow).arrange(DOWN, buff=0.45)
    scene.add(group)
    scene.wait(2)


class GeodesicMillimeter(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "A 1975 FORMULA STILL\nRUNS YOUR GPS DISTANCE",
            font_size=72, color=INK, weight=BOLD, line_spacing=1.2,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        setup = Text(
            "Earth is not a sphere.\nIt is a squashed ellipsoid.",
            font_size=36, color=INK, line_spacing=1.2,
        )
        setup.scale_to_fit_width(config.frame_width * 0.85)
        setup.move_to(UP * 2.3)
        self.play(FadeIn(setup))
        self.wait(1.5)

        ellipse = Ellipse(width=5.2, height=3.4, color=SAND, stroke_width=5)
        ellipse.move_to(ORIGIN + DOWN * 0.3)

        p1 = Dot(ellipse.point_at_angle(150 * DEGREES), color=SKY, radius=0.11)
        p2 = Dot(ellipse.point_at_angle(20 * DEGREES), color=ACCENT, radius=0.11)
        geodesic = ArcBetweenPoints(
            p1.get_center(), p2.get_center(), angle=-TAU / 10,
            color=WARN, stroke_width=5,
        )

        dist_label = Text("10 km to 18,000 km apart", font_size=28, color=INK)
        dist_label.scale_to_fit_width(config.frame_width * 0.8)
        dist_label.next_to(ellipse, DOWN, buff=0.4)

        diagram = VGroup(ellipse, p1, p2, geodesic, dist_label)
        self.play(FadeIn(diagram))
        self.wait(2)

        self.play(FadeOut(setup), FadeOut(diagram))

        badge_num = Text("0.115 mm", font_size=64, color=ACCENT, weight=BOLD)
        badge_sub = Text("agreement across 3,801 test lines", font_size=30, color=INK)
        badge_sub.scale_to_fit_width(config.frame_width * 0.85)
        badge = VGroup(badge_num, badge_sub).arrange(DOWN, buff=0.35)
        badge.move_to(ORIGIN + DOWN * 0.3)
        self.play(FadeIn(badge))
        self.wait(2)
        self.play(FadeOut(badge))

        fact = Text(
            "1975: Vincenty's geodesic formula.\n"
            "Checked in 2005 against an\n"
            "independent method: 0.115 mm off,\n"
            "over distances up to 18,000 km.",
            font_size=28, color=INK, line_spacing=1.25,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact))
        self.wait(2.5)

        punch = Text("Your map app still runs on this.", font_size=34, color=SAND, weight=BOLD)
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(DOWN * 4.4)
        self.play(FadeOut(fact), FadeIn(punch))
        self.wait(2)

        endcard(self)

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
    bg = Rectangle(width=config.frame_width, height=config.frame_height, color=BG, fill_color=BG, fill_opacity=1)
    title = Text('Maps, satellites & GeoAI', font_size=34, color=INK, weight=BOLD)
    title.scale_to_fit_width(config.frame_width * 0.85)
    line = Line(LEFT * 1.6, RIGHT * 1.6, color=ACCENT, stroke_width=5)
    line.next_to(title, DOWN, buff=0.35)
    follow = Text('Follow for more', font_size=30, color=ACCENT, weight=BOLD)
    follow.next_to(line, DOWN, buff=0.35)
    group = VGroup(title, line, follow)
    scene.add(bg)
    scene.play(FadeIn(group))
    scene.wait(1.5)


class DegreeVanishes(Scene):
    def construct(self):
        bg = Rectangle(width=config.frame_width, height=config.frame_height, color=BG, fill_color=BG, fill_opacity=1)
        self.add(bg)

        hook = VGroup(
            Text('A DEGREE OF LONGITUDE', font_size=50, color=INK, weight=BOLD),
            Text('DISAPPEARS AT THE POLES', font_size=50, color=ACCENT, weight=BOLD),
        ).arrange(DOWN, buff=0.18)
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)

        self.add(hook)
        self.wait(1)

        setup = Text('GPS lines of longitude run pole to pole', font_size=28, color=INK)
        setup.scale_to_fit_width(config.frame_width * 0.85)
        setup.move_to(UP * 3.2)
        self.play(FadeIn(setup))
        self.wait(1)

        eq_label = Text('AT THE EQUATOR', font_size=30, color=SAND, weight=BOLD)
        eq_label.move_to(UP * 1.9)
        eq_circle = Circle(radius=1.7, color=SKY, stroke_width=4).move_to(DOWN * 0.3)
        eq_spokes = VGroup(*[
            Line(eq_circle.get_center(), eq_circle.get_center() + 1.7 * np.array([np.cos(a), np.sin(a), 0]),
                 color=SKY, stroke_width=2)
            for a in np.linspace(0, 2 * PI, 13)[:-1]
        ])
        eq_wedge = Polygon(
            eq_circle.get_center(),
            eq_circle.get_center() + 1.7 * np.array([np.cos(PI / 2 - 0.26), np.sin(PI / 2 - 0.26), 0]),
            eq_circle.get_center() + 1.7 * np.array([np.cos(PI / 2 + 0.26), np.sin(PI / 2 + 0.26), 0]),
            color=ACCENT, fill_color=ACCENT, fill_opacity=0.75, stroke_width=0,
        )
        eq_km = Text('111.32 km', font_size=28, color=ACCENT, weight=BOLD)
        eq_km.next_to(eq_circle, DOWN, buff=0.3)

        self.play(FadeIn(eq_label), Create(eq_circle), Create(eq_spokes))
        self.play(FadeIn(eq_wedge), FadeIn(eq_km))
        self.wait(1.5)

        pole_label = Text('AT 89 DEGREES NORTH', font_size=30, color=WARN, weight=BOLD)
        pole_label.move_to(UP * 1.9)
        pole_circle = Circle(radius=0.25, color=SKY, stroke_width=4).move_to(DOWN * 0.3)
        pole_spokes = VGroup(*[
            Line(pole_circle.get_center(), pole_circle.get_center() + 0.25 * np.array([np.cos(a), np.sin(a), 0]),
                 color=SKY, stroke_width=2)
            for a in np.linspace(0, 2 * PI, 13)[:-1]
        ])
        pole_wedge = Polygon(
            pole_circle.get_center(),
            pole_circle.get_center() + 0.25 * np.array([np.cos(PI / 2 - 0.26), np.sin(PI / 2 - 0.26), 0]),
            pole_circle.get_center() + 0.25 * np.array([np.cos(PI / 2 + 0.26), np.sin(PI / 2 + 0.26), 0]),
            color=WARN, fill_color=WARN, fill_opacity=0.9, stroke_width=0,
        )
        pole_km = Text('under 2 km', font_size=28, color=WARN, weight=BOLD)
        pole_km.next_to(eq_circle, DOWN, buff=0.3)

        self.play(
            FadeOut(eq_label),
            Transform(eq_circle, pole_circle),
            Transform(eq_spokes, pole_spokes),
            Transform(eq_wedge, pole_wedge),
            Transform(eq_km, pole_km),
            FadeIn(pole_label),
            run_time=2,
        )
        self.wait(1.5)

        self.play(FadeOut(setup), FadeOut(pole_label), FadeOut(eq_label))

        fact = Text(
            'Longitude shrinks from 111.32 km at the\nequator to under 2 km at 89N (WGS84)',
            font_size=27, color=INK, line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact))
        self.wait(2)

        self.play(
            FadeOut(eq_circle), FadeOut(eq_spokes), FadeOut(eq_wedge), FadeOut(eq_km),
        )

        punch = Text('Same one degree. A different\ndistance every single time.', font_size=32,
                      color=ACCENT, weight=BOLD, line_spacing=1.2)
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(UP * 0.3)
        self.play(FadeIn(punch))
        self.wait(2)

        self.play(FadeOut(hook), FadeOut(fact), FadeOut(punch), FadeOut(bg))
        endcard(self)

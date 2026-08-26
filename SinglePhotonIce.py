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


class SinglePhotonIce(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'This satellite counts\nsingle photons from space',
            font_size=40,
            color=INK,
            line_spacing=1.15,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        sat_body = Rectangle(width=0.9, height=0.5, color=SKY, fill_color=SKY, fill_opacity=0.6)
        sat_panel_l = Rectangle(width=0.5, height=0.3, color=SAND, fill_color=SAND, fill_opacity=0.7).next_to(sat_body, LEFT, buff=0.05)
        sat_panel_r = Rectangle(width=0.5, height=0.3, color=SAND, fill_color=SAND, fill_opacity=0.7).next_to(sat_body, RIGHT, buff=0.05)
        satellite = VGroup(sat_body, sat_panel_l, sat_panel_r).move_to(UP * 3.6)
        self.play(FadeIn(satellite))

        ice = Line(LEFT * 2.6, RIGHT * 2.6, color=INK, stroke_width=6).move_to(DOWN * 1.6)
        ice_label = Text('ice sheet', font_size=22, color=INK).next_to(ice, DOWN, buff=0.2)
        self.play(Create(ice), FadeIn(ice_label))

        down_photons = VGroup(*[
            Dot(point=satellite.get_bottom() + DOWN * (0.3 + i * 0.05) + RIGHT * (i * 0.06 - 0.15), color=ACCENT, radius=0.05)
            for i in range(6)
        ])
        self.play(
            *[
                d.animate.move_to(ice.get_center() + RIGHT * (i * 0.3 - 0.75))
                for i, d in enumerate(down_photons)
            ],
            run_time=0.9,
        )
        self.wait(0.2)

        up_photons = VGroup(*[
            Dot(point=d.get_center(), color=SKY, radius=0.05) for d in down_photons
        ])
        self.add(up_photons)
        self.play(
            *[u.animate.move_to(satellite.get_bottom()) for u in up_photons],
            FadeOut(down_photons),
            run_time=0.9,
        )
        self.play(FadeOut(up_photons))

        rate = Text('10,000 pulses a second', font_size=26, color=ACCENT, weight=BOLD).move_to(UP * 0.7)
        self.play(FadeIn(rate, shift=UP * 0.1))
        self.wait(0.8)
        self.play(FadeOut(rate), FadeOut(satellite), FadeOut(ice), FadeOut(ice_label))

        fact = Text(
            "NASA's ICESat-2 tracks single\nreturning photons to measure\nGreenland and Antarctica\nlosing height, accurate to\nwithin 4mm a year",
            font_size=28,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        self.play(FadeOut(hook), FadeOut(fact))

        punch = Text(
            'One photon at a time.\nThat is how we know\nthe ice is shrinking',
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

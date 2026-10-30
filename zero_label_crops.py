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


class ZeroLabelCrops(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            "ZERO LABELS BEAT\n50,000 LABELS",
            font_size=72, color=INK, weight=BOLD, line_spacing=1.2,
        )
        hook.scale_to_fit_width(config.frame_width * 0.9)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        setup = Text(
            "An AI sorted farmland tiles\nusing only one rule: near or far?",
            font_size=34, color=INK, line_spacing=1.25,
        )
        setup.scale_to_fit_width(config.frame_width * 0.85)
        setup.move_to(UP * 2.2)
        self.play(FadeIn(setup))
        self.wait(1.5)

        grid = VGroup(*[
            Square(side_length=0.62, color=SAND, stroke_width=2, fill_color=SAND, fill_opacity=0.15)
            for _ in range(16)
        ]).arrange_in_grid(rows=4, cols=4, buff=0.08)
        grid.move_to(ORIGIN + DOWN * 0.1)
        self.play(FadeIn(grid))

        anchor = grid[5]
        near = grid[6]
        far = grid[15]
        self.play(
            anchor.animate.set_fill(ACCENT, opacity=0.9).set_stroke(ACCENT),
            near.animate.set_fill(SKY, opacity=0.9).set_stroke(SKY),
            far.animate.set_fill(WARN, opacity=0.9).set_stroke(WARN),
        )

        tag_anchor = Text("ANCHOR", font_size=18, color=ACCENT).next_to(grid, UP, buff=0.18)
        tag_near = Text("NEAR: pulled close", font_size=18, color=SKY)
        tag_near.scale_to_fit_width(config.frame_width * 0.55)
        tag_near.next_to(grid, DOWN, buff=0.35).shift(LEFT * 1.1)
        tag_far = Text("FAR: pushed apart", font_size=18, color=WARN)
        tag_far.scale_to_fit_width(config.frame_width * 0.55)
        tag_far.next_to(tag_near, DOWN, buff=0.2)
        self.play(FadeIn(tag_anchor), FadeIn(tag_near), FadeIn(tag_far))
        self.wait(2)

        self.play(FadeOut(setup), FadeOut(grid), FadeOut(tag_anchor), FadeOut(tag_near), FadeOut(tag_far))

        badge_num = Text("0 LABELS", font_size=58, color=ACCENT, weight=BOLD)
        badge_sub = Text("still beat AI trained on 50,000", font_size=28, color=INK)
        badge_sub.scale_to_fit_width(config.frame_width * 0.85)
        badge = VGroup(badge_num, badge_sub).arrange(DOWN, buff=0.35)
        badge.move_to(ORIGIN + DOWN * 0.3)
        self.play(FadeIn(badge))
        self.wait(2)
        self.play(FadeOut(badge))

        fact = Text(
            "A label-free AI beat supervised\n"
            "models trained on up to 50,000\n"
            "labeled tiles, on California\n"
            "cropland data.\n"
            "Jean et al., AAAI 2019.",
            font_size=27, color=INK, line_spacing=1.25,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact))
        self.wait(2.5)

        punch = Text(
            "Near things look alike.\nThat rule alone taught it geography.",
            font_size=30, color=SAND, weight=BOLD, line_spacing=1.2,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(DOWN * 4.4)
        self.play(FadeOut(fact), FadeIn(punch))
        self.wait(2)

        endcard(self)

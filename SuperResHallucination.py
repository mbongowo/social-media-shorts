from manim import *

config.frame_width = 8.0
config.frame_height = 14.22
config.pixel_width = 1080
config.pixel_height = 1920

INK = "#eaf2ef"
ACCENT = "#39d98a"
WARN = "#ff6b6b"
SKY = "#4aa8ff"
SAND = "#e8c268"
BG = "#0b1c17"

config.background_color = BG


def endcard(scene):
    line1 = Text("Maps, satellites & GeoAI", font_size=32, color=INK, weight=BOLD)
    line1.scale_to_fit_width(config.frame_width * 0.85)
    divider = Line(LEFT, RIGHT, color=ACCENT, stroke_width=4).set_width(3.2)
    line2 = Text("Follow for more", font_size=28, color=ACCENT, weight=BOLD)
    group = VGroup(line1, divider, line2).arrange(DOWN, buff=0.35).move_to(ORIGIN)
    scene.play(FadeIn(group, scale=1.05), run_time=0.7)
    scene.wait(1.2)
    scene.play(FadeOut(group), run_time=0.5)


class SuperResHallucination(Scene):
    def construct(self):
        self.camera.background_color = BG

        # 1. Hook (near top, constrained to frame width to avoid clipping)
        hook1 = Text("AI can sharpen a blurry", font_size=38, color=INK, weight=BOLD)
        hook2 = Text("satellite photo.", font_size=38, color=INK, weight=BOLD)
        hook3 = Text("It can also invent it.", font_size=38, color=WARN, weight=BOLD)
        for h in (hook1, hook2, hook3):
            h.scale_to_fit_width(min(h.width, config.frame_width * 0.88))
        hook = VGroup(hook1, hook2, hook3).arrange(DOWN, buff=0.22).move_to(UP * 4.8)
        self.play(Write(hook1), run_time=0.6)
        self.play(Write(hook2), run_time=0.6)
        self.play(Write(hook3), run_time=0.7)
        self.wait(0.6)
        self.play(FadeOut(hook), run_time=0.5)

        # 2. Visual: blurry low-res tile -> "sharpened" by AI
        label_lowres = Text("Real satellite pixels (low-res)", font_size=24, color=SAND)
        label_lowres.scale_to_fit_width(min(label_lowres.width, config.frame_width * 0.85))
        label_lowres.move_to(UP * 3.0)

        grid = VGroup(*[
            Square(side_length=0.62, stroke_color=BG, stroke_width=2, fill_color=SAND,
                   fill_opacity=0.35 + 0.5 * ((i + j) % 3) / 2)
            for i in range(5) for j in range(5)
        ]).arrange_in_grid(rows=5, cols=5, buff=0.03).move_to(UP * 1.1)

        self.play(FadeIn(label_lowres, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(grid, lag_ratio=0.02), run_time=1.0)
        self.wait(0.5)

        arrow = Text("AI super-resolution ->", font_size=26, color=SKY)
        arrow.scale_to_fit_width(min(arrow.width, config.frame_width * 0.85))
        arrow.move_to(DOWN * 0.7)
        self.play(FadeIn(arrow, shift=UP * 0.15), run_time=0.6)
        self.wait(0.4)

        # Sharpened output: same field but now with a fabricated building + road
        label_sharp = Text("AI's 'sharpened' output", font_size=24, color=SKY)
        label_sharp.scale_to_fit_width(min(label_sharp.width, config.frame_width * 0.85))
        label_sharp.move_to(DOWN * 1.7)

        sharp_grid = VGroup(*[
            Square(side_length=0.62, stroke_color=BG, stroke_width=1, fill_color=SAND,
                   fill_opacity=0.35 + 0.5 * ((i + j) % 3) / 2)
            for i in range(5) for j in range(5)
        ]).arrange_in_grid(rows=5, cols=5, buff=0.03).move_to(DOWN * 3.9)

        fake_building = Square(side_length=0.9, fill_color=WARN, fill_opacity=0.9,
                                stroke_color=INK, stroke_width=2)
        fake_building.move_to(sharp_grid.get_center() + UP * 0.2 + RIGHT * 0.1)
        fake_tag = Text("not really there", font_size=18, color=WARN)
        fake_tag.scale_to_fit_width(min(fake_tag.width, config.frame_width * 0.8))
        fake_tag.next_to(fake_building, DOWN, buff=0.2)

        self.play(FadeOut(grid), FadeOut(label_lowres), run_time=0.4)
        self.play(FadeIn(label_sharp, shift=UP * 0.2), run_time=0.5)
        self.play(FadeIn(sharp_grid, lag_ratio=0.02), run_time=0.8)
        self.play(GrowFromCenter(fake_building), run_time=0.6)
        self.play(FadeIn(fake_tag), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(VGroup(arrow, label_sharp, sharp_grid, fake_building, fake_tag)),
            run_time=0.5,
        )

        # 3. Fact (near bottom)
        fact = Text(
            "Super-resolution models pattern-\ncomplete missing detail. Trained\non photos, they can hallucinate\nroads or buildings that were\nnever in the real scene.",
            font_size=26, color=INK, line_spacing=1.25,
        )
        fact.scale_to_fit_width(min(fact.width, config.frame_width * 0.88))
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2), run_time=0.8)
        self.wait(1.6)
        self.play(FadeOut(fact), run_time=0.5)

        # 4. Punch line
        punch = Text("Sharper isn't the same as true.", font_size=34, color=ACCENT, weight=BOLD)
        punch.scale_to_fit_width(min(punch.width, config.frame_width * 0.88))
        punch.move_to(ORIGIN)
        self.play(Write(punch), run_time=1.0)
        self.wait(1.3)
        self.play(FadeOut(punch), run_time=0.5)

        # 5. End card
        endcard(self)

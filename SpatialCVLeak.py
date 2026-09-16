from manim import *
import random

config.frame_width = 8.0
config.frame_height = 14.22

INK = '#eaf2ef'
ACCENT = '#39d98a'
WARN = '#ff6b6b'
SKY = '#4aa8ff'
SAND = '#e8c268'
BG = '#0b1c17'


def endcard(scene):
    scene.clear()
    brand = Text('Maps, satellites & GeoAI', color=INK, font_size=40)
    brand.scale_to_fit_width(config.frame_width * 0.85)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=6)
    line.next_to(brand, DOWN, buff=0.4)
    follow = Text('Follow for more', color=ACCENT, font_size=34)
    follow.next_to(line, DOWN, buff=0.4)
    group = VGroup(brand, line, follow).move_to(ORIGIN)
    scene.add(group)
    scene.wait(2)


class SpatialCVLeak(Scene):
    def construct(self):
        self.camera.background_color = BG
        random.seed(7)

        hook = Text(
            "That '99% accurate' map model\nmight be grading its own answers",
            color=INK,
            font_size=40,
            line_spacing=1.1,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 4.8)
        self.add(hook)
        self.wait(1)

        n = 7
        dots = VGroup()
        for row in range(n):
            for col in range(n):
                d = Dot(radius=0.14, color=SAND, fill_opacity=1)
                d.move_to(RIGHT * (col - (n - 1) / 2) * 0.62 + UP * (row - (n - 1) / 2) * 0.62)
                dots.add(d)
        dots.move_to(UP * 1.2)
        self.play(FadeIn(dots), run_time=0.7)
        self.wait(0.3)

        label_random = Text('Random split', color=INK, font_size=26).next_to(dots, UP, buff=0.3)
        self.play(FadeIn(label_random), run_time=0.4)

        idxs = list(range(n * n))
        random.shuffle(idxs)
        test_idxs = set(idxs[: (n * n) // 3])
        anims = []
        for i, d in enumerate(dots):
            color = SKY if i in test_idxs else ACCENT
            anims.append(d.animate.set_color(color))
        self.play(*anims, run_time=0.8)
        self.wait(0.4)

        leak_note = Text(
            'Next-door pixels look almost\nidentical, so train and test mix',
            color=WARN,
            font_size=24,
            line_spacing=1.1,
        )
        leak_note.scale_to_fit_width(config.frame_width * 0.85)
        leak_note.next_to(dots, DOWN, buff=0.45)
        self.play(FadeIn(leak_note), run_time=0.5)
        self.wait(1.1)

        self.play(FadeOut(label_random), FadeOut(leak_note), run_time=0.4)

        label_block = Text('Spatial block split', color=INK, font_size=26).next_to(dots, UP, buff=0.3)
        self.play(FadeIn(label_block), run_time=0.4)

        block_anims = []
        for i, d in enumerate(dots):
            row = i // n
            col = i % n
            color = SKY if col >= n - 2 else ACCENT
            block_anims.append(d.animate.set_color(color))
        self.play(*block_anims, run_time=0.8)
        self.wait(0.3)

        held_out = VGroup(*[dots[i] for i in range(n * n) if i % n >= n - 2])
        block_box = SurroundingRectangle(held_out, color=WARN, buff=0.18, stroke_width=4)
        self.play(Create(block_box), run_time=0.6)
        self.wait(0.8)

        self.play(FadeOut(label_block), FadeOut(block_box), run_time=0.4)

        fact = Text(
            "A rooftop-detection study found random splits\ninflated accuracy by up to 17 points,\nmisreporting over 99% where it was not earned",
            color=INK,
            font_size=26,
            line_spacing=1.15,
        )
        fact.scale_to_fit_width(config.frame_width * 0.88)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact), run_time=0.6)
        self.wait(1.6)

        punch = Text(
            "Test your model on ground\nit has never quietly seen",
            color=WARN,
            font_size=32,
            line_spacing=1.1,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        punch.move_to(ORIGIN)
        self.play(FadeOut(dots), FadeOut(fact), run_time=0.4)
        self.play(FadeIn(punch), run_time=0.6)
        self.wait(1.3)

        self.play(FadeOut(hook), FadeOut(punch), run_time=0.4)
        endcard(self)

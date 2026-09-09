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


class RandomFeaturesWin(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text(
            'This satellite AI\nnever trained its own eyes',
            font_size=38,
            color=INK,
            line_spacing=1.2,
            weight=BOLD,
        )
        hook.scale_to_fit_width(config.frame_width * 0.88)
        hook.move_to(UP * 5.7)
        self.add(hook)
        self.wait(1)

        cnn_box = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.15, color=SKY, stroke_width=3)
        cnn_label = Text('CNN', font_size=26, color=SKY)
        cnn_sub = Text('7.9 hrs / task\non a V100 GPU', font_size=18, color=INK, line_spacing=1.2)
        cnn_group = VGroup(cnn_box, cnn_label).move_to(UP * 3.0 + LEFT * 1.8)
        cnn_label.move_to(cnn_box.get_center())
        cnn_sub.next_to(cnn_box, DOWN, buff=0.2)

        mosaiks_box = RoundedRectangle(width=2.6, height=1.6, corner_radius=0.15, color=ACCENT, stroke_width=3)
        mosaiks_label = Text('random\nfilters', font_size=24, color=ACCENT, line_spacing=1.1)
        mosaiks_sub = Text('minutes\non a laptop', font_size=18, color=INK, line_spacing=1.2)
        mosaiks_group = VGroup(mosaiks_box, mosaiks_label).move_to(UP * 3.0 + RIGHT * 1.8)
        mosaiks_label.move_to(mosaiks_box.get_center())
        mosaiks_sub.next_to(mosaiks_box, DOWN, buff=0.2)

        self.play(
            Create(cnn_box), FadeIn(cnn_label), FadeIn(cnn_sub),
            Create(mosaiks_box), FadeIn(mosaiks_label), FadeIn(mosaiks_sub),
            run_time=1.0,
        )
        self.wait(0.6)

        vs = Text('same accuracy', font_size=22, color=SAND).move_to(UP * 1.0)
        arrow_l = Arrow(cnn_box.get_bottom() + DOWN * 0.5, vs.get_left() + LEFT * 0.2, color=SAND, stroke_width=2, buff=0.1)
        arrow_r = Arrow(mosaiks_box.get_bottom() + DOWN * 0.5, vs.get_right() + RIGHT * 0.2, color=SAND, stroke_width=2, buff=0.1)
        self.play(FadeIn(vs, shift=UP * 0.1))
        self.wait(1.0)

        speed_label = Text('up to 10,000x faster to train', font_size=26, color=ACCENT, weight=BOLD)
        speed_label.scale_to_fit_width(config.frame_width * 0.8)
        speed_label.move_to(DOWN * 1.0)
        self.play(FadeIn(speed_label, shift=UP * 0.2))
        self.wait(1.4)

        self.play(
            FadeOut(cnn_box), FadeOut(cnn_label), FadeOut(cnn_sub),
            FadeOut(mosaiks_box), FadeOut(mosaiks_label), FadeOut(mosaiks_sub),
            FadeOut(vs), FadeOut(speed_label),
        )

        fact = Text(
            'MOSAIKS: fixed, never-optimized\nrandom filters matched a trained\nCNN on all 7 mapping tasks',
            font_size=26,
            color=INK,
            line_spacing=1.2,
        )
        fact.scale_to_fit_width(config.frame_width * 0.85)
        fact.move_to(DOWN * 4.4)
        self.play(FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        self.play(FadeOut(hook), FadeOut(fact))

        punch = Text(
            'The features were never learned.\nOnly the last, tiny step was.',
            font_size=32,
            color=ACCENT,
            line_spacing=1.2,
            weight=BOLD,
        )
        punch.scale_to_fit_width(config.frame_width * 0.85)
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.wait(1.5)
        self.play(FadeOut(punch))

        endcard(self)

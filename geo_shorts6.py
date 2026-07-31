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
    title = Text('Maps, satellites & GeoAI', font_size=30, color=INK)
    line = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
    follow = Text('Follow for more', font_size=26, color=ACCENT)
    group = VGroup(title, line, follow).arrange(DOWN, buff=0.35)
    scene.play(FadeIn(group, shift=UP * 0.3))
    scene.wait(1.0)
    scene.play(FadeOut(group))


class RadarBackscatter(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text('This satellite image\nisn\'t a photo', font_size=34,
                     color=INK, line_spacing=1.1).move_to(UP * 4.8)
        self.play(FadeIn(hook, shift=DOWN * 0.3))
        self.wait(0.5)

        sat = Triangle(color=SKY, fill_opacity=1).scale(0.35).move_to(UP * 2.6)
        rough = Square(side_length=1.6, color=SAND, fill_opacity=1).move_to(LEFT * 1.6 + DOWN * 0.5)
        smooth = Rectangle(width=1.6, height=1.6, color=SKY, fill_opacity=1).move_to(RIGHT * 1.6 + DOWN * 0.5)

        speckles = VGroup(*[
            Dot(point=rough.get_center() + np.array([np.random.uniform(-0.7, 0.7), np.random.uniform(-0.7, 0.7), 0]),
                radius=0.05, color=INK)
            for _ in range(18)
        ])

        self.play(FadeIn(sat), FadeIn(rough), FadeIn(smooth))
        self.wait(0.3)

        wave_rough = Arrow(sat.get_center(), rough.get_center(), color=ACCENT, buff=0.4)
        wave_smooth = Arrow(sat.get_center(), smooth.get_center(), color=WARN, buff=0.4)
        self.play(GrowArrow(wave_rough), GrowArrow(wave_smooth))
        self.wait(0.3)

        echo_rough = Arrow(rough.get_center(), sat.get_center(), color=ACCENT, buff=0.4)
        echo_away = Arrow(smooth.get_center(), smooth.get_center() + RIGHT * 1.5 + UP * 0.8, color=WARN, buff=0.1)
        self.play(GrowArrow(echo_rough), GrowArrow(echo_away), FadeIn(speckles))
        self.wait(0.5)

        label_rough = Text('rough = bright', font_size=22, color=ACCENT).next_to(rough, DOWN, buff=0.3)
        label_smooth = Text('smooth = dark', font_size=22, color=WARN).next_to(smooth, DOWN, buff=0.3)
        self.play(FadeIn(label_rough), FadeIn(label_smooth))
        self.wait(0.8)

        fact = Text(
            'Radar sends its own microwave pulses\nand measures the echo. Choppy water\nand crop fields scatter it back bright;\ncalm water and runways bounce it away.',
            font_size=24, color=INK, line_spacing=1.2
        ).move_to(DOWN * 4.4)
        self.play(FadeOut(hook), FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        punch = Text('It measures roughness, not color.', font_size=28, color=ACCENT).move_to(DOWN * 6.0)
        self.play(Write(punch))
        self.wait(1.0)

        self.play(FadeOut(VGroup(sat, rough, smooth, speckles, wave_rough, wave_smooth,
                                  echo_rough, echo_away, label_rough, label_smooth, fact, punch)))
        endcard(self)


class SpectralFingerprint(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text('Every material has a\nbarcode from orbit', font_size=32,
                     color=INK, line_spacing=1.1).move_to(UP * 4.8)
        self.play(FadeIn(hook, shift=DOWN * 0.3))
        self.wait(0.5)

        axes = Axes(
            x_range=[0, 4, 1], y_range=[0, 1, 0.5],
            x_length=5.5, y_length=3.5,
            axis_config={'color': INK, 'stroke_width': 2},
            tips=False,
        ).move_to(UP * 1.0)
        x_label = Text('wavelength ->', font_size=18, color=INK).next_to(axes, DOWN, buff=0.2)
        self.play(Create(axes), FadeIn(x_label))

        leaf = axes.plot(lambda x: 0.15 + 0.1 * np.sin(x) + 0.5 * np.exp(-((x - 3.2) ** 2) / 0.2),
                          color=ACCENT, x_range=[0, 4])
        water = axes.plot(lambda x: 0.6 * np.exp(-x * 1.3), color=SKY, x_range=[0, 4])
        soil = axes.plot(lambda x: 0.2 + 0.12 * x, color=SAND, x_range=[0, 4])

        leaf_lbl = Text('vegetation', font_size=18, color=ACCENT).next_to(axes, UP, buff=0.15).shift(LEFT * 1.6)
        water_lbl = Text('water', font_size=18, color=SKY).next_to(leaf_lbl, RIGHT, buff=0.5)
        soil_lbl = Text('soil', font_size=18, color=SAND).next_to(water_lbl, RIGHT, buff=0.5)

        self.play(Create(leaf), FadeIn(leaf_lbl))
        self.play(Create(water), FadeIn(water_lbl))
        self.play(Create(soil), FadeIn(soil_lbl))
        self.wait(0.8)

        fact = Text(
            'Healthy leaves, dry soil, and water each\nreflect light in a distinct pattern across\ninvisible infrared bands. Scientists match\nthese curves to identify materials from space.',
            font_size=23, color=INK, line_spacing=1.2
        ).move_to(DOWN * 4.6)
        self.play(FadeOut(hook), FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        punch = Text('You don\'t need to touch it to know it.', font_size=26, color=ACCENT).move_to(DOWN * 6.2)
        self.play(Write(punch))
        self.wait(1.0)

        self.play(FadeOut(VGroup(axes, x_label, leaf, water, soil, leaf_lbl, water_lbl, soil_lbl, fact, punch)))
        endcard(self)


class ContourSlope(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text('These squiggly lines are\na 3D map on paper', font_size=32,
                     color=INK, line_spacing=1.1).move_to(UP * 4.8)
        self.play(FadeIn(hook, shift=DOWN * 0.3))
        self.wait(0.5)

        steep_lines = VGroup(*[
            Ellipse(width=2.4 - i * 0.3, height=1.6 - i * 0.2, color=ACCENT, stroke_width=3)
            for i in range(4)
        ]).move_to(LEFT * 1.7 + UP * 1.2)

        gentle_lines = VGroup(*[
            Ellipse(width=2.6 - i * 0.5, height=1.8 - i * 0.35, color=SAND, stroke_width=3)
            for i in range(4)
        ]).move_to(RIGHT * 1.7 + UP * 1.2)

        self.play(Create(steep_lines))
        self.wait(0.3)
        self.play(Create(gentle_lines))
        self.wait(0.3)

        steep_lbl = Text('steep', font_size=22, color=ACCENT).next_to(steep_lines, DOWN, buff=0.4)
        gentle_lbl = Text('gentle', font_size=22, color=SAND).next_to(gentle_lines, DOWN, buff=0.4)
        self.play(FadeIn(steep_lbl), FadeIn(gentle_lbl))
        self.wait(0.8)

        fact = Text(
            'Each contour line connects points of equal\nelevation. The closer the lines, the steeper\nthe slope, at a fixed interval you can read\na mountain\'s shape without a single number.',
            font_size=23, color=INK, line_spacing=1.2
        ).move_to(DOWN * 4.6)
        self.play(FadeOut(hook), FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        punch = Text('Read the spacing, read the slope.', font_size=27, color=ACCENT).move_to(DOWN * 6.2)
        self.play(Write(punch))
        self.wait(1.0)

        self.play(FadeOut(VGroup(steep_lines, gentle_lines, steep_lbl, gentle_lbl, fact, punch)))
        endcard(self)


class FoundationModel(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text('This AI never saw a\nsingle labeled image', font_size=32,
                     color=INK, line_spacing=1.1).move_to(UP * 4.8)
        self.play(FadeIn(hook, shift=DOWN * 0.3))
        self.wait(0.5)

        cloud = VGroup(*[
            Square(side_length=0.35, color=SKY, fill_opacity=0.7).move_to(
                UP * 2.0 + np.array([np.random.uniform(-2.2, 2.2), np.random.uniform(-0.6, 0.6), 0]))
            for _ in range(24)
        ])
        cloud_lbl = Text('millions of unlabeled scenes', font_size=18, color=SKY).next_to(cloud, UP, buff=0.2)
        self.play(FadeIn(cloud), FadeIn(cloud_lbl))
        self.wait(0.5)

        funnel = Triangle(color=INK).scale(0.6).rotate(PI).move_to(DOWN * 0.3)
        self.play(Create(funnel))

        small_set = VGroup(*[
            Square(side_length=0.35, color=ACCENT, fill_opacity=1).move_to(
                DOWN * 2.0 + np.array([i * 0.5 - 0.75, 0, 0]))
            for i in range(4)
        ])
        small_lbl = Text('a handful of labeled examples', font_size=18, color=ACCENT).next_to(small_set, DOWN, buff=0.2)
        self.play(FadeIn(small_set), FadeIn(small_lbl))
        self.wait(0.8)

        fact = Text(
            'Geospatial foundation models pretrain on\nvast unlabeled satellite archives using\nself-supervised learning, then fine-tune\nwith just a few examples for a new task.',
            font_size=23, color=INK, line_spacing=1.2
        ).move_to(DOWN * 4.8)
        self.play(FadeOut(hook), FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        punch = Text('Pretrain once. Fine-tune fast on anything.', font_size=25, color=ACCENT).move_to(DOWN * 6.3)
        self.play(Write(punch))
        self.wait(1.0)

        self.play(FadeOut(VGroup(cloud, cloud_lbl, funnel, small_set, small_lbl, fact, punch)))
        endcard(self)


class MAUP(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text('Same data, same map,\nopposite conclusion', font_size=32,
                     color=INK, line_spacing=1.1).move_to(UP * 4.8)
        self.play(FadeIn(hook, shift=DOWN * 0.3))
        self.wait(0.5)

        np.random.seed(3)
        dots = VGroup(*[
            Dot(point=UP * 1.4 + np.array([np.random.uniform(-2.2, 2.2), np.random.uniform(-1.6, 1.6), 0]),
                radius=0.06, color=INK)
            for _ in range(40)
        ])
        self.play(FadeIn(dots))
        self.wait(0.3)

        grid1 = VGroup(*[
            Square(side_length=1.5).move_to(UP * 1.4 + np.array([x, y, 0]))
            for x in (-1.5, 0.0, 1.5) for y in (-1.5, 0.0, 1.5)
        ]).set_stroke(color=ACCENT, width=3)
        self.play(Create(grid1))
        left_shade = Square(side_length=1.5, fill_color=ACCENT, fill_opacity=0.5, stroke_width=0).move_to(UP * 1.4 + LEFT * 1.5)
        self.play(FadeIn(left_shade))
        lbl1 = Text('grid A: west "highest"', font_size=18, color=ACCENT).move_to(UP * 3.2)
        self.play(FadeIn(lbl1))
        self.wait(0.7)
        self.play(FadeOut(grid1), FadeOut(left_shade), FadeOut(lbl1))

        grid2 = VGroup(*[
            Rectangle(width=4.5, height=1.0).move_to(UP * 1.4 + np.array([0, y, 0]))
            for y in (-1.0, 0.0, 1.0)
        ]).set_stroke(color=SAND, width=3)
        self.play(Create(grid2))
        top_shade = Rectangle(width=4.5, height=1.0, fill_color=SAND, fill_opacity=0.5, stroke_width=0).move_to(UP * 1.4 + UP * 1.0)
        self.play(FadeIn(top_shade))
        lbl2 = Text('grid B: north "highest"', font_size=18, color=SAND).move_to(UP * 3.2)
        self.play(FadeIn(lbl2))
        self.wait(0.8)

        fact = Text(
            'The Modifiable Areal Unit Problem: the\nsame points, aggregated into different\nboundary shapes or sizes, can flip which\nregion looks highest, lowest, or riskiest.',
            font_size=23, color=INK, line_spacing=1.2
        ).move_to(DOWN * 4.6)
        self.play(FadeOut(hook), FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        punch = Text('The boundaries you pick can pick the answer.', font_size=23, color=ACCENT).move_to(DOWN * 6.2)
        self.play(Write(punch))
        self.wait(1.0)

        self.play(FadeOut(VGroup(dots, grid2, top_shade, lbl2, fact, punch)))
        endcard(self)


class SpatialAutocorrelation(Scene):
    def construct(self):
        self.camera.background_color = BG

        hook = Text('The first law of geography\nfits in one sentence', font_size=30,
                     color=INK, line_spacing=1.1).move_to(UP * 4.8)
        self.play(FadeIn(hook, shift=DOWN * 0.3))
        self.wait(0.5)

        np.random.seed(7)
        clustered = VGroup()
        for cx, cy, col in [(-1.6, 1.0, ACCENT), (1.6, 1.0, SKY), (0, -1.2, SAND)]:
            for _ in range(9):
                clustered.add(Dot(point=np.array([cx + np.random.uniform(-0.6, 0.6),
                                                    cy + np.random.uniform(-0.6, 0.6), 0]),
                                   radius=0.07, color=col))
        clustered.move_to(UP * 1.6)
        clustered_lbl = Text('near things: similar', font_size=20, color=INK).next_to(clustered, DOWN, buff=0.3)
        self.play(FadeIn(clustered), FadeIn(clustered_lbl))
        self.wait(1.0)

        quote = Text(
            '"Everything is related to everything\nelse, but near things are more\nrelated than distant things."',
            font_size=22, color=INK, line_spacing=1.2, slant=ITALIC
        ).move_to(DOWN * 1.6)
        self.play(FadeIn(quote, shift=UP * 0.2))
        self.wait(1.2)
        self.play(FadeOut(clustered), FadeOut(clustered_lbl), FadeOut(quote))

        fact = Text(
            'Tobler\'s First Law. Statisticians measure\nthis clustering with Moran\'s I, and ignoring\nit is a common way machine learning models\nquietly cheat by memorizing geography.',
            font_size=22, color=INK, line_spacing=1.2
        ).move_to(DOWN * 4.6)
        self.play(FadeOut(hook), FadeIn(fact, shift=UP * 0.2))
        self.wait(1.8)

        punch = Text('Your model just memorized geography.', font_size=26, color=WARN).move_to(DOWN * 6.2)
        self.play(Write(punch))
        self.wait(1.0)

        self.play(FadeOut(VGroup(fact, punch)))
        endcard(self)

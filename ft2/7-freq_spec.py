from manim import *


class SpecTrum(Scene):
    def construct(self):
        eq1 = MathTex(
            r"x(t)",  # 0
            r"=",  # 1
            r"\sum^{\infty}_{n=1}",
            r"\frac{ 4 }{ (2n-1) \pi}",  # 11
            r"\; sin(",  # 12
            r"(2n-1) \pi t",  # 13
            r")",  # 14
            font_size=30,
        ).to_edge(UP, buff=1)
        sin_wave_formulas = VGroup()
        sin_wave_1 = MathTex(r"\frac{4}{\pi} \sin(\pi t)", font_size=30, color=GOLD_A)
        sin_wave_2 = MathTex(r"\frac{4}{3 \pi} \sin(3\pi t)", font_size=30, color=PINK)
        sin_wave_3 = MathTex(r"\frac{4}{5 \pi} \sin(5\pi t)", font_size=30, color=GREEN)
        sin_wave_4 = MathTex(
            r"\frac{4}{7 \pi} \sin(7\pi t)", font_size=30, color=ORANGE
        )

        sin_wave_formulas.add(sin_wave_1, sin_wave_2, sin_wave_3, sin_wave_4).arrange(
            DOWN, buff=0.5
        )
        sin_wave_formulas.to_edge(LEFT, buff=1)

        axes = Axes(
            x_range=[0, 8 * PI, PI],
            y_range=[0, 5.5, 1],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"color": BLUE, "stroke_width": 4, "tick_size": 0.05},
        ).shift(RIGHT)
        x_axis_label = axes.get_x_axis_label(
            MathTex("\\omega", color=WHITE, font_size=33),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )

        y_axis_label = axes.get_y_axis_label(
            Tex("x(t)", color=RED_A, font_size=33), edge=UP, direction=UP, buff=0.15
        )
        x_labels = VGroup()
        pi_values = [
            0,
            PI,
            2 * PI,
            3 * PI,
            4 * PI,
            5 * PI,
            6 * PI,
            7 * PI,
            8 * PI,
        ]
        pi_labels = [
            "0",
            "\\pi",
            "2 \\pi",
            "3 \\pi",
            "4\\pi",
            "5\\pi",
            "6\\pi",
            "7\\pi",
            "8\\pi",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 8 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.3)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.3)
                    )

            x_labels.add(x_label)

        y_labelss = VGroup()
        y_values = [
            1,
            2,
            3,
            4,
            5,
        ]
        y_labels = [
            "\\frac{4}{9  \\pi}",
            "\\frac{4}{7 \\pi}",
            "\\frac{4}{5 \\pi}",
            "\\frac{4}{3 \\pi}",
            "\\frac{4}{  \\pi}",
        ]
        i = 0
        for y_val, label in zip(y_values, y_labels):
            if y_val <= 5:

                y_label = MathTex(label, font_size=24, color=WHITE).move_to(
                    axes.c2p(-0.8, y_val)
                )

            y_labelss.add(y_label)

        axes_graph = VGroup(axes, x_labels, y_labelss, x_axis_label, y_axis_label)
        axes_graph.shift(DOWN * 0.5)
        line1 = Line(
            start=axes.c2p(PI, 0), end=axes.c2p(PI, 4 + 1), color=GOLD_A, stroke_width=3
        )
        dot1 = Dot(point=axes.c2p(PI, 4 + 1), color=GOLD_A, radius=0.07)
        d_line1 = DashedLine(
            start=axes.c2p(0, 4 + 1),
            end=axes.c2p(PI, 4 + 1),
            color=GOLD_A,
            stroke_width=3,
        )
        line_dot_1 = VGroup(line1, dot1, d_line1)

        line2 = Line(
            start=axes.c2p(3 * PI, 0),
            end=axes.c2p(3 * PI, 3 + 1),
            color=PINK,
            stroke_width=3,
        )
        dot2 = Dot(point=axes.c2p(3 * PI, 3 + 1), color=PINK, radius=0.07)
        d_line2 = DashedLine(
            start=axes.c2p(0, 4),
            end=axes.c2p(3 * PI, 3 + 1),
            color=PINK,
            stroke_width=3,
        )
        line_dot_2 = VGroup(line2, dot2, d_line2)

        line3 = Line(
            start=axes.c2p(5 * PI, 0),
            end=axes.c2p(5 * PI, 2 + 1),
            color=GREEN,
            stroke_width=3,
        )
        dot3 = Dot(point=axes.c2p(5 * PI, 2 + 1), color=GREEN, radius=0.07)
        d_line3 = DashedLine(
            start=axes.c2p(0, 3),
            end=axes.c2p(5 * PI, 2 + 1),
            color=GREEN,
            stroke_width=3,
        )
        line_dot_3 = VGroup(line3, dot3, d_line3)

        line4 = Line(
            start=axes.c2p(7 * PI, 0),
            end=axes.c2p(7 * PI, 1 + 1),
            color=ORANGE,
            stroke_width=3,
        )
        dot4 = Dot(point=axes.c2p(7 * PI, 1 + 1), color=ORANGE, radius=0.07)
        d_line4 = DashedLine(
            start=axes.c2p(0, 2),
            end=axes.c2p(7 * PI, 1 + 1),
            color=ORANGE,
            stroke_width=3,
        )
        line_dot_4 = VGroup(line4, dot4, d_line4)
        lines_fre = VGroup(line_dot_1, line_dot_2, line_dot_3, line_dot_4)

        x_axis_label2 = axes.get_x_axis_label(
            MathTex(
                "2 \\pi f", color=WHITE, font_size=33
            ),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )
        x_axis_label3 = axes.get_x_axis_label(
            MathTex("f", color=WHITE, font_size=33),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )

        x_labels1 = VGroup()
        pi_values = [
            0,
            PI,
            2 * PI,
            3 * PI,
            4 * PI,
            5 * PI,
            6 * PI,
            7 * PI,
            8 * PI,
        ]
        pi_labels = [
            "0",
            "\\frac{\\pi}{2\\pi}",
            "\\frac{2 \\pi}{2\\pi}",
            "\\frac{3 \\pi}{2\\pi}",
            "\\frac{4\\pi}{2\\pi}",
            "\\frac{5\\pi}{2\\pi}",
            "\\frac{6\\pi}{2\\pi}",
            "\\frac{7\\pi}{2\\pi}",
            "\\frac{8\\pi}{2\\pi}",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 8 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.3)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.5)
                    )

            x_labels1.add(x_label)

        x_labels3 = VGroup()
        pi_values = [
            0,
            PI,
            2 * PI,
            3 * PI,
            4 * PI,
            5 * PI,
            6 * PI,
            7 * PI,
            8 * PI,
        ]
        pi_labels = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 8 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.3)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.3)
                    )

            x_labels3.add(x_label)

        x_axis_label_temp_first = axes.get_x_axis_label(
            MathTex("\\omega", color=WHITE, font_size=33),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )
        x_axis_label4 = axes.get_x_axis_label(
            MathTex("n", color=WHITE, font_size=33),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )
        self.play(Write(eq1))
        self.wait()
        self.play(
            LaggedStart(*[Write(s_w) for s_w in sin_wave_formulas], LaggedStart=0.2),
            run_time=2,
        )
        self.wait()
        self.play(Create(axes_graph), run_time=3)

        self.wait()
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(s_w, lin)
                    for s_w, lin in zip(sin_wave_formulas, lines_fre)
                ],
                lag_ratio=1,
            ),
            run_time=4,
        )
        self.wait()
        rec = SurroundingRectangle(x_axis_label, color=ORANGE, buff=0.1, stroke_width=3)
        self.play(Create(rec))
        self.wait()
        self.play(ReplacementTransform(x_axis_label, x_axis_label2), FadeOut(rec))
        self.wait()
        self.play(TransformMatchingShapes(x_labels, x_labels1))
        self.wait()
        self.play(TransformMatchingTex(x_axis_label2, x_axis_label3))
        self.wait()
        self.play(TransformMatchingShapes(x_labels1, x_labels))
        self.wait()
        self.play(TransformMatchingTex(x_axis_label3, x_axis_label2))
        self.wait()
        self.play(ReplacementTransform(x_axis_label2, x_axis_label_temp_first))
        self.wait()
        self.play(TransformMatchingShapes(x_labels, x_labels3))
        self.wait()
        self.play(TransformMatchingTex(x_axis_label_temp_first, x_axis_label4))
        self.wait()

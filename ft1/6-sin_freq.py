from manim import *
import numpy as np


def fx_sin(A, w, t):
    return A * np.sin(w * t)


def main_eq(Fr, pos=None):
    eq = MathTex(f"f(t) = \\sin({Fr.get_value():.1f}t)", font_size=40)
    # if pos is not None:
    #     eq.to_edge(RIGHT).shift(UP)
    # else:
    eq.to_edge(UP, buff=1)
    return eq


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class SinOmega(Scene):
    def construct(self):
        fx_sin_tex = MathTex("f(t)=A\\sin(\\omega t)", font_size=40)
        fx_sin_tex.to_edge(UP, buff=1)
        self.play(Write(fx_sin_tex))
        self.wait()
        omega = MathTex("f(t)=\\sin(\\omega t)", font_size=40).to_edge(UP, buff=1)
        self.play(TransformMatchingShapes(fx_sin_tex, omega))
        self.wait()
        w = ValueTracker(1.0)

        axes = Axes(
            x_range=[0, 4 * PI, PI / 2],
            y_range=[-2, 2],
            x_length=8,
            y_length=4,
            tips=False,
            axis_config={"color": BLUE, "tick_size": 0.05},
        ).to_edge(LEFT, buff=1)
        x_labels = VGroup()
        pi_values = [
            0,
            PI / 2,
            PI,
            3 * PI / 2,
            2 * PI,
            5 * PI / 2,
            3 * PI,
            7 * PI / 2,
            4 * PI,
        ]
        pi_labels = [
            "0",
            "\\frac{\\pi}{2}",
            "\\pi",
            "\\frac{3\\pi}{2}",
            "2\\pi",
            "\\frac{5\\pi}{2}",
            "3\\pi",
            "\\frac{7\\pi}{2}",
            "4\\pi",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 4 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.5)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.5)
                    )

            x_labels.add(x_label)

        axes_graph = VGroup(axes, x_labels)

        self.play(Create(axes_graph))
        self.wait()

        equation3 = always_redraw(lambda: main_eq(w, 1))

        self.play(
            axes_graph.animate.shift(0.5 * UP),
            TransformMatchingShapes(omega, equation3),
        )
        self.wait(1)

        sin_graph = always_redraw(
            lambda: axes.plot(
                lambda x: fx_sin(1, w.get_value(), x),
                x_range=[0, 4 * PI],
                color=YELLOW,
                stroke_width=3,
            )
        )

        self.play(Create(sin_graph))
        self.wait()

        static_sin_graph = axes.plot(
            lambda x: fx_sin(1, 1, x), x_range=[0, 4 * PI], color=RED, stroke_width=5
        )

        cir = Circle(radius=1.5, color=YELLOW).to_edge(RIGHT, buff=1).shift(0.5 * UP)
        circle_center = cir.get_center()

        # Horizontal line (x-axis)
        h_line = Line(
            circle_center + LEFT * 1.5,
            circle_center + RIGHT * 1.5,
            color=BLUE,
            stroke_width=2,
        )

        # Vertical line (y-axis)
        v_line = Line(
            circle_center + DOWN * 1.5,
            circle_center + UP * 1.5,
            color=BLUE,
            stroke_width=2,
        )

        # Create angle labels
        angles = [0, PI / 2, PI, 3 * PI / 2]
        angle_labels = ["0", "\\frac{\\pi}{2}", "\\pi", "\\frac{3\\pi}{2}"]

        labels_group = VGroup()

        for angle, label_text in zip(angles, angle_labels):
            # Calculate position on circle circumference
            label_pos = circle_center + 1.8 * np.array(
                [np.cos(angle), np.sin(angle), 0]
            )

            label = MathTex(label_text, font_size=24, color=WHITE)
            label.move_to(label_pos)
            labels_group.add(label)

        # Create dots at the cardinal points
        cardinal_dots = VGroup()
        cardinal_points = [
            circle_center + 1.5 * RIGHT,  # 0 radians (right)
            circle_center + 1.5 * UP,  # π/2 radians (top)
            circle_center + 1.5 * LEFT,  # π radians (left)
            circle_center + 1.5 * DOWN,  # 3π/2 radians (bottom)
        ]

        for point in cardinal_points:
            dot = Dot(point, radius=0.04, color=WHITE)
            cardinal_dots.add(dot)

        # Group everything together
        circle_with_axes = VGroup(cir, h_line, v_line, labels_group, cardinal_dots)

        period = static_sin_graph.get_subcurve(0, 0.5)
        period_copy = period.copy()
        self.play(Create(period_copy))
        self.wait()
        self.play(Transform(period_copy, cir))
        # self.remove(cir)
        self.wait()
        self.play(
            Create(h_line), Create(v_line), Create(labels_group), Create(cardinal_dots)
        )
        self.wait()
        dot_graph = Dot(radius=0.1, color=RED)
        dot_circle = Dot(radius=0.1, color=RED)

        dot_graph.move_to(period.get_start())
        dot_circle.move_to(cir.get_start())

        self.play(Create(dot_graph), Create(dot_circle))
        self.wait()

        self.play(
            MoveAlongPath(dot_graph, period, run_time=3, rate_func=smooth),
            MoveAlongPath(dot_circle, cir, run_time=3, rate_func=smooth),
        )
        self.wait(2)

        double_arrow = DoubleArrow(
            start=period.get_start(),
            end=period.get_end(),
            buff=0,
            color=GREEN,
            stroke_width=5,
            tip_length=0.2,
        ).next_to(period, UP, buff=0.1)
        period_symbol = MathTex("T", font_size=36).next_to(double_arrow, UP, buff=0.2)
        self.add(period)
        self.play(Create(double_arrow))
        self.play(Write(period_symbol))
        self.wait()

        definition = ar_text("الدور: هو الزمن اللازم لاتمام دورة كاملة.", 30).shift(
            2 * DOWN
        )
        self.play(Write(definition, reverse=True))
        self.add(definition)
        self.wait()
        self.play(FadeOut(period_symbol, period, definition, double_arrow))
        speed1 = MathTex(r"v", r"=", r"\frac{x}{t}").shift(2 * DOWN)
        self.play(Write(speed1))
        self.wait()
        speed2 = MathTex(r"v", r"=", r"\frac{2 \pi}{T}").shift(2 * DOWN)
        vg_g = VGroup(speed1, circle_with_axes.copy())
        self.play(ReplacementTransform(vg_g, speed2), run_time=1)
        self.wait()
        speed3 = MathTex(r"\omega", r"=", r"\frac{2 \pi}{T}").shift(2 * DOWN)
        self.play(TransformMatchingTex(speed2, speed3))
        self.wait()

        self.play(speed3.animate.shift(0.5 * UP))
        difination_omega = ar_text(
            "السرعة الزاوية: هي معدل تغير طور الموجة.", 30
        ).next_to(speed3, DOWN, buff=0.5)
        self.play(Write(difination_omega, reverse=True))
        self.add(difination_omega)
        self.wait()
        self.play(
            FadeOut(
                difination_omega,
                speed3,
                circle_with_axes,
                dot_circle,
                dot_graph,
                period_copy,
            )
        )
        # self.remove(cir)
        self.wait(2)

        freq_ar = [2, 5, 8, 4, 2, 0.5, 0.8]
        for i in freq_ar:
            self.play(w.animate.set_value(i), run_time=2, rate_func=smooth)

        self.wait(2)

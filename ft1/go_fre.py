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


class SinOmega(Scene):
    def construct(self):

        # fx_sin_tex = MathTex("f(t)=A\\sin(\\omega t)", font_size=40)
        # fx_sin_tex.to_edge(UP, buff=1)
        # self.play(Write(fx_sin_tex))
        # self.wait()
        # omega = MathTex("f(t)=\\sin(\\omega t)", font_size=40).to_edge(UP, buff=1)
        # self.play(TransformMatchingShapes(fx_sin_tex, omega))
        # self.wait()

        w = ValueTracker(1.0)

        # # equation = MathTex("f(t)=1.0sin(t)", font_size=40).to_edge(UP, buff=1)

        # self.wait()

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
        # axes_graph.to_edge(LEFT, buff=0.5)
        self.play(Create(axes_graph))
        self.wait()
        # equation = MathTex("f(t)=1.0sin(t)", font_size=40).to_edge(UP, buff=1)

        # equation = MathTex("f(t)=1.0sin(t)", font_size=40).to_edge(RIGHT, buff=1)
        # self.play(ReplacementTransform(omega, equation))
        # self.wait()
        equation3 = always_redraw(lambda: main_eq(w, 1))

        self.play(
            axes_graph.animate.shift(0.5 * UP),
            Create(
                # omega,
                equation3
            ),
        )
        self.wait(2)

        sin_graph = always_redraw(
            lambda: axes.plot(
                lambda x: fx_sin(1, w.get_value(), x),
                x_range=[0, 4 * PI],
                color=YELLOW,
                stroke_width=3,
            )
        )
        # A_label = always_redraw(
        #     lambda: MathTex(
        #         f"A = {Am.get_value():.1f}", font_size=30, color=GREEN
        #     ).next_to(axes.c2p(0, Am.get_value()), 0.3 * RIGHT + 0.6 * UP, buff=0.2)
        # )
        # neg_A_label = always_redraw(
        #     lambda: MathTex(
        #         f"-A = {-Am.get_value():.1f}", font_size=30, color=RED
        #     ).next_to(axes.c2p(0, -Am.get_value()), 0.3 * RIGHT + 0.6 * DOWN, buff=0.2)
        # )
        # A_line = always_redraw(
        #     lambda: DashedLine(
        #         start=axes.c2p(0, Am.get_value()),
        #         end=axes.c2p(4 * PI, Am.get_value()),
        #         color=GREEN,
        #         stroke_width=2,
        #     )
        # )
        # neg_A_line = always_redraw(
        #     lambda: DashedLine(
        #         start=axes.c2p(0, -Am.get_value()),
        #         end=axes.c2p(4 * PI, -Am.get_value()),
        #         color=RED,
        #         stroke_width=2,
        #     )
        # )
        # pos_arrow = always_redraw(
        #     lambda: Arrow(
        #         start=axes.c2p(PI / 2, 0),
        #         end=axes.c2p(PI / 2, Am.get_value()),
        #         color=GREEN,
        #         stroke_width=3,
        #         buff=0.1,
        #         max_tip_length_to_length_ratio=0.2,
        #     )
        # )
        # neg_arrow = always_redraw(
        #     lambda: Arrow(
        #         start=axes.c2p(3 * PI / 2, 0),
        #         end=axes.c2p(3 * PI / 2, -Am.get_value()),
        #         color=RED,
        #         stroke_width=4,
        #         buff=0.1,
        #         max_tip_length_to_length_ratio=0.2,
        #         # tip_length=0.1,  # Smaller tip length
        #         # tip_width=0.1,
        #     )
        # )
        self.play(Create(sin_graph))
        self.wait()
        # self.play(Create(A_line), Create(neg_A_line))
        # self.play(Write(A_label), Write(neg_A_label))
        # self.wait()
        # self.play(Create(pos_arrow), Create(neg_arrow))

        # amplitude_values = [0.5, 1.5, 2.0, 1.2, 2.5, 1.8]

        # for amp in amplitude_values:
        #     self.play(w.animate.set_value(amp), run_time=2, rate_func=smooth)
        #     self.wait()
        # self.wait(2)
        # Store original properties
        # original_width = axes.x_axis.stroke_width
        # original_color = axes.x_axis.get_stroke_color()

        # Highlight
        # self.play(axes.x_axis.animate.set_stroke(width=7, color=RED))
        # self.wait(1)

        # Revert
        # self.play(
        #     axes.x_axis.animate.set_stroke(width=original_width, color=original_color)
        # )
        static_sin_graph = axes.plot(
            lambda x: fx_sin(1, 1, x), x_range=[0, 4 * PI], color=RED, stroke_width=5
        )

        x_unit_scale = PI
        cir = Circle(radius=1.5, color=YELLOW).to_edge(RIGHT, buff=1).shift(0.5 * UP)

        period = static_sin_graph.get_subcurve(0, 0.5)
        self.play(Create(period))
        self.wait()
        self.play(Transform(period, cir))
        self.wait()

        dot_graph = Dot(radius=0.1, color=RED)
        dot_circle = Dot(radius=0.1, color=RED)

        dot_graph.move_to(period.get_start())
        dot_circle.move_to(cir.get_start())

        self.play(Create(dot_graph), Create(dot_circle))
        self.wait()

        self.play(
            MoveAlongPath(dot_graph, period, run_time=3),
            MoveAlongPath(dot_circle, cir, run_time=3),
        )
        self.wait(2)

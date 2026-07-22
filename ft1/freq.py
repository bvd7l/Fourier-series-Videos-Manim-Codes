from manim import *
import numpy as np


# def fx_sin(A, w, t):
#     return A * np.sin(w * t)


def main_eq(Fr, pos=None):
    eq = MathTex(f"f(t) = \\sin({Fr.get_value():.1f}t)", font_size=40)
    # if pos is not None:
    #     eq.to_edge(RIGHT).shift(UP)
    # else:
    eq.to_edge(UP, buff=1)
    return eq


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class SinFr(Scene):
    def construct(self):
        # fx_sin_tex = MathTex("f(t)=A\\sin(\\omega t)", font_size=40)
        # fx_sin_tex.to_edge(UP, buff=1)
        # self.play(Write(fx_sin_tex))
        # self.wait()
        # omega = MathTex("f(t)=\\sin(\\omega t)", font_size=40).to_edge(UP, buff=1)
        # self.play(TransformMatchingShapes(fx_sin_tex, omega))  # Changed to Transform
        # self.wait()
        # frequency = ValueTracker(1.0)
        # equation = always_redraw(lambda: main_eq(frequency))
        # self.play(TransformMatchingShapes(omega, equation))
        # self.wait()

        # axes = Axes(
        #     x_range=[0, 4 * PI, PI / 2],
        #     y_range=[-3, 3],
        #     x_length=8,
        #     y_length=4,
        #     tips=False,
        #     axis_config={"color": BLUE, "tick_size": 0.05},
        # ).to_edge(LEFT, buff=0.5)

        # self.play(Create(axes))
        # self.wait()

        # fx_sin = axes.plot(
        #     lambda x: np.sin(x), x_range=[0, 3 * PI], color=LIGHT_PINK
        # ).move_to(axes)
        # circle = Circle(radius=1, color=RED, stroke_width=10)
        # circle.move_to(axes.get_right() + RIGHT)

        # self.play(Create(fx_sin))
        # self.wait()

        # one_perios = fx_sin.get_subcurve(0, 0.75).set_color(RED)
        # self.play(Create(one_perios))
        # self.play(one_perios.animate.set_stroke_width(10))
        # self.wait()
        # self.play(Transform(one_perios, circle), run_time=2)
        # self.wait()

        # self.play(FadeOut(axes, fx_sin, one_perios))
        # self.wait()

        # cir = Circle(radius=2, color=ORANGE)
        # cir.to_edge(LEFT, buff=1)
        # dot = Dot(color=RED, radius=0.1)

        # dot.move_to(cir.point_from_proportion(0.5))

        # line = always_redraw(
        #     lambda: Line(
        #         start=cir.get_center(),
        #         end=dot.get_center(),
        #         color=YELLOW,
        #         stroke_width=4,
        #     )
        # )

        # self.play(Create(cir), Create(dot), Create(line))
        # self.wait(1)

        # self.play(MoveAlongPath(dot, cir), run_time=2, rate_func=smooth)
        # self.wait(2)

        # title = ar_text("الدائرة المثلثية", 30)
        # title.to_edge(UP, buff=0.5)
        # self.play(Write(title, reverse=True))
        # self.add(title)
        # self.wait()

        # axes = Axes(
        #     x_range=[-1.05, 1.05, 1],
        #     y_range=[-1.05, 1.05, 1],
        #     x_length=4.5,
        #     y_length=4.5,
        #     tips=False,
        #     axis_config={"color": BLUE, "tick_size": 0.1},
        # ).to_edge(LEFT, buff=1)
        # x_unit_scale = 4.5 / (2 * 1.05)
        # circle = Circle(radius=x_unit_scale, color=WHITE, stroke_width=3)
        # circle.move_to(axes.c2p(0, 0))
        # self.play(Create(axes))
        # self.wait()

        # angles = [0, PI / 2, PI, 3 * PI / 2]
        # angle_labesls = ["0", "\\frac{\\pi}{2}", "\\pi", "\\frac{3\\pi}{2}"]
        # angle_group = VGroup()
        # for angle, label in zip(angles, angle_labesls):
        #     x = np.cos(angle)
        #     y = np.sin(angle)

        #     point = axes.c2p(x, y)
        #     text = MathTex(label, font_size=30, color=YELLOW)

        #     if angle == 0:
        #         text.next_to(point, RIGHT, buff=0.2)
        #     elif angle == PI / 2:
        #         text.next_to(point, UP, buff=0.2)
        #     elif angle == PI:
        #         text.next_to(point, LEFT, buff=0.2)
        #     else:
        #         text.next_to(point, DOWN, buff=0.2)
        #     angle_group.add(text)

        # self.play(Create(circle))
        # self.play(Write(angle_group))
        # self.wait(2)

        # dot = Dot(radius=0.15, color=RED)
        # dot.move_to(circle.point_from_proportion(0))
        # line = always_redraw(
        #     lambda: Line(
        #         start=circle.get_center(),
        #         end=dot.get_center(),
        #         color=YELLOW,
        #         stroke_width=3,
        #     )
        # )
        # self.play(LaggedStart(Create(dot), Create(line), lag_ratio=0.5))

        # self.wait()

        # self.play(
        #     MoveAlongPath(dot, circle),
        #     run_time=2,
        #     rate_func=rate_functions.double_smooth,
        # )
        # self.wait(2)

        # self.play(
        #     MoveAlongPath(dot, circle),
        #     run_time=1,
        #     rate_func=rate_functions.smooth,
        # )
        # self.wait(2)

        text = ar_text("الدور: هو الزمن اللازم لاتمام دورة كاملة.")

        self.play(Write(text, reverse=True))
        self.wait(2)

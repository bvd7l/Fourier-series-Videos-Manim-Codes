from manim import *
import math
import numpy as np


def derivative(func, x, n=1, dx=0.01):
    samples = [func(x + (k - n / 2) * dx) for k in range(n + 1)]
    while len(samples) > 1:
        samples = [(s_plus_dx - s) / dx for s, s_plus_dx in zip(samples, samples[1:])]
    return samples[0]


def taylor_approximation(func, highest_term, center_point=0):
    derivatives = [derivative(func, center_point, n=n) for n in range(highest_term + 1)]
    coefficients = [d / math.factorial(n) for n, d in enumerate(derivatives)]
    return lambda x: sum(
        [c * ((x - center_point) ** n) for n, c in enumerate(coefficients)]
    )


class TS(Scene):
    def construct(self):
        # main f(x) = e^x config
        fx = lambda x: np.exp(x)
        fx_tex = "e^{x}"
        fx_color = BLUE

        # taylor config
        order_seq = [0, 1, 2, 3, 4, 5]
        center_point_a = 0
        approx_terms = [
            "1",
            "+x",
            "+\\frac{1}{2}x^2",
            "+\\frac{1}{6}x^3",
            "+\\frac{1}{24}x^4",
            # "+...",
        ]
        approx_color = RED

        axes = Axes(
            x_range=[-3, 4, 1], y_range=[-1, 10, 1], x_length=10, y_length=6, tips=False
        )
        axes.shift(2 * LEFT)

        # plot the main f(x)
        fx_graph = axes.plot(fx, color=fx_color)

        # plot the approx terms
        approx_graphs = [
            axes.plot(taylor_approximation(fx, n), color=approx_color)
            for n in order_seq
        ]

        near_text = Tex(f"Near $x = {center_point_a}$", font_size=36)
        near_text.to_corner(UP + RIGHT).shift(LEFT * 2)
        near_text.add_background_rectangle(BLACK, 0.7)

        # Create initial equation (just the base)
        equation_parts = [
            MathTex(fx_tex, font_size=36).set_color(fx_color),
            MathTex("\\approx", font_size=36),
        ]

        # Create all term objects but keep them hidden
        term_objects = []
        for term in approx_terms:
            term_obj = MathTex(term, font_size=36).set_color(approx_color)
            term_obj.set_opacity(0)  # Start invisible
            term_objects.append(term_obj)

        # Group all equation parts
        all_parts = VGroup(*equation_parts, *term_objects)
        all_parts.arrange(RIGHT, buff=0.1)
        all_parts.next_to(near_text, DOWN, buff=0.5)
        all_parts.to_edge(RIGHT)

        # Add background
        # bg_rect = BackgroundRectangle(
        #     all_parts, buff=0.2, color=BLACK, fill_opacity=0.7
        # )

        # create initial approximation graph
        center_dot = Dot(
            axes.c2p(center_point_a, fx(center_point_a)),
            color=approx_color,
            radius=0.08,
        )

        # Animation sequence
        self.play(Create(axes))
        self.wait(0.5)

        # Show only the base equation initially (e^x ≈)
        self.play(
            Create(fx_graph, run_time=1),
            Write(VGroup(*equation_parts)),
            Write(near_text),
            # Write(bg_rect),
        )

        # Add all term objects to scene (but they're invisible)
        for term_obj in term_objects:
            self.add(term_obj)

        self.wait(1)
        curr_approx = center_dot
        self.play(FadeIn(curr_approx))
        self.wait(0.5)

        # Gradually reveal terms
        for i, (graph, term_obj) in enumerate(zip(approx_graphs, term_objects)):
            self.play(
                ReplacementTransform(curr_approx, graph, run_time=1),
                term_obj.animate.set_opacity(1),
            )
            curr_approx = graph
            self.wait()

        self.wait(1)

        center_dot = Dot(axes.c2p(-2.5, 0), radius=0.05)
        right_current_dot = Dot(axes.c2p(2.3, 10), radius=0.05)
        rec = SurroundingRectangle(
            center_dot, color=ORANGE, buff=0.4, fill_opacity=0.1, stroke_width=3
        )
        rec2 = SurroundingRectangle(
            right_current_dot, color=ORANGE, buff=0.4, fill_opacity=0.1, stroke_width=3
        )

        self.play(
            Create(rec),
            Create(rec2),
            run_time=0.5,
            # rate_func=rate_functions.ease_in_out_circ,
        )
        self.wait()
        self.play(FadeOut(rec, rec2))
        self.wait()

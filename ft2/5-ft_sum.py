from manim import *
import numpy as np


def sigmod(x):
    return 1 / (1 + np.exp(-x))


def f_sin(x, f=9, A=1):
    return A * np.sin(f * x)


def f_cos(x, f=9):
    return np.cos(f * x)


def f2(x, a, b, offset=5):
    return sigmod(-a * (x - b - offset))


def f3(x, a, b, offset=5):
    return sigmod(a * (x + b - offset))


def fin_fun(x, a, b, freq, fun):
    return fun(x, freq) * f2(x, a, b) * f3(x, a, b)


class FT(Scene):
    def Create_small_axes_copy(self):
        small_axes = Axes(
            x_range=[-0.2, 10],
            y_range=[-2, 2],
            x_length=10.5,
            y_length=1,
            tips=False,
            x_axis_config={"tick_size": 0.05},
        )
        dashed2 = DashedLine(
            start=small_axes.c2p(0, 1.5),
            end=small_axes.c2p(10, 1.5),
            color=WHITE,
            stroke_opacity=0.5,
            dash_length=0.09,
            dashed_ratio=0.5,
        )
        group_small_graph = VGroup(small_axes, dashed2)

        return group_small_graph

    def construct(self):
        big_axes = Axes(
            x_range=[-0.2, 10],
            y_range=[-2, 2],
            x_length=10.5,
            y_length=1.5,
            tips=False,
        )

        dashed = DashedLine(
            start=big_axes.c2p(0, 1.5),
            end=big_axes.c2p(10, 1.5),
            color=WHITE,
            stroke_opacity=0.5,
            dash_length=0.09,
            dashed_ratio=0.5,
        )
        group_big_graph = VGroup(big_axes, dashed)
        main_graph = group_big_graph.copy()
        main_graph.to_corner(UP + LEFT, buff=0.7)
        # self.play(FadeIn(main_graph))

        small_axes_list = [self.Create_small_axes_copy() for _ in range(4)]
        all_small_axes = VGroup(*small_axes_list)
        all_small_axes.arrange(DOWN, buff=0.3)
        all_small_axes.next_to(main_graph, DOWN, buff=0.3)
        main_axes = main_graph[0]
        points = [
            (0, 0),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (2, -1),
            (2, 0),
            (2, 1),
            (3, 1),
            (3, 0),
            (3, -1),
            (4, -1),
            (4, 0),
            (4, 1),
            (5, 1),
            (5, 0),
            (5, -1),
            (6, -1),
            (6, 0),
            (6, 1),
            (7, 1),
            (7, 0),
            (7, -1),
            (8, -1),
            (8, 0),
            (8, 1),
            (9, 1),
            (9, 0),
            (9, -1),
            (10, -1),
            (10, 0),
            # (10, 1),
        ]
        # screenPoints = [main_axes.coords_to_point(x, y) for x, y in points]
        # lines = VGroup()

        # for i in range(len(screenPoints) - 1):
        #     line = Line(
        #         start=screenPoints[i],
        #         end=screenPoints[i + 1],
        #         color=RED,
        #         stroke_width=3,
        #     )
        #     lines.add(line)
        waveform_path = VMobject()
        waveform_path.set_points_as_corners([main_axes.c2p(x, y) for x, y in points])
        waveform_path.set_stroke(color=BLUE, width=3, opacity=1.0)

        fr = [(2 * i + 1) * PI for i in range(4)]
        Amm = [4 / ((2 * i + 1) * PI) for i in range(4)]
        col = [GOLD_A, PINK, GREEN, ORANGE]

        sin_waves = []
        wave_functions = []
        for i, (ax_g, f, a_m, cl) in enumerate(zip(all_small_axes, fr, Amm, col)):
            ax = ax_g[0]
            wave_func = lambda x, freq=f, AA_m=a_m: f_sin(x, f, AA_m) + 1.1
            sin_wave = ax.plot(
                wave_func,
                x_range=[0, 10],
                color=cl,
                stroke_width=2.5,
            )

            sin_waves.append(sin_wave)
            wave_functions.append(wave_func)
        sin_wave_formulas = VGroup()
        sin_wave_1 = (
            MathTex(r"\frac{4}{\pi} \sin(\pi t)", font_size=30, color=GOLD_A)
            .next_to(small_axes_list[0], RIGHT, buff=1)
            .shift(0.03 * UP)
        )
        sin_wave_2 = (
            MathTex(r"\frac{4}{3 \pi} \sin(3\pi t)", font_size=30, color=PINK)
            .next_to(small_axes_list[1], RIGHT, buff=1)
            .shift(0.03 * UP)
        )
        sin_wave_3 = (
            MathTex(r"\frac{4}{5 \pi} \sin(5\pi t)", font_size=30, color=GREEN)
            .next_to(small_axes_list[2], RIGHT, buff=1)
            .shift(0.03 * UP)
        )
        sin_wave_4 = (
            MathTex(r"\frac{4}{7 \pi} \sin(7\pi t)", font_size=30, color=ORANGE)
            .next_to(small_axes_list[3], RIGHT, buff=1)
            .shift(0.03 * UP)
        )
        sin_wave_formulas.add(sin_wave_1, sin_wave_2, sin_wave_3, sin_wave_4)
        self.play(FadeIn(main_graph, all_small_axes))

        # self.wait(1)
        self.play(FadeIn(waveform_path))
        self.play(waveform_path.animate.set_stroke(color=RED, width=3.5), run_time=2)
        self.play(
            LaggedStart(
                *[Create(wave) for wave in sin_waves],
                lag_ratio=0.3,
            ),
            LaggedStart(
                *[Write(s_w) for s_w in sin_wave_formulas],
                lag_ratio=0.3,
            ),
            run_time=5,
        )
        self.wait()
        # main_axes = main_graph[0]
        current_sum_wave = None

        for i, (small_wave, color, amplitude) in enumerate(zip(sin_waves, col, Amm)):

            wave_copy = small_wave.copy()
            wave_copy.set_stroke(width=2.5)

            if current_sum_wave is None:

                def first_wave_func(x):
                    return f_sin(x, fr[i], amplitude)

                first_wave_main = main_axes.plot(
                    first_wave_func,
                    x_range=[0, 10],
                    color=color,
                    stroke_width=2.5,
                )

                # Animate: Move the wave copy to main axes position
                self.play(
                    wave_copy.animate.move_to(first_wave_main).match_style(
                        first_wave_main
                    ),
                    run_time=2,
                )

                # Remove the copy and create the actual wave
                self.remove(wave_copy)
                self.add(first_wave_main)
                current_sum_wave = first_wave_main

            else:
                # Create the new wave component function
                def new_component_func(x):
                    return f_sin(x, fr[i], amplitude)

                # Create the new component wave on main axes
                new_component_main = main_axes.plot(
                    new_component_func,
                    x_range=[0, 10],
                    color=color,
                    stroke_width=2.5,
                )

                def partial_sum_func(x):
                    total = 0
                    for j in range(i + 1):
                        total += f_sin(x, fr[j], Amm[j])
                    return total

                updated_sum_wave = main_axes.plot(
                    partial_sum_func,
                    x_range=[0, 10],
                    color=BLUE,
                    stroke_width=3.5,
                )

                self.play(
                    wave_copy.animate.move_to(new_component_main).match_style(
                        new_component_main
                    ),
                    run_time=1.5,
                )

                self.remove(wave_copy)
                self.add(new_component_main)
                self.wait(0.5)

                temp_current = current_sum_wave.copy().set_color(YELLOW)
                temp_new = new_component_main.copy().set_color(color)

                self.play(
                    FadeOut(current_sum_wave),
                    FadeOut(new_component_main),
                    FadeIn(temp_current),
                    FadeIn(temp_new),
                    run_time=0.5,
                )

                self.play(
                    temp_current.animate.shift(UP * 0.2),
                    temp_new.animate.shift(DOWN * 0.2),
                    run_time=0.5,
                )

                self.play(
                    temp_current.animate.move_to(updated_sum_wave).match_style(
                        updated_sum_wave
                    ),
                    temp_new.animate.move_to(updated_sum_wave).match_style(
                        updated_sum_wave
                    ),
                    run_time=1,
                )

                self.play(
                    FadeOut(temp_current),
                    FadeOut(temp_new),
                    FadeIn(updated_sum_wave),
                    run_time=1,
                )

                current_sum_wave = updated_sum_wave

            self.wait(1)

        self.play(current_sum_wave.animate.set_stroke(width=5), run_time=1)
        self.wait()
        num = 5
        fr_f = [(2 * i + 1) * PI for i in range(num)]
        Amm_f = [4 / ((2 * i + 1) * PI) for i in range(num)]

        def the_final_signal(x):
            tot = 0
            for i in range(num):
                tot += f_sin(x, fr_f[i], Amm_f[i])
            return tot

        graphing_f = main_axes.plot(
            the_final_signal, x_range=[0, 10], color=BLUE, stroke_width=3.5
        )
        self.play(Transform(current_sum_wave, graphing_f))
        self.wait()
        point_1 = Dot(main_axes.c2p(1, 1), radius=0.0001)
        point_2 = Dot(main_axes.c2p(2, -1), radius=0.0001)
        point_3 = Dot(main_axes.c2p(3, 1), radius=0.0001)
        point_4 = Dot(main_axes.c2p(4, -1), radius=0.0001)
        rec1 = SurroundingRectangle(
            point_1, color=ORANGE, buff=0.2, fill_opacity=0.1, stroke_width=3
        )
        rec2 = SurroundingRectangle(
            point_2, color=ORANGE, buff=0.2, fill_opacity=0.1, stroke_width=3
        )
        rec3 = SurroundingRectangle(
            point_3, color=ORANGE, buff=0.2, fill_opacity=0.1, stroke_width=3
        )
        rec4 = SurroundingRectangle(
            point_4, color=ORANGE, buff=0.2, fill_opacity=0.1, stroke_width=3
        )

        recs = VGroup(rec1, rec2, rec3, rec4)
        self.play(
            LaggedStart(*[Create(rec) for rec in recs], lag_ratio=0.2), run_time=2
        )
        self.wait()
        all_objects = VGroup(
            waveform_path,  # Original blue/red waveform
            main_graph,  # Contains big_axes and dashed
            # labels,  # Text labels for axes
            all_small_axes,  # Small axes group
            VGroup(*sin_waves),  # Convert list to VGroup
            sin_wave_formulas,  # Math formulas
            recs,  # Rectangles
            current_sum_wave,  # or graphing_f (they're the same after Transform)
        )
        self.play(FadeOut(all_objects))
        self.wait()

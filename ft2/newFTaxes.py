from manim import *
import numpy as np


def sigmod(x):
    return 1 / (1 + np.exp(-x))


def f_sin(x, f=9):
    return np.sin(f * x)


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
            x_length=11.5,
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
        # group_small_graph.next_to(, DOWN, buff=0.5)
        return group_small_graph

    def construct(self):
        big_axes = Axes(
            x_range=[-0.2, 10],
            y_range=[-2, 2],
            x_length=11.5,
            y_length=1.5,
            tips=False,
        )
        # big_axes.add_coordinates()
        labels = big_axes.get_axis_labels(
            x_label=Text("Time", font_size=30),
            y_label=Text("Presure", font_size=30),
        )
        labels[0].shift(LEFT * 0.5 + DOWN * 1.3)
        labels[1].shift(LEFT + 0.2 * UP)
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
        main_graph.to_edge(UP, buff=1)
        self.add(main_graph)

        small_axes_list = [self.Create_small_axes_copy() for _ in range(4)]
        all_small_axes = VGroup(*small_axes_list)
        all_small_axes.arrange(DOWN, buff=0.3)
        all_small_axes.next_to(main_graph, DOWN, buff=0.3)

        fr = [6, 12, 3, 15]
        col = [RED, PINK, GREEN, ORANGE]

        sin_waves = []
        wave_functions = []
        for i, (ax_g, f, cl) in enumerate(zip(all_small_axes, fr, col)):
            ax = ax_g[0]
            if i & 1:
                wave_func = lambda x, freq=f: fin_fun(x, 1, 2.2, freq, f_sin) + 1.1
                sin_wave = ax.plot(
                    wave_func,
                    x_range=[0, 10],
                    color=cl,
                    stroke_width=2,
                )
            else:
                wave_func = lambda x, freq=f: fin_fun(x, 1, 2.2, freq, f_cos) + 1.1
                sin_wave = ax.plot(
                    wave_func,
                    x_range=[0, 10],
                    color=cl,
                    stroke_width=2,
                )
            sin_waves.append(sin_wave)
            wave_functions.append(wave_func)

        self.add(all_small_axes)

        self.wait(1)

        self.play(
            LaggedStart(*[Create(wave) for wave in sin_waves], lag_ratio=0.3),
            run_time=10,
        )
        self.wait(2)
        main_axes = main_graph[0]

        # Remove the original sum function and replace with gradual summing

        # Store the current sum wave on main axes
        current_sum_wave = None
        previous_sum_wave = None  # To track the previous sum wave for removal

        # Create gradual summing effect
        for i, (small_wave, color) in enumerate(zip(sin_waves, col)):
            # Create a copy of the current small wave
            wave_copy = small_wave.copy()
            wave_copy.set_stroke(width=3)  # Make it slightly thicker for visibility

            if current_sum_wave is None:
                # First wave - transform directly to main axes
                def first_sum_func(x):
                    return wave_functions[i](x) - 1.1

                first_sum_wave = main_axes.plot(
                    first_sum_func, x_range=[0, 10], color=color, stroke_width=3.5
                )

                self.play(Transform(wave_copy, first_sum_wave), run_time=2)
                current_sum_wave = first_sum_wave
                previous_sum_wave = current_sum_wave

            else:
                # Subsequent waves - show addition process
                def partial_sum_func(x):
                    total = 0
                    for j in range(i + 1):
                        total += wave_functions[j](x) - 1.1
                    return total

                def new_component_func(x):
                    return wave_functions[i](x) - 1.1

                # Create the new component wave on main axes
                new_component = main_axes.plot(
                    new_component_func,
                    x_range=[0, 10],
                    color=color,
                    stroke_width=2.5,
                    stroke_opacity=0.7,
                )

                # Create the updated sum wave
                updated_sum_wave = main_axes.plot(
                    partial_sum_func, x_range=[0, 10], color=BLUE, stroke_width=3.5
                )

                # Transform the copy to show new component appearing
                self.play(Transform(wave_copy, new_component), run_time=1.5)
                self.wait(0.5)

                # Remove the previous sum wave and show the new updated sum
                self.play(
                    FadeOut(previous_sum_wave),  # Remove previous sum wave
                    Create(updated_sum_wave),  # Create new sum wave
                    FadeOut(new_component),  # Remove the temporary component
                    run_time=2,
                )

                # Update references
                previous_sum_wave = current_sum_wave
                current_sum_wave = updated_sum_wave

            self.wait(1)

        # Final emphasis on the complete sum wave
        self.wait(2)

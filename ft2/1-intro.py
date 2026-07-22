from manim import *


class Intro(Scene):
    def construct(self):
        a_0 = MathTex(
            r"a_0",
            r"=",
            r"\frac{1}{T}",
            r"\int^{T}_{0}",
            r"f(t)",
            r"\, dt",
            font_size=30,
        )
        a_0[0].set_color(RED)
        a_0[3].set_color(YELLOW)
        a_0[5].set_color(YELLOW)

        a_n = MathTex(
            r"a_n",  # index 0
            r"=",  # index 1
            r"\frac{2}{T}",  # index 2
            r"\int^{T}_{0}",  # index 3
            r"f(t)",  # index 4
            r"\:cos(n \omega t)",  # index 5
            r"\:dt",  # index 6
            font_size=33,
        )
        a_n[0].set_color(RED)
        a_n[3].set_color(YELLOW)
        a_n[6].set_color(YELLOW)

        b_n = MathTex(
            r"b_n",  # index 0
            r"=",  # index 1
            r"\frac{2}{T}",  # index 2
            r"\int^{T}_{0}",  # index 3
            r"f(t)",  # index 4
            r"\:sin(n \omega t)",  # index 5
            r"\:dt",  # index 6
            font_size=33,
        )
        b_n[0].set_color(RED)
        b_n[3].set_color(YELLOW)
        b_n[6].set_color(YELLOW)

        g = VGroup(a_0, a_n, b_n).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        self.play(LaggedStart(*[Write(i) for i in g], lag_ratio=1), run_time=3)
        self.wait()
        self.play(FadeOut(g))
        self.wait()

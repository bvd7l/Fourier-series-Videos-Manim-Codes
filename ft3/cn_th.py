from manim import *


class CNThum(Scene):
    def construct(self):
        c_n = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{- \infty}^{\infty}",  # 2
            r"C_n",
            r"e^{j n \omega t}",  # 12
            # font_size=36
        ).shift(UP)
        c_n[3].set_color(GREEN)

        c_n7 = MathTex(
            r"C_n",  # 6
            r"=",  # 4
            r"\frac{1}{T_0}",
            r"\int_{0}^{T_0}",  # 0
            r"\, f(t)",  # 1
            r"e^{-j n \omega t}",  # 0
            r"\; dt",  # 3
            # font_size=36,
        ).next_to(c_n, DOWN, buff=0.5)
        c_n7[0].set_color(GREEN)
        c_n7[5].set_color(RED)
        c_n7[3].set_color(YELLOW)
        c_n7[6].set_color(YELLOW)

        self.add(c_n)
        self.add(c_n7)
        self.wait(5)

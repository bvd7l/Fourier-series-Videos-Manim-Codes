from manim import *


class SplitIntegralAnimation(Scene):
    def construct(self):

        eq1 = MathTex(
            r"f(t)",  # index 0
            r"=",  # index 1
            r"a_0",
            r"+" r"\sum^{\infty}_{n=1}",  # index 2
            r"a_n \:",  # index 3
            r"cos(n \omega t)",  # index 4
            r"+",  # index 5
            r"b_n \:",  # index 6
            r"sin(n \omega t)",  # index 7
            font_size=30,
        )
        eq2 = MathTex(
            r"f(t)",  # index 0
            r"=",  # index 1
            r"a_0",
            r"+",
            r"\sum^{\infty}_{n=1}",  # index 2
            r"a_n \:",  # index 3
            r"cos(n \omega t)",  # index 4
            r"+",  # index 5
            r"\sum^{\infty}_{n=1}"  # 6
            r"b_n \:",  # index 7
            r"sin(n \omega t)",  # index 8
            font_size=30,
        )
        eq3 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\: dt",  # index 2
            r"=",  # index 3
            r"\int^{T}_{0}",  # index 4
            r"a_0",  # index 5
            r"\: dt",  # index 6
            r"+",  # index 7
            r"\int^{T}_{0}",  # index 8
            r"\sum^{\infty}_{n=1}",  # index 9
            r"a_n",  # index 10
            r"\: \cos(n \omega t)",  # index 11
            r"\: dt",  # index 12
            r"+",  # index 13
            r"\int^{T}_{0}",  # index 14
            r"\sum^{\infty}_{n=1}",  # index 15
            r"b_n",  # index 16
            r"\: \sin(n \omega t)",  # index 17
            r"\: dt",  # index 18
            font_size=30,
        ).shift(2 * UP)
        eq3[0].set_color(YELLOW)
        eq3[4].set_color(YELLOW)
        eq3[8].set_color(YELLOW)
        eq3[14].set_color(YELLOW)

        eq4 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\: dt",  # index 2
            r"=",  # index 3
            r"\int^{T}_{0}",  # index 4
            r"a_0",  # index 5
            r"\: dt",  # index 6
            r"+",  # index 7
            r"\sum^{\infty}_{n=1}",  # index 8
            r"a_n",  # index 9
            r"\int^{T}_{0}",  # index 10
            r"\: \cos(n \omega t)",  # index 11
            r"\: dt",  # index 12
            r"+",  # index 13
            r"\sum^{\infty}_{n=1}",  # index 14
            r"b_n",  # index 15
            r"\int^{T}_{0}",  # index 16
            r"\: \sin(n \omega t)",  # index 17
            r"\: dt",  # index 18
            font_size=30,
        ).shift(2 * UP)
        eq4[0].set_color(YELLOW)
        eq4[4].set_color(YELLOW)
        eq4[10].set_color(YELLOW)
        eq4[16].set_color(YELLOW)

        eq5 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\: dt",  # index 2
            r"=",  # index 3
            r"\int^{T}_{0}",  # index 4
            r"a_0",  # index 5
            r"\: dt",  # index 6
            r"+",  # index 7
            r"\sum^{\infty}_{n=1}",  # index 8
            r"a_n",  # index 9
            r"0",
            r"+",  # index 13
            r"\sum^{\infty}_{n=1}",  # index 14
            r"b_n",  # index 15
            r"0",
            font_size=30,
        ).next_to(eq4, DOWN, buff=0.5)
        eq5[0].set_color(YELLOW)
        eq5[4].set_color(YELLOW)

        eq6 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\: dt",  # index 2
            r"=",  # index 3
            r"\int^{T}_{0}",  # index 4
            r"a_0",  # index 5
            r"\: dt",  # index 6
            font_size=30,
        ).next_to(eq4, DOWN, buff=0.5)
        eq6[0].set_color(YELLOW)
        eq6[4].set_color(YELLOW)
        eq7 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\: dt",  # index 2
            r"=",
            r"a_0 \left[ t \right]_{0}^{T}",  # index 5  # index 6
            font_size=30,
        ).next_to(eq4, DOWN, buff=0.5)
        eq7[0].set_color(YELLOW)
        eq8 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\: dt",  # index 2
            r"=",
            r"a_0 T",  # index 5  # index 6
            font_size=30,
        ).next_to(eq4, DOWN, buff=0.5)
        eq8[0].set_color(YELLOW)
        eq9 = MathTex(
            r"a_0",
            r"=",
            r"\frac{1}{T}",
            r"\int^{T}_{0}",
            r"f(t)",
            r"\, dt",
            font_size=30,
        ).next_to(eq8, DOWN, buff=0.5)
        eq9[0].set_color(RED)
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingShapes(eq1, eq2))
        self.wait()
        self.play(eq2.animate.shift(2 * UP))
        self.wait()
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait()
        rec1 = SurroundingRectangle(eq4[16:], color=ORANGE, stroke_width=3, buff=0.1)
        rec2 = SurroundingRectangle(eq4[10:13], color=ORANGE, stroke_width=3, buff=0.1)
        self.play(Create(rec1), Create(rec2))
        self.wait()
        eq4_copy = eq4.copy()
        self.play(TransformMatchingTex(eq4_copy, eq5), FadeOut(rec1, rec2))
        self.wait()
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait()
        self.play(TransformMatchingTex(eq6, eq7))
        self.wait()
        self.play(TransformMatchingTex(eq7, eq8))
        self.wait()
        eq8_copy = eq8.copy()
        self.play(TransformMatchingTex(eq8_copy, eq9))
        self.wait()
        rec3 = SurroundingRectangle(eq9, color=BLUE, stroke_width=3, buff=0.1)
        self.play(Create(rec3))
        self.wait()

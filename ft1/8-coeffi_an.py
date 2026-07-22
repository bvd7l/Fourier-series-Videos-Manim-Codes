from manim import *


class SplitIntegralAnimation(Scene):
    def construct(self):

        equation1 = MathTex(
            r"f(t)",  # index 0
            "=",  # index 1
            r"\sum^{\infty}_{n=0}",  # index 2
            r"a_n \:",  # index 3
            r"cos(n \omega t)",  # index 4
            r"+",  # index 5
            r"b_n \:",  # index 6
            r"sin(n \omega t)",  # index 7
            font_size=33,
        )
        equation2 = MathTex(
            r"f(t)",  # index 0
            r"=",  # index 1
            r"\sum^{\infty}_{n=0}",  # index 2
            r"a_n \:",  # index 3
            r"cos(n \omega t)",  # index 4
            r"+",  # index 5
            r"\sum^{\infty}_{n=0}",  # index 6
            r"b_n \:",  # index 7
            r"sin(n \omega t)",  # index 8
            font_size=33,
        )

        equation3 = MathTex(
            r"f(t)",  # index 0
            r"\:cos(m \omega t)",  # index 1
            r"=",  # index 2
            r"\sum^{\infty}_{n=0}",  # index 3
            r"a_n \:",  # index 4
            r"cos(n \omega t)",  # index 5
            r"\:cos(m \omega t)",  # index 6
            r"+",  # index 7
            r"\sum^{\infty}_{n=0}",  # index 8
            r"b_n \:",  # index 9
            r"sin(n \omega t)",  # index 10
            r"\:cos(m \omega t)",  # index 11
            font_size=33,
        ).shift(2 * UP)
        equation3[1].set_color(RED)
        equation3[6].set_color(RED)
        equation3[11].set_color(RED)

        equation4 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\:cos(m \omega t)",  # index 2
            r"\:dt",  # index 3
            r"=",  # index 4
            r"\int^{T}_{0}",  # index 5
            r"\sum^{\infty}_{n=0}",  # index 6
            r"a_n \:",  # index 7
            r"cos(n \omega t)",  # index 8
            r"\:cos(m \omega t)",  # index 9
            r"\:dt",  # index 10
            r"+",  # index 11
            r"\int^{T}_{0}",  # index 12
            r"\sum^{\infty}_{n=0}",  # index 13
            r"b_n \:",  # index 14
            r"sin(n \omega t)",  # index 15
            r"\:cos(m \omega t)",  # index 16
            r"\:dt",  # index 17
            font_size=33,
        ).shift(2 * UP)
        equation4[2].set_color(RED)
        equation4[9].set_color(RED)
        equation4[16].set_color(RED)
        equation4[0].set_color(YELLOW)
        equation4[5].set_color(YELLOW)
        equation4[12].set_color(YELLOW)

        equation5 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\:cos(m \omega t)",  # index 2
            r"\:dt",  # index 3
            r"=",  # index 4
            r"\sum^{\infty}_{n=0}",  # index 5
            r"a_n",  # index 6
            r"\int^{T}_{0}",  # index 7
            r"cos(n \omega t)",  # index 8
            r"\:cos(m \omega t)",  # index 9
            r"\:dt",  # index 10
            r"+",  # index 11
            r"\sum^{\infty}_{n=0}",  # index 12
            r"b_n",  # index 13
            r"\int^{T}_{0}",  # index 14
            r"sin(n \omega t)",  # index 15
            r"\:cos(m \omega t)",  # index 16
            r"\:dt",  # index 17
            font_size=33,
        ).shift(2 * UP)
        equation5[2].set_color(RED)
        equation5[9].set_color(RED)
        equation5[16].set_color(RED)
        equation5[0].set_color(YELLOW)
        equation5[7].set_color(YELLOW)
        equation5[14].set_color(YELLOW)

        int_zero = VGroup(equation5[14:18])  # Updated: integral + sin + cos + dt
        box1 = SurroundingRectangle(int_zero, color=ORANGE, stroke_width=3, buff=0.1)

        equation6 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\:cos(m \omega t)",  # index 2
            r"\:dt",  # index 3
            r"=",  # index 4
            r"\sum^{\infty}_{n=0}",  # index 5
            r"a_n",  # index 6
            r"\int^{T}_{0}",  # index 7
            r"cos(n \omega t)",  # index 8
            r"\:cos(m \omega t)",  # index 9
            r"\:dt",  # index 10
            r"+",  # index 11
            r"\sum^{\infty}_{n=0}",  # index 12
            r"b_n",  # index 13
            r"0",  # index 14
            font_size=33,
        ).next_to(equation5, DOWN, buff=0.5)
        equation6[2].set_color(RED)
        equation6[14].set_color(YELLOW)
        equation6[0].set_color(YELLOW)
        equation6[7].set_color(YELLOW)

        equation7 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\:cos(m \omega t)",  # index 2
            r"\:dt",  # index 3
            r"=",  # index 4
            r"\sum^{\infty}_{n=0}",  # index 5
            r"a_n",  # index 6
            r"\int^{T}_{0}",  # index 7
            r"cos(n \omega t)",  # index 8
            r"\:cos(m \omega t)",  # index 9
            r"\:dt",  # index 10
            font_size=33,
        ).next_to(equation5, DOWN, buff=0.5)
        equation7[2].set_color(RED)
        equation7[9].set_color(RED)
        equation7[0].set_color(YELLOW)
        equation7[7].set_color(YELLOW)
        int_pi = VGroup(equation7[7:11])  # Updated: integral + cos + cos + dt
        box2 = SurroundingRectangle(int_pi, color=ORANGE, stroke_width=3, buff=0.1)
        n_eq_m = MathTex(r"n=m", font_size=33, color=ORANGE).next_to(
            equation7, RIGHT, buff=1
        )

        equation8 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\:cos(m \omega t)",  # index 2
            r"\:dt",  # index 3
            r"=",  # index 4
            r"\sum^{\infty}_{n=0}",  # index 5
            r"a_n",  # index 6
            r"\int^{T}_{0}",  # index 7
            r"cos(n \omega t)",  # index 8
            r"\:cos(m \omega t)",  # index 9
            r"\:dt",  # index 10
            font_size=33,
        ).next_to(equation5, DOWN, buff=0.5)
        equation8[2].set_color(RED)
        equation8[9].set_color(RED)
        equation8[0].set_color(YELLOW)
        equation8[7].set_color(YELLOW)

        equation9 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\:cos(m \omega t)",  # index 2
            r"\:dt",  # index 3
            r"=",  # index 4
            r"a_n",  # index 5
            r"\int^{T}_{0}",  # index 6
            r"cos(n \omega t)",  # index 7
            r"\:cos(n \omega t)",  # index 8
            r"\:dt",  # index 9
            font_size=33,
        ).next_to(equation5, DOWN, buff=0.5)
        equation9[2].set_color(RED)
        equation9[8].set_color(RED)
        equation9[0].set_color(YELLOW)
        equation9[6].set_color(YELLOW)
        int_T2 = VGroup(equation9[6:10])  # Updated: integral + cos + cos + dt
        box3 = SurroundingRectangle(int_T2, color=ORANGE, stroke_width=3, buff=0.1)

        equation10 = MathTex(
            r"\int^{T}_{0}",  # index 0
            r"f(t)",  # index 1
            r"\:cos(m \omega t)",  # index 2
            r"\:dt",  # index 3
            r"=",  # index 4
            r"a_n",  # index 5
            r"\frac{T}{2}",  # index 6
            font_size=33,
        ).next_to(equation5, DOWN, buff=0.5)
        equation10[2].set_color(RED)
        equation10[0].set_color(YELLOW)
        equation10[6].set_color(YELLOW)

        equation11 = MathTex(
            r"a_n",  # index 0
            r"=",  # index 1
            r"\frac{2}{T}",  # index 2
            r"\int^{T}_{0}",  # index 3
            r"f(t)",  # index 4
            r"\:cos(n \omega t)",  # index 5
            r"\:dt",  # index 6
            font_size=33,
        ).next_to(equation10, DOWN, buff=0.5)
        equation11[0].set_color(RED)
        box4 = SurroundingRectangle(equation11, color=BLUE, stroke_width=3, buff=0.1)

        self.play(Write(equation1))
        self.wait()
        self.play(TransformMatchingShapes(equation1, equation2))
        self.wait()
        self.play(equation2.animate.shift(UP * 2))
        self.wait()
        self.play(TransformMatchingTex(equation2, equation3))
        self.wait()
        self.play(TransformMatchingTex(equation3, equation4))
        self.wait()
        self.play(TransformMatchingTex(equation4, equation5))
        self.wait()
        self.play(Create(box1))
        self.wait()
        self.add(equation5)
        equation5_copy = equation5.copy()
        self.play(FadeOut(box1), TransformMatchingTex(equation5_copy, equation6))
        self.wait()
        self.play(TransformMatchingTex(equation6, equation7))
        self.wait()
        self.play(Create(box2))
        self.wait()
        self.play(FadeOut(box2))
        self.wait()
        self.play(Write(n_eq_m))
        self.wait()
        self.play(TransformMatchingShapes(equation7, equation8))
        self.wait()
        self.play(TransformMatchingTex(equation8, equation9))
        self.wait()
        self.play(Create(box3))
        self.wait()
        self.play(FadeOut(box3, n_eq_m, lag_ratio=0.5))
        self.wait()
        self.play(TransformMatchingTex(equation9, equation10))
        self.wait()
        self.add(equation10)
        equation10_copy = equation10.copy()
        self.play(TransformMatchingTex(equation10_copy, equation11))
        self.wait()
        self.play(Create(box4))
        self.wait()

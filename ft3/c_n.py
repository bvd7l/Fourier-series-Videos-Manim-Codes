from manim import *


class CN(Scene):
    def construct(self):
        c_n = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{- \infty}^{\infty}",  # 2
            r"C_n",
            r"e^{j n \omega t}",  # 12
            font_size=36,
        )
        c_n[3].set_color(GREEN)

        c_n1 = MathTex(
            r"f(t)",  # 1
            r"\, e^{-j m \omega t}",  # 0
            r"=",  # 2
            r"\sum_{- \infty}^{\infty}",  # 3
            r"C_n",  # 4
            r"e^{j n \omega t} \,",  # 5
            r"e^{-j m \omega t}",  # 6
            font_size=36,
        )
        c_n1[4].set_color(GREEN)
        c_n1[1].set_color(RED)
        c_n1[6].set_color(RED)

        c_n2 = MathTex(
            r"\, f(t)",  # 1
            r"e^{-j m \omega t}",  # 0
            r"=",  # 2
            r"\sum_{- \infty}^{\infty}",  # 3
            r"C_n",  # 4
            r"e^{",
            r"j \omega t",
            r"(n-",
            r"m",
            r")",
            r"}",
            font_size=36,
        )
        c_n2[4].set_color(GREEN)
        c_n2[1].set_color(RED)
        c_n2[8].set_color(RED)

        c_n3 = MathTex(
            r"\int_{0}^{T_0}",  # 0
            r"\, f(t)",  # 1
            r"e^{-j m \omega t}",  # 0
            r"\; dt",  # 3
            r"=",  # 4
            r"\int_{0}^{T_0}",  # 5
            r"\sum_{- \infty}^{\infty}",  # 6
            r"C_n",  # 7
            r"e^{",  # 8
            r"j \omega t",  # 9
            r"(n-",  # 10
            r"m",  # 11
            r")",  # 12
            r"}",  # 13
            r"\; dt",  # 14
            font_size=36,
        )
        c_n3[7].set_color(GREEN)
        c_n3[2].set_color(RED)
        c_n3[11].set_color(RED)
        c_n3[0].set_color(YELLOW)
        c_n3[3].set_color(YELLOW)
        c_n3[5].set_color(YELLOW)
        c_n3[14].set_color(YELLOW)

        c_n4 = MathTex(
            r"\int_{0}^{T_0}",  # 0
            r"\, f(t)",  # 1
            r"e^{-j m \omega t}",  # 0
            r"\; dt",  # 3
            r"=",  # 4
            r"\sum_{- \infty}^{\infty}",  # 5
            r"C_n",  # 6
            r"\int_{0}^{T_0}",  # 7
            r"e^{",  # 8
            r"j \omega t",  # 9
            r"(n-",  # 10
            r"m",  # 11
            r")",  # 12
            r"}",  # 13
            r"\; dt",  # 14
            font_size=36,
        )
        c_n4[6].set_color(GREEN)
        c_n4[2].set_color(RED)
        c_n4[11].set_color(RED)
        c_n4[0].set_color(YELLOW)
        c_n4[3].set_color(YELLOW)
        c_n4[7].set_color(YELLOW)
        c_n4[14].set_color(YELLOW)
        case1 = MathTex(r"n", r"\neq", r"m", color=ORANGE, font_size=36)
        n_m11 = MathTex(r"n=2", font_size=36)
        n_m12 = MathTex(r"m=1", font_size=36)
        n_m1 = VGroup(n_m11, n_m12).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        case1_int1 = MathTex(
            r"\int_{0}^{T_0}", r"e ^ {j \omega t}", r"\, dt", font_size=36
        )
        case1_int2 = MathTex(
            r"\left[",
            r"\frac{1}{j \omega}",
            r"e ^ {j \omega t}",
            r"\right]_{0}^{T_0}",
            font_size=36,
        )
        case1_int3 = MathTex(
            r"\frac{1}{j \omega}",
            r"\left[",
            r"e ^ {j \omega t}",
            r"\right]_{0}^{T_0}",
            font_size=36,
        )
        case1_int4 = MathTex(
            r"\frac{1}{j \omega}",
            r"\left[",
            r"e ^ {j \omega T_0}",
            r"-",
            r"e ^ {j \omega 0}",
            r"\right]",
            font_size=36,
        )
        case1_int5 = MathTex(
            r"\frac{1}{j \omega}",
            r"\left[",
            r"e ^ {j \frac{2\pi}{T_0} T_0}",
            r"-",
            r"e ^ {0}",
            r"\right]",
            font_size=36,
        )
        case1_int6 = MathTex(
            r"\frac{1}{j \omega}",
            r"\left[",
            r"e ^ {j 2 \pi}",
            r"-",
            r"1",
            r"\right]",
            font_size=36,
        )
        case1_int7 = MathTex(
            r"\frac{1}{j \omega}",
            r"\left[",
            r"e ^ {j 0}",
            r"-",
            r"1",
            r"\right]",
            font_size=36,
        )
        case1_int8 = MathTex(
            r"\frac{1}{j \omega}",
            r"\left[",
            r"1",
            r"-",
            r"1",
            r"\right]",
            font_size=36,
        )
        case1_int9 = MathTex(
            r"\frac{1}{j \omega}",
            r"\left[",
            r"0",
            r"\right]",
            font_size=36,
        )
        case1_int10 = MathTex(
            r"0",
            font_size=36,
        )
        case1_int11 = MathTex(
            r"\int_{0}^{T_0}", r"e ^ {j \omega t}", r"\, dt", r"=", r"0", font_size=36
        )

        case2 = MathTex(r"n", r"=", r"m", color=ORANGE, font_size=36)
        case2_int1 = MathTex(
            r"\int_{0}^{T_0}", r"e ^ {j \omega t (0)}", r"\, dt", font_size=36
        )
        case2_int2 = MathTex(r"\int_{0}^{T_0}", r"e ^ {0}", r"\, dt", font_size=36)
        case2_int3 = MathTex(r"\int_{0}^{T_0}", r"1", r"\, dt", font_size=36)
        case2_int4 = MathTex(r"\left[", r"t", r"\right]_{0}^{T_0}", font_size=36)
        case2_int5 = MathTex(r"\left[", r"T_0", r"-", r"0", r"\right]", font_size=36)
        case2_int6 = MathTex(r"T_0", font_size=36)
        case2_int7 = MathTex(
            r"\int_{0}^{T_0}",
            r"e ^ {j \omega t (0)}",
            r"\, dt",
            r"=",
            r"T_0",
            font_size=36,
        )
        full_int = MathTex(
            r"\int_{0}^{T_0}",  # 7
            r"e^{",  # 8
            r"j \omega t",  # 9
            r"(n-",  # 10
            r"m",  # 11
            r")",  # 12
            r"}",  # 13
            r"\; dt",  # 14
            r"=",
            r"\begin{cases} T_0 & n = m \\ 0 & n \neq m \end{cases}",
            font_size=36,
        )
        t0 = MathTex(r"T_0", font_size=36)
        c_n5 = MathTex(
            r"\int_{0}^{T_0}",  # 0
            r"\, f(t)",  # 1
            r"e^{-j m \omega t}",  # 0
            r"\; dt",  # 3
            r"=",  # 4
            r"C_n",  # 6
            r"T_0",
            font_size=36,
        ).shift(2 * UP)
        c_n5[5].set_color(GREEN)
        c_n5[2].set_color(RED)
        c_n5[0].set_color(YELLOW)
        c_n5[3].set_color(YELLOW)
        c_n6 = MathTex(
            r"\int_{0}^{T_0}",  # 0
            r"\, f(t)",  # 1
            r"e^{-j n \omega t}",  # 0
            r"\; dt",  # 3
            r"=",  # 4
            r"C_n",  # 6
            r"T_0",
            font_size=36,
        ).shift(2 * UP)
        c_n6[5].set_color(GREEN)
        c_n6[2].set_color(RED)
        c_n6[0].set_color(YELLOW)
        c_n6[3].set_color(YELLOW)
        c_n7 = MathTex(
            r"C_n",  # 6
            r"=",  # 4
            r"\frac{1}{T_0}",
            r"\int_{0}^{T_0}",  # 0
            r"\, f(t)",  # 1
            r"e^{-j n \omega t}",  # 0
            r"\; dt",  # 3
            font_size=36,
        ).shift(2 * UP)
        c_n7[0].set_color(GREEN)
        c_n7[5].set_color(RED)
        c_n7[3].set_color(YELLOW)
        c_n7[6].set_color(YELLOW)
        ## --------------- animations section ---------------

        self.play(Write(c_n))
        self.wait()
        self.play(TransformMatchingTex(c_n, c_n1))
        self.wait()
        brc1 = Brace(c_n1[-1], DOWN, buff=0.1)
        brc2 = Brace(c_n1[-2], DOWN, buff=0.1)
        self.play(Create(brc1), Create(brc2))
        self.wait()
        self.play(FadeOut(brc1, brc2), TransformMatchingTex(c_n1, c_n2))
        self.wait()
        self.play(TransformMatchingTex(c_n2, c_n3))
        self.wait()
        self.play(TransformMatchingTex(c_n3, c_n4))
        self.wait()
        self.play(c_n4.animate.shift(2 * UP))
        self.wait()
        brc1 = Brace(c_n4[7:], DOWN, buff=0.1)
        self.play(Create(brc1))
        self.wait()
        case1.next_to(c_n4, DOWN, buff=0.5)
        case1.shift(3 * LEFT)
        self.play(TransformFromCopy(VGroup(c_n4[7:]), case1))
        self.wait()
        n_m1.next_to(case1, DOWN, buff=0.5)
        n_m1.shift(2 * LEFT)
        self.play(Write(n_m1))
        self.wait()
        case1_int1.next_to(case1, DOWN, buff=0.5)
        self.play(Write(case1_int1))
        self.wait()
        self.play(FadeOut(n_m1))
        self.wait()
        case1_int2.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformFromCopy(case1_int1, case1_int2))
        self.wait()
        case1_int3.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int2, case1_int3))
        self.wait()
        case1_int4.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int3, case1_int4))
        self.wait()
        case1_int5.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int4, case1_int5))
        self.wait()
        case1_int6.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int5, case1_int6))
        self.wait()
        case1_int7.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int6, case1_int7))
        self.wait()
        case1_int8.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int7, case1_int8))
        self.wait()
        case1_int9.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int8, case1_int9))
        self.wait()
        case1_int10.next_to(case1_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case1_int9, case1_int10))
        self.wait()
        case1_int11.move_to(case1_int1)
        self.play(TransformMatchingTex(case1_int1, case1_int11), FadeOut(case1_int10))
        self.wait()

        # case n = m animations
        case2.next_to(case1, RIGHT, buff=3)
        self.play(TransformFromCopy(VGroup(c_n4[7:]), case2))
        self.wait()
        case2_int1.next_to(case2, DOWN, buff=0.5)
        self.play(Write(case2_int1))
        self.wait()
        case2_int2.next_to(case2_int1, DOWN, buff=0.5)
        self.play(TransformFromCopy(case2_int1, case2_int2))
        self.wait()
        case2_int3.next_to(case2_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case2_int2, case2_int3))
        self.wait()
        case2_int4.next_to(case2_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case2_int3, case2_int4))
        self.wait()
        case2_int5.next_to(case2_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case2_int4, case2_int5))
        self.wait()
        case2_int6.next_to(case2_int1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(case2_int5, case2_int6))
        self.wait()
        case2_int7.move_to(case2_int1)
        self.play(TransformMatchingTex(case2_int1, case2_int7), FadeOut(case2_int6))
        self.wait()
        rest = VGroup(case1, case1_int11, case2, case2_int7)
        self.play(ReplacementTransform(rest, full_int))
        self.wait()
        t0.move_to(VGroup(c_n4[7:]).get_center() + LEFT)
        self.play(ReplacementTransform(VGroup(c_n4[7:]), t0), FadeOut(brc1))
        self.wait()
        rec = SurroundingRectangle(c_n4[5], color=ORANGE, stroke_width=3, buff=0.1)
        self.play(Create(rec))
        self.wait()
        self.play(FadeOut(rec), c_n4[5].animate.set_opacity(0))
        self.wait()
        # c_n5.move_to(c_n4)
        self.play(TransformMatchingTex(c_n4, c_n5), FadeOut(t0))
        self.wait()
        rec = SurroundingRectangle(c_n5[2], color=ORANGE, stroke_width=3, buff=0.1)
        self.play(Create(rec))
        self.wait()
        self.play(TransformMatchingTex(c_n5, c_n6), FadeOut(rec))
        self.wait()
        self.play(FadeOut(full_int))
        self.wait()
        self.play(TransformMatchingTex(c_n6, c_n7))
        self.wait()
        self.play(FadeOut(c_n7))
        self.wait()

from manim import *
from reactive_manim import *


class ComplexFormFT(Scene):
    def construct(self):
        distance = 3
        cos_theta = (
            MathTex(
                r"\cos(\theta)",
                r"=",
                r"\frac{e^{j \theta} + e^{-j \theta}}{2}",
                font_size=36,
            )
            .to_edge(UP, buff=1)
            .shift(distance * LEFT)
        )

        sin_theta = (
            MathTex(
                r"\sin(\theta)",
                r"=",
                r"\frac{e^{j \theta} - e^{-j \theta}}{2j}",
                font_size=36,
            )
            .to_edge(UP, buff=1)
            .shift(distance * RIGHT)
        )
        ft_formula = MathTex(
            r"f(t)",
            r"=",
            r"\sum_{n=0}^{\infty}",
            r"a_n",
            r"\cos(n \omega t)",
            r"+",
            r"b_n",
            r"\sin(n \omega t)",
            font_size=36,
        ).shift(UP)
        ft_formula[3].set_color(RED)
        ft_formula[6].set_color(RED)
        ft_formula2 = MathTex(
            r"f(t)",
            r"=",
            r"\sum_{n=0}^{\infty}",
            r"a_n",
            r"\frac{e^{j n \omega t} + e^{-j n \omega t}}{2}",
            r"+",
            r"b_n",
            r"\sin(n \omega t)",
            font_size=36,
        ).shift(UP)
        ft_formula2[3].set_color(RED)
        ft_formula2[6].set_color(RED)
        ft_formula3 = MathTex(
            r"f(t)",
            r"=",
            r"\sum_{n=0}^{\infty}",
            r"a_n",
            r"\left[",
            r"\frac{e^{j n \omega t} + e^{-j n \omega t}}{2}",
            r"\right]",
            r"+",
            r"b_n",
            r"\sin(n \omega t)",
            font_size=36,
        ).shift(UP)
        ft_formula3[3].set_color(RED)
        ft_formula3[8].set_color(RED)
        ft_formula4 = MathTex(
            r"f(t)",
            r"=",
            r"\sum_{n=0}^{\infty}",
            r"a_n",
            r"\left[",
            r"\frac{e^{j n \omega t} + e^{-j n \omega t}}{2}",
            r"\right]",
            r"+",
            r"b_n",
            r"\left[",
            r"\frac{e^{j n \omega t} - e^{-j n \omega t}}{2j}",
            r"\right]",
            font_size=36,
        ).shift(UP)
        ft_formula4[3].set_color(RED)
        ft_formula4[8].set_color(RED)
        ft_formula5 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"{",  # 3
            r"a_n",  # 4
            r"\over",  # 5
            r"2}",  # 6
            r"e^{j n \omega t}",  # 7
            r"+",  # 8
            r"{",  # 9
            r"a_n",  # 10
            r"\over",  # 11
            r"2}",  # 12
            r"e^{-j n \omega t}",  # 13
            r"+",  # 14
            r"{",  # 15
            r"b_n",  # 16
            r"\over",  # 17
            r"2j}",  # 18
            r"e^{j n \omega t}",  # 19
            r"-",  # 20
            r"{",  # 21
            r"b_n",  # 22
            r"\over",  # 23
            r"2j}",  # 24
            r"e^{-j n \omega t}",  # 25
            font_size=36,
        ).next_to(ft_formula4, DOWN, buff=0.5)
        ft_formula5[4].set_color(RED)
        ft_formula5[10].set_color(RED)
        ft_formula5[16].set_color(RED)
        ft_formula5[22].set_color(RED)

        ft_formula6 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"\over",  # 6
            r"2}",  # 7
            r"+",  # 8
            r"{",  # 9
            r"b_n",  # 10
            r"\over",  # 11
            r"2j}",  # 12
            r"\right]",  # 13
            r"e^{j n \omega t}",  # 14
            r"+",
            r"{",  # 15
            r"a_n",  # 17
            r"\over",  # 18
            r"2}",  # 19
            r"e^{-j n \omega t}",  # 20
            r"-",  # 21
            r"{",  # 22
            r"b_n",  # 23
            r"\over",  # 24
            r"2j}",  # 25
            r"e^{-j n \omega t}",  # 26
            font_size=36,
        ).next_to(ft_formula4, DOWN, buff=0.5)

        ft_formula6[5].set_color(RED)
        ft_formula6[10].set_color(RED)
        ft_formula6[17].set_color(RED)
        ft_formula6[23].set_color(RED)

        ft_formula7 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"\over",  # 6
            r"2}",  # 7
            r"+",  # 8
            r"{",  # 9
            r"b_n",  # 10
            r"\over",  # 11
            r"2j}",  # 12
            r"\right]",  # 13
            r"e^{j n \omega t}",  # 14
            r"+",  # 15
            r"\left[",  # 16
            r"{",  # 17 (added missing {)
            r"a_n",  # 18
            r"\over",  # 19
            r"2}",  # 20
            r"-",  # 21
            r"{",  # 22
            r"b_n",  # 23
            r"\over",  # 24
            r"2j}",  # 25
            r"\right]",  # 26 (added missing \right])
            r"e^{-j n \omega t}",  # 27
            font_size=36,
        ).next_to(ft_formula4, DOWN, buff=0.5)

        ft_formula7[5].set_color(RED)
        ft_formula7[10].set_color(RED)
        ft_formula7[18].set_color(RED)
        ft_formula7[23].set_color(RED)

        ft_formula8 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"\over",  # 6
            r"2}",  # 7
            r"+",  # 8
            r"{",  # 9
            r"b_n",  # 10
            r"j",
            r"\over",  # 11
            r"2 j^2}",  # 12
            r"\right]",  # 13
            r"e^{j n \omega t}",  # 14
            r"+",  # 15
            r"\left[",  # 16
            r"{",  # 17 (added missing {)
            r"a_n",  # 18
            r"\over",  # 19
            r"2}",  # 20
            r"-",  # 21
            r"{",  # 22
            r"b_n",  # 23
            r"\over",  # 24
            r"2j}",  # 25
            r"\right]",  # 26 (added missing \right])
            r"e^{-j n \omega t}",  # 27
            font_size=36,
        ).next_to(ft_formula4, DOWN, buff=0.5)

        ft_formula8[5].set_color(RED)
        ft_formula8[10].set_color(RED)
        ft_formula8[19].set_color(RED)
        ft_formula8[24].set_color(RED)

        ft_formula9 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"\over",  # 6
            r"2}",  # 7
            r"-",  # 8
            r"{",  # 9
            r"b_n",  # 10
            r"j",
            r"\over",  # 11
            r"2}",  # 12
            r"\right]",  # 13
            r"e^{j n \omega t}",  # 14
            r"+",  # 15
            r"\left[",  # 16
            r"{",  # 17 (added missing {)
            r"a_n",  # 18
            r"\over",  # 19
            r"2}",  # 20
            r"-",  # 21
            r"{",  # 22
            r"b_n",  # 23
            r"\over",  # 24
            r"2j}",  # 25
            r"\right]",  # 26 (added missing \right])
            r"e^{-j n \omega t}",  # 27
            font_size=36,
        ).next_to(ft_formula4, DOWN, buff=0.5)

        ft_formula9[5].set_color(RED)
        ft_formula9[10].set_color(RED)
        ft_formula9[19].set_color(RED)
        ft_formula9[24].set_color(RED)

        ft_formula10 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"\over",  # 6
            r"2}",  # 7
            r"-",  # 8
            r"{",  # 9
            r"b_n",  # 10
            r"j",
            r"\over",  # 11
            r"2}",  # 12
            r"\right]",  # 13
            r"e^{j n \omega t}",  # 14
            r"+",  # 15
            r"\left[",  # 16
            r"{",  # 17 (added missing {)
            r"a_n",  # 18
            r"\over",  # 19
            r"2}",  # 20
            r"+",  # 21
            r"{",  # 22
            r"b_n",  # 23
            r"j",
            r"\over",  # 24
            r"2}",  # 25
            r"\right]",  # 26 (added missing \right])
            r"e^{-j n \omega t}",  # 27
            font_size=36,
        ).next_to(ft_formula4, DOWN, buff=0.5)

        ft_formula10[5].set_color(RED)
        ft_formula10[10].set_color(RED)
        ft_formula10[19].set_color(RED)
        ft_formula10[24].set_color(RED)

        ft_formula11 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"-",  # 6
            r"b_n",  # 7
            r"j",  # 8
            r"\over",  # 9
            r"2}",  # 10
            r"\right]",  # 11
            r"e^{j n \omega t}",  # 12
            r"+",  # 13
            r"\left[",  # 14
            r"{",  # 15
            r"a_n",  # 16
            r"+",  # 17
            r"b_n",  # 18
            r"j",  # 19
            r"\over",  # 20
            r"2}",  # 21 (added missing "2}")
            r"\right]",  # 22
            r"e^{-j n \omega t}",  # 23
            font_size=36,
        ).next_to(ft_formula4, DOWN, buff=0.5)

        ft_formula11[5].set_color(RED)
        ft_formula11[7].set_color(RED)
        ft_formula11[16].set_color(RED)
        ft_formula11[18].set_color(RED)

        ft_formula12 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"-",  # 6
            r"b_n",  # 7
            r"j",  # 8
            r"\over",  # 9
            r"2}",  # 10
            r"\right]",  # 11
            r"e^{j n \omega t}",  # 12
            r"+",  # 13
            r"\sum_{n=0}^{\infty}",  # 14
            r"\left[",  # 15
            r"{",  # 16
            r"a_n",  # 17
            r"+",  # 18
            r"b_n",  # 19
            r"j",  # 20
            r"\over",  # 21
            r"2}",  # 22
            r"\right]",  # 23
            r"e^{-j n \omega t}",  # 24
            font_size=36,
        )

        ft_formula12[5].set_color(RED)  # First a_n
        ft_formula12[7].set_color(RED)  # First b_n
        ft_formula12[17].set_color(RED)  # Second a_n
        ft_formula12[19].set_color(RED)  # Second b_n
        neg_n = MathTex(r"n", r":=", r"-n", color=ORANGE, font_size=36)

        ft_formula13 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"-",  # 6
            r"b_n",  # 7
            r"j",  # 8
            r"\over",  # 9
            r"2}",  # 10
            r"\right]",  # 11
            r"e^{j n \omega t}",  # 12
            r"+",  # 13
            r"\sum_{n=0}^{\infty}",  # 14
            r"\left[",  # 15
            r"{",  # 16
            r"a_{(-n)}",  # 17
            r"+",  # 18
            r"b_{(-n)}",  # 19
            r"j",  # 20
            r"\over",  # 21
            r"2}",  # 22
            r"\right]",  # 23
            r"e^{-j (-n) \omega t}",  # 24
            font_size=36,
        )

        ft_formula13[5].set_color(RED)  # First a_n
        ft_formula13[7].set_color(RED)  # First b_n
        ft_formula13[17].set_color(RED)  # Second a_n
        ft_formula13[19].set_color(RED)  # Second b_n

        ft_formula14 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"-",  # 6
            r"b_n",  # 7
            r"j",  # 8
            r"\over",  # 9
            r"2}",  # 10
            r"\right]",  # 11
            r"e^{j n \omega t}",  # 12
            r"+",  # 13
            r"\sum_{-n=0}^{-n=\infty}",  # 14
            r"\left[",  # 15
            r"{",  # 16
            r"a_{(-n)}",  # 17
            r"+",  # 18
            r"b_{(-n)}",  # 19
            r"j",  # 20
            r"\over",  # 21
            r"2}",  # 22
            r"\right]",  # 23
            r"e^{-j (-n) \omega t}",  # 24
            font_size=36,
        )

        ft_formula14[5].set_color(RED)  # First a_n
        ft_formula14[7].set_color(RED)  # First b_n
        ft_formula14[17].set_color(RED)  # Second a_n
        ft_formula14[19].set_color(RED)  # Second b_n

        ft_formula15 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"-",  # 6
            r"b_n",  # 7
            r"j",  # 8
            r"\over",  # 9
            r"2}",  # 10
            r"\right]",  # 11
            r"e^{j n \omega t}",  # 12
            r"+",  # 13
            r"\sum_{-n=0}^{-n=\infty}",  # 14
            r"\left[",  # 15
            r"{",  # 16
            r"a_{-n}",  # 17
            r"+",  # 18
            r"b_{-n}",  # 19
            r"j",  # 20
            r"\over",  # 21
            r"2}",  # 22
            r"\right]",  # 23
            r"e^{j n\omega t}",  # 24
            font_size=36,
        )

        ft_formula15[5].set_color(RED)  # First a_n
        ft_formula15[7].set_color(RED)  # First b_n
        ft_formula15[17].set_color(RED)  # Second a_n
        ft_formula15[19].set_color(RED)  # Second b_n

        ft_formula16 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"\left[",  # 3
            r"{",  # 4
            r"a_n",  # 5
            r"-",  # 6
            r"b_n",  # 7
            r"j",  # 8
            r"\over",  # 9
            r"2}",  # 10
            r"\right]",  # 11
            r"e^{j n \omega t}",  # 12
            r"+",  # 13
            r"\sum_{-\infty}^{n=0}",  # 14
            r"\left[",  # 15
            r"{",  # 16
            r"a_{-n}",  # 17
            r"+",  # 18
            r"b_{-n}",  # 19
            r"j",  # 20
            r"\over",  # 21
            r"2}",  # 22
            r"\right]",  # 23
            r"e^{j n\omega t}",  # 24
            font_size=36,
        )

        ft_formula16[5].set_color(RED)  # First a_n
        ft_formula16[7].set_color(RED)  # First b_n
        ft_formula16[17].set_color(RED)  # Second a_n
        ft_formula16[19].set_color(RED)  # Second b_n
        c_n = MathTex(
            r"C_n",
            r"=",
            r"\begin{cases} \dfrac{a_n - b_n j}{2} & n \geq 0 \\ \dfrac{a_{-n} + b_{-n} j}{2} & n \leq 0 \end{cases}",
            font_size=36,
        )
        c_n[0].set_color(GREEN)
        c_n_1 = MathTex(
            r"C_n",
            r"=",
            r"\begin{cases} \dfrac{a_n - b_n j}{2} & n > 0 \\ \dfrac{a_{-n} + b_{-n} j}{2} & n < 0 \\ \quad \quad a_0 & n = 0 \end{cases}",
            font_size=36,
        )
        c_n_1[0].set_color(GREEN)
        c_n_p1 = MathTex(r"C_n", color=GREEN, font_size=36)
        c_n_p2 = MathTex(r"C_n", color=GREEN, font_size=36)

        ft_formula17 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{n=0}^{\infty}",  # 2
            r"C_n",
            r"e^{j n \omega t}",  # 12
            r"+",  # 13
            r"\sum_{-\infty}^{n=0}",  # 14
            r"C_n",
            r"e^{j n\omega t}",  # 24
            font_size=36,
        )
        ft_formula17[3].set_color(GREEN)  # First C_n
        ft_formula17[7].set_color(GREEN)  # First C_n

        ft_formula18 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{- \infty}^{\infty}",  # 2
            r"C_n",
            r"e^{j n \omega t}",  # 12
            font_size=36,
        )
        ft_formula18[3].set_color(GREEN)  # First C_n

        ## Finding C_n
        cc_n = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"\sum_{- \infty}^{\infty}",  # 2
            r"C_n",
            r"e^{j n \omega t}",  # 12
            font_size=36,
        )
        ## ------------------- animation part -------------------

        self.add(cos_theta, sin_theta)
        # self.play(Write(cos_theta), Write(sin_theta))
        # self.wait()
        # self.play(Write(ft_formula))
        # self.wait()
        # self.play(ReplacementTransform(ft_formula, ft_formula2))
        # self.wait()
        # self.play(TransformMatchingTex(ft_formula2, ft_formula3))
        # self.wait()
        # self.play(TransformMatchingTex(ft_formula3, ft_formula4))
        # self.wait()
        # self.play(TransformFromCopy(ft_formula4, ft_formula5))
        # self.wait()
        # brace1 = Brace(ft_formula5[7], DOWN, buff=0.1)
        # brace2 = Brace(ft_formula5[19], DOWN, buff=0.1)
        # self.play(Create(brace1), Create(brace2))
        # self.wait()
        # self.play(
        #     FadeOut(brace1, brace2), TransformMatchingShapes(ft_formula5, ft_formula6)
        # )
        # self.wait()
        # self.play(TransformMatchingTex(ft_formula6, ft_formula7))
        # self.wait()
        # self.play(TransformMatchingTex(ft_formula7, ft_formula8))
        # self.wait()
        # self.play(TransformMatchingTex(ft_formula8, ft_formula9))
        # self.wait()
        # self.play(TransformMatchingTex(ft_formula9, ft_formula10))
        # self.wait()
        # self.play(TransformMatchingTex(ft_formula10, ft_formula11))
        # self.wait()
        # self.play(FadeOut(ft_formula4), ft_formula11.animate.shift(UP))
        # self.wait()
        # ft_formula12.move_to(ft_formula11)
        # self.play(TransformMatchingTex(ft_formula11, ft_formula12))
        # self.wait()
        # neg_n.next_to(VGroup(ft_formula12[14:-1]), DOWN, buff=0.5)
        # self.play(Write(neg_n))
        # self.wait()
        # ft_formula13.move_to(ft_formula11)
        # self.play(TransformMatchingTex(ft_formula12, ft_formula13))
        # self.wait()
        # ft_formula14.move_to(ft_formula11)
        # self.play(TransformMatchingTex(ft_formula13, ft_formula14), FadeOut(neg_n))
        # self.wait()
        # ft_formula15.move_to(ft_formula11)
        # self.play(TransformMatchingTex(ft_formula14, ft_formula15))
        # self.wait()
        # ft_formula16.move_to(ft_formula11)
        # self.play(TransformMatchingTex(ft_formula15, ft_formula16))
        # self.wait()
        # brace1 = Brace(ft_formula16[12], DOWN, buff=0.1)
        # brace2 = Brace(ft_formula16[24], DOWN, buff=0.1)
        # self.play(Create(brace1), Create(brace2))
        # self.wait()
        # rec1 = SurroundingRectangle(
        #     VGroup(ft_formula16[5:11]), color=ORANGE, stroke_width=3, buff=0.1
        # )
        # rec2 = SurroundingRectangle(
        #     VGroup(ft_formula16[17:23]), color=ORANGE, stroke_width=3, buff=0.1
        # )
        # self.play(Create(rec1), Create(rec2))
        # self.wait()
        # c_n.next_to(ft_formula16, DOWN, buff=0.5)
        # self.play(Write(c_n))
        # self.wait()
        # self.play(FadeOut(rec1, rec2))
        # c_n_1.move_to(c_n)
        # self.play(TransformMatchingShapes(c_n, c_n_1))
        # self.wait()
        # vg1_center = VGroup(ft_formula16[5:11])
        # vg2_center = VGroup(ft_formula16[17:23])
        # vg1 = VGroup(ft_formula16[3:12])
        # vg2 = VGroup(ft_formula16[15:24])
        # brc1 = Brace(vg1, UP, color=ORANGE, buff=0.1)
        # brc2 = Brace(vg2, UP, color=ORANGE, buff=0.1)
        # self.play(Create(brc1), Create(brc2))
        # self.wait()
        # c_n_p1.move_to(vg1_center.get_center())
        # c_n_p2.move_to(vg2_center.get_center())
        # self.play(
        #     ReplacementTransform(VGroup(ft_formula16[3:12]), c_n_p1), FadeOut(brc1)
        # )
        # self.wait()
        # self.play(
        #     ReplacementTransform(VGroup(ft_formula16[15:24]), c_n_p2), FadeOut(brc2)
        # )
        # self.wait()
        # ft_formula17.move_to(ft_formula16)
        # self.play(
        #     FadeOut(
        #         brace1,
        #         brace2,
        #         c_n_p1,
        #         c_n_p2,
        #     ),
        #     TransformMatchingTex(ft_formula16, ft_formula17),
        # )
        # self.wait()
        # self.play(
        #     ft_formula17.animate.shift(3 * LEFT),
        #     c_n_1.animate.next_to(ft_formula17.get_center(), RIGHT, buff=1),
        # )
        # self.wait()
        # ft_formula18.next_to(ft_formula17, DOWN, buff=0.5)
        # self.play(Write(ft_formula18[0]), Write(ft_formula18[1]))
        # self.wait()
        # rec1 = SurroundingRectangle(
        #     ft_formula17[2], color=ORANGE, stroke_width=3, buff=0.1
        # )
        # rec2 = SurroundingRectangle(
        #     ft_formula17[6], color=ORANGE, stroke_width=3, buff=0.1
        # )
        # self.play(Create(rec1), Create(rec2))
        # self.wait()
        # self.play(Write(ft_formula18[2]), FadeOut(rec1, rec2))
        # self.wait()
        # self.play(Write(ft_formula18[3]), Write(ft_formula18[4]))
        # self.wait()
        self.play(ft_formula18.animate.move_to(ORIGIN), FadeOut(c_n_1, ft_formula17))
        self.wait()
        ft_formula.move_to(ORIGIN)
        ft_formula.to_edge(LEFT, buff=1.5)
        self.play(
            ft_formula18.animate.next_to(ft_formula, RIGHT, buff=2), FadeIn(ft_formula)
        )
        self.wait()
        arw = Arrow(
            start=ft_formula.get_right(),
            end=ft_formula18.get_left(),
            color=BLUE,
            buff=0.2,
        )
        rec1 = SurroundingRectangle(cos_theta, color=ORANGE, stroke_width=3, buff=0.1)
        rec2 = SurroundingRectangle(sin_theta, color=ORANGE, stroke_width=3, buff=0.1)

        self.play(Create(arw))
        self.wait()
        self.play(Create(rec1), Create(rec2))
        self.wait()
        self.play(
            FadeOut(arw, ft_formula, rec1, rec2, cos_theta, sin_theta),
            ft_formula18.animate.move_to(ORIGIN),
        )
        self.wait()
        rec = SurroundingRectangle(
            ft_formula18[3], color=ORANGE, stroke_width=3, buff=0.1
        )
        self.play(Create(rec))
        self.wait()
        self.play(FadeOut(rec))
        self.wait()

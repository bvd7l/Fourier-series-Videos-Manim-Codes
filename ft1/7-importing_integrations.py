from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class Texting(Scene):
    def construct(self):

        # fs_formula = MathTex("f(x)=\sum_{n=0}^{\infty}", font_size=36).to_edge(
        #     UP, buff=0.5
        # )
        # fs_formula1 = MathTex(
        #     "f(x)=\sum_{n=0}^{\infty}cos()+sin()", font_size=36
        # ).next_to(fs_formula, DOWN, buff=0.5)

        # center_fs_formula = MathTex("f(x)=\sum_{n=0}^{\infty}", font_size=36)
        # center_fs_formula1 = MathTex(
        #     "f(x)=\sum_{n=0}^{\infty}cos()+sin()", font_size=36
        # )
        # # formula_center = MathTex("f(x)=\int_{a}^{b}f(x)dx")
        # self.play(Write(fs_formula), Write(center_fs_formula))
        # self.wait()
        # self.play(
        #     ReplacementTransform(fs_formula, fs_formula1),
        #     ReplacementTransform(center_fs_formula, center_fs_formula1),
        # )
        # self.wait()
        # formula = MathTex(
        #     "\\int_0^\\infty",
        #     "e^{-x^2}\\,",
        #     "dx",
        #     "=",
        #     "\\frac{\\sqrt{\\pi}}{2}",
        #     font_size=36,
        # )
        # formula2 = MathTex(
        #     "\\int_0^\\infty",
        #     "e^{-x^2}\\;",
        #     "dx",
        #     "=",
        #     "\\frac{\\sqrt{\\pi}}{2}",
        #     font_size=36,
        # ).next_to(formula, DOWN, buff=1)
        # self.play(Write(formula))
        # self.wait()

        # new_int = MathTex("\\sum_{x=0}^{\\infty}", font_size=36)
        # new_int.move_to(formula[0])
        # self.play(Transform(formula[0], new_int))
        # self.wait()

        # self.play(FadeOut(formula[2]))
        # new_tex = MathTex(
        #     "\\sum_{x=0}^{\\infty}",
        #     "e^{-x^2}",
        #     "=",
        #     "\\frac{\\sqrt{\\pi}}{2}",
        #     font_size=36,
        # )

        # # Position the new formula at the same location
        # new_tex.move_to(formula.get_center())

        # # Transform to the new properly spaced formula
        # self.play(
        #     Transform(VGroup(formula[0], formula[1], formula[3], formula[4]), new_tex)
        # )
        # self.wait(2)
        ## ------------ BEGIN OF FOURIER SERIES LOW ------------

        title = ar_text("سلسلة فورييه:", 30).to_corner(UP + RIGHT, buff=0.7)
        self.play(Write(title, reverse=True))
        self.add(title)
        self.wait()
        fs_formula = MathTex(
            "f(t)",  # 0
            "=",  # 1
            "\\sum_{n=0}^{\\infty}",  # 2
            "a_n",  # 3
            "cos(",  # 4
            "n",  # 5
            "\\omega t",  # 6
            ")",  # 7
            "+",  # 8
            "b_n",  # 9
            "sin(",  # 10
            "n",  # 11
            "\\omega t",  # 12
            ")",  # 13
            font_size=30,
        )
        fs_formula[3].set_color(RED_C)
        fs_formula[9].set_color(RED_C)
        self.play(Write(fs_formula[0]), Write(fs_formula[1]))
        self.wait()
        self.play(Write(fs_formula[2]))
        self.wait()
        self.play(
            LaggedStart(
                Write(fs_formula[4]),
                Write(fs_formula[7]),
                Write(fs_formula[8]),
                Write(fs_formula[10]),
                Write(fs_formula[13]),
                lag_ratio=0.1,
            )
        )

        self.play(
            LaggedStart(
                Write(fs_formula[6]),
                Write(fs_formula[12]),
                lag_ratio=0.1,
            )
        )
        self.wait()

        self.play(
            LaggedStart(
                Write(fs_formula[5]),
                Write(fs_formula[11]),
                lag_ratio=0.1,
            )
        )
        self.wait()
        self.play(
            LaggedStart(
                Write(fs_formula[3]),
                Write(fs_formula[9]),
                lag_ratio=0.1,
            )
        )
        self.wait()

        self.play(fs_formula.animate.shift(1.5 * UP))

        # self.play(Write(fs_formula))
        self.wait()

        fs_formula_modified = MathTex(
            "f(t)",  # 0
            "=",  # 1
            "a_0",  # 2
            "+",  # 3
            "\\sum_{n=1}^{\\infty}",  # 4
            "a_n",  # 5
            "cos(",  # 6
            "n",  # 7
            "\\omega t",  # 8
            ")",  # 9
            "+",  # 10
            "b_n",  # 11
            "sin(",  # 12
            "n",  # 13
            "\\omega t",  # 14
            ")",  # 15
            font_size=30,
        )
        fs_formula_modified[2].set_color(RED)
        fs_formula_modified[5].set_color(RED)
        fs_formula_modified[11].set_color(RED)
        fs_formula_modified.next_to(fs_formula, DOWN, buff=0.5)
        self.play(TransformFromCopy(fs_formula, fs_formula_modified))
        self.wait()

        a_0 = MathTex("a_0", "=", "\\;?", font_size=30)
        a_n = MathTex("a_n", "=", "\\;?", font_size=30)
        b_n = MathTex("b_n", "=", "\\;?", font_size=30)
        a_0[0].set_color(RED)
        a_n[0].set_color(RED)
        b_n[0].set_color(RED)

        question_group = VGroup(a_0, a_n, b_n)
        question_group.arrange(RIGHT, buff=0.8)
        question_group.next_to(fs_formula_modified, DOWN, buff=0.5)
        self.play(LaggedStart(Write(question_group), lag_ratio=0.1))
        self.wait()

        self.play(FadeOut(fs_formula, fs_formula_modified, question_group, title))
        self.wait()

        # ------------ END OF FOURIER SERIES LOW ------------

        # ------------ BEGIN OF OF INTEGRATIONS ------------

        title2 = ar_text("تكاملات مهمة:", 30).to_corner(UP + RIGHT, buff=0.7)
        self.play(Write(title2, reverse=True))
        self.add(title2)
        self.wait()

        integral = (
            MathTex(
                r"\int_{0}^{2\pi} \sin(nt)\,\sin(mt)\,dt",
                # "=",
                # r"\begin{cases}"
                # r"\;\pi & \text{; } m = n \neq 0 \\"
                # r"\;0   & \text{; } m \neq n"
                # r"\end{cases}",
                font_size=30,
            )
            .to_corner(LEFT + UP, buff=0.7)
            .shift(DOWN * 0.5)
        )

        self.play(Write(integral))
        self.wait()

        self.wait()
        Case1 = MathTex("Case \\: 1:", " n\\ne m", font_size=30).next_to(
            integral, RIGHT, buff=0.5
        )
        Case1[1].set_color(ORANGE)
        self.play(Write(Case1))
        self.wait()
        integral1 = MathTex(
            r"\int_{0}^{2\pi} \sin(nt)\,\sin(mt)",  # 0
            r"=",  # 1
            r"\int_{0}^{2\pi}",  # 2
            r"\frac{1}{2}\left[",  # 3
            r"\cos((n-m)t)",  # 4
            r"-",  # 5
            r"\cos((n+m)t)",  # 6
            r"\right]",  # 7
            font_size=30,
        ).next_to(integral, DOWN, buff=0.5, aligned_edge=LEFT)
        integral1[4].set_color(PINK)
        integral1[6].set_color(YELLOW)
        self.play(TransformFromCopy(integral, integral1), run_time=2)
        self.wait()

        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-2, 2],
            x_length=7,
            y_length=4,
            tips=False,
            axis_config={"color": BLUE},
        ).to_edge(DOWN, buff=0.5)
        x_labels = VGroup()
        pi_values = [
            0,
            PI / 2,
            PI,
            3 * PI / 2,
            2 * PI,
            5 * PI / 2,
            3 * PI,
            7 * PI / 2,
            4 * PI,
        ]
        pi_labels = [
            "0",
            "\\frac{\\pi}{2}",
            "\\pi",
            "\\frac{3\\pi}{2}",
            "2\\pi",
            "\\frac{5\\pi}{2}",
            "3\\pi",
            "\\frac{7\\pi}{2}",
            "4\\pi",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 2 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.5)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.5)
                    )

            x_labels.add(x_label)

        axes_graph = VGroup(axes, x_labels)
        self.play(TransformFromCopy(integral1[4], axes_graph), run_time=2)
        self.wait(0.5)

        n, m = 1, 2

        # Create the cosine functions from the identity
        cos_diff = axes.plot(lambda x: np.cos((n - m) * x), color=PINK, stroke_width=3)
        cos_sum = axes.plot(lambda x: np.cos((n + m) * x), color=YELLOW, stroke_width=3)

        self.play(Create(cos_diff), run_time=1)
        self.wait()

        positive_areas_diff = VGroup()
        negative_areas_diff = VGroup()

        # Cos(-x) = Cos(x) has period 2π - positive in [0,π/2]∪[3π/2,2π], negative in [π/2,3π/2]
        positive_ranges = [(0, PI / 2), (3 * PI / 2, 2 * PI)]
        negative_ranges = [(PI / 2, 3 * PI / 2)]

        for start, end in positive_ranges:
            area = axes.get_area(cos_diff, [start, end], color=GREEN, opacity=0.3)
            positive_areas_diff.add(area)

        for start, end in negative_ranges:
            area = axes.get_area(cos_diff, [start, end], color=RED, opacity=0.3)
            negative_areas_diff.add(area)

        self.play(Create(positive_areas_diff), Create(negative_areas_diff), run_time=2)
        self.wait()
        self.play(
            positive_areas_diff[0].animate.shift((PI + 0.35) * RIGHT),
            positive_areas_diff[1].animate.shift((PI + 0.35) * LEFT),
            run_time=1,
        )
        self.wait()

        ans1 = MathTex("0", font_size=30, color=PINK).move_to(integral1[4])
        self.play(ReplacementTransform(integral1[4], ans1))

        self.wait()

        self.play(
            FadeOut(
                axes_graph,
                positive_areas_diff,
                negative_areas_diff,
                cos_diff,
            ),
            run_time=2,
        )
        self.wait()

        self.play(TransformFromCopy(integral1[6], axes_graph), run_time=2)
        self.wait()
        self.play(Create(cos_sum), run_time=2)
        self.wait()

        positive_areas_cos3 = VGroup()
        negative_areas_cos3 = VGroup()

        positive_ranges_cos3 = [
            (0, PI / 6),
            (PI / 2, 5 * PI / 6),
            (7 * PI / 6, 3 * PI / 2),
            (11 * PI / 6, 2 * PI),
        ]
        negative_ranges_cos3 = [
            (PI / 6, PI / 2),
            (5 * PI / 6, 7 * PI / 6),
            (3 * PI / 2, 11 * PI / 6),
        ]

        for start, end in positive_ranges_cos3:
            area = axes.get_area(cos_sum, [start, end], color=GREEN, opacity=0.3)
            positive_areas_cos3.add(area)

        for start, end in negative_ranges_cos3:
            area = axes.get_area(cos_sum, [start, end], color=RED, opacity=0.3)
            negative_areas_cos3.add(area)

        self.play(
            Create(positive_areas_cos3),
            Create(negative_areas_cos3),
            run_time=1.5,
            rate_func=rate_functions.double_smooth,
        )
        self.wait()

        ans2 = MathTex("0", font_size=30, color=YELLOW).move_to(integral1[6])
        self.play(ReplacementTransform(integral1[6], ans2))

        self.wait()

        self.play(
            FadeOut(
                axes_graph,
                positive_areas_cos3,
                negative_areas_cos3,
                cos_sum,
            ),
            run_time=2,
        )
        self.wait()
        ans = MathTex("0", font_size=30).next_to(
            integral1[1], RIGHT, buff=0.2, aligned_edge=RIGHT
        )
        self.play(Transform(integral1[2:], ans))
        self.wait()

        integral2 = MathTex(
            r"\int_{0}^{2\pi} \sin(nt)\,\sin(mt)\,dt",
            font_size=30,
        ).next_to(integral1, DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(Write(integral2))
        self.wait()

        self.wait()
        Case2 = MathTex("Case \\: 2:", " n=m", font_size=30).next_to(
            integral2, RIGHT, buff=0.5
        )
        Case2[1].set_color(ORANGE)
        self.play(Write(Case2))
        self.wait()
        integral3 = MathTex(
            r"\int_{0}^{2\pi} \sin(nt)\,\sin(nt)",  # 0
            r"=",  # 1
            r"\int_{0}^{2\pi}",  # 2
            r"\sin^2 (nt)",  # 3
            r"=",  # 4
            r"\int_{0}^{2\pi} \frac{1 - \cos(4nt)}{2} \, dt",
            font_size=30,
        ).next_to(integral2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(TransformFromCopy(integral2, integral3), run_time=2)
        self.wait()
        split_int1 = (
            MathTex(
                r"\frac{1}{2} \int_{0}^{2\pi} 1 \, dt",  # 0
                r"-",  # 1
                r"\frac{1}{2} \int_{0}^{2\pi} \cos(4nt) \, dt",  # 2
                font_size=30,
            )
            .move_to(integral3)
            .next_to(integral3[4], RIGHT, buff=0.15)
        )

        self.play(ReplacementTransform(integral3[5], split_int1))
        # self.remove(split_int1)

        self.wait()
        split_int12 = (
            MathTex(r"0", font_size=30)
            .move_to(split_int1[2])
            .next_to(split_int1[1], RIGHT, buff=0.15)
        )
        final_expression = (
            MathTex(r"\frac{1}{2} \int_{0}^{2\pi} 1 \, dt", font_size=30)
            .move_to(split_int1)
            .next_to(integral3[4], RIGHT, buff=0.15)
        )
        self.play(ReplacementTransform(split_int1[-1], split_int12))
        self.wait()
        self.play(TransformMatchingShapes(split_int1, final_expression))
        self.wait()
        first_term = (
            MathTex(
                r"\frac{1}{2} \left[ t \right]_{0}^{2\pi} = \frac{1}{2} (2\pi) = \pi",
                font_size=30,
            )
            .move_to(split_int1)
            .next_to(integral3[4], RIGHT, buff=0.15)
        )
        self.play(ReplacementTransform(final_expression, first_term))
        self.wait()

        split_int13 = (
            MathTex(r"\pi", font_size=30)
            .move_to(split_int1)
            .next_to(integral3[4], RIGHT, buff=0.15)
        )
        self.play(ReplacementTransform(first_term, split_int13))
        self.wait()
        split_int13.move_to(split_int1).next_to(integral3[1], RIGHT, buff=0.15)
        left_over = VGroup(integral3[4], integral3[3], integral3[2])
        self.play(ReplacementTransform(left_over, split_int13))
        self.wait()

        group_res = VGroup(
            integral, Case1, integral1, ans, integral2, Case2, integral3, split_int13
        )

        final_res = MathTex(
            r"\int_{0}^{2\pi}",
            r"\sin(nt)\,\sin(mt)\,dt",
            "=",
            r"\begin{cases}"
            r"\;\pi & \text{; } m = n \neq 0 \\"
            r"\;0   & \text{; } m \neq n"
            r"\end{cases}",
            font_size=40,
        ).shift(UP * 1.5)

        self.play(
            ReplacementTransform(group_res, final_res),
            run_time=1,
            rate_func=rate_functions.smooth,
        )
        self.wait()
        rec1 = SurroundingRectangle(
            final_res[0], stroke_width=3, color=YELLOW, buff=0.1
        )
        T_tex = MathTex(r"T = 2 \pi", font_size=40).next_to(final_res, DOWN, buff=0.5)
        self.play(Create(rec1))
        self.play(Write(T_tex))
        self.wait()
        self.play(FadeOut(rec1, T_tex))
        final_res1 = MathTex(
            r"\int^{T}_{0}",
            r"\sin(nt)\,\sin(mt)\,dt",
            "=",
            r"\begin{cases}"
            r"\;\dfrac{T}{2} & \text{; } m = n \neq 0 \\"
            r"\;0   & \text{; } m \neq n"
            r"\end{cases}",
            font_size=40,
        ).shift(UP * 1.5)
        self.play(TransformMatchingShapes(final_res, final_res1))
        self.wait()
        final_res2 = MathTex(
            r"\int^{T}_{0}",
            r" \cos(nt)\,\cos(mt)\,dt",
            "=",
            r"\begin{cases}"
            r"\;\dfrac{T}{2} & \text{; } m = n \neq 0 \\"
            r"\;0   & \text{; } m \neq n"
            r"\end{cases}",
            font_size=40,
        ).next_to(final_res1, DOWN, buff=0.5)
        self.play(Write(final_res2), run_time=2)
        self.wait()
        final_res3 = MathTex(
            r"\int^{T}_{0}",
            r" \sin(nt)\,\cos(mt)\,dt",
            "=",
            r"\begin{cases}"
            r"\;0 & \text{; } m = n \neq 0 \\"
            r"\;0   & \text{; } m \neq n"
            r"\end{cases}",
            font_size=40,
        ).next_to(final_res2, DOWN, buff=0.5)
        self.play(Write(final_res3), run_time=2)
        self.wait()

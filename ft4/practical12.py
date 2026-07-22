from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class Part2(Scene):
    def construct(self):
        ft_signal_def = (
            MathTex(
                r"f(t)",
                r"=",
                r"\begin{cases} \; 2 + \dfrac{2}{\pi}t & -\pi < t <0 \\[10pt] \; 2 - \dfrac{2}{\pi}t & \; 0 < t < \pi \end{cases}",
                font_size=36,
            )
            .to_edge(LEFT, buff=1)
            .shift(1 * UP)
        )
        axes = Axes(
            x_range=[-3.5, 3.5],
            y_range=[-0.5, 3],
            y_length=3.5,
            x_length=7,
            tips=True,
            axis_config={
                "stroke_width": 3,
                "tip_shape": StealthTip,
                "tip_length": 2,
                "tip_width": 2,
                "tick_size": 0.05,
            },
        )
        axes.shift(1.5 * UP + 3.5 * LEFT).scale(0.9)
        ft_signal_def.next_to(axes, RIGHT, buff=1)
        ft_signal_def.shift(0.5 * DOWN)
        ft_signal_def.to_edge(LEFT, buff=1).shift(1 * UP)

        the_question = ar_text("المطلوب:", 30)
        the_question.to_corner(UP + RIGHT, buff=0.7)
        q1 = ar_text("- ما هو الدور والتردد والتردد الزاوي؟", 24).next_to(
            the_question, DOWN, aligned_edge=RIGHT, buff=0.7
        )
        q2 = ar_text("- أوجد معادلة هذه الإشارة خلال دور واحد.", 24).next_to(
            q1, DOWN, aligned_edge=RIGHT, buff=0.5
        )
        q3 = ar_text("- أوجد سلسلة فورييه لهذه الإشارة.", 24).next_to(
            q2, DOWN, aligned_edge=RIGHT, buff=0.5
        )
        q1.shift(UP)
        q3.move_to(q1)
        eq1 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"a_0",  # 2
            r"+",  # 3
            r"\sum^{\infty}_{n=1}",  # 4
            r"a_n",  # 5
            r"\; cos(",  # 6
            r"n \omega t",  # 7
            r")",  # 8
            r"+",  # 9
            r"\sum^{\infty}_{n=1}",  # 10
            r"b_n",  # 11
            r"\; sin(",  # 12
            r"n \omega t",  # 13
            r")",  # 14
            font_size=36,
        ).next_to(ft_signal_def, RIGHT, buff=0.5)
        eq1[2].set_color(RED)
        eq1[5].set_color(RED)
        eq1[11].set_color(RED)
        brcBn = Brace(VGroup(eq1[10:15]), DOWN, buff=0.2)
        zero = MathTex(r"0", font_size=36).move_to(eq1[10:15].get_center())
        eq2 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"a_0",  # 2
            r"+",  # 3
            r"\sum^{\infty}_{n=1}",  # 4
            r"a_n",  # 5
            r"\; cos(",  # 6
            r"n \omega t",  # 7
            r")",  # 8
            font_size=36,
        ).next_to(ft_signal_def, RIGHT, buff=0.5)

        eq2[2].set_color(RED)
        eq2[5].set_color(RED)
        omega = MathTex(r"\omega", r"=", r"1", color=ORANGE, font_size=36).next_to(
            eq2, RIGHT, buff=1
        )
        eq3 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"a_0",  # 2
            r"+",  # 3
            r"\sum^{\infty}_{n=1}",  # 4
            r"a_n",  # 5
            r"\; cos(",  # 6
            r"n t",  # 7
            r")",  # 8
            font_size=36,
        ).next_to(ft_signal_def, RIGHT, buff=0.5)
        eq3_new_pos = eq1.get_center()
        eq3[2].set_color(RED)
        eq3[5].set_color(RED)
        a_0_1 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{T}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"f(t)",  # 5
            r"\;",  # 6
            r"dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"f(t)",  # 10
            r"\;dt",  # 11
            r"\right]",  # 12
            font_size=36,
        )
        a_0_1[0].set_color(RED)
        a_0_1[4].set_color(YELLOW)
        a_0_1[7].set_color(YELLOW)
        a_0_1[9].set_color(YELLOW)
        a_0_1[11].set_color(YELLOW)

        a_0_2 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{2\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"f(t)",  # 5
            r"\;",  # 6
            r"dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"f(t)",  # 10
            r"\;dt",  # 11
            r"\right]",  # 12
            font_size=36,
        )
        a_0_2[0].set_color(RED)
        a_0_2[4].set_color(YELLOW)
        a_0_2[7].set_color(YELLOW)
        a_0_2[9].set_color(YELLOW)
        a_0_2[11].set_color(YELLOW)

        a_0_3 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{2\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"(2 + \dfrac{2}{\pi}t)",  # 5
            r"\;",  # 6
            r"dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"(2 - \dfrac{2}{\pi}t)",  # 10
            r"\;dt",  # 11
            r"\right]",  # 12
            font_size=36,
        )
        a_0_3[0].set_color(RED)
        a_0_3[4].set_color(YELLOW)
        a_0_3[7].set_color(YELLOW)
        a_0_3[9].set_color(YELLOW)
        a_0_3[11].set_color(YELLOW)
        a_0_4 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{2}{2\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"(1 + \dfrac{1}{\pi}t)",  # 5
            r"\;",  # 6
            r"dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"(1 - \dfrac{1}{\pi}t)",  # 10
            r"\;dt",  # 11
            r"\right]",  # 12
            font_size=36,
        )
        a_0_4[0].set_color(RED)
        a_0_4[4].set_color(YELLOW)
        a_0_4[7].set_color(YELLOW)
        a_0_4[9].set_color(YELLOW)
        a_0_4[11].set_color(YELLOW)
        a_0_5 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"(1 + \dfrac{1}{\pi}t)",  # 5
            r"\;",  # 6
            r"dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"(1 - \dfrac{1}{\pi}t)",  # 10
            r"\;dt",  # 11
            r"\right]",  # 12
            font_size=36,
        )
        a_0_5[0].set_color(RED)
        a_0_5[4].set_color(YELLOW)
        a_0_5[7].set_color(YELLOW)
        a_0_5[9].set_color(YELLOW)
        a_0_5[11].set_color(YELLOW)
        f1_int = (
            MathTex(
                r"\int^{0}_{-\pi}",  # 4
                r"(1 + \dfrac{1}{\pi}t)",  # 5
                r"\;",  # 6
                r"dt",  # 7
                font_size=36,
            )
            .next_to(a_0_5, DOWN, buff=0.5)
            .shift(4 * LEFT)
        )
        f1_int[0].set_color(YELLOW)
        f1_int[3].set_color(YELLOW)
        f1_int2 = MathTex(
            r"=",
            r"\left[",
            r"t",
            r"+",
            r"\frac{1}{2\pi}",
            r"t^2",
            r"\right]_{-\pi}^{0}",
            font_size=36,
        ).next_to(f1_int.get_right(), RIGHT, buff=0.1)
        f1_int3 = MathTex(
            r"=",
            r"\left[",
            r"0",
            r"-",
            r"(-\pi + \frac{1}{2\pi} (-\pi)^2)" r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)

        f1_int4 = MathTex(
            r"=",
            r"\left[",
            r"\pi - \frac{1}{2\pi} \pi ^2)" r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)
        f1_int5 = MathTex(
            r"=",
            r"\left[",
            r"\pi - \frac{1}{2} \pi)" r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)

        f1_int6 = MathTex(
            r"=",
            r"\left[",
            r"\frac{1}{2} \pi",
            r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)
        f1_ans = MathTex(r"\frac{1}{2} \pi", font_size=36).move_to(
            a_0_5[4:8].get_center()
        )
        a_0_6 = MathTex(
            r"a_0",  # Index 0
            r"=",  # Index 1
            r"\frac{1}{\pi}",  # Index 2
            r"\left[",  # Index 3
            r"\frac{1}{2} \pi",  # Index 4
            r"+",  # Index 5
            r"\int^{\pi}_{0}",  # Index 6
            r"(1 - \dfrac{1}{\pi}t)",  # Index 7
            r"\;dt",  # Index 8
            r"\right]",  # Index 9
            font_size=36,
        )
        a_0_6[0].set_color(RED)
        a_0_6[6].set_color(YELLOW)
        a_0_6[8].set_color(YELLOW)

        f2_int = (
            MathTex(
                r"\int^{\pi}_{0}",  # 4
                r"(1 - \dfrac{1}{\pi}t)",  # 5
                r"\;",  # 6
                r"dt",  # 7
                font_size=36,
            )
            .next_to(a_0_5, DOWN, buff=0.5)
            .shift(4 * LEFT)
        )
        f2_int[0].set_color(YELLOW)
        f2_int[3].set_color(YELLOW)
        f2_int2 = MathTex(
            r"=",
            r"\left[",
            r"t",
            r"-",
            r"\frac{1}{2\pi}",
            r"t^2",
            r"\right]_{0}^{\pi}",
            font_size=36,
        ).next_to(f2_int.get_right(), RIGHT, buff=0.1)
        f2_int3 = MathTex(
            r"=",
            r"\left[",
            r"\pi",
            r"-",
            r"\frac{1}{2\pi} \pi ^2",
            r"-",
            r"0",
            r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)
        f2_int4 = MathTex(
            r"=",
            r"\left[",
            r"\pi",
            r"-",
            r"\frac{1}{2\pi} \pi ^ 2",
            r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)
        f2_int5 = MathTex(
            r"=",
            r"\left[",
            r"\pi",
            r"-",
            r"\frac{1}{2} \pi",
            r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)
        f2_int6 = MathTex(
            r"=",
            r"\left[",
            r"\frac{1}{2} \pi",
            r"\right]",
            font_size=36,
        ).next_to(f1_int2.get_right(), RIGHT, buff=0.1)
        f2_ans = MathTex(r"\frac{1}{2} \pi", font_size=36).move_to(
            VGroup(a_0_6[6:9]).get_center()
        )
        a_0_7 = MathTex(
            r"a_0",  # Index 0
            r"=",  # Index 1
            r"\frac{1}{\pi}",  # Index 2
            r"\left[",  # Index 3
            r"\frac{1}{2} \pi",  # Index 4
            r"+",  # Index 5
            r"\frac{1}{2} \pi",  # Index 4
            r"\right]",  # Index 9
            font_size=36,
        )
        a_0_7[0].set_color(RED)
        a_0_8 = MathTex(
            r"a_0",  # Index 0
            r"=",  # Index 1
            r"\frac{1}{\pi}",  # Index 2
            r"\left[",  # Index 3
            r"\pi",
            r"\right]",  # Index 9
            font_size=36,
        )
        a_0_8[0].set_color(RED)

        a_0_9 = MathTex(
            r"a_0",  # Index 0
            r"=",  # Index 1
            r"1",
            font_size=36,
        )
        a_0_9[0].set_color(RED)
        a_0_ans = MathTex(r"1", font_size=36)
        eq4 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"1",
            r"+",  # 3
            r"\sum^{\infty}_{n=1}",  # 4
            r"a_n",  # 5
            r"\; cos(",  # 6
            r"n t",  # 7
            r")",  # 8
            font_size=36,
        ).next_to(ft_signal_def, RIGHT, buff=0.5)
        eq4[5].set_color(RED)

        ## finding a_n

        # --------------------- animation sectioin ---------------------

        self.add(ft_signal_def)
        self.add(q3)
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(Create(brcBn))
        self.wait()
        self.play(ReplacementTransform(VGroup(eq1[10:15]), zero), FadeOut(brcBn))
        self.wait()
        self.play(TransformMatchingShapes(eq1, eq2), FadeOut(zero))
        self.wait()
        self.play(Write(omega))
        self.wait()
        self.play(TransformMatchingShapes(eq2, eq3), FadeOut(omega))
        self.play(eq3.animate.move_to(eq3_new_pos))
        self.play(Write(a_0_1))
        self.wait()
        self.play(TransformMatchingShapes(a_0_1, a_0_2))
        self.wait()
        self.play(TransformMatchingShapes(a_0_2, a_0_3))
        self.wait()
        self.play(TransformMatchingShapes(a_0_3, a_0_4))
        self.wait()
        self.play(TransformMatchingShapes(a_0_4, a_0_5))
        self.wait()
        self.play(TransformFromCopy(VGroup(a_0_5[4:8]), f1_int))
        self.wait()
        self.play(Write(f1_int2))
        self.wait()
        self.play(Write(f1_int3))
        self.wait()
        self.play(TransformMatchingShapes(f1_int3, f1_int4))
        self.wait()
        self.play(TransformMatchingShapes(f1_int4, f1_int5))
        self.wait()
        self.play(TransformMatchingShapes(f1_int5, f1_int6))
        self.wait()
        self.play(
            ReplacementTransform(VGroup(a_0_5[4:8]), f1_ans),
            FadeOut(f1_int6, f1_int, f1_int2),
        )
        self.wait()
        self.play(TransformMatchingShapes(a_0_5, a_0_6), FadeOut(f1_ans))
        self.wait()

        self.play(TransformFromCopy(VGroup(a_0_6[6:9]), f2_int))
        self.wait()
        self.play(Write(f2_int2))
        self.wait()
        self.play(Write(f2_int3))
        self.wait()
        self.play(TransformMatchingShapes(f2_int3, f2_int4))
        self.wait()
        self.play(TransformMatchingShapes(f2_int4, f2_int5))
        self.wait()
        self.play(TransformMatchingShapes(f2_int5, f2_int6))
        self.wait()
        self.play(
            ReplacementTransform(VGroup(a_0_6[6:9]), f2_ans),
            FadeOut(f2_int6, f2_int, f2_int2),
        )
        self.wait()
        self.play(TransformMatchingShapes(a_0_6, a_0_7), FadeOut(f2_ans))
        self.wait()
        self.play(TransformMatchingShapes(a_0_7, a_0_8))
        self.wait()
        self.play(TransformMatchingShapes(a_0_8, a_0_9))
        self.wait()
        eq4.move_to(eq3)
        a_0_ans.move_to(eq3[2].get_center())
        self.play(ReplacementTransform(eq3[2], a_0_ans), FadeOut(a_0_9))
        self.wait()
        self.play(TransformMatchingShapes(eq3, eq4))
        self.wait()

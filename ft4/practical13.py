from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class Part3(Scene):
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
        q4 = ar_text(
            "- أوجد أول ثلاث حدود من  السلسلة، ثم استنتج شكل التابع بناءً عليها.", 24
        ).next_to(q3, DOWN, aligned_edge=RIGHT, buff=0.5)
        q1.shift(UP)
        q4_copy = q4.copy()
        q3.move_to(q1)
        q4_copy.move_to(q3.get_center())
        q4_copy.align_to(q3, RIGHT)
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
        a_n = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2}{T}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"f(t)",  # 5
            r"\, \cos(n \omega t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"f(t)",  # 10
            r"\, \cos(n \omega t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=36,
        )
        a_n[0].set_color(RED)
        a_n[4].set_color(YELLOW)
        a_n[7].set_color(YELLOW)
        a_n[9].set_color(YELLOW)
        a_n[12].set_color(YELLOW)

        a_n_1 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2}{2\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"f(t)",  # 5
            r"\, \cos(n t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"f(t)",  # 10
            r"\, \cos(n t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=36,
        )
        a_n_1[0].set_color(RED)
        a_n_1[4].set_color(YELLOW)
        a_n_1[7].set_color(YELLOW)
        a_n_1[9].set_color(YELLOW)
        a_n_1[12].set_color(YELLOW)
        a_n_2 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{1}{\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"f(t)",  # 5
            r"\, \cos(n t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"f(t)",  # 10
            r"\, \cos(n t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=36,
        )
        a_n_2[0].set_color(RED)
        a_n_2[4].set_color(YELLOW)
        a_n_2[7].set_color(YELLOW)
        a_n_2[9].set_color(YELLOW)
        a_n_2[12].set_color(YELLOW)

        a_n_3 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{1}{\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"(2 + \dfrac{2}{\pi}t)",  # 5
            r"\, \cos(n  t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"(2 - \dfrac{2}{\pi}t)",  # 10
            r"\, \cos(n  t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=36,
        )
        a_n_3[0].set_color(RED)
        a_n_3[4].set_color(YELLOW)
        a_n_3[7].set_color(YELLOW)
        a_n_3[9].set_color(YELLOW)
        a_n_3[12].set_color(YELLOW)
        a_n_4 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2}{\pi}",  # 2
            r"\left[",  # 3
            r"\int^{0}_{-\pi}",  # 4
            r"(1 + \dfrac{1}{\pi}t)",  # 5
            r"\, \cos(n  t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int^{\pi}_{0}",  # 9
            r"(1 - \dfrac{1}{\pi}t)",  # 10
            r"\, \cos(n  t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=36,
        )
        a_n_4[0].set_color(RED)
        a_n_4[4].set_color(YELLOW)
        a_n_4[7].set_color(YELLOW)
        a_n_4[9].set_color(YELLOW)
        a_n_4[12].set_color(YELLOW)
        f1_int = VGroup(a_n_4[4:8])
        f1_int1 = (
            MathTex(
                r"\int^{0}_{-\pi}",  # 4
                r"(1 + \dfrac{1}{\pi}t)",  # 5
                r"\, \cos(n  t)",  # 6
                r"\, dt",  # 7
                font_size=36,
            )
            .next_to(a_n_4, DOWN, buff=0.5)
            .shift(4 * LEFT)
        )
        f1_int1[0].set_color(YELLOW)
        f1_int1[3].set_color(YELLOW)

        f1_int2 = (
            MathTex(
                r"=",
                r"\int^{0}_{-\pi}",  # 4
                r"\cos(n  t)",  # 6
                r"\, dt",
                r"+",
                r"\int^{0}_{-\pi}",  # 4
                r"\frac{1}{\pi}",
                r"t" r"\cos(nt)",
                r"\, dt",  # 7
                font_size=36,
            )
        ).next_to(f1_int1.get_right(), RIGHT, buff=0.1)
        f1_int2[1].set_color(YELLOW)
        f1_int2[3].set_color(YELLOW)
        f1_int2[5].set_color(YELLOW)
        f1_int2[8].set_color(YELLOW)
        cos_group = VGroup(f1_int2[1:4])
        cos_int1 = MathTex(
            r"\int^{0}_{-\pi}",  # 4
            r"\cos(n  t)",  # 6
            r"\, dt",
            font_size=36,
        )
        cos_int1[0].set_color(YELLOW)
        cos_int1[2].set_color(YELLOW)
        cos_int1.next_to(f1_int1, DOWN, aligned_edge=LEFT, buff=0.5)
        cos_int2 = MathTex(
            r"=",
            r"\left[",
            r"\frac{1}{n}",
            r"\sin(nt)",
            r"\right]_{-\pi}^{0}",
            font_size=36,
        ).next_to(cos_int1.get_right(), RIGHT, buff=0.1)
        cos_int3 = MathTex(
            r"=",
            r"\frac{1}{n}",
            r"\left[",
            r"\sin(nt)",
            r"\right]_{-\pi}^{0}",
            font_size=36,
        ).next_to(cos_int2.get_right(), RIGHT, buff=0.1)
        cos_int4 = MathTex(
            r"=",
            r"\frac{1}{n}",
            r"\left[",
            r"\sin(0)",
            r"-",
            r"\sin(-\pi)",
            r"\right]",
            font_size=36,
        ).next_to(cos_int2.get_right(), RIGHT, buff=0.1)
        cos_int5 = MathTex(
            r"=",
            r"\frac{1}{n}",
            r"\left[",
            r"0",
            r"-",
            r"0",
            r"\right]",
            font_size=36,
        ).next_to(cos_int2.get_right(), RIGHT, buff=0.1)
        cos_int6 = MathTex(
            r"=",
            r"0",
            font_size=36,
        ).next_to(cos_int2.get_right(), RIGHT, buff=0.1)
        cos_int_ans = MathTex(r"0", font_size=36)
        cos_int_ans.move_to(cos_group.get_center())
        f1_int3 = (
            MathTex(
                r"=",
                r"\int^{0}_{-\pi}",  # 4
                r"\frac{1}{\pi}",
                r"t",
                r"\cos(nt)",
                r"\, dt",  # 7
                font_size=36,
            )
        ).next_to(f1_int1.get_right(), RIGHT, buff=0.1)
        f1_int3[1].set_color(YELLOW)
        f1_int3[5].set_color(YELLOW)
        f1_int4 = (
            MathTex(
                r"=",
                r"\frac{1}{\pi}",
                r"\int^{0}_{-\pi}",  # 4
                r"t",
                r"\cos(nt)",
                r"\, dt",  # 7
                font_size=36,
            )
        ).next_to(f1_int1.get_right(), RIGHT, buff=0.1)
        f1_int4[2].set_color(YELLOW)
        f1_int4[5].set_color(YELLOW)
        integration_bp_group = VGroup(f1_int4[2:])
        integration_bp1 = MathTex(
            r"\int^{0}_{-\pi}",  # 4
            r"t",
            r"\cos(nt)",
            r"\, dt",  # 7
            font_size=36,
        ).next_to(f1_int1, DOWN, aligned_edge=LEFT, buff=0.5)
        integration_bp1[0].set_color(YELLOW)
        integration_bp1[3].set_color(YELLOW)

        u_term = MathTex(r"u", r"=", r"t", font_size=36)
        u_term[0].set_color(BLUE)
        udt_term = MathTex(r"u'", r"=", r"1", font_size=36)
        udt_term[0].set_color(BLUE)
        vdt_term = MathTex(r"v'", r"=", r"\cos(nt)", font_size=36)
        vdt_term[0].set_color(GREEN)
        v_term = MathTex(r"v", r"=", r"\frac{1}{n}", r"\sin(nt)", font_size=36)
        v_term[0].set_color(GREEN)
        tab = MobjectTable(
            [[u_term, vdt_term], [udt_term, v_term]],
            v_buff=0.3,
            h_buff=0.6,
            line_config={
                "stroke_width": 1.5,  # This controls the table line thickness
                "color": WHITE,
            },
        ).next_to(a_n_4.get_right(), DOWN, buff=1)
        tab.shift(0.1 * RIGHT)

        integration_bp2 = MathTex(
            r"=",
            r"\left[",
            r"\frac{1}{n}",
            r"t",
            r"\sin(nt)",
            r"\right]^{0}_{-\pi}",
            r"-",
            r"\int^{0}_{-\pi}",  # 4
            r"\frac{1}{n}",
            r"\sin(nt)",
            r"\, dt",  # 7
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp2[7].set_color(YELLOW)
        integration_bp2[10].set_color(YELLOW)

        integration_bp3 = MathTex(
            r"=",
            r"\left[",
            r"\frac{1}{n}",
            r"t",
            r"\sin(nt)",
            r"\right]^{0}_{-\pi}",
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        # integration_bp3[7].set_color(YELLOW)
        # integration_bp3[10].set_color(YELLOW)
        integration_bp4 = MathTex(
            r"=",
            r"\frac{1}{n}",
            r"\left[",
            r"t",
            r"\sin(nt)",
            r"\right]^{0}_{-\pi}",
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp5 = MathTex(
            r"=",
            r"\frac{1}{n}",
            r"\left[",
            r"0",
            r"\sin(n0)",
            r"-",
            r"(",
            r"(-\pi)",
            r"\sin(n(-\pi))",
            r")",
            r"\right]",
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp6 = MathTex(
            r"=",
            r"\frac{1}{n}",
            r"\left[",
            r"0" r"-",
            r"(",
            r"(-\pi)",
            r"0",
            r")",
            r"\right]",
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp7 = MathTex(
            r"=",
            r"\frac{1}{n}",
            r"\left[",
            r"0" r"-",
            r"0",
            r"\right]",
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp8 = MathTex(
            r"=",
            r"0",
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp9 = MathTex(
            r"=",
            r"-",
            r"\int^{0}_{-\pi}",  # 4
            r"\frac{1}{n}",
            r"\sin(nt)",
            r"\, dt",  # 7
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp9[2].set_color(YELLOW)
        integration_bp9[5].set_color(YELLOW)
        integration_bp10 = MathTex(
            r"=",
            r"-",
            r"\frac{1}{n}",
            r"\int^{0}_{-\pi}",  # 4
            r"\sin(nt)",
            r"\, dt",  # 7
            font_size=36,
        ).next_to(integration_bp1.get_right(), RIGHT, buff=0.5)
        integration_bp10[3].set_color(YELLOW)
        integration_bp10[5].set_color(YELLOW)
        integration_bp11 = MathTex(
            r"=",
            r"-",
            r"\frac{1}{n}",
            r"\left[",
            r"-\frac{1}{n}",
            r"\cos(nt)",
            r"\right]^{0}_{-\pi}",  # 4
            font_size=36,
        ).next_to(integration_bp10.get_right(), RIGHT, buff=0.5)
        integration_bp12 = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"\cos(nt)",
            r"\right]^{0}_{-\pi}",  # 4
            font_size=36,
        ).next_to(integration_bp10.get_right(), RIGHT, buff=0.5)
        integration_bp13 = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"\cos(0)",
            r"-",
            r"\cos(-n\pi)",
            r"\right]",  # 4
            font_size=36,
        ).next_to(integration_bp10.get_right(), RIGHT, buff=0.5)
        integration_bp14 = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"1",
            r"-",
            r"\cos(-n\pi)",
            r"\right]",  # 4
            font_size=36,
        ).next_to(integration_bp10.get_right(), RIGHT, buff=0.5)
        integration_bp15 = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"1",
            r"-",
            r"\cos(n\pi)",
            r"\right]",  # 4
            font_size=36,
        ).next_to(integration_bp10.get_right(), RIGHT, buff=0.5)
        f1_int4_ans = MathTex(
            r"\frac{1}{n^2}",
            r"\left[",
            r"1",
            r"-",
            r"\cos(n\pi)",
            r"\right]",  # 4
            font_size=36,
        ).next_to(integration_bp_group.get_left(), RIGHT, buff=0.1)

        f1_int5 = (
            MathTex(
                r"=",
                r"\frac{1}{n^2 \pi}",
                r"\left[",
                r"1",
                r"-",
                r"\cos(n\pi)",
                r"\right]",  # 4
                font_size=36,
            )
        ).next_to(f1_int1.get_right(), RIGHT, buff=0.1)
        integration_bp1_2 = MathTex(
            r"\int^{b}_{a}",  # 4
            r"t",
            r"\cos(nt)",
            r"\, dt",  # 7
            font_size=36,
        ).next_to(f1_int1, DOWN, aligned_edge=LEFT, buff=0.5)
        integration_bp1_2[0].set_color(YELLOW)
        integration_bp1_2[3].set_color(YELLOW)
        integration_bp1_2_ans = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"cos(nt)",
            r"\right]_{a}^{b}",
            font_size=36,
        ).next_to(integration_bp1_2.get_right(), RIGHT, buff=0.1)

        f1_int_ans = MathTex(
            r"\frac{1}{n^2 \pi}",
            r"(",
            r"1",
            r"-",
            r"\cos(n\pi)",
            r")",  # 4
            font_size=36,
        ).move_to(f1_int.get_center())

        a_n_5 = MathTex(
            r"a_n",  # Index 0
            r"=",  # Index 1
            r"\frac{2}{\pi}",  # Index 2
            r"\left[",  # Index 3
            r"\frac{1}{n^2 \pi}",  # Index 4
            r"(",  # Index 5
            r"1",  # Index 6
            r"-",  # Index 7
            r"\cos(n\pi)",  # Index 8
            r")",  # Index 9
            r"+",  # Index 10
            r"\int^{\pi}_{0}",  # Index 11
            r"(1 - \dfrac{1}{\pi}t)",  # Index 12
            r"\, \cos(n  t)",  # Index 13
            r"\, dt",  # Index 14
            r"\right]",  # Index 15
            font_size=36,
        )
        a_n_5[0].set_color(RED)
        a_n_5[11].set_color(YELLOW)
        a_n_5[14].set_color(YELLOW)
        f2_int = VGroup(a_n_5[11:15])
        f2_full_int = VGroup(a_n_5[10:15])
        f2_int1 = MathTex(
            r"\int^{\pi}_{0}",  # Index 11
            r"(1 - \dfrac{1}{\pi}t)",  # Index 12
            r"\, \cos(n  t)",  # Index 13
            r"\, dt",  # Index 14
            font_size=36,
        ).next_to(a_n_5, DOWN, aligned_edge=LEFT, buff=0.5)
        f2_int1[0].set_color(YELLOW)
        f2_int1[3].set_color(YELLOW)
        f2_int2 = MathTex(
            r"=",
            r"\int^{\pi}_{0}",  # Index 0
            r"\, \cos(n  t)",  # Index 1
            r"\, dt",  # Index 2
            r"-",  # Index 3
            r"\int^{\pi}_{0}",  # Index 4
            r"\dfrac{1}{\pi}",  # Index 5
            r"t",  # Index 6
            r"\cos(nt)",  # Index 7
            r"\, dt",  # Index 8
            font_size=36,
        ).next_to(f2_int1.get_right(), RIGHT, buff=0.1)
        f2_int2[1].set_color(YELLOW)
        f2_int2[3].set_color(YELLOW)
        f2_int2[5].set_color(YELLOW)
        f2_int2[9].set_color(YELLOW)
        cos_part = VGroup(f2_int2[1:4])
        ans_zero = MathTex(r"0", font_size=36).move_to(cos_part.get_center())

        f2_int3 = MathTex(
            r"=",
            r"-",
            r"\int^{\pi}_{0}",  # Index 4
            r"\dfrac{1}{\pi}",  # Index 5
            r"t",  # Index 6
            r"\cos(nt)",  # Index 7
            r"\, dt",  # Index 8
            font_size=36,
        ).next_to(f2_int1.get_right(), RIGHT, buff=0.1)
        f2_int3[2].set_color(YELLOW)
        f2_int3[6].set_color(YELLOW)
        f2_int4 = MathTex(
            r"=",
            r"-\dfrac{1}{\pi}",  # Index 5
            r"\int^{\pi}_{0}",  # Index 4
            r"t",  # Index 6
            r"\cos(nt)",  # Index 7
            r"\, dt",  # Index 8
            font_size=36,
        ).next_to(f2_int1.get_right(), RIGHT, buff=0.1)
        f2_int4[2].set_color(YELLOW)
        f2_int4[5].set_color(YELLOW)
        temp_part = VGroup(f2_int4[2:7])
        f2_int5 = MathTex(
            r"\int^{\pi}_{0}",  # Index 4
            r"t",  # Index 6
            r"\cos(nt)",  # Index 7
            r"\, dt",  # Index 8
            font_size=36,
        ).next_to(f2_int1, DOWN, aligned_edge=LEFT, buff=0.5)
        f2_int5[0].set_color(YELLOW)
        f2_int5[3].set_color(YELLOW)

        f2_int6 = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"\cos(nt)",
            r"\right]^{\pi}_{0}",
            font_size=36,
        ).next_to(f2_int5.get_right(), RIGHT, buff=0.1)
        f2_int7 = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"\cos(n\pi)",
            r"-",
            r"\cos(0)",
            r"\right]",
            font_size=36,
        ).next_to(f2_int6.get_right(), RIGHT, buff=0.1)
        f2_int8 = MathTex(
            r"=",
            r"\frac{1}{n^2}",
            r"\left[",
            r"\cos(n\pi)",
            r"-",
            r"1",
            r"\right]",
            font_size=36,
        ).next_to(f2_int6.get_right(), RIGHT, buff=0.1)
        f2_int_ans = MathTex(
            r"\frac{1}{n^2}",
            r"\left[",
            r"\cos(n\pi)",
            r"-",
            r"1",
            r"\right]",
            font_size=36,
        ).move_to(temp_part.get_center())
        f2_int4b = MathTex(
            r"=",
            r"-\frac{1}{n^2 \pi}",
            r"\left[",
            r"\cos(n\pi)",
            r"-",
            r"1",
            r"\right]",
            font_size=36,
        ).next_to(f2_int1.get_right(), RIGHT, buff=0.1)
        f2_ans = MathTex(
            r"-\frac{1}{n^2 \pi}",
            r"(",
            r"\cos(n\pi)",
            r"-",
            r"1",
            r")",
            font_size=36,
        ).move_to(f2_full_int.get_center())
        a_n_6 = MathTex(
            r"a_n",  # Index 0
            r"=",  # Index 1
            r"\frac{2}{\pi}",  # Index 2
            r"\big[",  # Index 3
            r"\frac{1}{n^2 \pi}",  # Index 4
            r"(",  # Index 5
            r"1",  # Index 6
            r"-",  # Index 7
            r"\cos(n\pi)",  # Index 8
            r")",  # Index 9
            r"-",  # Index 10
            r"\frac{1}{n^2 \pi}",
            r"(",
            r"\cos(n\pi)",
            r"-",
            r"1",
            r")",
            r"\big]",
            font_size=36,
        )
        a_n_6[0].set_color(RED)
        a_n_7 = MathTex(
            r"a_n",  # Index 0
            r"=",  # Index 1
            r"\frac{2}{n^2 \pi^2}",  # Index 2
            r"\big[",  # Index 3
            r"(",  # Index 5
            r"1",  # Index 6
            r"-",  # Index 7
            r"\cos(n\pi)",  # Index 8
            r")",  # Index 9
            r"-",  # Index 10
            r"(",
            r"\cos(n\pi)",
            r"-",
            r"1",
            r")",
            r"\big]",
            font_size=36,
        )
        a_n_7[0].set_color(RED)
        a_n_8 = MathTex(
            r"a_n",  # Index 0
            r"=",  # Index 1
            r"\frac{2}{n^2 \pi^2}",  # Index 2
            r"\big[",  # Index 3
            r"1",  # Index 6
            r"-",  # Index 7
            r"\cos(n\pi)",  # Index 8
            r"-\cos(n\pi)",
            r"+",
            r"1",
            r"\big]",
            font_size=36,
        )
        a_n_8[0].set_color(RED)
        a_n_9 = MathTex(
            r"a_n",  # Index 0
            r"=",  # Index 1
            r"\frac{2}{n^2 \pi^2}",  # Index 2
            r"\big[",  # Index 3
            r"2",
            r"-",
            r"2\cos(n\pi)",
            r"\big]",
            font_size=36,
        )
        a_n_9[0].set_color(RED)
        a_n_10 = MathTex(
            r"a_n",  # Index 0
            r"=",  # Index 1
            r"\frac{4}{n^2 \pi^2}",  # Index 2
            r"\big[",  # Index 3
            r"1",
            r"-",
            r"\cos(n\pi)",
            r"\big]",
            font_size=36,
        )
        a_n_10[0].set_color(RED)

        eq5 = MathTex(
            r"f(t)",  # 0
            r"=",  # 1
            r"1",
            r"+",  # 3
            r"\sum^{\infty}_{n=1}",  # 4
            r"\frac{4}{n^2 \pi^2}",  # Index 2
            r"\big[",  # Index 3
            r"1",
            r"-",
            r"\cos(n\pi)",
            r"\big]",
            r"\; cos(nt)",  # 6
            font_size=36,
        )
        eq5[11].set_color(RED)

        # --------------------- animation sectioin ---------------------

        self.add(ft_signal_def)
        self.add(q3)
        eq3.move_to(eq3_new_pos)
        eq4.move_to(eq3)
        self.add(eq4)
        self.wait()
        self.play(Write(a_n))
        self.wait()
        self.play(TransformMatchingShapes(a_n, a_n_1))
        self.wait()
        self.play(TransformMatchingShapes(a_n_1, a_n_2))
        self.wait()
        self.play(TransformMatchingShapes(a_n_2, a_n_3))
        self.wait()
        self.play(TransformMatchingShapes(a_n_3, a_n_4))
        self.wait()
        self.play(TransformFromCopy(f1_int, f1_int1))
        self.wait()
        self.play(Write(f1_int2))
        self.wait()
        self.play(TransformFromCopy(cos_group, cos_int1))
        self.wait()
        self.play(Write(cos_int2))
        self.wait()
        self.play(Write(cos_int3))
        self.wait()
        self.play(TransformMatchingShapes(cos_int3, cos_int4))
        self.wait()
        self.play(TransformMatchingShapes(cos_int4, cos_int5))
        self.wait()
        self.play(TransformMatchingShapes(cos_int5, cos_int6))
        self.wait()
        self.play(
            ReplacementTransform(cos_group, cos_int_ans),
            FadeOut(cos_int1, cos_int2, cos_int6),
        )
        self.wait()
        self.play(TransformMatchingShapes(f1_int2, f1_int3), FadeOut(cos_int_ans))
        self.wait()
        self.play(TransformMatchingShapes(f1_int3, f1_int4))
        self.wait()
        self.play(TransformFromCopy(integration_bp_group, integration_bp1))
        self.wait()
        self.play(Create(tab[0][0]))
        self.wait(0.5)
        self.play(Create(tab[0][1]))
        self.wait(0.5)
        self.play(LaggedStart(Create(tab[1]), Create(tab[2]), lag_ratio=0.3))
        self.wait()
        self.play(Create(tab[0][2]))
        self.wait(0.5)
        self.play(Create(tab[0][3]))
        self.wait(0.5)
        self.play(Write(integration_bp2))
        self.wait()
        self.play(FadeOut(tab))
        self.wait()
        brc = Brace(VGroup(integration_bp2[6:11]), DOWN, buff=0.2)
        self.play(Create(brc))
        self.wait()
        self.play(
            TransformMatchingShapes(integration_bp2, integration_bp3), FadeOut(brc)
        )
        self.wait()
        self.play(TransformMatchingShapes(integration_bp3, integration_bp4))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp4, integration_bp5))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp5, integration_bp6))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp6, integration_bp7))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp7, integration_bp8))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp8, integration_bp9))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp9, integration_bp10))
        self.wait()
        self.play(Write(integration_bp11))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp11, integration_bp12))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp12, integration_bp13))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp13, integration_bp14))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp14, integration_bp15))
        self.wait()
        self.play(ReplacementTransform(integration_bp_group, f1_int4_ans))
        self.wait()
        self.play(TransformMatchingShapes(f1_int4, f1_int5), FadeOut(f1_int4_ans))
        self.wait()
        self.play(FadeOut(integration_bp15, integration_bp10))
        self.wait()
        self.play(TransformMatchingShapes(integration_bp1, integration_bp1_2))
        self.wait()
        self.play(Write(integration_bp1_2_ans))
        self.wait()
        self.play(FadeOut(integration_bp1_2, integration_bp1_2_ans))
        self.wait()
        self.play(ReplacementTransform(f1_int, f1_int_ans), FadeOut(f1_int1, f1_int5))
        self.wait()
        self.play(TransformMatchingShapes(a_n_4, a_n_5), FadeOut(f1_int_ans))
        self.wait()
        self.play(TransformFromCopy(f2_int, f2_int1))
        self.wait()
        self.play(Write(f2_int2))
        self.wait()
        brc = Brace(VGroup(cos_part), DOWN, buff=0.1)
        self.play(Create(brc))
        self.wait()
        self.play(ReplacementTransform(cos_part, ans_zero), FadeOut(brc))
        self.wait()
        self.play(TransformMatchingShapes(f2_int2, f2_int3), FadeOut(ans_zero))
        self.wait()
        self.play(TransformMatchingShapes(f2_int3, f2_int4))
        self.wait()
        self.play(TransformFromCopy(temp_part, f2_int5))
        self.wait()
        self.play(Write(f2_int6))
        self.wait()
        self.play(Write(f2_int7))
        self.wait()
        self.play(TransformMatchingShapes(f2_int7, f2_int8))
        self.wait()
        self.play(ReplacementTransform(temp_part, f2_int_ans), FadeOut(f2_int8))
        self.wait()
        self.play(TransformMatchingShapes(f2_int4, f2_int4b), FadeOut(f2_int_ans))
        self.wait()
        self.play(FadeOut(f2_int6, f2_int5))
        self.wait()
        self.play(ReplacementTransform(f2_full_int, f2_ans), FadeOut(f2_int4b))
        self.wait()
        self.play(TransformMatchingShapes(a_n_5, a_n_6), FadeOut(f2_int1, f2_ans))
        self.wait()
        s1 = SurroundingRectangle(a_n_6[4], color=ORANGE, stroke_width=3, buff=0.1)
        s2 = SurroundingRectangle(a_n_6[11], color=ORANGE, stroke_width=3, buff=0.1)
        self.play(Create(s1), Create(s2))
        self.wait()
        self.play(TransformMatchingShapes(a_n_6, a_n_7), FadeOut(s1, s2))
        self.wait()
        self.play(TransformMatchingShapes(a_n_7, a_n_8))
        self.wait()
        self.play(TransformMatchingShapes(a_n_8, a_n_9))
        self.wait()
        self.play(TransformMatchingShapes(a_n_9, a_n_10))
        self.wait()
        # self.play(a_n_10.animate.shift(1.5 * DOWN), eq4.animate.move_to(ORIGIN))
        # self.wait()
        eq5.move_to(eq4)
        self.play(TransformMatchingShapes(eq4, eq5), FadeOut(a_n_10))
        self.wait()
        self.play(
            FadeOut(q3),
            q4.animate.move_to(q4_copy),
        )
        self.wait()
        self.play(FadeOut(ft_signal_def), eq5.animate.move_to(UP * eq5.get_y()))
        self.wait()

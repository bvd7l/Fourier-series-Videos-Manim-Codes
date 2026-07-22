from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class Part4(Scene):
    def construct(self):
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
        q3.move_to(q1)
        q4.move_to(q3.get_center())
        q4.align_to(q3, RIGHT)
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
        ft_signal_def.next_to(axes, RIGHT, buff=1)
        ft_signal_def.shift(0.5 * DOWN)
        ft_signal_def.to_edge(LEFT, buff=1).shift(1 * UP)

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
        ).next_to(ft_signal_def, RIGHT, buff=0.5)
        eq5[11].set_color(RED)
        eq5.move_to(UP * eq5.get_y())
        ## new code
        n_term = MathTex(r"n", font_size=36).set_color(TEAL)
        zero_term = MathTex(r"0", font_size=36).set_color(TEAL)
        one_term = MathTex(r"1", font_size=36).set_color(TEAL)
        two_term = MathTex(r"2", font_size=36).set_color(TEAL)
        three_term = MathTex(r"3", font_size=36).set_color(TEAL)
        a_n_term = MathTex(r"a_n", font_size=36).set_color(BLUE)
        nwt_term = MathTex(r"n\omega t ", font_size=36).set_color(RED)
        a_n_cos_nwt = MathTex(r"a_n", r"\cos(n\omega t)", font_size=36)
        a_n_cos_nwt[0].set_color(BLUE)
        a_n_cos_nwt[1].set_color(RED)
        temp_zero = MathTex(r"0", font_size=36)
        temp_one = MathTex(r"1", font_size=36)
        an1 = MathTex(r"\frac{8}{\pi ^ 2}", font_size=36)
        nwt1 = MathTex(r"t", font_size=36)
        nwt2 = MathTex(r"2t", font_size=36)
        an3 = MathTex(r"\frac{8}{9\pi ^ 2}", font_size=36)
        nwt3 = MathTex(r"3t", font_size=36)
        a1coswt = MathTex(r"\frac{8}{\pi ^ 2}\cos(t)", font_size=36)
        a3coswt = MathTex(r"\frac{8}{9\pi ^ 2}\cos(3t)", font_size=36)
        table = MobjectTable(
            [
                [n_term, zero_term, one_term, two_term, three_term],
                [a_n_term, temp_one.copy(), an1, temp_zero.copy(), an3],
                [nwt_term, temp_zero.copy(), nwt1, nwt2, nwt3],
                [a_n_cos_nwt, temp_one.copy(), a1coswt, temp_zero.copy(), a3coswt],
            ],
            v_buff=0.4,
            h_buff=1,
            line_config={
                "stroke_width": 1.5,  # This controls the table line thickness
                "color": WHITE,
            },
        ).next_to(eq5, DOWN, buff=0.3)
        table.remove(*table.get_vertical_lines())
        table.remove(*table.get_horizontal_lines()[1:])

        last_row = table.get_rows()[3]
        ft_3_eq = MathTex(
            r"f(t)",
            r"=",
            r"1",
            r"+",
            r"\frac{8}{\pi ^ 2}\cos(t)",
            r"+",
            r"0",
            r"+",
            r"\frac{8}{9\pi ^ 2}\cos(3t)",
            font_size=36,
        ).next_to(table, DOWN, buff=0.4)
        ft_3_eq2 = MathTex(
            r"f(t)",
            r"=",
            r"1",
            r"+",
            r"\frac{8}{\pi ^ 2}\cos(t)",
            r"+",
            r"\frac{8}{9\pi ^ 2}\cos(3t)",
            font_size=36,
        ).next_to(table, DOWN, buff=0.4)
        ## animation section
        self.add(q4)
        self.add(eq5)
        self.wait()
        self.play(Create(table[0][0]))
        self.wait()
        self.play(Create(table[1]))
        self.wait()
        self.play(
            LaggedStart([Create(table[0][i]) for i in range(1, 5)], lag_ratio=0.2)
        )
        self.wait()
        for j in range(5, 10):
            for i in range(j, 20, 5):
                self.play(Create(table[0][i]))
                # self.wait(0.5)
            self.wait()
        rec = SurroundingRectangle(last_row, color=ORANGE, stroke_width=3, buff=0.1)
        self.play(Create(rec))
        self.wait()
        self.play(TransformFromCopy(last_row, ft_3_eq), FadeOut(rec))
        self.wait()
        self.play(TransformMatchingTex(ft_3_eq, ft_3_eq2))
        self.wait()
        self.play(FadeOut(ft_3_eq2, table, eq5, q4))
        self.wait()

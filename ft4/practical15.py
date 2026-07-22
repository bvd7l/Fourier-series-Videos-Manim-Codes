from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


def bracket(x: str, fl_col=WHITE, st_col=WHITE):
    bracket_tex = Tex(x, font_size=72)
    bracket_path = bracket_tex.family_members_with_points()[0]
    # Now you can manipulate it
    bracket_path.stretch(3, 1)  # Make it 3 times taller
    bracket_path.set_stroke(width=3, color=st_col)
    bracket_path.set_fill(color=fl_col)
    return bracket_path


class Part5(Scene):
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
        q5 = ar_text("- ارسم الطيف المطالي الترددي.", 24).next_to(
            q4, DOWN, aligned_edge=RIGHT, buff=0.5
        )
        q6 = ar_text(
            "- إذا أرسلت هذه الإشارة عبر قناة وكان المجال الترددي للقناة [0,2π/2[ ، أوجد الإشارة الناتجة.",
            24,
        ).next_to(q5, DOWN, aligned_edge=RIGHT, buff=0.5)
        q1.shift(UP)
        q3.move_to(q1)
        q4.move_to(q3.get_center())
        q4.align_to(q3, RIGHT)
        q5.move_to(q4.get_center())
        q5.align_to(q4, RIGHT)
        q6_copy = q6.copy()
        q6_copy.move_to(q5.get_center())
        q6_copy.align_to(q5, RIGHT)

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

        cos_wave_formulas = VGroup()
        cos_wave_1 = MathTex(r"1", font_size=33, color=PINK)
        cos_wave_2 = MathTex(r"\frac{8}{\pi ^2} \cos(t)", font_size=33, color=GREEN)
        cos_wave_3 = MathTex(r"0", font_size=33, color=GOLD_A)
        cos_wave_4 = MathTex(r"\frac{8}{9 \pi^2} \cos(3 t)", font_size=33, color=ORANGE)

        cos_wave_formulas.add(cos_wave_1, cos_wave_2, cos_wave_3, cos_wave_4).arrange(
            DOWN, buff=0.5
        )
        cos_wave_formulas.to_edge(LEFT, buff=1)

        axes = Axes(
            x_range=[0, 5 * PI, PI],
            y_range=[0, 5.5, 1],
            x_length=7,
            y_length=4,
            tips=False,
            axis_config={"color": BLUE, "stroke_width": 4, "tick_size": 0.05},
        ).shift(RIGHT)
        axes.shift(UP)
        x_axis_label = axes.get_x_axis_label(
            MathTex("\\omega", color=WHITE, font_size=33),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )
        y_axis_label = axes.get_y_axis_label(
            Tex("f(t)", color=RED_A, font_size=33), edge=UP, direction=UP, buff=0.15
        )
        x_labels = VGroup()
        pi_values = [
            0,
            PI,
            2 * PI,
            3 * PI,
            4 * PI,
            5 * PI,
            6 * PI,
            # 7 * PI,
            # 8 * PI,
        ]
        pi_labels = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            # "6",
            # "7",
            # "8",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 8 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.3)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.3)
                    )

            x_labels.add(x_label)

        y_labelss = VGroup()
        y_values = [
            1,
            2,
            3,
            4,
            5,
        ]
        y_labels = [
            "1",
            "\\frac{8}{ \\pi^2}",
            "\\frac{8}{4 \\pi^2}",
            "\\frac{8}{9 \\pi^2}",
            "\\frac{8}{  27\\pi^2}",
        ]
        y_labels.reverse()
        i = 0
        for y_val, label in zip(y_values, y_labels):
            if y_val <= 5:

                y_label = MathTex(label, font_size=24, color=WHITE).move_to(
                    axes.c2p(-0.8, y_val)
                )

            y_labelss.add(y_label)

        axes_graph = VGroup(axes, x_labels, y_labelss, x_axis_label, y_axis_label)
        axes_graph.shift(DOWN)
        line1 = Line(
            start=axes.c2p(0, 0), end=axes.c2p(0, 4 + 1), color=PINK, stroke_width=3
        )
        dot1 = Dot(point=axes.c2p(0, 4 + 1), color=PINK, radius=0.07)
        d_line1 = DashedLine(
            start=axes.c2p(0, 4 + 1),
            end=axes.c2p(0, 4 + 1),
            color=PINK,
            stroke_width=3,
        )
        line_dot_1 = VGroup(line1, dot1, d_line1)

        line2 = Line(
            start=axes.c2p(1 * PI, 0),
            end=axes.c2p(1 * PI, 3 + 1),
            color=GREEN,
            stroke_width=3,
        )
        dot2 = Dot(point=axes.c2p(1 * PI, 3 + 1), color=GREEN, radius=0.07)
        d_line2 = DashedLine(
            start=axes.c2p(0, 4),
            end=axes.c2p(1 * PI, 3 + 1),
            color=GREEN,
            stroke_width=3,
        )
        line_dot_2 = VGroup(line2, dot2, d_line2)

        line3 = Line(
            start=axes.c2p(2 * PI, 0),
            end=axes.c2p(2 * PI, 0),
            color=GOLD_A,
            stroke_width=3,
        )
        dot3 = Dot(point=axes.c2p(2 * PI, 0), color=GOLD_A, radius=0.07)
        d_line3 = DashedLine(
            start=axes.c2p(2 * PI, 0),
            end=axes.c2p(2 * PI, 0),
            color=GOLD_A,
            stroke_width=3,
        )
        line_dot_3 = VGroup(line3, dot3, d_line3)

        line4 = Line(
            start=axes.c2p(3 * PI, 0),
            end=axes.c2p(3 * PI, 1 + 1),
            color=ORANGE,
            stroke_width=3,
        )
        dot4 = Dot(point=axes.c2p(3 * PI, 1 + 1), color=ORANGE, radius=0.07)
        d_line4 = DashedLine(
            start=axes.c2p(0, 2),
            end=axes.c2p(3 * PI, 1 + 1),
            color=ORANGE,
            stroke_width=3,
        )
        line_dot_4 = VGroup(line4, dot4, d_line4)
        lines_fre = VGroup(line_dot_1, line_dot_2, line_dot_3, line_dot_4)
        x_axis_label2 = axes.get_x_axis_label(
            MathTex(
                "2 \\pi f", color=WHITE, font_size=33
            ),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )
        x_labels1 = VGroup()
        pi_values = [
            0,
            PI,
            2 * PI,
            3 * PI,
            4 * PI,
            5 * PI,
            # 6 * PI,
            # 7 * PI,
            # 8 * PI,
        ]
        pi_labels = [
            "0",
            "\\frac{1}{2\\pi}",
            "\\frac{2 }{2\\pi}",
            "\\frac{3 }{2\\pi}",
            "\\frac{4}{2\\pi}",
            "\\frac{5}{2\\pi}",
            # "\\frac{6\\pi}{2\\pi}",
            # "\\frac{7\\pi}{2\\pi}",
            # "\\frac{8\\pi}{2\\pi}",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 8 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.3)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.5)
                    )

            x_labels1.add(x_label)

        x_labels3 = VGroup()
        pi_values = [
            0,
            PI,
            2 * PI,
            3 * PI,
            4 * PI,
            5 * PI,
            #     6 * PI,
            #     7 * PI,
            #     8 * PI,
        ]
        pi_labels = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            # "6",
            # "7",
            # "8",
        ]
        i = 0
        for x_val, label in zip(pi_values, pi_labels):
            if x_val <= 8 * PI:
                if i == 0:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val + 0.15, -0.3)
                    )
                    i += 1
                else:
                    x_label = MathTex(label, font_size=24, color=WHITE).move_to(
                        axes.c2p(x_val, -0.3)
                    )

            x_labels3.add(x_label)

        x_axis_label3 = axes.get_x_axis_label(
            MathTex("f", color=WHITE, font_size=33),  # You can use Tex or MathTex
            edge=RIGHT,
            direction=RIGHT,
            buff=0.3,  # Distance from axis
        )
        rang = MathTex(r"]", r"0", r",", r"\frac{2}{2\pi}", r"]", font_size=36)
        left_sb = bracket("]", RED, RED).next_to(axes.c2p(0, 0), RIGHT, buff=0)
        righ_sb = bracket(r"]", RED, RED).next_to(axes.c2p(2 * PI, 0), RIGHT, buff=0)

        second_third_eq = VGroup(cos_wave_formulas[1], cos_wave_formulas[2])
        rect_both = SurroundingRectangle(
            second_third_eq, color=YELLOW, buff=0.2, stroke_width=3
        )
        final_ans = MathTex(
            r"\; \Rightarrow \;", r"f(t)", r"=", r"\frac{8}{\pi^2}\cos(t)", font_size=36
        )
        ## animation section
        self.play(FadeIn(q5))
        self.add(q5)
        self.wait()
        # new animations
        self.play(
            LaggedStart(*[Write(s_w) for s_w in cos_wave_formulas], LaggedStart=0.2),
            run_time=2,
        )
        self.wait()
        self.play(Create(axes_graph), run_time=3)

        self.wait()
        self.play(
            LaggedStart(
                *[
                    TransformFromCopy(s_w, lin)
                    for s_w, lin in zip(cos_wave_formulas, lines_fre)
                ],
                lag_ratio=1,
            ),
            run_time=4,
        )
        self.wait()
        rec = SurroundingRectangle(x_axis_label, color=ORANGE, buff=0.1, stroke_width=3)
        self.play(Create(rec))
        self.wait()
        self.play(ReplacementTransform(x_axis_label, x_axis_label2), FadeOut(rec))
        self.wait()
        self.play(TransformMatchingShapes(x_labels, x_labels1))
        self.wait()
        self.play(TransformMatchingTex(x_axis_label2, x_axis_label3))
        self.wait()
        self.play(FadeOut(q5), q6.animate.move_to(q6_copy))
        self.wait()
        rang.next_to(q6, DOWN, buff=1)
        self.play(Write(rang))
        self.wait()
        self.play(TransformFromCopy(rang[0], left_sb))
        self.wait()
        self.play(TransformFromCopy(rang[-1], righ_sb))
        self.wait()
        self.play(Create(rect_both))
        self.wait()
        self.play(FadeOut(rect_both, left_sb, righ_sb))
        self.wait()
        final_ans.next_to(rang, RIGHT, buff=0.5)
        self.play(TransformFromCopy(second_third_eq, final_ans))
        self.wait()

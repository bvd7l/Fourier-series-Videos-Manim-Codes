from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class EX1(Scene):
    def construct(self):

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
        axes.x_axis.tip.scale(0.7)
        axes.y_axis.tip.scale(0.7)
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("t", font_size=36),  # Smaller font size
            y_label=MathTex("f(t)", font_size=36),
        )
        number_of_points = 3
        amplitude_value = 2
        points = [
            (i, 0 if i & 1 else amplitude_value)
            for i in range(-number_of_points, number_of_points + 1)
        ]

        waveform_path = VMobject()
        waveform_path.set_points_as_corners([axes.c2p(x, y) for x, y in points])
        waveform_path.set_stroke(color=PURE_RED, width=3, opacity=1.0)
        x_labels = VGroup()
        for i in range(-number_of_points, number_of_points + 1):
            if i == 0:
                label = MathTex(f"{i}", font_size=30)
                x, y = points[i + number_of_points]
                label.next_to(axes.c2p(x + 0.15, 0), DOWN, buff=0.1)
                x_labels.add(label)
                continue

            label = MathTex(f"{i}\\pi", font_size=30)
            x, y = points[i + number_of_points]
            label.next_to(axes.c2p(x, 0), DOWN, buff=0.1)
            x_labels.add(label)
        triangle_pattern = points[0:3]
        pattern = VGroup()
        pattern.set_points_as_corners([axes.c2p(x, y) for x, y in triangle_pattern])
        pattern.set_stroke(color=YELLOW, width=3, opacity=1)
        dashedY2 = DashedLine(
            start=axes.c2p(-3, 2),
            end=axes.c2p(3, 2),
            color=WHITE,
            stroke_width=2,
        )
        number2 = MathTex(r"2", font_size=36).next_to(axes.c2p(0, 2), UP, buff=0.2)
        number2.shift(0.15 * RIGHT)
        dashed_number = VGroup(dashedY2, number2)
        axes_full = VGroup(axes, axes_labels, waveform_path, x_labels, dashed_number)
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
        point1 = Dot(point=axes.c2p(1, 0), color=PURE_RED, radius=0.08)
        point2 = Dot(point=axes.c2p(3, 0), color=PURE_RED, radius=0.08)
        double_arrow = DoubleArrow(
            start=axes.c2p(1, 0),
            end=axes.c2p(3, 0),
            buff=0.1,
            color=GREEN,
            stroke_width=5,
            tip_length=0.2,
        )

        T0 = MathTex(r"T_0", font_size=36)
        T01 = MathTex(r"T_0", r"=", r"3\pi", r"-", r"\pi", font_size=36)
        T02 = MathTex(r"T_0", r"=", r"2\pi", r"\quad s", font_size=36)
        f0 = MathTex(
            r"f",
            r"=",
            r"\frac{1}{T_0}",
            r"=",
            r"\frac{1}{2\pi}",
            r"\quad s^{-1}",
            font_size=36,
        )
        omega = MathTex(
            r"\omega",
            r"=",
            r"\frac{2\pi}{T_0}",
            r"=",
            r"2\pi f",
            r"=",
            r"1",
            r"\quad rad.s^{-1}",
            font_size=36,
        )
        DotA = Dot(point=axes.c2p(-1, 0), color=PURE_RED, radius=0.08)
        DotB = Dot(point=axes.c2p(0, 2), color=PURE_RED, radius=0.08)
        point_A = MathTex(r"A", r"(-\pi,0)", font_size=36)
        # point_A[0].set_color(RED)
        point_B = MathTex(r"B", r"(0,2)", font_size=36)
        # point_B[0].set_color(RED)
        dots = VGroup(point_A, point_B)
        dots.arrange(RIGHT, buff=1)
        y1_eq = MathTex(r"y", r"=", r"m", r"t", r"+", r"b", font_size=36)
        y1_eq[2].set_color(RED)
        y1_eq[5].set_color(BLUE)
        m1_eq = MathTex(r"m", r"=", r"\frac{2 - 0}{0 - (-\pi)}", font_size=36)
        m1_eq[0].set_color(RED)
        m1_eq2 = MathTex(r"m", r"=", r"\frac{2}{\pi}", font_size=36)
        m1_eq2[0].set_color(RED)
        y1_eq2 = MathTex(r"y", r"=", r"\frac{2}{\pi}", r"t", r"+", r"b", font_size=36)
        y1_eq2[5].set_color(BLUE)
        b1 = MathTex(r"2", r"=", r"0", r"+", r"b", font_size=36)
        b12 = MathTex(r"b", r"=", r"2", font_size=36)
        b1[4].set_color(BLUE)
        b12[0].set_color(BLUE)
        y1_eq3 = MathTex(r"y", r"=", r"2", r"+", r"\frac{2}{\pi}", r"t", font_size=36)
        point_A2 = MathTex(r"A(0,2)", font_size=36)
        point_B2 = MathTex(r"B(\pi,0)", font_size=36)
        dots2 = VGroup(point_A2, point_B2).arrange(RIGHT, buff=1)
        y2_eq = MathTex(r"y", r"=", r"m", r"t", r"+", r"b", font_size=36)
        y2_eq[2].set_color(RED)
        y2_eq[5].set_color(BLUE)
        m2_eq = MathTex(r"m", r"=", r"\frac{0-2}{\pi - 0 }", font_size=36)
        m2_eq[0].set_color(RED)
        m2_eq2 = MathTex(r"m", r"=", r"- \frac{2}{\pi}", font_size=36)
        m2_eq2[0].set_color(RED)
        y2_eq2 = MathTex(r"y", r"=", r"-\frac{2}{\pi}", r"x", r"+", r"b", font_size=36)
        y2_eq2[5].set_color(BLUE)
        b2 = MathTex(r"2", r"=", r"0", r"+", r"b", font_size=36)
        b22 = MathTex(r"b", r"=", r"2", font_size=36)
        b2[4].set_color(BLUE)
        b22[0].set_color(BLUE)
        y2_eq3 = MathTex(r"y", r"=", r"2", r"-", r"\frac{2}{\pi}", r"t", font_size=36)
        ft_signal_def = MathTex(
            r"f(t)",
            r"=",
            r"\begin{cases} \; 2 + \dfrac{2}{\pi}t & -\pi < t <0 \\[10pt] \; 2 - \dfrac{2}{\pi}t & \; 0 < t < \pi \end{cases}",
            font_size=36,
        )

        self.play(Create(axes))
        self.wait()
        self.play(Write(axes_labels))
        self.wait()
        self.play(FadeIn(waveform_path))
        self.wait()
        self.play(Create(x_labels))
        self.wait()
        self.play(Create(dashedY2), Write(number2))
        self.wait()
        self.play(axes_full.animate.shift(1.5 * UP + 3.5 * LEFT).scale(0.9))
        self.wait()
        triangle_pattern = points[0:3]
        pattern = VGroup()
        pattern.set_points_as_corners([axes.c2p(x, y) for x, y in triangle_pattern])
        pattern.set_stroke(color=YELLOW, width=3, opacity=1)
        self.play(Write(the_question, reverse=True))
        self.add(the_question)
        self.wait(0.5)
        self.play(Write(q1, reverse=True))
        self.add(q1)
        self.wait(0.5)
        self.play(Write(q2, reverse=True))
        self.add(q2)
        self.wait(0.5)
        self.play(Write(q3, reverse=True))
        self.add(q3)
        self.wait(0.5)
        self.play(Write(q4, reverse=True))
        self.add(q4)
        self.wait(0.5)
        self.play(Write(q5, reverse=True))
        self.add(q5)
        self.wait(0.5)
        self.play(Write(q6, reverse=True))
        self.add(q6)
        self.wait(0.5)
        self.play(FadeOut(q2, q3, q4, q5, q6, the_question), q1.animate.shift(UP))
        self.wait(0.5)
        self.play(Create(pattern))
        self.wait()
        shift_ammount = axes.c2p(2, 0) - axes.c2p(0, 0)
        for _ in range(2):
            self.play(pattern.animate.shift(shift_ammount * RIGHT))
        self.wait()
        double_arrow.next_to(pattern, DOWN, buff=0.3)
        point1 = Dot(point=axes.c2p(1, 0), color=PURE_RED, radius=0.08)
        point2 = Dot(point=axes.c2p(3, 0), color=PURE_RED, radius=0.08)
        self.play(LaggedStart(Create(point1), Create(point2), lag_ratio=0.2))
        self.wait()
        T0.next_to(double_arrow, DOWN, buff=0.1)
        self.play(Create(double_arrow))
        self.play(Write(T0))
        self.wait()
        T01.next_to(q1, DOWN, buff=1)
        self.play(ReplacementTransform(VGroup(double_arrow, T0, point1, point2), T01))
        self.wait()
        T02.next_to(q1, DOWN, buff=1)
        self.play(TransformMatchingShapes(T01, T02))
        self.wait()
        f0.next_to(T02, DOWN, buff=0.5)
        self.play(TransformFromCopy(T02, f0))
        self.wait()
        omega.next_to(f0, DOWN, buff=0.5)
        self.play(Write(omega[0:5]))
        self.wait()
        self.play(Write(omega[5:]))
        self.wait()
        q1_group = VGroup(q1, T02, f0, omega)

        self.play(FadeOut(q1_group))
        self.wait(0.5)
        self.play(q2.animate.move_to(q1))
        self.wait()
        self.play(pattern.animate.shift(LEFT * shift_ammount))
        self.wait()
        dots.next_to(q2, DOWN, buff=1)
        DotA = Dot(point=axes.c2p(-1, 0), color=PURE_RED, radius=0.08)
        DotB = Dot(point=axes.c2p(0, 2), color=PURE_RED, radius=0.08)
        self.play(Create(DotA), Create(DotB))
        self.wait()
        dots.next_to(q2, DOWN, buff=1)
        self.play(LaggedStart(Write(point_A), Write(point_B), lag_ratio=0.2))
        self.wait()
        y1_eq.next_to(dots, DOWN, buff=0.5)
        self.play(Write(y1_eq))
        self.wait()
        m1_eq.next_to(y1_eq, DOWN, buff=0.5)
        self.play(TransformFromCopy(VGroup(point_A, point_B), m1_eq))
        self.wait()
        m1_eq2.move_to(m1_eq)
        self.play(TransformMatchingShapes(m1_eq, m1_eq2))
        self.wait()
        y1_eq2.move_to(y1_eq)
        self.play(TransformMatchingShapes(y1_eq, y1_eq2), FadeOut(m1_eq2))
        self.wait()
        b1.next_to(y1_eq2, DOWN, buff=0.5)
        self.play(TransformFromCopy(VGroup(point_B, y1_eq2), b1))
        self.wait()
        b12.move_to(b1)
        self.play(TransformMatchingShapes(b1, b12))
        self.wait()
        y1_eq3.move_to(y1_eq2)
        self.play(TransformMatchingShapes(y1_eq2, y1_eq3), FadeOut(b12))
        self.wait()

        self.play(FadeOut(DotB, DotA, dots), y1_eq3.animate.move_to(dots))
        self.wait()
        DotA = Dot(point=axes.c2p(0, 2), color=PURE_RED, radius=0.08)
        DotB = Dot(point=axes.c2p(1, 0), color=PURE_RED, radius=0.08)
        self.play(Create(DotA), Create(DotB))
        self.wait()
        dots2.next_to(y1_eq3, DOWN, buff=1)
        self.play(Write(point_A2), Write(point_B2))
        self.wait()
        y2_eq.next_to(dots2, DOWN, buff=0.5)
        self.play(Write(y2_eq))
        self.wait()
        m2_eq.next_to(y2_eq, DOWN, buff=0.5)
        self.play(TransformFromCopy(VGroup(point_A2, point_B2), m2_eq))
        self.wait()
        m2_eq2.move_to(m2_eq)
        self.play(TransformMatchingShapes(m2_eq, m2_eq2))
        self.wait()
        y2_eq2.move_to(y2_eq)
        self.play(TransformMatchingShapes(y2_eq, y2_eq2), FadeOut(m2_eq2))
        self.wait()
        b1.next_to(y2_eq2, DOWN, buff=0.5)
        self.play(TransformFromCopy(VGroup(point_A2, y2_eq2), b1))
        self.wait()
        b12.move_to(b1)
        self.play(TransformMatchingShapes(b1, b12))
        self.wait()
        y2_eq3.move_to(y2_eq)
        self.play(TransformMatchingShapes(y2_eq2, y2_eq3), FadeOut(b12, DotA, DotB))
        self.wait()
        self.play(
            y2_eq3.animate.next_to(y1_eq3, DOWN, buff=0.5), FadeOut(point_A2, point_B2)
        )
        self.wait()
        ft_signal_def.next_to(axes, RIGHT, buff=1)
        ft_signal_def.shift(0.5 * DOWN)
        self.play(ReplacementTransform(VGroup(y1_eq3, y2_eq3), ft_signal_def))
        self.wait()

        right_pattern = VGroup()
        right_pattern.set_points_as_corners([axes.c2p(0, 2), axes.c2p(1, 0)])
        right_pattern.set_stroke(color=PURE_RED, width=3, opacity=1)
        left_pattern = VGroup()
        left_pattern.set_points_as_corners([axes.c2p(-1, 0), axes.c2p(0, 2)])
        left_pattern.set_stroke(color=PURE_RED, width=3, opacity=1)
        self.play(FadeIn(right_pattern))
        self.wait()
        self.play(TransformFromCopy(right_pattern, left_pattern))
        self.wait()
        self.play(q3.animate.move_to(q2), FadeOut(q2))
        self.wait()
        self.play(FadeOut(axes_full, right_pattern, left_pattern, pattern))

        self.play(ft_signal_def.animate.to_edge(LEFT, buff=1).shift(1 * UP))
        self.wait()

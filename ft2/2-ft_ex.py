from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


def half_smooth(t):
    return smooth(t * 0.5)


class LogScalingExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 3],
            y_range=[-2, 2],
            y_length=4,
            x_length=5,
            tips=False,
            axis_config={
                "tip_shape": StealthTip,
                "tip_length": 0.05,
                "tip_width": 0.05,
                "tick_size": 0.05,
            },
        )

        axes_labels = axes.get_axis_labels(
            x_label=MathTex("t", font_size=30),  # Smaller font size
            y_label=MathTex("x(t)", font_size=30),
        )

        points = [
            # (-3, -1),
            # (-2, -1),
            # (-2, 0),
            # (-2, 1),
            # (-1, 1),
            # (-1, 0),
            # (-1, -1),
            # (0, -1),
            # (0, 0),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (2, -1),
            (2, 0),
            # (2, 1),
            # (3, 1),
        ]
        screenPoints = [axes.coords_to_point(x, y) for x, y in points]
        lines = VGroup()

        for i in range(len(screenPoints) - 1):
            line = Line(
                start=screenPoints[i],
                end=screenPoints[i + 1],
                color=RED,
                stroke_width=3,
            )
            lines.add(line)

        # lines1 = lines.copy()
        # lines2 = lines.copy()
        # lines1.shift(LEFT * 2.5).set_opacity(0.2)
        # lines2.shift(RIGHT * 2.5).set_opacity(0.2)

        x_label1 = MathTex(r"\frac{T_0}{2}", font_size=30).move_to(
            axes.c2p(1 + 0.2, 0 + 0.5)
        )
        x_label2 = MathTex(r"T_0", font_size=30).move_to(axes.c2p(2 + 0.2, -(0 + 0.5)))
        txt1 = MathTex("A", font_size=36)
        txt1.next_to(lines[0], DOWN, buff=0.3)
        txt2 = MathTex("-A", font_size=36)
        txt2.next_to(lines[3], UP, buff=0.3)

        res_group = VGroup(axes, axes_labels, txt1, lines, txt2, x_label1, x_label2)
        res_group.shift(UP * 1).to_edge(LEFT, buff=1)

        lines1 = lines.copy()
        lines2 = lines.copy()
        lines1.shift(LEFT * 2.5).set_opacity(0.2)
        lines2.shift(RIGHT * 2.5).set_opacity(0.2)
        lines12 = VGroup(lines1, lines2)
        signal_def = (
            MathTex(
                r"x(t)",
                "=",
                r"\begin{cases}"
                r"\;A & \text{; } 0 < t < \dfrac{T_0}{2} \\"
                r"\;-A   & \text{; } \dfrac{T_0}{2} < t < T_0"
                r"\end{cases}",
                font_size=36,
            )
            # .scale(0.7)
            .next_to(res_group, RIGHT, buff=1)
        )
        graph_signlaDef = VGroup(res_group, signal_def)
        the_question = (
            ar_text(
                "أوجد سلسة فورييه لهذه الإشارة علماً أنها تنتشر بشكل دوري خارج هذا المجال.",
                26,
            )
            .to_edge(RIGHT, buff=1)
            .shift(1.5 * DOWN)
        )
        # ------------- the solution section -------------
        eq1 = MathTex(
            r"x(t)",  # 0
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
            font_size=30,
        )
        eq1[2].set_color(RED)
        eq1[5].set_color(RED)
        eq1[11].set_color(RED)
        ## finding a_0
        a_0 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{T_0}",  # 2
            r"\left[",  # 3
            r"\int^{\frac{T_0}{2}}_{0}",  # 4
            r"x(t)",  # 5
            r"\;",  # 6
            r"dt",  # 7
            r"+",  # 8
            r"\int^{T_0}_{\frac{T_0}{2}}",  # 9
            r"x(t)",  # 10
            r"\;dt",  # 11
            r"\right]",  # 12
            font_size=30,
        )
        a_0[0].set_color(RED)
        a_0[4].set_color(YELLOW)
        a_0[7].set_color(YELLOW)
        a_0[9].set_color(YELLOW)
        a_0[11].set_color(YELLOW)

        a_0_1 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{T_0}",  # 2
            r"\left[",  # 3
            r"\int^{\frac{T_0}{2}}_{0}",  # 4
            r"A",  # 5
            r"\;",  # 6
            r"dt",  # 7
            r"+",  # 8
            r"\int^{T_0}_{\frac{T_0}{2}}",  # 9
            r"-A",  # 10
            r"\;dt",  # 11
            r"\right]",  # 12
            font_size=30,
        ).next_to(eq1, DOWN, buff=0.5)
        a_0_1[0].set_color(RED)
        a_0_1[4].set_color(YELLOW)
        a_0_1[7].set_color(YELLOW)
        a_0_1[9].set_color(YELLOW)
        a_0_1[11].set_color(YELLOW)

        a_0_2 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{T_0}",  # 2
            r"\left[",  # 3
            r"A",  # 4
            r"\left[\,",  # 5
            r"t\,",  # 6
            r"\right] ^{\frac{T_0}{2}}_{0}",  # 7
            r"-",  # 8
            r"A",  # 9
            r"\left[\,",  # 10
            r"t\,",  # 11
            r"\right] ^{T_0}_{\frac{T_0}{2}}",  # 12
            r"\right]",  # 13
            font_size=30,
        )
        a_0_2[0].set_color(RED)
        a_0_2[5:8].set_color(YELLOW)
        a_0_2[10:13].set_color(YELLOW)

        a_0_3 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{A}{T_0}",  # 2
            r"\left[",  # 3
            r"\left[\,",  # 4
            r"t\,",  # 5
            r"\right] ^{\frac{T_0}{2}}_{0}",  # 6
            r"-",  # 7
            r"\left[\,",  # 8
            r"t\,",  # 9
            r"\right] ^{T_0}_{\frac{T_0}{2}}",  # 10
            r"\right]",  # 11
            font_size=30,
        )
        a_0_3[0].set_color(RED)
        a_0_3[4:7].set_color(YELLOW)
        a_0_3[8:11].set_color(YELLOW)

        a_0_4 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{A}{T_0}",  # 2
            r"\left[",  # 3
            r"\frac{T_0}{2}",  # 4
            r"-0",  # 5
            r"-",  # 6
            r"(",  # 7
            r"T_0",  # 8
            r"- \frac{T_0}{2}",  # 9
            r")",  # 10
            r"\right]",  # 11
            font_size=30,
        )
        a_0_4[0].set_color(RED)
        a_0_4[4:6].set_color(YELLOW)
        a_0_4[7:11].set_color(YELLOW)

        a_0_5 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{A}{T_0}",  # 2
            r"\left[",  # 3
            r"\frac{T_0}{2}",  # 4
            r"- T_0",  # 8
            r"+ \frac{T_0}{2}",  # 9
            r"\right]",  # 11
            font_size=30,
        )
        a_0_5[0].set_color(RED)
        a_0_5[4:7].set_color(YELLOW)

        a_0_6 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{A}{T_0}",  # 2
            r"\left[",  # 3
            r"T_0",  # 4
            r"- T_0",  # 8
            r"\right]",  # 11
            font_size=30,
        )
        a_0_6[0].set_color(RED)
        a_0_6[4:6].set_color(YELLOW)
        a_0_7 = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"0",
            font_size=30,
        )
        a_0_7[0].set_color(RED)
        a_0_7[4:6].set_color(YELLOW)

        res_group_copy = res_group.copy()
        a_0_7_copy = a_0_7.copy()
        res_group_copy.move_to(a_0_7_copy)
        res_group_copy.to_edge(DOWN, buff=0.4)
        axes_copy = res_group_copy[0]
        pos_area_sq = Polygon(
            axes_copy.coords_to_point(0, 0),
            axes_copy.coords_to_point(1, 0),
            axes_copy.coords_to_point(1, 1),
            axes_copy.coords_to_point(0, 1),
            color=GREEN,
            fill_opacity=0.3,
            stroke_width=2,
        )
        neg_area_sq = Polygon(
            axes_copy.coords_to_point(1, 0),
            axes_copy.coords_to_point(1, -1),
            axes_copy.coords_to_point(2, -1),
            axes_copy.coords_to_point(2, 0),
            color=RED,
            fill_opacity=0.3,
            stroke_width=2,
        )
        a_0_aux = MathTex(
            r"a_0",  # 0
            r"=",  # 1
            r"\frac{1}{T_0}",  # 2
            r"\int^{T_0}_{0}",  # 4
            r"x(t)",  # 5
            r"\;",  # 6
            r"dt",  # 7
            font_size=30,
        ).next_to(res_group_copy, LEFT, buff=1)

        ## End of finding a_0

        ## finding a_n
        a_n = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2}{T_0}",  # 2
            r"\left[",  # 3
            r"\int_{0}^{\frac{T_0}{2}}",  # 4
            r"x(t)",  # 5
            r"\, \cos(n \omega t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int_{\frac{T_0}{2}}^{T_0}",  # 9
            r"x(t)",  # 10
            r"\, \cos(n \omega t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=30,
        )
        a_n[0].set_color(RED)
        a_n[4].set_color(YELLOW)
        a_n[7].set_color(YELLOW)
        a_n[9].set_color(YELLOW)
        a_n[12].set_color(YELLOW)

        a_n_1 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2}{T_0}",  # 2
            r"\left[",  # 3
            r"\int_{0}^{\frac{T_0}{2}}",  # 4
            r"A",  # 5
            r"\, \cos(n \omega t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int_{\frac{T_0}{2}}^{T_0}",  # 9
            r"-A",  # 10
            r"\, \cos(n \omega t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=30,
        )
        a_n_1[0].set_color(RED)
        a_n_1[4].set_color(YELLOW)
        a_n_1[7].set_color(YELLOW)
        a_n_1[9].set_color(YELLOW)
        a_n_1[12].set_color(YELLOW)

        a_n_2 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2 A}{T_0}",  # 2
            r"\left[",  # 3
            r"\int_{0}^{\frac{T_0}{2}}",  # 4
            r"\, \cos(n \omega t)",  # 5
            r"\, dt",  # 6
            r"-",  # 7
            r"\int_{\frac{T_0}{2}}^{T_0}",  # 8
            r"\, \cos(n \omega t)",  # 9
            r"\, dt",  # 10
            r"\right]",  # 11
            font_size=30,
        )
        a_n_2[0].set_color(RED)
        a_n_2[4].set_color(YELLOW)
        a_n_2[6].set_color(YELLOW)
        a_n_2[8].set_color(YELLOW)
        a_n_2[10].set_color(YELLOW)

        a_n_3 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2 A}{T_0}",  # 2
            r"\Bigg[",  # 3
            r"\left[",  # 4
            r"\frac{1}{n \omega }",  # 5
            r"\sin(n \omega t)",  # 6
            r"\right]_{0}^{\frac{T_0}{2}}",  # 7
            r"-\;",  # 8
            r"\left[",  # 9
            r"\frac{1}{n \omega}",  # 10
            r"\sin(n \omega t)",  # 11
            r"\right]_{\frac{T_0}{2}}^{T_0}",  # 12
            r"\Bigg]",  # 13
            font_size=30,
        )

        a_n_3[0].set_color(RED)
        a_n_3[4].set_color(YELLOW)
        a_n_3[7].set_color(YELLOW)
        a_n_3[9].set_color(YELLOW)
        a_n_3[12].set_color(YELLOW)

        a_n_4 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2 A}{T_0 n \omega}",  # 2
            r"\Bigg[",  # 3
            r"\left[",  # 4
            r"\sin(n \omega t)",  # 5
            r"\right]_{0}^{\frac{T_0}{2}}",  # 6
            r"-\;",  # 7
            r"\left[",  # 8
            r"\sin(n \omega t)",  # 9
            r"\right]_{\frac{T_0}{2}}^{T_0}",  # 10
            r"\Bigg]",  # 11
            font_size=30,
        )

        a_n_4[0].set_color(RED)
        a_n_4[4].set_color(YELLOW)
        a_n_4[6].set_color(YELLOW)
        a_n_4[8].set_color(YELLOW)
        a_n_4[10].set_color(YELLOW)
        omega_formula = MathTex(
            r"\omega",
            r"=",
            r"\frac{2\pi}{T_0}",
            font_size=30,
            color=ORANGE,
        ).next_to(a_n_4, RIGHT, buff=1.5)

        a_n_5 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{2 A T_0 }{T_0 n 2\pi}",  # 2
            r"\Bigg[",  # 3
            r"\left[",  # 4
            r"\sin(n \frac{2\pi}{T_0} \, t)",  # 5
            r"\right]_{0}^{\frac{T_0}{2}}",  # 6
            r"-\;",  # 7
            r"\left[",  # 8
            r"\sin(n \frac{2\pi}{T_0} \, t)",  # 9
            r"\right]_{\frac{T_0}{2}}^{T_0}",  # 10
            r"\Bigg]",  # 11
            font_size=30,
        )

        a_n_5[0].set_color(RED)
        a_n_5[4].set_color(YELLOW)
        a_n_5[6].set_color(YELLOW)
        a_n_5[8].set_color(YELLOW)
        a_n_5[10].set_color(YELLOW)

        a_n_6 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{ A  }{ n \pi}",  # 2
            r"\Bigg[",  # 3
            r"\left[",  # 4
            r"\sin(n \frac{2\pi}{T_0} \, t)",  # 5
            r"\right]_{0}^{\frac{T_0}{2}}",  # 6
            r"-\;",  # 7
            r"\left[",  # 8
            r"\sin(n \frac{2\pi}{T_0} \, t)",  # 9
            r"\right]_{\frac{T_0}{2}}^{T_0}",  # 10
            r"\Bigg]",  # 11
            font_size=30,
        )

        a_n_6[0].set_color(RED)
        a_n_6[4].set_color(YELLOW)
        a_n_6[6].set_color(YELLOW)
        a_n_6[8].set_color(YELLOW)
        a_n_6[10].set_color(YELLOW)

        a_n_7 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{ A }{ n \pi}",  # 2
            r"\Bigg[",  # 3
            r"\sin(n \frac{2\pi}{T_0} \, \frac{T_0}{2})",  # 4
            r"-",  # 5
            r"\sin(n \frac{2\pi}{T_0} \, 0)",  # 6
            r"-\;",  # 7
            r"(",  # 8
            r"\sin(n \frac{2\pi}{T_0} \, T_0)",  # 9
            r"-",  # 10
            r"\sin(n \frac{2\pi}{T_0} \, \frac{T_0}{2})",  # 11
            r")",  # 12
            r"\Bigg]",  # 13
            font_size=30,
        ).next_to(a_n_6, DOWN, buff=0.5)

        a_n_7[0].set_color(RED)
        a_n_7[4].set_color(YELLOW)
        a_n_7[6].set_color(YELLOW)
        a_n_7[9].set_color(YELLOW)
        a_n_7[11].set_color(YELLOW)

        a_n_8 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{ A }{ n \pi}",  # 2
            r"\Bigg[",  # 3
            r"\sin(n \frac{2\pi}{2})",  # 4
            r"-",  # 5
            r"\sin(n \frac{2\pi}{T_0} \, 0)",  # 6
            r"-\;",  # 7
            r"(",  # 8
            r"\sin(n 2\pi)",  # 9
            r"-",  # 10
            r"\sin(n \frac{2\pi}{2})",  # 11
            r")",  # 12
            r"\Bigg]",  # 13
            font_size=30,
        ).next_to(a_n_6, DOWN, buff=0.5)

        a_n_8[0].set_color(RED)
        a_n_8[4].set_color(YELLOW)
        a_n_8[6].set_color(YELLOW)
        a_n_8[9].set_color(YELLOW)
        a_n_8[11].set_color(YELLOW)

        a_n_9 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{ A }{ n \pi}",  # 2
            r"\Bigg[",  # 3
            r"\sin(n \pi)",  # 4
            r"-",  # 5
            r"\sin(0)",  # 6
            r"-\;",  # 7
            r"(",  # 8
            r"\sin(2 n\pi)",  # 9
            r"-",  # 10
            r"\sin(n \pi)",  # 11
            r")",  # 12
            r"\Bigg]",  # 13
            font_size=30,
        ).next_to(a_n_6, DOWN, buff=0.5)

        a_n_9[0].set_color(RED)
        a_n_9[4].set_color(YELLOW)
        a_n_9[6].set_color(YELLOW)
        a_n_9[9].set_color(YELLOW)
        a_n_9[11].set_color(YELLOW)

        zero_n_9 = MathTex(r"0", font_size=30, color=YELLOW).move_to(
            a_n_9[6].get_center()
        )

        a_n_10 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{ A }{ n \pi}",  # 2
            r"\Bigg[",  # 3
            r"\sin(n \pi)",  # 4
            r"-",  # 7
            r"\sin(2 n\pi)",  # 8
            r"+",  # 9
            r"\sin(n \pi)",  # 10
            r"\Bigg]",  # 11
            font_size=30,
        ).next_to(a_n_6, DOWN, buff=0.5)

        a_n_10[0].set_color(RED)
        a_n_10[4].set_color(YELLOW)
        a_n_10[6].set_color(YELLOW)
        a_n_10[8].set_color(YELLOW)

        a_n_11 = MathTex(
            r"a_n",  # 0
            r"=",  # 1
            r"\frac{ A }{ n \pi}",  # 2
            r"\Bigg[",  # 3
            r"2\, \sin(n \pi)",  # 4
            r"-",  # 5
            r"\sin(2 n\pi)",  # 6
            r"\Bigg]",  # 7
            font_size=30,
        ).next_to(a_n_6, DOWN, buff=0.5)

        a_n_11[0].set_color(RED)
        a_n_11[4].set_color(YELLOW)
        a_n_11[6].set_color(YELLOW)

        cir = Circle(radius=1.5, color=YELLOW).to_edge(RIGHT, buff=1).shift(0.5 * UP)
        circle_center = cir.get_center()

        # Horizontal line (x-axis)
        h_line = Line(
            circle_center + LEFT * 1.5,
            circle_center + RIGHT * 1.5,
            color=BLUE,
            stroke_width=2,
        )

        # Vertical line (y-axis)
        v_line = Line(
            circle_center + DOWN * 1.5,
            circle_center + UP * 1.5,
            color=BLUE,
            stroke_width=2,
        )

        # Create angle labels
        angles = [0, PI / 2, PI, 3 * PI / 2]
        angle_labels = [r"0 \; 2\pi", "\\frac{\\pi}{2}", "\\pi", "\\frac{3\\pi}{2}"]

        labels_group = VGroup()

        for angle, label_text in zip(angles, angle_labels):
            # Calculate position on circle circumference
            label_pos = circle_center + 1.8 * np.array(
                [np.cos(angle), np.sin(angle), 0]
            )

            label = MathTex(label_text, font_size=24, color=WHITE)
            label.move_to(label_pos)
            labels_group.add(label)

        # Create dots at the cardinal points
        cardinal_dots = VGroup()
        cardinal_points = [
            circle_center + 1.5 * RIGHT,  # 0 radians (right)
            circle_center + 1.5 * UP,  # π/2 radians (top)
            circle_center + 1.5 * LEFT,  # π radians (left)
            circle_center + 1.5 * DOWN,  # 3π/2 radians (bottom)
        ]

        for point in cardinal_points:
            dot = Dot(point, radius=0.04, color=WHITE)
            cardinal_dots.add(dot)

        # Group everything together
        circle_with_axes = VGroup(cir, h_line, v_line, labels_group, cardinal_dots)
        circle_with_axes.to_edge(RIGHT, buff=1.5).shift(DOWN * 2)
        dot_circle = Dot(radius=0.09, color=BLUE)

        zero_n_11 = (
            MathTex(r"0", font_size=30, color=YELLOW)
            .move_to(a_n_11[6].get_center())
            .shift(2 * LEFT)
        )
        half_circle1 = (
            Arc(
                radius=1.5,  # نفس نصف قطر الدائرة الأصلية
                start_angle=0,
                angle=PI,  # 180 درجة فقط
                color=BLUE,
                arc_center=circle_center,
            )
            .to_edge(RIGHT, buff=2.03)
            .shift(DOWN * 2)
        )
        half_circle2 = (
            Arc(
                radius=1.5,  # نفس نصف قطر الدائرة الأصلية
                start_angle=PI,
                angle=PI,  # 180 درجة فقط
                color=BLUE,
                arc_center=circle_center,
            )
            .to_edge(RIGHT, buff=2.03)
            .shift(DOWN * 2)
        )
        zero_n_11_2 = (
            MathTex(r"0", font_size=30, color=YELLOW)
            .move_to(a_n_11[4].get_center())
            .shift(2 * LEFT)
        )

        a_n_12 = (
            MathTex(
                r"a_n",  # 0
                r"=",  # 1
                r"\frac{A}{n \pi}",  # 2
                r"\left[",
                r"0",
                r"\right]",  # 7
                font_size=30,
            )
            .next_to(a_n_6, DOWN, buff=0.5)
            .shift(2 * LEFT)
        )

        a_n_12[0].set_color(RED)
        a_n_12[4].set_color(YELLOW)
        a_n_13 = (
            MathTex(
                r"a_n",  # 0
                r"=",  # 1
                r"0",
                font_size=30,
            )
            .next_to(a_n_6, DOWN, buff=0.5)
            .shift(2 * LEFT)
        )
        a_n_13[0].set_color(RED)

        ## finding b_n
        b_n_1 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{2}{T_0}",  # 2
            r"\left[",  # 3
            r"\int_{0}^{\frac{T_0}{2}}",  # 4
            r"x(t)",  # 5
            r"\, \sin(n \omega t)",  # 6
            r"\, dt",  # 7
            r"+",  # 8
            r"\int_{\frac{T_0}{2}}^{T_0}",  # 9
            r"x(t)",  # 10
            r"\, \sin(n \omega t)",  # 11
            r"\, dt",  # 12
            r"\right]",  # 13
            font_size=30,
        )
        b_n_1[0].set_color(RED)
        b_n_1[4].set_color(YELLOW)
        b_n_1[7].set_color(YELLOW)
        b_n_1[9].set_color(YELLOW)
        b_n_1[12].set_color(YELLOW)
        b_n_2 = MathTex(
            r"b_n",  # 0
            r"=",
            r"\frac{2}{T_0}",  # 3
            r"\int_{0}^{\frac{T_0}{2}}",  # 4
            r"x(t)",  # 5
            r"\, \sin(n \omega t)",  # 6
            r"\, dt",  # 7
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_2[0].set_color(RED)
        b_n_2[2].set_color(RED)
        b_n_2[3].set_color(YELLOW)
        b_n_2[6].set_color(YELLOW)
        b_n_3 = MathTex(
            r"b_n",  # 0
            r"=",
            r"2\,",  # 2
            r"\frac{2}{T_0}",  # 3
            r"\int_{0}^{\frac{T_0}{2}}",  # 4
            r"x(t)",  # 5
            r"\, \sin(n \omega t)",  # 6
            r"\, dt",  # 7
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_3[0].set_color(RED)
        b_n_3[2].set_color(RED)
        b_n_3[4].set_color(YELLOW)
        b_n_3[7].set_color(YELLOW)

        b_n_4 = MathTex(
            r"b_n",  # 0
            r"=",
            r"2\,",  # 2
            r"\frac{2}{T_0}",  # 3
            r"\int_{0}^{\frac{T_0}{2}}",  # 4
            r"A",  # 5
            r"\, \sin(n \omega t)",  # 6
            r"\, dt",  # 7
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_4[0].set_color(RED)
        b_n_4[2].set_color(RED)
        b_n_4[4].set_color(YELLOW)
        b_n_4[7].set_color(YELLOW)

        b_n_5 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{4 A}{T_0}",  # 2
            r"\int_{0}^{\frac{T_0}{2}}",  # 3
            r" \sin(n \omega t)",  # 4
            r"\, dt",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_5[0].set_color(RED)
        b_n_5[3].set_color(YELLOW)
        b_n_5[5].set_color(YELLOW)

        b_n_6 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 4 A }{ T_0}",  # 2
            r"\Bigg[",  # 3
            r"- \frac{1}{n \omega}",  # 4
            r"\cos(n \omega t)",  # 6
            r"\Bigg]_{0}^{\frac{T_0}{2}}",  # 7
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_6[0].set_color(RED)
        b_n_6[3].set_color(YELLOW)
        b_n_6[6].set_color(YELLOW)

        b_n_7 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 4 A }{ T_0 n \omega}",  # 2
            r"\Bigg[",
            r"-",  # 3
            r"\cos(n \omega t)",  # 4
            r"\Bigg]_{0}^{\frac{T_0}{2}}",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_7[0].set_color(RED)
        b_n_7[3].set_color(YELLOW)
        b_n_7[6].set_color(YELLOW)
        omega_formula_copy = omega_formula.copy()
        omega_formula_copy.next_to(b_n_7, RIGHT, buff=2)

        b_n_8 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 4 A T_0 }{ T_0 n 2 \pi}",  # 2
            r"\Bigg[",  # 3
            r"-",
            r"\cos(n \frac{2 \pi}{T_0})",  # 4
            r"\Bigg]_{0}^{\frac{T_0}{2}}",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_8[0].set_color(RED)
        b_n_8[3].set_color(YELLOW)
        b_n_8[6].set_color(YELLOW)

        b_n_9 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 2 A  }{ n \pi}",  # 2
            r"\Bigg[",
            r"-",  # 3
            r"\cos(n \frac{2 \pi}{T_0})",  # 4
            r"\Bigg]_{0}^{\frac{T_0}{2}}",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_9[0].set_color(RED)
        b_n_9[3].set_color(YELLOW)
        b_n_9[6].set_color(YELLOW)

        b_n_10 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 2 A  }{ n \pi}",  # 2
            r"\Bigg[",  # 3
            r"-",
            r"\cos(n \frac{2 \pi}{T_0} \frac{T_0}{2})",
            r"+",
            r"\cos(n \frac{2 \pi}{T_0} 0)",
            r"\Bigg]",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_10[0].set_color(RED)
        b_n_10[5].set_color(YELLOW)
        b_n_10[7].set_color(YELLOW)

        b_n_11 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 2 A  }{ n \pi}",  # 2
            r"\Bigg[",
            r"-",  # 3
            r"\cos(n \frac{2 \pi}{T_0} \frac{T_0}{2})",
            r"+",
            r"1",
            r"\Bigg]",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_11[0].set_color(RED)
        b_n_11[5].set_color(YELLOW)
        b_n_11[7].set_color(YELLOW)

        b_n_12 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 2 A  }{ n \pi}",  # 2
            r"\Bigg[",
            r"-",  # 3
            r"\cos(n \pi)",
            r"+",
            r"1",
            r"\Bigg]",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_12[0].set_color(RED)
        b_n_12[5].set_color(YELLOW)

        b_n_13 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 2 A  }{ n \pi}",  # 2
            r"\left[",
            r"1",
            r"-",  # 3
            r"\cos(n \pi)",
            r"\right]",  # 5
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_13[0].set_color(RED)
        b_n_13[6].set_color(YELLOW)

        cos_np_1 = MathTex(
            r"\cos(n \pi)",
            "=",
            r"\begin{cases}"
            r"\;-1 & \text{; } n \; odd \\"
            r"\; 1  & \text{; } n \; even"
            r"\end{cases}",
            font_size=30,
        ).next_to(b_n_13, DOWN, buff=0.5)
        cos_np_1[0].set_color(YELLOW)

        cos_np_2 = MathTex(
            r"-",
            r"\cos(n \pi)",
            "=",
            r"\begin{cases}"
            r"\;1 & \text{; } n \; odd \\"
            r"\; -1  & \text{; } n \; even"
            r"\end{cases}",
            font_size=30,
        ).next_to(b_n_13, DOWN, buff=0.5)
        cos_np_2[1].set_color(YELLOW)

        cos_np_3 = MathTex(
            r"1",
            r"-",
            r"\cos(n \pi)",
            "=",
            r"\begin{cases}"
            r"\;2 & \text{; } n \; odd \\"
            r"\; 0  & \text{; } n \; even"
            r"\end{cases}",
            font_size=30,
        ).next_to(b_n_13, DOWN, buff=0.5)
        cos_np_3[2].set_color(YELLOW)
        b_n_13_2 = MathTex(r"\: 2", font_size=30)
        b_n_14 = MathTex(
            r"b_n",  # 0
            r"=",  # 1
            r"\frac{ 4 A  }{ n \pi}",  # 2
            font_size=30,
        ).next_to(b_n_1, DOWN, buff=0.5)
        b_n_14[0].set_color(RED)

        # animatieng the fourier solution
        eq2 = MathTex(
            r"x(t)",  # 0
            r"=",  # 1
            r"\sum^{\infty}_{n=1}",
            r"b_n",  # 11
            r"\; sin(",  # 12
            r"n \omega t",  # 13
            r")",  # 14
            font_size=30,
        )
        eq2[3].set_color(RED)
        eq3 = MathTex(
            r"x(t)",  # 0
            r"=",  # 1
            r"\sum^{\infty}_{n=1}",
            r"\frac{ 4 A  }{ n \pi}",  # 11
            r"\; sin(",  # 12
            r"n \omega t",  # 13
            r")",  # 14
            font_size=30,
        )

        n_odd = MathTex(
            r"n",
            r":=",
            r"(2n-1)",
            font_size=30,
            color=ORANGE,
        )

        eq4 = MathTex(
            r"x(t)",  # 0
            r"=",  # 1
            r"\sum^{\infty}_{n=1}",
            r"\frac{ 4 A  }{ (2n-1) \pi}",  # 11
            r"\; sin(",  # 12
            r"(2n-1) \omega t",  # 13
            r")",  # 14
            font_size=30,
        )
        sin_wave_1 = MathTex(r"\frac{4}{\pi} \sin(\pi t)", font_size=30, color=GOLD_A)
        sin_wave_2 = MathTex(r"\frac{4}{3 \pi} \sin(3\pi t)", font_size=30, color=PINK)
        sin_wave_3 = MathTex(r"\frac{4}{5 \pi} \sin(5\pi t)", font_size=30, color=GREEN)
        sin_wave_4 = MathTex(
            r"\frac{4}{7 \pi} \sin(7\pi t)", font_size=30, color=ORANGE
        )
        sin_wave_formulas = VGroup(
            sin_wave_1, sin_wave_2, sin_wave_3, sin_wave_4
        ).arrange(RIGHT, buff=1)
        eq5 = MathTex(
            r"x(t)",  # 0
            r"=",  # 1
            r"\sum^{\infty}_{n=1}",
            r"\frac{ 4 }{ (2n-1) \pi}",  # 11
            r"\; sin(",  # 12
            r"(2n-1) \pi t",  # 13
            r")",  # 14
            font_size=30,
        )
        A_val = MathTex(r"A", r"=", r"1", font_size=30, color=ORANGE)
        T_val = MathTex(r"T_0", r"=", r"2", r"\; s", font_size=30, color=ORANGE)
        omega_val = MathTex(
            r"\omega",
            r"=",
            r"\frac{2\pi}{T_0}",
            r"=",
            r"\pi",
            r"\; rad.s^{-1}",
            font_size=30,
            color=ORANGE,
        )
        vals = VGroup(A_val, T_val, omega_val).arrange(DOWN, buff=0.5)
        # n_labels = VGroup()
        # final_sin_waves_lab = VGroup()
        # for i in range(4):
        #     n_lab = MathTex(
        #         f"n={i+1}", font_size=30, color=sin_wave_formulas[i].get_color()
        #     )
        #     n_lab.next_to(sin_wave_formulas[i], UP, buff=0.2)
        #     final_sin_waves_lab.add(VGroup(n_lab, sin_wave_formulas[i]))

        # ------------- End solution section -------------
        # self.play(Create(res_group), run_time=2)
        # self.wait()
        # self.play(Write(signal_def))
        # self.wait()
        # self.play(Write(the_question, reverse=True))
        # self.add(the_question)
        # self.wait()
        # self.play(FadeIn(lines12))
        # self.wait()
        self.play(
            FadeOut(the_question, res_group, lines12),
            signal_def.animate.move_to(ORIGIN).shift(3 * UP).scale(0.7),
        )
        self.wait()
        self.play(
            Write(eq1[0]),
            Write(eq1[1]),
        )
        self.wait()
        self.play(
            Write(eq1[4]),
            Write(eq1[9]),
            Write(eq1[10]),
        )
        self.wait()
        self.play(
            Write(eq1[6]),
            Write(eq1[8]),
            Write(eq1[12]),
            Write(eq1[14]),
        )
        self.wait()
        self.play(
            Write(eq1[7]),
            Write(eq1[13]),
        )
        self.wait()
        self.play(
            Write(eq1[5]),
            Write(eq1[11]),
        )
        self.play(
            Write(eq1[2]),
            Write(eq1[3]),
        )
        self.wait()
        self.play(eq1.animate.next_to(signal_def, DOWN, buff=0.5))
        self.wait()
        # a_0.next_to(eq1, DOWN, buff=0.5)
        # self.play(Write(a_0))
        # self.wait()
        # a_0_1.move_to(a_0)
        # self.play(TransformMatchingTex(a_0, a_0_1))
        # self.wait()
        # a_0_2.move_to(a_0_1)
        # self.play(TransformMatchingTex(a_0_1, a_0_2))
        # self.wait()
        # rec1 = SurroundingRectangle(a_0_2[4], color=ORANGE, stroke_width=3, buff=0.1)
        # rec2 = SurroundingRectangle(a_0_2[9], color=ORANGE, stroke_width=3, buff=0.1)
        # self.play(Create(rec1), Create(rec2))
        # self.wait()
        # a_0_3.move_to(a_0_2)
        # self.play(TransformMatchingShapes(a_0_2, a_0_3), FadeOut(rec1, rec2))
        # self.wait()
        # a_0_4.move_to(a_0_3)
        # self.play(TransformMatchingTex(a_0_3, a_0_4))
        # self.wait()
        # a_0_5.move_to(a_0_4)
        # self.play(TransformMatchingTex(a_0_4, a_0_5))
        # self.wait()
        # a_0_6.move_to(a_0_5)
        # self.play(TransformMatchingShapes(a_0_5, a_0_6))
        # self.wait()
        # a_0_7.move_to(a_0_6)
        # self.play(TransformMatchingShapes(a_0_6, a_0_7))
        # self.wait()
        # a_0_7_copy.move_to(a_0_7)
        # self.add(a_0_7_copy)
        # self.play(FadeOut(a_0_7))
        # self.play(ReplacementTransform(a_0_7_copy, res_group_copy), run_time=2)
        # self.wait()
        # original_width = axes_copy.x_axis.stroke_width
        # original_color = axes_copy.x_axis.get_stroke_color()
        # self.play(axes_copy.x_axis.animate.set_stroke(width=5, color=YELLOW))
        # self.wait()
        # self.play(
        #     axes_copy.x_axis.animate.set_stroke(
        #         width=original_width, color=original_color
        #     )
        # )
        # self.wait()
        # self.play(Write(a_0_aux))
        # self.wait()
        # self.play(Create(pos_area_sq), Create(neg_area_sq), run_time=2)
        # self.wait()
        # self.play(Rotate(neg_area_sq, PI, about_point=axes_copy.coords_to_point(1, 0)))
        # self.wait()
        # self.play(FadeOut(res_group_copy, pos_area_sq, neg_area_sq, a_0_aux))

        # self.play(FadeIn(a_0_7))
        # self.wait()
        # self.play(a_0_7.animate.next_to(eq1, LEFT, buff=1.5).shift(1 * UP))
        # self.wait()

        # self.play(Write(a_n))
        # self.wait()
        # self.play(TransformMatchingTex(a_n, a_n_1))
        # self.wait()
        # rec1 = SurroundingRectangle(a_n_1[5], color=ORANGE, stroke_width=3, buff=0.1)
        # rec2 = SurroundingRectangle(a_n_1[10], color=ORANGE, stroke_width=3, buff=0.1)
        # self.play(Create(rec1), Create(rec2))
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_1, a_n_2), FadeOut(rec1, rec2))
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_2, a_n_3))
        # self.wait()
        # rec1 = SurroundingRectangle(a_n_3[5], color=ORANGE, stroke_width=3, buff=0.1)
        # rec2 = SurroundingRectangle(a_n_3[10], color=ORANGE, stroke_width=3, buff=0.1)
        # self.play(Create(rec1), Create(rec2))
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_3, a_n_4), FadeOut(rec1, rec2))
        # self.wait()
        # self.play(Write(omega_formula))
        # self.wait()
        # self.play(TransformMatchingTex(a_n_4, a_n_5))
        # self.wait()
        # rec = SurroundingRectangle(a_n_5[2], color=ORANGE, stroke_width=3, buff=0.1)
        # self.play(Create(rec))
        # self.wait()
        # self.play(TransformMatchingTex(a_n_5, a_n_6), FadeOut(rec))
        # self.wait()
        # self.play(FadeOut(omega_formula))
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_6.copy(), a_n_7), run_time=3)
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_7, a_n_8), run_time=2)
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_8, a_n_9), run_time=2)
        # self.wait()
        # self.play(ReplacementTransform(a_n_9[6], zero_n_9))
        # self.wait()
        # self.play(TransformMatchingTex(a_n_9, a_n_10))
        # self.wait()
        # self.play(TransformMatchingTex(a_n_10, a_n_11))
        # self.wait()
        # self.play(
        #     a_n_11.animate.shift(2 * LEFT),
        #     a_n_6.animate.shift(2 * LEFT),
        #     Create(h_line),
        #     Create(v_line),
        #     Create(labels_group),
        #     Create(cardinal_dots),
        #     Create(cir),
        #     run_time=2,
        # )
        # self.wait()
        # rec = SurroundingRectangle(a_n_11[6], color=ORANGE, stroke_width=3, buff=0.1)
        # self.play(Create(rec))
        # self.wait()
        # dot_circle.move_to(cir.get_start())
        # self.play(FadeIn(dot_circle))
        # self.play(
        #     MoveAlongPath(dot_circle, cir, run_time=3, rate_func=smooth),
        # )
        # self.wait()
        # self.play(ReplacementTransform(a_n_11[6], zero_n_11), FadeOut(rec))
        # self.wait()
        # rec = SurroundingRectangle(a_n_11[4], color=ORANGE, stroke_width=3, buff=0.1)
        # self.play(Create(rec))
        # self.wait()
        # dot_circle.move_to(half_circle1.get_start())
        # self.play(
        #     MoveAlongPath(dot_circle, half_circle1, run_time=1.5),
        # )
        # self.wait()
        # dot_circle.move_to(half_circle2.get_start())
        # self.play(
        #     MoveAlongPath(dot_circle, half_circle2, run_time=1.5),
        # )
        # self.wait()
        # self.play(ReplacementTransform(a_n_11[4], zero_n_11_2), FadeOut(rec))
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_11, a_n_12))
        # self.wait()
        # self.play(TransformMatchingShapes(a_n_12, a_n_13))
        # self.wait()
        # self.play(
        #     FadeOut(circle_with_axes, dot_circle),
        #     a_n_13.animate.shift(RIGHT * 2),
        #     a_n_6.animate.shift(RIGHT * 2),
        # )
        # self.wait()
        # self.play(a_n_13.animate.move_to(a_n_6), FadeOut(a_n_6))
        # self.wait()
        # self.play(a_n_13.animate.next_to(a_0_7, DOWN, buff=0.5))
        # self.wait()
        # ## Fading Out all
        # self.play(FadeOut(a_0_7, a_n_13, signal_def, eq1))
        # self.wait()
        # ## Fading In back all
        # self.play(FadeIn(a_0_7, a_n_13, signal_def, eq1))
        # self.wait()
        # ## b_n animations
        # self.play(Write(b_n_1))
        # self.wait()
        # self.play(TransformMatchingTex(b_n_1.copy(), b_n_2), run_time=2)
        # self.wait()
        # self.play(TransformMatchingTex(b_n_2, b_n_3))
        # self.wait()
        # self.play(TransformMatchingTex(b_n_3, b_n_4))
        # self.wait()
        # self.play(TransformMatchingShapes(b_n_4, b_n_5))
        # self.wait()
        # self.play(TransformMatchingShapes(b_n_5, b_n_6))
        # self.wait()
        # self.play(TransformMatchingShapes(b_n_6, b_n_7))
        # self.wait()
        # self.play(Write(omega_formula_copy))
        # self.wait()
        # self.play(TransformMatchingTex(b_n_7, b_n_8))
        # self.wait()
        # self.play(TransformMatchingTex(b_n_8, b_n_9))
        # self.wait()
        # self.play(FadeOut(omega_formula_copy))
        # self.wait()
        # self.play(TransformMatchingShapes(b_n_9, b_n_10), run_time=2)
        # self.wait()
        # self.play(TransformMatchingShapes(b_n_10, b_n_11))
        # self.wait()
        # self.play(TransformMatchingShapes(b_n_11, b_n_12))
        # self.wait()
        # self.play(TransformMatchingShapes(b_n_12, b_n_13))
        # self.wait()
        # self.play(
        #     b_n_1.animate.shift(2 * LEFT),
        #     b_n_13.animate.shift(2 * LEFT),
        #     Create(h_line),
        #     Create(v_line),
        #     Create(labels_group),
        #     Create(cardinal_dots),
        #     Create(cir),
        #     run_time=2,
        # )
        # self.wait()
        # dot_circle.move_to(cir.get_start())
        # self.play(FadeIn(dot_circle))
        # dot_circle.move_to(half_circle1.get_start())
        # self.play(
        #     MoveAlongPath(dot_circle, half_circle1, run_time=1.5),
        # )
        # self.wait()
        # dot_circle.move_to(half_circle2.get_start())
        # self.play(
        #     MoveAlongPath(dot_circle, half_circle2, run_time=1.5),
        # )
        # self.wait()
        # self.play(
        #     FadeOut(circle_with_axes, dot_circle),
        #     b_n_1.animate.shift(RIGHT * 2),
        #     b_n_13.animate.shift(RIGHT * 2),
        # )
        # self.wait()
        # self.play(Write(cos_np_1))
        # self.wait()
        # self.play(TransformMatchingTex(cos_np_1, cos_np_2))
        # self.wait()
        # self.play(TransformMatchingTex(cos_np_2, cos_np_3))
        # self.wait()
        # to_two = VGroup(b_n_13[3:8])
        # b_n_13_2.move_to(to_two.get_left() + 0.1 * RIGHT)
        # self.play(
        #     FadeOut(cos_np_3),
        #     ReplacementTransform(b_n_13[3:8], b_n_13_2),
        # )
        # self.wait()
        # self.play(
        #     LaggedStart(
        #         FadeOut(b_n_13_2),
        #         TransformMatchingShapes(b_n_13, b_n_14),
        #         lag_ratio=0.2,
        #     )
        # )
        # self.wait()
        # self.play(FadeOut(b_n_1))
        # self.wait()
        self.play(b_n_14.animate.next_to(a_n_13, DOWN, buff=0.5))
        self.wait()
        eq2.next_to(eq1, DOWN, buff=0.5)
        self.play(ReplacementTransform(eq1.copy(), eq2), FadeOut(a_0_7, a_n_13))
        self.wait()
        eq3.next_to(eq1, DOWN, buff=0.5)
        self.play(TransformMatchingTex(eq2, eq3), FadeOut(b_n_14))
        self.wait()
        n_odd.next_to(eq3, RIGHT, buff=1.5)
        self.play(Write(n_odd))
        self.wait()
        self.play(TransformMatchingTex(eq3, eq4), FadeOut(n_odd))
        self.wait()
        vals.next_to(eq4, LEFT, buff=1.5)
        self.play(Write(vals), run_time=2)
        self.wait()
        self.play(TransformMatchingShapes(eq4, eq5))
        self.wait()
        self.play(FadeOut(vals))
        self.wait()
        final_sin_waves_lab = VGroup()
        sin_wave_formulas.next_to(eq5, DOWN, buff=1)
        for i in range(4):
            n_lab = MathTex(
                f"n={2*i+1}", font_size=30, color=sin_wave_formulas[i].get_color()
            )
            n_lab.next_to(sin_wave_formulas[i], UP, buff=0.2)
            final_sin_waves_lab.add(VGroup(n_lab, sin_wave_formulas[i]))
        self.play(
            LaggedStart(
                *[TransformFromCopy(eq4, s_w) for s_w in final_sin_waves_lab],
                lag_ratio=1,
            ),
            run_time=4,
        )
        self.wait()
        self.play(FadeOut(eq5, final_sin_waves_lab, signal_def, eq1))
        self.wait()

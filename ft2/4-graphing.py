from manim import *


def ar_text(text, font_size=36):
    return Text(text, font_size=font_size, font="Cairo")


class Grphing(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 4],
            y_range=[-2, 2],
            y_length=4,
            x_length=8,
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
        lines1.shift(LEFT * 2.3).set_opacity(0.2)
        lines2.shift(RIGHT * 2.3).set_opacity(0.2)
        lines12 = VGroup(lines1, lines2)

        title = ar_text("التابع الفردي:", 30).to_corner(UP + RIGHT, buff=0.7)
        odd_function_eq = MathTex(r"f(-x)", r"=", r"-f(x)", font_size=33).next_to(
            res_group, RIGHT, buff=1.5
        )
        odd_function_eq[0].set_color(TEAL)
        odd_function_eq[2].set_color(GREEN)
        pos_a_point = axes.c2p(0.5, 0)
        f_pos_a_point = axes.c2p(0.5, 1)
        neg_a_point = axes.c2p(-0.5, 0)
        f_neg_a_point = axes.c2p(-0.5, -1)
        dot_pos_a = Dot(point=pos_a_point, radius=0.06, color=GREEN)
        dot_neg_a = Dot(point=neg_a_point, color=TEAL, radius=0.06)
        pos_a_point_label = (
            MathTex(r"a", font_size=33)
            .set_color(GREEN)
            .next_to(dot_pos_a, DOWN, buff=0.1)
        )
        neg_a_point_label = (
            MathTex(r"-a", font_size=33)
            .set_color(TEAL)
            .next_to(dot_neg_a, UP, buff=0.1)
        )
        line_pos_a = Line(
            start=pos_a_point,
            end=f_pos_a_point,
            color=GREEN,
            stroke_width=3,
        )
        line_neg_a = Line(
            start=neg_a_point, end=f_neg_a_point, color=TEAL, stroke_width=3
        )
        a_group = VGroup(
            dot_pos_a,
            dot_neg_a,
            pos_a_point_label,
            neg_a_point_label,
            line_pos_a,
            line_neg_a,
        )
        odd_symmetry = ar_text("متناظر بالنسبة للمبدأ", 26).next_to(
            odd_function_eq, DOWN, buff=0.5
        )
        origin_dot = Dot(axes.c2p(0, 0), color=ORANGE, radius=0.06)
        lines_copy = lines[0 : len(lines) - 1].copy()
        lines_copy.rotate(1 * PI, about_point=axes.c2p(0, 0))
        odd_integration = MathTex(
            r"\int_{-T_0}^{T_0} odd", r"=", r"0", font_size=33
        ).next_to(odd_symmetry, DOWN, buff=0.5)
        even_title = ar_text("التابع الزوجي:", 30).to_corner(UP + RIGHT, buff=0.7)

        even_function_eq = MathTex(r"f(-x)", r"=", r"f(x)", font_size=33).next_to(
            res_group, RIGHT, buff=1.5
        )
        even_function_eq[0].set_color(TEAL)
        even_function_eq[2].set_color(GREEN)

        even_symmerty = ar_text("متنظار بالنسبة لمحور التراتيب", 26).next_to(
            even_function_eq, DOWN, buff=0.5
        )
        pos_b_point = axes.c2p(1.0, 0)
        f_pos_b_point = axes.c2p(1.0, 1)
        neg_b_point = axes.c2p(-1.0, 0)
        f_neg_b_point = axes.c2p(-1.0, 1)
        dot_pos_b = Dot(point=pos_b_point, radius=0.06, color=RED)
        dot_neg_b = Dot(point=neg_b_point, color=PURPLE, radius=0.06)
        pos_b_point_label = (
            MathTex(r"b", font_size=33)
            .set_color(RED)
            .next_to(dot_pos_b, DOWN, buff=0.1)
        )
        neg_b_point_label = (
            MathTex(r"-b", font_size=33)
            .set_color(PURPLE)
            .next_to(dot_neg_b, DOWN, buff=0.1)
        )
        line_pos_b = Line(
            start=pos_b_point,
            end=f_pos_b_point,
            color=RED,
            stroke_width=3,
        )
        line_neg_b = Line(
            start=neg_b_point, end=f_neg_b_point, color=PURPLE, stroke_width=3
        )
        b_group = VGroup(
            dot_pos_b,
            dot_neg_b,
            pos_b_point_label,
            neg_b_point_label,
            line_pos_b,
            line_neg_b,
        )
        cos_graph = axes.plot(
            lambda x: x**2,
            x_range=[-3, 3],
            color=GREEN,
            stroke_width=3,
        )
        sub_cos_graph_pos = axes.plot(
            lambda x: x**2,
            x_range=[0, 3],
            color=YELLOW,
            stroke_width=3,
        )

        # sub_cos_graph_neg = axes.plot(
        #     lambda x: x**2,
        #     x_range=[-3, 0],
        #     color=YELLOW,
        #     stroke_width=3,
        # )
        sub_cos_graph_neg = sub_cos_graph_pos.copy()
        even_integration = MathTex(
            r"\int_{-T_0}^{T_0} even" r"=", r"2 \int_{0}^{T_0} even", font_size=33
        ).next_to(even_symmerty, DOWN, buff=0.5)
        even_area = axes.get_area(cos_graph, [-3, 3], color=GREEN, opacity=0.3)
        self.play(Create(res_group), run_time=2)
        self.wait()
        self.play(FadeIn(lines12))
        self.wait()
        self.play(Write(title, reverse=True))
        self.add(title)
        self.wait()
        self.play(Write(odd_function_eq))
        self.wait()
        self.play(Create(dot_pos_a))
        self.play(Write(pos_a_point_label))
        self.wait()
        self.play(Create(dot_neg_a))
        self.play(Write(neg_a_point_label))
        self.wait()
        self.play(Create(line_pos_a), Create(line_neg_a))
        self.wait()
        self.play(FadeOut(a_group))
        self.wait()
        self.play(Write(odd_symmetry, reverse=True))
        self.add(odd_symmetry)
        self.wait()
        self.play(Create(origin_dot))
        self.wait()
        self.play(TransformFromCopy(lines.copy(), lines_copy), run_time=2)
        self.wait()
        self.play(FadeOut(lines_copy))
        self.wait()
        self.play(Write(odd_integration))
        self.wait()

        self.play(
            FadeOut(
                lines,
                lines12,
                txt1,
                txt2,
                x_label1,
                x_label2,
                odd_symmetry,
                odd_integration,
                odd_function_eq,
                origin_dot,
            )
        )
        self.wait()
        self.play(ReplacementTransform(title, even_title))
        self.wait()
        self.play(Create(cos_graph))
        self.wait()
        self.play(Write(even_function_eq))
        self.wait()
        self.play(Create(dot_pos_b))
        self.play(Write(pos_b_point_label))
        self.wait()
        self.play(Create(dot_neg_b))
        self.play(Write(neg_b_point_label))
        self.wait()
        self.play(Create(line_pos_b), Create(line_neg_b))
        self.wait()
        self.play(FadeOut(b_group))
        self.wait()
        self.play(FadeIn(sub_cos_graph_pos))
        self.wait()
        self.play(Write(even_symmerty, reverse=True))
        self.add(even_symmerty)
        self.wait()

        self.play(
            Rotate(
                sub_cos_graph_neg,
                angle=PI,
                axis=UP,  # Rotate around vertical axis
                about_point=axes.c2p(0, 0),  # Rotate around origin
            ),
            # sub_cos_graph_neg.animate.stretch(-1, 0),
            # Transform(sub_cos_graph_pos.copy(), sub_cos_graph_neg),
            # sub_cos_graph_pos.animate.stretch(-1, 0)  # Flip horizontally
            # .move_to(
            #     axes.c2p(0, 0) - sub_cos_graph_pos.get_start()
            # )  # Move to negative side
            # .set_color(YELLOW),  # Optional: change color
            run_time=2,
            rate_functions=rate_functions.double_smooth,
        )
        self.wait()
        self.play(FadeOut(sub_cos_graph_pos, sub_cos_graph_neg))
        self.wait()
        self.play(Write(even_integration))
        self.wait()
        self.play(FadeIn(even_area))
        self.wait()
        self.play(
            FadeOut(
                even_title,
                even_function_eq,
                even_symmerty,
                cos_graph,
                even_integration,
                axes,
                axes_labels,
                even_area,
            )
        )
        self.wait()

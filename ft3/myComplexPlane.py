from manim import *


def arrow_AB(number_line, a, b, color=YELLOW):
    arrow_2 = Arrow(
        start=number_line.n2p(a),
        end=number_line.n2p(b),
        color=color,
        stroke_width=6,
        buff=0,
        max_tip_length_to_length_ratio=0.25,
    )
    return arrow_2


class MyComplexPlane(Scene):
    def construct(self):
        scale_factor = 1.5
        grid = NumberPlane(
            x_range=[-8 * scale_factor, 8 * scale_factor, 1],
            y_range=[-4 * scale_factor, 4 * scale_factor, 1],
            x_length=12 * scale_factor,
            y_length=6.5 * scale_factor,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3,
            },
            faded_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 0.5,
                "stroke_opacity": 0.1,
            },
            faded_line_ratio=2,
            axis_config={
                "stroke_opacity": 0.1,  # Completely transparent axes
                "stroke_width": 0.5,
                # "stroke_color": BLUE_E
            },
        )
        number_line = NumberLine(
            x_range=[-8, 8, 1],
            length=12,
            include_numbers=True,
            tick_size=0.05,
        )
        point_1 = Dot(number_line.n2p(0), color=RED)
        arrow_02 = arrow_AB(number_line, 0, 2)
        arrow_02_tex = MathTex(r"\vec{v}", r"=" r"2").next_to(arrow_02, UP, buff=0.2)
        arrow_02_tex[0].set_color(YELLOW)
        arrow_02x2_tex = MathTex(r"\vec{v}" r"\times", r"2").shift(1.5 * UP)
        arrow_02x2_tex[0].set_color(YELLOW)
        arrow_24 = arrow_AB(number_line, 2, 4)
        arrow_04 = arrow_AB(number_line, 0, 4)
        arrow_024_tex = MathTex(r"\vec{v}", r"\times", "2", r"\times", r"(-1)").shift(
            1.5 * UP
        )
        arrow_024_tex[0].set_color(YELLOW)
        arrow_024_tex2 = MathTex(
            r"\vec{v}" r"\times", "2", r"\times", r"(-1)", r"\times", r"(-1)"
        ).shift(1.5 * UP)
        arrow_024_tex2[0].set_color(YELLOW)
        eq1 = MathTex(r"x^2 + 1 = 0").shift(2.5 * UP + 3.5 * LEFT)
        eq12 = MathTex(r"x^2 =  - 1").shift(2.5 * UP + 3.5 * LEFT)
        end_point = ValueTracker(2)
        moving_arrow = always_redraw(
            lambda: arrow_AB(number_line, 0, end_point.get_value())
        )
        base_arrow = arrow_AB(number_line, 0, 2)
        base_arrow_tex = MathTex(r"\vec{v}", r"\times", r"-1").shift(UP * 1.5)
        base_arrow_tex[0].set_color(YELLOW)
        base_arrow_tex2 = MathTex(
            r"\vec{v}", r"\times", r"\sqrt{-1}", r"\times", r"\sqrt{-1}"
        ).shift(UP * 1.5)
        base_arrow_tex2[0].set_color(YELLOW)
        base_arrow_tex3 = MathTex(r"\vec{v}", r"\times", r"\sqrt{-1}").shift(UP * 1.5)
        base_arrow_tex3[0].set_color(YELLOW)
        i_eq = MathTex(r"i", r"=", r"\sqrt{-1}").next_to(eq12, DOWN, buff=0.5)
        i2_eq = MathTex(r"i^2", r"=", r"-1").next_to(i_eq, DOWN, buff=0.5)
        base_arrow_tex4 = MathTex(r"\vec{v}", r"\times", r"i").shift(UP * 2.5)
        base_arrow_tex4[0].set_color(YELLOW)
        base_arrow_tex5 = MathTex(r"\vec{v}", r"i").shift(UP * 2.5)
        base_arrow_tex5[0].set_color(YELLOW)

        complex_plane = ComplexPlane(
            x_range=[-8, 8, 1],  # Real axis range
            y_range=[-4, 4, 1],  # Imaginary axis range
            x_length=12,
            y_length=6.5,
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.01,
            },
            axis_config={
                # "stroke_color": WHITE,
                # "stroke_width": 3,
                "include_ticks": True,
                # "include_numbers": True,
                "tick_size": 0.05,
                "font_size": 36,
            },
            x_axis_config={
                "include_numbers": True,
                # "numbers_to_include": [-4, -3, -2, -1, 1, 2, 3, 4],
            },
            y_axis_config={
                "include_numbers": False,  # Disable default numbers
            },
        )
        imag_labels = VGroup()
        for i in range(-4, 5):
            if i == 0:
                continue  # Skip 0 to avoid overlap
            label = MathTex(f"{i}i", font_size=36).next_to(
                complex_plane.coords_to_point(0, i), LEFT, buff=0.2
            )
            imag_labels.add(label)
        imag_labelsj = VGroup()
        for i in range(-4, 5):
            if i == 0:
                continue  # Skip 0 to avoid overlap
            label = MathTex(f"{i}j", font_size=36).next_to(
                complex_plane.coords_to_point(0, i), LEFT, buff=0.2
            )
            imag_labelsj.add(label)
        complex_pln = VGroup(complex_plane, imag_labels)
        blue_point = 4 + 3j
        point43 = Dot(complex_plane.n2p(blue_point), color=BLUE, radius=0.08)
        vector43 = arrow_AB(
            complex_plane,
            0,
            blue_point,
            TEAL,
        )
        y_dashed_line = DashedLine(
            start=complex_plane.n2p(3j), end=complex_plane.n2p(4 + 3j), color=RED
        )
        x_dashed_line = DashedLine(
            start=complex_plane.n2p(4), end=complex_plane.n2p(4 + 3j), color=RED
        )
        letterA = MathTex(r"a", color=RED)
        lineA = Line(
            complex_plane.c2p(0.1, -0.5), complex_plane.c2p(3.9, -0.5), color=BLUE
        )
        letterB = MathTex(r"b", color=BLUE)
        lineB = Line(
            complex_plane.c2p(4.3, 0.1), complex_plane.c2p(4.3, 2.9), color=BLUE
        )
        complex_number_z = MathTex(r"z", r"=", r"a", r"+", r"b", r"j").shift(
            UP * 3 + LEFT * 4
        )
        complex_number_z[2].set_color(RED)
        complex_number_z[4].set_color(BLUE)
        # complex_number_z[2].set_color(RED)\
        angle_blue_piont = Angle(
            line1=complex_plane.get_x_axis(),
            line2=vector43,
            radius=0.8,
            color=RED,
            other_angle=False,
        )
        theta_symbol = MathTex(r"\theta").next_to(angle_blue_piont, RIGHT, buff=0.1)
        # Define points (x, y, z=0)
        point1 = complex_plane.c2p(0, 0)  # (0, 0)
        point2 = complex_plane.c2p(4, 0)  # (4, 0)
        point3 = complex_plane.c2p(4, 3)  # (4, 3)

        # Create triangle using Polygon
        triangle = Polygon(
            point1,
            point2,
            point3,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.5,
            stroke_width=2,
        )
        r_symbol = MathTex(r"r")
        r_eq = MathTex(r"r", r"=", r"\sqrt{a^2 + b^2}").next_to(
            complex_number_z, DOWN, buff=0.5
        )
        complex_number_z_cos = MathTex(r"\cos(\theta)", r"=", r"\frac{a}{r}").next_to(
            complex_number_z, DOWN, buff=0.5
        )
        complex_number_z_cos2 = MathTex(r"a", r"=", r"r \cos(\theta)").next_to(
            complex_number_z, DOWN, buff=0.5
        )
        complex_number_z_sin = MathTex(r"\sin(\theta)", r"=", r"\frac{b}{r}").next_to(
            complex_number_z_cos2, DOWN, buff=0.5
        )
        complex_number_z_sin2 = MathTex(r"b", r"=", r"r \sin(\theta)").next_to(
            complex_number_z_cos2, DOWN, buff=0.5
        )
        z_cos_sin = MathTex(
            r"z", r"=", r"r \cos(\theta)", r"+", r"j r \sin(\theta)"
        ).move_to(complex_number_z)
        z_cos_sin2 = MathTex(
            r"z", r"=", r"r" r"(\cos(\theta)", r"+", r"j \sin(\theta))"
        ).move_to(complex_number_z)
        ## animation section

        self.add(grid)
        self.wait()
        self.play(Create(number_line), run_time=2)
        self.wait()
        self.play(Create(point_1))
        self.wait()
        self.play(Create(arrow_02))
        self.wait()
        self.play(Write(arrow_02_tex))
        self.wait()
        self.play(FadeOut(arrow_02_tex))
        self.wait()
        self.play(Write(arrow_02x2_tex))
        self.wait()
        self.play(Create(arrow_24))
        self.wait()
        arrow_024 = VGroup(arrow_02.copy(), arrow_04.copy())
        self.add(arrow_024)
        self.remove(arrow_02)
        self.remove(arrow_24)
        self.play(ReplacementTransform(arrow_024, arrow_04))
        self.wait()
        self.play(TransformMatchingShapes(arrow_02x2_tex, arrow_024_tex))
        self.wait()
        rec = SurroundingRectangle(
            arrow_024_tex[-1], color=YELLOW, stroke_width=3, buff=0.1
        )
        self.play(
            arrow_04.animate.rotate(PI / 2, about_point=number_line.n2p(0)),
            Create(rec),
            run_time=1,
        )
        self.play(
            arrow_04.animate.rotate(PI / 2, about_point=number_line.n2p(0)),
            run_time=1,
        )
        self.wait()
        self.play(FadeOut(rec))
        self.wait()
        self.play(TransformMatchingShapes(arrow_024_tex, arrow_024_tex2))
        self.wait()
        rec = SurroundingRectangle(
            arrow_024_tex2[-1], color=YELLOW, stroke_width=3, buff=0.1
        )
        self.play(
            arrow_04.animate.rotate(PI / 2, about_point=number_line.n2p(0)),
            Create(rec),
            run_time=1,
        )
        self.play(
            arrow_04.animate.rotate(PI / 2, about_point=number_line.n2p(0)),
            run_time=1,
        )
        self.wait()
        self.play(FadeOut(rec))
        self.wait()
        self.play(FadeOut(arrow_04, arrow_024_tex2))
        self.wait()
        self.play(FadeIn(moving_arrow))
        self.wait()
        end_points = [3, 5, 7, 4, 2]
        for po in end_points:
            self.play(end_point.animate.set_value(po))
            self.wait(0.5)
        self.wait()
        self.add(base_arrow)
        self.remove(moving_arrow)
        for i in range(4):
            self.play(
                base_arrow.animate.rotate(PI / 2, about_point=number_line.n2p(0)),
                run_time=1,
            )
        self.wait()
        self.play(FadeOut(base_arrow))
        self.wait()
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingShapes(eq1, eq12))
        self.wait()
        self.play(FadeIn(base_arrow))
        self.wait()
        self.play(Write(base_arrow_tex))
        self.wait()
        for i in range(2):
            self.play(
                base_arrow.animate.rotate(PI / 2, about_point=number_line.p2n(0)),
                run_time=1,
            )

        self.wait()
        self.play(TransformMatchingShapes(base_arrow_tex, base_arrow_tex2))
        self.wait()
        self.play(TransformMatchingShapes(base_arrow_tex2, base_arrow_tex3))
        self.play(
            base_arrow_tex3.animate.shift(UP),
            base_arrow.animate.rotate(-PI / 2, about_point=number_line.n2p(0)),
        )
        self.wait()
        self.play(
            Write(i_eq), TransformMatchingShapes(base_arrow_tex3, base_arrow_tex4)
        )
        self.wait()
        self.play(Write(i2_eq))
        self.wait()
        self.play(FadeOut(i_eq, i2_eq))
        self.wait()
        self.play(TransformMatchingShapes(base_arrow_tex4, base_arrow_tex5))
        self.wait()
        self.play(FadeOut(base_arrow, base_arrow_tex5, eq12))
        self.wait()
        self.play(TransformMatchingShapes(number_line, complex_plane), run_time=2)
        # self.add(complex_pln)
        self.remove(point_1)
        self.add(point_1)
        self.wait()
        self.play(Create(imag_labels), run_time=3)
        self.wait()
        self.play(TransformMatchingShapes(imag_labels, imag_labelsj))
        self.wait()
        self.play(FadeIn(point43))
        self.wait()
        self.play(Create(x_dashed_line), Create(y_dashed_line))
        self.wait()
        brcA = Brace(lineA, stroke_width=0.5, buff=0.1)
        letterA.next_to(brcA.get_center(), DOWN, buff=0.2)
        self.play(Create(brcA), Write(letterA))
        self.wait()
        brcB = Brace(lineB, stroke_width=0.5, direction=RIGHT, buff=0.1)
        letterB.next_to(brcB.get_center(), RIGHT, buff=0.2)
        self.play(Create(brcB), Write(letterB))
        self.wait()
        self.play(Write(complex_number_z))
        self.wait()
        self.play(Create(vector43))
        self.wait()
        self.play(Create(angle_blue_piont))
        self.play(Write(theta_symbol))
        self.wait()
        self.play(FadeIn(triangle))
        self.wait()
        self.play(FadeOut(triangle))
        self.wait()
        r_symbol.next_to(
            vector43.get_center(), direction=vector43.get_unit_vector(), buff=0
        )
        r_symbol.shift(0.1 * UP + 0.2 * LEFT)
        self.play(Write(r_symbol))
        self.wait()
        self.play(Write(r_eq))
        self.wait()
        self.play(FadeOut(r_eq))
        self.wait()
        self.play(Write(complex_number_z_cos))
        self.wait()
        self.play(TransformMatchingShapes(complex_number_z_cos, complex_number_z_cos2))
        self.wait()
        self.play(Write(complex_number_z_sin))
        self.wait()
        self.play(TransformMatchingShapes(complex_number_z_sin, complex_number_z_sin2))
        self.wait()
        self.play(
            TransformMatchingShapes(complex_number_z, z_cos_sin),
            FadeOut(complex_number_z_cos2, complex_number_z_sin2),
        )
        self.wait()
        self.play(TransformMatchingShapes(z_cos_sin, z_cos_sin2))
        self.wait()
        self.play(
            FadeOut(
                complex_plane,
                imag_labelsj,
                grid,
                point_1,
                brcA,
                brcB,
                letterA,
                letterB,
                r_symbol,
                point43,
                vector43,
                y_dashed_line,
                x_dashed_line,
                angle_blue_piont,
                theta_symbol,
            )
        )
        self.wait()
        self.play(z_cos_sin2.animate.move_to(ORIGIN).shift(UP))
        self.wait()

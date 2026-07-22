from manim import *


class EvenOdd(Scene):
    def construct(self):
        rule1 = MathTex(
            r"\bullet",
            r"\quad",
            r"odd",
            r"\times",
            r"even",
            r"\: :",
            r"\: odd",
            font_size=36,
        )
        rule1[2].set_color(YELLOW)
        rule1[4].set_color(PINK)
        rule1[6].set_color(YELLOW)
        rec_rule1 = SurroundingRectangle(rule1, color=ORANGE, buff=0.1, stroke_width=3)
        rule2 = MathTex(
            r"\bullet",
            r"\quad",
            r"odd",
            r"\times",
            r"odd",
            r"\: :",
            r"\: even",
            font_size=36,
        )
        rule2[2].set_color(YELLOW)
        rule2[4].set_color(YELLOW)
        rule2[6].set_color(PINK)
        rec_rule2 = SurroundingRectangle(rule2, color=ORANGE, buff=0.1, stroke_width=3)

        rule3 = MathTex(
            r"\bullet",
            r"\quad",
            r"even",
            r"\times",
            r"even",
            r"\: :",
            r"\: even",
            font_size=36,
        )
        rule3[2].set_color(PINK)
        rule3[4].set_color(PINK)
        rule3[6].set_color(PINK)

        rules = VGroup(rule1, rule2, rule3)
        rules.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        rules.to_edge(LEFT, buff=1).shift(2.5 * UP)
        rec_rule1.move_to(rule1.get_center())
        rec_rule2.move_to(rule2.get_center())

        f_odd = MathTex(r"f ", r"\: : \: ", r"odd \; function", font_size=36).next_to(
            rules, RIGHT, buff=1.5
        )
        f_odd[0].set_color(YELLOW)
        f_rule = MathTex(r"f(-x)", r"=", r"-f(x)", font_size=36).next_to(
            f_odd, DOWN, buff=0.5
        )
        g_even = MathTex(r"g ", r"\: : \: ", r"even \; function", font_size=36).next_to(
            f_odd, RIGHT, buff=1.5
        )
        g_even[0].set_color(PINK)
        g_rule = MathTex(r"g(-x)", r"=", r"g(x)", font_size=36).next_to(
            g_even, DOWN, buff=0.5
        )
        h_pro1 = MathTex(r"h(x)", r"=", r"f(x)", r"\,", r"g(x)", font_size=36)
        h_pro2 = MathTex(r"h(-x)", r"=", r"f(-x)", r"\,", r"g(-x)", font_size=36)
        h_pro3 = MathTex(r"h(-x)", r"=", r"-f(x)", r"\,", r"g(x)", font_size=36)
        ff = MathTex(r"-f(x)", font_size=36).move_to(h_pro2[2])
        gg = MathTex(r"g(x)", font_size=36).move_to(h_pro2[4])
        h_pro4 = MathTex(r"h(-x)", r"=", r"-", r"h(x)", font_size=36)
        a_n_for = MathTex(
            r"a_n",
            r"=",
            r"\frac{2}{T_0}",
            r"\,",
            r"\int_{0}^{T_0}",
            r"x(t)",
            r"\:",
            r"cos(n \omega t)",
            r"\;",
            r"dt",
            font_size=36,
        )
        brace_odd = Brace(a_n_for[5], DOWN, buff=0.15)
        brace_odd_text = MathTex(r"odd", color=YELLOW, font_size=36).next_to(
            brace_odd, DOWN, buff=0.1
        )
        brace_even = Brace(a_n_for[7], DOWN, buff=0.15)
        brace_even_text = MathTex(r"even", color=PINK, font_size=36).next_to(
            brace_even, DOWN, buff=0.1
        )
        big_barce = Brace(a_n_for[5:8], DOWN, buff=0.15)
        big_brace_text = MathTex(r"odd", color=YELLOW, font_size=36).next_to(
            big_barce, DOWN, buff=0.1
        )
        a_n_0 = MathTex(r"a_n", r"=", r"0", font_size=36).next_to(
            a_n_for, DOWN, buff=0.7
        )

        ## bn
        b_n_for = MathTex(
            r"b_n",
            r"=",
            r"\frac{2}{T_0}",
            r"\,",
            r"\int_{0}^{T_0}",
            r"x(t)",
            r"\:",
            r"sin(n \omega t)",
            r"\;",
            r"dt",
            font_size=36,
        )
        b_brace_odd1 = Brace(b_n_for[5], DOWN, buff=0.15)
        b_brace_odd1_text = MathTex(r"odd", color=YELLOW, font_size=36).next_to(
            b_brace_odd1, DOWN, buff=0.1
        )
        b_brace_odd2 = Brace(b_n_for[7], DOWN, buff=0.15)
        b_brace_odd2_text = MathTex(r"odd", color=YELLOW, font_size=36).next_to(
            b_brace_odd2, DOWN, buff=0.1
        )
        b_big_brace = Brace(b_n_for[5:8], DOWN, buff=0.15)
        b_big_brace_text = MathTex(r"even", color=PINK, font_size=36).next_to(
            b_big_brace, DOWN, buff=0.1
        )
        b_n_ans = MathTex(
            r"b_n",
            r"=",
            r"2\,",
            r"\frac{2}{T_0}",
            r"\,",
            r"\int_{0}^{\frac{T_0}{2}}",
            r"x(t)",
            r"\:",
            r"sin(n \omega t)",
            r"\;",
            r"dt",
            font_size=36,
        ).next_to(b_n_for, DOWN, buff=0.7)
        b_n_ans[2].set_color(RED)
        ## anmi

        for i in rules:
            self.play(Write(i[0 : len(i) - 1]))
            self.wait()
        self.play(Write(f_odd))
        self.wait()
        self.play(Write(g_even))
        self.wait()
        self.play(Write(f_rule))
        self.wait()
        self.play(Write(g_rule))
        self.wait()
        self.play(Write(h_pro1))
        self.wait()
        self.play(TransformMatchingShapes(h_pro1, h_pro2))
        self.wait()
        self.play(ReplacementTransform(h_pro2[2], ff))
        self.wait()
        self.play(ReplacementTransform(h_pro2[4], gg))
        self.wait()
        self.play(TransformMatchingShapes(h_pro2, h_pro3))
        self.wait()
        self.play(TransformMatchingTex(h_pro3, h_pro4))
        self.wait()
        self.play(ReplacementTransform(h_pro4, rule1[-1]))
        self.wait()
        self.play(Write(rule2[-1]))
        self.wait()
        self.play(Write(rule3[-1]))
        self.wait()
        self.play(Write(a_n_for))
        self.wait()
        self.play(Create(brace_odd))
        self.play(Write(brace_odd_text))
        self.wait()
        self.play(Create(brace_even))
        self.play(Write(brace_even_text))
        self.wait()
        self.play(Create(rec_rule1))
        braces_group = VGroup(brace_odd, brace_even)
        braces_text_group = VGroup(brace_odd_text, brace_even_text)
        self.play(
            FadeOut(rec_rule1),
            ReplacementTransform(braces_group, big_barce),
            TransformMatchingTex(braces_text_group, big_brace_text),
        )
        self.wait()
        self.play(TransformFromCopy(a_n_for, a_n_0), FadeOut(big_barce, big_brace_text))
        self.wait()
        self.play(FadeOut(a_n_for, a_n_0))
        self.wait()
        self.play(Write(b_n_for))
        self.wait()
        self.play(Create(b_brace_odd1))
        self.play(Write(b_brace_odd1_text))
        self.wait()
        self.play(Create(b_brace_odd2))
        self.play(Write(b_brace_odd2_text))
        self.wait()
        self.play(Create(rec_rule2))
        self.wait()
        b_braces_group = VGroup(b_brace_odd1, b_brace_odd2)
        b_braces_group_text = VGroup(b_brace_odd1_text, b_brace_odd2_text)
        self.play(
            FadeOut(rec_rule2),
            ReplacementTransform(b_braces_group, b_big_brace),
            TransformMatchingTex(b_braces_group_text, b_big_brace_text),
        )
        self.wait()
        self.play(
            FadeOut(b_big_brace, b_big_brace_text),
            TransformFromCopy(b_n_for, b_n_ans),
        )
        self.wait()
        self.play(
            FadeOut(
                rules,
                f_odd,
                g_even,
                f_rule,
                g_rule,
                b_n_for,
                b_n_ans,
            )
        )
        self.wait()

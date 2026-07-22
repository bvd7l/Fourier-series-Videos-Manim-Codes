from manim import *


class z_e(Scene):
    def construct(self):
        eq1 = MathTex(
            r"z", r"=", r"|z|", r"(cos(\theta)", r"+", r"j sin(\theta))"
        ).shift(UP * 2)
        eq2 = MathTex(r"z", r"=", r"cos(\theta)", r"+", r"j sin(\theta)").shift(UP * 2)
        eq3 = MathTex(
            r"\frac{dz}{d\theta}", r"=", r"-sin(\theta)", r"+", r"j cos(\theta)"
        ).shift(UP * 1)
        j_1 = MathTex(r"j^2 = -1", color=ORANGE).next_to(eq3, RIGHT, buff=1)
        eq4 = MathTex(
            r"\frac{dz}{d\theta}", r"=", r"j^2 sin(\theta)", r"+", r"j cos(\theta)"
        ).shift(UP * 1)
        eq5 = MathTex(
            r"\frac{dz}{d\theta}",
            r"=",
            r"j",
            r"(j sin(\theta)",
            r"+",
            r"j cos(\theta))",
        ).shift(UP * 1)
        eq6 = MathTex(r"\frac{dz}{d\theta}", r"=", r"j", r"z").shift(UP * 1)
        eq7 = MathTex(r"\frac{dz}{z}", r"=", r"j", r"d \theta").shift(UP * 1)
        eq8 = MathTex(r"ln(z)", r"=", r"j", r"\theta")
        eq9 = MathTex(r"z", r"=", r"e ^ {j \theta}")
        # --------
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()
        eq2_copy = eq2.copy()
        self.play(TransformMatchingTex(eq2_copy, eq3))
        self.wait()
        self.play(Write(j_1))
        self.wait()
        self.play(TransformMatchingTex(eq3, eq4))
        self.play(FadeOut(j_1))
        self.wait()
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait()
        self.play(TransformMatchingTex(eq5, eq6))
        self.wait()
        self.play(TransformMatchingTex(eq6, eq7))
        self.wait()
        eq7_copy = eq7.copy()
        self.play(TransformMatchingTex(eq7_copy, eq8))
        self.wait()
        self.play(TransformMatchingTex(eq8, eq9))
        self.wait()

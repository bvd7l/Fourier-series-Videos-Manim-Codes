from manim import *


class Ts_formula(Scene):
    def construct(self):
        eq1 = MathTex(
            r"f(x)=\sum^{\infty}_{n=0} a_n cos(n \omega x) + b_n sin(n \omega x)"
        )
        eq2 = MathTex(
            r"f(t)=\sum^{\infty}_{n=0} a_n cos(n \omega t) + b_n sin(n \omega t)"
        )
        self.play(Write(eq1))

        self.wait()
        self.play(TransformMatchingShapes(eq1, eq2))
        self.wait()

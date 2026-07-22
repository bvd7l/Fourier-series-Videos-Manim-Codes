from manim import *
import numpy as np

# config.background_color = "#1f1f1f"


def ar_text(text, font_size):
    return Text(text, font_size=font_size, font="Cairo")


def roman_text(text, font_size):
    return Text(text, font_size=font_size, font="Times New Roman")


class Taylor(Scene):
    def construct(self):
        title = ar_text("سلسلة تايلور:", 36)
        title.to_corner(UP + RIGHT, buff=0.8)
        self.play(Write(title, reverse=True))
        self.add(title)
        self.wait()

        image = ImageMobject("./taylor_image.jpg")
        image.scale(0.8)
        image.to_edge(LEFT, buff=0.8).shift(0.5 * UP)
        stroke = BackgroundRectangle(
            image,
            color=WHITE,
            buff=0.1,
            stroke_width=4,
            fill_opacity=0,
            stroke_opacity=1,
        )
        # image_stroke = VGroup(image, stroke)
        self.play(FadeIn(image, stroke))
        im_name = roman_text("Brook Taylor", 25)
        im_date = roman_text("1685 - 1731", 25)
        im_name.next_to(stroke, DOWN, buff=0.3)
        im_date.next_to(im_name, DOWN, 0.2)
        self.play(Write(im_name), Write(im_date))
        self.wait()

        image_right_edge = image.get_right()[0]

        right_area_center_x = (image_right_edge + config.frame_width / 2) / 2
        right_area_center = np.array([right_area_center_x, 0, 0])

        self.wait()
        eq1 = MathTex(r"f(x)").move_to(right_area_center)
        eq2 = MathTex(r"f(x)", r"=", r"(x-a)").move_to(right_area_center)
        eq3 = MathTex(r"f(x)", r"=", r"\sum^{\infty}_{n=0}", r"(x-a)").move_to(
            right_area_center
        )
        eq4 = MathTex(r"f(x)", r"=", r"\sum^{\infty}_{n=0}", r"(x-a)", r"^n").move_to(
            right_area_center
        )
        eq5 = MathTex(
            r"f(x)",
            r"=",
            r"\sum^{\infty}_{n=0}",
            r"\frac{f^{(n)}(a)}{n!}",
            r"(x-a)",
            r"^n",
        ).move_to(right_area_center)
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait()
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait()
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait()
        # step3 = MathTex("f(x)=\\sum_{n=0}^{\\infty}(x-a)")
        # step3.move_to(right_area_center)

        # self.play(FadeTransformPieces(step2, step3))
        # self.wait()
        # step4 = MathTex("f(x)=\\sum_{n=0}^{\\infty}(x-a)^{n}")
        # step4.move_to(right_area_center)
        # self.play(FadeTransformPieces(step3, step4))
        # self.wait()

        # step5 = MathTex("f(x)=\\sum_{n=0}^{\\infty}\\frac{f^{(n)}(a)}{n!}(x-a)^{n}")
        # step5.move_to(right_area_center)
        # self.play(FadeTransformPieces(step4, step5))
        # self.wait()

        # self.play(step5.animate.shift(UP))
        # self.wait()
        # step1 = MathTex("f(x)", font_size=50)
        # step1.set_color(BLUE)
        # step1.move_to(right_area_center)
        # self.play(Write(step1))
        # self.wait()

        # step2 = MathTex(
        #     "f(x) = \\sum_{n=0}^{\\infty}",
        #     "\\frac{f^{(n)}(a)}{n!}",
        #     "(x-a)^n",
        #     font_size=50,
        # )
        # step2.set_color(RED)
        # step2[1].set_opacity(0)
        # step2.move_to(right_area_center)
        # self.play(Transform(step1, step2))

        # self.wait()

        # step2[1].set_opacity(1)
        # self.play(FadeIn(step2[1]))
        # self.wait(2)

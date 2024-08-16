from manim import *
import math
import numpy as np

class Try(Scene):
    def construct(self):
        t1 = MathTex(r"\mathcal{\mathbf{{\Huge Calculus } } } ")
        t2 = MathTex(r"{f}'(x) =\lim_{h \to 0} \frac{f(x+h)-f(x)}{x+h-x}")
        t3 = MathTex(r"= \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}")
        t4 = MathTex(r"and \ if \ f(x)=x^2")
        t5 = MathTex(r"= \lim_{h \to 0} \frac{(x+h)^2-x^2}{h} ")
        t6 = MathTex(r"= \lim_{h \to 0} \frac{x^2+h^2+2xh-x^2}{h} ")
        t7 = MathTex(r"= \lim_{h \to 0} \frac{h^2+2xh}{h} ")
        t8 = MathTex(r"= \lim_{h \to 0} {h+2x} ")
        t9 = MathTex(r"= 2x")
        t10 = MathTex(r"Function \ Graph")

        tt1 = MathTex(r"so \ {f}' (x) = 2x")
        tt2 = MathTex(r"i.e\ \ \  \int_{a}^{b}2x\ dx =\left [ x^2 + C \right ]_{a}^{b}  =b^2 - a^2")

        t4.to_edge(LEFT,buff = 0.5)

        npl = NumberPlane()

        func1 = lambda x: x ** 2
        func2 = lambda x: 2 * x

        gra1 = npl.plot(func1, color = BLUE)
        gra2 = npl.plot(func2, color = YELLOW)


        self.play(Write(t1))
        self.wait()
        self.play(FadeOut(t1))

        self.play(FadeIn(t2))
        self.wait()
        self.play(t2.animate.to_edge(UL,buff = 0.5))
        #self.play(t2.animate.shift(UP),run_time = 4)
        t3.next_to(t2, DOWN, buff = 0.5)
        self.play(FadeIn(t3),t3.animate.to_edge(LEFT,buff = 0.5))
        self.wait()

        self.play(FadeIn(t4),t4.animate.to_edge(RIGHT,buff = 0.5))
        self.wait()
        self.play(FadeOut(t4))

        t5.next_to(t3, DOWN, buff = 0.5)
        self.play(FadeIn(t5))
        self.wait()

        t6.next_to(t5, DOWN, buff = 0.5)
        self.play(FadeIn(t6))
        self.wait()

        self.play(FadeOut(t5,t3,t2),t6.animate.to_edge(UL,buff = 0.5))
        self.wait()

        t7.next_to(t6, DOWN, buff = 0.5)
        self.play(FadeIn(t7))
        self.wait()

        t8.next_to(t7, DOWN, buff = 0.5)
        self.play(FadeIn(t8))
        self.wait()

        t9.next_to(t8, DOWN, buff = 0.5)
        self.play(FadeIn(t9))
        self.wait()

        self.play(FadeOut(t6,t7,t8,t9))
        tt1.animate.to_edge(UP,buff = 0.5)
        self.wait()

        #self.play(tt1.animate.to_edge(UP,buff = 0.5))
        tt1.to_edge(UP,buff = 0.5)
        self.play(FadeIn(tt1))
        tt2.next_to(tt1, DOWN, buff = 1)
        self.play(FadeIn(tt2))
        self.wait()
        self.play(FadeOut(tt1,tt2))
        self.play(FadeIn(t10))
        self.wait()
        self.play(FadeOut(t10))


        self.play(FadeIn(npl))
        self.add(gra1)
        self.play(Create(gra1, run_time=3))
        self.add(gra2)
        self.play(Create(gra2, run_time=3))
        self.play(FadeOut(gra1,npl,gra2))








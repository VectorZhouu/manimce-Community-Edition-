from manim import *

class Try(Scene):
    def construct(self):
        #return super().construct()
        t1 = MathTex(r"(a+b)^3 = a^3 + 3a^2b + 3ab^2 +b^3")
        t2 = MathTex(r"(a-b)^3 = a^3 - 3a^2b + 3ab^2 -b^3")
        t3 = MathTex(r"(a \pm b)^3 = a^3 \pm 3a^2b + 3ab^2 \pm b^3")
        t4 = MathTex(r"a ^ 3 + b ^ 3 = (a+b)(a^2+b^2-ab)")
        t5 = MathTex(r"a ^ 3 - b ^ 3 = (a-b)(a^2+b^2+ab)")
        t6 = MathTex(r"a ^ 3 \pm b ^ 3 = (a \pm b)(a^2+b^2\pm ab)")


        self.play(FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(t1,t2))
        self.wait()
        self.play(ReplacementTransform(t2,t3))
        self.play(t3.animate.to_edge(UP,buff = 0.5))
        
        self.play(FadeIn(t4))
        self.wait()
        self.play(ReplacementTransform(t4,t5))
        self.wait()
        self.play(ReplacementTransform(t5,t6))
        self.wait()
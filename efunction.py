from manim import *
import math
import numpy as np

class GraphingFunction(Scene):
    def construct(self):
        # 创建NumberPlane
        plane = NumberPlane(x_range=[-7, 7, 1], y_range=[-1, 7, 1])
        plane1 = NumberPlane()


        #self.add(plane)

        t1 = MathTex(r"y = x^2")
        t2 = MathTex(r"y = 3")
        t3 = MathTex(r"y = 2x")
        t4 = MathTex(r"y = \frac {1}{x}")
        t5 = MathTex(r"y = |x|")
        t6 = MathTex(r"y = sin(x)")
        t7 = MathTex(r"y = cos(x)")
        t8 = MathTex(r"y = tan(x)")

        # 定义函数
        func1 = lambda x: 3
        func = lambda x: x**2
        func2 = lambda x: 2 * x 
        func4 = lambda x: 1/x
        func5 = lambda x: abs(x)
        func6 = lambda x: np.sin(x)
        func7 = lambda x: np.cos(x)
        func8 = lambda x: np.tan(x)

        # 创建函数图像
        graph1 = plane1.plot(func1,color = BLUE)
        graph2 = plane1.plot(func2,color = BLUE)
        graph = plane.plot(func, color=BLUE)
        graph4 = plane1.plot(
            func4,
            discontinuities=[0],
            dt = 0.1,
            color = BLUE
            )
        graph5 = plane1.plot(func5,color = BLUE)
        graph6 = plane1.plot(func6,color = BLUE)
        graph7 = plane1.plot(func7,color = BLUE)
        graph8 = plane1.plot(
            func8,
            discontinuities=[-2.5 * PI, -1.5 * PI, -PI / 2, PI / 2, 1.5 * PI, 2.5 * PI],
            dt = 0.1,
            color = BLUE)
 
        # 将图像添加到场景中  y = 3
        #1
        self.play(FadeIn(t2))
        self.wait()
        self.play(FadeOut(t2))
        self.wait()
        self.play(FadeIn(plane1))
        self.add(graph1)
        # 创建动画，显示函数图像的绘制过程
        self.play(Create(graph1, run_time=4))
        self.play(FadeOut(graph1,plane1))

        #2
        self.play(FadeIn(t3))
        self.wait()
        self.play(FadeOut(t3))
        self.play(FadeIn(plane1))
        self.add(graph2)

        self.play(Create(graph2, run_time=4))
        self.play(FadeOut(graph2,plane1))

        #3
        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeOut(t1))
        self.play(FadeIn(plane))
        self.add(graph)

        self.play(Create(graph, run_time=4))
        self.play(FadeOut(graph,plane))

        #4
        self.play(FadeIn(t4))
        self.wait()
        self.play(FadeOut(t4))
        self.play(FadeIn(plane1))
        self.add(graph4)

        self.play(Create(graph4, run_time=4))
        self.play(FadeOut(graph4,plane1))

        #5
        self.play(FadeIn(t5))
        self.wait()
        self.play(FadeOut(t5))
        self.play(FadeIn(plane1))
        self.add(graph5)

        self.play(Create(graph5, run_time=4))
        self.play(FadeOut(graph5,plane1))

        #6
        self.play(FadeIn(t6))
        self.wait()
        self.play(FadeOut(t6))
        self.play(FadeIn(plane1))
        self.add(graph6)

        self.play(Create(graph6, run_time=4))
        self.play(FadeOut(graph6,plane1))

        #7
        self.play(FadeIn(t7))
        self.wait()
        self.play(FadeOut(t7))
        self.play(FadeIn(plane1))
        self.add(graph7)

        self.play(Create(graph7, run_time=4))
        self.play(FadeOut(graph7,plane1))

        #8
        self.play(FadeIn(t8))
        self.wait()
        self.play(FadeOut(t8))
        self.play(FadeIn(plane1))
        self.add(graph8)

        self.play(Create(graph8, run_time=4))
        self.play(FadeOut(graph8,plane1))


        # 如果你想要一个点的动画沿着曲线移动，可以添加以下代码
        # 创建一个点
        #dot = Dot(color=RED)
        #dot.move_to(plane.c2p(-10, func(-10)))

        # 将点添加到场景中
        #self.add(dot)

        # 创建沿着曲线移动的动画
        #self.play(MoveAlongPath(dot, graph, rate_func=linear), run_time=5)


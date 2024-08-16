from manim import *
import numpy as np

# 定义泰勒级数的函数
def taylor_approximation(n, x):
    return sum([x**i / np.math.factorial(i) for i in range(n)])

class TaylorSeriesAnimation(Scene):
    def construct(self):
        # 创建坐标轴
        ax = Axes(
            x_range=[-10, 10, 1],
            y_range=[0, 2.5, 0.5],
            x_length=10,
            y_length=6,
            tips=False
        )
        self.add(ax)

        # 绘制实际的e^x函数
        e_x_graph = ax.plot(lambda x: np.exp(x), x_range=[-10, 10], color=BLUE)
        e_x_label = MathTex("e^x").next_to(e_x_graph, RIGHT)
        self.add(e_x_graph, e_x_label)

        # 创建泰勒级数的逼近动画
        n = 10  # 泰勒级数的项数
        for i in range(1, n + 1):
            # 绘制当前项数的泰勒级数逼近
            taylor_graph = ax.plot(
                lambda x: taylor_approximation(i, x),
                x_range=[-10, 10],
                color=YELLOW
            )
            taylor_label = MathTex(f"Taylor approximation (n={i})").next_to(taylor_graph, RIGHT)
            self.add(taylor_graph, taylor_label)

            # 显示一段时间，然后移除
            self.wait(1)
            self.remove(taylor_graph, taylor_label)


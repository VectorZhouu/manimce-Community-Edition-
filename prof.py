from manim import *
import math
import numpy as np

class Function(Scene):
    def construct(self):
        # 创建NumberPlane
        plane = NumberPlane(x_range=[-7, 7, 1], y_range=[-1, 7, 1])
        plane1 = NumberPlane()
        #plane2 = NumberPlane(x_range=[0,14,1],y_range=[-4,4,1])
        plane2 = NumberPlane()

        t1 = MathTex(r"2x + y - 1 = 0")
        t2 = MathTex(r"(x - 1)^2 + y ^ 2 = 1")
        t3 = MathTex(r"y = e^x")
        #t4 = MathTex(r"y = \log_{2}{x} ")
        t4 = MathTex(r"y = \frac{1}{ \sqrt{2\pi }}e^{-\frac{1}{2}x^2 }")
        t5 = MathTex(r"\sin x = \cos(\frac{x+4}{y}) ")
        t6 = MathTex(r"|\sin (x ^ 2 +2xy)| = sin(x-2y)")
        t7 = MathTex(r"\sin (x^2 + y^2) =\cos (xy)")
        t8 = MathTex(r"\sin (\sqrt[]{y} ) = (x + y^2)^2")
        t9 = MathTex(r"\sin(x) = \cos(y)")
        #t10 = MathTex(r"y = \sin(6x)tan(6x) ")
        #t11 = MathTex(r"y = -\sin(6x)tan(6x) ")
        t10 = MathTex(r"\tan(x^2+y^2)=1")
        t11 = MathTex(r"y = \frac{2x}{x^2+1} ")

        func1 = lambda x: -2 * x + 1
        #func2 = lambda x,y: (x - 1) ** 2 + y ** 2 - 1
        func3 = lambda x: np.exp(x)
        #func4 = lambda x: np.log10(x)
        func4 = lambda x: (1/np.sqrt(2 * PI)) * (np.exp(-1/2 * (x ** 2)))
        func11 = lambda x: (2 * x)/(x ** 2 + 1)
        
        

        graph1 = plane1.plot(func1,color = BLUE)
        #graph2 = plane1.plot(func2,color = BLUE)
        graph3 = plane1.plot(func3,color = BLUE)
        graph4 = plane2.plot(func4,color = BLUE)
        graph11 = plane2.plot(func11,color = BLUE)
        

    

        graph2 = ImplicitFunction(
            lambda x, y: (x - 1) ** 2 + y ** 2 - 1,
            color=YELLOW
        )
        graph5 = ImplicitFunction(
            lambda x,y: np.sin(x) - np.cos((x + 4) / y),
            color = YELLOW
        )
        graph6 = ImplicitFunction(
            lambda x,y: np.abs(np.sin(x ** 2 + 2 * x * y))-np.sin(x - 2 * y),
            color = YELLOW
        )
        graph7 = ImplicitFunction(
            lambda x,y: np.sin(x ** 2 + y ** 2)-np.cos(x * y),
            color = YELLOW
        )
        graph8 = ImplicitFunction(
            lambda x,y: np.sin(np.sqrt(y))-(x + y ** 2) ** 2,
            color = YELLOW
        )
        graph9 = ImplicitFunction(
            lambda x,y: np.sin(x)-np.cos(y),
            color = YELLOW
        )
        graph10 = ImplicitFunction(
            lambda x,y: np.tan(x ** 2 + y ** 2) - 1,
            color = YELLOW
        )
       # graph10 = ImplicitFunction(
            #lambda x,y: 8 * np.sin(5 * x) * np.tan(5 * x) + np.abs(x),

       #     color = YELLOW
        #)
       # graph11 = ImplicitFunction(
            #lambda x,y: -8 * np.sin(5 * x) * np.tan(5 * x) - np.abs(x),
       #     color = YELLOW
       # )
       # graph4 = plane2.plot(
        #    func4,
         #   discontinuities=[0],
          #  dt = 0.1,
           # color = BLUE)

        #1
        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeOut(t1))
        self.wait()
        self.play(FadeIn(plane1))
        self.add(graph1)
        
        self.play(Create(graph1, run_time=4))
        self.play(FadeOut(graph1,plane1))

        #2
        self.play(FadeIn(t2))
        self.wait()
        self.play(FadeOut(t2))
        self.wait()
        self.play(FadeIn(plane1))
        self.add(graph2)
        
        self.play(Create(graph2, run_time=4))
        self.play(FadeOut(graph2,plane1))

        #3
        self.play(FadeIn(t3))
        self.wait()
        self.play(FadeOut(t3))
        self.wait()
        self.play(FadeIn(plane1))
        self.add(graph3)
        
        self.play(Create(graph3, run_time=4))
        self.play(FadeOut(graph3,plane1))

        #11
        self.play(FadeIn(t11))
        self.wait()
        self.play(FadeOut(t11))
        self.wait()
        self.play(FadeIn(plane1))
        self.add(graph11)
        
        self.play(Create(graph11, run_time=4))
        self.play(FadeOut(graph11,plane1))

        #4
        self.play(FadeIn(t4))
        self.wait()
        self.play(FadeOut(t4))
        self.wait()
        self.play(FadeIn(plane2))
        self.add(graph4)
        
        self.play(Create(graph4, run_time=4))
        self.play(FadeOut(graph4,plane2))

        #5
        self.play(FadeIn(t5))
        self.wait()
        self.play(FadeOut(t5))
        self.wait()
        self.play(FadeIn(plane2))
        self.add(graph5)
        
        self.play(Create(graph5, run_time=4))
        self.play(FadeOut(graph5,plane2))

        #6
        self.play(FadeIn(t6))
        self.wait()
        self.play(FadeOut(t6))
        self.wait()
        self.play(FadeIn(plane2))
        self.add(graph6)
        
        self.play(Create(graph6, run_time=4))
        self.play(FadeOut(graph6,plane2))

        #7
        self.play(FadeIn(t7))
        self.wait()
        self.play(FadeOut(t7))
        self.wait()
        self.play(FadeIn(plane2))
        self.add(graph7)
        
        self.play(Create(graph7, run_time=4))
        self.play(FadeOut(graph7,plane2))

        #8
        self.play(FadeIn(t8))
        self.wait()
        self.play(FadeOut(t8))
        self.wait()
        self.play(FadeIn(plane2))
        self.add(graph8)
        
        self.play(Create(graph8, run_time=4))
        self.play(FadeOut(graph8,plane2))

        #9
        self.play(FadeIn(t9))
        self.wait()
        self.play(FadeOut(t9))
        self.wait()
        self.play(FadeIn(plane2))
        self.add(graph9)
        
        self.play(Create(graph9, run_time=4))
        self.play(FadeOut(graph9,plane2))

        #10
        self.play(FadeIn(t10))
        self.wait()
        self.play(FadeOut(t10))
        self.wait()
        self.play(FadeIn(plane2))
        self.add(graph10)
        
        self.play(Create(graph10, run_time=4))
        self.play(FadeOut(graph10,plane2))


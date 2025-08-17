# manimce-Community-Edition
Lots of samples of manim graph animation.Pay attention to the edition(COMUUNITY EDITION).More detail you can see in the discord of Manim \
许多函数的动画。⚠️注意版本（社区版本）。更多细节可以加入manim的dicord
> ### Download manimce
Make sure that tou hava downloaded ```manimce``` by running \
通过运行以下命令确保你已正确安装```manimce```
```bash
pip3 install manim
```
don't run(unless you want to use manimgl) \
不要输入（除非你想下载的不是社区版本manimce，而是个人版manimgl）
```python
pip3 install manimgl
```
> ### Download perl ,FFmpeg ,dvisvgm
> 
You can download them from official website.__The version of dvisvgm must be higher than 2.4,but sometimes the highest version is not working,too(3.4),you can download 3.4.4(supported)__
> ### Download MikTex
You can download it at official website.__If you have a 360 Guard scanner on your computer, turn off its automatic scanner as they will automatically delete miktex files__


> ### Test
Create a new file called a.py(or other name),than put this code into your file
```python
from manim import *
class Try(Scene):
  def construct(self):
    s = Circle(color = BLUE,opacity = 0.5)
    self.play(FadeIn(s))
    self.wait()
```
>> Finally run
```
manim a.py -p
```
>> High quality
```
manim a.py -pqh
```
>> Low quality
```
manim a.py -pql
```

> ### Plugin
You can download ```manim sideview``` to hava a better environment at VSCode


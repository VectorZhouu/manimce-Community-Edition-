# manimce-Community-Edition😄
Lots of samples of manim graph animation.Pay attention to the edition(COMUUNITY EDITION).More detail you can see in the discord of Manim \
许多函数的动画。⚠️注意版本（社区版本）。更多细节可以加入manim的discord
> ### Download manimce
Make sure that tou hava downloaded ```manimce``` by running \
通过运行以下命令确保你已正确安装```manimce```
```py
pip3 install manim
```
don't run(unless you want to use manimgl) \
不要输入（除非你想下载的不是社区版本manimce，而是个人版manimgl）
```bash
pip3 install manimgl
```
> ### Download perl ,FFmpeg ,dvisvgm
> 
You can download them from official website.__The version of dvisvgm must be higher than 2.4,but sometimes the highest version is not working,too(3.4),you can download 3.4.4(supported)__ \
你可以从官方网站下载他们。__dvisvgm的版本必须高于2.4，但是又有时候过高版本并不支持，推荐3.4.4__

> ### Download MikTex
You can download it at official website.__If you have a 360 Guard scanner on your computer, turn off its automatic scanner as they will automatically delete miktex files__ \
你可以从官方网站下载miktex __如果你有360安全卫士，请关闭他的自动检测，因为下载完miktex后它会自动删除miktex的文件__


> ### Test
Create a new file called a.py(or other name),then put this code into your file \
创建一个文件叫做a.py（或其他名字），然后输入下面的代码
```python
from manim import *
class Try(Scene):
  def construct(self):
    s = Circle(color = BLUE,opacity = 0.5)
    self.play(FadeIn(s))
    self.wait()
```
>> Finally run \
>> 最后运行
```bash
manim a.py -p
```
>> High quality \
>> 高品质
```bash
manim a.py -pqh
```
>> Low quality \
>> 低品质
```bash
manim a.py -pql
```

> ### Plugin
You can download ```manim sideview``` to hava a better environment at VSCode \
你可以在vscode里面下载```manim sideview```插件

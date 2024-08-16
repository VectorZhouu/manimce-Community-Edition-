# manimce-Community-Edition
Lots of samples of manim graph animation.
> ### Download manimce
Make sure that tou hava downloaded ```manimce``` by running 
```python
pip3 install manim
```
dont run(they are not the same thing)

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


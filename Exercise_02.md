用turtle函数画出自己的名字，移动名字的同时清屏
-
源代码如下
```python
import turtle
for i in range(20):
    turtle.forward(100)
    turtle.right(90)
    turtle.clear()
    turtle.write("周思源",font=("Times",20,"bold"))
```

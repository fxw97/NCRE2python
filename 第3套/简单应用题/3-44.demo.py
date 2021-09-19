# 绘制五边形
import turtle
turtle.pensize(2)
d = 0
for i in range(5):
    turtle.seth(d)
    d+=72
    turtle.fd(200)
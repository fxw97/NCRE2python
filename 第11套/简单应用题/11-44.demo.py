# 绘制正12边形
import turtle
turtle.pensize(2)
d = 0
for i in range(1,13):
    turtle.fd(30)
    d+=30
    turtle.seth(d)
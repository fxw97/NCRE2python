# 绘制边长200的太阳花
import turtle
turtle.color('red','yellow')
turtle.begin_fill()
for i in range(36):
    turtle.fd(200)
    turtle.left(170)
turtle.end_fill()
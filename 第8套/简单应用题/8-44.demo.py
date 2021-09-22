import turtle
for i in range(4):
    turtle.seth(90*(i+1))
    turtle.circle(50,90)
    turtle.seth(90*(i-1))
    turtle.circle(50, 90)
turtle.hideturtle()
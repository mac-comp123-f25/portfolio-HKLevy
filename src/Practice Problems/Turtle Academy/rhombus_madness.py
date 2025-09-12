import random
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

colors=["#dee9fc","#6395f2","#1258dc","#0a337f","#091834"]

for x in range(50):
    start_x = random.randrange(-300, 300)
    start_y = random.randrange(-300, 300)
    start_angle = random.randrange(0, 360)
    color_index = random.randrange(0,5)
    color = colors[color_index]
    size = random.randrange(50, 101)
    angle = random.randrange(10, 80)

    t.penup()
    t.goto(start_x,start_y)
    t.pendown()
    t.rt(start_angle)

    t.fillcolor(color)
    t.begin_fill()
    for y in range(2):
        t.fd(size)
        t.rt(angle)
        t.fd(size)
        t.rt(180-angle)
    t.end_fill()

wn.exitonclick()
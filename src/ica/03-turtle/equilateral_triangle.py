import turtle
wn=turtle.Screen()
galen=turtle.Turtle()

galen.fillcolor("cyan")
galen.begin_fill()
for reps in range(3):
    galen.forward(300)
    galen.left(120)
galen.end_fill()

wn.exitonclick()

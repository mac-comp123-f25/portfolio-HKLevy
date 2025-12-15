import turtle
wn=turtle.Screen()
galen=turtle.Turtle()

sides=input("How many sides do you want for the polygon?")
sides=int(sides)

galen.fillcolor("cyan")
galen.pensize(5)
galen.begin_fill()
for reps in range(sides):
    galen.forward(100)
    galen.left(360/sides)
galen.end_fill()

wn.exitonclick()
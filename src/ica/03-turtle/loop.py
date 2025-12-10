import turtle

wind = turtle.Screen()
galen = turtle.Turtle()
wind.bgcolor("light green")
for reps in range(20):
    galen.forward(200)
    galen.right(180)
wind.exitonclick()
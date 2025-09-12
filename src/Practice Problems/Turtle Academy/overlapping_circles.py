'''radius of each of n circles needs to be bigger
than the circle of their centers so they overlap'''

import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(8)

n = int(input("How many circles do you want? "))
central_radius = 100
n_radius = 125

t.up()
t.goto(0,-central_radius)
t.down()
for x in range(n):
    t.dot(5)
    t.up()
    t.goto(t.xcor(),t.ycor()-n_radius)
    angle=t.heading()
    t.down()
    t.rt(angle)
    t.circle(n_radius)
    t.up()
    t.goto(t.xcor(),t.ycor()+n_radius)
    t.lt(angle)
    t.circle(central_radius,360/n)

wn.exitonclick()
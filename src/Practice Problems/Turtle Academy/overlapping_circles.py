"""
Draws some positive integer n overlapping circles

@author: Helen K. Levy (hlevy@macalester.edu)

@ref: pythonturtle.academy/n-overlapping-circle-with-python-and-turtle/
"""
import turtle

#establishes the parameters for the drawing
n = int(input("How many circles do you want? "))
n_radius = int(input("How big should each circle be? Recommended 80-150. "))
overlap = int(input("By how much should the circles overlap? Recommended 15-30. "))
central_radius = n_radius - overlap

#establishes the Screen and Turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.up()
t.speed(8)
t.goto(0,-central_radius)
t.down()

#draws the circles
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
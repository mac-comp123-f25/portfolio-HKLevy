'''
Draws a sun-like shape.

Worked on by Gabby, Apui, Helen
'''

import turtle
wn = turtle.Screen()
t = turtle.Turtle()

#creating the circle
t.penup()
t.goto(0,-100) #ensuring that the center of the circle is the middle of the screen
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()

t.right(90)
t.forward(50)
t.left(90)

#creating the triangles
'''We decided to simplify the problem a bit
by drawing equilateral triangles rather than
isosceles triangles'''

t.fillcolor('orange')
for triangle in range(12):
    t.left(60)
    t.begin_fill()
    for side in range(3):
        t.forward(30)
        t.left(120)
    t.end_fill()
    t.right(60)
    t.circle(150,30)

wn.exitonclick()
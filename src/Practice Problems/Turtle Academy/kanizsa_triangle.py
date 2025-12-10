"""
Draws a Kanizsa Triangle.

@author: Helen K. Levy (hlevy@macalester.edu)

@ref: pythonturtle.academy/kanizsa-triangle-with-python-turtle/
"""
import turtle


#establishes the Screen, Turtle, and its initial position
wn = turtle.Screen()
t=turtle.Turtle()
t.speed(8)
t.up()
t.goto(0,-150)
t.lt(30)

#collects coordinate points for each of the 6 important corners of the 2 triangles
pts=[]
for x in range(6):
    xcor=int(t.xcor())
    ycor=int(t.ycor())
    pts.append((xcor,ycor))
    t.fd(100)
    t.lt(60)

#makes the turtle's heading the way it should be for the loop
t.rt(60)

for x in range(len(pts)):
    t.goto(pts[x])
    if x%2==0:
        #draws the pac-man shape at the corners of one triangle
        t.down()
        t.lt(90)
        t.fillcolor('black')
        t.begin_fill()
        t.fd(30)
        t.lt(90)
        t.circle(30,-300)
        t.lt(90)
        t.fd(30)
        t.end_fill()
        t.lt(60)
        t.up()
    else:
        #draws the lines at the corners of the other triangle
        t.down()
        t.lt(120)
        t.fd(50)
        t.bk(50)
        t.lt(60)
        t.fd(50)
        t.bk(50)
        t.rt(90)
        t.up()

wn.exitonclick()
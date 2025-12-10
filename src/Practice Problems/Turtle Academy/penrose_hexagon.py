"""
Draws an impossible Penrose Hexagon.

@author: Helen K. Levy (hlevy@macalester.edu)

@ref: pythonturtle.academy/penrose-hexagon-with-python-turtle/
"""
import turtle
import math


def draw_segment(color):
    """
    Draws a segment of the penrose hexagon.
    :param color: the color of the segment
    :return: None
    """
    t.fillcolor(color)
    t.begin_fill()
    t.fd(side+d)
    t.rt(60)
    t.fd(side+d) #simplified from side - d/2 + 3d/2
    t.lt(150)
    t.fd(math.sqrt(3)*d)
    t.lt(30)
    t.fd(side)
    t.lt(60)
    t.fd(side+d)
    t.lt(60)
    t.fd(d)
    t.lt(120)
    t.end_fill()


#establishes parameters for the hexagon: size of a side, width of a segment, and colors, respectively
side=int(input("How big should the hexagon be? Recommended between 75 and 250. "))
d=int(input("How wide should each piece be? Recommended 1/5 of the previous answer. "))
colors=["#f6c3c0","#fffdc6","#cafac4","#cbfcfe","#c0c2fa","#f6c6fb"]

#establishes the turtle's initial position so the hexagon is centered on the screen
wn = turtle.Screen()
t = turtle.Turtle()
t.up()
t.width(3)
t.speed(5)
t.goto(int(-side/2),int(-side*math.sqrt(3)/2))
t.lt(120)
t.down()

#draws the penrose hexagon
for x in colors:
    draw_segment(x)
    t.fd(side)
    t.rt(60)

wn.exitonclick()
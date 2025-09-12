'''
Draws an impossible Penrose Hexagon.

@author: Helen K. Levy (hlevy@macalester.edu


Still very much in progress. need to step back
and do more math on paper first.
'''
import turtle
import math

wn = turtle.Screen()
t = turtle.Turtle()

colors=["#f6c3c0","#fffdc6","#cafac4","#cbfcfe","#c0c2fa","#f6c6fb"]

width=30 #this is the vertical (perpendicular) width between each set of parallel lines
length=150 #this is the length of 3 of the 4 long sides

for x in range(1): #will change to 6 once I get the shape down
    t.fd(length)
    t.lt(60)
    t.fd(width/math.sin(math.radians(60)))
    t.lt(120)
    t.fd(length)
    t.rt(60)
    t.fd(length)
    t.lt(150)
    t.fd(width/math.sin(math.radians(30)))
    t.lt(30)
    t.fd(length-width*math.sqrt(3)+width/math.sqrt(3))
    t.ht()


wn.exitonclick()
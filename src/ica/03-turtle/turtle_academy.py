'''
Draw the circle, filled in yellow.
Then draw the triangles, filled in orange.
'''

import turtle
wn = turtle.Screen()
t = turtle.Turtle()

#creating the circle
t.fillcolor('yellow')
t.begin_fill()
t.penup()
t.circle(100)
t.end_fill()

t.right(90)
t.forward(50)
t.left(90)
#creating the triangles
t.pendown() #will delete later, keeping in to see where the turtle is
for triangle in range(12):
    t.left(30) #this is wrong. fix later
    for side in range(3):
        t.forward(30)
        t.left(120)
    t.right(30)
    t.circle(150,30)

wn.exitonclick()
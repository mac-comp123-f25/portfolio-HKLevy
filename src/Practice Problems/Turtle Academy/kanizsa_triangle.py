import turtle
wn = turtle.Screen()
t=turtle.Turtle()
t.speed(2)

'''
Get points of the hexagon.
Every other one will be the pac-man shape
The others will be drawn.'''

'''This is still not what I want it to look like but it's much closer.'''

pts=[]
t.goto(0,-150)
t.lt(30)
for x in range(6):
    xcor=int(t.xcor())
    ycor=int(t.ycor())
    pts.append((xcor,ycor))
    t.fd(100)
    t.lt(60)

t.rt(30) #heading is now 0

# i want the turtle to end its drawing at
# every corner facing towards the next corner.
t.rt(30) #because it should start facing the way it came from
for x in range(len(pts)):
    t.goto(pts[x])
    if x%2==0:
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
    else:
        t.lt(120)
        t.fd(50)
        t.bk(50)
        t.lt(60)
        t.fd(50)
        t.bk(50)
        t.rt(90)

wn.exitonclick()
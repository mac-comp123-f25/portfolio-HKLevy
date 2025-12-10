import turtle
import math
wn = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.dot(5)

def goto_corner(n,side_length):
    tip_angle = 360/n
    twin_angle = (180-tip_angle)/2
    dist = side_length*math.sin(math.radians(twin_angle))/math.sin(math.radians(tip_angle))
    t.up()
    t.goto(0,0)
    t.seth(0)
    t.rt(90+tip_angle/2)
    t.fd(dist)
    t.lt(90+tip_angle/2)

def get_points(n,side_length):
    point_list=[]
    angle = 360/n
    goto_corner(n,side_length)
    for x in range(n):
        point_list.append(t.pos())
        t.fd(side_length)
        t.lt(angle)
    return point_list

my_points=get_points(24,75)
t.down()
for x in range(len(my_points)):
    for y in range(x,len(my_points)):
        t.goto(my_points[x])
        t.goto(my_points[y])
wn.exitonclick()
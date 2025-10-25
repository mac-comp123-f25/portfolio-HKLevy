import turtle
win = turtle.Screen()
turt = turtle.Turtle()
import math

from polar_coordinate_graphing import graph_sin_theta_transformation

if __name__ == '__main__':
    graph_sin_theta_transformation(turt,'black',0,180,0,0,50,3,0)
    graph_sin_theta_transformation(turt,'black',0,180,0,0,50,3,180)
    turt.up()
    lstpts=[]
    turt.goto(0,-50)
    turt.down()
    for x in range(12):
        lstpts.append(turt.pos())
        turt.circle(50,extent=30)
    for x in range(1,len(lstpts),2):
        turt.up()
        turt.goto(lstpts[x])
        turt.down()
        turt.goto(0,0)
    turt.up()
    turt.goto(0,-50)
    turt.rt(180)
    turt.down()
    print(lstpts)
    for x in range(12):
        # graph_sin_theta_transformation(turt,'black',0,60,lstpts[x][0],lstpts[x][1],50,3,240+30*x)
        turt.circle(25/2*math.sin(math.radians(75)))
        turt.rt(180)
        turt.circle(50,extent=30)
        turt.rt(180)
    turt.up()
    turt.goto(0,-100)
    turt.seth(0)
    turt.down()
    turt.circle(100)
    win.exitonclick()
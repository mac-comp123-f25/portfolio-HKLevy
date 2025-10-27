import turtle
win = turtle.Screen()
turt = turtle.Turtle()
turt.speed(0)
turt.ht()
import math

from polar_coordinate_graphing import graph_sin_theta_transformation

if __name__ == '__main__':
    """
    This is starting off by looking very nice. Just maybe not what I want, but I also don't want to delete it.
    I found an inspiration picture that I think I can mimic/adapt.
    This will challenge me more in terms of creativity and coding.
    
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
    new_radius = 50*math.sin(math.radians(15))/(1-math.sin(math.radians(15)))
    for x in range(12):
        turt.circle(new_radius)
        turt.rt(180)
        turt.circle(50,extent=30)
        turt.rt(180)
    turt.up()
    turt.goto(0,-1*(50+2*new_radius))
    turt.seth(0)
    turt.down()
    turt.circle(50+2*new_radius)
    """

    """Take user input in terms of number of layers and color and size."""
    layers = 3 #will become user inputted later.
    start_size = 75
    inc_size = 50
    for x in range(layers):
        petal_size = start_size + x * inc_size
        graph_sin_theta_transformation(turt,'black',0,180,0,0,petal_size,3,30)
        graph_sin_theta_transformation(turt,'black',0,180,0,0,petal_size,3,90)
        turt.up()
        for y in range(6):
            turt.fd(petal_size)
            turt.dot(15)
            turt.bk(petal_size)
            turt.rt(60)
        turt.down()
    turt.dot(35)

    win.exitonclick()